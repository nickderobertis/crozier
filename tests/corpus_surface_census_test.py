#!/usr/bin/env python3
"""Network-tier census journeys over the fetched registered corpus."""

from __future__ import annotations

import csv
import hashlib
import importlib.util
import itertools
import re
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
        self.assertEqual(193, len(sources))
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

    def test_byte_identical_dispositions_are_the_registered_source_bytes(self) -> None:
        """A candidate settled as a copy of a corpus row carries that row's bytes.

        The witness-search ledgers dispose a screened copy of a registered source
        as `byte-identical to CORPUS row N, sha256 X`. X must be the candidate's
        own recorded digest and the sha256 of row N's fetched source document, so
        the claim is re-measured rather than trusted.
        """
        disposition = re.compile(r"byte-identical to CORPUS row (\d+), sha256 ([0-9a-f]{64})")
        rows: dict[int, tuple[str, str]] = {}
        for line in (REPO / "tests" / "fixtures" / "CORPUS.md").read_text(encoding="utf-8").splitlines():
            match = re.match(r"^\| (\d+) \| `([^`]+)` \| [^|]+ \| (\S+) \|", line)
            if match:
                rows.setdefault(int(match.group(1)), (match.group(2), match.group(3)))
        sources = {
            source.fixture: source
            for source in census.registered_sources(
                REPO / "tests" / "fixtures", REPO / ".local" / "corpus", False
            )
        }
        copies = 0
        for ledger in ("witness-search-registries", "witness-search-github"):
            path = REPO / "docs" / "openapi-surface" / ledger / "candidates.tsv"
            with path.open(encoding="utf-8", newline="") as stream:
                for candidate in csv.DictReader(stream, delimiter="\t"):
                    match = disposition.fullmatch(candidate["disposition"])
                    if not match:
                        continue
                    copies += 1
                    number, digest = int(match.group(1)), match.group(2)
                    with self.subTest(candidate=candidate["candidate"], key=candidate["key"]):
                        self.assertIn(number, rows, "names no CORPUS row")
                        name, url = rows[number]
                        self.assertNotEqual(url, candidate["candidate"], "is the row's own source")
                        self.assertEqual(candidate["digest"], digest)
                        source = sources[name]
                        self.assertIsNotNone(source.path, f"{name} is unfetched; run scripts/fetch-corpus.sh")
                        self.assertEqual(
                            digest, hashlib.sha256(source.path.read_bytes()).hexdigest()
                        )
        self.assertGreater(copies, 0)


if __name__ == "__main__":
    unittest.main()
