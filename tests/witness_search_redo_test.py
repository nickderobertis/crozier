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
        return subprocess.run(command, cwd=REPO, capture_output=True, text=True, encoding="utf-8")

    def changed(self, source: Path, old: str, new: str) -> Path:
        directory = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, directory)
        target = directory / source.name
        candidate = source.parent / "candidates.md"
        if source.name == "schemas.md" and candidate.is_file():
            shutil.copyfile(candidate, directory / "candidates.md")
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
        (schemas.parent / "candidates.md").write_text("# Candidate screens\n", encoding="utf-8")
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
                "--candidates",
                str(schemas.parent / "candidates.md"),
            ],
            cwd=REPO,
            capture_output=True,
            text=True, encoding="utf-8",
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
        result = subprocess.run(command, cwd=REPO, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(0, result.returncode, result.stderr)
        rows = list(csv.DictReader(result.stdout.splitlines(), dialect="excel-tab"))
        hits = {
            row["document"]
            for row in rows
            if row["key"] == "anyof-sole-member" and int(row["count"]) > 0
        }
        self.assertEqual({"first.json", "second.json", "third.yaml"}, hits)

        (directory / "broken.json").write_text("{", encoding="utf-8")
        bad = subprocess.run(command, cwd=REPO, capture_output=True, text=True, encoding="utf-8")
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
                    text=True, encoding="utf-8",
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

    @staticmethod
    def document_rows(text: str) -> list[list[str]]:
        return [
            [cell.strip().strip("`") for cell in line.strip("|").split("|")]
            for line in text.splitlines()
            if line.startswith("| `")
        ]

    def test_code_platform_candidate_screens_match_source_records(self) -> None:
        source = self.document_rows(SHARDS[1].read_text(encoding="utf-8"))
        source = [row for row in source if len(row) == 9 and row[4].isdigit() and int(row[4])]
        candidates = (ROOT / "candidates.md").read_text(encoding="utf-8")
        section = candidates.split("## Code-platform artifacts", 1)[1]
        rows = self.document_rows(section.split("## Previously rejected specs", 1)[0])
        self.assertTrue(rows)
        covered: dict[int, set[str]] = {}
        for row in rows:
            artifact, keys, redistribution, publisher, fern, retention, verdict, evidence = row
            pin = re.search(r"[0-9a-f]{40}", artifact)
            self.assertIsNotNone(pin, artifact)
            filename = artifact.split(" at ", 1)[0].split()[-1] if " at " in artifact else artifact.rsplit("/", 1)[1]
            matches = [
                (index, record) for index, record in enumerate(source)
                if pin[0] in record[6] and filename in record[5]
                and ((record[6].startswith("immutable commits:")
                      and (not artifact.startswith("ballerina-platform/")
                           or artifact.rsplit("/", 2)[1].lower() in record[5].lower()))
                     or (not record[6].startswith("immutable commits:")
                         and artifact.split("@", 1)[1] in record[6]))
            ]
            self.assertTrue(matches, artifact)
            self.assertEqual(
                {record[0] for _, record in matches},
                set(re.findall(r"[a-z][a-z0-9-]+", keys)),
                artifact,
            )
            for index, record in matches:
                covered.setdefault(index, set()).add(artifact)
                # The multi-document GitHub result only screened its best survivor.
                grouped = record[6].startswith("immutable commits:")
                accepted = "check exit 0" in record[8] and (not grouped or artifact.startswith("paypal/"))
                refused = "check exit 1" in record[8]
                expected = "witness-found" if accepted else "fern-rejected" if refused else "witness-blocked"
                self.assertEqual(expected, verdict, artifact)
                if accepted:
                    self.assertTrue(all(cell.startswith("passed:") for cell in row[2:6]), artifact)
                    count = re.search(r"(\d+) files", record[8])[1]
                    self.assertIn(f"{count} files", fern)
                    for version in re.findall(r"\b5\.\d+\.\d+\b", record[8]):
                        self.assertIn(version, fern)
                    models = re.findall(r"\b(?:FourHundred\w+|Auth\w+Payload)\b", record[8])
                    self.assertTrue(models)
                    for model in models:
                        self.assertIn(model, retention + evidence)
                elif refused:
                    self.assertTrue(redistribution.startswith("passed:"))
                    self.assertTrue(publisher.startswith("passed:"))
                    self.assertTrue(fern.startswith("refused:"))
                    self.assertEqual("not reached", retention)
                    diagnostic = record[8].split(": ", 1)[1].split(";", 1)[0]
                    self.assertIn(diagnostic, fern)
                else:
                    self.assertTrue("blocked:" in redistribution or "blocked:" in publisher)
                    self.assertEqual("not reached", fern)
                    self.assertEqual("not reached", retention)
        self.assertEqual(set(range(len(source))), set(covered))
        for index, record in enumerate(source):
            expected_count = len(record[5].split(";")) if record[6].startswith("immutable commits:") else 1
            self.assertEqual(expected_count, len(covered[index]), record[5])

    def test_registration_choices_match_candidate_proof(self) -> None:
        candidates = self.document_rows((ROOT / "candidates.md").read_text(encoding="utf-8"))
        schemas = (REPO / "docs/openapi-surface/schemas.md").read_text(encoding="utf-8")
        choices = schemas.split("| key ready to register |", 1)[1].split("\n\n", 1)[0]
        rows = self.document_rows(choices)
        self.assertTrue(rows)
        for key, link, proof in rows:
            url = re.search(r"\((https://raw.githubusercontent.com/[^)]+)\)", link)[1]
            owner, repo, pin, path = url.removeprefix("https://raw.githubusercontent.com/").split("/", 3)
            artifact = f"{owner}/{repo}@{pin}/{path}"
            if owner == "jentic":
                artifact = path.removeprefix("apis/")
            matches = [row for row in candidates if row[0] == artifact]
            self.assertEqual(1, len(matches), artifact)
            candidate = matches[0]
            self.assertIn(key, candidate[1].replace("`", "").split(", "))
            self.assertEqual("witness-found", candidate[6])
            self.assertTrue(all(cell.startswith("passed:") for cell in candidate[2:6]))
            evidence = " ".join(candidate[2:])
            if owner == "jentic":
                self.assertIn(pin, evidence)
            counts = set(re.findall(r"(\d+) (?:Python )?files", evidence))
            self.assertEqual(counts, set(re.findall(r"(\d+) (?:Python )?files", proof)))
            self.assertTrue(counts)
            for version in re.findall(r"\b5\.\d+\.\d+\b", candidate[4]):
                self.assertIn(version, proof)
            for model in re.findall(r"\b(?:Auth\w+Payload|GroundTruthList\w*)\b", proof):
                self.assertIn(model, evidence)

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

    def test_paypal_registration_accounts_for_all_owned_keys(self) -> None:
        source = REPO / ".local/corpus/paypal-catalog-products/openapi.json"
        if not source.is_file():
            self.skipTest("PayPal source not fetched; run just fetch-corpus --fixture paypal-catalog-products")
        keys = dict(self.contract_keys())
        self.assertEqual(30, len(keys))
        result = subprocess.run(
            [sys.executable, str(REPO / "scripts/openapi-surface-census.py"),
             "--fixture", "paypal-catalog-products", "--json",
             *(arg for selector in keys.values() for arg in ("--selector", selector))],
            cwd=REPO, capture_output=True, text=True, encoding="utf-8",
        )
        self.assertEqual(0, result.returncode, result.stderr)
        census = json.loads(result.stdout)
        counts = {row["selector"]: row["count"] for row in census["rows"]}
        self.assertEqual({"schema.anyOf:sole-member": 4}, counts)
        self.assertEqual(set(keys.values()) - set(counts), set(census["absent_selectors"]))
        # Authoritative entry rows use bare keys, unlike candidate tables.
        entries = {}
        for line in (REPO / "docs/openapi-surface/schemas.md").read_text(encoding="utf-8").splitlines():
            if line.startswith("| "):
                cells = [cell.strip().strip("`") for cell in line.strip("|").split("|")]
                if len(cells) == 8 and cells[0] in keys:
                    entries[cells[0]] = cells
        self.assertEqual(set(keys), set(entries))
        for key, selector in keys.items():
            self.assertEqual("golden" if selector in counts else "gap", entries[key][3], key)
        self.assertIn("**4** declaration sites", entries["anyof-sole-member"][4])
        self.assertIn("paypal-catalog-products", entries["anyof-sole-member"][4])

    def test_committed_reports_reconcile_with_authoritative_rows(self) -> None:
        result = self.run_validator(*SHARDS, reconcile=True)
        self.assertEqual(0, result.returncode, result.stderr)

    def test_screened_witness_overrides_unanswered_sources_and_requires_retention(self) -> None:
        shards, schemas = self.completed_documents()
        key = self.contract_keys()[0][0]
        candidates = schemas.parent / "candidates.md"
        row = (
            f"| `publisher/spec@pin/openapi.json` | `{key}` | passed: grant | "
            "passed: publisher pin | passed: non-empty generation | "
            "passed: generated model | `witness-found` | model.py |\n"
        )
        candidates.write_text(row, encoding="utf-8")
        schemas.write_text(schemas.read_text(encoding="utf-8").replace(
            "search outcome `search-incomplete`", "search outcome `witness-found`", 1
        ), encoding="utf-8")
        found = self.reconcile_documents(shards, schemas)
        self.assertEqual(0, found.returncode, found.stderr)
        for screen in ("grant", "publisher pin", "non-empty generation", "generated model"):
            with self.subTest(screen=screen):
                candidates.write_text(row.replace(f"passed: {screen}", f"blocked: {screen}"), encoding="utf-8")
                rejected = self.reconcile_documents(shards, schemas)
                self.assertNotEqual(0, rejected.returncode)
                self.assertIn("search-incomplete", rejected.stderr)
        candidates.write_text(row.replace("passed: generated model", f"passed: model; discarded keys: `{key}`"), encoding="utf-8")
        discarded = self.reconcile_documents(shards, schemas)
        self.assertNotEqual(0, discarded.returncode)
        self.assertIn("search-incomplete", discarded.stderr)
        candidates.write_text(row, encoding="utf-8")
        recovered = self.reconcile_documents(shards, schemas)
        self.assertEqual(0, recovered.returncode, recovered.stderr)

    def test_seven_zero_answers_allow_absence_but_one_unanswered_forbids_it(self) -> None:
        shards, schemas = self.completed_documents()
        for path in shards:
            path.write_text(
                path.read_text(encoding="utf-8").replace("| unanswered |", "| 0 |"),
                encoding="utf-8",
            )
        schemas.write_text(
            schemas.read_text(encoding="utf-8")
            .replace("→ `unanswered`", "→ 0")
            .replace("search outcome `search-incomplete`", "search outcome `none-found`"),
            encoding="utf-8",
        )
        result = self.reconcile_documents(shards, schemas)
        self.assertEqual(0, result.returncode, result.stderr)
        shards[0].write_text(
            shards[0].read_text(encoding="utf-8").replace("| 0 |", "| unanswered |", 1),
            encoding="utf-8",
        )
        schemas.write_text(
            schemas.read_text(encoding="utf-8").replace("→ 0", "→ `unanswered`", 1),
            encoding="utf-8",
        )
        refused = self.reconcile_documents(shards, schemas)
        self.assertNotEqual(0, refused.returncode)
        self.assertIn("expected 'search-incomplete'", refused.stderr)
        schemas.write_text(
            schemas.read_text(encoding="utf-8").replace(
                "search outcome `none-found`", "search outcome `search-incomplete`", 1
            ),
            encoding="utf-8",
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
            text=True, encoding="utf-8",
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
