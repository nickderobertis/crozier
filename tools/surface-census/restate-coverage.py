#!/usr/bin/env python3
"""Restate category totals and the FIXTURE ranking without re-measuring coverage.

Exit status: 0 on success, 1 on drift or input/write failure, 2 on usage errors.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import io
import json
import re
import sys
import textwrap
from collections import Counter
from enum import StrEnum
from pathlib import Path
from types import ModuleType
from typing import NamedTuple

REPO = Path(__file__).resolve().parents[2]


class Settlement(StrEnum):
    FIXTURE = "FIXTURE"
    PROBE = "PROBE"
    UNREACHABLE = "UNREACHABLE"


SETTLEMENTS = tuple(Settlement)


class CategoryRow(NamedTuple):
    region: str
    key: str
    category: str
    evidence: str
    sites: str
    artifacts: str
    settlement: str


class Totals(NamedTuple):
    total: int
    golden: int
    limitations: int
    handwritten: int
    gap: int
    fixture: int
    probe: int
    unreachable: int


class Score(NamedTuple):
    sites: int
    blind: int
    artifacts: int
    witnesses: int


class Ranked(NamedTuple):
    order: tuple[int, int, int, int, str]
    row: str
    score: Score
    has_file: bool


class Reach(NamedTuple):
    witnesses: str
    unreached_sites: int


ARTIFACTS = ("types/", "client.py", "raw_client.py", "errors/", "reference.md", "core/")
SOURCE = r"src/(?:[a-z_]+/)*[a-z_]+\.rs"


def reader(filename: str = "witness-search-region-keys.py") -> ModuleType:
    """Use the region parser shared by the census and its gate."""
    path = Path(__file__).with_name(filename)
    spec = importlib.util.spec_from_file_location("coverage_region_reader", path)
    if spec is None or spec.loader is None:
        raise ValueError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def decided_keys(root: Path) -> set[str]:
    """Keys the shared table decides output-insensitive as a whole (context `-`).

    Such a `gap` row is neither proven nor unproven; any invalid evidence or a
    key also claimed proven refuses the restatement rather than counting it.
    """
    path = Path(__file__).with_name("output-insensitive.py")
    spec = importlib.util.spec_from_file_location("coverage_output_insensitive", path)
    if spec is None or spec.loader is None:
        raise ValueError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    try:
        records, failures = module.read_records(root)
    except SystemExit as error:
        raise ValueError(str(error)) from error
    if failures:
        raise ValueError("; ".join(failures))
    return {key for key, context in records if context == "-"}


def substitute(text: str, pattern: str, replacement: str) -> str:
    """Refuse a changed document layout rather than silently leaving stale totals."""
    result, count = re.subn(pattern, lambda _match: replacement, text, count=1, flags=re.M | re.S)
    if count != 1:
        raise ValueError(f"coverage index no longer matches {pattern!r}")
    return result


def source_counts(root: Path) -> tuple[int, int, int]:
    """Use the census's source discovery, without parsing or re-measuring specs."""
    path = Path(__file__).with_name("openapi-surface-census.py")
    spec = importlib.util.spec_from_file_location("coverage_source_reader", path)
    if spec is None or spec.loader is None:
        raise ValueError(f"cannot load {path}")
    census = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = census
    spec.loader.exec_module(census)
    fixtures = root / "tests/fixtures"
    if not fixtures.is_dir():
        raise ValueError("tests/fixtures is missing; restore the source population before restating")
    try:
        acquired = census.acquisition_sources(fixtures, fixtures / "corpus-sources", False)
        sources = census.registered_sources(fixtures, fixtures / "corpus-sources", False)
    except SystemExit as error:
        raise ValueError(str(error)) from error
    aliases = census.corpus_aliases(fixtures)
    golden = sum((fixtures / aliases.get(source.fixture, source.fixture) / "expected").is_dir() for source in sources)
    return len(acquired), len(sources), golden


def validate_reach_population(keys: set[str], features: set[str], combinations: set[str]) -> None:
    """Require each measured population in full, without counting combinations as features."""
    prefix = reader().COMBINATION_PREFIX
    for label, expected, actual in (
        ("feature", features, {key for key in keys if not key.startswith(prefix)}),
        ("combination", combinations, {key for key in keys if key.startswith(prefix)}),
    ):
        if actual != expected:
            raise ValueError(
                f"golden-reach.tsv: {label} keys must equal the golden category population; "
                f"missing {sorted(expected - actual)}, extra {sorted(actual - expected)}"
            )


COMBINATION_SENTENCE = (
    r"\*\*Feature combinations are counted apart\.\*\* \d+ combinations are selected\s+"
    r"\(\[the list\]\(openapi-surface/combinations\.md\)\): [^\n.]+\.\n"
    r"\d+ of the `gap` ones (?:is|are) decided output-insensitive in\n"
    r"\[the shared table\]\(openapi-surface/output-insensitive\.tsv\), neither proven nor unproven\."
)


def combination_categories(root: Path) -> tuple[Counter[str], int]:
    """Read combinations apart from features, using the shared category parser.

    Returns every category the combination rows carry, and how many of their
    `gap` rows the shared table decides output-insensitive as a whole.
    """
    parser = reader()
    decided = decided_keys(root)
    settled = 0
    index = root / "docs/openapi-surface-coverage.md"
    categories: Counter[str] = Counter()
    seen: set[str] = set()
    for name in parser.region_files(index):
        text = (root / "docs/openapi-surface" / name).read_text(encoding="utf-8")
        # `region_rows` drops a row it cannot parse; a combination row it drops
        # would leave the population short, so each combination-keyed line
        # must parse on its own.
        for line in text.splitlines():
            key = line.removeprefix("| ").partition(" |")[0].strip("`")
            if line.startswith("| ") and key.startswith(parser.COMBINATION_PREFIX) and not parser.region_rows(line):
                raise ValueError(f"{name}: combination row {key} is not an eight-cell row with a known category")
        for cells in parser.region_rows(text):
            key = cells[0].strip("`")
            if not key.startswith(parser.COMBINATION_PREFIX):
                continue
            if key in seen:
                raise ValueError(f"duplicate combination row {key}")
            seen.add(key)
            categories[cells[3].strip("`")] += 1
            settled += cells[3].strip("`") == "gap" and key in decided
    if not categories:
        raise ValueError("no combination region rows")
    return categories, settled


