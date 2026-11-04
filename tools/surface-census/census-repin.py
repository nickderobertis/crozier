#!/usr/bin/env python3
"""`just census-repin`: bring every census table that pins crozier's code back to the tree at HEAD.

The one verb a census-tier failure about a stale site anchor, ledger row, reach
cell, arm section, coverage count or `handwritten-reach.tsv` row names. In order:

1. **Find the base**: the nearest first-parent ancestor of HEAD with a saved
   golden-reach measurement (`reach_base.py`), or none.
2. **Re-anchor** every site of `docs/openapi-surface/golden-reach-sites.tsv` that
   no longer resolves to exactly one line. The anchored line is located in the
   base tree and followed into HEAD by its tokens; where they are unchanged
   (rustfmt split or joined the line, or a duplicate line made the pattern
   ambiguous) the pattern is rewritten to a unique anchor, everywhere the old
   spec is quoted. Where the anchored code itself changed, nothing is re-anchored
   and the verb exits non-zero naming the site, its old and new code, and the
   decision left to you.
3. **Re-measure incrementally**: the golden tests and hand-written fixtures whose
   base entry executed changed code (or all of them, for a change no function
   digest can attribute), carrying the rest (`reach_store.py`).
4. **Regenerate every derived file**: the ledger, reach cells and arm sections,
   `handwritten-reach.tsv`, the census tallies, `scenario-proof-index.tsv`, the
   region keys, the coverage headline, the arm searches' outstanding list and the
   witness-search registries index.
5. **During a merge** whose conflicted hunks all lie in derived content, those
   hunks are resolved by regenerating (the merge is committed first, so the
   measurement names a commit); any other conflicted hunk is refused by name.

It holds the host-wide instrumented-measurement lock around every instrumented
build and run, defaults to `--jobs 1` outside CI, and prints one summary line,
naming the base it stepped from and why (or why it measured fully); `--verbose`
also names each re-anchored site and each re-run with its reason.
"""

from __future__ import annotations

import argparse
import importlib.util
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile
from collections.abc import Callable
from pathlib import Path
from typing import TYPE_CHECKING, Any, NamedTuple, NoReturn, Protocol

if TYPE_CHECKING:
    from reach_store import Function, ParsedFile, Store

HERE = Path(__file__).resolve().parent
REGIONS = Path("docs") / "openapi-surface"
SITES = REGIONS / "golden-reach-sites.tsv"
COVERAGE = Path("docs") / "openapi-surface-coverage.md"


def _load(name: str, file: str) -> Any:
    """A sibling script by path: its hyphenated name is no importable module, so it is typed `Any`."""
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, HERE / file)
    if spec is None or spec.loader is None:
        raise SystemExit(f"census-repin: cannot load tools/surface-census/{file}; restore it from git")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


REACH = _load("census_repin_golden_reach", "golden-reach.py")
RS = REACH.RS
# A site that runs to the end of its line, as golden-reach.py's `Site` marks one.
EOL = REACH.Site._field_defaults["end_col"]
BASES = _load("reach_base", "reach_base.py")


def refuse(message: str) -> NoReturn:
    raise SystemExit(f"census-repin: {message}")


WHOLLY_DERIVED = {
    (REGIONS / name).as_posix()
    for name in (
        "golden-reach.tsv",
        "handwritten-reach.tsv",
        "handwritten-config-gates.tsv",
        "witness-search-keys.tsv",
        "witness-search-registries/outstanding.tsv",
        "witness-search-registries/candidates.tsv",
        "golden-reach-witnesses/outstanding.tsv",
    )
}
SCENARIO_INDEX = (REGIONS / "scenario-proof-index.tsv").as_posix()


class Hunk(NamedTuple):
    """One conflicted hunk: its `<<<<<<<` and `>>>>>>>` lines (1-indexed) and each side's lines."""

    path: str
    line: int
    ours: list[str]
    theirs: list[str]
    last: int = 0


