//! The handed-off body and media-type root causes, each measured on a
//! from-scratch document against the certified pair
//! (`docs/fern-measurements/handed-off/bodies-media/`, triaged in
//! `docs/fern-measurements/handed-off/bodies-media.tsv`).
//!
//! Every cause was a parity gap, repaired in `src/`: crozier's complete SDK for
//! the measurement document must equal the certified pair's committed tree, and
//! the line the repair decides must fail the comparison when written the way
//! crozier wrote it before the repair. The causes whose verdict rests on the
//! wire are driven through both generated SDKs against a local HTTP server
//! (`bodies_media_wire.py`), the journey each `runtime.txt` records.

use std::path::{Path, PathBuf};

use predicates::prelude::*;

use super::{departure_ledger, golden_tree_failures, probe_command, repo_root, runtime_python_env};

/// Where the measurements live; each cause's `fern-expected/` is a compared golden.
pub(crate) const BODIES_MEDIA_DIR: &str = "docs/fern-measurements/handed-off/bodies-media";
/// The one cause whose result turns on the enum mode keeps the certified pair's
/// complete `literals` tree beside its `python_enums` one.
pub(crate) const RESPONSE_LITERALS_GOLDEN: &str = "docs/fern-measurements/handed-off/bodies-media/response-type-resolution/expected-literals/fern-expected";
const WIRE: &str = "crates/crozier-e2e/tests/e2e/bodies_media_wire.py";

fn case_dir(cause: &str) -> PathBuf {
    repo_root().join(BODIES_MEDIA_DIR).join(cause)
}

fn generate(cause: &str, out: &Path) {
    probe_command(&case_dir(cause).join("openapi.yml"), out)
        .assert()
        .success();
}

/// crozier's SDK at `out` against `cause`'s certified-pair tree, apart from the
/// departures the ledger records for it.
fn failures(cause: &str, out: &Path) -> Vec<String> {
    let golden = format!("{BODIES_MEDIA_DIR}/{cause}/fern-expected");
    let ledger = departure_ledger()
        .golden(&golden, &[])
        .unwrap_or_else(|failures| panic!("{}", failures.join("\n")));
    golden_tree_failures(
        cause,
        &case_dir(cause).join("openapi.yml").display().to_string(),
        &ledger,
        &repo_root().join(&golden),
        out,
    )
}

/// Generate `cause`'s SDK and hold it whole to the certified pair's, then show
/// that `file` spelling `fern` (as both trees do) is what the comparison turns
/// on: written as crozier wrote it before the repair (`before`), the comparison
/// names `file`.
fn holds(cause: &str, file: &str, fern: &str, before: &str) {
    let temp = tempfile::tempdir().expect("output tempdir");
    let out = temp.path().join("sdk");
    generate(cause, &out);
    let matched = failures(cause, &out);
    assert!(matched.is_empty(), "{cause}: {}", matched.join("\n\n"));
    for tree in [case_dir(cause).join("fern-expected"), out.clone()] {
        let path = tree.join(file);
        let text = std::fs::read_to_string(&path)
            .unwrap_or_else(|error| panic!("{}: {error}", path.display()));
        assert!(text.contains(fern), "{}: no {fern:?}", path.display());
    }
    let generated = out.join(file);
    let text = std::fs::read_to_string(&generated).expect("the generated file");
    std::fs::write(&generated, text.replacen(fern, before, 1)).expect("rewrite the file");
    let unexplained = failures(cause, &out);
    assert!(
        unexplained.iter().any(|failure| failure.contains(file)),
        "{cause}: {file} written as {before:?} must fail the comparison: {unexplained:?}"
    );
}

/// As [`holds`], for a repair that stopped crozier writing a file: written back,
/// the model `file` crozier used to declare fails the comparison.
fn holds_without(cause: &str, file: &str, contents: &str) {
    let temp = tempfile::tempdir().expect("output tempdir");
    let out = temp.path().join("sdk");
    generate(cause, &out);
    let matched = failures(cause, &out);
    assert!(matched.is_empty(), "{cause}: {}", matched.join("\n\n"));
    assert!(
        !out.join(file).exists(),
        "{cause}: crozier still writes {file}"
    );
    std::fs::create_dir_all(out.join(file).parent().expect("a parent")).expect("the directory");
    std::fs::write(out.join(file), contents).expect("write the file back");
    let unexplained = failures(cause, &out);
    assert!(
        unexplained.iter().any(|failure| failure.contains(file)),
        "{cause}: a written-back {file} must fail the comparison: {unexplained:?}"
    );
}

