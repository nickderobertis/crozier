# llmlint: ignore-file[new_code_lands_in_a_project] Departure evidence stays beside its note in docs/departures/evidence, as invalid-example-values/validate.py does; it is a measurement run by hand, its results committed beside it.
"""Audit the Python examples of generated SDK trees against the trees' own code.

For each tree: every ```python block of README.md and reference.md, and every
`Examples` section of a client.py docstring, is checked for
  syntax      the block does not compile (a repeated keyword is a SyntaxError);
              `'yield' outside function` is matched Fern behaviour and skipped
  import      `from M import N` names a module or name the tree does not define
  call        a call on `client...` or a client constructor passes a keyword the
              method does not take, too many positional arguments, or omits a
              required argument
  placeholder a "YOUR_*" string passed where the parameter is not a string
Output: TSV rows tree, file, line, check, detail.

Usage, from the repository root after `cargo build -p crozier --bin crozier`:
  documentation-audit.py fern
      every tree tests/fixtures/compared-goldens.json names, an overlay rebuilt
      over its base as the gate rebuilds it
  documentation-audit.py crozier TREE...
      crozier's own tree for each named golden, generated with the settings its
      comparison uses, audited the same way
"""
import ast
import json
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
import tomllib
from functools import cache
from pathlib import Path

QUOTE3, APOS3 = chr(34) * 3, chr(39) * 3
FENCE = re.compile(r"```python\n(.*?)```", re.S)


def package_root(tree: Path):
    src = tree / "src"
    if src.is_dir():
        pkgs = [p for p in src.iterdir() if p.is_dir() and (p / "__init__.py").is_file()]
        return (src, pkgs[0].name) if pkgs else (None, None)
    if (tree / "__init__.py").is_file() and (tree / "client.py").is_file():
        return (tree.parent, None)  # flat: modules at the root
    return (None, None)


