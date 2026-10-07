//! The crozier-e2e project's report scripts — `fixtures-report.sh` (`just
//! fixtures-gaps` / `just fixtures-diff`) and `departures-ledger.sh` (`just
//! departures-ledger`) — run as the recipes run them, from a scratch checkout.
//!
//! Each script's whole job is to drive `cargo` over the e2e suite and shape
//! what it printed, so `cargo` is the one thing replaced: a stand-in first on
//! PATH that records how it was called and prints (or writes) what the real
//! reporter would. Running the real `cargo` here would rebuild and rerun this
//! very suite over the whole corpus from inside itself. Everything the script
//! does with that output — the report it extracts, the summary it requires,
//! the ledger it reports, the log and fix it prints on failure — is real.

use std::os::unix::fs::PermissionsExt;
use std::path::Path;
use std::process::Command;

use crate::{DIFFS_SUMMARY, GAPS_SUMMARY};

struct Run {
    /// The scratch checkout, kept until the case has read what the script wrote.
    root: tempfile::TempDir,
    status: i32,
    stdout: String,
    stderr: String,
    calls: String,
}

/// A scratch checkout holding `script` at its repository path, and a `cargo`
/// stand-in running `cargo_body` (under `sh`, `$CALLS` its call record).
fn run_script(script: &str, args: &[&str], cargo_body: &str, setup: impl FnOnce(&Path)) -> Run {
    let root = tempfile::tempdir().unwrap();
    let repo = Path::new(env!("CARGO_MANIFEST_DIR")).join("../..");
    let at = root.path().join("crates/crozier-e2e").join(script);
    std::fs::create_dir_all(at.parent().unwrap()).unwrap();
    std::fs::copy(repo.join("crates/crozier-e2e").join(script), &at).unwrap();
    let bin = root.path().join("bin");
    std::fs::create_dir(&bin).unwrap();
    let cargo = bin.join("cargo");
    // llmlint: ignore[e2e_not_mocked] the scripts' real path runs the ignored whole-corpus reporters or the entire crozier-e2e suite (departures-ledger.sh also rewrites tests/fixtures/departures-ledger.tsv), so running it here would rebuild and rerun this suite inside itself; these cases run the real scripts with only the `cargo` boundary stood in, covering extraction, a missing summary, a failing reporter, a refused merge and temp-file cleanup. The real path is `just fixtures-gaps` / `just fixtures-diff` / `just departures-ledger`.
    std::fs::write(
        &cargo,
        format!("#!/bin/sh\necho \"$*\" >> \"$CALLS\"\n{cargo_body}"),
    )
    .unwrap();
    std::fs::set_permissions(&cargo, std::fs::Permissions::from_mode(0o755)).unwrap();
    setup(root.path());
    let calls = root.path().join("calls");
    let path = std::env::join_paths(
        std::iter::once(bin).chain(std::env::split_paths(&std::env::var_os("PATH").unwrap())),
    )
    .unwrap();
    let out = Command::new("bash")
        .arg(&at)
        .args(args)
        .env("PATH", path)
        .env("CALLS", &calls)
        .env("TMPDIR", root.path())
        .output()
        .unwrap();
    let leftovers: Vec<_> = std::fs::read_dir(root.path())
        .unwrap()
        .filter_map(|entry| {
            let name = entry.unwrap().file_name().into_string().unwrap();
            name.starts_with("crozier-").then_some(name)
        })
        .collect();
    assert!(leftovers.is_empty(), "the script left {leftovers:?} behind");
    Run {
        root,
        status: out.status.code().unwrap(),
        stdout: String::from_utf8(out.stdout).unwrap(),
        stderr: String::from_utf8(out.stderr).unwrap(),
        calls: std::fs::read_to_string(&calls).unwrap_or_default(),
    }
}

/// What `cargo test` prints around a reporter's report: build lines before,
/// the harness's verdict after.
fn reporter_output(report: &str) -> String {
    format!(
        "printf '%s\\n' '   Compiling crozier-e2e' 'running 1 test' {report} 'test result: ok. 1 passed'\n"
    )
}

#[test]
fn each_report_prints_only_from_its_first_corpus_through_its_summary() {
    for (mode, reporter, summary) in [
        ("gaps", "report_fixture_gaps", GAPS_SUMMARY),
        ("diff", "report_fixture_diffs", DIFFS_SUMMARY),
    ] {
        let body = reporter_output(&format!(
            "'=== petstore' '  unmatched: a.py' '2 {summary}.'"
        ));
        let run = run_script("fixtures-report.sh", &[mode], &body, |_| {});
        assert_eq!(run.status, 0, "{mode}: {}", run.stderr);
        assert_eq!(
            run.stdout,
            format!("=== petstore\n  unmatched: a.py\n2 {summary}.\n")
        );
        assert_eq!(
            run.calls,
            format!(
                "test --locked -p crozier-e2e --test e2e -- --ignored --nocapture {reporter}\n"
            )
        );
    }
}

#[test]
fn a_report_of_any_size_survives_the_temporary_file() {
    let body = format!(
        "printf '=== big\\n'\nyes 'line of a long diff' | head -n 200000\nprintf '1 {GAPS_SUMMARY}.\\n'\n"
    );
    let run = run_script("fixtures-report.sh", &["gaps"], &body, |_| {});
    assert_eq!(run.status, 0, "{}", run.stderr);
    assert_eq!(run.stdout.lines().count(), 200_002);
}

