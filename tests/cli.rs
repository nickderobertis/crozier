//! In-process CLI tests. These call `crozier::cli::run_from` directly (not the
//! binary), so they are measured by coverage and exercise the dispatch and error
//! branches. The binary itself is driven end-to-end in `tests/e2e.rs`.

use crozier::cli::run_from;

/// Minimal valid spec with one named object schema.
const SPEC: &str = "openapi: 3.0.0\ninfo:\n  title: Tiny\ncomponents:\n  schemas:\n    Thing:\n      type: object\n      properties:\n        name:\n          type: string\n";

#[test]
fn generate_succeeds_and_writes() {
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.yml");
    std::fs::write(&spec, SPEC).unwrap();
    let out = dir.path().join("out");

    run_from([
        "crozier",
        "generate",
        "--spec",
        spec.to_str().unwrap(),
        "--output",
        out.to_str().unwrap(),
        "--package-name",
        "tiny",
    ])
    .expect("generate ok");

    assert!(out.join("src/tiny/types/thing.py").is_file());
}

#[test]
fn traversal_package_name_is_rejected_before_any_delete() {
    // A crafted --package-name must not reach the regeneration `remove_dir_all`.
    // The output dir holds a sentinel; a rejected run must leave it untouched.
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.yml");
    std::fs::write(&spec, SPEC).unwrap();
    let out = dir.path().join("out");
    std::fs::create_dir_all(&out).unwrap();
    let sentinel = out.join("keep.txt");
    std::fs::write(&sentinel, "do not delete").unwrap();

    for bad in ["../evil", "..", "a/b", "/etc"] {
        let err = run_from([
            "crozier",
            "generate",
            "--spec",
            spec.to_str().unwrap(),
            "--output",
            out.to_str().unwrap(),
            "--package-name",
            bad,
        ])
        .unwrap_err();
        assert!(err.contains("invalid package name"), "{bad}: {err}");
    }
    assert!(sentinel.is_file(), "a rejected run must not touch the filesystem");
}

#[test]
fn regeneration_prunes_stale_modules() {
    // Regenerating into a populated output dir clears the crozier-owned package
    // tree first, so a schema removed from the spec does not leave an orphan.
    let dir = tempfile::tempdir().unwrap();
    let out = dir.path().join("out");

    let two = dir.path().join("two.yml");
    std::fs::write(
        &two,
        "openapi: 3.0.0\ninfo:\n  title: T\ncomponents:\n  schemas:\n    Widget:\n      type: object\n      properties:\n        id:\n          type: string\n    Gadget:\n      type: object\n      properties:\n        id:\n          type: string\n",
    )
    .unwrap();
    run_from([
        "crozier",
        "generate",
        "--spec",
        two.to_str().unwrap(),
        "--output",
        out.to_str().unwrap(),
        "--package-name",
        "t",
    ])
    .expect("first generate ok");
    assert!(out.join("src/t/types/gadget.py").is_file());

    let one = dir.path().join("one.yml");
    std::fs::write(
        &one,
        "openapi: 3.0.0\ninfo:\n  title: T\ncomponents:\n  schemas:\n    Widget:\n      type: object\n      properties:\n        id:\n          type: string\n",
    )
    .unwrap();
    run_from([
        "crozier",
        "generate",
        "--spec",
        one.to_str().unwrap(),
        "--output",
        out.to_str().unwrap(),
        "--package-name",
        "t",
    ])
    .expect("regenerate ok");
    assert!(out.join("src/t/types/widget.py").is_file());
    assert!(!out.join("src/t/types/gadget.py").exists());
}

#[test]
fn internal_strip_runs() {
    let dir = tempfile::tempdir().unwrap();
    let file = dir.path().join("x.py");
    std::fs::write(&file, "x = 1  # comment\n").unwrap();
    run_from(["crozier", "internal-strip", file.to_str().unwrap()]).expect("strip ok");
}

#[test]
fn internal_strip_missing_file_errors() {
    let err = run_from(["crozier", "internal-strip", "no-such-file.py"]).unwrap_err();
    assert!(err.contains("could not read"), "{err}");
}

#[test]
fn generate_missing_spec_errors() {
    let dir = tempfile::tempdir().unwrap();
    let out = dir.path().join("out");
    let err = run_from([
        "crozier",
        "generate",
        "--spec",
        "missing.yml",
        "--output",
        out.to_str().unwrap(),
    ])
    .unwrap_err();
    assert!(err.contains("could not read spec"), "{err}");
}

