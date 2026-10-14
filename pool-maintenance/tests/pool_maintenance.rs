//! Pool maintenance's scripts, run for real: `measure.sh` and the justfile's own
//! `pool-maintenance` recipe over a scratch cargo workspace laid out as this
//! repository is (its justfile and `.cargo/config.toml`, the script at
//! `pool-maintenance/measure.sh`), with the installed cargo-prune-superseded
//! doing the pruning; and `install-pruner.sh`'s skip and refusal. POSIX only:
//! pool maintenance runs on the Linux hosts that pool slots.
#![cfg(unix)]

use std::collections::BTreeSet;
use std::fs;
use std::path::{Path, PathBuf};
use std::process::{Command, Output};

use serde_json::Value;

/// The repository root: this crate sits one level below it.
fn root() -> &'static Path {
    Path::new(env!("CARGO_MANIFEST_DIR"))
        .parent()
        .expect("pool-maintenance sits one level below the repository root")
}

fn copy(rel: &str, into: &Path) {
    let dest = into.join(rel);
    fs::create_dir_all(dest.parent().unwrap()).unwrap();
    fs::copy(root().join(rel), &dest).unwrap_or_else(|e| panic!("copy {rel}: {e}"));
}

/// A cargo command in `dir`, free of the outer build's target-dir overrides.
fn cargo(dir: &Path) -> Command {
    let mut command = Command::new("cargo");
    command
        .current_dir(dir)
        .env_remove("CARGO_TARGET_DIR")
        .env_remove("CARGO_BUILD_TARGET_DIR");
    command
}

fn run(command: &mut Command) -> Output {
    let output = command.output().expect("the command starts");
    assert!(
        output.status.success(),
        "{command:?} failed: {}",
        String::from_utf8_lossy(&output.stderr)
    );
    output
}

/// A one-crate workspace with a test, carrying the repository's justfile, cargo
/// config and measure script where the repository keeps them.
fn workspace() -> tempfile::TempDir {
    let dir = tempfile::tempdir().unwrap();
    for rel in [
        "justfile",
        ".cargo/config.toml",
        "pool-maintenance/measure.sh",
    ] {
        copy(rel, dir.path());
    }
    fs::write(
        dir.path().join("Cargo.toml"),
        "[package]\nname = \"slot\"\nversion = \"0.1.0\"\nedition = \"2021\"\n",
    )
    .unwrap();
    fs::create_dir_all(dir.path().join("src")).unwrap();
    fs::write(
        dir.path().join("src/lib.rs"),
        "pub fn add(a: u32, b: u32) -> u32 { a + b }\n\n#[test]\nfn adds() { assert_eq!(add(1, 2), 3); }\n",
    )
    .unwrap();
    run(cargo(dir.path()).args(["generate-lockfile", "--offline"]));
    dir
}

/// The build-container entries listed in one of the script's evidence files.
fn listed(evidence: &Path, name: &str) -> BTreeSet<String> {
    fs::read_to_string(evidence.join(name))
        .unwrap_or_else(|e| panic!("evidence {name}: {e}"))
        .lines()
        .map(str::to_owned)
        .collect()
}

/// The `builds removed: N` count a pruner detail states first.
fn builds_removed(detail: &str) -> u64 {
    detail
        .split("builds removed: ")
        .nth(1)
        .and_then(|rest| rest.split(';').next())
        .and_then(|n| n.parse().ok())
        .unwrap_or_else(|| panic!("no builds-removed count in {detail:?}"))
}

