//! Name-collision refusal shapes the committed registry probes do not reach,
//! driven through the library the way `crozier generate` drives it. Each case is
//! a small document carrying one shape a `names`-family detector classifies;
//! every `names` class is `refuse`, so the document is refused in both modes
//! with a line naming the class id and the offending element. The controls next
//! to them are the shapes pinned Fern accepts, which must still generate.

use std::path::{Path, PathBuf};

use crozier::{render_files, GenerateArgs};

const HEAD: &str = "openapi: 3.0.3\ninfo: {title: t, version: \"1\"}\n";

fn render(spec: &Path, fern_strict: bool) -> Result<usize, String> {
    render_files(GenerateArgs {
        spec: spec.to_path_buf(),
        output: PathBuf::from("unused"),
        package_name: Some("acme".to_string()),
        project_name: Some("acme".to_string()),
        client_class_name: None,
        audiences: Vec::new(),
        audience_strict: false,
        fern_strict,
        extra_fields: crozier::settings::ExtraFields::Allow,
        enum_type: crozier::settings::EnumType::PythonEnums,
        default_max_retries: crozier::settings::DEFAULT_MAX_RETRIES,
        layout: crozier::settings::Layout::Packaged,
    })
    .map(|files| files.len())
    .map_err(|error| error.to_string())
}

fn write(dir: &Path, body: &str) -> PathBuf {
    let spec = dir.join("api.yml");
    std::fs::write(&spec, format!("{HEAD}{body}")).expect("write the document");
    spec
}

/// The document is refused in default and strict mode under `class`, naming
/// `element`; the strict line also names `fern-strict` as its cause.
fn assert_refused(body: &str, class: &str, element: &str) {
    let dir = tempfile::tempdir().expect("temp dir");
    let spec = write(dir.path(), body);
    for strict in [false, true] {
        let error = render(&spec, strict).expect_err(&format!(
            "{class}: crozier generated from a document it must refuse (strict: {strict})"
        ));
        assert!(
            error.contains(&format!("{class}: ")) && error.contains(element),
            "expected a {class} refusal naming {element:?} (strict: {strict}), got: {error}"
        );
        assert_eq!(error.contains("fern-strict"), strict, "{error}");
        assert_eq!(error.lines().count(), 1, "one refusal line: {error}");
    }
}

#[test]
fn parameters_in_different_locations_with_one_request_name_are_refused() {
    assert_refused(
        r#"paths:
  /items:
    get:
      operationId: listItems
      parameters:
        - {name: id, in: query, schema: {type: string}}
        - {name: id, in: header, schema: {type: string}}
      responses: {'200': {description: ok}}
"#,
        "request-property-camelcase-collision",
        r#"GET /items parameters "id" and "id" in different locations"#,
    );
    assert_refused(
        r#"paths:
  /items:
    get:
      operationId: listItems
      parameters:
        - {name: limit, in: query, x-fern-parameter-name: size, schema: {type: string}}
        - {name: size, in: header, schema: {type: string}}
      responses: {'200': {description: ok}}
"#,
        "request-property-name-collision",
        r#"GET /items parameters "size" and "limit" in different locations declare the same request name "size""#,
    );
}

#[test]
fn a_content_parameter_schema_is_checked_for_enum_names() {
    assert_refused(
        r#"paths:
  /items:
    get:
      operationId: listItems
      parameters:
        - name: filter
          in: query
          content: {application/json: {schema: {type: string, enum: ["!!!"]}}}
      responses: {'200': {description: ok}}
"#,
        "enum-name-unsuitable",
        r#"GET /items parameter filter enum value "!!!""#,
    );
}

const INHERITED_BODY: &str = r#"paths:
  /items:
    parameters: []
    post:
      operationId: createItem
      requestBody:
        content:
          application/json:
            schema:
              allOf:
                - $ref: '#/components/schemas/Base'
                - properties: {b: {type: string, x-fern-parameter-name: a}}
      responses: {'200': {description: ok}}
components:
  schemas:
    Base:
      type: object
      nullable: "yes"
      properties: {a: {type: string}}
"#;

#[test]
fn an_inherited_body_collision_is_refused_when_another_field_is_malformed() {
    // `nullable: "yes"` stops the typed load; the collision is still classified
    // from the source document rather than reported as a parse failure.
    assert_refused(
        INHERITED_BODY,
        "request-property-name-collision",
        r#"POST /items body property "a" collides with another request property"#,
    );
}

#[test]
fn a_malformed_document_without_a_collision_keeps_its_own_error() {
    let dir = tempfile::tempdir().expect("temp dir");
    let spec = write(
        dir.path(),
        &INHERITED_BODY.replace(", x-fern-parameter-name: a", ""),
    );
    for strict in [false, true] {
        let error = render(&spec, strict).expect_err("a malformed document fails");
        assert!(
            !error.contains("collision") && error.contains("nullable"),
            "expected the malformed field's own error (strict: {strict}), got: {error}"
        );
    }
}

