#!/usr/bin/env python3
# llmlint: ignore-file[new_code_lands_in_a_project] crozier is a Cargo crate driven by `just`, with no Nx workspace; this measurement script sits in scripts/ beside fixtures-coverage-report.py, whose tiers it reuses, and runs as `just golden-reach`.
"""Measure how much of crozier's handling of each `golden` census row its witnesses reach.

A `golden` row in `docs/openapi-surface/*.md` says a registered source declares a
feature and its committed Fern golden byte-matches. It does not say which of
crozier's handling sites for that feature any golden actually drives. This script
turns that into a number, from the one tier that means *Fern produced this output
and crozier reproduces it byte for byte*: the `golden-only` tier of
`just fixtures-coverage` (every `*matches_fern_output*` test).

Two subcommands:

* ``measure`` runs that tier **one golden test at a time** against one
  instrumented build and keeps, per test, the production counter regions it
  executed (`#[cfg(test)]` excluded by the report module's own scanner). Counter
  hits add, so a row's scoped run — the tier restricted to the row's witnesses —
  is exactly the union of its witnesses' per-test sets; nothing here estimates.
* ``report`` joins three inputs into the committed ledger
  (`docs/openapi-surface/golden-reach.tsv`) and, with ``--write``, the reach
  cell of every `golden` row:

  - the row's **witnesses** — every golden-bearing registered source the census
    reports declaring the row's selectors (`just surface-census --json`);
  - the row's **handling sites** — the crozier functions, or brace-delimited arms
    inside them, that read the feature, declared per row in
    `docs/openapi-surface/golden-reach-sites.tsv`;
  - the per-test coverage ``measure`` left behind.

  A site's *regions* are the production counter regions that start inside its
  span; a site is *reached* when the witnesses' scoped run executed at least one
  of them. The ranking key is the row's **unreached sites**, then its unreached
  regions, then its key; a row reaching every handling site ties at the bottom.

What the site table declares is where crozier handles a feature; what the cell
reports about those sites is measured, never read off the source. `just
golden-reach` runs the whole pipeline; `just golden-reach-report` re-joins an
existing measurement after the site table changes.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import fnmatch
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading
from collections import defaultdict
from pathlib import Path
from typing import IO, NamedTuple

REPO = Path(__file__).resolve().parent.parent
REGIONS_DIR = REPO / "docs" / "openapi-surface"
SITES_TABLE = REGIONS_DIR / "golden-reach-sites.tsv"
LEDGER = REGIONS_DIR / "golden-reach.tsv"
DEFAULT_OUT = REPO / ".local" / "golden-reach"
GOLDEN_TEST = re.compile(r"matches_fern_output")
CATEGORIES = ("golden", "limitations", "gap")
CELL_PREFIX = "reach:"
# A site spec may hold a comma inside its `[regex]`, so the ledger separates
# sites with a string no spec may contain.
SITE_SEPARATOR = " ; "


def _report_module():
    spec = importlib.util.spec_from_file_location(
        "fixtures_coverage_report", REPO / "scripts" / "fixtures-coverage-report.py"
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


REPORT = _report_module()


def fail(message: str) -> None:
    raise SystemExit(f"golden-reach: {message}")




def region_rows(text: str) -> list[list[str]]:
    """Every entry-table row of one region file, as its eight cells.

    The same parse `RankedBacklogTests.region_rows` performs: `\\|` inside a cell
    is an escaped pipe, not a column break.
    """
    rows = []
    for line in text.splitlines():
        if not line.startswith("| "):
            continue
        cells = [
            cell.replace("\x00", "\\|").strip()
            for cell in line.replace("\\|", "\x00").strip().strip("|").split("|")
        ]
        if len(cells) == 8 and cells[3].strip("`") in CATEGORIES:
            rows.append(cells)
    return rows


def golden_rows(regions_dir: Path = REGIONS_DIR) -> dict[str, str]:
    """`golden` row key -> the region file stem that owns it."""
    out = {}
    for path in sorted(regions_dir.glob("*.md")):
        for cells in region_rows(path.read_text(encoding="utf-8")):
            if cells[3].strip("`") == "golden":
                out[cells[0].strip("`")] = path.stem
    return out




class Site(NamedTuple):
    """One declared handling site, resolved to an inclusive span of a file.

    Positions are `(line, column)`, 1-indexed as llvm-cov reports a counter
    region's start. A function site spans its whole item. An arm site starts at
    the brace that opens the arm's body, so the condition that chooses the arm —
    which runs whether or not the arm is taken — is not part of it, and it stops
    at the brace that closes the body, so an `} else {` after it is not either.
    """

    spec: str
    file: str
    start: int
    end: int
    start_col: int = 1
    end_col: int = 1 << 30

    def holds(self, region: tuple[int, int, int, int]) -> bool:
        """Whether a counter region starting at `region[:2]` is part of this site.

        The end is exclusive: llvm-cov starts the region for the code *after* a
        block at that block's closing brace, and that code runs whether or not the
        arm did.
        """
        return (self.start, self.start_col) <= (region[0], region[1]) < (self.end, self.end_col)


class SiteRow(NamedTuple):
    key: str
    selectors: tuple[str, ...]
    sites: tuple[str, ...]
    # Why an arm that looks like this feature's is not counted: a rejection or
    # absence arm, or code no document can reach. Rendered into the reach cell.
    note: str = ""


def read_sites_table(path: Path = SITES_TABLE) -> dict[str, SiteRow]:
    """`key -> (selectors, site specs, note)` from the tab-separated declaration table."""
    if not path.is_file():
        fail(f"{path} is missing; it declares every golden row's selectors and sites")
    lines = path.read_text(encoding="utf-8").splitlines()
    header = ["key", "selectors", "sites", "note"]
    if not lines or lines[0].split("\t") != header:
        fail(f"{path} must start with the header {'<TAB>'.join(header)}")
    rows: dict[str, SiteRow] = {}
    for number, line in enumerate(lines[1:], start=2):
        fields = line.split("\t")
        if len(fields) != 4:
            fail(f"{path}:{number} has {len(fields)} fields, not 4")
        key, selectors, sites, note = fields
        if key in rows:
            fail(f"{path}:{number} declares {key} twice")
        selector_list = tuple(s.strip() for s in selectors.split(",") if s.strip())
        if not selector_list:
            fail(f"{path}:{number} ({key}) names no census selector")
        site_list = () if sites.strip() == "none" else tuple(
            s.strip() for s in _split_sites(sites) if s.strip()
        )
        if not site_list and sites.strip() != "none":
            fail(f"{path}:{number} ({key}) names no site; write `none` for a feature crozier reads nowhere")
        rows[key] = SiteRow(key, selector_list, site_list, note.strip())
    return rows


def _split_sites(cell: str) -> list[str]:
    """Split a sites cell on the commas outside a `[regex]`, so a regex may hold one."""
    out, depth, current = [], 0, []
    for char in cell:
        if char == "[" and (not current or current[-1] != "\\"):
            depth += 1
        elif char == "]" and depth and (not current or current[-1] != "\\"):
            depth -= 1
        if char == "," and depth == 0:
            out.append("".join(current))
            current = []
            continue
        current.append(char)
    out.append("".join(current))
    return out


_SITE = re.compile(r"^(?P<file>src/[a-z_]+\.rs)::(?P<item>[A-Za-z_][A-Za-z0-9_:]*)(?:\[(?P<arm>[^\]]+)\])?$")


def _function_spans(lines: list[str], item: str) -> list[tuple[int, int]]:
    """Inclusive 1-indexed spans of every `fn` named by `item` (`name` or `Type::name`)."""
    owner, _, name = item.rpartition("::")
    fn = re.compile(rf"^\s*(?:pub(?:\([a-z]+\))?\s+)?(?:const\s+)?fn\s+{re.escape(name)}\b")
    impl = re.compile(r"^(?:impl(?:<[^>]*>)?\s+(?:[A-Za-z_][A-Za-z0-9_<>, ]*\s+for\s+)?(?P<type>[A-Za-z_][A-Za-z0-9_]*))")
    spans = []
    current_impl: tuple[str, int] | None = None
    for index, line in enumerate(lines):
        header = impl.match(line)
        if header:
            end = REPORT._item_end_line(lines, index - 1)
            current_impl = (header.group("type"), end or index + 1)
        if current_impl and index + 1 > current_impl[1]:
            current_impl = None
        if not fn.match(line):
            continue
        if owner and (current_impl is None or current_impl[0] != owner):
            continue
        if not owner and current_impl is not None and line.startswith(" "):
            # A bare name means a free function; methods are named `Type::name`.
            continue
        end = REPORT._item_end_line(lines, index - 1)
        if end is None:
            fail(f"cannot bound the body of `fn {name}` at line {index + 1}; check its braces balance (`cargo check`), or name a different site in {SITES_TABLE.name}")
        spans.append((index + 1, end))
    return spans


def resolve_site(spec: str, repo_root: Path = REPO) -> Site:
    """The inclusive line span `spec` names, or an actionable refusal.

    `src/<file>.rs::<fn>` is a free function, `src/<file>.rs::<Type>::<fn>` a
    method, and a trailing `[<regex>]` narrows either to the brace-delimited block
    opened on the one line inside it the regex matches — an `if` body or a match
    arm, read at the grain of the arm rather than the whole function.
    """
    match = _SITE.match(spec)
    if SITE_SEPARATOR in spec:
        fail(f"site {spec!r} contains {SITE_SEPARATOR!r}, which separates sites in the ledger")
    if "|" in spec:
        # The spec is quoted in a markdown table cell, where a pipe — escaped or
        # not — splits the row for any reader that does not unescape it first.
        fail(f"site {spec!r} contains `|`; write `\\x7c` for a literal pipe in its regex")
    if not match:
        fail(f"site {spec!r} is not `src/<file>.rs::<fn>`, `::<Type>::<fn>`, or either with `[<regex>]`")
    path = repo_root / match.group("file")
    if not path.is_file():
        fail(f"site {spec!r} names {match.group('file')}, which does not exist")
    lines = path.read_text(encoding="utf-8").splitlines()
    spans = _function_spans(lines, match.group("item"))
    if len(spans) != 1:
        fail(
            f"site {spec!r} matches {len(spans)} functions; name exactly one "
            f"(qualify a method as `Type::name`)"
        )
    start, end = spans[0]
    arm = match.group("arm")
    if arm is None:
        return Site(spec, match.group("file"), start, end)
    line_only = arm.startswith("=")
    pattern = re.compile(arm[1:] if line_only else arm)
    hits = [n for n in range(start, end + 1) if pattern.search(lines[n - 1])]
    if len(hits) != 1:
        fail(f"site {spec!r}: the arm regex matches {len(hits)} lines of its function, not 1")
    first = hits[0]
    if line_only:
        column = pattern.search(lines[first - 1]).start() + 1
        return Site(spec, match.group("file"), first, first, column, 1 << 30)
    opening = _opening_line(lines, first, end)
    if opening is None:
        fail(
            f"site {spec!r}: no brace block opens on line {first} or within the "
            f"next {_CONDITION_LINES} lines; use `[=regex]` for a one-line arm"
        )
    code = lines[opening - 1].rstrip()
    if code.endswith("{"):
        # The block is the one the line's trailing brace opens — so a pattern
        # like `Auth::Bearer { required } => {` is bounded by its body, not by
        # the braces of the pattern it destructures.
        open_col = len(code)
        # `_item_end_line` answers 1-indexed within the list it is given, whose
        # second entry stands for the opening line itself.
        relative = REPORT._item_end_line(["", "{"] + lines[opening:], 0)
        arm_end = None if relative is None else opening + relative - 2
    else:
        open_col = lines[opening - 1].index("{") + 1
        arm_end = REPORT._item_end_line(lines, opening - 2)
    if arm_end is None or arm_end > end:
        fail(f"site {spec!r}: cannot bound the block opened on line {opening}; anchor the arm regex on a line that opens a balanced block, or use `[=regex]` for a one-line arm")
    arrow = code.find("=>")
    if arrow != -1 and arrow < open_col:
        # A match arm: its body starts after `=>`, whether that body is a block
        # or an expression holding braces of its own (`=> Auth::Bearer {`).
        body = code[arrow + 2 :]
        open_col = arrow + 3 + (len(body) - len(body.lstrip()))
    closing = lines[arm_end - 1]
    close_col = closing.index("}") + 1 if arm_end != opening and "}" in closing else 1 << 30
    return Site(spec, match.group("file"), opening, arm_end, open_col, close_col)


_CONDITION_LINES = 8


def _opening_line(lines: list[str], first: int, end: int) -> int | None:
    """The line opening the arm's block: the matched line when it holds a brace,
    else the first line ending in one within a multi-line condition's reach."""
    if "{" in lines[first - 1]:
        return first
    for number in range(first + 1, min(end, first + _CONDITION_LINES) + 1):
        if lines[number - 1].rstrip().endswith("{"):
            return number
    return None




