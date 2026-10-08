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
    SEARCH = "tools/surface-census/golden-reach-search.py"
    RECENSUS = "tools/witness-search/witness-search-recensus.py"
    PIN = '# dependencies = ["ruamel.yaml==0.19.1"]\n'

    def run_over(self, header: str, stage: str, **headers: str | None) -> subprocess.CompletedProcess[str]:
        """`run.sh stage` over scripts whose headers carry `header`, or the
        `headers` entry its key (`search`, `recensus`) names; `None` there leaves
        the script unreadable."""
        with tempfile.TemporaryDirectory() as scratch:
            root = Path(scratch)
            (root / "tests" / "census_fallback").mkdir(parents=True)
            shutil.copy2(RUNNER, root / "tests" / "census_fallback" / "run.sh")
            for name, script in (("search", self.SEARCH), ("recensus", self.RECENSUS)):
                (root / script).parent.mkdir(parents=True, exist_ok=True)
                (root / script).write_text(f"# /// script\n{headers.get(name, header) or ''}# ///\n", encoding="utf-8")
                if name in headers and headers[name] is None:
                    (root / script).chmod(0)
            # A stand-in `uv` that would record any run it was asked for.
            bin_dir = root / "bin"
            bin_dir.mkdir()
            (bin_dir / "uv").write_text('#!/bin/sh\necho ran > "$(dirname "$0")/uv-ran"\n', encoding="utf-8")
            (bin_dir / "uv").chmod(0o755)
            result = subprocess.run(
                ["bash", str(root / "tests" / "census_fallback" / "run.sh"), stage],
                capture_output=True,
                text=True,
                env={"PATH": f"{bin_dir}:/usr/bin:/bin"},
            )
            self.assertFalse((bin_dir / "uv-ran").exists(), f"{stage} ran a suite: {result.stderr}")
            return result

    def test_a_script_without_one_exact_pin_stops_the_stage_naming_it(self) -> None:
        for header in (
            "",
            '# dependencies = ["ruamel.yaml==0.19.1"]\n# dependencies = ["ruamel.yaml==0.18"]\n',
            '# dependencies = ["ruamel.yaml"]\n',
            '# dependencies = ["ruamel.yaml>=0.18"]\n',
            '# dependencies = ["ruamel.yaml==0.19.1", "pyyaml==6.0"]\n',
        ):
            for stage in ("samples", "parsers"):
                with self.subTest(header=header, stage=stage):
                    result = self.run_over(header, stage)
                    self.assertNotEqual(result.returncode, 0, result.stderr)
                    self.assertIn(
                        "tools/surface-census/golden-reach-search.py declares no single pinned dependency",
                        result.stderr,
                    )
                    self.assertIn("then re-run", result.stderr)

    def test_a_pin_outside_the_pep_723_block_is_no_pin(self) -> None:
        # The search script's header declares none; a later comment that looks like one does not count.
        result = self.run_over(
            "",
            "parsers",
            search='# requires-python = ">=3.11"\n# ///\n# dependencies = ["ruamel.yaml==0.19.1"]\n# /// script\n',
        )
        self.assertNotEqual(result.returncode, 0, result.stderr)
        self.assertIn(f"{self.SEARCH} declares no single pinned dependency", result.stderr)

    def test_the_recensus_pin_is_held_after_the_search_pin_is_taken(self) -> None:
        result = self.run_over(self.PIN, "parsers", recensus='# dependencies = ["ruamel.yaml"]\n')
        self.assertNotEqual(result.returncode, 0, result.stderr)
        self.assertIn(f"{self.RECENSUS} declares no single pinned dependency", result.stderr)
        self.assertNotIn(self.SEARCH, result.stderr)

    @unittest.skipIf(hasattr(os, "geteuid") and os.geteuid() == 0, "root reads a file whatever its mode")
    def test_a_script_it_cannot_read_is_named_not_mistaken_for_an_unpinned_one(self) -> None:
        result = self.run_over(self.PIN, "parsers", recensus=None)
        self.assertNotEqual(result.returncode, 0, result.stderr)
        self.assertIn(f"census-fallback: cannot read {self.RECENSUS}", result.stderr)
        self.assertNotIn("declares no single pinned dependency", result.stderr)

    def test_an_invocation_it_cannot_read_exits_two_with_the_usage(self) -> None:
        for args, named in (
            (["pin"], "pin takes exactly one SCRIPT, got 0"),
            (["pin", "a.py", "b.py"], "pin takes exactly one SCRIPT, got 2"),
            (["sideways"], "unknown subcommand 'sideways'"),
            ([], "no subcommand given"),
            (["samples", "extra"], "samples takes no arguments, got: extra"),
            (["parsers", "--all"], "parsers takes no arguments, got: --all"),
        ):
            with self.subTest(args=args):
                result = subprocess.run(["bash", str(RUNNER), *args], cwd=REPO, capture_output=True, text=True)
                self.assertEqual(2, result.returncode, result.stderr)
                self.assertIn(f"census-fallback: {named} — usage: tests/census_fallback/run.sh", result.stderr)

    def test_pin_prints_the_one_exact_pin_the_stages_install(self) -> None:
        printed = subprocess.run(
            ["bash", str(RUNNER), "pin", "tools/surface-census/golden-reach-search.py"],
            cwd=REPO,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, printed.returncode, printed.stderr)
        self.assertRegex(printed.stdout, r"^ruamel\.yaml==\d[\w.]*\n$")


if __name__ == "__main__":
    unittest.main()
