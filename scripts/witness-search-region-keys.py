#!/usr/bin/env python3
# llmlint: ignore-file[new_code_lands_in_a_project] This Cargo crate has no Nx graph; this region-key derivation command lives with the just-driven census scripts and is drift-checked by the acquisition tier.
"""Derive the witness-search key set from six region tables at this checkout."""

from __future__ import annotations

import csv
import importlib.util
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
REGIONS = (
    "document-paths.md", "parameters.md", "bodies-media.md",
    "schemas.md", "security.md", "oas31-extensions.md",
)


def census_module():
    path = REPO / "scripts/openapi-surface-census.py"
    spec = importlib.util.spec_from_file_location("witness_keys_census", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def keys(regions: Path) -> list[tuple[str, str, str, str]]:
    census = census_module()
    found: dict[str, tuple[str, str, str, str]] = {}
    for name in REGIONS:
        path = regions / name
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.startswith("|"):
                continue
            cells = [cell.strip() for cell in line.replace("\\|", "\0").strip().strip("|").split("|")]
            if len(cells) != 8 or cells[3].strip("` ") != "gap" or "FIXTURE" not in cells[7]:
                continue
            key = cells[0].strip("` ")
            match = re.search(r"census `([^`]+)`|Shape read `([^`]+)`", line)
            if not match:
                raise ValueError(f"{path}: gap {key} has no selector")
            selector = match.group(1) or match.group(2)
            status = "supported" if census.selector_error(selector) is None else "unsupported-by-census"
            if key in found:
                raise ValueError(f"duplicate gap key {key}")
            found[key] = (key, selector, name, status)
    if not found:
        raise ValueError(f"no FIXTURE gap rows in {regions}")
    return sorted(found.values())


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--regions-dir", type=Path, default=REPO / "docs/openapi-surface")
    args = parser.parse_args()
    writer = csv.writer(sys.stdout, dialect="excel-tab", lineterminator="\n")
    writer.writerow(("key", "selector", "region", "census_status"))
    try:
        writer.writerows(keys(args.regions_dir))
    except (OSError, ValueError) as error:
        print(f"witness-search-region-keys: {error}; repair the FIXTURE gap rows in {args.regions_dir}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
