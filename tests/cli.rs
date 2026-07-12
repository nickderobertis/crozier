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
    assert!(
        sentinel.is_file(),
        "a rejected run must not touch the filesystem"
    );
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
fn generate_python_selector_works() {
    // The explicit built-in `python` selector generates exactly like the
    // no-selector form — it works with zero config file.
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.yml");
    std::fs::write(&spec, SPEC).unwrap();
    let out = dir.path().join("out");

    run_from([
        "crozier",
        "generate",
        "python",
        "--spec",
        spec.to_str().unwrap(),
        "--output",
        out.to_str().unwrap(),
        "--package-name",
        "tiny",
    ])
    .expect("generate python ok");

    assert!(out.join("src/tiny/types/thing.py").is_file());
}

/// Write a spec and return `(tempdir, spec_path, out_dir)` for the config tests.
fn spec_and_out() -> (tempfile::TempDir, std::path::PathBuf, std::path::PathBuf) {
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.yml");
    std::fs::write(&spec, SPEC).unwrap();
    let out = dir.path().join("out");
    (dir, spec, out)
}

#[test]
fn config_file_drives_a_named_generator() {
    let (dir, spec, out) = spec_and_out();
    let cfg = dir.path().join("crozier.yml");
    std::fs::write(
        &cfg,
        format!(
            "generators:\n  admin:\n    spec: {}\n    output: {}\n    package-name: admin\n",
            spec.display(),
            out.display()
        ),
    )
    .unwrap();

    run_from([
        "crozier",
        "--config",
        cfg.to_str().unwrap(),
        "generate",
        "admin",
    ])
    .expect("config-driven generate ok");

    assert!(out.join("src/admin/types/thing.py").is_file());
    drop(dir);
}

#[test]
fn generate_all_runs_every_configured_generator() {
    // Two generators sharing the top-level spec, each with its own output/name.
    let (dir, spec, _out) = spec_and_out();
    let out_a = dir.path().join("a");
    let out_b = dir.path().join("b");
    let cfg = dir.path().join("crozier.yml");
    std::fs::write(
        &cfg,
        format!(
            "spec: {}\ngenerators:\n  a:\n    output: {}\n    package-name: a\n  b:\n    output: {}\n    package-name: b\n",
            spec.display(),
            out_a.display(),
            out_b.display()
        ),
    )
    .unwrap();

    // No selector → run both configured generators.
    run_from(["crozier", "--config", cfg.to_str().unwrap(), "generate"]).expect("generate-all ok");

    assert!(out_a.join("src/a/types/thing.py").is_file());
    assert!(out_b.join("src/b/types/thing.py").is_file());
    drop(dir);
}

#[test]
fn per_generation_flags_with_multiple_generators_error() {
    let (dir, spec, _out) = spec_and_out();
    let cfg = dir.path().join("crozier.yml");
    std::fs::write(
        &cfg,
        format!(
            "spec: {}\ngenerators:\n  a:\n    output: {}\n  b:\n    output: {}\n",
            spec.display(),
            dir.path().join("a").display(),
            dir.path().join("b").display()
        ),
    )
    .unwrap();

    let err = run_from([
        "crozier",
        "--config",
        cfg.to_str().unwrap(),
        "generate",
        "--package-name",
        "x",
    ])
    .unwrap_err();
    assert!(err.contains("single generator"), "{err}");
    drop(dir);
}

#[test]
fn unknown_generator_is_an_error() {
    let (dir, spec, out) = spec_and_out();
    let cfg = dir.path().join("crozier.yml");
    std::fs::write(
        &cfg,
        format!(
            "generators:\n  admin:\n    spec: {}\n    output: {}\n",
            spec.display(),
            out.display()
        ),
    )
    .unwrap();

    let err = run_from([
        "crozier",
        "--config",
        cfg.to_str().unwrap(),
        "generate",
        "nope",
    ])
    .unwrap_err();
    assert!(err.contains("unknown generator"), "{err}");
    // The message lists what could be run instead.
    assert!(err.contains("admin") && err.contains("python"), "{err}");
    drop(dir);
}

