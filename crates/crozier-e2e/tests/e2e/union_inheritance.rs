//! The union-nullability and inherited-model repairs of tickets #825, #826,
//! #827, #838 and #839, each settled against a from-scratch document under
//! [`DIR`] and the certified pair's complete tree for it (Fern CLI 5.200.0,
//! fern-python-sdk 5.41.25), in both enum modes.
//!
//! Every measurement runs the real binary and compares its SDK with the
//! certified tree file for file; each is shown to fail for its own rule by
//! writing back into crozier's output the bytes crozier wrote before the repair.

use std::collections::BTreeSet;
use std::path::{Path, PathBuf};

use super::{departure_ledger, golden_tree_failures, probe_command, repo_root, walk_files};

/// Where the measurements live; each case's `fern-expected/` is a compared golden.
pub(crate) const DIR: &str = "docs/fern-measurements/union-inheritance";

/// A case's literals overlay, laid over its `fern-expected/`.
pub(crate) const LITERALS: &str = "expected-literals/fern-expected";

/// The overlay manifest `tools/fern-goldens/golden_overlay.py` writes.
const MANIFEST: &str = ".crozier-overlay.json";

/// Each ticket's case and the rule's characteristic bytes in the certified
/// pair's tree: `(ticket, case, file, certified bytes, what crozier wrote before)`.
const MEASUREMENTS: &[(&str, &str, &str, &str, &str)] = &[
    (
        "#825",
        "null-union-alternative",
        "src/fern/kilns/types/register_kiln_request_settings_value_zero.py",
        "typing.Union[str, float, bool, typing.Dict[str, typing.Any]]",
        "typing.Union[str, float, bool, typing.Any, typing.Dict[str, typing.Any]]",
    ),
    (
        "#826",
        "nullable-typeless-component",
        "src/fern/types/shuttle_state.py",
        "ShuttleState = typing.Optional[typing.Any]",
        "ShuttleState = typing.Any",
    ),
    (
        "#827",
        "overridden-parent-layout",
        "src/fern/types/vent_closed_alert.py",
        "from .alert_base_severity import AlertBaseSeverity",
        "from .vent_alert_severity import VentAlertSeverity",
    ),
    (
        "#838",
        "restated-default-inherits-enum",
        "src/fern/types/crossing_delayed_notice.py",
        "phase: typing.Optional[CrossingDelayedNoticePhase]",
        "phase: typing.Optional[str]",
    ),
    (
        "#839",
        "declared-scalar-union-members",
        "src/fern/types/reading_value.py",
        "typing.Optional[str]",
        "typing.Optional[ReadingValueText]",
    ),
];

fn spec(case: &str) -> PathBuf {
    repo_root().join(DIR).join(case).join("openapi.yml")
}

fn golden(case: &str) -> String {
    format!("{DIR}/{case}/fern-expected")
}

fn generate(case: &str, mode: &str, out: &Path) {
    probe_command(&spec(case), out)
        .args(["--enum-type", mode])
        .assert()
        .success();
}

/// crozier's python-enums SDK for `case` against its certified-pair tree.
fn enum_failures(case: &str, out: &Path) -> Vec<String> {
    let golden = golden(case);
    let ledger = departure_ledger()
        .golden(&golden, &[])
        .unwrap_or_else(|failures| panic!("{}", failures.join("\n")));
    golden_tree_failures(
        &format!("{case} (python-enums)"),
        &spec(case).display().to_string(),
        &ledger,
        &repo_root().join(&golden),
        out,
    )
}

/// The removed base files a literals overlay's manifest names.
fn removed(overlay: &Path) -> Vec<String> {
    let manifest: serde_json::Value = serde_json::from_str(
        &std::fs::read_to_string(overlay.join(MANIFEST)).expect("the overlay manifest"),
    )
    .expect("the overlay manifest is JSON");
    assert_eq!(manifest["enum_type"], "literals", "{}", overlay.display());
    manifest["removed"]
        .as_array()
        .expect("a removed list")
        .iter()
        .map(|rel| rel.as_str().expect("a path").to_string())
        .collect()
}

