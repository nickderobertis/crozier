//! The GitHub Action's journeys, in-tree: `action.yml`'s steps are thin calls to
//! the scripts under `scripts/action/`, so these tests run those scripts the way
//! the composite action does — `bash <script>` with the step's `env` — against
//! the real `crozier` binary and real repository layouts, with `RUNNER_TEMP`,
//! `GITHUB_OUTPUT` and `GITHUB_STEP_SUMMARY` pointed at temporary files. Only the
//! runner is stood in for; nothing between the script and the CLI is.
//!
//! The reference commands are small committed or written scripts that copy a
//! committed golden, alter it, or refuse: a reference command is just a command,
//! so no reference tool is needed to reach every status.

use std::collections::BTreeMap;
use std::os::unix::fs::PermissionsExt;
use std::path::{Path, PathBuf};
use std::process::Command;

const GREEN: &str = "\u{1b}[32m";
const RED: &str = "\u{1b}[31m";
const YELLOW: &str = "\u{1b}[33m";
const RESET: &str = "\u{1b}[0m";

/// The committed layout whose three generators match, mismatch and cannot be
/// checked (`tests/action-fixture/crozier.yml`).
const FIXTURE_LAYOUT: &str = "tests/action-fixture";

fn repo_root() -> &'static Path {
    Path::new(env!("CARGO_MANIFEST_DIR"))
}

fn golden(name: &str) -> PathBuf {
    repo_root()
        .join("tests/fixtures/client-class-name")
        .join(name)
}

fn write(root: &Path, rel: &str, text: &str) {
    let path = root.join(rel);
    std::fs::create_dir_all(path.parent().unwrap()).unwrap();
    std::fs::write(path, text).unwrap();
}

fn write_executable(root: &Path, rel: &str, text: &str) {
    write(root, rel, text);
    std::fs::set_permissions(root.join(rel), std::fs::Permissions::from_mode(0o755)).unwrap();
}

/// `key=value` lines, as GitHub Actions reads `$GITHUB_OUTPUT`.
fn parse_outputs(text: &str) -> BTreeMap<String, String> {
    text.lines()
        .map(|line| {
            let (key, value) = line
                .split_once('=')
                .unwrap_or_else(|| panic!("not a key=value output line: {line:?}"));
            (key.to_string(), value.to_string())
        })
        .collect()
}

/// What one run of the action's compare and finish steps left behind.
struct ActionRun {
    outputs: BTreeMap<String, String>,
    summary: String,
    /// The compare step's log: the CLI's progress and report, then the
    /// script's own result line.
    compare_log: String,
    /// The finish step's log line and the status the action ends with.
    finish_log: String,
    final_status: i32,
    runner_temp: tempfile::TempDir,
}

impl ActionRun {
    fn output(&self, key: &str) -> &str {
        self.outputs
            .get(key)
            .unwrap_or_else(|| panic!("no `{key}` output in {:?}", self.outputs))
    }
}

/// The `bash` on this process's PATH, as an absolute path.
fn bash() -> PathBuf {
    std::env::split_paths(&std::env::var_os("PATH").unwrap())
        .map(|dir| dir.join("bash"))
        .find(|candidate| candidate.is_file())
        .expect("bash is on PATH")
}

/// The step environment: a fresh runner directory, the colour variables cleared
/// so only what the action and `env` set reaches the scripts, then `env`.
fn step(script: &str, cwd: &Path, runner_temp: &Path, env: &[(&str, &str)]) -> Command {
    // Resolved here, so a step whose PATH a test narrows still starts.
    let mut command = Command::new(bash());
    command
        .arg(repo_root().join("scripts/action").join(script))
        .current_dir(cwd)
        .env("RUNNER_TEMP", runner_temp)
        .env_remove("NO_COLOR")
        .env_remove("CLICOLOR_FORCE")
        .env_remove("GITHUB_OUTPUT")
        .env_remove("GITHUB_STEP_SUMMARY");
    for (key, value) in env {
        command.env(key, value);
    }
    command
}

/// Run the compare step (with `CROZIER` naming the real binary, as the install
/// step's `bin` output does) and then the finish step on its `exit-code`, the
/// way `action.yml` chains them.
fn run_action(cwd: &Path, env: &[(&str, &str)]) -> ActionRun {
    let runner_temp = tempfile::tempdir().unwrap();
    let output_file = runner_temp.path().join("github-output");
    let summary_file = runner_temp.path().join("step-summary");
    std::fs::write(&output_file, "").unwrap();
    std::fs::write(&summary_file, "").unwrap();

    let compare = step("compare.sh", cwd, runner_temp.path(), env)
        .env("CROZIER", env!("CARGO_BIN_EXE_crozier"))
        .env("GITHUB_OUTPUT", &output_file)
        .env("GITHUB_STEP_SUMMARY", &summary_file)
        .output()
        .unwrap();
    let compare_log = String::from_utf8_lossy(&compare.stderr).into_owned();
    assert!(
        compare.status.success(),
        "the compare step itself must not fail; finish.sh carries the CLI's status: {compare_log}"
    );
    let outputs = parse_outputs(&std::fs::read_to_string(&output_file).unwrap());

    let exit_code = outputs.get("exit-code").cloned().unwrap_or_default();
    let finish = step("finish.sh", cwd, runner_temp.path(), env)
        .env("EXIT_CODE", &exit_code)
        .output()
        .unwrap();
    ActionRun {
        outputs,
        summary: std::fs::read_to_string(&summary_file).unwrap(),
        compare_log,
        finish_log: String::from_utf8_lossy(&finish.stderr).into_owned(),
        final_status: finish.status.code().expect("finish.sh exited"),
        runner_temp,
    }
}

