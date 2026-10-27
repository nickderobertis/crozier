//! Union shapes from ingef/conquery's `openapi.yaml` that crozier generated
//! differently from the certified pair, each in a from-scratch document held
//! whole to its certified-pair tree in both enum modes
//! (`docs/fern-measurements/emission-parity/`, recorded in its `README.md`).
//!
//! - `allof-only-base`: a union variant that is `allOf: [$ref Base, {…}]`,
//!   where `Base` is itself only an `allOf` over another `$ref`, an inline
//!   member or an inline union. Fern's wrapper carries every field the chain
//!   declares; the variant over a base with direct `properties` is the control.
//! - `dangling-mapping-target`: a discriminator mapping whose `METEOR` target
//!   names no component, beside targets that do. Fern writes the union's
//!   wrappers, and crozier matches every line but the `METEOR` wrapper's, which
//!   carries the tagged member's fields where Fern's holds `value: typing.Any`
//!   (the `dangling-mapping-variant-fields` departure). `Instrument`, whose
//!   targets all resolve, is the control.

use std::path::{Path, PathBuf};

use predicates::prelude::*;

use super::{departure_ledger, golden_tree_failures, probe_command, repo_root, runtime_python_env};

/// Where the measurements live; each case's `fern-expected/` is a compared golden.
pub(crate) const EMISSION_PARITY_DIR: &str = "docs/fern-measurements/emission-parity";
const ALLOF_ONLY_BASE: &str = "allof-only-base";
const DANGLING_TARGET: &str = "dangling-mapping-target";
const WIRE: &str = "crates/crozier-e2e/tests/e2e/dangling_mapping_wire.py";

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

/// The case's golden for `mode`: `<case>/` under `python-enums`,
/// `<case>-literals/` under `literals`.
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

// llmlint: ignore-end[expensive_tests_stay_behind_their_own_edge]

fn wire(python: &Path, sdk_src: &Path) -> assert_cmd::Command {
    let mut command = assert_cmd::Command::new(python);
    command
        .arg(repo_root().join(WIRE))
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
#[test]
#[ignore = "SDK Python-environment tier (builds a venv from PyPI, runs mypy/pytest); run via `just test-sdk-env`"]
fn sdk_env_a_dangling_mapping_variant_round_trips_through_the_client() {
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