#[test]
fn a_recursive_inline_property_reference_is_refused() {
    assert_refused(
        r#"paths: {}
components:
  schemas:
    Node:
      type: object
      properties:
        child: {$ref: '#/components/schemas/Node/properties/child'}
"#,
        "generated-file-name-too-long",
        "#/components/schemas/Node has a recursive inline property reference",
    );
}

#[test]
fn references_that_form_no_letter_led_type_name_are_refused() {
    assert_refused(
        r#"paths:
  /items:
    get:
      operationId: listItems
      responses:
        '200':
          description: ok
          content: {application/json: {schema: {$ref: '#/definitions/Thing'}}}
definitions:
  Thing: {type: object, properties: {a: {type: string}}}
"#,
        "type-name-not-letter-led",
        r##"GET /items reference "#/definitions/Thing" forms an empty object type name"##,
    );
    assert_refused(
        r#"paths: {}
components:
  schemas:
    Ext: {$ref: 'missing.yml#/Foo'}
"#,
        "type-name-not-letter-led",
        "#/components/schemas/Ext cannot form a letter-led type name",
    );
}

#[test]
fn component_schemas_differing_only_in_initial_case_are_refused() {
    assert_refused(
        r#"paths: {}
components:
  schemas:
    user: {type: object, properties: {a: {type: string}}}
    User: {type: object, properties: {b: {type: string}}}
"#,
        "type-name-collision",
        r#"component schemas "user" and "User" both declare type User"#,
    );
}

const PARAMETER_ENUM: &str = r#"paths:
  /items:
    get:
      tags: [items]
      operationId: listItems
      parameters:
        - {name: status, in: query, schema: {type: string, enum: [open, closed]}}
      responses: {'200': {description: ok}}
components:
  schemas:
    ListItemsRequestStatus: {type: object, properties: {a: {type: string}}}
"#;

#[test]
fn a_query_parameter_enum_named_like_a_root_schema_is_refused() {
    assert_refused(
        PARAMETER_ENUM,
        "type-name-collision",
        "enum ListItemsRequestStatus in namespace items collides with a schema declaration",
    );
}

#[test]
fn a_header_parameter_enum_named_like_a_root_schema_still_generates() {
    // Pinned Fern accepts the header form (see the type-name-collision
    // evidence), so neither mode refuses it.
    let dir = tempfile::tempdir().expect("temp dir");
    let spec = write(
        dir.path(),
        &PARAMETER_ENUM.replace("in: query", "in: header"),
    );
    for strict in [false, true] {
        let files = render(&spec, strict).unwrap_or_else(|error| {
            panic!("a header enum named like a root schema is refused (strict: {strict}): {error}")
        });
        assert!(files > 0);
    }
}

/// hellopatient's shape: a body property named like the operation's path
/// parameter, which `RENAME` (blank by default) can rename clear of it.
const PATH_PARAMETER_BODY: &str = r#"paths:
  /practice/{practice_id}/service-metadata:
    post:
      operationId: createServiceMetadata
      parameters:
        - {name: practice_id, in: path, required: true, schema: {type: string}}
      requestBody:
        content:
          application/json:
            schema: {$ref: '#/components/schemas/PracticeServiceMetadataCreate'}
      responses: {'200': {description: ok}}
  /practice/{practice_id}/intents:
    post:
      operationId: createIntent
      parameters:
        - {name: practice_id, in: path, required: true, schema: {type: string}}
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties: {practice_id: {type: string RENAME}}
      responses: {'200': {description: ok}}
components:
  schemas:
    PracticeServiceMetadataCreate:
      type: object
      properties: {practice_id: {type: string RENAME}, service_name: {type: string}}
"#;

#[test]
fn a_body_property_named_like_a_path_parameter_is_refused() {
    assert_refused(
        &PATH_PARAMETER_BODY.replace(" RENAME", ""),
        "request-property-name-collision",
        r#"POST /practice/{practice_id}/service-metadata body property "practice_id" collides with another request property"#,
    );
}

#[test]
fn a_body_property_renamed_clear_of_a_path_parameter_generates() {
    // Either spelling of the property-name extension, on a referenced and an
    // inline body alike, gives the property a declared name Fern accepts.
    for rename in [
        ", x-fern-property-name: body_practice_id",
        ", x-crozier-property-name: body_practice_id",
        ", x-crozier-property-name: body_practice_id, x-fern-property-name: other_practice_id",
    ] {
        let dir = tempfile::tempdir().expect("temp dir");
        let spec = write(dir.path(), &PATH_PARAMETER_BODY.replace(" RENAME", rename));
        for strict in [false, true] {
            let files = render(&spec, strict).unwrap_or_else(|error| {
                panic!("a renamed body property is refused ({rename}, strict: {strict}): {error}")
            });
            assert!(files > 0);
        }
    }
}

#[test]
fn a_blank_property_name_leaves_the_collision_refused() {
    assert_refused(
        &PATH_PARAMETER_BODY.replace(" RENAME", ", x-fern-property-name: ' '"),
        "request-property-name-collision",
        r#"body property "practice_id" collides with another request property"#,
    );
}