// llmlint: ignore-block[expensive_tests_stay_behind_their_own_edge] Each of these journeys generates one small SDK and compares it whole, on the crozier-e2e edge every other golden comparison shares; splitting that edge is the drafted follow-up "Give crozier-e2e's generator-replay journeys an Nx edge narrower than e2eReads".
/// Fern reads `200`, `201`, `202` and `204` only, reads JSON before text, keeps
/// a nullable inline object's model optional, names an inline enum response, and
/// reads a `*/*` declared before a schema-less `application/json`.
#[test]
fn response_types_follow_the_entry_fern_reads() {
    holds(
        "response-type-resolution",
        "reference.md",
        ">get_profile</a>(...) -> Profile</code>",
        ">get_profile</a>(...) -> typing.Any</code>",
    );
    holds(
        "response-type-resolution",
        "src/fern/firings/client.py",
        "    ) -> typing.Optional[GetFiringResponse]:\n",
        "    ) -> GetFiringResponse:\n",
    );
    holds(
        "response-type-resolution",
        "src/fern/errors/conflict_error.py",
        "body: str,",
        "body: ConflictErrorBody,",
    );
}

/// Under `literals`, the hoisted enum responses are the certified pair's literal
/// aliases, and the rest of the SDK matches as under `python_enums`.
#[test]
fn response_types_follow_the_entry_fern_reads_under_literals() {
    let temp = tempfile::tempdir().expect("output tempdir");
    let out = temp.path().join("sdk");
    probe_command(
        &case_dir("response-type-resolution").join("openapi.yml"),
        &out,
    )
    .args(["--enum-type", "literals"])
    .assert()
    .success();
    let ledger = departure_ledger()
        .golden(RESPONSE_LITERALS_GOLDEN, &[])
        .unwrap_or_else(|failures| panic!("{}", failures.join("\n")));
    let found = golden_tree_failures(
        "response-type-resolution (literals)",
        &case_dir("response-type-resolution")
            .join("openapi.yml")
            .display()
            .to_string(),
        &ledger,
        &repo_root().join(RESPONSE_LITERALS_GOLDEN),
        &out,
    );
    assert!(found.is_empty(), "{}", found.join("\n\n"));
}

/// A `200` JSON body beside a `207` offering only `text/event-stream` streams
/// the method, and the README gains its Streaming section.
#[test]
fn an_events_only_success_streams_the_method() {
    holds(
        "streaming-detection",
        "README.md",
        "- [Streaming](#streaming)\n",
        "",
    );
}

/// A `text/json` body is JSON, sent under its own key.
#[test]
fn a_text_json_body_is_sent_under_its_key() {
    holds(
        "media-type-recognition",
        "src/fern/deposits/raw_client.py",
        "\"content-type\": \"text/json\",",
        "\"content-type\": \"application/json\",",
    );
}

/// A wildcard spread body, a titled body and a described inline body each send
/// the content type Fern's importer decides.
#[test]
fn json_bodies_send_the_content_type_fern_decides() {
    holds(
        "request-content-type-header",
        "src/fern/notes/raw_client.py",
        "            headers={\n                \"content-type\": \"application/json\",\n            },\n",
        "",
    );
    holds_without(
        "request-content-type-header",
        "src/fern/types/tuning.py",
        "from ..core.pydantic_utilities import UniversalBaseModel\n\n\nclass Tuning(UniversalBaseModel):\n    strike_note: str\n",
    );
}

/// `application/*+json` declared first names no content type.
#[test]
fn a_vendor_range_declared_first_sends_no_content_type() {
    holds(
        "vendor-json-media-first-content-type",
        "src/fern/bays/raw_client.py",
        "                \"humidity\": humidity,\n            },\n            request_options=request_options,",
        "                \"humidity\": humidity,\n            },\n            headers={\n                \"content-type\": \"application/json\",\n            },\n            request_options=request_options,",
    );
}

