#!/usr/bin/env python3
"""`tests/corpus_match/match.sh` runs its inventory as one nextest pass: what
nextest selects under the recipe's filter is the inventory, name for name, an
inventory nextest would select differently is refused before anything runs, and
a golden that fails fails the recipe by name.

The variants run the script's own text with one inventory swapped in, as
`bash -c TEXT PATH` so `$0` is still the real script and it runs in this checkout.

Run: `just nx run corpus-match:test-selection` (part of the project's `test`).
It builds and runs the real nextest and crozier, so it stays out of `test-offline`.
"""
from __future__ import annotations

import os
import re
import subprocess
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SCRIPT = REPO / "tests" / "corpus_match" / "match.sh"


def inventory(text: str) -> list[str]:
    lines = text.splitlines()
    start = lines.index("inventory=(") + 1
    end = lines.index(")", start)
    return [line.strip() for line in lines[start:end] if line.strip() and not line.strip().startswith("#")]


def with_inventory(text: str, names: list[str]) -> str:
    lines = text.splitlines()
    start = lines.index("inventory=(") + 1
    end = lines.index(")", start)
    return "\n".join(lines[:start] + [f"  {name}" for name in names] + lines[end:]) + "\n"


def run(text: str, **env: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["bash", "-c", text, str(SCRIPT)], capture_output=True, text=True,
                          timeout=1800, env={**os.environ, **env})


@unittest.skipIf(os.name == "nt", "match.sh runs on the Linux legs only")
class MatchSelection(unittest.TestCase):
    def setUp(self) -> None:
        self.text = SCRIPT.read_text(encoding="utf-8")
        self.listed = inventory(self.text)

    def test_nextest_selects_exactly_the_listed_inventory(self) -> None:
        # Nx forces colour on, as CI can; the selection must still read as plain names.
        result = subprocess.run(["bash", str(SCRIPT)], capture_output=True, text=True, timeout=1800,
                                env={**os.environ, "CORPUS_MATCH_LIST": "1", "FORCE_COLOR": "1",
                                     "CLICOLOR_FORCE": "1", "CARGO_TERM_COLOR": "always"})
        self.assertEqual(0, result.returncode, result.stderr)
        selected = result.stdout.splitlines()
        self.assertEqual(len(self.listed), len(set(self.listed)), "the inventory lists a test twice")
        self.assertEqual(sorted(self.listed), sorted(selected))
        # A substring filter would also pick these siblings of listed names up.
        self.assertIn("otoroshi_matches_fern_output", selected)
        self.assertIn("overlay_goldens::overlay_goldens_match_fern_output", selected)

    def test_an_inventory_nextest_selects_differently_is_refused_before_running(self) -> None:
        for names, named in ((self.listed + ["no_such_golden_matches_fern_output"],
                              "< no_such_golden_matches_fern_output"),
                             (self.listed + [self.listed[0]], f"< {self.listed[0]}"),
                             ([name.removeprefix("overlay_goldens::") for name in self.listed],
                              "< overlay_goldens_match_fern_output")):
            with self.subTest(named=named):
                result = run(with_inventory(self.text, names), CORPUS_MATCH_LIST="1")
                self.assertEqual(1, result.returncode, result.stderr)
                self.assertEqual("", result.stdout)
                self.assertIn("corpus-match: nextest's selection differs from the inventory", result.stderr)
                self.assertIn(f"\n{named}\n", result.stderr)
                self.assertIn("then re-run", result.stderr)

    def test_a_failing_golden_fails_the_recipe_naming_it(self) -> None:
        # A client class name Fern's golden was not generated with: the real
        # crozier writes a different SDK, so the byte comparison fails.
        result = run(with_inventory(self.text, ["basic_auth_matches_fern_output", "bracketed_property_names_matches_fern_output"]),
                     CROZIER_CLIENT_CLASS_NAME="NotFernsClient", CARGO_TERM_COLOR="always")
        # Nx forces colour on; the names are asserted on the text a reader sees.
        output = re.sub(r"\x1b\[[0-9;]*m", "", result.stdout + result.stderr)
        self.assertEqual(100, result.returncode, output)
        self.assertRegex(output, r"FAIL \[.*\] \(\s*\d+/2\) crozier-e2e::e2e basic_auth_matches_fern_output")
        self.assertRegex(output, r"FAIL \[.*\] \(\s*\d+/2\) crozier-e2e::e2e bracketed_property_names_matches_fern_output")
        self.assertIn("2 tests run: 0 passed, 2 failed", output)
        self.assertIn("corpus-match: `CROZIER_REQUIRE_CORPUS=1 cargo nextest run", output)
        self.assertNotIn("Ran 2 tests", output, "the surface census ran after a failing golden")


if __name__ == "__main__":
    unittest.main()
