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


def table(text: str, heading: str) -> list[list[str]]:
    body = text.split(heading, 1)[1] if heading in text else ""
    rows = []
    for line in body.splitlines():
        if line.startswith("| "):
            rows.append([cell.strip() for cell in line.strip().strip("|").split("|")])
    return rows


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
        key, selector, source = key.strip("`"), selector.strip("`"), source.strip("`")
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
        if not result:
            failures.append(f"{path}: {source}/{key} is missing a result")
        if result == "0" and "unanswered" in " ".join(row).lower():
            failures.append(
                f"{path}: {source}/{key} presents zero for an unanswered source"
            )
        if result == "unanswered" and candidates not in ("—", ""):
            failures.append(
                f"{path}: {source}/{key} gives candidates for an unanswered source"
            )
        if result != "unanswered" and not provenance:
            failures.append(f"{path}: {source}/{key} is missing immutable provenance")
        if result != "unanswered" and (not licence or not fern):
            failures.append(f"{path}: {source}/{key} is missing a screen")
    return failures


def reconcile(paths: list[Path], contract: Path, schemas: Path) -> list[str]:
    failures = [failure for path in paths for failure in validate_shard(path, contract)]
    keys = contract_keys(contract)
    records: dict[tuple[str, str], list[str]] = {}
    for path in paths:
        for row in table(path.read_text(encoding="utf-8"), "## Records")[1:]:
            if len(row) == len(FIELDS):
                records[(row[0].strip("`"), row[2].strip("`"))] = row
    missing = sorted(
        (key, source)
        for key in keys
        for source in sum(SOURCES.values(), ())
        if (key, source) not in records
    )
    if missing:
        failures.append(f"reconciliation: missing source/key coverage {missing}")
        return failures
    text = schemas.read_text(encoding="utf-8")
    for key in keys:
        answered = all(
            records[(key, source)][4] != "unanswered"
            for source in sum(SOURCES.values(), ())
        )
        expected = (
            "none-found"
            if answered
            and all(
                records[(key, source)][4] == "0" for source in sum(SOURCES.values(), ())
            )
            else "search-incomplete"
            if not answered
            else "witness-found"
        )
        if f"`{key}`" not in text or f"search outcome `{expected}`" not in text:
            failures.append(
                f"reconciliation: schemas.md does not record {key} as {expected}"
            )
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("contract", type=Path)
    parser.add_argument("shards", nargs="+", type=Path)
    parser.add_argument("--reconcile", action="store_true")
    parser.add_argument("--schemas", type=Path)
    args = parser.parse_args()
    failures = (
        reconcile(args.shards, args.contract, args.schemas)
        if args.reconcile
        else [
            failure
            for path in args.shards
            for failure in validate_shard(path, args.contract)
        ]
    )
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
