#!/usr/bin/env python3
"""Reduce a full Fern `enum_type: literals` tree to an overlay of a fixture's golden.

A fixture's literals golden is Fern's own output with `pydantic_config.enum_type`
left unset (fern-python-sdk's `literals` default), stripped exactly like
`expected/`. It differs from the committed python-enums `expected/` tree only in
the files that mention an enum, so it is committed as an overlay: every file
whose bytes differ from (or are absent in) `expected/`, plus a manifest naming
the files Fern does not emit in literals mode (`core/enum.py`). The e2e gate
rebuilds the full tree as `expected/` - removed + overlay.

Usage: literals_overlay.py reduce BASE TREE PROVENANCE_JSON
  BASE             the fixture's committed python-enums `expected/` tree
  TREE             the full stripped literals tree; reduced IN PLACE
  PROVENANCE_JSON  a JSON object merged into the manifest (versions, settings)
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

MANIFEST = ".crozier-literals-overlay.json"
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
        raise SystemExit(
            f"literals_overlay: no python-enums golden at {base}; "
            "generate the fixture's expected/ first"
        )
    base_files = files(base)
    tree_files = files(tree)
    for rel in sorted(tree_files & base_files):
        if (tree / rel).read_bytes() == (base / rel).read_bytes():
            (tree / rel).unlink()
    for directory in sorted(
        (p for p in tree.rglob("*") if p.is_dir()), key=lambda p: len(p.parts), reverse=True
    ):
        if not any(directory.iterdir()):
            directory.rmdir()
    manifest = {**provenance, "removed": sorted(base_files - tree_files)}
    (tree / MANIFEST).write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def main(argv: list[str]) -> int:
    if len(argv) != 4 or argv[0] != "reduce":
        print("usage: literals_overlay.py reduce BASE TREE PROVENANCE_JSON", file=sys.stderr)
        return 2
    reduce(Path(argv[1]), Path(argv[2]), json.loads(argv[3]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
