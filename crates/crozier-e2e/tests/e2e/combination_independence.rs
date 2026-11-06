//! Replay each independent combination's three authored documents against its
//! complete certified trees through the real command line and parity engine.

use super::*;

#[derive(Clone, Copy, Debug, serde::Deserialize, serde::Serialize)]
#[serde(rename_all = "snake_case")]
enum Mode {
    PythonEnums,
    Literals,
}

impl Mode {
    fn cli_value(self) -> &'static str {
        match self {
            Self::PythonEnums => "python-enums",
            Self::Literals => "literals",
        }
    }
}

#[derive(serde::Deserialize)]
#[serde(deny_unknown_fields)]
struct Document {
    document: PathBuf,
    python_enums: PathBuf,
    literals: Option<PathBuf>,
}

impl Document {
    fn tree(&self, mode: Mode) -> &Path {
        match mode {
            Mode::PythonEnums => &self.python_enums,
            Mode::Literals => self.literals.as_deref().expect("validated literals tree"),
        }
    }
}

#[derive(serde::Deserialize)]
#[serde(deny_unknown_fields)]
struct Documents {
    first: Document,
    second: Document,
    both: Document,
}

#[derive(serde::Deserialize)]
#[serde(deny_unknown_fields)]
struct Proof {
    key: String,
    modes: Vec<Mode>,
    documents: Documents,
}

fn read_proofs(root: &Path) -> Vec<Proof> {
    let reader = std::process::Command::new(
        python_interpreter().expect("Python to read the independence manifest"),
    )
    .arg(repo_root().join("tools/surface-census/combination-independence.py"))
    .arg("--json")
    .arg("--repo-root")
    .arg(root)
    .output()
    .expect("run the shared independence reader");
    assert!(
        reader.status.success(),
        "{}",
        String::from_utf8_lossy(&reader.stderr)
    );
    serde_json::from_slice(&reader.stdout).expect("validated independence records")
}

fn write_manifest(root: &Path, key: &str, modes: &[Mode]) {
    let manifest = root.join("docs/openapi-surface/combination-independence.toml");
    std::fs::create_dir_all(manifest.parent().unwrap()).unwrap();
    let mut text = String::from(
        r#"schema_version = 1
[[combinations]]
[[combinations.conditions]]
feature = "first"
handler = "src/ir.rs::error_response_entries"
condition = "if code.starts_with('2') {"
[[combinations.conditions]]
feature = "second"
handler = "src/ir.rs::error_body_schema"
condition = ".find(|schema| !is_unknown(schema))"
[combinations.documents]
"#,
    );
    text = text.replacen(
        "[[combinations]]\n",
        &format!(
            "[[combinations]]\nkey = {}\nmodes = {}\n",
            serde_json::to_string(key).unwrap(),
            serde_json::to_string(modes).unwrap()
        ),
        1,
    );
    for label in ["first", "second", "both"] {
        let literals = if modes.iter().any(|mode| matches!(mode, Mode::Literals)) {
            format!(", literals = \"cases/{label}/literals\"")
        } else {
            String::new()
        };
        text.push_str(&format!(
            "{label} = {{document = \"cases/{label}/openapi.yml\", python_enums = \"cases/{label}/enums\"{literals}}}\n"
        ));
    }
    std::fs::write(&manifest, text).unwrap();
}