/// A GeoJSON success is parsed as its model.
#[test]
fn a_geo_json_success_is_parsed_as_its_model() {
    holds(
        "geo-json-success-media",
        "src/fern/trailheads/raw_client.py",
        "from ..core.pydantic_utilities import parse_obj_as\n",
        "",
    );
}

/// A binary alternative makes the success a download that hoists no model.
#[test]
fn a_binary_alternative_hoists_no_response_model() {
    holds_without(
        "success-media-binary-before-json",
        "src/fern/specimens/types/render_scan_response.py",
        "from ...core.pydantic_utilities import UniversalBaseModel\n\n\nclass RenderScanResponse(UniversalBaseModel):\n    specimen_id: str\n",
    );
}

/// A `207`-only operation returns nothing.
#[test]
fn a_multi_status_only_operation_returns_nothing() {
    holds(
        "multi-status-success-return-type",
        "src/fern/harvests/client.py",
        "    ) -> None:\n",
        "    ) -> BatchOutcome:\n",
    );
}

/// A `nullable: true` error component is an optional error body.
#[test]
fn a_nullable_error_component_is_an_optional_body() {
    holds(
        "R5",
        "src/fern/errors/not_found_error.py",
        "body: typing.Optional[LockFault]",
        "body: LockFault",
    );
}

/// A multipart form with no field still sends `data={}`, its component gets no
/// model, a comma list's first media type is the file's default, and a union of
/// form primitives is sent as is.
#[test]
fn multipart_parts_take_fern_encodings() {
    holds(
        "multipart-empty-body",
        "src/fern/queue/raw_client.py",
        "            data={},\n",
        "",
    );
    holds(
        "multipart-encoding-content-type-list",
        "src/fern/plates/raw_client.py",
        "default_content_type=\"image/png\")",
        "default_content_type=\"image/png, image/jpeg, image/tiff\")",
    );
    holds(
        "multipart-scalar-union-part-encoding",
        "src/fern/scans/raw_client.py",
        "\"drawer\": drawer,",
        "\"drawer\": json.dumps(jsonable_encoder(drawer)),",
    );
}

/// A path union with a `uint64` member is converted before it is encoded.
#[test]
fn a_path_union_outside_the_data_primitives_is_converted() {
    holds(
        "path-param-serialization",
        "src/fern/blocks/raw_client.py",
        "encode_path_param(convert_and_respect_annotation_metadata(object_=id, annotation=GetBlockRequestId, direction='write'))",
        "encode_path_param(id)",
    );
}

/// A bytes body beside a JSON alternative documents the bytes it takes, and the
/// alternative's model survives.
#[test]
fn a_bytes_body_documents_bytes() {
    holds(
        "reference-body-param-doc",
        "reference.md",
        "**request:** `typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]`",
        "**request:** `ScoreSubmission`",
    );
}

/// A component posted once under `*/*` is inlined: its properties are
/// documented and it gets no model.
#[test]
fn a_single_use_wildcard_body_is_inlined() {
    holds(
        "request-body-spread-vs-request",
        "reference.md",
        "**apiary:** `str` — The apiary the hive stands in.",
        "**request:** `HiveRegistration`",
    );
}

/// A `required: false` closed empty object is a required `request`.
#[test]
fn an_optional_closed_empty_body_is_required() {
    holds(
        "request-body-optionality",
        "src/fern/lamps/client.py",
        "request: typing.Dict[str, typing.Any], request_options",
        "request: typing.Optional[typing.Dict[str, typing.Any]] = None, request_options",
    );
}

/// An `allOf` member carrying its own `anyOf` adds nothing to the body.
#[test]
fn an_any_of_all_of_member_adds_no_body_property() {
    holds(
        "body-property-set",
        "src/fern/dispatches/client.py",
        "        *,\n        parcel: str,\n",
        "        *,\n        route: str,\n        parcel: str,\n",
    );
}

