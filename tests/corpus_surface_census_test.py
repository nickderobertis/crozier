#!/usr/bin/env python3
"""Network-tier census journeys over the fetched registered corpus."""

from __future__ import annotations

import importlib.util
import itertools
import subprocess
import sys
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "openapi-surface-census.py"
CENSUS_TIMEOUT = 60


def load_census():
    """Load the authoritative source registry from the production census."""
    spec = importlib.util.spec_from_file_location("openapi_surface_census_corpus", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


census = load_census()


class RegisteredCorpusCensusTests(unittest.TestCase):
    def test_case_11_is_absent_from_the_registered_corpus(self) -> None:
        """The recorded gap is measured over every registered source, end to end."""
        selector = (
            "schema.oneOf>!schema.$ref&!schema.additionalProperties&!schema.allOf&"
            "!schema.example:schema-shaped&!schema.properties:non-empty&"
            "schema.example=object&schema.type:primary=object"
        )
        sources = census.registered_sources(
            REPO / "tests" / "fixtures", REPO / ".local" / "corpus", False
        )
        self.assertEqual(169, len(sources))
        declared: list[str] = []
        for offset in range(0, len(sources), 30):
            fixture_args = list(
                itertools.chain.from_iterable(
                    ("--fixture", source.fixture)
                    for source in sources[offset : offset + 30]
                )
            )
            completed = subprocess.run(
                [sys.executable, str(SCRIPT), "--selector", selector, *fixture_args],
                cwd=REPO,
                capture_output=True,
                text=True,
                timeout=CENSUS_TIMEOUT,
            )
            self.assertEqual(0, completed.returncode, completed.stderr)
            for line in completed.stdout.splitlines():
                _reported_selector, separator, remainder = line.partition("  ")
                if separator and not remainder.strip().startswith("("):
                    declared.append(line)
        self.assertEqual([], declared)


if __name__ == "__main__":
    unittest.main()
