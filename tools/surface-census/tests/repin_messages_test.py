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

import pytest

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


def test_the_scenario_index_writer_refuses_a_broken_catalog_and_writes_once_it_is_repaired(tmp_path: Path) -> None:
    """`write` names a golden whose metadata does not read, leaves the index as it was, then restates it."""
    root = tmp_path / "repo"
    subprocess.run(["git", "clone", "-q", "--shared", str(REPO), str(root)], check=True, timeout=600)
    script = root / "tools/surface-census/scenario-proof-index.py"
    shutil.copy2(REPO / "tools/surface-census/scenario-proof-index.py", script)
    index = root / "docs/openapi-surface/scenario-proof-index.tsv"
    row = next(
        line
        for line in index.read_text(encoding="utf-8").splitlines()[1:]
        if "\treal\t" in line and line.split("\t")[7] == "match"
    )
    golden = row.split("\t")[4].split(";")[0]
    metadata = root / golden / ".fern" / "metadata.json"
    good = metadata.read_bytes()
    metadata.write_text("{ not json", encoding="utf-8")
    # A stale derived cell the writer would restate, were its catalogs readable.
    stale = index.read_text(encoding="utf-8").replace(row, row.replace("\tmatch\t", "\tdeparture\t", 1), 1)
    assert stale != index.read_text(encoding="utf-8")
    index.write_text(stale, encoding="utf-8")
    refused = subprocess.run(
        [sys.executable, str(script), "--repo-root", str(root), "write"], capture_output=True, text=True, timeout=300
    )
    assert refused.returncode == 1
    assert f"golden {golden}'s metadata is not JSON" in refused.stderr
    assert index.read_text(encoding="utf-8") == stale, "a refused write leaves the index as it was"
    metadata.write_bytes(good)
    written = subprocess.run(
        [sys.executable, str(script), "--repo-root", str(root), "write"], capture_output=True, text=True, timeout=300
    )
    assert written.returncode == 0, written.stderr
    assert index.read_text(encoding="utf-8") == (REPO / "docs/openapi-surface/scenario-proof-index.tsv").read_text(
        encoding="utf-8"
    ), "the repaired catalogs restate the committed index"


def _measured(root: Path, out: Path) -> Any:
    """A store of the tree at `root` (its functions' universe left empty), left where `measure` leaves one."""
    reach = _load("repin_messages_golden_reach", REPO / "tools/surface-census/golden-reach.py")
    store_module = reach.RS
    tree = store_module.read_tree(root)
    commit = "a" * 40
    store = {
        "schema": store_module.SCHEMA,
        "commit": commit,
        "rustc": "1.96.0 abc",
        "llvm": "22.1.2",
        "full_at": commit,
        "steps_since_full": 0,
        "measured_at": store_module.now_iso(),
        "tests": {},
        "fixtures": {},
        "functions": tree.table(),
    }
    store_module.save(store, out / reach.STORE_FILE)
    return reach


def test_a_report_over_a_tree_its_measurement_predates_names_the_verb_and_succeeds_once_repinned(
    tmp_path: Path,
) -> None:
    root, out = tmp_path / "repo", tmp_path / "out"
    (root / "src").mkdir(parents=True)
    (root / "src" / "lib.rs").write_text("pub fn a() -> u8 {\n    1\n}\n", encoding="utf-8")
    reach = _measured(root, out)
    reach.stale_measurement(out, root)  # the store's functions are this tree's
    (root / "src" / "lib.rs").write_text("pub fn a() -> u8 {\n    2\n}\n", encoding="utf-8")
    try:
        reach.stale_measurement(out, root)
    except SystemExit as refused:
        message = str(refused)
    else:
        raise AssertionError("a store of another tree was accepted")
    assert "1 function(s) of this tree differ from it (src/lib.rs::a)" in message and f"run `{VERB}`" in message
    _measured(root, out)  # what a repin leaves: a store of this tree
    reach.stale_measurement(out, root)


def test_a_corrupt_checkout_store_is_reported_and_ignored_rather_than_stepped_from(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    reach = _load("repin_messages_golden_reach", REPO / "tools/surface-census/golden-reach.py")
    (tmp_path / reach.STORE_FILE).write_bytes(b"not gzip")
    assert reach.local_store(tmp_path) is None, "a measurement never steps from a store it cannot read"
    assert "ignoring" in capsys.readouterr().err