fn assert_seconds(run: &ActionRun, key: &str) -> f64 {
    let value = run.output(key);
    value
        .parse::<f64>()
        .unwrap_or_else(|_| panic!("`{key}` is not a number of seconds: {value:?}"))
}

/// The three-result journey over the committed layout: one generator matches,
/// one mismatches (one altered file), one cannot be checked (its command
/// refuses). Every output, the summary's marks and rows, the colours in the log
/// under the action's own `CLICOLOR_FORCE=1`, and the action's final status.
#[test]
fn the_action_reports_one_of_each_status_over_the_fixture_layout() {
    let run = run_action(repo_root(), &[("COMPARE_PATHS", FIXTURE_LAYOUT)]);

    assert_eq!(run.output("matched"), "1");
    assert_eq!(run.output("mismatched"), "1");
    assert_eq!(run.output("could-not-check"), "1");
    assert_eq!(run.output("exit-code"), "3");
    for key in [
        "total-reference-seconds",
        "total-crozier-seconds",
        "total-saved-seconds",
    ] {
        assert_seconds(&run, key);
    }
    assert!(run.output("total-speedup").parse::<f64>().unwrap() > 0.0);

    // The outputs are the report's own figures (jq may render a float's last
    // digit differently from the CLI, so they agree to within that).
    let report: serde_json::Value =
        serde_json::from_str(&std::fs::read_to_string(run.output("report-path")).unwrap()).unwrap();
    assert_eq!(report["exit_code"], 3);
    for (key, field) in [
        ("total-reference-seconds", "reference_seconds"),
        ("total-crozier-seconds", "crozier_seconds"),
        ("total-speedup", "speedup"),
        ("total-saved-seconds", "saved_seconds"),
    ] {
        let reported = report["timing_totals"][field].as_f64().unwrap();
        let output = assert_seconds(&run, key);
        assert!(
            (output - reported).abs() <= reported.abs() * 1e-12,
            "{key} {output} is not the report's {field} {reported}"
        );
    }
    // The mismatch's diff is in the directory the upload step uploads.
    let diffs: Vec<_> = std::fs::read_dir(run.output("diff-dir"))
        .unwrap()
        .map(|entry| entry.unwrap().file_name().into_string().unwrap())
        .collect();
    assert_eq!(diffs.len(), 1, "{diffs:?}");
    assert!(diffs[0].ends_with("-mismatched.diff"), "{diffs:?}");

    let summary = &run.summary;
    assert!(
        summary.contains("❌ **1 generator(s) mismatched the reference.**"),
        "{summary}"
    );
    assert!(summary.contains("| 1 | 1 | 1 |"), "{summary}");
    let config = "<code>tests/action-fixture/crozier.yml</code>";
    for row in [
        format!("| ✅ matched | {config} | <code>matched</code> | <code>./reference/copy-golden.sh</code> | 40 file(s) compared, layout <code>packaged</code> |"),
        format!("| ❌ mismatched | {config} | <code>mismatched</code> | <code>./reference/copy-golden.sh --alter</code> | differ: <code>README.md</code> |"),
        format!("| ⚠️ could not check | {config} | <code>could-not-check</code> | <code>./reference/refuse.sh</code> | the reference command exited with status 7:<br>reference tool: this document is not supported |"),
    ] {
        assert!(summary.contains(&row), "missing row {row}\n{summary}");
    }
    // Every generator row carries its four figures; the could-not-check one has
    // a reference time and no crozier side.
    let rows: Vec<&str> = summary
        .lines()
        .filter(|line| {
            line.starts_with("| ✅") || line.starts_with("| ❌ ") || line.starts_with("| ⚠️")
        })
        .filter(|line| line.contains("<code>"))
        .collect();
    assert_eq!(rows.len(), 3, "{summary}");
    for row in &rows[..2] {
        assert!(row.ends_with(" s |") && row.contains("× |"), "{row}");
    }
    assert!(rows[2].ends_with(" s | — | — | — |"), "{}", rows[2]);
    assert!(
        summary.contains("| **Total** (2 generator(s) where both sides ran) |"),
        "{summary}"
    );
    assert!(
        summary.contains("_Reference time_ is the wall time of that generator's one reference-command invocation; a first invocation may include one-time costs such as an image pull. _crozier time_ is its generation only."),
        "{summary}"
    );

    // The test environment has no CLICOLOR_FORCE and the log is a pipe, not a
    // terminal: the colours are there because the action sets it.
    let log = &run.compare_log;
    for painted in [
        format!("{GREEN}matched{RESET}"),
        format!("{RED}mismatched{RESET}"),
        format!("{YELLOW}could_not_check{RESET}"),
        format!("crozier-action: {GREEN}1 matched{RESET}, {RED}1 mismatched{RESET}, {YELLOW}1 could not check{RESET}"),
    ] {
        assert!(log.contains(&painted), "no {painted:?} in the log:\n{log}");
    }
    assert_eq!(
        run.finish_log,
        format!("{RED}crozier compare: a generator mismatched its reference (exit 3){RESET}\n")
    );
    assert_eq!(run.final_status, 3);
}

