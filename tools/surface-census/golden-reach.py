#!/usr/bin/env python3
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
reports about those sites is measured, never read off the source. Each test's
executed regions persist in the store `reach_store.py` documents, so `measure
--incremental` (and `just census-repin`, which every stale-table failure names)
re-runs only the tests whose base entry executed changed code. `just
golden-reach` is the full measurement; `just golden-reach-report` re-joins an
existing measurement after the site table changes.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import csv
import fnmatch
import importlib.util
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib
import types
from collections import Counter, defaultdict
from enum import StrEnum
from pathlib import Path
from typing import IO, Any, NamedTuple, NoReturn

REPO = Path(__file__).resolve().parents[2]
REGIONS_DIR = REPO / "docs" / "openapi-surface"
SITES_TABLE = REGIONS_DIR / "golden-reach-sites.tsv"
LEDGER = REGIONS_DIR / "golden-reach.tsv"
DEFAULT_OUT = REPO / ".local" / "golden-reach"
# What a native binary's file name ends in: the llvm tools and cargo's outputs carry it.
EXE = ".exe" if os.name == "nt" else ""
CELL_PREFIX = "reach:"
# A site spec may hold a comma inside its `[regex]`, so the ledger separates
# sites with a string no spec may contain.
SITE_SEPARATOR = " ; "


def _report_module():
    spec = importlib.util.spec_from_file_location(
        "fixtures_coverage_report", REPO / "tools" / "surface-census" / "fixtures-coverage-report.py"
    )
    if spec is None or spec.loader is None:
        raise SystemExit(
            "golden-reach: cannot load tools/surface-census/fixtures-coverage-report.py; restore it from git"
        )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


REPORT = _report_module()


def fail(message: str) -> NoReturn:
    raise SystemExit(f"golden-reach: {message}")


def _output_insensitive_module():
    spec = importlib.util.spec_from_file_location(
        "output_insensitive", REPO / "tools/surface-census/output-insensitive.py"
    )
    if spec is None or spec.loader is None:
        fail("cannot load output-insensitive.py; restore it from git")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _region_keys_module():
    spec = importlib.util.spec_from_file_location(
        "golden_reach_region_keys", REPO / "tools" / "surface-census" / "witness-search-region-keys.py"
    )
    if spec is None or spec.loader is None:
        raise SystemExit(
            "golden-reach: cannot load tools/surface-census/witness-search-region-keys.py; restore it from git"
        )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# The one parse of a region file's entry rows, and the categories it admits.
region_rows = _region_keys_module().region_rows


COMBINATION_PREFIX = "combo-"
# The site cell of a combination row no measured crozier branch joins both features
# of: no condition reads both, or one does but no counter region's execution implies
# both hold. `combination-cooccurrence.tsv` audits which functions handle each feature
# and why. Admitted on a combination row alone.
COOCCURRENCE = "co-occurrence"


def golden_rows(regions_dir: Path = REGIONS_DIR) -> dict[str, str]:
    """`golden` row key -> the region file stem that owns it."""
    out = {}
    for path in sorted(regions_dir.glob("*.md")):
        for cells in region_rows(path.read_text(encoding="utf-8")):
            if cells[3].strip("`") == "golden":
                out[cells[0].strip("`")] = path.stem
    return out


def measured_rows(regions_dir: Path = REGIONS_DIR, listed: set[str] | frozenset[str] = frozenset()) -> dict[str, str]:
    """The rows the ledger measures: every `golden` row, and every `gap` combination row in `listed`.

    A combination whose interaction branch no golden-only witness executes is `gap`,
    and its ledger row is the measurement its named reason restates, so it stays
    measured while the site table declares its interaction sites.
    """
    out = golden_rows(regions_dir)
    for path in sorted(regions_dir.glob("*.md")):
        for cells in region_rows(path.read_text(encoding="utf-8")):
            key = cells[0].strip("`")
            if key.startswith(COMBINATION_PREFIX) and key in listed and cells[3].strip("`") == "gap":
                out[key] = path.stem
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
    # A combination row whose cell is `co-occurrence`: no interaction branch to measure.
    cooccurrence: bool = False


def read_sites_table(path: Path = SITES_TABLE) -> dict[str, SiteRow]:
    """`key -> (selectors, site specs, note)` from the tab-separated declaration table."""
    if not path.is_file():
        fail(
            f"{path} is missing; it declares every golden row's selectors and sites — restore it from git (`git checkout -- {path}`)"
        )
    lines = path.read_text(encoding="utf-8").splitlines()
    header = ["key", "selectors", "sites", "note"]
    if not lines or lines[0].split("\t") != header:
        fail(f"{path} must start with the header {'<TAB>'.join(header)}; restore that first line")
    rows: dict[str, SiteRow] = {}
    for number, line in enumerate(lines[1:], start=2):
        fields = line.split("\t")
        if len(fields) != 4:
            fail(
                f"{path}:{number} has {len(fields)} fields, not 4; give it `key`, `selectors`, `sites` and `note`, tab-separated, as the header names them"
            )
        key, selectors, sites, note = fields
        if key in rows:
            fail(f"{path}:{number} declares {key} twice; merge the two rows' sites into one row")
        selector_list = tuple(s.strip() for s in selectors.split(",") if s.strip())
        if not selector_list:
            fail(
                f"{path}:{number} ({key}) names no census selector; give it the selector(s) its region row's census cell names, comma-separated"
            )
        cooccurrence = sites.strip() == COOCCURRENCE
        if cooccurrence and not key.startswith(COMBINATION_PREFIX):
            fail(
                f"{path}:{number} ({key}) reads `{COOCCURRENCE}`, which only a combination row may; "
                "name the sites that handle the feature, or `none`"
            )
        site_list = (
            ()
            if sites.strip() in ("none", COOCCURRENCE)
            else tuple(s.strip() for s in _split_sites(sites) if s.strip())
        )
        if not site_list and sites.strip() not in ("none", COOCCURRENCE):
            fail(f"{path}:{number} ({key}) names no site; write `none` for a feature crozier reads nowhere")
        rows[key] = SiteRow(key, selector_list, site_list, note.strip(), cooccurrence)
    return rows


COOCCURRENCE_AUDIT = REGIONS_DIR / "combination-cooccurrence.tsv"


class CooccurrenceAudit(NamedTuple):
    """One `combination-cooccurrence.tsv` row, its cells in column order."""

    key: str
    witness: str
    site: str
    handlers: str
    why_no_branch: str


# The file's header is the model's fields, so the two cannot drift apart.
COOCCURRENCE_COLUMNS = CooccurrenceAudit._fields


def read_cooccurrence(path: Path = COOCCURRENCE_AUDIT) -> tuple[dict[str, CooccurrenceAudit], list[str]]:
    """`combination-cooccurrence.tsv` as `key -> row`, and every way its form is broken.

    One row per `co-occurrence` combination, sorted by key, every cell filled: the
    witness declaring the combination, the JSON Pointer where both features occur in
    its committed document, each feature's handling functions and why no measured
    branch in them joins both.
    """
    if not path.is_file():
        return {}, [f"{path.name}: missing — restore it from git"]
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or tuple(lines[0].split("\t")) != COOCCURRENCE_COLUMNS:
        return {}, [f"{path.name}: the header line must be exactly {'<TAB>'.join(COOCCURRENCE_COLUMNS)}"]
    rows: dict[str, CooccurrenceAudit] = {}
    failures = []
    keys = []
    for number, line in enumerate(lines[1:], start=2):
        cells = line.split("\t")
        keys.append(cells[0])
        if len(cells) != len(COOCCURRENCE_COLUMNS) or not all(cell.strip() for cell in cells):
            failures.append(f"{cells[0] or f'line {number}'}: {path.name} line {number} has an empty or missing cell")
            continue
        if cells[0] in rows:
            failures.append(f"{cells[0]}: {path.name} audits it twice")
        try:
            handler_specs(cells[3])
        except ValueError as error:
            failures.append(f"{cells[0]}: {path.name}'s handlers cell {error}")
            continue
        rows[cells[0]] = CooccurrenceAudit(*cells)
    if keys != sorted(keys):
        failures.append(f"{path.name}: rows are not sorted by key")
    return rows, failures


HANDLER_SPEC = re.compile(r"src/[\w/]+\.rs::\w+(?:::\w+)*")


def handler_specs(cell: str) -> list[str]:
    """The function specs a `handlers` cell names: `<feature>: src/x.rs::f, … ; <feature>: …`.

    Raises ValueError unless the cell names at least two distinct features, each with a
    non-empty list of `src/<file>.rs::<function>` specs.
    """
    specs: list[str] = []
    groups = cell.split(" ; ")
    if len(groups) < 2:
        raise ValueError(f"`{cell}` names fewer than two features; write `<feature>: src/x.rs::f ; <feature>: …`")
    features = [group.partition(": ")[0].strip() for group in groups]
    if len(set(features)) != len(features):
        raise ValueError(f"`{cell}` names a feature twice; give each feature one group of its own handlers")
    for group in groups:
        feature, separator, names = group.partition(": ")
        listed = [name.strip() for name in names.split(",")]
        if not separator or not feature.strip() or not all(HANDLER_SPEC.fullmatch(name) for name in listed):
            raise ValueError(
                f"group `{group}` is not `<feature>: src/x.rs::f, src/y.rs::g`; name each feature's handling functions"
            )
        specs += [name for name in listed if name not in specs]
    return specs


def measured_table(table: dict[str, SiteRow], regions_dir: Path = REGIONS_DIR) -> dict[str, SiteRow]:
    """The site-table rows this ledger measures: a `handwritten` combination's interaction
    sites are `just handwritten-reach`'s to measure, over its fixture, so its row is set aside."""
    handwritten = {
        cells[0].strip("`")
        for path in sorted(regions_dir.glob("*.md"))
        for cells in region_rows(path.read_text(encoding="utf-8"))
        if cells[0].strip("`").startswith(COMBINATION_PREFIX) and cells[3].strip("`") == "handwritten"
    }
    return {key: row for key, row in table.items() if key not in handwritten}


