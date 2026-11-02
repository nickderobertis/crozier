"""Boundary tests for the golden-reach store (`tools/surface-census/reach_store.py`).

The store keeps each golden test's executed counter regions relative to its
enclosing function, and `plan` decides what a change re-runs. These cases drive
the real parser over real Rust source, the real store files on disk, `plan` over
a real scratch git repository (every rule of the carry rule, one commit each),
and the real host lock from a second process. The instrumented journey is
`tools/surface-reach/tests/incremental_test.py`.
"""

from __future__ import annotations

import datetime
import gzip
import importlib.util
import json
import os
import re
import subprocess
import sys
import textwrap
import time
from collections.abc import Mapping
from pathlib import Path
from typing import Any

import pytest

REPO = Path(__file__).resolve().parents[3]
HERE = REPO / "tools" / "surface-census"


def _load(name: str, file: str) -> Any:
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, HERE / file)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


RS = _load("reach_store", "reach_store.py")

LIB = textwrap.dedent(
    """\
    use std::fmt;

    pub const LIMIT: usize = 3;

    pub struct Model {
        name: String,
    }

    pub trait Shape {
        fn area(&self) -> u8 {
            0
        }
    }

    impl Shape for Model {}

    impl Model {
        pub fn new(name: &str) -> Self {
            Model { name: name.to_string() }
        }
    }

    impl fmt::Display for Model {
        fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
            write!(f, "{}", self.name)
        }
    }

    pub fn render(names: &[&str]) -> String {
        let shown: Vec<String> = names.iter().take(LIMIT).map(|n| Model::new(n).to_string()).collect();
        shown.join(",")
    }

    pub fn untouched(x: u8) -> u8 {
        if x > 1 { x * 2 } else { x }
    }

    pub const fn width() -> usize {
        4
    }

    pub fn outer() -> u8 {
        fn inner() -> u8 {
            7
        }
        inner()
    }

    #[cfg(windows)]
    fn separator() -> char {
        '\\\\'
    }

    #[cfg(not(windows))]
    fn separator() -> char {
        '/'
    }

    #[cfg(test)]
    mod tests {
        use super::*;
        const SAMPLE: &str = "a";

        #[test]
        fn renders() {
            assert_eq!(render(&[SAMPLE]), "a");
        }
    }
    """
)


def tree_of(source: str, path: str = "src/lib.rs") -> Any:
    return RS.read_tree(Path("."), {path: source.encode()})


def test_tokens_keep_strings_chars_and_lifetimes_whole_and_drop_comments() -> None:
    source = "let a = \"{ } \\\" //\"; /* x /* y */ z */ let b = r#\"q\"{\"#; f('\\'', '{', &'a str, b'}'); // tail"
    texts = [t.text for t in RS.tokenize(source.encode())]
    assert '"{ } \\" //"' in texts
    assert 'r#"q"{"#' in texts
    assert "'\\''" in texts and "'{'" in texts and "'a" in texts and "b'}'" in texts
    assert not any(t.startswith(("/*", "//")) for t in texts)
    assert texts.count("{") == 0, "a brace inside a literal is never a token of its own"


def test_function_keys_name_methods_trait_impls_nested_fns_and_twins_and_drop_test_code() -> None:
    tree = tree_of(LIB)
    keys = set(tree.functions)
    assert {
        "src/lib.rs::Shape::area",
        "src/lib.rs::Model::new",
        "src/lib.rs::<Model as Display>::fmt",
        "src/lib.rs::render",
        "src/lib.rs::untouched",
        "src/lib.rs::width",
        "src/lib.rs::outer",
        "src/lib.rs::outer::inner",
        "src/lib.rs::separator",
        "src/lib.rs::separator#2",
        "src/lib.rs::{items}",
    } == keys
    assert tree.functions["src/lib.rs::width"].const_fn
    assert tree.functions["src/lib.rs::<Model as Display>::fmt"].trait_ctx