/// A `NO_COLOR` the workflow sets wins over the action's `CLICOLOR_FORCE=1`,
/// for the CLI and for the action's own lines alike.
#[test]
fn no_color_from_the_workflow_turns_every_colour_off() {
    let run = run_action(
        repo_root(),
        &[("COMPARE_PATHS", FIXTURE_LAYOUT), ("NO_COLOR", "1")],
    );
    assert_eq!(run.output("exit-code"), "3");
    for log in [&run.compare_log, &run.finish_log] {
        assert!(
            !log.contains('\u{1b}'),
            "colour codes under NO_COLOR:\n{log}"
        );
    }
    assert!(run
        .compare_log
        .contains("crozier-action: 1 matched, 1 mismatched, 1 could not check"));
    assert_eq!(run.final_status, 3);
}

/// A git repository holding the fixture spec and the given files.
fn layout(files: &[(&str, &str)]) -> tempfile::TempDir {
    let repo = tempfile::tempdir().unwrap();
    let status = Command::new("git")
        .args(["init", "-q"])
        .current_dir(repo.path())
        .env_remove("GIT_DIR")
        .env_remove("GIT_WORK_TREE")
        .status()
        .unwrap();
    assert!(status.success());
    std::fs::copy(golden("openapi.yml"), repo.path().join("openapi.yml")).unwrap();
    for (rel, text) in files {
        if rel.ends_with(".sh") {
            write_executable(repo.path(), rel, text);
        } else {
            write(repo.path(), rel, text);
        }
    }
    repo
}

const NAMING: &str =
    "package-name: fern\nproject-name: default_package_name\nclient-class-name: AcmeClient\n";

/// Everything checked matched — a packaged and a flat generator, in two configs
/// named by a whitespace-separated `paths`, under one `reference-command` that
/// reads the layout crozier passes — and the action passes.
#[test]
fn every_generator_matching_passes_the_action() {
    let reference = format!(
        "#!/bin/sh\nset -eu\nif [ \"$CROZIER_REFERENCE_LAYOUT\" = flat ]; then golden='{}'; else golden='{}'; fi\n\
         cp -R \"$golden/.\" \"$CROZIER_REFERENCE_OUTPUT\"\n",
        golden("expected-flat").display(),
        golden("expected").display(),
    );
    let packaged = format!("spec: ../openapi.yml\n{NAMING}generators:\n  packaged: {{}}\n");
    let flat = format!("spec: ../openapi.yml\n{NAMING}generators:\n  flat:\n    layout: flat\n");
    let repo = layout(&[
        ("reference.sh", &reference),
        ("packaged/crozier.yml", &packaged),
        ("flat/.crozier.yml", &flat),
        // Not named by `paths`, so never checked.
        ("other/crozier.yml", "spec: ./missing.yml\n"),
    ]);
    let command = repo.path().join("reference.sh");
    let run = run_action(
        repo.path(),
        &[
            ("COMPARE_PATHS", "  packaged\tflat  "),
            ("REFERENCE_COMMAND", command.to_str().unwrap()),
        ],
    );

    assert_eq!(run.output("matched"), "2");
    assert_eq!(run.output("mismatched"), "0");
    assert_eq!(run.output("could-not-check"), "0");
    assert_eq!(run.output("exit-code"), "0");
    assert_seconds(&run, "total-speedup");
    assert!(
        run.summary
            .contains("✅ **Every checked generator matched.**"),
        "{}",
        run.summary
    );
    assert!(run.summary.contains("| 2 | 0 | 0 |"), "{}", run.summary);
    let command_cell = format!("<code>{}</code>", command.display());
    for (config, layout) in [
        ("packaged/crozier.yml", "packaged"),
        ("flat/.crozier.yml", "flat"),
    ] {
        let row = format!(
            "| ✅ matched | <code>{config}</code> | <code>{layout}</code> | {command_cell} | "
        );
        let line = run
            .summary
            .lines()
            .find(|line| line.starts_with(&row))
            .unwrap_or_else(|| panic!("no row starting {row}\n{}", run.summary));
        assert!(
            line.contains(&format!("file(s) compared, layout <code>{layout}</code> |")),
            "{line}"
        );
    }
    assert!(
        !run.summary.contains("| ❌ mismatched |")
            && !run.summary.contains("| ⚠️ could not check |"),
        "{}",
        run.summary
    );
    assert!(
        run.compare_log.contains(&format!(
            "crozier-action: {GREEN}2 matched{RESET}, {RED}0 mismatched{RESET}, {YELLOW}0 could not check{RESET}"
        )),
        "{}",
        run.compare_log
    );
    assert_eq!(
        run.finish_log,
        format!("{GREEN}crozier compare: every checked generator matched (exit 0){RESET}\n")
    );
    assert_eq!(run.final_status, 0);
}