def combination_site_failures(table: dict[str, SiteRow]) -> list[str]:
    """A combination row's sites cell: `co-occurrence`, or interaction branches only.

    An interaction branch is an arm-form site (`src/<file>.rs::<fn>[<regex>]`), the
    branch whose condition reads both features. A whole function, or `none`, says
    nothing about where the two features meet, so it is refused, naming the key.
    """
    failures = []
    for key, row in sorted(table.items()):
        if not key.startswith(COMBINATION_PREFIX) or row.cooccurrence:
            continue
        if not row.sites:
            failures.append(
                f"{key}: a combination row's sites cell is `none`; name its interaction branch as "
                f"`src/<file>.rs::<fn>[<regex>]`, or write `{COOCCURRENCE}` and audit it in "
                "combination-cooccurrence.tsv"
            )
        for spec in row.sites:
            match = _SITE.match(spec)
            if match is None or match.group("arm") is None:
                failures.append(
                    f"{key}: `{spec}` names a whole function, not the branch where the combination's "
                    "features meet; narrow it to that arm with `[<regex>]`"
                )
    return failures


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
    impl = re.compile(
        r"^(?:impl(?:<[^>]*>)?\s+(?:[A-Za-z_][A-Za-z0-9_<>, ]*\s+for\s+)?(?P<type>[A-Za-z_][A-Za-z0-9_]*))"
    )
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
            fail(
                f"cannot bound the body of `fn {name}` at line {index + 1}; check its braces balance (`cargo check`), or name a different site in {SITES_TABLE.name} (`{REPIN}` re-anchors one whose code only moved)"
            )
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
        fail(
            f"site {spec!r} contains {SITE_SEPARATOR!r}, which separates sites in the ledger; "
            f"rewrite its regex in {SITES_TABLE.name} without that sequence (`\\s*;\\s*` matches it)"
        )
    if "|" in spec:
        # The spec is quoted in a markdown table cell, where a pipe — escaped or
        # not — splits the row for any reader that does not unescape it first.
        fail(f"site {spec!r} contains `|`; write `\\x7c` for a literal pipe in its regex")
    if not match:
        fail(
            f"site {spec!r} is not `src/<file>.rs::<fn>`, `::<Type>::<fn>`, or either with `[<regex>]`; "
            f"rewrite it in {SITES_TABLE.name} in one of those forms"
        )
    path = repo_root / match.group("file")
    if not path.is_file():
        fail(f"site {spec!r} names {match.group('file')}, which does not exist; correct its path in {SITES_TABLE.name}")
    lines = path.read_text(encoding="utf-8").splitlines()
    spans = _function_spans(lines, match.group("item"))
    if len(spans) != 1:
        fail(
            f"site {spec!r} matches {len(spans)} functions; run `{REPIN}` if its code only moved, else name "
            "exactly one (qualify a method as `Type::name`)"
        )
    start, end = spans[0]
    arm = match.group("arm")
    if arm is None:
        return Site(spec, match.group("file"), start, end)
    line_only = arm.startswith("=")
    pattern = re.compile(arm[1:] if line_only else arm)
    hits = [n for n in range(start, end + 1) if pattern.search(lines[n - 1])]
    if len(hits) != 1:
        fail(
            f"site {spec!r}: the arm regex matches {len(hits)} lines of its function, not 1; run `{REPIN}`, "
            f"which re-anchors a site whose code only moved, else anchor it (`^`, a leading-space count, more of "
            f"the line) in {SITES_TABLE.name} until one line matches"
        )
    first = hits[0]
    if line_only:
        found = pattern.search(lines[first - 1])
        # `hits` holds only the lines the pattern matches.
        assert found is not None
        column = found.start() + 1
        return Site(spec, match.group("file"), first, first, column, 1 << 30)
    opening = _opening_line(lines, first, end)
    if opening is None:
        fail(
            f"site {spec!r}: no brace block opens on line {first} or within the "
            f"next {_CONDITION_LINES} lines; run `{REPIN}` if rustfmt moved it, else use `[=regex]` for a one-line arm"
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
        fail(
            f"site {spec!r}: cannot bound the block opened on line {opening}; run `{REPIN}` if its code only moved, else anchor the arm regex on a line that opens a balanced block, or use `[=regex]` for a one-line arm"
        )
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
    sysroot = subprocess.run(["rustc", "--print", "sysroot"], check=True, capture_output=True, text=True).stdout.strip()
    host = next(
        line.split(":", 1)[1].strip()
        for line in subprocess.run(["rustc", "-vV"], check=True, capture_output=True, text=True).stdout.splitlines()
        if line.startswith("host:")
    )
    tool = Path(sysroot) / "lib" / "rustlib" / host / "bin" / f"{name}{EXE}"
    if not tool.is_file():
        fail(f"{tool} is missing — run `rustup component add llvm-tools-preview` (`just bootstrap`)")
    return str(tool)


def tool_name(path: str) -> str:
    """The tool a path runs, as a message names it on every platform: no `.exe`."""
    name = re.split(r"[\\/]", path)[-1]
    return name[: -len(".exe")] if name.lower().endswith(".exe") else name


def run_llvm(argv: list[str], stdout: IO[str] | None = None) -> None:
    """Run an llvm-profdata/llvm-cov step, failing with its stderr and the fix."""
    run = subprocess.run(argv, stdout=stdout, stderr=subprocess.PIPE, text=True)
    if run.returncode != 0:
        fail(
            f"`{tool_name(argv[0])} {argv[1]}` exited {run.returncode}: {run.stderr.strip()[-400:]} — "
            f"the profiles and the instrumented binaries disagree; rebuild them with "
            f"`{REPIN}` and retry"
        )


def _instrumented_binaries(repo_root: Path) -> tuple[Path, Path]:
    deps = repo_root / "target" / "llvm-cov-target" / "debug" / "deps"
    candidates = [p for p in deps.glob("e2e-*") if p.is_file() and os.access(p, os.X_OK) and p.suffix == EXE]
    if not candidates:
        fail(f"no instrumented e2e binary under {deps} — run `{REPIN}`, which builds it")
    e2e = max(candidates, key=lambda p: p.stat().st_mtime)
    crozier = repo_root / "target" / "llvm-cov-target" / "debug" / f"crozier{EXE}"
    if not crozier.is_file():
        fail(f"no instrumented crozier binary at {crozier} — run `{REPIN}`, which builds it")
    return e2e, crozier


def _covered(export: Path, repo_root: Path) -> tuple[dict[str, list[list[int]]], dict[str, list[list[int]]]]:
    """(every production region, the executed ones) per `src/` file of one export."""
    tier = {"t": REPORT.load_tier(export, repo_root)}
    REPORT.drop_test_regions(tier, repo_root)
    universe = {f: sorted(list(r) for r in counts) for f, counts in tier["t"].items()}
    hit = {f: sorted(list(r) for r, n in counts.items() if n > 0) for f, counts in tier["t"].items()}
    return universe, {f: v for f, v in hit.items() if v}


def golden_test_cwd(repo_root: Path) -> Path:
    """Where a golden test runs: the e2e crate's directory, as cargo runs it.

    From the root, the crozier a golden spawns runs `ruff format` under the
    tooling's own `[tool.ruff]`, whose `templates` exclude leaves a generated
    `templates/` package unformatted and fails its golden.
    """
    return repo_root / "crates" / "crozier-e2e"


def run_golden_test(
    e2e: list[str], test: str, repo_root: Path, env: dict[str, str]
) -> subprocess.CompletedProcess[str]:
    """Run one golden test alone through the e2e binary `e2e`, from [`golden_test_cwd`]."""
    return subprocess.run(
        [*e2e, "--exact", test, "--test-threads", "1", "--quiet"],
        cwd=golden_test_cwd(repo_root),
        capture_output=True,
        text=True,
        env=env,
    )


def uncommitted_changes(repo_root: Path) -> list[str]:
    """Tracked paths that differ from `HEAD` — what a measurement stamped with
    `HEAD` would silently include."""
    status = subprocess.run(
        ["git", "status", "--porcelain", "--untracked-files=no"],
        cwd=repo_root,
        capture_output=True,
        text=True,
    )
    if status.returncode != 0:
        fail(
            f"git status exited {status.returncode}: {status.stderr.strip()[-400:]} — "
            "run `just golden-reach` from inside this repository's checkout"
        )
    return [line[3:] for line in status.stdout.splitlines() if line.strip()]


def _sibling(name: str) -> Any:
    """A module of this directory by file name, registered so its dataclasses resolve."""
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, Path(__file__).resolve().parent / f"{name}.py")
    if spec is None or spec.loader is None:
        fail(f"cannot load tools/surface-census/{name}.py; restore it from git")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


RS = _sibling("reach_store")
STORE_FILE = "store.json.gz"
REPIN = RS.REPIN


def instrumented_build(repo_root: Path) -> tuple[Path, Path]:
    """Build the instrumented e2e suite and crozier every measurement runs; return both binaries."""
    if shutil.which("cargo") is None:
        fail("cargo is not on PATH; install the pinned toolchain with `just bootstrap`")
    build = subprocess.run(
        [
            "cargo",
            "llvm-cov",
            "--locked",
            "--no-report",
            "nextest",
            "--workspace",
            "-E",
            "binary(e2e) and test(=every_feature_target_has_its_own_golden_test)",
        ],
        cwd=repo_root,
        capture_output=True,
        text=True,
    )
    if build.returncode != 0:
        sys.stderr.write(build.stdout[-4000:] + build.stderr[-4000:])
        fail(f"the instrumented build failed (its output is above); fix what it names and re-run `{REPIN}`")
    return _instrumented_binaries(repo_root)


