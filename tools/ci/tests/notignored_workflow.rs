//! The lint lane's notignored step posts the suppressions review comment on a pull
//! request. Its effect is a comment on GitHub, which no local run can produce, so these
//! tests hold the properties that make it safe: it runs on pull requests with a read-only
//! tree and a comment grant, skips forks (whose token cannot comment), sees the base
//! branch it diffs against, and stays a review artifact: a failed comment never fails
//! the required lane it sits in, and no second workflow or job runs it.

#[path = "../../../src/yaml.rs"]
mod yaml;

use serde_json::Value;

const CI_WORKFLOW: &str = include_str!("../../../.github/workflows/ci.yml");
const FORK_GUARD: &str = "github.event_name == 'pull_request' && github.event.pull_request.head.repo.full_name == github.repository";

fn lint() -> Value {
    let workflow: Value = crate::yaml::from_str(CI_WORKFLOW).expect("ci.yml is valid YAML");
    workflow
        .get("jobs")
        .and_then(|jobs| jobs.get("lint"))
        .cloned()
        .expect("ci.yml has a lint lane")
}

fn steps(job: &Value) -> Vec<Value> {
    job.get("steps")
        .and_then(Value::as_array)
        .expect("the job has steps")
        .clone()
}

fn is_notignored(step: &Value) -> bool {
    step.get("uses")
        .and_then(Value::as_str)
        .is_some_and(|uses| uses.starts_with("nickderobertis/notignored@"))
}

#[test]
fn runs_as_one_step_of_the_lint_lane_alone() {
    let workflow: Value = crate::yaml::from_str(CI_WORKFLOW).expect("ci.yml is valid YAML");
    let mut found = Vec::new();
    for (id, job) in workflow.get("jobs").and_then(Value::as_object).unwrap() {
        let Some(job_steps) = job.get("steps").and_then(Value::as_array) else {
            continue;
        };
        found.extend(
            job_steps
                .iter()
                .filter(|step| is_notignored(step))
                .map(|_| id.clone()),
        );
    }
    assert_eq!(found, ["lint"]);
}

#[test]
fn grants_only_what_the_comment_and_gallery_need() {
    let job = lint();
    let permissions = job
        .get("permissions")
        .and_then(Value::as_object)
        .expect("the lane sets its permissions");
    assert_eq!(
        permissions.get("pull-requests").and_then(Value::as_str),
        Some("write"),
        "the comment"
    );
    let workflow: Value = crate::yaml::from_str(CI_WORKFLOW).expect("ci.yml is valid YAML");
    assert_eq!(
        workflow
            .get("permissions")
            .and_then(|permissions| permissions.get("contents"))
            .and_then(Value::as_str),
        Some("read"),
        "every other job stays read-only"
    );
}

#[test]
fn skips_forks_and_checks_out_full_history_before_the_action() {
    let job = lint();
    let steps = steps(&job);
    let at = steps
        .iter()
        .position(is_notignored)
        .expect("the lane runs notignored");
    assert_eq!(
        steps[at].get("if").and_then(Value::as_str),
        Some(FORK_GUARD)
    );
    let checkout = steps[..at]
        .iter()
        .find(|step| {
            step.get("uses")
                .and_then(Value::as_str)
                .is_some_and(|uses| uses.starts_with("actions/checkout@"))
        })
        .expect("the lane checks out before it");
    assert_eq!(
        checkout
            .get("with")
            .and_then(|with| with.get("fetch-depth"))
            .and_then(Value::as_u64),
        Some(0),
        "the scan diffs against the base branch, which a shallow checkout omits"
    );
}

#[test]
fn a_failed_comment_does_not_fail_the_required_lane() {
    let job = lint();
    let steps = steps(&job);
    let step = steps
        .iter()
        .find(|step| is_notignored(step))
        .expect("the lane runs notignored");
    assert_eq!(
        step.get("continue-on-error").and_then(Value::as_bool),
        Some(true),
        "a review artifact, not a gate"
    );
}
