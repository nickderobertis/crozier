"""Restate ledger-derived reach sections without measuring or generating an SDK."""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path
from typing import Protocol

import port_pins
import residual_attribution_record as attribution

INDEX = Path("docs/openapi-surface-coverage.md")
SURFACE = Path("docs/openapi-surface")


class LedgerRow(Protocol):
    @property
    def key(self) -> str: ...
    @property
    def region(self) -> str: ...
    @property
    def witnesses(self) -> tuple[str, ...]: ...
    @property
    def outside(self) -> tuple[str, ...]: ...
    @property
    def sites(self) -> tuple[tuple[str, int, int], ...]: ...
    @property
    def unreached_sites(self) -> int: ...
    @property
    def unreached(self) -> int: ...


class SupplementalProof(Protocol):
    @property
    def key(self) -> str: ...


class ReachReader(Protocol):
    def read_ledger(self, path: Path) -> list[tuple[int, LedgerRow]]: ...
    def golden_rows(self, regions_dir: Path) -> dict[str, str]: ...


class HandwrittenReader(Protocol):
    def output_insensitive_declarers(self, root: Path) -> tuple[dict[str, frozenset[str]], list[str]]: ...
    def read_residual_proofs(self, root: Path) -> tuple[list[SupplementalProof], list[str]]: ...


def summary(text: str, pattern: str, replacement: str, name: str) -> str:
    updated, count = re.subn(pattern, replacement, text)
    if count != 1:
        raise ValueError(f"{name}: restore exactly one summary, then run `just census-repin`")
    return updated


def table(text: str, heading: str, rows: list[str]) -> str:
    if text.count(heading) != 1:
        raise ValueError(f"{heading}: restore exactly one section, then run `just census-repin`")
    start = text.index(heading)
    end = text.find("\n#### ", start + len(heading))
    end = len(text) if end < 0 else end
    section = text[start:end]
    updated, count = re.subn(
        r"(\|[^\n]+\|\n\|[-| ]+\|\n)(?:\|[^\n]*\|\n)*", lambda match: match[1] + "".join(rows), section, count=1
    )
    if count != 1:
        raise ValueError(f"{heading}: restore the table header, then run `just census-repin`")
    return text[:start] + updated + text[end:]


