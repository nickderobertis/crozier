//! The two union shapes of ingef/conquery's document, each in a from-scratch
//! document held whole to its certified-pair tree in both enum modes, beside
//! its control. The shapes and their repairs are recorded in
//! `docs/fern-measurements/emission-parity/README.md`.

use std::path::{Path, PathBuf};

use predicates::prelude::*;

use super::{departure_ledger, golden_tree_failures, probe_command, repo_root, runtime_python_env};

/// Where the measurements live; each case's `fern-expected/` is a compared golden.
pub(crate) const EMISSION_PARITY_DIR: &str = "docs/fern-measurements/emission-parity";
const ALLOF_ONLY_BASE: &str = "allof-only-base";
const DANGLING_TARGET: &str = "dangling-mapping-target";
const WIRE: &str = "crates/crozier-e2e/tests/e2e/dangling_mapping_wire.py";
const CONQUERY_WIRE: &str = "crates/crozier-e2e/tests/e2e/conquery_secondary_id_wire.py";
/// Corpus row 3477's committed source and its certified-pair golden.
const CONQUERY_SPEC: &str = "tests/fixtures/corpus-sources/ingef-conquery/openapi.yaml";
const CONQUERY_GOLDEN: &str = "tests/fixtures/ingef-conquery/expected";

fn spec(case: &str) -> PathBuf {
    repo_root()
        .join(EMISSION_PARITY_DIR)
        .join(case)
        .join("openapi.yml")
}

fn generate(case: &str, mode: &str, out: &Path) {
    probe_command(&spec(case), out)
        .args(["--enum-type", mode])
        .assert()
        .success();
}

fn golden(case: &str, mode: &str) -> String {
    let suffix = if mode == "literals" { "-literals" } else { "" };
    format!("{EMISSION_PARITY_DIR}/{case}{suffix}/fern-expected")
}

/// crozier's SDK for `case` in `mode` against its certified-pair tree, apart
/// from the departures the ledger records for it.
fn failures(case: &str, mode: &str, out: &Path) -> Vec<String> {
    let golden = golden(case, mode);
    let ledger = departure_ledger()
        .golden(&golden, &[])
        .unwrap_or_else(|failures| panic!("{}", failures.join("\n")));
    golden_tree_failures(
        &format!("{case} ({mode})"),
        &spec(case).display().to_string(),
        &ledger,
        &repo_root().join(&golden),
        out,
    )
}

fn module(out: &Path, name: &str) -> String {
    std::fs::read_to_string(out.join("src/fern/types").join(name)).expect("the generated module")
}

// llmlint: ignore-block[expensive_tests_stay_behind_their_own_edge] Each of these journeys generates one small SDK through the binary, on the crozier-e2e edge every other golden comparison shares; splitting that edge is the drafted follow-up "Give crozier-e2e's generator-replay journeys an Nx edge narrower than e2eReads".
/// Every wrapper carries the fields its variant inherits through an
/// `allOf`-only base, and the SDK is Fern's file for file in both enum modes.
/// Written as crozier wrote it before the repair, without them, the
/// comparison names `sensor.py`.
#[test]
fn a_variant_inherits_fields_through_an_all_of_only_base() {
    for mode in ["python-enums", "literals"] {
        let temp = tempfile::tempdir().expect("output tempdir");
        let out = temp.path().join("sdk");
        generate(ALLOF_ONLY_BASE, mode, &out);
        let found = failures(ALLOF_ONLY_BASE, mode, &out);
        assert!(found.is_empty(), "{mode}: {}", found.join("\n\n"));
        let sensor = module(&out, "sensor.py");
        let thermo = sensor
            .split("class Sensor_")
            .find(|class| class.starts_with("Thermo("))
            .expect("Sensor_Thermo");
        for field in ["celsius:", "unit:", "precision:", "name: str", "label:"] {
            assert!(
                thermo.contains(field),
                "{mode}: Sensor_Thermo lacks {field}:\n{thermo}"
            );
        }
        let wind = sensor
            .split("class Sensor_")
            .find(|class| class.starts_with("Wind("))
            .expect("Sensor_Wind");
        for field in [
            "heading:",
            "degrees:",
            "compass_point:",
            "calibrated_on:",
            "name: str",
        ] {
            assert!(
                wind.contains(field),
                "{mode}: Sensor_Wind lacks {field}:\n{wind}"
            );
        }
        std::fs::write(
            out.join("src/fern/types/sensor.py"),
            sensor.replacen("    name: str\n", "", 1),
        )
        .unwrap();
        let unexplained = failures(ALLOF_ONLY_BASE, mode, &out);
        assert!(
            unexplained
                .iter()
                .any(|failure| failure.contains("src/fern/types/sensor.py")),
            "{mode}: a wrapper missing an inherited field must fail: {unexplained:?}"
        );
    }
}

