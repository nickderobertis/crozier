#!/usr/bin/env python3
"""Real-CLI tests for the additive witness-search shard boundary."""

from __future__ import annotations

import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "witness-search-redo.py"
ROOT = REPO / "docs" / "openapi-surface" / "witness-search-redo"
CONTRACT = ROOT / "contract.md"
SHARDS = (ROOT / "catalogue-portals.md", ROOT / "code-platforms.md")


class WitnessSearchRedoTests(unittest.TestCase):
    def run_validator(
        self, *paths: Path, reconcile: bool = False
    ) -> subprocess.CompletedProcess[str]:
        command = [str(SCRIPT), str(CONTRACT), *(str(path) for path in paths)]
        if reconcile:
            command += [
                "--reconcile",
                "--schemas",
                str(REPO / "docs/openapi-surface/schemas.md"),
            ]
        return subprocess.run(command, cwd=REPO, capture_output=True, text=True)

    def changed(self, source: Path, old: str, new: str) -> Path:
        directory = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, directory)
        target = directory / source.name
        text = source.read_text(encoding="utf-8")
        self.assertIn(old, text)
        target.write_text(text.replace(old, new, 1), encoding="utf-8")
        return target

    def test_each_empty_shard_is_independently_valid_and_outcome_invisible(
        self,
    ) -> None:
        for shard in SHARDS:
            with self.subTest(shard=shard.name):
                result = self.run_validator(shard)
                self.assertEqual(0, result.returncode, result.stderr)

    def test_omitted_key_is_rejected(self) -> None:
        bad = self.changed(SHARDS[0], "| `anyof-sole-member` |\n", "")
        self.assertIn("owned keys omitted", self.run_validator(bad).stderr)

    def test_duplicate_missing_query_and_missing_result_are_rejected(self) -> None:
        prefix = "| `anyof-sole-member` | `schema.anyOf:sole-member` | `apis.guru` |"
        valid = (
            prefix
            + " `grep -F anyOf APIs` | 1 | candidate | commit `abc` | admitted | accepted |\n"
        )
        for suffix, message in (
            (valid + valid, "duplicate source/key"),
            (
                prefix + " — | 1 | candidate | commit `abc` | admitted | accepted |\n",
                "missing a rerunnable query",
            ),
            (
                prefix
                + " `grep -F anyOf APIs` |  | candidate | commit `abc` | admitted | accepted |\n",
                "missing a result",
            ),
        ):
            with self.subTest(message=message):
                bad = self.changed(
                    SHARDS[0],
                    "|---|---|---|---|---|---|---|---|---|\n",
                    "|---|---|---|---|---|---|---|---|---|\n" + suffix,
                )
                self.assertIn(message, self.run_validator(bad).stderr)

    def test_unanswered_cannot_be_presented_as_zero(self) -> None:
        row = "| `anyof-sole-member` | `schema.anyOf:sole-member` | `apis.guru` | `query` | 0 | unanswered | — | — | — |\n"
        bad = self.changed(
            SHARDS[0],
            "|---|---|---|---|---|---|---|---|---|\n",
            "|---|---|---|---|---|---|---|---|---|\n" + row,
        )
        self.assertIn(
            "presents zero for an unanswered source", self.run_validator(bad).stderr
        )

    def test_enabled_reconciliation_refuses_incomplete_source_key_coverage(
        self,
    ) -> None:
        result = self.run_validator(*SHARDS, reconcile=True)
        self.assertNotEqual(0, result.returncode)
        self.assertIn("missing source/key coverage", result.stderr)

    def test_enabled_reconciliation_accepts_complete_seven_source_coverage(
        self,
    ) -> None:
        keys = []
        for line in CONTRACT.read_text(encoding="utf-8").splitlines():
            if line.startswith("| `") and line.count("|") == 3:
                cells = [cell.strip().strip("`") for cell in line.split("|")[1:3]]
                keys.append(tuple(cells))
        owned = (
            (SHARDS[0], ("apis.guru", "jentic", "vendor-portals")),
            (SHARDS[1], ("sourcegraph", "github-code-search", "swaggerhub", "postman")),
        )
        completed = []
        for source, families in owned:
            records = "".join(
                f"| `{key}` | `{selector}` | `{family}` | `query {key}` | unanswered | — | — | — | — |\n"
                for key, selector in keys
                for family in families
            )
            completed.append(
                self.changed(
                    source,
                    "|---|---|---|---|---|---|---|---|---|\n",
                    "|---|---|---|---|---|---|---|---|---|\n" + records,
                )
            )
        directory = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, directory)
        schemas = directory / "schemas.md"
        schemas.write_text(
            "\n".join(f"`{key}` search outcome `search-incomplete`" for key, _ in keys),
            encoding="utf-8",
        )
        command = [
            str(SCRIPT),
            str(CONTRACT),
            *(str(path) for path in completed),
            "--reconcile",
            "--schemas",
            str(schemas),
        ]
        result = subprocess.run(command, cwd=REPO, capture_output=True, text=True)
        self.assertEqual(0, result.returncode, result.stderr)


if __name__ == "__main__":
    unittest.main()
