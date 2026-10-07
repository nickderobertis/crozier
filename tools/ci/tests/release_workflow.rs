//! `release.yml` runs only on a published GitHub Release, so no pull request
//! exercises it. These tests hold the parts of it that have failed a tag's run
//! where CI passed: every Windows job must enable git's long paths before it
//! checks out, or the checkout fails on the deepest committed fixture paths.

use serde_yaml_ng::{Mapping, Value};
use std::path::Path;
use std::process::Command;

const RELEASE_WORKFLOW: &str = include_str!("../../../.github/workflows/release.yml");
const LONG_PATHS: &str = "git config --global core.longpaths true";
/// The committed fixture whose paths exceed Windows' 260-character limit.
const LONG_FIXTURE: &str = "tests/fixtures/openbanking.org.uk-account-info-openapi";
/// The only step condition a pre-checkout step may carry; a new one would need
/// this test to decide whether it runs on Windows.
const WINDOWS_ONLY: &str = "runner.os == 'Windows'";

fn workflow() -> Value {
    serde_yaml_ng::from_str(RELEASE_WORKFLOW).expect("release.yml is valid YAML")
}

fn str_of<'a>(mapping: &'a Mapping, key: &str) -> Option<&'a str> {
    mapping.get(key).and_then(Value::as_str)
}