COMBINATION_PROOF_SENTENCE = r"\*\*Combinations by proof\.\*\*.*?= \d+\."
NAMED_COMBINATIONS_HEADING = "#### Unproven combinations, named"


class ProofSplit(NamedTuple):
    real: int
    cooccurrence: int
    measured: int
    handwritten: int
    unproven: int
    decided: int
    # Of `handwritten`, the rows whose fixture's cover reads `witness-blocked`.
    blocked: int = 0
    # Of `unproven`, the rows the named table leaves unproven by the user's ruling.
    ruled: int = 0
    # Of `handwritten`, the rows no crozier branch reads both features of, which
    # rest on their fixture apart from real-specification co-occurrence.
    together: int = 0

    @property
    def classes(self) -> tuple[int, ...]:
        """The six classes that sum to every selected combination."""
        return (self.real, self.cooccurrence, self.measured, self.handwritten, self.unproven, self.decided)


def witness_blocked_keys(root: Path) -> set[str]:
    """Combination keys a hand-written fixture's feature-level cover reads `witness-blocked` for."""
    gate = reader("handwritten-fixtures.py")
    keys = set()
    for path in sorted((root / gate.HANDWRITTEN).glob("*/evidence.toml")):
        fixture, _failures = gate.read_evidence(path.parent)
        if fixture is not None:
            keys |= {cover.key for cover in fixture.covers if cover.verdict == "witness-blocked" and cover.arm is None}
    return keys


def user_ruled_combinations(root: Path) -> set[str]:
    """Keys the `Unproven combinations, named` table leaves unproven by the user's ruling.

    The gate (`finished_state_failures`) holds the reason's form; this only counts it.
    """
    text = (root / "docs/openapi-surface-coverage.md").read_text(encoding="utf-8")
    if NAMED_COMBINATIONS_HEADING not in text:
        return set()
    body = text.split(NAMED_COMBINATIONS_HEADING, 1)[1].split("\n#", 1)[0]
    return set(re.findall(r"^\| `(combo-[^`]+)` \| [^|]+ \| `?user ruling`? — ", body, re.M))


def combination_proofs(root: Path) -> ProofSplit:
    """Split the combination rows by the proof each rests on.

    A `golden` row is a real-specification byte-match only when the reach ledger
    names a golden-only witness for it and reports every interaction site reached;
    one whose site cell is `co-occurrence` is counted apart, since no crozier
    branch reads both its features. One with no witness, no ledger row or an
    unreached interaction site is unproven. A `limitations` row and an undecided
    `UNREACHABLE` gap rest on a committed measurement of non-generation; a gap the
    shared table decides is neither proven nor unproven; every other gap is unproven.
    """
    parser = reader()
    decided = decided_keys(root)
    surface = root / "docs/openapi-surface"
    try:
        ledger = {
            reach.key: reach for _rank, reach in reader("golden-reach.py").read_ledger(surface / "golden-reach.tsv")
        }
    except SystemExit as error:
        raise ValueError(str(error)) from error
    blocked = witness_blocked_keys(root)
    ruled = user_ruled_combinations(root)
    try:
        table = reader("golden-reach.py").read_sites_table(surface / "golden-reach-sites.tsv")
    except SystemExit as error:
        raise ValueError(str(error)) from error
    split: Counter[str] = Counter()
    for name in parser.region_files(root / "docs/openapi-surface-coverage.md"):
        for cells in parser.region_rows((surface / name).read_text(encoding="utf-8")):
            key = cells[0].strip("`")
            if not key.startswith(parser.COMBINATION_PREFIX):
                continue
            category = cells[3].strip("`")
            settlement = cells[7].lstrip("`*").split(" ", 1)[0].strip("`*—")
            reach = ledger.get(key)
            match category:
                case "golden" if reach is not None and reach.witnesses and reach.cooccurrence:
                    split["cooccurrence"] += 1
                case "golden" if reach is not None and reach.witnesses and reach.sites and not reach.unreached_sites:
                    split["real"] += 1
                case "golden":
                    split["unproven"] += 1
                case "handwritten":
                    split["handwritten"] += 1
                    split["blocked"] += key in blocked
                    split["together"] += key in table and table[key].cooccurrence
                case "limitations":
                    split["measured"] += 1
                case _ if key in decided:
                    split["decided"] += 1
                case _ if settlement == Settlement.UNREACHABLE:
                    split["measured"] += 1
                case _:
                    split["unproven"] += 1
                    split["ruled"] += key in ruled
    return ProofSplit(*(split[field] for field in ProofSplit._fields))


