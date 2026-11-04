//! Ticket triage reuses landed measurements and holds each new reduction whole
//! against the certified pair. The index is the single list of ticket proofs.
use super::{crozier, filtered_tree_failures, repo_root};

pub(crate) const DIR: &str = "docs/fern-measurements/handed-off/follow-up-tickets";

fn read_rows(path: &std::path::Path) -> Result<Vec<[String; 6]>, String> {
    let text =
        std::fs::read_to_string(path).map_err(|error| format!("{}: {error}", path.display()))?;
    let mut lines = text.lines();
    if lines.next() != Some("source\troot_cause\tverdict\tmeasurement\tdeparture\tnote") {
        return Err(format!(
            "{}: expected the six-column ticket triage header",
            path.display()
        ));
    }
    lines
        .enumerate()
        .map(|(index, line)| {
            line.split('\t')
                .map(str::to_owned)
                .collect::<Vec<_>>()
                .try_into()
                .map_err(|cells: Vec<String>| {
                    format!(
                        "{}:{}: expected six columns, found {}",
                        path.display(),
                        index + 2,
                        cells.len()
                    )
                })
        })
        .collect()
}

fn rows() -> Vec<[String; 6]> {
    read_rows(&repo_root().join(format!("{DIR}.tsv"))).expect("valid ticket index")
}

/// Every independent replay validates the file before accessing its columns.
#[test]
fn follow_up_ticket_index_loader_rejects_bad_files_and_recovers() {
    let temp = tempfile::tempdir().unwrap();
    let path = temp.path().join("tickets.tsv");
    assert!(read_rows(&path).unwrap_err().contains("tickets.tsv"));
    std::fs::write(&path, "wrong header\n").unwrap();
    assert!(read_rows(&path).unwrap_err().contains("header"));
    let valid = std::fs::read_to_string(repo_root().join(format!("{DIR}.tsv"))).unwrap();
    let header = valid.lines().next().unwrap();
    for row in ["short\trow", "a\tb\tc\td\te\tf\tg"] {
        std::fs::write(&path, format!("{header}\n{row}\n")).unwrap();
        assert!(read_rows(&path)
            .unwrap_err()
            .contains(":2: expected six columns"));
    }
    std::fs::write(&path, &valid).unwrap();
    assert_eq!(read_rows(&path).unwrap(), rows());
}

#[test]
fn follow_up_ticket_index_holds_every_ticket_once() {
    let rows = rows();
    let actual: Vec<&str> = rows.iter().map(|row| row[1].as_str()).collect();
    assert_eq!(
        actual,
        ["602", "679", "685", "694", "696", "697", "698", "699", "700", "701", "702", "703"]
    );
    for row in rows {
        assert_eq!(
            row[0],
            format!(
                "https://github.com/nickderobertis/crozier/issues/{}",
                row[1]
            )
        );
        assert!(repo_root().join(&row[3]).join("README.md").is_file());
    }
}

// llmlint: ignore-block[expensive_tests_stay_behind_their_own_edge] These small SDK replays must drive the existing crozier-e2e binary and its golden comparison engine, as this task requires. The whole golden family inherits e2eReads; splitting that shared project edge is the already-drafted follow-up "Give crozier-e2e's generator-replay journeys an Nx edge narrower than e2eReads", outside this ticket triage.
#[test]
fn follow_up_ticket_matching_outputs_hold_against_the_certified_pair() {
    let mut failures = Vec::new();
    for row in rows()
        .iter()
        .filter(|row| row[2] == "already-matching" || row[2] == "parity-gap-repaired")
    {
        let case = repo_root().join(&row[3]);
        let golden = format!("{}fern-expected", row[3]);
        failures.extend(filtered_tree_failures(
            &row[1],
            &golden,
            &case.join("openapi.yml"),
            &case.join("fern-expected"),
            &[],
        ));
    }
    assert!(failures.is_empty(), "{}", failures.join("\n\n"));
}

