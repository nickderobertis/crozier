"""Boundary coverage for the admissible-licence drift gate.

The corpus's admissible-licence rule used to live nowhere: the four names were
restated in prose across a dozen documents and stated authoritatively in none,
so the set drifted out of date without anything noticing. The repair states it
once, in `docs/corpus-licensing.md`, and `tools/corpus-licensing/corpus-licensing-drift.py`
keeps the statement single.

These tests drive the REAL script over the REAL repository — the same
invocation `just lint-corpus-licensing` runs — rather than over a tree of
fixtures standing in for it, because a gate that reads only its own fixtures
proves nothing about the documents it exists to hold. The discriminating cases
plant a second enumeration, or gut the rule, in a scratch repository holding
the real script and a copy of every tracked Markdown document, and require the
script to fail naming the file: without that, "the check passes" would be
indistinguishable from "the check matches nothing at all". They never write the
real tree, which other gate targets read while this one runs.

Run: `just test-corpus-licensing` (part of `just check`).
"""

from __future__ import annotations

import importlib.util
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
SCRIPT = REPO / "tools" / "corpus-licensing" / "corpus-licensing-drift.py"
RULE = "docs/corpus-licensing.md"


def load_gate():
    """The gate as a module, for the cases that read its path constants."""
    spec = importlib.util.spec_from_file_location("corpus_licensing_drift", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_gate(root: Path = REPO) -> subprocess.CompletedProcess[str]:
    """The gate exactly as its `lint-licensing` target runs it, from `root`'s copy."""
    return subprocess.run(
        [sys.executable, str(root / SCRIPT.relative_to(REPO))],
        cwd=root,
        capture_output=True,
        text=True,
    )


def git(root: Path, *args: str) -> None:
    subprocess.run(["git", *args], cwd=root, check=True, capture_output=True)


class ScratchTree(unittest.TestCase):
    """A scratch repository holding the real script and every tracked Markdown
    document as the checkout has them, for the cases that must write the tree."""

    def setUp(self) -> None:
        scratch = tempfile.TemporaryDirectory(prefix="corpus-licensing-test-")
        self.addCleanup(scratch.cleanup)
        self.root = Path(scratch.name)
        listing = subprocess.run(
            ["git", "ls-files", "-z", "--", "*.md"], cwd=REPO, check=True, capture_output=True
        ).stdout.decode("utf-8")
        for path in [*filter(None, listing.split("\0")), SCRIPT.relative_to(REPO).as_posix()]:
            target = self.root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(REPO / path, target)
        git(self.root, "init", "--quiet")
        git(self.root, "add", "--all")
        self.assertEqual(run_gate(self.root).returncode, 0, "the copied tree does not pass as the real one does")


class TheGateHoldsTheFinishedTree(unittest.TestCase):
    def test_the_real_repository_has_no_second_enumeration(self) -> None:
        result = run_gate()
        self.assertEqual(
            result.returncode,
            0,
            f"the tree enumerates the admissible licences outside {RULE}:\n{result.stderr}",
        )

    def test_it_is_quiet_on_success(self) -> None:
        result = run_gate()
        self.assertEqual(result.stdout, "")
        self.assertEqual(result.stderr, "")


class TheGateStillDiscriminates(ScratchTree):
    """Plant a second enumeration in the tree; require a named failure."""

    def plant(self, body: str) -> str:
        handle = tempfile.NamedTemporaryFile(
            dir=self.root / "docs",
            prefix="corpus-licensing-drift-probe-",
            suffix=".md",
            mode="w",
            encoding="utf-8",
            delete=False,
        )
        with handle:
            handle.write(body)
        planted = Path(handle.name)
        # `git ls-files` only reports tracked paths, so the probe has to be
        # staged for the walk to reach it — the same way a real drifting
        # document would arrive.
        git(self.root, "add", "--intent-to-add", "--", str(planted))
        # Git spells paths with forward slashes on every platform, and so does
        # the gate; compare against that spelling, not the host's.
        return planted.relative_to(self.root).as_posix()

    def test_a_planted_second_enumeration_fails_naming_the_file(self) -> None:
        planted = self.plant(
            "# probe\n\nThis document restates the rule: the corpus admits Apache-2.0/MIT/BSD/CC0 and nothing else.\n"
        )
        result = run_gate(self.root)
        self.assertEqual(
            result.returncode,
            1,
            "a document enumerating the admissible licences passed the gate",
        )
        self.assertIn(planted, result.stderr)
        self.assertIn("Apache-2.0/MIT/BSD/CC0", result.stderr)
        self.assertIn(RULE, result.stderr)

    def test_it_reads_a_comma_and_conjunction_list_too(self) -> None:
        """Drift will not necessarily arrive in the spelling it left in."""
        planted = self.plant("# probe\n\nRegistrable sources are MIT, Apache-2.0, BSD-3-Clause and CC0-1.0.\n")
        result = run_gate(self.root)
        self.assertEqual(result.returncode, 1)
        self.assertIn(planted, result.stderr)

    def test_naming_one_licence_as_provenance_is_not_drift(self) -> None:
        """A `CORPUS.md` row's own licence column must stay writable."""
        self.plant(
            "# probe\n\n| source | licence |\n|---|---|\n| `drakkan/sftpgo` |"
            " AGPL-3.0 (the repository's own, per the GitHub API) |\n| `jentic`"
            " | CC0-1.0 (the aggregating repository's `LICENSE`); the document"
            " declares no `info.license` |\n"
        )
        result = run_gate(self.root)
        self.assertEqual(
            result.returncode,
            0,
            f"per-document licence provenance was read as a second copy of the rule:\n{result.stderr}",
        )

    def test_prose_referring_to_the_rule_is_not_drift(self) -> None:
        self.plant(
            "# probe\n\nNot a witness — its licence is outside the admissible"
            " set ([the rule](corpus-licensing.md)), which is stated once and"
            " not restated here.\n"
        )
        self.assertEqual(run_gate(self.root).returncode, 0)


class TheRuleFileIsWhereTheGateSaysItIs(ScratchTree):
    """A gate whose subject can vanish silently is not a gate."""

    def test_removing_the_canonical_enumeration_fails(self) -> None:
        rule = self.root / RULE
        original = rule.read_text(encoding="utf-8")
        rule.write_text(
            original.replace("corpus-licence-set:", "no-longer-the-marker:"),
            encoding="utf-8",
        )
        result = run_gate(self.root)
        self.assertEqual(result.returncode, 1)
        self.assertIn("the canonical enumeration is gone", result.stderr)

    def test_gutting_the_enumeration_under_the_marker_fails_differently(self) -> None:
        """The marker can survive an edit that empties the list beneath it."""
        rule = self.root / RULE
        original = rule.read_text(encoding="utf-8")
        gutted = re.sub(
            r"\*\*Admissible[^\n]*\n(?:[^\n]*\n)*?\n",
            "**Admissible — any licence that grants redistribution.**\n\n",
            original,
            count=1,
        )
        self.assertNotEqual(gutted, original, "the rule's wording moved; retarget this")
        rule.write_text(gutted, encoding="utf-8")
        result = run_gate(self.root)
        self.assertEqual(result.returncode, 1)
        self.assertIn("no longer lists three or more", result.stderr)


class TheGateSpellsPathsTheWayGitDoes(unittest.TestCase):
    """`git ls-files` reports POSIX paths on Windows too, and so must the gate.

    This is a regression guard with a history: the gate first excluded its own
    rule file from its own walk by comparing the listing against
    `str(Path("docs/corpus-licensing.md"))`. On a POSIX host that is the string
    git reports and everything passed; on the Windows leg of `check` it is
    `docs\\corpus-licensing.md`, which matches nothing git ever emits, so the
    rule file was read as an ordinary document and the gate failed quoting the
    canonical enumeration as its own drift. Every other case in this file runs
    the gate as a subprocess on this host and cannot see that, so hold the
    spelling directly.
    """

    def test_the_paths_it_matches_the_listing_against_are_posix_strings(self) -> None:
        gate = load_gate()
        compared = {"RULE": gate.RULE}
        compared.update((f"SKIP_PREFIXES[{index}]", value) for index, value in enumerate(gate.SKIP_PREFIXES))
        compared.update((f"SKIP_FILES[{index}]", value) for index, value in enumerate(gate.SKIP_FILES))
        compared["SKIP_FIXTURE_OUTPUT"] = gate.SKIP_FIXTURE_OUTPUT.pattern
        for name, value in compared.items():
            self.assertIsInstance(
                value,
                str,
                f"{name} is a {type(value).__name__}; a path compared against"
                " `git ls-files` output must be the POSIX string git reports,"
                " because `str(Path(...))` is backslash-spelled on Windows",
            )
            self.assertNotIn("\\", value, f"{name} is spelled with a backslash")

    def test_every_skip_is_decided_on_the_spelling_git_reports(self) -> None:
        """Drive the walk's own decision on git-spelled paths, not this host's.

        `tracked_markdown` shells out to git, so on a POSIX host it can only
        ever see POSIX paths and cannot tell a sound comparison from a
        separator-dependent one. `is_read` is the same predicate the walk
        applies, so feed it the paths git reports directly: each exclusion must
        fire on that spelling, and the documents this repository writes about
        its own corpus must still be read.
        """
        gate = load_gate()
        excluded = (
            RULE,
            "CHANGELOG.md",
            "llmlint-plugins/llmlint-rules/rules/some-rule.md",
            "licenses/fern-APACHE-2.0.md",
            "tests/fixtures/adyen-capital/expected/README.md",
        )
        for path in excluded:
            self.assertFalse(
                gate.is_read(path),
                f"the walk reads {path}, which it is meant to skip; a skip that"
                " misses the spelling `git ls-files` reports skips nothing",
            )
        read = ("tests/fixtures/CORPUS.md", "tests/fixtures/AGENTS.md", "AGENTS.md")
        for path in read:
            self.assertTrue(
                gate.is_read(path),
                f"the walk skips {path}, which is exactly where the rule used to be restated",
            )

    def test_the_walk_still_excludes_the_rule_file(self) -> None:
        gate = load_gate()
        self.assertNotIn(
            RULE,
            gate.tracked_markdown(REPO),
            "the gate reads its own rule file as an ordinary document, so the"
            " canonical enumeration counts as drift against itself",
        )


class TheGateAndItsTestsAreBothInTheDeterministicTier(unittest.TestCase):
    def test_check_runs_both(self) -> None:
        # `just check` runs every affected project's `lint` and `test`; the
        # corpus-licensing project's `lint` aggregate names the gate, its `test`
        # runs this file, and the project is not promoted out of that tier.
        project = json.loads((REPO / "tools" / "corpus-licensing" / "project.json").read_text(encoding="utf-8"))
        targets = project["targets"]
        self.assertNotIn("tier:promoted", project["tags"])
        self.assertIn("lint-licensing", targets["lint"]["dependsOn"])
        self.assertEqual(
            targets["lint-licensing"]["options"]["command"],
            f"python3 {SCRIPT.relative_to(REPO).as_posix()}",
        )
        self.assertEqual(
            targets["test"]["options"]["command"],
            f"python3 {Path(__file__).resolve().relative_to(REPO).as_posix()}",
        )


if __name__ == "__main__":
    unittest.main()
