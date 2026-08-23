#!/usr/bin/env python3
"""Boundary tests for `just surface-census` (`just test-surface-census`).

The census decides which OpenAPI features `docs/openapi-surface-coverage.md`
calls covered and which it calls a gap, so its whole value is that the number is
*measured*. These drive the real thing: the real
`scripts/openapi-surface-census.py`, the real vendored source documents, the real
filesystem. Nothing is mocked, and no fixture is written to make a case pass that
the corpus does not already contain.

Two things make this the gate's copy of the recipe rather than a paraphrase of it:

* The script under test is **read out of the justfile**, from the `surface-census`
  recipe itself. Renaming or rewiring the recipe fails these tests instead of
  silently leaving them testing a file nothing runs.
* Every end-to-end case passes `--vendored-only`, which is the same code path the
  unscoped recipe runs over both halves of the corpus — minus the fetch that would
  put the network inside `just check`.
"""

from __future__ import annotations

import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
FIXTURES = REPO / "tests" / "fixtures"

# The vendored sources these cases assert against, and what each one is here for:
# a 3.1 document with webhooks and a callback whose only `name:` line is a schema
# property; a document whose `type:` lines mean three different things; the only
# vendored document declaring cookie parameters; and the widest document in the
# corpus, which reuses one YAML anchor 53 times.
WEBHOOKS = "servers-webhooks"
DISCRIMINATED = "discriminated-unions"
COOKIES = "cookie-parameters"
EXHAUSTIVE = "exhaustive"


def grep_speaks_pcre() -> bool:
    """Whether this `grep` really does PCRE — asked by running one, not by reading prose.

    A grep without PCRE refuses in its own wording, and every implementation words
    it differently: BSD grep on macOS says `invalid option -- P`, a GNU grep built
    without libpcre says something else again, and either could reword next
    release. Sniffing stderr for a phrase therefore fails *open* — the guard misses,
    the command "succeeds" with no output, and an empty join set reads as "no
    limitations row names this feature", which is the miscategorisation this whole
    test exists to prevent. So probe the capability instead, with the two PCRE
    constructs the documented command actually depends on: `\\K` and a lookahead.
    """
    probe = subprocess.run(
        ["grep", "-oP", r"a\Kb(?=c)"], input="abc\n", capture_output=True, text=True
    )
    return probe.returncode == 0 and probe.stdout.strip() == "b"


def recipe_body(name: str) -> list[str]:
    """The command lines of one justfile recipe, so a rewiring fails here."""
    source = (REPO / "justfile").read_text(encoding="utf-8").splitlines()
    for index, line in enumerate(source):
        if not re.match(rf"^{re.escape(name)}( +[\w*\"=]+)*:", line):
            continue
        body: list[str] = []
        for candidate in source[index + 1 :]:
            if not candidate.startswith(" ") and candidate.strip():
                break
            if candidate.strip():
                body.append(candidate.strip())
        return body
    raise AssertionError(f"the justfile has no `{name}` recipe")


def script_under_test() -> Path:
    """The census script as the `surface-census` recipe names it.

    Every token is considered, not just the first: the recipe leads with the
    interpreter `scripts/census-python.sh` resolves, so the script it runs is an
    argument rather than the command.
    """
    for command in recipe_body("surface-census"):
        for token in command.split():
            candidate = REPO / token
            if candidate.suffix == ".py":
                return candidate
    raise AssertionError("the `surface-census` recipe runs no Python script")


SCRIPT = script_under_test()


def load_census():
    """Import the script as a module for the loader's own unit cases."""
    spec = importlib.util.spec_from_file_location("openapi_surface_census", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    # Registered before execution because the module defines dataclasses, whose
    # type resolution reads the module out of sys.modules.
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


census = load_census()


# Every census run in this file is bounded: a test that can only fail by hanging
# does not fail, it wedges the gate. The whole vendored corpus censuses in well
# under a second, so this is nowhere near a timing assertion.
CENSUS_TIMEOUT = 60


def run(*args: str) -> subprocess.CompletedProcess:
    """The real script, as its own process, exactly as the recipe invokes it."""
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        cwd=REPO,
        capture_output=True,
        text=True,
        timeout=CENSUS_TIMEOUT,
    )


def rows(completed: subprocess.CompletedProcess) -> dict[tuple[str, str], int]:
    """The reported (selector, fixture) -> count, parsed off the text report."""
    parsed: dict[tuple[str, str], int] = {}
    for line in completed.stdout.splitlines():
        selector, _, remainder = line.partition("  ")
        remainder = remainder.strip()
        if remainder.startswith("("):
            continue
        fixture, _, count = remainder.rpartition("  ")
        parsed[(selector.strip(), fixture.strip())] = int(count)
    return parsed


def write_fixture(root: Path, name: str, document: str) -> Path:
    directory = root / name
    directory.mkdir(parents=True)
    (directory / "openapi.yml").write_text(textwrap.dedent(document), encoding="utf-8")
    return directory


class RecipeWiringTests(unittest.TestCase):
    """The gate must run this file, and this file must test the recipe's script."""

    def test_the_unscoped_recipe_fetches_the_corpus_then_censuses_it(self) -> None:
        self.assertEqual(
            [
                "./scripts/fetch-corpus.sh",
                '"$(./scripts/census-python.sh)" ./scripts/openapi-surface-census.py "$@"',
            ],
            recipe_body("surface-census"),
        )
        self.assertTrue(SCRIPT.is_file(), SCRIPT)

    def test_the_gate_runs_this_file_offline(self) -> None:
        self.assertEqual(
            [f'"$(./scripts/census-python.sh)" tests/{Path(__file__).name}'],
            recipe_body("test-surface-census"),
        )
        check = next(
            line for line in (REPO / "justfile").read_text(encoding="utf-8").splitlines()
            if line.startswith("check:")
        )
        self.assertIn("test-surface-census", check.split())


