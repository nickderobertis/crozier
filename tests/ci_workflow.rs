//! `ci.yml` reports the required contexts on every pull request. A draft that is
//! lifted to ready for review must re-run them on its head: the default
//! `pull_request` types omit `ready_for_review`, so without it the lift reports
//! nothing new and the merge path is left reading draft-time runs.
// llmlint: ignore-file[new_code_lands_in_a_project] crozier is a Cargo crate driven by `just`, with no Nx workspace yet; this integration test sits in tests/ beside notignored_workflow.rs, its sibling workflow test, and runs under `just test`.

use serde_yaml_ng::Value;

const CI_WORKFLOW: &str = include_str!("../.github/workflows/ci.yml");

#[test]
fn pull_requests_rerun_when_a_draft_is_marked_ready() {
    let workflow: Value = serde_yaml_ng::from_str(CI_WORKFLOW).expect("ci.yml is valid YAML");
    let types: Vec<&str> = workflow
        .get("on")
        .and_then(|on| on.get("pull_request"))
        .and_then(|pull_request| pull_request.get("types"))
        .and_then(Value::as_sequence)
        .expect("ci.yml lists its pull_request types")
        .iter()
        .map(|kind| kind.as_str().expect("types are strings"))
        .collect();
    assert_eq!(
        types,
        ["opened", "synchronize", "reopened", "ready_for_review"],
        "ci.yml keeps the default pull_request types and adds ready_for_review"
    );
}
