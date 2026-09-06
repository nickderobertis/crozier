#!/usr/bin/env python3
"""Hold `docs/licence-rescreening.md` to the shape a registering node can read.

The screening record is one line per candidate the six
`docs/openapi-surface/*.md` region files record as blocked on a licence. The
node that registers witnesses works from that record and from nothing else, so
a line missing its verdict, its reason, its pinned reference, either half of
the Fern screen, or naming a coverage row no region file carries is worse than
no line at all: it reads as a screening that happened.

What every line of the record's table must carry:

* an **admission verdict** — exactly `admitted` or `still-blocked`;
* the **reason** behind it, as prose rather than a bare restatement;
* the candidate's **pinned reference** — a 40-character commit, an APIs.guru
  version reference, or an explicit `none — <why>` where the world offers no
  immutable one;
* the **document check's result** — the `fern check` command and either an exit
  status or `not run — <why>`;
* the **generate's result** — the `fern generate` command and the same;
* **coverage rows** that the region files actually carry, read off their
  `## Entries` tables, or an explicit `none`.

Run: `just lint-licence-rescreening` (part of `just check`).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RECORD = "docs/licence-rescreening.md"
REGION_DIR = "docs/openapi-surface"
REGIONS = (
    "bodies-media",
    "document-paths",
    "oas31-extensions",
    "parameters",
    "schemas",
    "security",
)
TABLE_HEADING = "## The record"
COLUMNS = (
    "candidate",
    "pinned ref",
    "licence",
    "admission",
    "why the rule reaches it or does not",
    "rows it declares",
    "document check",
    "generate",
)
VERDICTS = ("admitted", "still-blocked")
# A reason has to say something. Anything this short is a label, not a reason.
MIN_REASON = 25

KEY = re.compile(r"`([a-z0-9][a-z0-9.\-]*)`")
COMMIT = re.compile(r"\b[0-9a-f]{40}\b")
APIS_GURU = re.compile(r"APIs\.guru\s+`[^`]+`")
NO_REF = re.compile(r"^none — (?P<why>.+)$", re.DOTALL)
EXIT = re.compile(r"exit\*{0,2}\s*\*{0,2}(\d+)")
NOT_RUN = re.compile(r"not run — (?P<why>.+)$", re.DOTALL)


def region_keys(root: Path) -> dict[str, str]:
    """Every coverage-row key the six region files carry, to its region."""
    keys: dict[str, str] = {}
    for region in REGIONS:
        text = (root / REGION_DIR / f"{region}.md").read_text(encoding="utf-8")
        lines = text.split("\n")
        try:
            start = next(
                index
                for index, line in enumerate(lines)
                if line.strip() == "## Entries"
            )
        except StopIteration:
            continue
        for line in lines[start + 1 :]:
            if line.startswith("## "):
                break
            if not line.startswith("| "):
                continue
            cell = line.strip().strip("|").split(" | ")[0].strip().strip("`")
            if cell != "key" and re.fullmatch(r"[a-z0-9][a-z0-9.\-]*", cell):
                keys[cell] = region
    return keys


def record_rows(text: str) -> tuple[list[str], list[tuple[int, list[str]]]]:
    """The record table's header cells and its `(line number, cells)` rows."""
    lines = text.split("\n")
    try:
        start = next(
            index for index, line in enumerate(lines) if line.strip() == TABLE_HEADING
        )
    except StopIteration:
        return [], []
    header: list[str] = []
    rows: list[tuple[int, list[str]]] = []
    for offset, line in enumerate(lines[start + 1 :], start=start + 2):
        if line.startswith("## "):
            break
        if not line.startswith("| "):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split(" | ")]
        if not header:
            header = cells
            continue
        if set("".join(cells)) <= {"-", ":"}:
            continue
        rows.append((offset, cells))
    return header, rows


def check_ref(cell: str) -> str | None:
    if COMMIT.search(cell) or APIS_GURU.search(cell):
        return None
    match = NO_REF.match(cell)
    if match and len(match.group("why")) >= MIN_REASON:
        return None
    return (
        "the pinned ref is neither a 40-character commit, an APIs.guru version"
        " reference, nor `none — <why the world offers no immutable one>`"
    )


def check_fern(cell: str, command: str) -> str | None:
    if command not in cell:
        return f"names no `{command}` command, so nothing says what was run"
    if EXIT.search(cell):
        return None
    match = NOT_RUN.search(cell)
    if match and len(match.group("why")) >= MIN_REASON:
        return None
    return (
        f"carries no `{command}` result: give an exit status, or"
        " `not run — <why it was not run>`"
    )


def check_rows(cell: str, keys: dict[str, str]) -> str | None:
    named = KEY.findall(cell)
    unknown = [key for key in named if key not in keys]
    if unknown:
        return (
            "names coverage row(s) no region file carries: "
            + ", ".join(sorted(set(unknown)))
        )
    if not named and "none" not in cell.lower():
        return "names no coverage row and does not say `none`"
    return None


def check(root: Path) -> list[str]:
    problems: list[str] = []
    record = root / RECORD
    if not record.is_file():
        return [f"{RECORD}:0 — the screening record is missing"]
    header, rows = record_rows(record.read_text(encoding="utf-8"))
    if not rows:
        return [
            f"{RECORD}:0 — no table under `{TABLE_HEADING}`, so the record"
            " records nothing"
        ]
    if header != list(COLUMNS):
        return [
            f"{RECORD}:0 — the record's columns are {header}, not"
            f" {list(COLUMNS)}; this check reads them by position"
        ]
    keys = region_keys(root)
    for line, cells in rows:
        where = f"{RECORD}:{line}"
        if len(cells) != len(COLUMNS):
            problems.append(
                f"{where} — {len(cells)} cells, not {len(COLUMNS)}: {cells[0][:60]}"
            )
            continue
        candidate, ref, licence, verdict, why, declares, checked, generated = cells
        if not candidate:
            problems.append(f"{where} — no candidate named")
        if not licence:
            problems.append(f"{where} — no licence recorded for {candidate[:60]}")
        if verdict not in VERDICTS:
            problems.append(
                f"{where} — admission is {verdict!r}, not one of"
                f" {' / '.join(VERDICTS)}"
            )
        if len(why) < MIN_REASON:
            problems.append(
                f"{where} — the admission verdict carries no reason"
                f" ({len(why)} characters)"
            )
        for problem in (
            check_ref(ref),
            check_rows(declares, keys),
            check_fern(checked, "fern check"),
            check_fern(generated, "fern generate"),
        ):
            if problem:
                problems.append(f"{where} — {problem}")
    return problems


def main() -> int:
    problems = check(REPO)
    if not problems:
        return 0
    print(f"licence-rescreening: {RECORD} does not hold:", file=sys.stderr)
    for problem in problems:
        print(f"  {problem}", file=sys.stderr)
    print(
        "\nEvery line is one candidate's whole screening: the admission verdict"
        " and its reason, the ref it was screened at, what `fern check` and"
        " `fern generate` returned, and coverage rows the region files carry.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
