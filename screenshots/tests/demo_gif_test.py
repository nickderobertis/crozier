#!/usr/bin/env python3
"""`demo-gif.py` renders the session the real crozier produces, and refuses a
`crozier generate` that failed or said nothing.

The GIF replays the real summary line crozier prints, so a binary that exits
non-zero, or prints nothing, must stop the render with the fix rather than a
traceback or a GIF of an error; those cases run the real script against a stub
binary standing in for a broken build. The render itself is driven with the
freshly built crozier (`crozier:build` runs first). Needs Pillow (the script's
renderer): run it as the `screenshots` project's `test` target, which installs
it with uv.
"""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

SCREENSHOTS = Path(__file__).resolve().parent.parent
REPO = SCREENSHOTS.parent
SCRIPT = SCREENSHOTS / "demo-gif.py"


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

    def test_a_binary_that_cannot_be_launched_is_refused_with_the_fix(self) -> None:
        scratch = tempfile.TemporaryDirectory()
        self.addCleanup(scratch.cleanup)
        out = Path(scratch.name) / "demo.gif"
        run = subprocess.run(
            [sys.executable, str(SCRIPT)],
            env={**os.environ, "CROZIER_BIN": scratch.name, "DEMO_GIF_OUT": str(out)},
            capture_output=True, text=True, timeout=120,
        )
        self.assertEqual(1, run.returncode, run.stdout + run.stderr)
        self.assertIn(f"demo-gif: cannot run {scratch.name}", run.stderr)
        self.assertIn("point CROZIER_BIN at the crozier binary", run.stderr)
        self.assertNotIn("Traceback", run.stderr)

    def test_a_generate_that_prints_nothing_is_refused_rather_than_indexed(self) -> None:
        run, out = self.render_with("exit 0\n")
        self.assertEqual(1, run.returncode, run.stdout + run.stderr)
        self.assertIn("generate` exited 0 and printed nothing", run.stderr)
        self.assertNotIn("Traceback", run.stderr)
        self.assertFalse(out.exists())


class TheRealBinaryRendersTheSession(unittest.TestCase):
    def test_a_successful_generate_renders_an_animated_gif(self) -> None:
        from PIL import Image

        binary = REPO / "target" / "debug" / ("crozier.exe" if os.name == "nt" else "crozier")
        self.assertTrue(binary.is_file(), f"no {binary}; run `just nx run crozier:build`")
        with tempfile.TemporaryDirectory() as scratch:
            out = Path(scratch) / "demo.gif"
            run = subprocess.run(
                [sys.executable, str(SCRIPT)],
                env={**os.environ, "CROZIER_BIN": str(binary), "DEMO_GIF_OUT": str(out)},
                capture_output=True, text=True, timeout=300,
            )
            self.assertEqual(0, run.returncode, run.stderr)
            frames = int(run.stderr.rsplit("(", 1)[1].split(" frames)")[0])
            self.assertGreater(frames, 10, run.stderr)
            with Image.open(out) as gif:
                self.assertEqual("GIF", gif.format)
                self.assertTrue(gif.is_animated)
                # The encoder folds identical consecutive frames into one.
                self.assertLessEqual(gif.n_frames, frames)
                self.assertGreater(gif.n_frames, 10)
                self.assertGreater(gif.size[0] * gif.size[1], 0)


if __name__ == "__main__":
    unittest.main()