def restate_combinations(root: Path, text: str) -> str:
    """Restate only the combination sentences; category vocabulary comes from rows."""
    categories, decided = combination_categories(root)
    parts = [f"{count} are `{category}`" for category, count in sorted(categories.items())]
    counts = ", ".join(parts[:-1]) + " and " + parts[-1] if len(parts) > 1 else parts[0]
    text = substitute(
        text,
        COMBINATION_SENTENCE,
        f"**Feature combinations are counted apart.** {sum(categories.values())} combinations are selected\n"
        f"([the list](openapi-surface/combinations.md)): {counts}.\n"
        f"{decided} of the `gap` ones {'is' if decided == 1 else 'are'} decided output-insensitive in\n"
        "[the shared table](openapi-surface/output-insensitive.tsv), neither proven nor unproven.",
    )
    split = combination_proofs(root)
    return substitute(
        text,
        COMBINATION_PROOF_SENTENCE,
        "**Combinations by proof.** A combination is proven only where the run that byte-matches Fern\n"
        "executes the branch where its two features meet. `finished_state_failures` in\n"
        "[the census suite](../tools/surface-census/tests/surface_census_test.py) holds that bar, with\n"
        "[the hand-written fixture format](openapi-surface/handwritten/AGENTS.md) it reads.\n"
        f"**{split.real}** are byte-matched against a registered real specification at their\n"
        f"interaction branch, **{split.cooccurrence}** "
        f"{'is a byte-matched co-occurrence' if split.cooccurrence == 1 else 'are byte-matched co-occurrences'}, "
        "where no crozier branch reads both features\n"
        "([the audit](openapi-surface/combination-cooccurrence.tsv)), "
        f"**{split.measured}** {'is' if split.measured == 1 else 'are'} compared against a committed measurement of\n"
        f"non-generation, **{split.handwritten}** rest on a hand-written fixture "
        f"({split.blocked} of them witness-blocked, {split.together} of them co-occurrences proven on the "
        f"fixture), **{split.unproven}** "
        f"{'remains' if split.unproven == 1 else 'remain'}\nunproven, each named below "
        f"({split.ruled} left unproven by the user's ruling), and **{split.decided}** "
        f"{'is' if split.decided == 1 else 'are'} decided output-insensitive: "
        f"{' + '.join(map(str, split.classes))} = {sum(split.classes)}.",
    )


def combination_headline_failures(root: Path) -> list[str]:
    """Require the whole category/count mapping, including the total and grammar."""
    text = (root / "docs/openapi-surface-coverage.md").read_text(encoding="utf-8")
    expected = restate_combinations(root, text)
    return [] if text == expected else ["combination headline differs from the complete region category counts"]


