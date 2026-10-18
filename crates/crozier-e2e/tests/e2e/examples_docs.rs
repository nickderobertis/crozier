//! The examples-and-docs shapes driven through the real binary beyond the
//! hand-written gate: the measurement cases under [`EXAMPLES_DOCS_DIR`], and,
//! for each `fern-defect` correction this work catalogues, the proof that an
//! unexplained byte beside the corrected one still fails the comparison.
//!
//! Every hand-written fixture of these shapes is held whole, in both enum
//! modes, by `handwritten_fixtures_match_fern_goldens` and
//! `literals_mode_measurements_match_fern`; this module adds only what those
//! gates do not already say.

use std::path::Path;

use super::literals_mode;
use super::{
    copy_dir, departure_ledger, golden_path, golden_tree_failures, probe_command, repo_root,
    HANDWRITTEN_DIR,
};

/// Where the measurement cases live; see its README.
pub(super) const EXAMPLES_DOCS_DIR: &str = "docs/fern-measurements/examples-docs";

/// Every measurement case: its directory, the document crozier generates from,
/// and the flags matching the setting Fern ran under.
// llmlint: ignore-block[expensive_tests_stay_behind_their_own_edge] Every Fern golden comparison — the corpus `*_matches_fern_output` tests, the hand-written, probe and measurement gates — runs in this one binary suite by the project's design (crates/crozier-e2e/AGENTS.md), which drives the binary crozier:build leaves; giving golden comparisons their own Nx edge is a graph change for that whole family, not for these cases.
const CASES: &[(&str, &str, &[&str])] = &[
    (
        "archive-glob-rules",
        "docs/fern-measurements/examples-docs/archive-glob-rules/openapi.yml",
        &[],
    ),
    (
        "archive-glob-rules-literals",
        "docs/fern-measurements/examples-docs/archive-glob-rules/openapi.yml",
        &["--enum-type", "literals"],
    ),
    (
        "marina-component-examples",
        "docs/fern-measurements/examples-docs/marina-component-examples/openapi.yml",
        &[],
    ),
    (
        "marina-component-examples-literals",
        "docs/fern-measurements/examples-docs/marina-component-examples/openapi.yml",
        &["--enum-type", "literals"],
    ),
    (
        "marina-crew-roles",
        "docs/fern-measurements/examples-docs/marina-crew-roles/openapi.yml",
        &[],
    ),
    (
        "marina-dock-log",
        "docs/fern-measurements/examples-docs/marina-dock-log/openapi.yml",
        &[],
    ),
    (
        "marina-dock-refs",
        "docs/fern-measurements/examples-docs/marina-dock-refs/openapi.yml",
        &[],
    ),
    (
        "marina-emoji-tag",
        "docs/fern-measurements/examples-docs/marina-emoji-tag/openapi.yml",
        &[],
    ),
    (
        "marina-empty-list-example",
        "docs/fern-measurements/examples-docs/marina-empty-list-example/openapi.yml",
        &[],
    ),
    (
        "marina-firmware-upload",
        "docs/fern-measurements/examples-docs/marina-firmware-upload/openapi.yml",
        &[],
    ),
    (
        "marina-nullable-note",
        "docs/fern-measurements/examples-docs/marina-nullable-note/openapi.yml",
        &[],
    ),
    (
        "marina-radio-parts",
        "docs/fern-measurements/examples-docs/marina-radio-parts/openapi.yml",
        &[],
    ),
    (
        "marina-skipper-refs",
        "docs/fern-measurements/examples-docs/marina-skipper-refs/openapi.yml",
        &[],
    ),
    (
        "marina-tide-channels",
        "docs/fern-measurements/examples-docs/marina-tide-channels/openapi.yml",
        &[],
    ),
];
// llmlint: ignore-end[expensive_tests_stay_behind_their_own_edge]

/// Crozier's output over `spec` with `flags`, compared whole with the Fern
/// tree `expected`, every departure held to `golden`'s ledger rows.
fn tree_failures(
    key: &str,
    spec: &Path,
    flags: &[&str],
    golden: &str,
    expected: &Path,
) -> Vec<String> {
    let out = tempfile::tempdir().expect("crozier output tempdir");
    let result = probe_command(spec, out.path())
        .args(flags)
        .output()
        .expect("run crozier");
    if !result.status.success() {
        return vec![format!(
            "{key}: crozier failed over {}: {}",
            spec.display(),
            String::from_utf8_lossy(&result.stderr)
        )];
    }
    match departure_ledger().golden(golden, &[]) {
        Ok(ledger) => golden_tree_failures(
            key,
            &spec.display().to_string(),
            &ledger,
            expected,
            out.path(),
        ),
        Err(failures) => failures,
    }
}

