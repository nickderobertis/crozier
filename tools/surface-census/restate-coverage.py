#!/usr/bin/env python3
"""Restate category totals and the FIXTURE ranking without re-measuring coverage."""

from __future__ import annotations

import argparse
import csv
import importlib.util
import re
import sys
import textwrap
from collections import Counter
from pathlib import Path
from types import ModuleType

REPO = Path(__file__).resolve().parents[2]
SETTLEMENTS = ("FIXTURE", "PROBE", "UNREACHABLE")
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
    entries: dict[str, tuple[str, list[str]]] = {}
    counts: dict[str, list[int]] = {}
    gaps: dict[str, list[str]] = {name: [] for name in SETTLEMENTS}
    for name in parser.region_files(index):
        region = Path(name).stem
        rows = parser.region_rows((index.parent / "openapi-surface" / name).read_text(encoding="utf-8"))
        categories = Counter(row[3].strip("`") for row in rows)
        settlements: Counter[str] = Counter()
        for cells in rows:
            key = cells[0].strip("`")
            if key in entries:
                raise ValueError(f"duplicate category row: {key}")
            entries[key] = (region, cells)
            if cells[3].strip("`") == "gap":
                settlement = cells[7].lstrip("`*").split(" ", 1)[0].strip("`*—")
                if settlement not in gaps:
                    raise ValueError(f"{key}: unknown settlement {settlement}")
                gaps[settlement].append(key)
                settlements[settlement] += 1
        counts[region] = [
            len(rows),
            *[categories[c] for c in parser.CATEGORIES],
            *[settlements[s] for s in SETTLEMENTS],
        ]
    totals = [sum(column) for column in zip(*counts.values(), strict=True)]
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
    ranked = []
    pointing: Counter[str] = Counter()
    for key in gaps["FIXTURE"]:
        region, cells = entries[key]
        sites = [(path, int(n)) for path, n in re.findall(rf"({SOURCE})`?(?!:\d)[^0-9A-Za-z]{{0,14}}(\d+)", cells[5])]
        if not sites and not cells[5].lstrip("`").startswith("none"):
            raise ValueError(f"{key}: crozier sites has no measured count")
        missing = [path for path, _n in sites if path not in blind]
        if missing:
            raise ValueError(f"{key}: no committed blind-spot measurement for {missing}")
        artifacts = [name for name in ARTIFACTS if re.search(r"(?<![\w])" + re.escape(name), cells[6])]
        if not artifacts:
            raise ValueError(f"{key}: artifact cell names none of {ARTIFACTS}")
        witness = re.search(r":\s*(\d+) declarations", cells[4])
        if witness is None:
            raise ValueError(f"{key}: evidence has no measured declaration count")
        score = (sum(n for _p, n in sites), sum(blind[p] for p, _n in sites), len(artifacts), int(witness[1]))
        pointing.update({path for path, _n in sites})
        own = ", ".join(f"`{path}` {n}" for path, n in sites) or "none"
        reach = ", ".join(f"`{path}` {blind[path]}" for path, _n in sites) or "none"
        row = (
            f"[`{key}`](openapi-surface/{region}.md) | `{region}` | **{score[0]}** ({own}) | "
            f"**{score[1]}** ({reach}) | **{score[2]}** ({', '.join(artifacts)}) | **{score[3]}** |"
        )
        ranked.append(((score[0], -score[1], -score[2], -score[3], key), row, score))
    ranked.sort()
    table = "| # | key | region | 1. crozier sites | 2. blind spots | 3. artifacts | 4. witnesses |\n|---|---|---|---|---|---|---|\n"
    table += "\n".join(f"| {rank} | {row}" for rank, (_order, row, _score) in enumerate(ranked, 1))
    text = substitute(
        text,
        r"^\| # \| key \| region \| 1\. crozier sites[^\n]*\n\|---[^\n]*\n(?:\|[^\n]*\n)*",
        table.rstrip("\n") + "\n",
    )
    text = re.sub(r"All \d+ `FIXTURE` gaps", f"All {fixture} `FIXTURE` gaps", text)
    zero_witness = sum(score[3] == 0 for _order, _row, score in ranked)
    text = re.sub(
        r"(?:\d+ of the \d+ score zero|no ranked witnesses remain)",
        f"{zero_witness} of the {fixture} score zero" if fixture else "no ranked witnesses remain",
        text,
    )
    no_file = sum(score[0] == 0 for _order, _row, score in ranked)
    text = re.sub(r"\d+ of the \d+ entries name no", f"{no_file} of the {fixture} entries name no", text)
    text = re.sub(
        r"\d+ of the \d+ ranked entries reach no", f"{no_file} of the {fixture} ranked entries reach no", text
    )
    values = sorted(score[1] for _order, _row, score in ranked)
    median = (values[(len(values) - 1) // 2] + values[len(values) // 2]) // 2 if values else None
    if median is None:
        narrative = "The ranked backlog is empty.\n"
    else:
        named = ", ".join(f"{n} entries name `{path}`" for path, n in sorted(pointing.items()))
        narrative = (
            f"**The median blind-spot count of this list is {median}** — {named}. "
            f"{no_file} of the {fixture} entries name no `src/` file at all. "
            f"{no_file} of the {fixture} ranked entries reach no blind region. "
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
    with (surface / "golden-reach.tsv").open(encoding="utf-8", newline="") as handle:
        ledger = {
            row["key"]: row
            for row in csv.DictReader((line for line in handle if not line.startswith("#")), delimiter="\t")
        }
    residual_section = text.partition("#### Golden rows resting only on residual goldens")[2].split("\n#", 1)[0]
    residual = set(re.findall(r"^\| `([^`]+)` \|[^\n]*\| `open gap` \|$", residual_section, re.M))
    no_witness = sum(c[3].strip("`") == "golden" and not ledger[k]["witnesses"] for k, (_r, c) in entries.items())
    real = golden - len(residual) - no_witness
    proof = limitations + unreachable
    unproven = fixture + len(residual) + no_witness
    text = substitute(
        text,
        r"The walk enumerates \d+ features\. By category,.*?`gap`\.",
        f"The walk enumerates {total} features. By category, {golden} are `golden`, {limitations}\n`limitations`, {handwritten} `handwritten` and {gap} `gap`.",
    )
    text = re.sub(r"\*\*\d+ carry byte-match evidence", f"**{real} carry byte-match evidence", text)
    text = re.sub(r"\*\*\d+ carry a committed Fern", f"**{proof} carry a committed Fern", text)
    text = re.sub(r"\*\*\d+ rest on a hand-written fixture", f"**{handwritten} rest on a hand-written fixture", text)
    text = re.sub(r"They are not among the \d+", f"They are not among the {real}", text)
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
    sys.exit(main())
