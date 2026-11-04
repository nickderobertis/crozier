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

#[test]
fn independent_combination_documents_match_certified_trees() {
    let root = repo_root();
    let reader = std::process::Command::new(
        python_interpreter().expect("Python to read the independence manifest"),
    )
    .arg(root.join("tools/surface-census/combination-independence.py"))
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
    let proofs: Vec<Proof> =
        serde_json::from_slice(&reader.stdout).expect("validated independence records");
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
