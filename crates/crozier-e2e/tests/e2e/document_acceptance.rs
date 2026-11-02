//! The document-acceptance handed-off area: documents the certified pair reads
//! where crozier refused, failed to parse or wrote invalid Python, each
//! measured from scratch under
//! `docs/fern-measurements/handed-off/document-acceptance/<root cause>/` and
//! triaged in `docs/fern-measurements/handed-off/document-acceptance.tsv`.
//!
//! - A cause recorded `parity-gap-repaired` generates its measurement's
//!   certified-pair tree, in both enum modes where the mode changes it, by
//!   default and under `--fern-strict`.
//! - A cause recorded `refusal-kept` is refused in both modes with the class
//!   `docs/fern-refusals/README.md` records, as the certified pair refuses it.
//! - Each refusal class narrowed for a cause still fires on a control of the
//!   shape the certified pair refuses.

use std::path::{Path, PathBuf};

use super::departures_ledger::GoldenLedger;
use super::{
    departure_ledger, golden_path, golden_tree_failures, probe_artifact_digest, probe_command,
    repo_root, walk_files,
};

/// Where the measurements live.
pub(crate) const DOCUMENT_ACCEPTANCE_DIR: &str =
    "docs/fern-measurements/handed-off/document-acceptance";
/// A measurement's literals overlay over its `fern-expected/`.
const OVERLAY_DIR: &str = "expected-literals";
const MANIFEST: &str = ".crozier-overlay.json";

/// The causes whose measurement crozier now byte-matches.
const REPAIRED: [&str; 11] = [
    "R14",
    "bare-string-parameter-example",
    "crozier-invalid-duplicate-parameter",
    "crozier-refuses-boolean-schema",
    "crozier-refuses-component-link-ref",
    "crozier-refuses-nullable-error-extension",
    "crozier-refuses-path-without-slash",
    "crozier-refuses-type-name-collision",
    "crozier-refuses-unknown-type-value",
    "never-compared-request-property-name-collision",
    "never-compared-type-name-collision",
];

/// The repaired causes whose document declares an enum, so the literals mode
/// changes the certified pair's tree and an overlay holds it.
const WITH_LITERALS: [&str; 3] = [
    "crozier-invalid-duplicate-parameter",
    "crozier-refuses-type-name-collision",
    "never-compared-type-name-collision",
];

/// The causes the certified pair refuses, and the class crozier refuses each
/// with in both modes.
const REFUSED: [(&str, &str); 4] = [
    (
        "crozier-refuses-dangling-component-ref",
        "unresolved-reference: paths//payments/post/responses/403: #/components/schemas/payment_error",
    ),
    (
        "crozier-refuses-unreferenced-path-parameter",
        "path-parameter-unreferenced: GET /trees/{treeId} parameter growerId",
    ),
    (
        "never-compared-request-property-camelcase-collision",
        "request-property-camelcase-collision: GET /loans parameters \"shelf\" and \"shelf[]\" normalize to the same identifier",
    ),
    ("null-info-paths-components", "missing-info-object: info"),
];

/// Every tree this module compares: each repaired cause's `fern-expected/`
/// and each literals overlay, the overlay's manifest excluded.
pub(super) fn compared() -> Vec<(String, Vec<String>)> {
    REPAIRED
        .iter()
        .map(|case| {
            (
                format!("{DOCUMENT_ACCEPTANCE_DIR}/{case}/fern-expected"),
                Vec::new(),
            )
        })
        .chain(WITH_LITERALS.iter().map(|case| {
            (
                format!("{DOCUMENT_ACCEPTANCE_DIR}/{case}/{OVERLAY_DIR}"),
                vec![MANIFEST.to_string()],
            )
        }))
        .collect()
}

fn case_dir(case: &str) -> PathBuf {
    repo_root().join(DOCUMENT_ACCEPTANCE_DIR).join(case)
}

fn spec(case: &str) -> PathBuf {
    case_dir(case).join("openapi.yml")
}

