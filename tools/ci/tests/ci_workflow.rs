//! Pins `ci.yml`'s `pull_request` trigger types; the reason is the comment
//! beside them.

#[path = "../../../src/yaml.rs"]
mod yaml;

use serde_json::Value;

const CI_WORKFLOW: &str = include_str!("../../../.github/workflows/ci.yml");

#[test]
fn marking_a_draft_ready_does_not_rerun_ci() {
    let workflow: Value = crate::yaml::from_str(CI_WORKFLOW).expect("ci.yml is valid YAML");
    let types: Vec<&str> = workflow
        .get("on")
        .and_then(|on| on.get("pull_request"))
        .and_then(|pull_request| pull_request.get("types"))
        .and_then(Value::as_array)
        .expect("ci.yml lists its pull_request types")
        .iter()
        .map(|kind| kind.as_str().expect("types are strings"))
        .collect();
    assert_eq!(
        types,
        ["opened", "synchronize", "reopened"],
        "ci.yml keeps the default pull_request types and does not add ready_for_review"
    );
}

const RELEASE_WORKFLOW: &str = include_str!("../../../.github/workflows/release.yml");

fn job<'a>(workflow: &'a Value, name: &str) -> &'a Value {
    workflow
        .get("jobs")
        .and_then(|jobs| jobs.get(name))
        .unwrap_or_else(|| panic!("the workflow has no `{name}` job"))
}

fn text<'a>(value: &'a Value, key: &str) -> Option<&'a str> {
    value.get(key).and_then(Value::as_str)
}

fn steps(job: &Value) -> &[Value] {
    job.get("steps")
        .and_then(Value::as_array)
        .expect("the job has steps")
}

/// The contexts branch protection requires today are reported on every pull request
/// under exactly their names: no path or branch filter on `pull_request`, and each
/// job's condition is the one that keeps it reporting. `gate` aggregates the four lanes
/// and the two transitional checks, and is the only job with a `needs` edge.
#[test]
fn the_required_contexts_report_on_every_pull_request() {
    let workflow: Value = crate::yaml::from_str(CI_WORKFLOW).expect("ci.yml is valid YAML");
    let pull_request = workflow
        .get("on")
        .and_then(|on| on.get("pull_request"))
        .expect("ci.yml runs on pull_request");
    for filter in ["paths", "paths-ignore", "branches", "branches-ignore"] {
        assert!(
            pull_request.get(filter).is_none(),
            "a `{filter}` filter on pull_request could leave a required context unreported"
        );
    }
    for (name, condition) in [
        (
            "gate",
            Some("always() && github.event_name == 'pull_request'"),
        ),
        ("commitlint", Some("github.event_name == 'pull_request'")),
        (
            "llmlint",
            Some("github.event_name == 'pull_request' && github.event.action != 'edited'"),
        ),
    ] {
        let job = job(&workflow, name);
        assert_eq!(
            text(job, "name"),
            Some(name),
            "the `{name}` context's job name"
        );
        assert_eq!(text(job, "if"), condition, "the `{name}` job's condition");
    }
    let needs: Vec<&str> = job(&workflow, "gate")
        .get("needs")
        .and_then(Value::as_array)
        .expect("gate aggregates its legs")
        .iter()
        .map(|need| need.as_str().expect("needs are job ids"))
        .collect();
    assert_eq!(
        needs,
        [
            "lint",
            "test-linux",
            "test-windows",
            "test-macos",
            "commitlint",
            "llmlint"
        ]
    );
    for (name, job) in workflow.get("jobs").and_then(Value::as_object).unwrap() {
        assert!(
            name.as_str() == "gate" || job.get("needs").is_none(),
            "{name} waits on another job; only the transitional gate may"
        );
    }
}

const LANES: [&str; 4] = ["lint", "test-linux", "test-windows", "test-macos"];

