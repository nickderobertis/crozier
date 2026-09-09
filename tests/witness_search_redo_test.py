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

    def contract_keys(self) -> list[tuple[str, str]]:
        keys = []
        for line in CONTRACT.read_text(encoding="utf-8").splitlines():
            if line.startswith("| `") and line.count("|") == 3:
                keys.append(
                    tuple(cell.strip().strip("`") for cell in line.split("|")[1:3])
                )
        return keys

    def completed_documents(self) -> tuple[list[Path], Path]:
        keys = self.contract_keys()
        owned = (
            (SHARDS[0], ("apis.guru", "jentic", "vendor-portals")),
            (SHARDS[1], ("sourcegraph", "github-code-search", "swaggerhub", "postman")),
        )
        completed = []
        for source, families in owned:
            records = "".join(
                f"| `{key}` | `{selector}` | `{family}` | `query {key} {family}` | unanswered | — | — | — | — |\n"
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
        sources = (
            "apis.guru",
            "jentic",
            "vendor-portals",
            "sourcegraph",
            "github-code-search",
            "swaggerhub",
            "postman",
        )
        schemas.write_text(
            "| key | oas | spec location | category | evidence | crozier sites | why bytes could move | settlement |\n"
            "|---|---|---|---|---|---|---|---|\n"
            + "".join(
                f"| {key} | both | Schema Object | gap | search outcome `search-incomplete`; "
                + "; ".join(
                    f"**{source}** `query {key} {source}` → `unanswered`"
                    for source in sources
                )
                + " | site | bytes | FIXTURE |\n"
                for key, _ in keys
            ),
            encoding="utf-8",
        )
        return completed, schemas

    def reconcile_documents(
        self, shards: list[Path], schemas: Path
    ) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                str(SCRIPT),
                str(CONTRACT),
                *(str(path) for path in shards),
                "--reconcile",
                "--schemas",
                str(schemas),
            ],
            cwd=REPO,
            capture_output=True,
            text=True,
        )

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
                "result must be a nonnegative integer or unanswered",
            ),
        ):
            with self.subTest(message=message):
                bad = self.changed(
                    SHARDS[0],
                    "|---|---|---|---|---|---|---|---|---|\n",
                    "|---|---|---|---|---|---|---|---|---|\n" + suffix,
                )
                self.assertIn(message, self.run_validator(bad).stderr)

    def test_invalid_result_and_positive_result_without_candidates_are_rejected(
        self,
    ) -> None:
        prefix = "| `anyof-sole-member` | `schema.anyOf:sole-member` | `apis.guru` | `query` |"
        for row, message in (
            (prefix + " many | — | — | — | — |\n", "nonnegative integer or unanswered"),
            (
                prefix + " 1 | — | commit `abc` | admitted | accepted |\n",
                "positive result is missing ['candidates']",
            ),
        ):
            with self.subTest(message=message):
                bad = self.changed(
                    SHARDS[0],
                    "|---|---|---|---|---|---|---|---|---|\n",
                    "|---|---|---|---|---|---|---|---|---|\n" + row,
                )
                self.assertIn(message, self.run_validator(bad).stderr)

    def test_enabled_reconciliation_refuses_incomplete_source_key_coverage(
        self,
    ) -> None:
        result = self.run_validator(*SHARDS, reconcile=True)
        self.assertNotEqual(0, result.returncode)
        self.assertIn("missing source/key coverage", result.stderr)

    def test_enabled_reconciliation_accepts_complete_seven_source_coverage(
        self,
    ) -> None:
        """The real region contract's bare key is found and compared successfully."""
        completed, schemas = self.completed_documents()
        result = self.reconcile_documents(completed, schemas)
        self.assertEqual(0, result.returncode, result.stderr)

    def test_reconcile_requires_an_authoritative_schemas_document(self) -> None:
        result = subprocess.run(
            [
                str(SCRIPT),
                str(CONTRACT),
                *(str(path) for path in SHARDS),
                "--reconcile",
            ],
            cwd=REPO,
            capture_output=True,
            text=True,
        )
        self.assertEqual(2, result.returncode)
        self.assertIn("--reconcile requires --schemas PATH", result.stderr)

    def test_cross_shard_duplicate_is_rejected(self) -> None:
        completed, _schemas = self.completed_documents()
        first = self.contract_keys()[0]
        duplicate = f"| `{first[0]}` | `{first[1]}` | `apis.guru` | `query duplicate` | unanswered | — | — | — | — |\n"
        completed[1] = self.changed(
            completed[1],
            "|---|---|---|---|---|---|---|---|---|\n",
            "|---|---|---|---|---|---|---|---|---|\n" + duplicate,
        )
        self.assertIn("duplicate source/key", self.run_validator(*completed).stderr)

    def test_authoritative_outcome_and_source_details_are_row_local_and_exact(
        self,
    ) -> None:
        for old, new, message in (
            (
                "search outcome `search-incomplete`",
                "search outcome `none-found`",
                "records outcome",
            ),
            (
                "**postman** `query annotated-ref-target-closed-object postman` → `unanswered`",
                "",
                "omits source details",
            ),
            (
                "`query annotated-ref-target-closed-object postman` → `unanswered`",
                "`different query` → `unanswered`",
                "mismatches postman",
            ),
        ):
            with self.subTest(message=message):
                completed, schemas = self.completed_documents()
                bad_schemas = self.changed(schemas, old, new)
                self.assertIn(
                    message, self.reconcile_documents(completed, bad_schemas).stderr
                )


if __name__ == "__main__":
    unittest.main()
