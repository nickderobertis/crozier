//! The shapes behind RS-Server's and ingef/conquery's emission differences,
//! each in a document written for it, held whole against the certified pair's
//! tree in both enum modes (`docs/fern-measurements/emission-parity/`).
//!
//! - `survey-shapes`, `tide-windows`, `lantern-open-ping`: RS-Server's causes,
//!   recorded in `docs/rs-server-emission-parity.md`.
//! - `allof-only-base`, `dangling-mapping-target`, `unaffected-control`:
//!   conquery's two union shapes, each beside its control, recorded in
//!   `docs/fern-measurements/emission-parity/README.md`.

use std::path::{Path, PathBuf};

use predicates::prelude::*;

use super::{
    crozier_clean_env, departure_ledger, golden_tree_failures, probe_command, repo_root,
    runtime_python_env, sha256_hex,
};

/// Where the measurements live; each case's `fern-expected/` is a compared golden.
pub(crate) const EMISSION_PARITY_DIR: &str = "docs/fern-measurements/emission-parity";
const ALLOF_ONLY_BASE: &str = "allof-only-base";
const DANGLING_TARGET: &str = "dangling-mapping-target";
/// A document of neither shape, held to the base's tree rather than Fern's.
const UNAFFECTED_CONTROL: &str = "unaffected-control";
const WIRE: &str = "crates/crozier-e2e/tests/e2e/dangling_mapping_wire.py";
const CONQUERY_WIRE: &str = "crates/crozier-e2e/tests/e2e/conquery_secondary_id_wire.py";
/// Corpus row 3478's committed source and its certified-pair golden.
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

fn assert_dangling_rule_abstains(comparison: &crozier::parity::TreeComparison, path: &str) {
    assert!(
        comparison.differences.iter().any(|(name, _)| name == path),
        "the unexpected SDK change at {path} was hidden: {comparison:?}"
    );
    assert!(
        !comparison.departures.iter().any(|departure| {
            departure.file == path && departure.id == "dangling-mapping-variant-fields"
        }),
        "the rule claimed an unrelated SDK change: {comparison:?}"
    );
}

/// The public tree-comparison boundary used by `compare` must recognize only
/// the declared Python wrapper. Corrupted SDK files remain differences; valid
/// forward-reference and import uses survive the wrapper rewrite.
#[test]
fn dangling_mapping_departure_respects_source_scope_and_wrapper_structure() {
    const MODULE: &str = "src/fern/types/reading.py";
    const WRAPPER: &str = "Reading_Meteor";
    for mode in ["python-enums", "literals"] {
        let temp = tempfile::tempdir().expect("comparison tempdir");
        let generated = temp.path().join("generated");
        generate(DANGLING_TARGET, mode, &generated);
        let reference = repo_root().join(golden(DANGLING_TARGET, mode));
        let source = spec(DANGLING_TARGET);
        let compare = |reference: &Path, generated: &Path| {
            crozier::parity::compare_trees_with_document(
                reference,
                generated,
                None,
                true,
                Some(crozier::openapi::load(&source).unwrap()),
            )
            .expect("real SDK trees can be compared")
        };
        let baseline = compare(&reference, &generated);
        assert!(baseline.differences.is_empty(), "{mode}: {baseline:?}");
        assert!(baseline.departures.iter().any(|departure| {
            departure.file == MODULE && departure.id == "dangling-mapping-variant-fields"
        }));

        let without_source =
            crozier::parity::compare_trees(&reference, &generated, None, true).unwrap();
        assert_dangling_rule_abstains(&without_source, MODULE);

        let original = module(&generated, "reading.py");
        let reference_module = std::fs::read_to_string(reference.join(MODULE)).unwrap();
        let text_reference = temp.path().join("text-reference");
        let text_generated = temp.path().join("text-generated");
        super::copy_dir(&reference, &text_reference);
        super::copy_dir(&generated, &text_generated);
        let text_path = "src/fern/types/reading.txt";
        for (root, content) in [
            (&text_reference, &reference_module),
            (&text_generated, &original),
        ] {
            std::fs::write(
                root.join(text_path),
                crozier::normalize::strip_python_comments(content),
            )
            .unwrap();
        }
        assert_dangling_rule_abstains(&compare(&text_reference, &text_generated), text_path);

        let class = original.find(&format!("class {WRAPPER}(")).unwrap();
        let config = class + original[class..].find("    if IS_PYDANTIC_V2:").unwrap();
        let opening = class + original[class..].find("    \"\"\"").unwrap();
        let closing = opening
            + "    \"\"\"".len()
            + original[opening + "    \"\"\"".len()..]
                .find("    \"\"\"")
                .unwrap();
        let mut unclosed_docstring = original.clone();
        unclosed_docstring.replace_range(closing..closing + "    \"\"\"".len(), "    \"\"");
        let tag = "kind: typing.Literal[\"METEOR\"] = \"METEOR\"";
        assert!(original[class..].contains(tag));
        let mut missing_config = original.clone();
        missing_config.replace_range(config..config + "    if IS_PYDANTIC_V2:".len(), "");
        for (name, changed) in [
            ("truncated", original[..config].to_owned()),
            ("unclosed-docstring", unclosed_docstring),
            ("missing-config", missing_config),
            (
                "wrong-tag",
                original.replacen(tag, "kind: typing.Literal[\"COMET\"] = \"COMET\"", 1),
            ),
        ] {
            let edited = temp.path().join(name);
            super::copy_dir(&generated, &edited);
            std::fs::write(edited.join(MODULE), changed).unwrap();
            assert_dangling_rule_abstains(&compare(&reference, &edited), MODULE);
        }

        let single = temp.path().join("single-forward-reference");
        super::copy_dir(&generated, &single);
        // A harmless rebuild is a valid post-processing step on a generated SDK.
        // It must not leave an unused helper import after the Any-wrapper rewrite.
        assert!(!original.contains("update_forward_refs"));
        let future = "from __future__ import annotations\n";
        assert!(original.contains(future));
        let mut one_line = original.replacen(
            future,
            &format!("{future}from ..core.pydantic_utilities import update_forward_refs\n"),
            1,
        );
        one_line.push_str(&format!("\nupdate_forward_refs({WRAPPER})\n"));
        std::fs::write(single.join(MODULE), one_line).unwrap();
        let compared = compare(&reference, &single);
        assert!(compared.differences.is_empty(), "{mode}: {compared:?}");

        let kept_reference = temp.path().join("kept-import-reference");
        let kept_generated = temp.path().join("kept-import-generated");
        super::copy_dir(&reference, &kept_reference);
        super::copy_dir(&generated, &kept_generated);
        let import = "from .trail import Trail";
        let import_at = original.find(import).unwrap();
        assert!(!reference_module.lines().any(|line| line == import));
        let anchor = original[..import_at]
            .lines()
            .rev()
            .find(|line| !line.is_empty() && reference_module.lines().any(|other| other == *line))
            .unwrap();
        let reference_with_import =
            reference_module.replacen(&format!("{anchor}\n"), &format!("{anchor}\n{import}\n"), 1);
        let extension = "\n\ndef retained_trail(value: Trail) -> Trail:\n    return value\n";
        for (root, content) in [
            (&kept_reference, reference_with_import),
            (&kept_generated, original.clone()),
        ] {
            std::fs::write(root.join(MODULE), content + extension).unwrap();
        }
        let compared = compare(&kept_reference, &kept_generated);
        assert!(compared.differences.is_empty(), "{mode}: {compared:?}");
    }
}