#[test]
fn follow_up_ticket_refusals_hold_in_default_and_strict_modes() {
    for row in rows().iter().filter(|row| row[2] == "refusal-kept") {
        let case = repo_root().join(&row[3]);
        assert_ne!(
            std::fs::read_to_string(case.join("exit-code"))
                .unwrap()
                .trim(),
            "0"
        );
        assert!(!std::fs::read_to_string(case.join("fern.log"))
            .unwrap()
            .is_empty());
        let class = if row[1] == "679" {
            "generator-lint-failure"
        } else {
            "request-property-camelcase-collision"
        };
        for strict in [false, true] {
            let out = tempfile::tempdir().unwrap();
            let mut command = crozier();
            command
                .args(["generate", "--no-config", "--spec"])
                .arg(case.join("openapi.yml"))
                .arg("--output")
                .arg(out.path());
            if strict {
                command.arg("--fern-strict");
            }
            let result = command.output().unwrap();
            assert!(!result.status.success());
            assert!(
                String::from_utf8_lossy(&result.stderr).contains(class),
                "{}",
                String::from_utf8_lossy(&result.stderr)
            );
            assert!(std::fs::read_dir(out.path()).unwrap().next().is_none());
        }
    }
}

#[test]
fn follow_up_ticket_alias_refusal_recovers_with_safe_wire_names() {
    let source = repo_root().join(DIR).join("679/openapi.yml");
    let mut document: serde_json::Value =
        serde_json::from_str(&std::fs::read_to_string(source).unwrap()).unwrap();
    document["components"]["schemas"]["Reading"]["properties"] = serde_json::json!({
        "probe-code": {"type": "string"}
    });
    let temp = tempfile::tempdir().unwrap();
    let spec = temp.path().join("openapi.json");
    std::fs::write(&spec, document.to_string()).unwrap();
    let out = temp.path().join("sdk");
    let result = super::probe_command(&spec, &out).output().unwrap();
    assert!(
        result.status.success(),
        "{}",
        String::from_utf8_lossy(&result.stderr)
    );
    let model = std::fs::read_to_string(out.join("src/fern/types/reading.py")).unwrap();
    assert!(model.contains("alias=\"probe-code\""), "{model}");
}

#[test]
fn follow_up_ticket_escaped_quote_alias_still_matches_the_certified_pair() {
    let case = repo_root().join(DIR).join("679-escaped-quote-control");
    let golden = format!("{DIR}/679-escaped-quote-control/fern-expected");
    let failures = filtered_tree_failures(
        "679 escaped quote",
        &golden,
        &case.join("openapi.yml"),
        &case.join("fern-expected"),
        &[],
    );
    assert!(failures.is_empty(), "{}", failures.join("\n"));
}

#[test]
fn follow_up_ticket_invalid_aliases_refuse_with_the_class_in_both_modes() {
    for name in [
        "probe\"code",
        "probe\ncode",
        "probe\rcode",
        "probe\\x",
        "probe\\",
    ] {
        let mut document: serde_json::Value = serde_json::from_str(
            &std::fs::read_to_string(repo_root().join(DIR).join("679/openapi.yml")).unwrap(),
        )
        .unwrap();
        document["components"]["schemas"]["Reading"]["properties"] =
            serde_json::json!({name: {"type": "string"}});
        let temp = tempfile::tempdir().unwrap();
        let spec = temp.path().join("openapi.json");
        std::fs::write(&spec, document.to_string()).unwrap();
        for strict in [false, true] {
            let out = temp.path().join(if strict { "strict" } else { "default" });
            let mut command = super::probe_command(&spec, &out);
            if strict {
                command.arg("--fern-strict");
            }
            let result = command.output().unwrap();
            assert!(!result.status.success(), "{name:?}");
            assert!(
                String::from_utf8_lossy(&result.stderr).contains("generator-lint-failure"),
                "{}",
                String::from_utf8_lossy(&result.stderr)
            );
            assert!(!out.exists());
        }
    }
}

