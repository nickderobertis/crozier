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

const GOVERNANCE: &str = include_str!("../../../.github/governance.json");

/// The contexts branch protection requires, as `.github/governance.json` declares them.
fn required_checks() -> Vec<String> {
    let governance: Value = serde_json::from_str(GOVERNANCE).expect("governance.json is JSON");
    governance["required_checks"]
        .as_array()
        .expect("governance lists its checks")
        .iter()
        .map(|check| check.as_str().expect("checks are strings").to_string())
        .collect()
}

/// Every committed workflow, by file name, read from disk so a workflow added beside the
/// others is counted without anyone listing it here.
fn every_workflow() -> Vec<(String, Value)> {
    let dir = std::path::Path::new(env!("CARGO_MANIFEST_DIR")).join("../../.github/workflows");
    let mut files: Vec<_> = std::fs::read_dir(&dir)
        .expect("read .github/workflows")
        .map(|entry| entry.expect("a directory entry").path())
        .filter(|path| {
            path.extension()
                .is_some_and(|ext| ext == "yml" || ext == "yaml")
        })
        .collect();
    files.sort();
    files
        .into_iter()
        .map(|path| {
            let name = path.file_name().unwrap().to_string_lossy().into_owned();
            let source = std::fs::read_to_string(&path).expect("read a workflow");
            let value =
                crate::yaml::from_str(&source).unwrap_or_else(|_| panic!("{name} is valid YAML"));
            (name, value)
        })
        .collect()
}

/// Whether a pull request push (`opened`, `synchronize` or `reopened`) starts the workflow.
/// GitHub's default types are exactly those three.
fn starts_on_a_pull_request_push(file: &str, workflow: &Value) -> bool {
    let on = workflow
        .get("on")
        .unwrap_or_else(|| panic!("{file} names its triggers"));
    let config = match on {
        Value::String(event) => (event == "pull_request").then_some(&Value::Null),
        Value::Array(events) => events
            .iter()
            .any(|event| event.as_str() == Some("pull_request"))
            .then_some(&Value::Null),
        Value::Object(events) => {
            for unsupported in ["pull_request_target", "workflow_run"] {
                assert!(
                    !events.contains_key(unsupported),
                    "{file}: `{unsupported}` starts a run a pull request causes, outside the lanes"
                );
            }
            events.get("pull_request")
        }
        _ => panic!("{file}: unreadable triggers"),
    };
    let Some(config) = config else {
        return false;
    };
    let types: Vec<&str> = match config.get("types") {
        None => vec!["opened", "synchronize", "reopened"],
        Some(types) => types
            .as_array()
            .unwrap_or_else(|| panic!("{file}: pull_request types are a list"))
            .iter()
            .map(|kind| kind.as_str().expect("types are strings"))
            .collect(),
    };
    types
        .iter()
        .any(|kind| ["opened", "synchronize", "reopened"].contains(kind))
}

/// The legs of a job's matrix, expanded as GitHub expands it: the product of its axes,
/// less `exclude`, plus each `include` that matches no leg. A matrix computed at run time
/// cannot be counted here, so it fails rather than counting as one job.
fn matrix_legs(file: &str, id: &str, job: &Value) -> usize {
    let Some(matrix) = job
        .get("strategy")
        .and_then(|strategy| strategy.get("matrix"))
    else {
        return 1;
    };
    let matrix = matrix
        .as_object()
        .unwrap_or_else(|| panic!("{file}:{id}: a computed matrix's legs cannot be counted"));
    let mut legs: Vec<serde_json::Map<String, Value>> = vec![serde_json::Map::new()];
    for (axis, values) in matrix {
        if axis == "include" || axis == "exclude" {
            continue;
        }
        let values = values
            .as_array()
            .unwrap_or_else(|| panic!("{file}:{id}: matrix axis {axis} is not a list"));
        legs = legs
            .into_iter()
            .flat_map(|leg| {
                values.iter().map(move |value| {
                    let mut next = leg.clone();
                    next.insert(axis.clone(), value.clone());
                    next
                })
            })
            .collect();
    }
    let rows = |key: &str| -> Vec<serde_json::Map<String, Value>> {
        matrix.get(key).map_or_else(Vec::new, |rows| {
            rows.as_array()
                .unwrap_or_else(|| panic!("{file}:{id}: matrix {key} is not a list"))
                .iter()
                .map(|row| row.as_object().expect("matrix rows are mappings").clone())
                .collect()
        })
    };
    let matches = |leg: &serde_json::Map<String, Value>, row: &serde_json::Map<String, Value>| {
        row.iter()
            .all(|(key, value)| leg.get(key).is_none_or(|have| have == value))
    };
    let excluded = rows("exclude");
    legs.retain(|leg| {
        !excluded
            .iter()
            .any(|row| matches(leg, row) && row.keys().all(|key| leg.contains_key(key)))
    });
    let axes = matrix
        .keys()
        .any(|key| key != "include" && key != "exclude");
    let mut count = if axes { legs.len() } else { 0 };
    for row in rows("include") {
        if !axes || !legs.iter().any(|leg| matches(leg, &row)) {
            count += 1;
        }
    }
    count
}

