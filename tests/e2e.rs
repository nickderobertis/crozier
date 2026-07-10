//! End-to-end tests: drive the compiled `crozier` binary the way a user does —
//! as a subprocess over real files in a real temp directory — and byte-compare
//! its (comment-stripped) output against the committed Fern fixtures.
//!
//! This is the product's only faithful QA loop, so it never mocks the generator,
//! the filesystem, or the process boundary. The `just check` gate runs it.

use std::path::{Path, PathBuf};

use assert_cmd::Command;
use predicates::prelude::*;

/// A vendored Fern corpus: the spec at `tests/fixtures/<api>/openapi.yml`, the
/// naming flags crozier is driven with, and the generated files it reproduces
/// byte-for-byte today (paths relative to the output root). Each `matched` list
/// is the source of truth for what that corpus matches; it grows as generation
/// lands. See docs/matching.md.
struct Corpus {
    api: &'static str,
    package_name: &'static str,
    project_name: &'static str,
    matched: &'static [&'static str],
}

/// Fern's OpenAPI-sourced `query-parameters-openapi` seed (offline corpus).
const QUERY_PARAMETERS: Corpus = Corpus {
    api: "query-parameters-openapi",
    package_name: "seed",
    project_name: "fern_query-parameters-openapi",
    matched: &[
        "src/seed/version.py",
        "src/seed/py.typed",
        "src/seed/types/user.py",
        "src/seed/types/nested_user.py",
    ],
};

/// The broad `exhaustive` target: Fern's Python output regenerated from the
/// vendored OpenAPI document (see scripts/generate-fern-fixture.sh). Every
/// `types/` module matches; only `types/__init__.py` (a lazy-loader over the
/// full type set) is still pending. See docs/matching.md.
const EXHAUSTIVE: Corpus = Corpus {
    api: "exhaustive",
    package_name: "fern",
    project_name: "default_package_name",
    matched: &[
        "src/fern/version.py",
        "src/fern/py.typed",
        // The static core runtime, emitted verbatim (assets/core/).
        "src/fern/core/__init__.py",
        "src/fern/core/api_error.py",
        "src/fern/core/client_wrapper.py",
        "src/fern/core/datetime_utils.py",
        "src/fern/core/file.py",
        "src/fern/core/force_multipart.py",
        "src/fern/core/http_client.py",
        "src/fern/core/http_response.py",
        "src/fern/core/http_sse/__init__.py",
        "src/fern/core/http_sse/_api.py",
        "src/fern/core/http_sse/_decoders.py",
        "src/fern/core/http_sse/_exceptions.py",
        "src/fern/core/http_sse/_models.py",
        "src/fern/core/jsonable_encoder.py",
        "src/fern/core/pydantic_utilities.py",
        "src/fern/core/query_encoder.py",
        "src/fern/core/remove_none_from_dict.py",
        "src/fern/core/request_options.py",
        "src/fern/core/serialization.py",
        "src/fern/types/bad_object_request_info.py",
        "src/fern/types/endpoints_error.py",
        "src/fern/types/endpoints_error_category.py",
        "src/fern/types/endpoints_error_code.py",
        "src/fern/types/endpoints_paginated_response.py",
        "src/fern/types/endpoints_put_response.py",
        "src/fern/types/types_animal.py",
        "src/fern/types/types_animal_one.py",
        "src/fern/types/types_animal_one_animal.py",
        "src/fern/types/types_animal_zero.py",
        "src/fern/types/types_animal_zero_animal.py",
        "src/fern/types/types_cat.py",
        "src/fern/types/types_documented_unknown_type.py",
        "src/fern/types/types_dog.py",
        "src/fern/types/types_double_optional.py",
        "src/fern/types/types_map_of_documented_unknown_type.py",
        "src/fern/types/types_mixed_type.py",
        "src/fern/types/types_nested_object_with_optional_field.py",
        "src/fern/types/types_nested_object_with_required_field.py",
        "src/fern/types/types_object_with_datetime_like_string.py",
        "src/fern/types/types_object_with_docs.py",
        "src/fern/types/types_object_with_documented_unknown_type.py",
        "src/fern/types/types_object_with_map_of_map.py",
        "src/fern/types/types_object_with_optional_field.py",
        "src/fern/types/types_object_with_required_field.py",
        "src/fern/types/types_object_with_unknown_field.py",
        "src/fern/types/types_optional_alias.py",
        "src/fern/types/types_weather_report.py",
        // Endpoint client package markers (one per operation group).
        "src/fern/endpoints_container/__init__.py",
        "src/fern/endpoints_content_type/__init__.py",
        "src/fern/endpoints_enum/__init__.py",
        "src/fern/endpoints_http_methods/__init__.py",
        "src/fern/endpoints_object/__init__.py",
        "src/fern/endpoints_pagination/__init__.py",
        "src/fern/endpoints_params/__init__.py",
        "src/fern/endpoints_primitive/__init__.py",
        "src/fern/endpoints_put/__init__.py",
        "src/fern/endpoints_union/__init__.py",
        "src/fern/endpoints_urls/__init__.py",
        "src/fern/inlinedrequests/__init__.py",
        "src/fern/noauth/__init__.py",
        "src/fern/noreqbody/__init__.py",
        "src/fern/reqwithheaders/__init__.py",
        // Per-tag raw clients for the no-request-body tags (path params only,
        // single JSON success response). Other tags await wider endpoint support.
        "src/fern/endpoints_put/raw_client.py",
        "src/fern/endpoints_urls/raw_client.py",
        "src/fern/noreqbody/raw_client.py",
        // Query-parameter-only tag (no request body, no headers).
        "src/fern/endpoints_pagination/raw_client.py",
        // Named enum (`$ref`) request body → `json=request` + content-type header.
        "src/fern/endpoints_enum/raw_client.py",
        // Scalar request bodies, incl. the uuid/byte content-type nuance.
        "src/fern/endpoints_primitive/raw_client.py",
        // Named union (`$ref`) request body → `convert_and_respect_annotation_metadata`.
        "src/fern/endpoints_union/raw_client.py",
        // Header params + a scalar body + a 204 (no-content) response.
        "src/fern/reqwithheaders/raw_client.py",
    ],
};

