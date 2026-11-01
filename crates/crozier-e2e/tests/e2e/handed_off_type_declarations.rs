//! The type-declaration root causes the fixture-only witness searches handed
//! off, each settled against a from-scratch document and the certified pair's
//! complete tree under [`DIR`] (Fern CLI 5.163.1, fern-python-sdk 5.41.3):
//! the triage record is `docs/fern-measurements/handed-off/type-declarations.tsv`.
//!
//! Every measurement is held whole through the real binary, in both enum modes
//! where its `expected-literals/` overlay records a literals tree, and each is
//! shown to fail for its own rule: the tamper written back into crozier's
//! output is the bytes crozier wrote before the repair.

use std::collections::BTreeSet;
use std::path::{Path, PathBuf};

use super::{departure_ledger, golden_tree_failures, probe_command, repo_root, walk_files};

/// Where the measurements live; each cause's `fern-expected/` is a compared golden.
pub(crate) const DIR: &str = "docs/fern-measurements/handed-off/type-declarations";

/// A cause's literals overlay, laid over its `fern-expected/`.
pub(crate) const LITERALS: &str = "expected-literals/fern-expected";

/// The overlay manifest `tools/fern-goldens/golden_overlay.py` writes.
const MANIFEST: &str = ".crozier-overlay.json";

/// Each measurement and the rule's characteristic bytes in the certified
/// pair's tree: `(cause, file, certified bytes, what crozier wrote before)`.
const MEASUREMENTS: &[(&str, &str, &str, &str)] = &[
    (
        "digit-leading-schema-name",
        "src/fern/types/__init__.py",
        "FourHundredOneResponse",
        "Four01Response",
    ),
    (
        "number-uint32-format",
        "src/fern/types/lamp.py",
        "rotations: typing.Optional[int]",
        "rotations: typing.Optional[float]",
    ),
    (
        "inline-type-naming",
        "src/fern/captions/media/types/__init__.py",
        "CaptionMediaRequestDialect",
        "CaptionUrlMediaRequestDialect",
    ),
    (
        "allof-description-wrapper",
        "src/fern/client.py",
        "def retire_telescope(self, name: str,",
        "def retire_telescope(self, name: typing.Any,",
    ),
    (
        "parameter-type-resolution",
        "src/fern/client.py",
        "request: typing.Sequence[typing.Any],",
        "request: typing.Sequence[typing.Optional[typing.Any]],",
    ),
    (
        "map-value-modelling",
        "src/fern/client.py",
        "typing.Dict[str, GetCraneSummaryResponseValue]",
        "typing.Dict[str, typing.Any]",
    ),
    (
        "blank-description-enum-docstring",
        "src/fern/types/crossing_weather.py",
        "    \"\"\" \"\"\"\n\n",
        "",
    ),
    (
        "allof-member-description-docstring",
        "src/fern/types/bad_request_error_body.py",
        "class BadRequestErrorBody(UniversalBaseModel):\n",
        "class BadRequestErrorBody(UniversalBaseModel):\n    \"\"\"\n    The fields that were rejected\n    \"\"\"\n\n",
    ),
    (
        "nullable-anyof-member-description-alias-docstring",
        "src/fern/types/job_stopped.py",
        "    Why the job stopped.\n",
        "",
    ),
    (
        "nullable-anyof-allof-described-member",
        "src/fern/types/create_plan_body_course.py",
        "class CreatePlanBodyCourse(enum.StrEnum):",
        "class CreatePlanBodyCourse(Course):",
    ),
    (
        "description-source",
        "src/fern/types/piece_links.py",
        "    \"\"\" \"\"\"\n\n",
        "",
    ),
    (
        "R3",
        "src/fern/client.py",
        ") -> typing.Optional[ClimateReading]:",
        ") -> ClimateReading:",
    ),
    (
        "R6",
        "reference.md",
        "**boat_name:** `str` \n\n\n",
        "**boat_name:** `str` — \n",
    ),
    (
        "reference-description-leading-newline",
        "src/fern/client.py",
        "request: PacketNoteCreateRequest",
        "request: typing.Any",
    ),
    (
        "R7",
        "src/fern/types/__init__.py",
        "GetTileV2TilesCoastalZxyPbfGetRequestShading",
        "GetTileV2TilesCoastalZXYPbfGetRequestShading",
    ),
    (
        "type-placement",
        "src/fern/parcels/types/__init__.py",
        "ListParcelsRequestLabelStyle",
        "ListParcelsRequestCarrierStyle",
    ),
    (
        "schema-type-resolution",
        "src/fern/types/oven_status.py",
        "alarms: typing.Optional[typing.List[Alarm]]",
        "alarms: typing.Optional[OvenStatusAlarms]",
    ),
    (
        "R19",
        "src/fern/types/survey.py",
        "strata: typing.Optional[SurveyStrata]",
        "strata: typing.Optional[typing.List[typing.Any]]",
    ),
];

/// The one measurement whose comparison is not whole: the bodies record's
/// `reference-body-param-doc` (owned by the `parity-bodies-media-r1` node)
/// documents a bytes body beside JSON types as the component name, and that
/// single `reference.md` line stays attributed to it.
const ORPHAN: &str = "orphan-type-emission";

fn spec(cause: &str) -> PathBuf {
    repo_root().join(DIR).join(cause).join("openapi.yml")
}

fn golden(cause: &str) -> String {
    format!("{DIR}/{cause}/fern-expected")
}