#[test]
fn examples_docs_measurements_match_fern() {
    let root = repo_root();
    let mut directories: Vec<String> = std::fs::read_dir(root.join(EXAMPLES_DOCS_DIR))
        .expect("the measurement directory exists")
        .filter_map(Result::ok)
        .filter(|entry| entry.path().is_dir())
        .map(|entry| entry.file_name().to_string_lossy().into_owned())
        .collect();
    directories.sort();
    let mut cases: Vec<&str> = CASES.iter().map(|(case, _, _)| *case).collect();
    cases.sort_unstable();
    assert_eq!(
        directories, cases,
        "{EXAMPLES_DOCS_DIR}: every case directory needs a CASES row"
    );
    let failures: Vec<String> = CASES
        .iter()
        .flat_map(|(case, spec, flags)| {
            let expected = root
                .join(EXAMPLES_DOCS_DIR)
                .join(case)
                .join("fern-expected");
            tree_failures(
                case,
                &root.join(spec),
                flags,
                &golden_path(&expected),
                &expected,
            )
        })
        .collect();
    assert!(failures.is_empty(), "{}", failures.join("\n\n"));
}

/// A hand-written fixture's committed Fern tree, copied so a test may perturb
/// it, with the golden its ledger rows belong to.
fn handwritten_copy(fixture: &str) -> (tempfile::TempDir, String, std::path::PathBuf) {
    let root = repo_root().join(HANDWRITTEN_DIR).join(fixture);
    let expected = root.join("fern-expected");
    let copy = tempfile::tempdir().expect("golden copy tempdir");
    copy_dir(&expected, copy.path());
    (copy, golden_path(&expected), root.join("openapi.yml"))
}

/// Plant one unexplained byte; a `from` the golden no longer holds fails here,
/// so a regenerated golden cannot leave a negative case silently unperturbed.
fn perturb(tree: &Path, rel: &str, from: &str, to: &str) {
    let path = tree.join(rel);
    let text = std::fs::read_to_string(&path).expect("a committed Fern file");
    assert!(text.contains(from), "{rel} holds no `{from}`");
    std::fs::write(&path, text.replace(from, to)).expect("perturb the tree");
}

/// `int64-example-rounded-out-of-range` explains exactly the out-of-range
/// rounding: an in-range rounding Fern writes is matched, so a changed value
/// there fails, as does an out-of-range spelling that is not the declared
/// example's nearest double. A missing document writes no SDK.
#[test]
fn int64_example_correction_explains_only_the_out_of_range_rounding() {
    let (tree, golden, spec) = handwritten_copy("odometer-reading");
    let check = |tree: &Path| tree_failures("odometer-reading", &spec, &[], &golden, tree);
    assert_eq!(check(tree.path()), Vec::<String>::new());
    for (rel, from, to) in [
        (
            "README.md",
            "trip_count=9007199254740992,",
            "trip_count=9007199254740993,",
        ),
        (
            "src/fern/client.py",
            "metres=9223372036854776000,",
            "metres=9223372036854775000,",
        ),
    ] {
        let (perturbed, _, _) = handwritten_copy("odometer-reading");
        perturb(perturbed.path(), rel, from, to);
        let failures = check(perturbed.path());
        assert!(
            failures
                .iter()
                .any(|failure| failure.contains(&format!("{rel} differs"))),
            "{rel}: {failures:?}"
        );
    }
    let missing = tempfile::tempdir().expect("missing source tempdir");
    let out = missing.path().join("sdk");
    probe_command(&missing.path().join("openapi.yml"), &out)
        .assert()
        .failure()
        .stderr(predicates::str::contains("could not read spec"));
    assert!(!out.exists(), "a missing document must write no SDK");
}

/// `docstring-literal-dollar-escape` explains only a docstring passing the
/// declared `const`: Fern's own README spelling of it is matched, and the
/// plain `label` string beside it takes no correction.
#[test]
fn dollar_docstring_correction_explains_only_the_declared_const() {
    let case = literals_mode::case("prompt-variable");
    let baseline = case.materialize();
    assert_eq!(
        literals_mode::case_failures(&case, baseline.path(), "literals"),
        Vec::<String>::new()
    );
    for (rel, from, to) in [
        (
            "README.md",
            "    variable=\"$PS1\",",
            "    variable=\"\\\\$PS1\",",
        ),
        (
            "src/fern/client.py",
            "            label=\"Costs $5 at $HOST\",",
            "            label=\"Costs \\\\$5 at \\\\$HOST\",",
        ),
    ] {
        let tree = case.materialize();
        perturb(tree.path(), rel, from, to);
        let failures = literals_mode::case_failures(&case, tree.path(), "literals");
        assert!(
            failures
                .iter()
                .any(|failure| failure.contains(&format!("{rel} differs"))),
            "{rel}: {failures:?}"
        );
    }
}

