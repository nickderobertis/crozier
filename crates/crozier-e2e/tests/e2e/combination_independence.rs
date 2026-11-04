//! Replay each independent combination's three authored documents against its
//! complete certified trees through the real command line and parity engine.

use super::*;

#[derive(Clone, Copy, Debug, serde::Deserialize)]
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

#[test]
fn a_populated_independence_manifest_crosses_the_python_rust_boundary() {
    let scratch = tempfile::tempdir().unwrap();
    let manifest = scratch
        .path()
        .join("docs/openapi-surface/combination-independence.toml");
    std::fs::create_dir_all(manifest.parent().unwrap()).unwrap();
    let mut text = String::from(
        r#"schema_version = 1
[[combinations]]
key = "combo-parser-boundary"
modes = ["python_enums", "literals"]
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
    for label in ["first", "second", "both"] {
        text.push_str(&format!(
            "{label} = {{document = \"cases/{label}/openapi.yml\", python_enums = \"cases/{label}/enums\", literals = \"cases/{label}/literals\"}}\n"
        ));
    }
    std::fs::write(&manifest, text).unwrap();
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

// llmlint: ignore[expensive_tests_stay_behind_their_own_edge] This complete-tree replay belongs to the existing compiled-binary golden suite (crates/crozier-e2e/AGENTS.md), alongside corpus and hand-written replays using the same parity engine; splitting that family's graph edge is the existing generator-replay follow-up rather than a separate boundary introduced for this one comparison.
#[test]
fn independent_combination_documents_match_certified_trees() {
    let root = repo_root();
    let proofs = read_proofs(root);
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
