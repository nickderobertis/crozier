#!/usr/bin/env python3
"""Drive the real `just handwritten-reach` recipe over temporary fixtures.

The recipe builds crozier instrumented and runs it over each hand-written
fixture's `openapi.yml` alone, so this is its journey rather than a mock of it:
two fixtures covering the same arm, one whose document takes it and one whose
document does not, read back from the ledger the recipe writes; one document
measured with and without the `audiences` its fixture declares; a combination
measured at its interaction branch alone, over a document declaring both of its
features and two declaring one each; and a cover naming an arm the site table
does not list, refused before anything is written. The same three documents,
joined by the golden ledger's own measurement, show the golden reach of the
interaction branch the same way.
"""

from __future__ import annotations

import csv
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
# The certified Fern pair, from its one declaration: the pair a fixture's evidence names.
CERTIFIED = json.loads((REPO / "assets" / "scaffolding" / "metadata.json").read_text(encoding="utf-8"))
PAIR_EVIDENCE = (
    f'fern_cli_version = "{CERTIFIED["cliVersion"]}"\nfern_python_sdk_version = "{CERTIFIED["generatorVersion"]}"\n'
)
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
EVIDENCE = (
    PAIR_EVIDENCE
    + """digest = "{zero}"

[[covers]]
key = "format-email"
arm = '{arm}'
search = "docs/openapi-surface/golden-reach-witnesses/searches/format-email.md#witness-search-exhaustive"
verdict = "exhausted"
"""
)
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
AUDIENCE_EVIDENCE = (
    PAIR_EVIDENCE
    + """digest = "{zero}"
{audiences}
[[covers]]
key = "discriminator-mapping"
arm = '{arm}'
search = "docs/openapi-surface/golden-reach-witnesses/searches/discriminator-mapping.md#configuration-gate"
verdict = "config-gated"
"""
)


def site_cell(key: str) -> str:
    """The `sites` cell the committed `golden-reach-sites.tsv` declares for `key`."""
    with (REPO / "docs" / "openapi-surface" / "golden-reach-sites.tsv").open(encoding="utf-8", newline="") as handle:
        return next(
            row["sites"] for row in csv.DictReader(handle, delimiter="\t", quoting=csv.QUOTE_NONE) if row["key"] == key
        )


