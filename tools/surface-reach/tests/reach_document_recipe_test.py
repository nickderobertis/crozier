"""Offline document restatement through the real host recipe and file boundaries."""

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

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "surface-census"))
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
        ".cargo/config.toml",
        "pyproject.toml",
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
    assert f"**{len(none)}** golden rows have no golden-only witness" in expected
    count = sum(int(row["unreached_sites"]) == 0 for row in records)
    assert f"**{count}** golden rows reach every handling site" in expected
    assert f"**{len(one)}** golden rows rest on one document" in expected
    saved_attribution = json.loads((tmp_path / attribution.RECORD).read_text(encoding="utf-8"))["rows"]
    residual_cells = cells(expected, "#### Golden rows resting only on residual goldens")
    supplements, errors = repin._load("census_repin_handwritten", "handwritten-fixtures.py").read_residual_proofs(
        tmp_path
    )
    assert not errors
    assert (
        f"**{len(residual_cells) + len(supplements)}** golden rows rest only on residual golden witnesses" in expected
    )
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
    for phrase in (
        "golden rows rest on one document",
        "golden rows have no golden-only witness",
        "golden rows rest only on residual golden witnesses",
    ):
        stale = re.sub(r"\*\*\d+\*\* " + phrase, "**99999** " + phrase, stale)
    stale = re.sub(r"\d+ of \[the \d+ unreached arms\]", "99999 of [the 99999 unreached arms]", stale)
    assert stale != expected
    for args in (
        ("init", "-q"),
        ("add", "-A"),
        ("-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "-m", "fixture"),
    ):
        subprocess.run(["git", *args], cwd=tmp_path, check=True, capture_output=True)
    path.write_text(stale, encoding="utf-8")
    confirm = subprocess.run(
        ["just", "census-repin", "--confirm-port", "camel_join"],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        timeout=120,
    )
    assert confirm.returncode == 0, confirm.stderr
    for section in (
        "The reach ranking",
        "Rows resting on one document",
        "Golden rows with no golden-only witness",
        "Golden rows resting only on residual goldens",
        "Blind-spot rows' unreached-arm counts",
    ):
        assert f"stale {section}; run `just census-repin`" in confirm.stderr
    assert path.read_text(encoding="utf-8") == stale
    run = subprocess.run(["just", "census-repin"], cwd=tmp_path, capture_output=True, text=True, timeout=120)
    # The recipe completes its offline restatement, then deliberately cannot
    # start measurement in this fixture: its interpreter selector is absent.
    assert run.returncode != 0 and "interpreter selector" in run.stderr, run.stderr
    assert path.read_text(encoding="utf-8") == expected
    reach_document.rewrite(tmp_path, repin.REACH, repin._load("census_repin_handwritten", "handwritten-fixtures.py"))
    assert path.read_text(encoding="utf-8") == expected
    # A current document is silent, an absent ledger skips the optional
    # report, and unreadable report inputs produce an actionable diagnostic.
    confirmation = ["just", "census-repin", "--confirm-port", "camel_join"]
    clean = subprocess.run(confirmation, cwd=tmp_path, capture_output=True, text=True, timeout=120)
    assert clean.returncode == 0 and "stale " not in clean.stderr, clean.stderr
    saved_ledger = ledger.with_suffix(".saved")
    ledger.rename(saved_ledger)
    absent = subprocess.run(confirmation, cwd=tmp_path, capture_output=True, text=True, timeout=120)
    assert absent.returncode == 0 and "stale " not in absent.stderr, absent.stderr
    saved_ledger.rename(ledger)
    saved_index = path.with_suffix(".saved")
    path.rename(saved_index)
    unreadable = subprocess.run(confirmation, cwd=tmp_path, capture_output=True, text=True, timeout=120)
    assert unreadable.returncode == 0, unreadable.stderr
    assert "openapi-surface-coverage.md" in unreadable.stderr and "just census-repin" in unreadable.stderr
    assert not path.exists()
    saved_index.rename(path)
    rust = tmp_path / "src/ir.rs"
    original_rust = rust.read_bytes()
    signature = b"fn camel_join(words: &[String]) -> String {"
    assert signature in original_rust
    rust.write_bytes(original_rust.replace(signature, signature + b" let _drift = 1;", 1))
    drifted = subprocess.run(["just", "census-repin"], cwd=tmp_path, capture_output=True, text=True, timeout=120)
    assert drifted.returncode != 0, drifted.stderr
    assert "--confirm-port camel_join" in drifted.stderr
    assert "boolean-schema-true: stale residual attribution" in drifted.stderr
    assert "just residual-attribution" in drifted.stderr
    assert path.read_text(encoding="utf-8") == expected
    rust.write_bytes(original_rust)
    # Missing or stale measurements fail at the real recipe boundary before
    # either SDK generation or a documentation write can occur.
    record_path = tmp_path / attribution.RECORD
    saved_record = record_path.read_bytes()
    for missing in (True, False):
        if missing:
            record_path.unlink()
        else:
            record_path.write_bytes(saved_record)
            source = tmp_path / "src/lib.rs"
            source.write_bytes(source.read_bytes() + b"\n// changed generator input\n")
        refused = subprocess.run(["just", "census-repin"], cwd=tmp_path, capture_output=True, text=True, timeout=120)
        assert refused.returncode != 0
        reason = "no residual attribution" if missing else "stale residual attribution"
        assert f"boolean-schema-true: {reason}" in refused.stderr
        assert "just residual-attribution" in refused.stderr
        assert path.read_text(encoding="utf-8") == expected
    source.write_bytes(source.read_bytes().removesuffix(b"\n// changed generator input\n"))
    # Confirmation is read-only even when the renderer cannot restate a
    # missing or duplicated summary. Exercise every anchor via the recipe.
    for phrase in (
        "golden rows reach every handling site",
        "golden rows rest on one document",
        "golden rows have no golden-only witness",
        "golden rows rest only on residual golden witnesses",
    ):
        anchor = re.search(r"\*\*\d+\*\* " + phrase, expected)
        assert anchor
        for replacement in ("missing summary", anchor[0] + "\n" + anchor[0]):
            broken = expected.replace(anchor[0], replacement, 1)
            path.write_text(broken, encoding="utf-8")
            refused = subprocess.run(
                ["just", "census-repin", "--confirm-port", "camel_join"],
                cwd=tmp_path,
                capture_output=True,
                text=True,
                timeout=120,
            )
            assert refused.returncode == 0, refused.stderr
            assert "restore exactly one summary" in refused.stderr
            assert "just census-repin" in refused.stderr
            assert path.read_text(encoding="utf-8") == broken
    path.write_text(expected, encoding="utf-8")
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