/// Every lane goes through the recipes that derive its base, with the history that
/// base needs; none runs the gate or Nx directly; and each lane's scopes between them
/// are the groups the projects' own tags declare.
#[test]
fn every_lane_routes_its_tier_through_the_ci_recipes() {
    let workflow: Value = crate::yaml::from_str(CI_WORKFLOW).expect("ci.yml is valid YAML");
    let mut scopes = Vec::new();
    for name in LANES {
        let job = job(&workflow, name);
        let checkout = steps(job)
            .iter()
            .find(|step| {
                text(step, "uses").is_some_and(|uses| uses.starts_with("actions/checkout"))
            })
            .expect("the job checks out");
        assert_eq!(
            checkout
                .get("with")
                .and_then(|with| with.get("fetch-depth"))
                .and_then(Value::as_u64),
            Some(0),
            "{name}: the affected base must be in the checkout"
        );
        assert!(
            !steps(job).iter().any(|step| text(step, "run")
                .is_some_and(|run| run.starts_with("just check") || run.contains(" nx "))),
            "{name}: the tier comes from the ci recipes, never a second gate or Nx directly"
        );
        scopes.push(
            steps(job)
                .iter()
                .filter_map(|step| text(step, "run"))
                .filter(|run| run.starts_with("just ci-"))
                .collect::<Vec<_>>(),
        );
    }
    let offline = "just ci-test --exclude=tag:tier:promoted";
    let sdk = "just ci-test --projects=tag:lane:sdk-env";
    assert_eq!(
        scopes,
        [
            vec!["just ci-lint"],
            vec![
                "just ci-test --projects=tag:lane:packaging",
                offline,
                sdk,
                "just ci-budgets-host",
                "just ci-test --projects=tag:lane:live",
            ],
            vec![offline, sdk],
            vec![offline, sdk],
        ]
    );
}

/// `just bootstrap` syncs the Python tooling's uv workspace (`just sync-python`)
/// and every Python target runs under `uv run`, but GitHub runners carry no uv:
/// every job that bootstraps, in either workflow, installs uv before it does.
#[test]
fn every_job_that_bootstraps_installs_uv_first() {
    let mut bootstrapping = Vec::new();
    for (file, source) in [("ci.yml", CI_WORKFLOW), ("release.yml", RELEASE_WORKFLOW)] {
        let workflow: Value =
            crate::yaml::from_str(source).unwrap_or_else(|_| panic!("{file} is valid YAML"));
        let jobs = workflow
            .get("jobs")
            .and_then(Value::as_object)
            .unwrap_or_else(|| panic!("{file} has jobs"));
        for (name, job) in jobs {
            let name = name.as_str();
            let Some(steps) = job.get("steps").and_then(Value::as_array) else {
                continue;
            };
            let Some(bootstrap) = steps
                .iter()
                .position(|step| text(step, "run") == Some("just bootstrap"))
            else {
                continue;
            };
            let uv = steps.iter().position(|step| {
                text(step, "uses").is_some_and(|uses| uses.starts_with("astral-sh/setup-uv@"))
            });
            assert!(
                uv.is_some_and(|uv| uv < bootstrap),
                "{file}: job `{name}` runs `just bootstrap` without installing uv first"
            );
            bootstrapping.push(format!("{file}:{name}"));
        }
    }
    bootstrapping.sort();
    assert_eq!(
        bootstrapping,
        [
            "ci.yml:lint",
            "ci.yml:test-linux",
            "ci.yml:test-macos",
            "ci.yml:test-windows"
        ],
        "the jobs that bootstrap"
    );
}

/// Every test lane holds what its projects run before the first recipe starts them:
/// cargo-nextest, which the e2e and corpus-match targets run under, and a toolchain
/// installed once by `just bootstrap`, so the gate's parallel cargo tasks never race
/// one first-use rustup install.
#[test]
fn every_lane_installs_nextest_and_its_toolchain_before_the_gate() {
    let workflow: Value = crate::yaml::from_str(CI_WORKFLOW).expect("ci.yml is valid YAML");
    for name in LANES {
        let steps = steps(job(&workflow, name));
        let gate = steps
            .iter()
            .position(|step| text(step, "run").is_some_and(|run| run.starts_with("just ci-")))
            .unwrap_or_else(|| panic!("{name} runs no `just ci-` step"));
        let before = &steps[..gate];
        assert!(
            before.iter().any(|step| {
                text(step, "uses").is_some_and(|uses| uses.starts_with("taiki-e/install-action"))
                    && step
                        .get("with")
                        .and_then(|with| text(with, "tool"))
                        .is_some_and(|tools| tools.split(',').any(|tool| tool == "cargo-nextest"))
            }),
            "{name}: cargo-nextest is installed before the gate"
        );
        assert!(
            before
                .iter()
                .any(|step| text(step, "run") == Some("just bootstrap")),
            "{name}: the pinned toolchain is installed once before the gate"
        );
    }
}