/// One measurement from a slot holding the ordinary build plus a backlog: the
/// untimed pass clears the backlog, the timed pass removes exactly the
/// alternative build's entries, every other entry survives, and the figure is the
/// timed pass's own report with the backlog's beside it in the detail.
#[test]
fn measure_times_one_steady_state_pass_after_clearing_the_backlog() {
    let slot = workspace();
    let dir = slot.path();
    run(cargo(dir).args(["test", "--no-run", "--locked", "--quiet"]));
    // A backlog: a build under another profile, backdated past the window.
    let fingerprints = |dir: &Path| -> BTreeSet<PathBuf> {
        fs::read_dir(dir.join("target/debug/.fingerprint"))
            .unwrap()
            .map(|entry| entry.unwrap().path())
            .collect()
    };
    let ordinary = fingerprints(dir);
    run(cargo(dir).args([
        "test",
        "--no-run",
        "--locked",
        "--quiet",
        "--config",
        "profile.dev.debug-assertions=false",
    ]));
    let backlog: Vec<PathBuf> = fingerprints(dir).difference(&ordinary).cloned().collect();
    assert!(
        !backlog.is_empty(),
        "the backlog build made new fingerprints"
    );
    run(Command::new("find").arg(dir.join("target/debug")).args([
        "-exec",
        "touch",
        "-h",
        "-t",
        "200101010000",
        "{}",
        "+",
    ]));
    // The ordinary build stays each unit's newest.
    run(Command::new("find")
        .args(ordinary.iter())
        .args(["-exec", "touch", "-h", "{}", "+"]));

    let result = dir.join("result.json");
    let evidence = dir.join("evidence");
    let measured = Command::new(dir.join("pool-maintenance/measure.sh"))
        .current_dir(dir.join("pool-maintenance"))
        .env("ONEBUDGETSPEC_RESULT", &result)
        .env("POOL_MAINTENANCE_EVIDENCE", &evidence)
        .env_remove("CARGO_TARGET_DIR")
        .env_remove("CARGO_BUILD_TARGET_DIR")
        .output()
        .unwrap();
    let stderr = String::from_utf8_lossy(&measured.stderr);
    assert!(measured.status.success(), "measure.sh failed: {stderr}");
    assert!(
        stderr.contains("cargo-prune-superseded: target: removed"),
        "the declared recipe printed the pruner's per-target line: {stderr}"
    );

    let alt = listed(&evidence, "alt");
    let before = listed(&evidence, "before-pass");
    let after = listed(&evidence, "after-pass");
    let removed = listed(&evidence, "removed");
    assert!(!removed.is_empty(), "the timed pass removed something");
    assert!(
        removed.is_subset(&alt),
        "the timed pass removed only the alternative build's entries: {:?}",
        removed.difference(&alt).collect::<Vec<_>>()
    );
    let others: BTreeSet<_> = before.difference(&alt).cloned().collect();
    assert!(
        !others.is_empty(),
        "the ordinary build's entries were listed"
    );
    assert!(
        others.is_subset(&after),
        "every other entry survived the timed pass: {:?}",
        others.difference(&after).collect::<Vec<_>>()
    );
    let before_alt = listed(&evidence, "before-alt");
    for stale in &backlog {
        let name = stale.file_name().unwrap().to_str().unwrap();
        assert!(
            !before_alt.iter().any(|entry| entry.ends_with(name)),
            "the untimed pass cleared the backlog's {name} before the timed one"
        );
    }

    let report: Value =
        serde_json::from_str(&fs::read_to_string(&result).expect("the pass reported")).unwrap();
    let figure = report["value"].as_f64().expect("a numeric figure");
    assert!(figure.is_finite() && figure > 0.0, "{report}");
    let detail = report["detail"].as_str().expect("a detail");
    let (timed, backlog_detail) = detail
        .split_once("; untimed backlog pass, not in the figure: ")
        .unwrap_or_else(|| panic!("the backlog pass is beside the figure: {detail}"));
    assert!(builds_removed(timed) > 0, "{detail}");
    assert!(builds_removed(backlog_detail) > 0, "{detail}");
    for part in ["entries walked: ", "profile directories: ", "bytes freed: "] {
        assert!(timed.contains(part), "{detail}");
    }
}

/// A test build that fails stops the measurement with the build's error and no
/// figure, rather than timing a pass over a half-built slot.
#[test]
fn measure_refuses_a_slot_whose_test_build_fails() {
    let slot = workspace();
    let dir = slot.path();
    fs::write(dir.join("src/lib.rs"), "pub fn broken( {}\n").unwrap();
    let result = dir.join("result.json");
    let measured = Command::new(dir.join("pool-maintenance/measure.sh"))
        .current_dir(dir)
        .env("ONEBUDGETSPEC_RESULT", &result)
        .env_remove("CARGO_TARGET_DIR")
        .env_remove("CARGO_BUILD_TARGET_DIR")
        .output()
        .unwrap();
    let stderr = String::from_utf8_lossy(&measured.stderr);
    assert!(!measured.status.success());
    assert!(
        stderr.contains("measure: the test build failed (above); fix it, then rerun"),
        "{stderr}"
    );
    assert!(
        stderr.contains("error"),
        "the build's own error is shown: {stderr}"
    );
    assert!(!result.exists(), "no figure is reported");
}

/// A PATH holding only the installed pruner and the shell's own tools: no cargo
/// or rustup, so an attempt to install would fail.
fn path_with_pruner_only(bin: &Path) -> std::ffi::OsString {
    let pruner = String::from_utf8(
        run(Command::new("sh").args(["-c", "command -v cargo-prune-superseded"])).stdout,
    )
    .unwrap();
    std::os::unix::fs::symlink(pruner.trim(), bin.join("cargo-prune-superseded")).unwrap();
    std::ffi::OsString::from(format!("{}:/usr/bin:/bin", bin.display()))
}

fn installed_version() -> String {
    let version =
        String::from_utf8(run(Command::new("cargo-prune-superseded").arg("--version")).stdout)
            .unwrap();
    version
        .trim()
        .strip_prefix("cargo-prune-superseded ")
        .expect("the pruner names itself")
        .to_owned()
}

/// The release already on PATH is left as it is: nothing installs, nothing prints.
#[test]
fn install_pruner_skips_the_release_already_installed() {
    let bin = tempfile::tempdir().unwrap();
    let output = Command::new(root().join("pool-maintenance/install-pruner.sh"))
        .arg(installed_version())
        .env("PATH", path_with_pruner_only(bin.path()))
        .output()
        .unwrap();
    assert!(
        output.status.success(),
        "{}",
        String::from_utf8_lossy(&output.stderr)
    );
    assert!(output.stdout.is_empty() && output.stderr.is_empty());
}

/// Another release on PATH means an install, which without rustup fails with the
/// next step named.
#[test]
fn install_pruner_names_rustup_when_it_must_install_without_it() {
    let bin = tempfile::tempdir().unwrap();
    let output = Command::new(root().join("pool-maintenance/install-pruner.sh"))
        .arg("0.0.0-not-installed")
        .env("PATH", path_with_pruner_only(bin.path()))
        .output()
        .unwrap();
    let stderr = String::from_utf8_lossy(&output.stderr);
    assert!(!output.status.success());
    assert!(
        stderr.contains("install-pruner: rustup not found — install it (https://rustup.rs), then rerun 'just install-pruner'"),
        "{stderr}"
    );
}
