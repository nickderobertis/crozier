#!/usr/bin/env python3
"""`tests/census_fallback/run.sh` refuses to run a fallback suite without the
parser pin it reads from each script's PEP 723 header, rather than handing uv
an empty `--with`. Driven as the targets drive it, over a scratch root whose
scripts carry no pin (or two), so nothing is installed and no suite runs."""

from __future__ import annotations

import shutil
import subprocess
import os
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
RUNNER = REPO / "tests" / "census_fallback" / "run.sh"


@unittest.skipIf(os.name == "nt", "run.sh runs on the Linux legs only")
class ThePinIsRequired(unittest.TestCase):
    def run_over(self, header: str, stage: str) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as scratch:
            root = Path(scratch)
            (root / "tests" / "census_fallback").mkdir(parents=True)
            shutil.copy2(RUNNER, root / "tests" / "census_fallback" / "run.sh")
            for script in ("tools/surface-census/golden-reach-search.py",
                           "tools/witness-search/witness-search-recensus.py"):
                (root / script).parent.mkdir(parents=True, exist_ok=True)
                (root / script).write_text(f"# /// script\n{header}# ///\n", encoding="utf-8")
            # A stand-in `uv` that would record any run it was asked for.
            bin_dir = root / "bin"
            bin_dir.mkdir()
            (bin_dir / "uv").write_text("#!/bin/sh\necho ran > \"$(dirname \"$0\")/uv-ran\"\n", encoding="utf-8")
            (bin_dir / "uv").chmod(0o755)
            result = subprocess.run(
                ["bash", str(root / "tests" / "census_fallback" / "run.sh"), stage],
                capture_output=True, text=True, env={"PATH": f"{bin_dir}:/usr/bin:/bin"},
            )
            self.assertFalse((bin_dir / "uv-ran").exists(), f"{stage} ran a suite: {result.stderr}")
            return result

    def test_a_script_without_a_pin_or_with_two_stops_the_stage_naming_it(self) -> None:
        for header in ("", '# dependencies = ["ruamel.yaml==0.19.1"]\n# dependencies = ["ruamel.yaml==0.18"]\n'):
            for stage in ("samples", "parsers"):
                with self.subTest(header=header, stage=stage):
                    result = self.run_over(header, stage)
                    self.assertNotEqual(result.returncode, 0, result.stderr)
                    self.assertIn("tools/surface-census/golden-reach-search.py declares no single pinned dependency",
                                  result.stderr)
                    self.assertIn("then re-run", result.stderr)


if __name__ == "__main__":
    unittest.main()
