"""Every stale census table names its one fix, `just census-repin`.

Each case makes one table stale on a scratch copy of the committed tables and
runs the real check that reads it: a site anchor through `golden-reach.py
sites`, a ledger row through the reach-cell comparison the census suite runs,
and a row of `witness-search-registries/outstanding.tsv` through
`witness-search-registries-index.py --check`.
"""

from __future__ import annotations

import importlib.util
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parents[3]
REGIONS = REPO / "docs" / "openapi-surface"
VERB = "just census-repin"


def _load(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules.setdefault(name, module)
    spec.loader.exec_module(module)
    return module


def test_a_site_whose_anchor_no_longer_resolves_names_the_verb(tmp_path: Path) -> None:
    table = (REGIONS / "golden-reach-sites.tsv").read_text(encoding="utf-8")
    spec = "src/ir.rs::untagged_inline_discriminator[if untagged \\{]"
    assert spec in table, "the case anchors on a committed site; pick another if this one moved"
    stale = tmp_path / "golden-reach-sites.tsv"
    stale.write_text(table.replace(spec, spec.replace("if untagged", "if untagged_and_moved"), 1), encoding="utf-8")
    run = subprocess.run(
        [sys.executable, str(REPO / "tools/surface-census/golden-reach.py"), "sites", "--table", str(stale)],
        capture_output=True,
        text=True,
        timeout=300,
    )
    assert run.returncode != 0
    assert "matches 0 lines of its function" in run.stderr
    assert f"run `{VERB}`" in run.stderr


def test_a_ledger_row_its_reach_cell_no_longer_renders_names_the_verb(tmp_path: Path) -> None:
    regions = tmp_path / "docs" / "openapi-surface"
    regions.mkdir(parents=True)
    for path in REGIONS.glob("*.md"):
        shutil.copy2(path, regions / path.name)
    for name in ("golden-reach.tsv", "golden-reach-sites.tsv"):
        shutil.copy2(REGIONS / name, regions / name)
    # A cell links its row's arm-search record where one exists.
    shutil.copytree(REGIONS / "golden-reach-witnesses" / "searches", regions / "golden-reach-witnesses" / "searches")
    reach = _load("repin_messages_golden_reach", REPO / "tools/surface-census/golden-reach.py")
    assert reach.stale_cells(regions) == [], "the committed cells are their ledger rows'"
    ledger = (regions / "golden-reach.tsv").read_text(encoding="utf-8").splitlines(keepends=True)
    row = next(i for i, line in enumerate(ledger[2:], start=2) if "=0/" not in line and "/" in line.split("\t")[8])
    fields = ledger[row].split("\t")
    spec, _, counts = fields[8].split(" ; ")[0].rpartition("=")
    hit, _, total = counts.partition("/")
    fields[8] = fields[8].replace(f"{spec}={hit}/{total}", f"{spec}={int(hit) - 1}/{total}", 1)
    ledger[row] = "\t".join(fields)
    (regions / "golden-reach.tsv").write_text("".join(ledger), encoding="utf-8")
    failures = reach.stale_cells(regions)
    assert len(failures) == 1, failures
    assert f"`{fields[1]}`" in failures[0] and f"run `{VERB}`" in failures[0]


def test_a_stale_outstanding_row_names_the_verb(tmp_path: Path) -> None:
    root = tmp_path / "openapi-surface"
    root.mkdir()
    for path in REGIONS.glob("witness-search-*"):
        if path.is_file():
            shutil.copy2(path, root / path.name)
        else:
            (root / path.name).mkdir()
            for table in path.glob("*.tsv"):
                shutil.copy2(table, root / path.name / table.name)
    command = [
        sys.executable,
        str(REPO / "tools/witness-search/witness-search-registries-index.py"),
        "--root",
        str(root),
    ]
    assert subprocess.run([*command, "--check"], capture_output=True, text=True, timeout=120).returncode == 0
    outstanding = root / "witness-search-registries" / "outstanding.tsv"
    lines = outstanding.read_text(encoding="utf-8").splitlines(keepends=True)
    assert len(lines) > 1, "the committed index lists outstanding items"
    outstanding.write_text("".join(lines[:1] + lines[2:]), encoding="utf-8")
    stale = subprocess.run([*command, "--check"], capture_output=True, text=True, timeout=120)
    assert stale.returncode == 1
    assert f"outstanding.tsv is stale; run `{VERB}`" in stale.stderr
