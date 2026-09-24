#!/usr/bin/env python3
"""Reconcile acquired search results into per-source and consolidated candidate rows."""

from __future__ import annotations

import argparse
import csv
import io
import json
from pathlib import Path
from typing import Any

SOURCES = ("github-code-search", "github-publisher-trees", "sourcegraph")
FIELDS = (
    "source",
    "key",
    "candidate",
    "revision",
    "digest",
    "census",
    "licence_screen",
    "revision_screen",
    "fern_screen",
    "disposition",
    "evidence",
)
CENTRAL_FIELDS = (*FIELDS[:-1], "record")


def jsonl(path: Path) -> list[tuple[int, dict[str, Any]]]:
    if not path.is_file():
        return []
    return [
        (i, json.loads(line))
        for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1)
    ]


def normalize_repo(value: str) -> str:
    return value.removeprefix("github.com/")


def candidate_name(row: dict[str, Any]) -> str:
    return f"{normalize_repo(row['repository'])}:{row['path']}"


def screen_value(value: str) -> str:
    if value.startswith("passed"):
        return "pass"
    if value.startswith("not-run:"):
        return value
    return "failed: " + value.split(": ", 1)[-1]


def screens(directory: Path) -> dict[tuple[str, str, str], dict[str, Any]]:
    found = {}
    for _, row in jsonl(directory / "screens.jsonl"):
        for key in row.get("keys") or [row.get("key")]:
            if key:
                found[(key, candidate_name(row), row.get("sha256", ""))] = row
    return found


def classify(
    source: str,
    key: str,
    row: dict[str, Any],
    evidence: str,
    screened: dict[tuple[str, str, str], dict[str, Any]],
    *,
    closed: bool = False,
) -> dict[str, str]:
    name = candidate_name(row)
    revision = (
        row.get("commit") or f"blob:{row.get('blob') or row.get('sha') or 'unresolved'}"
    )
    digest = row.get("sha256") or "not-fetched"
    count = row.get("selector_count", row.get("selector_counts", {}).get(key, 0))
    status = row.get("disposition") or row.get("status") or "acquisition-outstanding"
    if status in ("declares", "readable") and count:
        census = f"census {count}"
        screen = screened.get((key, name, digest))
        if screen:
            licence = screen_value(screen["license"])
            ref = screen_value(screen["ref"])
            fern = screen_value(screen["fern"])
            disposition = {
                "witness-found": "witness-found",
                "not-owed": "not-owed",
            }.get(screen["disposition"], "rejected")
        else:
            licence = ref = fern = (
                "not-run: key closed by found witness"
                if closed
                else "not-run: declaration screen outstanding"
            )
            disposition = "not-owed" if closed else "outstanding"
    elif status in ("acquisition-failure", "parse-failure", "acquisition-outstanding"):
        census = f"{status}: {row.get('diagnostic') or 'document not yet fetched'}"
        licence = ref = fern = f"not-run: {status}"
        disposition = (
            "not-owed"
            if closed and status == "acquisition-outstanding"
            else "outstanding"
        )
    else:
        census = (
            "census 0"
            if status in ("does-not-declare", "readable")
            else f"{status}: not OpenAPI 3"
        )
        licence = ref = fern = "not-run: census found no declaration"
        disposition = "rejected"
    return {
        "source": source,
        "key": key,
        "candidate": name,
        "revision": revision,
        "digest": digest,
        "census": census,
        "licence_screen": licence,
        "revision_screen": ref,
        "fern_screen": fern,
        "disposition": disposition,
        "evidence": evidence,
    }