@cache
def parse(path: Path):
    try:
        return ast.parse(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def module_file(tree, pkg, dotted):
    """The file a dotted module `pkg.a.b` names inside the tree, or None."""
    parts = dotted.split(".")
    if pkg is not None:
        if parts[0] != pkg:
            return None
        base = tree / "src" / pkg
    else:
        base = tree
    rel = parts[1:]
    for cand in (base.joinpath(*rel, "__init__.py"), base.joinpath(*rel[:-1], rel[-1] + ".py") if rel else None):
        if cand is not None and cand.is_file():
            return cand
    return None


def defined_names(path: Path):
    mod = parse(path)
    names = set()
    if mod is None:
        return names
    for node in mod.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            names.add(node.name)
        elif isinstance(node, (ast.Assign, ast.AnnAssign)):
            for t in node.targets if isinstance(node, ast.Assign) else [node.target]:
                for n in ast.walk(t):
                    if isinstance(n, ast.Name):
                        names.add(n.id)
                if isinstance(node, ast.Assign) and isinstance(node.value, ast.Dict) and any(
                    isinstance(t, ast.Name) and t.id == "_dynamic_imports" for t in node.targets
                ):
                    names |= {k.value for k in node.value.keys if isinstance(k, ast.Constant)}
        elif isinstance(node, (ast.ImportFrom, ast.Import)):
            names |= {a.asname or a.name.split(".")[0] for a in node.names}
        elif isinstance(node, ast.If):
            for sub in ast.walk(node):
                if isinstance(sub, (ast.ImportFrom, ast.Import)):
                    names |= {a.asname or a.name.split(".")[0] for a in sub.names}
    return names


def classes(path):
    mod = parse(path)
    return {n.name: n for n in mod.body if isinstance(n, ast.ClassDef)} if mod else {}


def signature(fn):
    a = fn.args
    pos = [x.arg for x in a.posonlyargs + a.args if x.arg != "self"]
    ndef = len(a.defaults)
    allpos = a.posonlyargs + a.args
    pos_required = [x.arg for x in allpos[: len(allpos) - ndef] if x.arg != "self"]
    kw = [x.arg for x in a.kwonlyargs]
    kw_required = [x.arg for x, d in zip(a.kwonlyargs, a.kw_defaults) if d is None]
    ann = {x.arg: (ast.unparse(x.annotation) if x.annotation else "") for x in allpos + a.kwonlyargs}
    return dict(pos=pos, pos_required=pos_required, kw=kw, kw_required=kw_required, varkw=a.kwarg is not None, ann=ann)


def method(cls, name):
    for n in cls.body:
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == name:
            return n
    return None


def client_files(tree, pkg):
    base = tree / "src" / pkg if pkg else tree
    return base


def resolve_call(tree, pkg, chain, is_async, client_names):
    """chain: ['client', 'a', 'b', 'method'] -> FunctionDef or None (unknown)."""
    base = client_files(tree, pkg)
    *path, name = chain[1:]
    f = base.joinpath(*path, "client.py") if path else base / "client.py"
    cls_map = classes(f) if f.is_file() else {}
    if not cls_map:
        return "nofile", f
    # The module's first client class is the sync one, its next the async one
    # (a group may itself be named `Async…`, as `asyncapi` is).
    ordered = [c for c in cls_map.values() if "Raw" not in c.name]
    picks = ordered[1:2] if is_async else ordered[:1]
    for c in picks:
        m = method(c, name)
        if m is not None:
            return m, f
    # a property (sub-client) or unknown name
    return None, f


def admits_str(annotation: str) -> bool:
    """Whether a plain `str` value satisfies `annotation` (an unparsed type)."""
    try:
        node = ast.parse(annotation, mode="eval").body
    except SyntaxError:
        return True
    def ok(n):
        if isinstance(n, ast.Name):
            return n.id in ("str", "Any")
        if isinstance(n, ast.Attribute):
            return n.attr in ("Any",)
        if isinstance(n, ast.Constant) and isinstance(n.value, str):
            return ok(ast.parse(n.value, mode="eval").body)
        if isinstance(n, ast.Subscript):
            head = ast.unparse(n.value)
            inner = n.slice.elts if isinstance(n.slice, ast.Tuple) else [n.slice]
            if head in ("typing.Optional", "Optional"):
                return ok(inner[0])
            if head in ("typing.Union", "Union"):
                return any(ok(x) for x in inner)
            return False
        if isinstance(n, ast.BinOp):
            return ok(n.left) or ok(n.right)
        return False
    return ok(node)


def check_call(call, sig, where, out):
    args = call.args
    if len(args) == 1 and isinstance(args[0], ast.Constant) and args[0].value is Ellipsis:
        return
    kws = [k.arg for k in call.keywords if k.arg is not None]
    if any(k.arg is None for k in call.keywords):
        return
    for k in kws:
        if k not in sig["pos"] and k not in sig["kw"] and not sig["varkw"]:
            out.append(("call", f"{where}: keyword `{k}` is not a parameter"))
    if len(args) > len(sig["pos"]):
        out.append(("call", f"{where}: {len(args)} positional argument(s) for {len(sig['pos'])}"))
    given = set(kws) | set(sig["pos"][: len(args)])
    missing = [p for p in sig["pos_required"] + sig["kw_required"] if p not in given]
    if missing:
        out.append(("call", f"{where}: missing required {missing}"))
    for k in call.keywords:
        v = k.value
        if isinstance(v, ast.Constant) and isinstance(v.value, str) and v.value.startswith("YOUR_"):
            ann = sig["ann"].get(k.arg, "")
            if ann and not admits_str(ann):
                out.append(("placeholder", f"{where}: `{k.arg}={v.value!r}` for `{ann}`"))


def audit_block(tree, pkg, code, file, line, out):
    try:
        mod = ast.parse(code)
        compile(code, file, "exec")
    except SyntaxError as e:
        if "'yield' outside function" in str(e) or "'await' outside" in str(e):
            try:
                mod = ast.parse(code)
            except SyntaxError:
                out.append((file, line + (e.lineno or 1) - 1, "syntax", str(e.msg)))
                return
        else:
            out.append((file, line + (e.lineno or 1) - 1, "syntax", str(e.msg)))
            return
    found = []
    client_names = {}
    for node in ast.walk(mod):
        if isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
            top = node.module.split(".")[0]
            if top in ("typing", "datetime", "asyncio", "uuid", "httpx", "decimal", "enum", "json", "os", "io"):
                continue
            mf = module_file(tree, pkg, node.module)
            if mf is None:
                found.append((node.lineno, "import", f"module `{node.module}` is not in the tree"))
                continue
            names = defined_names(mf)
            subdir = mf.parent if mf.name == "__init__.py" else None
            for a in node.names:
                if a.name not in names and not (subdir and ((subdir / a.name).is_dir() or (subdir / (a.name + ".py")).is_file())):
                    found.append((node.lineno, "import", f"`{a.name}` is not defined by `{node.module}`"))
    # client variable assignments: client = X(...)
    root_client = client_files(tree, pkg) / "client.py"
    root_classes = classes(root_client) if root_client.is_file() else {}
    for node in ast.walk(mod):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in root_classes:
            init = method(root_classes[node.func.id], "__init__")
            if init is not None:
                o = []
                check_call(node, signature(init), f"{node.func.id}(...)", o)
                found += [(node.lineno, c, d) for c, d in o]
    awaited = {id(n.value) for n in ast.walk(mod) if isinstance(n, ast.Await)}
    for node in ast.walk(mod):
        if not (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)):
            continue
        chain, cur = [], node.func
        while isinstance(cur, ast.Attribute):
            chain.append(cur.attr)
            cur = cur.value
        if not (isinstance(cur, ast.Name) and cur.id == "client"):
            continue
        chain = ["client"] + chain[::-1]
        if chain[-1] in ("with_raw_response",) or "with_raw_response" in chain:
            continue
        fn, f = resolve_call(tree, pkg, chain, id(node) in awaited or "async" in code[:0], client_names)
        if fn == "nofile":
            found.append((node.lineno, "call", f"`{'.'.join(chain)}`: no client module {f.relative_to(tree)}"))
            continue
        if fn is None:
            found.append((node.lineno, "call", f"`{'.'.join(chain)}`: no such method"))
            continue
        o = []
        check_call(node, signature(fn), ".".join(chain), o)
        found += [(node.lineno, c, d) for c, d in o]
    for ln, c, d in found:
        out.append((file, line + ln - 1, c, d))