def golden_population(repo_root: Path) -> dict[str, Any]:
    """Every golden test the e2e suite registers -> its inputs (fixture directory, source names)."""
    census = _census_module()
    registrations = census.golden_registrations(repo_root / census.GOLDEN_REGISTRY)
    names: dict[str, set[str]] = defaultdict(set)
    for name, api in census.corpus_aliases(repo_root / "tests" / "fixtures").items():
        names[api].add(name)
    return {
        registration.test: RS.Inputs(registration.test, api, frozenset({api} | names[api]))
        for api, registration in registrations.items()
    }


def golden_constants(repo_root: Path) -> dict[str, str]:
    """`Corpus` constant -> the golden test that drives it, read off the e2e suite."""
    census = _census_module()
    source = (repo_root / census.GOLDEN_REGISTRY).read_text(encoding="utf-8")
    by_api = {api: r.test for api, r in census.golden_registrations(repo_root / census.GOLDEN_REGISTRY).items()}
    return {
        constant: by_api[api]
        for constant, api in re.findall(r'^const (\w+): Corpus = Corpus \{\s*api: "([^"]+)"', source, re.M)
        if api in by_api
    }


def _export_regions(
    profiles: list[Path], scratch: Path, objects: list[Path], profdata: str, llvm_cov: str, repo_root: Path
) -> tuple[dict[str, list[list[int]]], dict[str, list[list[int]]]]:
    merged = scratch / "merged.profdata"
    run_llvm([profdata, "merge", "-sparse", *map(str, profiles), "-o", str(merged)])
    export = scratch / "export.json"
    extra = [argument for path in objects[1:] for argument in ("-object", str(path))]
    with export.open("w", encoding="utf-8") as sink:
        run_llvm([llvm_cov, "export", "-format=text", f"-instr-profile={merged}", str(objects[0]), *extra], stdout=sink)
    return _covered(export, repo_root)


def universe_regions(e2e: Path, crozier: Path, repo_root: Path, profdata: str, llvm_cov: str) -> dict:
    """Every production counter region the two instrumented binaries carry, executed or not."""
    with tempfile.TemporaryDirectory(prefix="golden-reach-universe-") as scratch:
        raw = Path(scratch)
        env = dict(os.environ, LLVM_PROFILE_FILE=str(raw / "%p-%m.profraw"))
        subprocess.run([str(e2e), "--list"], cwd=golden_test_cwd(repo_root), capture_output=True, env=env)
        subprocess.run([str(crozier), "--version"], cwd=repo_root, capture_output=True, env=env)
        profiles = sorted(raw.glob("*.profraw"))
        if not profiles:
            fail(f"the instrumented binaries wrote no profile; rebuild them with `{REPIN}`")
        universe, _hit = _export_regions(profiles, raw, [crozier, e2e], profdata, llvm_cov, repo_root)
    return universe


class Step(NamedTuple):
    """What one measurement step did."""

    store: dict[str, Any]
    base: str | None
    full: str | None
    tests_run: tuple[str, ...]
    tests_carried: tuple[str, ...]
    fixtures_run: tuple[str, ...]
    fixtures_carried: tuple[str, ...]
    reasons: dict[str, str]


def measure_step(
    repo_root: Path,
    *,
    base: dict[str, Any] | None,
    full_reason: str = "",
    forced_tests: frozenset[str] = frozenset(),
    forced_fixtures: frozenset[str] = frozenset(),
    select_tests: re.Pattern[str] | None = None,
    select_fixtures: re.Pattern[str] | None = None,
    include_tests: bool = True,
    include_fixtures: bool = True,
    plan_fixtures: bool = True,
    handwritten_dir: Path | None = None,
    jobs: int = 1,
) -> Step:
    """One step of the store from `base` to the tree at `repo_root`'s HEAD.

    No base measures every selected test and fixture. Otherwise `reach_store.plan`
    decides what re-runs, and every other entry is carried, translated to HEAD's
    universe. A test or fixture left out (`include_*`) is carried only where the
    carry rule allows, and dropped where it does not: nothing is carried for a
    test that executed changed code.
    """
    handwritten = _load_handwritten_module()
    head = RS.git(repo_root, "rev-parse", "HEAD").strip()
    tree = RS.read_tree(repo_root)
    versions = RS.toolchain(repo_root)
    population = golden_population(repo_root)
    if select_tests is not None:
        population = {name: inputs for name, inputs in population.items() if select_tests.search(name)}
    fixture_base = handwritten_dir or repo_root / "docs" / "openapi-surface" / "handwritten"
    # Fixtures left out and none forced are never planned: a tree whose hand-written
    # evidence does not plan (an older commit's) still measures its golden tests.
    fixtures = handwritten.measured_fixtures(repo_root, fixture_base) if include_fixtures or forced_fixtures else {}
    if select_fixtures is not None:
        fixtures = {name: audiences for name, audiences in fixtures.items() if select_fixtures.search(name)}
    if base is None:
        plan = RS.Plan(full_reason or "no base", frozenset(population), frozenset(fixtures), (), {})
    else:
        plan = RS.plan(repo_root, base, tree, population, fixtures, golden_constants(repo_root), versions)
    carry = base is not None and plan.full is None
    run_tests = (set(plan.tests) if include_tests else set()) | (forced_tests & set(population))
    run_fixtures = (set(plan.fixtures) if include_fixtures else set()) | (forced_fixtures & set(fixtures))
    built = bool(run_tests or run_fixtures or not carry or plan.changed)
    binaries: tuple[Path, Path] | None = None
    if built:
        binaries = instrumented_build(repo_root)
        profdata, llvm_cov = _llvm_tool("llvm-profdata"), _llvm_tool("llvm-cov")
        universe = universe_regions(*binaries, repo_root, profdata, llvm_cov)
        functions = RS.universe_table(tree, universe)
    else:
        assert base is not None
        table = tree.table()
        functions = {key: {**table[key], "regions": base["functions"][key]["regions"]} for key in table}
    tests: dict[str, Any] = {}
    fixture_entries: dict[str, Any] = {}
    if carry:
        assert base is not None
        for name, entry in base["tests"].items():
            if name not in population or name in run_tests or name in plan.tests:
                continue
            moved = RS.remap(entry["regions"], base["functions"], functions)
            if moved is None:
                run_tests.add(name) if include_tests else None
                continue
            tests[name] = {"commit": entry["commit"], "regions": moved}
        for name, entry in base["fixtures"].items():
            if name not in fixtures or name in run_fixtures or name in plan.fixtures:
                continue
            moved = RS.remap(entry["regions"], base["functions"], functions)
            control = RS.remap(entry.get("control", {}), base["functions"], functions)
            if moved is None or control is None:
                run_fixtures.add(name) if include_fixtures else None
                continue
            fixture_entries[name] = {"commit": entry["commit"], "regions": moved}
            if "control" in entry:
                fixture_entries[name]["control"] = control
    if (run_tests or run_fixtures) and binaries is None:
        binaries = instrumented_build(repo_root)
    if run_tests or run_fixtures:
        assert binaries is not None
        e2e, crozier = binaries
        profdata, llvm_cov = _llvm_tool("llvm-profdata"), _llvm_tool("llvm-cov")
        if run_tests:
            listed = _listed_golden_tests(e2e, repo_root)
            unknown = sorted(run_tests - set(listed))
            if unknown:
                fail(f"the e2e suite registers {unknown[:3]} but its binary lists no such test; rebuild with `{REPIN}`")
        env = dict(os.environ, CROZIER_REQUIRE_CORPUS="1")

        def one(test: str) -> tuple[str, dict | None, str | None]:
            with tempfile.TemporaryDirectory(prefix="golden-reach-") as scratch:
                raw = Path(scratch)
                run = run_golden_test(
                    [str(e2e)], test, repo_root, dict(env, LLVM_PROFILE_FILE=str(raw / "%p-%m.profraw"))
                )
                if run.returncode != 0:
                    return test, None, (run.stdout + run.stderr)[-3000:]
                _universe, hit = _export_regions(
                    sorted(raw.glob("*.profraw")), raw, [crozier, e2e], profdata, llvm_cov, repo_root
                )
            return test, hit, None

        failures = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=jobs) as pool:
            for done, (test, hit, error) in enumerate(pool.map(one, sorted(run_tests)), start=1):
                if done % 25 == 0 and done < len(run_tests):
                    print(f"golden-reach: ran {done} of {len(run_tests)} golden test(s)", file=sys.stderr, flush=True)
                if error is not None or hit is None:
                    failures.append((test, error))
                    continue
                tests[test] = {"commit": head, "regions": RS.entry_regions(tree, functions, hit)}
        for test, error in failures:
            sys.stderr.write(f"--- {test} ---\n{error}\n")
        if failures:
            fail(
                f"{len(failures)} golden test(s) failed under instrumentation; a failing "
                f"golden measures nothing. Fix them (`just test-corpus-match`) and re-run `{REPIN}`."
            )
        tools = types.SimpleNamespace(run_llvm=run_llvm, _covered=_covered)
        for name in sorted(run_fixtures):
            spec, audiences = fixture_base / name / "openapi.yml", fixtures[name]
            _universe, hit = handwritten.scoped_run(spec, audiences, crozier, profdata, llvm_cov, repo_root, tools)
            entry = {"commit": head, "regions": RS.entry_regions(tree, functions, hit)}
            if audiences:
                _universe, control = handwritten.scoped_run(spec, (), crozier, profdata, llvm_cov, repo_root, tools)
                entry["control"] = RS.entry_regions(tree, functions, control)
            fixture_entries[name] = entry
    store = {
        "schema": RS.SCHEMA,
        "commit": head,
        "rustc": versions[0],
        "llvm": versions[1],
        "full_at": base["full_at"] if carry and base is not None else head,
        "steps_since_full": base["steps_since_full"] + 1 if carry and base is not None else 0,
        "measured_at": RS.now_iso(),
        "tests": dict(sorted(tests.items())),
        "fixtures": dict(sorted(fixture_entries.items())),
        "functions": functions,
    }
    return Step(
        store,
        base["commit"] if base is not None else None,
        None if carry else plan.full or full_reason or "no base",
        tuple(sorted(run_tests)),
        tuple(sorted(set(tests) - run_tests)),
        tuple(sorted(run_fixtures)),
        tuple(sorted(set(fixture_entries) - run_fixtures)),
        dict(plan.reasons),
    )


