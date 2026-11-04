//! Residuals measured after the handed-off repairs, against complete certified trees.

use super::{probe_command, repo_root};

pub(crate) const DIR: &str = "docs/fern-measurements/handed-off/remeasure";

fn generate(cause: &str) -> (tempfile::TempDir, std::path::PathBuf, std::path::PathBuf) {
    let work = tempfile::tempdir().expect("measurement output");
    let out = work.path().join("sdk");
    let case = repo_root().join(DIR).join(cause);
    probe_command(&case.join("openapi.yml"), &out)
        .assert()
        .success();
    let comparison = crozier::parity::compare_trees(&case.join("fern-expected"), &out, None, true)
        .expect("compare the complete generated SDK");
    assert!(comparison.differences.is_empty(), "{comparison:#?}");
    (work, case, out)
}

#[test]
fn remeasure_collapsed_body_keeps_the_shared_model_and_documents_accepted_fields() {
    let (_work, case, out) = generate("json-ref-body-kept-whole");
    assert!(out.join("src/fern/types/label_registration.py").is_file());
    let raw = std::fs::read_to_string(out.join("src/fern/raw_client.py")).unwrap();
    assert!(raw.contains("label: str"));
    assert!(!raw.contains("\"content-type\""));
    let reference = std::fs::read_to_string(out.join("reference.md")).unwrap();
    assert!(reference.contains("**label:** `str`"));
    assert!(!reference.contains("**request:**"));
    std::fs::write(
        out.join("reference.md"),
        reference.replace("**label:** `str`", "**label:** `int`"),
    )
    .unwrap();
    let adjacent =
        crozier::parity::compare_trees(&case.join("fern-expected"), &out, None, false).unwrap();
    assert!(adjacent
        .differences
        .iter()
        .any(|(path, _)| path == "reference.md"));
}

#[test]
fn remeasure_split_media_body_writes_no_unreferenced_json_model() {
    let (_work, case, out) = generate("split-media-body-orphan-model");
    let model = out.join("src/fern/types/recording_url.py");
    assert!(!model.exists());
    std::fs::create_dir_all(model.parent().unwrap()).unwrap();
    std::fs::write(&model, "class RecordingUrl:\n    url: str\n").unwrap();
    let adjacent =
        crozier::parity::compare_trees(&case.join("fern-expected"), &out, None, false).unwrap();
    assert!(adjacent
        .differences
        .iter()
        .any(|(path, _)| path.ends_with("recording_url.py")));
}