def audit_tree(tree: Path):
    src_root, pkg = package_root(tree)
    out = []
    if src_root is None and not (tree / "README.md").is_file():
        return out, 0
    blocks = 0
    for doc in ("README.md", "reference.md"):
        p = tree / doc
        if not p.is_file():
            continue
        text = p.read_text(encoding="utf-8")
        for m in FENCE.finditer(text):
            line = text.count("\n", 0, m.start(1)) + 1
            blocks += 1
            audit_block(tree, pkg, m.group(1), doc, line, out)
    base = tree / "src" / pkg if pkg else tree
    for cf in sorted(base.rglob("client.py")):
        src = cf.read_text(encoding="utf-8")
        mod = parse(cf)
        if mod is None:
            continue
        for node in ast.walk(mod):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                # The docstring as written in the file: Fern's are not raw, so
                # evaluating one turns a backslash-n inside an example's string
                # literal into a line break the source does not have.
                first = node.body[0] if node.body else None
                doc = None
                if isinstance(first, ast.Expr) and isinstance(first.value, ast.Constant) and isinstance(first.value.value, str):
                    segment = ast.get_source_segment(src, first.value) or ""
                    if segment[:3] in (QUOTE3, APOS3):
                        doc = segment[3:-3]
                header = re.search(r"\n[ \t]*Examples\n[ \t]*-{8}\n", doc or "")
                if header is None:
                    continue
                code = textwrap.dedent(doc[header.end():])
                start = node.body[0].lineno + doc[: header.end()].count("\n")
                blocks += 1
                audit_block(tree, pkg, code, str(cf.relative_to(tree)), start, out)
    return out, blocks