def _llvm_tool(name: str) -> str:
    sysroot = subprocess.run(
        ["rustc", "--print", "sysroot"], check=True, capture_output=True, text=True
    ).stdout.strip()
    host = next(
        line.split(":", 1)[1].strip()
        for line in subprocess.run(
            ["rustc", "-vV"], check=True, capture_output=True, text=True
        ).stdout.splitlines()
        if line.startswith("host:")
    )
    tool = Path(sysroot) / "lib" / "rustlib" / host / "bin" / name
    if not tool.is_file():
        fail(f"{tool} is missing — run `rustup component add llvm-tools-preview` (`just bootstrap`)")
    return str(tool)


def run_llvm(argv: list[str], stdout: IO[str] | None = None) -> None:
    """Run an llvm-profdata/llvm-cov step, failing with its stderr and the fix."""
    run = subprocess.run(argv, stdout=stdout, stderr=subprocess.PIPE, text=True)
    if run.returncode != 0:
        fail(
            f"`{Path(argv[0]).name} {argv[1]}` exited {run.returncode}: {run.stderr.strip()[-400:]} — "
            f"the profiles and the instrumented binaries disagree; rebuild them with "
            f"`just golden-reach` and retry"
        )


def _instrumented_binaries(repo_root: Path) -> tuple[Path, Path]:
    deps = repo_root / "target" / "llvm-cov-target" / "debug" / "deps"
    candidates = [
        p for p in deps.glob("e2e-*") if p.is_file() and os.access(p, os.X_OK) and p.suffix == ""
    ]
    if not candidates:
        fail(f"no instrumented e2e binary under {deps} — run `just golden-reach`, which builds it")
    e2e = max(candidates, key=lambda p: p.stat().st_mtime)
    crozier = repo_root / "target" / "llvm-cov-target" / "debug" / "crozier"
    if not crozier.is_file():
        fail(f"no instrumented crozier binary at {crozier} — run `just golden-reach`, which builds it")
    return e2e, crozier