fn generate(cause: &str, mode: &str, out: &Path) {
    probe_command(&spec(cause), out)
        .args(["--enum-type", mode])
        .assert()
        .success();
}

/// crozier's python-enums SDK for `cause` against its certified-pair tree.
fn enum_failures(cause: &str, out: &Path) -> Vec<String> {
    let golden = golden(cause);
    let ledger = departure_ledger()
        .golden(&golden, &[])
        .unwrap_or_else(|failures| panic!("{}", failures.join("\n")));
    golden_tree_failures(
        &format!("{cause} (python-enums)"),
        &spec(cause).display().to_string(),
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

/// crozier's literals SDK for `cause` against the certified pair's literals
/// tree: the base less the files the overlay removes, with the overlay's own
/// files laid over it.
fn literals_failures(cause: &str, out: &Path) -> Vec<String> {
    let base = repo_root().join(golden(cause));
    let overlay_golden = format!("{DIR}/{cause}/{LITERALS}");
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
        .golden(&golden(cause), &[])
        .unwrap_or_else(|failures| panic!("{}", failures.join("\n")));
    let ledger = departure_ledger()
        .golden(&overlay_golden, &[])
        .unwrap_or_else(|failures| panic!("{}", failures.join("\n")))
        .inherit(inherited, own, &removed);
    golden_tree_failures(
        &format!("{cause} (literals)"),
        &spec(cause).display().to_string(),
        &ledger,
        tree.path(),
        out,
    )
}

fn has_literals(cause: &str) -> bool {
    repo_root().join(DIR).join(cause).join(LITERALS).is_dir()
}

// llmlint: ignore-block[expensive_tests_stay_behind_their_own_edge] Each of these journeys generates one small SDK per measurement and compares it whole, on the crozier-e2e edge every other golden comparison shares; splitting that edge is the drafted follow-up "Give crozier-e2e's generator-replay journeys an Nx edge narrower than e2eReads".
/// Every settled measurement is the certified pair's tree file for file in
/// python-enums mode and, where an overlay records one, in literals mode; and
/// each comparison fails once the rule's bytes are written back the way crozier
/// wrote them before the repair.
#[test]
fn handed_off_type_declarations_match_the_certified_pair() {
    let mut failures = Vec::new();
    for (cause, file, certified, before) in MEASUREMENTS {
        let temp = tempfile::tempdir().expect("output tempdir");
        let out = temp.path().join("sdk");
        generate(cause, "python-enums", &out);
        failures.extend(enum_failures(cause, &out));
        let path = out.join(file);
        let written = std::fs::read_to_string(&path)
            .unwrap_or_else(|error| panic!("{cause}: {file}: {error}"));
        assert!(
            written.contains(certified),
            "{cause}: {file} lacks the certified bytes {certified:?}"
        );
        std::fs::write(&path, written.replacen(certified, before, 1)).expect("tamper");
        let tampered = enum_failures(cause, &out);
        assert!(
            tampered.iter().any(|failure| failure.contains(file)),
            "{cause}: writing {before:?} back into {file} must fail the comparison: {tampered:?}"
        );
        if has_literals(cause) {
            let literals = temp.path().join("literals");
            generate(cause, "literals", &literals);
            failures.extend(literals_failures(cause, &literals));
        }
    }
    assert!(failures.is_empty(), "{}", failures.join("\n\n"));
}

/// The orphan-type measurement is the certified pair's tree in both enum modes
/// apart from one `reference.md` line another area owns: no model for a
/// download's JSON alternative, for a dropped readOnly body object or for a
/// body only a replaced operation posts, and the model a bytes body names kept.
#[test]
fn orphan_types_match_the_certified_pair_but_one_attributed_line() {
    let temp = tempfile::tempdir().expect("output tempdir");
    let out = temp.path().join("sdk");
    generate(ORPHAN, "python-enums", &out);
    for absent in [
        "src/fern/archive/types/get_archive_path_response.py",
        "src/fern/sensors/types/register_sensor_request_calibration.py",
        "src/fern/types/sensors_add_note_request.py",
    ] {
        assert!(!out.join(absent).exists(), "crozier wrote {absent}");
    }
    assert!(out.join("src/fern/types/create_key_request.py").is_file());
    let expect_attributed = |failures: Vec<String>, mode: &str| {
        let [only] = failures.as_slice() else {
            panic!("{mode}: expected the one attributed reference.md difference: {failures:?}");
        };
        assert!(
            only.contains("reference.md")
                && only.contains("**request:** `CreateKeyRequest`")
                && only.contains("typing.Union[bytes, typing.Iterator[bytes]"),
            "{mode}: the difference is not reference-body-param-doc's line: {only}"
        );
    };
    expect_attributed(enum_failures(ORPHAN, &out), "python-enums");
    let literals = temp.path().join("literals");
    generate(ORPHAN, "literals", &literals);
    expect_attributed(literals_failures(ORPHAN, &literals), "literals");
    // A model written back for the download's JSON alternative is unexplained.
    std::fs::copy(
        out.join("src/fern/types/create_key_request.py"),
        out.join("src/fern/types/get_archive_path_response.py"),
    )
    .expect("tamper");
    assert!(enum_failures(ORPHAN, &out)
        .iter()
        .any(|failure| failure.contains("get_archive_path_response.py")));
}
// llmlint: ignore-end[expensive_tests_stay_behind_their_own_edge]
