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
];

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

/// Replace `from` with `to` in the tree's `rel`, which must hold `from`.
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
