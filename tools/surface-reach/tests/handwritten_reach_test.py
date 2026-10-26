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
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any, NamedTuple

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


ECHO_FLAG = r"src/emit.rs::append_request_call_args[=^ {28}&& ep\.body_response_same_ref$]"
ECHO_ARM = site_cell("combo-echo-body-effective-anonymous")


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
SCHEMA_EXAMPLE = r"src/ir.rs::parameter_example_value[=parameter\.schema\.as_ref\(\)\.and_then\(schema_example\)]"
URL_SCALARS = r"src/ir.rs::build_endpoint[=^ {20}&& !hoister\.reaches_url_as_scalars\(&type_ref\),$]"
NAMED_STREAM = r"src/ir.rs::stream_condition_method_names[if op\.sdk_method_name\(\)\.is_some\(\) \{]"
ID_STREAM = r"src/ir.rs::stream_condition_method_names[\} else if !id\.is_empty\(\) \{]"
UNAUTHENTICATED = r"src/ir.rs::all_operations_authenticated[if !authed \{]"
CLIENT, RAW = "client.py", "raw_client.py"
STREAMS = "typing.Iterator[bytes]"
# The constructor's bearer credential, optional; `async_token` is optional always.
OPTIONAL_TOKEN = "        token: typing.Optional["

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
)


class CooccurrenceOutcomeTest(unittest.TestCase):
    """Each outcome-proven co-occurrence row, run through the instrumented crozier."""

    def generate(self, scratch: Path, document: str, reach: Any, crozier: Path) -> tuple[Path, dict, dict]:
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

    def ran(self, reach: Any, spec: str, universe: dict, hit: dict) -> bool:
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
