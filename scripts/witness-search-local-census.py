#!/usr/bin/env python3
"""Census arbitrary pinned OpenAPI trees with the shared surface evaluator."""

from __future__ import annotations

import argparse
import csv
import concurrent.futures
import datetime
import hashlib
import importlib.util
import json
import os
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
    if path.suffix == ".tsv":
        with path.open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle, dialect="excel-tab")
            if not {"key", "selector", "census_status"} <= set(reader.fieldnames or ()):
                raise ValueError("TSV contract requires key, selector, and census_status")
            rows = [(row["key"], row["selector"]) for row in reader
                    if row["census_status"] == "supported"]
    else:
        rows = []
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith("| `") and line.count("|") == 3:
                cells = [cell.strip().strip("`") for cell in line.split("|")[1:3]]
                rows.append((cells[0], cells[1]))
    for key, selector in rows:
        if not key or any(existing == key for existing, _ in keys):
            raise ValueError(f"empty or duplicate contract key: {key!r}")
        error = CENSUS.selector_error(selector)
        if error:
            raise ValueError(error)
        keys.append((key, selector))
    if not keys:
        raise ValueError("no key/selector rows found")
    return keys


def census_one(
    job: tuple[Path, dict[str, Any], list[tuple[str, str]], Path | None],
) -> tuple[Path, str, str, str | None, list[tuple[str, int]]]:
    path, conjunctions, keys, progress = job
    if progress is not None:
        with progress.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps({"event": "start", "document": str(path),
                                     "pid": os.getpid(), "taken_utc": datetime.datetime.now(
                                         datetime.timezone.utc).isoformat()}) + "\n")
    digest = ""
    try:
        raw = path.read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        if path.suffix.lower() in {".yaml", ".yml"} and b"openapi" not in raw:
            return path, digest, "", None, [(key, 0) for key, _ in keys]
        # Some publisher trees label JSON bytes as .yaml. Parsing those with
        # the YAML reader is much slower on large composed descriptions.
        document = (
            json.loads(raw)
            if raw.lstrip().startswith((b"{", b"["))
            else CENSUS.load_document(path)
        )
        version = str(document.get("openapi") or document.get("swagger") or "") if isinstance(document, dict) else ""
        # A repository may contain generated metadata with an OpenAPI document
        # nested inside it. Only a root OpenAPI 3 document is a source document.
        counts = (CENSUS.census_document(document, conjunctions=conjunctions)
                  if version.startswith("3.") else {})
        return (
            path,
            digest,
            version,
            None,
            [(key, counts.get(selector, 0)) for key, selector in keys],
        )
    except (OSError, ValueError, CENSUS.DocumentError) as error:
        return path, digest, "", str(error), []
    finally:
        if progress is not None:
            with progress.open("a", encoding="utf-8") as handle:
                handle.write(json.dumps({"event": "end", "document": str(path),
                                         "pid": os.getpid(), "taken_utc": datetime.datetime.now(
                                             datetime.timezone.utc).isoformat()}) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--start-after", default="",
                        help="resume a sorted tree after this relative document path")
    parser.add_argument("--progress-log", type=Path,
                        help="append per-worker document start/end events for long enumerations")
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
    documents = []
    for value in args.documents:
        source, separator, root_text = value.partition("=")
        root = Path(root_text)
        if not separator or not source or not root_text or not root.is_dir():
            parser.error(
                f"--documents must be SOURCE=DIR with an existing DIR: {value}"
            )
        documents.append((source, root))
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
    for source, root in documents:
        paths = sorted(
            path
            for path in root.rglob("*")
            if path.suffix.lower() in {".json", ".yaml", ".yml"}
            and path.relative_to(root).as_posix() > args.start_after
        )
        jobs = ((path, conjunctions, keys, args.progress_log) for path in paths)
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
