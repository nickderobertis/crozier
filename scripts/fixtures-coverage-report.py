#!/usr/bin/env python3
"""Turn per-tier `llvm-cov export` JSON into the fixtures-coverage report.

`scripts/fixtures-coverage.sh` measures three test tiers against the same
instrumented build and hands each tier's JSON export here. This module answers
the one question the repo could not previously answer with a number: *what do the
committed Fern goldens prove, as opposed to what crozier's own tests assert?*

Three honesty rules, none of which a bare `cargo llvm-cov` run obeys:

* **Counter regions, not just lines.** The lcov export carries no `BRDA` records
  and llvm-cov reports zero branches for this crate, so counter regions are the
  closest available branch proxy: a `match` with forty unexercised arms shows as
  covered *lines* if the match head ran, but as forty uncovered *regions*.
* **`#[cfg(test)]` is not production code.** llvm-cov's own per-file summary
  counts the crate's inline test modules (thousands of regions in `emit.rs` and
  `ir.rs`), which inflates every percentage. Those spans are found in the source
  and removed from both numerator and denominator here.
* **One shared denominator.** A tier that never links the `crozier` binary is
  simply missing `src/main.rs` from its export; scoring it 0/0 would hide that.
  The denominator is the union of every region any tier reported, so the tiers
  are directly comparable and an absent object reads as uncovered.

Line coverage is derived from the same regions — a line is *instrumented* when a
counter region spans it and *covered* when a region spanning it executed. That is
marginally more conservative than llvm-cov's own line count, which additionally
credits macro-expansion segments; regions are the headline number either way.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import textwrap
from collections import defaultdict
from pathlib import Path
from typing import Iterable, NamedTuple

# LLVM's coverage export encodes a region as
# [line_start, col_start, line_end, col_end, count, file_id, expanded_file_id, kind]
# with kind 0 == Code; the other kinds (expansion/skipped/gap) carry no counter of
# their own and are dropped.
REGION_CODE_KIND = 0


class Region(NamedTuple):
    """A counter region's source span — its identity within a file."""

    line_start: int
    col_start: int
    line_end: int
    col_end: int


class Span(NamedTuple):
    """An inclusive `#[cfg(test)]` item span, 1-indexed."""

    start: int
    end: int


def cfg_test_spans(source: str) -> list[Span]:
    """Inclusive line spans of every `#[cfg(test)]` item in one Rust source file.

    Brace matching is string- and comment-aware (Rust raw strings, nested block
    comments, and `'a` lifetimes all bite a naive scanner), because the crate's
    test modules are full of Python templates whose braces and quotes would
    otherwise desynchronize the span.
    """
    lines = source.splitlines()
    spans: list[Span] = []
    end_of_last_span = 0
    for index, line in enumerate(lines):
        stripped = line.strip()
        if stripped != "#[cfg(test)]":
            if stripped.startswith("#[cfg(") and re.search(r"\btest\b", stripped):
                raise SystemExit(
                    f"fixtures-coverage: line {index + 1} carries a test-conditional "
                    f"attribute this scanner does not recognize ({stripped}). Teach "
                    f"cfg_test_spans that spelling, or the regions it guards would "
                    f"silently inflate the production denominator."
                )
            continue
        start = index + 1
        if start <= end_of_last_span:
            # Nested inside a span already excluded; nothing more to exclude.
            continue
        end = _item_end_line(lines, index)
        if end is None:
            raise SystemExit(
                f"fixtures-coverage: unbalanced braces after the #[cfg(test)] on "
                f"line {start}; the span scanner cannot bound the item. Fix the "
                f"source, or teach _item_end_line the construct it tripped on."
            )
        end_of_last_span = end
        spans.append(Span(start, end))
    return spans