/// Each cached result's key holds what Nx does not hash: the OS and architecture, the
/// host's tools, every lock, the toolchain and the generator pin, and the workflow.
/// The key of an earlier commit is only a starting point: Nx replays a result only for
/// an unchanged input hash.
#[test]
fn every_lane_keys_its_results_on_the_host_and_its_pins() {
    let workflow: Value = crate::yaml::from_str(CI_WORKFLOW).expect("ci.yml is valid YAML");
    for name in LANES {
        let steps = steps(job(&workflow, name));
        let cache = steps
            .iter()
            .find(|step| text(step, "uses").is_some_and(|uses| uses.starts_with("actions/cache@")))
            .unwrap_or_else(|| panic!("{name} restores no results"));
        let with = cache.get("with").expect("the cache step has inputs");
        assert_eq!(text(with, "path"), Some(".nx/cache"));
        let key = text(with, "key").expect("the cache step has a key");
        for part in [
            "github.job",
            "runner.os",
            "runner.arch",
            "steps.host.outputs.key",
            "bun.lock",
            "Cargo.lock",
            "uv.lock",
            "rust-toolchain.toml",
            ".cargo/config.toml",
            ".ruff-version",
            ".github/workflows/ci.yml",
            "github.sha",
        ] {
            assert!(key.contains(part), "{name}: the key omits {part}: {key}");
        }
        assert_eq!(
            text(with, "restore-keys"),
            key.strip_suffix("${{ github.sha }}"),
            "{name}: the fallback differs only by commit"
        );
        let host = steps
            .iter()
            .position(|step| text(step, "id") == Some("host"))
            .expect("the host key step");
        let bootstrap = steps
            .iter()
            .position(|step| text(step, "run") == Some("just bootstrap"))
            .expect("the lane bootstraps");
        assert!(
            bootstrap < host,
            "{name}: the key reads the installed tools"
        );
        assert!(text(&steps[host], "run")
            .unwrap()
            .contains("tools/ci/suite-cases/cache-key.mjs"));
    }
}

/// The pool-maintenance budget builds the repository twice, so it runs only where the
/// project is affected, through its recipe in the Linux lane; no other job in either
/// workflow runs it, and the release branch's skip is not its only invocation.
#[test]
fn the_pool_maintenance_budget_runs_in_the_linux_lane_when_affected() {
    let workflow: Value = crate::yaml::from_str(CI_WORKFLOW).expect("ci.yml is valid YAML");
    let lane = job(&workflow, "test-linux");
    let runs: Vec<&str> = steps(lane)
        .iter()
        .filter_map(|step| text(step, "run"))
        .collect();
    let pruner = runs.iter().position(|run| *run == "just install-pruner");
    let budget = runs.iter().position(|run| *run == "just ci-budgets-host");
    assert!(pruner.is_some_and(|pruner| Some(pruner) < budget));
    for (file, source) in [("ci.yml", CI_WORKFLOW), ("release.yml", RELEASE_WORKFLOW)] {
        let workflow: Value =
            crate::yaml::from_str(source).unwrap_or_else(|_| panic!("{file} is valid YAML"));
        for (name, job) in workflow.get("jobs").and_then(Value::as_object).unwrap() {
            if file == "ci.yml" && name == "test-linux" {
                continue;
            }
            let Some(steps) = job.get("steps").and_then(Value::as_array) else {
                continue;
            };
            assert!(
                !steps.iter().any(|step| text(step, "run")
                    .is_some_and(|run| run.contains("budgets-host")
                        || run.contains("budgets-pool-maintenance")
                        || run.contains("pool-maintenance:budgets"))),
                "{file}: job `{name}` runs the pool-maintenance budget"
            );
        }
    }
}