/// crozier's SDK for `spec`, in `enum_type`, by default or under
/// `--fern-strict`, against `expected` held to `ledger`.
fn tree_failures(
    name: &str,
    spec: &Path,
    expected: &Path,
    ledger: &GoldenLedger,
    enum_type: &str,
    strict: bool,
) -> Vec<String> {
    let out = tempfile::tempdir().expect("tempdir");
    let mut command = probe_command(spec, out.path());
    command.args(["--enum-type", enum_type]);
    if strict {
        command.arg("--fern-strict");
    }
    let result = command.output().expect("crozier runs");
    let label = format!("{name} (enum-type {enum_type}, fern-strict {strict})");
    if !result.status.success() {
        return vec![format!(
            "{label}: crozier refused a document the certified pair generates: {}",
            String::from_utf8_lossy(&result.stderr)
        )];
    }
    golden_tree_failures(
        &label,
        &spec.display().to_string(),
        ledger,
        expected,
        out.path(),
    )
}

/// `case`'s literals tree: `fern-expected/` less the files the manifest
/// removes, the overlay laid over it, held to the manifest's digest of the
/// complete tree the certified pair generated; and the ledger that tree is
/// held to.
fn literals_tree(case: &str) -> Result<(tempfile::TempDir, GoldenLedger), String> {
    let overlay = case_dir(case).join(OVERLAY_DIR);
    let text = std::fs::read_to_string(overlay.join(MANIFEST))
        .map_err(|error| format!("{case}: cannot read its literals manifest: {error}"))?;
    let manifest: serde_json::Value = serde_json::from_str(&text)
        .map_err(|error| format!("{case}: invalid literals manifest: {error}"))?;
    let pair = crozier::emit::certified_fern_pair();
    for (key, value) in [
        ("enum_type", "literals"),
        ("base", "fern-expected"),
        ("fern_cli_version", pair.cli),
        ("fern_python_sdk_version", pair.python_sdk),
    ] {
        if manifest[key] != value {
            return Err(format!(
                "{case}: its literals manifest must record {key} `{value}`"
            ));
        }
    }
    let removed: Vec<String> = manifest["removed"]
        .as_array()
        .ok_or_else(|| format!("{case}: its literals manifest has no `removed` list"))?
        .iter()
        .map(|entry| {
            entry
                .as_str()
                .map(str::to_string)
                .ok_or_else(|| format!("{case}: `removed` lists a non-path: {entry}"))
        })
        .collect::<Result<_, _>>()?;
    let tree = tempfile::tempdir().map_err(|error| format!("tempdir: {error}"))?;
    let copy = |from: &Path, rel: &str| -> Result<(), String> {
        let to = tree.path().join(rel);
        std::fs::create_dir_all(to.parent().expect("a file has a parent"))
            .and_then(|()| std::fs::copy(from.join(rel), &to).map(drop))
            .map_err(|error| format!("{case}: cannot copy {rel}: {error}"))
    };
    let base = case_dir(case).join("fern-expected");
    for rel in walk_files(&base) {
        if !removed.contains(&rel) {
            copy(&base, &rel)?;
        }
    }
    let own: std::collections::BTreeSet<String> = walk_files(&overlay)
        .into_iter()
        .filter(|rel| rel != MANIFEST)
        .collect();
    for rel in &own {
        copy(&overlay, rel)?;
    }
    let digest = probe_artifact_digest(tree.path())?;
    if manifest["digest"] != digest.as_str() {
        return Err(format!(
            "{case}: the rebuilt literals tree hashes to {digest}, not the {} its manifest \
             records — a committed Fern file changed; restore it",
            manifest["digest"]
        ));
    }
    let ledger = departure_ledger()
        .golden(
            &format!("{DOCUMENT_ACCEPTANCE_DIR}/{case}/{OVERLAY_DIR}"),
            &[],
        )
        .and_then(|own_rows| {
            Ok(own_rows.inherit(
                departure_ledger().golden(&golden_path(&base), &[])?,
                own,
                &removed,
            ))
        })
        .map_err(|failures| failures.join("\n"))?;
    Ok((tree, ledger))
}

