#!/usr/bin/env python3
# llmlint: ignore-file[new_code_lands_in_a_project] this repository is a Cargo crate driven by `just`, with no Nx workspace (no nx.json or project.json anywhere); its scripts live together in scripts/, which is where this one sits beside the census scripts it shares an engine with.
"""Check that a `differential` probe pair isolates the feature its key names.

Contract A's `differential` form proves non-generation by two committed Fern
trees that agree byte for byte, and that proof only speaks for the feature if
the two documents differ in that feature and in nothing else. This checks the
three conditions on the parsed documents, never on their text:

1. the probe declares the shape under that shape's census selector, and the
   control does not;
2. the two documents are not identical;
3. every place the two differ is part of the declaration: putting the control's
   value back at that one place lowers the probe's count under the selector.
   A difference that leaves the count where it was lies outside the
   declaration, so the pair would be varying something besides the feature.

The selector is read from the key's own region row, which is where every
feature's census selector is recorded: the first code span in its `evidence`
cell that the census grammar accepts. `tests/e2e.rs` runs this for every
`differential` row of `docs/openapi-surface/probe-expected/MANIFEST.tsv`.

Usage: probe-differential-isolation.py ROOT KEY PROBE CONTROL
Quiet with exit 0 when the pair isolates the feature. Otherwise it prints why,
naming the key, and exits 1.
"""

from __future__ import annotations

import copy
import importlib.util
import re
import sys
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parent.parent
ABSENT = object()


def load_census() -> Any:
    path = REPO / "scripts" / "openapi-surface-census.py"
    spec = importlib.util.spec_from_file_location("probe_isolation_census", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def region_evidence(root: Path, key: str) -> str | None:
    """The `evidence` cell of `key`'s row in one of the six region files."""
    for path in sorted((root / "docs" / "openapi-surface").glob("*.md")):
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.startswith("| "):
                continue
            cells = [c.strip() for c in line.replace("\\|", "\x00").strip().strip("|").split("|")]
            if len(cells) == 8 and cells[0].strip("`") == key:
                return cells[4].replace("\x00", "\\|")
    return None


def selector_for(census: Any, root: Path, key: str) -> str:
    evidence = region_evidence(root, key)
    if evidence is None:
        raise SystemExit(
            f"{key}: no region row carries this key, so it names no census selector — "
            "spell the manifest key exactly as its region row does"
        )
    for span in re.findall(r"`([^`]+)`", evidence):
        if census.selector_error(span) is None:
            return span
    raise SystemExit(
        f"{key}: its region row's evidence cell cites no census selector — cite the "
        "shape's selector there in a code span, as `census <selector>`"
    )


def differences(left: Any, right: Any, path: tuple = ()) -> list[tuple]:
    """Every minimal path at which two parsed documents disagree."""
    if isinstance(left, dict) and isinstance(right, dict):
        found: list[tuple] = []
        for name in list(left) + [name for name in right if name not in left]:
            if name not in left or name not in right:
                found.append(path + (name,))
            else:
                found += differences(left[name], right[name], path + (name,))
        return found
    if isinstance(left, list) and isinstance(right, list) and len(left) == len(right):
        found = []
        for index, (a, b) in enumerate(zip(left, right)):
            found += differences(a, b, path + (index,))
        return found
    return [] if left == right and type(left) is type(right) else [path]


def lookup(node: Any, path: tuple) -> Any:
    for step in path:
        if isinstance(node, dict):
            if step not in node:
                return ABSENT
            node = node[step]
        else:
            node = node[step]
    return node


def reverted(probe: Any, control: Any, path: tuple) -> Any:
    """The probe with the control's value put back at `path`, and nothing else."""
    document = copy.deepcopy(probe)
    if not path:
        return copy.deepcopy(control)
    parent = lookup(document, path[:-1])
    value = lookup(control, path)
    if value is ABSENT:
        del parent[path[-1]]
    else:
        parent[path[-1]] = copy.deepcopy(value)
    return document


def failures(root: Path, key: str, probe_path: Path, control_path: Path) -> list[str]:
    census = load_census()
    selector = selector_for(census, root, key)
    probe = census.load_document(probe_path)
    control = census.load_document(control_path)

    def count(document: Any) -> int:
        return census.census_document(document).get(selector, 0)

    declared = count(probe)
    found: list[str] = []
    if probe_path.read_bytes() == control_path.read_bytes():
        found.append(
            f"{key}: the probe and its control are byte-identical documents — the probe "
            "must declare the feature and the control must not"
        )
    if declared == 0:
        found.append(
            f"{key}: the probe does not declare `{selector}`, the shape its row names — "
            "add the declaration to the probe document"
        )
    if count(control):
        found.append(
            f"{key}: the control declares `{selector}`, so the pair does not isolate it — "
            "remove the declaration from the control document"
        )
    if declared and not found:
        for path in differences(probe, control):
            if count(reverted(probe, control, path)) >= declared:
                shown = "/".join(str(step) for step in path) or "(the document root)"
                found.append(
                    f"{key}: the probe and control differ at `{shown}`, "
                    f"outside the `{selector}` declaration — make the two documents "
                    "identical there, so they differ only in the feature"
                )
    return found


def main(argv: list[str]) -> int:
    if len(argv) != 4:
        print("usage: probe-differential-isolation.py ROOT KEY PROBE CONTROL", file=sys.stderr)
        return 2
    root, key, probe, control = Path(argv[0]), argv[1], Path(argv[2]), Path(argv[3])
    found = failures(root, key, probe, control)
    for line in found:
        print(line, file=sys.stderr)
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
