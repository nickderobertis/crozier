#!/usr/bin/env python3
"""Restate category totals and the FIXTURE ranking without re-measuring coverage.

Exit status: 0 on success, 1 on drift or input/write failure, 2 on usage errors.
"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import io
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


ARTIFACTS = ("types/", "client.py", "raw_client.py", "errors/", "reference.md", "core/")
SOURCE = r"src/(?:[a-z_]+/)*[a-z_]+\.rs"


def reader() -> ModuleType:
    """Use the region parser shared by the census and its gate."""
    path = Path(__file__).with_name("witness-search-region-keys.py")
    spec = importlib.util.spec_from_file_location("coverage_region_reader", path)
    if spec is None or spec.loader is None:
        raise ValueError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def substitute(text: str, pattern: str, replacement: str) -> str:
    """Refuse a changed document layout rather than silently leaving stale totals."""
    result, count = re.subn(pattern, lambda _match: replacement, text, count=1, flags=re.M | re.S)
    if count != 1:
        raise ValueError(f"coverage index no longer matches {pattern!r}")
    return result


def restate(root: Path) -> str:
    """Derive tables from category rows and the committed blind-spot measurement."""
    index = root / "docs/openapi-surface-coverage.md"
    text = index.read_text(encoding="utf-8")
    parser = reader()
    entries: dict[str, CategoryRow] = {}
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
        if not records.fieldnames or "key" not in records.fieldnames or "witnesses" not in records.fieldnames:
            raise ValueError("golden-reach.tsv: missing key/witnesses header")
        for row in records:
            if None in row or any(value is None for value in row.values()) or not row["key"]:
                raise ValueError("golden-reach.tsv: incomplete record")
            if row["key"] in ledger:
                raise ValueError(f"golden-reach.tsv: duplicate key {row['key']}")
            ledger[row["key"]] = Reach(row["witnesses"])
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
    no_witness = len(witnessless)
    real = golden - len(residual) - no_witness
    proof = limitations + unreachable
    unproven = fixture + len(residual) + no_witness
    text = substitute(
        text,
        r"The walk enumerates \d+ features\. By category,.*?`gap`\.",
        f"The walk enumerates {total} features. By category, {golden} are `golden`, {limitations}\n`limitations`, {handwritten} `handwritten` and {gap} `gap`.",
    )
    text = substitute(text, r"those \d+\nsplit four ways", f"those {total}\nsplit four ways")
    text = substitute(text, r"\*\*\d+ carry byte-match evidence", f"**{real} carry byte-match evidence")
    text = substitute(text, r"\*\*\d+ carry a committed Fern", f"**{proof} carry a committed Fern")
    text = substitute(
        text, r"\*\*\d+ rest on a hand-written fixture", f"**{handwritten} rest on a hand-written fixture"
    )
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
    text = substitute(
        text,
        r"- \*\*\d+ remain unproven\.\*\*.*?(?=\n\n\d+ \+)",
        textwrap.fill(remainder, width=88, subsequent_indent="  ", break_long_words=False, break_on_hyphens=False),
    )
    text = substitute(
        text, r"^\d+ \+ \d+ \+ \d+ \+ \d+ = \d+\.$", f"{real} + {proof} + {handwritten} + {unproven} = {total}."
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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=REPO)
    parser.add_argument("--write", action="store_true", help="write the derived tables; otherwise check for drift")
    args = parser.parse_args()
    path = args.repo_root / "docs/openapi-surface-coverage.md"
    try:
        result = restate(args.repo_root)
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