/// CD builds, installs and publishes what a pull request proved: no release job runs
/// the gate again.
#[test]
fn the_release_workflow_runs_no_test_sweep() {
    let workflow: Value =
        crate::yaml::from_str(RELEASE_WORKFLOW).expect("release.yml is valid YAML");
    let jobs = workflow.get("jobs").and_then(Value::as_object).unwrap();
    assert!(jobs.get("test").is_none(), "release.yml has no test job");
    for (name, job) in jobs {
        let Some(steps) = job.get("steps").and_then(Value::as_array) else {
            continue;
        };
        assert!(
            !steps.iter().any(|step| text(step, "run")
                .is_some_and(|run| run.contains("just check") || run.contains("just ci-"))),
            "release.yml: job `{name}` runs the gate"
        );
    }
}

const GOLDEN_REACH_BASE: &str = include_str!("../../../.github/workflows/golden-reach-base.yml");

/// The golden-reach base `just census-repin` steps from: published on each push
/// to main, a newer push cancelling a run in progress, with only the read access
/// its measurement and upload need, by the recipe `census-repin` reads bases from
/// (`tools/surface-census/tests/repin_base_test.py` finds what it packages). A
/// measurement artifact in a workflow of its own, which no pull request push starts.
#[test]
fn the_golden_reach_base_is_published_for_each_push_to_main() {
    let workflow: Value =
        crate::yaml::from_str(GOLDEN_REACH_BASE).expect("golden-reach-base.yml is valid YAML");
    let triggers: Vec<&str> = workflow
        .get("on")
        .and_then(Value::as_object)
        .expect("the workflow names its triggers")
        .keys()
        .map(|key| key.as_str())
        .collect();
    assert_eq!(triggers, ["push"], "no pull request push starts it");
    let branches: Vec<&str> = workflow
        .get("on")
        .and_then(|on| on.get("push"))
        .and_then(|push| push.get("branches"))
        .and_then(Value::as_array)
        .expect("it runs on pushes to named branches")
        .iter()
        .map(|branch| branch.as_str().expect("branches are strings"))
        .collect();
    assert_eq!(branches, ["main"], "its push trigger is main alone");
    let ci: Value = crate::yaml::from_str(CI_WORKFLOW).expect("ci.yml is valid YAML");
    assert!(
        ci.get("on").and_then(|on| on.get("push")).is_none(),
        "ci.yml does not run on a push"
    );
    let job = job(&workflow, "golden-reach-base");
    let concurrency = job
        .get("concurrency")
        .expect("the job has a concurrency group");
    assert_eq!(text(concurrency, "group"), Some("golden-reach-base"));
    assert_eq!(
        concurrency
            .get("cancel-in-progress")
            .and_then(Value::as_bool),
        Some(true),
        "a newer push cancels a base measurement in progress"
    );
    let permissions = job
        .get("permissions")
        .and_then(Value::as_object)
        .expect("the job states its permissions");
    let granted: Vec<(&str, &str)> = permissions
        .iter()
        .map(|(scope, level)| (scope.as_str(), level.as_str().expect("levels are strings")))
        .collect();
    assert_eq!(
        granted,
        [("contents", "read"), ("actions", "read")],
        "checkout and the earlier base's download read; the upload needs no grant"
    );
    let steps = steps(job);
    assert!(
        steps.iter().any(|step| text(step, "run")
            == Some("just golden-reach-base \"$RUNNER_TEMP/golden-reach-base\"")),
        "the job measures through the `golden-reach-base` recipe"
    );
    let upload = steps
        .iter()
        .find(|step| {
            text(step, "uses").is_some_and(|uses| uses.starts_with("actions/upload-artifact"))
        })
        .and_then(|step| step.get("with"))
        .expect("the job uploads an artifact");
    assert_eq!(
        text(upload, "name"),
        Some("golden-reach-base-${{ github.sha }}")
    );
    assert_eq!(
        text(upload, "path"),
        Some("${{ runner.temp }}/golden-reach-base/base.json.gz")
    );
    assert_eq!(
        upload.get("retention-days").and_then(Value::as_u64),
        Some(90)
    );
}
