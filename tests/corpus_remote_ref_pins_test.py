"""Boundary coverage for the corpus remote-`$ref` pin mechanism.

The pin lives in the FETCH path, so inspecting
`tests/fixtures/corpus-remote-ref-pins.tsv` proves nothing about it. Every test
below drives the real `scripts/fetch-corpus.sh` over a synthetic repository root
— a real `CORPUS.md`, a real pin manifest, a real `.local/corpus` destination —
against a loopback HTTP server this suite starts itself. Real `curl`, real
sockets, real files, and no dependence on GitHub: the assertions read the
document the fetch published, or the server's own request log, never a mock.

`serve_once` in `src/refs.rs` is the precedent one level down; a loopback socket
is established practice in this gate rather than a new dependency.

The same file holds the offline lint's boundary cases: the real `check` command
over the real tree, then over a manifest breaking each demand in turn, so a gate
that had stopped discriminating fails here instead of passing silently.

Run: `just test-corpus-remote-ref-pins` (part of `just check`).
"""

from __future__ import annotations

import hashlib
import http.server
import os
import shutil
import subprocess
import sys
import tempfile
import textwrap
import threading
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
MODULE = REPO / "scripts" / "corpus_remote_ref_pins.py"
MANIFEST_NAME = "corpus-remote-ref-pins.tsv"
COPIED_SCRIPTS = (
    "corpus-lib.sh",
    "corpus_remote_ref_pins.py",
    "fetch-corpus.sh",
    "lib.sh",
    "openapi-surface-census.py",
)

RAW = "https://raw.githubusercontent.com"
OWNER_REPO = "ethereum/execution-apis"
PINNED_SHA = "80d0a6ee6c129a29c507c35b0245a16c5a81b9d3"
SUPERSEDED_SHA = "46e9fb7df0fb241ea2c316d5938b1eb8ff4204a3"


def mutable_url(document: str) -> str:
    return f"{RAW}/{OWNER_REPO}/refs/heads/main/src/schemas/{document}.yaml"


def pinned_url(document: str, sha: str = PINNED_SHA) -> str:
    return f"{RAW}/{OWNER_REPO}/{sha}/src/schemas/{document}.yaml"


def pinned_path(document: str, sha: str = PINNED_SHA) -> str:
    """The loopback path a pinned URL becomes once its origin is overridden."""
    return f"/{OWNER_REPO}/{sha}/src/schemas/{document}.yaml"


def schema_document(name: str) -> bytes:
    return f"{name}:\n  type: string\n  title: {name}\n".encode()


def root_document(title: str, *, refs: dict[str, str], link: str | None = None) -> bytes:
    """A small OpenAPI document whose component schemas carry `refs`."""
    description = f"    Home page: {link}\n" if link else "    Home page: none\n"
    schemas = "".join(
        f"    {name}:\n      $ref: {reference}\n" for name, reference in refs.items()
    )
    return (
        "openapi: 3.0.0\n"
        "info:\n"
        f"  title: {title}\n"
        "  version: 0.0.0\n"
        "  description: >\n"
        f"{description}"
        "paths: {}\n"
        "components:\n"
        "  schemas:\n"
        f"{schemas}"
        "    Local:\n"
        "      $ref: '#/components/schemas/Alias'\n"
        "    Alias:\n"
        "      type: string\n"
    ).encode()


class RecordingHandler(http.server.BaseHTTPRequestHandler):
    """Serves the registered documents and appends every request path to a log."""

    protocol_version = "HTTP/1.1"

    def do_GET(self) -> None:  # noqa: N802 - http.server's spelling
        self.server.requests.append(self.path)
        body = self.server.documents.get(self.path)
        if body is None:
            self.send_error(404, "no such document")
            return
        self.send_response(200)
        self.send_header("Content-Type", "application/yaml")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args: object) -> None:
        """Quiet: the request log is the assertion surface, not stderr."""


