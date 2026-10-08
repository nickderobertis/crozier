"""Boundary coverage for the corpus remote-`$ref` pin mechanism.

The pin lives in the FETCH path, so inspecting
`tests/fixtures/corpus-remote-ref-pins.tsv` proves nothing about it. Every test
below drives the real `tools/corpus/fetch-corpus.sh` over a synthetic repository root
— a real `CORPUS.md`, a real pin manifest, a real `.local/corpus` destination —
against a loopback HTTP server this suite starts itself. Real `curl`, real
sockets, real files, and no dependence on GitHub: the assertions read the
document the fetch published, or the server's own request log, never a mock.

`serve_once` in `src/refs.rs` is the precedent one level down; a loopback socket
is established practice in this gate rather than a new dependency.

The offline lint's boundary cases, which start no server and run no curl, are
`tools/corpus/tests/corpus_remote_ref_pins_test.py` in the `corpus` project; this
suite is the `corpus-fetch` project's, so an edit to an offline script there
never pays for the fetch.

Run: `just test-corpus-remote-ref-pins` (part of `just check`).
"""

from __future__ import annotations

import datetime
import email.utils
import hashlib
import http.server
import os
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
MANIFEST_NAME = "corpus-remote-ref-pins.tsv"
# Repository-relative, and copied to the same path under the synthetic root, so
# each script finds its neighbours where the real tree keeps them.
COPIED_SCRIPTS = (
    "tools/corpus/corpus-lib.sh",
    "tools/corpus/corpus_remote_ref_pins.py",
    "tools/corpus/fetch-corpus.sh",
    "scripts/lib.sh",
    "tools/surface-census/openapi-surface-census.py",
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
    schemas = "".join(f"    {name}:\n      $ref: {reference}\n" for name, reference in refs.items())
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

    def do_GET(self) -> None:
        self.server.requests.append(self.path)
        if self.server.throttles.get(self.path, 0):
            self.server.throttles[self.path] -= 1
            self.send_response(429)
            self.send_header("Retry-After", self.server.throttle_retry_after.get(self.path, "0"))
            self.send_header("Content-Length", "0")
            self.end_headers()
            return
        body = self.server.documents.get(self.path)
        # A hook the request runs first, as a host changing under the fetch would.
        self.server.on_request.pop(self.path, lambda: None)()
        if body is None:
            self.send_error(404, "no such document")
            return
        self.send_response(200)
        self.send_header("Content-Type", "application/yaml")
        if self.path in self.server.success_retry_after:
            self.send_header("Retry-After", self.server.success_retry_after[self.path])
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args: object) -> None:
        """Quiet: the request log is the assertion surface, not stderr."""


