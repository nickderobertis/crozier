//! The shapes behind RS-Server's emission differences, each in a document
//! written for it, held whole against the certified pair's tree in both enum
//! modes (`docs/fern-measurements/emission-parity/`). The record is
//! `docs/rs-server-emission-parity.md`.
//!
//! - `survey-shapes`: GeoJSON-like members tagged by a `const` `kind`, inlined
//!   as variants of a discriminated union and also named by an undiscriminated
//!   one; their nullable tuple `extent`; coordinates two and three arrays deep;
//!   an inline PATCH body union beside a `const` property; and a tag-scoped
//!   discriminated body union.
//! - `tide-windows`: nullable items two arrays deep, with a `minItems` the
//!   worked examples repair.
//! - `lantern-open-ping`: an empty root `security` list beside a secured and an
//!   unsecured operation, the `empty-root-security-optional-credential`
//!   departure.

use std::path::Path;

use super::{crozier_clean_env, departure_ledger, golden_tree_failures, repo_root};

/// Where the measurements live; each case's `fern-expected/` is a compared golden.
pub(crate) const EMISSION_PARITY_DIR: &str = "docs/fern-measurements/emission-parity";

fn generate(spec: &Path, out: &Path, mode: &str) -> std::process::Output {
    crozier_clean_env()
        .args(["--no-config", "generate", "python", "--spec"])
        .arg(spec)
        .arg("--output")
        .arg(out)
        .args([
            "--package-name",
            "fern",
            "--project-name",
            "default_package_name",
            "--enum-type",
            mode,
        ])
        .output()
        .expect("run crozier")
}

/// crozier's tree for `case` in both enum modes matches the certified pair's,
/// apart from the departures its ledger pins; then `break_it` edits crozier's
/// tree and the comparison must name `broken`.
fn holds_in_both_modes(case: &str, broken: &str, break_it: fn(&str) -> String) {
    let spec = repo_root()
        .join(EMISSION_PARITY_DIR)
        .join(case)
        .join("openapi.yml");
    // The source document, so rules that read it (the credential departure,
    // the rejected-example repairs) can.
    let source = spec.display().to_string();
    for (mode, tree) in [
        ("python-enums", case.to_owned()),
        ("literals", format!("{case}-literals")),
    ] {
        let golden = format!("{EMISSION_PARITY_DIR}/{tree}/fern-expected");
        let expected = repo_root().join(&golden);
        let ledger = departure_ledger()
            .golden(&golden, &[])
            .unwrap_or_else(|failures| panic!("{}", failures.join("\n")));
        let temp = tempfile::tempdir().expect("output tempdir");
        let out = temp.path().join("sdk");
        let run = generate(&spec, &out, mode);
        assert!(
            run.status.success(),
            "{case} {mode}: {}",
            String::from_utf8_lossy(&run.stderr)
        );
        let failures = golden_tree_failures(case, &source, &ledger, &expected, &out);
        assert!(
            failures.is_empty(),
            "{case} {mode}: {}",
            failures.join("\n\n")
        );
        let file = out.join(broken);
        let text = std::fs::read_to_string(&file).expect("the file to break");
        let edited = break_it(&text);
        assert_ne!(edited, text, "{case} {mode}: the edit must change {broken}");
        std::fs::write(&file, edited).unwrap();
        let unexplained = golden_tree_failures(case, &source, &ledger, &expected, &out);
        assert!(
            unexplained.iter().any(|failure| failure.contains(broken)),
            "{case} {mode}: an unexplained {broken} must fail the comparison: {unexplained:?}"
        );
    }
}

// llmlint: ignore-block[expensive_tests_stay_behind_their_own_edge] Each of these journeys generates one small SDK through the binary, on the crozier-e2e edge every other golden comparison shares; splitting that edge is the drafted follow-up "Give crozier-e2e's generator-replay journeys an Nx edge narrower than e2eReads".
/// Causes 1, 2 and 5: each flattened variant types its fields as its member
/// model does, the members keep their `kind` tag, the PATCH body's `const`
/// property is declared, and the tag's `types/__init__.py` imports a union's
/// names together. Undoing the variant typing fails the comparison.
#[test]
fn inlined_variants_tags_and_body_siblings_match_fern() {
    holds_in_both_modes("survey-shapes", "src/fern/types/site_outline.py", |text| {
        text.replacen(
            "extent: typing.Optional[typing.List[typing.Any]] = None",
            "extent: typing.Optional[MarkerExtent] = None",
            1,
        )
    });
}

/// Cause 3: nullable items two arrays deep are optional elements. A named
/// item alias in their place fails the comparison.
#[test]
fn nullable_items_two_arrays_deep_match_fern() {
    holds_in_both_modes("tide-windows", "src/fern/types/window_plan.py", |text| {
        text.replacen(
            "typing.List[typing.List[typing.Optional[dt.datetime]]]",
            "typing.List[typing.List[WindowPlanWindowsItemItem]]",
            1,
        )
    });
}

/// Cause 4: only the credential lines differ, under the departure; a
/// credential mismatch it does not describe still fails.
#[test]
fn an_empty_root_security_list_departs_only_on_the_credential() {
    holds_in_both_modes(
        "lantern-open-ping",
        "src/fern/core/client_wrapper.py",
        |text| {
            text.replacen(
                "api_key: typing.Optional[str] = None,",
                "api_key: typing.Optional[str] = \"\",",
                1,
            )
        },
    );
}
// llmlint: ignore-end[expensive_tests_stay_behind_their_own_edge]