/// Path to a fixture directory under `tests/fixtures/`.
fn fixture_dir(api: &str) -> PathBuf {
    Path::new(env!("CARGO_MANIFEST_DIR"))
        .join("tests/fixtures")
        .join(api)
}

/// Fresh `crozier` command bound to the built binary.
fn crozier() -> Command {
    Command::cargo_bin("crozier").expect("crozier binary is built for tests")
}

/// Drive the compiled binary over a corpus's spec and require every file in its
/// `matched` list to equal the committed fixture once comments are stripped.
fn assert_corpus_matches(c: &Corpus) {
    let fixtures = fixture_dir(c.api);
    let out = tempfile::tempdir().expect("tempdir");

    crozier()
        .args(["generate", "--spec"])
        .arg(fixtures.join("openapi.yml"))
        .arg("--output")
        .arg(out.path())
        .args([
            "--package-name",
            c.package_name,
            "--project-name",
            c.project_name,
        ])
        .assert()
        .success()
        .stderr(predicate::str::contains("generated"));

    for rel in c.matched {
        let generated = std::fs::read_to_string(out.path().join(rel))
            .unwrap_or_else(|e| panic!("crozier did not write {rel}: {e}"));
        let expected = std::fs::read_to_string(fixtures.join("expected").join(rel))
            .unwrap_or_else(|e| panic!("missing fixture {rel}: {e}"));
        // Strip comments from crozier's output the same way the fixtures were
        // produced, then require an exact match.
        assert_eq!(
            crozier::strip_python_comments(&generated),
            expected,
            "generated {rel} does not match the Fern fixture (comments stripped)"
        );
    }
}

#[test]
fn query_parameters_matches_fern_output_byte_for_byte() {
    assert_corpus_matches(&QUERY_PARAMETERS);
}

#[test]
fn exhaustive_matches_fern_output_byte_for_byte() {
    assert_corpus_matches(&EXHAUSTIVE);
}

#[test]
fn missing_spec_fails_with_actionable_message() {
    let out = tempfile::tempdir().expect("tempdir");
    crozier()
        .args(["generate", "--spec", "does-not-exist.yml", "--output"])
        .arg(out.path())
        .assert()
        .failure()
        .code(1)
        .stderr(predicate::str::contains("could not read spec"));
}

#[test]
fn unsupported_extension_fails() {
    let dir = tempfile::tempdir().expect("tempdir");
    let spec = dir.path().join("api.txt");
    std::fs::write(&spec, "openapi: 3.0.0").unwrap();
    let out = dir.path().join("out");
    crozier()
        .args(["generate", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(&out)
        .assert()
        .failure()
        .code(1)
        .stderr(predicate::str::contains("unsupported spec extension"));
}

#[test]
fn non_openapi_document_fails_clearly() {
    let dir = tempfile::tempdir().expect("tempdir");
    let spec = dir.path().join("api.yml");
    std::fs::write(&spec, "just: some yaml\nnot: openapi\n").unwrap();
    let out = dir.path().join("out");
    crozier()
        .args(["generate", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(&out)
        .assert()
        .failure()
        .code(1)
        .stderr(predicate::str::contains("missing `openapi` version"));
}

#[test]
fn unsupported_openapi_version_fails() {
    let dir = tempfile::tempdir().expect("tempdir");
    let spec = dir.path().join("api.yml");
    std::fs::write(&spec, "openapi: 2.0\ninfo:\n  title: Old\n").unwrap();
    let out = dir.path().join("out");
    crozier()
        .args(["generate", "--spec"])
        .arg(&spec)
        .arg("--output")
        .arg(&out)
        .assert()
        .failure()
        .code(1)
        .stderr(predicate::str::contains("crozier supports 3.x"));
}

#[test]
fn help_lists_generate() {
    crozier()
        .arg("--help")
        .assert()
        .success()
        .stdout(predicate::str::contains("generate"));
}