def conflict_hunks(text: str, path: str) -> list[Hunk]:
    """Every `<<<<<<<` … `>>>>>>>` hunk of a conflicted file (a diff3 base section dropped)."""
    hunks, lines = [], text.splitlines()
    index = 0
    while index < len(lines):
        if not lines[index].startswith("<<<<<<< "):
            index += 1
            continue
        start, ours, theirs, part = index + 1, [], [], "ours"
        separator, base_seen = False, False
        index += 1
        while index < len(lines) and not lines[index].startswith(">>>>>>> "):
            line = lines[index]
            if (
                line.startswith("<<<<<<< ")
                or (line == "=======" and separator)
                or (line.startswith("||||||| ") and (base_seen or separator))
            ):
                refuse(
                    f"{path}:{start}: malformed conflict markers; resolve the hunk by hand, then re-run `just census-repin`"
                )
            match line, part:
                case _, _ if line.startswith("||||||| "):
                    part = "base"
                    base_seen = True
                case "=======", _:
                    part = "theirs"
                    separator = True
                case _, "ours":
                    ours.append(line)
                case _, "theirs":
                    theirs.append(line)
            index += 1
        if index == len(lines) or not separator:
            refuse(
                f"{path}:{start}: incomplete conflict markers (separator or closing marker missing); resolve the hunk by hand, then re-run `just census-repin`"
            )
        hunks.append(Hunk(path, start, ours, theirs, index + 1))
        index += 1
    return hunks


def _region_row_derived(ours: list[str], theirs: list[str]) -> bool:
    """Both sides are the same golden rows, differing only in their generated reach cells."""
    if len(ours) != len(theirs) or not ours:
        return False
    rows = REACH.region_rows
    for left, right in zip(ours, theirs, strict=True):
        a, b = rows(left), rows(right)
        if len(a) != 1 or len(b) != 1:
            return False
        a, b = a[0], b[0]
        if len(a) != len(b) or a[0] != b[0] or a[3].strip("`") != "golden" or a[:5] != b[:5] or a[6:] != b[6:]:
            return False
        if not (a[5].startswith(REACH.CELL_PREFIX) and b[5].startswith(REACH.CELL_PREFIX)):
            return False
    return True


def _scenario_rows_derived(ours: list[str], theirs: list[str]) -> bool:
    """Both sides are the same index rows, differing only in the cells its `write` restates."""
    if len(ours) != len(theirs) or not ours:
        return False
    index = _load("census_repin_scenario_index", "scenario-proof-index.py")
    derived = set(index.DERIVED_COLUMNS)
    columns = index.INDEX_HEADER
    for left, right in zip(ours, theirs, strict=True):
        a, b = left.split("\t"), right.split("\t")
        if len(a) != len(columns) or len(b) != len(columns) or a[0] != b[0]:
            return False
        if not index.has_derived_cells(a[columns.index("kind")], a[columns.index("goldens")]):
            return False
        if any(x != y for name, x, y in zip(columns, a, b, strict=True) if name not in derived):
            return False
    return True


def _generated_sections(text: str) -> list[tuple[int, int]]:
    """1-indexed line spans between a `BEGIN GENERATED` and its `END GENERATED` marker."""
    spans, start = [], None
    for number, line in enumerate(text.splitlines(), start=1):
        if "<!-- BEGIN GENERATED" in line:
            start = number
        elif "<!-- END GENERATED" in line and start is not None:
            spans.append((start, number))
            start = None
    return spans


def derived_hunk(hunk: Hunk, text: str) -> bool:
    if hunk.path in WHOLLY_DERIVED:
        return True
    if hunk.path == SCENARIO_INDEX:
        return _scenario_rows_derived(hunk.ours, hunk.theirs)
    if hunk.path == COVERAGE.as_posix():
        # Wholly inside one generated section, its markers outside the hunk on both sides.
        marked = any("<!-- BEGIN GENERATED" in line or "<!-- END GENERATED" in line for line in hunk.ours + hunk.theirs)
        return not marked and any(lo < hunk.line and hunk.last < hi for lo, hi in _generated_sections(text))
    if hunk.path.startswith(REGIONS.as_posix() + "/") and hunk.path.count("/") == 2 and hunk.path.endswith(".md"):
        return _region_row_derived(hunk.ours, hunk.theirs)
    return False


