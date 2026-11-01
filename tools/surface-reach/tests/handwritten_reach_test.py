#!/usr/bin/env python3
"""Drive the real `just handwritten-reach` recipe over temporary fixtures.

The recipe builds crozier instrumented and runs it over each hand-written
fixture's `openapi.yml` alone, so this is its journey rather than a mock of it:
two fixtures covering the same arm, one whose document takes it and one whose
document does not, read back from the ledger the recipe writes; one document
measured with and without the `audiences` its fixture declares; a combination
measured at its interaction branch alone, over a document declaring both of its
features and two declaring one each, and a map's discriminated value union
measured at the body its success opens against the untagged union that runs the
same call; fixtures covering combinations alone,
measured at the interaction branch or at each handler the co-occurrence audit
names; and a cover naming an arm the site table does not list, a malformed
audit and an interaction site naming no function, each refused before anything
is written. The same three documents,
joined by the golden ledger's own measurement, show the golden reach of the
interaction branch the same way.
"""

from __future__ import annotations

import csv
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from typing import IO, NamedTuple, Protocol

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
# `combo-array-of-nullable-unknown-item`: the arm of `base_type_ref` an array takes
# when its untyped item schema is nullable. The function holding it is measured whole
# through `property-residual`, the feature row the site table lists it under.
COMBINATION = "combo-array-of-nullable-unknown-item"
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
# Both features; the untyped item without `nullable`; `nullable` with no untyped item.
LABELS = {
    "array-of-nullable-unknown-items": "      type: array\n      items:\n        nullable: true\n",
    "array-of-unknown-items": "      type: array\n      items: {}\n",
    "nullable-alone": "      nullable: true\n",
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
# A fixture covering a combination alone: no arm-level cover, so the recipe measures it
# only at the combination's interaction sites.
COMBINATION_ONLY_EVIDENCE = (
    PAIR_EVIDENCE
    + """digest = "{zero}"

[[covers]]
key = "{key}"
search = "docs/openapi-surface/witness-search-schema-combinations-models-unions-refs/README.md#verdicts"
verdict = "exhausted"
"""
)
# A combination whose site cell reads `co-occurrence`: no measured branch joins both
# features, so a fixture covering it is measured at each handling function the
# committed audit names, over a document declaring security at both levels. The
# scheme is bearer: a header api key's `required` short-circuits on the document's
# own `security` before `all_operations_authenticated` runs.
COOCCURRING = "combo-document-operation-security"
SECURITY_DOCUMENT = """openapi: 3.0.3
info:
  title: sample
  version: 1.0.0
security:
  - bearer: []
paths:
  /ping:
    get:
      operationId: ping
      security:
        - bearer: []
      responses:
        "200":
          description: ok
components:
  securitySchemes:
    bearer:
      type: http
      scheme: bearer
"""


# `combo-map-of-discriminated-union`: the body `field_type_ref` enters when a
# property-less map's inline value union is one `discriminated_union` builds. The
# call opening it also runs for an ordinary multi-member value union, inside the
# `combo-map-of-oneof` arm, and for a union outside any map the property arm
# `discriminator` lists runs instead.
MAP_UNION = "combo-map-of-discriminated-union"
MAP_UNION_SITES = {
    MAP_UNION: site_cell(MAP_UNION),
    "combo-map-of-oneof": site_cell("combo-map-of-oneof"),
    "discriminator": next(
        site for site in site_cell("discriminator").split(",") if site.startswith("src/ir.rs::Builder::field_type_ref[")
    ),
}
TAGGED = """oneOf:
{indent}  - type: object
{indent}    required: [kind]
{indent}    properties:
{indent}      kind: {{type: string, enum: [single]}}
{indent}      text: {{type: string}}
{indent}  - type: object
{indent}    required: [kind]
{indent}    properties:
{indent}      kind: {{type: string, enum: [multiple]}}
{indent}      picks: {{type: array, items: {{type: string}}}}
"""
UNTAGGED = """oneOf:
{indent}  - type: string
{indent}  - type: integer
"""
MAP_UNION_DOCUMENTS = {
    # Both features: a map whose value is a union its members tag.
    "map-of-tagged-union": "type: object\n          additionalProperties:\n            "
    + TAGGED.format(indent="            "),
    # The map without the discriminated union: two untagged members.
    "map-of-untagged-union": "type: object\n          additionalProperties:\n            "
    + UNTAGGED.format(indent="            "),
    # The discriminated union without the map, at the property itself.
    "tagged-union-property": TAGGED.format(indent="          "),
}
MAP_UNION_COMPONENTS = """openapi: 3.0.3
info:
  title: sample
  version: 1.0.0
paths:
  /answers:
    get:
      operationId: getAnswers
      responses:
        "200":
          description: ok
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Answers"
components:
  schemas:
    Answers:
      type: object
      properties:
        byQuestion:
          {value}"""
MAP_UNION_EVIDENCE = (
    PAIR_EVIDENCE
    + """digest = "{zero}"

[[covers]]
key = "combo-map-of-discriminated-union"
search = "docs/openapi-surface/witness-search-schema-combinations-models-unions-refs/README.md#verdicts"
verdict = "exhausted"

[[covers]]
key = "combo-map-of-oneof"
search = "docs/openapi-surface/witness-search-schema-combinations-models-unions-refs/README.md#verdicts"
verdict = "exhausted"

[[covers]]
key = "discriminator"
arm = '{arm}'
search = "docs/openapi-surface/golden-reach-witnesses/searches/discriminator.md#witness-search-exhaustive"
verdict = "exhausted"
"""
)


def golden_reach():
    return _module("golden_reach_recipe", "golden-reach.py")


def cooccurrence_handlers(key: str) -> list[str]:
    """The handling functions the committed `combination-cooccurrence.tsv` names for `key`."""
    reach = golden_reach()
    audit, failures = reach.read_cooccurrence(REPO / "docs" / "openapi-surface" / "combination-cooccurrence.tsv")
    if failures:
        raise AssertionError(failures)
    return reach.handler_specs(audit[key].handlers)


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
                    if name == "array-of-nullable-unknown-items":
                        self.assertGreater(executed, 0, "the document declaring both features missed the branch")
                    else:
                        self.assertEqual(0, executed, f"{name} declares one feature, yet reached the branch")

    def test_a_map_value_union_reaches_its_interaction_body_only_when_discriminated(self) -> None:
        """The map of a tagged union, the map of an untagged one and the tagged union
        outside any map each run `field_type_ref`; only the first enters the body
        `discriminated_union`'s success opens, though the second runs that call too."""
        with tempfile.TemporaryDirectory() as temporary:
            base, ledger = Path(temporary) / "handwritten", Path(temporary) / "reach.tsv"
            for name, value in MAP_UNION_DOCUMENTS.items():
                directory = base / name
                directory.mkdir(parents=True)
                (directory / "openapi.yml").write_text(MAP_UNION_COMPONENTS.format(value=value), encoding="utf-8")
                (directory / "evidence.toml").write_text(
                    MAP_UNION_EVIDENCE.format(zero="0" * 64, arm=MAP_UNION_SITES["discriminator"]), encoding="utf-8"
                )
            run = self.run_recipe(base, ledger)
            self.assertEqual(0, run.returncode, run.stdout + run.stderr)
            with ledger.open(encoding="utf-8", newline="") as handle:
                rows = list(csv.reader(handle, delimiter="\t"))
            self.assertEqual(HEADER, rows[0])
            executed = {(row[0], row[1], row[2]): int(row[3]) for row in rows[1:]}
            self.assertEqual(
                {(name, key, site) for name in MAP_UNION_DOCUMENTS for key, site in MAP_UNION_SITES.items()},
                set(executed),
                "the recipe did not measure each fixture at all three sites",
            )
            reached = {
                name: {key for key, site in MAP_UNION_SITES.items() if executed[(name, key, site)] > 0}
                for name in MAP_UNION_DOCUMENTS
            }
            self.assertEqual(
                {
                    "map-of-tagged-union": {MAP_UNION, "combo-map-of-oneof"},
                    # The map's value union runs `discriminated_union`, which returns
                    # `None` for untagged members: the body stays unreached.
                    "map-of-untagged-union": {"combo-map-of-oneof"},
                    "tagged-union-property": {"discriminator"},
                },
                reached,
            )

    def test_a_fixture_covering_only_combinations_is_measured_at_each_interaction_site(self) -> None:
        """A fixture with no arm-level cover still runs: at the combination's interaction
        branch, or at every handler the co-occurrence audit names when no branch joins
        both features; no configuration gate is written for either."""
        handlers = cooccurrence_handlers(COOCCURRING)
        self.assertEqual(
            "co-occurrence",
            site_cell(COOCCURRING),
            f"{COOCCURRING} no longer reads `co-occurrence`; pick a key the site table measures by its handlers",
        )
        with tempfile.TemporaryDirectory() as temporary:
            base, ledger = Path(temporary) / "handwritten", Path(temporary) / "reach.tsv"
            for name, key, document in (
                (
                    "nullable-map-only",
                    COMBINATION,
                    COMBINATION_DOCUMENT.format(labels=LABELS["array-of-nullable-unknown-items"]),
                ),
                ("security-both-levels", COOCCURRING, SECURITY_DOCUMENT),
            ):
                directory = base / name
                directory.mkdir(parents=True)
                (directory / "openapi.yml").write_text(document, encoding="utf-8")
                (directory / "evidence.toml").write_text(
                    COMBINATION_ONLY_EVIDENCE.format(zero="0" * 64, key=key), encoding="utf-8"
                )
            run = self.run_recipe(base, ledger)
            self.assertEqual(0, run.returncode, run.stdout + run.stderr)
            with ledger.open(encoding="utf-8", newline="") as handle:
                rows = list(csv.reader(handle, delimiter="\t"))
            self.assertEqual(HEADER, rows[0])
            measured = {(row[0], row[1], row[2]): (int(row[3]), int(row[4])) for row in rows[1:]}
            expected = {("nullable-map-only", COMBINATION, INTERACTION)} | {
                ("security-both-levels", COOCCURRING, handler) for handler in handlers
            }
            self.assertEqual(expected, set(measured), "a combination-only fixture was not measured at its sites")
            for site, (executed, total) in measured.items():
                with self.subTest(site=site):
                    self.assertGreaterEqual(total, 1)
                    self.assertGreater(executed, 0, f"{site[0]} declares both features, yet missed {site[2]}")
            with ledger.with_name("gates.tsv").open(encoding="utf-8", newline="") as handle:
                self.assertEqual(
                    [["fixture", "key", "site", "setting", "regions_executed", "regions"]],
                    list(csv.reader(handle, delimiter="\t")),
                )
            self.assertIn(
                f"measured 0 arm-level cover(s) and {len(expected)} combination interaction site(s) into {ledger}, "
                f"0 configuration gate(s) into {ledger.with_name('gates.tsv')}",
                run.stdout,
            )

    def measure_in(self, root: Path) -> tuple[subprocess.CompletedProcess[str], Path]:
        """`measure` over one combination-only fixture, reading the site table and audit
        under `root`; refusals land before the instrumented build."""
        base, ledger = root / "handwritten", root / "reach.tsv"
        directory = base / "nullable-map-only"
        directory.mkdir(parents=True)
        (directory / "openapi.yml").write_text(
            COMBINATION_DOCUMENT.format(labels=LABELS["array-of-nullable-unknown-items"]), encoding="utf-8"
        )
        (directory / "evidence.toml").write_text(
            COMBINATION_ONLY_EVIDENCE.format(zero="0" * 64, key=COMBINATION), encoding="utf-8"
        )
        run = subprocess.run(
            [
                sys.executable,
                str(REPO / "tools" / "surface-census" / "handwritten-fixtures.py"),
                "--repo-root",
                str(root),
                "measure",
                "--handwritten-dir",
                str(base),
                "--ledger",
                str(ledger),
                "--gates",
                str(ledger.with_name("gates.tsv")),
            ],
            capture_output=True,
            text=True,
            timeout=600,
        )
        return run, ledger

    def staged_surface(self, root: Path) -> Path:
        surface = root / "docs" / "openapi-surface"
        surface.mkdir(parents=True)
        for name in ("golden-reach-sites.tsv", "combination-cooccurrence.tsv"):
            shutil.copyfile(REPO / "docs" / "openapi-surface" / name, surface / name)
        shutil.copytree(REPO / "src", root / "src")
        return surface

    def test_a_malformed_cooccurrence_audit_is_refused_before_measuring(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            audit = self.staged_surface(root) / "combination-cooccurrence.tsv"
            lines = audit.read_text(encoding="utf-8").splitlines(keepends=True)
            audit.write_text(lines[0].replace("handlers", "functions") + "".join(lines[1:]), encoding="utf-8")
            run, ledger = self.measure_in(root)
            self.assertNotEqual(0, run.returncode)
            self.assertIn(
                "handwritten-reach: combination-cooccurrence.tsv: the header line must be exactly", run.stderr
            )
            self.assertNotIn("Traceback", run.stderr)
            self.assertFalse(ledger.exists(), "a refused measurement wrote a ledger")
            # Restored, the same tree passes the audit and reaches site resolution.
            audit.write_text("".join(lines), encoding="utf-8")
            self.assertEqual([], golden_reach().read_cooccurrence(audit)[1])

    def test_an_interaction_site_naming_no_function_is_refused_before_measuring(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            sites = self.staged_surface(root) / "golden-reach-sites.tsv"
            text = sites.read_text(encoding="utf-8")
            missing = "src/ir.rs::no_such_interaction_branch"
            row = next(line for line in text.splitlines() if line.startswith(f"{COMBINATION}\t"))
            self.assertIn(f"\t{INTERACTION}\t", row)
            sites.write_text(
                text.replace(row, row.replace(f"\t{INTERACTION}\t", f"\t{missing}\t", 1)), encoding="utf-8"
            )
            run, ledger = self.measure_in(root)
            self.assertNotEqual(0, run.returncode)
            self.assertIn(f"site {missing!r} matches 0 functions", run.stderr)
            self.assertNotIn("Traceback", run.stderr)
            self.assertFalse(ledger.exists(), "a refused measurement wrote a ledger")
            self.assertFalse(ledger.with_name("gates.tsv").exists(), "a refused measurement wrote a gate ledger")

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
                    if name == "array-of-nullable-unknown-items":
                        self.assertGreater(executed, 0, "the document declaring both features missed the branch")
                    else:
                        self.assertEqual(0, executed, f"{name} declares one feature, yet reached the branch")


ECHO_FLAG = r"src/emit.rs::append_request_call_args[=^ {28}&& ep\.body_response_same_ref$]"


# A co-occurrence row whose two features meet in one condition, but whose
# qualifying outcome no counter region's execution implies, is held to an
# outcome proof instead: `combination-cooccurrence.tsv`'s `why_no_branch` for
# each key below names this test. Each case runs the instrumented crozier over
# a from-scratch document declaring both features and over a control declaring
# one, and asserts which operands of that condition ran and what each generated.
def operation_document(paths: str, components: str = "", security: str = "") -> str:
    return (
        "openapi: 3.0.3\ninfo:\n  title: sample\n  version: 1.0.0\n"
        + security
        + "paths:\n"
        + paths
        + ("components:\n" + components if components else "")
    )


def responses(content: str) -> str:
    return (
        "  /archive:\n    get:\n      operationId: getArchive\n      responses:\n"
        '        "200":\n          description: ok\n          content:\n' + content
    )


def optional_body(schema: str) -> str:
    return (
        "  /labels:\n    post:\n      operationId: setLabels\n      requestBody:\n        required: false\n"
        "        content:\n          application/json:\n            schema:\n"
        + schema
        + '      responses:\n        "204":\n          description: done\n'
    )


OPTIONAL_BODY_SCHEMAS = (
    "    Labels:\n      type: object\n      additionalProperties:\n        type: string\n"
    "    Pick:\n      oneOf:\n        - type: string\n        - type: integer\n"
)
ECHO_PATHS = (
    "  /kennels:\n    post:\n      operationId: createKennel\n      requestBody:\n        content:\n"
    "          application/xml:\n            schema:\n              type: object\n"
    '          application/json:\n            schema:\n              $ref: "#/components/schemas/Kennel"\n'
    '      responses:\n        "200":\n          description: ok\n          content:\n            application/json:\n'
    '              schema:\n                $ref: "#/components/schemas/Kennel"\n'
)
KENNEL = "    Kennel:\n      type: object\n      properties:\n        name:\n          type: string\n"
BEARER = "  securitySchemes:\n    bearerAuth:\n      type: http\n      scheme: bearer\n"
ENTRY = (
    '  /entries:\n    get:\n      operationId: getEntry\n      responses:\n        "200":\n'
    "          description: ok\n          content:\n            application/json:\n              schema:\n"
    '                $ref: "#/components/schemas/Entry"\n'
)


def entry_schemas(memo: str) -> str:
    return (
        "    Entry:\n      type: object\n      required: [memo]\n      properties:\n        memo:\n"
        "          description: A note kept beside the entry.\n          allOf:\n"
        '            - $ref: "#/components/schemas/Memo"\n            - description: The wording.\n'
        "    Memo:\n      type: string\n" + memo
    )


def parcel_query(schema: str) -> str:
    return (
        "  /parcels:\n    get:\n      operationId: findParcels\n      parameters:\n        - name: code\n"
        "          in: query\n          required: true\n          example: param-sample\n          schema:\n"
        + schema
        + '      responses:\n        "204":\n          description: done\n'
    )


def craft_path(target: str) -> str:
    return (
        "  /craft/{kind}:\n    get:\n      operationId: listCraft\n      parameters:\n        - name: kind\n"
        f'          in: path\n          required: true\n          schema:\n            $ref: "#/components/schemas/{target}"\n'
        '      responses:\n        "204":\n          description: done\n'
    )


CRAFT = (
    "    Kind:\n      type: string\n      enum: [glider, balloon]\n"
    "    Slot:\n      type: object\n      properties:\n        bay:\n          type: string\n"
)


def watch(method_name: str) -> str:
    return (
        "  /widgets/watch:\n    post:\n      operationId: watchEvents\n"
        + method_name
        + "      x-fern-streaming:\n        format: sse\n"
        '        response: { $ref: "#/components/schemas/Event" }\n'
        '        response-stream: { $ref: "#/components/schemas/Event" }\n'
        "        stream-condition: $request.stream\n      requestBody:\n        required: true\n"
        "        content:\n          application/json:\n            schema:\n"
        '              $ref: "#/components/schemas/WatchFilter"\n      responses:\n        "200":\n'
        "          description: events\n          content:\n            application/json:\n"
        '              schema: { $ref: "#/components/schemas/Event" }\n            text/event-stream:\n'
        '              schema: { $ref: "#/components/schemas/Event" }\n'
    )


WATCH = (
    "    WatchFilter:\n      type: object\n      properties:\n        stream:\n          type: boolean\n"
    "    Event:\n      type: object\n      properties:\n        kind:\n          type: string\n"
)


def secured(operation_security: str) -> str:
    return (
        "  /vaults:\n    get:\n      operationId: listVaults\n"
        + operation_security
        + '      responses:\n        "204":\n          description: done\n'
    )


class ReachSite(Protocol):
    """A resolved `golden-reach-sites.tsv` site: its file, and which counter regions it holds."""

    @property
    def file(self) -> str: ...

    def holds(self, region: tuple[int, int, int, int]) -> bool: ...


class ReachMeasurement(Protocol):
    """What these proofs call of `golden-reach.py`, which loads by path, so has no importable type."""

    def _llvm_tool(self, name: str) -> str: ...

    def run_llvm(self, argv: list[str], stdout: IO[str] | None = None) -> None: ...

    def _covered(self, export: Path, repo_root: Path) -> tuple[dict, dict]: ...

    def resolve_site(self, spec: str, repo_root: Path = ...) -> ReachSite: ...


class Run(NamedTuple):
    """One document's expected outcome: the sites that ran, those that did not, and
    `(file under src/fern, text)` pairs its generated SDK holds and lacks."""

    document: str
    ran: tuple[str, ...] = ()
    skipped: tuple[str, ...] = ()
    holds: tuple[tuple[str, str], ...] = ()
    lacks: tuple[tuple[str, str], ...] = ()


class Outcome(NamedTuple):
    key: str
    both: Run
    control: Run


BINARY = "src/ir.rs::is_binary_response"
JSON_OPERAND = BINARY + r'[=^ {16}&& !resp\.content\.contains_key\("application/json"\)$]'
SCHEMA_DISJUNCT = BINARY + r"[=^ {16}\x7c\x7c resp\.content\.values\(\)\.any]"
FORMAT_OPERAND = BINARY + r'[=^ {28}&& schema\.format\.as_deref\(\) == Some\("binary"\)$]'
TEXT_OPERAND = BINARY + r"[=is_text_response_media\(media_type\)$]"
PASSED_WHOLE = r"src/ir.rs::resolve_request_body[=^ {8}\x7c\x7c passed_whole$]"
INLINE_MAP = r"src/ir.rs::resolve_request_body[=^ {8}\x7c\x7c is_map\(schema\)$]"
TARGET_NULLABLE = r"src/ir.rs::Builder::collect_fields[=\.is_some_and\(\x7ctarget\x7c schema_accepts_none\(target, self\.schemas\)\);$]"
NOT_REQUIRED = r"src/ir.rs::Builder::collect_fields[=!spec_required;$]"
SCHEMA_EXAMPLE = r"src/ir.rs::parameter_example_value[=parameter\.schema\.as_ref\(\)\.and_then\(typed_schema_example\)]"
URL_SCALARS = r"src/ir.rs::build_endpoint[=^ {20}&& !hoister\.reaches_url_as_scalars\(&type_ref\),$]"
NAMED_STREAM = r"src/ir.rs::stream_condition_method_names[if op\.sdk_method_name\(\)\.is_some\(\) \{]"
ID_STREAM = r"src/ir.rs::stream_condition_method_names[\} else if !id\.is_empty\(\) \{]"
UNAUTHENTICATED = r"src/ir.rs::all_operations_authenticated[if !authed \{]"
CLIENT, RAW = "client.py", "raw_client.py"
STREAMS = "typing.Iterator[bytes]"
# The constructor's bearer credential, optional; `async_token` is optional always.
OPTIONAL_TOKEN = "        token: typing.Optional["

TALLY = (
    '  /tallies:\n    get:\n      operationId: getTally\n      responses:\n        "200":\n'
    "          description: ok\n          content:\n            application/json:\n              schema:\n"
    '                $ref: "#/components/schemas/Tally"\n'
)


def tally(schemas: str) -> str:
    return operation_document(TALLY, "  schemas:\n" + schemas)


TALLY_MEMBERS = (
    "      allOf:\n"
    '        - $ref: "#/components/schemas/Kennel"\n'
    "        - type: object\n          properties:\n            count:\n              type: integer\n"
)
PEN = (
    "    Tally:\n      required: [badge]\n      allOf:\n"
    '        - $ref: "#/components/schemas/Pen"\n'
    "        - type: object\n          properties:\n            count:\n              type: integer\n"
    "    Pen:\n      type: object\n      properties:\n        badge:\n"
    '          $ref: "#/components/schemas/Badge"\n'
    "    Badge:\n      type: string\n"
)
PINNED = (
    "    Tally:\n      type: object\n      required: [badge]\n      properties:\n        badge:\n"
    '          $ref: "#/components/schemas/Badge"\n'
    "    Badge:\n      type: string\n"
)
VALUES = "          additionalProperties:\n            type: integer\n"
SIZED = (
    "          additionalProperties:\n            type: object\n"
    "            properties:\n              size:\n                type: integer\n"
)
PICK = "          anyOf:\n            - type: string\n            - type: integer\n"


def counts(schema: str) -> str:
    return tally(
        "    Tally:\n      type: object\n      properties:\n        counts:\n          type: object\n" + schema
    )


def rejected(body: str) -> str:
    return operation_document(
        '  /kennels:\n    get:\n      operationId: getKennel\n      responses:\n        "200":\n'
        "          description: ok\n          content:\n            application/json:\n              schema:\n"
        '                $ref: "#/components/schemas/Kennel"\n        "400":\n          description: rejected\n'
        "          content:\n            application/json:\n              schema:\n                type: object\n"
        + body,
        "  schemas:\n" + KENNEL,
    )


def emptied(statuses: str) -> str:
    return operation_document(
        '  /kennels:\n    get:\n      operationId: getKennel\n      responses:\n        "200":\n'
        "          description: ok\n          content:\n            application/json:\n              schema:\n"
        '                $ref: "#/components/schemas/Kennel"\n' + statuses,
        "  schemas:\n" + KENNEL,
    )


FLATTEN_ALL = r"src/ir.rs::Builder::add_object[let inlined_by_base = if flatten_all \{]"
PROMOTED = r"src/ir.rs::promote_required_parent_properties[if !required && !read_only \{]"
MAP_ARM = r"src/ir.rs::base_type_ref[^ {4}if is_map\(schema\) \{]"
MAP_ANY_OF = r"src/ir.rs::base_type_ref[=\x7c\x7c schema\.any_of\.is_some\(\)\);]"
NULLABLE_VALUES = r"src/ir.rs::base_type_ref[if is_optional\(schema\) \x7c\x7c is_optional\(value\) \{]"
VALUE_HOIST = (
    r"src/ir.rs::Builder::field_type_ref[if prop_schema\.properties\.is_empty\(\) && value\.reference\.is_none\(\) \{]"
)
VALUE_PROPERTIES = (
    r"src/ir.rs::Builder::field_type_ref[=prop_schema\.properties\.is_empty\(\) && value\.reference\.is_none\(\)]"
)
VALUE_UNREFERENCED = r"src/ir.rs::Builder::field_type_ref[=&& value\.reference\.is_none\(\) \{$]"
NULLABLE_TARGET = r"src/ir.rs::referenced_schema_accepts_none[if target\.nullable_at_references\(\) \{]"
READ_ONLY_OPERAND = r"src/ir.rs::promote_required_parent_properties[=!read_only \{]"
ERROR_STRUCT = r"src/ir.rs::hoist_error_body_types[if is_inline_struct\(schema\) \{]"
BODYLESS = r"src/ir.rs::build_endpoint[if has_bodyless_success\(response_op\) && !has_text_response\(response_op\) \{]"
OPTIONAL_ARM = r"src/ir.rs::build_endpoint[=other => optional_type_ref\(other\),]"


# The echo guard's last operand, which the anonymous and OAuth2 echo rows audit as
# their shared condition rather than declare as an interaction site.
ECHO_ARM = r"src/emit.rs::append_request_call_args[=^ {28}&& !ep\.body_schema_titled$]"
ECHO_GUARD = r"src/ir.rs::body_response_same_ref[^ {4}\{$]"
BASIC_REQUIRED = r"src/emit.rs::auth_wrapper_parts[=^ {16}format!\(.*httpx\.BasicAuth\(self\._get_]"
OBJECT_QUERY = r"src/ir.rs::requires_object_query[=!schema\.properties\.is_empty\(\)]"
HEADER_ENUM_ARM = r"src/emit.rs::append_request_call_args[let value = if header_param\.enum_value]"
QUERY_EXAMPLE_DROPPED = r"src/ir.rs::build_endpoint[let example = if omit_synthesized_example]"
QUERY_EXAMPLE_TAKEN = r"src/ir.rs::build_endpoint[=^ {16}query_parameter_example\(doc, p\)$]"
ALIASED_TEMPORAL = (
    r"src/ir.rs::build_endpoint[=TypeRef::Primitive\(prim @ \(Prim::Date \x7c Prim::Datetime\)\) => Some\(prim\)]"
)
BODY_COLLISION = r"src/ir.rs::build_endpoint[if let Some\(prefix\) = &field\.collision_prefix]"
QUERY_UNION_GLOBAL = r"src/ir.rs::parameter_union_is_global[=parameter\.required\.unwrap_or\(false\) == nullable]"
ONE_OR_MANY = r"src/ir.rs::one_or_many_query_schema[=let nullable = non_null\.len\(\) < members\.len\(\)]"
BASIC = "  securitySchemes:\n    basicAuth:\n      type: http\n      scheme: basic\n"
OAUTH = (
    "  securitySchemes:\n    kennelOAuth:\n      type: oauth2\n      flows:\n        clientCredentials:\n"
    "          tokenUrl: https://kennels.example.com/token\n          scopes: {}\n"
)
# The client wrapper's header line for required basic credentials.
REQUIRED_BASIC = "httpx.BasicAuth(self._get_username(), self._get_password())"
TALLY_FILTER = (
    "    TallyFilter:\n      type: object\n      properties:\n        marks:\n          type: array\n"
    "          items:\n            type: string\n    TallyCode:\n      type: string\n"
)
EXAMPLED_CRAFT = (
    "    Rig:\n      type: string\n      enum: [glider, balloon]\n      example: balloon\n"
    "    Tag:\n      type: string\n      example: hangar-nine\n"
    "    Landed:\n      type: string\n      format: date-time\n"
)
HANGAR_BAY = "hangars/raw_client.py"


def tally_query(schema: str) -> str:
    return (
        "  /tallies:\n    get:\n      operationId: listTallies\n      parameters:\n        - name: filter\n"
        "          in: query\n          required: true\n          schema:\n"
        + schema
        + "        - name: ids\n          in: query\n          required: true\n          schema:\n"
        "            type: array\n            items:\n              type: string\n"
        '      responses:\n        "204":\n          description: done\n'
    )


def craft_query(target: str) -> str:
    return (
        "  /craft:\n    get:\n      operationId: listCraft\n      parameters:\n        - name: kind\n"
        f'          in: query\n          required: true\n          schema:\n            $ref: "#/components/schemas/{target}"\n'
        '      responses:\n        "204":\n          description: done\n'
    )


# A second operation without the header keeps it a per-call argument, not a client-wide global.
def craft_header(target: str) -> str:
    return (
        "  /craft:\n    get:\n      operationId: listCraft\n      parameters:\n        - name: X-Craft-Kind\n"
        f'          in: header\n          required: true\n          schema:\n            $ref: "#/components/schemas/{target}"\n'
        '      responses:\n        "204":\n          description: done\n'
        '  /hangars:\n    get:\n      operationId: listHangars\n      responses:\n        "204":\n          description: done\n'
    )


def locker_claim(header: str) -> str:
    return (
        "  /lockers/{lockerId}/claims:\n    post:\n      operationId: claimLocker\n      parameters:\n"
        "        - name: lockerId\n          in: path\n          required: true\n          schema:\n            type: string\n"
        f"        - name: {header}\n          in: header\n          schema:\n            type: string\n"
        "      requestBody:\n        required: true\n        content:\n          application/json:\n            schema:\n"
        "              type: object\n              properties:\n                owner:\n                  type: string\n"
        "                shelf:\n                  type: string\n"
        '      responses:\n        "204":\n          description: done\n'
        '  /lockers:\n    get:\n      operationId: listLockers\n      responses:\n        "204":\n          description: done\n'
    )


def tagged_union(location: str, keyword: str) -> str:
    return (
        "  /hangars:\n    get:\n      operationId: listHangars\n      tags: [hangars]\n      parameters:\n"
        f"        - name: bay\n          in: {location}\n          schema:\n            {keyword}:\n"
        "              - type: string\n              - type: integer\n"
        '      responses:\n        "204":\n          description: done\n'
        '  /runways:\n    get:\n      operationId: listRunways\n      tags: [hangars]\n      responses:\n        "204":\n          description: done\n'
    )


FORM_JSON_MEDIA = r"src/ir.rs::resolve_request_body[if selected_json_request_media\(rb\)\.is_some\(\) \{]"
FORM_UNION = r"src/ir.rs::resolve_request_body[if let Some\(members\) = obj\.one_of\.as_ref\(\)\.or\(obj\.any_of\.as_ref\(\)\) \{]"
FORM_UNION_SUFFIX = r"src/ir.rs::resolve_request_body[^ {20}let name = if union_body_suffix \{]"
UNION_BODY_SUFFIX = r"src/ir.rs::resolve_request_body[^ {8}let request_body_name = if union_body_suffix \{]"
COMPOSED_MEDIA_EXAMPLE = (
    r"src/emit.rs::build_example_inner[let mut example_fields: Vec<&BodyField> = if composed_request_media_example \{]"
)
FALLBACKS_ONLY = r"src/ir.rs::resolve_request_body[=Some\(_\) => ComponentExamplePolicy::PropertyFallbacksOnly,]"
UNION_EXAMPLE = r"src/emit.rs::ExampleCtx::value_from_example[if let TypeRef::Union\(variants\) = t \{]"
MATCHED_VARIANT = r"src/emit.rs::ExampleCtx::value_from_example[if self\.example_matches_type\(variant, &value\) \{]"
MULTIPART_CLAIMS = r"src/ir.rs::rename_claimed_path_params[Some\(RequestBody::Form\(form\)\) if form\.multipart => \{]"
CLAIMED_RENAME = (
    r'src/ir.rs::rename_claimed_path_params[=let mut renamed = format!\("\{\}PathParam", param\.wire_name\);]'
)


def tally_post(content: str, parameters: str = "") -> str:
    return (
        "  /tallies:\n    post:\n      operationId: postTally\n"
        + parameters
        + "      requestBody:\n        content:\n"
        + content
        + '      responses:\n        "204":\n          description: done\n'
    )


TALLY_JSON = "          application/json:\n            schema:\n"
TALLY_FORM = "          application/x-www-form-urlencoded:\n            schema:\n"
TALLY_QUERY = (
    "      parameters:\n        - name: ledger\n          in: query\n          schema:\n            type: string\n"
)
TALLY_UNION = (
    "              oneOf:\n                - type: object\n                  properties:\n                    count:\n"
    "                      type: integer\n                - type: object\n                  properties:\n"
    "                    label:\n                      type: string\n"
)
TALLY_ANY = TALLY_UNION.replace("oneOf", "anyOf")
LITTER = (
    "              required: [size]\n              properties:\n                note:\n                  type: string\n"
    "                size:\n                  type: integer\n"
)
KENNEL_BASE = '              allOf:\n                - $ref: "#/components/schemas/Kennel"\n'
LITTER_EXAMPLE = "            example:\n              name: Rex\n              note: tidy\n              size: 3\n"
PUPPY = (
    '    Puppy:\n      allOf:\n        - $ref: "#/components/schemas/Kennel"\n'
    "        - type: object\n          required: [size]\n          properties:\n            note:\n"
    "              type: string\n            size:\n              type: integer\n"
    "      example:\n        name: Max\n        note: messy\n        size: 9\n"
)
PUPPY_BODY = '              $ref: "#/components/schemas/Puppy"\n'
PUPPY_EXAMPLE = "            example:\n              name: Rex\n              size: 3\n"
PENS = (
    "    Hutch:\n      type: object\n      required: [name]\n      properties:\n        name:\n          type: string\n"
    "    Cage:\n      type: object\n      required: [width]\n      properties:\n        width:\n          type: integer\n"
)


def crate(union: str, example: str = "") -> str:
    return (
        f"    Crate:\n      type: object\n      required: [pen]\n      properties:\n        pen:\n          {union}:\n"
        '            - $ref: "#/components/schemas/Hutch"\n            - $ref: "#/components/schemas/Cage"\n'
        + example
        + PENS
    )


CRATE_BODY = (
    "              type: object\n              required: [crate]\n              properties:\n                crate:\n"
    '                  $ref: "#/components/schemas/Crate"\n'
)
CAGE_EXAMPLE = "          example:\n            width: 4\n"
PERCH = (
    '    Perch:\n      oneOf:\n        - $ref: "#/components/schemas/Hutch"\n        - $ref: "#/components/schemas/Cage"\n'
    + PENS
)
PERCH_BODY = '              $ref: "#/components/schemas/Perch"\n'
PERCH_EXAMPLE = "            example:\n              width: 4\n"


def bay(body: str) -> str:
    return (
        "  /bays/{slot}:\n    post:\n      operationId: loadBay\n      parameters:\n        - name: slot\n"
        "          in: path\n          required: true\n          schema:\n            type: string\n"
        + body
        + '      responses:\n        "204":\n          description: done\n'
    )


BAY_MULTIPART = (
    "      requestBody:\n        content:\n          multipart/form-data:\n            schema:\n"
    "              type: object\n              properties:\n                slot:\n                  type: string\n"
    "                manifest:\n                  type: string\n                  format: binary\n"
)


OUTCOMES = (
    # Required non-OAuth security holds the echo flag false: the guard reads it, the
    # echo operand after it never runs, and the header the anonymous echo drops stays.
    Outcome(
        "combo-echo-body-effective-non-oauth-required",
        Run(
            operation_document(ECHO_PATHS, BEARER + "  schemas:\n" + KENNEL, "security:\n  - bearerAuth: []\n"),
            ran=(ECHO_FLAG,),
            skipped=(ECHO_ARM,),
            holds=((RAW, '"content-type": "application/json"'),),
        ),
        Run(
            operation_document(ECHO_PATHS, "  schemas:\n" + KENNEL),
            ran=(ECHO_FLAG, ECHO_ARM),
            lacks=((RAW, '"content-type"'),),
        ),
    ),
    # A download first beside JSON: `!json` reads false, so the binary-schema
    # disjunct runs, and the method returns JSON where a download alone streams.
    Outcome(
        "combo-success-json-beside-download",
        Run(
            operation_document(
                responses(
                    "            application/octet-stream: {}\n            application/json:\n              schema:\n                type: object\n"
                )
            ),
            ran=(JSON_OPERAND, SCHEMA_DISJUNCT),
            lacks=((CLIENT, STREAMS),),
        ),
        Run(
            operation_document(responses("            application/octet-stream: {}\n")),
            ran=(JSON_OPERAND,),
            skipped=(SCHEMA_DISJUNCT,),
            holds=((CLIENT, STREAMS),),
        ),
    ),
    # A binary schema beside JSON: `!json` reads false and the binary-schema
    # disjunct decides, streaming where the same media without the schema does not.
    Outcome(
        "combo-success-json-beside-binary-schema",
        Run(
            operation_document(
                responses(
                    "            application/json:\n              schema:\n                type: object\n            application/octet-stream:\n              schema:\n                type: string\n                format: binary\n"
                )
            ),
            ran=(JSON_OPERAND, FORMAT_OPERAND),
            holds=((CLIENT, STREAMS),),
        ),
        Run(
            operation_document(
                responses(
                    "            application/json:\n              schema:\n                type: object\n            application/octet-stream:\n              schema: {}\n"
                )
            ),
            ran=(JSON_OPERAND,),
            skipped=(FORMAT_OPERAND,),
            lacks=((CLIENT, STREAMS),),
        ),
    ),
    # Text first beside a download: the text operand of `download_first` reads it, so
    # `!json` never runs and the method returns `str` where the download streams.
    Outcome(
        "combo-success-text-beside-download",
        Run(
            operation_document(
                responses(
                    "            text/plain:\n              schema:\n                type: string\n            application/octet-stream: {}\n"
                )
            ),
            ran=(TEXT_OPERAND,),
            skipped=(JSON_OPERAND,),
            holds=((CLIENT, "-> str:"),),
        ),
        Run(
            operation_document(responses("            application/octet-stream: {}\n")),
            ran=(JSON_OPERAND,),
            skipped=(TEXT_OPERAND,),
            holds=((CLIENT, STREAMS),),
        ),
    ),
    # An optional body naming a map is passed whole: `passed_whole` reads true, the
    # inline-map operand after it never runs, and the request argument is required.
    Outcome(
        "combo-optional-ref-map-body",
        Run(
            operation_document(
                optional_body('              $ref: "#/components/schemas/Labels"\n'),
                "  schemas:\n" + OPTIONAL_BODY_SCHEMAS,
            ),
            ran=(PASSED_WHOLE,),
            skipped=(INLINE_MAP,),
            holds=((CLIENT, "*, request: Labels,"),),
        ),
        Run(
            operation_document(
                optional_body(
                    "              type: object\n              additionalProperties:\n                type: string\n"
                )
            ),
            ran=(PASSED_WHOLE, INLINE_MAP),
            holds=((CLIENT, "request: typing.Optional["),),
        ),
    ),
    Outcome(
        "combo-optional-ref-union-body",
        Run(
            operation_document(
                optional_body('              $ref: "#/components/schemas/Pick"\n'),
                "  schemas:\n" + OPTIONAL_BODY_SCHEMAS,
            ),
            ran=(PASSED_WHOLE,),
            skipped=(INLINE_MAP,),
            holds=((CLIENT, "*, request: Pick,"),),
        ),
        Run(
            operation_document(
                optional_body(
                    "              type: object\n              additionalProperties:\n                type: string\n"
                )
            ),
            ran=(PASSED_WHOLE, INLINE_MAP),
            holds=((CLIENT, "request: typing.Optional["),),
        ),
    ),
    # An annotated reference to a nullable target reads the target's nullability, so
    # the required property is optional without consulting `required` at all.
    Outcome(
        "combo-annotated-ref-to-nullable-target",
        Run(
            operation_document(ENTRY, "  schemas:\n" + entry_schemas("      nullable: true\n")),
            ran=(TARGET_NULLABLE,),
            skipped=(NOT_REQUIRED,),
            holds=(("types/entry.py", "memo: typing.Optional[str]"),),
        ),
        Run(
            operation_document(ENTRY, "  schemas:\n" + entry_schemas("")),
            ran=(TARGET_NULLABLE, NOT_REQUIRED),
            holds=(("types/entry.py", "memo: str ="),),
        ),
    ),
    # A parameter example beside a `$ref` schema is filtered out, so the referenced
    # schema's example is read instead; beside an inline string it is kept.
    Outcome(
        "combo-param-example-beside-ref-schema",
        Run(
            operation_document(
                parcel_query('            $ref: "#/components/schemas/Code"\n'),
                "  schemas:\n    Code:\n      type: string\n      example: ref-sample\n",
            ),
            ran=(SCHEMA_EXAMPLE,),
            holds=((CLIENT, 'code="ref-sample"'),),
        ),
        Run(
            operation_document(parcel_query("            type: string\n            example: ref-sample\n")),
            skipped=(SCHEMA_EXAMPLE,),
            holds=((CLIENT, 'code="param-sample"'),),
        ),
    ),
    # A path parameter naming a string enum needs no conversion, so the scalar test
    # after `needs_convert` never runs and the value is interpolated as it is.
    Outcome(
        "combo-path-param-ref-string-enum",
        Run(
            operation_document(craft_path("Kind"), "  schemas:\n" + CRAFT),
            skipped=(URL_SCALARS,),
            holds=((RAW, "encode_path_param(kind)"),),
        ),
        Run(
            operation_document(craft_path("Slot"), "  schemas:\n" + CRAFT),
            ran=(URL_SCALARS,),
            holds=((RAW, "convert_and_respect_annotation_metadata(object_=kind"),),
        ),
    ),
    # A stream-condition operation naming its method takes the method-name arm, not
    # the operationId one, and names its streaming half from the method name.
    Outcome(
        "combo-streaming-method-name",
        Run(
            operation_document(watch("      x-fern-sdk-method-name: watch\n"), "  schemas:\n" + WATCH),
            ran=(NAMED_STREAM,),
            skipped=(ID_STREAM,),
            holds=((CLIENT, "def watch_stream("),),
        ),
        Run(
            operation_document(watch(""), "  schemas:\n" + WATCH),
            ran=(ID_STREAM,),
            skipped=(NAMED_STREAM,),
            holds=((CLIENT, "def watch_events_stream("),),
        ),
    ),
    # An operation's own security replaces the document's: over an unauthenticated
    # document it leaves the API authenticated, so the credential stays required.
    Outcome(
        "combo-document-operation-security",
        Run(
            operation_document(secured("      security:\n        - bearerAuth: []\n"), BEARER, "security: []\n"),
            skipped=(UNAUTHENTICATED,),
            lacks=((CLIENT, OPTIONAL_TOKEN),),
        ),
        Run(
            operation_document(secured(""), BEARER, "security: []\n"),
            ran=(UNAUTHENTICATED,),
            holds=((CLIENT, OPTIONAL_TOKEN),),
        ),
    ),
    # An operation's empty list replaces the document's requirement, so the API is
    # not wholly authenticated and the credential becomes optional.
    Outcome(
        "combo-document-security-security-empty",
        Run(
            operation_document(secured("      security: []\n"), BEARER, "security:\n  - bearerAuth: []\n"),
            ran=(UNAUTHENTICATED,),
            holds=((CLIENT, OPTIONAL_TOKEN),),
        ),
        Run(
            operation_document(secured(""), BEARER, "security:\n  - bearerAuth: []\n"),
            skipped=(UNAUTHENTICATED,),
            lacks=((CLIENT, OPTIONAL_TOKEN),),
        ),
    ),
    # A nullability-only `allOf` member sets `flatten_all`, so the model copies its
    # base's fields flat where the same composition without it extends the base.
    Outcome(
        "combo-allof-nullable-member",
        Run(
            tally(KENNEL + "    Tally:\n" + TALLY_MEMBERS + "        - nullable: true\n"),
            ran=(FLATTEN_ALL,),
            holds=(("types/tally.py", "class Tally(UniversalBaseModel):"),),
        ),
        Run(
            tally(KENNEL + "    Tally:\n" + TALLY_MEMBERS),
            skipped=(FLATTEN_ALL,),
            holds=(("types/tally.py", "class Tally(Kennel):"),),
        ),
    ),
    # The composition's own `required` names a base property, so it is promoted to a
    # required field of a flat model where the composition alone extends the base.
    Outcome(
        "combo-allof-with-required",
        Run(
            tally(KENNEL + "    Tally:\n      required: [name]\n" + TALLY_MEMBERS),
            ran=(PROMOTED,),
            holds=(("types/tally.py", "    name: str\n"),),
        ),
        Run(
            tally(KENNEL + "    Tally:\n" + TALLY_MEMBERS),
            skipped=(PROMOTED,),
            lacks=(("types/tally.py", "name"),),
        ),
    ),
    # A map beside an `anyOf` sets `map_first`: the union arm is passed over for the
    # map arm, and the property is a dict where the `anyOf` alone hoists a union.
    Outcome(
        "combo-map-beside-anyof",
        Run(
            counts(VALUES + PICK),
            ran=(MAP_ANY_OF, MAP_ARM),
            holds=(("types/tally.py", "counts: typing.Optional[typing.Dict[str, int]]"),),
        ),
        Run(
            counts(PICK),
            skipped=(MAP_ANY_OF, MAP_ARM),
            holds=(("types/tally_counts.py", "TallyCounts = typing.Union[str, int]"),),
        ),
    ),
    # The same beside a `oneOf`, which decides `map_first` before the `anyOf` test runs.
    Outcome(
        "combo-map-beside-oneof",
        Run(
            counts(VALUES + PICK.replace("anyOf", "oneOf")),
            ran=(MAP_ARM,),
            skipped=(MAP_ANY_OF,),
            holds=(("types/tally.py", "counts: typing.Optional[typing.Dict[str, int]]"),),
        ),
        Run(
            counts(PICK.replace("anyOf", "oneOf")),
            skipped=(MAP_ANY_OF, MAP_ARM),
            holds=(("types/tally_counts.py", "TallyCounts = typing.Union[str, int]"),),
        ),
    ),
    # A map's nullable value schema opens the optional-value arm, so the dict's value
    # type is `Optional` where a plain value schema leaves it bare.
    Outcome(
        "combo-map-of-nullable-values",
        Run(
            counts(VALUES + "            nullable: true\n"),
            ran=(NULLABLE_VALUES,),
            holds=(("types/tally.py", "typing.Optional[typing.Dict[str, typing.Optional[int]]]"),),
        ),
        Run(
            counts(VALUES),
            skipped=(NULLABLE_VALUES,),
            holds=(("types/tally.py", "typing.Optional[typing.Dict[str, int]]"),),
        ),
    ),
    # Properties beside a map value short-circuit the value-hoisting test, so the
    # property is a model of its own where the bare map hoists `{Owner}{Prop}Value`.
    Outcome(
        "combo-properties-beside-additional-properties",
        Run(
            counts("          properties:\n            label:\n              type: string\n" + SIZED),
            ran=(VALUE_PROPERTIES,),
            skipped=(VALUE_UNREFERENCED, VALUE_HOIST),
            holds=(("types/tally.py", "counts: typing.Optional[TallyCounts]"),),
        ),
        Run(
            counts(SIZED),
            ran=(VALUE_PROPERTIES, VALUE_UNREFERENCED, VALUE_HOIST),
            holds=(("types/tally.py", "typing.Dict[str, TallyCountsValue]"),),
        ),
    ),
    # A required property naming a nullable component reads the target's nullability,
    # so it is optional without the `required` test after it ever running.
    Outcome(
        "combo-property-ref-to-nullable-target",
        Run(
            tally(PINNED + "      nullable: true\n"),
            ran=(NULLABLE_TARGET,),
            skipped=(TARGET_NULLABLE, NOT_REQUIRED),
            holds=(("types/tally.py", "badge: typing.Optional[Badge]"),),
        ),
        Run(
            tally(PINNED),
            ran=(TARGET_NULLABLE, NOT_REQUIRED),
            skipped=(NULLABLE_TARGET,),
            holds=(("types/tally.py", "badge: Badge\n"),),
        ),
    ),
    # A parent property naming a `readOnly` component reads `!read_only` false, so the
    # child's `required` never promotes it and the model still extends the parent.
    Outcome(
        "combo-property-ref-to-read-only-target",
        Run(
            tally(PEN + "      readOnly: true\n"),
            ran=(READ_ONLY_OPERAND,),
            skipped=(PROMOTED,),
            holds=(("types/tally.py", "class Tally(Pen):"),),
        ),
        Run(
            tally(PEN),
            ran=(READ_ONLY_OPERAND, PROMOTED),
            holds=(("types/tally.py", "badge: Badge\n"),),
        ),
    ),
    # An error response's inline object with properties is an inline struct, so its
    # error class carries a hoisted body model where a bare object stays a dict.
    Outcome(
        "combo-error-object",
        Run(
            rejected("                properties:\n                  reason:\n                    type: string\n"),
            ran=(ERROR_STRUCT,),
            holds=(("errors/bad_request_error.py", "body: BadRequestErrorBody,"),),
        ),
        Run(
            rejected(""),
            skipped=(ERROR_STRUCT,),
            holds=(("errors/bad_request_error.py", "body: typing.Dict[str, typing.Any],"),),
        ),
    ),
    # A bodyless `204` beside a typed `200` opens the empty-success arm, so the method
    # returns its model optionally where the `200` alone returns it as is.
    Outcome(
        "combo-success-statuses-mixed-media",
        Run(
            emptied('        "204":\n          description: emptied\n'),
            ran=(BODYLESS, OPTIONAL_ARM),
            holds=((CLIENT, "-> typing.Optional[Kennel]:"),),
        ),
        Run(
            emptied(""),
            skipped=(BODYLESS, OPTIONAL_ARM),
            holds=((CLIENT, "-> Kennel:"),),
        ),
    ),
    # A document requirement naming a basic scheme makes the credentials required:
    # the required arm runs, where without it the operation leaves them optional.
    Outcome(
        "combo-basic-auth-document-requirement",
        Run(
            operation_document(secured(""), BASIC, "security:\n  - basicAuth: []\n"),
            ran=(BASIC_REQUIRED,),
            skipped=(UNAUTHENTICATED,),
            holds=(("core/client_wrapper.py", REQUIRED_BASIC),),
        ),
        Run(
            operation_document(secured(""), BASIC),
            ran=(UNAUTHENTICATED,),
            skipped=(BASIC_REQUIRED,),
            lacks=(("core/client_wrapper.py", REQUIRED_BASIC),),
        ),
    ),
    # An operation's own requirement naming a basic scheme, with none on the
    # document, makes the credentials required the same way.
    Outcome(
        "combo-basic-auth-operation-requirement",
        Run(
            operation_document(secured("      security:\n        - basicAuth: []\n"), BASIC),
            ran=(BASIC_REQUIRED,),
            skipped=(UNAUTHENTICATED,),
            holds=(("core/client_wrapper.py", REQUIRED_BASIC),),
        ),
        Run(
            operation_document(secured(""), BASIC),
            ran=(UNAUTHENTICATED,),
            skipped=(BASIC_REQUIRED,),
            lacks=(("core/client_wrapper.py", REQUIRED_BASIC),),
        ),
    ),
    # An anonymous alternative beside a bearer requirement skips the required-security
    # return, so the echo flag holds and the content-type header is dropped.
    Outcome(
        "combo-echo-body-effective-anonymous",
        Run(
            operation_document(ECHO_PATHS, BEARER + "  schemas:\n" + KENNEL, "security:\n  - bearerAuth: []\n  - {}\n"),
            ran=(ECHO_FLAG, ECHO_ARM),
            skipped=(ECHO_GUARD,),
            lacks=((RAW, '"content-type"'),),
        ),
        Run(
            operation_document(ECHO_PATHS, BEARER + "  schemas:\n" + KENNEL, "security:\n  - bearerAuth: []\n"),
            ran=(ECHO_FLAG, ECHO_GUARD),
            skipped=(ECHO_ARM,),
            holds=((RAW, '"content-type": "application/json"'),),
        ),
    ),
    # Required OAuth2 security skips the required-security return a bearer one takes,
    # so the echo flag holds and the content-type header is dropped.
    Outcome(
        "combo-echo-body-effective-oauth2",
        Run(
            operation_document(ECHO_PATHS, OAUTH + "  schemas:\n" + KENNEL, "security:\n  - kennelOAuth: []\n"),
            ran=(ECHO_FLAG, ECHO_ARM),
            skipped=(ECHO_GUARD,),
            lacks=((RAW, '"content-type"'),),
        ),
        Run(
            operation_document(ECHO_PATHS, BEARER + "  schemas:\n" + KENNEL, "security:\n  - bearerAuth: []\n"),
            ran=(ECHO_FLAG, ECHO_GUARD),
            skipped=(ECHO_ARM,),
            holds=((RAW, '"content-type": "application/json"'),),
        ),
    ),
    # A required query object with properties leaves Fern no endpoint example, so
    # the worked call drops the required query array a string beside it keeps.
    Outcome(
        "combo-query-param-inline-object",
        Run(
            operation_document(
                tally_query(
                    "            type: object\n            properties:\n              marks:\n"
                    "                type: array\n                items:\n                  type: string\n"
                )
            ),
            ran=(OBJECT_QUERY,),
            holds=((CLIENT, "filter=ListTalliesRequestFilter(),"),),
            lacks=((CLIENT, 'ids=["ids"]'),),
        ),
        Run(
            operation_document(tally_query("            type: string\n")),
            skipped=(OBJECT_QUERY,),
            holds=((CLIENT, 'ids=["ids"]'),),
        ),
    ),
    # The same through a `$ref` to an object component: the reference is resolved
    # first, and the worked call drops the required query array.
    Outcome(
        "combo-query-param-ref-object",
        Run(
            operation_document(
                tally_query('            $ref: "#/components/schemas/TallyFilter"\n'), "  schemas:\n" + TALLY_FILTER
            ),
            ran=(OBJECT_QUERY,),
            holds=((CLIENT, "filter=TallyFilter(),"),),
            lacks=((CLIENT, 'ids=["ids"]'),),
        ),
        Run(
            operation_document(
                tally_query('            $ref: "#/components/schemas/TallyCode"\n'), "  schemas:\n" + TALLY_FILTER
            ),
            skipped=(OBJECT_QUERY,),
            holds=((CLIENT, 'ids=["ids"]'),),
        ),
    ),
    # A header naming a string-enum component is sent by its `.value`; one naming a
    # plain string component is stringified.
    Outcome(
        "combo-header-param-ref-string-enum",
        Run(
            operation_document(craft_header("Rig"), "  schemas:\n" + EXAMPLED_CRAFT),
            ran=(HEADER_ENUM_ARM,),
            holds=((RAW, '"X-Craft-Kind": craft_kind.value if'),),
        ),
        Run(
            operation_document(craft_header("Tag"), "  schemas:\n" + EXAMPLED_CRAFT),
            skipped=(HEADER_ENUM_ARM,),
            holds=((RAW, '"X-Craft-Kind": str(craft_kind) if'),),
        ),
    ),
    # A query parameter naming a string-enum component drops its example, so the call
    # takes the first member; a plain string component's example is kept.
    Outcome(
        "combo-query-param-ref-string-enum",
        Run(
            operation_document(craft_query("Rig"), "  schemas:\n" + EXAMPLED_CRAFT),
            ran=(QUERY_EXAMPLE_DROPPED,),
            skipped=(QUERY_EXAMPLE_TAKEN,),
            holds=((CLIENT, "kind=Rig.GLIDER,"),),
            lacks=((CLIENT, "balloon"),),
        ),
        Run(
            operation_document(craft_query("Tag"), "  schemas:\n" + EXAMPLED_CRAFT),
            ran=(QUERY_EXAMPLE_TAKEN,),
            skipped=(QUERY_EXAMPLE_DROPPED,),
            holds=((CLIENT, 'kind="hangar-nine",'),),
        ),
    ),
    # A query parameter naming a date-time component is serialized as a datetime;
    # one naming a plain string component is sent as it is.
    Outcome(
        "combo-query-param-ref-date-time",
        Run(
            operation_document(craft_query("Landed"), "  schemas:\n" + EXAMPLED_CRAFT),
            ran=(ALIASED_TEMPORAL,),
            holds=((RAW, '"kind": serialize_datetime(kind),'),),
        ),
        Run(
            operation_document(craft_query("Tag"), "  schemas:\n" + EXAMPLED_CRAFT),
            skipped=(ALIASED_TEMPORAL,),
            holds=((RAW, '"kind": kind,'),),
        ),
    ),
    # A body property sharing a header's name takes the body-context prefix; beside
    # a header of another name it keeps its own.
    Outcome(
        "combo-body-property-named-as-header-param",
        Run(
            operation_document(locker_claim("shelf")),
            ran=(BODY_COLLISION,),
            holds=((RAW, '"shelf": claim_locker_request_shelf,'),),
        ),
        Run(
            operation_document(locker_claim("tier")),
            skipped=(BODY_COLLISION,),
            holds=((RAW, '"shelf": shelf,'),),
        ),
    ),
    # An optional, non-nullable query `anyOf` is declared in the root `types/`; the
    # same union on a header stays in its tag's package.
    Outcome(
        "combo-query-param-anyof",
        Run(
            operation_document(tagged_union("query", "anyOf")),
            ran=(QUERY_UNION_GLOBAL, ONE_OR_MANY),
            holds=((HANGAR_BAY, "from ..types.list_hangars_request_bay import"),),
        ),
        Run(
            operation_document(tagged_union("header", "anyOf")),
            skipped=(QUERY_UNION_GLOBAL, ONE_OR_MANY),
            holds=((HANGAR_BAY, "from .types.list_hangars_request_bay import"),),
        ),
    ),
    Outcome(
        "combo-query-param-oneof",
        Run(
            operation_document(tagged_union("query", "oneOf")),
            ran=(QUERY_UNION_GLOBAL, ONE_OR_MANY),
            holds=((HANGAR_BAY, "from ..types.list_hangars_request_bay import"),),
        ),
        Run(
            operation_document(tagged_union("header", "oneOf")),
            skipped=(QUERY_UNION_GLOBAL, ONE_OR_MANY),
            holds=((HANGAR_BAY, "from .types.list_hangars_request_bay import"),),
        ),
    ),
    # A urlencoded union with no JSON beside it skips the JSON `continue` and takes
    # the union arm: the body is one named union sent through `data=`, not `json=`.
    Outcome(
        "combo-form-urlencoded-union-body",
        Run(
            operation_document(tally_post(TALLY_FORM + TALLY_UNION)),
            ran=(FORM_UNION,),
            skipped=(FORM_JSON_MEDIA,),
            holds=((RAW, "object_=request, annotation=typing.Optional[PostTallyRequest]"),),
            lacks=((RAW, "json=request"),),
        ),
        Run(
            operation_document(tally_post(TALLY_JSON + "              type: object\n" + TALLY_FORM + TALLY_UNION)),
            ran=(FORM_JSON_MEDIA,),
            skipped=(FORM_UNION,),
            holds=((RAW, "json=request,"),),
            lacks=((RAW, "x-www-form-urlencoded"),),
        ),
    ),
    # A query parameter beside an inline `anyOf` body sets `union_body_suffix`, so
    # the hoisted union takes the `Body` infix it lacks alone.
    Outcome(
        "combo-params-beside-inline-anyof-body",
        Run(
            operation_document(tally_post(TALLY_JSON + TALLY_ANY, TALLY_QUERY)),
            ran=(UNION_BODY_SUFFIX,),
            holds=((CLIENT, "request: PostTallyRequestBody,"),),
        ),
        Run(
            operation_document(tally_post(TALLY_JSON + TALLY_ANY)),
            skipped=(UNION_BODY_SUFFIX,),
            holds=((CLIENT, "request: PostTallyRequest,"),),
            lacks=((CLIENT, "PostTallyRequestBody"),),
        ),
    ),
    Outcome(
        "combo-params-beside-inline-oneof-body",
        Run(
            operation_document(tally_post(TALLY_JSON + TALLY_UNION, TALLY_QUERY)),
            ran=(UNION_BODY_SUFFIX,),
            holds=((CLIENT, "request: PostTallyRequestBody,"),),
        ),
        Run(
            operation_document(tally_post(TALLY_JSON + TALLY_UNION)),
            skipped=(UNION_BODY_SUFFIX,),
            holds=((CLIENT, "request: PostTallyRequest,"),),
            lacks=((CLIENT, "PostTallyRequestBody"),),
        ),
    ),
    # A query parameter beside a urlencoded union names it in the form arm's own
    # suffix test: the union takes the `Body` infix, the JSON union arm never runs.
    Outcome(
        "combo-form-urlencoded-body-with-params",
        Run(
            operation_document(tally_post(TALLY_FORM + TALLY_UNION, TALLY_QUERY)),
            ran=(FORM_UNION_SUFFIX,),
            skipped=(UNION_BODY_SUFFIX,),
            holds=((CLIENT, "request: typing.Optional[PostTallyRequestBody] = None,"),),
        ),
        Run(
            operation_document(tally_post(TALLY_FORM + TALLY_UNION)),
            skipped=(FORM_UNION_SUFFIX, UNION_BODY_SUFFIX),
            holds=((CLIENT, "request: typing.Optional[PostTallyRequest] = None,"),),
            lacks=((CLIENT, "PostTallyRequestBody"),),
        ),
    ),
    # A media example on an inline `allOf` body is a composed media example: the
    # example passes the inherited field it names, ahead of the body's own.
    Outcome(
        "combo-media-example-on-inline-allof-body",
        Run(
            operation_document(tally_post(TALLY_JSON + KENNEL_BASE + LITTER + LITTER_EXAMPLE), "  schemas:\n" + KENNEL),
            ran=(COMPOSED_MEDIA_EXAMPLE,),
            holds=((CLIENT, 'name="Rex",\n            note="tidy",\n            size=3,'),),
        ),
        Run(
            operation_document(tally_post(TALLY_JSON + LITTER + LITTER_EXAMPLE), "  schemas:\n" + KENNEL),
            skipped=(COMPOSED_MEDIA_EXAMPLE,),
            holds=((CLIENT, 'note="tidy",\n            size=3,'),),
            lacks=((CLIENT, 'name="Rex"'),),
        ),
    ),
    # A media example on a referenced `allOf` body keeps the component's example
    # to property fallbacks only, so the media's values replace the component's.
    Outcome(
        "combo-media-example-on-ref-allof-body",
        Run(
            operation_document(tally_post(TALLY_JSON + PUPPY_BODY + PUPPY_EXAMPLE), "  schemas:\n" + KENNEL + PUPPY),
            ran=(COMPOSED_MEDIA_EXAMPLE, FALLBACKS_ONLY),
            holds=((CLIENT, 'name="Rex",\n            size=3,'),),
            lacks=((CLIENT, 'note="messy"'),),
        ),
        Run(
            operation_document(tally_post(TALLY_JSON + PUPPY_BODY), "  schemas:\n" + KENNEL + PUPPY),
            skipped=(COMPOSED_MEDIA_EXAMPLE, FALLBACKS_ONLY),
            holds=((CLIENT, 'name="Max",\n            note="messy",\n            size=9,'),),
            lacks=((CLIENT, 'name="Rex"'),),
        ),
    ),
    # An `anyOf` property's own example picks the member it matches, where the
    # same property without one synthesizes its first member.
    Outcome(
        "combo-anyof-schema-example",
        Run(
            operation_document(tally_post(TALLY_JSON + CRATE_BODY), "  schemas:\n" + crate("anyOf", CAGE_EXAMPLE)),
            ran=(UNION_EXAMPLE, MATCHED_VARIANT),
            holds=((CLIENT, "pen=Cage("), (CLIENT, "width=4,")),
            lacks=((CLIENT, "pen=Hutch("),),
        ),
        Run(
            operation_document(tally_post(TALLY_JSON + CRATE_BODY), "  schemas:\n" + crate("anyOf")),
            skipped=(UNION_EXAMPLE, MATCHED_VARIANT),
            holds=((CLIENT, "pen=Hutch("),),
            lacks=((CLIENT, "pen=Cage("),),
        ),
    ),
    # A media example on a referenced `oneOf` body is matched to the member it
    # fits; without it the request synthesizes the first member.
    Outcome(
        "combo-media-example-on-ref-union-body",
        Run(
            operation_document(tally_post(TALLY_JSON + PERCH_BODY + PERCH_EXAMPLE), "  schemas:\n" + PERCH),
            ran=(UNION_EXAMPLE, MATCHED_VARIANT),
            holds=((CLIENT, "request=Cage(\n                width=4,"),),
            lacks=((CLIENT, "request=Hutch("),),
        ),
        Run(
            operation_document(tally_post(TALLY_JSON + PERCH_BODY), "  schemas:\n" + PERCH),
            skipped=(UNION_EXAMPLE, MATCHED_VARIANT),
            holds=((CLIENT, 'request=Hutch(\n                name="name",'),),
            lacks=((CLIENT, "request=Cage("),),
        ),
    ),
    # A multipart property claims the name of the path parameter beside it, so
    # the path argument is renamed `slot_path_param`; without the body it is not.
    Outcome(
        "combo-multipart-body-with-params",
        Run(
            operation_document(bay(BAY_MULTIPART)),
            ran=(MULTIPART_CLAIMS, CLAIMED_RENAME),
            holds=((CLIENT, "        slot_path_param: str,\n"), (CLIENT, "slot: typing.Optional[str] = OMIT,")),
        ),
        Run(
            operation_document(bay("")),
            skipped=(MULTIPART_CLAIMS, CLAIMED_RENAME),
            holds=((CLIENT, "def load_bay(self, slot: str, *,"),),
            lacks=((CLIENT, "slot_path_param"),),
        ),
    ),
)


class CooccurrenceOutcomeTest(unittest.TestCase):
    """Each outcome-proven co-occurrence row, run through the instrumented crozier."""

    def generate(self, scratch: Path, document: str, reach: ReachMeasurement, crozier: Path) -> tuple[Path, dict, dict]:
        """(the generated package, every production region, the executed ones) for one document."""
        spec = scratch / "openapi.yml"
        spec.write_text(document, encoding="utf-8")
        raw = scratch / "profile"
        raw.mkdir()
        run = subprocess.run(
            [
                *(str(crozier), "generate", "python", "--spec", str(spec), "--output", str(scratch / "sdk")),
                *("--package-name", "fern", "--project-name", "default_package_name"),
            ],
            cwd=REPO,
            capture_output=True,
            text=True,
            env=dict(os.environ, LLVM_PROFILE_FILE=str(raw / "%p-%m.profraw")),
        )
        self.assertEqual(0, run.returncode, run.stderr)
        merged, export = raw / "merged.profdata", raw / "export.json"
        reach.run_llvm(
            [reach._llvm_tool("llvm-profdata"), "merge", "-sparse", *map(str, raw.glob("*.profraw")), "-o", str(merged)]
        )
        with export.open("w", encoding="utf-8") as sink:
            reach.run_llvm(
                [reach._llvm_tool("llvm-cov"), "export", "-format=text", f"-instr-profile={merged}", str(crozier)],
                stdout=sink,
            )
        universe, hit = reach._covered(export, REPO)
        return scratch / "sdk" / "src" / "fern", universe, hit

    def ran(self, reach: ReachMeasurement, spec: str, universe: dict, hit: dict) -> bool:
        """Whether the run executed any counter region of the site `spec` names."""
        site = reach.resolve_site(spec)
        regions = {tuple(r) for r in universe.get(site.file, []) if site.holds(tuple(r))}
        self.assertTrue(regions, f"{spec} spans no counter region")
        return bool(regions & {tuple(r) for r in hit.get(site.file, [])})

    def test_each_outcome_proven_cooccurrence_reaches_its_outcome_only_with_both_features(self) -> None:
        reach = _module("golden_reach_outcomes", "golden-reach.py")
        handwritten = _module("handwritten_fixtures_outcomes", "handwritten-fixtures.py")
        crozier = handwritten.instrumented_crozier(REPO, reach)
        audited, _failures = reach.read_cooccurrence()
        for outcome in OUTCOMES:
            self.assertIn(outcome.key, audited, "an outcome-proven row is not a co-occurrence row")
            self.assertIn(
                type(self).__name__, audited[outcome.key].why_no_branch, "its audit row cites no outcome proof"
            )
            for label, expected in (("both features", outcome.both), ("one feature", outcome.control)):
                with self.subTest(key=outcome.key, document=label), tempfile.TemporaryDirectory() as temporary:
                    package, universe, hit = self.generate(Path(temporary), expected.document, reach, crozier)
                    for spec in expected.ran:
                        self.assertTrue(self.ran(reach, spec, universe, hit), f"{spec} did not run")
                    for spec in expected.skipped:
                        self.assertFalse(self.ran(reach, spec, universe, hit), f"{spec} ran")
                    for name, text in expected.holds:
                        self.assertIn(text, (package / name).read_text(encoding="utf-8"), name)
                    for name, text in expected.lacks:
                        self.assertNotIn(text, (package / name).read_text(encoding="utf-8"), name)


if __name__ == "__main__":
    unittest.main()