@unittest.skipIf(os.name == "nt", "the corpus fetch scripts run on Linux/macOS")
class PinMechanismTests(unittest.TestCase):
    """Every case drives the real `tools/corpus/fetch-corpus.sh`."""

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name) / "repo"
        (self.root / "scripts").mkdir(parents=True)
        (self.root / "tests" / "fixtures").mkdir(parents=True)
        for script in COPIED_SCRIPTS:
            (self.root / script).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(REPO / script, self.root / script)
        shutil.copy2(
            REPO / "tests" / "fixtures" / "corpus-aliases.tsv",
            self.root / "tests" / "fixtures" / "corpus-aliases.tsv",
        )

        self.server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), RecordingHandler)
        self.server.documents = {}
        self.server.requests = []
        self.server.throttles = {}
        self.server.throttle_retry_after = {}
        self.server.success_retry_after = {}
        self.server.on_request = {}
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
            "plain-row": root_document("Plain Row", refs={}, link=f"{RAW}/example/plain/refs/heads/main/README.md"),
            "mutable-row": root_document("Mutable Row", refs={"Block": f"{mutable_url('block')}#/block"}),
            "digest-row": root_document("Digest Row", refs={"State": f"{mutable_url('state')}#/state"}),
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

    def destination(self, name: str) -> Path:
        return self.root / ".local" / "corpus" / name

    def published(self, name: str) -> Path:
        return self.destination(name) / "openapi.yaml"

    def fetch(self, name: str, *args: str, **environment: str) -> subprocess.CompletedProcess[str]:
        env = os.environ.copy()
        env["CROZIER_CORPUS_PIN_ORIGIN"] = self.origin
        env.update(environment)
        return subprocess.run(
            [str(self.root / "tools" / "corpus" / "fetch-corpus.sh"), "--fixture", name, *args],
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

    def test_a_throttled_pinned_document_is_retried_before_publication(self) -> None:
        path = pinned_path("block")
        self.server.throttles[path] = 1
        result = self.fetch("pinned-row")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.server.requests.count(path), 2)
        self.assertEqual(self.published("pinned-row").read_bytes(), self.expected_pinned_bytes())

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

    def test_a_row_with_no_records_may_not_publish_a_mutable_absolute_ref(self) -> None:
        result = self.fetch("mutable-row")
        self.assert_actionable(result, mutable_url("block"), str(self.manifest), "add a record")

    def test_a_row_with_no_records_and_no_absolute_ref_publishes_the_served_bytes(
        self,
    ) -> None:
        result = self.fetch("plain-row")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.published("plain-row").read_bytes(), self.roots["plain-row"])
        self.assertEqual(result.stderr, "")

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

    def test_a_record_the_served_document_does_not_reference_fails(self) -> None:
        result = self.fetch("stale-row")
        self.assert_actionable(result, mutable_url("absent"), str(self.manifest), "delete it")

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
        superseded = self.expected_pinned_bytes().replace(PINNED_SHA.encode(), SUPERSEDED_SHA.encode())
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

    def register_tree(self, *, sibling_digest: str | None = None, include_sibling: bool = True) -> None:
        """Add an immutable, real two-file source to the boundary repository."""
        base = f"{RAW}/example/api/{PINNED_SHA}/spec"
        root = b"openapi: 3.0.3\ninfo: {title: Tree, version: '1'}\npaths: {}\ncomponents:\n  schemas:\n    Item:\n      $ref: './schemas/item.yaml#/components/schemas/Item'\n"
        sibling = (
            b"components:\n  schemas:\n    Item:\n      type: object\n      properties:\n        id: {type: string}\n"
        )
        self.server.documents[f"/example/api/{PINNED_SHA}/spec/openapi.yaml"] = root
        self.server.documents[f"/example/api/{PINNED_SHA}/spec/schemas/item.yaml"] = sibling
        corpus = self.root / "tests" / "fixtures" / "CORPUS.md"
        corpus.write_text(
            corpus.read_text()
            + f"| 99 | `tree-row` | github-raw | {base}/openapi.yaml | `{PINNED_SHA}` | MIT | link-ok | relative ref |\n"
        )
        records = [
            (
                "tree",
                "tree-row",
                "spec/openapi.yaml",
                f"{RAW}/example/api/{PINNED_SHA}/spec/openapi.yaml",
                hashlib.sha256(root).hexdigest(),
            ),
        ]
        if include_sibling:
            records.append(
                (
                    "tree",
                    "tree-row",
                    "spec/schemas/item.yaml",
                    f"{RAW}/example/api/{PINNED_SHA}/spec/schemas/item.yaml",
                    sibling_digest or hashlib.sha256(sibling).hexdigest(),
                )
            )
        with self.manifest.open("a") as stream:
            for record in records:
                stream.write("\t".join(record) + "\n")

    def test_a_tree_fetches_every_pinned_file_and_refreshes_a_drifted_cache(self) -> None:
        self.register_tree()
        fetched = self.fetch("tree-row")
        self.assertEqual(fetched.returncode, 0, fetched.stderr)
        root = self.destination("tree-row") / "spec/openapi.yaml"
        sibling = self.destination("tree-row") / "spec/schemas/item.yaml"
        self.assertEqual(fetched.stdout.strip(), str(root))
        self.assertIn(b"Item:", sibling.read_bytes())
        self.server.requests.clear()
        self.assertEqual(self.fetch("tree-row", "--if-missing").returncode, 0)
        self.assertEqual(self.server.requests, [])
        sibling.write_text("drift")
        self.assertEqual(self.fetch("tree-row", "--if-missing").returncode, 0)
        self.assertIn("/example/api/" + PINNED_SHA + "/spec/schemas/item.yaml", self.server.requests)
        self.assertIn(b"Item:", sibling.read_bytes())

    def test_a_tree_ref_outside_the_pinned_set_is_refused(self) -> None:
        self.register_tree(include_sibling=False)
        self.assert_actionable(self.fetch("tree-row"), "leaves the pinned tree", "schemas/item.yaml")

    def test_a_tree_member_digest_mismatch_is_refused(self) -> None:
        self.register_tree(sibling_digest="0" * 64)
        self.assert_actionable(self.fetch("tree-row"), "serves sha256", "0" * 64)

    def test_tree_verification_refuses_extra_files_and_mutable_absolute_refs(self) -> None:
        self.register_tree()
        self.assertEqual(self.fetch("tree-row").returncode, 0)
        tree = self.destination("tree-row")
        extra = tree / "extra.yaml"
        extra.write_text("type: string\n")
        result = subprocess.run(
            [
                sys.executable,
                str(self.root / "tools/corpus/corpus_remote_ref_pins.py"),
                "--root",
                str(self.root),
                "verify-tree",
                "tree-row",
                str(tree),
            ],
            text=True,
            capture_output=True,
            check=False,
        )
        self.assert_actionable(result, "tree file set drifted", "extra.yaml")
        extra.unlink()
        root = tree / "spec/openapi.yaml"
        root.write_bytes(root.read_bytes().replace(b"./schemas/item.yaml", mutable_url("block").encode()))
        # Re-pin only this controlled boundary document to reach the reference guard.
        manifest = self.manifest.read_text()
        old_digest = hashlib.sha256(self.server.documents[f"/example/api/{PINNED_SHA}/spec/openapi.yaml"]).hexdigest()
        self.manifest.write_text(manifest.replace(old_digest, hashlib.sha256(root.read_bytes()).hexdigest()))
        result = subprocess.run(
            [
                sys.executable,
                str(self.root / "tools/corpus/corpus_remote_ref_pins.py"),
                "--root",
                str(self.root),
                "verify-tree",
                "tree-row",
                str(tree),
            ],
            text=True,
            capture_output=True,
            check=False,
        )
        self.assert_actionable(result, "absolute `$ref`", "bytes it serves can change")

    def test_retry_after_dates_and_success_pacing_are_honoured(self) -> None:
        self.register_tree()
        path = f"/example/api/{PINNED_SHA}/spec/openapi.yaml"
        self.server.throttles[path] = 1
        self.server.throttle_retry_after[path] = email.utils.format_datetime(
            datetime.datetime.now(datetime.UTC) + datetime.timedelta(seconds=1),
            usegmt=True,
        )
        self.server.success_retry_after[path] = "1"
        started = time.monotonic()
        result = self.fetch("tree-row")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertGreaterEqual(time.monotonic() - started, 0.9)
        self.assertGreaterEqual(self.server.requests.count(path), 2)

    def test_a_publisher_that_keeps_throttling_gets_an_actionable_failure(self) -> None:
        self.register_tree()
        path = f"/example/api/{PINNED_SHA}/spec/openapi.yaml"
        self.server.throttles[path] = 6
        result = self.fetch("tree-row")
        self.assert_actionable(result, "remains throttled after five waits", "retry the fetch")
        self.assertEqual(self.server.requests.count(path), 6)
        self.assertFalse(self.destination("tree-row").exists())

    def test_tree_pin_lint_rejects_invalid_records_and_inconsistent_sources(self) -> None:
        self.register_tree()
        original = self.manifest.read_text()
        tree_lines = [line for line in original.splitlines() if line.startswith("tree\t")]
        root_line, sibling_line = tree_lines

        def check_with(manifest: str, phrase: str, corpus: str | None = None) -> None:
            with self.subTest(phrase=phrase):
                self.manifest.write_text(manifest)
                if corpus is not None:
                    (self.root / "tests/fixtures/CORPUS.md").write_text(corpus)
                result = subprocess.run(
                    [
                        sys.executable,
                        str(self.root / "tools/corpus/corpus_remote_ref_pins.py"),
                        "--root",
                        str(self.root),
                        "check",
                    ],
                    text=True,
                    capture_output=True,
                    check=False,
                )
                self.assert_actionable(result, phrase)
                self.manifest.write_text(original)

        check_with(original.replace(root_line, root_line.rsplit("\t", 1)[0]), "five tab-separated cells")
        check_with(
            original.replace(root_line, root_line.replace("spec/openapi.yaml", "spec/../openapi.yaml")),
            "invalid tree name or relative document path",
        )
        check_with(original.replace(root_line, root_line.replace(PINNED_SHA, "refs/heads/main")), "40-character commit")
        check_with(original.replace(root_line, root_line.rsplit("\t", 1)[0] + "\tbad"), "invalid SHA-256")
        check_with(original + root_line + "\n", "duplicate tree member")
        check_with(
            original.replace(root_line + "\n" + sibling_line, sibling_line + "\n" + root_line), "tree records must sort"
        )
        check_with(original.replace("tree\ttree-row\t", "tree\tunknown-row\t"), "unknown corpus")
        check_with(
            original.replace(root_line, root_line.replace(PINNED_SHA, SUPERSEDED_SHA)),
            "must pin its CORPUS.md root URL exactly once",
        )
        check_with(
            original.replace(sibling_line, sibling_line.replace(PINNED_SHA, SUPERSEDED_SHA)),
            "does not share the root URL",
        )
        corpus_path = self.root / "tests/fixtures/CORPUS.md"
        corpus = corpus_path.read_text()
        check_with(
            original,
            "must use CORPUS.md pinned ref",
            corpus.replace(
                f"`{PINNED_SHA}` | MIT | link-ok | relative ref", f"`{SUPERSEDED_SHA}` | MIT | link-ok | relative ref"
            ),
        )

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

    # The fetchers run inside the caller's command substitution, where errexit
    # does not reach, so each step's failure must be returned explicitly.

    def assert_refused_without_a_path(self, result: subprocess.CompletedProcess[str], *names: str) -> None:
        self.assert_actionable(result, *names, "then re-run")
        self.assertEqual(result.stdout, "", "a failed fetch must not print a source path")

    def test_a_missing_manifest_names_how_to_restore_it(self) -> None:
        (self.root / "tests" / "fixtures" / "CORPUS.md").unlink()
        self.assert_actionable(self.fetch("plain-row"), "git checkout -- tests/fixtures/CORPUS.md", "then re-run")

    def test_a_missing_alias_file_names_how_to_restore_it(self) -> None:
        (self.root / "tests" / "fixtures" / "corpus-aliases.tsv").unlink()
        self.assert_refused_without_a_path(
            self.fetch("plain-row"),
            "missing fixture alias file",
            "git checkout -- tests/fixtures/corpus-aliases.tsv",
        )

    def test_an_invalid_alias_file_names_the_line_and_how_to_repair_it(self) -> None:
        (self.root / "tests" / "fixtures" / "corpus-aliases.tsv").write_text(
            "# aliases\nbroken-row\n", encoding="utf-8"
        )
        self.assert_refused_without_a_path(
            self.fetch("plain-row"),
            "line 2: expected two safe fixture names",
            "fix that line",
            "git checkout -- tests/fixtures/corpus-aliases.tsv",
        )

    def test_an_alias_file_that_maps_ambiguously_names_the_line_and_how_to_repair_it(self) -> None:
        for label, body, reason in (
            ("self-alias", "plain-row\tplain-row\n", "line 2: alias source and fixture directory must differ"),
            ("duplicate source", "plain-row\tfirst\nplain-row\tsecond\n", "line 3: duplicate alias source plain-row"),
            ("duplicate fixture", "first\tshared\nsecond\tshared\n", "line 3: duplicate fixture directory shared"),
        ):
            with self.subTest(label):
                (self.root / "tests" / "fixtures" / "corpus-aliases.tsv").write_text(
                    "# aliases\n" + body, encoding="utf-8"
                )
                self.assert_refused_without_a_path(
                    self.fetch("plain-row"),
                    reason,
                    "fix that line",
                    "git checkout -- tests/fixtures/corpus-aliases.tsv",
                )

    def test_an_alias_file_with_no_aliases_resolves_each_row_to_its_own_directory(self) -> None:
        (self.root / "tests" / "fixtures" / "corpus-aliases.tsv").write_text("# no aliases left\n", encoding="utf-8")
        result = self.fetch("plain-row")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.published("plain-row").read_bytes(), self.roots["plain-row"])

    def test_a_failed_download_names_the_row_and_what_to_check(self) -> None:
        self.add_repository_row("absent-row", self.spec_url("absent-row"), "HEAD")
        self.assert_refused_without_a_path(
            self.fetch("absent-row"),
            f"could not download the spec for absent-row from {self.spec_url('absent-row')}",
            "source URL in tests/fixtures/CORPUS.md",
        )
        self.assert_no_leftovers("absent-row", expected=set())

    def test_an_empty_download_names_the_row_and_what_to_check(self) -> None:
        self.server.documents["/specs/empty-row.yaml"] = b""
        self.add_repository_row("empty-row", self.spec_url("empty-row"), "HEAD")
        self.assert_refused_without_a_path(
            self.fetch("empty-row"),
            "fetched an empty spec for empty-row",
            "serves the OpenAPI document itself",
        )
        self.assert_no_leftovers("empty-row", expected=set())

    def test_a_partial_download_it_cannot_remove_is_named_with_how_to_delete_it(self) -> None:
        if os.geteuid() == 0:
            self.skipTest("root removes files from a read-only directory")
        self.server.documents["/specs/stuck-row.yaml"] = b""
        self.add_repository_row("stuck-row", self.spec_url("stuck-row"), "HEAD")
        cache = self.destination("stuck-row")
        # The cache directory turns read-only once the fetch has made its temporary file.
        self.server.on_request["/specs/stuck-row.yaml"] = lambda: cache.chmod(0o555)
        self.addCleanup(lambda: cache.exists() and cache.chmod(0o755))
        result = self.fetch("stuck-row")
        self.assert_refused_without_a_path(result, "fetched an empty spec for stuck-row")
        [temporary] = [path for path in cache.iterdir() if path.name.startswith(".openapi.")]
        self.assertIn(f"could not remove the partial download {temporary} for stuck-row", result.stderr)
        self.assertIn(f"delete it (rm -f {temporary}) before re-running", result.stderr)

    def test_a_directory_or_link_where_the_spec_is_published_is_refused(self) -> None:
        for label in ("directory", "link to a directory"):
            with self.subTest(label):
                name = "blocked-row" if label == "directory" else "linked-row"
                self.server.documents[f"/specs/{name}.yaml"] = b"openapi: 3.0.3\n"
                self.add_repository_row(name, self.spec_url(name), "HEAD")
                cache = self.destination(name)
                cache.mkdir(parents=True)
                if label == "directory":
                    (cache / "openapi.yaml").mkdir()
                else:
                    (cache / "elsewhere").mkdir()
                    (cache / "openapi.yaml").symlink_to(cache / "elsewhere")
                result = self.fetch(name)
                self.assert_refused_without_a_path(
                    result,
                    f"corpus: {cache / 'openapi.yaml'} is a directory or a link, not the cached spec for {name}",
                    f"(rm -rf {cache / 'openapi.yaml'})",
                )
                held = cache / ("openapi.yaml" if label == "directory" else "elsewhere")
                self.assertEqual([], list(held.iterdir()), "the document was moved inside it")

    @unittest.skipIf(os.name == "nt" or os.geteuid() == 0, "root enters a directory whatever its mode")
    def test_a_library_directory_it_cannot_enter_stops_the_pin_step_with_its_fix(self) -> None:
        library = self.root / "tools" / "corpus"
        for step in (
            'corpus_pin_apply plain-row "$2" openapi.yaml',
            "corpus_tree_root plain-row",
            'corpus_fetch_source "$2" plain-row https://example.test/openapi.yaml HEAD',
        ):
            with self.subTest(step=step):
                result = subprocess.run(
                    [
                        "bash",
                        "-c",
                        f'. "$1/corpus-lib.sh" && chmod 0 "$1" && {{ {step}; status=$?; '
                        'chmod 0755 "$1"; exit "$status"; }',
                        "bash",
                        str(library),
                        str(self.root / "document.yaml"),
                    ],
                    text=True,
                    capture_output=True,
                    encoding="utf-8",
                    check=False,
                )
                library.chmod(0o755)
                self.assertEqual(1, result.returncode, result.stderr)
                self.assertIn("corpus: cannot resolve tools/corpus/", result.stderr)
                self.assertIn("run it from a readable checkout", result.stderr)
                self.assertNotIn("corpus_remote_ref_pins.py", result.stderr, "Python was started with no script")

    def test_an_unsupported_spec_suffix_names_the_supported_ones(self) -> None:
        result = subprocess.run(
            [
                "bash",
                "-c",
                '. "$1" && corpus_spec_cache_filename "$2"',
                "bash",
                str(self.root / "tools" / "corpus" / "corpus-lib.sh"),
                "https://example.test/openapi.txt",
            ],
            text=True,
            capture_output=True,
            check=False,
        )
        self.assert_refused_without_a_path(
            result, "https://example.test/openapi.txt", ".json, .yaml or .yml", "CORPUS.md"
        )

    def test_a_second_destination_root_asks_for_exactly_one(self) -> None:
        result = self.fetch("plain-row", str(self.root / "one"), str(self.root / "two"))
        self.assert_refused_without_a_path(result, "more than one destination root", "supply exactly one DEST_ROOT")
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertEqual(self.server.requests, [])

    def test_an_invalid_fixture_name_states_the_accepted_shape(self) -> None:
        result = self.fetch("../plain-row")
        self.assert_refused_without_a_path(
            result,
            "invalid fixture name '../plain-row'",
            "letters, digits, '.', '_' and '-'",
        )
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertEqual(self.server.requests, [])

    def test_an_invalid_invocation_exits_two_with_the_usage_and_fetches_nothing(self) -> None:
        script = str(self.root / "tools" / "corpus" / "fetch-corpus.sh")
        for arguments, message in (
            (["--fixture"], "--fixture needs a name"),
            (["--sideways"], "unknown argument '--sideways'"),
            (["--if-missing"], "--if-missing requires --fixture"),
        ):
            with self.subTest(arguments=arguments):
                result = subprocess.run(
                    [script, *arguments],
                    cwd=self.root,
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    check=False,
                )
                self.assertEqual(result.returncode, 2, result.stderr)
                self.assertIn(message, result.stderr)
                self.assertIn("Exit status: 0 on success, 1 when a fetch", result.stderr)
                self.assertEqual(result.stdout, "")
        self.assertEqual(self.server.requests, [])

    def test_an_unknown_row_says_where_the_valid_rows_are_listed(self) -> None:
        self.assert_refused_without_a_path(
            self.fetch("no-such-row"),
            "'no-such-row' is not a canonical CORPUS.md row",
            "tests/fixtures/CORPUS.md",
            "--dry-run",
        )
        self.assertEqual(self.server.requests, [])

    def test_an_uncreatable_cache_directory_fails_the_fetch(self) -> None:
        self.destination("plain-row").parent.mkdir(parents=True)
        self.destination("plain-row").write_text("in the way\n", encoding="utf-8")
        self.assert_refused_without_a_path(self.fetch("plain-row"), "cannot create the cache directory", "plain-row")

    def test_an_unwritable_cache_directory_fails_before_fetching(self) -> None:
        if os.geteuid() == 0:
            self.skipTest("root writes into a read-only directory")
        directory = self.destination("plain-row")
        directory.mkdir(parents=True)
        directory.chmod(0o555)
        self.addCleanup(directory.chmod, 0o755)
        self.assert_refused_without_a_path(self.fetch("plain-row"), "cannot create a temporary file in", "writable")
        self.assertEqual(self.server.requests, [])

    def test_a_failed_publication_keeps_the_prior_cache_and_prints_no_path(self) -> None:
        directory = self.destination("plain-row")
        directory.mkdir(parents=True)
        (directory / "openapi.json").write_text("{}\n", encoding="utf-8")
        real_mv = shutil.which("mv")
        self.assertIsNotNone(real_mv)
        stubs = Path(self.temporary.name) / "failing-mv"
        stubs.mkdir()
        (stubs / "mv").write_text(
            "#!/usr/bin/env bash\n"
            'case "${@: -1}" in */openapi.yaml) echo "mv: simulated rename failure" >&2; exit 1 ;; esac\n'
            f'exec "{real_mv}" "$@"\n',
            encoding="utf-8",
        )
        (stubs / "mv").chmod(0o755)
        result = self.fetch("plain-row", PATH=f"{stubs}{os.pathsep}{os.environ['PATH']}")
        self.assert_refused_without_a_path(
            result, "mv: simulated rename failure", "could not publish the fetched spec for plain-row"
        )
        # The stale sibling is removed only after a successful publication.
        self.assert_no_leftovers("plain-row", expected={"openapi.json"})

    def test_a_stale_sibling_directory_is_cleared_once_the_spec_is_published(self) -> None:
        stale = self.destination("plain-row") / "openapi.json"
        stale.mkdir(parents=True)
        (stale / "left").write_text("a directory the cache owns\n", encoding="utf-8")
        result = self.fetch("plain-row")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assert_no_leftovers("plain-row", expected={"openapi.yaml"})

    def test_a_stale_sibling_that_cannot_be_removed_fails_the_fetch(self) -> None:
        if os.geteuid() == 0:
            self.skipTest("root removes a read-only directory's entries")
        blocking = self.destination("plain-row") / "openapi.json"
        blocking.mkdir(parents=True)
        (blocking / "keep").write_text("held by a read-only directory\n", encoding="utf-8")
        blocking.chmod(0o555)
        self.addCleanup(blocking.chmod, 0o755)
        self.assert_refused_without_a_path(
            self.fetch("plain-row"),
            "could not remove the stale cached spec",
            f"(chmod -R u+w {blocking} && rm -rf {blocking})",
        )
        self.assertTrue((blocking / "keep").exists())

    def upstream_repository(self) -> tuple[Path, str]:
        """A real local git repository standing in for a repository-source row."""
        upstream = Path(self.temporary.name) / "upstream"
        upstream.mkdir()
        (upstream / "openapi.yaml").write_bytes(self.roots["plain-row"])
        environment = {**os.environ, "GIT_CONFIG_GLOBAL": os.devnull}
        for command in (
            ["init", "-q"],
            ["add", "-A"],
            ["-c", "user.name=t", "-c", "user.email=t@example.test", "commit", "-qm", "upstream"],
        ):
            subprocess.run(["git", "-C", str(upstream), *command], env=environment, check=True)
        head = subprocess.run(
            ["git", "-C", str(upstream), "rev-parse", "HEAD"],
            text=True,
            capture_output=True,
            check=True,
        ).stdout.strip()
        return upstream, head

    def add_repository_row(self, name: str, source: str, ref: str) -> None:
        corpus = self.root / "tests" / "fixtures" / "CORPUS.md"
        corpus.write_text(
            corpus.read_text(encoding="utf-8")
            + f"| 99 | `{name}` | git | {source} | `{ref}` | MIT | link-ok | repository row |\n",
            encoding="utf-8",
        )

    def test_a_repository_row_prints_its_clone_only_once_every_git_step_succeeded(self) -> None:
        upstream, head = self.upstream_repository()
        self.add_repository_row("repo-row", str(upstream), head)
        self.add_repository_row("bad-ref-row", str(upstream), "0" * 40)
        self.add_repository_row("missing-repo-row", str(upstream.with_name("no-such-repo")), "HEAD")

        fetched = self.fetch("repo-row")
        self.assertEqual(fetched.returncode, 0, fetched.stderr)
        self.assertEqual(fetched.stdout.strip(), str(self.destination("repo-row")))
        self.assertTrue((self.destination("repo-row") / "openapi.yaml").is_file())

        with self.subTest("clone"):
            self.assert_refused_without_a_path(
                self.fetch("missing-repo-row"), "could not clone", "source URL in tests/fixtures/CORPUS.md"
            )
        with self.subTest("checkout"):
            self.assert_refused_without_a_path(
                self.fetch("bad-ref-row"), f"could not check out {'0' * 40} for bad-ref-row", "pinned ref"
            )
        with self.subTest("update"):
            upstream.rename(upstream.with_name("upstream-gone"))
            self.assert_refused_without_a_path(
                self.fetch("repo-row"),
                "could not update the cached clone of repo-row",
                f"rm -rf {self.destination('repo-row')}",
            )


if __name__ == "__main__":
    unittest.main(verbosity=0)
