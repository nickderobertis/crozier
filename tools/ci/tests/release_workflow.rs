//! `release.yml` runs only on a published GitHub Release, so no pull request
//! exercises it. These tests hold the parts of it that have failed a tag's run
//! where CI passed: every Windows job must enable git's long paths before it
//! checks out, or the checkout fails on the deepest committed fixture paths.
//! The real checkout that proves the setting takes effect drives git, so it is
//! `ci-journeys`'s (`tools/ci-journeys/tests/release_checkout.rs`).

#[path = "support/release.rs"]
mod release;

use release::{str_of, windows_checkout_jobs, windows_pre_checkout_commands, workflow, LONG_PATHS};
use serde_json::Value;

#[test]
fn every_windows_release_job_enables_long_paths_before_checkout() {
    let jobs = windows_checkout_jobs();
    let ids: Vec<&str> = jobs.iter().map(|(id, _)| id.as_str()).collect();
    // The two jobs that failed at checkout since v0.0.32; if detection stops
    // finding them, the assertion below would pass over nothing.
    for expected in ["upload", "build-wheels"] {
        assert!(
            ids.contains(&expected),
            "{expected} no longer reads as a Windows job that checks out (found {ids:?})"
        );
    }
    for (id, steps) in &jobs {
        let commands = windows_pre_checkout_commands(steps);
        assert!(
            commands
                .iter()
                .any(|command| command.lines().any(|line| line.trim() == LONG_PATHS)),
            "release.yml job {id} checks out on Windows without first running \
             `{LONG_PATHS}`; add ci.yml's \"Enable Git long paths\" step before its \
             actions/checkout"
        );
    }
}

/// The floating major tag (`v0`) is what every `@v0` consumer of the GitHub
/// Action resolves, so it may move only after the release fully shipped: the
/// `major-tag` job waits on every publish and verify job and on the upload to
/// the GitHub Release, runs only when none of them failed (a skipped registry is
/// fine), and leaves the decision to `scripts/update-major-tag.sh`, which it
/// tells whether the Release is flagged as a pre-release.
const MOVE_MAJOR_TAG: &str = "Move the floating major tag onto this release";

#[test]
fn the_major_tag_job_moves_v0_only_after_every_publish_and_verify_job() {
    let workflow = workflow();
    let jobs = workflow
        .get("jobs")
        .and_then(Value::as_object)
        .expect("release.yml has jobs");
    let job = jobs
        .get("major-tag")
        .and_then(Value::as_object)
        .expect("release.yml has a major-tag job");

    let needs: Vec<&str> = job
        .get("needs")
        .and_then(Value::as_array)
        .expect("major-tag lists its needs")
        .iter()
        .map(|need| need.as_str().expect("each need is a job id"))
        .collect();
    let gated: Vec<&str> = jobs
        .keys()
        .map(|id| id.as_str())
        .filter(|id| *id == "upload" || id.starts_with("publish-") || id.starts_with("verify-"))
        .collect();
    assert!(
        gated.len() >= 6,
        "found too few publish/verify jobs to gate on: {gated:?}"
    );
    for id in &gated {
        assert!(
            needs.contains(id),
            "major-tag does not wait on {id}, so v0 could move onto a release whose {id} failed"
        );
    }
    assert_eq!(
        str_of(job, "if"),
        Some("${{ !failure() && !cancelled() && needs.upload.result == 'success' }}"),
        "major-tag must run only when no job it needs failed and the GitHub Release upload succeeded"
    );
    assert_eq!(
        job.get("permissions")
            .and_then(|permissions| permissions.get("contents"))
            .and_then(Value::as_str),
        Some("write"),
        "moving a tag needs contents: write, scoped to this job alone"
    );

    let steps = job
        .get("steps")
        .and_then(Value::as_array)
        .expect("major-tag has steps");
    let checkout = steps
        .iter()
        .find(|step| {
            step.get("uses")
                .and_then(Value::as_str)
                .is_some_and(|uses| uses.starts_with("actions/checkout@"))
        })
        .expect("major-tag checks the repository out");
    assert_eq!(
        checkout
            .get("with")
            .and_then(|with| with.get("fetch-depth"))
            .and_then(Value::as_u64),
        Some(0),
        "the newest-release decision needs every tag, which a shallow checkout lacks"
    );
    let runs: Vec<&str> = steps
        .iter()
        .filter_map(|step| step.get("run").and_then(Value::as_str))
        .filter(|run| run.contains("major-tag"))
        .collect();
    assert_eq!(
        runs,
        ["bash scripts/update-major-tag.sh --tag \"$GITHUB_REF_NAME\" --prerelease \"$PRERELEASE\""],
        "the tag decision belongs to scripts/update-major-tag.sh alone"
    );
    // The Release's own pre-release flag reaches the script through `env`,
    // never interpolated into the `run:` (crates/crozier-tool-journeys/tests/tool_journeys/major_tag.rs runs the step).
    let step = steps
        .iter()
        .find(|step| text(step, "name") == Some(MOVE_MAJOR_TAG))
        .expect("major-tag runs the script");
    assert_eq!(
        step.get("env")
            .and_then(|env| env.get("PRERELEASE"))
            .and_then(Value::as_str),
        Some("${{ github.event.release.prerelease }}"),
        "the script must be told when the Release is flagged as a pre-release"
    );
}

