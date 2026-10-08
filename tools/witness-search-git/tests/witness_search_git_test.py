"""witness-search's cases that drive the real `git`: a publisher tree indexed
from a real repository's commits, and the default cache kept out of git by the
repository's own ignore rules.

They need the git host tool, so they are a project of their own; the offline
suites, and the fixtures these share, are `tools/witness-search/tests/`'s.
Run: `just nx run witness-search-git:test`.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "witness-search" / "tests"))

import witness_search_github_test as github  # noqa: E402 - the shared fixtures' directory must be on sys.path first
import witness_search_redo_test as redo  # noqa: E402 - the shared fixtures' directory must be on sys.path first

REPO = github.REPO
SEARCH = github.SEARCH
DOCUMENT = github.DOCUMENT


class ATreeIndexedFromARealRepository(redo.WideWitnessFixture, unittest.TestCase):
    """`index-tree` over a real git repository: its pins, bytes and line endings."""

    def test_index_tree_joins_every_version_to_verified_git_bytes(self) -> None:
        import hashlib
        tree = self.work / 'tree'
        tree.mkdir()
        def git(*args):
            return subprocess.run(['git', '-C', str(tree), *args], capture_output=True, errors="backslashreplace", encoding='utf-8', check=True)
        git('init', '-q')
        # The fixture represents literal publisher bytes, independent of the
        # host's Git defaults. The CRLF rejection is exercised explicitly below.
        git('config', 'core.autocrlf', 'false')
        git('config', 'user.name', 'Witness test')
        git('config', 'user.email', 'witness@example.invalid')
        path = tree / 'APIs/publisher/1/openapi.yaml'
        path.parent.mkdir(parents=True)
        path.write_bytes('openapi: 3.0.3\ninfo: {title: réel, version: 1}\npaths: {}\n'.encode('utf-8'))
        git('add', 'APIs')
        git('commit', '-qm', 'test: record publisher tree')
        pin = git('rev-parse', 'HEAD').stdout.strip()
        index = self.work / 'list.json'
        index.write_text(json.dumps({'publisher': {'versions': {
            '1': {'swaggerUrl': 'https://api.apis.guru/v2/specs/publisher/1/openapi.json', 'swaggerYamlUrl': 'https://api.apis.guru/v2/specs/publisher/1/openapi.yaml'},
            '2': {'swaggerUrl': 'https://api.apis.guru/v2/specs/publisher/2/openapi.json'}
        }}}), encoding='utf-8')
        output = self.work / 'associated.json'
        args = ('index-tree', '--index', index, '--index-sha256', hashlib.sha256(index.read_bytes()).hexdigest(),
                '--tree', tree, '--ref', pin, '--prior-ref', pin, '--local-paths', '--output', output)
        wrong_pin = list(args)
        wrong_pin[wrong_pin.index('--ref') + 1] = '0' * 40
        refused = self.cli(*wrong_pin)
        self.assertNotEqual(0, refused.returncode)
        self.assertIn('tree commit differs from the requested pin', refused.stderr)
        self.assertFalse(output.exists())
        result = self.cli(*args)
        self.assertEqual(0, result.returncode, result.stderr)
        measured = json.loads(output.read_text(encoding='utf-8'))
        self.assertEqual(1, measured['schema_version'])
        self.assertEqual(2, len(measured['sources']))
        self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), measured['sources'][0]['prior_sha256'])
        self.assertIn('absent from pinned', measured['sources'][1]['tree_diagnostic'])
        self.assertEqual(str(path.resolve()), measured['sources'][0].get('local_path'))
        local_inventory = self.work / 'local-inventory.json'
        local_inventory.write_text(json.dumps({'schema_version': 1, 'sources': [measured['sources'][0]]}), encoding='utf-8')
        local_output = self.work / 'local-acquisition.json'
        acquire = self.cli('acquire', '--inventory', local_inventory, '--cache', self.work / 'local-cache',
                           '--contract', self.report / 'keys.md', '--output', local_output, '--workers', '2')
        self.assertEqual(0, acquire.returncode, acquire.stderr)
        acquired = json.loads(local_output.read_text(encoding='utf-8'))['sources'][0]
        self.assertEqual('readable', acquired['status'])
        self.assertEqual(measured['sources'][0]['sha256'], acquired['sha256'])
        self.assertEqual(path.read_bytes(), (self.work / 'local-cache' / acquired['sha256']).read_bytes())
        self.assertTrue(local_output.with_suffix('.census.tsv').read_text(encoding='utf-8').startswith('source\tkey\tselector'))
        path.write_text('changed: bytes\n', encoding='utf-8')
        refused = self.cli(*args)
        self.assertNotEqual(0, refused.returncode)
        self.assertIn('changed bytes', refused.stderr)
        git('restore', 'APIs')
        self.assertEqual(0, self.cli(*args).returncode)
        original_bytes = path.read_bytes()
        git('config', 'core.autocrlf', 'true')
        path.write_bytes(original_bytes.replace(b'\n', b'\r\n'))
        git('diff', '--quiet', 'HEAD', '--', 'APIs')
        refused = self.cli(*args)
        self.assertNotEqual(0, refused.returncode)
        self.assertIn('changed literal bytes', refused.stderr)
        git('config', 'core.autocrlf', 'false')
        path.write_bytes(original_bytes)
        self.assertEqual(0, self.cli(*args).returncode)
        index.write_text('{}', encoding='utf-8')
        refused = self.cli(*args)
        self.assertNotEqual(0, refused.returncode)
        self.assertIn('catalogue digest changed', refused.stderr)


class TheDefaultCacheStaysIgnored(github.WitnessSearchGithubFixture, unittest.TestCase):
    """A walk without `--cache` writes where the repository's `.gitignore` keeps it out."""

    def test_cli_without_cache_keeps_fetched_documents_out_of_the_evidence_directory(self) -> None:
        """With no `--cache`, fetched bytes land in the gitignored `.local` cache, not beside the ledgers.

        The document carries this test's temporary directory name, so its digest
        names a cache file no other run writes, and that one file is removed after.
        """
        document = DOCUMENT + f"# {self.root.name}\n".encode()
        self.server.state["raw_document"] = document
        digest = hashlib.sha256(document).hexdigest()
        cached = REPO / ".local" / "witness-search-cache" / "documents" / f"{digest}.yaml"
        self.addCleanup(cached.unlink, missing_ok=True)
        evidence = self.root / "cli-default-cache"

        walked = self.walk_cli(evidence)
        self.assertEqual(0, walked.returncode, walked.stderr)
        row = json.loads((evidence / "documents.jsonl").read_text(encoding="utf-8").splitlines()[0])
        self.assertEqual(digest, row["sha256"])
        self.assertFalse((evidence / "documents").exists(), "fetched bytes were written into the evidence directory")
        self.assertEqual(document, cached.read_bytes())
        ignored = subprocess.run(["git", "check-ignore", "--quiet", str(cached)], cwd=REPO)
        self.assertEqual(0, ignored.returncode, f"{cached} is not gitignored")
        self.assertEqual(cached.parent.parent, SEARCH.DEFAULT_CACHE)


if __name__ == "__main__":
    unittest.main()