/// The union is Fern's discriminated union of wrappers in both enum modes, and
/// the one `METEOR` wrapper is the departure the ledger records: it carries
/// `MeteorReading`'s fields. Any other change to that module is unexplained.
#[test]
fn a_mapping_target_naming_no_schema_keeps_fern_s_union_but_its_wrapper_s_fields() {
    for mode in ["python-enums", "literals"] {
        let temp = tempfile::tempdir().expect("output tempdir");
        let out = temp.path().join("sdk");
        generate(DANGLING_TARGET, mode, &out);
        let found = failures(DANGLING_TARGET, mode, &out);
        assert!(found.is_empty(), "{mode}: {}", found.join("\n\n"));
        let reading = module(&out, "reading.py");
        let meteor = reading
            .split("class Reading_")
            .find(|class| class.starts_with("Meteor("))
            .expect("Reading_Meteor");
        assert!(!meteor.contains("value: typing.Any"), "{mode}: {meteor}");
        for field in ["trail:", "brightness:"] {
            assert!(
                meteor.contains(field),
                "{mode}: Reading_Meteor lacks {field}:\n{meteor}"
            );
        }
        // The member keeps its own tag, as Fern's model does.
        assert!(module(&out, "meteor_reading.py").contains("kind: typing.Optional["));
        std::fs::write(
            out.join("src/fern/types/reading.py"),
            reading.replacen("brightness:", "luminosity:", 1),
        )
        .unwrap();
        let unexplained = failures(DANGLING_TARGET, mode, &out);
        assert!(
            unexplained
                .iter()
                .any(|failure| failure.contains("src/fern/types/reading.py")),
            "{mode}: a change the departure does not describe must fail: {unexplained:?}"
        );
    }
}

fn variant_of(case: &str, from: &str, to: &str, dir: &Path) -> PathBuf {
    let text = std::fs::read_to_string(spec(case)).expect("the measurement document");
    assert!(text.contains(from), "{case}: no {from:?} to replace");
    let path = dir.join(format!("{case}.yml"));
    std::fs::write(&path, text.replacen(from, to, 1)).unwrap();
    path
}

/// One class of a comment-stripped module, from its header to the next
/// top-level statement.
fn class_block(module: &str, class: &str) -> String {
    let text = crozier::normalize::strip_python_comments(module);
    let start = text
        .find(&format!("class {class}("))
        .unwrap_or_else(|| panic!("no class {class} in:\n{text}"));
    let rest = &text[start..];
    let end = rest[1..]
        .find("\n\n\n")
        .map_or(rest.len(), |index| index + 1);
    rest[..end]
        .lines()
        .map(str::trim_end)
        .collect::<Vec<_>>()
        .join("\n")
}

/// With no member tagging itself `METEOR`, crozier has no fields to give the
/// dangling value's wrapper and writes Fern's own: the certified tree's
/// `Reading_Meteor` reads no member either (it holds `value` though
/// `MeteorReading` tags itself `METEOR`), and crozier's class is that class
/// line for line, docstring left off, in both enum modes.
#[test]
fn a_dangling_target_no_member_tags_keeps_fern_s_value_wrapper() {
    let temp = tempfile::tempdir().expect("output tempdir");
    let untagged = variant_of(
        DANGLING_TARGET,
        "enum: [METEOR]",
        "enum: [SHOOTING_STAR]",
        temp.path(),
    );
    for mode in ["python-enums", "literals"] {
        let out = temp.path().join(mode);
        probe_command(&untagged, &out)
            .args(["--enum-type", mode])
            .assert()
            .success();
        let fern = std::fs::read_to_string(
            repo_root()
                .join(golden(DANGLING_TARGET, mode))
                .join("src/fern/types/reading.py"),
        )
        .unwrap();
        assert_eq!(
            class_block(&module(&out, "reading.py"), "Reading_Meteor"),
            class_block(&fern, "Reading_Meteor"),
            "{mode}"
        );
    }
}

/// A base chain that reaches back to itself (`Named` an `allOf` over `Gauge`,
/// which is an `allOf` over `Named`) generates, and each wrapper over it lists
/// every field of the chain once.
#[test]
fn a_cyclic_all_of_base_chain_generates_each_field_once() {
    let temp = tempfile::tempdir().expect("output tempdir");
    let cyclic = variant_of(
        ALLOF_ONLY_BASE,
        "    Named:\n      type: object\n",
        "    Named:\n      allOf:\n        - $ref: '#/components/schemas/Gauge'\n",
        temp.path(),
    );
    let out = temp.path().join("sdk");
    probe_command(&cyclic, &out).assert().success();
    let thermo = class_block(&module(&out, "sensor.py"), "Sensor_Thermo");
    let fields: Vec<&str> = thermo
        .lines()
        .filter_map(|line| line.strip_prefix("    "))
        .filter(|line| !line.starts_with([' ', '"']) && line.contains(':'))
        .map(|line| line.split_once(':').unwrap().0)
        .filter(|name| !name.starts_with("if ") && *name != "else")
        .collect();
    assert_eq!(
        fields,
        ["kind", "celsius", "unit", "precision", "name", "label"],
        "{thermo}"
    );
}
// llmlint: ignore-end[expensive_tests_stay_behind_their_own_edge]

fn wire(python: &Path, sdk_src: &Path) -> assert_cmd::Command {
    journey(WIRE, python, sdk_src)
}

