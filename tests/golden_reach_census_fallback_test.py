#!/usr/bin/env python3
# llmlint: ignore-file[new_code_lands_in_a_project] crozier has no Nx workspace; this test sits in tests/ beside golden_reach_test.py and runs under `just test-census-fallback`, which CI's live-e2e leg runs.
"""The arm search's YAML fallback counts what the census's own loader would.

`scripts/golden-reach-search.py recensus` counts a document the census's stdlib
YAML loader refuses through ruamel.yaml, the full YAML 1.2 parser the search
pins. That reading is only as good as its agreement with the loader it stands
in for, so this suite holds it to two things over a committed sample:

* on every registered-corpus YAML source the stdlib loader reads, the census's
  object-model walk counts exactly the same selectors over both readings;
* on one real document of each form only ruamel.yaml reads —
  `tests/data/census-fallback-sample.tsv`, pinned by commit and digest — the
  stdlib loader refuses it and the fallback reading counts the declarations the
  document visibly makes.

It needs the pinned parser and, for a sample document not yet cached, the
network: run it as `just test-census-fallback`, which CI's `live-e2e` leg does.
The registered-corpus census and `just check` never use the fallback.
"""

from __future__ import annotations

import csv
import hashlib
import importlib.util
import os
import sys
import unittest
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SAMPLE = REPO / "tests" / "data" / "census-fallback-sample.tsv"
CACHE = REPO / ".local" / "census-fallback-sample"


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


search = _load("golden_reach_search", REPO / "scripts" / "golden-reach-search.py")


def registered_yaml_sources() -> list[Path]:
    """Every registered source written in YAML: the vendored half, and the fetched `link-ok` half."""
    vendored = sorted(REPO.glob("tests/fixtures/*/openapi.y*ml"))
    fetched = sorted((REPO / ".local" / "corpus").glob("*/openapi.y*ml"))
    return vendored + fetched


def sample_document(url: str, sha256: str) -> Path:
    """A sample document's bytes at its pinned digest, fetched once into `.local/`."""
    suffix = Path(url).suffix
    path = CACHE / f"{sha256}{suffix}"
    if not path.is_file():
        with urllib.request.urlopen(url, timeout=60) as response:  # noqa: S310 - a pinned https raw URL
            data = response.read()
        if hashlib.sha256(data).hexdigest() != sha256:
            raise AssertionError(f"{url} is not the pinned {sha256}")
        CACHE.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    return path


class FallbackAgreementTests(unittest.TestCase):
    def test_both_loaders_count_the_same_selectors_wherever_both_read(self) -> None:
        sources = registered_yaml_sources()
        self.assertTrue(sources, "no registered YAML source to compare the loaders on")
        if os.environ.get("CROZIER_REQUIRE_CORPUS") and not (REPO / ".local" / "corpus").is_dir():
            self.fail("the link-ok corpus is unfetched; run scripts/fetch-corpus.sh")
        for path in sources:
            with self.subTest(source=str(path.relative_to(REPO))):
                stdlib = search.CENSUS.load_document(path)
                stream = search.yaml_stream(path.read_bytes())
                self.assertEqual(1, len(stream), "a registered source is one YAML document")
                self.assertEqual(
                    search.CENSUS.census_document(stdlib, root_path=path),
                    search.CENSUS.census_document(stream[0], root_path=path),
                )

    def test_each_refused_form_reads_as_the_declarations_it_makes(self) -> None:
        with SAMPLE.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle, delimiter="\t"))
        self.assertEqual(
            {"explicit-key", "escape", "flow-collection", "indentation", "tag", "stream"},
            {row["form"] for row in rows},
        )
        for row in rows:
            with self.subTest(form=row["form"], url=row["url"]):
                path = sample_document(row["url"], row["sha256"])
                with self.assertRaises(search.CENSUS.DocumentError):
                    search.CENSUS.load_document(path)
                reading = search.fallback_reading(path, path.read_bytes())
                self.assertIsNotNone(reading, "the pinned parser reads one description")
                document, loader = reading
                self.assertTrue(loader.startswith(search.YAML_LOADER), loader)
                counts = search.CENSUS.census_document(document, root_path=path)
                declared = dict(pair.split("=") for pair in row["declares"].split(";"))
                self.assertEqual({selector: int(n) for selector, n in declared.items()},
                                 {selector: counts.get(selector, 0) for selector in declared})

    def test_the_pin_is_the_one_the_inline_metadata_installs(self) -> None:
        header = (REPO / "scripts" / "golden-reach-search.py").read_text(encoding="utf-8").split('"""', 1)[0]
        self.assertIn(f'# dependencies = ["ruamel.yaml=={search.RUAMEL_YAML_PIN}"]', header)
        import ruamel.yaml

        self.assertEqual(search.RUAMEL_YAML_PIN, ruamel.yaml.__version__)


if __name__ == "__main__":
    unittest.main()
