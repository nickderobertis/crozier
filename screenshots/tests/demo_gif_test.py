#!/usr/bin/env python3
"""`demo-gif.py` refuses a `crozier generate` that failed or said nothing.

The GIF replays the real summary line crozier prints, so a binary that exits
non-zero, or prints nothing, must stop the render with the fix rather than a
traceback or a GIF of an error. Each case runs the real script against a stub
binary standing in for a broken build. Needs Pillow (the script's renderer):
run it as the `screenshots` project's `test` target, which installs it with uv.
"""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SCRIPT = REPO / "screenshots" / "demo-gif.py"


@unittest.skipIf(os.name == "nt", "the stub binary is a POSIX shell script")
class AFailedGenerateStopsTheRender(unittest.TestCase):
    def render_with(self, stub_body: str) -> tuple[subprocess.CompletedProcess[str], Path]:
        scratch = tempfile.TemporaryDirectory()
        self.addCleanup(scratch.cleanup)
        root = Path(scratch.name)
        stub = root / "crozier"
        stub.write_text("#!/bin/sh\n" + textwrap.dedent(stub_body), encoding="utf-8")
        stub.chmod(0o755)
        out = root / "demo.gif"
        run = subprocess.run(
            [sys.executable, str(SCRIPT)],
            env={**os.environ, "CROZIER_BIN": str(stub), "DEMO_GIF_OUT": str(out)},
            capture_output=True, text=True, timeout=120,
        )
        return run, out

    def test_a_generate_that_exits_non_zero_names_the_exit_and_the_rebuild(self) -> None:
        run, out = self.render_with('echo "error: could not read spec" >&2\nexit 3\n')
        self.assertEqual(1, run.returncode, run.stdout + run.stderr)
        self.assertIn("generate` exited 3: error: could not read spec", run.stderr)
        self.assertIn("cargo build --release --locked --bin crozier", run.stderr)
        self.assertNotIn("Traceback", run.stderr)
        self.assertFalse(out.exists())

    def test_a_generate_that_prints_nothing_is_refused_rather_than_indexed(self) -> None:
        run, out = self.render_with("exit 0\n")
        self.assertEqual(1, run.returncode, run.stdout + run.stderr)
        self.assertIn("generate` exited 0 and printed nothing", run.stderr)
        self.assertNotIn("Traceback", run.stderr)
        self.assertFalse(out.exists())


if __name__ == "__main__":
    unittest.main()
