//! The documentation audit, `documentation-audit.py`, held over crozier's own
//! output. Every whole-tree golden comparison runs it on the tree crozier
//! generated, so a documented example that does not bind to the generated
//! code fails the comparison that reads that golden. Byte parity alone cannot
//! show this: where crozier departs from Fern on a documentation line, this is
//! what shows the departed line binds. The script's checks and exit codes are
//! its docstring's; the journeys below drive each of them.

use std::path::Path;
use std::process::Command;

use super::{
    handwritten_document_as_json, probe_command, python_interpreter, repo_root, runtime_python_env,
};

/// The audit, beside the evidence note that reports its population.
const SCRIPT: &str = "docs/departures/evidence/documentation-audit/documentation-audit.py";

/// One run of the audit: its exit status, stdout rows and stderr.
struct Audit {
    status: Option<i32>,
    stdout: String,
    stderr: String,
}

fn audit(trees: &[&Path]) -> Audit {
    let python = python_interpreter().expect("a python3 interpreter runs the documentation audit");
    let output = Command::new(python)
        .arg(repo_root().join(SCRIPT))
        .args(trees)
        .output()
        .unwrap_or_else(|error| panic!("{SCRIPT} did not start: {error}"));
    Audit {
        status: output.status.code(),
        stdout: String::from_utf8_lossy(&output.stdout).into_owned(),
        stderr: String::from_utf8_lossy(&output.stderr).into_owned(),
    }
}

/// What the audit finds in crozier's generated tree `out`: nothing, when every
/// documented example binds to the code beside it.
pub(super) fn failures(out: &Path) -> Vec<String> {
    let found = audit(&[out]);
    let prefix = format!("{}\t", out.display());
    match found.status {
        Some(0) => Vec::new(),
        Some(1) => vec![format!(
            "crozier's documentation examples do not bind to the code it generates \
             ({SCRIPT}: file, line, check, detail). Fix the generator; where the bytes \
             are Fern's, depart from the defect through a catalogued departure:\n{}",
            found.stdout.replace(&prefix, "")
        )],
        _ => vec![format!(
            "{SCRIPT} could not audit {}: {}",
            out.display(),
            found.stderr.trim()
        )],
    }
}

/// One check's rows (the audit's fourth column names the check) that mention
/// `detail`, so an assertion reads only the finding it is about and another
/// check reporting the same file cannot satisfy it.
fn rows<'a>(found: &'a Audit, check: &str, detail: &str) -> Vec<&'a str> {
    found
        .stdout
        .lines()
        .filter(|row| row.split('\t').nth(3) == Some(check) && row.contains(detail))
        .collect()
}

/// crozier's tree for the hand-written `odometer-reading` document audits
/// clean. Each class of defect written into its README is then reported on the
/// line it lands on, and only that defect.
#[test]
fn the_audit_reports_each_defect_class_on_its_line_and_nothing_in_crozier_s_tree() {
    let scratch = tempfile::tempdir().unwrap();
    let document = handwritten_document_as_json("odometer-reading", scratch.path());
    let generated = scratch.path().join("crozier");
    probe_command(&document, &generated).assert().success();
    let clean = audit(&[&generated]);
    assert_eq!(clean.status, Some(0), "{}{}", clean.stdout, clean.stderr);
    assert!(clean.stdout.is_empty(), "{}", clean.stdout);
    assert!(clean.stderr.contains("1 tree(s)"), "{}", clean.stderr);

    let readme = generated.join("README.md");
    let original = std::fs::read_to_string(&readme).unwrap();
    let base = original.lines().count();
    let defects = [
        ("from fern import FernApi, NoSuchClient", "import", "`NoSuchClient` is not defined by `fern`"),
        ("from fern.nowhere import FernApi", "import", "module `fern.nowhere` is not in the tree"),
        ("client = FernApi(base_url=\"https://x\", tenant=1)", "call", "FernApi(...): keyword `tenant` is not a parameter"),
        ("client = FernApi()", "call", "FernApi(...): missing required ['base_url']"),
        ("client.record_reading(depot=\"YOUR_DEPOT\", vehicle=\"v\", metres=1, trip_count=1, drift=1, bias=1, checkpoints=[1])", "placeholder", "client.record_reading: `depot='YOUR_DEPOT'` for `int`"),
        ("client.no_such_method()", "call", "`client.no_such_method`: no such method"),
        // A top-level `await` or `yield` is exempt from the syntax check, as Fern
        // lays out async and streaming examples; the call it makes is still checked.
        (
            "await client.no_such_async()",
            "call",
            "`client.no_such_async`: no such method",
        ),
        (
            "yield client.no_such_stream()",
            "call",
            "`client.no_such_stream`: no such method",
        ),
        (
            "client.record_reading(1, depot=1, vehicle=\"v\", metres=1, trip_count=1, drift=1, bias=1, checkpoints=[1])",
            "call",
            "client.record_reading: 1 positional argument(s) for 0",
        ),
        ("client.f(depot=1, depot=2)", "syntax", "keyword argument repeated: depot"),
    ];
    let mut text = original.clone();
    for (code, _, _) in &defects {
        text.push_str(&format!("\n```python\n{code}\n```\n"));
    }
    std::fs::write(&readme, &text).unwrap();
    let found = audit(&[&generated]);
    assert_eq!(found.status, Some(1), "{}{}", found.stdout, found.stderr);
    for (index, (code, check, detail)) in defects.iter().enumerate() {
        // Each block is a blank line, its fence, then the code.
        let line = base + 3 + index * 4;
        let matched = rows(&found, check, detail);
        assert_eq!(
            matched,
            vec![format!(
                "{}\tREADME.md\t{line}\t{check}\t{detail}",
                generated.display()
            )],
            "{code}\n{}",
            found.stdout
        );
    }
    assert_eq!(
        found.stdout.lines().count(),
        defects.len(),
        "{}",
        found.stdout
    );
    // The gate's form of the same run names each finding without the tree.
    let failures = failures(&generated);
    assert_eq!(failures.len(), 1, "{failures:?}");
    assert!(
        failures[0].contains("README.md\t")
            && !failures[0].contains(&generated.display().to_string()),
        "{}",
        failures[0]
    );
}

