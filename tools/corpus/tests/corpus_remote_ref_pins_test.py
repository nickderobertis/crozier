"""Boundary coverage for the corpus remote-`$ref` pin manifest's offline lint.

The real `check` command over the real tree, then over a manifest breaking each
demand in turn, so a gate that had stopped discriminating fails here instead of
passing silently. No server and no curl: the pin MECHANISM, which drives the
real fetch, is `tools/corpus-fetch/tests/corpus_remote_ref_pins_fetch_test.py`.

Run: `just test-corpus-remote-ref-pins` (part of `just check`).
"""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
MODULE = REPO / "tools" / "corpus" / "corpus_remote_ref_pins.py"
sys.path.insert(0, str(MODULE.parent))
import corpus_remote_ref_pins as pin_owner  # noqa: E402 - the production script's directory must be on sys.path first

MANIFEST_NAME = "corpus-remote-ref-pins.tsv"
RAW = "https://raw.githubusercontent.com"
OWNER_REPO = "ethereum/execution-apis"
PINNED_SHA = "80d0a6ee6c129a29c507c35b0245a16c5a81b9d3"


def mutable_url(document: str) -> str:
    return f"{RAW}/{OWNER_REPO}/refs/heads/main/src/schemas/{document}.yaml"


def pinned_url(document: str, sha: str = PINNED_SHA) -> str:
    return f"{RAW}/{OWNER_REPO}/{sha}/src/schemas/{document}.yaml"


class TheLintHoldsTheFinishedTree(unittest.TestCase):
    def run_check(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(MODULE), *args, "check"],
            cwd=REPO,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_the_real_manifest_passes_and_the_lint_is_quiet(self) -> None:
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "")
        self.assertEqual(result.stderr, "")

    def test_search_evidence_member_inventory_matches_the_authoritative_pins(self) -> None:
        evidence = REPO / "docs/openapi-surface/witness-search-github-publisher-trees/pinned-members.tsv"
        expected = ["corpus\tpath\timmutable_url\tsha256"]
        expected.extend(
            "\t".join((record.corpus_name, record.path, record.pinned_url, record.sha256))
            for record in pin_owner.load_tree_records(REPO)
            if record.corpus_name in {"folio-mod-authtoken", "raybot"}
        )
        self.assertEqual(
            evidence.read_text(encoding="utf-8").splitlines(),
            expected,
            "refresh the search inventory from the authoritative corpus tree pins",
        )


