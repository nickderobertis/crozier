//! `default-max-retries` through the binary: its resolution through every
//! settings layer, its schema entry, and the client defaults it writes. Its Fern
//! parity is proven by the overlay goldens in `overlay_goldens.rs`; its runtime
//! effect by `sdk_env_default_max_retries_bounds_the_attempts_a_client_makes`.

use std::path::Path;

/// A document with one operation, enough for a root client and its wrappers.
pub(super) const SPEC: &str = "openapi: 3.0.0
info:
  title: Pets
paths:
  /pets:
    get:
      operationId: listPets
      tags: [Pets]
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema: { type: string }
";

/// `crozier config`'s `default-max-retries` row for the python generator in
/// `dir`: `(value, source)`.
fn retries_row(dir: &Path, env: &[(&str, &str)]) -> (String, String) {
    let mut command = super::crozier_clean_env();
    command.current_dir(dir).arg("config");
    for (name, value) in env {
        command.env(name, value);
    }
    let out = command.output().expect("run crozier config");
    let stdout = String::from_utf8(out.stdout).expect("utf-8 stdout");
    assert!(out.status.success(), "{stdout}");
    super::config_rows(&stdout, "python")
        .into_iter()
        .find(|(field, _, _)| field == "default-max-retries")
        .map(|(_, value, source)| (value, source))
        .unwrap_or_else(|| panic!("`crozier config` printed no default-max-retries row:\n{stdout}"))
}

/// The default the SDK generated under `out` was written with, asserting every
/// place the setting reaches agrees on it: the root clients' documented default
/// and fallback, and each client wrapper's parameter default.
fn written_default(out: &Path) -> String {
    let pkg = out.join("src/pets");
    let client = std::fs::read_to_string(pkg.join("client.py")).expect("client.py");
    let wrapper =
        std::fs::read_to_string(pkg.join("core/client_wrapper.py")).expect("client_wrapper.py");
    let fallbacks: Vec<&str> = client
        .lines()
        .filter_map(|line| {
            line.trim().strip_prefix(
                "_defaulted_max_retries = max_retries if max_retries is not None else ",
            )
        })
        .collect();
    assert_eq!(
        fallbacks.len(),
        2,
        "a sync and an async root client:\n{client}"
    );
    let value = fallbacks[0].to_string();
    assert!(fallbacks.iter().all(|v| *v == value), "{client}");
    assert_eq!(
        client
            .matches(&format!("Defaults to {value}. Per-request"))
            .count(),
        2,
        "{client}"
    );
    assert_eq!(
        wrapper
            .matches(&format!("max_retries: int = {value},"))
            .count(),
        3,
        "the base, sync and async wrappers:\n{wrapper}"
    );
    value
}

/// `default-max-retries` resolves CLI > `CROZIER_DEFAULT_MAX_RETRIES` >
/// `generators.<name>` > Fern's default of 2, like every Python-generator
/// setting; `crozier config` names the layer that won; it has no shared
/// top-level form; and a bad value is refused before anything is written.
#[test]
fn default_max_retries_resolves_through_every_layer_through_the_binary() {
    let dir = tempfile::tempdir().expect("tempdir");
    std::fs::write(dir.path().join("api.yml"), SPEC).unwrap();
    let config = dir.path().join("crozier.yml");
    let pair = |value: &str, source: &str| (value.to_string(), source.to_string());
    let generate = |env: &[(&str, &str)], args: &[&str], output: &str| {
        let mut command = super::crozier_clean_env();
        command.current_dir(dir.path());
        for (name, value) in env {
            command.env(name, value);
        }
        command
            .args(["generate", "python", "--output", output])
            .args(args)
            .assert()
            .success();
        written_default(&dir.path().join(output))
    };

    // No layer: Fern's default of 2, unchanged.
    std::fs::write(
        &config,
        "spec: ./api.yml\ngenerators:\n  python:\n    package-name: pets\n",
    )
    .unwrap();
    assert_eq!(retries_row(dir.path(), &[]), pair("2", "default"));
    assert_eq!(generate(&[], &[], "default"), "2");

    // The generator's own entry.
    std::fs::write(
        &config,
        "spec: ./api.yml\ngenerators:\n  python:\n    package-name: pets\n    default-max-retries: 0\n",
    )
    .unwrap();
    assert_eq!(retries_row(dir.path(), &[]), pair("0", "generator"));
    assert_eq!(generate(&[], &[], "generator"), "0");

    // The environment beats the config file; the flag beats the environment.
    let env = [("CROZIER_DEFAULT_MAX_RETRIES", "5")];
    assert_eq!(retries_row(dir.path(), &env), pair("5", "env"));
    assert_eq!(generate(&env, &[], "env"), "5");
    assert_eq!(generate(&env, &["--default-max-retries", "1"], "flag"), "1");

    // Python-generator-specific: a shared top-level value is a config error.
    std::fs::write(&config, "spec: ./api.yml\ndefault-max-retries: 0\n").unwrap();
    super::crozier_clean_env()
        .current_dir(dir.path())
        .arg("config")
        .assert()
        .failure()
        .stderr(predicates::str::contains("default-max-retries"));

    // A bad value is refused, from any layer, and writes nothing.
    std::fs::write(
        &config,
        "spec: ./api.yml\ngenerators:\n  python:\n    package-name: pets\n",
    )
    .unwrap();
    super::crozier_clean_env()
        .current_dir(dir.path())
        .env("CROZIER_DEFAULT_MAX_RETRIES", "-1")
        .args(["generate", "python", "--output", "bad-env"])
        .assert()
        .failure()
        .code(1)
        .stderr(predicates::str::contains(
            "`CROZIER_DEFAULT_MAX_RETRIES` must be a non-negative integer, got `-1`",
        ));
    super::crozier_clean_env()
        .current_dir(dir.path())
        .args([
            "generate",
            "python",
            "--output",
            "bad-flag",
            "--default-max-retries",
            "many",
        ])
        .assert()
        .failure()
        .code(2)
        .stderr(predicates::str::contains("--default-max-retries"));
    std::fs::write(
        &config,
        "spec: ./api.yml\ngenerators:\n  python:\n    package-name: pets\n    default-max-retries: -1\n",
    )
    .unwrap();
    super::crozier_clean_env()
        .current_dir(dir.path())
        .args(["generate", "python", "--output", "bad-file"])
        .assert()
        .failure()
        .stderr(predicates::str::contains("default-max-retries"));
    for bad in ["bad-env", "bad-flag", "bad-file"] {
        assert!(!dir.path().join(bad).exists(), "{bad}");
    }
}

/// The published JSON Schema documents `default-max-retries` on a generator as
/// a non-negative integer, and not at the shared top level.
#[test]
fn the_schema_documents_default_max_retries() {
    let out = super::crozier_clean_env()
        .arg("schema")
        .output()
        .expect("run crozier schema");
    assert!(out.status.success());
    let schema: serde_json::Value = serde_json::from_slice(&out.stdout).expect("schema JSON");
    let field = &schema["$defs"]["GeneratorSettings"]["properties"]["default-max-retries"];
    assert_eq!(
        field["type"],
        serde_json::json!(["integer", "null"]),
        "{field}"
    );
    assert_eq!(field["minimum"], 0, "{field}");
    assert!(schema["properties"].get("default-max-retries").is_none());
}