def source_rows(root: Path, source: str) -> list[dict[str, str]]:
    directory = root / f"witness-search-{source}"
    screened = screens(directory)
    keys = sorted(
        json.loads((directory / "keys.json").read_text(encoding="utf-8"))["keys"]
    )
    latest: dict[tuple[str, str, str], dict[str, str]] = {}
    resolved_blobs = set()
    filename = (
        "documents.jsonl" if source == "github-publisher-trees" else "candidates.jsonl"
    )
    for number, row in jsonl(directory / filename):
        targets = keys if source == "github-publisher-trees" else [row["key"]]
        for key in targets:
            closed = (directory / f"closure-{key}.json").is_file()
            result = classify(
                source, key, row, f"{filename}:{number}", screened, closed=closed
            )
            latest[(key, result["candidate"], result["revision"])] = result
            if source == "github-code-search" and row.get("blob"):
                resolved_blobs.add((key, result["candidate"], row["blob"]))
    if source == "github-publisher-trees":
        for number, tree in jsonl(directory / "trees.jsonl"):
            if "paths" not in tree:
                continue
            for path in tree["paths"]:
                item = {
                    "repository": tree["repository"],
                    "path": path["path"],
                    "commit": tree["commit"],
                    "blob": path.get("blob"),
                }
                for key in keys:
                    identity = (key, candidate_name(item), tree["commit"])
                    if identity not in latest:
                        latest[identity] = classify(
                            source,
                            key,
                            item,
                            f"trees.jsonl:{number}",
                            screened,
                            closed=(directory / f"closure-{key}.json").is_file(),
                        )
    else:
        for number, query in jsonl(directory / "queries.jsonl"):
            if query.get("outcome") != "answered":
                continue
            key = query["key"]
            closed = (directory / f"closure-{key}.json").is_file()
            for item in query.get("results", []):
                name = candidate_name(item)
                revision = (
                    item.get("commit") or f"blob:{item.get('sha') or 'unresolved'}"
                )
                identity = (key, name, revision)
                if identity in latest:
                    continue
                # GitHub search supplies a blob SHA; the contents acquisition
                # resolves it to a pinned commit. Match by blob before creating
                # an outstanding row for the unresolved query hit.
                if (
                    source == "github-code-search"
                    and (key, name, item.get("sha")) in resolved_blobs
                ):
                    continue
                latest[identity] = classify(
                    source,
                    key,
                    item,
                    f"queries.jsonl:{number}",
                    screened,
                    closed=closed,
                )
    return sorted(
        latest.values(), key=lambda row: (row["key"], row["candidate"], row["revision"])
    )


def render(rows: list[dict[str, str]], fields: tuple[str, ...]) -> str:
    output = io.StringIO()
    writer = csv.DictWriter(
        output, fieldnames=fields, delimiter="\t", lineterminator="\n"
    )
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--evidence-root", type=Path, default=Path("docs/openapi-surface")
    )
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    changed = []
    central = []
    for source in SOURCES:
        directory = args.evidence_root / f"witness-search-{source}"
        rows = source_rows(args.evidence_root, source)
        target = directory / "records.tsv"
        expected = render(rows, FIELDS)
        if args.check:
            if not target.is_file() or target.read_text(encoding="utf-8") != expected:
                changed.append(str(target))
        else:
            target.write_text(expected, encoding="utf-8")
        for number, row in enumerate(rows, 2):
            central.append(
                {
                    **{field: row[field] for field in FIELDS if field != "evidence"},
                    "record": f"witness-search-{source}/records.tsv:{number}",
                }
            )
    central.sort(
        key=lambda row: (row["source"], row["key"], row["candidate"], row["revision"])
    )
    target = args.evidence_root / "witness-search-github/candidates.tsv"
    target.parent.mkdir(parents=True, exist_ok=True)
    expected = render(central, CENTRAL_FIELDS)
    if args.check:
        if not target.is_file() or target.read_text(encoding="utf-8") != expected:
            changed.append(str(target))
        if changed:
            print("candidate records differ from evidence: " + ", ".join(changed))
            return 1
        return 0
    target.write_text(expected, encoding="utf-8")
    print(f"{target}: {len(central)} candidate records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