fn text<'a>(value: &'a Value, key: &str) -> Option<&'a str> {
    value.get(key).and_then(Value::as_str)
}

const PACKAGE_JSON: &str = include_str!("../../../package.json");
const BUDGETS: &str = include_str!("../../../budgets.yaml");

/// The release tail: `major-tag`'s final step reports budgets.yaml's `release-tail`
/// budgets, after the tag has moved, and nothing reads its result: no job needs
/// `major-tag`, and the step neither continues on error (so an over figure shows red) nor
/// writes outputs. Its tools are pinned: onevcs at the release dero-skills a73a309's
/// create-repo pins, onebudgetspec at package.json's pin. The shell this asserts is the one
/// `tools/ci-journeys/tests/release-tail.test.mjs` runs over recorded host answers.
/// The install step is held here by shape rather than run by that journey: running it
/// needs the npm registry, which an offline suite cannot reach. What it installs is
/// what the journey already drives: onebudgetspec at the pin asserted below, which the
/// journey runs from the workspace's node_modules, and onevcs, the host boundary the
/// journey doubles, whose pinned 0.57.6 answers were checked against the recordings.
#[test]
fn the_release_tail_is_the_last_step_of_major_tag_and_nothing_reads_it() {
    let workflow = workflow();
    let jobs = workflow
        .get("jobs")
        .and_then(Value::as_object)
        .expect("release.yml has jobs");
    for (id, job) in jobs {
        let needs: Vec<&str> = match job.get("needs") {
            Some(Value::String(need)) => vec![need.as_str()],
            Some(Value::Array(needs)) => needs.iter().filter_map(Value::as_str).collect(),
            _ => vec![],
        };
        assert!(
            !needs.contains(&"major-tag"),
            "{id} depends on the release tail's job"
        );
    }
    let job = &jobs["major-tag"];
    for (scope, level) in [
        ("contents", "write"),
        ("actions", "read"),
        ("pull-requests", "read"),
    ] {
        assert_eq!(
            job["permissions"].get(scope).and_then(Value::as_str),
            Some(level),
            "the tail reads runs, jobs and pull requests"
        );
    }
    let steps = job["steps"].as_array().expect("major-tag has steps");
    let names: Vec<&str> = steps.iter().filter_map(|step| text(step, "name")).collect();
    assert_eq!(
        names[names.len() - 3..],
        [
            MOVE_MAJOR_TAG,
            "Install onevcs and onebudgetspec for the release tail",
            "Report the release-tail budgets"
        ],
        "the tail runs after the tag has moved, last"
    );
    let tail = steps.last().unwrap();
    assert_eq!(
        text(tail, "run"),
        Some("onebudgetspec check budgets.yaml --label release-tail")
    );
    assert_eq!(text(tail, "shell"), Some("bash"));
    assert_eq!(
        tail["env"]
            .as_object()
            .map(|env| env.keys().collect::<Vec<_>>()),
        Some(vec![&"GH_TOKEN".to_string()])
    );
    assert_eq!(text(&tail["env"], "GH_TOKEN"), Some("${{ github.token }}"));
    for key in ["continue-on-error", "id", "if"] {
        assert!(tail.get(key).is_none(), "the tail step's {key}");
    }
    let package: Value = serde_json::from_str(PACKAGE_JSON).expect("package.json is JSON");
    let pin = package["devDependencies"]["@onebudgetspec/cli"]
        .as_str()
        .expect("package.json pins onebudgetspec");
    let install = text(&steps[steps.len() - 2], "run").expect("the install step runs");
    let words: Vec<&str> = install.split_whitespace().collect();
    for package in [
        format!("@onebudgetspec/cli@{pin}"),
        "onevcs-cli@0.57.6".to_string(),
    ] {
        assert!(
            words.contains(&package.as_str()),
            "{install} installs {package}"
        );
    }
    let budgets: Value = release::yaml::from_str(BUDGETS).expect("budgets.yaml is YAML");
    let tail_budgets: Vec<(&str, Vec<&str>)> = budgets["budgets"]
        .as_array()
        .expect("budgets.yaml lists budgets")
        .iter()
        .filter(|budget| {
            budget["labels"]
                .as_array()
                .is_some_and(|labels| labels.iter().any(|label| label == "release-tail"))
        })
        .map(|budget| {
            (
                budget["id"].as_str().unwrap(),
                budget["command"]
                    .as_array()
                    .unwrap()
                    .iter()
                    .map(|part| part.as_str().unwrap())
                    .collect(),
            )
        })
        .collect();
    assert_eq!(
        tail_budgets,
        [
            (
                "crozier-ci-check-time",
                vec![
                    "bash",
                    "scripts/actions-budget-figures.sh",
                    "longest-job",
                    "--stage",
                    "pr"
                ]
            ),
            (
                "crozier-ci-job-count",
                vec![
                    "bash",
                    "scripts/actions-budget-figures.sh",
                    "job-count",
                    "--stage",
                    "pr"
                ]
            ),
            (
                "crozier-pr-read-requests",
                vec![
                    "bash",
                    "scripts/actions-budget-figures.sh",
                    "pr-read-requests"
                ]
            ),
        ]
    );
}