/// Every job a pull request push starts, over every workflow, through every local reusable
/// workflow, one entry per matrix leg: `(workflow, job id, context, job)`. A remote reusable
/// workflow's jobs are slots this cannot see, so one fails the expansion.
fn pull_request_push_jobs() -> Vec<(String, String, String, Value)> {
    fn expand(
        file: &str,
        workflow: &Value,
        prefix: &str,
        into: &mut Vec<(String, String, String, Value)>,
    ) {
        let jobs = workflow
            .get("jobs")
            .and_then(Value::as_object)
            .unwrap_or_else(|| panic!("{file} has jobs"));
        for (id, job) in jobs {
            let context = format!("{prefix}{}", text(job, "name").unwrap_or(id));
            if let Some(uses) = text(job, "uses") {
                let local = uses
                    .strip_prefix("./.github/workflows/")
                    .unwrap_or_else(|| {
                        panic!("{file}:{id} calls {uses}, whose jobs cannot be counted")
                    });
                let path = std::path::Path::new(env!("CARGO_MANIFEST_DIR"))
                    .join("../../.github/workflows")
                    .join(local);
                let callee: Value = crate::yaml::from_str(
                    &std::fs::read_to_string(&path)
                        .unwrap_or_else(|_| panic!("{file}:{id} calls a missing {local}")),
                )
                .unwrap_or_else(|_| panic!("{local} is valid YAML"));
                // A matrix over a reusable call starts the callee once per leg.
                for _ in 0..matrix_legs(file, id, job) {
                    expand(local, &callee, &format!("{context} / "), into);
                }
                continue;
            }
            for _ in 0..matrix_legs(file, id, job) {
                into.push((file.to_string(), id.clone(), context.clone(), job.clone()));
            }
        }
    }
    let mut jobs = Vec::new();
    for (file, workflow) in every_workflow() {
        if starts_on_a_pull_request_push(&file, &workflow) {
            expand(&file, &workflow, "", &mut jobs);
        }
    }
    jobs
}

/// The required contexts are reported on every pull request under exactly their names, and
/// nothing else runs: expanding every workflow a pull request push starts, every reusable
/// call and every matrix leg yields the four lanes `.github/governance.json` declares, once
/// each, in `ci.yml` alone. No lane waits on another, each holds the timeout that lets
/// its work on main finish, and no path or branch filter can leave a context unreported.
#[test]
fn a_pull_request_push_runs_exactly_the_governed_lanes() {
    let expanded = pull_request_push_jobs();
    let contexts: Vec<&str> = expanded
        .iter()
        .map(|(_, _, context, _)| context.as_str())
        .collect();
    assert_eq!(
        contexts,
        required_checks(),
        "the jobs a pull request push starts"
    );
    for (file, id, _, job) in &expanded {
        assert_eq!(
            file, "ci.yml",
            "{id} runs in a separately triggered workflow"
        );
        assert!(job.get("needs").is_none(), "{id} waits on another job");
        assert!(job.get("name").is_none(), "{id}'s context is its job id");
        // At or above what each lane's records on main show.
        let ceiling = match id.as_str() {
            "lint" => 30,
            "test-linux" => 150,
            "test-windows" => 150,
            "test-macos" => 150,
            other => panic!("{other} is not a lane"),
        };
        assert_eq!(
            job.get("timeout-minutes").and_then(Value::as_u64),
            Some(ceiling),
            "{id}'s timeout-minutes"
        );
    }
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
    assert!(
        workflow.get("on").and_then(|on| on.get("push")).is_none(),
        "ci.yml does not run on a push, to main or anywhere"
    );
    // Main runs no CI: whatever a push to main starts reports none of the required contexts.
    for (file, workflow) in every_workflow() {
        if workflow.get("on").and_then(|on| on.get("push")).is_some() {
            assert_reports_no_required_context(&file, &workflow);
        }
    }
}