def take_ours(text: str) -> str:
    out, part = [], None
    for line in text.splitlines(keepends=True):
        match part:
            case _ if line.startswith("<<<<<<< "):
                part = "ours"
            case str() if line.startswith("||||||| "):
                part = "base"
            case str() if line.rstrip("\r\n") == "=======":
                part = "theirs"
            case str() if line.startswith(">>>>>>> "):
                part = None
            case None | "ours":
                out.append(line)
    return "".join(out)


def resolve_merge(root: Path) -> int:
    """Complete a merge whose every conflicted hunk is derived content; refuse otherwise. Returns hunks resolved."""
    merge_head = Path(RS.git(root, "rev-parse", "--git-path", "MERGE_HEAD").strip())
    if not (merge_head if merge_head.is_absolute() else root / merge_head).is_file():
        return 0
    paths = [p for p in RS.git(root, "diff", "--name-only", "--diff-filter=U").splitlines() if p]
    refused: list[str] = []
    texts: dict[str, str] = {}
    resolved = 0
    for path in paths:
        try:
            text = (root / path).read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            refused.append(f"{path}: cannot read the conflicted path as UTF-8 text ({error})")
            continue
        if "\x00" in text:
            refused.append(f"{path}: binary conflict, not a generated text hunk")
            continue
        texts[path] = text
        hunks = conflict_hunks(text, path)
        if not hunks:
            refused.append(f"{path}: conflicted without text markers (a binary, deleted or renamed file)")
        for hunk in hunks:
            if derived_hunk(hunk, text):
                resolved += 1
                continue
            first = (hunk.ours or hunk.theirs or [""])[0]
            refused.append(f"{path}:{hunk.line}: `{first[:100]}` is not derived content")
    if refused:
        refuse(
            "refusing to finish the merge: these conflicted hunks are not derived content, so regenerating "
            "cannot resolve them — resolve them by hand, `git add` them, then re-run `just census-repin`:\n  "
            + "\n  ".join(refused)
        )
    for path, text in texts.items():
        (root / path).write_text(take_ours(text), encoding="utf-8")
        RS.git(root, "add", "--", path)
    RS.git(root, "commit", "--no-edit", "--quiet")
    return resolved


class Anchor(NamedTuple):
    spec: str
    replacement: str | None
    problem: str | None


def _broken(spec: str, root: Path) -> str | None:
    try:
        REACH.resolve_site(spec, root)
    except SystemExit as error:
        return str(error)
    return None


def _file_root(root: Path, commit: str, path: str) -> Path | None:
    data = RS.show(root, commit, path)
    if data is None:
        return None
    scratch = Path(tempfile.mkdtemp(prefix="census-repin-base-"))
    (scratch / path).parent.mkdir(parents=True, exist_ok=True)
    (scratch / path).write_bytes(data)
    return scratch


def _matched_line(spec: str, root: Path) -> int:
    match = REACH._SITE.match(spec)
    assert match is not None
    lines = (root / match.group("file")).read_text(encoding="utf-8").splitlines()
    start, end = REACH._function_spans(lines, match.group("item"))[0]
    arm = match.group("arm")
    pattern = re.compile(arm[1:] if arm.startswith("=") else arm)
    return next(n for n in range(start, end + 1) if pattern.search(lines[n - 1]))


def _token_at(parsed: ParsedFile, offset: int) -> int:
    starts = [token.start for token in parsed.tokens]
    import bisect

    return max(bisect.bisect_right(starts, offset) - 1, 0)


