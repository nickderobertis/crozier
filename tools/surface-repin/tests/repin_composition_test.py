"""The measurement and repin CLIs over a tiny, genuinely instrumented Rust workspace.

Two golden tests call different production functions; a configured fixture calls
one, and its control calls the other. The production tooling, cargo-llvm-cov and
LLVM exports are real. This keeps composition proof in CI without instrumenting
crozier's corpus. No measurement, planner or writer is replaced.
"""

from __future__ import annotations

import ast
import gzip
import importlib.util
import json
import os
import shlex
import shutil
import subprocess
import sys
import textwrap
from pathlib import Path
from typing import Any

import pytest

REPO = Path(__file__).resolve().parents[3]
PYTHON = str(Path(sys.executable).absolute())
ALPHA = "alpha_matches_fern_output"
BETA = "beta_matches_fern_output"

LIBRARY = """\
pub fn alpha() -> usize {
    1
}

pub fn beta() -> usize {
    2
}
"""

E2E = """\
struct Corpus { api: &'static str }
const ALPHA: Corpus = Corpus {
    api: "alpha",
};
const BETA: Corpus = Corpus {
    api: "beta",
};
fn assert_committed_corpus_matches(corpus: &Corpus) {
    let actual = match corpus.api {
        "alpha" => crozier::alpha(),
        "beta" => crozier::beta(),
        _ => panic!("unknown synthetic golden"),
    };
    let expected = std::fs::read(format!("../../tests/fixtures/{}/expected/result.txt", corpus.api)).unwrap();
    assert_eq!(format!("{actual}\\n").as_bytes(), expected.as_slice());
}
#[test]
fn every_feature_target_has_its_own_golden_test() {
    assert_ne!(ALPHA.api, BETA.api);
}
#[test]
fn alpha_matches_fern_output() {
    assert_committed_corpus_matches(&ALPHA);
}
#[test]
fn beta_matches_fern_output() {
    assert_committed_corpus_matches(&BETA);
}
"""

DOCUMENT = """\
openapi: 3.0.3
info: {title: Synthetic measurement, version: '1'}
paths: {}
components:
  schemas:
    Value: {type: string}
"""


GENERATED_INDEX = """\
import runpy
import sys
from pathlib import Path

verb = runpy.run_path("tools/surface-census/census-repin.py", run_name="composition_expected_index")
handwritten = verb["_load"]("composition_expected_handwritten", "handwritten-fixtures.py")
sys.stdout.write(verb["reach_document"].generated(Path.cwd(), verb["REACH"], handwritten))
"""


def write(root: Path, name: str, text: str) -> None:
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(text), encoding="utf-8", newline="\n")


def git(root: Path, *args: str) -> str:
    return subprocess.run(["git", *args], cwd=root, capture_output=True, text=True, check=True).stdout.strip()


def commit(root: Path, message: str) -> str:
    git(root, "add", "-A")
    git(root, "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-qm", message)
    return git(root, "rev-parse", "HEAD")


def store(root: Path) -> dict[str, Any]:
    with gzip.open(root / ".local/golden-reach/store.json.gz", "rt", encoding="utf-8") as handle:
        return json.load(handle)