/// crozier's literals SDK for `case` against the certified pair's literals
/// tree: the base less the files the overlay removes, with the overlay's own
/// files laid over it.
fn literals_failures(case: &str, out: &Path) -> Vec<String> {
    let base = repo_root().join(golden(case));
    let overlay_golden = format!("{DIR}/{case}/{LITERALS}");
    let overlay = repo_root().join(&overlay_golden);
    let removed = removed(&overlay);
    let tree = tempfile::tempdir().expect("literals tree tempdir");
    let copy = |from: &Path, rel: &str| {
        let to = tree.path().join(rel);
        std::fs::create_dir_all(to.parent().expect("a file has a parent")).expect("mkdir");
        std::fs::copy(from.join(rel), &to).expect("copy a Fern file");
    };
    for rel in walk_files(&base) {
        if !removed.contains(&rel) {
            copy(&base, &rel);
        }
    }
    let own: BTreeSet<String> = walk_files(&overlay)
        .into_iter()
        .filter(|rel| rel != MANIFEST)
        .collect();
    for rel in &own {
        copy(&overlay, rel);
    }
    let inherited = departure_ledger()
        .golden(&golden(case), &[])
        .unwrap_or_else(|failures| panic!("{}", failures.join("\n")));
    let ledger = departure_ledger()
        .golden(&overlay_golden, &[])
        .unwrap_or_else(|failures| panic!("{}", failures.join("\n")))
        .inherit(inherited, own, &removed);
    golden_tree_failures(
        &format!("{case} (literals)"),
        &spec(case).display().to_string(),
        &ledger,
        tree.path(),
        out,
    )
}

/// Each ticket's measurement is the certified pair's tree file for file in
/// both enum modes, and the comparison fails once the rule's bytes are written
/// back the way crozier wrote them before the repair.
#[test]
fn union_inheritance_repairs_match_the_certified_pair() {
    let mut failures = Vec::new();
    for (ticket, case, file, certified, before) in MEASUREMENTS {
        let temp = tempfile::tempdir().expect("output tempdir");
        let out = temp.path().join("sdk");
        generate(case, "python-enums", &out);
        failures.extend(enum_failures(case, &out));
        let path = out.join(file);
        let written = std::fs::read_to_string(&path)
            .unwrap_or_else(|error| panic!("{ticket} {case}: {file}: {error}"));
        assert!(
            written.contains(certified),
            "{ticket} {case}: {file} lacks the certified bytes {certified:?}"
        );
        std::fs::write(&path, written.replacen(certified, before, 1)).expect("tamper");
        let tampered = enum_failures(case, &out);
        assert!(
            tampered.iter().any(|failure| failure.contains(file)),
            "{ticket} {case}: writing {before:?} back into {file} must fail the comparison: {tampered:?}"
        );
        let literals = temp.path().join("literals");
        generate(case, "literals", &literals);
        failures.extend(literals_failures(case, &literals));
    }
    assert!(failures.is_empty(), "{}", failures.join("\n\n"));
}

/// #839's other half: a structured alternative declaring a type name is still
/// named by it, while the scalar alternatives beside it stay inline and no
/// module is written for them.
#[test]
fn declared_scalar_union_members_stay_inline_and_structured_ones_stay_named() {
    let temp = tempfile::tempdir().expect("output tempdir");
    let out = temp.path().join("sdk");
    generate("declared-scalar-union-members", "python-enums", &out);
    let types = out.join("src/fern/types");
    assert!(types.join("threshold_band.py").is_file(), "the object alternative keeps its declared name");
    for scalar in [
        "reading_value_text.py",
        "reading_value_number.py",
        "reading_value_flag.py",
        "reading_value_blob.py",
        "threshold_count.py",
    ] {
        assert!(!types.join(scalar).exists(), "crozier wrote a module for {scalar}");
    }
    let threshold = std::fs::read_to_string(types.join("reading_threshold.py")).expect("the alias");
    assert!(
        threshold.contains("ReadingThreshold = typing.Union[int, ThresholdBand]"),
        "{threshold}"
    );
}