fn journey(script: &str, python: &Path, sdk_src: &Path) -> assert_cmd::Command {
    let mut command = assert_cmd::Command::new(python);
    command
        .arg(repo_root().join(script))
        .arg(sdk_src)
        .env("PYTHONDONTWRITEBYTECODE", "1");
    command
}

// llmlint: ignore-block[expensive_tests_stay_behind_their_own_edge] This `sdk_env_*` journey runs only in the `sdk-env` project (tests/sdk_env/project.json: `tier:promoted`, `cache: false`), promoted out of the affected tier into its own required CI leg; crates/crozier-e2e/AGENTS.md makes `#[ignore]` the one mechanism that routes a journey to that project.
/// Through the real client, against a local HTTP server: crozier's SDK, in
/// either enum mode, parses a `METEOR` reading into `Reading_Meteor` with the
/// meteor's fields and posts it back as the server sent it, beside the `STAR`
/// control. The certified tree's `value: typing.Any` wrapper raises on the
/// same response, which is the defect the departure corrects.
pub(crate) fn dangling_mapping_variant_round_trips_through_the_client() {
    let python = runtime_python_env().expect("SDK runtime environment");
    let work = tempfile::tempdir().unwrap();
    wire(&python, work.path())
        .assert()
        .code(2)
        .stderr(predicate::str::contains(
            "must contain the generated fern package",
        ));
    for mode in ["python-enums", "literals"] {
        let out = work.path().join(mode);
        generate(DANGLING_TARGET, mode, &out);
        wire(&python, &out.join("src"))
            .assert()
            .success()
            .stdout(predicate::str::contains(
                "METEOR: parsed into Reading_Meteor and posted back as \
                 {\"brightness\": -3.5, \"kind\": \"METEOR\", \"trail\": {\"colour\": \"green\", \"degrees\": 12.0}}",
            ))
            .stdout(predicate::str::contains("STAR: parsed into Reading_Star"));
    }
    wire(
        &python,
        &repo_root()
            .join(golden(DANGLING_TARGET, "python-enums"))
            .join("src"),
    )
    .assert()
    .code(1)
    .stdout(predicate::str::contains("STAR: parsed into Reading_Star"))
    .stderr(predicate::str::contains(
        "METEOR: reading the entry raised ParsingError",
    ))
    .stderr(predicate::str::contains("reading.METEOR.value"));
}
// llmlint: ignore-end[expensive_tests_stay_behind_their_own_edge]

// llmlint: ignore-block[expensive_tests_stay_behind_their_own_edge] This `sdk_env_*` journey runs only in the `sdk-env` project (tests/sdk_env/project.json: `tier:promoted`, `cache: false`), promoted out of the affected tier into its own required CI leg; crates/crozier-e2e/AGENTS.md makes `#[ignore]` the one mechanism that routes a journey to that project.
/// The same defect on the exact registered conquery document, through the
/// client generated from it, against a local HTTP server: in either enum mode,
/// a `SECONDARY_ID_QUERY` status parses into `Query_SecondaryIdQuery` with
/// `SecondaryIdQuery`'s `secondary_id` and `date_aggregation_mode`, and posting
/// that query back sends the server exactly the payload it answered, beside the
/// `CONCEPT_QUERY` control. The certified golden's client raises on the same
/// response, at the `value` its wrapper requires.
pub(crate) fn conquery_secondary_id_query_round_trips_through_the_client() {
    let python = runtime_python_env().expect("SDK runtime environment");
    let work = tempfile::tempdir().unwrap();
    journey(CONQUERY_WIRE, &python, work.path())
        .assert()
        .code(2)
        .stderr(predicate::str::contains(
            "must contain the generated fern package",
        ));
    for mode in ["python-enums", "literals"] {
        let out = work.path().join(mode);
        probe_command(&repo_root().join(CONQUERY_SPEC), &out)
            .args(["--enum-type", mode])
            .assert()
            .success();
        journey(CONQUERY_WIRE, &python, &out.join("src"))
            .assert()
            .success()
            .stdout(predicate::str::contains(
                "SECONDARY_ID_QUERY: parsed into Query_SecondaryIdQuery and posted back as \
                 {\"dateAggregationMode\": \"MERGE\", \"secondaryId\": \"dataset.sid\", \"type\": \"SECONDARY_ID_QUERY\"}",
            ))
            .stdout(predicate::str::contains(
                "CONCEPT_QUERY: parsed into Query_ConceptQuery",
            ));
    }
    journey(
        CONQUERY_WIRE,
        &python,
        &repo_root().join(CONQUERY_GOLDEN).join("src"),
    )
    .assert()
    .code(1)
    .stdout(predicate::str::contains(
        "CONCEPT_QUERY: parsed into Query_ConceptQuery",
    ))
    .stderr(predicate::str::contains(
        "SECONDARY_ID_QUERY: reading the status raised ParsingError",
    ))
    .stderr(predicate::str::contains("query.SECONDARY_ID_QUERY.value"));
}
// llmlint: ignore-end[expensive_tests_stay_behind_their_own_edge]
