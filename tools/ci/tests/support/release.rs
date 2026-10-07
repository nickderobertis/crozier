//! The parts of `release.yml` both of its suites read: the workflow itself and
//! which commands each Windows job runs before it checks out. Included by path
//! from `tools/ci/tests/release_workflow.rs` (the structural contract) and
//! `tools/ci-journeys/tests/release_checkout.rs` (the real-git checkout journey).

use serde_yaml_ng::{Mapping, Value};

const RELEASE_WORKFLOW: &str = include_str!("../../../../.github/workflows/release.yml");
pub const LONG_PATHS: &str = "git config --global core.longpaths true";
/// The only step condition a pre-checkout step may carry; a new one would need
/// this test to decide whether it runs on Windows.
const WINDOWS_ONLY: &str = "runner.os == 'Windows'";

pub fn workflow() -> Value {
    serde_yaml_ng::from_str(RELEASE_WORKFLOW).expect("release.yml is valid YAML")
}

pub fn str_of<'a>(mapping: &'a Mapping, key: &str) -> Option<&'a str> {
    mapping.get(key).and_then(Value::as_str)
}

/// Every runner label a job can land on: its literal `runs-on`, or each
/// `os` its matrix supplies when `runs-on` is `${{ matrix.os }}`.
pub fn runner_labels(job: &Mapping) -> Vec<String> {
    let runs_on = str_of(job, "runs-on").expect("every release job names runs-on");
    if !runs_on.contains("matrix.os") {
        return vec![runs_on.to_owned()];
    }
    let matrix = job
        .get("strategy")
        .and_then(|strategy| strategy.get("matrix"))
        .and_then(Value::as_mapping)
        .expect("a job on matrix.os has a strategy.matrix");
    let listed = matrix
        .get("os")
        .and_then(Value::as_sequence)
        .into_iter()
        .flatten();
    let included = matrix
        .get("include")
        .and_then(Value::as_sequence)
        .into_iter()
        .flatten()
        .filter_map(|entry| entry.get("os"));
    listed
        .chain(included)
        .map(|os| os.as_str().expect("matrix os is a string").to_owned())
        .collect()
}

/// (job id, steps before its `actions/checkout`) for every job that can run on
/// a Windows runner and checks the repository out.
pub fn windows_checkout_jobs() -> Vec<(String, Vec<Mapping>)> {
    let workflow = workflow();
    let jobs = workflow
        .get("jobs")
        .and_then(Value::as_mapping)
        .expect("release.yml has jobs");
    let mut found = Vec::new();
    for (id, job) in jobs {
        let id = id.as_str().expect("job ids are strings");
        let job = job.as_mapping().expect("each job is a mapping");
        if !runner_labels(job)
            .iter()
            .any(|label| label.starts_with("windows"))
        {
            continue;
        }
        let steps: Vec<Mapping> = job
            .get("steps")
            .and_then(Value::as_sequence)
            .expect("each job has steps")
            .iter()
            .map(|step| step.as_mapping().expect("each step is a mapping").clone())
            .collect();
        let Some(checkout) = steps.iter().position(|step| {
            str_of(step, "uses").is_some_and(|uses| uses.starts_with("actions/checkout@"))
        }) else {
            continue;
        };
        found.push((id.to_owned(), steps[..checkout].to_vec()));
    }
    found
}

/// The `run` commands a Windows runner executes before the checkout.
pub fn windows_pre_checkout_commands(steps: &[Mapping]) -> Vec<String> {
    steps
        .iter()
        .filter(|step| match str_of(step, "if") {
            None => true,
            Some(condition) if condition == WINDOWS_ONLY => true,
            Some(other) => panic!(
                "pre-checkout step condition {other:?} is not one this test can evaluate; \
                 extend tools/ci/tests/support/release.rs to decide whether it runs on Windows"
            ),
        })
        .filter_map(|step| str_of(step, "run").map(str::to_owned))
        .collect()
}
