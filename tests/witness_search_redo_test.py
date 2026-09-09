#!/usr/bin/env python3
"""Real-CLI tests for the additive witness-search shard boundary."""

from __future__ import annotations

import csv
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "witness-search-redo.py"
ROOT = REPO / "docs" / "openapi-surface" / "witness-search-redo"
CONTRACT = ROOT / "contract.md"
DECLARERS = ROOT / "catalogue-portals-declarers.tsv"
SHARDS = (ROOT / "catalogue-portals.md", ROOT / "code-platforms.md")


class WitnessSearchRedoTests(unittest.TestCase):
    def run_validator(
        self, *paths: Path, reconcile: bool = False
    ) -> subprocess.CompletedProcess[str]:
        command = [
            sys.executable,
            str(SCRIPT),
            str(CONTRACT),
            *(str(path) for path in paths),
        ]
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
            directory = Path(tempfile.mkdtemp())
            self.addCleanup(shutil.rmtree, directory)
            target = directory / source.name
            text = source.read_text(encoding="utf-8")
            separator = "|---|---|---|---|---|---|---|---|---|\n"
            self.assertIn(separator, text)
            before, existing = text.split(separator, 1)
            appendix = existing.find("\n## ")
            suffix = existing[appendix:] if appendix >= 0 else ""
            target.write_text(before + separator + records + suffix, encoding="utf-8")
            completed.append(target)
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
                sys.executable,
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

    def test_each_shard_is_independently_valid_and_outcome_invisible(
        self,
    ) -> None:
        for shard in SHARDS:
            with self.subTest(shard=shard.name):
                result = self.run_validator(shard)
                self.assertEqual(0, result.returncode, result.stderr)

    def test_catalogue_report_covers_every_owned_key_and_source(self) -> None:
        result = self.run_validator(SHARDS[0])
        self.assertEqual(0, result.returncode, result.stderr)
        text = SHARDS[0].read_text(encoding="utf-8").split("## Records", 1)[1]
        text = text.split("\n## ", 1)[0]
        rows = {
            (cells[0].strip("`"), cells[2].strip("`"))
            for line in text.splitlines()
            if line.startswith("| `")
            for cells in ([cell.strip() for cell in line.strip("|").split("|")],)
        }
        expected = {
            (key, source)
            for key, _selector in self.contract_keys()
            for source in ("apis.guru", "jentic", "vendor-portals")
        }
        self.assertEqual(expected, rows)

    def test_local_census_drives_real_documents_and_reports_bad_input(self) -> None:
        directory = Path(tempfile.mkdtemp(prefix="witness census "))
        self.addCleanup(shutil.rmtree, directory)
        for name in ("first.json", "second.json"):
            (directory / name).write_text(
                json.dumps(
                    {
                        "openapi": "3.1.0",
                        "info": {"title": name, "version": "1"},
                        "paths": {},
                        "components": {
                            "schemas": {"Witness": {"anyOf": [{"type": "string"}]}}
                        },
                    }
                ),
                encoding="utf-8",
            )
        (directory / "third.yaml").write_text(
            "openapi: 3.1.0\ninfo: {title: YAML witness, version: '1'}\n"
            "paths: {}\ncomponents:\n  schemas:\n    Witness:\n"
            "      anyOf:\n        - type: string\n",
            encoding="utf-8",
        )
        command = [
            "just",
            "witness-search-local-census",
            "--workers",
            "8",
            "--contract",
            str(CONTRACT),
            "--documents",
            f"test={directory}",
        ]
        result = subprocess.run(command, cwd=REPO, capture_output=True, text=True)
        self.assertEqual(0, result.returncode, result.stderr)
        rows = list(csv.DictReader(result.stdout.splitlines(), dialect="excel-tab"))
        hits = {
            row["document"]
            for row in rows
            if row["key"] == "anyof-sole-member" and int(row["count"]) > 0
        }
        self.assertEqual({"first.json", "second.json", "third.yaml"}, hits)

        (directory / "broken.json").write_text("{", encoding="utf-8")
        bad = subprocess.run(command, cwd=REPO, capture_output=True, text=True)
        self.assertNotEqual(0, bad.returncode)
        self.assertIn("test/broken.json", bad.stderr)

    def test_local_census_rejects_invalid_arguments_and_contracts(self) -> None:
        directory = Path(tempfile.mkdtemp(prefix="witness census "))
        self.addCleanup(shutil.rmtree, directory)
        empty = directory / "empty.md"
        empty.write_text("No contract rows.\n", encoding="utf-8")
        malformed = directory / "malformed.md"
        malformed.write_text("| `key` | `unknown.selector` |\n", encoding="utf-8")
        duplicate = directory / "duplicate.md"
        duplicate.write_text("| `key` | `schema.type` |\n" * 2, encoding="utf-8")
        empty_key = directory / "empty-key.md"
        empty_key.write_text("| `` | `schema.type` |\n", encoding="utf-8")
        for args, diagnostic in (
            (["--workers", "0"], "--workers must be positive"),
            (["--documents", "missing-equals"], "--documents must be SOURCE=DIR"),
            (["--documents", f"={directory}"], "--documents must be SOURCE=DIR"),
            (["--documents", "test="], "--documents must be SOURCE=DIR"),
            (
                ["--documents", f"test={directory / 'missing'}"],
                "--documents must be SOURCE=DIR",
            ),
            (["--contract", str(directory / "missing.md")], "invalid --contract"),
            (["--contract", str(directory)], "invalid --contract"),
            (["--contract", str(empty)], "no key/selector rows"),
            (["--contract", str(malformed)], "invalid --contract"),
            (["--contract", str(duplicate)], "empty or duplicate contract key"),
            (["--contract", str(empty_key)], "empty or duplicate contract key"),
        ):
            with self.subTest(args=args):
                result = subprocess.run(
                    [
                        "just",
                        "witness-search-local-census",
                        "--contract",
                        str(CONTRACT),
                        "--documents",
                        f"test={directory}",
                        *args,
                    ],
                    cwd=REPO,
                    capture_output=True,
                    text=True,
                )
                self.assertNotEqual(0, result.returncode)
                self.assertIn(diagnostic, result.stderr)
                self.assertNotIn("Traceback", result.stderr)
                self.assertEqual("", result.stdout)

    def test_every_measured_declarer_appears_in_the_report(self) -> None:
        with DECLARERS.open(encoding="utf-8", newline="") as handle:
            declarers = {
                (row["source"], row["key"], row["document"], row["count"])
                for row in csv.DictReader(handle, dialect="excel-tab")
            }
        report = SHARDS[0].read_text(encoding="utf-8")
        actual = set()
        for heading, source in (
            ("## Appendix A", "apis.guru"),
            ("## Appendix B", "jentic"),
            ("## Appendix C", "vendor-portals"),
        ):
            section = report.split(heading, 1)[1].split("\n## ", 1)[0]
            for line in section.splitlines():
                match = re.match(
                    r"^- `([^`]+)` — `([^`]+)`(?: at `[^`]+`)? — (\d+) declaration\(s\):",
                    line,
                )
                if match:
                    actual.add((source, *match.groups()))
        self.assertEqual(declarers, actual)

    def test_jentic_dispositions_carry_artifact_specific_trace_evidence(self) -> None:
        report = SHARDS[0].read_text(encoding="utf-8")
        section = report.split("## Appendix B", 1)[1].split("\n## ", 1)[0]
        rows = [line for line in section.splitlines() if line.startswith("- `")]
        self.assertEqual(681, len(rows))
        for row in rows:
            self.assertIn("artifact SHA-256", row)
            self.assertTrue(
                "pinned import trace" in row or "pinned `apis.json`" in row,
                row,
            )
        self.assertNotRegex(
            section,
            r"jentic-public-apis/[0-9a-f]{40}/openapi/",
        )
        self.assertIn(
            "jentic-public-apis/eb9d12a2684b0fbcb5aecf51e8ae54dba0929743/apis/openapi/stripe.com/",
            section,
        )
        self.assertIn(
            "stripe/openapi/refs/heads/master/openapi/spec3.json",
            section,
        )
        self.assertIn("discarded at Fern acceptance: check exit 1", section)
        self.assertIn("Fern acceptance screen incomplete, not rejected", section)
        self.assertNotIn(
            "check remained CPU-active for more than 22 minutes without a result",
            section,
        )
        self.assertNotIn("named declaring components", section)
        self.assertIn("generated-model evidence retained", section)
        self.assertIn("losing the declared `additionalProperties: false`", section)
        self.assertIn(
            "publisher relationship traced through the APIs.guru origin",
            section,
        )
        self.assertNotIn(
            "source artifact to third-party `https://api.apis.guru",
            section,
        )

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
        completed, schemas = self.completed_documents()
        complete = self.reconcile_documents(completed, schemas)
        self.assertEqual(0, complete.returncode, complete.stderr)
        row = next(
            line
            for line in completed[0]
            .read_text(encoding="utf-8")
            .splitlines(keepends=True)
            if line.startswith("| `anyof-sole-member` | `schema.anyOf:sole-member` |")
        )
        completed[0] = self.changed(completed[0], row, "")
        result = self.reconcile_documents(completed, schemas)
        self.assertNotEqual(0, result.returncode)
        self.assertIn("missing source/key coverage", result.stderr)

    def test_enabled_reconciliation_accepts_complete_seven_source_coverage(
        self,
    ) -> None:
        """The real region contract's bare key is found and compared successfully."""
        completed, schemas = self.completed_documents()
        result = self.reconcile_documents(completed, schemas)
        self.assertEqual(0, result.returncode, result.stderr)

    def test_catalogue_candidates_are_reconciled_once_with_all_four_screens(self) -> None:
        report = SHARDS[0].read_text(encoding="utf-8")
        expected: dict[str, set[str]] = {}
        for key, artifact in re.findall(r"^- `([^`]+)` — `([^`]+)`", report, re.M):
            expected.setdefault(artifact, set()).add(key)
        text = (ROOT / "candidates.md").read_text(encoding="utf-8")
        section = text.split("## Catalogue and portal artifacts", 1)[1]
        section = section.split("## Code-platform artifacts", 1)[0]
        actual = {}
        for line in section.splitlines():
            if not line.startswith("| `"):
                continue
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            self.assertEqual(8, len(cells))
            artifact = cells[0].strip("`")
            self.assertNotIn(artifact, actual)
            actual[artifact] = set(re.findall(r"`([^`]+)`", cells[1]))
            self.assertTrue(all(cells[index] for index in range(2, 6)))
            self.assertIn(cells[6].strip("`"), {
                "witness-found", "witness-blocked", "fern-rejected", "search-incomplete"
            })
            if "attentivemobile.com" in artifact:
                self.assertEqual("`search-incomplete`", cells[6])
                self.assertIn("no completed check", cells[4])
            if artifact in {"asana.com/1.0", "box.com/2.0.0"}:
                self.assertEqual("`fern-rejected`", cells[6])
                self.assertIn("17" if artifact.startswith("asana") else "25", cells[7])
        self.assertEqual(expected, actual)

    def test_previously_rejected_specs_keep_one_matching_disposition(self) -> None:
        instructions = (REPO / "tests/fixtures/AGENTS.md").read_text(encoding="utf-8")
        rejected = instructions.split("### Specs already tried and REJECTED", 1)[1]
        rejected = rejected.split("\n## ", 1)[0]
        candidates = (ROOT / "candidates.md").read_text(encoding="utf-8")
        recorded: dict[str, list[list[str]]] = {}
        for line in candidates.splitlines():
            if line.startswith("| `"):
                cells = [cell.strip() for cell in line.strip("|").split("|")]
                recorded.setdefault(cells[0].strip("`"), []).append(cells)
        count = 0
        for line in rejected.splitlines():
            if not line.startswith("| `"):
                continue
            label, source, diagnostic = (
                cell.strip() for cell in line.strip("|").split("|")
            )
            catalogue = re.search(r"api-guru `([^`]+)`", label)
            artifact = catalogue[1] if catalogue else source.strip("`")
            with self.subTest(spec=label):
                rows = recorded.get(artifact, [])
                self.assertEqual(1, len(rows), f"{artifact}: expected exactly one record")
                self.assertEqual("`fern-rejected`", rows[0][6])
                self.assertIn(
                    diagnostic.replace("../../docs/", "../../"), rows[0][7]
                )
            count += 1
        self.assertGreater(count, 0, "rejected-spec source table must not be empty")

    def test_committed_reports_reconcile_with_authoritative_rows(self) -> None:
        result = self.run_validator(*SHARDS, reconcile=True)
        self.assertEqual(0, result.returncode, result.stderr)

    def test_seven_zero_answers_allow_absence_but_one_unanswered_forbids_it(self) -> None:
        shards, schemas = self.completed_documents()
        for path in shards:
            path.write_text(path.read_text().replace("| unanswered |", "| 0 |"))
        schemas.write_text(
            schemas.read_text()
            .replace("→ `unanswered`", "→ 0")
            .replace("search outcome `search-incomplete`", "search outcome `none-found`")
        )
        result = self.reconcile_documents(shards, schemas)
        self.assertEqual(0, result.returncode, result.stderr)
        shards[0].write_text(shards[0].read_text().replace("| 0 |", "| unanswered |", 1))
        schemas.write_text(schemas.read_text().replace("→ 0", "→ `unanswered`", 1))
        refused = self.reconcile_documents(shards, schemas)
        self.assertNotEqual(0, refused.returncode)
        self.assertIn("expected 'search-incomplete'", refused.stderr)
        schemas.write_text(
            schemas.read_text().replace("search outcome `none-found`", "search outcome `search-incomplete`", 1)
        )
        recovered = self.reconcile_documents(shards, schemas)
        self.assertEqual(0, recovered.returncode, recovered.stderr)

    def test_reconcile_requires_an_authoritative_schemas_document(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
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