def _line_tokens(parsed: ParsedFile, line: int) -> list[int]:
    lo = parsed.line_starts[line - 1]
    hi = parsed.line_starts[line] if line < len(parsed.line_starts) else len(parsed.source)
    return [k for k, token in enumerate(parsed.tokens) if lo <= token.start < hi]


def _pattern(parsed: ParsedFile, indices: list[int]) -> str:
    """A regex matching those tokens on one line: each escaped, gaps as whitespace."""
    out = []
    for position, k in enumerate(indices):
        token = parsed.tokens[k]
        if position and parsed.tokens[indices[position - 1]].end != token.start:
            out.append(r"\s+")
        text = token.text.encode("latin-1").decode("utf-8", "replace")
        for char in text:
            match char:
                case _ if char.isalnum() or char == "_":
                    out.append(char)
                # Characters a spec cannot hold literally: its `[...]`, a table's `|`, a TOML quote, a space.
                case "[" | "]" | "|" | "'" | '"' | " " | "\t":
                    out.append(f"\\x{ord(char):02x}")
                case _:
                    out.append(re.escape(char))
    return "".join(out).replace(" ; ", " \\x3b ")


class _Span(Protocol):
    """A resolved site's span, as golden-reach.py's `Site` gives it (that module is loaded by path)."""

    start: int
    end: int
    start_col: int
    end_col: int


def _site_offsets(site: _Span, parsed: ParsedFile) -> tuple[int, int | None]:
    start = parsed.offset(site.start, site.start_col)
    end = None if site.end_col == EOL else parsed.offset(site.end, site.end_col)
    return start, end


def _old_new_code(old: ParsedFile, a: int, b: int, new: ParsedFile, function: Function, guess: int) -> tuple[str, str]:
    def lines(parsed: ParsedFile, lo: int, hi: int) -> str:
        first = parsed.position(parsed.tokens[lo].start)[0]
        last = parsed.position(parsed.tokens[hi].start)[0]
        body = parsed.source.decode("utf-8", "replace").splitlines()[first - 1 : last]
        return "\n      ".join(f"{first + i}: {line}" for i, line in enumerate(body))

    k = function.indices[min(max(guess, 0), len(function.indices) - 1)]
    span = min(b - a, len(function.indices) - 1)
    hi = function.indices[min(function.indices.index(k) + span, len(function.indices) - 1)]
    return lines(old, a, b), lines(new, k, hi)