def _covered(export: Path, repo_root: Path) -> tuple[dict[str, list[list[int]]], dict[str, list[list[int]]]]:
    """(every production region, the executed ones) per `src/` file of one export."""
    tier = {"t": REPORT.load_tier(export, repo_root)}
    REPORT.drop_test_regions(tier, repo_root)
    universe = {f: sorted(list(r) for r in counts) for f, counts in tier["t"].items()}
    hit = {f: sorted(list(r) for r, n in counts.items() if n > 0) for f, counts in tier["t"].items()}
    return universe, {f: v for f, v in hit.items() if v}


def uncommitted_changes(repo_root: Path) -> list[str]:
    """Tracked paths that differ from `HEAD` — what a measurement stamped with
    `HEAD` would silently include."""
    status = subprocess.run(
        ["git", "status", "--porcelain", "--untracked-files=no"],
        cwd=repo_root, capture_output=True, text=True,
    )
    if status.returncode != 0:
        fail(f"git status exited {status.returncode}: {status.stderr.strip()[-400:]}")
    return [line[3:] for line in status.stdout.splitlines() if line.strip()]


def measure(args: argparse.Namespace) -> int:
    repo_root: Path = args.repo_root
    out: Path = args.out
    for tool in ("cargo",):
        if shutil.which(tool) is None:
            fail(f"{tool} is not on PATH; install the pinned toolchain with `just bootstrap`")
    # The ledger names the commit it was measured at, so the measured tree must
    # be that commit's: a merge measured before it is committed would stamp its
    # first parent.
    dirty = uncommitted_changes(repo_root)
    if dirty:
        fail(
            f"{len(dirty)} tracked file(s) differ from HEAD ({', '.join(dirty[:5])}); "
            "commit them first so the ledger's measured commit is the tree measured"
        )
    build = subprocess.run(
        ["cargo", "llvm-cov", "--locked", "--no-report", "nextest", "-E",
         "binary(e2e) and test(=every_feature_target_has_its_own_golden_test)"],
        cwd=repo_root, capture_output=True, text=True,
    )
    if build.returncode != 0:
        sys.stderr.write(build.stdout[-4000:] + build.stderr[-4000:])
        fail("the instrumented build failed (its output is above); fix what it names and re-run `just golden-reach`")
    e2e, crozier = _instrumented_binaries(repo_root)
    listed = subprocess.run(
        [str(e2e), "--list", "--format", "terse"], cwd=repo_root,
        capture_output=True, text=True,
    )
    if listed.returncode != 0:
        fail(f"{e2e} --list exited {listed.returncode}: {listed.stderr.strip()[-400:]} — rebuild it with `just golden-reach`")
    listing = listed.stdout
    tests = sorted(
        line.rsplit(": test", 1)[0]
        for line in listing.splitlines()
        if line.endswith(": test") and GOLDEN_TEST.search(line)
    )
    if args.tests:
        selected = re.compile(args.tests)
        tests = [t for t in tests if selected.search(t)]
    if not tests:
        fail(
            "no golden test is selected — check the --tests regex against "
            "`cargo nextest list -E 'binary(e2e)'`, or register the corpus's "
            "`*_matches_fern_output` test in tests/e2e.rs"
        )
    profdata = _llvm_tool("llvm-profdata")
    llvm_cov = _llvm_tool("llvm-cov")
    (out / "tests").mkdir(parents=True, exist_ok=True)
    # Every region set is this build's: the universe is rewritten from this run's
    # first export, and a full run starts from no per-test file at all, so a
    # measurement never pairs one build's hits with another build's regions.
    if not args.tests:
        for stale in (out / "tests").glob("*.json"):
            stale.unlink()
    (out / "universe.json").unlink(missing_ok=True)
    universe_lock = threading.Lock()
    env = dict(os.environ, CROZIER_REQUIRE_CORPUS="1")

    def one(test: str) -> tuple[str, str | None]:
        with tempfile.TemporaryDirectory(prefix="golden-reach-") as scratch:
            raw = Path(scratch)
            run = subprocess.run(
                [str(e2e), "--exact", test, "--test-threads", "1", "--quiet"],
                cwd=repo_root, capture_output=True, text=True,
                env=dict(env, LLVM_PROFILE_FILE=str(raw / "%p-%m.profraw")),
            )
            if run.returncode != 0:
                return test, (run.stdout + run.stderr)[-3000:]
            profiles = sorted(str(p) for p in raw.glob("*.profraw"))
            merged = raw / "merged.profdata"
            run_llvm([profdata, "merge", "-sparse", *profiles, "-o", str(merged)])
            export = raw / "export.json"
            with export.open("w", encoding="utf-8") as sink:
                run_llvm(
                    [llvm_cov, "export", "-format=text", f"-instr-profile={merged}",
                     str(crozier), "-object", str(e2e)],
                    stdout=sink,
                )
            universe, hit = _covered(export, repo_root)
            (out / "tests" / f"{test}.json").write_text(json.dumps(hit), encoding="utf-8")
            universe_path = out / "universe.json"
            with universe_lock:
                if not universe_path.exists():
                    universe_path.write_text(json.dumps(universe), encoding="utf-8")
        return test, None

    failures = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as pool:
        for test, error in pool.map(one, tests):
            if error is not None:
                failures.append((test, error))
    for test, error in failures:
        sys.stderr.write(f"--- {test} ---\n{error}\n")
    if failures:
        fail(
            f"{len(failures)} golden test(s) failed under instrumentation; a failing "
            f"golden measures nothing. Fix them (`just test-corpus-match`) and re-run."
        )
    (out / "provenance.json").write_text(
        json.dumps(
            {
                "commit": subprocess.run(
                    ["git", "rev-parse", "HEAD"], cwd=repo_root, capture_output=True, text=True
                ).stdout.strip(),
                "tests": len(tests),
            }
        ),
        encoding="utf-8",
    )
    print(f"golden-reach: measured {len(tests)} golden test(s) into {out}")
    return 0




