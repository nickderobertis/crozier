//! `notignored.yml` posts the suppressions review comment on a pull request.
//! Its effect is a comment on GitHub, which no local run can produce, so these
//! tests hold the properties that make it safe: it runs on pull requests with a
//! read-only tree and comment-only write grant, skips forks (whose token cannot
//! comment), sees the base branch it diffs against, and never becomes part of a
//! required check — a required context that skips on forks would block them.
//! Every context `ci.yml` reports is a candidate for branch protection, so the
//! job must share a name with none of them and none may depend on it.
// llmlint: ignore-file[new_code_lands_in_a_project] crozier is a Cargo crate driven by `just`, with no Nx workspace yet; this integration test sits in tests/ beside release_workflow.rs, its sibling workflow test, and runs under `just test`.

use serde_yaml_ng::{Mapping, Value};

const NOTIGNORED_WORKFLOW: &str = include_str!("../.github/workflows/notignored.yml");
const CI_WORKFLOW: &str = include_str!("../.github/workflows/ci.yml");
const FORK_GUARD: &str = "github.event.pull_request.head.repo.full_name == github.repository";

fn parse(source: &str) -> Value {
    serde_yaml_ng::from_str(source).expect("workflow is valid YAML")
}

fn jobs(workflow: &Value) -> &Mapping {
    workflow
        .get("jobs")
        .and_then(Value::as_mapping)
        .expect("workflow has jobs")
}

fn only_job(workflow: &Value) -> (&str, &Mapping) {
    let jobs = jobs(workflow);
    assert_eq!(jobs.len(), 1, "notignored.yml defines exactly one job");
    let (id, job) = jobs.iter().next().expect("one job");
    (
        id.as_str().expect("job ids are strings"),
        job.as_mapping().expect("the job is a mapping"),
    )
}

/// The context a job reports: its `name`, else its id.
fn context<'a>(id: &'a str, job: &'a Mapping) -> &'a str {
    job.get("name").and_then(Value::as_str).unwrap_or(id)
}

fn needs(job: &Mapping) -> Vec<String> {
    match job.get("needs") {
        None => Vec::new(),
        Some(Value::String(one)) => vec![one.clone()],
        Some(Value::Sequence(many)) => many
            .iter()
            .map(|need| need.as_str().expect("needs are job ids").to_owned())
            .collect(),
        Some(other) => panic!("unexpected needs: {other:?}"),
    }
}

#[test]
fn runs_on_pull_requests_only() {
    let workflow = parse(NOTIGNORED_WORKFLOW);
    let on = workflow
        .get("on")
        .expect("notignored.yml declares its trigger");
    let triggers: Vec<&str> = on
        .as_mapping()
        .expect("`on` is a mapping")
        .keys()
        .map(|key| key.as_str().expect("trigger names are strings"))
        .collect();
    assert_eq!(triggers, ["pull_request"]);
}

#[test]
fn grants_only_a_read_tree_and_a_pull_request_comment() {
    let workflow = parse(NOTIGNORED_WORKFLOW);
    let permissions = workflow
        .get("permissions")
        .and_then(Value::as_mapping)
        .expect("notignored.yml sets workflow permissions");
    let granted: Vec<(&str, &str)> = permissions
        .iter()
        .map(|(scope, level)| {
            (
                scope.as_str().expect("scopes are strings"),
                level.as_str().expect("levels are strings"),
            )
        })
        .collect();
    assert_eq!(granted, [("contents", "read"), ("pull-requests", "write")]);
    let (_, job) = only_job(&workflow);
    assert!(
        job.get("permissions").is_none(),
        "the job must not widen the workflow's grant"
    );
}

#[test]
fn skips_forks_and_checks_out_full_history_before_the_action() {
    let workflow = parse(NOTIGNORED_WORKFLOW);
    let (_, job) = only_job(&workflow);
    assert_eq!(job.get("if").and_then(Value::as_str), Some(FORK_GUARD));
    let steps = job
        .get("steps")
        .and_then(Value::as_sequence)
        .expect("the job has steps");
    let uses: Vec<&str> = steps
        .iter()
        .filter_map(|step| step.get("uses").and_then(Value::as_str))
        .collect();
    assert_eq!(
        uses,
        ["actions/checkout@v4", "nickderobertis/notignored@v0"]
    );
    let depth = steps[0]
        .get("with")
        .and_then(|with| with.get("fetch-depth"))
        .and_then(Value::as_u64);
    assert_eq!(
        depth,
        Some(0),
        "the scan diffs against the base branch, which a shallow checkout omits"
    );
}

#[test]
fn shares_no_context_with_ci_and_nothing_in_ci_needs_it() {
    let notignored = parse(NOTIGNORED_WORKFLOW);
    let (id, job) = only_job(&notignored);
    let own = context(id, job);

    let ci = parse(CI_WORKFLOW);
    let ci_jobs = jobs(&ci);
    for (ci_id, ci_job) in ci_jobs {
        let ci_id = ci_id.as_str().expect("job ids are strings");
        let ci_job = ci_job.as_mapping().expect("each job is a mapping");
        let name = context(ci_id, ci_job);
        assert_ne!(name, own, "notignored reports ci.yml's {name} context");
        let mut pending = needs(ci_job);
        let mut seen = Vec::new();
        while let Some(need) = pending.pop() {
            assert_ne!(need, id, "ci.yml's {name} needs notignored's job");
            if seen.contains(&need) {
                continue;
            }
            let upstream = ci_jobs
                .get(need.as_str())
                .and_then(Value::as_mapping)
                .unwrap_or_else(|| panic!("{name} needs unknown job {need}"));
            pending.extend(needs(upstream));
            seen.push(need);
        }
    }
}