class GrammarContractTests(unittest.TestCase):
    """The doc states the selector grammar; the script implements it. Pin them together.

    Six region passes classify features against
    `docs/openapi-surface-coverage.md`'s closed lists, so a list that drifted from
    the walk would silently invalidate their evidence. These re-derive the doc's
    lists and compare them to the tables the census actually walks.
    """

    DOC = REPO / "docs" / "openapi-surface-coverage.md"

    def backticked(self, start: str, end: str) -> set[str]:
        text = self.DOC.read_text(encoding="utf-8")
        self.assertIn(start, text, f"the grammar section no longer says {start!r}")
        body = text.split(start, 1)[1].split(end, 1)[0]
        return set(re.findall(r"`([A-Za-z][A-Za-z.]*)`", body))

    def test_the_documented_anchor_kinds_are_the_ones_that_head_a_selector(self) -> None:
        documented = self.backticked("- **Anchor kinds head their own selector.**", "- **")
        self.assertEqual(
            {name for name, kind in census.OBJECTS.items() if kind.anchor}, documented
        )

    def test_the_documented_extending_kinds_are_the_ones_that_extend_a_selector(self) -> None:
        documented = self.backticked(
            "- **Extending kinds append to their parent's selector under the field that holds",
            "So a License",
        )
        self.assertEqual(
            {name for name, kind in census.OBJECTS.items() if not kind.anchor}, documented
        )

    def test_the_documented_valued_fields_are_the_ones_that_emit_a_value(self) -> None:
        documented = self.backticked("themselves a closed list:", "\n\nA **count**")
        self.assertEqual(census.VALUED, documented)

    def test_each_region_file_repeats_the_index_s_boundary_verbatim(self) -> None:
        """Six copies of the region boundaries; the index's table is the original."""
        text = self.DOC.read_text(encoding="utf-8")
        owns = {
            cells[1].strip("`"): cells[3]
            for line in text.splitlines()
            if line.startswith("| `") and "openapi-surface/" in line
            for cells in [[cell.strip() for cell in line.split("|")]]
        }
        self.assertEqual(6, len(owns), "the index no longer lists six regions")
        for region, boundary in sorted(owns.items()):
            with self.subTest(region=region):
                body = (REPO / "docs" / "openapi-surface" / f"{region}.md").read_text(
                    encoding="utf-8"
                )
                self.assertIn("\n## Scope\n", body, f"{region}.md has no ## Scope section")
                scope = body.split("\n## Scope\n", 1)[1].split("\n## ", 1)[0]
                self.assertEqual(
                    " ".join(boundary.split()).rstrip("."),
                    " ".join(scope.split()).rstrip("."),
                    f"{region}.md's ## Scope is not the index's `owns` cell",
                )

    def test_the_stated_corpus_sizes_are_the_measured_ones(self) -> None:
        """31 vendored / 93 link-ok / 124 registered is restated in prose; measure it."""
        vendored = census.registered_sources(FIXTURES, REPO / ".local" / "corpus", True)
        registered = census.registered_sources(FIXTURES, REPO / ".local" / "corpus", False)
        counts = (len(vendored), len(registered) - len(vendored), len(registered))
        doc = self.DOC.read_text(encoding="utf-8")
        stated = re.search(
            r"the (\d+) vendored\n`tests/fixtures/<name>/openapi\.\*` documents, and the (\d+) `link-ok`", doc
        )
        self.assertIsNotNone(stated, "the instrument section no longer states the corpus split")
        self.assertEqual(counts[:2], (int(stated.group(1)), int(stated.group(2))))
        script = SCRIPT.read_text(encoding="utf-8")
        in_script = re.search(r"and (\d+) of the (\d+) registered sources are `link-ok`", script)
        self.assertIsNotNone(in_script, "the script's docstring no longer states the corpus split")
        self.assertEqual(
            (counts[1], counts[2]), (int(in_script.group(1)), int(in_script.group(2)))
        )

    def test_the_verdict_vocabulary_is_the_one_fern_limitations_defines(self) -> None:
        """A `limitations` row quotes that file's verdict; the enum is its property."""
        ledger = (REPO / "docs" / "fern-limitations.md").read_text(encoding="utf-8")
        section = ledger.split("## How to read a verdict", 1)[1].split("\nA verdict is", 1)[0]
        defined = re.findall(r"^\| \*\*(\w+)\*\* \|", section, re.M)
        self.assertGreater(len(defined), 3, "the verdict table no longer parses")
        quoted = self.backticked("section spells them (", ") —")
        self.assertEqual(set(defined), quoted)

    def test_the_documented_join_command_still_finds_the_limitations_keys(self) -> None:
        """The key-extraction recipe encodes that file's column layout.

        Its failure mode is an EMPTY list, not an error, so a region would join on
        nothing and read it as "no limitations row names this feature" — the wrong
        category. This runs the documented pattern, and where GNU grep is present
        (the Linux gate leg) runs the command itself and requires the same answer.
        """
        doc = self.DOC.read_text(encoding="utf-8")
        pattern = re.search(r"^grep -oP '(.+)' docs/fern-limitations\.md", doc, re.M)
        self.assertIsNotNone(pattern, "the index no longer documents the join command")
        ledger = (REPO / "docs" / "fern-limitations.md").read_text(encoding="utf-8")
        # The same expression with PCRE's \K — which Python's re does not have —
        # rewritten as the capture group it is shorthand for.
        self.assertIn("\\K", pattern.group(1), "the documented pattern lost its \\K anchor")
        before, _, after = pattern.group(1).partition("\\K")
        keys = set(re.findall(f"{before}({after})", ledger, re.M))
        self.assertGreater(len(keys), 40, "the documented pattern extracts almost no keys")
        for key in keys:
            self.assertRegex(key, r"^[A-Za-z0-9][A-Za-z0-9._-]*$")

        if not grep_speaks_pcre():
            self.skipTest("this grep has no PCRE support, so the command cannot run here")
        grep = subprocess.run(
            ["grep", "-oP", pattern.group(1), "docs/fern-limitations.md"],
            cwd=REPO, capture_output=True, text=True,
        )
        # Fail loudly on a refusal rather than comparing against empty output:
        # every way this command can go wrong has to be a red, not a quiet zero.
        self.assertEqual(0, grep.returncode, grep.stderr)
        self.assertEqual(keys, set(grep.stdout.split()))

    @unittest.skipUnless(os.name == "posix", "the shim is a /bin/sh script")
    def test_the_join_command_is_skipped_not_failed_where_grep_lacks_pcre(self) -> None:
        """The guard fires on a leg this one is not, so prove it from the leg it is.

        A first cut of the guard sniffed grep's stderr for `-P`. BSD grep refuses
        with `invalid option -- P`, which does not contain that substring, so the
        guard fell through and compared 56 keys against empty output: the macOS
        gate leg went red while Linux and Windows stayed green, and nothing local
        could see it. Running the real case against a real `grep` that refuses
        `-P` reproduces that leg wherever this file runs.
        """
        real = shutil.which("grep")
        if real is None:
            self.skipTest("no grep on PATH to fall back to")
        case = (
            f"{type(self).__name__}"
            ".test_the_documented_join_command_still_finds_the_limitations_keys"
        )
        with tempfile.TemporaryDirectory() as shim:
            refuser = Path(shim) / "grep"
            refuser.write_text(
                textwrap.dedent(
                    f"""\
                    #!/bin/sh
                    for arg in "$@"; do
                      case "$arg" in
                        -*P*) echo "grep: invalid option -- P" >&2; exit 2;;
                      esac
                    done
                    exec {real} "$@"
                    """
                ),
                encoding="utf-8",
            )
            refuser.chmod(0o755)
            run = subprocess.run(
                [sys.executable, str(Path(__file__).resolve()), case],
                cwd=REPO, capture_output=True, text=True,
                env={**os.environ, "PATH": f"{shim}{os.pathsep}{os.environ['PATH']}"},
            )
        self.assertEqual(0, run.returncode, run.stderr)
        self.assertIn("skipped=1", run.stderr)

    def test_the_region_files_carry_the_agreed_table_header(self) -> None:
        """Six files, one skeleton: the regions have to compose into one table."""
        header = (
            "| key | oas | spec location | category | evidence | crozier sites | "
            "why bytes could move | settlement |"
        )
        self.assertIn(header, self.DOC.read_text(encoding="utf-8"))
        regions = sorted(p.stem for p in (REPO / "docs" / "openapi-surface").glob("*.md"))
        self.assertEqual(
            ["bodies-media", "document-paths", "oas31-extensions", "parameters",
             "schemas", "security"],
            regions,
        )
        for region in regions:
            with self.subTest(region=region):
                text = (REPO / "docs" / "openapi-surface" / f"{region}.md").read_text(
                    encoding="utf-8"
                )
                self.assertIn(header, text)
                self.assertIn(f"openapi-surface/{region}.md", self.DOC.read_text(encoding="utf-8"))
                for section in ("## Scope", "## Entries", "## Method notes"):
                    self.assertIn(section, text)