/// `multipart-object-required-file-example` adds only the required file's
/// placeholder to a plain multipart docstring: any other changed argument in
/// the same call still fails.
#[test]
fn plain_multipart_file_correction_explains_only_the_placeholder() {
    let (tree, golden, spec) = handwritten_copy("poster-upload");
    let check = |tree: &Path| tree_failures("poster-upload", &spec, &[], &golden, tree);
    assert_eq!(check(tree.path()), Vec::<String>::new());
    perturb(
        tree.path(),
        "src/fern/client.py",
        "            title=\"title\",",
        "            title=\"poster\",",
    );
    let failures = check(tree.path());
    assert!(
        failures
            .iter()
            .any(|failure| failure.contains("src/fern/client.py differs")),
        "{failures:?}"
    );
}

// llmlint: ignore-block[expensive_tests_stay_behind_their_own_edge] Every Fern golden comparison — the corpus `*_matches_fern_output` tests, the hand-written, probe and measurement gates — runs in this one binary suite by the project's design (crates/crozier-e2e/AGENTS.md), which drives the binary crozier:build leaves; giving golden comparisons their own Nx edge is a graph change for that whole family, not for these cases.
/// Each isolating case of a component, empty-array, union-item, map,
/// parameter-list or description match, and of a catalogued departure, fails
/// on one unexplained byte beside what it pins: the match is byte for byte, and
/// each departure's rule admits only its own difference.
#[test]
fn examples_docs_cases_fail_on_an_adjacent_unexplained_byte() {
    let root = repo_root();
    for (case, rel, from, to) in [
        (
            "marina-component-examples",
            "reference.md",
            "    grant=SessionFormGrant.HARBOUR_PASS,",
            "    grant=SessionFormGrant.REFRESH,",
        ),
        (
            "marina-component-examples-literals",
            "reference.md",
            "    grant=\"harbour_pass\",",
            "    grant=\"refresh\",",
        ),
        (
            "marina-crew-roles",
            "src/fern/crews/client.py",
            "                        name=\"Ada\",\n                    ),",
            "                        name=\"Ada\",\n                    )",
        ),
        (
            "marina-empty-list-example",
            "reference.md",
            "        \"8801723\"",
            "        \"5520193\"",
        ),
        (
            "marina-firmware-upload",
            "reference.md",
            "**version:** `typing.Optional[str]` ",
            "**version:** `typing.Optional[int]` ",
        ),
        (
            "marina-nullable-note",
            "reference.md",
            " — Pontoon the berth is moored to",
            " — Pontoon",
        ),
        (
            "marina-radio-parts",
            "src/fern/radio/client.py",
            "transcript=\"Requesting a berth for the night\",",
            "transcript=\"Requesting a berth\",",
        ),
        (
            "marina-tide-channels",
            "reference.md",
            "client.tides.get_surge(\n    station_id=\"station_id\",",
            "client.tides.get_surge(\n    station_id=\"station\",",
        ),
        (
            "marina-dock-refs",
            "src/fern/docks/client.py",
            "dock_id_or_code=\"dock_id_or_code\",",
            "dock_id_or_code=\"dock\",",
        ),
        (
            "marina-dock-log",
            "src/fern/docks/client.py",
            "dock_id=\"dock_id\",",
            "dock_id=\"dock\",",
        ),
        (
            "marina-skipper-refs",
            "reference.md",
            "**skipper:** `str` ",
            "**skipper:** `int` ",
        ),
        (
            "marina-emoji-tag",
            "reference.md",
            "client.🚧_legacy_endpoints.list_legacy_moorings(",
            "client.🚧_legacy_endpoint.list_legacy_moorings(",
        ),
    ] {
        let (_, spec, flags) = CASES
            .iter()
            .find(|(name, _, _)| *name == case)
            .unwrap_or_else(|| panic!("{case} is a CASES row"));
        let expected = root
            .join(EXAMPLES_DOCS_DIR)
            .join(case)
            .join("fern-expected");
        let copy = tempfile::tempdir().expect("golden copy tempdir");
        copy_dir(&expected, copy.path());
        perturb(copy.path(), rel, from, to);
        let failures = tree_failures(
            case,
            &root.join(spec),
            flags,
            &golden_path(&expected),
            copy.path(),
        );
        assert!(
            failures
                .iter()
                .any(|failure| failure.contains(&format!("{rel} differs"))),
            "{case} {rel}: {failures:?}"
        );
    }
}
// llmlint: ignore-end[expensive_tests_stay_behind_their_own_edge]