# A combination's interaction branch, read from the committed site table for
# `combo-map-of-nullable-values`: the arm of `base_type_ref` a map takes when it or
# its value schema is nullable. The function holding it is measured whole through
# `property-residual`, the feature row the site table lists it under.
COMBINATION = "combo-map-of-nullable-values"
INTERACTION = site_cell(COMBINATION)
CONTAINING = ("property-residual", site_cell("property-residual"))
COMBINATION_DOCUMENT = """openapi: 3.0.3
info:
  title: sample
  version: 1.0.0
paths:
  /labels:
    get:
      operationId: getLabels
      responses:
        "200":
          description: ok
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Labels"
components:
  schemas:
    Labels:
{labels}"""
# Both features; the map without a nullable value; a nullable value with no map.
LABELS = {
    "map-of-nullable-values": "      type: object\n      additionalProperties:\n        type: string\n        nullable: true\n",
    "map-of-plain-values": "      type: object\n      additionalProperties:\n        type: string\n",
    "nullable-value-alone": "      type: string\n      nullable: true\n",
}
COMBINATION_EVIDENCE = (
    PAIR_EVIDENCE
    + """digest = "{zero}"

[[covers]]
key = "{key}"
search = "docs/openapi-surface/witness-search-schema-combinations-models-unions-refs/README.md#verdicts"
verdict = "exhausted"

[[covers]]
key = "{feature}"
arm = '{arm}'
search = "docs/openapi-surface/golden-reach-witnesses/searches/{feature}.md#witness-search-exhaustive"
verdict = "exhausted"
"""
)


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

    def test_a_combination_is_measured_reached_only_where_both_features_meet(self) -> None:
        """Each document runs the function holding the interaction branch; only the one
        declaring both features executes the branch itself."""
        with tempfile.TemporaryDirectory() as temporary:
            base, ledger = Path(temporary) / "handwritten", Path(temporary) / "reach.tsv"
            for name, labels in LABELS.items():
                directory = base / name
                directory.mkdir(parents=True)
                (directory / "openapi.yml").write_text(COMBINATION_DOCUMENT.format(labels=labels), encoding="utf-8")
                (directory / "evidence.toml").write_text(
                    COMBINATION_EVIDENCE.format(
                        zero="0" * 64, key=COMBINATION, feature=CONTAINING[0], arm=CONTAINING[1]
                    ),
                    encoding="utf-8",
                )
            run = self.run_recipe(base, ledger)
            self.assertEqual(0, run.returncode, run.stdout + run.stderr)
            with ledger.open(encoding="utf-8", newline="") as handle:
                rows = list(csv.reader(handle, delimiter="\t"))
            self.assertEqual(HEADER, rows[0])
            measured = {(row[0], row[1], row[2]): (int(row[3]), int(row[4])) for row in rows[1:]}
            self.assertEqual(
                {(name, key, site) for name in LABELS for key, site in ((COMBINATION, INTERACTION), CONTAINING)},
                set(measured),
                "the recipe did not measure each fixture at the interaction site and the containing function",
            )
            for name in LABELS:
                with self.subTest(document=name):
                    executed, total = measured[(name, *CONTAINING)]
                    self.assertGreater(executed, 0, f"{name} never ran the function holding the branch")
                    executed, total = measured[(name, COMBINATION, INTERACTION)]
                    self.assertGreaterEqual(total, 1)
                    if name == "map-of-nullable-values":
                        self.assertGreater(executed, 0, "the document declaring both features missed the branch")
                    else:
                        self.assertEqual(0, executed, f"{name} declares one feature, yet reached the branch")

    def test_a_cover_naming_an_unlisted_site_is_refused(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            base, ledger = Path(temporary) / "handwritten", Path(temporary) / "reach.tsv"
            self.fixture(base, "wrong-arm", email=True, arm="src/ir.rs::base_type_ref")
            run = self.run_recipe(base, ledger)
            self.assertNotEqual(0, run.returncode)
            self.assertIn("wrong-arm: cover `format-email` arm `src/ir.rs::base_type_ref` is not a site", run.stderr)
            self.assertFalse(ledger.exists(), "a refused measurement wrote a ledger")
            self.assertFalse(ledger.with_name("gates.tsv").exists(), "a refused measurement wrote a gate ledger")


def _module(name: str, script: str):
    spec = importlib.util.spec_from_file_location(name, REPO / "tools" / "surface-census" / script)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules.setdefault(name, module)
    spec.loader.exec_module(module)
    return module


class GoldenReachInteractionTest(unittest.TestCase):
    """The golden ledger's per-site reach at a combination's interaction branch.

    Each document is one run of the instrumented crozier `just golden-reach`
    builds, written as that measurement writes a golden test's executed regions
    (`tests/<test>.json` beside the build's `universe.json`), then read back and
    joined by golden-reach's own `load_coverage` and `compute`, each document the
    one witness of the combination and of the feature row measuring the function
    whole.
    """

    def test_the_interaction_arm_is_reached_only_by_the_document_declaring_both(self) -> None:
        self.assertEqual(f"{CONTAINING[1]}[", INTERACTION[: len(CONTAINING[1]) + 1], "the branch is not inside it")
        reach = _module("golden_reach_interaction", "golden-reach.py")
        handwritten = _module("handwritten_fixtures_interaction", "handwritten-fixtures.py")
        crozier = handwritten.instrumented_crozier(REPO, reach)
        profdata, llvm_cov = reach._llvm_tool("llvm-profdata"), reach._llvm_tool("llvm-cov")
        with tempfile.TemporaryDirectory() as temporary:
            out = Path(temporary) / "measurement"
            (out / "tests").mkdir(parents=True)
            for name, labels in LABELS.items():
                spec = Path(temporary) / f"{name}.yml"
                spec.write_text(COMBINATION_DOCUMENT.format(labels=labels), encoding="utf-8")
                universe, hit = handwritten.scoped_run(spec, (), crozier, profdata, llvm_cov, REPO, reach)
                (out / "tests" / f"{name}.json").write_text(json.dumps(hit), encoding="utf-8")
                (out / "universe.json").write_text(json.dumps(universe), encoding="utf-8")
            (out / "provenance.json").write_text(json.dumps({"commit": "0" * 40, "tests": 3}), encoding="utf-8")
            coverage, universe, _commit = reach.load_coverage(out)
            census = {"rows": [], "sources": [{"fixture": name} for name in LABELS]}
            feature, function = CONTAINING
            for name in LABELS:
                with self.subTest(document=name):
                    witness = (f"fixture={name}",)
                    table = {
                        COMBINATION: reach.SiteRow(COMBINATION, witness, (INTERACTION,)),
                        feature: reach.SiteRow(feature, witness, (function,)),
                    }
                    measured = {
                        row.key: row
                        for row in reach.compute(
                            {COMBINATION: "schemas", feature: "schemas"},
                            table,
                            census,
                            {other: other for other in LABELS},
                            coverage,
                            universe,
                            REPO,
                        )
                    }
                    self.assertEqual((name,), measured[COMBINATION].witnesses)
                    ((_spec, executed, _total),) = measured[feature].sites
                    self.assertGreater(executed, 0, f"{name} never ran the function holding the branch")
                    ((spec, executed, total),) = measured[COMBINATION].sites
                    self.assertEqual(INTERACTION, spec)
                    self.assertGreaterEqual(total, 1)
                    if name == "map-of-nullable-values":
                        self.assertGreater(executed, 0, "the document declaring both features missed the branch")
                    else:
                        self.assertEqual(0, executed, f"{name} declares one feature, yet reached the branch")


if __name__ == "__main__":
    unittest.main()
