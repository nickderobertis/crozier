#!/usr/bin/env python3
"""Reduce a full Fern tree generated under one non-default setting to an overlay.

A setting golden (`expected-literals/` for `enum_type` unset,
`expected-default-max-retries/` for `default_max_retries`) is Fern's own output
for a fixture's spec with one generator setting changed, stripped exactly like
`expected/`. It differs from the committed `expected/` tree only in the files
that setting reaches, so it is committed as an overlay: every file whose bytes
differ from (or are absent in) `expected/`, plus a manifest naming the files
Fern does not emit under the setting (literals drop `core/enum.py`). The e2e
gate rebuilds the full tree as `expected/` - removed + overlay.

Usage: golden_overlay.py reduce BASE TREE PROVENANCE_JSON
  BASE             the fixture's committed python-enums `expected/` tree
  TREE             the full stripped setting tree; reduced IN PLACE
  PROVENANCE_JSON  a JSON object merged into the manifest (versions, settings)
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

MANIFEST = ".crozier-overlay.json"
# Provenance of the base tree, never part of either generated tree.
IGNORED = {".crozier-fern-golden.json", MANIFEST}


def files(root: Path) -> set[str]:
    return {
        path.relative_to(root).as_posix()
        for path in root.rglob("*")
        if path.is_file() and path.relative_to(root).as_posix() not in IGNORED
    }


def reduce(base: Path, tree: Path, provenance: dict[str, object]) -> None:
    if not base.is_dir():
        raise SystemExit(f"golden_overlay: no python-enums golden at {base}; generate the fixture's expected/ first")
    base_files = files(base)
    tree_files = files(tree)
    for rel in sorted(tree_files & base_files):
        if (tree / rel).read_bytes() == (base / rel).read_bytes():
            (tree / rel).unlink()
    for directory in sorted((p for p in tree.rglob("*") if p.is_dir()), key=lambda p: len(p.parts), reverse=True):
        if not any(directory.iterdir()):
            directory.rmdir()
    manifest = {**provenance, "removed": sorted(base_files - tree_files)}
    (tree / MANIFEST).write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def main(argv: list[str]) -> int:
    if len(argv) != 4 or argv[0] != "reduce":
        print("usage: golden_overlay.py reduce BASE TREE PROVENANCE_JSON", file=sys.stderr)
        return 2
    tree = Path(argv[2])
    if not tree.is_dir():
        raise SystemExit(f"golden_overlay: no generated tree at {tree}; pass the directory Fern generated into")
    try:
        provenance = json.loads(argv[3])
    except json.JSONDecodeError as error:
        raise SystemExit(
            f"golden_overlay: PROVENANCE_JSON is not JSON ({error.msg}); pass the overlay's "
            "provenance as one JSON object"
        ) from None
    if not isinstance(provenance, dict) or "removed" in provenance:
        raise SystemExit(
            "golden_overlay: PROVENANCE_JSON must be a JSON object without a `removed` key "
            "(the reduction writes that one)"
        )
    reduce(Path(argv[1]), tree, provenance)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
