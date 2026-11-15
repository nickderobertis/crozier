# llmlint: ignore-file[new_code_lands_in_a_project] Departure evidence stays beside its note in docs/departures/evidence, as invalid-example-values/validate.py does; crozier-e2e drives it through its e2eReads input.
"""Audit the Python examples of generated SDK trees against the trees' own code.

For each TREE: every ```python block of README.md and reference.md, and every
numpydoc `Examples` section of a client.py docstring, read as the file writes
it, is checked for
  syntax      the block does not compile (a repeated keyword is a SyntaxError);
              `yield` or `await` outside a function is how Fern lays out a
              streaming example and is not a finding
  import      `from M import N` names a module, or a name, the tree does not define
  call        a call on `client.…`, or a client constructor, passes a keyword the
              method does not take, too many positional arguments, or omits a
              required argument
  placeholder a "YOUR_*" string is passed where the annotation admits no `str`

Each finding is a stdout row: tree, file, line, check, detail, tab-separated.
Exit 0 when there is none (a directory documenting no example has none), 1
when there are findings, 2 when a TREE is not a directory or holds a document
or client module it cannot read as UTF-8 (stderr says why). A one-line summary
of trees, blocks and findings goes to stderr.
"""

from __future__ import annotations

import ast
import re
import sys
import textwrap
from collections.abc import Mapping
from dataclasses import dataclass
from enum import StrEnum
from functools import cache
from pathlib import Path

QUOTES = (chr(34) * 3, chr(39) * 3)
FENCE = re.compile(r"```python\n(.*?)```", re.S)
EXAMPLES = re.compile(r"\n[ \t]*Examples\n[ \t]*-{8}\n")
# Modules an example imports from outside the SDK.
EXTERNAL = frozenset(("typing", "datetime", "asyncio", "uuid", "httpx", "decimal", "enum", "json", "os", "io"))
TOP_LEVEL_ONLY = ("'yield' outside function", "'await' outside")


class InputError(ValueError):
    """A TREE the audit cannot read."""


class Check(StrEnum):
    SYNTAX = "syntax"
    IMPORT = "import"
    CALL = "call"
    PLACEHOLDER = "placeholder"


@dataclass(frozen=True)
class Finding:
    file: str
    line: int
    check: Check
    detail: str


@dataclass(frozen=True)
class Problem:
    """What is wrong at one place of an example, before it is located."""

    check: Check
    detail: str


@dataclass(frozen=True)
class Block:
    """One example: its file, its code and the file line its code starts on."""

    file: str
    code: str
    first_line: int


@dataclass(frozen=True)
class Report:
    """One tree's audit: its findings, and how many example blocks it read."""

    findings: list[Finding]
    blocks: int


@dataclass(frozen=True)
class Package:
    """Where an SDK tree keeps its modules: `src/<name>/`, else the tree itself,
    as the flat layout does, whose modules are imported by the tree's own name.
    A tree holding neither (a measurement that keeps only some files) resolves
    no module."""

    tree: Path
    modules: Path
    name: str

    @classmethod
    def of(cls, tree: Path) -> Package:
        src = tree / "src"
        packages = sorted(p for p in src.iterdir() if (p / "__init__.py").is_file()) if src.is_dir() else []
        return cls(tree, packages[0], packages[0].name) if packages else cls(tree, tree, "")

    def module_file(self, dotted: str) -> Path | None:
        """The file the dotted module names inside the tree, or None."""
        parts = dotted.split(".")
        if self.name and parts[0] != self.name:
            return None
        rest = parts[1:]
        candidates = [self.modules.joinpath(*rest, "__init__.py")]
        if rest:
            candidates.append(self.modules.joinpath(*rest[:-1], rest[-1] + ".py"))
        return next((path for path in candidates if path.is_file()), None)


