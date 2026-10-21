//! A document that writes the integer `1` or `0` where OpenAPI holds a boolean,
//! through the binary: it generates the SDK the same document with `true` /
//! `false` there generates, in YAML and JSON, with and without `--fern-strict`
//! (atacan/MistralAPI's `APIError.code` writes `nullable: 1`, and Fern CLI
//! 5.163.1 generates from it). Any other non-boolean stays refused with the
//! reader's own message.

use std::collections::BTreeMap;
use std::path::Path;

use serde_json::{json, Value};

/// A document holding every boolean keyword this suite substitutes, each at
/// `true`; [`SITES`] points at them.
const DOCUMENT: &str = r#"
openapi: 3.0.3
info:
  title: Flags
  version: '1'
paths:
  /items/{id}:
    get:
      operationId: getItem
      tags: [items]
      parameters:
        - name: id
          in: path
          required: true
          schema: { type: string }
        - name: tags
          in: query
          required: true
          explode: true
          allowEmptyValue: true
          allowReserved: true
          schema:
            type: array
            items: { type: string }
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema: { $ref: '#/components/schemas/Item' }
        '400':
          description: Bad request
          content:
            application/json:
              schema: { $ref: '#/components/schemas/APIError' }
  /items:
    post:
      operationId: createItem
      tags: [items]
      deprecated: true
      requestBody:
        required: true
        content:
          application/json:
            schema: { $ref: '#/components/schemas/Item' }
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema: { $ref: '#/components/schemas/Item' }
components:
  schemas:
    APIError:
      properties:
        code:
          nullable: true
          title: Code
          type: string
        message:
          type: string
      required: [message]
    Item:
      type: object
      required: [id, name]
      additionalProperties: true
      properties:
        id:
          type: string
          readOnly: true
        name:
          type: string
        secret:
          type: string
          writeOnly: true
        legacy:
          type: string
          deprecated: true
        labels:
          type: array
          uniqueItems: true
          items: { type: string }
        score:
          type: number
          minimum: 0
          maximum: 10
          exclusiveMinimum: true
          exclusiveMaximum: true
"#;

/// Every boolean keyword [`DOCUMENT`] writes: its name and JSON pointer.
const SITES: &[(&str, &str)] = &[
    (
        "nullable",
        "/components/schemas/APIError/properties/code/nullable",
    ),
    (
        "parameter required",
        "/paths/~1items~1{id}/get/parameters/1/required",
    ),
    (
        "request body required",
        "/paths/~1items/post/requestBody/required",
    ),
    ("operation deprecated", "/paths/~1items/post/deprecated"),
    (
        "schema deprecated",
        "/components/schemas/Item/properties/legacy/deprecated",
    ),
    (
        "readOnly",
        "/components/schemas/Item/properties/id/readOnly",
    ),
    (
        "writeOnly",
        "/components/schemas/Item/properties/secret/writeOnly",
    ),
    (
        "uniqueItems",
        "/components/schemas/Item/properties/labels/uniqueItems",
    ),
    (
        "exclusiveMinimum",
        "/components/schemas/Item/properties/score/exclusiveMinimum",
    ),
    (
        "exclusiveMaximum",
        "/components/schemas/Item/properties/score/exclusiveMaximum",
    ),
    (
        "allowEmptyValue",
        "/paths/~1items~1{id}/get/parameters/1/allowEmptyValue",
    ),
    ("explode", "/paths/~1items~1{id}/get/parameters/1/explode"),
    (
        "allowReserved",
        "/paths/~1items~1{id}/get/parameters/1/allowReserved",
    ),
    (
        "additionalProperties",
        "/components/schemas/Item/additionalProperties",
    ),
];