/// Only could-not-check: a refusing reference command and a generator with no
/// command at all. Nothing mismatched, so no diff is uploaded, and the action
/// fails with 4.
#[test]
fn only_could_not_check_fails_the_action_with_four() {
    let repo = layout(&[
        (
            "refuse.sh",
            "#!/bin/sh\necho 'cannot generate this | document' >&2\nexit 2\n",
        ),
        (
            "crozier.yml",
            &format!(
                "spec: ./openapi.yml\n{NAMING}generators:\n  refused:\n    reference:\n      command: ./refuse.sh\n  unconfigured: {{}}\n"
            ),
        ),
    ]);
    let run = run_action(repo.path(), &[]);

    assert_eq!(run.output("matched"), "0");
    assert_eq!(run.output("mismatched"), "0");
    assert_eq!(run.output("could-not-check"), "2");
    assert_eq!(run.output("exit-code"), "4");
    // The refused command was timed; no generator ran on both sides.
    assert_eq!(run.output("total-speedup"), "");
    assert_eq!(assert_seconds(&run, "total-reference-seconds"), 0.0);
    assert!(
        run.summary
            .contains("⚠️ **No mismatch, but 2 generator(s) could not be checked.**"),
        "{}",
        run.summary
    );
    // Report text is data in the table: a `|` cannot split the row.
    assert!(
        run.summary.contains(
            "| ⚠️ could not check | <code>crozier.yml</code> | <code>refused</code> | <code>./refuse.sh</code> | the reference command exited with status 2:<br>cannot generate this &#124; document |"
        ),
        "{}",
        run.summary
    );
    assert!(
        run.summary.contains(
            "| ⚠️ could not check | <code>crozier.yml</code> | <code>unconfigured</code> | — | no reference command configured"
        ),
        "{}",
        run.summary
    );
    assert!(run.summary.contains("| **Total** (0 generator(s) where both sides ran) | | | | | **0.00 s** | **0.00 s** | **—** | **0.00 s** |"), "{}", run.summary);
    assert!(run
        .compare_log
        .contains(&format!("{YELLOW}could_not_check{RESET}")));
    assert_eq!(
        run.finish_log,
        format!(
            "{YELLOW}crozier compare: no mismatch, but a generator could not be checked (exit 4){RESET}\n"
        )
    );
    assert_eq!(run.final_status, 4);
}

/// A repository with no crozier config: nothing to check is a pass.
#[test]
fn nothing_found_passes_the_action() {
    let repo = layout(&[("README.md", "no crozier here\n")]);
    let run = run_action(repo.path(), &[]);

    assert_eq!(run.output("matched"), "0");
    assert_eq!(run.output("mismatched"), "0");
    assert_eq!(run.output("could-not-check"), "0");
    assert_eq!(run.output("exit-code"), "0");
    assert!(!run.output("report-path").is_empty());
    assert!(
        run.summary
            .contains("✅ **Nothing to check:** no crozier config was found."),
        "{}",
        run.summary
    );
    // No generator rows, so no table of them.
    assert!(!run.summary.contains("| Status |"), "{}", run.summary);
    assert_eq!(run.final_status, 0);
    assert!(run.finish_log.starts_with(GREEN), "{}", run.finish_log);
}

/// The command itself failing (a path that does not exist) leaves no report:
/// the outputs say so, the summary points at the log, and the action fails 1.
#[test]
fn a_failed_command_fails_the_action_with_its_own_status() {
    let repo = layout(&[]);
    let run = run_action(repo.path(), &[("COMPARE_PATHS", "does-not-exist")]);

    assert_eq!(run.output("exit-code"), "1");
    assert_eq!(run.output("report-path"), "");
    assert_eq!(run.output("matched"), "");
    assert_eq!(run.output("mismatched"), "");
    assert!(
        run.compare_log.contains("does-not-exist"),
        "{}",
        run.compare_log
    );
    assert!(
        run.summary
            .contains("❌ **crozier compare failed (exit 1) before writing a report.**"),
        "{}",
        run.summary
    );
    assert_eq!(
        run.finish_log,
        format!("{RED}crozier compare: the command failed (exit 1); see its error above{RESET}\n")
    );
    assert_eq!(run.final_status, 1);
}

/// An `exit-code` that never arrived (the compare step did not finish) is not a
/// pass.
#[test]
fn finish_refuses_a_missing_exit_code() {
    let runner_temp = tempfile::tempdir().unwrap();
    let out = step(
        "finish.sh",
        repo_root(),
        runner_temp.path(),
        &[("EXIT_CODE", "")],
    )
    .output()
    .unwrap();
    assert_eq!(out.status.code(), Some(1));
    assert!(String::from_utf8_lossy(&out.stderr).contains("is not an exit status"));
}

