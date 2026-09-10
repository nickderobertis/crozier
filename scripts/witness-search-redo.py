#!/usr/bin/env python3
"""Validate the two non-authoritative witness-search redo shards."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SOURCES = {
    "catalogue-portals": ("apis.guru", "jentic", "vendor-portals"),
    "code-platforms": ("sourcegraph", "github-code-search", "swaggerhub", "postman"),
}
FIELDS = (
    "key",
    "selector",
    "source",
    "query",
    "result",
    "candidates",
    "provenance",
    "licence-screen",
    "fern-screen",
)
ALL_SOURCES = sum(SOURCES.values(), ())
EMPTY = {"", "—"}


def table(text: str, heading: str) -> list[list[str]]:
    body = text.split(heading, 1)[1] if heading in text else ""
    rows = []
    for line in body.splitlines():
        if line.startswith("| "):
            rows.append([cell.strip() for cell in line.strip().strip("|").split("|")])
    return rows


def value(cell: str) -> str:
    """Strip the code span used around atomic record values."""
    return cell.strip().strip("`")


def schema_rows(text: str) -> dict[str, list[list[str]]]:
    """Parse bare or code-spanned keys from authoritative eight-cell entry rows."""
    found: dict[str, list[list[str]]] = {}
    for line in text.splitlines():
        if not line.startswith("| "):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if (
            len(cells) == 8
            and value(cells[0]) != "key"
            and value(cells[3]) in {"golden", "limitations", "gap"}
        ):
            found.setdefault(value(cells[0]), []).append(cells)
    return found


def authoritative_details(
    row: list[str],
) -> tuple[str | None, dict[str, tuple[str, str]]]:
    """Read outcome and seven query/results from this row only."""
    cell = " | ".join(row)
    outcome = re.search(r"search outcome `([^`]+)`", cell)
    details: dict[str, tuple[str, str]] = {}
    pattern = re.compile(
        r"\*\*([^*]+)\*\*\s+(`[^`]+`)\s+(?:→|->)\s+(`?unanswered`?|\d+)"
    )
    for source, query, result in pattern.findall(cell):
        details[value(source)] = (query, value(result))
    return (outcome.group(1) if outcome else None), details


def contract_keys(path: Path) -> dict[str, str]:
    rows = table(path.read_text(encoding="utf-8"), "## Owned keys")
    return {row[0].strip("`"): row[1].strip("`") for row in rows[1:] if len(row) == 2}


def validate_shard(path: Path, contract: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    failures: list[str] = []
    match = re.search(r"^shard: `([^`]+)`$", text, re.M)
    shard = match.group(1) if match else ""
    if shard not in SOURCES:
        return [f"{path}: missing or unknown shard declaration"]
    keys = contract_keys(contract)
    declared = {
        row[0].strip("`") for row in table(text, "## Owned keys")[1:] if len(row) == 1
    }
    if declared != set(keys):
        failures.append(f"{path}: owned keys omitted {sorted(set(keys) - declared)}")
    rows = table(text, "## Records")
    if not rows or tuple(cell.strip("`") for cell in rows[0]) != FIELDS:
        failures.append(f"{path}: records header is not the shared record shape")
        return failures
    seen: set[tuple[str, str]] = set()
    for number, row in enumerate(rows[1:], 1):
        if len(row) != len(FIELDS):
            failures.append(
                f"{path}: record {number} has {len(row)} fields, expected {len(FIELDS)}"
            )
            continue
        key, selector, source, query, result, candidates, provenance, licence, fern = (
            row
        )
        key, selector, source, result = map(value, (key, selector, source, result))
        pair = (key, source)
        if pair in seen:
            failures.append(f"{path}: duplicate source/key record {source}/{key}")
        seen.add(pair)
        if key not in keys:
            failures.append(f"{path}: unknown key {key}")
        elif selector != keys[key]:
            failures.append(f"{path}: {key} has the wrong selector")
        if source not in SOURCES[shard]:
            failures.append(f"{path}: source {source} is not owned by {shard}")
        if not (query.startswith("`") and query.endswith("`") and len(query) > 2):
            failures.append(f"{path}: {source}/{key} is missing a rerunnable query")
        if result != "unanswered" and not re.fullmatch(r"\d+", result):
            failures.append(
                f"{path}: {source}/{key} result must be a nonnegative integer or unanswered"
            )
            continue
        supporting = tuple(
            value(cell) for cell in (candidates, provenance, licence, fern)
        )
        if result == "unanswered" and any(cell not in EMPTY for cell in supporting):
            failures.append(
                f"{path}: {source}/{key} unanswered result has supporting fields"
            )
        elif result == "0" and any(cell not in EMPTY for cell in supporting):
            failures.append(
                f"{path}: {source}/{key} zero result has candidate evidence"
            )
        elif result.isdigit() and int(result) > 0:
            labels = (
                "candidates",
                "immutable provenance",
                "licence screen",
                "Fern screen",
            )
            missing = [
                label for label, cell in zip(labels, supporting) if cell in EMPTY
            ]
            if missing:
                failures.append(
                    f"{path}: {source}/{key} positive result is missing {missing}"
                )
    return failures


def validate_documents(paths: list[Path], contract: Path) -> list[str]:
    failures = [failure for path in paths for failure in validate_shard(path, contract)]
    seen: dict[tuple[str, str], Path] = {}
    for path in paths:
        for row in table(path.read_text(encoding="utf-8"), "## Records")[1:]:
            if len(row) != len(FIELDS):
                continue
            pair = (value(row[0]), value(row[2]))
            if pair in seen:
                failures.append(
                    f"duplicate source/key record {pair[1]}/{pair[0]} across "
                    f"{seen[pair]} and {path}"
                )
            else:
                seen[pair] = path
    return failures


def screened_keys(path: Path, *, artifact: str | None = None) -> set[str]:
    """A declaration count is not proof that an artifact passed all four screens."""
    found: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| `"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != 8 or value(cells[6]) != "witness-found":
            continue
        if artifact is not None and value(cells[0]) != artifact:
            continue
        if not all(cell.startswith("passed:") for cell in cells[2:6]):
            continue
        keys = set(re.findall(r"`([^`]+)`", cells[1]))
        if "discarded keys:" in cells[5]:
            keys -= set(re.findall(r"`([^`]+)`", cells[5].split("discarded keys:", 1)[1]))
        found.update(keys)
    return found


def reconcile(paths: list[Path], contract: Path, schemas: Path, candidates: Path, supplement_candidates: tuple[Path, ...] = ()) -> list[str]:
    failures = validate_documents(paths, contract)
    keys = contract_keys(contract)
    records: dict[tuple[str, str], list[str]] = {}
    for path in paths:
        for row in table(path.read_text(encoding="utf-8"), "## Records")[1:]:
            if len(row) == len(FIELDS):
                pair = (value(row[0]), value(row[2]))
                if pair not in records:
                    records[pair] = row
    missing = sorted(
        (key, source)
        for key in keys
        for source in ALL_SOURCES
        if (key, source) not in records
    )
    if missing:
        failures.append(f"reconciliation: missing source/key coverage {missing}")
        return failures
    witnesses = screened_keys(candidates)
    for supplement in supplement_candidates:
        witnesses.update(screened_keys(supplement))
    rows = schema_rows(schemas.read_text(encoding="utf-8"))
    for key in keys:
        answered = all(
            value(records[(key, source)][4]) != "unanswered" for source in ALL_SOURCES
        )
        expected = (
            "witness-found"
            if key in witnesses
            else "none-found"
            if answered
            and all(value(records[(key, source)][4]) == "0" for source in ALL_SOURCES)
            else "search-incomplete"
            if not answered
            else "witness-blocked"
        )
        owned_rows = rows.get(key, [])
        if len(owned_rows) != 1:
            failures.append(
                f"reconciliation: schemas.md has {len(owned_rows)} rows for {key}"
            )
            continue
        outcome, details = authoritative_details(owned_rows[0])
        if outcome != expected:
            failures.append(
                f"reconciliation: schemas.md row {key} records outcome {outcome!r}, expected {expected!r}"
            )
        missing_details = sorted(set(ALL_SOURCES) - set(details))
        if missing_details:
            failures.append(
                f"reconciliation: schemas.md row {key} omits source details {missing_details}"
            )
        for source in sorted(set(ALL_SOURCES) & set(details)):
            shard_query = records[(key, source)][3]
            shard_result = value(records[(key, source)][4])
            if details[source] != (shard_query, shard_result):
                failures.append(
                    f"reconciliation: schemas.md row {key} mismatches {source} query/result"
                )
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("contract", type=Path)
    parser.add_argument("shards", nargs="+", type=Path)
    parser.add_argument("--reconcile", action="store_true")
    parser.add_argument("--schemas", type=Path)
    parser.add_argument("--candidates", type=Path, help="four-screen record (default: beside CONTRACT)")
    parser.add_argument("--supplement-candidates", type=Path, action="append", default=[],
                        help="additional four-screen records; repeatable, historical inputs unchanged")
    args = parser.parse_args()
    for supplement in args.supplement_candidates:
        if not supplement.is_file():
            parser.error(f"--supplement-candidates requires a candidate file: {supplement}")
    if args.reconcile and args.schemas is None:
        parser.error("--reconcile requires --schemas PATH")
    failures = (
        reconcile(args.shards, args.contract, args.schemas, args.candidates or args.contract.with_name("candidates.md"), tuple(args.supplement_candidates))
        if args.reconcile
        else validate_documents(args.shards, args.contract)
    )
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