/// The sites whose value the document model reads, so a non-boolean there is
/// refused; the parser's message for it in YAML and JSON (`{}` is the value's
/// serde description, as `integer \`2\``).
const READ_SITES: &[(&str, &str, &str)] = &[
    (
        "nullable",
        "invalid boolean (strict mode expects true/false)",
        "invalid type: {}, expected a boolean",
    ),
    (
        "parameter required",
        "invalid boolean (strict mode expects true/false)",
        "invalid type: {}, expected a boolean",
    ),
    (
        "request body required",
        "invalid boolean (strict mode expects true/false)",
        "invalid type: {}, expected a boolean",
    ),
    (
        "readOnly",
        "invalid boolean (strict mode expects true/false)",
        "invalid type: {}, expected a boolean",
    ),
    (
        "uniqueItems",
        "invalid boolean (strict mode expects true/false)",
        "invalid type: {}, expected a boolean",
    ),
    (
        "explode",
        "invalid boolean (strict mode expects true/false)",
        "invalid type: {}, expected a boolean",
    ),
    (
        "additionalProperties",
        "data did not match any variant of untagged enum AdditionalProperties",
        "data did not match any variant of untagged enum AdditionalProperties",
    ),
];

#[derive(Clone, Copy, Debug)]
enum Format {
    Yaml,
    Json,
}

/// [`DOCUMENT`] with every site in `sites` set to `value`.
fn document(sites: &[&str], value: &Value) -> Value {
    let mut document: Value = serde_saphyr::from_str(DOCUMENT).expect("DOCUMENT is YAML");
    for name in sites {
        let pointer = SITES
            .iter()
            .find(|(site, _)| site == name)
            .unwrap_or_else(|| panic!("no site {name}"))
            .1;
        *document
            .pointer_mut(pointer)
            .unwrap_or_else(|| panic!("DOCUMENT holds no {pointer}")) = value.clone();
    }
    document
}

/// Write `document` as `format` into `dir` under `stem`, returning its path.
fn write(dir: &Path, stem: &str, document: &Value, format: Format) -> std::path::PathBuf {
    let (extension, text) = match format {
        Format::Yaml => (
            "yaml",
            serde_saphyr::to_string(document).expect("serialize YAML"),
        ),
        Format::Json => (
            "json",
            serde_json::to_string_pretty(document).expect("serialize JSON"),
        ),
    };
    let path = dir.join(format!("{stem}.{extension}"));
    std::fs::write(&path, text).expect("write document");
    path
}

/// Run `crozier generate python` over `spec`; on success, every generated file
/// and its bytes, else the failure's stderr.
fn generate(spec: &Path, strict: bool) -> Result<BTreeMap<String, Vec<u8>>, String> {
    let out = tempfile::tempdir().expect("output tempdir");
    let mut command = super::crozier_clean_env();
    command
        .args(["generate", "python", "--spec"])
        .arg(spec)
        .arg("--output")
        .arg(out.path());
    if strict {
        command.arg("--fern-strict");
    }
    let run = command.output().expect("run crozier generate");
    let stderr = String::from_utf8_lossy(&run.stderr).into_owned();
    if !run.status.success() {
        return Err(stderr);
    }
    Ok(super::walk_files(out.path())
        .into_iter()
        .map(|file| {
            let bytes = std::fs::read(out.path().join(&file)).expect("read generated file");
            (file, bytes)
        })
        .collect())
}

/// Every case of formats and modes this suite runs.
fn cases() -> impl Iterator<Item = (Format, bool)> {
    [Format::Yaml, Format::Json]
        .into_iter()
        .flat_map(|format| [false, true].map(|strict| (format, strict)))
}