/// Every runner label a job can land on: its literal `runs-on`, or each
/// `os` its matrix supplies when `runs-on` is `${{ matrix.os }}`.
fn runner_labels(job: &Mapping) -> Vec<String> {
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
fn windows_checkout_jobs() -> Vec<(String, Vec<Mapping>)> {
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
fn windows_pre_checkout_commands(steps: &[Mapping]) -> Vec<String> {
    steps
        .iter()
        .filter(|step| match str_of(step, "if") {
            None => true,
            Some(condition) if condition == WINDOWS_ONLY => true,
            Some(other) => panic!(
                "pre-checkout step condition {other:?} is not one this test can evaluate; \
                 extend tests/release_workflow.rs to decide whether it runs on Windows"
            ),
        })
        .filter_map(|step| str_of(step, "run").map(str::to_owned))
        .collect()
}

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

fn git(dir: &Path, home: &Path, args: &[&str]) -> String {
    let output = Command::new("git")
        .args(args)
        .current_dir(dir)
        .env("HOME", home)
        .env("XDG_CONFIG_HOME", home.join("xdg"))
        .env("GIT_CONFIG_NOSYSTEM", "1")
        .env_remove("GIT_CONFIG_GLOBAL")
        .env_remove("GIT_DIR")
        .env_remove("GIT_WORK_TREE")
        .output()
        .expect("git is on PATH");
    assert!(
        output.status.success(),
        "git {args:?} failed: {}",
        String::from_utf8_lossy(&output.stderr)
    );
    String::from_utf8(output.stdout).expect("git output is UTF-8")
}

/// Run one workflow `run:` block the way the runner's default shell would.
fn run_step(command: &str, home: &Path) {
    let mut shell = if cfg!(windows) {
        let mut shell = Command::new("pwsh");
        shell.args(["-NoProfile", "-Command", command]);
        shell
    } else {
        let mut shell = Command::new("bash");
        shell.args(["-e", "-c", command]);
        shell
    };
    let status = shell
        .env("HOME", home)
        .env("XDG_CONFIG_HOME", home.join("xdg"))
        .env("GIT_CONFIG_NOSYSTEM", "1")
        .env_remove("GIT_CONFIG_GLOBAL")
        .status()
        .expect("the step's shell is on PATH");
    assert!(status.success(), "pre-checkout step {command:?} failed");
}

fn file_url(path: &Path) -> String {
    let path = path.to_string_lossy().replace('\\', "/");
    if path.starts_with('/') {
        format!("file://{path}")
    } else {
        format!("file:///{path}")
    }
}

/// For each Windows job: run its pre-checkout commands under a fresh `HOME`,
/// then check this repository's committed HEAD out the way actions/checkout
/// does (init, shallow fetch, forced checkout). Linux has no 260-character
/// limit, so here this proves the setting reaches a real checkout of the long
/// fixture; on ci.yml's Windows leg the same checkout is the real exercise.
#[test]
fn windows_release_checkout_journey_has_long_paths_and_the_long_fixture() {
    let repo = Path::new(env!("CARGO_MANIFEST_DIR"))
        .ancestors()
        .nth(2)
        .expect("this crate sits two levels below the repository root");
    let scratch = tempfile::tempdir().expect("temp dir");
    let committed_head = git(repo, scratch.path(), &["rev-parse", "HEAD"]);
    let committed: Vec<String> = git(
        repo,
        scratch.path(),
        &["ls-tree", "-r", "--name-only", "HEAD", "--", LONG_FIXTURE],
    )
    .lines()
    .map(str::to_owned)
    .collect();
    assert!(
        !committed.is_empty(),
        "{LONG_FIXTURE} has no committed files"
    );

    for (id, steps) in windows_checkout_jobs() {
        let root = scratch.path().join(&id);
        let home = root.join("home");
        let checkout = root.join("w");
        std::fs::create_dir_all(&home).expect("create HOME");
        std::fs::create_dir_all(&checkout).expect("create workspace");

        for command in windows_pre_checkout_commands(&steps) {
            run_step(&command, &home);
        }

        // The committed tree is gigabytes, so fetch it shallow and blobless and
        // check out only the long fixture; its blobs arrive on demand, and every
        // file it writes goes through the same checkout under the same config.
        git(&checkout, &home, &["init", "-q"]);
        // git strips config from a local transport's environment, so the
        // serving side's permission to filter travels in its own command.
        git(
            &checkout,
            &home,
            &["remote", "add", "origin", &file_url(repo)],
        );
        git(
            &checkout,
            &home,
            &[
                "config",
                "remote.origin.uploadpack",
                "git -c uploadpack.allowFilter=true -c uploadpack.allowAnySHA1InWant=true upload-pack",
            ],
        );
        git(
            &checkout,
            &home,
            &[
                "fetch",
                "-q",
                "--depth=1",
                "--filter=blob:none",
                "origin",
                "HEAD",
            ],
        );
        git(
            &checkout,
            &home,
            &["sparse-checkout", "set", "--no-cone", LONG_FIXTURE],
        );
        git(
            &checkout,
            &home,
            &["checkout", "-q", "--force", "FETCH_HEAD"],
        );
        assert_eq!(
            committed_head,
            git(&checkout, &home, &["rev-parse", "HEAD"]),
            "{id}: the checkout is not this repository's committed HEAD"
        );

        let longpaths = git(
            &checkout,
            &home,
            &["config", "--type=bool", "--default=false", "core.longpaths"],
        );
        assert_eq!(
            "true",
            longpaths.trim(),
            "{id}: core.longpaths is not in effect after its pre-checkout steps; \
             add `{LONG_PATHS}` before its actions/checkout"
        );

        let missing: Vec<&String> = committed
            .iter()
            .filter(|file| !checkout.join(file).is_file())
            .collect();
        assert!(
            missing.is_empty(),
            "{id}: {} committed file(s) under {LONG_FIXTURE} are missing from the checkout, e.g. {:?}",
            missing.len(),
            missing.first()
        );
    }
}

/// The floating major tag (`v0`) is what every `@v0` consumer of the GitHub
/// Action resolves, so it may move only after the release fully shipped: the
/// `major-tag` job waits on every publish and verify job and on the upload to
/// the GitHub Release, runs only when none of them failed (a skipped registry is
/// fine), and leaves the decision to `scripts/update-major-tag.sh`, which it
/// tells whether the Release is flagged as a pre-release.
#[test]
fn the_major_tag_job_moves_v0_only_after_every_publish_and_verify_job() {
    let workflow = workflow();
    let jobs = workflow
        .get("jobs")
        .and_then(Value::as_mapping)
        .expect("release.yml has jobs");
    let job = jobs
        .get("major-tag")
        .and_then(Value::as_mapping)
        .expect("release.yml has a major-tag job");

    let needs: Vec<&str> = job
        .get("needs")
        .and_then(Value::as_sequence)
        .expect("major-tag lists its needs")
        .iter()
        .map(|need| need.as_str().expect("each need is a job id"))
        .collect();
    let gated: Vec<&str> = jobs
        .keys()
        .map(|id| id.as_str().expect("job ids are strings"))
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
        .and_then(Value::as_sequence)
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
        .collect();
    assert_eq!(
        runs,
        ["bash scripts/update-major-tag.sh --tag \"$GITHUB_REF_NAME\" --prerelease \"$PRERELEASE\""],
        "the tag decision belongs to scripts/update-major-tag.sh alone"
    );
    // The Release's own pre-release flag reaches the script through `env`,
    // never interpolated into the `run:` (crates/crozier-e2e/tests/e2e/major_tag.rs runs the step).
    let step = steps
        .iter()
        .find(|step| step.get("run").is_some())
        .expect("major-tag runs the script");
    assert_eq!(
        step.get("env")
            .and_then(|env| env.get("PRERELEASE"))
            .and_then(Value::as_str),
        Some("${{ github.event.release.prerelease }}"),
        "the script must be told when the Release is flagged as a pre-release"
    );
}
