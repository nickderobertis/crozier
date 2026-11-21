//! The README's **Retries** section against the client it documents: the
//! section is Fern's own text at the certified pair, in every layout and enum
//! mode, and the generated client retries exactly the status codes it lists.

use std::path::Path;

use assert_cmd::prelude::*;
use predicates::prelude::*;

/// One operation under a tag, with an enum field so the enum mode shapes a model.
const SPEC: &str = "openapi: 3.0.3
info: {title: Beacon, version: '1.0'}
servers: [{url: 'https://api.example.test'}]
paths:
  /lamps/{lampId}:
    get:
      operationId: getLamp
      tags: [lamps]
      parameters:
        - {name: lampId, in: path, required: true, schema: {type: string}}
      responses:
        '200':
          description: ok
          content:
            application/json:
              schema: {$ref: '#/components/schemas/Lamp'}
components:
  schemas:
    Lamp:
      type: object
      required: [id, state]
      properties:
        id: {type: string}
        state: {type: string, enum: [lit, dark]}
";

/// The layouts a README is written in, each beside a committed Fern reference
/// README of that layout: `(name, crozier flags, Fern reference)`.
const LAYOUTS: [(&str, &[&str], &str); 3] = [
    (
        "packaged",
        &["--layout", "packaged"],
        "tests/fixtures/openepcis-dpp-ready/expected/README.md",
    ),
    (
        "flat",
        &["--layout", "flat"],
        "tests/fixtures/client-class-name/expected-flat/README.md",
    ),
    (
        "literals",
        &["--layout", "packaged", "--enum-type", "literals"],
        "tests/fixtures/happy-hamster/expected-literals/README.md",
    ),
];

/// The status-code paragraph of a README's Retries section: from the sentence
/// that introduces the list up to the `max_retries` sentence after it.
fn retried_codes_paragraph(readme: &str) -> &str {
    let start = readme
        .find("A request is deemed retryable when")
        .unwrap_or_else(|| panic!("no retryable-status sentence in:\n{readme}"));
    let end = start
        + readme[start..]
            .find("Use the `max_retries` request option")
            .expect("the max_retries sentence follows the list");
    &readme[start..end]
}

/// Generate the probe in `layout` under `dir`; returns the README path and the
/// directory to import the `beacon` package from.
fn generate(dir: &Path, name: &str, flags: &[&str]) -> (std::path::PathBuf, std::path::PathBuf) {
    let spec = dir.join("beacon.yml");
    std::fs::write(&spec, SPEC).unwrap();
    // A flat tree is the package itself, so it is written as `beacon/`.
    let root = dir.join(name);
    let out = if name == "flat" {
        root.join("beacon")
    } else {
        root.clone()
    };
    super::crozier_clean_env()
        .args(["--no-config", "generate", "python", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(&out)
        .args(["--package-name", "beacon"])
        .args(flags)
        .assert()
        .success();
    let import_root = if name == "flat" {
        root
    } else {
        out.join("src")
    };
    (out.join("README.md"), import_root)
}

/// The Retries section's status codes are Fern's text byte for byte, in every
/// layout and enum mode crozier writes a README in.
#[test]
fn readme_retries_section_is_fern_text_in_every_layout() {
    let repo = super::repo_root();
    let dir = tempfile::tempdir().unwrap();
    for (name, flags, reference) in LAYOUTS {
        let (readme, _) = generate(dir.path(), name, flags);
        let written = std::fs::read_to_string(&readme).unwrap();
        let fern = std::fs::read_to_string(repo.join(reference)).unwrap();
        assert_eq!(
            retried_codes_paragraph(&written),
            retried_codes_paragraph(&fern),
            "{name}: the Retries list differs from {reference}"
        );
    }
}

/// The generated client, behind a real local HTTP server, retries each status
/// its README lists and no other: 408, 409, 429 and every 5xx are attempted
/// twice under `max_retries=1`, an unlisted 4xx once. A README naming fewer
/// codes than the client retries is caught, and one with no list is refused.
#[test]
#[ignore = "SDK Python-environment tier (builds a venv from PyPI, runs mypy/pytest); run via `just test-sdk-env`"]
fn sdk_env_client_retries_exactly_what_its_readme_lists() {
    let repo = super::repo_root();
    let python = super::runtime_python_env().expect("SDK runtime environment");
    let script = repo.join("crates/crozier-e2e/tests/e2e/readme_retries_wire.py");
    let dir = tempfile::tempdir().unwrap();
    for (name, flags, _) in LAYOUTS {
        let (readme, import_root) = generate(dir.path(), name, flags);
        // llmlint: ignore-block[e2e_not_mocked] A local http.server stands in for the API alone, as in sdk_env_default_max_retries_bounds_the_attempts_a_client_makes; crozier and the emitted client run unmodified.
        std::process::Command::new(&python)
            .env("PYTHONDONTWRITEBYTECODE", "1")
            .arg(&script)
            .arg(&readme)
            .arg(&import_root)
            .args(["beacon", "BeaconApi"])
            .assert()
            .success()
            .stdout(
                predicate::str::diff(
                    "9 of 17 status(es) retried as the README lists, sync and async\n",
                )
                .normalize(),
            );
        // A README that drops 409 from its list no longer describes the client.
        let narrowed = dir.path().join(format!("{name}-narrowed.md"));
        let text = std::fs::read_to_string(&readme).unwrap();
        let kept: Vec<&str> = text
            .lines()
            .filter(|line| !line.starts_with("- [409]"))
            .collect();
        std::fs::write(&narrowed, kept.join("\n")).unwrap();
        std::process::Command::new(&python)
            .env("PYTHONDONTWRITEBYTECODE", "1")
            .arg(&script)
            .arg(&narrowed)
            .arg(&import_root)
            .args(["beacon", "BeaconApi"])
            .assert()
            .code(1)
            .stderr(predicate::str::contains(
                "sync 409: 2 attempt(s), the README implies 1",
            ));
        // llmlint: ignore-end[e2e_not_mocked]
    }
    let empty = dir.path().join("empty.md");
    std::fs::write(&empty, "# Beacon\n").unwrap();
    std::process::Command::new(&python)
        .arg(&script)
        .arg(&empty)
        .arg(dir.path().join("packaged/src"))
        .args(["beacon", "BeaconApi"])
        .assert()
        .code(2)
        .stderr(predicate::str::contains("no `### Retries` section"));
}
