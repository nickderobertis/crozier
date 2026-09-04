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


# The bound turns a wedged gate into a failing test.
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

    def test_the_documented_predicate_selectors_are_the_ones_the_script_declares(self) -> None:
        """The third kind of selector: `<selector>:<predicate>`.

        The list lives in the script and is restated in the grammar section, so a
        member added to one and not the other has to fail here — the way the
        valued-field list above is already reconciled.
        """
        text = self.DOC.read_text(encoding="utf-8")
        start = "A shape the two kinds above cannot express emits a **predicate selector**,"
        self.assertIn(start, text, "the grammar section documents no predicate selector")
        body = text.split(start, 1)[1].split("A predicate selector is a selector", 1)[0]
        documented = set(re.findall(r"`([A-Za-z][A-Za-z.]*:[a-z-]+)`", body))
        self.assertEqual(set(census.PREDICATES), documented)

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

    def test_bodies_media_ledger_citations_match_the_keyed_verdicts(self) -> None:
        """A cited verdict is the ledger's exact text, not a stale paraphrase."""
        region = (
            REPO / "docs" / "openapi-surface" / "bodies-media.md"
        ).read_text(encoding="utf-8")
        citations = re.findall(
            r"Ledger `(?P<key>[A-Za-z0-9._-]+)`: `(?P<verdict>.*?)`\.", region
        )
        self.assertGreater(len(citations), 10, "bodies-media.md has almost no Ledger citations")

        ledger = (REPO / "docs" / "fern-limitations.md").read_text(encoding="utf-8")
        verdicts: dict[str, str] = {}
        for line in ledger.splitlines():
            cells = [cell.strip() for cell in line.split("|")]
            if len(cells) < 6 or not re.fullmatch(r"`[A-Za-z0-9._-]+`", cells[1]):
                continue
            if not cells[2].isdigit() or not cells[3].isdigit():
                continue
            verdicts[cells[1].strip("`")] = cells[4]

        failures = []
        for key, cited in citations:
            if key not in verdicts:
                failures.append(f"missing ledger key: {key}")
            elif not verdicts[key]:
                failures.append(f"missing ledger verdict for key: {key}")
            elif cited != verdicts[key]:
                failures.append(
                    f"verdict mismatch for {key}: cited {cited!r}, ledger has {verdicts[key]!r}"
                )
        self.assertFalse(failures, "\n" + "\n".join(failures))

    @unittest.skipUnless(os.name == "posix", "the shim is a /bin/sh script")
    def test_the_join_command_is_skipped_not_failed_where_grep_lacks_pcre(self) -> None:
        """Exercise the join case with a real `grep` that refuses `-P`."""
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
        self.assertIn("32 vendored", completed.stderr)

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
            self.assertIn("32 vendored, 0 fetched", allowed.stderr)

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
            ("operation.tags:mutliple", "Did you mean: operation.tags:multiple"),
            ("openapi.paths:collision", "is not one of the predicate selectors"),
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
    output, on eight of the vendored documents, for every selector. The three
    properties below are what make that unrepeatable: it terminates, it terminates
    with the *right values*, and a cursor that cannot advance is an error.
    """

    # `info: { title: Widget API, version: 1.0.0 }` is the shape that stalled.
    FLOW_MAPPINGS = "audience-filter"

    def test_the_whole_vendored_corpus_censuses_within_the_timeout(self) -> None:
        """The unscoped vendored run — the exact invocation that never returned."""
        completed = run("--vendored-only")
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertIn("32 vendored", completed.stderr)
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


@unittest.skipIf(
    os.name == "nt",
    "the POSIX shell resolver's semantics are not reproduced by MSYS",
)
class CensusInterpreterTests(unittest.TestCase):
    """Pin the census interpreter's repository provenance."""

    RESOLVER = REPO / "scripts" / "census-python.sh"

    def shell(self) -> str:
        shell = shutil.which("bash")
        if shell is None:
            self.skipTest("no bash on PATH to run the resolver")
        return shell

    def shell_path(self, path: Path) -> str:
        """Return the spelling Bash uses for a native path."""
        completed = subprocess.run(
            [self.shell(), "-c", 'cd "$1" && pwd -P', "census-path", str(path)],
            capture_output=True,
            text=True,
            timeout=CENSUS_TIMEOUT,
        )
        self.assertEqual(0, completed.returncode, completed.stderr)
        return completed.stdout.strip()

    def resolve(self, path: str | None = None) -> subprocess.CompletedProcess:
        # Resolved before PATH is replaced: these cases hand the resolver a PATH
        # with no interpreter on it, which would otherwise hide `bash` too.
        shell = self.shell()
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
        exists = subprocess.run(
            [self.shell(), "-c", 'test -f "$1"', "census-python", interpreter],
            timeout=CENSUS_TIMEOUT,
        )
        self.assertEqual(0, exists.returncode, interpreter)
        prefixes = subprocess.run(
            [
                self.shell(), "-c", '"$1" -c "$2"', "census-python", interpreter,
                "import sys; print(sys.prefix); print(sys.base_prefix)",
            ],
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
            local = root / ".venv" / ("Scripts" if os.name == "nt" else "bin")
            local.mkdir(parents=True)
            interpreter = local / ("python.exe" if os.name == "nt" else "python3")
            shutil.copy2(Path(sys.executable).resolve(), interpreter)
            copied = root / "scripts" / self.RESOLVER.name
            shutil.copy2(self.RESOLVER, copied)

            completed = subprocess.run(
                [self.shell(), str(copied)], capture_output=True, text=True,
                timeout=CENSUS_TIMEOUT,
            )
            expected = f"{self.shell_path(local)}/{interpreter.name}"

            self.assertEqual(0, completed.returncode, completed.stderr)
            self.assertTrue(
                os.path.samefile(expected, completed.stdout.strip()),
                f"{expected!r} and {completed.stdout.strip()!r} are not the same file",
            )

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

            scripts = foreign / ("Scripts" if os.name == "nt" else "bin")
            completed = self.resolve(path=str(scripts))
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



class RankedBacklogTests(unittest.TestCase):
    """The index's synthesis restates the six region files; recompute it from them.

    `## Ranked gap backlog` is an aggregate — per-region category counts, one
    ranked `FIXTURE` list, one `PROBE` list, and a per-`src/`-file join against
    `just fixtures-coverage`. Every number in it is owned somewhere else, so
    without these the section goes stale silently the first time a region row is
    added or reclassified. The coverage figures are the one input no offline gate
    can re-derive; what is checked here is that the two tables carrying them agree
    with each other, which is what the ranking's second criterion rests on.
    """

    DOC = REPO / "docs" / "openapi-surface-coverage.md"
    REGIONS = REPO / "docs" / "openapi-surface"
    CATEGORIES = ("golden", "limitations", "gap")
    SETTLEMENTS = ("FIXTURE", "PROBE", "UNREACHABLE")
    PROBE_KINDS = ("structural", "witness-supply")
    WITNESS_SEARCH = "### Witness search (issue #188)"
    # The sources issue #188's search puts to every row, whatever the region: the
    # two regions that publish a bulleted source list name six and five, and these
    # five are the intersection. Sourcegraph is deliberately not required — only
    # `security` and `parameters` reached it — so a row is never failed for a
    # source its own region never searched.
    REQUIRED_WITNESS_SOURCES = {
        "APIs.guru": r"APIs\.guru",
        "GitHub code search": r"GitHub",
        "SwaggerHub": r"SwaggerHub",
        "Postman": r"Postman",
        "vendor portals": r"[Vv]endor [Pp]ortals",
    }

    @classmethod
    def setUpClass(cls) -> None:
        cls.doc = cls.DOC.read_text(encoding="utf-8")
        cls.entries = {}
        for path in sorted(cls.REGIONS.glob("*.md")):
            for cells in cls.region_rows(path.read_text(encoding="utf-8")):
                cls.entries[cells[0].strip("`")] = (path.stem, cells)

    @staticmethod
    def region_rows(text: str) -> list[list[str]]:
        """Every entry-table row of one region file, as its eight cells.

        `\\|` inside a cell is an escaped pipe, not a column break — one row's
        `crozier sites` cell holds a Rust `match` pattern that uses it.
        """
        rows = []
        for line in text.splitlines():
            if not line.startswith("| "):
                continue
            cells = [
                cell.replace("\x00", "\\|").strip()
                for cell in line.replace("\\|", "\x00").strip().strip("|").split("|")
            ]
            if len(cells) == 8 and cells[3].strip("`") in RankedBacklogTests.CATEGORIES:
                rows.append(cells)
        return rows

    def section(self, start: str, end: str | None = None) -> str:
        self.assertIn(start, self.doc, f"the index no longer carries {start!r}")
        body = self.doc.split(start, 1)[1]
        return body if end is None else body.split(end, 1)[0]

    def settlement_of(self, cells: list[str]) -> str:
        first = cells[7].lstrip("`*").split(" ", 1)[0].strip("`*—")
        self.assertIn(first, self.SETTLEMENTS, f"unknown settlement class in {cells[0]}")
        return first

    def gaps(self, settlement: str) -> set[str]:
        return {
            key
            for key, (_region, cells) in self.entries.items()
            if cells[3].strip("`") == "gap" and self.settlement_of(cells) == settlement
        }

    def ranked_rows(self) -> list[tuple[int, str, tuple[int, int, int, int], str]]:
        """(rank, key, the four published criteria, the whole line)."""
        out = []
        for line in self.section(
            "### The ranked `FIXTURE` backlog", "### The ranked list against"
        ).splitlines():
            row = re.match(r"\| (\d+) \| \[`([^`]+)`\]", line)
            if not row:
                continue
            measured = [int(value) for value in re.findall(r"\*\*(\d+)\*\*", line)]
            self.assertEqual(
                4, len(measured), f"{row.group(2)} does not publish four measured criteria"
            )
            out.append((int(row.group(1)), row.group(2), tuple(measured), line))
        self.assertTrue(out, "the ranked backlog table no longer parses")
        return out

    def blind_spot_table(self) -> dict[str, tuple[int, str, str]]:
        """`src/` file -> (printed count, per-tier breakdown, the ranked-gaps cell)."""
        found = {}
        for line in self.section("| `src/` file | printed |", "**Where the two").splitlines():
            row = re.match(r"\| `(src/[a-z_]+\.rs)` \| (\d+) \| ([^|]+) \| ([^|]+) \|", line)
            if row:
                found[row.group(1)] = (
                    int(row.group(2)), row.group(3).strip(), row.group(4).strip()
                )
        self.assertTrue(found, "the golden blind spots join table no longer parses")
        return found

    def test_every_enumerated_feature_is_classified_exactly_once(self) -> None:
        """One key per feature, and no spec location owned by two regions."""
        keys = [
            cells[0].strip("`")
            for path in sorted(self.REGIONS.glob("*.md"))
            for cells in self.region_rows(path.read_text(encoding="utf-8"))
        ]
        self.assertEqual(len(keys), len(set(keys)), "a feature key appears in two rows")
        stated = re.search(r"The (\d+) rows carry (\d+) distinct\s+keys", self.doc)
        self.assertIsNotNone(stated, "the reconciliation no longer states the row count")
        self.assertEqual(
            [len(keys), len(set(keys))],
            [int(stated.group(1)), int(stated.group(2))],
            "the reconciliation's row count is not the walk's own",
        )
        owners: dict[str, set[str]] = {}
        for region, cells in self.entries.values():
            owners.setdefault(cells[2], set()).add(region)
        shared = {loc: sorted(names) for loc, names in owners.items() if len(names) > 1}
        self.assertEqual({}, shared, "a spec location is classified in two region files")

    def test_the_summary_table_is_the_six_region_files_own_row_counts(self) -> None:
        """Per-region totals, recomputed from the tables they aggregate."""
        stated = {}
        for line in self.section("### What the walk enumerated", "The walk enumerated").splitlines():
            row = re.match(
                r"\| \[`([a-z0-9-]+)`\][^|]*\|" + r"\s*(\d+)\s*\|" * 7, line
            )
            if row:
                stated[row.group(1)] = [int(row.group(n)) for n in range(2, 9)]
        self.assertEqual(6, len(stated), "the summary table no longer lists six regions")
        totals = re.search(
            r"\| \*\*total\*\* \|" + r"\s*\*\*(\d+)\*\*\s*\|" * 7,
            self.section("### What the walk enumerated", "The walk enumerated"),
        )
        self.assertIsNotNone(totals, "the summary table no longer carries a total row")
        self.assertEqual(
            [sum(column) for column in zip(*stated.values())],
            [int(totals.group(n)) for n in range(1, 8)],
            "the total row is not the six region rows' own column sums",
        )
        for region, numbers in sorted(stated.items()):
            with self.subTest(region=region):
                rows = [c for r, c in self.entries.values() if r == region]
                counts = [len(rows)]
                counts += [
                    sum(1 for cells in rows if cells[3].strip("`") == category)
                    for category in self.CATEGORIES
                ]
                counts += [
                    sum(
                        1
                        for cells in rows
                        if cells[3].strip("`") == "gap"
                        and self.settlement_of(cells) == settlement
                    )
                    for settlement in self.SETTLEMENTS
                ]
                self.assertEqual(counts, numbers)

    def test_the_prose_totals_are_the_summary_tables_own_column_sums(self) -> None:
        """The narrated 402/271/42/89 and 39/30/20 are the table's totals."""
        rows = list(self.entries.values())
        totals = [len(rows)]
        totals += [
            sum(1 for _r, cells in rows if cells[3].strip("`") == category)
            for category in self.CATEGORIES
        ]
        prose = self.section("The walk enumerated", "**What the `gap` count means.**")
        narrated = [int(value.replace(",", "")) for value in re.findall(r"\*\*([\d,]+)\*\*", prose)]
        self.assertEqual(totals + [len(self.gaps(s)) for s in self.SETTLEMENTS], narrated)
        self.assertEqual(
            totals[3],
            sum(len(self.gaps(s)) for s in self.SETTLEMENTS),
            "the settlement classes do not partition the gap rows",
        )

    def test_the_gap_count_paragraph_recomputes_its_own_numbers(self) -> None:
        """What `gap` means restates the gap total twice, then its two parts."""
        gap = sum(
            1 for _region, cells in self.entries.values() if cells[3].strip("`") == "gap"
        )
        unreachable = len(self.gaps("UNREACHABLE"))
        prose = self.section("**What the `gap` count means.**", "### Reconciliation")
        self.assertEqual(
            [gap, gap, unreachable, gap - unreachable],
            [int(value) for value in re.findall(r"\b(\d+)\b", prose)],
            "the paragraph's counts are not the walk's own gap totals",
        )

    def ledger_keys(self) -> set[str]:
        """The keys the index's own documented join reports, run here."""
        pattern = re.search(
            r"^grep -oP '(.+)' docs/fern-limitations\.md", self.doc, re.M
        )
        self.assertIsNotNone(pattern, "the index no longer documents the join command")
        before, _, after = pattern.group(1).partition("\\K")
        ledger = (REPO / "docs" / "fern-limitations.md").read_text(encoding="utf-8")
        return set(re.findall(f"{before}({after})", ledger, re.M))

    def test_the_reconciliation_counts_the_rows_it_narrates(self) -> None:
        """How many spec locations carry several rows, and the three named by size."""
        owners: dict[str, int] = {}
        for _region, cells in self.entries.values():
            owners[cells[2]] = owners.get(cells[2], 0) + 1
        shared = {loc: count for loc, count in owners.items() if count > 1}
        flat = " ".join(
            self.section(
                "**Each feature is classified exactly once.**", "**Nothing is left"
            ).split()
        )
        stated = re.search(r"(\w+) spec locations carry more than one row", flat)
        self.assertIsNotNone(stated, "the reconciliation no longer counts the shared locations")
        self.assertEqual(len(shared), {"Thirteen": 13}.get(stated.group(1)))
        named = 0
        for location, count in sorted(shared.items()):
            if f"`{location}`" not in flat:
                continue
            named += 1
            with self.subTest(location=location):
                follows = re.search(
                    rf"`{re.escape(location)}`(?: heads)? (\d+)", flat
                )
                self.assertIsNotNone(follows, f"{location} is named without its row count")
                self.assertEqual(count, int(follows.group(1)))
        self.assertEqual(3, named, "the reconciliation no longer names three locations by size")

    def test_the_ledger_join_counts_the_keys_it_reports(self) -> None:
        """56 reported, 51 spelled by a region row, 55 that are feature keys."""
        keys = self.ledger_keys()
        verbatim = keys & set(self.entries)
        text = self.section("**Every ledger key is accounted for.**", "**The one correction")
        stated = re.search(
            r"canonical join reports (\d+) keys, of\nwhich (\d+) are a region row's key verbatim", text
        )
        self.assertIsNotNone(stated, "the reconciliation no longer counts the join")
        self.assertEqual((len(keys), len(verbatim)), (int(stated.group(1)), int(stated.group(2))))
        unaccounted = sorted(keys - verbatim)
        self.assertEqual(
            len(unaccounted),
            len(re.findall(r"^\| `([^`]+)` \|", text, re.M)),
            "the table of unaccounted keys is not the join's own remainder",
        )
        for key in unaccounted:
            self.assertIn(f"| `{key}` |", text, f"{key} has no row saying how it is accounted for")
        yielded = re.search(r"The join's real yield is (\d+)\.", text)
        self.assertIsNotNone(yielded, "the reconciliation no longer states the join's real yield")
        self.assertEqual(len(keys) - 1, int(yielded.group(1)), "one key is the non-feature label")

    def test_the_ranked_backlog_is_every_fixture_gap_in_rubric_order(self) -> None:
        """One total order over every `FIXTURE` row, by the four published numbers."""
        ranked = self.ranked_rows()
        self.assertEqual(self.gaps("FIXTURE"), {key for _n, key, _m, _line in ranked})
        self.assertEqual(
            list(range(1, len(ranked) + 1)), [n for n, _key, _m, _line in ranked]
        )
        sortable = [
            ((sites, -blind, -breadth, -witnesses, key), rank)
            for rank, key, (sites, blind, breadth, witnesses), _line in ranked
        ]
        self.assertEqual(sorted(sortable), sortable, "the ranked table is not in rubric order")
        stated = re.search(r"All (\d+) `FIXTURE` gaps", self.doc)
        self.assertIsNotNone(stated, "the ranked backlog no longer states its own size")
        self.assertEqual(len(ranked), int(stated.group(1)))

    def test_the_ranked_table_names_each_keys_owning_region(self) -> None:
        """The `region` column and the per-row link, against the file the key is in."""
        for _rank, key, _measured, line in self.ranked_rows():
            with self.subTest(key=key):
                region = self.entries[key][0]
                self.assertIn(f"](openapi-surface/{region}.md)", line)
                self.assertIn(f"| `{region}` |", line)

    def test_criterion_one_is_the_region_rows_own_crozier_sites_count(self) -> None:
        """Criterion 1 is the `crozier sites` cell's own integer, not a second copy.

        A cell spells its count several ways — ``` `src/ir.rs`: 6 places ```,
        `src/ir.rs (3 places)`, ``` `src/ir.rs` — 1 ``` — so the count is every
        integer that follows a `src/` file name, and a `src/ir.rs:627` line
        reference is excluded by the digit that follows its colon.
        """
        for _rank, key, measured, _line in self.ranked_rows():
            with self.subTest(key=key):
                cell = self.entries[key][1][5]
                if cell.lstrip("`").startswith("none"):
                    self.assertEqual(0, measured[0], "a `none` cell scores zero sites")
                    continue
                counted = re.findall(r"src/[a-z_]+\.rs`?(?!:\d)[^0-9A-Za-z]{0,14}(\d+)", cell)
                self.assertTrue(counted, f"{key}'s `crozier sites` cell states no count")
                self.assertEqual(sum(int(n) for n in counted), measured[0])

    def test_criterion_three_counts_the_artifact_kinds_its_own_cell_lists(self) -> None:
        """Criterion 3 is a reading of the region row's prose, so it is stated once.

        The region files name the artifacts in prose and publish no breadth
        number; this column normalizes that prose over the vocabulary the criteria
        list defines. What is checkable is that the number is the list beside it
        and that every name in the list is one of the six.
        """
        vocabulary = set(
            re.findall(
                r"`([a-z_./]+)`",
                self.section("**Criterion 3**, artifact breadth", "- **Criterion 4**"),
            )
        )
        self.assertEqual(6, len(vocabulary), "the criteria list no longer names six kinds")
        for _rank, key, measured, line in self.ranked_rows():
            with self.subTest(key=key):
                listed = line.split("|")[6].split("(", 1)[1].rsplit(")", 1)[0].split(", ")
                self.assertEqual(measured[2], len(listed))
                self.assertEqual(set(), set(listed) - vocabulary, "an artifact kind is not one of the six")

    def test_the_ranked_backlog_publishes_its_own_median_blind_spot_count(self) -> None:
        """The number the extension rule is stated in, recomputed from the rows."""
        blind = sorted(measured[1] for _n, _key, measured, _line in self.ranked_rows())
        median = blind[len(blind) // 2] if len(blind) % 2 else (
            blind[len(blind) // 2 - 1] + blind[len(blind) // 2]
        ) // 2
        stated = re.search(
            r"\*\*The median blind-spot count of this list is (\d+)\*\*", self.doc
        )
        self.assertIsNotNone(stated, "the ranked backlog no longer publishes its median")
        self.assertEqual(median, int(stated.group(1)))

    def test_each_ranked_row_reads_its_blind_spot_count_off_the_join_table(self) -> None:
        """Criterion 2 is the join table's own `printed` column, summed per row."""
        blind_spots = self.blind_spot_table()
        for _rank, key, measured, line in self.ranked_rows():
            with self.subTest(key=key):
                named = re.findall(r"`(src/[a-z_]+\.rs)` \d+", line)
                sites_named, blind_named = named[: len(named) // 2], named[len(named) // 2 :]
                self.assertEqual(
                    sites_named,
                    blind_named,
                    "criterion 2 does not score the files criterion 1 names",
                )
                self.assertEqual(
                    sum(blind_spots[name][0] for name in blind_named),
                    measured[1],
                    "criterion 2 is not the join table's printed count",
                )
                if not named:
                    self.assertEqual(
                        (0, 0), (measured[0], measured[1]), "a `none` row must score zero twice"
                    )

    def test_the_join_table_names_the_ranked_gaps_that_point_at_each_file(self) -> None:
        """The `ranked gaps pointing at it` cells are the ranked table's own counts."""
        pointing: dict[str, int] = {}
        for _rank, _key, _measured, line in self.ranked_rows():
            for name in set(re.findall(r"`(src/[a-z_]+\.rs)` \d+", line)):
                pointing[name] = pointing.get(name, 0) + 1
        for name, (_printed, _by_tier, cell) in sorted(self.blind_spot_table().items()):
            with self.subTest(file=name):
                stated = 0 if cell.startswith("none") else int(re.match(r"(\d+)", cell).group(1))
                self.assertEqual(pointing.get(name, 0), stated)

    def test_the_join_table_is_the_coverage_reports_own_blind_spot_block(self) -> None:
        """The one input outside `just check`, reconciled whenever its export exists.

        `just fixtures-coverage` needs network and an instrumented corpus run, so
        the gate cannot produce the measurement — but it can refuse a table that
        disagrees with the last one produced. The recipe's own
        `blind_spots()` renders the comparison, and the export paths and tier
        names are read out of `scripts/fixtures-coverage.sh`, so renaming either
        fails this case rather than turning it into a permanent silent skip. It
        skips, named, when the exports are absent, the way the corpus byte-diffs
        skip an unfetched spec.
        """
        recipe = (REPO / "scripts" / "fixtures-coverage.sh").read_text(encoding="utf-8")
        out_dir = re.search(r'^out_dir="\$repo_root/([^"]+)"', recipe, re.M)
        golden = re.search(r"^  --golden-tier (\S+)", recipe, re.M)
        self.assertTrue(out_dir and golden, "fixtures-coverage.sh no longer names its exports")
        exports = REPO / out_dir.group(1)
        names = re.findall(r'--output-path "\$out_dir/([a-z0-9-]+)\.json"', recipe)
        self.assertIn(golden.group(1), names, "the golden tier has no export in the recipe")
        order = [golden.group(1)] + sorted(name for name in names if name != golden.group(1))
        missing = sorted(name for name in order if not (exports / f"{name}.json").is_file())
        if missing:
            self.skipTest(
                f"no {', '.join(missing)} export in {exports}; run `just fixtures-coverage`"
            )
        spec = importlib.util.spec_from_file_location(
            "fixtures_coverage_report", REPO / "scripts" / "fixtures-coverage-report.py"
        )
        report = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(report)
        tiers = {name: report.load_tier(exports / f"{name}.json", REPO) for name in order}
        report.drop_test_regions(tiers, REPO)
        measured, total = {}, None
        for line in report.blind_spots(tiers, golden.group(1), order):
            row = re.match(r"  (src/\S+)\s+(\d+)\s+\((.+)\)$", line)
            if row:
                measured[row.group(1)] = (int(row.group(2)), row.group(3))
            elif line.startswith("  total "):
                total = line.strip()
        self.assertTrue(measured, "the report's blind-spot block no longer parses")
        self.assertEqual(
            measured,
            {name: cells[:2] for name, cells in self.blind_spot_table().items()},
            "the join table is not the last `just fixtures-coverage` run's blind spots",
        )
        self.assertIn(
            f"`{total}`", self.doc, "the join table does not quote the report's own total line"
        )

    def test_the_ranked_backlog_counts_its_own_populations(self) -> None:
        """The "N of the 39" figures the criteria list and the join narrate."""
        ranked = self.ranked_rows()
        zero_witness = sum(1 for _n, _key, measured, _line in ranked if measured[3] == 0)
        no_file = sum(1 for _n, _key, measured, _line in ranked if measured[0] == 0)
        flat = " ".join(self.doc.split())
        for population, total in re.findall(r"(\d+) of the (\d+)(?= ranked| entries| score)", flat):
            self.assertEqual(len(ranked), int(total), "a population is stated against the wrong total")
            self.assertIn(
                int(population), (zero_witness, no_file), "a stated population is neither count"
            )
        self.assertIn(f"{zero_witness} of the {len(ranked)} score zero", flat)
        self.assertIn(f"{no_file} of the {len(ranked)} entries name no", flat)
        self.assertIn(f"{no_file} of the {len(ranked)} ranked entries reach no", flat)

    def test_the_two_largest_unranked_files_sum_as_the_join_narrates(self) -> None:
        """The share of the block the two files no ranked gap points at hold."""
        table = self.blind_spot_table()
        unranked = sorted(
            (count, name)
            for name, (count, _tier, cell) in table.items()
            if cell.startswith("none")
        )
        largest = sum(count for count, _name in unranked[-2:])
        flat = " ".join(self.doc.split())
        stated = re.search(r"together ([\d,]+) of the block's ([\d,]+) printed regions", flat)
        self.assertIsNotNone(stated, "the join no longer states the two largest files' share")
        self.assertEqual(
            (largest, sum(count for count, _tier, _cell in table.values())),
            tuple(int(value.replace(",", "")) for value in stated.groups()),
        )
        paragraph = flat[: stated.start()][-200:]
        for _count, name in unranked[-2:]:
            self.assertIn(f"`{name}`", paragraph, f"{name} is not one of the two named")

    def test_the_probe_backlog_is_every_probe_gap_and_nothing_else(self) -> None:
        """The other backlog: probe work, listed apart from the fixture work."""
        listed = set(
            re.findall(r"^\| \[`([^`]+)`\]", self.section("## The probe backlog"), re.M)
        )
        self.assertEqual(self.gaps("PROBE"), listed)
        self.assertEqual(set(), listed & {key for _n, key, _m, _l in self.ranked_rows()})
        stated = re.search(r"The other (\d+) `gap` rows", self.doc)
        self.assertIsNotNone(stated, "the probe backlog no longer states its own size")
        self.assertEqual(len(listed), int(stated.group(1)))

    def test_the_documented_witness_supply_derivation_is_the_region_files_own(self) -> None:
        """The probe backlog derives its witness-supply set; run the command it prints.

        The index deliberately publishes no count beside that command — a number
        there would be the transcription the section promises not to make — so the
        command *is* the contract, and an untested one silently returns a shorter
        list the day a settlement cell is reworded. This runs it, and holds it to
        the two things that make its answer meaningful: it agrees with the same
        derivation done here, and every key it names is really a `PROBE` gap row.
        That last clause is the one with teeth. A row keeping the marker phrase
        while moving to `FIXTURE` — which is what `dollar-anchor` did — reads as a
        probe in this list and as fixture work everywhere else, and nothing but
        this assertion would say so.
        """
        command = re.search(
            r"^grep -h '[^']+' docs/openapi-surface/\*\.md \| grep -oP '[^']+'$",
            self.doc,
            re.M,
        )
        self.assertIsNotNone(command, "the probe backlog no longer documents its derivation")

        marker = re.search(r"grep -h '([^']+)'", command.group(0)).group(1)
        derived = {
            key
            for key, (_region, cells) in self.entries.items()
            if re.search(marker, cells[7])
        }
        self.assertTrue(derived, "the documented marker matches no settlement cell")

        if not grep_speaks_pcre():
            self.skipTest("this grep has no PCRE support, so the command cannot run here")
        run = subprocess.run(
            ["bash", "-c", command.group(0)], cwd=REPO, capture_output=True, text=True
        )
        # A pipeline's exit status is its last command's, and `grep` exits 1 on no
        # match, so an empty answer has to be a red rather than a quiet zero.
        self.assertEqual(0, run.returncode, run.stderr)
        self.assertEqual(derived, set(run.stdout.split()))
        self.assertEqual(
            set(),
            derived - self.gaps("PROBE"),
            "a row keeps the witness-supply marker but no longer settles PROBE",
        )

    def probe_kind(self, key: str, cells: list[str]) -> str:
        """Which of the two kinds this `PROBE` row's own settlement cell declares.

        The declaration is the bolded word, so a cell may say *why it is not the
        other one* — `witness-supply` grounds "rather than structural ones" — in
        prose without declaring both.
        """
        declared = [
            kind
            for kind in self.PROBE_KINDS
            if re.search(rf"\*\*{re.escape(kind)}\*\*", cells[7])
        ]
        self.assertEqual(
            1,
            len(declared),
            f"{key}: a PROBE settlement cell declares exactly one of "
            f"**structural** or **witness-supply**; this one declares {declared}",
        )
        return declared[0]

    def census_selectors_cited(self, cell: str) -> list[str]:
        """What in `cell` names a census selector: a selector span, or the word.

        The selector set is read out of the script's own grammar rather than
        transcribed, so a selector declared tomorrow is covered today. A code span
        counts only when the *whole* span is a selector — a Rust `match` pattern
        that happens to contain `scheme.scheme` is not a citation of one.
        """
        selectors, _prefixes = census.grammar()
        cited = [
            f"`{span}`"
            for span in re.findall(r"`([^`]+)`", cell)
            if span.partition("=")[0].partition(":")[0] in selectors
        ]
        return cited + re.findall(r"(?i)\b(?:the |a )?(selectors?)\b", cell)

    def witness_search_rows(self, region: str) -> dict[str, str]:
        """key -> the `sources searched and the exact query` cell, per region file."""
        text = (self.REGIONS / f"{region}.md").read_text(encoding="utf-8")
        if self.WITNESS_SEARCH not in text:
            return {}
        found = {}
        for line in text.split(self.WITNESS_SEARCH, 1)[1].splitlines():
            if not line.startswith("| "):
                continue
            cells = [
                cell.replace("\x00", "\\|").strip()
                for cell in line.replace("\\|", "\x00").strip().strip("|").split("|")
            ]
            if len(cells) == 7 and cells[0].startswith("`"):
                found[cells[0].strip("`")] = cells[6]
        return found

    def witness_sources_queried(self, cell: str) -> dict[str, str]:
        """Each required source's bold label in `cell`, mapped to the text under it.

        A row states its sources as bold labels in one cell, so a source's segment
        runs from its own label to the next one — which is where the query put to
        it has to be.
        """
        labels = list(re.finditer(r"\*\*[^*]+\*\*", cell))
        found = {}
        for name, pattern in self.REQUIRED_WITNESS_SOURCES.items():
            label = next(
                (match for match in labels if re.search(pattern, match.group(0))), None
            )
            if label is not None:
                found[name] = (label.start(), label.end())
        starts = sorted(start for start, _end in found.values())
        return {
            name: cell[end : next((s for s in starts if s > start), len(cell))]
            for name, (start, end) in found.items()
        }

    def test_every_probe_row_is_one_of_two_kinds_and_cites_no_census_selector(self) -> None:
        """A `PROBE` row says which kind it is, and never settles on the census.

        A selector reporting zero is `gap` evidence — the census's own statement
        that no *registered* source declares the shape — and reading it as a
        settlement is what put twenty-five rows in this class on a 124-spec
        sample. A shape the grammar cannot express has measured nothing at all.
        """
        for key in sorted(self.gaps("PROBE")):
            _region, cells = self.entries[key]
            with self.subTest(key=key):
                self.probe_kind(key, cells)
                self.assertEqual(
                    [],
                    self.census_selectors_cited(cells[7]),
                    f"{key}: its PROBE settlement cell names a census selector as "
                    f"its reason; a selector reporting zero belongs in the "
                    f"`evidence` cell as `gap` evidence, not in the settlement",
                )

    def test_every_witness_supply_probe_names_its_sources_and_their_queries(self) -> None:
        """The issue's own acceptance criterion, as a failure rather than a memo.

        A witness-supply `PROBE` claims the world supplies no witness. The only
        thing that backs a claim that size is the search itself, so the row is
        held to carrying one: a line of its own region file's witness-search
        table, naming every required source with the query put to each. Without
        this, "0 declarations across the registered sources" reads as the same
        claim and nothing says otherwise.
        """
        for key in sorted(self.gaps("PROBE")):
            region, cells = self.entries[key]
            if self.probe_kind(key, cells) != "witness-supply":
                continue
            with self.subTest(key=key):
                searched = self.witness_search_rows(region)
                # Not `assertIn`: the container is every witness-search cell in the
                # region, and printing it buries the message that names the row.
                self.assertTrue(
                    key in searched,
                    f"{key}: settles PROBE on witness-supply grounds with no row "
                    f"in {region}.md's `{self.WITNESS_SEARCH}` table",
                )
                queried = self.witness_sources_queried(searched[key])
                self.assertEqual(
                    set(self.REQUIRED_WITNESS_SOURCES),
                    set(queried),
                    f"{key}: its witness-search row omits "
                    f"{sorted(set(self.REQUIRED_WITNESS_SOURCES) - set(queried))}",
                )
                for name, segment in sorted(queried.items()):
                    self.assertTrue(
                        "`" in segment or "→" in segment,
                        f"{key}: its witness-search row names {name} with no query "
                        f"against it — a source is named with the exact query put "
                        f"to it and what that returned",
                    )

    def test_the_probe_backlog_splits_by_the_kind_each_region_row_declares(self) -> None:
        """The index's two named parts are the region files' own settlement cells."""
        kinds: dict[str, set[str]] = {kind: set() for kind in self.PROBE_KINDS}
        for key in sorted(self.gaps("PROBE")):
            kinds[self.probe_kind(key, self.entries[key][1])].add(key)
        for kind, expected in kinds.items():
            heading = f"### {kind[0].upper()}{kind[1:]} probes"
            with self.subTest(kind=kind):
                body = self.section(heading, "\n### " if kind == "structural" else None)
                listed = set(re.findall(r"^\| \[`([^`]+)`\]", body, re.M))
                self.assertEqual(
                    expected, listed, f"{heading} is not the rows whose cells say {kind}"
                )
                stated = re.match(r"\s*\*\*(\d+) rows?\.\*\*", body)
                self.assertIsNotNone(stated, f"{heading} no longer states its own size")
                self.assertEqual(len(expected), int(stated.group(1)))

    def test_the_stated_registered_and_golden_source_counts_are_measured(self) -> None:
        """124 registered / 107 golden-bearing, measured rather than transcribed."""
        sources = census.registered_sources(FIXTURES, REPO / ".local" / "corpus", False)
        aliases = census.corpus_aliases(FIXTURES)
        golden = sum(
            1
            for source in sources
            if (FIXTURES / aliases.get(source.fixture, source.fixture) / "expected").is_dir()
        )
        stated = re.search(
            r"It reads \*\*(\d+)\*\* registered sources, of which\n\s*\*\*(\d+)\*\* carry a committed golden",
            self.doc,
        )
        self.assertIsNotNone(stated, "the section no longer states the source counts")
        self.assertEqual(
            (len(sources), golden), (int(stated.group(1)), int(stated.group(2)))
        )


DOCUMENT = """openapi: 3.0.3
info: {{title: {name}, version: "1"}}
paths:
{paths}
"""

OPERATION = """    {method}:
{fields}
      responses:
        "200":
          description: ok"""


def document(name: str, routes: list[tuple[str, list[str]]]) -> str:
    """One source document declaring `routes`: a path key and its operations' fields."""
    paths = []
    for path, operations in routes:
        paths.append(f"  {json.dumps(path)}:")
        for index, fields in enumerate(operations):
            method = ("get", "post", "put", "delete")[index]
            body = "\n".join(f"      {line}" for line in fields.splitlines())
            paths.append(OPERATION.format(method=method, fields=body))
    return DOCUMENT.format(name=name, paths="\n".join(paths))


class PredicateSelectorTests(unittest.TestCase):
    """The third kind of selector: a shape the field selector cannot express.

    `operation.tags` counts the field and not its members, `operation.operationId`
    records declarations and not values, and a Paths Object key is a *name* the
    grammar excludes — so three real shapes were invisible to the instrument that
    is supposed to say whether the corpus has ever seen them. These drive the real
    script over real documents on the real filesystem, once for a document that
    declares each shape and once for one that does not.
    """

    def census(self, sources: dict[str, str], *selectors: str) -> subprocess.CompletedProcess:
        """Run the real script over a fixtures root holding `sources`."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name, body in sources.items():
                write_fixture(root, name, body)
            arguments = ["--vendored-only", "--fixtures-root", str(root)]
            for selector in selectors:
                arguments += ["--selector", selector]
            completed = run(*arguments)
        self.assertEqual(0, completed.returncode, completed.stderr)
        return completed

    def counts(self, sources: dict[str, str], selector: str) -> dict[str, int]:
        """The reported count per source for one selector; absent sources are 0."""
        completed = self.census(sources, selector)
        return {fixture: count for (_selector, fixture), count in rows(completed).items()}

    def test_a_multi_tag_operation_is_counted_once_per_operation(self) -> None:
        """`operation.tags:multiple`: the array's members, which the field cannot show."""
        sources = {
            "two-tagged": document("two-tagged", [
                ("/widgets", ["tags: [alpha, beta]", "tags: [alpha, beta, gamma]"]),
                ("/gadgets", ["tags: [alpha]"]),
            ]),
            "single-tagged": document("single-tagged", [
                ("/widgets", ["tags: [alpha]", "tags: []"]),
            ]),
        }
        self.assertEqual({"two-tagged": 2}, self.counts(sources, "operation.tags:multiple"))
        # The field selector still counts every declaration, multiple or not: the
        # predicate adds a reading of `tags`, it does not replace one.
        self.assertEqual(
            {"two-tagged": 3, "single-tagged": 2},
            self.counts(sources, "operation.tags"),
        )

    def test_a_duplicated_operation_id_counts_every_operation_that_writes_it(self) -> None:
        """`operation.operationId:duplicate`: two values compared, not two declarations."""
        sources = {
            "repeated-id": document("repeated-id", [
                ("/widgets", ["operationId: listWidgets", "operationId: listWidgets"]),
                ("/gadgets", ["operationId: listGadgets"]),
            ]),
            "thrice-repeated-id": document("thrice-repeated-id", [
                ("/widgets", ["operationId: one", "operationId: one", "operationId: one"]),
            ]),
            "distinct-ids": document("distinct-ids", [
                ("/widgets", ["operationId: listWidgets", "operationId: createWidget"]),
            ]),
        }
        self.assertEqual(
            {"repeated-id": 2, "thrice-repeated-id": 3},
            self.counts(sources, "operation.operationId:duplicate"),
        )

    def test_a_link_objects_operation_id_is_not_an_operations(self) -> None:
        """The object-model rule holds for the predicate too.

        `apideck.com-crm` writes `"operationId": "usersOne"` seven times and
        declares no duplicate: six of the seven are Link Objects naming the
        operation they follow. A text match over that document reports six
        duplicates that no Operation Object declares.
        """
        source = """\
            openapi: 3.0.3
            info: {title: linked, version: "1"}
            paths:
              /widgets:
                get:
                  operationId: listWidgets
                  responses:
                    "200":
                      description: ok
                      links:
                        next:
                          operationId: listWidgets
            """
        counted = self.counts({"linked": source}, "operation.operationId:duplicate")
        self.assertEqual({}, counted)
        self.assertEqual({"linked": 1}, self.counts({"linked": source}, "link.operationId"))

    def test_a_normalized_path_collision_counts_every_colliding_key(self) -> None:
        """`openapi.paths:normalized-collision`: the map keys the grammar excludes."""
        sources = {
            "colliding-paths": document("colliding-paths", [
                ("/users/{userId}", ["operationId: a"]),
                ("/users/{user_id}", ["operationId: b"]),
                ("/gadgets", ["operationId: c"]),
            ]),
            "three-colliding-paths": document("three-colliding-paths", [
                ("/z/{itemId}", ["operationId: a"]),
                ("/z/{item_id}", ["operationId: b"]),
                ("/z/{itemID}", ["operationId: c"]),
            ]),
            "distinct-paths": document("distinct-paths", [
                ("/users/{userId}", ["operationId: a"]),
                ("/users/{ownerId}", ["operationId: b"]),
            ]),
        }
        self.assertEqual(
            {"colliding-paths": 2, "three-colliding-paths": 3},
            self.counts(sources, "openapi.paths:normalized-collision"),
        )

    # Templates spanning what crozier's normalization distinguishes: the variable
    # name alone, where the variable sits, how many segments there are, literals
    # mixed with variables, and every case `naming::field_name` treats specially —
    # camel and acronym boundaries, a reserved name, a digit-leading name, a
    # digit-bearing word joining its neighbour, a digit-adjacent underscore
    # collapsing, and a non-identifier character folding to a boundary. The
    # expectation on each line is what crozier's own transform implies, not what
    # this script happens to compute: `NamingMirrorTests` below pins the transform
    # against `src/naming.rs`'s own expectations.
    NORMALIZATION_CASES: tuple[tuple[str, list[str], int], ...] = (
        ("camel-and-snake", ["/users/{userId}", "/users/{user_id}"], 2),
        ("acronym-boundary", ["/users/{userID}", "/users/{user_id}"], 2),
        ("distinct-variable-names", ["/users/{userId}", "/users/{ownerId}"], 0),
        ("variable-position", ["/{id}/users", "/users/{id}"], 0),
        ("segment-count", ["/users/{id}", "/users/{id}/roles"], 0),
        ("literal-not-a-variable", ["/users/{id}", "/users/id"], 0),
        ("literals-and-two-variables",
         ["/a/{fooBar}/b/{baz-qux}", "/a/{foo_bar}/b/{bazQux}"], 2),
        ("literal-segment-differs",
         ["/a/{fooBar}/b/{bazQux}", "/a/{fooBar}/c/{bazQux}"], 0),
        ("one-variable-differs",
         ["/a/{fooBar}/b/{bazQux}", "/a/{fooBar}/b/{quxBaz}"], 0),
        ("reserved-name", ["/x/{list}", "/x/{list_}"], 2),
        ("reserved-name-control", ["/x/{list}", "/x/{lists}"], 0),
        ("digit-leading-name", ["/x/{2fa-enabled}", "/x/{2fa_enabled}"], 2),
        ("digit-leading-control", ["/x/{2fa}", "/x/{2Fa}"], 0),
        ("digit-word-joins", ["/x/{user2FA}", "/x/{user2fa}"], 2),
        ("digit-boundary-collapses", ["/x/{address_line_1}", "/x/{addressLine1}"], 2),
        ("non-identifier-folds", ["/x/{filter[name]}", "/x/{filterName}"], 2),
        ("no-variables-at-all", ["/a", "/b"], 0),
    )

    def test_the_path_normalization_is_croziers_own(self) -> None:
        """Every case crozier's `naming::field_name` distinguishes, in one run."""
        sources = {
            name: document(name, [(path, ["operationId: op"]) for path in paths])
            for name, paths, _expected in self.NORMALIZATION_CASES
        }
        counted = self.counts(sources, "openapi.paths:normalized-collision")
        self.assertEqual(
            {name: expected for name, _paths, expected in self.NORMALIZATION_CASES if expected},
            counted,
        )

    def test_a_document_declaring_none_of_them_reports_each_as_absent(self) -> None:
        """Absent, not missing: the phrase a `gap` row cites as its evidence."""
        plain = {"plain": document("plain", [
            ("/widgets/{id}", ["tags: [alpha]\noperationId: listWidgets"]),
            ("/gadgets", ["operationId: listGadgets"]),
        ])}
        completed = self.census(plain, *sorted(census.PREDICATES))
        self.assertEqual({}, rows(completed))
        for selector in census.PREDICATES:
            with self.subTest(selector=selector):
                self.assertIn(selector, completed.stdout)
        self.assertEqual(
            len(census.PREDICATES),
            completed.stdout.count("(declared by no registered source)"),
        )

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root, "plain", plain["plain"])
            arguments = ["--vendored-only", "--fixtures-root", str(root), "--json"]
            for selector in sorted(census.PREDICATES):
                arguments += ["--selector", selector]
            payload = json.loads(run(*arguments).stdout)
        self.assertEqual([], payload["rows"])
        self.assertEqual(sorted(census.PREDICATES), payload["absent_selectors"])

    def test_each_predicate_selector_is_accepted_by_name(self) -> None:
        """The refusal that guards a typo must not refuse the three real ones."""
        for selector in sorted(census.PREDICATES):
            with self.subTest(selector=selector):
                self.assertIsNone(census.selector_error(selector))


class NamingMirrorTests(unittest.TestCase):
    """`openapi.paths:normalized-collision` normalizes the way crozier does.

    The census is Python and crozier is Rust, so the transform is mirrored rather
    than shared. What keeps the mirror honest is that `src/naming.rs`'s own unit
    tests already pin `field_name` case by case, against Fern's measured output —
    so those expectations are read out of the Rust source here and re-asserted
    against the port. A change to crozier's casing fails this test.
    """

    NAMING = REPO / "src" / "naming.rs"
    CASE = re.compile(
        r'assert_eq!\(\s*field_name\("((?:[^"\\]|\\.)*)"\),\s*"((?:[^"\\]|\\.)*)"\s*,?\s*\)'
    )

    @staticmethod
    def unescape(literal: str) -> str:
        return literal.replace('\\"', '"').replace("\\\\", "\\")

    def cases(self) -> list[tuple[str, str]]:
        found = [
            (self.unescape(wire), self.unescape(expected))
            for wire, expected in self.CASE.findall(
                self.NAMING.read_text(encoding="utf-8")
            )
        ]
        self.assertGreater(
            len(found), 25, "src/naming.rs no longer pins field_name case by case"
        )
        return found

    def test_the_port_reproduces_croziers_own_field_name_expectations(self) -> None:
        for wire, expected in self.cases():
            with self.subTest(wire=wire):
                self.assertEqual(expected, census.field_name(wire))

    def test_the_reserved_set_is_croziers_own(self) -> None:
        """The trailing-`_` rule is only right if the reserved set is the same one.

        Both directions, because both are collisions the census would invent. A
        name crozier reserves and the port does not leaves `/x/{list}` and
        `/x/{list_}` apart, which crozier renders as one URL; a name the port
        reserves and crozier does not brings `/x/{id}` and `/x/{id_}` together,
        which crozier renders as two. The `field_name` cases above cannot catch
        the second — they only exercise the words `src/naming.rs` happens to pin.
        """
        source = self.NAMING.read_text(encoding="utf-8")
        listed = set()
        for marker in ("const RESERVED_BUILTINS: &[&str] =", "const PYTHON_KEYWORDS: &[&str] = &["):
            self.assertIn(marker, source, f"src/naming.rs no longer declares {marker!r}")
            body = source.split(marker, 1)[1].split("];", 1)[0]
            listed |= set(re.findall(r'"([^"]+)"', body))
        self.assertEqual(
            listed,
            set(census._PYTHON_KEYWORDS) | set(census._RESERVED_BUILTINS),
            "the port's reserved set is not crozier's",
        )
        for name in listed:
            with self.subTest(name=name):
                self.assertTrue(census.is_reserved(name))
        self.assertFalse(census.is_reserved("widget"))

    def test_a_path_template_normalizes_only_its_expressions(self) -> None:
        """The literal text is what distinguishes two routes; it must not move."""
        self.assertEqual(
            "/users/{user_id}/roles/{role_id}",
            census.normalized_path("/users/{userId}/roles/{roleID}"),
        )
        self.assertEqual("/users/userId", census.normalized_path("/users/userId"))


if __name__ == "__main__":
    unittest.main(verbosity=1, buffer=False, argv=[sys.argv[0], *sys.argv[1:]])
