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
import re
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
FIXTURES = REPO / "tests" / "fixtures"

# The vendored sources these cases assert against, and why each is here:
# a 3.1 document with webhooks and a callback, a document whose only `name:` is a
# schema property, a document whose `type:` lines are three different things, and
# the widest document in the corpus (a YAML anchor reused 53 times).
WEBHOOKS = "servers-webhooks"
DISCRIMINATED = "discriminated-unions"
COOKIES = "cookie-parameters"
EXHAUSTIVE = "exhaustive"


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
    """The census script as the `surface-census` recipe names it."""
    for command in recipe_body("surface-census"):
        candidate = REPO / command.split()[0]
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


def run(*args: str) -> subprocess.CompletedProcess:
    """The real script, as its own process, exactly as the recipe invokes it."""
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args], cwd=REPO, capture_output=True, text=True
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
            ["./scripts/fetch-corpus.sh", './scripts/openapi-surface-census.py "$@"'],
            recipe_body("surface-census"),
        )
        self.assertTrue(SCRIPT.is_file(), SCRIPT)

    def test_the_gate_runs_this_file_offline(self) -> None:
        self.assertEqual(
            [f"python3 tests/{Path(__file__).name}"], recipe_body("test-surface-census")
        )
        check = next(
            line for line in (REPO / "justfile").read_text(encoding="utf-8").splitlines()
            if line.startswith("check:")
        )
        self.assertIn("test-surface-census", check.split())


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


class PyYamlOracleTests(unittest.TestCase):
    """Where a real YAML implementation is available, the loader must agree with it.

    Skipped rather than required: the gate installs no Python packages, and this
    file has to run on a machine that has none. When PyYAML *is* importable this
    is the strongest available check on the loader, so it runs then.
    """

    def test_the_census_matches_pyyaml_on_every_vendored_document(self) -> None:
        try:
            import yaml
        except ImportError:
            self.skipTest("PyYAML is not importable on this interpreter")
        documents = sorted(FIXTURES.glob("*/openapi.y*ml"))
        self.assertGreater(len(documents), 20)
        for path in documents:
            with self.subTest(document=path.name):
                mine = census.census_document(census.load_document(path))
                theirs = census.census_document(yaml.safe_load(path.read_text(encoding="utf-8")))
                self.assertEqual(theirs, mine)


if __name__ == "__main__":
    unittest.main(verbosity=1, buffer=False, argv=[sys.argv[0], *sys.argv[1:]])
