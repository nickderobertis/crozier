"""Boundary coverage for the committed corpus sources.

Every registered `tests/fixtures/CORPUS.md` row's source document is committed
under `tests/fixtures/corpus-sources/`, recorded with the SHA-256 of the bytes
fetched at its pinned revision in `tests/fixtures/corpus-sources.tsv`.
`TheCommittedTreeHolds` holds the real tree to that: every row, every digest.
`TheOfflineCommandsRunEverywhere` runs `prepare` and the fetch's bash
resolution on every platform, Windows included, over a synthetic root whose
loopback server must see no request. The suites that fetch through real `curl`
are `tools/corpus-fetch/tests/corpus_sources_fetch_test.py`, which imports the
synthetic root from here.

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

REPO = Path(__file__).resolve().parents[3]
SCRIPT = REPO / "tools" / "corpus" / "corpus_sources.py"
sys.path.insert(0, str(SCRIPT.parent))
import corpus_sources  # noqa: E402 - the production script's directory must be on sys.path first

# Repository-relative, and copied to the same path under the synthetic root, so
# each script finds its neighbours where the real tree keeps them.
COPIED_SCRIPTS = (
    "tools/corpus/corpus-lib.sh",
    "tools/corpus/corpus_remote_ref_pins.py",
    "tools/corpus/corpus_sources.py",
    "tools/corpus/fetch-corpus.sh",
    "scripts/lib.sh",
    "tools/surface-census/openapi-surface-census.py",
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
).encode()


def run(root: Path, *args: str, **environment: str) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env.update(environment)
    return subprocess.run(
        [sys.executable, str(root / "tools" / "corpus" / "corpus_sources.py"), *args],
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
            self.assertNotIn("https://raw.githubusercontent.com", source.read_text())
            self.assertTrue(list((staged / "remote").rglob("*.yaml")))
            self.assertEqual(0, run(REPO, "check").returncode)

    def test_both_manifest_readers_select_the_same_registered_sources(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [corpus_sources.bash(), str(REPO / "tools/corpus/fetch-corpus.sh"), "--dry-run", directory],
                cwd=REPO, capture_output=True, text=True,
            )
            self.assertEqual(0, result.returncode, result.stderr)
            fetched_rows = [tuple(line.split("\t")[:2]) for line in result.stdout.splitlines()]
            self.assertEqual([(row.name, row.url) for row in corpus_sources.corpus_rows(REPO)], fetched_rows)

    def test_prepare_rejects_unsafe_names(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            completed = run(REPO, "prepare", "--fixture", "../exhaustive", "--output", directory)
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
            (self.root / script).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(REPO / script, self.root / script)
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
            encoding="utf-8",
        )

    def write_corpus(self, decision: str, *, extra: str = "", remote: bool = True) -> None:
        remote_row = f"| 2 | `remote` | test | {self.origin}/specs/remote.yaml | `HEAD` | MIT | committed | remote |\n"
        (self.fixtures / "CORPUS.md").write_text(
            "# Corpus\n\n"
            "| # | name | method | source | pinned ref | license | decision | shapes |\n"
            "|---:|---|---|---|---|---|---|---|\n"
            f"| 1 | `plain` | test | {self.origin}/specs/plain.json | `HEAD` | MIT | {decision} | plain |\n"
            f"{remote_row if remote else ''}{extra}",
            encoding="utf-8",
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
        (self.fixtures / "corpus-aliases.tsv").write_text("broken-row\n", encoding="utf-8")
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

    @unittest.skipIf(os.name == "nt" or os.geteuid() == 0, "file modes do not deny this reader")
    def test_fetch_refuses_an_unreadable_manifest_rather_than_fetching_nothing(self) -> None:
        manifest = self.fixtures / "CORPUS.md"
        manifest.chmod(0)
        self.addCleanup(manifest.chmod, 0o644)
        completed = subprocess.run(
            [corpus_sources.bash(), str(self.root / "tools/corpus/fetch-corpus.sh"), "--dry-run"],
            cwd=self.root, capture_output=True, text=True, check=False,
        )
        self.assert_refused(completed, f"could not read the numbered rows of {manifest}",
                            "git checkout -- tests/fixtures/CORPUS.md")
        self.assertEqual("", completed.stdout)
        self.assertEqual([], self.server.requests)

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


if __name__ == "__main__":
    unittest.main()
