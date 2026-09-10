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
        supplement = REPO / "docs/openapi-surface/witness-scrape-wide/candidates.md"
        command = [sys.executable, str(SCRIPT), str(CONTRACT), *(str(p) for p in SHARDS),
                   "--reconcile", "--schemas", str(REPO / "docs/openapi-surface/schemas.md")]
        if supplement.is_file():
            command += ["--supplement-candidates", str(supplement)]
        result = subprocess.run(command, cwd=REPO, capture_output=True, encoding="utf-8")
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

class WideWitnessTests(unittest.TestCase):
    """Acquire pinned bytes and validate reports through the actual CLI boundary."""

    contract_keys = WitnessSearchRedoTests.contract_keys
    completed_documents = WitnessSearchRedoTests.completed_documents

    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.work = Path(self.directory.name)
        self.wide = REPO / 'scripts/witness-scrape-wide.py'
        self.report = self.work / 'report'
        result = self.cli('derive', '--report', self.report)
        self.assertEqual(0, result.returncode, result.stderr)
        self.key = next(iter(json.loads((self.report / 'baseline.json').read_text(encoding='utf-8'))['keys']))
        self.sha = 'a' * 64
        self.artifact = 'https://publisher.example/pinned/openapi.json'
        self.candidate = (
            '| artifact | keys | redistribution | immutable publisher reference | Fern acceptance | retention | disposition | evidence |\n'
            '|---|---|---|---|---|---|---|---|\n'
            f'| `{self.artifact}` | `{self.key}` | passed: grant | passed: immutable publisher | passed: real generation | passed: retained model | `witness-found` | fern.txt |\n'
        )
        (self.report / 'candidates.md').write_text(self.candidate, encoding='utf-8')
        (self.report / 'fern.txt').write_text('Fern evidence: modèle conservé\n', encoding='utf-8')
        (self.report / 'comparison.txt').write_text('comparison failed: modèle.py differs\n', encoding='utf-8')
        self.rank_header = 'rank\tartifact_sha256\tartifact\tkeys\tfern_evidence\tcomparison_evidence\n'
        self.rank_row = f'1\t{self.sha}\t{self.artifact}\t{json.dumps([self.key])}\tfern.txt\tcomparison.txt\n'
        (self.report / 'ranking.tsv').write_text(self.rank_header + self.rank_row, encoding='utf-8')
        self.slots_header = '| slot | artifact_sha256 | keys | disposition | evidence |\n|---|---|---|---|---|\n'
        (self.report / 'slots.md').write_text(self.slots_header, encoding='utf-8')

    def cli(self, *args) -> subprocess.CompletedProcess[str]:
        return subprocess.run([sys.executable, str(self.wide), *(str(a) for a in args)],
                              cwd=REPO, capture_output=True, encoding='utf-8')

    def validate(self, *args) -> subprocess.CompletedProcess[str]:
        return self.cli('validate', '--report', self.report, *args)

    def test_derive_preserves_key_specific_screening_metadata(self) -> None:
        root = self.work / 'history'
        root.mkdir()
        shutil.copyfile(CONTRACT, root / 'contract.md')
        keys = list(json.loads((self.report / 'baseline.json').read_text(encoding='utf-8'))['keys'])
        retained, discarded, absent = keys[:3]
        screens = ['passed: publisher grant', 'passed: pinned publisher', 'passed: generated SDK',
                   f'passed: retained first model; discarded keys: `{discarded}`']
        blocked = ['blocked: no publisher grant', 'not reached', 'not reached', 'not reached']
        table = '\n'.join(self.candidate.splitlines()[:2]) + '\n'
        table += f'| `publisher/retained-é.json` | `{retained}`, `{discarded}` | ' + ' | '.join(screens) + ' | `witness-found` | evidence.txt |\n'
        table += f'| `publisher/blocked.json` | `{discarded}` | ' + ' | '.join(blocked) + ' | `witness-blocked` | evidence.txt |\n'
        (root / 'candidates.md').write_text(table, encoding='utf-8')
        output = self.work / 'derived'
        result = self.cli('derive', '--report', output, '--contract', root / 'contract.md')
        self.assertEqual(0, result.returncode, result.stderr)
        baseline = json.loads((output / 'baseline.json').read_text(encoding='utf-8'))
        pin = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=REPO, encoding='utf-8').strip()
        self.assertEqual(pin, baseline['source_commit'])
        items = baseline['keys']
        self.assertTrue(items[retained]['usable_witness'])
        self.assertFalse(items[discarded]['usable_witness'])
        self.assertFalse(items[absent]['usable_witness'])
        self.assertEqual([], items[absent]['candidates'])
        self.assertEqual([{'artifact': 'publisher/retained-é.json', 'screens': screens,
                           'disposition': 'witness-found', 'discarded': False}], items[retained]['candidates'])
        self.assertEqual([{'artifact': 'publisher/retained-é.json', 'screens': screens,
                           'disposition': 'witness-found', 'discarded': True},
                          {'artifact': 'publisher/blocked.json', 'screens': blocked,
                           'disposition': 'witness-blocked', 'discarded': False}], items[discarded]['candidates'])
        # Changing the frozen selector must refuse derivation before writing a report.
        contract = root / 'contract.md'
        contract.write_text(contract.read_text(encoding='utf-8').replace('schema.', 'unknown.', 1), encoding='utf-8')
        refused = self.cli('derive', '--report', self.work / 'refused', '--contract', contract)
        self.assertNotEqual(0, refused.returncode)
        self.assertIn('selector', refused.stderr)
        self.assertFalse((self.work / 'refused').exists())

    def test_inventory_boundary_refusals_precede_acquisition_and_recover(self) -> None:
        inventory = self.work / 'inventaire-é.json'
        cache = self.work / 'cache'
        output = self.work / 'acquisition.json'
        source = {'artifact': (self.work / 'absent.json').as_uri()}
        cases = [([], 'expected inventory'), ({}, 'expected inventory'),
                 ({'schema_version': 2, 'sources': []}, 'expected inventory'),
                 ({'schema_version': 1, 'sources': {}}, 'expected inventory')]
        for row in (None, {}, {'artifact': ''}, {'artifact': 7}):
            cases.append(({'schema_version': 1, 'sources': [row]}, 'missing artifact identity'))
        cases.append(({'schema_version': 1, 'sources': [source, source]}, 'duplicate artifact'))
        for field in ('sha256', 'prior_sha256'):
            for value in ('A' * 64, 'a' * 63, 42):
                cases.append(({'schema_version': 1, 'sources': [dict(source, **{field: value})]}, f'malformed {field}'))
        args = ('acquire', '--inventory', inventory, '--cache', cache,
                '--contract', self.report / 'keys.md', '--output', output)
        for invalid, message in cases:
            with self.subTest(invalid=invalid):
                inventory.write_text(json.dumps(invalid), encoding='utf-8')
                refused = self.cli(*args)
                self.assertNotEqual(0, refused.returncode)
                self.assertIn(message, refused.stderr)
                self.assertIn('inventaire-é.json', refused.stderr)
                self.assertFalse(cache.exists())
                self.assertFalse(output.exists())
        inventory.write_text(json.dumps({'schema_version': 1, 'sources': [source]}), encoding='utf-8')
        recovered = self.cli(*args)
        self.assertEqual(0, recovered.returncode, recovered.stderr)
        self.assertEqual('inaccessible', json.loads(output.read_text(encoding='utf-8'))['sources'][0]['status'])

    def test_real_report_validator_rejects_contract_drift_and_recovers(self) -> None:
        good = self.validate()
        self.assertEqual(0, good.returncode, good.stderr)
        changes = [
            ('candidates.md', self.candidate.replace('witness-found', 'invented'), 'unknown candidate disposition'),
            ('ranking.tsv', self.rank_header + self.rank_row * 2, 'duplicate rank'),
            ('ranking.tsv', self.rank_header + self.rank_row.replace('1\t', '0\t', 1), 'malformed'),
            ('ranking.tsv', self.rank_header + self.rank_row.replace(self.key, 'unknown-key'), 'unknown keys'),
            ('ranking.tsv', self.rank_header + self.rank_row.replace('fern.txt', 'absent-é.txt'), 'absent-é.txt'),
            ('keys.md', (self.report / 'keys.md').read_text(encoding='utf-8').replace('schema.', 'invented.', 1), 'selector'),
            ('candidates.md', self.candidate.replace('passed: retained model', f'passed: other model; discarded keys: `{self.key}`'), 'retained candidate screens'),
        ]
        for filename, text, message in changes:
            with self.subTest(message=message):
                path = self.report / filename
                old = path.read_text(encoding='utf-8')
                path.write_text(text, encoding='utf-8')
                failed = self.validate()
                self.assertNotEqual(0, failed.returncode)
                self.assertIn(message, failed.stderr)
                path.write_text(old, encoding='utf-8')
        recovered = self.validate()
        self.assertEqual(0, recovered.returncode, recovered.stderr)

    def test_report_table_failures_identify_the_broken_contract_and_recover(self) -> None:
        candidate_row = self.candidate.splitlines()[-1] + '\n'
        exhausted = '| slot-1 | — | [] | exhausted | comparison.txt |\n'
        baseline = json.loads((self.report / 'baseline.json').read_text(encoding='utf-8'))
        baseline['schema_version'] = 2
        changes = [
            ('baseline.json', json.dumps(baseline), 'baseline schema_version must be 1'),
            ('candidates.md', self.candidate.replace('redistribution', 'grant'), 'candidate header'),
            ('candidates.md', self.candidate.replace(' | fern.txt |', ' |'), 'eight columns'),
            ('candidates.md', self.candidate.replace('passed: grant', ''), 'missing a screen state'),
            ('candidates.md', self.candidate + candidate_row, 'duplicate candidate artifact'),
            ('candidates.md', self.candidate.replace(self.key, 'unknown-key'), 'candidate has unknown keys'),
            ('ranking.tsv', (self.rank_header + self.rank_row).replace('rank\t', 'position\t', 1), 'ranking header'),
            ('slots.md', self.slots_header.replace('disposition', 'result'), 'slot header'),
            ('slots.md', self.slots_header + exhausted.replace(' | comparison.txt |', ' |'), 'five columns'),
            ('slots.md', self.slots_header + exhausted * 2, 'duplicate or empty slot'),
            ('slots.md', self.slots_header + exhausted.replace('slot-1', ''), 'duplicate or empty slot'),
            ('slots.md', self.slots_header + exhausted.replace('exhausted', 'invented'), 'unknown slot disposition'),
            ('slots.md', self.slots_header + exhausted.replace('—', self.sha), 'absent artifact and keys'),
            ('slots.md', self.slots_header + exhausted.replace('[]', json.dumps([self.key])), 'absent artifact and keys'),
        ]
        for filename, broken, diagnostic in changes:
            with self.subTest(diagnostic=diagnostic, broken=broken):
                path = self.report / filename
                original = path.read_text(encoding='utf-8')
                path.write_text(broken, encoding='utf-8')
                refused = self.validate()
                self.assertNotEqual(0, refused.returncode)
                self.assertIn(diagnostic, refused.stderr)
                path.write_text(original, encoding='utf-8')
        recovered = self.validate()
        self.assertEqual(0, recovered.returncode, recovered.stderr)

    def test_slots_reject_conflicting_claims_and_accept_exhaustion(self) -> None:
        path = self.report / 'slots.md'
        row = f'| slot-1 | {self.sha} | {json.dumps([self.key])} | registered | comparison.txt |\n'
        path.write_text(self.slots_header + row, encoding='utf-8')
        self.assertEqual(0, self.validate().returncode)
        path.write_text(self.slots_header + row + row.replace('slot-1', 'slot-2'), encoding='utf-8')
        failed = self.validate()
        self.assertNotEqual(0, failed.returncode)
        self.assertIn('conflicting slot claim', failed.stderr)
        path.write_text(self.slots_header + '| slot-1 | — | [] | exhausted | comparison.txt |\n', encoding='utf-8')
        self.assertEqual(0, self.validate().returncode)

    def multiple_ranked_candidates(self) -> tuple[list[tuple[str, str, list[str]]], list[str]]:
        keys = list(json.loads((self.report / 'baseline.json').read_text(encoding='utf-8'))['keys'])[:2]
        # Expected order is explicit: coverage beats firmness, then firmness beats
        # the digest, and the equal-firmness pair is ordered by ascending digest.
        definitions = [('d', keys, 0), ('b', keys[:1], 2), ('a', keys[:1], 1), ('c', keys[:1], 1)]
        header = self.candidate.splitlines()[:2]
        candidates = []
        sources = []
        for label, owned, firmness in definitions:
            sha = label * 64
            artifact = f'https://publisher.example/{"1" * 40}/{label}/openapi.json'
            candidates.append((sha, artifact, owned))
            header.append(f'| `{artifact}` | ' + ', '.join(f'`{key}`' for key in owned) + ' | passed: grant | passed: publisher pin | passed: generation | passed: retained model | `witness-found` | fern.txt |')
            row = {'artifact': artifact, 'sha256': sha, 'ref': '1' * 40,
                   'repository': 'APIs-guru/openapi-directory' if firmness == 0 else 'publisher/api',
                   'status': 'readable', 'document': sha + '.json'}
            row['repository_licences'] = [{'evidence': 'fern.txt'}]
            if firmness in {0, 2}:
                row['document_license'] = {'name': 'Document grant'}
            sources.append(row)
        # A retained provenance alias uses the existing byte rank, never a fifth rank.
        alias = 'https://publisher.example/' + '1' * 40 + '/mirror-b/openapi.json'
        header.append(f'| `{alias}` | `{keys[0]}` | passed: grant | passed: publisher pin | passed: generation | passed: retained model | `witness-found` | fern.txt |')
        sources.append(dict(sources[1], artifact=alias))
        (self.report / 'candidates.md').write_text('\n'.join(header) + '\n', encoding='utf-8')
        (self.report / 'acquisition.json').write_text(json.dumps({'schema_version': 1, 'sources': sources}), encoding='utf-8')
        self.write_ranks(candidates)
        return candidates, keys

    def write_ranks(self, candidates: list[tuple[str, str, list[str]]], ranks: list[int] | None = None) -> None:
        numbers = ranks if ranks is not None else list(range(1, len(candidates) + 1))
        rows = [f'{rank}\t{sha}\t{artifact}\t{json.dumps(keys)}\tfern.txt\tcomparison.txt\n'
                for rank, (sha, artifact, keys) in zip(numbers, candidates)]
        (self.report / 'ranking.tsv').write_text(self.rank_header + ''.join(rows), encoding='utf-8')

    def test_multiple_ranks_freeze_coverage_firmness_and_digest_order(self) -> None:
        candidates, _keys = self.multiple_ranked_candidates()
        valid = self.validate()
        self.assertEqual(0, valid.returncode, valid.stderr)
        for first, second, reason in [(0, 1, 'coverage'), (1, 2, 'firmness'), (2, 3, 'digest')]:
            with self.subTest(reason=reason):
                wrong = list(candidates)
                wrong[first], wrong[second] = wrong[second], wrong[first]
                self.write_ranks(wrong)
                refused = self.validate()
                self.assertNotEqual(0, refused.returncode)
                self.assertIn('ranking violates', refused.stderr)
        self.write_ranks(candidates, [1, 2, 3, 5])
        refused = self.validate()
        self.assertNotEqual(0, refused.returncode)
        self.assertIn('ranks must be contiguous', refused.stderr)
        self.write_ranks(candidates[:-1])
        refused = self.validate()
        self.assertNotEqual(0, refused.returncode)
        self.assertIn('retained candidate missing rank', refused.stderr)
        alias = 'https://publisher.example/' + '1' * 40 + '/mirror-b/openapi.json'
        self.write_ranks(candidates + [(candidates[1][0], alias, candidates[1][2])])
        refused = self.validate()
        self.assertNotEqual(0, refused.returncode)
        self.assertIn('duplicate ranked digest', refused.stderr)
        self.write_ranks(candidates)
        recovered = self.validate()
        self.assertEqual(0, recovered.returncode, recovered.stderr)

    def test_blocked_slots_do_not_claim_keys_but_registered_slots_cannot_conflict(self) -> None:
        candidates, keys = self.multiple_ranked_candidates()
        path = self.report / 'slots.md'
        blocked = f'| slot-1 | {candidates[0][0]} | {json.dumps(keys[:1])} | blocked | comparison.txt |\n'
        registered = f'| slot-2 | {candidates[1][0]} | {json.dumps(keys[:1])} | registered | comparison.txt |\n'
        path.write_text(self.slots_header + blocked + registered, encoding='utf-8')
        valid = self.validate()
        self.assertEqual(0, valid.returncode, valid.stderr)
        path.write_text(self.slots_header + blocked.replace('| blocked |', '| registered |') + registered, encoding='utf-8')
        refused = self.validate()
        self.assertNotEqual(0, refused.returncode)
        self.assertIn('conflicting registered key claims', refused.stderr)
        path.write_text(self.slots_header + blocked + registered, encoding='utf-8')
        recovered = self.validate()
        self.assertEqual(0, recovered.returncode, recovered.stderr)

    def test_supplements_are_optional_additive_and_discarded_keys_do_not_pass(self) -> None:
        shards, schemas = self.completed_documents()
        key = self.contract_keys()[0][0]
        supplemental = self.work / 'supplement.md'
        supplemental.write_text(self.candidate.replace(self.key, key), encoding='utf-8')
        command = [sys.executable, str(SCRIPT), str(CONTRACT), *(str(p) for p in shards),
                   '--reconcile', '--schemas', str(schemas), '--candidates', str(schemas.parent / 'candidates.md')]
        run = lambda extra: subprocess.run(command + extra, cwd=REPO, capture_output=True, encoding='utf-8')
        self.assertEqual(0, run([]).returncode)
        supplement = ['--supplement-candidates', str(supplemental)]
        self.assertIn("expected 'witness-found'", run(supplement).stderr)
        schemas.write_text(schemas.read_text(encoding='utf-8').replace('search outcome `search-incomplete`', 'search outcome `witness-found`', 1), encoding='utf-8')
        self.assertEqual(0, run(supplement * 2).returncode)
        self.assertNotEqual(0, run([]).returncode)
        supplemental.write_text(supplemental.read_text(encoding='utf-8').replace('passed: retained model', f'passed: other model; discarded keys: `{key}`'), encoding='utf-8')
        self.assertIn("expected 'search-incomplete'", run(supplement).stderr)
        missing = self.work / 'absent-supplément.md'
        missing_args = ['--supplement-candidates', str(missing)]
        refused = run(missing_args)
        self.assertEqual(2, refused.returncode)
        self.assertIn('requires a candidate file', refused.stderr)
        missing.write_text(self.candidate.replace(self.key, key), encoding='utf-8')
        self.assertEqual(0, run(missing_args).returncode)

    def test_acquisition_uses_real_files_cache_and_census_with_failure_recovery(self) -> None:
        import hashlib
        spec = self.work / 'publisher.yaml'  # publisher suffix may disagree with unchanged JSON bytes
        spec.write_text(json.dumps({'openapi': '3.0.3', 'info': {'title': 'Réel', 'version': '1'},
                                    'paths': {}, 'components': {'schemas': {'Sample': {'properties': {'x': {'anyOf': [{'type': 'object', 'properties': {'value': {'type': 'string'}}}]}}}}}}), encoding='utf-8')
        sha = hashlib.sha256(spec.read_bytes()).hexdigest()
        malformed = self.work / 'malformé.json'
        malformed.write_text('{é', encoding='utf-8')
        legacy = self.work / 'legacy.json'
        legacy.write_text(json.dumps({'swagger': '2.0', 'info': {'title': 'Legacy', 'version': '1'}, 'paths': {}}), encoding='utf-8')
        metadata = self.work / 'versions.json'
        metadata.write_text('{"versions": ["1", "2"]}', encoding='utf-8')
        inventory = self.work / 'inventory.json'
        rows = [{'artifact': spec.as_uri(), 'sha256': sha, 'prior_sha256': sha},
                {'artifact': malformed.as_uri()}, {'artifact': (self.work / 'absent.json').as_uri()},
                {'artifact': legacy.as_uri()}, {'artifact': metadata.as_uri()}]
        inventory.write_text(json.dumps({'schema_version': 1, 'sources': rows}), encoding='utf-8')
        import gzip
        compressed = inventory.with_suffix('.json.gz')
        compressed.write_bytes(gzip.compress(inventory.read_bytes(), mtime=0))
        inventory = compressed
        cache = self.work / 'cache'
        output = self.report / 'acquisition.json'
        args = ('acquire', '--inventory', inventory, '--cache', cache,
                '--contract', self.report / 'keys.md', '--output', output)
        for workers in ('0', '-1'):
            refused = self.cli(*args, '--workers', workers)
            self.assertNotEqual(0, refused.returncode)
            self.assertIn('workers must be positive', refused.stderr)
            self.assertFalse(cache.exists(), 'invalid worker counts must not start acquisition')
        args += ('--workers', '2')
        first = self.cli(*args)
        self.assertEqual(0, first.returncode, first.stderr)
        outcomes = json.loads(output.read_text(encoding='utf-8'))['sources']
        self.assertEqual(['readable', 'unreadable', 'inaccessible', 'excluded', 'excluded'], [r['status'] for r in outcomes])
        for excluded in outcomes[3:]:
            self.assertIn('no conversion performed', excluded['diagnostic'])
            self.assertNotIn('document', excluded)
        self.assertEqual('newly-fetched', outcomes[0]['acquisition'])
        self.assertEqual(sha + '.json', outcomes[0]['document'])
        self.assertNotIn('document_license', outcomes[0])
        self.assertIn('property-sole-anyof-struct-member', output.with_suffix('.census.tsv').read_text(encoding='utf-8'))
        self.assertEqual(0, self.validate('--inventory', inventory).returncode)
        spec.unlink()  # exact cached bytes still support a real census offline
        second = self.cli(*args)
        self.assertEqual(0, second.returncode, second.stderr)
        self.assertEqual('verified-reuse', json.loads(output.read_text(encoding='utf-8'))['sources'][0]['acquisition'])
        (cache / sha).write_bytes(b'changed cached bytes')
        third = self.cli(*args)
        self.assertEqual(0, third.returncode, third.stderr)
        self.assertEqual('inaccessible', json.loads(output.read_text(encoding='utf-8'))['sources'][0]['status'])
        spec.write_text('{"openapi":"3.1.0"}', encoding='utf-8')
        self.assertEqual(0, self.cli(*args).returncode)
        measured = json.loads(output.read_text(encoding='utf-8'))
        self.assertEqual('digest-changed', measured['sources'][0]['status'])
        measured['sources'].pop()
        output.write_text(json.dumps(measured), encoding='utf-8')
        partial = self.validate('--inventory', inventory)
        self.assertNotEqual(0, partial.returncode)
        self.assertIn('partial inventory', partial.stderr)

    def test_changed_publisher_bytes_record_the_document_licence(self) -> None:
        import hashlib
        spec = self.work / 'publisher.json'
        document = {'openapi': '3.0.3', 'info': {'title': 'Éditeur', 'version': '2',
                    'license': {'name': 'Publisher grant', 'url': 'https://publisher.example/grant'}}, 'paths': {}}
        spec.write_text(json.dumps(document), encoding='utf-8')
        sha = hashlib.sha256(spec.read_bytes()).hexdigest()
        inventory = self.work / 'inventory.json'
        inventory.write_text(json.dumps({'schema_version': 1, 'sources': [
            {'artifact': spec.as_uri(), 'sha256': sha, 'prior_sha256': '0' * 64}]}), encoding='utf-8')
        output = self.work / 'acquisition.json'
        run = self.cli('acquire', '--inventory', inventory, '--cache', self.work / 'cache',
                       '--contract', self.report / 'keys.md', '--output', output)
        self.assertEqual(0, run.returncode, run.stderr)
        row = json.loads(output.read_text(encoding='utf-8'))['sources'][0]
        self.assertEqual('readable', row['status'])
        self.assertEqual('changed-bytes', row['prior_relation'])
        self.assertEqual(sha, row['sha256'])
        self.assertEqual(document['info']['license'], row.get('document_license'))

    def test_acquisition_preserves_failed_real_census_logs_and_recovers(self) -> None:
        # JSON decoding succeeds, but a deeply nested schema exceeds the real
        # census walk's recursion depth. No substitute census process is used.
        spec = self.work / 'profond.json'
        schema = {'type': 'string'}
        for _ in range(700):
            schema = {'items': schema}
        document = {'openapi': '3.0.3', 'info': {'title': 'Profond', 'version': '1'},
                    'paths': {}, 'components': {'schemas': {'Deep': schema}}}
        spec.write_text(json.dumps(document), encoding='utf-8')
        inventory = self.work / 'inventory.json'
        inventory.write_text(json.dumps({'schema_version': 1, 'sources': [{'artifact': spec.as_uri()}]}), encoding='utf-8')
        output = self.work / 'acquisition.json'
        args = ('acquire', '--inventory', inventory, '--cache', self.work / 'cache',
                '--contract', self.report / 'keys.md', '--output', output)
        refused = self.cli(*args)
        self.assertNotEqual(0, refused.returncode)
        self.assertIn('census failed; see', refused.stderr)
        self.assertIn(str(output.with_suffix('.census.log')), refused.stderr)
        recorded = json.loads(output.read_text(encoding='utf-8'))
        self.assertEqual('readable', recorded['sources'][0]['status'])
        self.assertNotEqual(0, recorded['census_exit'])
        self.assertIn('RecursionError', output.with_suffix('.census.log').read_text(encoding='utf-8'))
        document['components']['schemas']['Deep'] = {'type': 'string'}
        spec.write_text(json.dumps(document), encoding='utf-8')
        recovered = self.cli(*args)
        self.assertEqual(0, recovered.returncode, recovered.stderr)
        self.assertEqual(0, json.loads(output.read_text(encoding='utf-8'))['census_exit'])

    def test_index_tree_joins_every_version_to_verified_git_bytes(self) -> None:
        import hashlib
        tree = self.work / 'tree'
        tree.mkdir()
        def git(*args):
            return subprocess.run(['git', '-C', str(tree), *args], capture_output=True, encoding='utf-8', check=True)
        git('init', '-q')
        git('config', 'user.name', 'Witness test')
        git('config', 'user.email', 'witness@example.invalid')
        path = tree / 'APIs/publisher/1/openapi.yaml'
        path.parent.mkdir(parents=True)
        path.write_text('openapi: 3.0.3\ninfo: {title: réel, version: 1}\npaths: {}\n', encoding='utf-8')
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

    def test_committed_wide_report(self) -> None:
        root = REPO / 'docs/openapi-surface/witness-scrape-wide'
        result = self.cli('validate', '--report', root, '--inventory', root / 'inventory.json.gz')
        self.assertEqual(0, result.returncode, result.stderr)

    def test_consolidated_report_rejects_lost_screens_and_census_evidence(self) -> None:
        import gzip
        import hashlib
        root = self.work / 'consolidated'
        shutil.copytree(REPO / 'docs/openapi-surface/witness-scrape-wide', root)
        run = lambda: self.cli('validate', '--report', root, '--inventory', root / 'inventory.json.gz')
        good = run()
        self.assertEqual(0, good.returncode, good.stderr)
        candidates = root / 'candidates.md'
        original = candidates.read_text(encoding='utf-8')
        row = next(line for line in original.splitlines(keepends=True) if line.startswith('| `'))
        candidates.write_text(original.replace(row, '', 1), encoding='utf-8')
        failed = run()
        self.assertNotEqual(0, failed.returncode)
        self.assertIn('missing completed or blocked screens', failed.stderr)
        candidates.write_text(original, encoding='utf-8')
        owned = re.findall(r'`([^`]+)`', row.split('|')[2])
        known = json.loads((root / 'baseline.json').read_text(encoding='utf-8'))['keys']
        other = next(key for key in known if key not in owned)
        candidates.write_text(original.replace(row, row.replace(f'`{owned[0]}`', f'`{other}`', 1), 1), encoding='utf-8')
        failed = run()
        self.assertNotEqual(0, failed.returncode)
        self.assertIn('candidate keys disagree with measured declarations', failed.stderr)
        candidates.write_text(original, encoding='utf-8')
        evidence = root / 'publisher-census.tsv'
        content = evidence.read_bytes()
        evidence.unlink()
        failed = run()
        self.assertNotEqual(0, failed.returncode)
        self.assertIn('missing or outside-report evidence', failed.stderr)
        evidence.write_bytes(content)
        acquisition = root / 'acquisition.json.gz'
        original_acquisition = acquisition.read_bytes()
        outcome = json.loads(gzip.decompress(original_acquisition))
        catalogue = root / 'catalogue-census.tsv'
        text = catalogue.read_text(encoding='utf-8')
        catalogue.write_text(text.replace('schema.', 'unknown.', 1), encoding='utf-8')
        for record in outcome['census_runs']:
            if record['stdout'] == catalogue.name:
                record['stdout_sha256'] = hashlib.sha256(catalogue.read_bytes()).hexdigest()
        acquisition.write_bytes(gzip.compress(json.dumps(outcome).encode('utf-8'), mtime=0))
        failed = run()
        self.assertNotEqual(0, failed.returncode)
        self.assertIn('unknown document, selector or key', failed.stderr)
        catalogue.write_text(text, encoding='utf-8')
        acquisition.write_bytes(original_acquisition)
        recovered = run()
        self.assertEqual(0, recovered.returncode, recovered.stderr)

    def test_consolidated_report_rejects_corrupt_accounting_and_recovers(self) -> None:
        import gzip
        import hashlib
        root = self.work / 'consolidated'
        shutil.copytree(REPO / 'docs/openapi-surface/witness-scrape-wide', root)
        run = lambda: self.cli('validate', '--report', root, '--inventory', root / 'inventory.json.gz')
        fingerprints = root / 'historical-sha256.tsv'
        original_fingerprints = fingerprints.read_text(encoding='utf-8')
        lines = original_fingerprints.splitlines()
        cells = lines[1].split('\t')
        header = lines[0].split('\t')
        cells[header.index('sha256')] = '0' * 64
        lines[1] = '\t'.join(cells)
        fingerprints.write_text('\n'.join(lines) + '\n', encoding='utf-8')
        refused = run()
        self.assertNotEqual(0, refused.returncode)
        self.assertIn('historical report bytes changed', refused.stderr)
        fingerprints.write_text(original_fingerprints, encoding='utf-8')
        acquisition = root / 'acquisition.json.gz'
        original = acquisition.read_bytes()
        for mode, message in [
            ('outcome', 'missing acquisition outcome'),
            ('diagnostic', 'failed acquisition missing diagnostic'),
            ('runs', 'missing census runs'),
            ('exit', 'unfinished or failed census'),
            ('digest', 'census evidence digest changed'),
            ('header', 'census evidence header changed'),
            ('count', 'invalid declaration count'),
        ]:
            with self.subTest(mode=mode):
                data = json.loads(gzip.decompress(original))
                catalogue = root / 'catalogue-census.tsv'
                census_bytes = catalogue.read_bytes()
                if mode == 'outcome':
                    data['sources'][0].pop('status')
                elif mode == 'diagnostic':
                    failed = next(row for row in data['sources'] if row['status'] != 'readable')
                    failed.pop('diagnostic')
                elif mode == 'runs':
                    data['census_runs'] = []
                elif mode == 'exit':
                    data['census_runs'][0]['exit_code'] = 1
                elif mode == 'digest':
                    data['census_runs'][0]['stdout_sha256'] = '0' * 64
                else:
                    rows = census_bytes.decode('utf-8').splitlines()
                    if mode == 'header':
                        rows[0] = rows[0].replace('count', 'total')
                    else:
                        cells = rows[1].split('\t')
                        cells[-1] = '0'
                        rows[1] = '\t'.join(cells)
                    catalogue.write_text('\n'.join(rows) + '\n', encoding='utf-8')
                    record = next(row for row in data['census_runs'] if row['stdout'] == catalogue.name)
                    record['stdout_sha256'] = hashlib.sha256(catalogue.read_bytes()).hexdigest()
                acquisition.write_bytes(gzip.compress(json.dumps(data).encode('utf-8'), mtime=0))
                refused = run()
                self.assertNotEqual(0, refused.returncode)
                self.assertIn(message, refused.stderr)
                catalogue.write_bytes(census_bytes)
                acquisition.write_bytes(original)
        recovered = run()
        self.assertEqual(0, recovered.returncode, recovered.stderr)


if __name__ == "__main__":
    unittest.main()
