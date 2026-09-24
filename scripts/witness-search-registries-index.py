#!/usr/bin/env python3
# llmlint: ignore-file[new_code_lands_in_a_project] This Cargo crate has no Nx graph; this derivation lives with the just-driven witness-search scripts and is drift-checked by the acquisition tier.
"""Derive the registry search's consolidated ledgers from its per-source records.

`candidates.tsv` is every source's `records.tsv` row, pointing back at it.
In `outstanding.tsv` every row is one `(key, source, kind, blocker)` group of items that keep the
key's search open for that source: an inconclusive screen, a document that
could not be read, a portal or query the source refused, a Postman hit whose
body no unauthenticated route returned, or a key the census cannot evaluate.
Nothing here decides an outcome; a key with any row cannot read `exhausted`.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SOURCES = ("apis.guru", "jentic", "postman", "vendor-portals")
FIELDS = ("key", "source", "kind", "count", "blocker", "items", "evidence")
RECORD_FIELDS = ("source", "key", "candidate", "revision", "digest", "census", "licence_screen",
                 "revision_screen", "fern_screen", "disposition", "evidence")
POSTMAN_KINDS = {"apinetwork.team": "team", "runtime.collection": "collection"}


def read_tsv(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        return []
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, dialect="excel-tab"))


def read_jsonl(path: Path) -> list[dict]:
    if not path.is_file():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def hit_blocker(row: dict) -> str | None:
    """Why a Postman hit's body stays unread, or None when it was read."""
    if row.get("classification") in ("openapi-3", "not-openapi-3"):
        return None
    status = row.get("status")
    if row["hit"] == "team":
        return ("a team has no document body: its public profile route returned "
                f"HTTP {status} {row.get('content_type') or ''}".strip()
                + "; its collections and APIs are listed only by the Postman API, "
                "which requires an API key this host does not hold")
    if status == 404 and "Link does not exist" in row.get("response", ""):
        return ("collection JSON link returned HTTP 404 `Link does not exist.`: the owner "
                "published no link; the Postman API requires an API key this host does not hold")
    if status == 401:
        return ("HTTP 401 from the Postman API, the only documented route to this "
                "resource: it requires an API key this host does not hold")
    return f"HTTP {status}: {row.get('response') or row.get('blocker') or row.get('classification')}"


def derive(root: Path) -> list[dict[str, str]]:
    keys = read_tsv(root / "witness-search-keys.tsv")
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
        for row in read_tsv(directory / "records.tsv"):
            if row["disposition"] == "outstanding":
                blocker = next(row[f] for f in ("licence_screen", "revision_screen", "fern_screen")
                               if row[f] != "pass")
                add(row["key"], source, "inconclusive-screen", blocker,
                    f"{row['candidate']}@{row['revision']}", f"witness-search-{source}/records.tsv")
        unreadable = [row for row in read_tsv(directory / "enumeration.tsv")
                      if row["status"].startswith("unreadable")]
        for key in supported:
            for row in unreadable:
                add(key, source, "unreadable-document",
                    "the document does not parse; each path's parser reason is in enumeration.tsv",
                    f"{row['document']}@{row['revision']}", f"witness-search-{source}/enumeration.tsv")
    for row in read_tsv(root / "witness-search-portal-plan.tsv"):
        if row["acquisition"] == "source-refused":
            for key in supported:
                add(key, "vendor-portals", "portal-unanswered", row["pinned_ref"],
                    row["repository"], "witness-search-portal-plan.tsv")
    postman = root / "witness-search-postman"
    for row in read_jsonl(postman / "queries.jsonl"):
        if row.get("classification") != "answered":
            read = row.get("offset", 0)
            add(row["key"], "postman", "query-refused",
                f"HTTP {row.get('status')} at {row['taken_utc']}: {row.get('response') or row.get('error')}",
                f"`{row['query']}` on {row['index']} from offset {read}",
                "witness-search-postman/queries.jsonl")
    for row in read_jsonl(postman / "hit-access.jsonl"):
        blocker = hit_blocker(row)
        declared = row.get("selectors") or {}
        for key in row["keys"]:
            if blocker is not None:
                add(key, "postman", f"{row['hit']}-body-unacquired", blocker, row["id"],
                    "witness-search-postman/hit-access.jsonl")
            elif declared.get(key):
                add(key, "postman", "unscreened-declarer",
                    "the census confirms the shape; licence, ref and Fern screens are not yet run",
                    row["url"], "witness-search-postman/hit-access.jsonl")
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
    parser.add_argument("--check", action="store_true", help="fail when outstanding.tsv is stale")
    args = parser.parse_args()
    directory = args.root / "witness-search-registries"
    try:
        expected = {
            directory / "candidates.tsv": render(candidates(args.root), (*RECORD_FIELDS[:-1], "record")),
            directory / "outstanding.tsv": render(derive(args.root)),
        }
    except (OSError, KeyError, ValueError) as error:
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