/// The expansion counts what it cannot see as a failure rather than as nothing: a matrix leg
/// is a job, a computed matrix or a remote reusable workflow fails, and a `pull_request`
/// workflow with default types is counted as starting on a push.
#[test]
fn the_expansion_counts_matrix_legs_and_refuses_what_it_cannot_resolve() {
    let job = |source: &str| -> Value { crate::yaml::from_str(source).expect("valid YAML") };
    assert_eq!(matrix_legs("t.yml", "j", &job("runs-on: x\n")), 1);
    assert_eq!(
        matrix_legs("t.yml", "j", &job("strategy:\n  matrix:\n    os: [a, b, c]\n    exclude:\n      - os: b\n    include:\n      - os: c\n        extra: 1\n      - os: d\n")),
        3,
        "a and c, plus the include matching no leg"
    );
    assert_eq!(
        matrix_legs(
            "t.yml",
            "j",
            &job("strategy:\n  matrix:\n    include:\n      - target: a\n      - target: b\n")
        ),
        2
    );
    let computed = job("strategy:\n  matrix: ${{ fromJSON(needs.plan.outputs.matrix) }}\n");
    assert!(std::panic::catch_unwind(|| matrix_legs("t.yml", "j", &computed)).is_err());
    for (on, starts) in [
        ("on: pull_request\n", true),
        ("on: [push, pull_request]\n", true),
        ("on:\n  pull_request:\n", true),
        ("on:\n  pull_request:\n    types: [closed]\n", false),
        ("on:\n  push:\n    branches: [main]\n", false),
    ] {
        assert_eq!(
            starts_on_a_pull_request_push("t.yml", &job(on)),
            starts,
            "{on}"
        );
    }
    let target = job("on:\n  pull_request_target:\n");
    assert!(std::panic::catch_unwind(|| starts_on_a_pull_request_push("t.yml", &target)).is_err());
}

