"""The corpus rebuild tooling through real `curl` against a loopback server.

`TheRebuildToolingFetches` drives `vendor` and `audit` through the real
`tools/corpus/fetch-corpus.sh` and real `curl` against the loopback HTTP server
the synthetic root starts, the way `corpus_remote_ref_pins_fetch_test.py` drives
the fetch itself. `TheCheckStillDiscriminates` vendors that root the same way,
then drives the real offline `check` over it breaking each demand in turn, so a
lint that had stopped discriminating fails here. The synthetic root, and the
offline cases that need no fetch, are `tools/corpus/tests/corpus_sources_test.py`.

Run: `just test-corpus-sources` (part of `just check`).
"""

from __future__ import annotations

import hashlib
import os
import shutil
import subprocess
import sys
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "tools" / "corpus" / "tests"))
from corpus_sources_test import (  # noqa: E402 - the offline suite's directory must be on sys.path first
    BLOCK,
    MUTABLE_URL,
    PINNED_SHA,
    PINNED_URL,
    PLAIN,
    SyntheticRoot,
    corpus_sources,
    run,
)


@unittest.skipIf(os.name == "nt", "the corpus fetch scripts run on Linux/macOS")
class TheRebuildToolingFetches(SyntheticRoot):
    """`vendor` and `audit` through the real fetch, real curl and a loopback server."""

    def test_vendor_commits_every_resolved_file_with_its_fetched_digest(self) -> None:
        completed = self.vendor()
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertEqual(PLAIN, self.committed("plain/openapi.json").read_bytes())
        published = self.committed("remote/openapi.yaml").read_bytes()
        self.assertIn(PINNED_URL.encode(), published)
        self.assertNotIn(MUTABLE_URL.encode(), published)
        remote = self.committed(f"remote/remote/raw.githubusercontent.com/example/schemas/{PINNED_SHA}/block.yaml")
        self.assertEqual(BLOCK, remote.read_bytes())
        records = {record.path: record for record in corpus_sources.load_manifest(self.root)}
        self.assertEqual(
            hashlib.sha256(published).hexdigest(),
            records["tests/fixtures/corpus-sources/remote/openapi.yaml"].sha256,
        )
        self.assertEqual(PINNED_URL, records[remote.relative_to(self.root).as_posix()].source_url)
        self.assertEqual(0, run(self.root, "check").returncode)

    def test_audit_passes_unchanged_upstream_and_names_a_drifted_file(self) -> None:
        self.assertEqual(0, self.vendor().returncode)
        self.assertEqual(0, self.audit().returncode)
        self.server.documents["/specs/plain.json"] = PLAIN.replace(b"Plain", b"Edited")
        completed = self.audit("--fixture", "plain")
        self.assert_refused(completed, "tests/fixtures/corpus-sources/plain/openapi.json")
        self.assertEqual(PLAIN, self.committed("plain/openapi.json").read_bytes(), "audit never writes")

    def test_rebuild_can_reuse_a_completed_fetch(self) -> None:
        self.assertEqual(0, self.vendor().returncode)
        fetched = self.root / "fetched"
        fetched.mkdir()
        result = subprocess.run(
            [corpus_sources.bash(), str(self.root / "tools/corpus/fetch-corpus.sh"), "--fixture", "plain", str(fetched)],
            cwd=self.root, capture_output=True, text=True,
        )
        self.assertEqual(0, result.returncode, result.stderr)
        requests = len(self.server.requests)
        self.assertEqual(0, self.vendor("--fixture", "plain", "--from", str(fetched)).returncode)
        self.assertEqual(0, self.audit("--fixture", "plain", "--from", str(fetched)).returncode)
        self.assertEqual(requests, len(self.server.requests), "completed plain fetch was not reused")
        self.assertEqual(PLAIN, self.committed("plain/openapi.json").read_bytes())

    def test_vendor_refuses_a_pinned_document_whose_bytes_moved(self) -> None:
        self.server.documents[f"/example/schemas/{PINNED_SHA}/block.yaml"] = BLOCK + b"# moved\n"
        completed = self.vendor()
        self.assert_refused(completed, "sha256")
        self.assertFalse(self.committed("remote").exists(), "nothing is committed from a refused fetch")

    def test_an_unknown_fixture_is_refused(self) -> None:
        self.assert_refused(self.vendor("--fixture", "absent"), "'absent' is not a canonical CORPUS.md row")