#[test]
fn a_reporter_that_prints_no_summary_fails_with_its_log_and_the_fix() {
    // `cargo test <name>` exits 0 when the name matches no test.
    let body = "printf 'running 0 tests\\ntest result: ok. 0 passed\\n'\n";
    let run = run_script("fixtures-report.sh", &["gaps"], body, |_| {});
    assert_eq!(run.status, 1);
    assert_eq!(run.stdout, "");
    assert!(run.stderr.contains("running 0 tests"), "{}", run.stderr);
    assert!(
        run.stderr
            .contains("fixtures-report: no report from report_fixture_gaps (output above)"),
        "{}",
        run.stderr
    );
    assert!(
        run.stderr
            .contains("restore report_fixture_gaps in crates/crozier-e2e/tests/e2e.rs"),
        "{}",
        run.stderr
    );
}

#[test]
fn a_failing_reporter_fails_with_its_log() {
    let body =
        format!("printf '=== x\\n1 {DIFFS_SUMMARY}.\\npanicked at corpus missing\\n'\nexit 101\n");
    let run = run_script("fixtures-report.sh", &["diff"], &body, |_| {});
    assert_eq!(run.status, 1);
    assert_eq!(run.stdout, "");
    assert!(
        run.stderr.contains("panicked at corpus missing"),
        "{}",
        run.stderr
    );
    assert!(
        run.stderr.contains("pass a corpus that exists"),
        "{}",
        run.stderr
    );
}

#[test]
fn an_unknown_report_is_refused_with_the_usage() {
    let run = run_script("fixtures-report.sh", &["gap"], "", |_| {});
    assert_eq!(run.status, 1);
    assert_eq!(run.calls, "");
    assert!(
        run.stderr.contains("unknown report 'gap'")
            && run
                .stderr
                .contains("usage: crates/crozier-e2e/fixtures-report.sh gaps|diff"),
        "{}",
        run.stderr
    );
}

/// The stand-in for `cargo nextest`: the recording run leaves one record per
/// golden under `$CROZIER_RECORD_DEPARTURES`; the merge (`write_departures_ledger`)
/// writes the ledger from them, failing as `$MERGE_FAILS` says.
const NEXTEST: &str = r#"case "$*" in
  *write_departures_ledger*)
    [ -z "${MERGE_FAILS:-}" ] || { echo "ledger refused: $MERGE_FAILS"; exit 100; }
    { printf 'golden\tfile\tline\tdeparture\n'; cat "$CROZIER_RECORD_DEPARTURES"/*; } > tests/fixtures/departures-ledger.tsv ;;
  *)
    [ "${CROZIER_REQUIRE_CORPUS:-}" = 1 ] || { echo "recorded without CROZIER_REQUIRE_CORPUS"; exit 100; }
    [ -z "${RECORD_FAILS:-}" ] || { echo "comparison failed: $RECORD_FAILS"; exit 100; }
    printf 'petstore\tREADME.md\t1\tbranding\n' > "$CROZIER_RECORD_DEPARTURES/petstore"
    printf 'plantstore\tREADME.md\t1\tbranding\n' > "$CROZIER_RECORD_DEPARTURES/plantstore" ;;
esac
"#;

fn departures_ledger(env: &str) -> Run {
    run_script(
        "departures-ledger.sh",
        &[],
        &format!("{env}{NEXTEST}"),
        |root| {
            std::fs::create_dir_all(root.join("tests/fixtures")).unwrap();
            std::fs::write(
                root.join("tests/fixtures/departures-ledger.tsv"),
                "golden\tfile\tline\tdeparture\n",
            )
            .unwrap();
        },
    )
}

#[test]
fn the_ledger_is_recorded_then_merged_and_its_rows_reported() {
    let run = departures_ledger("");
    assert_eq!(run.status, 0, "{}", run.stderr);
    assert_eq!(
        std::fs::read_to_string(run.root.path().join("tests/fixtures/departures-ledger.tsv")).unwrap(),
        "golden\tfile\tline\tdeparture\npetstore\tREADME.md\t1\tbranding\nplantstore\tREADME.md\t1\tbranding\n"
    );
    assert_eq!(
        run.stdout,
        "departures-ledger: wrote tests/fixtures/departures-ledger.tsv (2 rows)\n"
    );
    let calls: Vec<_> = run.calls.lines().collect();
    assert_eq!(calls.len(), 2, "{}", run.calls);
    assert!(
        calls[0].starts_with("nextest run --locked -p crozier-e2e --no-fail-fast"),
        "{}",
        calls[0]
    );
    assert!(
        calls[0].contains("not test(/^departures_ledger_gate::/)"),
        "{}",
        calls[0]
    );
    assert!(
        calls[1].contains("--run-ignored only")
            && calls[1].contains("test(=departures_ledger_gate::write_departures_ledger)"),
        "{}",
        calls[1]
    );
}

#[test]
fn a_comparison_that_fails_while_recording_stops_before_the_merge() {
    let run = departures_ledger("RECORD_FAILS=petstore\n");
    assert_eq!(run.status, 1);
    assert_eq!(run.stdout, "");
    assert_eq!(
        run.calls.lines().count(),
        1,
        "the merge ran after a failed recording"
    );
    assert!(
        run.stderr.contains("comparison failed: petstore"),
        "{}",
        run.stderr
    );
    assert!(
        run.stderr
            .contains("departures-ledger: a comparison failed while recording (above)")
            && run
                .stderr
                .contains("fix it, then rerun just departures-ledger"),
        "{}",
        run.stderr
    );
}

#[test]
fn a_refused_merge_fails_with_its_log_and_the_fix() {
    let run = departures_ledger("MERGE_FAILS=duplicate-row\n");
    assert_eq!(run.status, 1);
    assert_eq!(run.stdout, "");
    assert!(
        run.stderr.contains("ledger refused: duplicate-row"),
        "{}",
        run.stderr
    );
    assert!(
        run.stderr
            .contains("departures-ledger: the merged ledger was refused (above)"),
        "{}",
        run.stderr
    );
}