def test_a_file_only_a_cfg_test_module_declares_is_not_measured() -> None:
    tree = RS.read_tree(
        Path("."),
        {"src/lib.rs": b"#[cfg(test)]\nmod checks;\npub fn a() {}\n", "src/checks.rs": b"fn helper() {}\n"},
    )
    assert set(tree.files) == {"src/lib.rs"}
    assert "src/checks.rs::helper" not in tree.functions


def _span_of(source: str, snippet: str) -> tuple[int, int, int, int]:
    """The llvm-cov `[line, col, line, col]` of the first occurrence of `snippet` (end exclusive)."""
    start = source.index(snippet)
    end = start + len(snippet)

    def at(offset: int) -> tuple[int, int]:
        line = source.count("\n", 0, offset) + 1
        return line, offset - (source.rfind("\n", 0, offset) + 1) + 1

    return (*at(start), *at(end))


def _text(source: str, region: tuple[int, int, int, int]) -> str:
    lines = source.split("\n")
    starts = [0]
    for line in lines:
        starts.append(starts[-1] + len(line) + 1)
    return source[starts[region[0] - 1] + region[1] - 1 : starts[region[2] - 1] + region[3] - 1]


def test_a_region_maps_exactly_onto_its_code_through_comments_whitespace_and_reflow() -> None:
    regions = [_span_of(LIB, "{ x * 2 }"), _span_of(LIB, "x > 1"), _span_of(LIB, 'shown.join(",")')]
    before = tree_of(LIB)
    encoded = [before.encode("src/lib.rs", region) for region in regions]
    moved = LIB.replace(
        "pub fn untouched(x: u8) -> u8 {\n    if x > 1 { x * 2 } else { x }\n}",
        "// A comment above the function.\n\n/// And a doc comment.\npub fn untouched(\n    x: u8,\n) -> u8 {\n"
        "    // one inside\n    if x > 1 {\n        x * 2\n    } else {\n        x\n    }\n}",
    ).replace("pub fn render(", "// shifted\n\npub fn render(")
    after = tree_of(moved)
    for key in ("src/lib.rs::untouched", "src/lib.rs::render"):
        assert before.functions[key].digest == after.functions[key].digest, f"{key}'s tokens did not change"
    for region, (key, position) in zip(regions, encoded, strict=True):
        file, decoded = after.decode(key, position)
        assert file == "src/lib.rs"
        assert " ".join(_text(moved, decoded).split()) == " ".join(_text(LIB, region).split())
    # The reflowed arm now spans three lines; its start is exactly the `{` that opens it.
    _file, arm = after.decode(*encoded[0])
    assert _text(moved, arm).startswith("{") and _text(moved, arm).endswith("}") and arm[2] - arm[0] == 2


def test_a_token_change_changes_the_digest_and_a_comment_does_not() -> None:
    base = tree_of(LIB).functions["src/lib.rs::untouched"].digest
    assert tree_of(LIB.replace("x * 2", "x * /* doubled */ 2")).functions["src/lib.rs::untouched"].digest == base
    assert tree_of(LIB.replace("x * 2", "x * 3")).functions["src/lib.rs::untouched"].digest != base


def _store(tree: Any, commit: str, tests: dict[str, list[str]], fixtures: dict[str, list[str]], **top: Any) -> dict:
    functions = tree.table()
    for value in functions.values():
        value["regions"] = [[0, 0, 0, 1]]
    store = {
        "schema": 1,
        "commit": commit,
        "rustc": "1.96.0 abc",
        "llvm": "22.1.2",
        "full_at": commit,
        "steps_since_full": 0,
        "measured_at": RS.now_iso(),
        "tests": {name: {"commit": commit, "regions": {k: [0] for k in keys}} for name, keys in tests.items()},
        "fixtures": {name: {"commit": commit, "regions": {k: [0] for k in keys}} for name, keys in fixtures.items()},
        "functions": functions,
    }
    store.update(top)
    return store


