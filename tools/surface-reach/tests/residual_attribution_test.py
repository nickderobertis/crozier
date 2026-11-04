#!/usr/bin/env python3
"""`tools/surface-census/residual-attribution.py`, run for real, against the table
it feeds.

The coverage report's residual-attribution table names, for every `golden` row
resting only on goldens that declare an `unmatched` residual, which of the
witness's files byte-match and which stay an open gap. The script measures that
by generating every such witness twice with the built `crozier` and formatting
with `ruff`, so this suite needs both: `crozier:build` runs before it, and a
missing binary or `ruff` fails it with the command that supplies it. The
table's offline shape checks are `tools/surface-census/tests/surface_census_test.py`'s.
"""

from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import os
import shutil
import subprocess
import sys
import unittest
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "tools" / "surface-census" / "tests"))

from surface_census_test import residual_attributions  # noqa: E402 - sys.path must name its directory first

SCRIPT = REPO / "tools" / "surface-census" / "residual-attribution.py"
BINARY = REPO / "target" / "debug" / ("crozier.exe" if os.name == "nt" else "crozier")


class ResidualAttributionTests(unittest.TestCase):
    def test_the_residual_attribution_table_is_the_scripts_own_output(self) -> None:
        self.assertTrue(BINARY.is_file(), f"no {BINARY.relative_to(REPO)}; run `just nx run crozier:build`")
        self.assertIsNotNone(shutil.which("ruff"), "no ruff on PATH; install it with `just bootstrap`")
        completed = subprocess.run(
            [sys.executable, str(SCRIPT)],
            cwd=REPO,
            capture_output=True,
            text=True,
            timeout=1800,
            encoding="utf-8",
        )
        self.assertEqual(0, completed.returncode, completed.stderr)
        measured = {
            row["key"]: (row["fixture"], row["byte_matched"], row["unmatched"])
            for row in map(json.loads, completed.stdout.splitlines())
        }
        table = residual_attributions(REPO)
        self.assertEqual(set(table), set(measured))
        for key, (witness, files, gaps, verdict) in table.items():
            with self.subTest(key=key):
                fixture, matched, unmatched = measured[key]
                self.assertEqual(witness, fixture)
                self.assertEqual(sorted(files), sorted(matched))
                self.assertEqual(
                    sorted(gaps),
                    sorted(unmatched),
                    f"{key}: every `unmatched` file it moves is an open gap the table names",
                )
                expected = "split" if matched and unmatched else "byte-matched" if matched else "open gap"
                self.assertEqual(expected, verdict)

    def test_supplemental_null_proof_closes_only_the_approved_feature(self) -> None:
        commands = (
            [sys.executable, str(SCRIPT), "--key", "schema-example-null"],
            [sys.executable, str(SCRIPT), "--key", "schema-example-null", "--real-witnesses-only"],
        )
        closed, original = [
            subprocess.run(command, cwd=REPO, capture_output=True, text=True, timeout=1800, encoding="utf-8")
            for command in commands
        ]
        self.assertEqual(0, closed.returncode, closed.stderr)
        self.assertEqual("", closed.stdout)
        self.assertEqual(0, original.returncode, original.stderr)
        measured = json.loads(original.stdout)
        self.assertEqual("schema-example-null", measured["key"])
        self.assertEqual([], measured["byte_matched"])
        self.assertEqual([], measured["unmatched"])


class AMissingWitnessSource(unittest.TestCase):
    def test_a_case_whose_witness_has_no_committed_source_names_the_fix(self) -> None:
        """The script's own refusal, before it builds anything over a source that is not there."""
        spec = importlib.util.spec_from_file_location("residual_attribution_missing", SCRIPT)
        assert spec is not None and spec.loader is not None
        # The script's globals are reassigned below, which a plain `ModuleType` does not declare.
        module: Any = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        module.CROZIER = Path(sys.executable)
        module.CASES = {"some-row": ("no-such-witness", lambda document: 1)}
        if shutil.which("ruff") is None:
            self.fail("no ruff on PATH; install it with `just bootstrap`")
        with self.assertRaises(SystemExit) as refused, contextlib.redirect_stdout(io.StringIO()):
            module.main([])
        self.assertIn("some-row's witness no-such-witness has no committed source", str(refused.exception))
        self.assertIn("`just lint-corpus-sources` names what is missing", str(refused.exception))


