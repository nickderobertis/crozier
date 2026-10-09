#!/usr/bin/env python3
"""`tests/census_fallback/run.sh` with the real uv: a parser pin uv cannot
install stops the stage, naming the suite, the pin and what to check. Kept
apart from `run_test.py`, whose cases use a stand-in uv and need no host tool."""

from __future__ import annotations

import os
import shutil
import subprocess
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
RUNNER = REPO / "tests" / "census_fallback" / "run.sh"


@unittest.skipIf(os.name == "nt", "run.sh runs on the Linux legs only")
class ThePinMustInstall(unittest.TestCase):
    @unittest.skipUnless(shutil.which("uv"), "uv installs the fallback suites' parser pin")
    def test_a_pin_uv_cannot_install_names_the_suite_and_the_pin(self) -> None:
        # The real uv with no network and no cache: the install the stage owes fails.
        pin = subprocess.run(
            ["bash", str(RUNNER), "pin", "tools/surface-census/golden-reach-search.py"],
            cwd=REPO,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
        result = subprocess.run(
            ["bash", str(RUNNER), "parsers"],
            cwd=REPO,
            capture_output=True,
            text=True,
            env={**os.environ, "UV_OFFLINE": "1", "UV_NO_CACHE": "1"},
            timeout=300,
        )
        self.assertNotEqual(0, result.returncode, result.stderr)
        self.assertIn(
            f"census-fallback: python3 tools/surface-census/tests/golden_reach_test.py exited "
            f"{result.returncode} under {pin}",
            result.stderr,
        )
        self.assertIn("check that PyPI is reachable", result.stderr)


if __name__ == "__main__":
    unittest.main()