class CensusReportTests(unittest.TestCase):
    """What the instrument answers: who declares a feature, and who does not."""

    def test_a_declared_feature_names_its_sources_and_its_declaration_count(self) -> None:
        completed = run("--vendored-only", "--selector", "operation.callbacks")
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertEqual({("operation.callbacks", WEBHOOKS): 1}, rows(completed))
        self.assertIn("31 vendored", completed.stderr)

    def test_a_valued_selector_reports_one_member_of_a_closed_set(self) -> None:
        completed = run("--vendored-only", "--selector", "parameter.in=cookie")
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertEqual({("parameter.in=cookie", COOKIES): 2}, rows(completed))

    def test_a_feature_no_registered_source_declares_is_reported_as_absent(self) -> None:
        """The evidence a `gap` row cites has to be printed, not inferred from silence."""
        completed = run("--vendored-only", "--selector", "pathItem.trace")
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertEqual({}, rows(completed))
        self.assertIn("pathItem.trace", completed.stdout)
        self.assertIn("(declared by no registered source)", completed.stdout)

        as_json = run("--vendored-only", "--json", "--selector", "pathItem.trace")
        payload = json.loads(as_json.stdout)
        self.assertEqual([], payload["rows"])
        self.assertEqual(["pathItem.trace"], payload["absent_selectors"])

    def test_every_declaration_site_counts_including_a_reused_yaml_anchor(self) -> None:
        """`security: *ref_0` declares the field again; the census counts both uses."""
        source = (FIXTURES / EXHAUSTIVE / "openapi.yml").read_text(encoding="utf-8")
        written = len(re.findall(r"^ *security:", source, re.M))
        anchored = len(re.findall(r"^ *security: \*", source, re.M))
        self.assertGreater(anchored, 1, "the exhaustive fixture no longer reuses an anchor")
        completed = run("--vendored-only", "--fixture", EXHAUSTIVE, "--selector", "operation.security")
        self.assertEqual({("operation.security", EXHAUSTIVE): written}, rows(completed))

    def test_a_vendor_extension_is_reported_under_the_object_that_carries_it(self) -> None:
        """The `oas31-extensions` region is built on this: `x-` keys are census rows."""
        counted = rows(run("--vendored-only", "--selector", "operation.x-fern-audiences"))
        self.assertEqual(
            {
                ("operation.x-fern-audiences", "audience-filter"): 2,
                ("operation.x-fern-audiences", "audience-filter-strict"): 2,
            },
            counted,
        )
        for fixture, count in counted.items():
            with self.subTest(fixture=fixture[1]):
                source = (FIXTURES / fixture[1] / "openapi.yml").read_text(encoding="utf-8")
                self.assertEqual(count, len(re.findall(r"^ *x-fern-audiences:", source, re.M)))

    def test_the_document_version_is_censused_as_its_major_minor(self) -> None:
        """3.0-vs-3.1 is the delta a region asks about; the patch level is noise."""
        counted = rows(run("--vendored-only", "--selector", "openapi.openapi=3.1"))
        self.assertIn(("openapi.openapi=3.1", WEBHOOKS), counted)
        declared = (FIXTURES / WEBHOOKS / "openapi.yml").read_text(encoding="utf-8")
        self.assertIn("openapi: 3.1.0", declared, "the fixture no longer declares a patch level")
        every = {selector for selector, _ in rows(run("--vendored-only"))}
        versions = {s for s in every if s.startswith("openapi.openapi=")}
        self.assertEqual({"openapi.openapi=3.0", "openapi.openapi=3.1"}, versions)

    def test_the_json_report_carries_the_sources_it_read(self) -> None:
        completed = run("--vendored-only", "--fixture", WEBHOOKS, "--json")
        self.assertEqual(0, completed.returncode, completed.stderr)
        payload = json.loads(completed.stdout)
        self.assertEqual(
            [{
                "fixture": WEBHOOKS,
                "origin": "vendored",
                "path": f"tests/fixtures/{WEBHOOKS}/openapi.yml",
            }],
            payload["sources"],
        )
        self.assertIn(
            {"selector": "openapi.webhooks", "fixture": WEBHOOKS, "count": 1},
            payload["rows"],
        )