def _listed_golden_tests(e2e: Path, repo_root: Path) -> list[str]:
    listed = subprocess.run([str(e2e), "--list", "--format", "terse"], cwd=repo_root, capture_output=True, text=True)
    if listed.returncode != 0:
        fail(f"{e2e} --list exited {listed.returncode}: {listed.stderr.strip()[-400:]} — rebuild it with `{REPIN}`")
    golden_test = _census_module().GOLDEN_TEST
    return sorted(
        line.rsplit(": test", 1)[0]
        for line in listed.stdout.splitlines()
        if line.endswith(": test") and golden_test.search(line)
    )


def write_views(step: Step, out: Path, repo_root: Path) -> None:
    """Save the store, and the per-test absolute view `report` and the arm search read, at HEAD."""
    store = step.store
    RS.save(store, out / STORE_FILE)
    tree = RS.read_tree(repo_root)
    (out / "tests").mkdir(parents=True, exist_ok=True)
    for stale in (out / "tests").glob("*.json"):
        stale.unlink()
    universe = RS.positions(tree, store["functions"])
    (out / "universe.json").write_text(
        json.dumps({f: sorted(map(list, r)) for f, r in sorted(universe.items())}), encoding="utf-8"
    )
    for name, entry in store["tests"].items():
        hit = RS.positions(tree, store["functions"], entry["regions"])
        (out / "tests" / f"{name}.json").write_text(
            json.dumps({f: sorted(map(list, r)) for f, r in sorted(hit.items())}), encoding="utf-8"
        )
    (out / "provenance.json").write_text(
        json.dumps(
            {
                "commit": store["commit"],
                "tests": len(store["tests"]),
                "base": step.base,
                "full": step.full,
                "run": len(step.tests_run),
                "carried": len(step.tests_carried),
            }
        ),
        encoding="utf-8",
    )


def local_store(out: Path) -> dict[str, Any] | None:
    """The store this checkout's last measurement left, or None (a refused one is reported, then ignored)."""
    path = out / STORE_FILE
    if not path.is_file():
        return None
    try:
        return RS.load(path)
    except RS.StoreError as error:
        print(f"golden-reach: ignoring {path}: {error}", file=sys.stderr)
        return None


def describe(step: Step) -> str:
    """The one line a step reports: what ran, what was carried, and from which base."""
    origin = (
        f"full measurement ({step.full})" if step.full else f"from the base at {step.base[:12] if step.base else '?'}"
    )
    return (
        f"{len(step.tests_run)} test(s) run, {len(step.tests_carried)} carried; "
        f"{len(step.fixtures_run)} fixture(s) run, {len(step.fixtures_carried)} carried; {origin}"
    )