def census_witnesses(census: dict, selectors: tuple[str, ...]) -> dict[str, int]:
    """fixture -> declared sites, over every census selector `selectors` names (globs allowed).

    A `fixture=<name>` entry names a witness directly, for a shape no census
    selector expresses (a content-map or status-code *key*): the row's own
    evidence cell is then the measurement naming it, and the gate holds the two
    together. Its declared-site count is not the census's to report, so it
    counts 0 here.
    """
    names = {row["selector"] for row in census["rows"]}
    sources = {source["fixture"] for source in census["sources"]}
    matched = set()
    named: dict[str, int] = {}
    for pattern in selectors:
        if pattern.startswith("fixture="):
            fixture = pattern.removeprefix("fixture=")
            if fixture not in sources:
                fail(f"`{pattern}` names no registered source; correct the `fixture=` selector in {SITES_TABLE.name} to a CORPUS.md name")
            named[fixture] = 0
            continue
        hits = {name for name in names if fnmatch.fnmatchcase(name, pattern)}
        matched |= hits
    counts: dict[str, int] = defaultdict(int, named)
    for row in census["rows"]:
        if row["selector"] in matched:
            counts[row["fixture"]] += row["count"]
    return dict(counts)


class Reach(NamedTuple):
    key: str
    region: str
    witnesses: tuple[str, ...]
    # Registered sources the census reports declaring the row that carry no
    # committed golden (a DROPPED `CORPUS.md` row): counted by the census, but
    # never in the golden-only tier, so they witness nothing here.
    outside: tuple[str, ...]
    sites: tuple[tuple[str, int, int], ...]  # (spec, executed regions, regions)
    note: str = ""

    @property
    def unreached(self) -> int:
        return sum(total - hit for _spec, hit, total in self.sites)

    @property
    def regions(self) -> int:
        return sum(total for _spec, _hit, total in self.sites)

    @property
    def reached_sites(self) -> int:
        return sum(1 for _spec, hit, _total in self.sites if hit)

    @property
    def unreached_sites(self) -> int:
        return len(self.sites) - self.reached_sites