// llmlint: ignore-block[expensive_tests_stay_behind_their_own_edge] Each journey generates one small SDK per mode through the binary, on the crozier-e2e edge every other golden comparison shares; splitting that edge is the drafted follow-up "Give crozier-e2e's generator-replay journeys an Nx edge narrower than e2eReads".
/// Every repaired cause's measurement generates the certified pair's tree,
/// by default and under `--fern-strict`.
#[test]
fn each_repaired_cause_generates_its_certified_pair_tree() {
    let mut failures = Vec::new();
    for case in REPAIRED {
        let golden = format!("{DOCUMENT_ACCEPTANCE_DIR}/{case}/fern-expected");
        let ledger = departure_ledger()
            .golden(&golden, &[])
            .unwrap_or_else(|failures| panic!("{}", failures.join("\n")));
        for strict in [false, true] {
            failures.extend(tree_failures(
                case,
                &spec(case),
                &repo_root().join(&golden),
                &ledger,
                "python-enums",
                strict,
            ));
        }
    }
    assert!(failures.is_empty(), "{}", failures.join("\n\n"));
}

/// The repaired causes whose document declares an enum generate the certified
/// pair's literals tree too.
#[test]
fn enum_bearing_repairs_generate_the_literals_tree_too() {
    let mut failures = Vec::new();
    for case in WITH_LITERALS {
        let (tree, ledger) = literals_tree(case).unwrap_or_else(|error| panic!("{error}"));
        for strict in [false, true] {
            failures.extend(tree_failures(
                case,
                &spec(case),
                tree.path(),
                &ledger,
                "literals",
                strict,
            ));
        }
    }
    assert!(failures.is_empty(), "{}", failures.join("\n\n"));
}

/// Each cause the certified pair refuses is refused by crozier in both modes,
/// writing nothing, with the class the registry records; the certified pair's
/// committed run shows its refusal (a non-zero exit, or exit 0 over a document
/// its log says it failed to parse).
#[test]
fn each_refused_cause_is_refused_in_both_modes() {
    for (case, diagnostic) in REFUSED {
        let dir = case_dir(case);
        let exit = std::fs::read_to_string(dir.join("exit-code")).unwrap();
        let log = std::fs::read_to_string(dir.join("fern.log")).unwrap();
        assert!(
            exit.trim() != "0" || log.contains("Failed to parse openapi document"),
            "{case}: the committed certified-pair run records no refusal"
        );
        let class = diagnostic.split(':').next().unwrap();
        let classes =
            std::fs::read_to_string(repo_root().join("docs/fern-refusals/classes.tsv")).unwrap();
        assert!(
            classes
                .lines()
                .any(|row| row.split('\t').next() == Some(class) && row.contains("\trefuse\t")),
            "{case}: docs/fern-refusals/classes.tsv records no `refuse` class {class}"
        );
        for strict in [false, true] {
            let out = tempfile::tempdir().unwrap();
            let target = out.path().join("sdk");
            let mut command = probe_command(&spec(case), &target);
            if strict {
                command.arg("--fern-strict");
            }
            let result = command.output().unwrap();
            let stderr = String::from_utf8_lossy(&result.stderr);
            assert_eq!(
                result.status.code(),
                Some(1),
                "{case} (strict {strict}): {stderr}"
            );
            assert!(
                stderr.contains(diagnostic),
                "{case} (strict {strict}): {stderr}"
            );
            assert_eq!(stderr.trim().lines().count(), 1, "{case}: {stderr}");
            assert!(
                !target.exists(),
                "{case} (strict {strict}): a refusal writes nothing"
            );
        }
    }
}

/// Write `text` as an OpenAPI document under `dir` and run crozier on it.
fn run(dir: &Path, name: &str, text: &str, strict: bool) -> std::process::Output {
    let spec = dir.join(name);
    std::fs::write(&spec, text).unwrap();
    let mut command = probe_command(&spec, &dir.join(format!("{name}.sdk")));
    if strict {
        command.arg("--fern-strict");
    }
    command.output().unwrap()
}

/// `case`'s document with every `(from, to)` substitution applied, each of
/// which must change it.
fn edited(case: &str, edits: &[(&str, &str)]) -> String {
    let mut text = std::fs::read_to_string(spec(case)).unwrap();
    for (from, to) in edits {
        assert!(text.contains(from), "{case} no longer contains {from:?}");
        text = text.replace(from, to);
    }
    text
}