def reanchor(spec: str, root: Path, base_commit: str) -> Anchor:
    """Follow a broken arm site from the base tree into HEAD by its tokens (see the module docstring)."""
    match = REACH._SITE.match(spec)
    if match is None or match.group("arm") is None:
        return Anchor(spec, None, "it names a whole function, which no line anchor can follow; correct it by hand")
    path = match.group("file")
    base_root = _file_root(root, base_commit, path)
    if base_root is None or _broken(spec, base_root):
        return Anchor(
            spec, None, f"it does not resolve at the base {base_commit[:12]} either, so there is no line to follow"
        )
    if not (root / path).is_file():
        return Anchor(
            spec,
            None,
            f"its source file {path} is gone at HEAD (deleted or renamed); name where the feature is handled now",
        )
    old_site = REACH.resolve_site(spec, base_root)
    old = RS.parse(path, (base_root / path).read_bytes())
    new = RS.parse(path, (root / path).read_bytes())
    old_tree = RS.read_tree(base_root, {path: old.source})
    new_tree = RS.read_tree(root, {path: new.source})
    line = _matched_line(spec, base_root)
    on_line = _line_tokens(old, line)
    if not on_line:
        return Anchor(spec, None, f"its anchored line {path}:{line} at the base holds no code token")
    a = on_line[0]
    start_offset, end_offset = _site_offsets(old_site, old)
    last = _token_at(old, end_offset - 1) if end_offset is not None else on_line[-1]
    b = max(last, on_line[-1])
    owner = old_tree.owner(path, old.tokens[a].start)
    if owner is None or owner.key not in new_tree.functions:
        return Anchor(spec, None, f"its function is gone from {path} at HEAD; name where the feature is handled now")
    function = new_tree.functions[owner.key]
    anchored = [old.tokens[k].text for k in range(a, b + 1)]
    texts = [new.tokens[k].text for k in function.indices]
    hits = [i for i in range(len(texts) - len(anchored) + 1) if texts[i : i + len(anchored)] == anchored]
    if len(hits) != 1:
        guess = owner.indices.index(a) if a in owner.indices else 0
        old_code, new_code = _old_new_code(old, a, b, new, function, guess)
        how = "no longer holds" if not hits else f"holds {len(hits)} copies of"
        return Anchor(
            spec,
            None,
            f"the anchored code changed: `{owner.key}` at HEAD {how} it token for token.\n"
            f"    old ({base_commit[:12]}):\n      {old_code}\n    new (HEAD):\n      {new_code}\n"
            "    Decide whether the feature is still handled there: re-point the site in "
            f"{SITES.as_posix()} (and every file quoting it) at the arm that handles it now, or retire it",
        )
    k0 = function.indices[hits[0]]

    def moved(offset: int) -> int:
        t = _token_at(old, offset)
        return new.tokens[k0 + (t - a)].start + (offset - old.tokens[t].start)

    want = (moved(start_offset), None if end_offset is None else moved(end_offset))
    arm = match.group("arm")
    line_only = arm.startswith("=")
    first_new = k0 + (_token_at(old, start_offset) - a) if line_only else k0
    head_line = new.position(new.tokens[first_new].start)[0]
    whole = _line_tokens(new, head_line)
    tail = [k for k in whole if k >= first_new]
    indent = len(new.source.decode("latin-1").splitlines()[head_line - 1]) - len(
        new.source.decode("latin-1").splitlines()[head_line - 1].lstrip(" ")
    )
    candidates = [_pattern(new, tail)]
    if not line_only:
        candidates += [f"^\\s*{_pattern(new, whole)}", f"^ {{{indent}}}{_pattern(new, whole)}"]
    for candidate in candidates:
        replacement = f"{path}::{match.group('item')}[{'=' if line_only else ''}{candidate}]"
        if REACH._SITE.match(replacement) is None or REACH.SITE_SEPARATOR in replacement:
            continue
        if _broken(replacement, root):
            continue
        if _site_offsets(REACH.resolve_site(replacement, root), new) == want:
            return Anchor(spec, replacement, None)
    return Anchor(
        spec,
        None,
        f"its tokens are unchanged at {path}:{head_line}, but no single-line pattern anchors them uniquely; "
        "anchor it by hand",
    )


def spec_files(root: Path) -> list[Path]:
    """Every file that may quote a site spec."""
    regions = root / REGIONS
    files = [
        regions / "golden-reach-sites.tsv",
        regions / "golden-reach.tsv",
        regions / "handwritten-reach.tsv",
        regions / "handwritten-config-gates.tsv",
        root / COVERAGE,
    ]
    files += sorted(regions.glob("handwritten/*/evidence.toml"))
    files += sorted(p for p in regions.rglob("*.md") if p.is_file())
    return [p for p in dict.fromkeys(files) if p.is_file()]


def _toml_basic(text: str) -> str:
    return text.replace("\\", "\\\\").replace('"', '\\"')


_TOML_TEXT = re.compile(
    r"(?P<comment>\#[^\n]*)"
    r'|(?P<basic>"""(?:\\.|(?!""")[^\\])*"""|"(?:\\.|[^"\\\n])*")'
    r"|(?P<literal>'''[\s\S]*?'''|'[^'\n]*')",
    re.DOTALL,
)


def _rewrite_toml_specs(text: str, old: str, new: str) -> str:
    """Escape new regex backslashes in basic strings; preserve literal strings and comments."""

    def replace(match: re.Match[str]) -> str:
        before, after = (_toml_basic(old), _toml_basic(new)) if match.lastgroup == "basic" else (old, new)
        return match.group().replace(before, after)

    return _TOML_TEXT.sub(replace, text)


