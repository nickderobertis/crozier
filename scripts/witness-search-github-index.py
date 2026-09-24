#!/usr/bin/env python3
"""Build the three-source candidate index from its per-source JSONL evidence.

The index is a pointer, not a second acquisition ledger. Query results awaiting
fetch remain in queries.jsonl and are not silently classified as candidates.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
from pathlib import Path
from typing import Any

SOURCES = (
    "github-code-search",
    "github-publisher-trees",
    "sourcegraph",
)
FIELDS = (
    "repository",
    "path",
    "sha256",
    "pinned_refs",
    "sources",
    "classification",
    "declared_keys",
    "licence",
    "ref_screen",
    "fern",
    "disposition",
    "evidence",
    "screen_evidence",
)
SCREEN_OUTCOMES = {"witness-found", "witness-blocked", "fern-rejected", "not-owed"}


def records(path: Path) -> list[tuple[int, dict[str, Any]]]:
    if not path.is_file():
        return []
    return [
        (number, json.loads(line))
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1)
    ]


def latest_candidates(root: Path) -> list[tuple[str, int, dict[str, Any]]]:
    """One current verdict per source/result/key; retries supersede failures."""
    latest: dict[tuple[str, str, str, str, str], tuple[str, int, dict[str, Any]]] = {}
    for source in SOURCES:
        directory = root / f"witness-search-{source}"
        filename = (
            "documents.jsonl"
            if source == "github-publisher-trees"
            else "candidates.jsonl"
        )
        for number, row in records(directory / filename):
            identity = (
                source,
                row["repository"],
                row["path"],
                row.get("commit", ""),
                row.get("key", ""),
            )
            latest[identity] = (f"witness-search-{source}/{filename}", number, row)
    return list(latest.values())


def latest_screens(
    root: Path,
) -> dict[tuple[str, str, str], tuple[str, int, dict[str, Any]]]:
    latest = {}
    for source in SOURCES:
        filename = f"witness-search-{source}/screens.jsonl"
        for number, row in records(root / filename):
            identity = (row["repository"], row["path"], row["sha256"])
            latest[identity] = (filename, number, row)
    return latest


def index_rows(root: Path) -> list[dict[str, str]]:
    screens = latest_screens(root)
    groups: dict[tuple[str, str, str], list[tuple[str, int, dict[str, Any]]]] = {}
    for reference in latest_candidates(root):
        row = reference[2]
        digest = row.get("sha256") or f"unfetched:{row.get('commit', 'unknown')}"
        groups.setdefault((row["repository"], row["path"], digest), []).append(
            reference
        )

    indexed = []
    for (repository, path, digest), evidence in sorted(groups.items()):
        sources = sorted(
            {item[0].split("/")[0].removeprefix("witness-search-") for item in evidence}
        )
        refs = sorted({str(item[2].get("commit") or "unreported") for item in evidence})
        keys: set[str] = set()
        statuses: set[str] = set()
        for _, _, row in evidence:
            status = row.get("disposition") or row.get("status") or "unreported"
            statuses.add(status)
            if status == "declares" and row.get("key"):
                keys.add(row["key"])
            for key, count in row.get("selector_counts", {}).items():
                if count:
                    keys.add(key)
        classification = (
            "declares"
            if keys
            else "acquisition-failure"
            if "acquisition-failure" in statuses
            else "parse-failure"
            if "parse-failure" in statuses
            else "does-not-declare"
            if "does-not-declare" in statuses or "readable" in statuses
            else "excluded-non-openapi-3"
            if "excluded-non-openapi-3" in statuses
            else "unreported"
        )
        screen = screens.get((repository, path, digest))
        if screen:
            screen_file, screen_line, verdict = screen
            if verdict["disposition"] not in SCREEN_OUTCOMES:
                raise ValueError(
                    f"{screen_file}:{screen_line}: unfinished screen disposition"
                )
            licence = verdict["license"]
            ref_screen = verdict["ref"]
            fern = verdict["fern"]
            disposition = verdict["disposition"]
            screen_evidence = f"{screen_file}:{screen_line}"
        elif keys:
            licence = ref_screen = fern = disposition = screen_evidence = (
                "outstanding-screen"
            )
        else:
            licence = ref_screen = fern = screen_evidence = (
                "not-applicable-no-declaration"
            )
            disposition = classification
        indexed.append(
            {
                "repository": repository,
                "path": path,
                "sha256": digest,
                "pinned_refs": ",".join(refs),
                "sources": ",".join(sources),
                "classification": classification,
                "declared_keys": ",".join(sorted(keys)) or "none",
                "licence": licence,
                "ref_screen": ref_screen,
                "fern": fern,
                "disposition": disposition,
                "evidence": ";".join(
                    f"{file}:{line}" for file, line, _ in sorted(evidence)
                ),
                "screen_evidence": screen_evidence,
            }
        )
    return indexed


def render(root: Path) -> str:
    output = io.StringIO()
    writer = csv.DictWriter(
        output, fieldnames=FIELDS, delimiter="\t", lineterminator="\n"
    )
    writer.writeheader()
    writer.writerows(index_rows(root))
    return output.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--evidence-root", type=Path, default=Path("docs/openapi-surface")
    )
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    target = args.evidence_root / "witness-search-github/candidates.tsv"
    expected = render(args.evidence_root)
    if args.check:
        if not target.is_file() or target.read_text(encoding="utf-8") != expected:
            print(f"{target}: candidate index differs from per-source evidence")
            return 1
        return 0
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(expected, encoding="utf-8")
    print(f"{target}: {len(expected.splitlines()) - 1} candidates")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