class ObjectModelWalkTests(unittest.TestCase):
    """The distinction the whole instrument rests on: fields, not matching text."""

    def test_the_walk_disagrees_with_a_naive_text_match_on_a_property_name(self) -> None:
        """`servers-webhooks` writes `name:` once — as a schema *property* name.

        A text match scores that as a declared `name` field (the same mistake as
        scoring a `trace` operation off a path parameter called `trace`). The walk
        knows the keys under `properties` are names, so it reports no `.name`
        selector at all for this document, and the property shows up where it
        belongs: as one more `schema.properties` declaration.
        """
        source = FIXTURES / WEBHOOKS / "openapi.yml"
        naive = len(re.findall(r"^ *name:", source.read_text(encoding="utf-8"), re.M))
        self.assertEqual(1, naive, "the fixture's only `name:` line moved")

        completed = run("--vendored-only", "--fixture", WEBHOOKS)
        self.assertEqual(0, completed.returncode, completed.stderr)
        declared = {selector for selector, _ in rows(completed)}
        self.assertEqual(
            [], [selector for selector in declared if selector.endswith(".name")]
        )
        self.assertIn("schema.properties", declared)

    def test_the_walk_separates_three_different_meanings_of_one_key(self) -> None:
        """`discriminated-unions` writes `type:` nine times, meaning three things."""
        source = FIXTURES / DISCRIMINATED / "openapi.yml"
        naive = len(re.findall(r"^ *type:", source.read_text(encoding="utf-8"), re.M))
        counted = rows(run("--vendored-only", "--fixture", DISCRIMINATED))
        schema_types = counted[("schema.type", DISCRIMINATED)]
        scheme_types = counted[("securityScheme.type", DISCRIMINATED)]
        # The remainder are the `type` PROPERTIES of Circle and Square: named, not
        # declared, and so not a selector anywhere in the report.
        self.assertEqual(naive, schema_types + scheme_types + 2)
        self.assertLess(schema_types, naive)

    def test_a_reference_is_counted_once_and_not_followed(self) -> None:
        """A `$ref` in a schema is a keyword; a `$ref` elsewhere is a Reference Object."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root, "refs", """\
                openapi: 3.0.3
                info: {title: refs, version: "1"}
                paths:
                  /a:
                    get:
                      responses:
                        "200":
                          $ref: "#/components/responses/Ok"
                components:
                  responses:
                    Ok:
                      description: ok
                  schemas:
                    A:
                      $ref: "#/components/schemas/B"
                """)
            counted = rows(run("--vendored-only", "--fixtures-root", str(root)))
        self.assertEqual(1, counted[("reference.$ref", "refs")])
        self.assertEqual(1, counted[("schema.$ref", "refs")])


class SourceSelectionTests(unittest.TestCase):
    """Which documents the census is allowed to open, and which it must refuse to."""

    def test_it_reads_every_vendored_source_and_only_its_own_document(self) -> None:
        payload = json.loads(run("--vendored-only", "--json").stdout)
        vendored = sorted(
            directory.name
            for directory in FIXTURES.iterdir()
            if directory.is_dir() and any((directory / n).is_file() for n in census.SPEC_NAMES)
        )
        self.assertEqual(vendored, sorted(s["fixture"] for s in payload["sources"]))
        self.assertGreater(len(vendored), 20, "the vendored corpus shrank unexpectedly")
        for source in payload["sources"]:
            self.assertEqual("vendored", source["origin"])
            self.assertRegex(source["path"], r"^tests/fixtures/[^/]+/openapi\.(yml|yaml|json)$")
        declared = {row["fixture"] for row in payload["rows"]}
        self.assertEqual(set(vendored), declared, "a vendored source declared nothing")

    def test_a_generated_expected_tree_is_never_read(self) -> None:
        """A census that read the output would be measuring the answer, not the question."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fixture = write_fixture(root, "planted", """\
                openapi: 3.0.3
                info: {title: planted, version: "1"}
                paths: {}
                """)
            expected = fixture / "expected" / "src"
            expected.mkdir(parents=True)
            # A generated tree that would light up three selectors if it were read.
            (expected / "openapi.yml").write_text(
                "openapi: 3.1.0\npaths:\n  /x:\n    trace:\n      responses:\n"
                '        "200": {description: ok}\n',
                encoding="utf-8",
            )
            completed = run("--vendored-only", "--fixtures-root", str(root), "--json")
        payload = json.loads(completed.stdout)
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertEqual(
            [str(fixture / "openapi.yml")], [source["path"] for source in payload["sources"]]
        )
        self.assertEqual(
            [], [row for row in payload["rows"] if row["selector"] == "pathItem.trace"]
        )

    def test_an_unfetched_link_ok_source_is_a_hard_failure_not_a_silent_zero(self) -> None:
        """93 of the 124 registered sources are fetched; a silent zero would lie."""
        with tempfile.TemporaryDirectory() as directory:
            completed = run("--corpus-root", directory)
            self.assertEqual(1, completed.returncode, completed.stdout)
            self.assertIn("have not been fetched", completed.stderr)
            self.assertIn("just surface-census", completed.stderr)

            allowed = run("--corpus-root", directory, "--allow-unfetched", "--selector", "openapi.info")
            self.assertEqual(0, allowed.returncode, allowed.stderr)
            self.assertIn("is unfetched", allowed.stderr)
            self.assertIn("31 vendored, 0 fetched", allowed.stderr)

            payload = json.loads(
                run("--corpus-root", directory, "--allow-unfetched", "--json").stdout
            )
            corpus = [s for s in payload["sources"] if s["origin"] == "corpus"]
            self.assertGreater(len(corpus), 50, "the link-ok half is missing from the report")
            # Listed as registered but read as nothing: a path of null is the
            # difference between "declares nothing" and "was never opened".
            self.assertEqual({None}, {source["path"] for source in corpus})
            self.assertEqual(
                set(), {row["fixture"] for row in payload["rows"]} & {s["fixture"] for s in corpus}
            )

    def test_a_selector_the_grammar_cannot_emit_is_refused(self) -> None:
        """An unrefused typo would manufacture the evidence a `gap` row cites."""
        for selector, expected in (
            ("pathitem.trace", "Did you mean: pathItem.trace"),
            ("schema.notAKeyword", "is not a selector of the OpenAPI object model"),
            ("operation.tags=x", "is not one of the fields that emit a valued selector"),
            ("parameter.in=", "valued selector with no value"),
            ("notAnObject.x-thing", "is not an object the census walks"),
        ):
            with self.subTest(selector=selector):
                completed = run("--vendored-only", "--selector", selector)
                self.assertEqual(1, completed.returncode, completed.stdout)
                self.assertIn(expected, completed.stderr)
                self.assertNotIn("declared by no registered source", completed.stdout)

    def test_every_selector_the_census_emits_is_one_the_grammar_accepts(self) -> None:
        """The enumeration that refuses a typo and the walk that emits must agree."""
        emitted = {selector for selector, _ in rows(run("--vendored-only"))}
        self.assertGreater(len(emitted), 50, "the vendored census reported almost nothing")
        refused = {s: census.selector_error(s) for s in emitted if census.selector_error(s)}
        self.assertEqual({}, refused, "the census emits selectors its own grammar refuses")

    def test_a_source_whose_root_is_not_a_mapping_is_refused(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root, "listy", "- openapi: 3.0.3\n")
            completed = run("--vendored-only", "--fixtures-root", str(root))
        self.assertEqual(1, completed.returncode, completed.stdout)
        self.assertIn("is not an OpenAPI document", completed.stderr)
        self.assertIn("root is not a mapping", completed.stderr)

    def test_a_fixtures_root_without_the_corpus_manifest_is_refused(self) -> None:
        """The link-ok half is read out of CORPUS.md; its absence is not zero rows."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root, "solo", "openapi: 3.0.3\ninfo: {title: solo, version: \"1\"}\n")
            completed = run("--fixtures-root", str(root), "--corpus-root", directory)
        self.assertEqual(1, completed.returncode, completed.stdout)
        self.assertIn("missing corpus manifest", completed.stderr)

    def test_an_unknown_fixture_name_is_refused_with_what_the_names_are(self) -> None:
        completed = run("--vendored-only", "--fixture", "not-a-fixture")
        self.assertEqual(1, completed.returncode, completed.stdout)
        self.assertIn("no registered source is named 'not-a-fixture'", completed.stderr)
        self.assertIn("CORPUS.md", completed.stderr)

    def test_an_unreadable_document_names_the_file_and_the_line(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root, "broken", """\
                openapi: 3.0.3
                info:
                  title: broken
                paths:
                  /a: !ruby/object:Thing
                """)
            completed = run("--vendored-only", "--fixtures-root", str(root))
        self.assertEqual(1, completed.returncode, completed.stdout)
        self.assertIn("broken", completed.stderr)
        self.assertIn("openapi.yml:5:", completed.stderr)
        self.assertIn("YAML tags are not supported", completed.stderr)

    def test_a_bad_invocation_is_refused(self) -> None:
        completed = run("--nonsense")
        self.assertEqual(2, completed.returncode, completed.stdout)
        self.assertIn("unrecognized arguments", completed.stderr)
        missing = run("--vendored-only", "--fixtures-root", "/nonexistent-root")
        self.assertEqual(1, missing.returncode, missing.stdout)
        self.assertIn("missing fixtures root", missing.stderr)