def compute(
    rows: dict[str, str],
    table: dict[str, SiteRow],
    census: dict,
    fixture_tests: dict[str, str],
    coverage: dict[str, dict[str, set[tuple[int, int, int, int]]]],
    universe: dict[str, set[tuple[int, int, int, int]]],
    repo_root: Path = REPO,
) -> list[Reach]:
    """One `Reach` per golden row, in ledger order (unreached descending, then key)."""
    missing = sorted(set(rows) - set(table))
    extra = sorted(set(table) - set(rows))
    if missing or extra:
        fail(
            f"{SITES_TABLE.name} disagrees with the golden rows: missing {missing}, "
            f"not golden {extra}; add or remove those rows so it lists exactly the "
            f"region files' `golden` rows"
        )
    # Each site's regions, and which of them each golden test executed, are
    # computed once: a row's scoped run is the union over its witnesses of
    # those small per-test sets, never of whole-file coverage.
    inside: dict[str, frozenset[tuple[int, int, int, int]]] = {}
    executed_by: dict[tuple[str, str], frozenset[tuple[int, int, int, int]]] = {}

    def regions_of(spec: str) -> frozenset[tuple[int, int, int, int]]:
        if spec not in inside:
            site = resolve_site(spec, repo_root)
            found = frozenset(r for r in universe.get(site.file, set()) if site.holds(r))
            if not found:
                fail(f"site {spec} spans no production counter region; it handles nothing measurable. Point it at the arm that handles the feature, or re-run `just golden-reach` if src/ moved since the measurement")
            inside[spec] = found
            for test, files in coverage.items():
                executed_by[spec, test] = found & files.get(site.file, frozenset())
        return inside[spec]

    out = []
    for key, region in rows.items():
        declared = table[key]
        declaring = census_witnesses(census, declared.selectors)
        witnesses = tuple(sorted(f for f in declaring if f in fixture_tests))
        outside = tuple(sorted(f for f in declaring if f not in fixture_tests))
        sites = []
        for spec in declared.sites:
            found = regions_of(spec)
            hit: set[tuple[int, int, int, int]] = set()
            for fixture in witnesses:
                hit |= executed_by[spec, fixture_tests[fixture]]
            sites.append((spec, len(hit), len(found)))
        out.append(Reach(key, region, witnesses, outside, tuple(sites), declared.note))
    out.sort(key=ranking_key)
    return out