def measure(args: argparse.Namespace) -> int:
    """`measure`: full by default, `--tests` re-runs a subset into the store, `--incremental` steps from a base."""
    repo_root: Path = args.repo_root
    selected: re.Pattern[str] | None = None
    if args.tests:
        try:
            selected = re.compile(args.tests)
        except re.error as error:
            fail(f"--tests {args.tests!r} is not a regex ({error}); pass a Python regex over golden test names")
    out: Path = args.out
    # The ledger names the commit it was measured at, so the measured tree must
    # be that commit's: a merge measured before it is committed would stamp its
    # first parent.
    dirty = uncommitted_changes(repo_root)
    if dirty:
        fail(
            f"{len(dirty)} tracked file(s) differ from HEAD ({', '.join(dirty[:5])}); "
            "commit them first so the ledger's measured commit is the tree measured"
        )
    with RS.instrumented_lock("golden-reach measure"):
        if args.incremental:
            choice = _sibling("reach_base").find(repo_root)
            print(f"golden-reach: base: {choice.reason}", file=sys.stderr)
            step = measure_step(
                repo_root,
                base=choice.store,
                full_reason=choice.reason,
                plan_fixtures=not args.golden_only,
                jobs=args.jobs,
            )
        elif selected is not None:
            base = local_store(out)
            population = golden_population(repo_root)
            forced = frozenset(name for name in population if selected.search(name))
            if not forced:
                fail(
                    "no golden test is selected — check the --tests regex against "
                    "`cargo nextest list -E 'binary(e2e)'`, or register the corpus's "
                    "`*_matches_fern_output` test in crates/crozier-e2e/tests/e2e.rs"
                )
            step = measure_step(
                repo_root,
                base=base,
                full_reason="no store to merge into",
                forced_tests=forced,
                select_tests=None if base is not None else selected,
                include_tests=base is None,
                include_fixtures=False,
                jobs=args.jobs,
            )
        else:
            step = measure_step(
                repo_root,
                base=None,
                full_reason="a full measurement was asked for",
                plan_fixtures=not args.golden_only,
                jobs=args.jobs,
            )
    write_views(step, out, repo_root)
    _sibling("reach_base").publish(step.store)
    print(f"golden-reach: measured into {out}: {describe(step)}")
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
                fail(
                    f"`{pattern}` names no registered source; correct the `fixture=` selector in {SITES_TABLE.name} to a CORPUS.md name"
                )
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
    # A `co-occurrence` combination: its features meet in no crozier branch.
    cooccurrence: bool = False

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
            f"region files' `golden` rows and the `gap` combination rows it measures"
        )
    misdeclared = combination_site_failures(table)
    if misdeclared:
        fail("; ".join(misdeclared))
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
                fail(
                    f"site {spec} spans no production counter region; it handles nothing measurable. Run `{REPIN}` if src/ moved since the measurement, else point it at the arm that handles the feature"
                )
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
        out.append(Reach(key, region, witnesses, outside, tuple(sites), declared.note, declared.cooccurrence))
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
    cell is never edited by hand: run `just census-repin`. A
    row whose unreached arm has been searched for links its record, which sits at
    `golden-reach-witnesses/searches/<key>.md` beside the region files.
    """
    note = f"; not counted: {reach.note}" if reach.note else ""
    record = (regions_dir or REGIONS_DIR) / SEARCHES / f"{reach.key}.md"
    if record.is_file():
        note += f"; arm search [record]({SEARCHES}/{reach.key}.md)"
    if reach.cooccurrence:
        return (
            f"{CELL_PREFIX} {COOCCURRENCE} — no measured crozier branch joins both features, as "
            f"[the co-occurrence audit](combination-cooccurrence.tsv) records; {_witness_phrase(reach)}{note} "
            f"([ledger](golden-reach.tsv) rank {rank})"
        )
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


LEDGER_HEADER = "rank\tkey\tregion\tunreached_sites\tunreached_regions\tregions\twitnesses\toutside\tsites\tnote"


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
                    COOCCURRENCE
                    if reach.cooccurrence
                    else SITE_SEPARATOR.join(f"{spec}={hit}/{total}" for spec, hit, total in reach.sites) or "none",
                    reach.note or "-",
                ]
            )
        )
    return "\n".join(lines) + "\n"


def read_ledger(path: Path = LEDGER) -> list[tuple[int, Reach]]:
    """The committed ledger, parsed back into `(rank, Reach)` pairs in rank order."""
    lines = path.read_text(encoding="utf-8").splitlines()
    if len(lines) < 2 or not lines[0].startswith("# golden-reach ledger") or lines[1] != LEDGER_HEADER:
        fail(f"{path} is not a golden-reach ledger; regenerate it with `{REPIN}`")
    out = []
    columns = len(LEDGER_HEADER.split("\t"))
    for number, line in enumerate(lines[2:], start=3):
        fields = line.split("\t")
        if len(fields) != columns:
            fail(f"{path}:{number} has {len(fields)} tab-separated fields, not {columns}; regenerate it with `{REPIN}`")
        rank, key, region, _us, _ur, _regions, witnesses, outside, sites, note = fields
        parsed = []
        try:
            if sites not in ("none", COOCCURRENCE):
                for entry in sites.split(SITE_SEPARATOR):
                    spec, _, counts = entry.rpartition("=")
                    hit, _, total = counts.partition("/")
                    parsed.append((spec, int(hit), int(total)))
            rank_number = int(rank)
        except ValueError:
            fail(
                f"{path}:{number} carries a rank or a `site=hit/total` count that is not a number; "
                f"regenerate it with `{REPIN}`"
            )
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
                    sites == COOCCURRENCE,
                ),
            )
        )
    return out


def stale_cells(regions_dir: Path = REGIONS_DIR) -> list[str]:
    """Every `golden` row whose reach cell is not the one its ledger row renders, named with the fix."""
    ledger = {reach.key: (rank, reach) for rank, reach in read_ledger(regions_dir / "golden-reach.tsv")}
    failures = []
    for path in sorted(regions_dir.glob("*.md")):
        for cells in region_rows(path.read_text(encoding="utf-8")):
            key = cells[0].strip("`")
            if cells[3].strip("`") != "golden":
                continue
            if key not in ledger:
                failures.append(f"`{key}` ({path.name}) has no golden-reach.tsv row; run `{REPIN}`")
            elif cells[5] != reach_cell(ledger[key][1], ledger[key][0], regions_dir):
                failures.append(
                    f"`{key}` ({path.name}): its reach cell is not the one its golden-reach.tsv row renders; "
                    f"run `{REPIN}`"
                )
    return failures


def rewrite_cells(reaches: list[Reach], regions_dir: Path = REGIONS_DIR, ranks: dict[str, int] | None = None) -> int:
    """Put each golden row's reach cell in its `crozier sites` column; return rows changed."""
    by_key = {r.key: ((ranks or {}).get(r.key, rank), r) for rank, r in enumerate(reaches, start=1)}
    changed = 0
    for path in sorted(regions_dir.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        out_lines = []
        for line in text.splitlines(keepends=True):
            cells = region_rows(line)
            if cells and cells[0][3].strip("`") == "golden":
                row = cells[0]
                key = row[0].strip("`")
                if key in by_key:
                    cell = reach_cell(by_key[key][1], by_key[key][0], regions_dir)
                    if row[5] != cell:
                        row = row[:5] + [cell] + row[6:]
                        newline = "\n" if line.endswith("\n") else ""
                        line = "| " + " | ".join(row) + " |" + newline
                        changed += 1
                elif ranks and key in ranks:
                    updated = re.sub(
                        r"(\(\[ledger\]\(golden-reach\.tsv\) rank )\d+(\))",
                        lambda match, rank=ranks[key]: f"{match[1]}{rank}{match[2]}",
                        line,
                    )
                    changed += updated != line
                    line = updated
            out_lines.append(line)
        path.write_text("".join(out_lines), encoding="utf-8")
    return changed


COVERAGE_DOC = REPO / "docs" / "openapi-surface-coverage.md"
EXHAUSTIVE_SEARCH_HEADING = "### Witness search (exhaustive)"
CONFIG_GATE_HEADING = "### Configuration gate"
NOT_SEARCHED_CELL = "`not searched` — no arm search has run"
ARM_COUNTS_BEGIN = "<!-- BEGIN GENERATED ARM COUNTS: run `just golden-reach-arms` -->"
ARM_COUNTS_END = "<!-- END GENERATED ARM COUNTS -->"
ARM_TABLE_BEGIN = "<!-- BEGIN GENERATED ARM TABLE: run `just golden-reach-arms` -->"
ARM_TABLE_END = "<!-- END GENERATED ARM TABLE -->"
ARM_TABLE_HEADER = (
    "| rank | key | unreached site | regions | search verdict | hand-written cover |\n|---|---|---|---|---|---|\n"
)


# A hand-written combination fixture's cover verdict where admissible real witnesses
# exist but unrelated residuals block them (`docs/openapi-surface/handwritten/AGENTS.md`).
WITNESS_BLOCKED = "witness-blocked"


class Verdict(StrEnum):
    """What an arm-search record states for an arm (fern-limitations.md's vocabulary)."""

    EXHAUSTED = "exhausted"
    SEARCH_INCOMPLETE = "search-incomplete"
    CONFIG_GATED = "config-gated"


class Cover(NamedTuple):
    """One `[[covers]]` entry of a hand-written fixture's `evidence.toml`."""

    fixture: str
    key: str
    arm: str | None
    verdict: Verdict
    # The fixture declares a generation setting (`audiences`), so its runs are gated.
    set_up: bool
    # `<repo-relative path>#<anchor>` of the search record the cover cites, if any.
    search: str | None = None


class ArmRow(NamedTuple):
    """One unreached arm, as the coverage index's arm table states it."""

    rank: int
    key: str
    site: str
    regions: int
    verdict: Verdict | None  # None: no arm search has run and no cover cites a witness search
    covers: tuple[str, ...]

    def cells(self) -> list[str]:
        return [
            str(self.rank),
            f"`{self.key}`",
            f"`{self.site}`",
            str(self.regions),
            NOT_SEARCHED_CELL if self.verdict is None else f"`{self.verdict}`",
            ", ".join(f"`{name}`" for name in self.covers) or "—",
        ]


def table_cells(line: str, width: int) -> list[str] | None:
    """One markdown table row as `width` cells, or None; `\\|` is an escaped pipe, overflow folds into the last."""
    if not line.startswith("| "):
        return None
    cells = [cell.replace("\x00", "\\|").strip() for cell in line.replace("\\|", "\x00").strip().strip("|").split("|")]
    if len(cells) < width:
        return None
    return cells[: width - 1] + ["|".join(cells[width - 1 :])]


def _verdict(text: str, where: str) -> Verdict:
    try:
        return Verdict(text)
    except ValueError:
        fail(f"{where} states the verdict {text!r}, not one of {[v.value for v in Verdict]}; correct it, then re-run")


def config_gated_verdict(text: str, key: str) -> str | None:
    """The verdict a `config-gated` record's gate table states for `key`, else None."""
    if CONFIG_GATE_HEADING not in text.splitlines():
        return None
    body = text.split(CONFIG_GATE_HEADING, 1)[1].split("\n### ", 1)[0].split("\n#### ", 1)[0]
    stated = {
        cells[3].strip("`")
        for cells in (table_cells(line, 4) for line in body.splitlines())
        if cells and cells[0].strip("`") == key
    }
    return stated.pop() if len(stated) == 1 else None


class Measurement(NamedTuple):
    """One row of a `just handwritten-reach` ledger: a fixture's run over one arm."""

    fixture: str
    key: str
    site: str
    setting: str | None  # `handwritten-config-gates.tsv`'s setting column; `-` is no setting
    regions_executed: int
    regions: int


REACH_COLUMNS = ("fixture", "key", "site", "regions_executed", "regions")
GATE_COLUMNS = ("fixture", "key", "site", "setting", "regions_executed", "regions")


def read_measurements(path: Path, columns: tuple[str, ...]) -> list[Measurement]:
    """A `just handwritten-reach` TSV as typed rows, refused unless every row fills `columns` exactly."""
    with path.open(encoding="utf-8", newline="") as handle:
        lines = handle.read().splitlines()
    if not lines or tuple(lines[0].split("\t")) != columns:
        fail(f"{path} does not start with the columns {list(columns)}; run `{REPIN}`")
    rows = []
    for number, line in enumerate(lines[1:], start=2):
        cells = line.split("\t")
        row = dict(zip(columns, cells, strict=False))
        if (
            len(cells) != len(columns)
            or not all(row[name] for name in columns)
            or not all(re.fullmatch(r"[0-9]+", row[name]) for name in ("regions_executed", "regions"))
        ):
            fail(f"{path}:{number} is not {len(columns)} filled cells ending in two whole-number counts; run `{REPIN}`")
        if int(row["regions_executed"]) > int(row["regions"]):
            fail(
                f"{path}:{number} executes {row['regions_executed']} of only {row['regions']} regions, "
                f"a measurement no run can take; run `{REPIN}`"
            )
        rows.append(
            Measurement(
                row["fixture"],
                row["key"],
                row["site"],
                row.get("setting"),
                int(row["regions_executed"]),
                int(row["regions"]),
            )
        )
    return rows


def handwritten_covers(regions_dir: Path = REGIONS_DIR) -> list[Cover]:
    """Every cover a hand-written fixture's `evidence.toml` declares, validated."""
    covers = []
    for path in sorted((regions_dir / "handwritten").glob("*/evidence.toml")):
        with path.open("rb") as handle:
            declared = tomllib.load(handle)
        audiences = declared.get("audiences", [])
        entries = declared.get("covers", [])
        if (
            not isinstance(audiences, list)
            or not all(isinstance(name, str) and name for name in audiences)
            or not isinstance(entries, list)
        ):
            fail(
                f"{path}: `audiences` must be an array of audience names and `covers` an array; correct it, then re-run"
            )
        for cover in entries:
            arm = cover.get("arm") if isinstance(cover, dict) else None
            if (
                not isinstance(cover, dict)
                or not isinstance(cover.get("key"), str)
                or not cover["key"]
                or not isinstance(cover.get("verdict"), str)
                or not isinstance(arm, (str, type(None)))
                or arm == ""
            ):
                fail(f"{path}: every cover needs a non-empty string `key` and `verdict`, and a non-empty `arm` if any")
            if cover["verdict"] == WITNESS_BLOCKED and arm is None:
                # A feature-level combination cover whose witnesses are blocked proves
                # no arm; `handwritten-fixtures.py gate` holds it to its record.
                continue
            covers.append(
                Cover(
                    path.parent.name,
                    cover["key"],
                    arm,
                    _verdict(cover["verdict"], str(path)),
                    bool(audiences),
                    cover.get("search") if isinstance(cover.get("search"), str) else None,
                )
            )
    return covers


def config_gated_arm_verdict(
    key: str, site: str, text: str, regions_dir: Path = REGIONS_DIR, covers: list[Cover] | None = None
) -> Verdict | None:
    """The verdict a `config-gated` record's key gives one of its arms, by measurement.

    The gate table's verdict is the measured gate's: it holds for an arm
    `handwritten-config-gates.tsv` records with and without the setting. Any
    other arm of the key joined it later and is gated only if measured so: it
    reads the verdict its hand-written covers cite, and only when
    `handwritten-reach.tsv` shows a cover's fixture, declaring no setting,
    executing it. Otherwise no one verdict is stated (`None`).
    """
    gates = [
        row
        for row in read_measurements(regions_dir / "handwritten-config-gates.tsv", GATE_COLUMNS)
        if (row.key, row.site) == (key, site)
    ]
    if gates:
        with_setting = [row for row in gates if row.setting != "-"]
        without = [row for row in gates if row.setting == "-"]
        if (
            not with_setting
            or not without
            or any(row.regions_executed == 0 for row in with_setting)
            or any(row.regions_executed for row in without)
        ):
            fail(
                f"handwritten-config-gates.tsv: `{key}`'s arm `{site}` is not a measured gate — it needs a run "
                "with the setting that executes it and a run without one that does not; re-run "
                "`just handwritten-reach`"
            )
        stated = config_gated_verdict(text, key)
        return None if stated is None else _verdict(stated, f"{key}'s gate table")
    citing = [
        c for c in (handwritten_covers(regions_dir) if covers is None else covers) if (c.key, c.arm) == (key, site)
    ]
    ungated = {c.fixture for c in citing if not c.set_up}
    executed = any(
        row.fixture in ungated and (row.key, row.site) == (key, site) and row.regions_executed
        for row in read_measurements(regions_dir / "handwritten-reach.tsv", REACH_COLUMNS)
    )
    verdicts = {c.verdict for c in citing}
    return verdicts.pop() if executed and len(verdicts) == 1 else None


def arm_verdict(
    key: str, site: str, regions_dir: Path = REGIONS_DIR, covers: list[Cover] | None = None
) -> Verdict | None:
    """The verdict an unreached arm's linked arm-search record gives it, or None when no record exists.

    An ordinary record states one verdict for its key in its exhaustive-search
    table; a `config-gated` one gives each arm its own (`config_gated_arm_verdict`).
    """
    record = regions_dir / SEARCHES / f"{key}.md"
    if not record.is_file():
        return None
    text = record.read_text(encoding="utf-8")
    if CONFIG_GATE_HEADING in text.splitlines():
        verdict = config_gated_arm_verdict(key, site, text, regions_dir, covers)
    else:
        stated: set[str] = set()
        if EXHAUSTIVE_SEARCH_HEADING in text:
            body = text.split(EXHAUSTIVE_SEARCH_HEADING, 1)[1].split("\n#", 1)[0]
            for line in body.splitlines():
                cells = table_cells(line, 7)
                if cells and cells[0].strip("`") == key:
                    stated.add(cells[2].strip("`"))
        verdict = _verdict(stated.pop(), str(record)) if len(stated) == 1 else None
    if verdict is None:
        fail(f"{record}: states no one verdict for `{site}`; correct its record or measurements, then re-run")
    return verdict


def cited_search_verdict(
    key: str, site: str, regions_dir: Path = REGIONS_DIR, covers: list[Cover] | None = None
) -> Verdict | None:
    """The verdict the witness-search records an arm's hand-written covers cite state for its key.

    An arm no arm-search record names may still have been searched: a bounded
    witness search a cover cites decided it. Each cited record's section is read,
    never the cover's own copy of the verdict; None when no cover cites one.
    """
    cited = {
        cover.search
        for cover in (handwritten_covers(regions_dir) if covers is None else covers)
        if (cover.key, cover.arm) == (key, site) and cover.search
    }
    if not cited:
        return None
    gate = _load_handwritten_module()
    root = regions_dir.parents[1]
    stated: set[str] = set()
    for reference in sorted(cited):
        section, error = gate.record_section(root, reference)
        if section is None:
            fail(f"`{key}`'s arm `{site}` cites a search record that does not resolve: {error}")
        stated |= {
            cell.strip("`")
            for cells in gate.key_rows(section, key)
            for cell in cells
            if cell.strip("`") in set(Verdict)
        }
    if len(stated) != 1:
        fail(
            f"the records {sorted(cited)} state {sorted(stated) or 'no verdict'} for `{key}`, not one verdict "
            f"for its arm `{site}`; correct the records or the covers that cite them, then re-run"
        )
    return Verdict(stated.pop())


def _load_handwritten_module():
    spec = importlib.util.spec_from_file_location(
        "golden_reach_handwritten", REPO / "tools" / "surface-census" / "handwritten-fixtures.py"
    )
    if spec is None or spec.loader is None:
        fail("cannot load tools/surface-census/handwritten-fixtures.py; restore it from git")
    module = importlib.util.module_from_spec(spec)
    sys.modules.setdefault(spec.name, module)
    spec.loader.exec_module(module)
    return module


def golden_ledger(ledger: list[tuple[int, Reach]], regions_dir: Path = REGIONS_DIR) -> list[tuple[int, Reach]]:
    """The ledger's `golden` rows: a `gap` combination's unreached interaction branch is
    named with the combinations, never counted as an arm of a golden row."""
    golden = golden_rows(regions_dir)
    return [(rank, reach) for rank, reach in ledger if reach.key in golden]


def interaction_unreached_reason(sites: tuple[tuple[str, int, int], ...], by: str) -> str:
    """The `#### Unproven combinations, named` reason a combination's measurement gives it.

    `sites` are its interaction sites as the measurement reports them, and `by` the
    run that missed them: `golden-only witnesses `a`, `b`` or `hand-written fixture `f``.
    """
    unreached = ", ".join(f"`{spec}` {hit}/{total}" for spec, hit, total in sites if not hit)
    return f"`interaction branch unreached` — unreached {unreached} by {by}"


def witnesses_phrase(witnesses: tuple[str, ...]) -> str:
    """How an `interaction branch unreached` reason names a ledger row's golden-only witnesses."""
    if not witnesses:
        return "no golden-only witness"
    plural = "es" if len(witnesses) > 1 else ""
    return f"golden-only witness{plural} " + ", ".join(f"`{name}`" for name in witnesses)


def arm_rows(ledger: list[tuple[int, Reach]], regions_dir: Path = REGIONS_DIR) -> list[ArmRow]:
    """Every unreached arm of a `golden` row, in ledger rank order, as the arm table states it."""
    ledger = golden_ledger(ledger, regions_dir)
    covers = handwritten_covers(regions_dir)
    covering: dict[tuple[str, str], set[str]] = defaultdict(set)
    for cover in covers:
        if cover.arm:
            covering[(cover.key, cover.arm)].add(cover.fixture)
    return [
        ArmRow(
            rank,
            reach.key,
            spec,
            total,
            arm_verdict(reach.key, spec, regions_dir, covers)
            or cited_search_verdict(reach.key, spec, regions_dir, covers),
            tuple(sorted(covering.get((reach.key, spec), ()))),
        )
        for rank, reach in ledger
        for spec, hit, total in reach.sites
        if not hit
    ]


def arm_counts_text(ledger: list[tuple[int, Reach]], rows: list[ArmRow]) -> str:
    """The generated sentence counting the golden rows' reach and the arm table's verdicts."""
    partial = sum(1 for _rank, reach in ledger if reach.unreached_sites)
    phrases = [f"{sum(1 for row in rows if row.verdict is verdict)} read `{verdict}`" for verdict in Verdict]
    unsearched = sum(1 for row in rows if row.verdict is None)
    return (
        f"The golden rows split in two. **{len(ledger) - partial}** reach every handling site their\n"
        "[site table](openapi-surface/golden-reach-sites.tsv) declares, and "
        f"**{partial}** carry at least one handling site no golden-only witness executes: "
        f"{len(rows)} unreached arms in all. By the verdict each arm's linked record states, "
        f"{', '.join(phrases)}, and {unsearched} have no arm search.\n"
    )


def _replace_between(text: str, begin: str, end: str, body: str, path: Path) -> str:
    if (
        text.count(begin) != 1
        or text.count(begin + "\n") != 1
        or text.count(end) != 1
        or text.index(begin) > text.index(end)
    ):
        fail(f"{path} carries no single `{begin}` ... `{end}` section; restore the markers, then run `{REPIN}`")
    head, rest = text.split(begin + "\n", 1)
    _old, tail = rest.split(end, 1)
    return head + begin + "\n" + body + end + tail


def render_arm_sections(
    text: str, ledger: list[tuple[int, Reach]], regions_dir: Path = REGIONS_DIR, path: Path = COVERAGE_DOC
) -> str:
    """`text` with its generated arm counts and arm table restated from the committed measurements."""
    ledger = golden_ledger(ledger, regions_dir)
    rows = arm_rows(ledger, regions_dir)
    table = ARM_TABLE_HEADER + "".join("| " + " | ".join(row.cells()) + " |\n" for row in rows)
    text = _replace_between(text, ARM_COUNTS_BEGIN, ARM_COUNTS_END, arm_counts_text(ledger, rows), path)
    return _replace_between(text, ARM_TABLE_BEGIN, ARM_TABLE_END, table, path)


def rewrite_arm_sections(
    ledger: list[tuple[int, Reach]],
    regions_dir: Path = REGIONS_DIR,
    path: Path = COVERAGE_DOC,
    *,
    headline: bool = False,
) -> bool:
    """Restate the coverage index's generated arm sections in place; return whether they changed."""
    text = path.read_text(encoding="utf-8")
    restated = render_arm_sections(text, ledger, regions_dir, path)
    if headline:
        restated = render_arm_headline(restated, ledger, regions_dir, path)
    if restated != text:
        path.write_text(restated, encoding="utf-8", newline="\n")
    return restated != text


def headline_arm_keys(text: str, heading: str, columns: int) -> set[tuple[str, str]]:
    """The arm identities of one existing evidence table, without counting prose."""
    if text.count(heading) != 1:
        fail(f"missing or repeated {heading}; restore the evidence section, then re-run arms --headline")
    body = text.partition(heading)[2].split("\n#", 1)[0]
    return {
        (cells[0].strip("` "), cells[1].strip("` ").replace("\\|", "|"))
        for line in body.splitlines()
        if (cells := table_cells(line, columns)) and re.fullmatch(r"`[^`]+`", cells[0])
    }


def render_arm_headline(text: str, ledger: list[tuple[int, Reach]], regions: Path, path: Path) -> str:
    """Restate the current arm split, retaining historical and ownership sections."""
    declared = golden_rows(regions)
    ledger = golden_ledger(ledger, regions)
    if len(ledger) != len(declared) or {reach.key: reach.region for _rank, reach in ledger} != declared:
        fail("the reach ledger is not the golden region population; re-join it before arms --headline")
    rows = arm_rows(ledger, regions)
    unreached = {(row.key, row.site) for row in rows}
    measured = set()
    for filename, columns in (("handwritten-reach.tsv", REACH_COLUMNS), ("handwritten-config-gates.tsv", GATE_COLUMNS)):
        if (regions / filename).is_file():
            measured.update(
                (row.fixture, row.key, row.site)
                for row in read_measurements(regions / filename, columns)
                if row.regions_executed
            )
    covers: dict[tuple[str, str], set[Verdict]] = defaultdict(set)
    for cover in handwritten_covers(regions):
        if cover.arm and (cover.key, cover.arm) in unreached and (cover.fixture, cover.key, cover.arm) in measured:
            covers[(cover.key, cover.arm)].add(cover.verdict)
    if any(len(verdicts) != 1 for verdicts in covers.values()):
        fail("an arm cover has conflicting verdicts; correct its evidence before arms --headline")
    verdicts = Counter(next(iter(values)) for values in covers.values())
    try:
        refused_text = (regions.parent / "fern-limitations.md").read_text(encoding="utf-8")
        classes_path = regions.parent / "fern-refusals/classes.tsv"
        with classes_path.open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle, delimiter="\t", quoting=csv.QUOTE_NONE)
            if not reader.fieldnames or not {"class", "status"}.issubset(reader.fieldnames):
                fail("classes.tsv lacks class/status columns; restore the registry, then re-run arms --headline")
            classes = list(reader)
        if any(
            None in row
            or any(value is None for value in row.values())
            or not row["class"]
            or row["status"] not in {"generate", "refuse", "unevaluated"}
            for row in classes
        ):
            fail("classes.tsv has an incomplete or invalid row; restore it before arms --headline")
        if len({row["class"] for row in classes}) != len(classes):
            fail("classes.tsv repeats a class; repair the registry before arms --headline")
    except OSError as error:
        fail(f"cannot read headline evidence: {error}; restore it before arms --headline")
    decided, disposition_failures = _output_insensitive_module().read_records(regions.parent.parent)
    if disposition_failures:
        fail("; ".join(disposition_failures))
    insensitive = decided & unreached
    refused = headline_arm_keys(refused_text, "## Arms only a refused document reaches", 6) & unreached
    named = headline_arm_keys(text, "#### Unproven arms, named", 3) & unreached
    populations = [set(covers), refused, named, insensitive]
    if sum(map(len, populations)) != len(set().union(*populations)) or set().union(*populations) != unreached:
        fail("the headline arm populations overlap or leave an arm unaccounted for; repair their evidence first")
    sites = sum(len(reach.sites) for _rank, reach in ledger)
    reached = sites - len(unreached)
    refused_keys = ", ".join(f"`{key}`" for key in sorted({key for key, _site in refused})) or "none"
    body = (
        "`golden` is still not `golden`-exhausted, so the handling sites are split the\n"
        f"same way. The {len(declared)} `golden` rows declare {sites} handling sites in\n"
        "[the site table](openapi-surface/golden-reach-sites.tsv). The\n"
        "[ledger](openapi-surface/golden-reach.tsv) retains the base measurement's\n"
        "provenance and records scoped updates beside their rows.\n\n"
        f"- **{reached} are reached by a registered real specification.** Its scoped\n"
        "  golden test executes the site; file-level residuals remain recorded separately.\n"
        f"- **{len(covers)} are reached only by a hand-written fixture.** Each arm-level\n"
        "  cover executes the site and byte-matches the certified tree. Thus each of the "
        f"{len(covers)} is still one of the {len(unreached)} [unreached arms](#every-unreached-arm-and-its-search-verdict).\n"
        f"  The cited records of {verdicts[Verdict.EXHAUSTED]} read `exhausted`, "
        f"{verdicts[Verdict.SEARCH_INCOMPLETE]} read `search-incomplete` "
        f"and {verdicts[Verdict.CONFIG_GATED]} read `config-gated`.\n"
        f"- **{len(refused)} are reachable only by a document Fern refuses**, leaving no\n"
        "  successful complete tree to byte-match. Their refused documents and controls\n"
        "  are recorded in [the limitations ledger](fern-limitations.md#arms-only-a-refused-document-reaches).\n"
        f"  The keys are {refused_keys}.\n"
        f"- **{len(insensitive)} {'is' if len(insensitive) == 1 else 'are'} decided output-insensitive**, with identical complete\n"
        "  before/after trees in both generators recorded in [the shared table](openapi-surface/output-insensitive.tsv).\n"
        f"- **{len(named)} {'is a named gap' if len(named) == 1 else 'are named gaps'}**, "
        "whose outstanding evidence is in [Unproven arms, named](#unproven-arms-named).\n\n"
        f"{reached} + {len(covers)} + {len(refused)} + {len(insensitive)} + {len(named)} = {sites}."
    )
    pattern = r"`golden` is still not `golden`-exhausted.*?^\d+(?: \+ \d+){3,4} = \d+\."
    text, count = re.subn(pattern, lambda _match: body, text, count=1, flags=re.M | re.S)
    if count != 1:
        fail(f"{path}: missing current arm headline; restore it before arms --headline")
    paragraph = (
        "Where crozier deliberately differs from Fern is decided in\n"
        f"[the refusal registry](fern-refusals/README.md). Each of its {len(classes)} classes has a decided detector or a fully evaluated document population\n"
        "([the exception contract](fern-refusals/README.md)). A `refuse` detector stops\n"
        "generation in both modes. A `generate` decision writes by default and refuses\n"
        "under `fern-strict`; an evaluated `fern-limitation` document generates in both\n"
        "modes and carries its SDK evaluation.\n\n"
    )
    text, count = re.subn(
        r"Where crozier deliberately differs from Fern.*?(?=\*\*What the census still cannot enumerate\.\*\*)",
        lambda _match: paragraph,
        text,
        count=1,
        flags=re.S,
    )
    if count != 1:
        fail(f"{path}: missing refusal headline; restore it before arms --headline")
    return text


