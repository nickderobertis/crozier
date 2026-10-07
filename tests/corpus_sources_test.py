# llmlint: ignore-file[new_code_lands_in_a_project] crozier uses Cargo and just rather than Nx; this boundary suite belongs to test-corpus-sources in the deterministic check.
"""Boundary coverage for the committed corpus sources.

Every registered `tests/fixtures/CORPUS.md` row's source document is committed
under `tests/fixtures/corpus-sources/`, recorded with the SHA-256 of the bytes
fetched at its pinned revision in `tests/fixtures/corpus-sources.tsv`.
`TheCommittedTreeHolds` holds the real tree to that: every row, every digest.
`TheCheckStillDiscriminates` drives the real `check` over a synthetic root
breaking each demand in turn, so a lint that had stopped discriminating fails
here. `TheOfflineCommandsRunEverywhere` runs `prepare` and the fetch's bash
resolution on every platform, Windows included. `TheRebuildToolingFetches`
drives `vendor` and `audit` through the real `scripts/fetch-corpus.sh` and real
`curl` against a loopback HTTP server this suite starts, the way
`tests/corpus_remote_ref_pins_test.py` drives the fetch itself.

Run: `just test-corpus-sources` (part of `just check`).
"""

from __future__ import annotations

import ast
import hashlib
import http.server
import os
import shutil
import subprocess
import sys
import tempfile
import threading
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "corpus_sources.py"
sys.path.insert(0, str(REPO / "scripts"))
import corpus_sources  # noqa: E402 - the production scripts directory must be on sys.path first

COPIED_SCRIPTS = (
    "corpus-lib.sh",
    "corpus_remote_ref_pins.py",
    "corpus_sources.py",
    "fetch-corpus.sh",
    "lib.sh",
    "openapi-surface-census.py",
)
RAW = "https://raw.githubusercontent.com"
PINNED_SHA = "80d0a6ee6c129a29c507c35b0245a16c5a81b9d3"
MUTABLE_URL = f"{RAW}/example/schemas/refs/heads/main/block.yaml"
PINNED_URL = f"{RAW}/example/schemas/{PINNED_SHA}/block.yaml"
BLOCK = b"block:\n  type: string\n"
PLAIN = b'{"openapi": "3.0.0", "info": {"title": "Plain", "version": "1"}, "paths": {}}\n'
REMOTE_ROOT = (
    "openapi: 3.0.0\n"
    "info:\n  title: Remote\n  version: '1'\n"
    "paths: {}\n"
    "components:\n  schemas:\n    Block:\n"
    f"      $ref: '{MUTABLE_URL}#/block'\n"
).encode("utf-8")


def run(root: Path, *args: str, **environment: str) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env.update(environment)
    return subprocess.run(
        [sys.executable, str(root / "scripts" / "corpus_sources.py"), *args],
        cwd=root, env=env, text=True, capture_output=True, check=False,
    )