@unittest.skipIf(os.name == "nt", "scripts/corpus-lib.sh is a POSIX shell library")
class CorpusManifestAgreementTests(unittest.TestCase):
    """The census reads CORPUS.md; so does scripts/corpus-lib.sh. Pin them together.

    `manifest_rows` and `corpus_aliases` are second readers of the manifest and
    the alias file — the first is the shell library `scripts/fetch-corpus.sh`
    uses. A row grammar that drifted would leave the census counting a different
    set of registered sources than the fetch populates, and it would drift
    *quietly*: a source the census never lists is one it can never report as
    declaring anything, which is the one direction a "never seen" census must not
    err in.
    """

    def shell(self, snippet: str) -> str:
        return subprocess.run(
            ["bash", "-c", f". scripts/corpus-lib.sh\n{snippet}"],
            cwd=REPO, capture_output=True, text=True, check=True,
        ).stdout

    def test_the_census_registers_exactly_the_rows_the_fetcher_fetches(self) -> None:
        shell_rows = [
            line.split("\t")[0]
            for line in self.shell("corpus_rows tests/fixtures/CORPUS.md").splitlines()
            if line.strip()
        ]
        self.assertGreater(len(shell_rows), 50, "corpus-lib.sh reported almost no rows")
        self.assertEqual(shell_rows, list(census.manifest_rows(FIXTURES / "CORPUS.md")))

    def test_the_census_resolves_an_alias_the_way_the_fetcher_does(self) -> None:
        aliases = census.corpus_aliases(FIXTURES)
        self.assertTrue(aliases, "the alias file is empty or unreadable")
        for name in [*aliases, "apideck.com-crm"]:
            with self.subTest(name=name):
                self.assertEqual(
                    self.shell(f'corpus_fixture_for "{name}"').strip(),
                    aliases.get(name, name),
                )