@dataclass(frozen=True)
class Signature:
    positional: tuple[str, ...]
    positional_required: tuple[str, ...]
    keyword: tuple[str, ...]
    keyword_required: tuple[str, ...]
    variadic_keyword: bool
    annotations: Mapping[str, str]

    @classmethod
    def of(cls, function: ast.FunctionDef | ast.AsyncFunctionDef) -> Signature:
        arguments = function.args
        positional = arguments.posonlyargs + arguments.args
        required = positional[: len(positional) - len(arguments.defaults)]
        return cls(
            positional=tuple(a.arg for a in positional if a.arg != "self"),
            positional_required=tuple(a.arg for a in required if a.arg != "self"),
            keyword=tuple(a.arg for a in arguments.kwonlyargs),
            keyword_required=tuple(
                a.arg for a, default in zip(arguments.kwonlyargs, arguments.kw_defaults) if default is None
            ),
            variadic_keyword=arguments.kwarg is not None,
            annotations={
                a.arg: ast.unparse(a.annotation) if a.annotation else "" for a in positional + arguments.kwonlyargs
            },
        )


@dataclass(frozen=True)
class MissingModule:
    path: Path


@dataclass(frozen=True)
class MissingMethod:
    pass


@dataclass(frozen=True)
class Resolved:
    signature: Signature


@cache
def parse(path: Path) -> ast.Module | None:
    try:
        return ast.parse(path.read_text(encoding="utf-8"))
    except (SyntaxError, UnicodeDecodeError, OSError):
        return None


def imported_names(node: ast.Import | ast.ImportFrom) -> set[str]:
    return {alias.asname or alias.name.split(".")[0] for alias in node.names}


def defined_names(path: Path) -> set[str]:
    """The names a module defines at its top level, its lazy `_dynamic_imports`
    and its `if TYPE_CHECKING:` imports included."""
    module = parse(path)
    names: set[str] = set()
    for node in module.body if module else []:
        match node:
            case ast.FunctionDef(name=name) | ast.AsyncFunctionDef(name=name) | ast.ClassDef(name=name):
                names.add(name)
            case ast.Assign(targets=targets, value=value):
                names |= {n.id for t in targets for n in ast.walk(t) if isinstance(n, ast.Name)}
                if isinstance(value, ast.Dict) and any(
                    isinstance(t, ast.Name) and t.id == "_dynamic_imports" for t in targets
                ):
                    names |= {k.value for k in value.keys if isinstance(k, ast.Constant)}
            case ast.AnnAssign(target=target):
                names |= {n.id for n in ast.walk(target) if isinstance(n, ast.Name)}
            case ast.Import() | ast.ImportFrom():
                names |= imported_names(node)
            case ast.If():
                for inner in ast.walk(node):
                    if isinstance(inner, (ast.Import, ast.ImportFrom)):
                        names |= imported_names(inner)
    return names


def classes(path: Path) -> dict[str, ast.ClassDef]:
    module = parse(path)
    return {n.name: n for n in module.body if isinstance(n, ast.ClassDef)} if module else {}


def method(cls: ast.ClassDef, name: str) -> ast.FunctionDef | ast.AsyncFunctionDef | None:
    return next(
        (n for n in cls.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == name),
        None,
    )


def resolve_call(package: Package, chain: list[str], awaited: bool) -> MissingModule | MissingMethod | Resolved:
    """The method `client.a.b.method` calls: `method` of the client class in
    `a/b/client.py`. A module's first client class is the sync one and its next
    the async one (a group may itself be named `Async…`, as `asyncapi` is)."""
    *groups, name = chain[1:]
    path = package.modules.joinpath(*groups, "client.py")
    found = [c for c in classes(path).values() if "Raw" not in c.name] if path.is_file() else []
    if not found:
        return MissingModule(path)
    for cls in found[1:2] if awaited else found[:1]:
        if (function := method(cls, name)) is not None:
            return Resolved(Signature.of(function))
    return MissingMethod()