/// A mismatch touching many files lists the first twenty of each kind in its
/// row and counts the rest, which the diff artifact holds in full.
#[test]
fn a_long_mismatch_lists_twenty_paths_and_counts_the_rest() {
    let reference = format!(
        "#!/usr/bin/env bash\nset -euo pipefail\ncp -R '{}/.' \"$CROZIER_REFERENCE_OUTPUT\"\n\
         mkdir \"$CROZIER_REFERENCE_OUTPUT/extra\"\n\
         for i in $(seq -w 1 25); do echo \"$i\" > \"$CROZIER_REFERENCE_OUTPUT/extra/file-$i.txt\"; done\n",
        golden("expected").display(),
    );
    let repo = layout(&[
        ("reference.sh", &reference),
        (
            "crozier.yml",
            &format!("spec: ./openapi.yml\n{NAMING}reference:\n  command: ./reference.sh\n"),
        ),
    ]);
    let run = run_action(repo.path(), &[]);

    assert_eq!(run.output("mismatched"), "1");
    let row = run
        .summary
        .lines()
        .find(|line| line.starts_with("| ❌ mismatched |"))
        .unwrap_or_else(|| panic!("no mismatched row:\n{}", run.summary));
    let listed: Vec<&str> = row.matches("<code>extra/file-").collect();
    assert_eq!(listed.len(), 20, "{row}");
    assert!(
        row.contains("only in reference: <code>extra/file-01.txt</code>"),
        "{row}"
    );
    assert!(row.contains("<code>extra/file-20.txt</code>"), "{row}");
    assert!(!row.contains("extra/file-21.txt"), "{row}");
    assert!(row.contains("(5 more; see the diff artifact)"), "{row}");
    assert_eq!(run.final_status, 3);
}

/// When the CLI's own status is not the report's — a `--diff-dir` file it could
/// not write exits 1 over a report whose results say 3 — the summary says so
/// beside the result the report gives. Rendered from a real report.
#[test]
fn the_summary_states_a_cli_status_the_report_does_not_carry() {
    let run = run_action(repo_root(), &[("COMPARE_PATHS", FIXTURE_LAYOUT)]);
    let out = step("summary.sh", repo_root(), run.runner_temp.path(), &[])
        .env("REPORT", run.output("report-path"))
        .env("EXIT_CODE", "1")
        .output()
        .unwrap();
    assert!(out.status.success());
    let summary = String::from_utf8(out.stdout).unwrap();
    assert!(
        summary.contains("❌ **1 generator(s) mismatched the reference.**"),
        "{summary}"
    );
    assert!(
        summary.contains("❌ **crozier compare exited 1**, not 3: see the step log for its error."),
        "{summary}"
    );
    // The run whose statuses agree carries no such line.
    assert!(
        !run.summary.contains("**crozier compare exited"),
        "{}",
        run.summary
    );
}

/// The compare step refuses to run outside a runner rather than write its
/// outputs nowhere, and says what is missing.
#[test]
fn compare_refuses_a_missing_runner_environment() {
    let runner_temp = tempfile::tempdir().unwrap();
    let output_file = runner_temp.path().join("github-output");
    std::fs::write(&output_file, "").unwrap();
    // Only `dirname` (to find lib.sh) on PATH: no jq.
    let bin = tempfile::tempdir().unwrap();
    let dirname = Command::new("sh")
        .args(["-c", "command -v dirname"])
        .output()
        .unwrap();
    std::os::unix::fs::symlink(
        String::from_utf8(dirname.stdout).unwrap().trim(),
        bin.path().join("dirname"),
    )
    .unwrap();

    for (missing, env, named) in [
        (
            "RUNNER_TEMP",
            vec![("GITHUB_OUTPUT", output_file.as_path())],
            "RUNNER_TEMP is not set",
        ),
        ("GITHUB_OUTPUT", vec![], "GITHUB_OUTPUT is not set"),
        (
            "jq",
            vec![
                ("GITHUB_OUTPUT", output_file.as_path()),
                ("PATH", bin.path()),
            ],
            "jq is not on PATH",
        ),
    ] {
        let mut command = step("compare.sh", repo_root(), runner_temp.path(), &[]);
        if missing == "RUNNER_TEMP" {
            command.env_remove("RUNNER_TEMP");
        }
        for (key, value) in env {
            command.env(key, value);
        }
        let out = command.output().unwrap();
        let stderr = String::from_utf8_lossy(&out.stderr);
        assert_eq!(out.status.code(), Some(1), "{missing}: {stderr}");
        assert!(
            stderr.contains(named) && stderr.contains("ACTION:"),
            "{missing}: {stderr}"
        );
    }
    assert_eq!(std::fs::read_to_string(&output_file).unwrap(), "");
}

// The install step, run by the real scripts/action/install.sh with the real
// scripts/install.sh it calls. A published release is out of an offline test's
// reach, so the release is served from a local mirror laid out as the release
// workflow publishes one (`CROZIER_RELEASE_BASE_URL`, with the checksum under a
// separate root, `CROZIER_CHECKSUM_BASE_URL`), holding the crozier binary these
// tests built.

