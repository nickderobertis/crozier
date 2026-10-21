//! A document that writes the integer `1` or `0` where OpenAPI holds a boolean,
//! through the binary: it generates the SDK the same document with `true` /
//! `false` there generates, in YAML and JSON, with and without `--fern-strict`
//! (atacan/MistralAPI's `APIError.code` writes `nullable: 1`, and Fern CLI
//! 5.163.1 generates from it). Any other non-boolean stays refused with the
//! reader's own message.

use std::collections::BTreeMap;
use std::path::{Path, PathBuf};

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
        - name: trace
          in: query
          x-crozier-ignore: true
          schema: { type: string }
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
  /items/{id}/archive:
    post:
      operationId: archiveItem
      tags: [items]
      x-fern-ignore: true
      parameters:
        - name: id
          in: path
          required: true
          schema: { type: string }
      responses:
        '204':
          description: Archived
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
      x-is-beta: true
      properties:
        id:
          type: string
          readOnly: true
          xml: { attribute: true }
        name:
          type: string
        secret:
          type: string
          writeOnly: true
        internal:
          type: string
          x-fern-ignore: true
        legacy:
          type: string
          deprecated: true
        labels:
          type: array
          uniqueItems: true
          xml: { wrapped: true }
          items: { type: string }
        score:
          type: number
          minimum: 0
          maximum: 10
          exclusiveMinimum: true
          exclusiveMaximum: true
        shape: { $ref: '#/components/schemas/Shape' }
    Shape:
      oneOf:
        - $ref: '#/components/schemas/Circle'
        - $ref: '#/components/schemas/Square'
      discriminator: { propertyName: kind }
      x-fern-discriminated: true
    Circle:
      type: object
      required: [kind]
      properties:
        kind: { type: string }
        radius: { type: number }
    Square:
      type: object
      required: [kind]
      properties:
        kind: { type: string }
        side: { type: number }
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
    (
        "operation x-fern-ignore",
        "/paths/~1items~1{id}~1archive/post/x-fern-ignore",
    ),
    (
        "parameter x-crozier-ignore",
        "/paths/~1items~1{id}/get/parameters/2/x-crozier-ignore",
    ),
    (
        "property x-fern-ignore",
        "/components/schemas/Item/properties/internal/x-fern-ignore",
    ),
    ("x-is-beta", "/components/schemas/Item/x-is-beta"),
    (
        "x-fern-discriminated",
        "/components/schemas/Shape/x-fern-discriminated",
    ),
    (
        "xml attribute",
        "/components/schemas/Item/properties/id/xml/attribute",
    ),
    (
        "xml wrapped",
        "/components/schemas/Item/properties/labels/xml/wrapped",
    ),
];

/// What the YAML reader refuses a non-boolean scalar in a boolean place with.
const YAML_REFUSAL: &str = "invalid boolean (strict mode expects true/false)";

/// The sites whose value the document model reads, so a non-boolean there is
/// refused. `None` is the reader's plain-boolean refusal ([`YAML_REFUSAL`] in
/// YAML, serde's `invalid type` in JSON); `additionalProperties` may also hold
/// a schema, and is refused as neither.
const READ_SITES: &[(&str, Option<&str>)] = &[
    ("nullable", None),
    ("parameter required", None),
    ("request body required", None),
    ("readOnly", None),
    ("uniqueItems", None),
    ("explode", None),
    ("parameter x-crozier-ignore", None),
    ("x-fern-discriminated", None),
    (
        "additionalProperties",
        Some("data did not match any variant of untagged enum AdditionalProperties"),
    ),
];

#[derive(Clone, Copy, Debug)]
enum Format {
    Yaml,
    Json,
}