/// A docstring example is read as the file writes it: an escaped `\n` inside
/// one of its string literals is not a line break, and a call it documents is
/// checked against the method it documents. A module that does not parse is
/// reported, not skipped.
#[test]
fn a_docstring_example_is_audited_as_the_client_module_writes_it() {
    let scratch = tempfile::tempdir().unwrap();
    let document = handwritten_document_as_json("odometer-reading", scratch.path());
    let generated = scratch.path().join("crozier");
    probe_command(&document, &generated).assert().success();
    let client = generated.join("src/fern/client.py");
    let text = std::fs::read_to_string(&client).unwrap();
    let escaped = text.replacen("vehicle=\"vehicle\",", "vehicle=\"a\\nb\",", 1);
    assert_ne!(escaped, text, "the docstring passes `vehicle=\"vehicle\"`");
    std::fs::write(&client, &escaped).unwrap();
    let found = audit(&[&generated]);
    assert_eq!(found.status, Some(0), "{}{}", found.stdout, found.stderr);
    let unbound = escaped.replacen("vehicle=\"a\\nb\",", "vehicles=\"v\",", 1);
    std::fs::write(&client, &unbound).unwrap();
    let found = audit(&[&generated]);
    assert_eq!(found.status, Some(1), "{}{}", found.stdout, found.stderr);
    assert_eq!(
        rows(&found, "call", "keyword `vehicles` is not a parameter").len(),
        1,
        "{}",
        found.stdout
    );
    // A client module that does not parse has docstrings nobody can read: the
    // module itself is the finding, never a silently skipped file.
    std::fs::write(&client, format!("{text}\ndef broken(:\n")).unwrap();
    let found = audit(&[&generated]);
    assert_eq!(found.status, Some(1), "{}{}", found.stdout, found.stderr);
    assert_eq!(
        rows(&found, "syntax", "the module does not parse").len(),
        1,
        "{}",
        found.stdout
    );
}

/// Fern's own README for the evidence tree of `readme-client-class-casing`
/// imports client classes its package does not define; the audit says so.
#[test]
fn the_audit_finds_fern_s_undefined_client_import() {
    let tree =
        repo_root().join("docs/departures/evidence/readme-client-class-casing/fern-reference");
    // Audited beside a clean tree, in one run: each row names its own tree.
    let scratch = tempfile::tempdir().unwrap();
    let document = handwritten_document_as_json("odometer-reading", scratch.path());
    let clean = scratch.path().join("crozier");
    probe_command(&document, &clean).assert().success();
    let found = audit(&[&clean, &tree]);
    assert_eq!(found.status, Some(1), "{}{}", found.stdout, found.stderr);
    assert!(found.stderr.contains("2 tree(s)"), "{}", found.stderr);
    let prefix = format!("{}\t", tree.display());
    assert!(
        found.stdout.lines().all(|row| row.starts_with(&prefix)),
        "{}",
        found.stdout
    );
    assert!(
        !rows(
            &found,
            "import",
            "`LanternharborApi` is not defined by `LanternHarbor`"
        )
        .is_empty(),
        "{}",
        found.stdout
    );
}

