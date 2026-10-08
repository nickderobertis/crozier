#!/usr/bin/env python3
"""`tests/corpus_match/match.sh` takes `--strict` or nothing: any other argument
list is refused with its usage and status 2 before it builds or runs anything.

Run: `just test-corpus-offline` (the `corpus-match` project's `test-offline`).
"""
from __future__ import annotations

import os
import subprocess
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]


@unittest.skipIf(os.name == "nt", "match.sh runs on the Linux legs only")
class MatchUsage(unittest.TestCase):
    def test_an_argument_list_it_does_not_take_is_refused_before_building(self) -> None:
        for args, named in ((["--sideways"], "unknown argument '--sideways'"),
                            (["--strict", "extra"], "takes at most one argument, got 2"),
                            (["", "--strict"], "takes at most one argument, got 2")):
            with self.subTest(args=args):
                # No cargo on PATH: a run that got past the usage check would fail differently.
                result = subprocess.run(["bash", str(REPO / "tests" / "corpus_match" / "match.sh"), *args],
                                        capture_output=True, text=True, env={"PATH": "/usr/bin:/bin"})
                self.assertEqual(2, result.returncode, result.stderr)
                self.assertEqual(f"corpus-match: {named} — usage: tests/corpus_match/match.sh [--strict]\n",
                                 result.stderr)

    def test_a_build_that_fails_is_named_after_cargos_own_error(self) -> None:
        with tempfile.TemporaryDirectory() as scratch:
            # The real cargo, told to build into a path that is a regular file.
            blocker = Path(scratch) / "not-a-directory"
            blocker.write_text("", encoding="utf-8")
            result = subprocess.run(["bash", str(REPO / "tests" / "corpus_match" / "match.sh")],
                                    capture_output=True, text=True, timeout=600,
                                    env={**os.environ, "CARGO_TARGET_DIR": str(blocker)})
        self.assertEqual(101, result.returncode, result.stderr)
        self.assertIn("corpus-match: `cargo build --locked --quiet -p crozier --bin crozier` exited 101", result.stderr)
        self.assertIn("then re-run", result.stderr)


if __name__ == "__main__":
    unittest.main()