/// The release-asset target `scripts/install.sh` detects on this host.
fn host_target() -> String {
    let os = match std::env::consts::OS {
        "linux" => "unknown-linux-gnu",
        "macos" => "apple-darwin",
        other => panic!("no release target for {other}"),
    };
    format!("{}-{os}", std::env::consts::ARCH)
}

/// A local release mirror holding `tags`, each archive the real `crozier`.
struct Mirror {
    dir: tempfile::TempDir,
}

impl Mirror {
    fn new(tags: &[&str]) -> Self {
        let dir = tempfile::tempdir().unwrap();
        let staging = dir.path().join("staging");
        std::fs::create_dir_all(&staging).unwrap();
        std::fs::copy(env!("CARGO_BIN_EXE_crozier"), staging.join("crozier")).unwrap();
        for tag in tags {
            let base = format!("crozier-{tag}-{}", host_target());
            let releases = dir.path().join("releases").join(tag);
            let sums = dir.path().join("sums").join(tag);
            std::fs::create_dir_all(&releases).unwrap();
            std::fs::create_dir_all(&sums).unwrap();
            // The archive and its `.sha256` as the release workflow names them
            // (gzip's fastest level: the binary is large and only its bytes
            // matter here).
            let status = Command::new("sh")
                .arg("-c")
                .arg(
                    "set -e; tar -cf - -C \"$1\" crozier | gzip -1 > \"$2/$4.tar.gz\"; \
                     cd \"$2\"; if command -v sha256sum >/dev/null; then sha256sum \"$4.tar.gz\"; \
                     else shasum -a 256 \"$4.tar.gz\"; fi > \"$3/$4.sha256\"",
                )
                .arg("sh")
                .arg(&staging)
                .arg(&releases)
                .arg(&sums)
                .arg(&base)
                .status()
                .unwrap();
            assert!(status.success());
        }
        Mirror { dir }
    }

    fn env(&self) -> [(&'static str, String); 2] {
        [
            (
                "CROZIER_RELEASE_BASE_URL",
                format!("file://{}", self.dir.path().join("releases").display()),
            ),
            (
                "CROZIER_CHECKSUM_BASE_URL",
                format!("file://{}", self.dir.path().join("sums").display()),
            ),
        ]
    }
}

struct Install {
    status: i32,
    stderr: String,
    outputs: BTreeMap<String, String>,
    runner_temp: tempfile::TempDir,
}

impl Install {
    fn root(&self) -> PathBuf {
        self.runner_temp.path().join("crozier-action")
    }

