"""Ledger restatement and attribution refusals through real files and the recipe."""

from __future__ import annotations

import csv
import importlib.util
import json
import re
import shutil
import subprocess
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import reach_document
import residual_attribution_record as attribution

REPO = Path(__file__).resolve().parents[3]


def load(name: str, file: str) -> Any:
    # Hyphenated scripts have no static importable module type.
    spec = importlib.util.spec_from_file_location(name, REPO / "tools/surface-census" / file)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def synthetic(root: Path) -> attribution.Attribution:
    for name, value in {
        "src/lib.rs": "pub fn generated() {}",
        "crates/crozier-e2e/tests/e2e.rs": 'const DEMO: Corpus = Corpus {\n    api: "demo",\n    unmatched: &["unmatched.py"],\n};\nfn demo_matches_fern_output() { assert_committed_corpus_matches(&DEMO); }\n',
        "tests/fixtures/demo/expected/model.py": "value = 1\n",
        "tests/fixtures/corpus-sources/demo/openapi.yml": "openapi: 3.0.3\n",
    }.items():
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(value, encoding="utf-8")
    (root / attribution.RECORD).parent.mkdir(parents=True, exist_ok=True)
    golden, inputs = attribution.fingerprints(root, "demo")
    return attribution.Attribution("feature", "demo", ["model.py"], [], golden, inputs)


def test_attribution_round_trips_and_refuses_missing_or_changed_inputs(tmp_path: Path) -> None:
    row = synthetic(tmp_path)
    attribution.write(tmp_path, {row.key: row})
    saved = (tmp_path / attribution.RECORD).read_bytes()
    (tmp_path / attribution.RECORD).write_text("{broken", encoding="utf-8")
    with pytest.raises(ValueError, match="residual-attribution.json: cannot read attribution"):
        attribution.read(tmp_path)
    (tmp_path / attribution.RECORD).write_bytes(saved)
    loaded = attribution.read(tmp_path)
    assert attribution.require(tmp_path, row.key, row.fixture, loaded) == row
    attribution.write(tmp_path, loaded)
    assert (tmp_path / attribution.RECORD).read_bytes() == saved
    assert row.cell() == "| `feature` | `demo` | `model.py` | `byte-matched` |\n"
    for key in ("feature", "missing"):
        if key == "feature":
            (tmp_path / "src/lib.rs").write_text("pub fn changed() {}", encoding="utf-8")
        with pytest.raises(ValueError) as failure:
            attribution.require(tmp_path, key, "demo", loaded)
        assert key in str(failure.value)
        assert ("stale residual attribution" if key == "feature" else "no residual attribution") in str(failure.value)
        assert "just residual-attribution" in str(failure.value)
    # Changing only the unmatched registry must invalidate its classification.
    (tmp_path / "src/lib.rs").write_text("pub fn generated() {}", encoding="utf-8")
    registry = tmp_path / "crates/crozier-e2e/tests/e2e.rs"
    original_registry = registry.read_text(encoding="utf-8")
    registry.write_text(original_registry.replace("unmatched.py", "other.py"), encoding="utf-8")
    with pytest.raises(ValueError, match="feature: stale residual attribution"):
        attribution.require(tmp_path, row.key, row.fixture, loaded)
    registry.write_text(original_registry, encoding="utf-8")
    # Golden output is an independent content pin as well.
    (tmp_path / "src/lib.rs").write_text("pub fn generated() {}", encoding="utf-8")
    (tmp_path / "tests/fixtures/demo/expected/model.py").write_text("value = 2\n", encoding="utf-8")
    with pytest.raises(ValueError, match="feature: stale residual attribution"):
        attribution.require(tmp_path, row.key, row.fixture, loaded)