class TheCommittedTreeHolds(unittest.TestCase):
    """The real tree: every row committed, every byte at its recorded digest."""

    def test_the_real_check_passes_quietly(self) -> None:
        completed = run(REPO, "check")
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertEqual("", completed.stdout + completed.stderr)

    def test_every_golden_bearing_row_is_committed_at_its_recorded_digest(self) -> None:
        records = corpus_sources.load_manifest(REPO)
        recorded = {record.corpus_name for record in records}
        aliases = dict(
            line.split("\t")
            for line in (REPO / "tests/fixtures/corpus-aliases.tsv").read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.startswith("#")
        )
        golden_rows = [
            row.name for row in corpus_sources.corpus_rows(REPO)
            if (REPO / "tests/fixtures" / aliases.get(row.name, row.name) / "expected").is_dir()
            or (REPO / "tests/fixtures" / aliases.get(row.name, row.name) / "known-fern-failure.json").is_file()
        ]
        self.assertGreater(len(golden_rows), 150, "the golden-bearing rows were not found")
        self.assertEqual([], [name for name in golden_rows if name not in recorded])
        for record in records:
            with self.subTest(path=record.path):
                measured = hashlib.sha256((REPO / record.path).read_bytes()).hexdigest()
                self.assertEqual(record.sha256, measured)

    def test_no_registered_row_is_left_fetch_only(self) -> None:
        self.assertEqual(
            [], [row.name for row in corpus_sources.corpus_rows(REPO) if row.decision != "committed"]
        )

    def test_prepared_remote_references_use_committed_files_without_changing_sources(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            staged = Path(directory)
            completed = run(REPO, "prepare", "--fixture", "helios-verifiable-api",
                            "--output", str(staged))
            self.assertEqual(0, completed.returncode, completed.stderr)
            source = Path(completed.stdout.strip())
            self.assertNotIn("https://raw.githubusercontent.com", source.read_text(encoding="utf-8"))
            self.assertTrue(list((staged / "remote").rglob("*.yaml")))
            self.assertEqual(0, run(REPO, "check").returncode)

    def test_both_manifest_readers_select_the_same_registered_sources(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [corpus_sources.bash(), str(REPO / "scripts/fetch-corpus.sh"), "--dry-run", directory],
                cwd=REPO, capture_output=True, text=True,
            )
            self.assertEqual(0, result.returncode, result.stderr)
            fetched_rows = [tuple(line.split("\t")[:2]) for line in result.stdout.splitlines()]
            self.assertEqual([(row.name, row.url) for row in corpus_sources.corpus_rows(REPO)], fetched_rows)

    def test_offline_recipe_failure_restores_the_original_cache(self) -> None:
        import importlib.util
        spec = importlib.util.spec_from_file_location("offline_cache_recovery", REPO / "tests/corpus_offline_test.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        if getattr(module.OfflineCorpusRecipes, "__unittest_skip__", False):
            self.skipTest(module.OfflineCorpusRecipes.__unittest_skip_why__)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            cache = root / ".local/corpus"
            cache.mkdir(parents=True)
            marker = cache / "original.txt"
            marker.write_text("original cached bytes", encoding="utf-8", newline="\n")
            (root / "justfile").write_text(
                "test-corpus-match:\n    mkdir -p .local/corpus/generated\n    false\n\n"
                "surface-census:\n    true\n", encoding="utf-8", newline="\n"
            )
            # The warm step fetches locked crates: give the root a package with
            # none, so it succeeds offline and the failing recipe is reached.
            (root / "Cargo.toml").write_text('[package]\nname = "synthetic"\nversion = "0.0.0"\n', encoding="utf-8", newline="\n")
            (root / "src").mkdir()
            (root / "src/lib.rs").write_text("", encoding="utf-8", newline="\n")
            subprocess.run(["cargo", "generate-lockfile", "--offline"], cwd=root, check=True,
                           capture_output=True)
            tests = root / "tests"
            tests.mkdir()
            script = tests / "corpus_offline_test.py"
            shutil.copy2(REPO / "tests/corpus_offline_test.py", script)
            completed = subprocess.run(
                [sys.executable, str(script), "OfflineCorpusRecipes.test_real_recipes_without_network_or_cache"],
                cwd=root, capture_output=True, text=True,
            )
            self.assertEqual(1, completed.returncode, completed.stdout + completed.stderr)
            self.assertIn("mkdir -p .local/corpus/generated", completed.stderr)
            self.assertNotIn("Directory not empty", completed.stderr)
            self.assertEqual("original cached bytes", marker.read_text(encoding="utf-8"))
            self.assertFalse((cache / "generated").exists())

    def test_prepare_rejects_unsafe_names(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            completed = run(REPO, "prepare", "--fixture", "../outside-source", "--output", directory)
            self.assertEqual(1, completed.returncode)
            self.assertIn("unsafe fixture name", completed.stderr)

    def test_prepare_refuses_a_missing_source_with_recovery_guidance(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            completed = run(REPO, "prepare", "--fixture", "no-such-corpus",
                            "--output", directory)
            self.assertEqual(1, completed.returncode)
            self.assertIn("just lint-corpus-sources", completed.stderr)


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802 - http.server's spelling
        self.server.requests.append(self.path)
        body = self.server.documents.get(self.path)
        if body is None:
            self.send_error(404)
            return
        self.send_response(200)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args: object) -> None:
        """Quiet: the request log is the assertion surface."""


class SyntheticRoot(unittest.TestCase):
    """A repository root with two rows: one plain document, one with a remote-ref pin."""

    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name) / "repo"
        (self.root / "scripts").mkdir(parents=True)
        self.fixtures = self.root / "tests" / "fixtures"
        self.fixtures.mkdir(parents=True)
        for script in COPIED_SCRIPTS:
            shutil.copy2(REPO / "scripts" / script, self.root / "scripts" / script)
        shutil.copy2(REPO / "tests/fixtures/corpus-aliases.tsv", self.fixtures / "corpus-aliases.tsv")

        self.server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        self.server.requests = []
        self.server.documents = {
            "/specs/plain.json": PLAIN,
            "/specs/remote.yaml": REMOTE_ROOT,
            f"/example/schemas/{PINNED_SHA}/block.yaml": BLOCK,
        }
        self.origin = "http://{}:{}".format(*self.server.server_address[:2])
        thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(thread.join)
        self.addCleanup(self.server.server_close)
        self.addCleanup(self.server.shutdown)
        self.write_corpus("committed")
        (self.fixtures / "corpus-remote-ref-pins.tsv").write_text(
            "# Synthetic pins.\n"
            f"remote\t{MUTABLE_URL}\t{PINNED_URL}\t{hashlib.sha256(BLOCK).hexdigest()}\n",
            encoding="utf-8", newline="\n",
        )

    def write_corpus(self, decision: str, *, extra: str = "", remote: bool = True) -> None:
        remote_row = f"| 2 | `remote` | test | {self.origin}/specs/remote.yaml | `HEAD` | MIT | committed | remote |\n"
        (self.fixtures / "CORPUS.md").write_text(
            "# Corpus\n\n"
            "| # | name | method | source | pinned ref | license | decision | shapes |\n"
            "|---:|---|---|---|---|---|---|---|\n"
            f"| 1 | `plain` | test | {self.origin}/specs/plain.json | `HEAD` | MIT | {decision} | plain |\n"
            f"{remote_row if remote else ''}{extra}",
            encoding="utf-8", newline="\n",
        )

    def commit_plain_without_fetching(self) -> None:
        """Commit the `plain` row from a completed fetch, so no bash or curl runs."""
        self.write_corpus("committed", remote=False)
        fetched = self.root / "fetched"
        (fetched / "plain").mkdir(parents=True)
        (fetched / "plain" / "openapi.json").write_bytes(PLAIN)
        completed = self.vendor("--fixture", "plain", "--from", str(fetched))
        self.assertEqual(0, completed.returncode, completed.stderr)

    def vendor(self, *args: str) -> subprocess.CompletedProcess[str]:
        return run(self.root, "vendor", *args, CROZIER_CORPUS_PIN_ORIGIN=self.origin)

    def audit(self, *args: str) -> subprocess.CompletedProcess[str]:
        return run(self.root, "audit", *args, CROZIER_CORPUS_PIN_ORIGIN=self.origin)

    def committed(self, relative: str) -> Path:
        return self.fixtures / "corpus-sources" / relative

    def assert_refused(self, completed: subprocess.CompletedProcess[str], *needles: str) -> None:
        self.assertNotEqual(0, completed.returncode, "the command should have failed")
        for needle in needles:
            self.assertIn(needle, completed.stderr)


class TheOfflineCommandsRunEverywhere(SyntheticRoot):
    """`prepare` and the fetch's preflight, which run without the POSIX fetch scripts."""

    def test_prepare_rejects_malformed_aliases(self) -> None:
        self.commit_plain_without_fetching()
        (self.fixtures / "corpus-aliases.tsv").write_text("broken-row\n", encoding="utf-8", newline="\n")
        completed = run(self.root, "prepare", "--fixture", "plain",
                        "--output", str(self.root / "staged"))
        self.assertEqual(1, completed.returncode)
        self.assertIn("invalid alias", completed.stderr)
        self.assertNotIn("Traceback", completed.stderr)

    def test_prepare_reports_missing_bytes_without_a_traceback(self) -> None:
        self.commit_plain_without_fetching()
        self.committed("plain/openapi.json").unlink()
        completed = run(self.root, "prepare", "--fixture", "plain",
                        "--output", str(self.root / "staged"))
        self.assertEqual(1, completed.returncode)
        self.assertIn("just lint-corpus-sources", completed.stderr)
        self.assertNotIn("Traceback", completed.stderr)

    def test_vendor_without_bash_on_path_names_it(self) -> None:
        empty = self.root / "no-bash"
        empty.mkdir()
        completed = run(self.root, "vendor", "--fixture", "plain", PATH=str(empty))
        self.assert_refused(completed, "no bash on PATH", "Git Bash on Windows")
        self.assertNotIn("Traceback", completed.stderr)
        self.assertEqual([], self.server.requests)

    def test_no_subprocess_runs_a_bare_bash(self) -> None:
        """A bare `bash` argv is WSL's launcher on Windows; resolve it with `corpus_sources.bash()`."""
        for path in (SCRIPT, Path(__file__).resolve()):
            for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
                if isinstance(node, ast.List) and node.elts and isinstance(node.elts[0], ast.Constant):
                    with self.subTest(path=path.name, line=node.lineno):
                        self.assertNotEqual("bash", node.elts[0].value)


@unittest.skipIf(os.name == "nt", "the corpus fetch scripts run on Linux/macOS")
class TheRebuildToolingFetches(SyntheticRoot):
    """`vendor` and `audit` through the real fetch, real curl and a loopback server."""

    def test_vendor_commits_every_resolved_file_with_its_fetched_digest(self) -> None:
        completed = self.vendor()
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertEqual(PLAIN, self.committed("plain/openapi.json").read_bytes())
        published = self.committed("remote/openapi.yaml").read_bytes()
        self.assertIn(PINNED_URL.encode("utf-8"), published)
        self.assertNotIn(MUTABLE_URL.encode("utf-8"), published)
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
            [corpus_sources.bash(), str(self.root / "scripts/fetch-corpus.sh"), "--fixture", "plain", str(fetched)],
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
        self.committed("plain/notes.txt").write_text("stray\n", encoding="utf-8", newline="\n")
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
        corpus.write_text(corpus.read_text(encoding="utf-8").replace("| committed | plain |", "| withdrawn | plain |"), encoding="utf-8", newline="\n")
        self.assert_refused(self.check(), "plain: recorded in tests/fixtures/corpus-sources.tsv but is no canonical CORPUS.md row")

    def test_a_pinned_remote_document_left_uncommitted_is_refused(self) -> None:
        manifest = self.fixtures / "corpus-sources.tsv"
        manifest.write_text(
            "".join(line for line in manifest.read_text(encoding="utf-8").splitlines(keepends=True) if "block.yaml" not in line),
            encoding="utf-8", newline="\n",
        )
        shutil.rmtree(self.committed("remote/remote"))
        self.assert_refused(self.check(), f"remote: remote/raw.githubusercontent.com/example/schemas/{PINNED_SHA}/block.yaml is not committed")

    def test_a_record_disagreeing_with_the_pin_manifest_is_refused(self) -> None:
        pins = self.fixtures / "corpus-remote-ref-pins.tsv"
        pins.write_text(pins.read_text(encoding="utf-8").replace(hashlib.sha256(BLOCK).hexdigest(), "0" * 64), encoding="utf-8", newline="\n")
        self.assert_refused(self.check(), "corpus-remote-ref-pins.tsv pins " + "0" * 64)

    def test_manifest_structure_refuses_each_malformed_record(self) -> None:
        manifest = self.fixtures / "corpus-sources.tsv"
        original = manifest.read_text(encoding="utf-8")
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
                manifest.write_text(body, encoding="utf-8", newline="\n")
                self.assert_refused(self.check(), diagnostic)
        manifest.write_text(original, encoding="utf-8", newline="\n")
        self.assertEqual(0, self.check().returncode)

    def test_prepare_refuses_duplicate_aliases_and_nonempty_staging(self) -> None:
        aliases = self.fixtures / "corpus-aliases.tsv"
        original = aliases.read_text(encoding="utf-8")
        aliases.write_text("plain\tone\nplain\ttwo\n", encoding="utf-8", newline="\n")
        completed = run(self.root, "prepare", "--fixture", "plain", "--output", str(self.root / "staged"))
        self.assert_refused(completed, "duplicate alias")
        aliases.write_text(original, encoding="utf-8", newline="\n")
        staging = self.root / "staged"
        staging.mkdir()
        (staging / "keep.txt").write_text("keep", encoding="utf-8", newline="\n")
        completed = run(self.root, "prepare", "--fixture", "plain", "--output", str(staging))
        self.assert_refused(completed, "use a fresh directory")
        self.assertEqual("keep", (staging / "keep.txt").read_text(encoding="utf-8"))

    def test_unsafe_registered_names_are_refused_before_rebuild(self) -> None:
        corpus = self.fixtures / "CORPUS.md"
        corpus.write_text(corpus.read_text(encoding="utf-8").replace("`plain`", "`../outside`"), encoding="utf-8", newline="\n")
        self.assert_refused(self.vendor(), "unsafe corpus name")
        self.assertEqual(PLAIN, self.committed("plain/openapi.json").read_bytes())

    def test_prepare_refuses_forged_remote_provenance(self) -> None:
        manifest = self.fixtures / "corpus-sources.tsv"
        original = manifest.read_text(encoding="utf-8")
        for url in ("", "https://wrong.example/schema.yaml"):
            with self.subTest(url=url):
                lines = original.splitlines()
                for index, line in enumerate(lines):
                    if "\t" + PINNED_URL + "\t" in line:
                        cells = line.split("\t")
                        cells[2] = url
                        lines[index] = "\t".join(cells)
                manifest.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
                completed = run(self.root, "prepare", "--fixture", "remote",
                                "--output", str(self.root / "stage"))
                self.assert_refused(completed, "provenance disagrees")
                self.assertFalse((self.root / "stage").exists())
        manifest.write_text(original, encoding="utf-8", newline="\n")

    def test_a_malformed_digest_is_refused(self) -> None:
        manifest = self.fixtures / "corpus-sources.tsv"
        text = manifest.read_text(encoding="utf-8")
        digest = hashlib.sha256(PLAIN).hexdigest()
        manifest.write_text(text.replace(digest, digest.upper()), encoding="utf-8", newline="\n")
        self.assert_refused(self.check(), "is not 64 lowercase hexadecimal characters")

    def test_a_path_outside_its_row_is_refused(self) -> None:
        manifest = self.fixtures / "corpus-sources.tsv"
        text = manifest.read_text(encoding="utf-8")
        manifest.write_text(text.replace("corpus-sources/plain/openapi.json", "corpus-sources/remote/../plain/openapi.json"), encoding="utf-8", newline="\n")
        self.assert_refused(self.check(), "is not a file under tests/fixtures/corpus-sources/plain/")


if __name__ == "__main__":
    unittest.main()