/// An existing nested-name component must retain its own identity and callers.
#[test]
fn follow_up_ticket_nested_null_identity_keeps_an_occupied_target() {
    let source = repo_root().join(DIR).join("696/openapi.yml");
    let mut document: serde_json::Value =
        serde_json::from_str(&std::fs::read_to_string(source).unwrap()).unwrap();
    document["components"]["schemas"]["SilenceOne"] = serde_json::json!({"type": "string"});
    document["components"]["schemas"]["Reading"]["properties"]["reserved"] =
        serde_json::json!({"$ref": "#/components/schemas/SilenceOne"});
    let temp = tempfile::tempdir().unwrap();
    let spec = temp.path().join("openapi.json");
    std::fs::write(&spec, document.to_string()).unwrap();
    let out = temp.path().join("sdk");
    let result = super::probe_command(&spec, &out).output().unwrap();
    assert!(
        result.status.success(),
        "{}",
        String::from_utf8_lossy(&result.stderr)
    );
    let read = |name: &str| std::fs::read_to_string(out.join("src/fern/types").join(name)).unwrap();
    assert!(read("silence.py").contains("Silence = typing.Optional[typing.Any]"));
    assert!(read("silence_one.py").contains("SilenceOne = str"));
    let model = read("reading.py");
    assert!(
        model.contains("silence: typing.Optional[Silence]"),
        "{model}"
    );
    assert!(
        model.contains("reserved: typing.Optional[SilenceOne]"),
        "{model}"
    );
}
/// An absent formatter is an installation error, not a Fern refusal.
#[test]
fn follow_up_ticket_alias_validation_reports_missing_ruff() {
    let temp = tempfile::tempdir().unwrap();
    let out = temp.path().join("sdk");
    let result = super::probe_command(&repo_root().join(DIR).join("679/openapi.yml"), &out)
        .env("PATH", temp.path())
        .output()
        .unwrap();
    assert!(!result.status.success());
    let error = String::from_utf8_lossy(&result.stderr);
    assert!(
        error.contains("could not run `ruff`") && error.contains("install ruff"),
        "{error}"
    );
    assert!(!error.contains("generator-lint-failure"), "{error}");
    assert!(!out.exists());
}

/// Exercise the real CLI's failure handling across a real child-process pipe.
/// The external ruff double drains stdin before its abnormal exit, or closes
/// stdin while the large alias is still being sent.
// llmlint: ignore-block[e2e_not_mocked] Only the external ruff failure mode is doubled at its process boundary: the real crozier CLI writes real temp files and sends bytes through real child pipes. Real ruff cannot deterministically consume stdin then simulate exit 2 or close its input prematurely; the successful real-ruff paths are held by the matching, refusal and recovery journeys above. The task explicitly permits real subprocess doubles for this failure contract.
#[cfg(unix)]
#[test]
fn follow_up_ticket_alias_validation_reports_ruff_process_failures() {
    use std::os::unix::fs::PermissionsExt;
    for (script, name, diagnostic) in [
        ("#!/bin/sh\nwhile IFS= read -r line; do :; done\nprintf 'formatter unavailable\\n' >&2\nexit 2\n", "probe\"code".to_string(), "formatter unavailable"),
        ("#!/bin/sh\nexec 0<&-\nexit 2\n", format!("{}\"", "p".repeat(2 * 1024 * 1024)), "could not write source to ruff"),
    ] {
        let temp = tempfile::tempdir().unwrap();
        let bin = temp.path().join("bin");
        std::fs::create_dir(&bin).unwrap();
        let ruff = bin.join("ruff");
        std::fs::write(&ruff, script).unwrap();
        std::fs::set_permissions(&ruff, std::fs::Permissions::from_mode(0o755)).unwrap();
        let source = repo_root().join(DIR).join("679/openapi.yml");
        let mut document: serde_json::Value = serde_json::from_str(&std::fs::read_to_string(source).unwrap()).unwrap();
        document["components"]["schemas"]["Reading"]["properties"] = serde_json::json!({name: {"type": "string"}});
        let spec = temp.path().join("openapi.json");
        std::fs::write(&spec, document.to_string()).unwrap();
        let out = temp.path().join("sdk");
        let result = super::probe_command(&spec, &out).env("PATH", &bin).output().unwrap();
        assert!(!result.status.success());
        let error = String::from_utf8_lossy(&result.stderr);
        assert!(error.contains("formatting field-alias.py with ruff failed") && error.contains(diagnostic), "{error}");
        assert!(!error.contains("generator-lint-failure"), "{error}");
        assert!(!out.exists());
    }
}
// llmlint: ignore-end[e2e_not_mocked]
// llmlint: ignore-end[expensive_tests_stay_behind_their_own_edge]