def ranking_key(reach: Reach) -> tuple[int, int, str]:
    """Unreached handling sites, then unreached handling regions, descending; then key."""
    return (-reach.unreached_sites, -reach.unreached, reach.key)


def _witness_phrase(reach: Reach) -> str:
    if not reach.witnesses:
        declared = ", ".join(f"`{f}`" for f in reach.outside) or "no registered source"
        return (
            f"**no** golden-only witness — declared only by {declared}, "
            f"which carr{'ies' if len(reach.outside) == 1 else 'y'} no committed golden"
        )
    if len(reach.witnesses) == 1:
        return f"its **one** golden-only witness `{reach.witnesses[0]}`"
    return f"**{len(reach.witnesses)}** golden-only witnesses"


SEARCHES = "golden-reach-witnesses/searches"


def reach_cell(reach: Reach, rank: int, regions_dir: Path | None = None) -> str:
    """The `crozier sites` cell a `golden` row carries: its measured reach.

    Generated from the ledger row and held to it by `RankedBacklogTests`, so the
    cell is never edited by hand: re-run `just golden-reach-report`. A
    row whose unreached arm has been searched for links its record, which sits at
    `golden-reach-witnesses/searches/<key>.md` beside the region files.
    """
    note = f"; not counted: {reach.note}" if reach.note else ""
    record = (regions_dir or REGIONS_DIR) / SEARCHES / f"{reach.key}.md"
    if record.is_file():
        note += f"; arm search [record]({SEARCHES}/{reach.key}.md)"
    if not reach.sites:
        return (
            f"{CELL_PREFIX} no handling site — no crozier code runs because a "
            f"document declares this feature; {_witness_phrase(reach)}{note} "
            f"([ledger](golden-reach.tsv) rank {rank})"
        )
    reached = [f"`{spec}` {hit}/{total}" for spec, hit, total in reach.sites if hit]
    unreached = [f"`{spec}` 0/{total}" for spec, hit, total in reach.sites if not hit]
    return (
        f"{CELL_PREFIX} **{reach.reached_sites}** of **{len(reach.sites)}** handling "
        f"sites reached (**{reach.regions - reach.unreached}** of **{reach.regions}** "
        f"regions) by {_witness_phrase(reach)}; reached "
        f"{', '.join(reached) or 'none'}; unreached {', '.join(unreached) or 'none'}{note} "
        f"([ledger](golden-reach.tsv) rank {rank})"
    )


LEDGER_HEADER = (
    "rank\tkey\tregion\tunreached_sites\tunreached_regions\tregions\twitnesses\toutside\tsites\tnote"
)