def restate(root: Path) -> str:
    """Derive tables from category rows and the committed blind-spot measurement."""
    index = root / "docs/openapi-surface-coverage.md"
    text = restate_combinations(root, index.read_text(encoding="utf-8"))
    acquired, registered, golden_sources = source_counts(root)
    text = substitute(
        text,
        r"  acquires \d+ sources.*?evidence only\.",
        f"  acquires {acquired} sources. The walk reads the\n"
        f"  **{registered}** registered sources, of which **{golden_sources}** carry a committed golden; "
        f"the {acquired - registered}\n  others carry none and are acquisition evidence only.",
    )
    parser = reader()
    reach_reader = reader("golden-reach.py")
    decided = decided_keys(root)
    entries: dict[str, CategoryRow] = {}
    golden_combinations: set[str] = set()
    counts: dict[str, Totals] = {}
    gaps: dict[str, list[str]] = {name: [] for name in SETTLEMENTS}
    for name in parser.region_files(index):
        region = Path(name).stem
        region_text = (index.parent / "openapi-surface" / name).read_text(encoding="utf-8")
        candidates = [
            line
            for line in region_text.splitlines()
            if re.match(r"^\| [^|]+ \| (?:both|3\.[01](?:\.x)?|OAS[^|]*) \|", line)
        ]
        rows = parser.region_rows(region_text)
        if len(candidates) != len(rows):
            raise ValueError(f"{name}: malformed category row")
        for row in rows:
            if row[0].strip("`").startswith(parser.COMBINATION_PREFIX) and row[3].strip("`") == "golden":
                key = row[0].strip("`")
                if key in golden_combinations:
                    raise ValueError(f"duplicate category row: {key}")
                golden_combinations.add(key)
        rows = [row for row in rows if not row[0].strip("`").startswith(parser.COMBINATION_PREFIX)]
        categories = Counter(row[3].strip("`") for row in rows)
        settlements: Counter[str] = Counter()
        for cells in rows:
            key = cells[0].strip("`")
            if key in entries:
                raise ValueError(f"duplicate category row: {key}")
            entries[key] = CategoryRow(region, key, cells[3].strip("`"), cells[4], cells[5], cells[6], cells[7])
            if cells[3].strip("`") == "gap":
                settlement = cells[7].lstrip("`*").split(" ", 1)[0].strip("`*—")
                if settlement not in gaps:
                    raise ValueError(f"{key}: unknown settlement {settlement}")
                gaps[settlement].append(key)
                settlements[settlement] += 1
        counts[region] = Totals(
            len(rows),
            *[categories[c] for c in parser.CATEGORIES],
            *[settlements[s] for s in SETTLEMENTS],
        )
    totals = Totals(*(sum(column) for column in zip(*counts.values(), strict=True)))
    for region, numbers in counts.items():
        text = substitute(
            text,
            rf"^\| \[`{re.escape(region)}`\][^\n]+$",
            f"| [`{region}`](openapi-surface/{region}.md) | " + " | ".join(map(str, numbers)) + " |",
        )
    text = substitute(
        text, r"^\| \*\*total\*\* \|[^\n]+$", "| **total** | " + " | ".join(f"**{n}**" for n in totals) + " |"
    )
    total, golden, limitations, handwritten, gap, fixture, probe, unreachable = totals
    # A `gap` row the shared table decides at `-` leaves the unproven and
    # committed-proof counts for its own; its region tallies keep the category.
    settled = {key for key, entry in entries.items() if entry.category == "gap" and key in decided}
    fixture -= len(settled & set(gaps["FIXTURE"]))
    unreachable_open = unreachable - len(settled & set(gaps["UNREACHABLE"]))
    gaps["FIXTURE"] = [key for key in gaps["FIXTURE"] if key not in settled]
    text = substitute(
        text,
        r"The walk enumerated \*\*\d+\*\* features.*?`UNREACHABLE`\.",
        f"The walk enumerated **{total}** features and landed each in exactly one category:\n"
        f"**{golden}** `golden`, **{limitations}** `limitations`, **{handwritten}** `handwritten`, **{gap}** `gap`. "
        f"The `gap` column splits by\nsettlement class into **{fixture}** `FIXTURE`, **{probe}** `PROBE` and **{unreachable}** `UNREACHABLE`.",
    )
    join_header = "| `src/` file | printed | by tier | ranked gaps pointing at it | verdict |"
    join = text.partition(join_header)[2].partition("**Where the two backlogs agree.")[0]
    blind = {match[0]: int(match[1]) for match in re.findall(rf"^\| `({SOURCE})` \| (\d+) \|", join, re.M)}
    if not blind:
        raise ValueError("the committed blind-spot table is missing")
    ranked: list[Ranked] = []
    pointing: Counter[str] = Counter()
    for key in gaps["FIXTURE"]:
        entry = entries[key]
        region = entry.region
        sites = [
            (path, int(n)) for path, n in re.findall(rf"({SOURCE})`?(?!:\d)[^0-9A-Za-z]{{0,14}}(\d+)", entry.sites)
        ]
        if sorted(path for path, _count in sites) != sorted(re.findall(SOURCE, entry.sites.partition(" — ")[0])):
            raise ValueError(f"{key}: crozier sites has an unmeasured source file")
        if not sites and not entry.sites.lstrip("`").startswith("none"):
            raise ValueError(f"{key}: crozier sites has no measured count")
        missing = [path for path, _n in sites if path not in blind]
        if missing:
            raise ValueError(f"{key}: no committed blind-spot measurement for {missing}")
        artifacts = [name for name in ARTIFACTS if re.search(r"(?<![\w])" + re.escape(name), entry.artifacts)]
        if not artifacts:
            raise ValueError(f"{key}: artifact cell names none of {ARTIFACTS}")
        witness = re.search(r":\s*(\d+) declarations", entry.evidence)
        if witness is None:
            raise ValueError(f"{key}: evidence has no measured declaration count")
        score = Score(sum(n for _p, n in sites), sum(blind[p] for p, _n in sites), len(artifacts), int(witness[1]))
        pointing.update({path for path, _n in sites})
        own = ", ".join(f"`{path}` {n}" for path, n in sites) or "none"
        reach = ", ".join(f"`{path}` {blind[path]}" for path, _n in sites) or "none"
        row = (
            f"[`{key}`](openapi-surface/{region}.md) | `{region}` | **{score.sites}** ({own}) | "
            f"**{score.blind}** ({reach}) | **{score.artifacts}** ({', '.join(artifacts)}) | **{score.witnesses}** |"
        )
        ranked.append(
            Ranked((score.sites, -score.blind, -score.artifacts, -score.witnesses, key), row, score, bool(sites))
        )
    ranked.sort()
    table = "| # | key | region | 1. crozier sites | 2. blind spots | 3. artifacts | 4. witnesses |\n|---|---|---|---|---|---|---|\n"
    table += "\n".join(f"| {rank} | {row}" for rank, (_order, row, _score, _has_file) in enumerate(ranked, 1))
    text = substitute(
        text,
        r"^\| # \| key \| region \| 1\. crozier sites[^\n]*\n\|---[^\n]*\n(?:\|[^\n]*\n)*",
        table.rstrip("\n") + "\n",
    )
    text = substitute(text, r"All \d+ `FIXTURE` gaps", f"All {fixture} `FIXTURE` gaps")
    zero_witness = sum(score.witnesses == 0 for _order, _row, score, _has_file in ranked)
    text = substitute(
        text,
        r"(?:\d+ of the \d+ score zero|no ranked witnesses remain)",
        f"{zero_witness} of the {fixture} score zero" if fixture else "no ranked witnesses remain",
    )
    no_file = sum(not entry.has_file for entry in ranked)
    no_blind = sum(entry.score.blind == 0 for entry in ranked)
    values = sorted(score.blind for _order, _row, score, _has_file in ranked)
    median = (values[(len(values) - 1) // 2] + values[len(values) // 2]) // 2 if values else None
    if median is None:
        narrative = "The ranked backlog is empty.\n"
    else:
        named = ", ".join(f"{n} entries name `{path}`" for path, n in sorted(pointing.items()))
        narrative = (
            f"**The median blind-spot count of this list is {median}** — {named}. "
            f"{no_file} of the {fixture} entries name no `src/` file at all. "
            f"{no_blind} of the {fixture} ranked entries reach no blind region. "
            "The table follows the five criteria above.\n"
        )
    text = substitute(
        text,
        r"(?:\*\*The median blind-spot count of this list is \d+\*\*|The ranked backlog is empty\.).*?(?=\n\| # \| key)",
        narrative,
    )
    lines = []
    in_join = False
    for line in text.splitlines():
        if line == join_header:
            in_join = True
        elif line.startswith("**Where the two backlogs agree."):
            in_join = False
        match = re.match(rf"^\| `({SOURCE})` \|", line)
        if in_join and match:
            cells = line.split("|")
            if len(cells) != 7:
                raise ValueError(f"{match[1]}: truncated blind-spot table row")
            cells[4] = f" {pointing[match[1]]} (ranked `FIXTURE` gaps) " if pointing[match[1]] else " none "
            cells[5] = re.sub(
                r"(?:Seven|\d+) (?:named example|ranked feature) gaps point here;",
                f"{pointing[match[1]]} ranked feature gaps point here;",
                cells[5],
            )
            line = "|".join(cells)
        lines.append(line)
    text = "\n".join(lines) + "\n"
    sources = (
        ", ".join(f"{n} gaps point at `{path}`" for path, n in sorted(pointing.items())) or "no ranked gaps remain"
    )
    text = substitute(
        text,
        r"\*\*Where the two backlogs agree\.\*\*.*?(?=\n\n\*\*Where they do not)",
        f"**Where the two backlogs agree.** {sources}. Criterion 2 reads the committed printed counts above; "
        "per-arm proof and refusal measurements remain independent of the feature backlog.",
    )
    # Only feature totals change here. Arm measurements remain golden-reach's.
    surface = index.parent / "openapi-surface"
    ledger: dict[str, Reach] = {}
    with (surface / "golden-reach.tsv").open(encoding="utf-8", newline="") as handle:
        records = csv.DictReader((line for line in handle if not line.startswith("#")), delimiter="\t")
        if not records.fieldnames or not {"key", "witnesses", "unreached_sites"}.issubset(records.fieldnames):
            raise ValueError("golden-reach.tsv: missing key/witnesses header")
        for row in records:
            if None in row or any(value is None for value in row.values()) or not row["key"]:
                raise ValueError("golden-reach.tsv: incomplete record")
            if row["key"] in ledger:
                raise ValueError(f"golden-reach.tsv: duplicate key {row['key']}")
            if not row["unreached_sites"].isascii() or not row["unreached_sites"].isdigit():
                raise ValueError(f"golden-reach.tsv: invalid unreached_sites for {row['key']}")
            ledger[row["key"]] = Reach("" if row["witnesses"] == "-" else row["witnesses"], int(row["unreached_sites"]))
    golden_keys = {key for key, entry in entries.items() if entry.category == "golden"}
    try:
        listed = set(reach_reader.read_sites_table(surface / "golden-reach-sites.tsv"))
    except SystemExit as error:
        raise ValueError(str(error)) from error
    measured_combinations = {
        key for key in reach_reader.measured_rows(surface, listed) if key.startswith(parser.COMBINATION_PREFIX)
    }
    validate_reach_population(set(ledger), golden_keys, golden_combinations | measured_combinations)
    ledger = {key: reach for key, reach in ledger.items() if key in golden_keys}
    one = [
        f"| `{key}` | `{entries[key].region}` | `{reach.witnesses}` |"
        for key, reach in ledger.items()
        if reach.witnesses and "," not in reach.witnesses
    ]
    thin_heading = "#### Rows resting on one document"
    if text.count(thin_heading) != 1:
        raise ValueError("missing one-document witness section")
    before, _, remaining = text.partition(thin_heading)
    section, following, tail = remaining.partition("\n#### ")
    section = substitute(
        section,
        r"\*\*\d+\*\* golden rows rest on one document",
        f"**{len(one)}** golden rows rest on one document",
    )
    header = "| key | region | only golden-only witness |\n|---|---|---|\n"
    section = substitute(section, re.escape(header) + r"(?:\|[^\n]*\|\n)*", header + "\n".join(one) + "\n")
    text = before + thin_heading + section + following + tail
    reaching = sum(reach.unreached_sites == 0 for reach in ledger.values())
    text = substitute(
        text,
        r"\*\*\d+\*\* golden rows reach every handling site",
        f"**{reaching}** golden rows reach every handling site",
    )
    heading = "#### Golden rows resting only on residual goldens"
    if heading not in text:
        raise ValueError("missing residual-golden section")
    residual_section = text.partition(heading)[2].split("\n#", 1)[0]
    residual_rows = [line for line in residual_section.splitlines() if line.startswith("| `")]
    if any(
        len(line.split("|")) != 6 or not re.search(r"\| `(?:open gap|proven|split)` \|$", line)
        for line in residual_rows
    ):
        raise ValueError("malformed residual-golden row")
    residual_keys = [line.split("|")[1].strip().strip("`") for line in residual_rows]
    if len(set(residual_keys)) != len(residual_keys):
        raise ValueError("duplicate residual-golden key")
    if any(key not in entries or entries[key].category != "golden" for key in residual_keys):
        raise ValueError("residual-golden key is not a golden category row")
    residual = set(re.findall(r"^\| `([^`]+)` \|[^\n]*\| `open gap` \|$", residual_section, re.M))
    witnessless = {key for key, entry in entries.items() if entry.category == "golden" and not ledger[key].witnesses}
    if set(residual_keys) & witnessless:
        raise ValueError("residual-golden and witnessless populations overlap")
    spec = importlib.util.spec_from_file_location(
        "coverage_handwritten", Path(__file__).with_name("handwritten-fixtures.py")
    )
    if spec is None or spec.loader is None:
        raise ValueError("cannot load hand-written proof reader")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    supplements, failures = module.read_residual_proofs(root)
    if failures:
        raise ValueError("; ".join(failures))
    supplemental = {proof.key for proof in supplements}
    if supplemental & (set(residual_keys) | witnessless) or any(
        key not in entries or entries[key].category != "golden" for key in supplemental
    ):
        raise ValueError("supplemental proof must name a separate witnessed golden row")
    weak = handwritten + len(supplemental)
    header = "| key | fixture | byte-matched file | proof | real-CLI journey |\n|---|---|---|---|---|\n"
    table = "\n".join(
        f"| `{proof.key}` | `{proof.fixture}` | `{proof.file}` | `{proof.mode}` | `{proof.test}` |"
        for proof in supplements
    )
    if supplements:
        text = substitute(text, re.escape(header) + r"(?:\|[^\n]*\|\n)*", header + table + "\n")
    no_witness = len(witnessless)
    real = golden - len(residual) - no_witness - len(supplemental)
    proof = limitations + unreachable_open
    unproven = fixture + len(residual) + no_witness
    text = substitute(
        text,
        r"The walk enumerates \d+ features\. By category,.*?`gap`\.",
        f"The walk enumerates {total} features. By category, {golden} are `golden`, {limitations}\n`limitations`, {handwritten} `handwritten` and {gap} `gap`.",
    )
    text = substitute(text, r"those \d+\nsplit five ways", f"those {total}\nsplit five ways")
    text = substitute(text, r"\*\*\d+ carry byte-match evidence", f"**{real} carry byte-match evidence")
    text = substitute(text, r"\*\*\d+ carry a committed Fern", f"**{proof} carry a committed Fern")
    text = substitute(text, r"\*\*\d+ rest on a hand-written fixture", f"**{weak} rest on a hand-written fixture")
    text = substitute(text, r"They are not among the\s+\d+", f"They are not among the\n  {real}")
    feature_keys = ", ".join(f"`{key}`" for key in sorted(gaps["FIXTURE"]))
    residual_keys = ", ".join(f"`{key}`" for key in sorted(residual))
    feature_text = f"{feature_keys}. " if feature_keys else ""
    residual_verb = "is a `golden` row" if len(residual) == 1 else "are `golden` rows"
    remainder = (
        f"- **{unproven} remain unproven.** {fixture} are the `FIXTURE` `gap` rows. "
        "Their outstanding evidence is recorded in [Unproven features, named](#unproven-features-named). "
        f"{feature_text}{len(residual)} {residual_verb} resting only on residual goldens whose code moves no "
        f"byte-matched file: {residual_keys} "
        "([the attribution](#golden-rows-resting-only-on-residual-goldens)). "
        f"The other {no_witness} are `golden` rows declared only by corpus rows that carry no golden "
        "([the list](#golden-rows-with-no-golden-only-witness))."
    )
    settled_keys = ", ".join(f"`{key}`" for key in sorted(settled))
    decided_text = (
        f"- **{len(settled)} {'is' if len(settled) == 1 else 'are'} decided output-insensitive.** "
        "Deleting the feature leaves both generators' complete trees byte-identical, as "
        "[the shared table](openapi-surface/output-insensitive.tsv) records for the whole key; "
        "such a `gap` row is neither proven nor unproven" + (f": {settled_keys}." if settled else ".")
    )

    def fill(paragraph: str) -> str:
        return textwrap.fill(
            paragraph, width=88, subsequent_indent="  ", break_long_words=False, break_on_hyphens=False
        )

    text = substitute(
        text,
        r"- \*\*\d+ (?:is|are) decided output-insensitive\.\*\*.*?(?=\n- \*\*\d+ remain unproven)",
        fill(decided_text),
    )
    text = substitute(
        text,
        r"- \*\*\d+ remain unproven\.\*\*.*?(?=\n\n\d+ \+)",
        fill(remainder),
    )
    text = substitute(
        text,
        r"^\d+ \+ \d+ \+ \d+ \+ \d+ \+ \d+ = \d+\.$",
        f"{real} + {proof} + {weak} + {len(settled)} + {unproven} = {total}.",
    )
    text = substitute(
        text,
        r"None is among the \d+ features above, and each other `gap` one is named under",
        f"None is among the {total} features above, and each other `gap` one is named under",
    )
    text = substitute(
        text,
        r"(\*\*What the `gap` count means\.\*\*).*?(?=\n### Reconciliation)",
        f"**What the `gap` count means.** {gap} is the number of OpenAPI shapes no committed\n"
        "golden's source declares and no hand-written fixture covers, so no byte\n"
        f"comparison touches them. The gate is green over all {gap} either way, and it\n"
        f"is not a defect count. {unreachable} of them (`UNREACHABLE`) have no position in a\n"
        "generated Python SDK, each proved so by a committed differential pair\n"
        "that crozier is byte-compared against. The other "
        f"{gap - unreachable} need byte-match proof; their current\n"
        "search evidence and outstanding candidates are recorded in\n"
        "[Unproven features, named](#unproven-features-named), ranked in\n"
        "[the ranked backlog](#the-ranked-fixture-backlog).\n\n",
    )
    return text


class SnapshotOrigin(StrEnum):
    VENDORED = "vendored"
    CORPUS = "corpus"


class SnapshotSource(NamedTuple):
    fixture: str
    origin: SnapshotOrigin


class SnapshotCell(NamedTuple):
    selector: str
    fixture: str
    count: int


def document_snapshot(root: Path, payload: object) -> dict[Path, str]:
    """Render census cells from one native JSON walk before writing anything."""
    if (
        not isinstance(payload, dict)
        or not isinstance(payload.get("sources"), list)
        or not isinstance(payload.get("rows"), list)
    ):
        raise ValueError("snapshot needs native census JSON sources and rows")
    sources: dict[str, SnapshotSource] = {}
    for source in payload["sources"]:
        if (
            not isinstance(source, dict)
            or not isinstance(source.get("fixture"), str)
            or not source["fixture"]
            or not isinstance(source.get("origin"), str)
            or source["origin"] not in {"vendored", "corpus"}
        ):
            raise ValueError("invalid snapshot source")
        parsed_source = SnapshotSource(source["fixture"], SnapshotOrigin(source["origin"]))
        if parsed_source.fixture in sources:
            raise ValueError("duplicate snapshot source")
        sources[parsed_source.fixture] = parsed_source
    measured: dict[str, dict[str, int]] = {}
    for row in payload["rows"]:
        if (
            not isinstance(row, dict)
            or not isinstance(row.get("selector"), str)
            or not row["selector"]
            or not isinstance(row.get("fixture"), str)
            or row["fixture"] not in sources
            or type(row.get("count")) is not int
            or row["count"] <= 0
        ):
            raise ValueError("invalid snapshot census row")
        parsed_cell = SnapshotCell(row["selector"], row["fixture"], row["count"])
        counts = measured.setdefault(parsed_cell.selector, {})
        if parsed_cell.fixture in counts:
            raise ValueError("duplicate snapshot census row")
        counts[parsed_cell.fixture] = parsed_cell.count
    if not sources or "openapi.paths" not in measured:
        raise ValueError("snapshot has no registered sources or paths measurement")
    prefixes = {
        "OpenAPI Object": "openapi",
        "Info Object": "info",
        "Contact Object": "info.contact",
        "License Object": "info.license",
        "Server Object": "server",
        "Server Variable Object": "server.variables",
        "Path Item Object": "pathItem",
        "Operation Object": "operation",
        "Tag Object": "tag",
        "External Documentation Object": "externalDocs",
        "Components Object": "components",
        "Reference Object": "reference",
    }
    special = {
        "operation-id-digit-leading-method": "operation.operationId:digit-leading-method",
        "pathitem-ref": "pathItem.$ref",
        "relative-file-ref": "pathItem.$ref:relative-file",
        "nonascii-info-title": "info.title:non-ascii",
        "multi-tagged-operation": "operation.tags:multiple",
        "templated-path-segment": "openapi.paths:templated-key",
        "several-path-template-variables": "openapi.paths:several-template-expressions",
        "path-leading-literal-segment": "openapi.paths:leading-literal-segment",
        "path-template-before-literal-segment": "openapi.paths:template-before-literal-segment",
        "path-all-segments-templated": "openapi.paths:all-segments-templated",
    }
    methods = [f"pathItem.{method}" for method in ("get", "put", "post", "delete", "options", "head", "patch", "trace")]
    for key, field in (("missing-operation-id", "operation.operationId"), ("untagged-operation", "operation.tags")):
        measured[key] = {
            name: count
            for name in sources
            if (
                count := sum(measured.get(method, {}).get(name, 0) for method in methods)
                - measured.get(field, {}).get(name, 0)
            )
        }
        special[key] = key
    paths = set(measured["openapi.paths"])
    webhooks = set(measured.get("openapi.webhooks", {}))
    measured["paths-absent"] = dict.fromkeys(sorted(sources.keys() - paths), 1)
    measured["webhooks-without-paths"] = dict.fromkeys(sorted(webhooks - paths), 1)
    ignored: Counter[str] = Counter()
    for selector in (
        "operation.x-fern-ignore",
        "operation.x-crozier-ignore",
        "schema.x-fern-ignore",
        "schema.x-crozier-ignore",
    ):
        ignored.update(measured.get(selector, {}))
    measured["x-fern-or-crozier-ignore"] = dict(ignored)
    extension_selectors = {
        "json-schema-dialect": "openapi.jsonSchemaDialect",
        "webhooks": "openapi.webhooks",
        "info-summary": "info.summary",
        "license-identifier": "info.license.identifier",
        "reference-description": "reference.description",
        "paths-absent": "paths-absent",
        "webhooks-without-paths": "webhooks-without-paths",
        "x-fern-or-crozier-ignore": "x-fern-or-crozier-ignore",
    }
    outputs = {}
    tick = chr(96)
    pair_pattern = tick + r"([^" + tick + r"]+)" + tick + r" \((\d+)\)"
    for name in ("document-paths.md", "oas31-extensions.md"):
        path = root / "docs/openapi-surface" / name
        lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
        for index, line in enumerate(lines):
            cells = line.replace("\\|", "\x00").split("|")
            if len(cells) != 10 or cells[4].strip() != "golden":
                continue
            key, location, evidence = cells[1].strip().strip(tick), cells[3].strip(), cells[5]
            if key.startswith("combo-"):
                continue
            selector = special.get(key) if name == "document-paths.md" else extension_selectors.get(key)
            if (
                selector is None
                and name == "document-paths.md"
                and key
                not in {
                    "non-identifier-operation-id",
                    "duplicate-operation-id",
                    "duplicate-normalized-paths",
                    "server-description-multiword",
                    "operation-id-digit-leading-method",
                }
            ):
                obj, field = re.sub(r" \([^)]*\)$", "", location).split(".", 1)
                selector = prefixes[obj] + "." + field
            if selector is not None:
                counts = measured.get(selector, {})
                pairs = list(re.finditer(pair_pattern, evidence))
                if pairs:
                    selected = counts
                    if key in {
                        "templated-path-segment",
                        "several-path-template-variables",
                        "path-leading-literal-segment",
                        "path-template-before-literal-segment",
                        "path-all-segments-templated",
                    }:
                        selected = dict(
                            sorted(counts.items(), key=lambda item: (-item[1], item[0]))[
                                : 8 if key in {"templated-path-segment", "several-path-template-variables"} else 5
                            ]
                        )
                    listing = ", ".join(f"{tick}{fixture}{tick} ({count})" for fixture, count in selected.items())
                    evidence = evidence[: pairs[0].start()] + listing + evidence[pairs[-1].end() :]
                elif key == "operation-id-digit-leading-method":
                    listing = ", ".join(f"{tick}{fixture}{tick} ({count})" for fixture, count in counts.items())
                    evidence = f" Snapshot census {tick}{selector}{tick}: {listing}. " + evidence.lstrip()
                elif counts and "golden-bearing witnesses: ." in evidence:
                    listing = ", ".join(f"{tick}{fixture}{tick} ({count})" for fixture, count in counts.items())
                    evidence = evidence.replace(
                        "golden-bearing witnesses: .", f"golden-bearing witnesses: {listing}.", 1
                    )
                elif counts:
                    raise ValueError(f"{key}: missing census list in snapshot template")
                evidence = re.sub(
                    r"\d+ declaration sites across \d+ registered golden sources",
                    f"{sum(counts.values())} declaration sites across {len(counts)} registered golden sources",
                    evidence,
                )
            if name == "oas31-extensions.md" and selector is not None:
                evidence = re.sub(
                    r"\d+ declarations across \d+ registered golden sources",
                    f"{sum(counts.values())} declarations across {len(counts)} registered golden sources",
                    evidence,
                )
                if key == "webhooks-without-paths":
                    evidence = re.sub(
                        r"The other \d+ webhook declarers also declare paths",
                        f"The other {len(webhooks & paths)} webhook declarers also declare paths",
                        evidence,
                    )
                if key == "x-fern-or-crozier-ignore":
                    only_fern_operations = not any(
                        measured.get(name)
                        for name in ("operation.x-crozier-ignore", "schema.x-fern-ignore", "schema.x-crozier-ignore")
                    )
                    description = (
                        f"All {sum(ignored.values())} declarations are on operations under the Fern spelling"
                        if only_fern_operations
                        else f"The {sum(ignored.values())} declarations combine the supported ignore extensions"
                    )
                    evidence = re.sub(
                        r"(?:All \d+ declarations are on operations under the Fern spelling|The \d+ declarations combine the supported ignore extensions)",
                        description,
                        evidence,
                    )
                    other_count = sum(
                        sum(measured.get(name, {}).values())
                        for name in ("operation.x-crozier-ignore", "schema.x-fern-ignore", "schema.x-crozier-ignore")
                    )
                    other_description = (
                        "The other three selectors have zero declarations in the registered-source walk"
                        if not other_count
                        else f"The other three selectors carry {other_count} declarations in the registered-source walk"
                    )
                    evidence = re.sub(
                        r"The other three selectors (?:have zero|carry \d+) declarations in the registered-source walk",
                        other_description,
                        evidence,
                    )
            if name == "oas31-extensions.md" and key == "paths-absent":
                evidence = re.sub(
                    r"Of the \d+ registered golden sources, \d+ declare paths",
                    f"Of the {len(sources)} registered golden sources, {len(measured['openapi.paths'])} declare paths",
                    evidence,
                )
            if name == "oas31-extensions.md" and key == "paths-absent":
                evidence = re.sub(
                    r"and the (?:three|\d+) listed here omit it",
                    f"and the {len(counts)} listed here omit it",
                    evidence,
                )
            evidence = (
                re.sub(
                    r"\d+ declarations across \d+ registered sources",
                    f"{sum(counts.values())} declarations across {len(counts)} registered sources",
                    evidence,
                )
                if selector is not None
                else evidence
            )
            if selector is not None:
                evidence = re.sub(r"20\d\d-\d\d-\d\d census", "Snapshot census", evidence)
            cells[5] = evidence
            lines[index] = "|".join(cells).replace("\x00", "\\|")
        text = "".join(lines)
        if name == "document-paths.md":
            digest = hashlib.sha256(
                json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
            ).hexdigest()
            original = sum(source.origin == SnapshotOrigin.VENDORED for source in sources.values())
            pattern = (
                r"\*\*Snapshot digest:\*\* "
                + tick
                + r"[0-9a-f]{64}"
                + tick
                + r", over \*\*\d+\*\* registered golden sources \(\d+ original fixtures, \d+ corpus sources\)"
            )
            replacement = f"**Snapshot digest:** {tick}{digest}{tick}, over **{len(sources)}** registered golden sources ({original} original fixtures, {len(sources) - original} corpus sources)"
            text, count = re.subn(pattern, replacement, text)
            if count != 1:
                raise ValueError("snapshot template needs exactly one digest")
        if name == "document-paths.md":
            gaps = sum(
                1
                for line in lines
                if len(cells := line.replace("\\|", "\x00").split("|")) == 10
                and cells[4].strip() == "gap"
                and not cells[1].strip(" `").startswith("combo-")
            )
            golden_rows = sum(
                1
                for line in lines
                if len(cells := line.replace("\\|", "\x00").split("|")) == 10
                and cells[4].strip() == "golden"
                and not cells[1].strip(" `").startswith("combo-")
            )
            ledger_keys = len(
                dict(
                    re.findall(
                        r"ledger " + tick + r"([^" + tick + r"]+)" + tick + r" — ([^;|*]+?)(?= \||;| \*\*)", text
                    )
                )
            )
            text = re.sub(
                r"document-paths evidence: ok \(\d+ census rows, \d+ ledger keys, \d+ gap rows?\)",
                f"document-paths evidence: ok ({golden_rows} census rows, {ledger_keys} ledger keys, {gaps} gap rows)",
                text,
                count=1,
            )
            text = re.sub(r", taken on \*\*20\d\d-\d\d-\d\d\*\*\.", ", reproduced from native census JSON.", text)
            text = text.replace("is the result of the **2026-10-08** walk", "is the result of the native census walk")
            text = text.replace("re-transcribed whole from that", "generated whole from that")
        outputs[path] = text
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=REPO)
    parser.add_argument("--write", action="store_true", help="write the derived tables; otherwise check for drift")
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--combinations-only", action="store_true", help="restate only the combination sentence")
    modes.add_argument(
        "--snapshot-json", type=Path, help="restate document snapshot from native surface-census --json output"
    )
    args = parser.parse_args()
    path = args.repo_root / "docs/openapi-surface-coverage.md"
    try:
        if args.snapshot_json is not None:
            outputs = document_snapshot(args.repo_root, json.loads(args.snapshot_json.read_text(encoding="utf-8")))
            for target, content in outputs.items():
                if content != target.read_text(encoding="utf-8"):
                    if not args.write:
                        raise ValueError("document snapshot differs; rerun with --write")
                    target.write_text(content, encoding="utf-8", newline="\n")
            return 0
        result = (
            restate_combinations(args.repo_root, path.read_text(encoding="utf-8"))
            if args.combinations_only
            else restate(args.repo_root)
        )
        if result != path.read_text(encoding="utf-8"):
            if not args.write:
                raise ValueError("derived tables differ; run tools/surface-census/restate-coverage.py --write")
            path.write_text(result, encoding="utf-8", newline="\n")
    except (OSError, ValueError, KeyError) as error:
        print(f"coverage-restatement: {error}; repair the named input and rerun", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    for stream in (sys.stdout, sys.stderr):
        if isinstance(stream, io.TextIOWrapper):
            stream.reconfigure(encoding="utf-8", errors="backslashreplace")
    sys.exit(main())
