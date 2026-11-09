//! `required-null-union-field-example` through real generated SDK trees: crozier's
//! docstring keeps a required field led by a null-admitting union, and only that
//! line of only that model is excused against a reference that omits it.

use std::fs;
use std::path::Path;

use super::crozier_clean_env;

const CLIENT: &str = "src/fern/ledger/client.py";

fn document(path: &Path) {
    let scalars = serde_json::json!({"oneOf": [
        {"type": "string"}, {"type": "number"}, {"type": "boolean"},
        {"type": "null"}, {"type": "object"}
    ]});
    let doc = serde_json::json!({
        "openapi": "3.1.0",
        "info": {"title": "Ledger", "version": "1"},
        "servers": [{"url": "https://ledger.invalid"}],
        "paths": {"/entries": {"post": {
            "operationId": "postEntries",
            "tags": ["ledger"],
            "requestBody": {"required": true, "content": {"application/json": {"schema": {
                "type": "object",
                "required": ["entries"],
                "properties": {"entries": {"type": "array", "items": {"oneOf": [
                    {"type": "object", "required": ["label", "amount"], "properties": {
                        "label": {"type": "string"},
                        "amount": {"oneOf": [scalars.clone(), {"type": "array", "items": scalars}]}
                    }},
                    {"type": "object", "required": ["label"], "properties": {
                        "label": {"type": "string"}
                    }}
                ]}}}
            }}}},
            "responses": {"200": {"description": "OK", "content": {"application/json": {
                "schema": {"type": "object", "properties": {"status": {"type": "string"}}}
            }}}}
        }}}
    });
    fs::write(path, serde_json::to_string_pretty(&doc).unwrap()).unwrap();
}

fn copy_tree(from: &Path, to: &Path) {
    fs::create_dir_all(to).unwrap();
    for entry in fs::read_dir(from).unwrap() {
        let entry = entry.unwrap();
        let target = to.join(entry.file_name());
        if entry.file_type().unwrap().is_dir() {
            copy_tree(&entry.path(), &target);
        } else {
            fs::copy(entry.path(), target).unwrap();
        }
    }
}

/// A copy of `crozier` whose client docstrings leave out every `line`.
fn reference_without(crozier: &Path, reference: &Path, line: &str) {
    copy_tree(crozier, reference);
    let client = reference.join(CLIENT);
    let text = fs::read_to_string(&client).unwrap();
    let kept: Vec<&str> = text
        .split_inclusive('\n')
        .filter(|l| l.trim() != line)
        .collect();
    assert_ne!(kept.concat(), text, "{line} is in the generated docstring");
    fs::write(client, kept.concat()).unwrap();
}

#[test]
fn only_the_null_union_field_line_is_excused_in_a_real_sdk() {
    for mode in ["python-enums", "literals"] {
        let work = tempfile::tempdir().unwrap();
        let spec = work.path().join("openapi.json");
        document(&spec);
        let out = work.path().join("crozier");
        crozier_clean_env()
            .args(["--no-config", "generate", "python", "--spec"])
            .arg(&spec)
            .arg("--output")
            .arg(&out)
            .args([
                "--package-name",
                "fern",
                "--project-name",
                "default_package_name",
                "--enum-type",
                mode,
            ])
            .assert()
            .success();
        let reference_lacking = |line: &str, name: &str| {
            let reference = work.path().join(name);
            reference_without(&out, &reference, line);
            crozier::parity::compare_trees_with_document(
                &reference,
                &out,
                None,
                true,
                Some(crozier::openapi::load(&spec).unwrap()),
            )
            .expect("real SDK trees can be compared")
        };

        let excused = reference_lacking("amount=\"amount\",", "without-amount");
        assert!(excused.differences.is_empty(), "{mode}: {excused:?}");
        assert!(
            excused.departures.iter().any(|departure| {
                departure.file == CLIENT && departure.id == "required-null-union-field-example"
            }),
            "{mode}: the departure must be what absorbs the line: {excused:?}"
        );

        // The adjacent required field of the same model stays a mismatch.
        let unexplained = reference_lacking("label=\"label\",", "without-label");
        assert!(
            unexplained
                .differences
                .iter()
                .any(|(file, _)| file == CLIENT),
            "{mode}: {unexplained:?}"
        );
    }
}
