//! `release.yml` runs only on a published GitHub Release, so no pull request
//! exercises it. These tests hold the parts of it that have failed a tag's run
//! where CI passed: every Windows job must enable git's long paths before it
//! checks out, or the checkout fails on the deepest committed fixture paths.
//! The real checkout that proves the setting takes effect drives git, so it is
//! `ci-journeys`'s (`tools/ci-journeys/tests/release_checkout.rs`).

#[path = "support/release.rs"]
mod release;

use release::{str_of, windows_checkout_jobs, windows_pre_checkout_commands, workflow, LONG_PATHS};
use serde_yaml_ng::Value;

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