fn variant_of(case: &str, name: &str, edits: &[(&str, &str)], dir: &Path) -> PathBuf {
    let mut text = std::fs::read_to_string(spec(case)).expect("the measurement document");
    for (from, to) in edits {
        assert!(text.contains(from), "{case}: no {from:?} to replace");
        text = text.replacen(from, to, 1);
    }
    let path = dir.join(format!("{name}.yml"));
    std::fs::write(&path, text).unwrap();
    path
}

const METEOR_MEMBER: &str = "        - $ref: '#/components/schemas/MeteorReading'\n";

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

/// With no one member to stand for `METEOR`, because none tags itself so or
/// two do, crozier has no fields to give the dangling value's wrapper and
/// writes Fern's own: the certified tree's `Reading_Meteor` reads no member
/// either (it holds `value` though `MeteorReading` tags itself `METEOR`), and
/// crozier's class is that class line for line, docstring left off, in both
/// enum modes.
#[test]
fn a_dangling_target_no_single_member_tags_keeps_fern_s_value_wrapper() {
    let temp = tempfile::tempdir().expect("output tempdir");
    let untagged = variant_of(
        DANGLING_TARGET,
        "untagged",
        &[("enum: [METEOR]", "enum: [SHOOTING_STAR]")],
        temp.path(),
    );
    let twin = variant_of(
        DANGLING_TARGET,
        "twin",
        &[
            (
                METEOR_MEMBER,
                "        - $ref: '#/components/schemas/MeteorReading'\n        - $ref: '#/components/schemas/FireballReading'\n",
            ),
            (
                "    Trail:\n",
                "    FireballReading:\n      type: object\n      properties:\n        kind:\n          type: string\n          enum: [METEOR]\n        flare:\n          type: number\n    Trail:\n",
            ),
        ],
        temp.path(),
    );
    for (document, mode) in [&untagged, &twin]
        .into_iter()
        .flat_map(|document| ["python-enums", "literals"].map(|mode| (document, mode)))
    {
        let out = temp.path().join(document.file_stem().unwrap()).join(mode);
        probe_command(document, &out)
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
            "{} {mode}",
            document.display()
        );
    }
}