def admits_str(annotation: str) -> bool:
    """Whether a plain `str` value satisfies `annotation` (an unparsed type)."""
    try:
        node = ast.parse(annotation, mode="eval").body
    except SyntaxError:
        return True

    def admits(node: ast.expr) -> bool:
        match node:
            case ast.Name(id=name):
                return name in ("str", "Any")
            case ast.Attribute(attr=attribute):
                return attribute == "Any"
            case ast.Constant(value=str(forward)):
                # A forward reference that does not parse is unknown, as an
                # annotation that does not parse is: no placeholder is flagged for it.
                try:
                    return admits(ast.parse(forward, mode="eval").body)
                except SyntaxError:
                    return True
            case ast.Subscript(value=head, slice=ast.Tuple(elts=members)) if ast.unparse(head) in (
                "typing.Union",
                "Union",
            ):
                return any(admits(member) for member in members)
            case ast.Subscript(value=head, slice=inner) if ast.unparse(head) in ("typing.Optional", "Optional"):
                return admits(inner)
            case ast.BinOp(left=left, right=right):
                return admits(left) or admits(right)
            case _:
                return False

    return admits(node)


def check_call(call: ast.Call, signature: Signature, where: str) -> list[Problem]:
    """What is wrong with `call` against `signature`; an abbreviated `f(...)` or
    a `**kwargs` spread is not checked."""
    match call.args:
        case [ast.Constant(value=value)] if value is Ellipsis:
            return []
    if any(k.arg is None for k in call.keywords):
        return []
    found: list[Problem] = []
    keywords = [k.arg for k in call.keywords if k.arg is not None]
    for keyword in keywords:
        if keyword not in signature.positional + signature.keyword and not signature.variadic_keyword:
            found.append(Problem(Check.CALL, f"{where}: keyword `{keyword}` is not a parameter"))
    if len(call.args) > len(signature.positional):
        found.append(
            Problem(Check.CALL, f"{where}: {len(call.args)} positional argument(s) for {len(signature.positional)}")
        )
    given = set(keywords) | set(signature.positional[: len(call.args)])
    missing = [p for p in signature.positional_required + signature.keyword_required if p not in given]
    if missing:
        found.append(Problem(Check.CALL, f"{where}: missing required {missing}"))
    for keyword in call.keywords:
        match keyword.value:
            case ast.Constant(value=str(text)) if text.startswith("YOUR_"):
                annotation = signature.annotations.get(keyword.arg or "", "")
                if annotation and not admits_str(annotation):
                    found.append(Problem(Check.PLACEHOLDER, f"{where}: `{keyword.arg}={text!r}` for `{annotation}`"))
    return found


def call_chain(call: ast.Call) -> list[str] | None:
    """`['client', 'a', 'method']` for `client.a.method(...)`, else None."""
    chain: list[str] = []
    node = call.func
    while isinstance(node, ast.Attribute):
        chain.append(node.attr)
        node = node.value
    if chain and isinstance(node, ast.Name) and node.id == "client":
        return ["client", *reversed(chain)]
    return None


def audit_block(package: Package, block: Block) -> list[Finding]:
    """The findings of one example block, each on its file line."""
    found: list[Finding] = []

    def at(line: int, *problems: Problem) -> None:
        found.extend(Finding(block.file, block.first_line + line - 1, p.check, p.detail) for p in problems)

    try:
        module = ast.parse(block.code)
        compile(block.code, block.file, "exec")
    except SyntaxError as error:
        # `ast.parse` takes a top-level `yield`/`await`; only `compile` refuses it.
        if not any(reason in str(error) for reason in TOP_LEVEL_ONLY):
            at(error.lineno or 1, Problem(Check.SYNTAX, str(error.msg)))
            return found
        module = ast.parse(block.code)
    for node in ast.walk(module):
        if not isinstance(node, ast.ImportFrom) or not node.module or node.level != 0:
            continue
        if node.module.split(".")[0] in EXTERNAL:
            continue
        target = package.module_file(node.module)
        if target is None:
            at(node.lineno, Problem(Check.IMPORT, f"module `{node.module}` is not in the tree"))
            continue
        names = defined_names(target)
        directory = target.parent if target.name == "__init__.py" else None
        for alias in node.names:
            submodule = directory is not None and (
                (directory / alias.name).is_dir() or (directory / f"{alias.name}.py").is_file()
            )
            if alias.name not in names and not submodule:
                at(node.lineno, Problem(Check.IMPORT, f"`{alias.name}` is not defined by `{node.module}`"))
    constructors = classes(package.modules / "client.py")
    for node in ast.walk(module):
        match node:
            case ast.Call(func=ast.Name(id=name)) if name in constructors:
                if (init := method(constructors[name], "__init__")) is not None:
                    at(node.lineno, *check_call(node, Signature.of(init), f"{name}(...)"))
    awaited = {id(n.value) for n in ast.walk(module) if isinstance(n, ast.Await)}
    for node in ast.walk(module):
        if not isinstance(node, ast.Call) or (chain := call_chain(node)) is None or "with_raw_response" in chain:
            continue
        named = ".".join(chain)
        match resolve_call(package, chain, id(node) in awaited):
            case MissingModule(path=path):
                at(node.lineno, Problem(Check.CALL, f"`{named}`: no client module {path.relative_to(package.tree)}"))
            case MissingMethod():
                at(node.lineno, Problem(Check.CALL, f"`{named}`: no such method"))
            case Resolved(signature=signature):
                at(node.lineno, *check_call(node, signature, named))
    return found