/// Each measurement document is generated from as committed: removing it is an
/// actionable failure that writes no SDK.
#[test]
fn a_missing_measurement_document_fails_without_writing() {
    let temp = tempfile::tempdir().expect("output tempdir");
    let out = temp.path().join("sdk");
    probe_command(&temp.path().join("absent").join("openapi.yml"), &out)
        .assert()
        .failure()
        .stderr(predicate::str::contains("could not read spec"));
    assert!(!out.exists(), "a missing document writes no SDK");
}
// llmlint: ignore-end[expensive_tests_stay_behind_their_own_edge]

/// The causes whose verdict rests on what goes over the wire.
const WIRE_CAUSES: [&str; 6] = [
    "request-content-type-header",
    "media-type-recognition",
    "multipart-empty-body",
    "multipart-scalar-union-part-encoding",
    "streaming-detection",
    "geo-json-success-media",
];

fn wire(python: &Path, cause: &str, src: &Path) -> std::process::Output {
    std::process::Command::new(python)
        .arg(repo_root().join(WIRE))
        .arg(cause)
        .arg(src)
        .env("PYTHONDONTWRITEBYTECODE", "1")
        .output()
        .expect("run the wire journey")
}

// llmlint: ignore-block[expensive_tests_stay_behind_their_own_edge] This `sdk_env_*` journey runs only in the `sdk-env` project (tests/sdk_env/project.json: `tier:promoted`, `cache: false`), promoted out of the affected tier into its own required CI leg; crates/crozier-e2e/AGENTS.md makes `#[ignore]` the one mechanism that routes a journey to that project.
/// Both generated SDKs of each wire cause, crozier's and the certified pair's,
/// call a local HTTP server and send and return the same things, the ones each
/// measurement's `runtime.txt` records: the `text/json` and vendor content types
/// verbatim, a wildcard body as plain JSON, an empty multipart form, a union part
/// as its bare value, a stream's parsed events and a GeoJSON model. An SDK
/// directory without the package is refused with exit 2.
#[test]
#[ignore = "SDK Python-environment tier (builds a venv from PyPI, runs mypy/pytest); run via `just test-sdk-env`"]
fn sdk_env_bodies_media_wire_journeys_hold_for_crozier_and_fern() {
    let python = runtime_python_env().expect("SDK runtime environment");
    let work = tempfile::tempdir().expect("work dir");
    let missing = wire(&python, WIRE_CAUSES[0], &work.path().join("absent"));
    assert_eq!(missing.status.code(), Some(2), "{missing:?}");
    assert!(
        String::from_utf8_lossy(&missing.stderr)
            .contains("must contain the generated fern package"),
        "{missing:?}"
    );
    for cause in WIRE_CAUSES {
        let out = work.path().join(cause);
        generate(cause, &out);
        let mut lines = Vec::new();
        for src in [case_dir(cause).join("fern-expected/src"), out.join("src")] {
            let run = wire(&python, cause, &src);
            assert!(
                run.status.success(),
                "{cause} over {}: {}{}",
                src.display(),
                String::from_utf8_lossy(&run.stdout),
                String::from_utf8_lossy(&run.stderr)
            );
            lines.push(String::from_utf8(run.stdout).expect("UTF-8 output"));
        }
        assert_eq!(
            lines[0], lines[1],
            "{cause}: crozier's SDK sends or returns otherwise"
        );
        let recorded = std::fs::read_to_string(case_dir(cause).join("runtime.txt"))
            .expect("the cause's runtime record");
        for line in lines[0].lines() {
            assert!(
                recorded.contains(line),
                "{cause}: runtime.txt does not record {line}"
            );
        }
    }
    let content_types = String::from_utf8(
        wire(
            &python,
            "request-content-type-header",
            &work.path().join("request-content-type-header/src"),
        )
        .stdout,
    )
    .expect("UTF-8 output");
    for expected in [
        "\"content-type\": \"application/vnd.foundry.inscription+json\"",
        "\"step\": \"tune_bell\"",
    ] {
        assert!(
            content_types.contains(expected),
            "{expected}: {content_types}"
        );
    }
}
// llmlint: ignore-end[expensive_tests_stay_behind_their_own_edge]
