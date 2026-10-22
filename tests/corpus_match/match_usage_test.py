#!/usr/bin/env python3
"""`tests/corpus_match/match.sh` takes `--strict` or nothing: any other argument
list is refused with its usage and status 2 before it builds or runs anything.

Run: `just test-corpus-offline` (the `corpus-match` project's `test-offline`).
"""

from __future__ import annotations

import json
import os
import shlex
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]


@unittest.skipIf(os.name == "nt", "match.sh runs on the Linux legs only")
class MatchUsage(unittest.TestCase):
    def test_an_argument_list_it_does_not_take_is_refused_before_building(self) -> None:
        for args, named in (
            (["--sideways"], "unknown argument '--sideways'"),
            (["--strict", "extra"], "takes at most one argument, got 2"),
            (["", "--strict"], "takes at most one argument, got 2"),
        ):
            with self.subTest(args=args):
                # No cargo on PATH: a run that got past the usage check would fail differently.
                result = subprocess.run(
                    ["bash", str(REPO / "tests" / "corpus_match" / "match.sh"), *args],
                    capture_output=True,
                    text=True,
                    env={"PATH": "/usr/bin:/bin"},
                )
                self.assertEqual(2, result.returncode, result.stderr)
                self.assertEqual(
                    f"corpus-match: {named} — usage: tests/corpus_match/match.sh [--strict]\n", result.stderr
                )

    def test_strict_preflight_consumes_stdout_and_keeps_both_failures_strict(self) -> None:
        real_cargo = shutil.which("cargo")
        self.assertIsNotNone(real_cargo)
        with tempfile.TemporaryDirectory() as directory:
            scratch = Path(directory)
            tools = scratch / "tools"
            tools.mkdir()
            producer = scratch / "cargo_producer.py"
            producer.write_text(
                "import json, os, signal, sys\n"
                "from pathlib import Path\n"
                "args = sys.argv[1:]\n"
                "with Path(os.environ['MATCH_TEST_CALLS']).open('a') as calls:\n"
                "    calls.write(json.dumps(args) + '\\n')\n"
                "if args == ['run', '--locked', '--quiet', '--', 'config', 'python']:\n"
                "    signal.signal(signal.SIGPIPE, signal.SIG_DFL)\n"
                "    value = os.environ['MATCH_TEST_STRICT_VALUE']\n"
                "    os.write(1, f'  fern-strict {value} (env)\\n'.encode())\n"
                "    os.write(1, b'  remaining-config ' + b'x' * (4 * 1024 * 1024) + b'\\n')\n"
                "    Path(os.environ['MATCH_TEST_PRODUCER_DONE']).write_text('complete')\n"
                "    sys.exit(int(os.environ['MATCH_TEST_PRODUCER_EXIT']))\n"
                "real = os.environ['MATCH_TEST_REAL_CARGO']\n"
                "os.execv(real, [real, *args])\n",
                encoding="utf-8",
            )
            cargo = tools / "cargo"
            cargo.write_text(
                f'#!/bin/sh\nexec {shlex.quote(sys.executable)} {shlex.quote(str(producer))} "$@"\n',
                encoding="utf-8",
            )
            cargo.chmod(0o755)
            calls = scratch / "calls.jsonl"
            inventory = scratch / "inventory.txt"
            producer_done = scratch / "producer-done.txt"
            env = {
                **os.environ,
                "PATH": str(tools) + os.pathsep + os.environ["PATH"],
                "MATCH_TEST_CALLS": str(calls),
                "MATCH_TEST_REAL_CARGO": str(real_cargo),
                "MATCH_TEST_PRODUCER_DONE": str(producer_done),
                "CORPUS_MATCH_LIST": str(inventory),
            }
            # The stdout producer is a subprocess double. Later build/list calls
            # use real cargo, and inventory mode never runs a generated SDK.
            for value, producer_exit, success in [
                ("true", 0, True),
                ("false", 0, False),
                ("true", 23, False),
                ("true", 0, True),
            ]:
                with self.subTest(value=value, producer_exit=producer_exit, success=success):
                    calls.write_text("", encoding="utf-8")
                    inventory.unlink(missing_ok=True)
                    producer_done.unlink(missing_ok=True)
                    result = subprocess.run(
                        ["bash", str(REPO / "tests/corpus_match/match.sh"), "--strict"],
                        capture_output=True,
                        text=True,
                        timeout=600,
                        env={**env, "MATCH_TEST_STRICT_VALUE": value, "MATCH_TEST_PRODUCER_EXIT": str(producer_exit)},
                    )
                    seen = [json.loads(line) for line in calls.read_text(encoding="utf-8").splitlines()]
                    self.assertTrue(producer_done.exists(), "the config producer was cut off before draining stdout")
                    if success:
                        self.assertEqual(0, result.returncode, result.stderr)
                        self.assertIn(
                            "crozier_sdk_extensions_matches_fern_output", inventory.read_text(encoding="utf-8")
                        )
                        self.assertTrue(any(args[0] == "build" for args in seen))
                    else:
                        self.assertEqual(1, result.returncode, result.stderr)
                        self.assertIn("did not report fern-strict true", result.stderr)
                        self.assertEqual(1, len(seen), seen)
                        self.assertFalse(inventory.exists())

    def test_a_build_that_fails_is_named_after_cargos_own_error(self) -> None:
        with tempfile.TemporaryDirectory() as scratch:
            # The real cargo, told to build into a path that is a regular file.
            blocker = Path(scratch) / "not-a-directory"
            blocker.write_text("", encoding="utf-8")
            result = subprocess.run(
                ["bash", str(REPO / "tests" / "corpus_match" / "match.sh")],
                capture_output=True,
                text=True,
                timeout=600,
                env={**os.environ, "CARGO_TARGET_DIR": str(blocker)},
            )
        self.assertEqual(101, result.returncode, result.stderr)
        self.assertIn("corpus-match: `cargo build --locked --quiet -p crozier --bin crozier` exited 101", result.stderr)
        self.assertIn("then re-run", result.stderr)


if __name__ == "__main__":
    unittest.main()