def ledger_text(reaches: list[Reach], provenance: str) -> str:
    lines = [f"# golden-reach ledger — {provenance}", LEDGER_HEADER]
    for rank, reach in enumerate(reaches, start=1):
        lines.append(
            "\t".join(
                [
                    str(rank),
                    reach.key,
                    reach.region,
                    str(reach.unreached_sites),
                    str(reach.unreached),
                    str(reach.regions),
                    ",".join(reach.witnesses) or "-",
                    ",".join(reach.outside) or "-",
                    SITE_SEPARATOR.join(
                        f"{spec}={hit}/{total}" for spec, hit, total in reach.sites
                    ) or "none",
                    reach.note or "-",
                ]
            )
        )
    return "\n".join(lines) + "\n"


def read_ledger(path: Path = LEDGER) -> list[tuple[int, Reach]]:
    """The committed ledger, parsed back into `(rank, Reach)` pairs in rank order."""
    lines = path.read_text(encoding="utf-8").splitlines()
    if len(lines) < 2 or not lines[0].startswith("# golden-reach ledger") or lines[1] != LEDGER_HEADER:
        fail(f"{path} is not a golden-reach ledger; regenerate it with `just golden-reach-report`")
    out = []
    columns = len(LEDGER_HEADER.split("\t"))
    for number, line in enumerate(lines[2:], start=3):
        fields = line.split("\t")
        if len(fields) != columns:
            fail(f"{path}:{number} has {len(fields)} tab-separated fields, not {columns}; "
                 "regenerate it with `just golden-reach-report`")
        rank, key, region, _us, _ur, _regions, witnesses, outside, sites, note = fields
        parsed = []
        try:
            if sites != "none":
                for entry in sites.split(SITE_SEPARATOR):
                    spec, _, counts = entry.rpartition("=")
                    hit, _, total = counts.partition("/")
                    parsed.append((spec, int(hit), int(total)))
            rank_number = int(rank)
        except ValueError:
            fail(f"{path}:{number} carries a rank or a `site=hit/total` count that is not a number; "
                 "regenerate it with `just golden-reach-report`")
        out.append(
            (
                rank_number,
                Reach(
                    key,
                    region,
                    tuple(w for w in witnesses.split(",") if w != "-"),
                    tuple(o for o in outside.split(",") if o != "-"),
                    tuple(parsed),
                    "" if note == "-" else note,
                ),
            )
        )
    return out


