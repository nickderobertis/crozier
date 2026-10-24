//! The model and union shapes the `models-unions-refs` removal controls first
//! showed crozier departing from the certified pair on, each driven through the
//! real binary over one minimal document Fern generated `fern-expected/` from:
//! crozier's complete SDK must equal Fern's, the line that shape decides must
//! read as Fern writes it in both trees, and crozier's tree with that line put
//! back the way crozier used to write it must fail the comparison.

use std::path::Path;

use predicates::prelude::*;

use super::{
    certified_pair, departure_ledger, golden_tree_failures, probe_artifact_digest, probe_command,
    repo_root, sha256_hex,
};

const CASE: &str = "docs/fern-measurements/schema-shapes/pottery-studio-shapes";

/// The comparison failures of crozier's tree at `out` against Fern's.
fn failures(out: &Path) -> Vec<String> {
    let golden = format!("{CASE}/fern-expected");
    let ledger = departure_ledger()
        .golden(&golden, &[])
        .unwrap_or_else(|failures| panic!("{}", failures.join("\n")));
    let spec = repo_root().join(CASE).join("openapi.yml");
    golden_tree_failures(
        "pottery-studio-shapes",
        &spec.display().to_string(),
        &ledger,
        &repo_root().join(&golden),
        out,
    )
}

// llmlint: ignore-block[expensive_tests_stay_behind_their_own_edge] Each journey below generates one small SDK and compares it whole, on the crozier-e2e edge every other golden comparison shares; splitting that edge is the drafted follow-up "Give crozier-e2e's generator-replay journeys an Nx edge narrower than e2eReads".
/// Generate the case's SDK, hold it whole to Fern's, then show that `file`
/// spelling `fern` (as both trees do) is what the comparison turns on: with
/// `crozier` in its place the comparison names `file`.
fn holds_line(file: &str, fern: &str, crozier: &str) {
    let temp = tempfile::tempdir().expect("output tempdir");
    let out = temp.path().join("sdk");
    probe_command(&repo_root().join(CASE).join("openapi.yml"), &out)
        .assert()
        .success();
    let matched = failures(&out);
    assert!(matched.is_empty(), "{}", matched.join("\n\n"));
    let expected = repo_root().join(CASE).join("fern-expected").join(file);
    for tree in [expected.as_path(), out.join(file).as_path()] {
        let text = std::fs::read_to_string(tree)
            .unwrap_or_else(|error| panic!("{}: {error}", tree.display()));
        assert!(text.contains(fern), "{}: no {fern:?}", tree.display());
    }
    let generated = out.join(file);
    let text = std::fs::read_to_string(&generated).unwrap();
    std::fs::write(&generated, text.replacen(fern, crozier, 1)).unwrap();
    let unexplained = failures(&out);
    assert!(
        unexplained.iter().any(|failure| failure.contains(file)),
        "{file} written as {crozier:?} must fail the comparison: {unexplained:?}"
    );
}

/// The case's provenance is the certified pair and the committed bytes, and a
/// missing document is an actionable failure that writes nothing.
#[test]
fn pottery_studio_shapes_evidence_pins_the_certified_tree() {
    let case = repo_root().join(CASE);
    let evidence = std::fs::read_to_string(case.join("evidence.toml")).unwrap();
    for field in [
        format!("fern_cli_version = \"{}\"", certified_pair().cli),
        format!(
            "fern_python_sdk_version = \"{}\"",
            certified_pair().python_sdk
        ),
        format!(
            "digest = \"{}\"",
            probe_artifact_digest(&case.join("fern-expected")).unwrap()
        ),
        format!(
            "source_digest = \"{}\"",
            sha256_hex(&std::fs::read(case.join("openapi.yml")).unwrap())
        ),
    ] {
        assert!(evidence.contains(&field), "{CASE}: missing {field}");
    }
    let temp = tempfile::tempdir().unwrap();
    let out = temp.path().join("sdk");
    probe_command(&temp.path().join("openapi.yml"), &out)
        .assert()
        .failure()
        .stderr(predicate::str::contains("could not read spec"));
    assert!(!out.exists(), "a missing document writes no SDK");
}

/// An inline request-body union whose members tag themselves keeps the JSON
/// content-type header though it writes no `discriminator`.
#[test]
fn a_self_tagged_union_body_keeps_the_content_type_header() {
    holds_line(
        "src/fern/batches/raw_client.py",
        "            headers={\n                \"content-type\": \"application/json\",\n            },\n",
        "",
    );
}

/// A `discriminator` beside an `anyOf` is read as though unwritten, so the
/// members' typed tags are dropped from their models.
#[test]
fn a_discriminator_beside_any_of_strips_the_typed_member_tags() {
    holds_line(
        "src/fern/types/cooled.py",
        "class Cooled(UniversalBaseModel):\n    hours: int\n",
        "class Cooled(UniversalBaseModel):\n    outcome: CooledOutcome\n    hours: int\n",
    );
}

/// A lone tagged member under a written `discriminator` is a plain model
/// keeping its tag field, not a one-variant discriminated union.
#[test]
fn a_lone_tagged_member_is_a_plain_model() {
    holds_line(
        "src/fern/types/firing_booking_shelf.py",
        "class FiringBookingShelf(UniversalBaseModel):\n    level: FiringBookingShelfLevel\n",
        "class FiringBookingShelf_Upper(UniversalBaseModel):\n    level: typing.Literal[\"upper\"] = \"upper\"\n",
    );
}

/// The description beside the one-member union is lost with it on the
/// required field.
#[test]
fn a_lone_member_unions_description_is_lost_on_the_required_field() {
    holds_line(
        "src/fern/types/firing_booking.py",
        "    shelf: FiringBookingShelf\n",
        "    shelf: FiringBookingShelf = pydantic.Field()\n    \"\"\"\n    Where the load sits in the kiln.\n    \"\"\"\n\n",
    );
}

/// An `allOf` of one scalar `$ref` beside a `default` aliases the referenced
/// component, not the bare scalar.
#[test]
fn a_lone_scalar_reference_aliases_the_component() {
    holds_line(
        "src/fern/types/target_cone.py",
        "TargetCone = ConeNumber\n",
        "TargetCone = int\n",
    );
}

/// An operation description of several lines keeps its opening indentation in
/// the method docstring and in `reference.md`.
#[test]
fn a_several_line_operation_description_keeps_its_indentation() {
    holds_line(
        "src/fern/firings/client.py",
        "            Books a slot on the shared kiln.\n",
        "        Books a slot on the shared kiln.\n",
    );
    holds_line(
        "reference.md",
        "    Books a slot on the shared kiln.\n",
        "Books a slot on the shared kiln.\n",
    );
}

/// A required property `allOf` around one array is that array, undocumented.
#[test]
fn an_all_of_around_one_array_is_that_array() {
    holds_line(
        "src/fern/types/firing_booking.py",
        "    palette: typing.List[str]\n",
        "    palette: FiringBookingPalette\n",
    );
}
// llmlint: ignore-end[expensive_tests_stay_behind_their_own_edge]