#[test]
fn one_and_zero_generate_what_true_and_false_generate() {
    let names: Vec<&str> = SITES.iter().map(|(name, _)| *name).collect();
    for (format, strict) in cases() {
        let mut trees = Vec::new();
        for (flag, integer) in [(true, 1), (false, 0)] {
            let dir = tempfile::tempdir().expect("tempdir");
            let boolean = write(
                dir.path(),
                "boolean",
                &document(&names, &json!(flag)),
                format,
            );
            let numeric = write(
                dir.path(),
                "numeric",
                &document(&names, &json!(integer)),
                format,
            );
            let text = std::fs::read_to_string(&numeric).expect("read document");
            for (name, pointer) in SITES {
                let key = pointer.rsplit('/').next().expect("pointer has a key");
                let line = match format {
                    Format::Yaml => format!("{key}: {integer}\n"),
                    Format::Json => format!("\"{key}\": {integer}"),
                };
                assert!(
                    text.contains(&line),
                    "{name}: {format:?} writes no `{line}`:\n{text}"
                );
            }
            let expected = generate(&boolean, strict).unwrap_or_else(|error| {
                panic!("{format:?} strict={strict} `{flag}` refused: {error}")
            });
            let generated = generate(&numeric, strict).unwrap_or_else(|error| {
                panic!("{format:?} strict={strict} `{integer}` refused: {error}")
            });
            assert_eq!(
                generated.keys().collect::<Vec<_>>(),
                expected.keys().collect::<Vec<_>>(),
                "{format:?} strict={strict}: `{integer}` generates another file set than `{flag}`"
            );
            for (file, bytes) in &expected {
                assert!(
                    generated[file] == *bytes,
                    "{format:?} strict={strict}: {file} differs between `{integer}` and `{flag}`"
                );
            }
            trees.push(expected);
        }
        // The flags reach the output, so the comparison above is not vacuous.
        assert_ne!(trees[0], trees[1], "{format:?} strict={strict}");
    }
}

#[test]
fn each_site_reads_one_and_zero_alone() {
    // A site's integer is read where it stands, not only beside the others.
    // One thread a site: each case runs `ruff format` twice.
    std::thread::scope(|scope| {
        for (name, _) in SITES {
            scope.spawn(move || each_case_reads_one_and_zero(name));
        }
    });
}

/// `name`'s site alone at `1` / `0` generates what it does at `true` / `false`,
/// in every format and mode.
fn each_case_reads_one_and_zero(name: &str) {
    for (format, strict) in cases() {
        for (flag, integer) in [(true, 1), (false, 0)] {
            let dir = tempfile::tempdir().expect("tempdir");
            let boolean = write(
                dir.path(),
                "boolean",
                &document(&[name], &json!(flag)),
                format,
            );
            let numeric = write(
                dir.path(),
                "numeric",
                &document(&[name], &json!(integer)),
                format,
            );
            let expected = generate(&boolean, strict)
                .unwrap_or_else(|error| panic!("{name} {format:?} `{flag}`: {error}"));
            let generated = generate(&numeric, strict)
                .unwrap_or_else(|error| panic!("{name} {format:?} `{integer}`: {error}"));
            assert!(
                generated == expected,
                "{name} {format:?} strict={strict}: `{integer}` generates other bytes than `{flag}`"
            );
        }
    }
}

#[test]
fn any_other_value_in_a_boolean_place_is_refused() {
    for (name, yaml_message, json_message) in READ_SITES {
        for (value, unexpected) in [
            (json!(2), "integer `2`"),
            (json!("yes"), "string \"yes\""),
            (json!(1.0), "floating point `1.0`"),
            (json!(-1), "integer `-1`"),
        ] {
            for (format, strict) in cases() {
                let dir = tempfile::tempdir().expect("tempdir");
                let spec = write(dir.path(), "boolean", &document(&[name], &value), format);
                let error = generate(&spec, strict).err().unwrap_or_else(|| {
                    panic!("{name} {format:?} strict={strict}: {value} generated")
                });
                let message = match format {
                    Format::Yaml => (*yaml_message).to_owned(),
                    Format::Json => json_message.replace("{}", unexpected),
                };
                assert!(
                    error.starts_with("crozier: could not parse OpenAPI document")
                        && error.contains(&message),
                    "{name} {format:?} strict={strict} {value}: expected `{message}`:\n{error}"
                );
            }
        }
    }
}
