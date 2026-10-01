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
  `tests/data/census-fallback-sample.tsv`, pinned by commit, digest and licence,
  each committed under `tests/data/census-fallback-sample/` — the
  stdlib loader refuses it and the fallback reading counts the declarations the
  document visibly makes. A form the stdlib loader has since learned
  (`STDLIB_READS`) keeps its sample, now read by both loaders identically.

It needs the pinned parser but never the network: every sample is read from its
committed copy. Run it as `just test-census-fallback`, which CI's `live-e2e` leg
does.
The registered-corpus census and `just check` never use the fallback.
"""

from __future__ import annotations

import csv
import hashlib
import importlib.util
import os
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SAMPLE = REPO / "tests" / "data" / "census-fallback-sample.tsv"
COMMITTED = REPO / "tests" / "data" / "census-fallback-sample"


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


search = _load("golden_reach_search", REPO / "scripts" / "golden-reach-search.py")


def registered_yaml_sources() -> list[Path]:
    """Every committed registered YAML source, including multi-document trees."""
    vendored = sorted(REPO.glob("tests/fixtures/*/openapi.y*ml"))
    committed = sorted((REPO / "tests" / "fixtures" / "corpus-sources").rglob("*.y*ml"))
    return vendored + committed


def sample_document(url: str, sha256: str) -> Path:
    """A sample document's committed copy, held to its pinned digest."""
    path = COMMITTED / f"{sha256}{Path(url).suffix}"
    if not path.is_file():
        raise AssertionError(
            f"{path.relative_to(REPO)} is not committed; re-vendor it from its pinned URL "
            f"with `curl -fsSL {url} -o {path.relative_to(REPO)}` and commit it"
        )
    measured = hashlib.sha256(path.read_bytes()).hexdigest()
    if measured != sha256:
        raise AssertionError(f"{path.relative_to(REPO)} is {measured}, not the pinned {sha256} of {url}")
    return path


# Sampled forms the stdlib loader now reads although the sample pinned them as
# refused: a quote inside a flow plain scalar (dashy's `page's config`). Both
# loaders must agree on these rather than the stdlib loader refusing them.
STDLIB_READS = {"flow-collection"}


class FallbackAgreementTests(unittest.TestCase):
    def test_both_loaders_count_the_same_selectors_wherever_both_read(self) -> None:
        sources = registered_yaml_sources()
        self.assertTrue(sources, "no registered YAML source to compare the loaders on")
        if os.environ.get("CROZIER_REQUIRE_CORPUS") and not (REPO / "tests" / "fixtures" / "corpus-sources").is_dir():
            self.fail("the committed corpus sources are missing; run just lint-corpus-sources")
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
                if row["form"] in STDLIB_READS:
                    document = search.CENSUS.load_document(path)
                    self.assertEqual(search.yaml_stream(path.read_bytes()), [document])
                else:
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

    def test_every_sample_is_committed_at_its_pinned_digest_with_its_licence(self) -> None:
        with SAMPLE.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle, delimiter="\t"))
        expected = {f"{row['sha256']}{Path(row['url']).suffix}" for row in rows}
        self.assertEqual(expected, {path.name for path in COMMITTED.iterdir()})
        for row in rows:
            with self.subTest(form=row["form"]):
                self.assertTrue(row["license"].strip(), "record the repository licence the sample is committed under")
                self.assertTrue(row["url"].startswith("https://raw.githubusercontent.com/"), row["url"])
                path = sample_document(row["url"], row["sha256"])
                self.assertEqual(row["sha256"], hashlib.sha256(path.read_bytes()).hexdigest())

    def test_a_missing_or_drifted_sample_is_refused_with_its_next_action(self) -> None:
        global COMMITTED
        url = "https://raw.githubusercontent.com/example/specs/0123456789abcdef0123456789abcdef01234567/api.yaml"
        data = b"openapi: 3.0.0\n"
        pinned = hashlib.sha256(data).hexdigest()
        original = COMMITTED
        with tempfile.TemporaryDirectory(dir=REPO / "tests" / "data") as directory:
            COMMITTED = Path(directory)
            try:
                with self.assertRaises(AssertionError) as missing:
                    sample_document(url, pinned)
                self.assertIn(f"curl -fsSL {url} -o", str(missing.exception))
                (COMMITTED / f"{pinned}.yaml").write_bytes(data + b"# drifted\n")
                with self.assertRaises(AssertionError) as drifted:
                    sample_document(url, pinned)
                self.assertIn(f"not the pinned {pinned}", str(drifted.exception))
                (COMMITTED / f"{pinned}.yaml").write_bytes(data)
                self.assertEqual(data, sample_document(url, pinned).read_bytes())
            finally:
                COMMITTED = original

    def test_the_pin_is_the_one_the_inline_metadata_installs(self) -> None:
        header = (REPO / "scripts" / "golden-reach-search.py").read_text(encoding="utf-8").split('"""', 1)[0]
        self.assertIn(f'# dependencies = ["ruamel.yaml=={search.RUAMEL_YAML_PIN}"]', header)
        import ruamel.yaml

        self.assertEqual(search.RUAMEL_YAML_PIN, ruamel.yaml.__version__)


if __name__ == "__main__":
    unittest.main()
