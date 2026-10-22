#!/usr/bin/env python3
"""Read the shared, evidence-backed output-insensitive dispositions.

Comparison records use schema_version 1 and contain the complete before/after
relative-file SHA-256 maps. They measure each generator separately: equality
between generators is the corpus gate's responsibility, not this disposition.
"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import re
import sys
import tomllib
from pathlib import Path
from types import ModuleType

REGISTRY = Path("docs/openapi-surface/output-insensitive.tsv")
COLUMNS = ("key", "context", "search_record", "fern_comparison", "crozier_comparison")
SHA256 = re.compile(r"[0-9a-f]{64}")


def local_file(root: Path, value: str) -> Path:
    """Keep evidence references inside the committed documentation tree."""
    path = Path(value)
    if path.is_absolute() or ".." in path.parts or path.parts[:2] != ("docs", "openapi-surface"):
        raise ValueError(f"invalid evidence path {value!r}")
    resolved = (root / path).resolve()
    if not resolved.is_relative_to((root / "docs/openapi-surface").resolve()):
        raise ValueError(f"evidence escapes documentation: {value!r}")
    if not resolved.is_file():
        raise ValueError(f"missing comparison or search record: {value}")
    return resolved


def check_comparison(path: Path, generator: str, pin: dict) -> None:
    """Reject incomplete, uncertified, or output-sensitive comparison records."""
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or set(data) != {
        "schema_version",
        "generator",
        "fern_cli_version",
        "fern_python_sdk_version",
        "before",
        "after",
    }:
        raise ValueError(f"{path}: invalid comparison fields")
    if type(data["schema_version"]) is not int or data["schema_version"] != 1:
        raise ValueError(f"{path}: unsupported comparison schema_version")
    if data["generator"] != generator or (data["fern_cli_version"], data["fern_python_sdk_version"]) != (
        pin["cliVersion"],
        pin["generatorVersion"],
    ):
        raise ValueError(f"{path}: comparison does not use {generator} at the certified pair")
    for side in ("before", "after"):
        files = data[side]
        if not isinstance(files, dict) or not files:
            raise ValueError(f"{path}: {side} must record a non-empty complete generated tree")
        for name, digest in files.items():
            if not isinstance(name, str) or not name or Path(name).is_absolute() or ".." in Path(name).parts:
                raise ValueError(f"{path}: invalid generated-file path")
            if not isinstance(digest, str) or not SHA256.fullmatch(digest):
                raise ValueError(f"{path}: invalid generated-file SHA-256")
    if data["before"] != data["after"]:
        raise ValueError(f"{path}: generated files differ")


def load_reader(name: str, filename: str) -> ModuleType:
    """Reuse the canonical region and reach readers."""
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(filename))
    if spec is None or spec.loader is None:
        raise ValueError(f"cannot load the canonical reader {filename}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def proven_contexts(root: Path) -> set[tuple[str, str]]:
    """Read feature and arm proof claims without changing their ledger formats."""
    surface = root / "docs/openapi-surface"
    proven: set[tuple[str, str]] = set()
    regions = load_reader("output_insensitive_regions", "witness-search-region-keys.py")
    for path in surface.glob("*.md"):
        for cells in regions.region_rows(path.read_text(encoding="utf-8")):
            if cells[3].strip("`") == "golden":
                proven.add((cells[0].strip("`"), "-"))
    for path in (surface / "handwritten").glob("*/evidence.toml"):
        data = tomllib.loads(path.read_text(encoding="utf-8"))
        for cover in data.get("covers", []):
            proven.add((cover["key"], cover.get("arm", "-")))
    ledger = surface / "golden-reach.tsv"
    if ledger.exists():
        module = load_reader("output_insensitive_reach", "golden-reach.py")
        for _rank, reach in module.read_ledger(ledger):
            for name, hit, _total in reach.sites:
                if hit:
                    proven.add((reach.key, name))
    return proven


def read_records(root: Path) -> tuple[set[tuple[str, str]], list[str]]:
    """Return decided contexts and diagnostics; invalid evidence never settles one."""
    registry = root / REGISTRY
    if not registry.exists():
        return set(), []
    records: set[tuple[str, str]] = set()
    failures: list[str] = []
    try:
        pin = json.loads((root / "assets/scaffolding/metadata.json").read_text(encoding="utf-8"))
        proven = proven_contexts(root)
        with registry.open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle, delimiter="\t", quoting=csv.QUOTE_NONE)
            if reader.fieldnames != list(COLUMNS):
                raise ValueError(f"expected columns {COLUMNS}")
            seen: set[tuple[str, str]] = set()
            for row in reader:
                try:
                    if set(row) != set(COLUMNS) or any(not isinstance(v, str) or not v for v in row.values()):
                        raise ValueError("incomplete disposition row")
                    key, context = row["key"], row["context"]
                    pair = (key, context)
                    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", key):
                        raise ValueError("invalid census key")
                    if pair in seen:
                        raise ValueError("duplicate key and context")
                    seen.add(pair)
                    if pair in proven:
                        raise ValueError("key/context is also claimed proven")
                    search = local_file(root, row["search_record"])
                    if key not in search.read_text(encoding="utf-8"):
                        raise ValueError("search record does not cite the key")
                    for generator in ("fern", "crozier"):
                        check_comparison(local_file(root, row[f"{generator}_comparison"]), generator, pin)
                    records.add(pair)
                except (OSError, KeyError, TypeError, ValueError) as error:
                    failures.append(f"{REGISTRY}: {row.get('key', '?')}: {error}")
    except (OSError, KeyError, TypeError, ValueError) as error:
        failures.append(f"{REGISTRY}: {error}")
    return records, failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    _records, failures = read_records(args.root)
    for failure in failures:
        print(f"output-insensitive: {failure}; restore the measured evidence and rerun", file=sys.stderr)
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