/// A dangling mapping outside the measured shape reads as crozier read it
/// before. A `$ref` member to nothing leaves `Reading` the undiscriminated
/// union, `typing.Any` for that member, and `MeteorReading` without its tag.
/// A mapping none of whose targets names a component is refused for the
/// discriminant it cannot place, before any file is written.
#[test]
fn a_dangling_mapping_outside_the_measured_shape_reads_as_before() {
    let temp = tempfile::tempdir().expect("output tempdir");
    let gone = variant_of(
        DANGLING_TARGET,
        "gone",
        &[(
            METEOR_MEMBER,
            "        - $ref: '#/components/schemas/MeteorReading'\n        - $ref: '#/components/schemas/Gone'\n",
        )],
        temp.path(),
    );
    let out = temp.path().join("gone-sdk");
    probe_command(&gone, &out).assert().success();
    let reading = crozier::normalize::strip_python_comments(&module(&out, "reading.py"));
    assert!(
        reading.contains(
            "Reading = typing.Union[StarReading, CometReading, MeteorReading, typing.Any]"
        ),
        "{reading}"
    );
    assert!(!reading.contains("class Reading_"), "{reading}");
    let meteor = module(&out, "meteor_reading.py");
    assert!(!meteor.contains("    kind:"), "{meteor}");

    let unnamed = variant_of(
        DANGLING_TARGET,
        "unnamed",
        &[
            (
                "STAR: '#/components/schemas/StarReading'",
                "STAR: '#/components/schemas/star-reading'",
            ),
            (
                "COMET: '#/components/schemas/CometReading'",
                "COMET: '#/components/schemas/comet-reading'",
            ),
        ],
        temp.path(),
    );
    let refused = temp.path().join("unnamed-sdk");
    probe_command(&unnamed, &refused)
        .assert()
        .failure()
        .stderr(predicate::str::contains(
            "missing-discriminant-property: POST /readings request components/schemas/Reading discriminator kind",
        ));
    assert!(!refused.exists(), "a refused document writes no SDK");
}

/// A document neither cause touches — every mapping target resolves, each
/// `allOf` variant's base is a plain object, and `Letter`'s own tag is
/// optional — generates the tree crozier wrote before either repair, every
/// file of it, README.md and reference.md included, in both enum modes. Each
/// `base-tree.<mode>.sha256` pins the baseline tree; its provenance is recorded
/// in the linked measurement document. The Markdown examples still pass `Letter`'s
/// optional tag back, which only a union with a dangling target leaves out.
#[test]
fn a_document_neither_cause_touches_generates_the_base_tree_byte_for_byte() {
    let case = repo_root()
        .join(EMISSION_PARITY_DIR)
        .join(UNAFFECTED_CONTROL);
    for mode in ["python-enums", "literals"] {
        let temp = tempfile::tempdir().expect("output tempdir");
        let out = temp.path().join("sdk");
        probe_command(&case.join("openapi.yml"), &out)
            .args(["--enum-type", mode])
            .assert()
            .success();
        let manifest = std::fs::read_to_string(case.join(format!("base-tree.{mode}.sha256")))
            .expect("the base tree's manifest");
        let expected: Vec<(String, String)> = manifest
            .lines()
            .map(|line| {
                let (digest, path) = line.split_once("  ").expect("a sha256sum line");
                (path.to_string(), digest.to_string())
            })
            .collect();
        let mut generated = Vec::new();
        let mut pending = vec![out.clone()];
        while let Some(dir) = pending.pop() {
            for entry in std::fs::read_dir(&dir).unwrap() {
                let path = entry.unwrap().path();
                if path.is_dir() {
                    pending.push(path);
                } else {
                    let relative = path.strip_prefix(&out).unwrap();
                    let name = relative
                        .components()
                        .map(|part| part.as_os_str().to_string_lossy())
                        .collect::<Vec<_>>()
                        .join("/");
                    generated.push((name, sha256_hex(&std::fs::read(&path).unwrap())));
                }
            }
        }
        generated.sort();
        let differing: std::collections::BTreeSet<&str> = expected
            .iter()
            .filter(|entry| !generated.contains(entry))
            .chain(generated.iter().filter(|entry| !expected.contains(entry)))
            .map(|(path, _)| path.as_str())
            .collect();
        assert!(
            differing.is_empty(),
            "{mode}: these files differ from the base's tree: {differing:?}"
        );
        let tag = if mode == "literals" {
            "kind=\"LETTER\""
        } else {
            "kind=LetterKind.LETTER"
        };
        let reference = std::fs::read_to_string(out.join("reference.md")).unwrap();
        assert!(reference.contains(tag), "{mode}: {reference}");
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
        "cyclic",
        &[(
            "    Named:\n      type: object\n",
            "    Named:\n      allOf:\n        - $ref: '#/components/schemas/Gauge'\n",
        )],
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

/// crozier's SDK from `spec` in `mode`, the process output unasserted.
fn generate_spec(spec: &Path, out: &Path, mode: &str) -> std::process::Output {
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
        let run = generate_spec(&spec, &out, mode);
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
