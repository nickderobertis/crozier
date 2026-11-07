//! Journeys of the repository's tooling surfaces. Each drives the real script over real
//! files, with the `crozier` that `crozier:build` leaves in this profile's target directory
//! where it needs one; none reads a golden, so a change to one of these surfaces never pays
//! for the golden suite in crozier-e2e.

#[path = "../../../src/yaml.rs"]
mod yaml;

use std::path::{Path, PathBuf};

/// The "Migrating from Fern" guide's workflow, run from its own code blocks.
#[cfg(unix)]
#[path = "tool_journeys/migration.rs"]
mod migration;

/// The GitHub Action's scripts (`tools/github-action/`) over a real `crozier`.
#[cfg(unix)]
#[path = "tool_journeys/action.rs"]
mod action;

/// `scripts/update-major-tag.sh`, the release's floating major tag.
#[cfg(unix)]
#[path = "tool_journeys/major_tag.rs"]
mod major_tag;

/// The repository root, whatever directory the test runs from.
fn repo_root() -> &'static Path {
    Path::new(env!("CARGO_MANIFEST_DIR"))
        .ancestors()
        .nth(2)
        .expect("crates/crozier-tool-journeys sits two levels below the repository root")
}

/// The binary `crozier:build` leaves beside this suite's `deps/`. Cargo sets
/// `CARGO_BIN_EXE_crozier` only for the package that owns it, so a value there is a
/// caller's override, held to the same check: it must name a file.
#[cfg_attr(not(unix), allow(dead_code))]
fn crozier_bin() -> PathBuf {
    if let Some(explicit) = std::env::var_os("CARGO_BIN_EXE_crozier") {
        let binary = PathBuf::from(explicit);
        assert!(
            binary.is_file(),
            "CARGO_BIN_EXE_crozier names no file ({}): unset it to drive the binary \
             `crozier:build` leaves beside this suite, or point it at a built crozier",
            binary.display()
        );
        return binary;
    }
    let exe = std::env::current_exe().expect("the test executable has a path");
    let mut profile = exe
        .parent()
        .expect("the test executable sits in a directory");
    if profile.ends_with("deps") {
        profile = profile.parent().expect("deps/ sits in a profile directory");
    }
    let binary = profile.join(format!("crozier{}", std::env::consts::EXE_SUFFIX));
    assert!(
        binary.is_file(),
        "no crozier binary at {}: build it first: `nx run crozier-tool-journeys:test` runs \
         `crozier:build` (cargo build -p crozier) before this suite",
        binary.display()
    );
    binary
}

/// The gate's name keeps it out of the golden-only tier, which selects every
/// `*matches_fern_output*` test in `tools/surface-census/fixtures-coverage.sh` and in
/// `tools/surface-census/openapi-surface-census.py`, whose selector `tools/surface-census/golden-reach.py`
/// imports: a hand-written fixture never counts as a corpus golden.
#[test]
fn the_handwritten_gate_is_outside_the_golden_only_tier() {
    let root = repo_root();
    for (script, selector) in [
        (
            "tools/surface-census/fixtures-coverage.sh",
            "test(/matches_fern_output/)",
        ),
        (
            "tools/surface-census/openapi-surface-census.py",
            "GOLDEN_TEST = re.compile(r\"matches_fern_output\")",
        ),
        (
            "tools/surface-census/golden-reach.py",
            "_census_module().GOLDEN_TEST",
        ),
    ] {
        let text = std::fs::read_to_string(root.join(script)).expect("tier selector script");
        assert!(
            text.contains(selector),
            "{script} no longer selects the golden-only tier by {selector}; re-read this check"
        );
    }
    let source = std::fs::read_to_string(root.join("crates/crozier-e2e/tests/e2e.rs"))
        .expect("this suite's source");
    let declared: Vec<&str> = source
        .lines()
        .filter_map(|line| line.strip_prefix("fn "))
        .filter_map(|rest| rest.split('(').next())
        .collect();
    assert!(
        declared.contains(&"handwritten_fixtures_match_fern_goldens"),
        "the hand-written gate is no longer declared under the name the contract gives it"
    );
    for name in declared.iter().filter(|name| name.contains("handwritten")) {
        assert!(
            !name.contains("matches_fern_output"),
            "{name} would join the golden-only tier, which never reads a hand-written fixture"
        );
    }
}
