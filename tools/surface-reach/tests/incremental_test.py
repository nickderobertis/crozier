"""`just census-repin` over a real crozier, measured instrumented, one commit per step.

A scratch clone of a pinned crozier commit carries this tree's tooling on top
(`tools/`, `justfile`, `scripts/`), so the verb under test is the working tree's
and the crate it measures is fixed: a change under `src/` never reruns this
suite. Every step commits a real edit and runs the real recipe, which builds
crozier instrumented and runs the golden tests and hand-written fixture the step
re-runs (`--tests`/`--fixtures` scope the population to a few, so a step takes
minutes). The host cache of bases is a scratch directory; the instrumented-build
lock is the host's own.

The cases, in order (they build on each other's commits and bases):

* a missing base measures fully, and says so;
* a function-body edit re-runs exactly the tests whose base entry executed it;
* a two-step chain (that edit, then comments and a rustfmt reflow plus a second
  body edit) leaves per-test region sets, ledger rows and reach cells equal to a
  full measurement of the same tree;
* a `const`, a template the crate embeds and a `Cargo.lock` dependency each re-run
  every test; a release's own version bump and a `CHANGELOG.md` edit re-run none;
* a compiler change, a base older than seven days and a chain past twenty steps
  each measure fully, naming why;
* a golden's fixture tree and a hand-written fixture's document re-run exactly
  that test and that fixture;
* re-anchoring (a rustfmt split, a duplicate line), a refused changed arm, a merge
  of derived conflicts completed and a hand-written conflict refused;
* the base-publishing CI job's own command packages a full base at the pinned
  commit, served back as `golden-reach-base-<sha>` by a loopback stand-in for
  GitHub's artifact API, and an unscoped repin on a later commit that made every
  derived output stale finds it, steps from it, and restores each output to what
  its own generator writes.

After every step the test checks each entry's commit (re-run entries name the
step's commit, carried ones keep their base's) and the ledger's first line.
"""

from __future__ import annotations

import importlib.util
import io
import json
import os
import re
import shutil
import subprocess
import sys
import threading
import time
import zipfile
from collections.abc import Iterator
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, ClassVar

import pytest

REPO = Path(__file__).resolve().parents[3]
PINNED = "a08dc0421817103e9492361b5ef2cc78b79ff1e0"
OVERLAY = ("tools", "justfile", "scripts")
# Three quick golden tests: the first executes `ONLY_FIRST` and the others do not;
# the second executes `ONLY_SECOND` and the others do not.
TESTS = ("agco_ats_matches_fern_output", "ahasend_api_matches_fern_output", "adyen_capital_matches_fern_output")
FIXTURE = "atlas-untagged-inline-discriminator"
ONLY_FIRST = ("src/ir.rs", "fastapi_endpoint_name")
ONLY_SECOND = ("src/document_refusals/examples.rs", "plain_string")
SCOPE = ("--tests", "^(" + "|".join(TESTS) + ")$", "--fixtures", f"^{FIXTURE}$")
SITE = "src/ir.rs::untagged_inline_discriminator[if untagged \\{]"
SLUG = "owner/crozier"

pytestmark = [
    pytest.mark.skipif(sys.platform == "win32", reason="the instrumented-build lock is taken with fcntl"),
    pytest.mark.skipif(
        shutil.which("just") is None or shutil.which("cargo-llvm-cov") is None, reason="needs just and cargo-llvm-cov"
    ),
]


def _load(name: str, path: Path) -> Any:
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


RS = _load("reach_store", REPO / "tools" / "surface-census" / "reach_store.py")


def git(root: Path, *args: str) -> str:
    run = subprocess.run(["git", *args], cwd=root, capture_output=True, text=True)
    assert run.returncode == 0, f"git {' '.join(args)}: {run.stderr}"
    return run.stdout.strip()


Edit = tuple[str, str] | list[tuple[str, str]]


def pairs(edit: Edit) -> list[tuple[str, str]]:
    return edit if isinstance(edit, list) else [edit]