class YamlSubsetTests(unittest.TestCase):
    """The loader is the census's one non-obvious dependency, so it is pinned here.

    `just check` installs no Python packages and runs on Linux, macOS and Windows,
    so the loader is standard-library-only; these cases are the constructs real
    OpenAPI documents in the corpus actually use.
    """

    def load(self, document: str):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "openapi.yml"
            path.write_text(textwrap.dedent(document), encoding="utf-8")
            return census.load_document(path)

    def refusal(self, document: str) -> str:
        with self.assertRaises(census.DocumentError) as raised:
            self.load(document)
        return str(raised.exception)

    def test_anchors_aliases_and_merge_keys(self) -> None:
        self.assertEqual(
            {"a": ["x"], "b": ["x"], "c": {"k": 1, "j": 2}},
            self.load("""\
                a: &ref
                  - x
                b: *ref
                c:
                  <<: {k: 1}
                  j: 2
                """),
        )

    def test_a_block_sequence_may_sit_at_its_key_s_own_indentation(self) -> None:
        self.assertEqual(
            {"servers": [{"url": "u", "description": "d"}], "after": 1},
            self.load("""\
                servers:
                - url: u
                  description: d
                after: 1
                """),
        )

    def test_block_scalars_fold_chomp_and_keep(self) -> None:
        loaded = self.load("""\
            literal: |
              one
              two
            folded: >-
              one
              two

              three
            kept: |+
              one

            """)
        self.assertEqual("one\ntwo\n", loaded["literal"])
        self.assertEqual("one two\nthree", loaded["folded"])
        self.assertEqual("one\n\n", loaded["kept"])

    def test_a_scalar_may_be_written_under_its_key_and_wrap(self) -> None:
        self.assertEqual(
            {"description": "one two", "next": 1},
            self.load("""\
                description:
                  one
                  two
                next: 1
                """),
        )

    def test_a_quoted_scalar_spans_lines_without_losing_its_escapes(self) -> None:
        """A real corpus document (slurmdb-rest) writes both in one scalar: a `\\n`
        escape that must survive, and a trailing `\\` that cancels the source
        break along with the next line's indentation."""
        loaded = self.load('description: "a\\nb\\\n  c d"\n')
        self.assertEqual("a\nbc d", loaded["description"])

    def test_a_hash_inside_a_quoted_scalar_is_not_a_comment(self) -> None:
        self.assertEqual(
            {"a": {"$ref": "#/components/schemas/A"}, "b": 1},
            self.load("""\
                a:
                  $ref: "#/components/schemas/A"  # a real comment
                b: 1
                """),
        )

    def test_an_escaped_quote_does_not_end_the_scalar_a_comment_could_follow(self) -> None:
        self.assertEqual(
            {"a": 'he said "hi" # not a comment', "b": 1},
            self.load('a: "he said \\"hi\\" # not a comment"  # a real one\nb: 1\n'),
        )
        self.assertEqual(
            {"a": 'say " hi', "b": 1},
            self.load('a: "say \\" hi"  # a real one\nb: 1\n'),
        )

    def test_flow_collections_and_url_keys(self) -> None:
        self.assertEqual(
            {"info": {"title": "t", "tags": [1, "two"]}, "https://x.test": "y"},
            self.load("""\
                info: {title: t, tags: [1, two]}
                https://x.test: y
                """),
        )

    def test_the_core_schema_resolves_plain_scalars(self) -> None:
        self.assertEqual(
            {"n": None, "t": True, "f": False, "i": -3, "x": 1.5, "s": "3.0.1", "q": "1"},
            self.load("n: ~\nt: true\nf: false\ni: -3\nx: 1.5\ns: 3.0.1\nq: '1'\n"),
        )

    def test_unsupported_constructs_are_refused_by_name_and_line(self) -> None:
        for document, expected in (
            ("a: 1\n---\nb: 2\n", "more than one YAML document"),
            ("%YAML 1.2\n---\na: 1\n", "YAML directives are not supported"),
            ("a:\n\t- 1\n", "tabs cannot indent YAML"),
            ('a: "unterminated\n', "never closed"),
            ("a: [1, 2\n", "never closed"),
            ("? [a]\n: 1\n", "explicit `? ` mapping keys"),
            (": 1\n", "an empty mapping key"),
            ("info:\n  : 1\n", "an empty mapping key"),
            ("a: 1\nb\n", "expected a `key: value` mapping entry"),
        ):
            with self.subTest(document=document):
                self.assertIn(expected, self.refusal(document))

    def test_a_json_source_is_read_as_json(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "openapi.json"
            path.write_text('{"openapi": "3.1.0"}', encoding="utf-8")
            self.assertEqual({"openapi": "3.1.0"}, census.load_document(path))
            path.write_text("{oops", encoding="utf-8")
            with self.assertRaises(census.DocumentError) as raised:
                census.load_document(path)
            self.assertIn("is not valid JSON", str(raised.exception))


class FlowCollectionRegressionTests(unittest.TestCase):
    """The flow-collection parser, pinned against the defect that wedged the gate.

    A one-line edit disabled the branch that consumes the `:` of a flow *mapping*.
    `flow_node` stops at `,]}:` without consuming what it stopped at, so the loop
    re-entered on the same cursor and appended forever — 9.6 GB of RSS and no
    output, on eight of the 31 vendored documents, for every selector. The three
    properties below are what make that unrepeatable: it terminates, it terminates
    with the *right values*, and a cursor that cannot advance is an error.
    """

    # `info: { title: Widget API, version: 1.0.0 }` is the shape that stalled.
    FLOW_MAPPINGS = "audience-filter"

    def test_the_whole_vendored_corpus_censuses_within_the_timeout(self) -> None:
        """The unscoped vendored run — the exact invocation that never returned."""
        completed = run("--vendored-only")
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertIn("31 vendored", completed.stderr)
        self.assertGreater(len(rows(completed)), 100)

    def test_a_flow_mapping_parses_to_its_entries_not_a_list_of_its_keys(self) -> None:
        """Terminating is not enough: the disabled branch also built the wrong value."""
        document = census.load_document(FIXTURES / self.FLOW_MAPPINGS / "openapi.yml")
        self.assertEqual({"title": "Widget API", "version": "1.0.0"}, document["info"])
        widget = document["components"]["schemas"]["Widget"]["properties"]
        self.assertEqual({"type": "string"}, widget["id"])

        counted = rows(run("--vendored-only", "--fixture", self.FLOW_MAPPINGS))
        self.assertEqual(1, counted[("info.title", self.FLOW_MAPPINGS)])
        self.assertEqual(1, counted[("info.version", self.FLOW_MAPPINGS)])

    def test_the_recursive_callback_construct_terminates_with_its_count(self) -> None:
        """A Callback holds a Path Item holding Operations that may declare callbacks.

        The object model is recursive by construction, so the walk carries an
        ancestor set and a `$ref` is counted as a Reference Object rather than
        followed. This is the selector the wedged run was scoped to, so it is
        pinned bounded and by count rather than merely by "it finished".
        """
        completed = run("--vendored-only", "--selector", "operation.callbacks")
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertEqual({("operation.callbacks", WEBHOOKS): 1}, rows(completed))

    def test_a_flow_collection_that_cannot_advance_is_a_parse_error_not_a_hang(self) -> None:
        """The guard that makes the failure mode a message instead of an OOM.

        `{a]` balances by bracket count, so it reaches the collection loop, where
        `flow_node` stops at the `]` the loop does not recognise and consumes
        nothing. Without the progress check that is an infinite append.
        """
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "openapi.yml"
            path.write_text("info: {a]\n", encoding="utf-8")
            with self.assertRaises(census.DocumentError) as raised:
                census.load_document(path)
        self.assertIn("stalls", str(raised.exception))


class CensusInterpreterTests(unittest.TestCase):
    """Which Python the census runs under, which is a provenance question.

    The census scripts are standard-library-only, so a foreign interpreter does
    not fail — it answers, cleanly and with the wrong provenance. Both recipes ran
    a bare `python3` for a while, and on a machine with an unrelated project's
    virtualenv earlier on PATH the gate measured this repository under that
    project's environment without a word. `scripts/census-python.sh` is the one
    place that resolves it.
    """

    RESOLVER = REPO / "scripts" / "census-python.sh"

    def resolve(self, path: str | None = None) -> subprocess.CompletedProcess:
        # Resolved before PATH is replaced: these cases hand the resolver a PATH
        # with no interpreter on it, which would otherwise hide `bash` too.
        shell = shutil.which("bash")
        if shell is None:
            self.skipTest("no bash on PATH to run the resolver")
        environment = dict(os.environ)
        if path is not None:
            environment["PATH"] = path
        return subprocess.run(
            [shell, str(self.RESOLVER)],
            cwd=REPO,
            capture_output=True,
            text=True,
            env=environment,
            timeout=CENSUS_TIMEOUT,
        )

    def test_both_census_recipes_resolve_the_interpreter_through_the_resolver(self) -> None:
        for recipe in ("surface-census", "test-surface-census"):
            with self.subTest(recipe=recipe):
                body = " ".join(recipe_body(recipe))
                self.assertIn('"$(./scripts/census-python.sh)"', body)
                self.assertNotRegex(body, r"(?<!census-)\bpython3 ")

    def test_the_resolver_names_a_real_interpreter_that_is_not_a_virtualenv(self) -> None:
        completed = self.resolve()
        self.assertEqual(0, completed.returncode, completed.stderr)
        interpreter = completed.stdout.strip()
        self.assertTrue(Path(interpreter).is_file(), interpreter)
        prefixes = subprocess.run(
            [interpreter, "-c", "import sys; print(sys.prefix); print(sys.base_prefix)"],
            capture_output=True,
            text=True,
            timeout=CENSUS_TIMEOUT,
        )
        self.assertEqual(0, prefixes.returncode, prefixes.stderr)
        # This repository commits no virtualenv, so PATH's system Python is the
        # answer here. A deliberate local `.venv` would win instead, which is the
        # preference the next case drives.
        self.assertFalse((REPO / ".venv").exists(), "this case assumes no local .venv")
        first, second = prefixes.stdout.split()
        self.assertEqual(first, second, "the resolver chose a virtualenv")

    def test_a_repo_local_venv_is_preferred_over_anything_on_path(self) -> None:
        """The first branch, driven rather than tolerated.

        A `.venv` beside the resolver IS this repository's own environment, so it
        outranks PATH — including a perfectly good system Python that would other-
        wise be chosen. Driven by copying the real resolver into a root that has
        one, because the resolver locates the repository from its own path.
        """
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "scripts").mkdir()
            local = root / ".venv" / "bin"
            local.mkdir(parents=True)
            interpreter = local / "python3"
            interpreter.symlink_to(Path(sys.executable).resolve())
            copied = root / "scripts" / self.RESOLVER.name
            shutil.copy2(self.RESOLVER, copied)

            shell = shutil.which("bash")
            if shell is None:
                self.skipTest("no bash on PATH to run the resolver")
            completed = subprocess.run(
                [shell, str(copied)], capture_output=True, text=True,
                timeout=CENSUS_TIMEOUT,
            )

        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertEqual(str(interpreter), completed.stdout.strip())

    def test_a_foreign_virtualenv_is_refused_by_name_rather_than_used(self) -> None:
        """Driven against a real virtualenv, because that is the case that happened."""
        with tempfile.TemporaryDirectory() as directory:
            foreign = Path(directory) / "other-project" / ".venv"
            built = subprocess.run(
                [sys.executable, "-m", "venv", "--without-pip", str(foreign)],
                capture_output=True, text=True, timeout=CENSUS_TIMEOUT,
            )
            if built.returncode != 0:
                self.skipTest(f"this interpreter cannot build a venv: {built.stderr}")

            completed = self.resolve(path=str(foreign / "bin"))
            self.assertEqual(1, completed.returncode, completed.stdout)
            self.assertEqual("", completed.stdout.strip())
            self.assertIn("another project's virtualenv", completed.stderr)
            self.assertIn(str(foreign), completed.stderr)

    def test_no_python3_at_all_is_a_named_failure_rather_than_a_fall_through(self) -> None:
        with tempfile.TemporaryDirectory() as empty:
            completed = self.resolve(path=empty)
        self.assertEqual(1, completed.returncode, completed.stdout)
        self.assertEqual("", completed.stdout.strip())
        self.assertIn("no python3 on PATH", completed.stderr)


