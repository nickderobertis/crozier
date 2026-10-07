#!/usr/bin/env python3
"""Derive the registry search's consolidated ledgers from its per-source records.

`candidates.tsv` is every source's `records.tsv` row, pointing back at it.
In `outstanding.tsv` every row is one `(key, source, kind, blocker)` group of items that keep the
key's search open for that source: an inconclusive screen, a document that
could not be read, a portal the source refused, or a key the census cannot
evaluate.
Nothing here decides an outcome; a key with any row cannot read `exhausted`.

Exit status: 0 when the ledgers were written (or, with `--check`, are
current); 1 when a ledger it reads is missing or malformed, or `--check` finds
one stale, with the ledger named on stderr; 2 on a usage error.
"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import io
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
FIELDS = ("key", "source", "kind", "count", "blocker", "items", "evidence")
KINDS = ("selector-unavailable", "inconclusive-screen", "unreadable-document", "portal-unanswered")


def _load(name: str, file: str):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(file))
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


# Every source's `records.tsv` shares one candidate-record shape and one
# disposition grammar, both named once by the GitHub index that also writes them.
GITHUB_INDEX = _load("registries_github_index", "witness-search-github-index.py")
RECORD_FIELDS = GITHUB_INDEX.FIELDS
# What the region-key derivation writes in `census_status`.
CENSUS_STATUSES = ("supported", "unsupported-by-census")
# A portal-plan row's `acquisition`: refused by its source, acquired at a
# mutable ref, or acquired (at the pinned commit, saying where its digest is).
# Only a refusal keeps a key's search open.
SOURCE_REFUSED = "source-refused"
ACQUISITION = re.compile(r"source-refused|acquired|acquired-mutable|acquired at pinned commit; \S.*")
# The registries are the catalogue and portal sources, as the redo contract's
# `catalogue-portals` shard names them; the code platforms have their own index.
SOURCES = _load("registries_redo", "witness-search-redo.py").SOURCES["catalogue-portals"]


def read_tsv(path: Path, columns: tuple[str, ...], *, optional: bool = False) -> list[dict[str, str]]:
    """A ledger's rows, refused by name when it or a column it needs is missing."""
    if not path.is_file():
        if optional:
            return []
        raise ValueError(f"{path} is missing")
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, dialect="excel-tab")
        header = list(reader.fieldnames or ())
        repeated = sorted({column for column in header if header.count(column) > 1})
        if repeated:
            raise ValueError(f"{path} names column(s) {', '.join(repeated)} twice; one would overwrite the other")
        missing = sorted(set(columns) - set(header))
        if missing:
            raise ValueError(f"{path} lacks column(s) {', '.join(missing)}")
        rows = []
        for number, row in enumerate(reader, 2):
            # A short row leaves its trailing columns None; a long one files the
            # surplus under None. Neither is a row the header describes.
            if None in row or None in row.values():
                raise ValueError(f"{path}:{number} has another number of cells than its header names")
            empty = [column for column in columns if not row[column]]
            if empty:
                raise ValueError(f"{path}:{number} has no {', '.join(empty)}")
            rows.append(row)
        return rows


def screen_cell(value: str) -> bool:
    """A records.tsv screen cell: `pass`, `failed: <reason>` or `not-run: <reason>`, the
    reason non-empty."""
    return value == "pass" or any(value.startswith(prefix) and value[len(prefix):].strip()
                                  for prefix in ("failed: ", "not-run: "))


def records(root: Path, source: str) -> list[tuple[int, dict[str, str]]]:
    """One registry's candidate records with their line numbers, each held to the shared grammar.

    A record's key need not be in today's key set: a search that closed keeps
    its records after its key leaves the region tables.
    """
    path = root / f"witness-search-{source}" / "records.tsv"
    with path.open(encoding="utf-8", newline="") as handle:
        if tuple(csv.DictReader(handle, dialect="excel-tab").fieldnames or ()) != RECORD_FIELDS:
            raise ValueError(f"{path} does not have the candidate-record header")
    out = []
    for number, row in enumerate(read_tsv(path, RECORD_FIELDS[:4]), 2):
        where = f"{path}:{number}"
        if row["source"] != source:
            raise ValueError(f"{where} is filed under {source} but names source {row['source']!r}")
        bad = [field for field in ("licence_screen", "revision_screen", "fern_screen") if not screen_cell(row[field])]
        if bad:
            raise ValueError(f"{where} has {bad[0]} {row[bad[0]]!r}, not pass, failed: <reason> or not-run: <reason>")
        if not GITHUB_INDEX.known_disposition(row["disposition"]):
            raise ValueError(f"{where} has disposition {row['disposition']!r}, which the index grammar does not read")
        out.append((number, row))
    return out


def outstanding_rows(root: Path) -> list[dict[str, str]]:
    keys = read_tsv(root / "witness-search-keys.tsv", ("key", "selector", "census_status"))
    for number, row in enumerate(keys, 2):
        if row["census_status"] not in CENSUS_STATUSES:
            raise ValueError(f"{root / 'witness-search-keys.tsv'}:{number} has census_status "
                             f"{row['census_status']!r}, not one of {', '.join(CENSUS_STATUSES)}")
    supported = [row["key"] for row in keys if row["census_status"] == "supported"]
    groups: dict[tuple[str, str, str, str], dict] = {}

    def add(key: str, source: str, kind: str, blocker: str, item: str, evidence: str) -> None:
        assert kind in KINDS, kind
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
        for number, row in records(root, source):
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
        for number, row in enumerate(enumeration, 2):
            if row["status"] != "readable" and not (row["status"].startswith("unreadable: ")
                                                    and row["status"][len("unreadable: "):].strip()):
                raise ValueError(f"{directory / 'enumeration.tsv'}:{number} has status {row['status']!r}, "
                                 "not readable or unreadable: <reason>")
        unreadable = [row for row in enumeration if row["status"] != "readable"]
        for key in supported:
            for row in unreadable:
                add(key, source, "unreadable-document",
                    "the document does not parse; each path's parser reason is in enumeration.tsv",
                    f"{row['document']}@{row['revision']}", f"witness-search-{source}/enumeration.tsv")
    plan = read_tsv(root / "witness-search-portal-plan.tsv",
                    ("repository", "pinned_ref", "acquisition"))
    for number, row in enumerate(plan, 2):
        if not ACQUISITION.fullmatch(row["acquisition"]):
            raise ValueError(f"{root / 'witness-search-portal-plan.tsv'}:{number} has acquisition "
                             f"{row['acquisition']!r}, not {SOURCE_REFUSED}, acquired, acquired-mutable "
                             "or acquired at pinned commit; <where its digest is>")
        if row["acquisition"] == SOURCE_REFUSED:
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
        for number, row in records(root, source):
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