def _item_end_line(lines: list[str], attribute_index: int) -> int | None:
    """1-indexed line of the closing brace of the item after `lines[attribute_index]`."""
    depth = 0
    opened = False
    in_block_comment = 0
    in_raw_string: int | None = None  # hash count of the open raw string
    in_string = False
    for index in range(attribute_index + 1, len(lines)):
        line = lines[index]
        position = 0
        while position < len(line):
            rest = line[position:]
            if in_block_comment:
                if rest.startswith("*/"):
                    in_block_comment -= 1
                    position += 2
                    continue
                if rest.startswith("/*"):
                    in_block_comment += 1
                    position += 2
                    continue
                position += 1
                continue
            if in_raw_string is not None:
                closer = '"' + "#" * in_raw_string
                if rest.startswith(closer):
                    in_raw_string = None
                    position += len(closer)
                    continue
                position += 1
                continue
            if in_string:
                if rest.startswith("\\"):
                    position += 2
                    continue
                if rest.startswith('"'):
                    in_string = False
                position += 1
                continue
            if rest.startswith("//"):
                break
            if rest.startswith("/*"):
                in_block_comment = 1
                position += 2
                continue
            hashes = _raw_string_hashes(line, position)
            if hashes is not None:
                in_raw_string = hashes
                position += 1 + hashes + 1  # r + hashes + opening quote
                continue
            if rest.startswith('"'):
                in_string = True
                position += 1
                continue
            consumed = _char_literal_width(line, position)
            if consumed:
                position += consumed
                continue
            if rest.startswith("{"):
                depth += 1
                opened = True
            elif rest.startswith("}"):
                depth -= 1
                if opened and depth == 0:
                    return index + 1
            position += 1
        if in_string:
            # An unterminated non-raw string cannot span lines in valid Rust.
            in_string = False
    return None


def _raw_string_hashes(line: str, position: int) -> int | None:
    """Hash count if a raw string literal (`r"`, `br##"`, …) opens at `position`."""
    if position and (line[position - 1].isalnum() or line[position - 1] == "_"):
        return None  # part of an identifier such as `for_` or `br`
    index = position
    if line.startswith("b", index):
        index += 1
    if not line.startswith("r", index):
        return None
    index += 1
    hashes = 0
    while line.startswith("#", index + hashes):
        hashes += 1
    if not line.startswith('"', index + hashes):
        return None
    return hashes


def _char_literal_width(line: str, position: int) -> int:
    """Width of a char literal at `position`, or 0 (lifetimes are not literals)."""
    if not line.startswith("'", position):
        return 0
    rest = line[position:]
    if rest.startswith("'\\"):
        index = 2
        if rest.startswith("u", index):  # '\u{1F600}'
            closing = rest.find("}", index)
            if closing == -1:
                return 0
            index = closing + 1
        else:
            index += 1  # the escaped character itself
        return index + 1 if rest.startswith("'", index) else 0
    if len(rest) >= 3 and rest[2] == "'":
        return 3
    return 0  # `'a` — a lifetime, whose following token must still be scanned


def load_tier(path: Path, repo_root: Path) -> dict[str, dict[Region, int]]:
    """Region -> max execution count, per repo-relative `src/` file, for one tier.

    A function's regions are emitted once per object file that contains it (the
    `crozier` binary and the test harnesses each carry a copy), so counts are
    merged by taking the maximum — reproducing llvm-cov's own per-region totals.
    """
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise SystemExit(
            f"fixtures-coverage: cannot read the coverage export {path}: {error}. "
            f"Re-run `just fixtures-coverage`; if it persists, check that "
            f"`cargo llvm-cov report --json` still emits llvm.coverage.json.export."
        ) from error
    export = document["data"][0]
    files: dict[str, dict[Region, int]] = defaultdict(dict)
    for function in export.get("functions", []):
        filenames = function["filenames"]
        for raw in function["regions"]:
            if raw[7] != REGION_CODE_KIND:
                continue
            absolute = Path(filenames[raw[5]])
            try:
                relative = absolute.relative_to(repo_root).as_posix()
            except ValueError:
                continue  # dependency source outside the workspace
            if not relative.startswith("src/"):
                continue
            region = Region(raw[0], raw[1], raw[2], raw[3])
            counts = files[relative]
            counts[region] = max(counts.get(region, 0), raw[4])
    return dict(files)