def test_record_publication_runs_the_cli_and_preserves_unselected_rows(tmp_path: Path) -> None:
    """The real binary measures a small document; only the selected record changes."""
    for directory in ("src", "templates", "assets"):
        shutil.copytree(REPO / directory, tmp_path / directory)
    for name in ("Cargo.toml", "Cargo.lock", "rust-toolchain.toml", ".ruff-version"):
        shutil.copy2(REPO / name, tmp_path / name)
    scripts = tmp_path / "tools/surface-census"
    scripts.mkdir(parents=True)
    for source in SCRIPT.parent.glob("*.py"):
        shutil.copy2(source, scripts / source.name)
    corpus = tmp_path / "tools/corpus"
    corpus.mkdir()
    shutil.copy2(REPO / "tools/corpus/corpus_remote_ref_pins.py", corpus)
    binary = tmp_path / "target/debug" / BINARY.name
    binary.parent.mkdir(parents=True)
    shutil.copy2(BINARY, binary)
    document = tmp_path / "tests/fixtures/corpus-sources/webflow-v2/openapi.json"
    document.parent.mkdir(parents=True)
    document.write_text(
        json.dumps(
            {
                "openapi": "3.1.0",
                "info": {"title": "Record", "version": "1"},
                "paths": {},
                "components": {"schemas": {"Thing": {"type": "object", "properties": {"value": True}}}},
            }
        ),
        encoding="utf-8",
    )
    golden = tmp_path / "tests/fixtures/webflow-v2/expected"
    generated = subprocess.run(
        [
            str(binary),
            "generate",
            "--spec",
            str(document),
            "--output",
            str(golden),
            "--package-name",
            "fern",
            "--project-name",
            "default_package_name",
        ],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        timeout=120,
    )
    assert generated.returncode == 0, generated.stderr
    registry = tmp_path / "crates/crozier-e2e/tests/e2e.rs"
    registry.parent.mkdir(parents=True)
    registry.write_text(
        'const DEMO: Corpus = Corpus {\n    api: "webflow-v2",\n'
        '    unmatched: &["src/fern/types/thing.py"],\n};\n'
        "fn demo_matches_fern_output() { assert_committed_corpus_matches(&DEMO); }\n",
        encoding="utf-8",
    )
    record = tmp_path / "docs/openapi-surface/residual-attribution.json"
    record.parent.mkdir(parents=True)
    argv = [sys.executable, str(scripts / SCRIPT.name), "--key", "boolean-schema-true", "--write-record"]
    record.write_text("{broken", encoding="utf-8")
    refused = subprocess.run(argv, cwd=tmp_path, capture_output=True, text=True, timeout=120)
    assert refused.returncode != 0
    assert "residual-attribution.json: cannot read attribution" in refused.stderr
    assert "just residual-attribution" in refused.stderr
    assert "Traceback" not in refused.stderr
    assert record.read_text(encoding="utf-8") == "{broken"
    kept = {
        "key": "unselected",
        "fixture": "other",
        "byte_matched": [],
        "unmatched": [],
        "golden_digest": "0" * 64,
        "inputs_digest": "0" * 64,
    }
    record.write_text(json.dumps({"version": 1, "rows": [kept]}), encoding="utf-8")
    run = subprocess.run(argv, cwd=tmp_path, capture_output=True, text=True, timeout=120)
    assert run.returncode == 0, run.stderr
    published = json.loads(record.read_text(encoding="utf-8"))
    assert published["version"] == 1
    assert next(row for row in published["rows"] if row["key"] == "unselected") == kept
    measured = json.loads(run.stdout)
    selected = next(row for row in published["rows"] if row["key"] == "boolean-schema-true")
    assert {name: selected[name] for name in measured} == measured
    assert selected["unmatched"] == ["src/fern/types/thing.py"]
    assert len(selected["golden_digest"]) == len(selected["inputs_digest"]) == 64


if __name__ == "__main__":
    unittest.main()