def docstring_examples(source: str, module: ast.Module, file: str) -> list[Block]:
    """Each docstring `Examples` section of the client module `file`, as its
    source writes it. Fern's docstrings are not raw, so evaluating one would
    turn a backslash-n inside an example's string literal into a line break."""
    sections: list[Block] = []
    for node in ast.walk(module):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            continue
        match node.body:
            case [ast.Expr(value=ast.Constant(value=str()) as literal), *_]:
                segment = ast.get_source_segment(source, literal) or ""
            case _:
                continue
        if segment[:3] not in QUOTES:
            continue
        text = segment[3:-3]
        if (header := EXAMPLES.search(text)) is None:
            continue
        start = literal.lineno + text[: header.end()].count("\n")
        sections.append(Block(file, textwrap.dedent(text[header.end() :]), start))
    return sections


def read_text(path: Path) -> str:
    """A documentation or client file as UTF-8, or an input error naming it."""
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as error:
        raise InputError(f"{path} cannot be read as UTF-8 text: {error}") from error


def audit_tree(tree: Path) -> Report:
    """The findings of every example `tree` documents, and how many blocks."""
    if not tree.is_dir():
        raise InputError(f"{tree} is not a directory")
    package = Package.of(tree)
    blocks: list[Block] = []
    findings: list[Finding] = []
    for document in ("README.md", "reference.md"):
        if (tree / document).is_file():
            text = read_text(tree / document)
            blocks += [Block(document, m.group(1), text.count("\n", 0, m.start(1)) + 1) for m in FENCE.finditer(text)]
    for client in sorted(package.modules.rglob("client.py")):
        relative = str(client.relative_to(tree))
        source = read_text(client)
        try:
            module = ast.parse(source)
        except SyntaxError as error:
            # Its docstrings cannot be read, so the module itself is the finding.
            findings.append(Finding(relative, error.lineno or 1, Check.SYNTAX, f"the module does not parse: {error.msg}"))
            continue
        blocks += docstring_examples(source, module, relative)
    findings += [finding for block in blocks for finding in audit_block(package, block)]
    return Report(findings, len(blocks))


def main(argv: list[str]) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__, file=sys.stderr)
        return 0 if argv else 2
    total_findings = total_blocks = 0
    for argument in argv:
        tree = Path(argument)
        try:
            report = audit_tree(tree)
        except InputError as error:
            print(f"documentation-audit.py: {error}", file=sys.stderr)
            return 2
        for finding in report.findings:
            print("\t".join((argument, finding.file, str(finding.line), finding.check, finding.detail)))
        total_findings += len(report.findings)
        total_blocks += report.blocks
    print(
        f"documentation-audit.py: {len(argv)} tree(s), {total_blocks} block(s), {total_findings} finding(s)",
        file=sys.stderr,
    )
    return 1 if total_findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