@unittest.skipIf(os.name == "nt", "the corpus fetch scripts run on Linux/macOS")
class PinMechanismTests(unittest.TestCase):
    """Every case drives the real `scripts/fetch-corpus.sh`."""

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name) / "repo"
        (self.root / "scripts").mkdir(parents=True)
        (self.root / "tests" / "fixtures").mkdir(parents=True)
        for script in COPIED_SCRIPTS:
            shutil.copy2(REPO / "scripts" / script, self.root / "scripts" / script)
        shutil.copy2(
            REPO / "tests" / "fixtures" / "corpus-aliases.tsv",
            self.root / "tests" / "fixtures" / "corpus-aliases.tsv",
        )

        self.server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), RecordingHandler)
        self.server.documents = {}
        self.server.requests = []
        self.origin = "http://{}:{}".format(*self.server.server_address[:2])
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.addCleanup(self.thread.join)
        self.addCleanup(self.server.server_close)
        self.addCleanup(self.server.shutdown)
        self.addCleanup(self.temporary.cleanup)

        self.publish_documents()
        self.write_corpus()
        self.write_manifest()

    # -- the served world ---------------------------------------------------

    def publish_documents(self) -> None:
        """Serve the pinned schema documents and each row's root document."""
        self.digests: dict[str, str] = {}
        for document in ("block", "receipt", "withdrawal", "state", "absent"):
            body = schema_document(document)
            self.server.documents[pinned_path(document)] = body
            self.digests[document] = hashlib.sha256(body).hexdigest()

        self.roots = {
            "pinned-row": root_document(
                "Pinned Row",
                refs={
                    "Block": f"{mutable_url('block')}#/block",
                    "Receipt": f"{mutable_url('receipt')}#/receipt",
                    "Withdrawal": f"{mutable_url('withdrawal')}#/withdrawal",
                },
            ),
            # An absolute URL in a `description` is not a `$ref`: a text scan
            # would score this row as carrying a mutable cross-document reference.
            "plain-row": root_document(
                "Plain Row", refs={}, link=f"{RAW}/example/plain/refs/heads/main/README.md"
            ),
            "mutable-row": root_document(
                "Mutable Row", refs={"Block": f"{mutable_url('block')}#/block"}
            ),
            "digest-row": root_document(
                "Digest Row", refs={"State": f"{mutable_url('state')}#/state"}
            ),
            # Already carries an obsolete immutable address for a mapped file
            # beside the mutable one. Substituting the mutable spelling leaves
            # every current pin present and no mutable URL behind, so only the
            # obsolete-address rule can catch what remains.
            "mixed-row": root_document(
                "Mixed Row",
                refs={
                    "Block": f"{mutable_url('block')}#/block",
                    "BlockLegacy": f"{pinned_url('block', SUPERSEDED_SHA)}#/block",
                },
            ),
            "stale-row": root_document("Stale Row", refs={}),
        }
        for name, body in self.roots.items():
            self.server.documents[f"/specs/{name}.yaml"] = body

    def spec_url(self, name: str) -> str:
        return f"{self.origin}/specs/{name}.yaml"

    def write_corpus(self) -> None:
        rows = "\n".join(
            f"| {number} | `{name}` | test | {self.spec_url(name)} | `HEAD` | MIT | link-ok | pin boundary row |"
            for number, name in enumerate(sorted(self.roots), start=1)
        )
        (self.root / "tests" / "fixtures" / "CORPUS.md").write_text(
            "# Corpus\n\n"
            "| # | name | method | source | pinned ref | license | decision | shapes |\n"
            "|---:|---|---|---|---|---|---|---|\n"
            f"{rows}\n",
            encoding="utf-8",
        )

    def records(self) -> list[tuple[str, str, str, str]]:
        return [
            ("digest-row", mutable_url("state"), pinned_url("state"), "0" * 64),
            ("mixed-row", mutable_url("block"), pinned_url("block"), self.digests["block"]),
            ("pinned-row", mutable_url("block"), pinned_url("block"), self.digests["block"]),
            (
                "pinned-row",
                mutable_url("receipt"),
                pinned_url("receipt"),
                self.digests["receipt"],
            ),
            (
                "pinned-row",
                mutable_url("withdrawal"),
                pinned_url("withdrawal"),
                self.digests["withdrawal"],
            ),
            ("stale-row", mutable_url("absent"), pinned_url("absent"), self.digests["absent"]),
        ]

    def write_manifest(self, records: list[tuple[str, str, str, str]] | None = None) -> None:
        records = self.records() if records is None else records
        body = "".join("\t".join(record) + "\n" for record in records)
        (self.root / "tests" / "fixtures" / MANIFEST_NAME).write_text(
            "# Pin boundary manifest.\n" + body, encoding="utf-8"
        )

    @property
    def manifest(self) -> Path:
        return self.root / "tests" / "fixtures" / MANIFEST_NAME

    # -- driving the real fetch ---------------------------------------------

    def destination(self, name: str) -> Path:
        return self.root / ".local" / "corpus" / name

    def published(self, name: str) -> Path:
        return self.destination(name) / "openapi.yaml"

    def fetch(self, name: str, *args: str, **environment: str) -> subprocess.CompletedProcess[str]:
        env = os.environ.copy()
        env["CROZIER_CORPUS_PIN_ORIGIN"] = self.origin
        env.update(environment)
        return subprocess.run(
            [str(self.root / "scripts" / "fetch-corpus.sh"), "--fixture", name, *args],
            cwd=self.root,
            env=env,
            text=True,
            capture_output=True,
            check=False,
        )

    def expected_pinned_bytes(self) -> bytes:
        """What the served root document becomes under exactly the recorded pins."""
        text = self.roots["pinned-row"].decode()
        for _, mutable, pinned, _ in self.records():
            if mutable in text:
                text = text.replace(mutable, pinned)
        return text.encode()

    def assert_actionable(self, result: subprocess.CompletedProcess[str], *names: str) -> None:
        message = result.stdout + result.stderr
        self.assertNotEqual(result.returncode, 0, f"the fetch should have failed:\n{message}")
        for name in names:
            self.assertIn(name, message)

    def assert_no_leftovers(self, name: str, *, expected: set[str]) -> None:
        directory = self.destination(name)
        if not directory.exists():
            self.assertEqual(expected, set())
            return
        self.assertEqual({path.name for path in directory.iterdir()}, expected)

    # -- 1. rewriting happens, and it is exact ------------------------------

    def test_a_pinned_row_publishes_the_served_bytes_with_exactly_the_records_applied(
        self,
    ) -> None:
        result = self.fetch("pinned-row")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), str(self.published("pinned-row")))
        published = self.published("pinned-row").read_bytes()
        self.assertEqual(published, self.expected_pinned_bytes())
        self.assertNotIn(b"refs/heads/", published)
        for document in ("block", "receipt", "withdrawal"):
            self.assertIn(pinned_url(document).encode(), published)

    def test_the_successful_fetch_reports_only_the_path_its_callers_consume(self) -> None:
        result = self.fetch("pinned-row")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")

    # -- 2. rewriting happens BEFORE publication ----------------------------

    def test_a_refused_document_is_never_published_over_an_empty_cache(self) -> None:
        for name in ("mutable-row", "digest-row", "stale-row", "mixed-row"):
            with self.subTest(name):
                self.assert_actionable(self.fetch(name))
                self.assert_no_leftovers(name, expected=set())

    def test_a_refused_document_leaves_a_previously_published_file_intact(self) -> None:
        for name in ("mutable-row", "digest-row", "stale-row", "mixed-row"):
            with self.subTest(name):
                prior = f"openapi: 3.0.0\ninfo:\n  title: prior {name}\n".encode()
                self.destination(name).mkdir(parents=True, exist_ok=True)
                self.published(name).write_bytes(prior)
                self.assert_actionable(self.fetch(name))
                self.assertEqual(self.published(name).read_bytes(), prior)
                self.assert_no_leftovers(name, expected={"openapi.yaml"})

    # -- 3. a mutable absolute `$ref` is rejected for an unpinned row -------

    def test_a_row_with_no_records_may_not_publish_a_mutable_absolute_ref(self) -> None:
        result = self.fetch("mutable-row")
        self.assert_actionable(
            result, mutable_url("block"), str(self.manifest), "add a record"
        )

    # -- 4. ...and is inert when there is nothing to guard ------------------

    def test_a_row_with_no_records_and_no_absolute_ref_publishes_the_served_bytes(
        self,
    ) -> None:
        result = self.fetch("plain-row")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.published("plain-row").read_bytes(), self.roots["plain-row"])
        self.assertEqual(result.stderr, "")

    # -- 5. a digest mismatch fails -----------------------------------------

    def test_a_record_whose_digest_disagrees_with_the_served_bytes_fails(self) -> None:
        result = self.fetch("digest-row")
        self.assert_actionable(
            result,
            pinned_url("state"),
            self.digests["state"],
            "0" * 64,
            str(self.manifest),
            "re-measure the record",
        )

    # -- 6. a stale manifest record fails -----------------------------------

    def test_a_record_the_served_document_does_not_reference_fails(self) -> None:
        result = self.fetch("stale-row")
        self.assert_actionable(
            result, mutable_url("absent"), str(self.manifest), "delete it"
        )

    def test_an_obsolete_immutable_address_for_a_mapped_file_is_rejected(self) -> None:
        """The rule the mutable-URL and missing-pin rules cannot reach.

        `mixed-row`'s document names `block.yaml` twice: once mutably, once at a
        superseded commit. Substitution fixes the first; the second is still an
        address this repository no longer pins to.
        """
        result = self.fetch("mixed-row")
        self.assert_actionable(
            result,
            pinned_url("block", SUPERSEDED_SHA),
            pinned_url("block"),
            str(self.manifest),
            "re-run the fetch",
        )

    # -- 7. `--if-missing` hands back only a matching cache -----------------

    def plant(self, name: str, body: bytes) -> None:
        self.destination(name).mkdir(parents=True, exist_ok=True)
        self.published(name).write_bytes(body)
        self.server.requests.clear()

    def test_if_missing_refreshes_a_cache_that_still_carries_the_mutable_urls(self) -> None:
        self.plant("pinned-row", self.roots["pinned-row"])
        result = self.fetch("pinned-row", "--if-missing")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.published("pinned-row").read_bytes(), self.expected_pinned_bytes())
        self.assertIn("/specs/pinned-row.yaml", self.server.requests)

    def test_if_missing_refreshes_a_cache_pinned_to_a_superseded_commit(self) -> None:
        superseded = self.expected_pinned_bytes().replace(
            PINNED_SHA.encode(), SUPERSEDED_SHA.encode()
        )
        self.assertNotIn(b"refs/heads/", superseded)  # immutably addressed, yet stale
        self.plant("pinned-row", superseded)
        result = self.fetch("pinned-row", "--if-missing")
        self.assertEqual(result.returncode, 0, result.stderr)
        published = self.published("pinned-row").read_bytes()
        self.assertEqual(published, self.expected_pinned_bytes())
        self.assertNotIn(SUPERSEDED_SHA.encode(), published)
        self.assertIn("/specs/pinned-row.yaml", self.server.requests)

    def test_if_missing_refreshes_a_cache_predating_a_record(self) -> None:
        text = self.roots["pinned-row"].decode()
        for document in ("block", "receipt"):
            text = text.replace(mutable_url(document), pinned_url(document))
        self.plant("pinned-row", text.encode())
        result = self.fetch("pinned-row", "--if-missing")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.published("pinned-row").read_bytes(), self.expected_pinned_bytes())
        self.assertIn("/specs/pinned-row.yaml", self.server.requests)

    def test_if_missing_reuses_a_cache_that_matches_the_current_manifest(self) -> None:
        self.plant("pinned-row", self.expected_pinned_bytes())
        result = self.fetch("pinned-row", "--if-missing")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.published("pinned-row").read_bytes(), self.expected_pinned_bytes())
        self.assertEqual(self.server.requests, [], "a matching cache must cost no request")

    # -- the test-only fetch-origin override --------------------------------

    def test_the_fetch_origin_override_refuses_a_non_loopback_value(self) -> None:
        result = self.fetch("pinned-row", CROZIER_CORPUS_PIN_ORIGIN="https://example.test")
        self.assert_actionable(
            result,
            "https://example.test",
            "CROZIER_CORPUS_PIN_ORIGIN",
            "127.0.0.1",
            "unset it",
        )
        self.assert_no_leftovers("pinned-row", expected=set())


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