/// The test lanes skip a same-repository `release-plz-` branch, and only that: lint has no
/// condition, so on that branch it is the one job that executes, and its release guard step
/// runs under the same predicate, so the skip is held to the release tool's own edits
/// (`tools/ci-journeys/tests/release-guard.test.mjs` drives the guard).
#[test]
fn only_lint_executes_on_the_content_guarded_release_branch() {
    let workflow: Value = crate::yaml::from_str(CI_WORKFLOW).expect("ci.yml is valid YAML");
    let release = "github.event.pull_request.head.repo.full_name == github.repository && startsWith(github.head_ref, 'release-plz-')";
    let lint = job(&workflow, "lint");
    assert!(lint.get("if").is_none(), "lint runs on every pull request");
    let guard = steps(lint)
        .iter()
        .find(|step| text(step, "id") == Some("release-guard"))
        .expect("lint holds the release guard");
    assert_eq!(text(guard, "if"), Some(release));
    assert!(
        guard.get("continue-on-error").is_none(),
        "a refused release edit fails lint"
    );
    assert!(text(guard, "run")
        .is_some_and(|run| run.starts_with("node scripts/release-branch-guard.mjs ")));
    let skip = format!("!({release})");
    assert_eq!(
        text(job(&workflow, "test-linux"), "if"),
        Some(skip.as_str())
    );
    assert_eq!(
        text(job(&workflow, "test-windows"), "if"),
        Some(skip.as_str())
    );
    assert_eq!(
        text(job(&workflow, "test-macos"), "if"),
        Some(format!("(github.event_name == 'pull_request' && {skip}) || (github.event_name == 'workflow_dispatch' && inputs.macos-diagnostic)").as_str())
    );
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
        assert_eq!(text(with, "path"), Some(".ci-results"));
        assert_eq!(
            workflow
                .get("env")
                .and_then(|env| text(env, "CROZIER_RESULT_CACHE")),
            Some(".ci-results"),
            "the gate serves what the cache step restores"
        );
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

const CI_CACHES: &str = include_str!("../../../.github/workflows/ci-caches.yml");
const GALLERY: &str = include_str!("../../../.github/workflows/visual-docs-gallery.yml");
/// The workflow's triggers are a push to main and nothing else, so no pull request push
/// starts it.
fn assert_starts_only_on_a_push_to_main(file: &str, workflow: &Value) {
    let on = workflow
        .get("on")
        .and_then(Value::as_object)
        .unwrap_or_else(|| panic!("{file} names its triggers"));
    assert_eq!(
        on.keys().map(String::as_str).collect::<Vec<_>>(),
        ["push"],
        "{file}: no pull request push starts it"
    );
    assert_eq!(
        on["push"]["branches"],
        serde_json::json!(["main"]),
        "{file}: its push trigger is main alone"
    );
}

/// Neither workflow reports a context branch protection requires, so it gates nothing,
/// whatever its job ids are.
fn assert_reports_no_required_context(file: &str, workflow: &Value) {
    let required = required_checks();
    for (id, job) in workflow.get("jobs").and_then(Value::as_object).unwrap() {
        let context = text(job, "name").unwrap_or(id);
        assert!(
            !required.iter().any(|check| check == context),
            "{file}: job `{id}` reports the required context `{context}`"
        );
    }
}

/// What decides whether a lane's restore finds what this job saved: the same job id, runner
/// and inputs on every step a cache key or a tool version in it reads.
fn cache_relevant_steps(job: &Value) -> Vec<&Value> {
    steps(job)
        .iter()
        .filter(|step| {
            text(step, "id") == Some("host")
                || text(step, "uses").is_some_and(|uses| {
                    [
                        "actions/cache@",
                        "actions-rust-lang/",
                        "astral-sh/setup-uv",
                        "taiki-e/install-action",
                        "actions/setup-node",
                        "oven-sh/setup-bun",
                    ]
                    .iter()
                    .any(|prefix| uses.starts_with(prefix))
                })
        })
        .collect()
}

/// A pull request's lanes restore what main's writer saves: GitHub's restore matches by key
/// prefix within the base branch's scope, so each seeded lane's `restore-keys` must be a
/// prefix of the key this job saves under, with the job id, runner and every expression in
/// it evaluating alike. test-macos is left out on purpose: a Mac job here would fire on both
/// the base merge and the release merge, and crozier-macos-runs-per-change holds a change to
/// two Mac-spending runs, which the pull request and the release build already use.
#[test]
fn main_caches_are_written_under_the_keys_the_lanes_restore() {
    let writer: Value = crate::yaml::from_str(CI_CACHES).expect("ci-caches.yml is valid YAML");
    let ci: Value = crate::yaml::from_str(CI_WORKFLOW).expect("ci.yml is valid YAML");
    assert_starts_only_on_a_push_to_main("ci-caches.yml", &writer);
    assert_reports_no_required_context("ci-caches.yml", &writer);
    assert_eq!(
        writer.get("env"),
        ci.get("env"),
        "the gate serves the store the keys name"
    );
    let jobs: Vec<&str> = writer
        .get("jobs")
        .and_then(Value::as_object)
        .unwrap()
        .keys()
        .map(String::as_str)
        .collect();
    assert_eq!(jobs, ["lint", "test-linux", "test-windows"]);
    assert!(
        !CI_CACHES.contains("macos-latest"),
        "a Mac job here breaks crozier-macos-runs-per-change"
    );
    for (name, recipe) in [
        ("lint", "just ci-caches-lint"),
        ("test-linux", "just ci-caches-test"),
        ("test-windows", "just ci-caches-test"),
    ] {
        let (seed, lane) = (job(&writer, name), job(&ci, name));
        assert_eq!(
            seed.get("runs-on"),
            lane.get("runs-on"),
            "{name}: runner.os and runner.arch are in the key"
        );
        assert_eq!(
            cache_relevant_steps(seed),
            cache_relevant_steps(lane),
            "{name}: a key or a tool version in it differs from the lane's"
        );
        let cache = cache_relevant_steps(seed)
            .into_iter()
            .find(|step| text(step, "uses").is_some_and(|uses| uses.starts_with("actions/cache@")))
            .and_then(|step| step.get("with"))
            .unwrap_or_else(|| panic!("{name} writes no results"));
        let saved = text(cache, "key").expect("a key");
        assert!(
            saved.starts_with(text(cache, "restore-keys").expect("restore keys")),
            "{name}: the lane's restore cannot find {saved}"
        );
        let all = steps(seed);
        let runs = all
            .iter()
            .position(|step| text(step, "run") == Some(recipe))
            .unwrap_or_else(|| panic!("{name} does not run `{recipe}`"));
        let restores = all
            .iter()
            .position(|step| {
                text(step, "uses").is_some_and(|uses| uses.starts_with("actions/cache@"))
            })
            .unwrap();
        assert!(
            restores < runs,
            "{name}: the store is restored before it is added to"
        );
        assert_eq!(
            all[runs].get("continue-on-error").and_then(Value::as_bool),
            Some(true),
            "{name}: actions/cache saves only from a job that succeeded, so a red target must not cost the others' results"
        );
    }
}

/// The gh-pages root gallery comes from a push to main: the visual-docs action deploys to the
/// root only on a `push` event, so it needs a workflow that event starts, publishing what the
/// lint lane holds to the same baseline. Configuration assertions, because running the
/// publish would push to the real gh-pages branch: the capture and comparison run for real
/// in the lint lane on every pull request, and the deploy step is screencomp's own.
#[test]
fn the_root_gallery_is_published_from_a_push_to_main() {
    let gallery: Value =
        crate::yaml::from_str(GALLERY).expect("visual-docs-gallery.yml is valid YAML");
    let ci: Value = crate::yaml::from_str(CI_WORKFLOW).expect("ci.yml is valid YAML");
    assert_starts_only_on_a_push_to_main("visual-docs-gallery.yml", &gallery);
    assert_reports_no_required_context("visual-docs-gallery.yml", &gallery);
    let visual_docs = |job: &'_ Value| -> Value {
        steps(job)
            .iter()
            .find(|step| text(step, "uses").is_some_and(|uses| uses.contains("/visual-docs@")))
            .cloned()
            .expect("the job runs the visual-docs action")
    };
    let publishing = visual_docs(job(&gallery, "publish-gallery"));
    let lint = visual_docs(job(&ci, "lint"));
    assert_eq!(
        text(&publishing, "uses"),
        text(&lint, "uses"),
        "one screencomp version"
    );
    let (with, lint_with) = (&publishing["with"], &lint["with"]);
    assert_eq!(
        with.get("publish").and_then(Value::as_bool),
        Some(true),
        "the action deploys only when told to"
    );
    for input in [
        "arch",
        "current",
        "verify-second",
        "gallery-title",
        "fail-on-drift",
    ] {
        assert_eq!(
            with.get(input),
            lint_with.get(input),
            "the lint lane's {input}"
        );
    }
    let permissions = gallery
        .get("permissions")
        .expect("it states its permissions");
    assert_eq!(
        text(permissions, "contents"),
        Some("write"),
        "it pushes gh-pages"
    );
    let captures = |job: &'_ Value| {
        steps(job)
            .iter()
            .any(|step| text(step, "run") == Some("./screenshots/capture-visual-docs.sh"))
    };
    assert!(
        captures(job(&gallery, "publish-gallery")),
        "it publishes a real capture"
    );
}