class TheLintStillDiscriminates(unittest.TestCase):
    """The real `check` over a manifest breaking each demand in turn."""

    GOOD = (
        "helios-verifiable-api",
        mutable_url("block"),
        pinned_url("block"),
        "37586fcfd0e8ac21912b3a3a66693c6304e2983a4996ce8a8830d6b504b956c7",
    )
    SECOND = (
        "helios-verifiable-api",
        mutable_url("receipt"),
        pinned_url("receipt"),
        "5b8f15e2d926d8faad8d189d141972f990ce1978176bea0c4435e700081f9979",
    )

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        # Resolve before joining: the module reports the manifest under its own
        # `--root`.resolve(), and on Windows the temporary directory arrives as an
        # 8.3 short name (`RUNNER~1`) that resolves to a different string
        # (`runneradmin`), so an unresolved root never matches the reported path.
        self.root = Path(self.temporary.name).resolve() / "repo"
        (self.root / "tests" / "fixtures").mkdir(parents=True)
        (self.root / "tests" / "fixtures" / "CORPUS.md").write_text(
            textwrap.dedent(
                """\
                # Corpus

                | # | name | method | source | pinned ref | license | decision | shapes |
                |---:|---|---|---|---|---|---|---|
                | 1 | `helios-verifiable-api` | github-raw | https://example.test/o.yaml | `HEAD` | MIT | link-ok | remote refs |
                """
            ),
            encoding="utf-8",
        )

    def check(self, *records: tuple[str, ...] | str) -> subprocess.CompletedProcess[str]:
        body = "".join(
            (record if isinstance(record, str) else "\t".join(record)) + "\n"
            for record in records
        )
        (self.root / "tests" / "fixtures" / MANIFEST_NAME).write_text(body, encoding="utf-8")
        return subprocess.run(
            [sys.executable, str(MODULE), "--root", str(self.root), "check"],
            text=True,
            capture_output=True,
            check=False,
        )

    def assert_rejected(self, result: subprocess.CompletedProcess[str], *names: str) -> None:
        self.assertNotEqual(result.returncode, 0, f"accepted:\n{result.stdout}{result.stderr}")
        self.assertIn(str(self.root / "tests" / "fixtures" / MANIFEST_NAME), result.stderr)
        for name in names:
            self.assertIn(name, result.stderr)

    def test_the_well_formed_manifest_is_accepted(self) -> None:
        result = self.check(self.GOOD, self.SECOND)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout + result.stderr, "")

    def test_a_mutable_pinned_url_is_rejected(self) -> None:
        record = (*self.GOOD[:2], mutable_url("block"), self.GOOD[3])
        self.assert_rejected(self.check(record), "refs", "pin the reference to a commit URL")

    def test_a_pinned_url_on_another_host_is_rejected(self) -> None:
        elsewhere = f"https://example.test/{OWNER_REPO}/{PINNED_SHA}/src/schemas/block.yaml"
        self.assert_rejected(
            self.check((*self.GOOD[:2], elsewhere, self.GOOD[3])),
            elsewhere,
            "raw.githubusercontent.com",
            "pin the reference to a commit URL",
        )

    def test_a_pinned_url_with_a_malformed_port_or_host_is_rejected(self) -> None:
        for malformed in (
            f"https://raw.githubusercontent.com:notaport/{OWNER_REPO}/{PINNED_SHA}/b.yaml",
            f"https://[raw.githubusercontent.com/{OWNER_REPO}/{PINNED_SHA}/b.yaml",
        ):
            with self.subTest(malformed=malformed):
                result = self.check((*self.GOOD[:2], malformed, self.GOOD[3]))
                self.assert_rejected(result, "is not a well-formed URL", "pin the reference")
                self.assertNotIn("Traceback", result.stderr)

    def test_a_document_reference_that_is_no_url_is_refused_by_apply(self) -> None:
        self.assertEqual(0, self.check(self.GOOD, self.SECOND).returncode)
        # `apply` reads the document through the census's reader, which reads the pins back.
        for relative in ("tools/surface-census/openapi-surface-census.py", "tools/corpus/corpus_remote_ref_pins.py"):
            (self.root / relative).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(REPO / relative, self.root / relative)
        document = self.root / "openapi.yaml"
        # Every recorded pin is referenced, so the reading reaches the malformed one.
        document.write_text(
            "openapi: 3.0.3\npaths:\n"
            f"  /a:\n    $ref: '{self.GOOD[1]}'\n  /b:\n    $ref: '{self.SECOND[1]}'\n"
            "  /c:\n    $ref: 'http://[raw.githubusercontent.com/x.yaml'\n",
            encoding="utf-8")
        result = subprocess.run(
            [sys.executable, str(MODULE), "--root", str(self.root), "apply", "helios-verifiable-api", str(document)],
            text=True, capture_output=True, check=False,
        )
        self.assertEqual(1, result.returncode, result.stderr)
        self.assertIn("is not a well-formed URL", result.stderr)
        self.assertIn("fix the reference in the document", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_a_malformed_digest_is_rejected(self) -> None:
        self.assert_rejected(
            self.check((*self.GOOD[:3], "NOTADIGEST")), "NOTADIGEST", "sha256sum"
        )

    def test_an_unknown_corpus_name_is_rejected(self) -> None:
        self.assert_rejected(
            self.check(("no-such-row", *self.GOOD[1:])),
            "no-such-row",
            "CORPUS.md",
            "correct the name or delete the record",
        )

    def test_a_duplicate_record_is_rejected(self) -> None:
        self.assert_rejected(self.check(self.GOOD, self.GOOD), "duplicate", "delete the rest")

    def test_an_out_of_order_file_is_rejected(self) -> None:
        self.assert_rejected(
            self.check(self.SECOND, self.GOOD),
            "sorted",
            self.SECOND[1],
            "sort the records",
        )

    def test_a_mutable_url_prefixing_another_in_the_same_row_is_rejected(self) -> None:
        prefixed = (
            self.GOOD[0],
            self.GOOD[1] + ".bak",
            self.GOOD[2] + ".bak",
            self.GOOD[3],
        )
        self.assert_rejected(self.check(self.GOOD, prefixed), "prefix", "drop a record")

    def test_too_few_columns_is_rejected(self) -> None:
        self.assert_rejected(
            self.check(self.GOOD[:3]), "3 tab-separated column(s)", "rewrite the record"
        )

    def test_too_many_columns_is_rejected(self) -> None:
        self.assert_rejected(
            self.check((*self.GOOD, "extra")),
            "5 tab-separated column(s)",
            "rewrite the record",
        )

    def test_an_empty_column_is_rejected(self) -> None:
        for index, column in enumerate(("corpus_name", "mutable_url", "pinned_url", "sha256")):
            with self.subTest(column):
                record = list(self.GOOD)
                record[index] = ""
                self.assert_rejected(
                    self.check(tuple(record)),
                    column,
                    "non-empty value",
                    "fill it in or delete the record",
                )

    def test_a_relative_mutable_url_is_rejected(self) -> None:
        self.assert_rejected(
            self.check((self.GOOD[0], "./schemas/block.yaml", *self.GOOD[2:])),
            "./schemas/block.yaml",
            "not an absolute URL",
            "record the `$ref` exactly as the upstream root document writes it",
        )


if __name__ == "__main__":
    unittest.main(verbosity=0)