def rewrite_specs(root: Path, moves: dict[str, str]) -> list[Path]:
    """Replace every quoted old spec by its new spelling; return the files changed."""
    changed = []
    for path in spec_files(root):
        text = path.read_text(encoding="utf-8")
        updated = text
        for old, new in moves.items():
            updated = _rewrite_toml_specs(updated, old, new) if path.suffix == ".toml" else updated.replace(old, new)
        if updated != text:
            path.write_text(updated, encoding="utf-8", newline="\n")
            changed.append(path)
    return changed


def site_specs(root: Path) -> list[str]:
    table = REACH.read_sites_table(root / SITES)
    return sorted({spec for row in table.values() for spec in row.sites})


def ledger_commit(root: Path) -> str | None:
    ledger = root / REGIONS / "golden-reach.tsv"
    if not ledger.is_file():
        return None
    found = re.search(r"measured at commit ([0-9a-f]{7,40})", ledger.read_text(encoding="utf-8").split("\n", 1)[0])
    if not found:
        return None
    resolved = subprocess.run(
        ["git", "rev-parse", "--verify", "--quiet", f"{found.group(1)}^{{commit}}"],
        cwd=root,
        capture_output=True,
        text=True,
    )
    return resolved.stdout.strip() or None


def reanchor_all(root: Path, base_commit: str | None) -> dict[str, str]:
    """Re-anchor every broken site, or refuse naming each one that cannot be (rewriting nothing)."""
    broken = {spec: problem for spec in site_specs(root) if (problem := _broken(spec, root))}
    if not broken:
        return {}
    commits = [c for c in (base_commit, ledger_commit(root)) if c]
    moves: dict[str, str] = {}
    refused: list[str] = []
    for spec, problem in sorted(broken.items()):
        anchor = None
        for commit in dict.fromkeys(commits):
            anchor = reanchor(spec, root, commit)
            if anchor.replacement is not None:
                break
        match anchor:
            case None:
                refused.append(f"`{spec}`: {problem}; there is no base tree to follow it from")
            case Anchor(replacement=None, problem=reason):
                refused.append(f"`{spec}`: {reason}")
            case Anchor(replacement=str() as replacement):
                moves[spec] = replacement
    if refused:
        refuse(f"{len(refused)} site(s) cannot be re-anchored, so nothing was rewritten:\n  " + "\n  ".join(refused))
    return moves


def census_python(root: Path) -> str:
    # Resolve PATH explicitly: Windows CreateProcess otherwise prefers the
    # system's WSL bash over Git Bash, even when Git Bash is first on PATH.
    shell = shutil.which("bash")
    if shell is None:
        refuse("cannot run the interpreter selector: bash is not on PATH; run `just bootstrap` and repair the selector")
    try:
        run = subprocess.run([shell, "scripts/census-python.sh"], cwd=root, capture_output=True, text=True)
    except OSError as error:
        refuse(
            f"cannot run the interpreter selector scripts/census-python.sh ({error}); run `just bootstrap` and repair the selector"
        )
    if run.returncode != 0 or not run.stdout.strip():
        refuse(
            f"interpreter selector scripts/census-python.sh exited {run.returncode} or printed no interpreter: {run.stderr.strip()[-500:]}; run `just bootstrap` and repair the selector"
        )
    python = run.stdout.strip()
    try:
        probe = subprocess.run(
            [
                shell,
                "-c",
                '"$1" -c "$2"',
                "census-python",
                python,
                "import sys; assert sys.version_info >= (3, 11); print('crozier-census-python'); print(sys.executable)",
            ],
            cwd=root,
            capture_output=True,
            text=True,
        )
    except OSError as error:
        refuse(
            f"interpreter selector scripts/census-python.sh selected unusable {python!r} ({error}); run `just bootstrap` and repair the selector"
        )
    lines = probe.stdout.strip().splitlines()
    if probe.returncode != 0 or len(lines) != 2 or lines[0] != "crozier-census-python" or not Path(lines[-1]).is_file():
        refuse(
            f"interpreter selector scripts/census-python.sh selected {python!r}, which failed the Python 3.11+ probe: {probe.stderr.strip()[-500:]}; run `just bootstrap` and repair the selector"
        )
    # Bash may select /c/... on Windows; sys.executable is usable by native
    # Python subprocesses as well as by Bash.
    return lines[-1]