#[test]
fn generate_json_spec_supported() {
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.json");
    std::fs::write(
        &spec,
        r#"{"openapi":"3.0.0","info":{"title":"J"},"components":{"schemas":{"A":{"type":"string"}}}}"#,
    )
    .unwrap();
    let out = dir.path().join("out");
    run_from([
        "crozier",
        "generate",
        "--spec",
        spec.to_str().unwrap(),
        "--output",
        out.to_str().unwrap(),
        "--package-name",
        "j",
    ])
    .expect("json spec ok");
    assert!(out.join("src/j/types/a.py").is_file());
}

#[test]
fn generate_malformed_json_errors() {
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.json");
    std::fs::write(&spec, "{ not valid json").unwrap();
    let out = dir.path().join("out");
    let err = run_from([
        "crozier",
        "generate",
        "--spec",
        spec.to_str().unwrap(),
        "--output",
        out.to_str().unwrap(),
    ])
    .unwrap_err();
    assert!(err.contains("could not parse OpenAPI document"), "{err}");
}

#[test]
fn generate_malformed_yaml_errors() {
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.yml");
    // Valid-looking key but a broken structure serde cannot map.
    std::fs::write(&spec, "openapi: 3.0.0\ninfo: [not, a, map]\n").unwrap();
    let out = dir.path().join("out");
    let err = run_from([
        "crozier",
        "generate",
        "--spec",
        spec.to_str().unwrap(),
        "--output",
        out.to_str().unwrap(),
    ])
    .unwrap_err();
    assert!(err.contains("could not parse OpenAPI document"), "{err}");
}

#[test]
fn unknown_flag_is_a_parse_error() {
    let err = run_from(["crozier", "generate", "--nope"]).unwrap_err();
    assert!(!err.is_empty());
}

#[test]
fn unsupported_extension_errors() {
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.txt");
    std::fs::write(&spec, "openapi: 3.0.0").unwrap();
    let err = run_from([
        "crozier",
        "generate",
        "--spec",
        spec.to_str().unwrap(),
        "--output",
        dir.path().join("out").to_str().unwrap(),
    ])
    .unwrap_err();
    assert!(err.contains("unsupported spec extension"), "{err}");
}

#[test]
fn missing_openapi_field_errors() {
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.yml");
    std::fs::write(&spec, "info:\n  title: X\n").unwrap();
    let err = run_from([
        "crozier",
        "generate",
        "--spec",
        spec.to_str().unwrap(),
        "--output",
        dir.path().join("out").to_str().unwrap(),
    ])
    .unwrap_err();
    assert!(err.contains("missing `openapi` version"), "{err}");
}

#[test]
fn operation_without_operation_id_errors() {
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.yml");
    std::fs::write(
        &spec,
        "openapi: 3.0.0\ninfo:\n  title: X\npaths:\n  /thing:\n    get:\n      tags: [Thing]\n",
    )
    .unwrap();
    let err = run_from([
        "crozier",
        "generate",
        "--spec",
        spec.to_str().unwrap(),
        "--output",
        dir.path().join("out").to_str().unwrap(),
    ])
    .unwrap_err();
    assert!(err.contains("operationId"), "{err}");
}

#[test]
fn unsupported_version_errors() {
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.yml");
    std::fs::write(&spec, "openapi: 2.0\ninfo:\n  title: X\n").unwrap();
    let err = run_from([
        "crozier",
        "generate",
        "--spec",
        spec.to_str().unwrap(),
        "--output",
        dir.path().join("out").to_str().unwrap(),
    ])
    .unwrap_err();
    assert!(err.contains("crozier supports 3.x"), "{err}");
}

#[test]
fn write_failure_surfaces_error() {
    // Make the output root a *file*, so creating the package directory under it
    // fails — exercising the WriteOutput error path.
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.yml");
    std::fs::write(&spec, SPEC).unwrap();
    let out_file = dir.path().join("out");
    std::fs::write(&out_file, "i am a file, not a directory").unwrap();
    let err = run_from([
        "crozier",
        "generate",
        "--spec",
        spec.to_str().unwrap(),
        "--output",
        out_file.to_str().unwrap(),
        "--package-name",
        "tiny",
    ])
    .unwrap_err();
    assert!(err.contains("could not write"), "{err}");
}