/// A path that is not a directory is refused with a reason, never audited as
/// clean; a directory that documents no example has nothing to find.
#[test]
fn the_audit_refuses_a_path_that_is_not_a_directory() {
    let scratch = tempfile::tempdir().unwrap();
    let file = scratch.path().join("README.md");
    std::fs::write(&file, "```python\nimport nowhere\n```\n").unwrap();
    for path in [file.clone(), scratch.path().join("missing")] {
        let found = audit(&[&path]);
        assert_eq!(found.status, Some(2), "{}{}", found.stdout, found.stderr);
        assert!(found.stdout.is_empty(), "{}", found.stdout);
        assert!(
            found
                .stderr
                .contains(&format!("{} is not a directory", path.display())),
            "{}",
            found.stderr
        );
        assert!(!failures(&path).is_empty());
    }
    // A README that is not UTF-8 is an input error naming it, never a clean tree.
    let unreadable = scratch.path().join("unreadable");
    std::fs::create_dir(&unreadable).unwrap();
    std::fs::write(unreadable.join("README.md"), b"```python\n\xff\xfe\n```\n").unwrap();
    let found = audit(&[&unreadable]);
    assert_eq!(found.status, Some(2), "{}{}", found.stdout, found.stderr);
    assert!(
        found
            .stderr
            .contains("README.md cannot be read as UTF-8 text"),
        "{}",
        found.stderr
    );
    std::fs::remove_dir_all(&unreadable).unwrap();
    std::fs::remove_file(&file).unwrap();
    let empty = audit(&[scratch.path()]);
    assert_eq!(empty.status, Some(0), "{}{}", empty.stdout, empty.stderr);
    assert!(
        empty.stderr.contains("1 tree(s), 0 block(s), 0 finding(s)"),
        "{}",
        empty.stderr
    );
}

/// With no tree the audit prints its usage and exits 2; asked for help it
/// prints the same usage and exits 0.
#[test]
fn the_audit_prints_its_usage_for_no_tree_and_for_help() {
    for (args, status) in [
        (&[][..], Some(2)),
        (&["-h"][..], Some(0)),
        (&["--help"][..], Some(0)),
    ] {
        let python =
            python_interpreter().expect("a python3 interpreter runs the documentation audit");
        let output = Command::new(python)
            .arg(repo_root().join(SCRIPT))
            .args(args)
            .output()
            .unwrap();
        assert_eq!(output.status.code(), status, "{args:?}");
        assert!(output.stdout.is_empty(), "{args:?}");
        let stderr = String::from_utf8_lossy(&output.stderr);
        assert!(
            stderr.contains("Audit the Python examples of generated SDK trees"),
            "{args:?}: {stderr}"
        );
    }
}

/// A string annotation whose forward reference does not parse is unknown, not
/// a crash: a `YOUR_*` placeholder passed for it is not flagged.
#[test]
fn a_forward_reference_that_does_not_parse_is_an_unknown_annotation() {
    let scratch = tempfile::tempdir().unwrap();
    let document = handwritten_document_as_json("odometer-reading", scratch.path());
    let generated = scratch.path().join("crozier");
    probe_command(&document, &generated).assert().success();
    let client = generated.join("src/fern/client.py");
    let text = std::fs::read_to_string(&client).unwrap();
    let malformed = text.replacen("        depot: int,\n", "        depot: \"[\",\n", 1);
    assert_ne!(malformed, text, "the sync client declares `depot: int`");
    std::fs::write(&client, malformed).unwrap();
    let readme = generated.join("README.md");
    let mut text = std::fs::read_to_string(&readme).unwrap();
    text.push_str("\n```python\nclient.record_reading(depot=\"YOUR_DEPOT\", vehicle=\"v\", metres=1, trip_count=1, drift=1, bias=1, checkpoints=[1])\n```\n");
    std::fs::write(&readme, text).unwrap();
    let found = audit(&[&generated]);
    assert_eq!(found.status, Some(0), "{}{}", found.stdout, found.stderr);
}

/// The authored probe whose required array header every operation takes, so
/// both generators promote it to a client constructor argument (#810).
const PROMOTED_ARRAY: &str = "docs/openapi-surface/authored-probes/353-promoted-required-array";