def fixture_test_map(repo_root: Path) -> dict[str, str]:
    """census fixture name -> the golden test comparing its committed golden.

    The census reads `crates/crozier-e2e/tests/e2e.rs` for its golden-source population
    (`golden_registrations`), so the reach join reads the same registrations
    rather than a second parse: a corpus helper or a feature-target macro one
    reader recognises and the other did not would leave a golden source with no
    scoped run. The census reports a corpus by its `CORPUS.md` fixture name,
    which `corpus_aliases` maps back.
    """
    census = _census_module()
    registrations = census.golden_registrations(repo_root / census.GOLDEN_REGISTRY)
    by_fixture = {api: registration.test for api, registration in registrations.items()}
    for fixture, api in census.corpus_aliases(repo_root / "tests" / "fixtures").items():
        if api in registrations:
            by_fixture[fixture] = registrations[api].test
    return by_fixture


def _census_module():
    spec = importlib.util.spec_from_file_location(
        "openapi_surface_census", REPO / "tools" / "surface-census" / "openapi-surface-census.py"
    )
    if spec is None or spec.loader is None:
        raise SystemExit(
            "golden-reach: cannot load tools/surface-census/openapi-surface-census.py; restore it from git"
        )
    module = importlib.util.module_from_spec(spec)
    sys.modules.setdefault("openapi_surface_census", module)
    spec.loader.exec_module(module)
    return module


