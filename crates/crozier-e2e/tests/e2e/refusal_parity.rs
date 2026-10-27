//! Documents the certified pair generates from that crozier used to refuse,
//! driven through the real binary (`docs/fern-measurements/refusal-parity/`).
//!
//! - `quoted-continuation-at-key-column`: a multi-line quoted scalar whose
//!   continuation lines sit at its key's column (or shallower), which YAML
//!   reserves for the next key, as ingef/conquery's `openapi.yaml` writes its
//!   descriptions. Fern's reader folds those lines as it folds deeper ones, so
//!   crozier reads the same values and writes Fern's SDK. Each malformed
//!   neighbour beside it is one Fern's reader refuses too (its `*.fern.log`), and
//!   crozier still refuses it.
//! - A union variant's discriminant whose only enum value is `null`, in an
//!   inline `allOf` member or the variant's own `properties`
//!   (`docs/fern-refusals/generator-lint-failure/null-only-discriminant-control.yml`,
//!   `null-only-direct-discriminant-control.yml`), generates, as Fern generates it, while the same enum beside the
//!   discriminant (`null-only-beside-discriminant-probe.yml`) stays refused.

use std::path::{Path, PathBuf};

use predicates::prelude::*;

use super::{crozier, departure_ledger, golden_tree_failures, probe_command, repo_root};

/// Where the measurements live; each case's `fern-expected/` is a compared golden.
pub(crate) const REFUSAL_PARITY_DIR: &str = "docs/fern-measurements/refusal-parity";
const QUOTED_CONTINUATION: &str = "quoted-continuation-at-key-column";
const LINT_FAILURE_DIR: &str = "docs/fern-refusals/generator-lint-failure";

fn case_dir(case: &str) -> PathBuf {
    repo_root().join(REFUSAL_PARITY_DIR).join(case)
}

// llmlint: ignore-block[expensive_tests_stay_behind_their_own_edge] Each of these journeys generates one small SDK through the binary, on the crozier-e2e edge every other golden comparison shares; splitting that edge is the drafted follow-up "Give crozier-e2e's generator-replay journeys an Nx edge narrower than e2eReads".
/// The document generates, and its SDK is Fern's file for file: the folded
/// summary, descriptions and enum values are the ones Fern read.
#[test]
fn a_quoted_continuation_at_its_keys_column_generates_fern_s_sdk() {
    let temp = tempfile::tempdir().expect("output tempdir");
    let out = temp.path().join("sdk");
    let spec = case_dir(QUOTED_CONTINUATION).join("openapi.yml");
    probe_command(&spec, &out).assert().success();
    let golden = format!("{REFUSAL_PARITY_DIR}/{QUOTED_CONTINUATION}/fern-expected");
    let ledger = departure_ledger()
        .golden(&golden, &[])
        .unwrap_or_else(|failures| panic!("{}", failures.join("\n")));
    let failures = golden_tree_failures(
        QUOTED_CONTINUATION,
        &spec.display().to_string(),
        &ledger,
        &repo_root().join(&golden),
        &out,
    );
    assert!(failures.is_empty(), "{}", failures.join("\n\n"));
    let lamp = std::fs::read_to_string(out.join("src/fern/types/lamp.py")).unwrap();
    assert!(lamp.contains("OIL_WICK = \"oil wick\""), "{lamp}");
    assert!(lamp.contains("GAS_MANTLE = \"gas mantle\""), "{lamp}");
    let beacon = std::fs::read_to_string(out.join("src/fern/types/beacon.py")).unwrap();
    assert!(
        beacon.contains(
            "A light on the coast that ships steer by. Each one keeps its own schedule, and its own lamp."
        ),
        "{beacon}"
    );
}

/// Each malformed neighbour is refused by the certified pair, as its committed
/// log records, and by crozier at the parser, writing nothing.
#[test]
fn yaml_fern_s_reader_refuses_stays_refused() {
    for (stem, fern_says) in [
        (
            "unclosed-quote",
            "unexpected end of the stream within a double quoted scalar",
        ),
        (
            "document-marker",
            "unexpected end of the document within a double quoted scalar",
        ),
        (
            "trailing-content",
            "a multiline key may not be an implicit key",
        ),
    ] {
        let dir = case_dir(QUOTED_CONTINUATION);
        let log = std::fs::read_to_string(dir.join(format!("{stem}.fern.log"))).unwrap();
        assert!(
            log.contains("generate exit: 1") && log.contains(fern_says),
            "{stem}: the committed Fern log no longer records the refusal:\n{log}"
        );
        let temp = tempfile::tempdir().unwrap();
        let out = temp.path().join("sdk");
        probe_command(&dir.join(format!("{stem}.openapi.yml")), &out)
            .assert()
            .failure()
            .stderr(predicate::str::contains("could not parse OpenAPI document"));
        assert!(!out.exists(), "{stem}: a refused document writes no SDK");
    }
}

