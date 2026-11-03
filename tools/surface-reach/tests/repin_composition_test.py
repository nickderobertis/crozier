"""The measurement and repin CLIs over a tiny, genuinely instrumented Rust workspace.

Two golden tests call different production functions; a configured fixture calls
one, and its control calls the other. The production tooling, cargo-llvm-cov and
LLVM exports are real. This keeps composition proof in CI without instrumenting
crozier's corpus. No measurement, planner or writer is replaced.
"""

from __future__ import annotations

import gzip
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import textwrap
from pathlib import Path
from typing import Any

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


def write(root: Path, name: str, text: str) -> None:
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(text), encoding="utf-8")


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
        "key\tselectors\tsites\tnote\ntype\tschema.type\tsrc/lib.rs::alpha,src/lib.rs::beta\t\n",
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
    commit(root, "synthetic measurement workspace")


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

    c0 = git(root, "rev-parse", "HEAD")
    base = measure()
    assert set(base["tests"]) == {ALPHA, BETA}
    assert base["fixtures"]["configured"]["control"], "the fixture's unset-audience control executed code"
    original_beta = json.loads((root / f".local/golden-reach/tests/{BETA}.json").read_text(encoding="utf-8"))
    write(
        root,
        "src/lib.rs",
        LIBRARY.replace("    1\n", "    std::hint::black_box(());\n    1\n").replace(
            "pub fn beta()", "// moved beta\npub fn beta()"
        ),
    )
    c1 = commit(root, "change alpha and move beta")
    stepped = measure("--incremental")
    assert stepped["tests"][ALPHA]["commit"] == c1
    assert stepped["tests"][BETA]["commit"] == c0, "an unchanged test must retain its execution provenance"
    assert stepped["fixtures"]["configured"]["commit"] == c1
    beta_positions = json.loads((root / f".local/golden-reach/tests/{BETA}.json").read_text(encoding="utf-8"))
    assert beta_positions == {
        file: [[start + 2, col, end + 2, end_col] for start, col, end, end_col in regions]
        for file, regions in original_beta.items()
    }, "every carried region must move past the added statement and comment"
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
    assert "src/lib.rs::alpha=" in ledger and "src/lib.rs::beta=" in ledger
    schemas = (root / "docs/openapi-surface/schemas.md").read_text(encoding="utf-8")
    assert "reach: **2** of **2** handling sites reached" in schemas
    assert "[ledger](golden-reach.tsv)" in schemas
    index = root / "docs/openapi-surface-coverage.md"
    protected = index.read_bytes()
    run("just", "census-repin", "--jobs", "1", "--tests", f"^{ALPHA}$", "--fixtures", "^configured$")
    assert index.read_bytes() == protected, "a scoped repin cannot restate the arm sections or headline"
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