/// The narrowed refusals still fire on the shapes the certified pair refuses:
/// a response written as a `$ref` to a schema (`unresolved-reference`, the
/// dangling-ref measurement), a path key without a slash that is not empty,
/// a nullable extension reached through closed objects only, and a body whose
/// grandparent declares the path parameter's name.
#[test]
fn narrowed_refusals_still_fire_on_their_controls() {
    let temp = tempfile::tempdir().unwrap();
    let nullable_closed: String =
        std::fs::read_to_string(spec("crozier-refuses-nullable-error-extension"))
            .unwrap()
            .lines()
            .filter(|line| line.trim() != "additionalProperties: true")
            .map(|line| format!("{line}\n"))
            .collect();
    for (name, text, diagnostic) in [
        (
            "slashless.yml",
            edited("crozier-refuses-path-without-slash", &[("  '':\n", "  status:\n")]),
            "path-without-leading-slash: paths/status".to_string(),
        ),
        (
            "closed.yml",
            nullable_closed,
            "example-missing-required-property: POST /exports/get response extends nullable #/components/schemas/LedgerError".to_string(),
        ),
        (
            "grandparent.yml",
            std::fs::read_to_string(
                repo_root().join("docs/fern-refusals/request-property-name-collision/probe.yml"),
            )
            .unwrap(),
            "request-property-name-collision: PATCH /requests/{id} body property \"id\"".to_string(),
        ),
        (
            "case-collision.yml",
            std::fs::read_to_string(repo_root().join("docs/fern-refusals/type-name-collision/probe.yml"))
                .unwrap(),
            "type-name-collision".to_string(),
        ),
    ] {
        for strict in [false, true] {
            let result = run(temp.path(), name, &text, strict);
            let stderr = String::from_utf8_lossy(&result.stderr);
            assert_eq!(result.status.code(), Some(1), "{name} (strict {strict}): {stderr}");
            assert!(stderr.contains(&diagnostic), "{name} (strict {strict}): {stderr}");
        }
    }
    // Two query parameters whose names differ past their brackets still
    // generate, as the certified pair generates them.
    let distinct = edited(
        "never-compared-request-property-camelcase-collision",
        &[("name: shelf[]", "name: shelves[]")],
    );
    for strict in [false, true] {
        let result = run(temp.path(), "distinct.yml", &distinct, strict);
        assert!(
            result.status.success(),
            "{}",
            String::from_utf8_lossy(&result.stderr)
        );
    }
}

/// The repaired documents generate the method the certified pair writes for
/// each shape, and the doorbell body's calls pass each keyword once.
#[test]
fn repaired_documents_write_the_certified_pair_s_methods() {
    let temp = tempfile::tempdir().unwrap();
    for (case, module, needles) in [
        (
            "crozier-invalid-duplicate-parameter",
            "client.py",
            &["def send_alert(", "headline: typing.Optional[str] = OMIT,"][..],
        ),
        (
            "never-compared-request-property-name-collision",
            "client.py",
            &["def update_member(", "id_path_param: int,"][..],
        ),
        (
            "crozier-refuses-path-without-slash",
            "raw_client.py",
            &["def get_status("][..],
        ),
    ] {
        let out = temp.path().join(case);
        probe_command(&spec(case), &out).assert().success();
        let text = std::fs::read_to_string(out.join("src/fern").join(module)).unwrap();
        for needle in needles {
            assert!(text.contains(needle), "{case}: no {needle:?} in {module}");
        }
    }
    let client = std::fs::read_to_string(
        temp.path()
            .join("crozier-invalid-duplicate-parameter/src/fern/client.py"),
    )
    .unwrap();
    let forwarding: Vec<&str> = client
        .split("def ")
        .filter(|method| method.contains("headline=headline"))
        .collect();
    assert!(!forwarding.is_empty(), "no call forwards headline");
    for method in forwarding {
        assert_eq!(
            method.matches("headline=headline").count(),
            1,
            "a call passes headline twice:\n{method}"
        );
    }
}
// llmlint: ignore-end[expensive_tests_stay_behind_their_own_edge]
