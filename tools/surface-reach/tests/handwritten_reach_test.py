#!/usr/bin/env python3
"""Drive the real `just handwritten-reach` recipe over temporary fixtures.

The recipe builds crozier instrumented and runs it over each hand-written
fixture's `openapi.yml` alone, so this is its journey rather than a mock of it:
two fixtures covering the same arm, one whose document takes it and one whose
document does not, read back from the ledger the recipe writes; one document
measured with and without the `audiences` its fixture declares; and a cover
naming an arm the site table does not list, refused before anything is written.
"""

from __future__ import annotations

import csv
import subprocess
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
HEADER = ["fixture", "key", "site", "regions_executed", "regions"]
ARM = r'src/ir.rs::scalar_body[Some\("email" \x7c "hostname" \x7c "ipv4"]'
DOCUMENT = """openapi: 3.0.3
info:
  title: sample
  version: 1.0.0
paths:
  /probe:
    post:
      operationId: probe
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: string
{format}      responses:
        "200":
          description: ok
"""
EVIDENCE = """fern_cli_version = "5.67.1"
fern_python_sdk_version = "5.20.0"
digest = "{zero}"

[[covers]]
key = "format-email"
arm = '{arm}'
search = "docs/openapi-surface/golden-reach-witnesses/searches/format-email.md#witness-search-exhaustive"
verdict = "exhausted"
"""
# `collect_schema_refs` walks a schema only inside the audience filter's closure,
# so its discriminator arm runs only when the fixture is generated for an audience.
AUDIENCE_ARM = r"src/openapi.rs::collect_schema_refs[if let Some\(disc\) = &schema\.discriminator \{]"
AUDIENCE_DOCUMENT = """openapi: 3.0.3
info:
  title: sample
  version: 1.0.0
paths:
  /pets:
    get:
      operationId: getPet
      x-crozier-audiences: [public]
      responses:
        "200":
          description: ok
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Pet"
components:
  schemas:
    Pet:
      type: object
      properties:
        kind:
          type: string
      required: [kind]
      discriminator:
        propertyName: kind
        mapping:
          cat: "#/components/schemas/Cat"
    Cat:
      allOf:
        - $ref: "#/components/schemas/Pet"
"""
AUDIENCE_EVIDENCE = """fern_cli_version = "5.67.1"
fern_python_sdk_version = "5.20.0"
digest = "{zero}"
{audiences}
[[covers]]
key = "discriminator-mapping"
arm = '{arm}'
search = "docs/openapi-surface/golden-reach-witnesses/searches/discriminator-mapping.md#configuration-gate"
verdict = "config-gated"
"""


class HandwrittenReachRecipeTest(unittest.TestCase):
    def fixture(self, base: Path, name: str, email: bool, arm: str = ARM) -> None:
        directory = base / name
        directory.mkdir(parents=True)
        declared = "              format: email\n" if email else ""
        (directory / "openapi.yml").write_text(DOCUMENT.format(format=declared), encoding="utf-8")
        (directory / "evidence.toml").write_text(EVIDENCE.format(zero="0" * 64, arm=arm), encoding="utf-8")

    def run_recipe(self, base: Path, ledger: Path) -> subprocess.CompletedProcess[str]:
        gates = ledger.with_name("gates.tsv")
        return subprocess.run(
            [
                "just",
                "handwritten-reach",
                "--handwritten-dir",
                str(base),
                "--ledger",
                str(ledger),
                "--gates",
                str(gates),
            ],
            cwd=REPO,
            capture_output=True,
            text=True,
            timeout=3600,
        )

    def test_the_recipe_measures_each_fixture_alone(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base, ledger = Path(temporary) / "handwritten", Path(temporary) / "reach.tsv"
            self.fixture(base, "declares-email", email=True)
            self.fixture(base, "declares-no-format", email=False)
            run = self.run_recipe(base, ledger)
            self.assertEqual(0, run.returncode, run.stdout + run.stderr)
            with ledger.open(encoding="utf-8", newline="") as handle:
                rows = list(csv.reader(handle, delimiter="\t"))
            self.assertEqual(HEADER, rows[0])
            measured = {row[0]: row for row in rows[1:]}
            self.assertEqual(["declares-email", "declares-no-format"], [row[0] for row in rows[1:]])
            for row in rows[1:]:
                self.assertEqual(["format-email", ARM], row[1:3])
            executed, total = (int(n) for n in measured["declares-email"][3:])
            self.assertGreaterEqual(total, 1)
            self.assertEqual(total, executed, "the document declaring the format did not take the arm")
            self.assertEqual(
                ["0", str(total)],
                measured["declares-no-format"][3:],
                "a document without the format still counted the arm as executed",
            )

    def test_the_recipe_generates_each_fixture_for_its_declared_audiences(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base, ledger = Path(temporary) / "handwritten", Path(temporary) / "reach.tsv"
            for name, audiences in (("for-public", 'audiences = ["public"]\n'), ("unfiltered", "")):
                directory = base / name
                directory.mkdir(parents=True)
                (directory / "openapi.yml").write_text(AUDIENCE_DOCUMENT, encoding="utf-8")
                (directory / "evidence.toml").write_text(
                    AUDIENCE_EVIDENCE.format(zero="0" * 64, audiences=audiences, arm=AUDIENCE_ARM),
                    encoding="utf-8",
                )
            run = self.run_recipe(base, ledger)
            self.assertEqual(0, run.returncode, run.stdout + run.stderr)
            with ledger.open(encoding="utf-8", newline="") as handle:
                measured = {row[0]: row for row in list(csv.reader(handle, delimiter="\t"))[1:]}
            executed, total = (int(n) for n in measured["for-public"][3:])
            self.assertGreaterEqual(total, 1)
            self.assertEqual(total, executed, "the run for the declared audience did not take the arm")
            self.assertEqual(
                ["0", str(total)],
                measured["unfiltered"][3:],
                "a fixture declaring no audience was measured with a filter",
            )
            # The configuration gate: the fixture declaring the audience is
            # measured both ways, and only it — the unfiltered one has no setting.
            with ledger.with_name("gates.tsv").open(encoding="utf-8", newline="") as handle:
                gates = list(csv.reader(handle, delimiter="\t"))
            self.assertEqual(["fixture", "key", "site", "setting", "regions_executed", "regions"], gates[0])
            self.assertEqual(
                [
                    ["for-public", "discriminator-mapping", AUDIENCE_ARM, "-", "0", str(total)],
                    ["for-public", "discriminator-mapping", AUDIENCE_ARM, "audiences=public", str(total), str(total)],
                ],
                gates[1:],
            )

    def test_a_cover_naming_an_unlisted_site_is_refused(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base, ledger = Path(temporary) / "handwritten", Path(temporary) / "reach.tsv"
            self.fixture(base, "wrong-arm", email=True, arm="src/ir.rs::base_type_ref")
            run = self.run_recipe(base, ledger)
            self.assertNotEqual(0, run.returncode)
            self.assertIn("wrong-arm: cover `format-email` arm `src/ir.rs::base_type_ref` is not a site", run.stderr)
            self.assertFalse(ledger.exists(), "a refused measurement wrote a ledger")
            self.assertFalse(ledger.with_name("gates.tsv").exists(), "a refused measurement wrote a gate ledger")


if __name__ == "__main__":
    unittest.main()