/// A document already valid YAML reads as it always has: a continuation
/// deeper than its key, a plain multi-line scalar, a closing quote alone at
/// the key's column, and a one-line quoted value followed by the next key.
#[test]
fn valid_multi_line_scalars_read_as_before() {
    let temp = tempfile::tempdir().unwrap();
    let spec = temp.path().join("openapi.yml");
    std::fs::write(
        &spec,
        r#"openapi: 3.0.3
info:
  title: Lighthouse
  version: 1.0.0
paths:
  /beacons:
    get:
      operationId: listBeacons
      responses:
        '200':
          description: The beacons
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Beacon'
components:
  schemas:
    Beacon:
      type: object
      description: "A light on the coast
        that ships steer by."
      properties:
        id:
          type: string
          description: A plain identifier
            continued deeper.
        keeper:
          type: string
          description: "Who tends it
          "
        lamp:
          type: string
          description: "The lamp."
          title: Lamp
"#,
    )
    .unwrap();
    let out = temp.path().join("sdk");
    probe_command(&spec, &out).assert().success();
    let beacon = std::fs::read_to_string(out.join("src/fern/types/beacon.py")).unwrap();
    for expected in [
        "A light on the coast that ships steer by.",
        "A plain identifier continued deeper.",
        "Who tends it",
        "The lamp.",
    ] {
        assert!(beacon.contains(expected), "no {expected:?} in:\n{beacon}");
    }
}

fn lint_shape(name: &str) -> PathBuf {
    repo_root().join(LINT_FAILURE_DIR).join(name)
}

/// The certified pair's verdict on a shape, as `shapes.tsv` records it.
fn fern_verdict(name: &str) -> String {
    let table =
        std::fs::read_to_string(repo_root().join("docs/openapi-surface/fern-refusals/shapes.tsv"))
            .unwrap();
    let row = table
        .lines()
        .map(|line| line.split('\t').collect::<Vec<_>>())
        .find(|cells| {
            cells.first() == Some(&"generator-lint-failure") && cells.get(1) == Some(&name)
        })
        .unwrap_or_else(|| {
            panic!("{name} has no shapes.tsv row; measure it with `fern-refusals.py shapes`")
        });
    row[8].to_owned()
}

fn generate_shape(
    shape: &Path,
    out: &Path,
    enum_type: &str,
    strict: bool,
) -> assert_cmd::assert::Assert {
    let mut command = crozier();
    command
        .args(["generate", "python", "--spec"])
        .arg(shape)
        .arg("--output")
        .arg(out)
        .args(["--enum-type", enum_type]);
    if strict {
        command.arg("--fern-strict");
    }
    command.assert()
}

/// The null-only discriminant generates in both enum modes, with and without
/// `--fern-strict`, as the certified pair generates it; beside the
/// discriminant the same enum is refused in every mode, as the pair refuses it.
#[test]
fn a_null_only_discriminant_generates_where_the_same_enum_beside_it_is_refused() {
    for control in [
        "null-only-discriminant-control.yml",
        "null-only-direct-discriminant-control.yml",
    ] {
        assert_eq!(fern_verdict(control), "generates", "{control}");
    }
    assert_eq!(
        fern_verdict("null-only-beside-discriminant-probe.yml"),
        "refused"
    );
    for enum_type in ["python-enums", "literals"] {
        for strict in [false, true] {
            let temp = tempfile::tempdir().unwrap();
            for control in [
                "null-only-discriminant-control.yml",
                "null-only-direct-discriminant-control.yml",
            ] {
                let out = temp.path().join(control);
                generate_shape(&lint_shape(control), &out, enum_type, strict).success();
                let silence =
                    std::fs::read_to_string(out.join("src/probe/types/silence.py")).unwrap();
                assert!(
                    !silence.contains("kind"),
                    "{control} {enum_type}: the discriminant stays on the union:\n{silence}"
                );
            }
            let refused = temp.path().join("refused");
            generate_shape(
                &lint_shape("null-only-beside-discriminant-probe.yml"),
                &refused,
                enum_type,
                strict,
            )
            .failure()
            .stderr(predicate::str::contains(
                "generator-lint-failure: components/schemas/Silence/allOf/1/properties/kind enum has no non-null value",
            ));
            assert!(
                !refused.exists(),
                "{enum_type}: a refused document writes no SDK"
            );
        }
    }
}