def load_regions(path: Path) -> dict[str, set[tuple[int, ...]]]:
    """A measurement's `{file: [[line, col, line, col], ...]}` map, refused unless it is one."""
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        fail(f"{path} is unreadable ({error}); run `{REPIN}` to measure again")

    def region(r: Any) -> bool:
        # llvm-cov's spans: 1-based line and column pairs, the end not before the start.
        return (
            isinstance(r, list)
            and len(r) == 4
            and all(type(n) is int and n >= 1 for n in r)
            and (r[0], r[1]) <= (r[2], r[3])
        )

    if not isinstance(raw, dict) or not all(
        isinstance(regions, list) and all(region(r) for r in regions) for regions in raw.values()
    ):
        fail(
            f"{path} is not a map of files to [line, col, line, col] regions (1-based, end after start); "
            f"run `{REPIN}` to measure again"
        )
    return {f: {tuple(r) for r in regions} for f, regions in raw.items()}


def load_census(path: Path) -> dict[str, Any]:
    """The census's `--json` output, refused unless it carries its `sources` and `rows`."""
    if not path.is_file():
        fail(f"no census at {path}; run `{REPIN}` (it writes one there)")
    try:
        census = json.loads(path.read_text(encoding="utf-8"))
    except ValueError as error:
        fail(f"{path} is not JSON ({error}); run `{REPIN}` to write it again")
    shaped = (
        isinstance(census, dict)
        and isinstance(census.get("sources"), list)
        and all(isinstance(s, dict) and isinstance(s.get("fixture"), str) for s in census["sources"])
        and isinstance(census.get("rows"), list)
        and all(
            isinstance(r, dict)
            and isinstance(r.get("selector"), str)
            and isinstance(r.get("fixture"), str)
            and type(r.get("count")) is int
            and r["count"] >= 0
            for r in census["rows"]
        )
    )
    if not shaped:
        fail(
            f"{path} is not the census's `--json` output (`sources` naming string fixtures, and `rows` of "
            "string `selector` and `fixture` with a non-negative integer `count`); "
            f"run `{REPIN}` to write it again"
        )
    return census


def load_coverage(out: Path, repo_root: Path | None = None) -> tuple[dict[str, dict[str, set]], dict[str, set], str]:
    universe_path = out / "universe.json"
    if not universe_path.is_file():
        fail(f"no measurement under {out}; run `{REPIN}` first")
    if repo_root is not None and (out / STORE_FILE).is_file():
        stale_measurement(out, repo_root)
    universe = load_regions(universe_path)
    coverage = {path.stem: load_regions(path) for path in sorted((out / "tests").glob("*.json"))}
    return coverage, universe, measured_commit(out)


def stale_measurement(out: Path, repo_root: Path) -> None:
    """Refuse a measurement whose functions are not this tree's: its regions would land on other code."""
    try:
        store = RS.load(out / STORE_FILE)
    except RS.StoreError as error:
        fail(f"{error}; run `{REPIN}` to measure again")
    changed = RS.stale_functions(RS.read_tree(repo_root), store["functions"])
    if changed:
        fail(
            f"the measurement under {out} was taken at {store['commit'][:12]}, and {len(changed)} function(s) "
            f"of this tree differ from it ({', '.join(changed[:3])}); run `{REPIN}`"
        )