class PyYamlOracleTests(unittest.TestCase):
    """Where a real YAML implementation is available, the loader must agree with it.

    **This oracle is optional by design, not required.** The gate installs no
    Python packages and runs on the Linux/macOS/Windows matrix, so the interpreter
    `scripts/census-python.sh` resolves may legitimately have no PyYAML — making
    its absence an error would fail the gate on a correct host. The loader's
    behaviour is therefore pinned unconditionally by `YamlSubsetTests` and
    `FlowCollectionRegressionTests`, which need nothing installed; this class is a
    bonus check that runs wherever PyYAML happens to be importable. The skip names
    the interpreter, so a skip is always attributable rather than anonymous.
    """

    def test_the_census_matches_pyyaml_on_every_vendored_document(self) -> None:
        try:
            import yaml
        except ImportError:
            self.skipTest(f"PyYAML is not importable on {sys.executable}")
        documents = sorted(FIXTURES.glob("*/openapi.y*ml"))
        self.assertGreater(len(documents), 20)
        for path in documents:
            with self.subTest(document=path.name):
                mine = census.census_document(census.load_document(path))
                theirs = census.census_document(yaml.safe_load(path.read_text(encoding="utf-8")))
                self.assertEqual(theirs, mine)


if __name__ == "__main__":
    unittest.main(verbosity=1, buffer=False, argv=[sys.argv[0], *sys.argv[1:]])