def test_the_store_round_trips_byte_stably_and_refuses_any_other_schema(tmp_path: Path) -> None:
    store = _store(tree_of(LIB), "a" * 40, {"t": ["src/lib.rs::render"]}, {})
    path = tmp_path / "base.json.gz"
    RS.save(store, path)
    first = path.read_bytes()
    RS.save(RS.load(path), path)
    assert path.read_bytes() == first, "one content is one byte stream (mtime-free gzip, sorted keys)"
    assert RS.load(path) == store
    for broken, message in (
        ({**store, "schema": 2}, "schema 2"),
        ({k: v for k, v in store.items() if k != "llvm"}, "not exactly"),
        ({**store, "commit": "main"}, "40-hex"),
        ({**store, "tests": {"t": {"commit": "a" * 40, "regions": {"src/lib.rs::render": [5]}}}}, "entry"),
    ):
        with gzip.open(path, "wt", encoding="utf-8") as handle:
            json.dump(broken, handle)
        with pytest.raises(RS.StoreError, match=message):
            RS.load(path)


# --- The carry rule, over a real git repository ----------------------------

E2E = textwrap.dedent(
    """\
    use std::path::Path;

    struct Corpus {
        api: &'static str,
    }

    const ALPHA: Corpus = Corpus {
        api: "alpha",
    };

    const BETA: Corpus = Corpus {
        api: "beta",
    };

    const CORPORA: &[&Corpus] = &[&ALPHA, &BETA];

    fn fixture_dir(api: &str) -> std::path::PathBuf {
        Path::new("tests/fixtures").join(api)
    }

    fn assert_corpus_matches(c: &Corpus) {
        let compared = fixture_dir(c.api);
        assert!(compared.exists());
    }

    #[test]
    fn alpha_matches_fern_output() {
        assert_corpus_matches(&ALPHA);
    }

    #[test]
    fn beta_matches_fern_output() {
        assert_corpus_matches(&BETA);
    }

    #[test]
    fn every_corpus_is_listed() {
        assert_eq!(CORPORA.len(), 2);
    }

    fn compared() -> usize {
        CORPORA.len()
    }
    """
)

CARGO = '[package]\nname = "crozier"\nversion = "0.0.1"\n\n[dependencies]\nserde = "1"\n'
LOCK = (
    'version = 4\n\n[[package]]\nname = "crozier"\nversion = "0.0.1"\ndependencies = ["serde"]\n\n'
    '[[package]]\nname = "serde"\nversion = "1.0.1"\n'
)