def test_recipe_restores_every_ledger_derived_section_before_measurement(tmp_path: Path) -> None:
    # Copy only what the offline readers consume, including the real attribution
    # inputs. No binary, interpreter selector or instrumented toolchain is staged.
    for directory in (
        "src",
        "templates",
        "assets",
        "tools/surface-census",
        "tools/corpus",
        "tests/fixtures/webflow-v2/expected",
        "tests/fixtures/corpus-sources/webflow-v2",
    ):
        shutil.copytree(REPO / directory, tmp_path / directory, ignore=shutil.ignore_patterns("__pycache__"))
    for name in (
        "Cargo.toml",
        "Cargo.lock",
        "rust-toolchain.toml",
        ".ruff-version",
        "justfile",
        "crates/crozier-e2e/tests/e2e.rs",
        "docs/openapi-surface-coverage.md",
    ):
        target = tmp_path / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(REPO / name, target)
    surface = tmp_path / "docs/openapi-surface"
    surface.mkdir(exist_ok=True)
    for pattern in ("*.md", "*.tsv", "*.toml", "residual-attribution.json", "*/paired-removal-comparisons.json"):
        for source in (REPO / "docs/openapi-surface").glob(pattern):
            target = surface / source.relative_to(REPO / "docs/openapi-surface")
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
    # Mark the original vendored fixtures as such without copying their SDKs.
    for source in (REPO / "tests/fixtures").glob("*/openapi.*"):
        target = tmp_path / source.relative_to(REPO)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.touch()
    ledger = surface / "golden-reach.tsv"
    lines = ledger.read_text(encoding="utf-8").splitlines()
    cells = lines[2].split("\t")
    spec, counts = cells[8].split(" ; ")[0].rsplit("=", 1)
    hit, total = map(int, counts.split("/"))
    cells[8] = cells[8].replace(f"{spec}={hit}/{total}", f"{spec}={hit}/{total + 1}", 1)
    cells[4] = str(int(cells[4]) + 1)
    cells[5] = str(int(cells[5]) + 1)
    lines[2] = "\t".join(cells)
    ledger.write_text("\n".join(lines) + "\n", encoding="utf-8")
    repin = load("document_repin", "census-repin.py")
    path = tmp_path / reach_document.INDEX
    reach_document.rewrite(tmp_path, repin.REACH, repin._load("census_repin_handwritten", "handwritten-fixtures.py"))
    expected = path.read_text(encoding="utf-8")
    # Independently derive the published cells from raw TSV, rather than using
    # the renderer to supply both sides of this assertion.
    records = list(csv.DictReader(ledger.read_text(encoding="utf-8").splitlines()[1:], delimiter="\t"))
    features = [row for row in records if not row["key"].startswith("combo-")]

    def cells(document: str, heading: str) -> list[list[str]]:
        section = document.split(heading, 1)[1].split("\n#### ", 1)[0]
        return [
            [cell.strip() for cell in line.strip("|").split("|")]
            for line in section.splitlines()
            if re.match(r"^\| (?:`|[0-9])", line)
        ]

    ranking = [
        [
            row["rank"],
            f"`{row['key']}`",
            f"`{row['region']}`",
            f"**{row['unreached_sites']}**",
            f"**{row['unreached_regions']}**",
            f"**{len(row['witnesses'].split(',')) if row['witnesses'] != '-' else 0}**",
        ]
        for row in features
        if int(row["unreached_sites"])
    ]
    assert [row[:6] for row in cells(expected, "#### The reach ranking")] == ranking
    one = [
        [f"`{row['key']}`", f"`{row['region']}`", f"`{row['witnesses']}`"]
        for row in features
        if row["witnesses"] != "-" and "," not in row["witnesses"]
    ]
    assert cells(expected, "#### Rows resting on one document") == one
    none = [
        [f"`{row['key']}`", f"`{row['region']}`", ", ".join(f"`{name}`" for name in row["outside"].split(","))]
        for row in features
        if row["witnesses"] == "-"
    ]
    assert cells(expected, "#### Golden rows with no golden-only witness") == none
    count = sum(int(row["unreached_sites"]) == 0 for row in records)
    assert f"**{count}** golden rows reach every handling site" in expected
    assert f"**{len(one)}** golden rows rest on one document" in expected
    saved_attribution = json.loads((tmp_path / attribution.RECORD).read_text(encoding="utf-8"))["rows"]
    residual_cells = cells(expected, "#### Golden rows resting only on residual goldens")
    assert [row[0].strip("`") for row in residual_cells] == [row["key"] for row in saved_attribution]
    for row, measured in zip(residual_cells, saved_attribution, strict=True):
        assert row[1] == f"`{measured['fixture']}`"
        assert re.findall(r"`([^`]+)`", row[2]) == measured["byte_matched"] + measured["unmatched"]
    arms = Counter(
        spec.split("::", 1)[0]
        for row in features
        for site in row["sites"].split(" ; ")
        if "=" in site
        for spec, counts in [site.rsplit("=", 1)]
        if counts.startswith("0/")
    )
    for line in expected.splitlines():
        match = re.match(r"\| `(src/[^`]+\.rs)` \|", line)
        if match and arms[match[1]]:
            assert f"{arms[match[1]]} of [the {sum(arms.values())} unreached arms]" in line

    stale = expected
    for heading in (
        "#### The reach ranking",
        "#### Rows resting on one document",
        "#### Golden rows with no golden-only witness",
        "#### Golden rows resting only on residual goldens",
    ):
        stale = reach_document.table(stale, heading, ["| stale | stale | stale |\n"])
    stale = re.sub(
        r"\*\*\d+\*\* golden rows reach every handling site", "**99999** golden rows reach every handling site", stale
    )
    stale = re.sub(r"\d+ of \[the \d+ unreached arms\]", "99999 of [the 99999 unreached arms]", stale)
    assert stale != expected
    for args in (
        ("init", "-q"),
        ("add", "-A"),
        ("-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "-m", "fixture"),
    ):
        subprocess.run(["git", *args], cwd=tmp_path, check=True, capture_output=True)
    path.write_text(stale, encoding="utf-8")
    run = subprocess.run(["just", "census-repin"], cwd=tmp_path, capture_output=True, text=True, timeout=120)
    # The recipe completes its offline restatement, then deliberately cannot
    # start measurement in this fixture: its interpreter selector is absent.
    assert run.returncode != 0 and "interpreter selector" in run.stderr, run.stderr
    assert path.read_text(encoding="utf-8") == expected
    reach_document.rewrite(tmp_path, repin.REACH, repin._load("census_repin_handwritten", "handwritten-fixtures.py"))
    assert path.read_text(encoding="utf-8") == expected
    # A new residual-only population must not borrow one witness's measurement.
    ledger_lines = ledger.read_text(encoding="utf-8").splitlines()
    for number, line in enumerate(ledger_lines):
        if "\tboolean-schema-true\t" in line:
            fields = line.split("\t")
            fields[6] += ",komga"
            ledger_lines[number] = "\t".join(fields)
            break
    ledger.write_text("\n".join(ledger_lines) + "\n", encoding="utf-8")
    refused = subprocess.run(["just", "census-repin"], cwd=tmp_path, capture_output=True, text=True, timeout=120)
    assert refused.returncode != 0
    assert "boolean-schema-true: multiple residual witnesses" in refused.stderr
    assert "just residual-attribution" in refused.stderr
    assert path.read_text(encoding="utf-8") == expected


@pytest.mark.parametrize("anchor", ["golden rows rest on one document", "golden rows reach every handling site"])
def test_a_missing_summary_anchor_is_refused(anchor: str) -> None:
    with pytest.raises(ValueError, match="restore exactly one summary.*just census-repin"):
        reach_document.summary("missing anchor", rf"\*\*\d+\*\* {anchor}", "replacement", anchor)


def test_a_missing_ownership_source_is_refused_without_inventing_boundaries(tmp_path: Path) -> None:
    text = (
        (REPO / reach_document.INDEX)
        .read_text(encoding="utf-8")
        .replace("#### The rows this measurement's first pass owned", "missing ownership source", 1)
    )
    with pytest.raises(ValueError, match="restore exactly one ownership source.*just census-repin"):
        reach_document.render(tmp_path, text, [], set(), set(), set(), {}, set())
