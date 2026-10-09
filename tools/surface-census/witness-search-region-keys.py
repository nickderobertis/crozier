#!/usr/bin/env python3
"""Derive the witness-search key set from the region tables at this checkout.

The set is every `FIXTURE` `gap` row, plus every `handwritten` row: a hand-written
fixture is admitted only after that key's real-specification search failed, so
the key keeps its tracked selector here, and the hand-written fixture gate reads
it from this file (docs/openapi-surface/handwritten/AGENTS.md).

Exit status: 0 with the key set on stdout; 1 when a region row needs repair
(a gap with no selector, a duplicate key, a handwritten key with no tracked
selector), named on stderr; 2 on a usage error.
"""

from __future__ import annotations

import csv
import importlib.util
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
COVERAGE = REPO / "docs/openapi-surface-coverage.md"
CATEGORIES = ("golden", "limitations", "handwritten", "gap")
# Every `census_status` a key row carries: the one vocabulary its readers import.
CENSUS_STATUSES = ("supported", "unsupported-by-census")


def region_rows(text: str) -> list[list[str]]:
    """Every entry-table row of one region file, as its eight cells.

    The one parse of these rows: golden-reach, `RankedBacklogTests` and the
    witness-search tools read this function. `\\|` inside a cell is an escaped
    pipe, not a column break — one row's `crozier sites` cell holds a Rust
    `match` pattern that uses it.
    """
    rows = []
    for line in text.splitlines():
        if not line.startswith("| "):
            continue
        cells = [
            cell.replace("\x00", "\\|").strip() for cell in line.replace("\\|", "\x00").strip().strip("|").split("|")
        ]
        if len(cells) == 8 and cells[3].strip("`") in CATEGORIES:
            rows.append(cells)
    return rows


def region_files(coverage: Path = COVERAGE) -> list[str]:
    """The region files named by the coverage document's `## The region files` table."""
    section = coverage.read_text(encoding="utf-8").partition("\n## The region files\n")[2]
    section = section.partition("\n## ")[0]
    names = re.findall(r"^\| `[^`]+` \| \[`openapi-surface/([^`/]+\.md)`\]", section, re.MULTILINE)
    if not names:
        raise ValueError(f"{coverage} has no `## The region files` table")
    return names


def census_module():
    path = REPO / "tools/surface-census/openapi-surface-census.py"
    spec = importlib.util.spec_from_file_location("witness_keys_census", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def tracked_selectors(regions: Path) -> dict[str, str]:
    """key -> selector, from the tracked key set this command derives.

    A `handwritten` row's evidence cell names its fixtures and search, not its
    selector, so the key keeps the selector it was searched with here.
    """
    path = regions / "witness-search-keys.tsv"
    if not path.is_file():
        return {}
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, dialect="excel-tab")
        if not {"key", "selector"} <= set(reader.fieldnames or ()):
            raise ValueError(
                f"{path} has no `key` and `selector` columns; regenerate it with "
                "`tools/surface-census/witness-search-region-keys.py`"
            )
        return {row["key"]: row["selector"] for row in reader}


def keys(regions: Path) -> list[tuple[str, str, str, str]]:
    census = census_module()
    tracked = tracked_selectors(regions)
    found: dict[str, tuple[str, str, str, str]] = {}
    for name in region_files():
        path = regions / name
        for cells in region_rows(path.read_text(encoding="utf-8")):
            line = " | ".join(cells)
            category = cells[3].strip("` ")
            key = cells[0].strip("` ")
            if category == "handwritten":
                # Admitted only after a failed search of this very key, so the
                # key stays in the set that search ran over, with its selector.
                if key not in tracked:
                    raise ValueError(
                        f"{path}: handwritten {key} has no selector in witness-search-keys.tsv; "
                        "restore that file from git, where the key's search recorded it"
                    )
                selector = tracked[key]
            elif category != "gap" or "FIXTURE" not in cells[7]:
                continue
            else:
                match = re.search(r"census `([^`]+)`|Shape read `([^`]+)`", line)
                if not match:
                    raise ValueError(f"{path}: gap {key} has no selector")
                selector = match.group(1) or match.group(2)
            status = CENSUS_STATUSES[0] if census.selector_error(selector) is None else CENSUS_STATUSES[1]
            if key in found:
                raise ValueError(f"duplicate gap key {key}")
            found[key] = (key, selector, name, status)
    if not found:
        raise ValueError(f"no FIXTURE gap rows or handwritten rows in {regions}")
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
        print(
            f"witness-search-region-keys: {error}; repair the FIXTURE gap rows and handwritten rows in {args.regions_dir}",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
