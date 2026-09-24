#!/usr/bin/env python3
# llmlint: ignore-file[new_code_lands_in_a_project] This Cargo crate has no Nx graph; this derivation lives with the just-driven witness-search scripts and is drift-checked by the acquisition tier.
"""Derive the registry search's consolidated ledgers from its per-source records.

`candidates.tsv` is every source's `records.tsv` row, pointing back at it.
In `outstanding.tsv` every row is one `(key, source, kind, blocker)` group of items that keep the
key's search open for that source: an inconclusive screen, a document that
could not be read, a portal the source refused, or a key the census cannot
evaluate.
Nothing here decides an outcome; a key with any row cannot read `exhausted`.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SOURCES = ("apis.guru", "jentic", "vendor-portals")
FIELDS = ("key", "source", "kind", "count", "blocker", "items", "evidence")
RECORD_FIELDS = ("source", "key", "candidate", "revision", "digest", "census", "licence_screen",
                 "revision_screen", "fern_screen", "disposition", "evidence")


def read_tsv(path: Path, columns: tuple[str, ...], *, optional: bool = False) -> list[dict[str, str]]:
    """A ledger's rows, refused by name when it or a column it needs is missing."""
    if not path.is_file():
        if optional:
            return []
        raise ValueError(f"{path} is missing")
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, dialect="excel-tab")
        missing = sorted(set(columns) - set(reader.fieldnames or ()))
        if missing:
            raise ValueError(f"{path} lacks column(s) {', '.join(missing)}")
        return list(reader)


def outstanding_rows(root: Path) -> list[dict[str, str]]:
    keys = read_tsv(root / "witness-search-keys.tsv", ("key", "selector", "census_status"))
    supported = [row["key"] for row in keys if row["census_status"] == "supported"]
    groups: dict[tuple[str, str, str, str], dict] = {}

    def add(key: str, source: str, kind: str, blocker: str, item: str, evidence: str) -> None:
        group = groups.setdefault((key, source, kind, blocker), {"items": [], "evidence": evidence})
        group["items"].append(item)

    for row in keys:
        if row["census_status"] != "supported":
            for source in SOURCES:
                add(row["key"], source, "selector-unavailable",
                    f"selector `{row['selector']}` is {row['census_status']}; no document was evaluated",
                    row["key"], "witness-search-keys.tsv")
    for source in SOURCES:
        directory = root / f"witness-search-{source}"
        for number, row in enumerate(read_tsv(directory / "records.tsv", RECORD_FIELDS), 2):
            if row["disposition"] == "outstanding":
                blocker = next((row[f] for f in ("licence_screen", "revision_screen", "fern_screen")
                                if row[f] != "pass"), None)
                if blocker is None:
                    raise ValueError(f"{directory / 'records.tsv'}:{number} is outstanding but "
                                     "every screen reads pass")
                add(row["key"], source, "inconclusive-screen", blocker,
                    f"{row['candidate']}@{row['revision']}", f"witness-search-{source}/records.tsv")
        enumeration = read_tsv(directory / "enumeration.tsv",
                               ("document", "revision", "status"), optional=True)
        unreadable = [row for row in enumeration
                      if row["status"].startswith("unreadable")]
        for key in supported:
            for row in unreadable:
                add(key, source, "unreadable-document",
                    "the document does not parse; each path's parser reason is in enumeration.tsv",
                    f"{row['document']}@{row['revision']}", f"witness-search-{source}/enumeration.tsv")
    plan = read_tsv(root / "witness-search-portal-plan.tsv",
                    ("repository", "pinned_ref", "acquisition"))
    for row in plan:
        if row["acquisition"] == "source-refused":
            for key in supported:
                add(key, "vendor-portals", "portal-unanswered", row["pinned_ref"],
                    row["repository"], "witness-search-portal-plan.tsv")
    return [
        {"key": key, "source": source, "kind": kind, "count": str(len(group["items"])),
         "blocker": blocker, "items": json.dumps(sorted(group["items"])), "evidence": group["evidence"]}
        for (key, source, kind, blocker), group in sorted(groups.items())
    ]


def candidates(root: Path) -> list[dict[str, str]]:
    rows = []
    for source in SOURCES:
        path = root / f"witness-search-{source}/records.tsv"
        with path.open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle, dialect="excel-tab")
            if tuple(reader.fieldnames or ()) != RECORD_FIELDS:
                raise ValueError(f"{path} does not have the candidate-record header")
            for number, row in enumerate(reader, 2):
                rows.append({**{field: row[field] for field in RECORD_FIELDS[:-1]},
                             "record": f"witness-search-{source}/records.tsv:{number}"})
    return sorted(rows, key=lambda row: (row["key"], row["candidate"], row["revision"], row["source"]))


def render(rows: list[dict[str, str]], fields: tuple[str, ...] = FIELDS) -> str:
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=fields, dialect="excel-tab", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=REPO / "docs/openapi-surface")
    parser.add_argument("--check", action="store_true", help="fail when candidates.tsv or outstanding.tsv is stale")
    args = parser.parse_args()
    directory = args.root / "witness-search-registries"
    try:
        expected = {
            directory / "candidates.tsv": render(candidates(args.root), (*RECORD_FIELDS[:-1], "record")),
            directory / "outstanding.tsv": render(outstanding_rows(args.root)),
        }
    except (OSError, ValueError) as error:
        print(f"witness-search-registries-index: {error}; repair the ledger it names", file=sys.stderr)
        return 1
    for output, text in expected.items():
        if not args.check:
            output.write_text(text, encoding="utf-8")
        elif not output.is_file() or output.read_text(encoding="utf-8") != text:
            print(f"witness-search-registries-index: {output} is stale; rerun without --check",
                  file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