impl Format {
    fn of(path: &Path) -> Self {
        match path.extension().and_then(|extension| extension.to_str()) {
            Some("json") => Self::Json,
            _ => Self::Yaml,
        }
    }
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

fn write(dir: &Path, stem: &str, document: &Value, format: Format) -> PathBuf {
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
/// and its bytes, else the failure's stderr with `spec`'s directory elided.
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
    if !run.status.success() {
        let directory = spec.parent().expect("spec has a directory");
        return Err(
            String::from_utf8_lossy(&run.stderr).replace(&directory.display().to_string(), "<dir>")
        );
    }
    Ok(super::walk_files(out.path())
        .into_iter()
        .map(|file| {
            let bytes = std::fs::read(out.path().join(&file)).expect("read generated file");
            (file, bytes)
        })
        .collect())
}

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
fn a_yaml_boolean_keeps_the_spellings_it_read_before() {
    // The strict YAML boolean read accepts any letter case and a quoted
    // spelling, so a document written that way still generates as before.
    let dir = tempfile::tempdir().expect("tempdir");
    let names: Vec<&str> = SITES.iter().map(|(name, _)| *name).collect();
    let expected = generate(
        &write(
            dir.path(),
            "boolean",
            &document(&names, &json!(true)),
            Format::Yaml,
        ),
        false,
    )
    .expect("`true` generates");
    for spelling in ["True", "TRUE", "'true'"] {
        let spec = dir.path().join("spelled.yaml");
        let text = std::fs::read_to_string(dir.path().join("boolean.yaml")).expect("read");
        std::fs::write(&spec, text.replace(": true\n", &format!(": {spelling}\n"))).expect("write");
        assert!(
            std::fs::read_to_string(&spec)
                .unwrap()
                .contains(&format!("nullable: {spelling}\n")),
            "{spelling}"
        );
        let generated =
            generate(&spec, false).unwrap_or_else(|error| panic!("{spelling}: {error}"));
        assert!(
            generated == expected,
            "{spelling} generates other bytes than `true`"
        );
    }
}

#[test]
fn any_other_value_in_a_boolean_place_is_refused() {
    for (name, message) in READ_SITES {
        for (value, unexpected, yaml) in [
            (json!(2), "integer `2`", YAML_REFUSAL),
            (json!("yes"), "string \"yes\"", YAML_REFUSAL),
            (json!(1.0), "floating point `1.0`", YAML_REFUSAL),
            (json!(-1), "integer `-1`", YAML_REFUSAL),
            (json!([1]), "sequence", "expected string scalar"),
        ] {
            for (format, strict) in cases() {
                let dir = tempfile::tempdir().expect("tempdir");
                let spec = write(dir.path(), "boolean", &document(&[name], &value), format);
                let error = generate(&spec, strict).err().unwrap_or_else(|| {
                    panic!("{name} {format:?} strict={strict}: {value} generated")
                });
                let message = match (message, format) {
                    (Some(message), _) => (*message).to_owned(),
                    (None, Format::Yaml) => yaml.to_owned(),
                    (None, Format::Json) => {
                        format!("invalid type: {unexpected}, expected a boolean")
                    }
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

/// Keys that hold a name-keyed map, whose members' keys are names and never
/// keywords.
const NAMED_MAPS: &[&str] = &[
    "properties",
    "patternProperties",
    "$defs",
    "definitions",
    "schemas",
    "parameters",
    "responses",
    "requestBodies",
    "headers",
    "securitySchemes",
    "paths",
    "callbacks",
    "links",
    "variables",
    "mapping",
];

/// Keys whose value is data the document carries, not keywords.
const DATA: &[&str] = &[
    "example",
    "examples",
    "x-fern-examples",
    "x-crozier-examples",
    "default",
    "x-fern-default",
    "x-crozier-default",
    "enum",
    "const",
];

/// The keywords [`rewrite_booleans`] substitutes; `attribute` and `wrapped`
/// only inside an XML Object.
const BOOLEAN_KEYWORDS: &[&str] = &[
    "nullable",
    "required",
    "readOnly",
    "writeOnly",
    "deprecated",
    "uniqueItems",
    "explode",
    "allowEmptyValue",
    "allowReserved",
    "exclusiveMinimum",
    "exclusiveMaximum",
    "additionalProperties",
    "x-fern-ignore",
    "x-crozier-ignore",
    "x-fern-discriminated",
    "x-crozier-discriminated",
    "x-is-beta",
];

/// Rewrite every boolean keyword's `true`/`false` under `value` to `1`/`0`,
/// returning how many it rewrote.
fn rewrite_booleans(value: &mut Value, parent: Option<&str>) -> usize {
    let mut rewritten = 0;
    match value {
        Value::Object(members) => {
            let named = parent.is_some_and(|key| NAMED_MAPS.contains(&key));
            for (key, member) in members.iter_mut() {
                let keyword = BOOLEAN_KEYWORDS.contains(&key.as_str())
                    || (parent == Some("xml") && ["attribute", "wrapped"].contains(&key.as_str()));
                if let (false, true, Value::Bool(flag)) = (named, keyword, &*member) {
                    *member = json!(u8::from(*flag));
                    rewritten += 1;
                } else if !DATA.contains(&key.as_str()) || named {
                    rewritten += rewrite_booleans(member, (!named).then_some(key.as_str()));
                }
            }
        }
        Value::Array(members) => {
            for member in members {
                rewritten += rewrite_booleans(member, None);
            }
        }
        _ => {}
    }
    rewritten
}

/// Every committed Fern-refusal probe and control document (each class's
/// `probe.*` and `*-probe.*` / `*-control.*`), which reach the refusal checks
/// that read the source tree before the typed parse.
fn refusal_documents() -> Vec<PathBuf> {
    let root = super::repo_root().join("docs/fern-refusals");
    let mut documents = Vec::new();
    for class in std::fs::read_dir(&root).expect("read docs/fern-refusals") {
        let class = class.expect("class entry").path();
        if !class.is_dir() {
            continue;
        }
        for entry in std::fs::read_dir(&class).expect("read class directory") {
            let path = entry.expect("class file").path();
            let stem = path
                .file_stem()
                .and_then(|stem| stem.to_str())
                .unwrap_or("");
            let document = matches!(
                path.extension().and_then(|extension| extension.to_str()),
                Some("yml" | "yaml" | "json")
            );
            if document
                && (stem == "probe" || stem.ends_with("-probe") || stem.ends_with("-control"))
            {
                documents.push(path);
            }
        }
    }
    documents.sort();
    documents
}

#[test]
fn every_refusal_probe_reaches_the_same_strict_verdict_with_one_and_zero() {
    let documents = refusal_documents();
    let outcomes = std::sync::Mutex::new((0, Vec::new()));
    std::thread::scope(|scope| {
        for chunk in documents.chunks(documents.len().div_ceil(8).max(1)) {
            let outcomes = &outcomes;
            scope.spawn(move || {
                for path in chunk {
                    let text = std::fs::read_to_string(path).expect("read probe");
                    let format = Format::of(path);
                    let parsed: Value = match format {
                        Format::Json => serde_json::from_str(&text).expect("probe is JSON"),
                        Format::Yaml => serde_saphyr::from_str(&text).expect("probe is YAML"),
                    };
                    let mut numeric = parsed.clone();
                    if rewrite_booleans(&mut numeric, None) == 0 {
                        continue;
                    }
                    let dir = tempfile::tempdir().expect("tempdir");
                    // Both documents pass through the same writer, so they
                    // differ in their booleans alone.
                    let expected = generate(&write(dir.path(), "probe", &parsed, format), true);
                    let generated = generate(&write(dir.path(), "probe", &numeric, format), true);
                    let mut outcomes = outcomes.lock().expect("outcomes lock");
                    outcomes.0 += 1;
                    if generated != expected {
                        let verdict = |outcome: &Result<_, String>| match outcome {
                            Ok(_) => "generated".to_owned(),
                            Err(error) => error.clone(),
                        };
                        outcomes.1.push(format!(
                            "{}: `true`/`false` {} but `1`/`0` {}",
                            path.display(),
                            verdict(&expected),
                            verdict(&generated)
                        ));
                    }
                }
            });
        }
    });
    let (measured, mismatches) = outcomes.into_inner().expect("outcomes lock");
    assert!(
        measured >= 100,
        "only {measured} probes carry a boolean keyword"
    );
    assert!(mismatches.is_empty(), "{}", mismatches.join("\n"));
}
