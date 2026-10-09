//! `ci.yml` reports the required contexts on every pull request. A draft that is
//! lifted to ready for review must re-run them on its head: the default
//! `pull_request` types omit `ready_for_review`, so without it the lift reports
//! nothing new and the merge path is left reading draft-time runs.

use serde_yaml_ng::Value;

const CI_WORKFLOW: &str = include_str!("../../../.github/workflows/ci.yml");

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
        .and_then(Value::as_sequence)
        .expect("the job has steps")
}

/// The contexts branch protection requires are reported on every pull request
/// under exactly their names: no path or branch filter on `pull_request`, and
/// each job's condition is the one that keeps it reporting.
#[test]
fn the_required_contexts_report_on_every_pull_request() {
    let workflow: Value = serde_yaml_ng::from_str(CI_WORKFLOW).expect("ci.yml is valid YAML");
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
        ("gate", Some("always()")),
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
        .and_then(Value::as_sequence)
        .expect("gate aggregates its legs")
        .iter()
        .map(|need| need.as_str().expect("needs are job ids"))
        .collect();
    assert_eq!(
        needs,
        ["check", "sdk-env", "install", "package", "live-e2e"]
    );
}

/// Every leg `gate` aggregates that runs the gate goes through `just ci-check`,
/// which picks the tier for the event, with the history and the push base that
/// tier needs; and the legs between them cover every project.
#[test]
fn every_gate_leg_routes_its_tier_through_ci_check() {
    let workflow: Value = serde_yaml_ng::from_str(CI_WORKFLOW).expect("ci.yml is valid YAML");
    let mut scopes = Vec::new();
    for name in ["check", "sdk-env", "live-e2e"] {
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
        let gate = steps(job)
            .iter()
            .find(|step| text(step, "run").is_some_and(|run| run.starts_with("just ci-check")))
            .unwrap_or_else(|| panic!("{name} runs no `just ci-check` step"));
        assert_eq!(
            gate.get("env")
                .and_then(|env| text(env, "CROZIER_PUSH_BEFORE")),
            Some("${{ github.event.before }}"),
            "{name}: a push is scoped against the commit it replaced"
        );
        assert!(
            !steps(job).iter().any(|step| text(step, "run")
                .is_some_and(|run| run.starts_with("just check") || run.contains(" nx "))),
            "{name}: the tier comes from ci-check, never a second gate or Nx directly"
        );
        scopes.push(
            text(gate, "run")
                .unwrap()
                .trim_start_matches("just ci-check")
                .trim(),
        );
    }
    assert_eq!(
        scopes,
        [
            // The combined Python coverage floor holds on the Linux and macOS
            // legs only: the suites skip their POSIX-only cases on Windows.
            "--exclude=tag:tier:promoted${{ runner.os == 'Windows' && ',python-workspace' || '' }}",
            "--projects=sdk-env,runtime",
            "--projects=live-e2e,corpus-match,corpus-match-selection,census-fallback"
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
            serde_yaml_ng::from_str(source).unwrap_or_else(|_| panic!("{file} is valid YAML"));
        let jobs = workflow
            .get("jobs")
            .and_then(Value::as_mapping)
            .unwrap_or_else(|| panic!("{file} has jobs"));
        for (name, job) in jobs {
            let name = name.as_str().expect("job ids are strings");
            let Some(steps) = job.get("steps").and_then(Value::as_sequence) else {
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
    assert_eq!(
        bootstrapping,
        ["ci.yml:check", "ci.yml:sdk-env", "release.yml:test"],
        "the jobs that bootstrap"
    );
}

/// Every gate leg holds what its projects run before `just ci-check` starts
/// them: cargo-nextest, which the e2e and corpus-match targets run under, and a
/// toolchain installed once — by `just bootstrap`, or by `just
/// install-toolchain` where the leg skips bootstrap — so the gate's parallel cargo tasks
/// never race one first-use rustup install.
#[test]
fn every_gate_leg_installs_nextest_and_its_toolchain_before_the_gate() {
    let workflow: Value = serde_yaml_ng::from_str(CI_WORKFLOW).expect("ci.yml is valid YAML");
    for name in ["check", "sdk-env", "live-e2e"] {
        let steps = steps(job(&workflow, name));
        let gate = steps
            .iter()
            .position(|step| text(step, "run").is_some_and(|run| run.starts_with("just ci-check")))
            .unwrap_or_else(|| panic!("{name} runs no `just ci-check` step"));
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
            before.iter().any(|step| text(step, "run")
                .is_some_and(|run| run == "just bootstrap" || run == "just install-toolchain")),
            "{name}: the pinned toolchain is installed once before the gate"
        );
    }
}

/// A hand-cut Release can tag any commit, so release.yml re-gates it with the
/// full sweep over everything the check matrix gates.
#[test]
fn the_release_job_runs_the_full_sweep() {
    let workflow: Value =
        serde_yaml_ng::from_str(RELEASE_WORKFLOW).expect("release.yml is valid YAML");
    let runs: Vec<&str> = steps(job(&workflow, "test"))
        .iter()
        .filter_map(|step| text(step, "run"))
        .collect();
    assert!(
        runs.contains(&"just check --sweep --exclude=tag:tier:promoted"),
        "{runs:?}"
    );
}
