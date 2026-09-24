#!/usr/bin/env python3
"""Census arbitrary pinned OpenAPI trees with the shared surface evaluator."""

from __future__ import annotations

import argparse
import csv
import concurrent.futures
import hashlib
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parent.parent


def load_census() -> Any:
    path = REPO / "scripts/openapi-surface-census.py"
    spec = importlib.util.spec_from_file_location("local_source_census", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


CENSUS = load_census()


def contract_keys(path: Path) -> list[tuple[str, str]]:
    keys = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("| `") and line.count("|") == 3:
            cells = [cell.strip().strip("`") for cell in line.split("|")[1:3]]
            if not cells[0] or any(key == cells[0] for key, _ in keys):
                raise ValueError(f"empty or duplicate contract key: {cells[0]!r}")
            error = CENSUS.selector_error(cells[1])
            if error:
                raise ValueError(error)
            keys.append((cells[0], cells[1]))
    if not keys:
        raise ValueError("no key/selector rows found")
    return keys


def census_one(
    job: tuple[Path, dict[str, Any], list[tuple[str, str]]],
) -> tuple[Path, str, str, str | None, list[tuple[str, int]]]:
    path, conjunctions, keys = job
    digest = ""
    try:
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        document = CENSUS.load_document(path)
        version = str(document.get("openapi") or document.get("swagger") or "") if isinstance(document, dict) else ""
        counts = CENSUS.census_document(document, conjunctions=conjunctions)
        return (
            path,
            digest,
            version,
            None,
            [(key, counts.get(selector, 0)) for key, selector in keys],
        )
    except (OSError, ValueError, CENSUS.DocumentError) as error:
        return path, digest, "", str(error), []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--workers", type=int, default=1)
    output = parser.add_mutually_exclusive_group()
    output.add_argument("--all-documents", action="store_true",
                        help="emit one TSV selector result per document, including zeroes and SHA-256")
    output.add_argument("--all-documents-jsonl", action="store_true",
                        help="emit one JSON object per document with all selector counts")
    parser.add_argument(
        "--documents",
        action="append",
        required=True,
        metavar="SOURCE=DIR",
        help="recursively census JSON/YAML documents below DIR",
    )
    args = parser.parse_args()
    if args.workers < 1:
        parser.error("--workers must be positive")
    try:
        keys = contract_keys(args.contract)
    except (OSError, ValueError) as error:
        parser.error(f"invalid --contract {args.contract}: {error}")
    conjunctions = {
        selector: CENSUS.compile_conjunction(selector) for _key, selector in keys
    }
    selector_by_key = dict(keys)
    failures: list[str] = []
    writer = csv.writer(sys.stdout, dialect="excel-tab", lineterminator="\n")
    header = ("source", "key", "selector", "document", "count")
    if not args.all_documents_jsonl:
        writer.writerow((*header, "sha256", "openapi_version") if args.all_documents else header)
    for value in args.documents:
        source, separator, root_text = value.partition("=")
        root = Path(root_text)
        if not separator or not source or not root_text or not root.is_dir():
            parser.error(
                f"--documents must be SOURCE=DIR with an existing DIR: {value}"
            )
        paths = sorted(
            path
            for path in root.rglob("*")
            if path.suffix.lower() in {".json", ".yaml", ".yml"}
        )
        jobs = ((path, conjunctions, keys) for path in paths)
        with concurrent.futures.ProcessPoolExecutor(
            max_workers=args.workers
        ) as executor:
            results = executor.map(census_one, jobs, chunksize=16)
            for path, digest, version, error, hits in results:
                identity = {"source": source, "document": str(path.relative_to(root)),
                            "sha256": digest, "openapi_version": version}
                if error:
                    failures.append(f"{source}/{path.relative_to(root)}: {error}")
                    if args.all_documents_jsonl:
                        print(json.dumps({**identity, "classification": "unreadable", "error": error}, sort_keys=True))
                    continue
                if args.all_documents_jsonl:
                    print(json.dumps({**identity, "classification": "openapi-3" if version.startswith("3.") else "other-version",
                                      "selectors": {key: count for key, count in hits}}, sort_keys=True))
                    continue
                for key, count in hits:
                    if not args.all_documents and not count:
                        continue
                    selector = selector_by_key[key]
                    row = (source, key, selector, str(path.relative_to(root)), str(count))
                    writer.writerow((*row, digest, version) if args.all_documents else row)
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