/// A document whose head the parser refuses for a quoted continuation, with
/// `born`'s `format: date` example written as `Thing`'s plain timestamp: the
/// repaired document still reads that example as Fern's reader does (a
/// timestamp, so no string it rejects) and generates, where the same example
/// quoted is refused as `example-type-mismatch`.
#[test]
fn a_plain_timestamp_after_a_repaired_scalar_keeps_its_exemption() {
    let probe = std::fs::read_to_string(
        repo_root().join("docs/fern-refusals/example-type-mismatch/probe.yml"),
    )
    .unwrap();
    let quoted = "          example: \"2006-01-02T15:04:05+00:00\"\n";
    assert!(probe.contains(quoted));
    let repaired_head = probe.replace(
        "      type: object\n",
        "      type: object\n      description: \"A thing\n      that was born.\"\n",
    );
    for (example, refused) in [
        ("2006-01-02T15:04:05+00:00", false),
        ("\"2006-01-02T15:04:05+00:00\"", true),
    ] {
        let temp = tempfile::tempdir().unwrap();
        let spec = temp.path().join("openapi.yml");
        std::fs::write(
            &spec,
            repaired_head.replace(quoted, &format!("          example: {example}\n")),
        )
        .unwrap();
        let out = temp.path().join("sdk");
        let assert = probe_command(&spec, &out).assert();
        if refused {
            assert
                .failure()
                .stderr(predicate::str::contains("example-type-mismatch"));
            assert!(!out.exists(), "a refused document writes no SDK");
        } else {
            assert.success();
            let thing = std::fs::read_to_string(out.join("src/fern/types/thing.py")).unwrap();
            assert!(thing.contains("A thing that was born."), "{thing}");
        }
    }
}

/// An anchored and tagged quoted scalar continued at its key's column reads
/// folded, as an unadorned one does.
#[test]
fn an_anchored_and_tagged_continuation_reads_folded() {
    let temp = tempfile::tempdir().unwrap();
    let spec = temp.path().join("openapi.yml");
    std::fs::write(
        &spec,
        r#"openapi: 3.0.3
info:
  title: Lighthouse
  version: 1.0.0
paths:
  /beacons:
    get:
      operationId: listBeacons
      responses:
        '200':
          description: The beacons
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Beacon'
components:
  schemas:
    Beacon:
      type: object
      description: &beacon !!str "A light on the coast
      that ships steer by."
      properties:
        id:
          type: string
          description: *beacon
"#,
    )
    .unwrap();
    let out = temp.path().join("sdk");
    probe_command(&spec, &out).assert().success();
    let beacon = std::fs::read_to_string(out.join("src/fern/types/beacon.py")).unwrap();
    assert_eq!(
        beacon
            .matches("A light on the coast that ships steer by.")
            .count(),
        2,
        "{beacon}"
    );
}

/// Where a repairable scalar precedes one that is malformed, the refusal names
/// the malformed one's line, not the scalar Fern's reader accepts, and no SDK
/// is written.
#[test]
fn a_malformed_scalar_after_a_repairable_one_is_the_one_named() {
    let temp = tempfile::tempdir().unwrap();
    let spec = temp.path().join("openapi.yml");
    let document =
        std::fs::read_to_string(case_dir(QUOTED_CONTINUATION).join("document-marker.openapi.yml"))
            .unwrap()
            .replace(
                "      operationId: listBeacons\n",
                "      operationId: listBeacons\n      summary: \"List every\n      beacon\"\n",
            );
    let marker_line = document.lines().position(|line| line == "---").unwrap() + 1;
    std::fs::write(&spec, &document).unwrap();
    let out = temp.path().join("sdk");
    probe_command(&spec, &out)
        .assert()
        .failure()
        .stderr(predicate::str::contains(format!(
            "line {marker_line} column 1"
        )));
    assert!(!out.exists(), "a refused document writes no SDK");
}
// llmlint: ignore-end[expensive_tests_stay_behind_their_own_edge]