ROOT = Path.cwd()
CROZIER = ROOT / "target/debug/crozier"
E2E = open("crates/crozier-e2e/tests/e2e.rs").read()
corpora = {}
for m in re.finditer(r"Corpus \{\s*api: \"([^\"]+)\",(.*?)\n\s*\}", E2E, re.S):
    if m.group(1) in corpora:
        continue
    body = m.group(2)
    aud = re.search(r"audiences: &\[(.*?)\]", body, re.S)
    corpora[m.group(1)] = dict(
        package=(re.search(r'package_name: "([^"]*)"', body) or [0, "fern"])[1],
        project=(re.search(r'project_name: "([^"]*)"', body) or [0, "default_package_name"])[1],
        audiences=re.findall(r'"([^"]+)"', aud.group(1)) if aud else [],
        strict="audience_strict: true" in body,
        client=(re.search(r'client_class_name: Some\("([^"]+)"\)', body) or [0, None])[1],
        extra=(re.search(r'extra_fields: Some\("([^"]+)"\)', body) or [0, None])[1],
    )

def first(*paths):
    return next((p for p in paths if p.is_file()), None)

def corpus_spec(api: str):
    """The committed source of a registered corpus, as the e2e harness's
    `corpus_spec` finds it: a vendored or committed `openapi.*`, else the root
    of a multi-document tree `corpus_remote_ref_pins.py tree-root` names."""
    committed = ROOT / "tests/fixtures/corpus-sources" / api
    found = first(ROOT / "tests/fixtures" / api / "openapi.yml", *(committed / f"openapi.{e}" for e in ("json", "yaml", "yml")))
    if found is not None:
        return found
    result = subprocess.run([sys.executable, str(ROOT / "tools/corpus/corpus_remote_ref_pins.py"), "tree-root", api], capture_output=True, text=True)
    return first(committed / result.stdout.strip()) if result.returncode == 0 and result.stdout.strip() else None

def spec_in(d: Path):
    return first(*(d / f"openapi.{e}" for e in ("yml", "yaml", "json")), *(d.parent / f"{d.name}.{e}" for e in ("yml", "yaml", "json")))

def settings(golden: str):
    g = Path(golden)
    args = ["--package-name", "fern", "--project-name", "default_package_name"]
    if golden.startswith("tests/fixtures/"):
        api, kind = g.parts[2], g.parts[3]
        if kind == "expected-flat":
            state = json.loads((ROOT / golden / ".crozier-fern-golden.json").read_text())
            spec = ROOT / state["vendored_spec_path"] if "vendored_spec_path" in state else None
            c = corpora.get(api, dict(package="fern", project="default_package_name", audiences=[], strict=False, client=None, extra=None))
            if spec is None:
                spec = corpus_spec(api)
            organization = state.get("organization")
            package = organization or c["package"]
            project = {"acme": "acme-dist"}.get(organization or "", c["project"] if not organization else organization)
            args = ["--layout", "flat", "--package-name", package, "--project-name", project]
            for a in c["audiences"]:
                args += ["--audience", a]
            if c["strict"]:
                args.append("--audience-strict")
            if state.get("client_class_name") or c["client"]:
                args += ["--client-class-name", state.get("client_class_name") or c["client"]]
            if state.get("extra_fields") or c["extra"]:
                args += ["--extra-fields", state.get("extra_fields") or c["extra"]]
            return spec, args, None
        c = corpora.get(api)
        if c is None:
            return None, None, "no corpus registration"
        spec = corpus_spec(api)
        args = ["--package-name", c["package"], "--project-name", c["project"]]
        for a in c["audiences"]:
            args += ["--audience", a]
        if c["strict"]:
            args.append("--audience-strict")
        if c["client"]:
            args += ["--client-class-name", c["client"]]
        if c["extra"]:
            args += ["--extra-fields", c["extra"]]
        if kind == "expected-literals":
            args += ["--enum-type", "literals"]
        elif kind == "expected-default-max-retries":
            record = json.loads((ROOT / golden / ".crozier-overlay.json").read_text())
            args += ["--default-max-retries", str(record["default_max_retries"])]
        elif kind != "expected":
            return None, None, f"overlay kind {kind}"
        return spec, args, None
    if golden.startswith("docs/openapi-surface/probe-expected/"):
        key = g.parts[3]
        return first(*(ROOT / "docs/openapi-surface/probes" / f"{key}.{e}" for e in ("yml", "yaml", "json"))), args, None
    home = g.parent.parent if g.parent.name == "literals" else g.parent
    spec = spec_in(ROOT / home)
    for candidate in (
        home.parent,  # <cause>/expected-literals/fern-expected
        home.parent.parent,
        home.parent / home.name.removesuffix("-literals"),
        Path("docs/openapi-surface/handwritten") / home.name.removesuffix("-literals"),
        Path("docs/fern-measurements/superseded-fixtures") / home.name.removesuffix("-literals"),
        Path("docs/openapi-surface/probes") / home.name.removesuffix("-literals"),
    ):
        if spec is None:
            spec = spec_in(ROOT / candidate)
    meta = ROOT / golden / ".fern/metadata.json"
    if not meta.is_file():
        base = ROOT / g.parent / "fern-expected" / ".fern/metadata.json"
        meta = base if base.is_file() else meta
    config = (json.loads(meta.read_text()).get("generatorConfig") or {}) if meta.is_file() else {}
    pyd = config.get("pydantic_config") or {}
    if pyd.get("enum_type") != "python_enums" or g.name == "expected-literals" or g.parent.name == "literals":
        args += ["--enum-type", "literals"]
    if config.get("client_class_name"):
        args += ["--client-class-name", config["client_class_name"]]
    if pyd.get("extra_fields"):
        args += ["--extra-fields", pyd["extra_fields"]]
    evidence = ROOT / home / "evidence.toml"
    if evidence.is_file():
        for a in tomllib.loads(evidence.read_text()).get("audiences", []):
            args += ["--audience", a]
    return spec, args, None