def provenance_line(out: Path, commit: str, tests: int) -> str:
    """The ledger's first line: the measured commit, the base, and the tests run at it and carried."""
    line = (
        f"golden-only tier, one scoped run per golden test, measured at commit {commit[:12]} over {tests} golden tests"
    )
    try:
        recorded = json.loads((out / "provenance.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return line
    if not isinstance(recorded, dict) or not isinstance(recorded.get("run"), int):
        return line
    base = recorded.get("base")
    origin = f"base {base[:12]}" if isinstance(base, str) and not recorded.get("full") else "base none (full)"
    return f"{line}; {origin}: {recorded['run']} run at {commit[:12]}, {recorded.get('carried', 0)} carried"


def measured_commit(out: Path) -> str:
    """The commit the measurement under `out` was taken at, as `measure` recorded it."""
    path = out / "provenance.json"
    try:
        commit = json.loads(path.read_text(encoding="utf-8"))["commit"]
    except (OSError, ValueError, KeyError, TypeError) as error:
        fail(f"{path} names no measured commit ({error!r}); run `{REPIN}` first")
    if not isinstance(commit, str) or not re.fullmatch(r"[0-9a-f]{7,40}", commit):
        fail(f"{path} records {commit!r}, not a commit; run `{REPIN}` again")
    return commit


def report(args: argparse.Namespace) -> int:
    repo_root: Path = args.repo_root
    table = read_sites_table(repo_root / "docs" / "openapi-surface" / "golden-reach-sites.tsv")
    table = measured_table(table, repo_root / "docs" / "openapi-surface")
    rows = measured_rows(repo_root / "docs" / "openapi-surface", set(table))
    if args.keys:
        unknown = sorted(set(args.keys) - rows.keys())
        if unknown:
            fail(f"unknown golden key(s): {', '.join(unknown)}; pass keys the ledger measures")
        rows = {key: region for key, region in rows.items() if key in args.keys}
        table = {key: row for key, row in table.items() if key in rows}
    census = load_census(Path(args.census) if args.census else args.out / "census.json")
    coverage, universe, commit = load_coverage(args.out, repo_root)
    fixture_tests = {f: t for f, t in fixture_test_map(repo_root).items() if t in coverage}
    reaches = compute(
        rows,
        table,
        census,
        fixture_tests,
        coverage,
        universe,
        repo_root,
    )
    provenance = provenance_line(args.out, commit, len(coverage))
    if args.keys:
        return scoped_report(args, reaches, commit, len(coverage))
    if args.write:
        (repo_root / "docs" / "openapi-surface" / "golden-reach.tsv").write_text(
            ledger_text(reaches, provenance), encoding="utf-8"
        )
        changed = rewrite_cells(reaches, repo_root / "docs" / "openapi-surface")
        index = repo_root / "docs" / "openapi-surface-coverage.md"
        # A tree with no coverage index (a scratch region set) has no arm sections to restate.
        restated = (
            not getattr(args, "skip_arms", False)
            and index.is_file()
            and rewrite_arm_sections(
                read_ledger(repo_root / "docs" / "openapi-surface" / "golden-reach.tsv"),
                repo_root / "docs" / "openapi-surface",
                index,
            )
        )
        print(
            f"golden-reach: wrote the ledger and {changed} reach cell(s); "
            f"arm sections {'restated' if restated else 'unchanged'}"
        )
    else:
        sys.stdout.write(ledger_text(reaches, provenance))
    return 0


def scoped_report(args: argparse.Namespace, reaches: list[Reach], commit: str, tests: int) -> int:
    """Join selected measurements and rerank, preserving every other measurement.
    Other region content changes only where its derived rank link moves.
    """
    regions = args.repo_root / "docs/openapi-surface"
    ledger = regions / "golden-reach.tsv"
    previous = read_ledger(ledger)
    current_measured = measured_rows(regions, set(read_sites_table(regions / "golden-reach-sites.tsv")))
    combined = {reach.key: reach for _rank, reach in previous if reach.key in current_measured}
    measured = []
    for reach in reaches:
        note = f"measured at commit {commit} over {tests} scoped golden test(s)"
        reach = reach._replace(note=f"{reach.note}; {note}" if reach.note else note)
        measured.append(reach)
        combined[reach.key] = reach
    ranked = sorted(combined.values(), key=ranking_key)
    ranks = {reach.key: rank for rank, reach in enumerate(ranked, 1)}
    lines = ledger.read_text(encoding="utf-8").splitlines(keepends=True)
    lines[0] = lines[0].rstrip("\n").split("; scoped updates", 1)[0] + "; scoped updates carry per-row provenance\n"
    old_rows = {line.split("\t")[1]: line for line in lines[2:]}
    selected = {reach.key for reach in measured}
    output = lines[:2]
    for reach in ranked:
        if reach.key in selected:
            line = ledger_text([reach], "scoped").splitlines(keepends=True)[2]
        else:
            line = old_rows[reach.key]
        output.append(f"{ranks[reach.key]}\t{line.partition(chr(9))[2]}")
    text = "".join(output)
    if args.write:
        ledger.write_text(text, encoding="utf-8")
        changed = rewrite_cells(measured, regions, ranks)
        print(f"golden-reach: updated {len(measured)} scoped ledger row(s) and {changed} reach cell(s)")
    else:
        sys.stdout.write(text)
    return 0


def arms(args: argparse.Namespace) -> int:
    """Restate the coverage index's arm counts and arm table from the committed ledger and records."""
    regions = args.repo_root / "docs" / "openapi-surface"
    restated = rewrite_arm_sections(
        read_ledger(regions / "golden-reach.tsv"),
        regions,
        args.repo_root / "docs" / "openapi-surface-coverage.md",
        headline=args.headline,
    )
    print(f"golden-reach: arm sections {'restated' if restated else 'unchanged'}")
    return 0


def sites(args: argparse.Namespace) -> int:
    table = read_sites_table(args.table or args.repo_root / "docs" / "openapi-surface" / "golden-reach-sites.tsv")
    if args.census:
        census = load_census(Path(args.census))
        for row in table.values():
            if not census_witnesses(census, row.selectors):
                fail(
                    f"{row.key}: no registered source declares any of {', '.join(row.selectors)}; correct its selectors in {SITES_TABLE.name}, or run `{REPIN}` if the census is stale"
                )
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


def default_jobs() -> int:
    """One instrumented run at a time on a shared host; CI's runner is the job's own."""
    return 4 if os.environ.get("CI") else 1


def package_base(args: argparse.Namespace) -> int:
    """The base-publishing CI job's command: step from the nearest earlier base, package the result.

    Writes `<package>/base.json.gz`, the artifact `golden-reach-base-<sha>` uploads.
    """
    repo_root: Path = args.repo_root
    dirty = uncommitted_changes(repo_root)
    if dirty:
        fail(f"{len(dirty)} tracked file(s) differ from HEAD ({', '.join(dirty[:5])}); package a committed tree")
    base_module = _sibling("reach_base")
    with RS.instrumented_lock("golden-reach base"):
        choice = base_module.find(repo_root, include_head=False)
        print(f"golden-reach: base: {choice.reason}", file=sys.stderr)
        step = measure_step(repo_root, base=choice.store, full_reason=choice.reason, jobs=args.jobs)
    write_views(step, args.out, repo_root)
    base_module.publish(step.store)
    RS.save(step.store, args.package / base_module.ARTIFACT_FILE)
    print(
        f"golden-reach: packaged {args.package / base_module.ARTIFACT_FILE} for "
        f"{base_module.ARTIFACT_PREFIX}{step.store['commit']}: {describe(step)}"
    )
    return 0


def positive_int(text: str) -> int:
    """An argparse type for a worker count or timeout: a whole number above zero."""
    try:
        value = int(text)
    except ValueError:
        value = 0
    if value < 1:
        raise argparse.ArgumentTypeError(f"{text!r} is not a whole number above zero; pass one such as 4")
    return value


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("--repo-root", type=Path, default=REPO)
    parser.add_argument(
        "--out", type=Path, default=None, help="the measurement directory (default: REPO_ROOT/.local/golden-reach)"
    )
    sub = parser.add_subparsers(dest="command", required=True)
    m = sub.add_parser("measure", help="one instrumented run per golden test")
    m.add_argument("--jobs", type=positive_int, default=default_jobs())
    m.add_argument("--tests", help="re-run the golden tests this regex matches, merging them into the store")
    m.add_argument(
        "--incremental", action="store_true", help="step from the nearest saved base, re-running only what changed"
    )
    m.add_argument(
        "--golden-only",
        action="store_true",
        help="measure the golden tests alone, leaving the hand-written fixtures out",
    )
    b = sub.add_parser("base", help="CI: measure from the nearest earlier base and package base.json.gz")
    b.add_argument("--jobs", type=positive_int, default=default_jobs())
    b.add_argument("--package", type=Path, required=True, help="directory to write base.json.gz into")
    r = sub.add_parser("report", help="join census, sites and coverage into the ledger")
    r.add_argument("--census", help="`just surface-census --json` output (default: OUT/census.json)")
    r.add_argument("--write", action="store_true", help="write the ledger and reach cells")
    r.add_argument(
        "--skip-arms",
        action="store_true",
        help="leave the arm sections alone (a scoped measurement holds too few witnesses to restate them)",
    )
    r.add_argument(
        "--keys", nargs="+", help="update only these golden keys, retaining other measurements and recomputing ranks"
    )
    a = sub.add_parser("arms", help="restate the coverage index's arm counts and table from committed files")
    a.add_argument("--headline", action="store_true", help="also restate its current arm and refusal headline")
    s = sub.add_parser("sites", help="resolve every declared site against src/")
    s.add_argument("--verbose", action="store_true")
    s.add_argument("--table", type=Path, help="a site table other than the committed one")
    s.add_argument("--census", help="also check every selector against this census output")
    args = parser.parse_args(argv)
    if args.out is None:
        args.out = args.repo_root / ".local" / "golden-reach"
    return {"measure": measure, "report": report, "arms": arms, "sites": sites, "base": package_base}[args.command](
        args
    )


if __name__ == "__main__":
    # The CLI emits UTF-8 even when a Windows pipe defaults to a legacy codec.
    for stream in (sys.stdout, sys.stderr):
        if isinstance(stream, io.TextIOWrapper):
            stream.reconfigure(encoding="utf-8", errors="backslashreplace")
    sys.exit(main())
