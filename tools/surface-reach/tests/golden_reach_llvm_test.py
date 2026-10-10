#!/usr/bin/env python3
"""`tools/surface-census/golden-reach.py` against the real `llvm-profdata` and `ruff`.

The reach measurement merges raw profiles with the toolchain's own
`llvm-profdata`; a profile it cannot read must stop the run with the tool's
stderr and the command that rebuilds the profile, never a traceback. This drives
the real tool from the active Rust toolchain over a file that is not a profile.
It also runs each golden test from the directory cargo does, which the pinned
`ruff` (the one crozier formats with) shows matters under the tooling's own
`[tool.ruff]`. The rest of golden-reach's boundary cases need no host tool and
are `tools/surface-census/tests/golden_reach_test.py`.
"""

from __future__ import annotations

import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
SCRIPT = REPO / "tools" / "surface-census" / "golden-reach.py"

_spec = importlib.util.spec_from_file_location("golden_reach", SCRIPT)
assert _spec and _spec.loader
golden_reach = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(golden_reach)


class RealLlvmToolTests(unittest.TestCase):
    def test_a_profile_llvm_cannot_read_fails_with_its_stderr_and_the_rebuild(self) -> None:
        profdata = golden_reach._llvm_tool("llvm-profdata")
        with tempfile.TemporaryDirectory() as scratch:
            raw = Path(scratch) / "stale.profraw"
            raw.write_bytes(b"not a profile")
            with self.assertRaises(SystemExit) as refused:
                golden_reach.run_llvm([profdata, "merge", "-sparse", str(raw), "-o", str(Path(scratch) / "m.profdata")])
        message = str(refused.exception)
        # On Windows the real tool is `llvm-profdata.exe`, so this also proves
        # the message names it without the suffix.
        self.assertIn("`llvm-profdata merge` exited", message)
        self.assertIn("stale.profraw", message)
        self.assertIn("just golden-reach", message)


class RealRuffTests(unittest.TestCase):
    def test_golden_tests_run_where_the_tooling_ruff_config_does_not_reach_generated_output(self) -> None:
        """A golden runs from the e2e crate's directory, as cargo runs it, not the root.

        crozier's `ruff format --stdin-filename` resolves configuration from its
        working directory; from the root the tooling's `[tool.ruff]` excludes a
        generated `templates/` package, which then comes back unformatted.
        """
        cwd = golden_reach.golden_test_cwd(REPO)
        self.assertEqual(REPO / "crates" / "crozier-e2e", cwd)
        self.assertTrue((cwd / "Cargo.toml").is_file())
        line = "x = {" + ", ".join(f'"key_{n:02}": {n}' for n in range(12)) + "}\n"
        self.assertGreater(len(line), 120)

        def ruff_format(directory: Path) -> str:
            return subprocess.run(
                ["ruff", "format", "--line-length", "120", "--stdin-filename", "src/acme/templates/__init__.py", "-"],
                cwd=directory,
                input=line,
                capture_output=True,
                text=True,
                encoding="utf-8",
                check=True,
            ).stdout

        self.assertEqual(line, ruff_format(REPO))
        self.assertTrue(ruff_format(cwd).startswith("x = {\n"))


if __name__ == "__main__":
    unittest.main()