#[test]
fn bare_generate_without_a_spec_is_an_actionable_error() {
    // No config, no flags: the built-in `python` generator has nothing to read.
    let err = run_from(["crozier", "--no-config"]).unwrap_err();
    assert!(err.contains("no spec"), "{err}");
}

#[test]
fn missing_config_file_is_an_error() {
    let err = run_from(["crozier", "--config", "no-such-config.yml", "generate"]).unwrap_err();
    assert!(err.contains("not found"), "{err}");
}

#[test]
fn init_writes_a_config_with_the_schema_modeline() {
    let dir = tempfile::tempdir().unwrap();
    let cfg = dir.path().join("crozier.yml");
    run_from(["crozier", "init", "--output", cfg.to_str().unwrap()]).expect("init ok");

    let body = std::fs::read_to_string(&cfg).unwrap();
    // The `$schema` modeline leads the file so the YAML language server uses it.
    assert!(
        body.starts_with("# yaml-language-server: $schema="),
        "{body}"
    );
    assert!(body.contains("crozier.schema.json"), "{body}");
    // The generated starter parses and declares the built-in python generator.
    let parsed = crozier::settings::parse(&body).expect("starter config parses");
    assert!(parsed.generators.contains_key("python"));
}

#[test]
fn init_refuses_to_clobber_without_force() {
    let dir = tempfile::tempdir().unwrap();
    let cfg = dir.path().join("crozier.yml");
    std::fs::write(&cfg, "spec: ./x.yml").unwrap();

    let err = run_from(["crozier", "init", "--output", cfg.to_str().unwrap()]).unwrap_err();
    assert!(err.contains("already exists"), "{err}");
    // --force overwrites with the starter.
    run_from([
        "crozier",
        "init",
        "--output",
        cfg.to_str().unwrap(),
        "--force",
    ])
    .expect("force overwrite ok");
    assert!(std::fs::read_to_string(&cfg)
        .unwrap()
        .contains("generators:"));
}

#[test]
fn config_inspects_without_a_spec() {
    // `config` reports the layered config even when spec/output are incomplete —
    // it never runs generation, so a missing spec is fine.
    let (dir, spec, out) = spec_and_out();
    let cfg = dir.path().join("crozier.yml");
    std::fs::write(
        &cfg,
        format!(
            "spec: {}\ngenerators:\n  python:\n    output: {}\n  admin:\n    output: {}\n",
            spec.display(),
            out.display(),
            dir.path().join("admin").display()
        ),
    )
    .unwrap();

    // All generators, one generator, and the built-in-only (no-config) path.
    run_from(["crozier", "--config", cfg.to_str().unwrap(), "config"]).expect("config all ok");
    run_from([
        "crozier",
        "--config",
        cfg.to_str().unwrap(),
        "config",
        "admin",
    ])
    .expect("config one ok");
    run_from(["crozier", "--no-config", "config"]).expect("config built-in ok");
    drop(dir);
}

#[test]
fn config_unknown_generator_errors() {
    let err = run_from(["crozier", "--no-config", "config", "nope"]).unwrap_err();
    assert!(err.contains("unknown generator"), "{err}");
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
fn operation_without_operation_id_generates() {
    // `operationId` is optional in OpenAPI; crozier synthesizes one from the
    // tag/path + method rather than rejecting the document (issue #40).
    let dir = tempfile::tempdir().unwrap();
    let spec = dir.path().join("api.yml");
    std::fs::write(
        &spec,
        "openapi: 3.0.0\ninfo:\n  title: X\npaths:\n  /thing:\n    get:\n      tags: [Thing]\n      \
         responses:\n        '200':\n          description: OK\n          content:\n            \
         application/json:\n              schema:\n                type: object\n                \
         properties:\n                  ok: { type: boolean }\n",
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
    ])
    .expect("missing operationId is synthesized, not rejected");
    // The tag becomes the client module.
    assert!(
        out.join("src/x/thing").is_dir(),
        "expected a `thing` client module"
    );
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