def rewrite_cells(reaches: list[Reach], regions_dir: Path = REGIONS_DIR) -> int:
    """Put each golden row's reach cell in its `crozier sites` column; return rows changed."""
    by_key = {r.key: (rank, r) for rank, r in enumerate(reaches, start=1)}
    changed = 0
    for path in sorted(regions_dir.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        out_lines = []
        for line in text.splitlines(keepends=True):
            cells = region_rows(line)
            if cells and cells[0][3].strip("`") == "golden":
                row = cells[0]
                key = row[0].strip("`")
                cell = reach_cell(by_key[key][1], by_key[key][0], regions_dir)
                if row[5] != cell:
                    row = row[:5] + [cell] + row[6:]
                    newline = "\n" if line.endswith("\n") else ""
                    line = "| " + " | ".join(row) + " |" + newline
                    changed += 1
            out_lines.append(line)
        path.write_text("".join(out_lines), encoding="utf-8")
    return changed


def fixture_test_map(repo_root: Path) -> dict[str, str]:
    """census fixture name -> the golden test comparing its committed golden.

    Read off `tests/e2e.rs` itself: a `const X: Corpus` names its `api`, the test
    that drives `&X` is that fixture's golden test, and a feature target's test is
    the one `feature_target_goldens!` names for its `api`. The census reports a
    corpus by its `CORPUS.md` fixture name, which `corpus_aliases` maps back.
    """
    source = (repo_root / "tests" / "e2e.rs").read_text(encoding="utf-8")
    constants: dict[str, str] = {}
    pending = None
    for line in source.splitlines():
        header = re.match(r"^const (\w+): Corpus = Corpus \{", line)
        if header:
            pending = header.group(1)
            continue
        api = re.match(r'^\s*api: "([^"]+)",', line)
        if api and pending:
            constants[pending] = api.group(1)
            pending = None
    tests: dict[str, str] = {}
    current = None
    for line in source.splitlines():
        fn = re.match(r"^fn (\w+)\(", line)
        if fn:
            current = fn.group(1)
        drive = re.search(r"assert_(?:link_ok_)?corpus_matches\(&(\w+)\)", line)
        if drive and current and GOLDEN_TEST.search(current) and drive.group(1) in constants:
            tests[constants[drive.group(1)]] = current
    for test, api in re.findall(r"^\s*(\w+_matches_fern_output) => \"([^\"]+)\"", source, re.M):
        tests[api] = test
    census = _census_module()
    aliases = census.corpus_aliases(repo_root / "tests" / "fixtures")
    by_fixture = {}
    for api, test in tests.items():
        by_fixture[api] = test
    for fixture, api in aliases.items():
        if api in tests:
            by_fixture[fixture] = tests[api]
    return by_fixture


def _census_module():
    spec = importlib.util.spec_from_file_location(
        "openapi_surface_census", REPO / "scripts" / "openapi-surface-census.py"
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules.setdefault("openapi_surface_census", module)
    spec.loader.exec_module(module)
    return module


def load_coverage(out: Path) -> tuple[dict[str, dict[str, set]], dict[str, set], str]:
    universe_path = out / "universe.json"
    if not universe_path.is_file():
        fail(f"no measurement under {out}; run `just golden-reach` first")
    universe = {
        f: {tuple(r) for r in regions}
        for f, regions in json.loads(universe_path.read_text(encoding="utf-8")).items()
    }
    coverage = {}
    for path in sorted((out / "tests").glob("*.json")):
        coverage[path.stem] = {
            f: {tuple(r) for r in regions}
            for f, regions in json.loads(path.read_text(encoding="utf-8")).items()
        }
    return coverage, universe, measured_commit(out)


def measured_commit(out: Path) -> str:
    """The commit the measurement under `out` was taken at, as `measure` recorded it."""
    path = out / "provenance.json"
    try:
        commit = json.loads(path.read_text(encoding="utf-8"))["commit"]
    except (OSError, ValueError, KeyError, TypeError) as error:
        fail(f"{path} names no measured commit ({error!r}); run `just golden-reach` first")
    if not isinstance(commit, str) or not re.fullmatch(r"[0-9a-f]{7,40}", commit):
        fail(f"{path} records {commit!r}, not a commit; run `just golden-reach` again")
    return commit


def report(args: argparse.Namespace) -> int:
    repo_root: Path = args.repo_root
    census_path = Path(args.census) if args.census else args.out / "census.json"
    if not census_path.is_file():
        fail(f"no census at {census_path}; run `just golden-reach` (it writes one there)")
    census = json.loads(census_path.read_text(encoding="utf-8"))
    coverage, universe, commit = load_coverage(args.out)
    fixture_tests = {f: t for f, t in fixture_test_map(repo_root).items() if t in coverage}
    reaches = compute(
        golden_rows(repo_root / "docs" / "openapi-surface"),
        read_sites_table(repo_root / "docs" / "openapi-surface" / "golden-reach-sites.tsv"),
        census,
        fixture_tests,
        coverage,
        universe,
        repo_root,
    )
    provenance = (
        f"golden-only tier, one scoped run per golden test, measured at commit "
        f"{commit[:12]} over {len(coverage)} golden tests"
    )
    if args.write:
        (repo_root / "docs" / "openapi-surface" / "golden-reach.tsv").write_text(
            ledger_text(reaches, provenance), encoding="utf-8"
        )
        changed = rewrite_cells(reaches, repo_root / "docs" / "openapi-surface")
        print(f"golden-reach: wrote the ledger and {changed} reach cell(s)")
    else:
        sys.stdout.write(ledger_text(reaches, provenance))
    return 0


def sites(args: argparse.Namespace) -> int:
    table = read_sites_table(
        args.table or args.repo_root / "docs" / "openapi-surface" / "golden-reach-sites.tsv"
    )
    if args.census:
        census = json.loads(Path(args.census).read_text(encoding="utf-8"))
        for row in table.values():
            if not census_witnesses(census, row.selectors):
                fail(f"{row.key}: no registered source declares any of {', '.join(row.selectors)}; correct its selectors in {SITES_TABLE.name}, or re-run `just golden-reach` if the census is stale")
    seen = set()
    for row in table.values():
        for spec in row.sites:
            if spec in seen:
                continue
            seen.add(spec)
            site = resolve_site(spec, args.repo_root)
            if args.verbose:
                print(f"{spec}\t{site.file}:{site.start}:{site.start_col}-{site.end}:{site.end_col}")
    print(f"golden-reach: {len(seen)} site(s) across {len(table)} row(s) resolve")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("--repo-root", type=Path, default=REPO)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    sub = parser.add_subparsers(dest="command", required=True)
    m = sub.add_parser("measure", help="one instrumented run per golden test")
    m.add_argument("--jobs", type=int, default=4)
    m.add_argument("--tests", help="regex restricting the golden tests measured")
    r = sub.add_parser("report", help="join census, sites and coverage into the ledger")
    r.add_argument("--census", help="`just surface-census --json` output (default: OUT/census.json)")
    r.add_argument("--write", action="store_true", help="write the ledger and reach cells")
    s = sub.add_parser("sites", help="resolve every declared site against src/")
    s.add_argument("--verbose", action="store_true")
    s.add_argument("--table", type=Path, help="a site table other than the committed one")
    s.add_argument("--census", help="also check every selector against this census output")
    args = parser.parse_args(argv)
    return {"measure": measure, "report": report, "sites": sites}[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
