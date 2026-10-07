#!/usr/bin/env python3
"""`tools/surface-census/golden-reach.py` against the real `llvm-profdata`.

The reach measurement merges raw profiles with the toolchain's own
`llvm-profdata`; a profile it cannot read must stop the run with the tool's
stderr and the command that rebuilds the profile, never a traceback. This drives
the real tool from the active Rust toolchain over a file that is not a profile.
The rest of golden-reach's boundary cases need no host tool and are
`tools/surface-census/tests/golden_reach_test.py`.
"""

from __future__ import annotations

import importlib.util
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
                golden_reach.run_llvm(
                    [profdata, "merge", "-sparse", str(raw), "-o", str(Path(scratch) / "m.profdata")]
                )
        message = str(refused.exception)
        self.assertIn("`llvm-profdata merge` exited", message)
        self.assertIn("stale.profraw", message)
        self.assertIn("just golden-reach", message)


if __name__ == "__main__":
    unittest.main()
