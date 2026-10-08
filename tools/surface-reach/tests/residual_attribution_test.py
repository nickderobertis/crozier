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


class AMissingWitnessSource(unittest.TestCase):
    def test_a_case_whose_witness_has_no_committed_source_names_the_fix(self) -> None:
        """The script's own refusal, before it builds anything over a source that is not there."""
        spec = importlib.util.spec_from_file_location("residual_attribution_missing", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        module.CROZIER = Path(sys.executable)
        module.CASES = {"some-row": ("no-such-witness", lambda document: 1)}
        if shutil.which("ruff") is None:
            self.fail("no ruff on PATH; install it with `just bootstrap`")
        with self.assertRaises(SystemExit) as refused, contextlib.redirect_stdout(io.StringIO()):
            module.main()
        self.assertIn("some-row's witness no-such-witness has no committed source", str(refused.exception))
        self.assertIn("`just lint-corpus-sources` names what is missing", str(refused.exception))


if __name__ == "__main__":
    unittest.main()