def fixture(root: Path) -> None:
    """The real readers' smallest catalogs, with the coverage document as their template."""
    for name in ("surface-census", "witness-search", "corpus"):
        shutil.copytree(REPO / "tools" / name, root / "tools" / name, ignore=shutil.ignore_patterns("__pycache__"))
    # This synthetic crate has no Rust decisions mirrored by the census's Python
    # ports. Its catalog is empty; real-source port drift belongs to test-ports.
    census_path = root / "tools/surface-census/openapi-surface-census.py"
    source = census_path.read_text(encoding="utf-8")
    table = next(
        node
        for node in ast.parse(source).body
        if isinstance(node, ast.Assign)
        and any(isinstance(target, ast.Name) and target.id == "PORT_PINS" for target in node.targets)
    )
    assert table.end_lineno is not None
    lines = source.splitlines(keepends=True)
    census_path.write_text(
        "".join(lines[: table.lineno - 1]) + "PORT_PINS = ()\n" + "".join(lines[table.end_lineno :]),
        encoding="utf-8",
    )
    for name in ("justfile", "rust-toolchain.toml", "scripts/census-python.sh", "assets/scaffolding/metadata.json"):
        target = root / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(REPO / name, target)
    # Every child writer uses the same locked tooling environment, on Windows too.
    if os.name == "nt":
        subprocess.run(
            ["cmd", "/c", "mklink", "/J", str(root / ".venv"), str(Path(sys.prefix).absolute())],
            check=True,
            capture_output=True,
        )
    else:
        (root / ".venv").symlink_to(Path(sys.prefix).absolute(), target_is_directory=True)
    write(root, ".gitignore", "target/\n.local/\n.venv/\n__pycache__/\n*.profraw\n")
    write(root, ".cargo/config.toml", '[build]\ntarget-dir = "target"\n[net]\noffline = true\n')
    write(
        root,
        "Cargo.toml",
        """\
        [package]
        name = "crozier"
        version = "0.0.1"
        edition = "2021"
        [workspace]
        members = ["crates/crozier-e2e"]
        [profile.dev]
        debug = 0
        """,
    )
    write(
        root,
        "crates/crozier-e2e/Cargo.toml",
        """\
        [package]
        name = "crozier-e2e"
        version = "0.0.0"
        edition = "2021"
        [dev-dependencies]
        crozier = { path = "../.." }
        """,
    )
    write(root, "src/lib.rs", LIBRARY)
    write(
        root,
        "src/main.rs",
        """\
        fn main() {
            let public = std::env::args().any(|arg| arg == "public");
            println!("{}", if public { crozier::alpha() } else { crozier::beta() });
        }
        """,
    )
    write(root, "tests/smoke.rs", "#[test]\nfn binary_is_built() {}\n")
    write(root, "crates/crozier-e2e/tests/e2e.rs", E2E)
    subprocess.run(["cargo", "generate-lockfile", "--offline"], cwd=root, check=True, capture_output=True)
    for number, api in enumerate(("alpha", "beta"), start=1):
        write(root, f"tests/fixtures/{api}/openapi.yml", DOCUMENT)
        write(root, f"tests/fixtures/{api}/expected/result.txt", f"{number}\n")
    write(root, "tests/fixtures/CORPUS.md", "# No acquired sources\n")
    write(root, "tests/fixtures/corpus-aliases.tsv", "# aliases\nlegacy-alpha\talpha\n")
    write(
        root,
        "tests/fixtures/corpus-remote-ref-pins.tsv",
        "# immutable substitutions\nalpha\thttps://example.test/ref\thttps://example.test/pin-1\t" + "0" * 64 + "\n",
    )
    write(root, "tests/fixtures/compared-goldens.json", '{"goldens": {}}\n')
    write(root, "assets/departures.yml", "[]\n")
    for name in (
        "tests/fixtures/departures-ledger.tsv",
        "docs/fern-refusals/classes.tsv",
        "docs/openapi-surface/scenario-proof-index.tsv",
        "docs/openapi-surface/output-insensitive.tsv",
        "docs/openapi-surface/combination-cooccurrence.tsv",
        "docs/openapi-surface/witness-search-apis.guru/records.tsv",
        "docs/openapi-surface/witness-search-jentic/records.tsv",
        "docs/openapi-surface/witness-search-vendor-portals/records.tsv",
        "docs/openapi-surface/witness-search-portal-plan.tsv",
    ):
        write(root, name, (REPO / name).read_text(encoding="utf-8").splitlines()[0] + "\n")
    index = (REPO / "docs/openapi-surface-coverage.md").read_text(encoding="utf-8")
    blind_header = "| `src/` file | printed | by tier | ranked gaps pointing at it | verdict |"
    before, separator, rest = index.partition(blind_header)
    assert separator, "the coverage template must retain its blind-spot table"
    _old_table, boundary, after = rest.partition("**Where the two backlogs agree.")
    assert boundary
    index = (
        before + blind_header + "\n|---|---|---|---|---|\n"
        "| `src/lib.rs` | 0 | all covered | none | synthetic source |\n\n" + boundary + after
    )
    # Keep the generator-owned prose and markers, removing catalog rows this tiny
    # workspace does not declare. Its only region is schemas.
    index = (
        "\n".join(
            line
            for line in index.splitlines()
            if (not line.startswith("| `") or line.startswith(("| `src/", "| `schemas`")))
            and (not (line.startswith("| [`") and "](openapi-surface/" in line) or line.startswith("| [`schemas`]"))
        )
        + "\n"
    )
    write(root, "docs/openapi-surface-coverage.md", index)
    write(
        root,
        "docs/openapi-surface/schemas.md",
        """\
        # schemas

        | key | oas | spec location | category | evidence | crozier sites | why bytes could move | settlement |
        |---|---|---|---|---|---|---|---|
        | `type` | both | Schema Object.type | golden | census `schema.type`: `alpha` (1), `beta` (1) | | client.py | |
        | `combo-type-and-version` | both | Schema Object.type | gap | census `schema.type`: 2 declarations | none | client.py | UNREACHABLE synthetic combination |
        """,
    )
    write(
        root,
        "docs/openapi-surface/golden-reach-sites.tsv",
        "key\tselectors\tsites\tnote\ntype\tschema.type\tsrc/lib.rs::alpha,src/lib.rs::beta[=^pub fn beta]\t\n",
    )
    write(
        root,
        "docs/openapi-surface/document-paths.md",
        "**Snapshot digest:** `"
        + "0" * 64
        + "`, over **2** registered golden sources (2 original fixtures, 0 corpus sources)\n",
    )
    write(root, "docs/openapi-surface/oas31-extensions.md", "# No extension rows\n")
    (root / "docs/openapi-surface/golden-reach-witnesses/searches").mkdir(parents=True)
    (root / "docs/openapi-surface/witness-search-registries").mkdir()
    write(root, "docs/openapi-surface/handwritten/configured/openapi.yml", DOCUMENT)
    metadata = json.loads((REPO / "assets/scaffolding/metadata.json").read_text(encoding="utf-8"))
    write(
        root,
        "docs/openapi-surface/handwritten/configured/evidence.toml",
        f"""\
        fern_cli_version = "{metadata["cliVersion"]}"
        fern_python_sdk_version = "{metadata["generatorVersion"]}"
        digest = "{"0" * 64}"
        audiences = ["public"]
        [[covers]]
        key = "type"
        arm = "src/lib.rs::alpha"
        search = "docs/openapi-surface/golden-reach-witnesses/searches/type.md#configuration-gate"
        verdict = "config-gated"
        """,
    )
    git(root, "init", "-qb", "main")
    git(root, "config", "user.name", "t")
    git(root, "config", "user.email", "t@t")
    git(root, "config", "core.autocrlf", "false")
    git(root, "config", "merge.conflictStyle", "merge")
    git(root, "config", "rerere.enabled", "false")
    commit(root, "synthetic measurement workspace")