    /// The `bin` output, checked to be the installed binary's path.
    fn bin(&self) -> PathBuf {
        let bin = self.root().join("bin/crozier");
        assert_eq!(
            self.outputs.get("bin").map(String::as_str),
            Some(bin.to_str().unwrap()),
            "{}",
            self.stderr
        );
        bin
    }
}

/// Run the install step with `version` from `action` (its own checkout), with
/// the mirror's variables and any `env`.
fn install(action: &Path, version: &str, mirror: Option<&Mirror>, env: &[(&str, &str)]) -> Install {
    let runner_temp = tempfile::tempdir().unwrap();
    let output_file = runner_temp.path().join("github-output");
    std::fs::write(&output_file, "").unwrap();
    let mut command = step("install.sh", action, runner_temp.path(), env);
    command
        .env("GITHUB_ACTION_PATH", action)
        .env("GITHUB_OUTPUT", &output_file)
        .env("VERSION", version)
        .env_remove("GITHUB_PATH")
        .env_remove("CROZIER_VERSION")
        .env_remove("CROZIER_RELEASE_BASE_URL")
        .env_remove("CROZIER_CHECKSUM_BASE_URL");
    if !env.iter().any(|(key, _)| *key == "RUNNER_OS") {
        command.env_remove("RUNNER_OS");
    }
    for (key, value) in mirror.map(Mirror::env).into_iter().flatten() {
        command.env(key, value);
    }
    let out = command.output().unwrap();
    Install {
        status: out.status.code().unwrap(),
        stderr: String::from_utf8_lossy(&out.stderr).into_owned(),
        outputs: parse_outputs(&std::fs::read_to_string(&output_file).unwrap()),
        runner_temp,
    }
}

fn version_of(bin: &Path) -> String {
    let out = Command::new(bin).arg("--version").output().unwrap();
    assert!(out.status.success());
    String::from_utf8(out.stdout).unwrap().trim().to_string()
}

/// Empty `version` installs `v` + the `[package] version` of the action's own
/// `Cargo.toml` — here this repository itself is the action's checkout, whose
/// version Cargo read for this build (`CARGO_PKG_VERSION`), so the expectation
/// does not share the action's own reading of the manifest. The mirror holds
/// only that release, so nothing else could have been installed.
#[test]
fn an_empty_version_installs_the_release_the_action_ref_names() {
    let own = format!("v{}", env!("CARGO_PKG_VERSION"));
    let mirror = Mirror::new(&[&own]);
    let run = install(repo_root(), "", Some(&mirror), &[]);

    assert_eq!(run.status, 0, "{}", run.stderr);
    assert!(
        run.stderr
            .contains(&format!("crozier-{own}-{}.tar.gz", host_target())),
        "{}",
        run.stderr
    );
    assert!(run.stderr.contains("checksum OK."), "{}", run.stderr);
    assert_eq!(
        version_of(&run.bin()),
        format!("crozier {}", env!("CARGO_PKG_VERSION"))
    );
}

/// A `version` under another table, or a manifest that cannot be read, is no
/// version: the step fails naming the `version` input, and never falls back to
/// the latest release.
#[test]
fn an_unreadable_own_version_fails_naming_the_version_input() {
    // A mirror holding every version named here: a fallback would have
    // something to install.
    let mirror = Mirror::new(&["v1.2.3"]);
    for manifest in [
        None,
        Some("[dependencies]\nversion = \"1.2.3\"\n"),
        Some("[package]\nname = \"crozier\"\nversion = \"main\"\n"),
        Some("[package]\nversion = \"1.2.3\" trailing\n"),
    ] {
        // The real installer beside the manifest.
        let action = tempfile::tempdir().unwrap();
        if let Some(manifest) = manifest {
            write(action.path(), "Cargo.toml", manifest);
        }
        std::fs::create_dir_all(action.path().join("scripts")).unwrap();
        std::fs::copy(
            repo_root().join("scripts/install.sh"),
            action.path().join("scripts/install.sh"),
        )
        .unwrap();
        let run = install(action.path(), "", Some(&mirror), &[]);
        assert_eq!(run.status, 1, "{manifest:?}: {}", run.stderr);
        assert!(
            run.stderr
                .contains("::error::cannot read the release this action's ref names")
                && run.stderr.contains("set the version input"),
            "{manifest:?}: {}",
            run.stderr
        );
        assert!(!run.stderr.contains("downloading"), "{}", run.stderr);
        assert!(!run.outputs.contains_key("bin"));
        assert!(!run.root().join("bin/crozier").exists());
    }
}

/// An exact tag installs that release; one that was never published fails the
/// step, with no binary and no `bin` output.
#[test]
fn an_exact_tag_installs_that_release() {
    let mirror = Mirror::new(&["v0.0.80"]);
    let run = install(repo_root(), "v0.0.80", Some(&mirror), &[]);
    assert_eq!(run.status, 0, "{}", run.stderr);
    assert!(
        run.stderr
            .contains(&format!("crozier-v0.0.80-{}.tar.gz", host_target())),
        "{}",
        run.stderr
    );
    assert!(version_of(&run.bin()).starts_with("crozier "));

    let missing = install(repo_root(), "v0.0.81", Some(&mirror), &[]);
    assert_ne!(missing.status, 0);
    assert!(
        missing.stderr.contains("download failed"),
        "{}",
        missing.stderr
    );
    assert!(!missing.outputs.contains_key("bin"));
}

/// `latest` asks the installer for its newest release, which it resolves from
/// GitHub's API.
#[test]
fn latest_installs_the_newest_release() {
    let action = tempfile::tempdir().unwrap();
    // llmlint: ignore[e2e_not_mocked] `latest` is resolved by scripts/install.sh from api.github.com, which an offline test cannot reach and a live one would make depend on whatever was released last; the stand-in records that the step asked for no particular version, which is the whole of the action's part. The real installer is driven over a local mirror by the tests above.
    write_executable(
        action.path(),
        "scripts/install.sh",
        "#!/bin/sh\nset -eu\nprintf '%s\\n' \"$@\" > \"$RECORD\"\n\
         while [ $# -gt 0 ]; do case \"$1\" in --to) to=\"$2\"; shift 2 ;; *) shift ;; esac; done\n\
         mkdir -p \"$to\"\nprintf '#!/bin/sh\\n' > \"$to/crozier\"\nchmod +x \"$to/crozier\"\n",
    );
    let record = action.path().join("args");
    let run = install(
        action.path(),
        "latest",
        None,
        &[("RECORD", record.to_str().unwrap())],
    );
    assert_eq!(run.status, 0, "{}", run.stderr);
    let bin_dir = run.root().join("bin");
    assert_eq!(
        std::fs::read_to_string(&record).unwrap(),
        format!("--to\n{}\n", bin_dir.display())
    );
    run.bin();
}

/// A minimal crate standing in for the action's own source: `cargo install`
/// builds it for real, offline, in seconds.
fn local_source(bin_name: &str) -> tempfile::TempDir {
    let dir = tempfile::tempdir().unwrap();
    write(
        dir.path(),
        "Cargo.toml",
        &format!("[package]\nname = \"{bin_name}\"\nversion = \"9.9.9\"\nedition = \"2021\"\n"),
    );
    write(
        dir.path(),
        "Cargo.lock",
        &format!("version = 3\n\n[[package]]\nname = \"{bin_name}\"\nversion = \"9.9.9\"\n"),
    );
    write(
        dir.path(),
        "src/main.rs",
        "fn main() { println!(\"crozier 9.9.9 (built from the action's source)\"); }\n",
    );
    dir
}

/// `local` builds the action's own checkout with `cargo install` — never a
/// published release, so no mirror is offered.
#[test]
fn local_builds_the_action_source_with_cargo() {
    let source = local_source("crozier");
    let run = install(source.path(), "local", None, &[]);
    assert_eq!(run.status, 0, "{}", run.stderr);
    assert_eq!(
        version_of(&run.bin()),
        "crozier 9.9.9 (built from the action's source)"
    );
}

/// An install that leaves no `crozier` binary fails the step rather than hand
/// the compare step a path to nothing.
#[test]
fn an_install_without_a_crozier_binary_fails() {
    let source = local_source("not-crozier");
    let run = install(source.path(), "local", None, &[]);
    assert_eq!(run.status, 1, "{}", run.stderr);
    assert!(
        run.stderr.contains("no crozier binary at") && run.stderr.contains("ACTION:"),
        "{}",
        run.stderr
    );
    assert!(!run.outputs.contains_key("bin"));
}

/// The action runs on Linux and macOS runners only, and says so on Windows
/// before installing anything.
#[test]
fn a_windows_runner_is_refused() {
    let run = install(repo_root(), "v0.0.80", None, &[("RUNNER_OS", "Windows")]);
    assert_eq!(run.status, 1);
    assert!(
        run.stderr
            .contains("the crozier action runs on Linux and macOS runners only"),
        "{}",
        run.stderr
    );
    assert!(!run.root().exists());
}

/// Outside a runner the install step says what is missing and installs
/// nothing.
#[test]
fn install_refuses_a_missing_runner_environment() {
    for (missing, named) in [
        ("GITHUB_ACTION_PATH", "GITHUB_ACTION_PATH is not set"),
        ("RUNNER_TEMP", "RUNNER_TEMP is not set"),
    ] {
        let runner_temp = tempfile::tempdir().unwrap();
        let output_file = runner_temp.path().join("github-output");
        std::fs::write(&output_file, "").unwrap();
        let mut command = step("install.sh", repo_root(), runner_temp.path(), &[]);
        command
            .env("GITHUB_ACTION_PATH", repo_root())
            .env("GITHUB_OUTPUT", &output_file)
            .env("VERSION", "v0.0.80")
            .env_remove("RUNNER_OS")
            .env_remove(missing);
        let out = command.output().unwrap();
        let stderr = String::from_utf8_lossy(&out.stderr);
        assert_eq!(out.status.code(), Some(1), "{missing}: {stderr}");
        assert!(
            stderr.contains(named) && stderr.contains("ACTION:"),
            "{missing}: {stderr}"
        );
        assert!(!stderr.contains("downloading"), "{stderr}");
        assert_eq!(std::fs::read_to_string(&output_file).unwrap(), "");
    }
}

/// `ruff` is crozier's own dependency: absent, the action installs the version
/// `.ruff-version` pins, through the real `install-ruff.sh`; present, it is
/// left alone.
#[test]
fn ruff_is_installed_at_its_pinned_version_only_when_absent() {
    let pinned = std::fs::read_to_string(repo_root().join(".ruff-version")).unwrap();
    let mirror = Mirror::new(&["v0.0.80"]);
    let scratch = tempfile::tempdir().unwrap();
    let record = scratch.path().join("pipx-args");
    let stubs = tempfile::tempdir().unwrap();
    // llmlint: ignore[e2e_not_mocked] installing ruff means downloading it from PyPI, which an offline test cannot reach; the stand-in pipx records the package the real install-ruff.sh asked for, which is what the action decides. Everything before it — the action step, install-ruff.sh, .ruff-version — is real.
    write_executable(
        stubs.path(),
        "pipx",
        "#!/bin/sh\nprintf '%s\\n' \"$@\" > \"$RECORD\"\n",
    );
    // PATH without any `ruff`, the stand-in pipx first.
    let without_ruff = std::env::split_paths(&std::env::var("PATH").unwrap())
        .filter(|dir| !dir.join("ruff").exists())
        .collect::<Vec<_>>();
    let path =
        std::env::join_paths(std::iter::once(stubs.path().to_path_buf()).chain(without_ruff))
            .unwrap();
    let env = [
        ("PATH", path.to_str().unwrap()),
        ("RECORD", record.to_str().unwrap()),
        ("HOME", scratch.path().to_str().unwrap()),
    ];
    let run = install(repo_root(), "v0.0.80", Some(&mirror), &env);
    assert_eq!(run.status, 0, "{}", run.stderr);
    assert_eq!(
        std::fs::read_to_string(&record).unwrap(),
        format!("install\nruff=={}\n", pinned.trim())
    );

    // With `ruff` on PATH, nothing is installed for it.
    std::fs::remove_file(&record).unwrap();
    write_executable(stubs.path(), "ruff", "#!/bin/sh\n");
    let run = install(repo_root(), "v0.0.80", Some(&mirror), &env);
    assert_eq!(run.status, 0, "{}", run.stderr);
    assert!(!record.exists());
}