def drop_test_regions(
    tiers: dict[str, dict[str, dict[Region, int]]], repo_root: Path
) -> dict[str, list[Span]]:
    """Remove every region that starts inside a `#[cfg(test)]` span, in place."""
    spans: dict[str, list[Span]] = {}
    measured = {name for tier in tiers.values() for name in tier}
    for relative in sorted(measured):
        source = (repo_root / relative).read_text(encoding="utf-8")
        spans[relative] = cfg_test_spans(source)
    for tier in tiers.values():
        for relative, counts in tier.items():
            file_spans = spans.get(relative, [])
            if not file_spans:
                continue
            for region in list(counts):
                if any(s.start <= region.line_start <= s.end for s in file_spans):
                    del counts[region]
    return spans


def covered_lines(counts: dict[Region, int]) -> tuple[set[int], set[int]]:
    """(instrumented lines, covered lines) implied by a file's regions."""
    instrumented: set[int] = set()
    covered: set[int] = set()
    for region, count in counts.items():
        span = range(region.line_start, region.line_end + 1)
        instrumented.update(span)
        if count > 0:
            covered.update(span)
    return instrumented, covered


def percent(covered: int, total: int) -> str:
    return f"{100.0 * covered / total:5.1f}%" if total else "    --"


def render(
    tiers: dict[str, dict[str, dict[Region, int]]],
    order: list[str],
    selections: dict[str, tuple[str, int]],
) -> tuple[list[str], dict[str, tuple[int, int]]]:
    """The per-file three-tier table plus each tier's (covered, total) regions."""
    universe: dict[str, set[Region]] = defaultdict(set)
    line_universe: dict[str, set[int]] = defaultdict(set)
    for tier in tiers.values():
        for relative, counts in tier.items():
            universe[relative].update(counts)
            line_universe[relative].update(covered_lines(counts)[0])

    out: list[str] = []
    out.append("=== fixtures-coverage: src/ production coverage, #[cfg(test)] excluded ===")
    out.append("")
    out.append("tier selections (cargo-nextest filter expressions):")
    for name in order:
        expression, count = selections[name]
        plural = "test " if count == 1 else "tests"
        out.append(f"  {name:<12} {count:>4} {plural}  {expression}")
    out.append("")
    header = f"{'file':<20} {'tier':<12} {'regions':>18}  {'lines':>18}"
    out.append(header)
    out.append("-" * len(header))

    totals: dict[str, tuple[int, int]] = {}
    running = {name: [0, 0, 0, 0] for name in order}
    for relative in sorted(universe):
        region_total = len(universe[relative])
        line_total = len(line_universe[relative])
        for name in order:
            counts = tiers[name].get(relative, {})
            region_covered = sum(1 for count in counts.values() if count > 0)
            line_covered = len(covered_lines(counts)[1])
            running[name][0] += region_covered
            running[name][1] += region_total
            running[name][2] += line_covered
            running[name][3] += line_total
            label = relative if name == order[0] else ""
            out.append(
                f"{label:<20} {name:<12} "
                f"{region_covered:>6}/{region_total:<6} {percent(region_covered, region_total)}  "
                f"{line_covered:>6}/{line_total:<6} {percent(line_covered, line_total)}"
            )
        out.append("")
    out.append("-" * len(header))
    for name in order:
        rc, rt, lc, lt = running[name]
        totals[name] = (rc, rt)
        out.append(
            f"{'TOTAL':<20} {name:<12} "
            f"{rc:>6}/{rt:<6} {percent(rc, rt)}  {lc:>6}/{lt:<6} {percent(lc, lt)}"
        )
    return out, totals


