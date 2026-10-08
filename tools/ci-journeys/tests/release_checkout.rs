//! The real checkout behind `tools/ci/tests/release_workflow.rs`'s long-paths
//! contract: each Windows release job's pre-checkout commands, run under a
//! fresh `HOME`, then a shallow sparse checkout of this repository's committed
//! HEAD by the real `git`. It drives a host tool, so it lives here rather than
//! in the offline `ci` project.

#[path = "../../ci/tests/support/release.rs"]
mod release;

use release::{windows_checkout_jobs, windows_pre_checkout_commands, LONG_PATHS};
use std::path::Path;
use std::process::Command;

/// The committed fixture whose paths exceed Windows' 260-character limit.
const LONG_FIXTURE: &str = "tests/fixtures/openbanking.org.uk-account-info-openapi";

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