def _run(root: Path, argv: list[str], what: str, stdout: Path | None = None) -> None:
    run = subprocess.run(argv, cwd=root, capture_output=True, text=True)
    if run.returncode != 0:
        refuse(f"regenerating {what} failed (`{' '.join(argv[1:3])}` exited {run.returncode}):\n{run.stderr[-3000:]}")
    if stdout is not None:
        stdout.write_text(run.stdout, encoding="utf-8")


def regenerate(root: Path, store: Store, out: Path, scoped: bool = False, python: str | None = None) -> list[str]:
    """Every derived file, each from its own generator, in dependency order; return what was skipped.

    A scoped measurement (`--tests`/`--fixtures`) holds a subset of the witnesses,
    so the sections restating the whole population — the arm sections and the
    coverage headline — are left for an unscoped run.
    """
    python = python or census_python(root)
    tools = root / "tools" / "surface-census"
    census = out / "census.json"
    out.mkdir(parents=True, exist_ok=True)
    _run(root, [python, str(tools / "openapi-surface-census.py"), "--json"], "the census", census)
    handwritten = _load("census_repin_handwritten", "handwritten-fixtures.py")
    handwritten.report(root, store, partial=scoped)
    common = [python, str(tools / "golden-reach.py"), "--repo-root", str(root), "--out", str(out)]
    report = [*common, "report", "--write", "--census", str(census)]
    _run(root, [*report, "--skip-arms"] if scoped else report, "the ledger and reach cells")
    if not scoped:
        _run(root, [*common, "arms"], "the arm sections")
    restate = [python, str(tools / "restate-coverage.py"), "--repo-root", str(root)]
    _run(root, [*restate, "--snapshot-json", str(census), "--write"], "the census tallies")
    if not scoped:
        _run(root, [*restate, "--write"], "the coverage headline")
    _run(
        root,
        [python, str(tools / "scenario-proof-index.py"), "--repo-root", str(root), "write"],
        "scenario-proof-index.tsv",
    )
    _run(
        root,
        [python, str(tools / "witness-search-region-keys.py"), "--regions-dir", str(root / REGIONS)],
        "the region keys",
        root / REGIONS / "witness-search-keys.tsv",
    )
    _run(
        root,
        [python, str(tools / "golden-reach-search.py"), "outstanding"],
        "the arm searches' outstanding list",
    )
    _run(
        root,
        [
            python,
            str(root / "tools" / "witness-search" / "witness-search-registries-index.py"),
            "--root",
            str(root / REGIONS),
        ],
        "the witness-search registries index",
    )
    return ["the arm sections", "the coverage headline"] if scoped else []


INPUTS = re.compile(
    r"(src/|templates/|assets/|crates/|tests/fixtures/|tools/corpus/|\.cargo/|Cargo\.(toml|lock)$|"
    r"rust-toolchain|build\.rs$|docs/openapi-surface/handwritten/[^/]+/(openapi\.yml|evidence\.toml)$)"
)


def dirty_inputs(root: Path) -> list[str]:
    return [path for path in REACH.uncommitted_changes(root) if INPUTS.match(path)]


def tracked_changes(root: Path) -> set[str]:
    return set(REACH.uncommitted_changes(root))