def blind_spots(
    tiers: dict[str, dict[str, dict[Region, int]]], golden: str, order: Iterable[str]
) -> list[str]:
    """Regions some other tier reaches that no committed golden reaches."""
    reached = {
        name: {
            (relative, region)
            for relative, counts in tier.items()
            for region, count in counts.items()
            if count > 0
        }
        for name, tier in tiers.items()
    }
    others = [name for name in order if name != golden]
    out: list[str] = []
    out.append("")
    out.append(
        "golden blind spots — production regions another tier executes but no "
        "committed Fern golden does:"
    )
    per_file: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for name in others:
        for relative, _region in reached[name] - reached[golden]:
            per_file[relative][name] += 1
    if not per_file:
        out.append("  (none — every region any tier reaches, a golden reaches too)")
        return out
    width = max(len(relative) for relative in per_file)
    for relative in sorted(per_file, key=lambda f: -sum(per_file[f].values())):
        breakdown = ", ".join(f"{name} {per_file[relative][name]}" for name in others)
        out.append(
            f"  {relative:<{width}} {sum(per_file[relative].values()):>5}"
            f"   ({breakdown})"
        )
    unique = len(set().union(*(reached[name] for name in others)) - reached[golden])
    out.append(f"  total {unique} region(s) across {len(per_file)} file(s)")
    out.append("")
    out.extend(
        "  " + line
        for line in textwrap.wrap(
            "Read it as the fixture backlog: a file with a large count is "
            "generator behavior only crozier's own tests assert, so the next "
            "corpus spec worth adding is the one whose shapes reach those "
            "regions. A region another tier reaches is NOT parity evidence — "
            "only a committed Fern golden is.",
            width=76,
        )
    )
    return out


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", required=True, type=Path)
    parser.add_argument(
        "--tier",
        action="append",
        required=True,
        metavar="NAME=JSON=TESTS=EXPRESSION",
        help="a tier's name, llvm-cov JSON export, test count, and nextest filter",
    )
    parser.add_argument(
        "--golden-tier",
        required=True,
        help="which tier is the committed-golden one (drives the blind-spot report)",
    )
    parser.add_argument(
        "--subprocess-file",
        default="src/main.rs",
        help="a file reachable ONLY through the spawned binary",
    )
    parser.add_argument(
        "--subprocess-tier",
        action="append",
        default=[],
        help="tier that must show non-zero coverage of --subprocess-file",
    )
    args = parser.parse_args(argv)

    repo_root = args.repo_root.resolve()
    order: list[str] = []
    tiers: dict[str, dict[str, dict[Region, int]]] = {}
    selections: dict[str, tuple[str, int]] = {}
    for spec in args.tier:
        name, path, count, expression = spec.split("=", 3)
        order.append(name)
        tiers[name] = load_tier(Path(path), repo_root)
        selections[name] = (expression, int(count))

    drop_test_regions(tiers, repo_root)

    report, _ = render(tiers, order, selections)
    report.extend(blind_spots(tiers, args.golden_tier, order))

    report.append("")
    report.append(
        f"subprocess coverage proof — {args.subprocess_file} is compiled only into "
        "the spawned `crozier` binary, never into a test harness:"
    )
    failures: list[str] = []
    for name in order:
        counts = tiers[name].get(args.subprocess_file, {})
        covered = sum(1 for count in counts.values() if count > 0)
        report.append(f"  {name:<12} {covered} region(s) covered")
        if name in args.subprocess_tier and covered == 0:
            failures.append(name)
    print("\n".join(report))
    if failures:
        print(
            f"fixtures-coverage: no coverage of {args.subprocess_file} in tier(s) "
            f"{', '.join(failures)} — the spawned binary's profile was NOT captured, "
            f"so every e2e figure above understates reality. Check that "
            f"LLVM_PROFILE_FILE reaches the subprocess (cargo-llvm-cov sets it) and "
            f"that the e2e tests still run the built binary via assert_cmd.",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":  # pragma: no cover - exercised through the recipe
    raise SystemExit(main())