#[test]
fn a_populated_independence_manifest_crosses_the_python_rust_boundary() {
    let scratch = tempfile::tempdir().unwrap();
    write_manifest(
        scratch.path(),
        "combo-parser-boundary",
        &[Mode::PythonEnums, Mode::Literals],
    );
    let proofs = read_proofs(scratch.path());
    assert_eq!(proofs.len(), 1);
    let proof = &proofs[0];
    assert_eq!(proof.key, "combo-parser-boundary");
    assert_eq!(proof.modes.len(), 2);
    assert!(matches!(proof.modes[0], Mode::PythonEnums));
    assert!(matches!(proof.modes[1], Mode::Literals));
    for (label, document) in [
        ("first", &proof.documents.first),
        ("second", &proof.documents.second),
        ("both", &proof.documents.both),
    ] {
        assert_eq!(
            document.document,
            PathBuf::from(format!("cases/{label}/openapi.yml"))
        );
        assert_eq!(
            document.tree(Mode::PythonEnums),
            Path::new(&format!("cases/{label}/enums"))
        );
        assert_eq!(
            document.tree(Mode::Literals),
            Path::new(&format!("cases/{label}/literals"))
        );
    }
}

// llmlint: ignore[expensive_tests_stay_behind_their_own_edge] This complete-tree replay belongs to the compiled-binary golden suite (crates/crozier-e2e/AGENTS.md).
#[test]
fn independent_combination_documents_match_certified_trees() {
    replay_protocol_smoke();
    replay_proofs(repo_root(), read_proofs(repo_root()));
}

/// Exercise the replay protocol even while the selected manifest is empty.
/// These are semantic media controls, not an independence claim: the source
/// audit and instrumented union admission are separate gates.
fn replay_protocol_smoke() {
    let scratch = tempfile::tempdir().unwrap();
    let root = scratch.path();
    write_manifest(root, "combo-replay-boundary", &[Mode::PythonEnums]);
    for label in ["first", "second", "both"] {
        let source = repo_root().join(format!(
            "docs/fern-measurements/operation-independence/error-multiple-media-{label}"
        ));
        let target = root.join(format!("cases/{label}"));
        std::fs::create_dir_all(&target).unwrap();
        std::fs::copy(source.join("openapi.yml"), target.join("openapi.yml")).unwrap();
        copy_dir(&source.join("fern-expected"), &target.join("enums"));
    }
    replay_proofs(root, read_proofs(root));
    // A valid document bound to another document's untouched certified tree
    // must fail at the byte comparison, then recover when its source is restored.
    let first = root.join("cases/first/openapi.yml");
    let original = std::fs::read(&first).unwrap();
    std::fs::copy(root.join("cases/second/openapi.yml"), &first).unwrap();
    let failure = std::panic::catch_unwind(|| replay_proofs(root, read_proofs(root)))
        .expect_err("a mismatched document/tree binding must fail");
    let message = failure
        .downcast_ref::<String>()
        .expect("comparison diagnostic");
    assert!(
        message.contains("combo-replay-boundary first (PythonEnums)"),
        "{message}"
    );
    std::fs::write(&first, original).unwrap();
    replay_proofs(root, read_proofs(root));
}

fn replay_proofs(root: &Path, proofs: Vec<Proof>) {
    for proof in proofs {
        for mode in proof.modes {
            for (label, document) in [
                ("first", &proof.documents.first),
                ("second", &proof.documents.second),
                ("both", &proof.documents.both),
            ] {
                let spec = root.join(&document.document);
                let expected = root.join(document.tree(mode));
                let output = tempfile::tempdir().unwrap();
                crozier_clean_env()
                    .args(["--no-config", "generate", "python", "--spec"])
                    .arg(&spec)
                    .arg("--output")
                    .arg(output.path())
                    .args([
                        "--package-name",
                        "fern",
                        "--project-name",
                        "default_package_name",
                        "--enum-type",
                    ])
                    .arg(mode.cli_value())
                    .assert()
                    .success();
                let source = crozier::openapi::load(&spec).unwrap();
                let compared = parity::compare_trees_with_document(
                    &expected,
                    output.path(),
                    None,
                    true,
                    Some(source),
                )
                .unwrap_or_else(|error| panic!("{} {label} ({mode:?}): {error}", proof.key));
                assert!(
                    compared.differences.is_empty(),
                    "{} {label} ({mode:?}): {:?}",
                    proof.key,
                    compared.differences
                );
            }
        }
    }
}