def render(
    root: Path,
    text: str,
    ledger: list[tuple[int, LedgerRow]],
    golden: set[str],
    residual: set[str],
    vendored: set[str],
    insensitive: dict[str, frozenset[str]],
    supplemental: set[str],
) -> str:
    population = [(rank, row) for rank, row in ledger if row.key in golden and not row.key.startswith("combo-")]
    owned_heading = "#### The rows this measurement's first pass owned"
    if text.count(owned_heading) != 1:
        raise ValueError(f"{owned_heading}: restore exactly one ownership source, then run `just census-repin`")
    owned_section = text.partition(owned_heading)[2].split("\n#### ", 1)[0]
    owned = set(re.findall(r"^\|[^|]*\| `([^`]+)`", owned_section, re.M))
    ranking = []
    for rank, row in population:
        if row.unreached_sites:
            boundary = (
                "owned — first-pass search record below"
                if row.key in owned
                else "open — real-specification witness search remains open"
            )
            ranking.append(
                f"| {rank} | `{row.key}` | `{row.region}` | **{row.unreached_sites}** | **{row.unreached}** | **{len(row.witnesses)}** | {boundary} |\n"
            )
    text = table(text, "#### The reach ranking", ranking)
    one = [
        f"| `{row.key}` | `{row.region}` | `{row.witnesses[0]}` |\n"
        for _rank, row in population
        if len(row.witnesses) == 1
    ]
    text = table(text, "#### Rows resting on one document", one)
    text = summary(
        text,
        r"\*\*\d+\*\* golden rows rest on one document",
        f"**{len(one)}** golden rows rest on one document",
        "Rows resting on one document",
    )
    reaching = sum(not row.unreached_sites for _rank, row in ledger)
    text = summary(
        text,
        r"\*\*\d+\*\* golden rows reach every handling site",
        f"**{reaching}** golden rows reach every handling site",
        "The reach ranking",
    )
    witnessless_count = sum(not row.witnesses for _rank, row in population)
    text = summary(
        text,
        r"\*\*\d+\*\* golden rows have no golden-only witness",
        f"**{witnessless_count}** golden rows have no golden-only witness",
        "Golden rows with no golden-only witness",
    )
    text = table(
        text,
        "#### Golden rows with no golden-only witness",
        [
            f"| `{row.key}` | `{row.region}` | {', '.join(f'`{fixture}`' for fixture in row.outside)} |\n"
            for _rank, row in population
            if not row.witnesses
        ],
    )
    records = attribution.read(root)
    cells = []
    residual_count = 0
    for _rank, row in population:
        real = set(row.witnesses) - vendored - insensitive.get(row.key, frozenset())
        if not real or not real <= residual:
            continue
        residual_count += 1
        if row.key in supplemental:
            continue
        if len(real) != 1:
            raise ValueError(
                f"{row.key}: multiple residual witnesses need attribution; re-measure with `{attribution.REMEASURE}`"
            )
        cells.append(attribution.require(root, row.key, next(iter(real)), records).cell())
    text = summary(
        text,
        r"\*\*\d+\*\* golden rows rest only on residual golden witnesses",
        f"**{residual_count}** golden rows rest only on residual golden witnesses",
        "Golden rows resting only on residual goldens",
    )
    text = table(text, "#### Golden rows resting only on residual goldens", cells)
    unreached = Counter(
        spec.split("::", 1)[0] for _rank, row in population for spec, hit, _total in row.sites if not hit
    )
    total = sum(unreached.values())
    lines = []
    for line in text.splitlines(keepends=True):
        match = re.match(r"\| `(src/[^`]+\.rs)` \|", line)
        if match:
            line = re.sub(
                r" ?\d+ of \[the \d+ unreached arms\]\(#every-unreached-arm-and-its-search-verdict\) are in this file\.",
                "",
                line,
            )
            count = unreached[match[1]]
            if count:
                line = (
                    line.rstrip("\n").removesuffix(" |")
                    + f" {count} of [the {total} unreached arms](#every-unreached-arm-and-its-search-verdict) are in this file. |\n"
                )
        lines.append(line)
    return "".join(lines)


def generated(root: Path, reach: ReachReader, handwritten: HandwrittenReader) -> str:
    census = port_pins.census(root)
    registrations = census.golden_registrations(root / census.GOLDEN_REGISTRY)
    insensitive, errors = handwritten.output_insensitive_declarers(root)
    supplements, more = handwritten.read_residual_proofs(root)
    if errors or more:
        raise ValueError("; ".join(errors + more))
    path = root / INDEX
    return render(
        root,
        path.read_text(encoding="utf-8"),
        reach.read_ledger(root / SURFACE / "golden-reach.tsv"),
        set(reach.golden_rows(root / SURFACE)),
        {name for name, registration in registrations.items() if registration.unmatched},
        {path.parent.name for path in (root / "tests/fixtures").glob("*/openapi.*")},
        insensitive,
        {item.key for item in supplements},
    )


def stale_sections(root: Path, reach: ReachReader, handwritten: HandwrittenReader) -> list[str]:
    before = (root / INDEX).read_text(encoding="utf-8")
    after = generated(root, reach, handwritten)
    stale = []

    def section(text: str, heading: str) -> str:
        return text.partition("#### " + heading)[2].split("\n#### ", 1)[0]

    for heading in (
        "The reach ranking",
        "Rows resting on one document",
        "Golden rows with no golden-only witness",
        "Golden rows resting only on residual goldens",
    ):
        if section(before, heading) != section(after, heading):
            stale.append(heading)
    if re.findall(r"^\| `src/[^`]+\.rs` \|.*$", before, re.MULTILINE) != re.findall(
        r"^\| `src/[^`]+\.rs` \|.*$", after, re.MULTILINE
    ):
        stale.append("Blind-spot rows' unreached-arm counts")
    return stale


def rewrite(root: Path, reach: ReachReader, handwritten: HandwrittenReader) -> None:
    (root / INDEX).write_text(generated(root, reach, handwritten), encoding="utf-8", newline="\n")