@unittest.skipIf(os.name == "nt", "the corpus fetch scripts run on Linux/macOS")
class TheCheckStillDiscriminates(SyntheticRoot):
    """The offline `check` over a vendored synthetic root, broken one demand at a time."""

    def setUp(self) -> None:
        super().setUp()
        completed = self.vendor()
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.requests_before = len(self.server.requests)

    def check(self) -> subprocess.CompletedProcess[str]:
        completed = run(self.root, "check")
        self.assertEqual([], self.server.requests[self.requests_before:], "`check` opened a socket")
        return completed

    def test_the_vendored_root_passes(self) -> None:
        completed = self.check()
        self.assertEqual(0, completed.returncode, completed.stderr)

    def test_an_edited_byte_is_refused(self) -> None:
        path = self.committed("plain/openapi.json")
        path.write_bytes(path.read_bytes().replace(b"Plain", b"Plaim"))
        self.assert_refused(self.check(), "plain/openapi.json has sha256", "a committed source is never edited")

    def test_a_missing_file_is_refused(self) -> None:
        self.committed("plain/openapi.json").unlink()
        self.assert_refused(self.check(), "plain/openapi.json is recorded but missing")

    def test_an_unrecorded_file_is_refused(self) -> None:
        self.committed("plain/notes.txt").write_text("stray\n", encoding="utf-8")
        self.assert_refused(self.check(), "plain/notes.txt is not recorded")

    def test_a_fetch_only_row_is_refused(self) -> None:
        self.write_corpus("link-ok")
        self.assert_refused(self.check(), "plain: CORPUS.md decision is `link-ok`")

    def test_a_registered_row_without_a_committed_source_is_refused(self) -> None:
        self.write_corpus(
            "committed",
            extra=f"| 3 | `unvendored` | test | {self.origin}/specs/unvendored.json | `HEAD` | MIT | committed | new |\n",
        )
        self.assert_refused(self.check(), "unvendored: openapi.json is not committed")

    def test_a_recorded_row_the_manifest_no_longer_registers_is_refused(self) -> None:
        corpus = self.fixtures / "CORPUS.md"
        corpus.write_text(corpus.read_text(encoding="utf-8").replace("| committed | plain |", "| withdrawn | plain |"), encoding="utf-8")
        self.assert_refused(self.check(), "plain: recorded in tests/fixtures/corpus-sources.tsv but is no canonical CORPUS.md row")

    def test_a_pinned_remote_document_left_uncommitted_is_refused(self) -> None:
        manifest = self.fixtures / "corpus-sources.tsv"
        manifest.write_text(
            "".join(line for line in manifest.read_text(encoding="utf-8").splitlines(keepends=True) if "block.yaml" not in line),
            encoding="utf-8",
        )
        shutil.rmtree(self.committed("remote/remote"))
        self.assert_refused(self.check(), f"remote: remote/raw.githubusercontent.com/example/schemas/{PINNED_SHA}/block.yaml is not committed")

    def test_a_record_disagreeing_with_the_pin_manifest_is_refused(self) -> None:
        pins = self.fixtures / "corpus-remote-ref-pins.tsv"
        pins.write_text(pins.read_text(encoding="utf-8").replace(hashlib.sha256(BLOCK).hexdigest(), "0" * 64), encoding="utf-8")
        self.assert_refused(self.check(), "corpus-remote-ref-pins.tsv pins " + "0" * 64)

    def test_manifest_structure_refuses_each_malformed_record(self) -> None:
        manifest = self.fixtures / "corpus-sources.tsv"
        original = manifest.read_text()
        rows = [line for line in original.splitlines() if line and not line.startswith("#")]
        cases = (
            (rows[0] + "\textra\n", "expected 4 tab-separated cells"),
            ("\n".join(reversed(rows)) + "\n", "records must sort"),
            ("\n".join(sorted(rows + [rows[0]])) + "\n", "recorded twice"),
            (original.replace(self.origin + "/specs/plain.json", self.origin + "/other.json"),
             "records source"),
        )
        for body, diagnostic in cases:
            with self.subTest(diagnostic=diagnostic):
                manifest.write_text(body)
                self.assert_refused(self.check(), diagnostic)
        manifest.write_text(original)
        self.assertEqual(0, self.check().returncode)

    def test_prepare_refuses_duplicate_aliases_and_nonempty_staging(self) -> None:
        aliases = self.fixtures / "corpus-aliases.tsv"
        original = aliases.read_text()
        aliases.write_text("plain\tone\nplain\ttwo\n")
        completed = run(self.root, "prepare", "--fixture", "plain", "--output", str(self.root / "staged"))
        self.assert_refused(completed, "duplicate alias")
        aliases.write_text(original)
        staging = self.root / "staged"
        staging.mkdir()
        (staging / "keep.txt").write_text("keep")
        completed = run(self.root, "prepare", "--fixture", "plain", "--output", str(staging))
        self.assert_refused(completed, "use a fresh directory")
        self.assertEqual("keep", (staging / "keep.txt").read_text())

    def test_unsafe_registered_names_are_refused_before_rebuild(self) -> None:
        corpus = self.fixtures / "CORPUS.md"
        corpus.write_text(corpus.read_text().replace("`plain`", "`../outside`"))
        self.assert_refused(self.vendor(), "unsafe corpus name")
        self.assertEqual(PLAIN, self.committed("plain/openapi.json").read_bytes())

    def test_prepare_refuses_forged_remote_provenance(self) -> None:
        manifest = self.fixtures / "corpus-sources.tsv"
        original = manifest.read_text()
        for url in ("", "https://wrong.example/schema.yaml"):
            with self.subTest(url=url):
                lines = original.splitlines()
                for index, line in enumerate(lines):
                    if "\t" + PINNED_URL + "\t" in line:
                        cells = line.split("\t")
                        cells[2] = url
                        lines[index] = "\t".join(cells)
                manifest.write_text("\n".join(lines) + "\n")
                completed = run(self.root, "prepare", "--fixture", "remote",
                                "--output", str(self.root / "stage"))
                self.assert_refused(completed, "provenance disagrees")
                self.assertFalse((self.root / "stage").exists())
        manifest.write_text(original)

    def test_a_malformed_digest_is_refused(self) -> None:
        manifest = self.fixtures / "corpus-sources.tsv"
        text = manifest.read_text(encoding="utf-8")
        digest = hashlib.sha256(PLAIN).hexdigest()
        manifest.write_text(text.replace(digest, digest.upper()), encoding="utf-8")
        self.assert_refused(self.check(), "is not 64 lowercase hexadecimal characters")

    def test_a_path_outside_its_row_is_refused(self) -> None:
        manifest = self.fixtures / "corpus-sources.tsv"
        text = manifest.read_text(encoding="utf-8")
        manifest.write_text(text.replace("corpus-sources/plain/openapi.json", "corpus-sources/remote/../plain/openapi.json"), encoding="utf-8")
        self.assert_refused(self.check(), "is not a file under tests/fixtures/corpus-sources/plain/")


if __name__ == "__main__":
    unittest.main()