def git(root: Path, *args: str) -> str:
    run = subprocess.run(["git", *args], cwd=root, capture_output=True, text=True, check=True)
    return run.stdout.strip()


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    root = tmp_path / "repo"
    files = {
        "src/lib.rs": LIB,
        "templates/client.py.j2": "class Client: ...\n",
        "Cargo.toml": CARGO,
        "Cargo.lock": LOCK,
        "CHANGELOG.md": "# Changelog\n",
        "crates/crozier-e2e/tests/e2e.rs": E2E,
        "tests/fixtures/alpha/expected/client.py": "class Client: ...\n",
        "tests/fixtures/beta/expected/client.py": "class Client: ...\n",
        "tests/fixtures/corpus-sources/alpha/openapi.yaml": "openapi: 3.0.0\n",
        "docs/openapi-surface/handwritten/fx/openapi.yml": "openapi: 3.0.0\n",
        "docs/openapi-surface/handwritten/fx/fern-expected/x.py": "x = 1\n",
    }
    for path, text in files.items():
        (root / path).parent.mkdir(parents=True, exist_ok=True)
        (root / path).write_text(text, encoding="utf-8")
    git(root.parent, "init", "-q", "-b", "main", str(root))
    git(root, "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "--allow-empty", "-m", "empty")
    git(root, "add", "-A")
    git(root, "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "-m", "base")
    return root


TESTS = {
    "alpha_matches_fern_output": RS.Inputs("alpha_matches_fern_output", "alpha", frozenset({"alpha"})),
    "beta_matches_fern_output": RS.Inputs("beta_matches_fern_output", "beta", frozenset({"beta"})),
}
CONSTANTS = {"ALPHA": "alpha_matches_fern_output", "BETA": "beta_matches_fern_output"}
VERSIONS = ("1.96.0 abc", "22.1.2")


def base_of(root: Path, **top: Any) -> dict:
    return _store(
        RS.read_tree(root),
        git(root, "rev-parse", "HEAD"),
        {
            "alpha_matches_fern_output": ["src/lib.rs::render", "src/lib.rs::Model::new"],
            "beta_matches_fern_output": ["src/lib.rs::untouched"],
        },
        {"fx": ["src/lib.rs::<Model as Display>::fmt"]},
        **top,
    )


def step(root: Path, edits: Mapping[str, str | None], base: dict | None = None, **plan: Any) -> Any:
    base = base or base_of(root)
    for path, text in edits.items():
        if text is None:
            (root / path).unlink()
        else:
            (root / path).parent.mkdir(parents=True, exist_ok=True)
            (root / path).write_text(text, encoding="utf-8")
    git(root, "add", "-A")
    git(root, "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "--allow-empty", "-m", "step")
    return RS.plan(root, base, RS.read_tree(root), TESTS, {"fx"}, CONSTANTS, plan.get("versions", VERSIONS))


def edit(root: Path, path: str, old: str, new: str) -> dict[str, str]:
    text = (root / path).read_text(encoding="utf-8")
    assert old in text, old
    return {path: text.replace(old, new, 1)}


RERUN_CASES = [
    ("a body edit re-runs the tests that executed it", "src/lib.rs", "x * 2", "x * 3", {"beta"}, set()),
    (
        "a comment and a reflow re-run nothing",
        "src/lib.rs",
        "{ x * 2 }",
        "{\n        // doubled\n        x * 2\n    }",
        set(),
        set(),
    ),
    (
        "a body edit a fixture executed re-runs the fixture",
        "src/lib.rs",
        '"{}", self.name',
        '"{} ", self.name',
        set(),
        {"fx"},
    ),
    ("its golden's fixture tree", "tests/fixtures/alpha/expected/client.py", "...", "pass", {"alpha"}, set()),
    ("its source document", "tests/fixtures/corpus-sources/alpha/openapi.yaml", "3.0.0", "3.0.3", {"alpha"}, set()),
    (
        "a hand-written fixture's document",
        "docs/openapi-surface/handwritten/fx/openapi.yml",
        "3.0.0",
        "3.1.0",
        set(),
        {"fx"},
    ),
    (
        "a hand-written fixture's Fern tree is no input of its run",
        "docs/openapi-surface/handwritten/fx/fern-expected/x.py",
        "1",
        "2",
        set(),
        set(),
    ),
    (
        "a golden test's own function",
        "crates/crozier-e2e/tests/e2e.rs",
        "assert_corpus_matches(&ALPHA);",
        "assert_corpus_matches(&ALPHA);\n    let _ = 1;",
        {"alpha"},
        set(),
    ),
    (
        "a golden test's Corpus literal",
        "crates/crozier-e2e/tests/e2e.rs",
        'api: "beta",',
        'api: "beta", ',
        set(),
        set(),
    ),
    (
        "a corpus list no golden test reaches",
        "crates/crozier-e2e/tests/e2e.rs",
        "&[&ALPHA, &BETA]",
        "&[&BETA, &ALPHA]",
        set(),
        set(),
    ),
    (
        "an unrelated test",
        "crates/crozier-e2e/tests/e2e.rs",
        "CORPORA.len(), 2",
        'CORPORA.len(), 2, "two"',
        set(),
        set(),
    ),
    ("CHANGELOG.md alone", "CHANGELOG.md", "# Changelog", "# Changelog\n\n## 0.0.2", set(), set()),
]


@pytest.mark.parametrize(
    ("case", "path", "old", "new", "tests", "fixtures"), RERUN_CASES, ids=[c[0] for c in RERUN_CASES]
)
def test_a_change_re_runs_exactly_the_tests_and_fixtures_it_reaches(
    repo: Path, case: str, path: str, old: str, new: str, tests: set[str], fixtures: set[str]
) -> None:
    plan = step(repo, edit(repo, path, old, new))
    assert plan.full is None, case
    assert {name.split("_", 1)[0] for name in plan.tests} == tests, case
    assert set(plan.fixtures) == fixtures, case


FULL_CASES = [
    (
        "a const outside any function",
        {"src/lib.rs": ("LIMIT: usize = 3", "LIMIT: usize = 4")},
        "outside function bodies",
    ),
    ("a template the crate embeds", {"templates/client.py.j2": ("...", "pass")}, "templates/client.py.j2"),
    (
        "a dependency in Cargo.lock",
        {"Cargo.lock": ('version = "1.0.1"', 'version = "1.0.2"')},
        "Cargo.lock changed beyond",
    ),
    ("a const fn", {"src/lib.rs": ("    4\n", "    5\n")}, "const fn"),
    (
        "an override added to a trait impl",
        {
            "src/lib.rs": (
                "impl Shape for Model {}",
                "impl Shape for Model {\n    fn area(&self) -> u8 {\n        1\n    }\n}",
            )
        },
        "trait",
    ),
    (
        "a helper the golden tests reach",
        {"crates/crozier-e2e/tests/e2e.rs": ("join(api)", 'join(api).join(".")')},
        "the golden tests reach it",
    ),
    ("the toolchain file", {"rust-toolchain.toml": (None, '[toolchain]\nchannel = "1.97.0"\n')}, "rust-toolchain.toml"),
]


@pytest.mark.parametrize(("case", "changes", "reason"), FULL_CASES, ids=[c[0] for c in FULL_CASES])
def test_a_change_no_function_can_own_re_runs_every_test(
    repo: Path, case: str, changes: dict[str, tuple[str | None, str]], reason: str
) -> None:
    edits: dict[str, str | None] = {}
    for path, (old, new) in changes.items():
        edits |= {path: new} if old is None else edit(repo, path, old, new)
    plan = step(repo, edits)
    assert plan.full is not None and reason in plan.full, (case, plan.full)
    assert set(plan.tests) == set(TESTS) and set(plan.fixtures) == {"fx"}


def test_a_release_commit_bumping_only_crozier_s_version_re_runs_nothing(repo: Path) -> None:
    edits = edit(repo, "Cargo.toml", 'version = "0.0.1"', 'version = "0.0.2"')
    edits |= edit(repo, "Cargo.lock", 'name = "crozier"\nversion = "0.0.1"', 'name = "crozier"\nversion = "0.0.2"')
    edits |= edit(repo, "CHANGELOG.md", "# Changelog", "# Changelog\n\n## 0.0.2")
    plan = step(repo, edits)
    assert (plan.full, set(plan.tests), set(plan.fixtures)) == (None, set(), set())


@pytest.mark.parametrize(
    ("top", "versions", "reason"),
    [
        ({"rustc": "1.95.0 old"}, VERSIONS, "measured with rustc 1.95.0"),
        ({"measured_at": "2026-01-01T00:00:00Z"}, VERSIONS, "more than 7"),
        ({"steps_since_full": 20}, VERSIONS, "21 since a full measurement, over 20"),
    ],
    ids=["another compiler", "older than seven days", "past twenty steps"],
)
def test_the_drift_bound_measures_fully_and_says_why(repo: Path, top: dict, versions: tuple, reason: str) -> None:
    plan = step(repo, {}, base_of(repo, **top), versions=versions)
    assert plan.full is not None and reason in plan.full


def test_twenty_steps_is_still_inside_the_bound(repo: Path) -> None:
    assert step(repo, {}, base_of(repo, steps_since_full=19)).full is None


# --- The lock ---------------------------------------------------------------


@pytest.mark.skipif(sys.platform == "win32", reason="the holder takes the lock with fcntl")
def test_the_instrumented_lock_says_it_waits_and_enters_only_once_released(tmp_path: Path) -> None:
    import fcntl

    env = dict(os.environ, XDG_CACHE_HOME=str(tmp_path))
    lock = tmp_path / "crozier" / "instrumented-measurement.lock"
    lock.parent.mkdir(parents=True)
    with lock.open("a+") as held:
        fcntl.flock(held.fileno(), fcntl.LOCK_EX)
        child = subprocess.Popen(
            [
                sys.executable,
                "-c",
                f"import sys; sys.path.insert(0, {str(HERE)!r}); import reach_store as RS\n"
                "with RS.instrumented_lock('probe'):\n"
                "    with RS.instrumented_lock('nested'):\n"
                "        print('inside', flush=True)\n",
            ],
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        assert child.stderr is not None and child.stdout is not None
        waiting = child.stderr.readline()
        assert "probe: waiting for the instrumented-measurement lock" in waiting
        time.sleep(0.5)
        assert child.poll() is None, "it entered while another process held the lock"
        fcntl.flock(held.fileno(), fcntl.LOCK_UN)
    out, err = child.communicate(timeout=30)
    assert child.returncode == 0, err
    assert out == "inside\n", "re-entering in the same process takes the lock it holds, never a second wait"
    assert "probe: took the instrumented-measurement lock" in err


def test_measured_at_parses_the_stamp_the_store_writes() -> None:
    stamp = RS.measured_at({"measured_at": RS.now_iso()})
    assert abs((datetime.datetime.now(datetime.UTC) - stamp).total_seconds()) < 5


def test_the_coverage_index_states_the_contract_this_reader_enforces() -> None:
    """The base contract is stated once, in the coverage index; the reader's constants are held to it."""
    doc = (REPO / "docs" / "openapi-surface-coverage.md").read_text(encoding="utf-8")
    section = doc.split("#### Repinning: the store, the base and `just census-repin`", 1)[1].split("\n#", 1)[0]
    flat = " ".join(section.split())
    keys = flat.split("**keys**", 1)[1].split("**drift bound**", 1)[0]

    assert tuple(re.findall(r"`(\w+)`", keys)) == RS.TOP_LEVEL
    assert f"more than **{RS.MAX_AGE_DAYS}** days old" in flat
    assert f"more than **{RS.MAX_STEPS}** steps past a full measurement" in flat
    base = _load("reach_base", "reach_base.py")
    assert f"`{base.ARTIFACT_PREFIX}<40-hex commit>`, one file `{base.ARTIFACT_FILE}`, kept 90 days" in flat
    assert f"`schema` ({RS.SCHEMA}; any other is refused)" in keys


def test_a_region_ending_at_a_token_boundary_encodes_the_same_whatever_follows_it() -> None:
    """An end right after `tag` is one position, whether `)` follows at once or after a trailing comma."""
    before = "fn caller(tag: &str) -> usize {\n    count(tag)\n}\n"
    after = "fn caller(tag: &str) -> usize {\n    count(\n        tag,\n    )\n}\n"
    old, new = tree_of(before), tree_of(after)
    assert old.functions["src/lib.rs::caller"].digest == new.functions["src/lib.rs::caller"].digest
    start = before.index("tag)")
    region = (*_line_col(before, start), *_line_col(before, start + 3))
    start = after.index("tag,")
    moved = (*_line_col(after, start), *_line_col(after, start + 3))
    assert old.encode("src/lib.rs", region) == new.encode("src/lib.rs", moved)


def _line_col(source: str, offset: int) -> tuple[int, int]:
    return source.count("\n", 0, offset) + 1, offset - (source.rfind("\n", 0, offset) + 1) + 1