/// #810: a promoted array client header's constructor examples pass a list of
/// its item's placeholder, where the certified pair passes the `YOUR_*` string
/// the `typing.List[str]` annotation rejects (`non-string-client-header-example`).
/// The audit reports each certified construction and nothing in crozier's tree.
#[test]
fn a_promoted_array_header_is_constructed_from_a_list_in_every_docstring_example() {
    let probe = repo_root().join(PROMOTED_ARRAY);
    let scratch = tempfile::tempdir().unwrap();
    let generated = scratch.path().join("crozier");
    probe_command(&probe.join("openapi.yml"), &generated)
        .assert()
        .success();
    let constructions = |tree: &Path| -> Vec<String> {
        std::fs::read_to_string(tree.join("src/fern/client.py"))
            .unwrap()
            .lines()
            .map(str::trim)
            .filter(|line| line.starts_with("probe_param=") && *line != "probe_param=probe_param,")
            .map(str::to_owned)
            .collect()
    };
    // The two root client classes' examples and the sync and async methods'.
    assert_eq!(
        constructions(&generated),
        vec!["probe_param=[\"probeParam\", \"probeParam\"],"; 6]
    );
    let certified = probe.join("fern-expected");
    assert_eq!(
        constructions(&certified),
        vec!["probe_param=\"YOUR_PROBE_PARAM\","; 6]
    );
    let found = audit(&[&certified]);
    assert_eq!(found.status, Some(1), "{}{}", found.stdout, found.stderr);
    assert_eq!(
        rows(
            &found,
            "placeholder",
            "`probe_param='YOUR_PROBE_PARAM'` for `typing.List[str]`"
        )
        .len(),
        6,
        "{}",
        found.stdout
    );
    let ours = audit(&[&generated]);
    assert_eq!(ours.status, Some(0), "{}{}", ours.stdout, ours.stderr);
    assert!(ours.stdout.is_empty(), "{}", ours.stdout);
}

/// Each keyword a root client or method docstring passes to the client
/// constructor, validated strictly against the constructor's own annotation:
/// one `<where> <keyword> ok|rejected` line each.
const CONSTRUCTIONS: &str = r#"
import ast, inspect, sys, textwrap, typing
from pydantic import TypeAdapter, ValidationError
sys.path.insert(0, sys.argv[1])
import fern
for cls in (fern.FernApi, fern.AsyncFernApi):
    hints = typing.get_type_hints(cls.__init__)
    owners = [(cls.__name__, cls)] + [(f"{cls.__name__}.{name}", getattr(cls, name)) for name in ("probe", "other")]
    for where, owner in owners:
        code = textwrap.dedent(inspect.getdoc(owner).split("Examples\n--------\n", 1)[1])
        for node in ast.walk(ast.parse(code)):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == cls.__name__:
                for keyword in node.keywords:
                    try:
                        TypeAdapter(hints[keyword.arg]).validate_python(ast.literal_eval(keyword.value), strict=True)
                    except ValidationError:
                        print(where, keyword.arg, "rejected")
                    else:
                        print(where, keyword.arg, "ok")
"#;

// llmlint: ignore-block[expensive_tests_stay_behind_their_own_edge] This `sdk_env_*` journey runs only in the `sdk-env` project (tests/sdk_env/project.json: `tier:promoted`, `cache: false`), promoted out of the affected tier into its own required CI leg; crates/crozier-e2e/AGENTS.md makes `#[ignore]` the one mechanism that routes a journey to that project.
/// #810, run: every constructor example crozier documents for the promoted
/// array header validates against the generated `typing.List[str]` annotation,
/// and every certified one is rejected by it.
#[test]
#[ignore = "SDK Python-environment tier (builds a venv from PyPI); run via `just test-sdk-env`"]
fn sdk_env_promoted_array_header_examples_have_the_declared_type() {
    let python = runtime_python_env().expect("SDK runtime environment");
    let probe = repo_root().join(PROMOTED_ARRAY);
    let scratch = tempfile::tempdir().unwrap();
    let generated = scratch.path().join("crozier");
    probe_command(&probe.join("openapi.yml"), &generated)
        .assert()
        .success();
    let certified = scratch.path().join("certified");
    super::copy_dir(&probe.join("fern-expected"), &certified);
    let run = |tree: &Path| -> Vec<String> {
        let output = Command::new(&python)
            .args(["-c", CONSTRUCTIONS])
            .arg(tree.join("src"))
            .env("PYTHONDONTWRITEBYTECODE", "1")
            .output()
            .expect("run the construction check");
        assert!(
            output.status.success(),
            "{}",
            String::from_utf8_lossy(&output.stderr)
        );
        let mut lines: Vec<String> = String::from_utf8_lossy(&output.stdout)
            .lines()
            .map(str::to_owned)
            .collect();
        lines.sort();
        lines
    };
    let wheres = [
        "AsyncFernApi",
        "AsyncFernApi.other",
        "AsyncFernApi.probe",
        "FernApi",
        "FernApi.other",
        "FernApi.probe",
    ];
    let expect = |verdict: &str| -> Vec<String> {
        wheres
            .iter()
            .map(|place| format!("{place} probe_param {verdict}"))
            .collect()
    };
    assert_eq!(run(&generated), expect("ok"));
    assert_eq!(run(&certified), expect("rejected"));
}
// llmlint: ignore-end[expensive_tests_stay_behind_their_own_edge]
