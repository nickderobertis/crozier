#!/usr/bin/env python3
"""Census arbitrary pinned OpenAPI trees with the shared surface evaluator."""

from __future__ import annotations

import argparse
import csv
import concurrent.futures
import hashlib
import importlib.util
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
) -> tuple[Path, str, str | None, list[tuple[str, int]]]:
    path, conjunctions, keys = job
    try:
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        counts = CENSUS.census_document(
            CENSUS.load_document(path), conjunctions=conjunctions
        )
        return (
            path,
            digest,
            None,
            [(key, counts.get(selector, 0)) for key, selector in keys],
        )
    except (OSError, ValueError, CENSUS.DocumentError) as error:
        return path, "", str(error), []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--all-documents", action="store_true",
                        help="emit one selector result per document, including zeroes and SHA-256")
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
    rows: list[tuple[str, ...]] = []
    failures: list[str] = []
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
            for path, digest, error, hits in results:
                if error:
                    failures.append(f"{source}/{path.relative_to(root)}: {error}")
                    continue
                for key, count in hits:
                    if not args.all_documents and not count:
                        continue
                    selector = selector_by_key[key]
                    row = (source, key, selector, str(path.relative_to(root)), str(count))
                    rows.append((*row, digest) if args.all_documents else row)
    writer = csv.writer(sys.stdout, dialect="excel-tab", lineterminator="\n")
    header = ("source", "key", "selector", "document", "count")
    writer.writerow((*header, "sha256") if args.all_documents else header)
    writer.writerows(rows)
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