def test_composition_tree_passes_port_checks_before_refusing_a_broken_selector(tmp_path: Path) -> None:
    fixture(tmp_path)
    (tmp_path / "scripts/census-python.sh").write_text("exit 7\n", encoding="utf-8")
    result = subprocess.run(
        ["just", "census-repin", "--jobs", "1"],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert result.returncode != 0
    assert "interpreter selector scripts/census-python.sh" in result.stderr
    assert "just bootstrap" in result.stderr
    assert "Traceback" not in result.stderr


def test_real_measurement_carries_persists_merges_and_repins_with_recovery(tmp_path: Path) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    fixture(root)
    spec = importlib.util.spec_from_file_location("composition_host_lock", REPO / "tools/surface-census/reach_store.py")
    assert spec and spec.loader
    host = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = host
    spec.loader.exec_module(host)
    # Reserve one contiguous host-wide turn. Child CLIs still take their own
    # locks in a private cache, so they cannot deadlock on this outer hold.
    with host.instrumented_lock("synthetic repin composition"):
        exercise(root, tmp_path)


def exercise(root: Path, tmp_path: Path) -> None:
    env = {
        key: value
        for key, value in os.environ.items()
        if key not in ("GITHUB_TOKEN", "GH_TOKEN", "GITHUB_REPOSITORY", "CROZIER_GITHUB_API_URL", "CARGO_TARGET_DIR")
    }
    env |= {
        "CARGO_BUILD_JOBS": "1",
        "CROZIER_GOLDEN_REACH_BASE_CACHE": str(tmp_path / "bases"),
        "XDG_CACHE_HOME": str(tmp_path / "cache"),
        "PYTHONUTF8": "1",
    }

    def run(*args: str, success: bool = True) -> subprocess.CompletedProcess[str]:
        result = subprocess.run(args, cwd=root, env=env, capture_output=True, text=True, timeout=180)
        if success:
            assert result.returncode == 0, result.stdout + result.stderr
        else:
            assert result.returncode != 0, "this induced failure must be refused"
        return result

    def measure(*args: str) -> dict[str, Any]:
        run(PYTHON, "tools/surface-census/golden-reach.py", "measure", "--jobs", "1", *args)
        return store(root)

    selector = root / "scripts/census-python.sh"
    selected = selector.read_bytes()
    for bad_script in (
        "exit 7\n",
        "exit 0\n",
        "printf '%s\\n' " + shlex.quote(str(root / "missing-python")) + "\n",
    ):
        before = store(root) if (root / ".local/golden-reach/store.json.gz").exists() else None
        selector.write_text(bad_script, encoding="utf-8")
        refused = run("just", "census-repin", "--jobs", "1", success=False)
        assert "interpreter selector scripts/census-python.sh" in refused.stderr and "just bootstrap" in refused.stderr
        assert "Traceback" not in refused.stderr
        if before is None:
            assert not (root / ".local/golden-reach/store.json.gz").exists()
        else:
            assert store(root) == before, "interpreter selection is validated before measuring"
        selector.write_bytes(selected)
        run("just", "census-repin", "--jobs", "1")
    commit(root, "record interpreter recovery tables")
    c0 = git(root, "rev-parse", "HEAD")
    base = measure()
    out = root / ".local/golden-reach"
    for flag in ("--tests", "--fixtures"):
        before = {path: path.read_bytes() for path in out.rglob("*") if path.is_file()}
        if flag == "--tests":
            refused = run(
                PYTHON, "tools/surface-census/golden-reach.py", "measure", "--tests", "^absent$", success=False
            )
            assert "no golden test is selected" in refused.stderr
        else:
            refused = run("just", "census-repin", flag, "^absent$", success=False)
            assert "matches no measured hand-written fixture" in refused.stderr
        assert {path: path.read_bytes() for path in out.rglob("*") if path.is_file()} == before
        if flag == "--tests":
            measure("--tests", f"^{ALPHA}$")
        else:
            run("just", "census-repin", flag, "^configured$")
    base = store(root)
    assert set(base["tests"]) == {ALPHA, BETA}
    assert base["fixtures"]["configured"]["control"], "the fixture's unset-audience control executed code"
    original_beta = json.loads((root / f".local/golden-reach/tests/{BETA}.json").read_text(encoding="utf-8"))
    write(
        root,
        "src/lib.rs",
        LIBRARY.replace("    1\n", "    std::hint::black_box(());\n    1\n").replace(
            "pub fn beta()", "// moved beta\npub  fn beta()"
        ),
    )
    refused = run("just", "census-repin", "--jobs", "1", success=False)
    assert "measured input(s) differ from HEAD" in refused.stderr
    assert store(root) == base, "a dirty-input refusal cannot overwrite the last measurement"
    c1 = commit(root, "change alpha and move beta")
    verbose = run("just", "census-repin", "--jobs", "1", "--verbose")
    assert "census-repin: base:" in verbose.stderr
    assert "census-repin: re-anchored `src/lib.rs::beta[=^pub fn beta]`" in verbose.stderr
    assert f"census-repin: re-ran test {ALPHA}:" in verbose.stderr
    assert f"census-repin: re-ran test {BETA}:" not in verbose.stderr
    assert "1 test(s) run, 1 carried" in verbose.stdout
    assert "re-anchored `" not in verbose.stdout and "re-ran test" not in verbose.stdout
    stepped = store(root)
    assert stepped["tests"][ALPHA]["commit"] == c1
    assert stepped["tests"][BETA]["commit"] == c0, "an unchanged test must retain its execution provenance"
    assert stepped["fixtures"]["configured"]["commit"] == c1
    beta_positions = json.loads((root / f".local/golden-reach/tests/{BETA}.json").read_text(encoding="utf-8"))
    beta_header = LIBRARY.splitlines().index("pub fn beta() -> usize {") + 1
    assert beta_positions == {
        file: [
            [start + 2, col, end + 2, end_col + int(file == "src/lib.rs" and end == beta_header)]
            for start, col, end, end_col in regions
        ]
        for file, regions in original_beta.items()
    }, "carried regions follow the statement, comment and extra space in beta's header"
    commit(root, "record the first repinned tables")
    merged = measure("--tests", f"^{ALPHA}$")
    assert merged["tests"][BETA] == stepped["tests"][BETA]
    assert merged["fixtures"] == stepped["fixtures"]
    write(
        root,
        "src/lib.rs",
        (root / "src/lib.rs").read_text(encoding="utf-8").replace("    2\n", "    std::hint::black_box(());\n    2\n"),
    )
    c2 = commit(root, "change beta")
    scoped = measure("--tests", f"^{ALPHA}$", "--golden-only")
    assert set(scoped["tests"]) == {ALPHA}, "an invalidated excluded test cannot be carried"
    assert scoped["tests"][ALPHA]["commit"] == c2 and not scoped["fixtures"]
    assert not (root / f".local/golden-reach/tests/{BETA}.json").exists()
    measure("--incremental")
    scenario = root / "docs/openapi-surface/scenario-proof-index.tsv"
    good = scenario.read_text(encoding="utf-8")
    scenario.write_text("invalid header\n", encoding="utf-8")
    refused = run("just", "census-repin", "--jobs", "1", success=False)
    assert "regenerating scenario-proof-index.tsv failed" in refused.stderr
    scenario.write_text(good, encoding="utf-8")
    complete = run("just", "census-repin", "--jobs", "1")
    assert "0 test(s) run, 2 carried" in complete.stdout
    ledger = (root / "docs/openapi-surface/golden-reach.tsv").read_text(encoding="utf-8")
    assert f"measured at commit {c2[:12]}" in ledger.splitlines()[0]
    assert "src/lib.rs::alpha=" in ledger and "src/lib.rs::beta[" in ledger
    schemas = (root / "docs/openapi-surface/schemas.md").read_text(encoding="utf-8")
    assert "reach: **2** of **2** handling sites reached" in schemas
    assert "[ledger](golden-reach.tsv)" in schemas
    index = root / "docs/openapi-surface-coverage.md"
    protected = index.read_bytes()
    run("just", "census-repin", "--jobs", "1", "--tests", f"^{ALPHA}$", "--fixtures", "^configured$")
    scoped_index = index.read_bytes()
    scoped_text = index.read_text(encoding="utf-8")
    # Generate from the old template and new ledger: only ledger-derived sections
    # may change; the population-wide arm sections and headline stay protected.
    index.write_bytes(protected)
    try:
        expected_index = run(PYTHON, "-c", GENERATED_INDEX).stdout
    finally:
        index.write_bytes(scoped_index)
    assert scoped_text == expected_index, "a scoped repin must restate its ledger sections and preserve the rest"
    run("just", "census-repin", "--jobs", "1")
    commit(root, "record regenerated synthetic tables")
    ledger_path = root / "docs/openapi-surface/golden-reach.tsv"
    ledger = ledger_path.read_text(encoding="utf-8")
    row = ledger.splitlines()[2]
    git(root, "checkout", "-qb", "side")
    ledger_path.write_text(ledger.replace(row, row + "side-note"), encoding="utf-8")
    side = commit(root, "change a derived note on side")
    git(root, "checkout", "-q", "main")
    ledger_path.write_text(ledger.replace(row, row + "main-note"), encoding="utf-8")
    main = commit(root, "change the same derived note on main")
    run("git", "merge", "side", success=False)
    resolved = run("just", "census-repin", "--jobs", "1")
    assert "conflict hunk" in resolved.stdout
    parents = git(root, "rev-list", "--parents", "-1", "HEAD").split()
    assert set(parents[1:]) == {main, side}
    assert not (root / git(root, "rev-parse", "--git-path", "MERGE_HEAD")).exists()
    assert "-note" not in ledger_path.read_text(encoding="utf-8")
    assert store(root)["commit"] == parents[0]
    assert all(entry["commit"] == c2 for entry in store(root)["tests"].values())
    outputs = {path: path.read_bytes() for path in (root / "docs").rglob("*") if path.is_file()}
    run("just", "census-repin", "--jobs", "1")
    # The provenance line changes the step metadata; every derived row is stable.
    for path, before in outputs.items():
        after = path.read_bytes()
        if path == ledger_path:
            before, after = b"\n".join(before.splitlines()[1:]), b"\n".join(after.splitlines()[1:])
        assert after == before, f"a second complete repin moved {path.relative_to(root)}"

    # A valid old counter universe can contain a region the rebuilt binary no
    # longer emits. Consume that saved artifact through the real CLI: an
    # included witness must execute again; an excluded witness must disappear.
    for excluded in (False, True):
        saved = store(root)
        key = "src/lib.rs::beta"
        regions = saved["functions"][key]["regions"]
        extra = [0, 0, 0, 1]
        assert extra not in regions
        regions.append(extra)
        saved["tests"][BETA]["regions"][key].append(len(regions) - 1)
        previous = saved["tests"][BETA]["commit"]
        for destination in (
            root / ".local/golden-reach/store.json.gz",
            tmp_path / "bases" / saved["commit"] / "base.json.gz",
        ):
            destination.parent.mkdir(parents=True, exist_ok=True)
            with gzip.open(destination, "wt", encoding="utf-8") as handle:
                json.dump(saved, handle)
        library = root / "src/lib.rs"
        library.write_text(
            library.read_text(encoding="utf-8").replace(
                "pub fn alpha() -> usize {", "pub fn alpha() -> usize {\n    std::hint::black_box(());"
            ),
            encoding="utf-8",
        )
        changed = commit(root, "rebuild the counter universe")
        if excluded:
            recovered = measure("--tests", f"^{ALPHA}$")
            assert BETA not in recovered["tests"], "an excluded entry with a vanished counter cannot survive"
            assert not (root / f".local/golden-reach/tests/{BETA}.json").exists()
        else:
            recovered = measure("--incremental")
            assert recovered["tests"][BETA]["commit"] == changed != previous
            assert extra not in recovered["functions"][key]["regions"]

    measure("--incremental")
    for excluded in (False, True):
        saved = store(root)
        key = "src/lib.rs::beta"
        regions = saved["functions"][key]["regions"]
        extra = [0, 0, 0, 1]
        assert extra not in regions
        regions.append(extra)
        saved["fixtures"]["configured"]["control"][key].append(len(regions) - 1)
        previous = saved["fixtures"]["configured"]["commit"]
        for destination in (
            root / ".local/golden-reach/store.json.gz",
            tmp_path / "bases" / saved["commit"] / "base.json.gz",
        ):
            with gzip.open(destination, "wt", encoding="utf-8") as handle:
                json.dump(saved, handle)
        library = root / "src/lib.rs"
        with library.open("a", encoding="utf-8") as handle:
            handle.write(f"\npub fn unused_probe_{int(excluded)}() -> usize {{ 9 }}\n")
        changed = commit(root, "rebuild without changing any executed function")
        if excluded:
            recovered = measure("--tests", f"^{ALPHA}$")
            assert not recovered["fixtures"], "an excluded fixture with a vanished control counter cannot survive"
        else:
            recovered = measure("--incremental")
            assert recovered["fixtures"]["configured"]["commit"] == changed != previous
            assert recovered["tests"] == saved["tests"], "only the fixture with the vanished control counter executes"

    saved = store(root)
    saved["functions"]["src/lib.rs::beta"]["regions"][0] = [0, 10, 1, 0]
    for destination in (
        root / ".local/golden-reach/store.json.gz",
        tmp_path / "bases" / saved["commit"] / "base.json.gz",
    ):
        with gzip.open(destination, "wt", encoding="utf-8") as handle:
            json.dump(saved, handle)
    refused_base = run(PYTHON, "tools/surface-census/golden-reach.py", "measure", "--incremental", "--jobs", "1")
    assert "unusable counter regions" in refused_base.stdout and "starts after its end" in refused_base.stdout
    repaired = store(root)
    assert repaired["steps_since_full"] == 0
    assert all(entry["commit"] == repaired["commit"] for entry in repaired["tests"].values())
    assert repaired["fixtures"]["configured"]["control"]

    changes = (
        ("tests/fixtures/corpus-aliases.tsv", "legacy-alpha", "former-alpha", True),
        ("tests/fixtures/corpus-remote-ref-pins.tsv", "/pin-1", "/pin-2", True),
        (
            "docs/openapi-surface/handwritten/configured/evidence.toml",
            'audiences = ["public"]',
            'audiences = ["public", "also-public"]',
            False,
        ),
    )
    for path, old, new, golden_changed in changes:
        before = store(root)
        document = root / path
        contents = document.read_text(encoding="utf-8")
        assert old in contents
        document.write_text(contents.replace(old, new), encoding="utf-8")
        changed = commit(root, f"change existing {Path(path).name} input")
        measured = run("just", "census-repin", "--jobs", "1", "--verbose")
        after = store(root)
        assert after["tests"][BETA] == before["tests"][BETA]
        if golden_changed:
            assert after["tests"][ALPHA]["commit"] == changed
            assert after["fixtures"] == before["fixtures"]
            assert "1 test(s) run, 1 carried, 0 fixture(s) run, 1 carried" in measured.stdout
            assert f"{Path(path).name} row changed" in measured.stderr
        else:
            assert after["tests"] == before["tests"]
            assert after["fixtures"]["configured"]["commit"] == changed
            for part in ("regions", "control"):
                assert after["fixtures"]["configured"][part] == before["fixtures"]["configured"][part]
            assert "0 test(s) run, 2 carried, 1 fixture(s) run, 0 carried" in measured.stdout
            assert f"its fixture changed ({path})" in measured.stderr


def test_measure_refuses_incomplete_compiler_identity_before_building(tmp_path: Path) -> None:
    """A real executable supplies malformed rustc output at the process boundary."""
    root = tmp_path / "repo"
    root.mkdir()
    fixture(root)
    version = subprocess.run(["rustc", "-vV"], capture_output=True, text=True, check=True).stdout
    shim = tmp_path / "compiler.rs"
    shim.write_text(
        "fn main() {\n"
        " let exe = std::env::current_exe().unwrap();\n"
        ' if exe.file_stem().unwrap() == "rustc" {\n'
        '  print!("{}", std::env::var("PROBE_RUSTC_VERSION").unwrap());\n'
        " } else {\n"
        '  std::fs::write(std::env::var("PROBE_BUILD_MARKER").unwrap(), "built").unwrap();\n'
        "  std::process::exit(17);\n"
        " }\n}\n",
        encoding="utf-8",
    )
    binaries = tmp_path / "bin"
    binaries.mkdir()
    suffix = ".exe" if os.name == "nt" else ""
    compiler = binaries / f"rustc{suffix}"
    subprocess.run(["rustc", str(shim), "-o", str(compiler)], check=True, capture_output=True)
    shutil.copy2(compiler, binaries / f"cargo{suffix}")
    marker = tmp_path / "build-started"
    for field in ("release", "commit-hash", "LLVM version", "host"):
        env = os.environ | {
            "PATH": str(binaries) + os.pathsep + os.environ["PATH"],
            "XDG_CACHE_HOME": str(tmp_path / "cache"),
            "PROBE_RUSTC_VERSION": "\n".join(line for line in version.splitlines() if not line.startswith(field + ":")),
            "PROBE_BUILD_MARKER": str(marker),
        }
        result = subprocess.run(
            [PYTHON, "tools/surface-census/golden-reach.py", "measure", "--jobs", "1"],
            cwd=root,
            env=env,
            capture_output=True,
            text=True,
            timeout=30,
        )
        assert result.returncode != 0
        assert f"omitted a usable {field}" in result.stderr
        assert "install the pinned toolchain" in result.stderr
        assert not marker.exists(), "an unidentified compiler cannot start an instrumented build"
        assert not (root / ".local/golden-reach/store.json.gz").exists()

    identities: list[tuple[str, str]] = []
    hosts = ("x86_64-unknown-linux-gnu", "aarch64-apple-darwin")
    probe = "import json,sys\nfrom pathlib import Path\nsys.path.insert(0, sys.argv[1])\nimport reach_store\nprint(json.dumps(reach_store.toolchain(Path(sys.argv[2]))))"
    for host in hosts:
        env["PROBE_RUSTC_VERSION"] = "\n".join(
            f"host: {host}" if line.startswith("host:") else line for line in version.splitlines()
        )
        result = subprocess.run(
            [PYTHON, "-c", probe, str(root / "tools/surface-census"), str(root)],
            cwd=root,
            env=env,
            capture_output=True,
            text=True,
            timeout=30,
        )
        assert result.returncode == 0, result.stderr
        rustc_identity, llvm_identity = json.loads(result.stdout)
        assert isinstance(rustc_identity, str) and isinstance(llvm_identity, str)
        identities.append((rustc_identity, llvm_identity))
        assert rustc_identity.endswith(host)
    assert identities[0] != identities[1], "equal Rust releases built for different hosts cannot share counters"
    assert identities[0][0].rsplit(" ", 1)[0] == identities[1][0].rsplit(" ", 1)[0]
    assert identities[0][1] == identities[1][1]


@pytest.mark.parametrize(
    "failure", ["exit", "empty", "missing_bash", "missing_interpreter", "nonexecutable", "nonpython"]
)
def test_interpreter_selection_refuses_failure_and_recovers(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, failure: str
) -> None:
    root = tmp_path / "repo"
    write(root, "scripts/census-python.sh", "exit 7\n" if failure == "exit" else "exit 0\n")
    if failure in ("missing_interpreter", "nonexecutable", "nonpython"):
        selected = root / "selected-python"
        if failure == "nonexecutable":
            selected.mkdir()  # A directory is not executable on either Windows or POSIX.
        elif failure == "nonpython":
            compiler = shutil.which("rustc")
            assert compiler is not None
            selected = Path(compiler)  # A real native program that cannot pass the Python probe.
        write(root, "scripts/census-python.sh", "printf '%s\\n' " + shlex.quote(str(selected)) + "\n")
    spec = importlib.util.spec_from_file_location(
        "repin_interpreter_boundary", REPO / "tools/surface-census/census-repin.py"
    )
    assert spec and spec.loader
    verb = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = verb
    spec.loader.exec_module(verb)
    with monkeypatch.context() as environment:
        if failure == "missing_bash":
            environment.setenv("PATH", "")
        with pytest.raises(SystemExit) as refused:
            verb.census_python(root)
    assert "interpreter selector" in str(refused.value) and "just bootstrap" in str(refused.value)
    write(root, "scripts/census-python.sh", "printf '%s\\n' " + shlex.quote(PYTHON) + "\n")
    assert verb.census_python(root) == PYTHON


def test_selector_command_is_resolved_to_a_native_absolute_interpreter(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root = tmp_path / "repo"
    write(root, "scripts/census-python.sh", "printf '%s\\n' python\n")
    monkeypatch.setenv("PATH", str(Path(PYTHON).parent) + os.pathsep + os.environ["PATH"])
    spec = importlib.util.spec_from_file_location(
        "repin_native_interpreter_boundary", REPO / "tools/surface-census/census-repin.py"
    )
    assert spec and spec.loader
    verb = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = verb
    spec.loader.exec_module(verb)
    selected = Path(verb.census_python(root))
    assert selected.is_absolute(), "child writers need a native absolute path, not a Bash command or /c/ path"
    assert selected.samefile(PYTHON)