def repin(args: argparse.Namespace, say: Callable[[str], None]) -> int:
    root: Path = args.repo_root.resolve()
    out = root / ".local" / "golden-reach"
    if args.base_only:
        choice = BASES.find(root)
        print(f"census-repin: base {choice.commit or 'none'} ({choice.source}): {choice.reason}")
        return 0
    merged = resolve_merge(root)
    if merged:
        say(f"census-repin: resolved {merged} derived conflict hunk(s) and committed the merge")
    dirty = dirty_inputs(root)
    if dirty:
        refuse(
            f"{len(dirty)} measured input(s) differ from HEAD ({', '.join(dirty[:5])}); commit them first, "
            "so the measurement names the commit it measured"
        )
    python = census_python(root)
    choice = BASES.find(root)
    say(f"census-repin: base: {choice.reason}")
    before = {path: (root / path).read_bytes() if (root / path).is_file() else None for path in tracked_changes(root)}
    moves = reanchor_all(root, choice.commit)
    rewritten = {p.relative_to(root).as_posix() for p in rewrite_specs(root, moves)} if moves else set()
    for old, new in moves.items():
        say(f"census-repin: re-anchored `{old}` as `{new}`")
    with RS.instrumented_lock("census-repin"):
        step = REACH.measure_step(
            root,
            base=choice.store,
            full_reason=choice.reason,
            select_tests=re.compile(args.tests) if args.tests else None,
            select_fixtures=re.compile(args.fixtures) if args.fixtures else None,
            jobs=args.jobs,
        )
    if step.full:
        say(f"census-repin: measured fully: {step.full}")
    for subject, reason in sorted(step.reasons.items()):
        say(f"census-repin: re-ran {subject}: {reason}")
    REACH.write_views(step, out, root)
    BASES.publish(step.store)
    skipped = regenerate(root, step.store, out, scoped=bool(args.tests or args.fixtures), python=python)
    after = tracked_changes(root)
    for path in after:
        current = (root / path).read_bytes() if (root / path).is_file() else None
        if path not in before or before[path] != current:
            rewritten.add(path)
    origin = f"full: {step.full}" if step.full else f"base {(step.base or '?')[:12]}: {choice.reason}"
    notes = [f"a merge's {merged} derived conflict hunk(s) resolved"] if merged else []
    notes += [f"{' and '.join(skipped)} left to an unscoped run"] if skipped else []
    print(
        f"census-repin: {len(step.tests_run)} test(s) run, {len(step.tests_carried)} carried, "
        f"{len(step.fixtures_run)} fixture(s) run, {len(step.fixtures_carried)} carried; "
        f"{len(moves)} site(s) re-anchored, {len(rewritten)} file(s) rewritten "
        f"(measured {step.store['commit'][:12]}, {origin}){''.join('; ' + note for note in notes)}"
    )
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("--repo-root", type=Path, default=HERE.parents[1])
    parser.add_argument("--jobs", type=REACH.positive_int, default=REACH.default_jobs())
    parser.add_argument("--tests", help="measure only the golden tests this regex matches (a scoped measurement)")
    parser.add_argument("--fixtures", help="measure only the hand-written fixtures this regex matches")
    parser.add_argument(
        "--base-only", action="store_true", help="print the base a repin would step from, and why; measure nothing"
    )
    parser.add_argument(
        "--verbose", action="store_true", help="also name each re-anchored site, each re-run and why, on stderr"
    )
    args = parser.parse_args(argv)
    for pattern in (args.tests, args.fixtures):
        if pattern:
            try:
                re.compile(pattern)
            except re.error as error:
                parser.error(f"{pattern!r} is not a regex ({error}) — pass a Python regex over test or fixture names")
    return repin(
        args, (lambda line: print(line, file=sys.stderr, flush=True)) if args.verbose else (lambda _line: None)
    )


if __name__ == "__main__":
    for stream in (sys.stdout, sys.stderr):
        if isinstance(stream, io.TextIOWrapper):
            stream.reconfigure(encoding="utf-8", errors="backslashreplace")
    os.environ.setdefault("PYTHONUTF8", "1")
    sys.exit(main())