class Clone:
    """A scratch clone of the pinned commit with this tree's tooling, and the verb's environment."""

    def __init__(self, root: Path, scratch: Path) -> None:
        self.root = root
        self.scratch = scratch
        self.cache = scratch / "bases"
        self.env = {k: v for k, v in os.environ.items() if k not in ("GITHUB_TOKEN", "GH_TOKEN", "CI", "VIRTUAL_ENV")}
        self.env["CROZIER_GOLDEN_REACH_BASE_CACHE"] = str(self.cache)

    def head(self) -> str:
        return git(self.root, "rev-parse", "HEAD")

    def checkout(self, name: str, at: str) -> None:
        git(self.root, "reset", "-q", "--hard")
        git(self.root, "checkout", "-q", "-B", name, at)

    def commit(self, message: str, edits: dict[str, Edit], *, keep: bool = False) -> str:
        """Replace each `old` by `new` once in its file (an empty `old` appends), commit, return the commit.

        The working tree is reset first (a step's regenerated tables are not part of the
        next commit) unless `keep` commits what a tool already changed in it.
        """
        if not keep:
            git(self.root, "reset", "-q", "--hard")
        for path, edit in edits.items():
            target = self.root / path
            text = target.read_text(encoding="utf-8") if target.exists() else ""
            for old, new in pairs(edit):
                if old:
                    assert old in text, f"{path} no longer holds {old!r}; re-pin the edit to the pinned commit"
                    text = text.replace(old, new, 1)
                else:
                    text += new
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text, encoding="utf-8")
        git(self.root, "add", "-A")
        git(self.root, "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "--allow-empty", "-m", message)
        return self.head()

    def run(self, *argv: str, env: dict[str, str] | None = None, check: bool = True) -> subprocess.CompletedProcess:
        run = subprocess.run(argv, cwd=self.root, env=env or self.env, capture_output=True, text=True, timeout=7200)
        if check:
            assert run.returncode == 0, (
                f"{' '.join(argv)} exited {run.returncode}:\n{run.stdout[-3000:]}\n{run.stderr[-6000:]}"
            )
        return run

    def repin(self, *extra: str, scoped: bool = True, **kwargs: Any) -> subprocess.CompletedProcess:
        return self.run("just", "census-repin", *(SCOPE if scoped else ()), *extra, **kwargs)

    def store(self) -> dict:
        return RS.load(self.root / ".local" / "golden-reach" / "store.json.gz")

    def ledger_line(self) -> str:
        return (
            (self.root / "docs" / "openapi-surface" / "golden-reach.tsv").read_text(encoding="utf-8").split("\n", 1)[0]
        )

    def cached(self, commit: str) -> Path:
        return self.cache / commit / "base.json.gz"


@pytest.fixture(scope="module")
def clone(tmp_path_factory: pytest.TempPathFactory) -> Iterator[Clone]:
    scratch = tmp_path_factory.mktemp("incremental")
    root = scratch / "repo"
    git(REPO, "clone", "-q", "--shared", "--no-checkout", str(REPO), str(root))
    git(root, "checkout", "-q", "-B", "work", PINNED)
    for name in OVERLAY:
        source, target = REPO / name, root / name
        if source.is_dir():
            shutil.rmtree(target)
            shutil.copytree(source, target, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache"))
        else:
            shutil.copy2(source, target)
    git(root, "add", "-A")
    git(root, "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "--allow-empty", "-m", "tooling")
    git(root, "remote", "remove", "origin")
    yield Clone(root, scratch)


def entries(store: dict) -> dict[str, str]:
    """`test or fixture -> the commit it last executed at`."""
    return {name: entry["commit"] for part in ("tests", "fixtures") for name, entry in store[part].items()}


def assert_step(clone: Clone, base: str | None, rerun: set[str], before: dict[str, str]) -> dict:
    """The store names the step's commit for each re-run entry and keeps the base's for the rest."""
    head = clone.head()
    store = clone.store()
    assert store["commit"] == head
    names = set(TESTS) | {FIXTURE}
    assert set(entries(store)) == names
    for name, commit in entries(store).items():
        assert commit == (head if name in rerun else before[name]), (name, commit)
    tests_run = len(rerun & set(TESTS))
    origin = f"base {base[:12]}" if base else "base none (full)"
    assert clone.ledger_line().endswith(
        f"; {origin}: {tests_run} run at {head[:12]}, {len(TESTS) - tests_run} carried"
    ), clone.ledger_line()
    return store


def executed_by(store: dict, key: str) -> set[str]:
    return {name for part in ("tests", "fixtures") for name, e in store[part].items() if key in e["regions"]}


def region_sets(clone: Clone, store: dict) -> dict[str, dict[str, set]]:
    tree = RS.read_tree(clone.root)
    return {name: RS.positions(tree, store["functions"], e["regions"]) for name, e in store["tests"].items()}


def reach_cells(clone: Clone) -> dict[str, str]:
    reach = _load("incremental_golden_reach", clone.root / "tools" / "surface-census" / "golden-reach.py")
    cells = {}
    for path in sorted((clone.root / "docs" / "openapi-surface").glob("*.md")):
        for row in reach.region_rows(path.read_text(encoding="utf-8")):
            if row[3].strip("`") == "golden":
                cells[row[0]] = row[5]
    return cells


def ledger_rows(clone: Clone) -> list[str]:
    return (clone.root / "docs" / "openapi-surface" / "golden-reach.tsv").read_text(encoding="utf-8").split("\n")[1:]


# --- The steps, in order ----------------------------------------------------

STATE: dict[str, Any] = {}


def test_a_missing_base_measures_fully_and_says_why(clone: Clone) -> None:
    STATE["c0"] = clone.head()
    run = clone.repin()
    assert "measured fully: cannot ask GitHub for a nearer base" in run.stderr and "no cached base either" in run.stderr
    store = assert_step(clone, None, set(TESTS) | {FIXTURE}, {})
    assert store["full_at"] == STATE["c0"] and store["steps_since_full"] == 0
    assert clone.cached(STATE["c0"]).is_file(), "the step leaves its store as the next step's cached base"
    first, second = ONLY_FIRST[1], ONLY_SECOND[1]
    assert executed_by(store, f"{ONLY_FIRST[0]}::{first}") == {TESTS[0]}, (
        "re-pin ONLY_FIRST to a function only the first test runs"
    )
    assert executed_by(store, f"{ONLY_SECOND[0]}::{second}") == {TESTS[1]}, "re-pin ONLY_SECOND likewise"
    STATE["s0"] = entries(store)


NO_OP = "    std::hint::black_box(());\n"
BODY_EDIT: dict[str, Edit] = {
    "src/ir.rs": (
        "-> Option<&'a str> {\n    let path = url\n",
        "-> Option<&'a str> {\n" + NO_OP + "    let path = url\n",
    )
}
SECOND_EDIT: dict[str, Edit] = {
    "src/document_refusals/examples.rs": (
        "fn plain_string(schema: &Value) -> bool {\n",
        "fn plain_string(schema: &Value) -> bool {\n" + NO_OP,
    )
}
# A comment above and inside another function the first test runs, and a rustfmt-style reflow inside it.
REFLOW: dict[str, Edit] = {
    "src/ir.rs": [
        ("fn method_after_tag_tokens(", "// A comment above the function.\n\nfn method_after_tag_tokens("),
        (
            "    let tag_words = fern_location_tokens(tag);\n",
            "    // and one inside it\n    let tag_words =\n        fern_location_tokens(\n            tag,\n        );\n",
        ),
    ]
}


def test_a_function_body_edit_re_runs_exactly_the_tests_that_executed_it(clone: Clone) -> None:
    STATE["c1"] = clone.commit("a body edit", BODY_EDIT)
    run = clone.repin()
    assert f"re-ran test {TESTS[0]}: it executed changed {ONLY_FIRST[0]}::{ONLY_FIRST[1]}" in run.stderr
    store = assert_step(clone, STATE["c0"], {TESTS[0]}, STATE["s0"])
    assert store["full_at"] == STATE["c0"] and store["steps_since_full"] == 1
    STATE["s1"] = entries(store)


def test_a_two_step_chain_equals_a_full_measurement_of_the_same_tree(clone: Clone) -> None:
    STATE["c2"] = clone.commit("a reflow and a second body edit", REFLOW | SECOND_EDIT)
    clone.repin()
    store = assert_step(clone, STATE["c1"], {TESTS[1]}, STATE["s1"])
    assert store["steps_since_full"] == 2
    incremental = (region_sets(clone, store), ledger_rows(clone), reach_cells(clone), clone.ledger_line())
    full_env = dict(clone.env, CROZIER_GOLDEN_REACH_BASE_CACHE=str(clone.scratch / "bases-full"))
    clone.run("git", "checkout", "--", "docs")
    clone.repin(env=full_env)
    full = clone.store()
    assert full["steps_since_full"] == 0 and all(e == STATE["c2"] for e in entries(full).values())
    assert region_sets(clone, full) == incremental[0], "the chain's per-test region sets are a full measurement's"
    assert ledger_rows(clone) == incremental[1], "the chain's ledger rows are a full measurement's"
    assert reach_cells(clone) == incremental[2], "the chain's reach cells are a full measurement's"
    assert clone.ledger_line() != incremental[3], "only the provenance line differs"


NON_ATTRIBUTABLE: dict[str, dict[str, Edit]] = {
    "a const in a measured crate's source": {"src/lib.rs": ("", "\n#[allow(dead_code)]\nconst REPIN_PROBE: u8 = 1;\n")},
    "a template the crate embeds": {"templates/version.py.j2": ("", "{# a comment renders nothing #}")},
}


@pytest.mark.parametrize("case", [*NON_ATTRIBUTABLE, "a Cargo.lock dependency"])
def test_a_change_no_function_owns_re_runs_every_test(clone: Clone, case: str) -> None:
    clone.checkout(f"full-{len(STATE)}", STATE["c0"])
    if case == "a Cargo.lock dependency":
        lock = (clone.root / "Cargo.lock").read_text(encoding="utf-8")
        version = re.search(r'name = "itoa"\nversion = "1\.0\.(\d+)"', lock)
        assert version and int(version.group(1)) > 0, "re-pin the dependency the case moves"
        clone.run("cargo", "update", "--quiet", "-p", "itoa", "--precise", f"1.0.{int(version.group(1)) - 1}")
        assert git(clone.root, "status", "--porcelain", "Cargo.lock"), "cargo update changed nothing"
        clone.commit("a dependency", {}, keep=True)
        reason = "Cargo.lock changed beyond crozier's own version"
    else:
        clone.commit(case, NON_ATTRIBUTABLE[case])
        reason = "outside function bodies" if "const" in case else "templates/version.py.j2 changed"
    run = clone.repin()
    assert f"measured fully: {reason}" in run.stderr or reason in run.stderr
    store = clone.store()
    assert all(commit == clone.head() for commit in entries(store).values())
    assert clone.ledger_line().endswith(f"; base none (full): {len(TESTS)} run at {clone.head()[:12]}, 0 carried")


@pytest.mark.parametrize("case", ["a release's own version bump", "CHANGELOG.md alone"])
def test_a_release_bump_or_a_changelog_edit_re_runs_nothing(clone: Clone, case: str) -> None:
    clone.checkout(f"none-{len(STATE)}", STATE["c0"])
    if case == "CHANGELOG.md alone":
        clone.commit(case, {"CHANGELOG.md": ("", "\n<!-- a note -->\n")})
    else:
        version = re.search(r'^version = "0\.0\.(\d+)"', (clone.root / "Cargo.toml").read_text(encoding="utf-8"), re.M)
        assert version
        old, new = f"0.0.{version.group(1)}", f"0.0.{int(version.group(1)) + 1}"
        clone.commit(
            case,
            {
                "Cargo.toml": (f'version = "{old}"', f'version = "{new}"'),
                "Cargo.lock": (f'name = "crozier"\nversion = "{old}"', f'name = "crozier"\nversion = "{new}"'),
                "CHANGELOG.md": ("", f"\n## {new}\n"),
            },
        )
    run = clone.repin()
    assert "re-ran" not in run.stderr
    assert_step(clone, STATE["c0"], set(), STATE["s0"])


@pytest.mark.parametrize(
    ("case", "change", "reason"),
    [
        (
            "a base recorded under another compiler",
            {"rustc": "1.0.0 0000000"},
            "the base was measured with rustc 1.0.0",
        ),
        ("a base older than seven days", {"measured_at": "2020-01-01T00:00:00Z"}, "days ago, more than 7"),
        ("a chain past twenty steps", {"steps_since_full": 20}, "21 since a full measurement, over 20"),
    ],
)
def test_the_drift_bound_measures_fully_and_names_why(clone: Clone, case: str, change: dict, reason: str) -> None:
    clone.checkout(f"bound-{len(STATE)}", STATE["c0"])
    clone.commit(case, {"CHANGELOG.md": ("", f"\n<!-- {case} -->\n")})
    cache = clone.scratch / f"bases-{len(STATE)}"
    STATE[case] = True
    base = RS.load(clone.cached(STATE["c0"]))
    RS.save({**base, **change}, cache / STATE["c0"] / "base.json.gz")
    run = clone.repin(env=dict(clone.env, CROZIER_GOLDEN_REACH_BASE_CACHE=str(cache)))
    assert f"census-repin: measured fully: {reason}" in run.stderr
    assert all(commit == clone.head() for commit in entries(clone.store()).values())


def test_a_fixture_tree_and_a_fixture_document_re_run_exactly_their_test_and_fixture(clone: Clone) -> None:
    clone.checkout("inputs", STATE["c0"])
    api = TESTS[2].removesuffix("_matches_fern_output").replace("_", "-")
    expected = sorted((clone.root / "tests" / "fixtures" / api / "expected").rglob("*.py"))[0]
    clone.commit(
        "a golden's tree and a fixture's document",
        {
            expected.relative_to(clone.root).as_posix(): ("", "# a comment the comparison strips\n"),
            f"docs/openapi-surface/handwritten/{FIXTURE}/openapi.yml": ("", "# a comment no reader takes\n"),
        },
    )
    run = clone.repin()
    assert f"re-ran test {TESTS[2]}: its golden's fixture tree changed" in run.stderr
    assert f"re-ran fixture {FIXTURE}: its fixture changed" in run.stderr
    assert_step(clone, STATE["c0"], {TESTS[2], FIXTURE}, STATE["s0"])


# --- Re-anchoring and merges ------------------------------------------------


def files_quoting(clone: Clone, spec: str) -> set[str]:
    found = subprocess.run(["git", "grep", "-l", "-F", spec], cwd=clone.root, capture_output=True, text=True)
    return set(found.stdout.split())


@pytest.mark.parametrize(
    ("case", "edit"),
    [
        ("rustfmt splitting the anchored line", ("    if untagged {\n", "    if untagged\n    {\n")),
        (
            "a duplicate line making the anchor ambiguous",
            ("    if untagged {\n", "    // if untagged {\n    if untagged {\n"),
        ),
    ],
)
def test_a_moved_anchor_is_re_anchored_everywhere_it_is_quoted(clone: Clone, case: str, edit: tuple[str, str]) -> None:
    clone.checkout(f"anchor-{len(STATE)}", STATE["c0"])
    STATE[case] = True
    quoting = files_quoting(clone, SITE)
    assert {"docs/openapi-surface/golden-reach-sites.tsv", "docs/openapi-surface/golden-reach.tsv"} <= quoting
    clone.commit(case, {"src/ir.rs": edit})
    assert clone.run(sys.executable, "tools/surface-census/golden-reach.py", "sites", check=False).returncode != 0
    run = clone.repin()
    moved = re.search(r"re-anchored `" + re.escape(SITE) + r"` as `([^`]+)`", run.stderr)
    assert moved, run.stderr[-3000:]
    assert files_quoting(clone, SITE) == set(), "no file quotes the old anchor"
    assert files_quoting(clone, moved.group(1)) >= quoting, "every file that quoted it quotes the new one"
    clone.run(sys.executable, "tools/surface-census/golden-reach.py", "sites")
    assert re.search(r"census-repin: .* 1 site\(s\) re-anchored, \d+ file\(s\) rewritten", run.stdout)


def test_an_anchored_arm_whose_code_changed_is_refused_and_nothing_is_rewritten(clone: Clone) -> None:
    clone.checkout("changed-arm", STATE["c0"])
    clone.commit("the arm's code changes", {"src/ir.rs": ("    if untagged {\n", "    if untagged && true {\n")})
    run = clone.repin(check=False)
    assert run.returncode != 0
    assert f"`{SITE}`: the anchored code changed" in run.stderr
    assert (
        "old (" in run.stderr
        and "new (HEAD)" in run.stderr
        and "Decide whether the feature is still handled there" in run.stderr
    )
    assert git(clone.root, "status", "--porcelain", "--untracked-files=no") == "", "a refused repin rewrites nothing"


def _branches_that_conflict(clone: Clone, theirs: dict, ours: dict) -> None:
    clone.checkout("theirs", STATE["c0"])
    clone.commit("theirs", theirs)
    clone.checkout("ours", STATE["c0"])
    clone.commit("ours", ours)
    merge = subprocess.run(["git", "merge", "-q", "theirs"], cwd=clone.root, capture_output=True, text=True)
    assert merge.returncode != 0, "the two branches must conflict"


def _ledger_edit(old_count: str, new_count: str) -> dict:
    return {"docs/openapi-surface/golden-reach.tsv": (old_count, new_count)}


def test_a_merge_whose_conflicts_are_all_derived_is_completed(clone: Clone) -> None:
    ledger = (clone.root / "docs" / "openapi-surface" / "golden-reach.tsv").read_text(encoding="utf-8")
    first_row = ledger.split("\n")[2]
    cells = reach_cells(clone)
    key, cell = next((k, c) for k, c in cells.items() if "rank 1)" in c)
    region = next(
        p for p in (clone.root / "docs" / "openapi-surface").glob("*.md") if cell in p.read_text(encoding="utf-8")
    )
    rel = region.relative_to(clone.root).as_posix()
    _branches_that_conflict(
        clone,
        {"docs/openapi-surface/golden-reach.tsv": (first_row, first_row + "x"), rel: (cell, cell + " theirs")},
        {"docs/openapi-surface/golden-reach.tsv": (first_row, first_row + "y"), rel: (cell, cell + " ours")},
    )
    run = clone.repin()
    assert "resolved 2 derived conflict hunk(s) and committed the merge" in run.stderr
    assert len(git(clone.root, "rev-list", "--parents", "-n", "1", "HEAD").split()) == 3, "HEAD is the merge"
    text = (clone.root / "docs" / "openapi-surface" / "golden-reach.tsv").read_text(encoding="utf-8")
    assert "<<<<<<<" not in text and first_row + "x" not in text and first_row + "y" not in text
    assert key


def test_a_conflict_in_a_hand_written_line_is_refused_by_name(clone: Clone) -> None:
    sites = (clone.root / "docs" / "openapi-surface" / "golden-reach-sites.tsv").read_text(encoding="utf-8")
    row = sites.split("\n")[1]
    _branches_that_conflict(
        clone,
        {"docs/openapi-surface/golden-reach-sites.tsv": (row, row + " theirs")},
        {"docs/openapi-surface/golden-reach-sites.tsv": (row, row + " ours")},
    )
    run = clone.repin(check=False)
    assert run.returncode != 0
    assert "docs/openapi-surface/golden-reach-sites.tsv:2: `" in run.stderr and "is not derived content" in run.stderr
    git(clone.root, "merge", "--abort")


# --- The CI job's base, served back, and every derived output restored ------


class GitHub(BaseHTTPRequestHandler):
    artifacts: ClassVar[dict[str, bytes]] = {}

    def log_message(self, format: str, *args: object) -> None:
        return

    def _send(self, status: int, body: bytes) -> None:
        self.send_response(status)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        path = self.path.split("?", 1)[0]
        if path == "/rate_limit":
            core = {"limit": 5000, "used": 0, "remaining": 5000, "reset": int(time.time()) + 3600}
            self._send(200, json.dumps({"resources": {"core": core}}).encode())
        elif path == f"/repos/{SLUG}/actions/artifacts":
            listed = [{"id": i, "name": f"golden-reach-base-{sha}"} for i, sha in enumerate(sorted(self.artifacts), 1)]
            self._send(200, json.dumps({"artifacts": listed}).encode())
        elif path.endswith("/zip"):
            index = int(path.rsplit("/", 2)[-2])
            self._send(200, self.artifacts[sorted(self.artifacts)[index - 1]])
        else:
            self._send(404, b"{}")


STALE = {
    "a ledger row": ("docs/openapi-surface/golden-reach.tsv", None),
    "a reach cell": (None, None),
    "an arm section": ("docs/openapi-surface-coverage.md", "<!-- END GENERATED ARM TABLE -->"),
    "a handwritten-reach.tsv row": ("docs/openapi-surface/handwritten-reach.tsv", None),
    "a census tally": ("docs/openapi-surface/document-paths.md", "**Snapshot digest:** `"),
    "a scenario-proof-index.tsv row": ("docs/openapi-surface/scenario-proof-index.tsv", None),
    "the region keys": ("docs/openapi-surface/witness-search-keys.tsv", None),
    "the coverage headline": ("docs/openapi-surface-coverage.md", "registered sources, of which **"),
    "a row of outstanding.tsv": ("docs/openapi-surface/witness-search-registries/outstanding.tsv", None),
    "a row of the arm searches' outstanding list": (
        "docs/openapi-surface/golden-reach-witnesses/outstanding.tsv",
        None,
    ),
}


def _stale(clone: Clone) -> dict[str, Edit]:
    """One edit per derived output, each making it disagree with its generator."""
    regions = clone.root / "docs" / "openapi-surface"
    read = lambda path: (clone.root / path).read_text(encoding="utf-8")  # noqa: E731
    edits: dict[str, Edit] = {}
    ledger = read("docs/openapi-surface/golden-reach.tsv").split("\n")
    edits["docs/openapi-surface/golden-reach.tsv"] = (ledger[2], ledger[2].replace("\t", "\t9", 1))
    key, cell = next(iter(reach_cells(clone).items()))
    region = next(p for p in regions.glob("*.md") if cell in p.read_text(encoding="utf-8"))
    edits[region.relative_to(clone.root).as_posix()] = (cell, cell.replace("reach:", "reach: stale", 1))
    coverage = read("docs/openapi-surface-coverage.md")
    table_row = coverage.split("<!-- BEGIN GENERATED ARM TABLE")[1].split("\n")[3]
    headline = re.search(r"registered sources, of which \*\*(\d+)\*\*", coverage)
    assert headline
    edits["docs/openapi-surface-coverage.md"] = [
        (table_row + "\n", table_row.replace("|", "| stale", 1) + "\n"),
        (headline.group(0), headline.group(0).replace(headline.group(1), str(int(headline.group(1)) + 7))),
    ]
    handwritten = read("docs/openapi-surface/handwritten-reach.tsv").split("\n")
    edits["docs/openapi-surface/handwritten-reach.tsv"] = (handwritten[1] + "\n", handwritten[1] + "x\n")
    digest = re.search(r"\*\*Snapshot digest:\*\* `([0-9a-f]{64})`", read("docs/openapi-surface/document-paths.md"))
    assert digest
    edits["docs/openapi-surface/document-paths.md"] = (digest.group(1), "0" * 64)
    scenario = read("docs/openapi-surface/scenario-proof-index.tsv").split("\n")
    row = next(line for line in scenario[1:] if "\tpython_enums" in line)
    edits["docs/openapi-surface/scenario-proof-index.tsv"] = (row, row.replace("\tpython_enums", "\tstale", 1))
    keys = read("docs/openapi-surface/witness-search-keys.tsv").split("\n")
    edits["docs/openapi-surface/witness-search-keys.tsv"] = (keys[1] + "\n", "")
    outstanding = read("docs/openapi-surface/witness-search-registries/outstanding.tsv").split("\n")
    edits["docs/openapi-surface/witness-search-registries/outstanding.tsv"] = (outstanding[1] + "\n", "")
    searches = read("docs/openapi-surface/golden-reach-witnesses/outstanding.tsv").split("\n")
    edits["docs/openapi-surface/golden-reach-witnesses/outstanding.tsv"] = (searches[1] + "\n", "")
    assert key
    return edits


def test_the_ci_jobs_base_is_found_accepted_and_stepped_from_and_every_derived_output_restored(clone: Clone) -> None:
    clone.checkout("published", STATE["c0"])
    server = ThreadingHTTPServer(("127.0.0.1", 0), GitHub)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    api = f"http://127.0.0.1:{server.server_address[1]}"
    try:
        git(clone.root, "remote", "add", "origin", f"https://github.com/{SLUG}.git")
        git(clone.root, "update-ref", "refs/remotes/origin/main", STATE["c0"])
        ci = dict(clone.env, CROZIER_GITHUB_API_URL=api, GITHUB_TOKEN="offline-token")
        ci["CROZIER_GOLDEN_REACH_BASE_CACHE"] = str(clone.scratch / "ci-runner-cache")
        package = clone.scratch / "package"
        # The job's own command, as ci.yml runs it; the upload is the one step substituted.
        job = clone.run("just", "golden-reach-base", str(package), env=ci)
        assert f"packaged {package / 'base.json.gz'} for golden-reach-base-{STATE['c0']}" in job.stdout
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, "w") as archive:
            archive.write(package / "base.json.gz", "base.json.gz")
        GitHub.artifacts = {STATE["c0"]: buffer.getvalue()}
        published = RS.load(package / "base.json.gz")
        assert published["commit"] == STATE["c0"] and len(published["tests"]) > len(TESTS)
        stale = _stale(clone)
        later = clone.commit("every derived output made stale", stale)
        consumer = dict(ci, CROZIER_GOLDEN_REACH_BASE_CACHE=str(clone.scratch / "consumer-cache"))
        run = clone.repin(scoped=False, env=consumer)
        assert f"downloaded golden-reach-base-{STATE['c0']}" in run.stderr
        assert "measured fully" not in run.stderr, "the step carries every entry from the published base"
        store = clone.store()
        assert store["commit"] == later and store["full_at"] == STATE["c0"] and store["steps_since_full"] == 1
        assert all(e["commit"] == STATE["c0"] for e in store["tests"].values())
        assert clone.ledger_line().endswith(
            f"; base {STATE['c0'][:12]}: 0 run at {later[:12]}, {len(store['tests'])} carried"
        )
        for path, edit in stale.items():
            text = (clone.root / path).read_text(encoding="utf-8")
            for old, new in pairs(edit):
                if new:
                    assert new not in text, f"{path} still holds the stale edit {new[:80]!r}"
                else:
                    assert old in text, f"{path} did not get its removed row back"
        changed = set(git(clone.root, "diff", "--name-only").split())
        assert set(stale) <= changed, sorted(set(stale) - changed)
        snapshot = {path: (clone.root / path).read_bytes() for path in changed}
        # Each output is what its own generator writes from this tree: running them again moves nothing.
        python = sys.executable
        tools = "tools/surface-census"
        out = str(clone.root / ".local" / "golden-reach")
        for argv in (
            [python, f"{tools}/golden-reach.py", "report", "--write", "--census", f"{out}/census.json"],
            [python, f"{tools}/golden-reach.py", "arms"],
            [python, f"{tools}/restate-coverage.py", "--snapshot-json", f"{out}/census.json", "--write"],
            [python, f"{tools}/restate-coverage.py", "--write"],
            [python, f"{tools}/scenario-proof-index.py", "write"],
            [python, "tools/witness-search/witness-search-registries-index.py"],
            [python, f"{tools}/golden-reach-search.py", "outstanding"],
        ):
            clone.run(*argv)
        keys = clone.run(python, f"{tools}/witness-search-region-keys.py")
        assert keys.stdout == (clone.root / "docs/openapi-surface/witness-search-keys.tsv").read_text(encoding="utf-8")
        handwritten = _load("incremental_handwritten", clone.root / tools / "handwritten-fixtures.py")
        handwritten.report(clone.root, store)
        for path, content in snapshot.items():
            assert (clone.root / path).read_bytes() == content, f"{path} is not what its generator writes"
        assert sum(len(pairs(edit)) for edit in stale.values()) == len(STALE), "one stale edit per derived output"
    finally:
        server.shutdown()
        server.server_close()