def rebuilt(golden: str, scratch: Path) -> Path:
    """The tree a comparison reads for `golden`: an overlay over its base."""
    tree = ROOT / golden
    overlay = tree / ".crozier-overlay.json"
    if not overlay.is_file():
        return tree
    record = json.loads(overlay.read_text())
    base = tree.parent / record["base"]
    if not base.is_dir():
        base = tree.parent / "fern-expected"
    full = scratch / golden.replace("/", "%")
    shutil.copytree(base, full)
    for removed in record.get("removed", []):
        (full / removed).unlink(missing_ok=True)
    for path in tree.rglob("*"):
        if path.is_file() and path.name != ".crozier-overlay.json":
            target = full / path.relative_to(tree)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, target)
    return full


def emit(golden, rows):
    for file, line, check, detail in rows:
        print(f"{golden}\t{file}\t{line}\t{check}\t{detail}", flush=True)


def main(argv):
    if argv[:1] == ["fern"]:
        goldens = sorted(json.loads((ROOT / "tests/fixtures/compared-goldens.json").read_text())["goldens"])
        blocks = 0
        with tempfile.TemporaryDirectory() as scratch:
            for golden in goldens:
                parse.cache_clear()
                rows, count = audit_tree(rebuilt(golden, Path(scratch)))
                blocks += count
                emit(golden, rows)
        print(f"# trees\t{len(goldens)}\tblocks\t{blocks}", file=sys.stderr)
        return 0
    if argv[:1] == ["crozier"] and len(argv) > 1:
        with tempfile.TemporaryDirectory() as scratch:
            for golden in argv[1:]:
                spec, args, why = settings(golden)
                if spec is None:
                    print(f"{golden}\t-\t-\tunverified\t{why or 'no spec found'}", flush=True)
                    continue
                out = Path(scratch) / golden.replace("/", "%")
                run = subprocess.run(
                    [str(CROZIER), "--no-config", "generate", "python", "--spec", str(spec), "--output", str(out), *args],
                    capture_output=True,
                    text=True,
                )
                if run.returncode != 0:
                    print(f"{golden}\t-\t-\tunverified\tcrozier generate exited {run.returncode}", flush=True)
                    continue
                parse.cache_clear()
                rows, count = audit_tree(out)
                print(f"{golden}\t-\t-\tgenerated\t{count} blocks", flush=True)
                emit(golden, rows)
        return 0
    print(__doc__, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
