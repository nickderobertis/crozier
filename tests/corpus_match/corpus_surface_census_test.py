#!/usr/bin/env python3
"""Network-tier census journeys over the fetched registered corpus."""

from __future__ import annotations

import csv
import hashlib
import importlib.util
import io
import itertools
import os
import re
import subprocess
import sys
import unittest
from pathlib import Path

# Every child these tests start has its output decoded as UTF-8, so a Python
# child writes UTF-8 too, whatever the platform locale (cp1252 on Windows).
os.environ["PYTHONUTF8"] = "1"

REPO = Path(__file__).resolve().parents[2]
SCRIPT = REPO / "tools" / "surface-census" / "openapi-surface-census.py"
_INDEX_SPEC = importlib.util.spec_from_file_location(
    "witness_search_github_index_corpus", REPO / "tools" / "witness-search" / "witness-search-github-index.py"
)
assert _INDEX_SPEC and _INDEX_SPEC.loader
INDEX = importlib.util.module_from_spec(_INDEX_SPEC)
_INDEX_SPEC.loader.exec_module(INDEX)
_HANDWRITTEN_SPEC = importlib.util.spec_from_file_location(
    "handwritten_fixtures_corpus", REPO / "tools" / "surface-census" / "handwritten-fixtures.py"
)
assert _HANDWRITTEN_SPEC and _HANDWRITTEN_SPEC.loader
HANDWRITTEN = importlib.util.module_from_spec(_HANDWRITTEN_SPEC)
sys.modules[_HANDWRITTEN_SPEC.name] = HANDWRITTEN
_HANDWRITTEN_SPEC.loader.exec_module(HANDWRITTEN)
CENSUS_TIMEOUT = 60
CASE_11_KEY = "oneof-bare-object-example-variant"


def load_census():
    """Load the authoritative source registry from the production census."""
    spec = importlib.util.spec_from_file_location("openapi_surface_census_corpus", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


census = load_census()


class RegisteredCorpusCensusTests(unittest.TestCase):
    def test_case_11_declarers_are_whole_byte_matches_their_removal_leaves_unmoved(self) -> None:
        """Every registered declarer of the shape is measured, end to end, and none proves the row.

        Two Ironclad documents declare it. `oneof-bare-object-example-variant` stays
        `handwritten` only while each declarer's committed paired removal moves no file in
        either generator; a declarer without that record may be a real witness, so it fails here.
        """
        selector = (
            "schema.oneOf>!schema.$ref&!schema.additionalProperties&!schema.allOf&"
            "!schema.example:schema-shaped&!schema.properties:non-empty&"
            "schema.example=object&schema.type:primary=object"
        )
        fixtures = REPO / "tests" / "fixtures"
        sources = census.registered_sources(fixtures, fixtures / "corpus-sources", False)
        # "Every registered source" is every committed golden tree, whatever the
        # corpus has grown to: a tree the census drops would pass the search below
        # unmeasured, so this names the fixture rather than pinning a count.
        aliases = census.corpus_aliases(fixtures)
        self.assertEqual(
            sorted(path.parent.name for path in fixtures.glob("*/expected") if path.is_dir()),
            sorted(aliases.get(source.fixture, source.fixture) for source in sources),
        )
        self.assertTrue(sources)
        declared: set[str] = set()
        for offset in range(0, len(sources), 30):
            fixture_args = list(
                itertools.chain.from_iterable(("--fixture", source.fixture) for source in sources[offset : offset + 30])
            )
            completed = subprocess.run(
                [sys.executable, str(SCRIPT), "--selector", selector, *fixture_args],
                cwd=REPO,
                capture_output=True,
                text=True,
                timeout=CENSUS_TIMEOUT,
                encoding="utf-8",
            )
            self.assertEqual(0, completed.returncode, completed.stderr)
            for line in completed.stdout.splitlines():
                _reported_selector, separator, remainder = line.partition("  ")
                if separator and not remainder.strip().startswith("("):
                    declared.add(remainder.split()[0])
        measured, failures = HANDWRITTEN.output_insensitive_declarers(REPO)
        self.assertEqual([], failures)
        self.assertEqual(sorted(measured.get(CASE_11_KEY, ())), sorted(declared))
        registrations = census.golden_registrations(REPO / census.GOLDEN_REGISTRY)
        for fixture in declared:
            with self.subTest(fixture=fixture):
                self.assertEqual([], list(registrations[fixture].unmatched))
                self.assertTrue((fixtures / fixture / "expected").is_dir())
                self.assertTrue((fixtures / fixture / "expected-literals").is_dir())

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
            for source in census.acquisition_sources(
                REPO / "tests" / "fixtures", REPO / "tests" / "fixtures" / "corpus-sources", False
            )
        }
        copies = 0
        for ledger in ("witness-search-registries", "witness-search-github"):
            path = REPO / "docs" / "openapi-surface" / ledger / "candidates.tsv"
            with io.StringIO(INDEX.read_ledger(path), newline="") as stream:
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
                        self.assertIsNotNone(source.path, f"{name} is unfetched; run tools/corpus/fetch-corpus.sh")
                        self.assertEqual(digest, hashlib.sha256(source.path.read_bytes()).hexdigest())
        self.assertGreater(copies, 0)


if __name__ == "__main__":
    unittest.main()
