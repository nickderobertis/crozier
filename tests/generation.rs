//! In-process integration tests over the generation pipeline. Unlike the binary
//! e2e (`tests/e2e.rs`), these call the library directly so they are measured by
//! coverage; they exercise the type-mapping and emit branches a single fixture
//! cannot, while still driving real parsing over real temp files.

use std::collections::HashMap;
use std::path::{Path, PathBuf};

use crozier::{generate, render_files, GenerateArgs};

/// Write `spec` to a temp `.yml` and render it in-process, returning
/// path-string -> contents for every generated file.
fn render(spec: &str) -> HashMap<String, String> {
    let dir = tempfile::tempdir().expect("tempdir");
    let path = dir.path().join("api.yml");
    std::fs::write(&path, spec).unwrap();
    let files = render_files(GenerateArgs {
        spec: path,
        output: PathBuf::from("unused"),
        package_name: Some("acme".to_string()),
        project_name: Some("acme".to_string()),
        client_class_name: None,
        audiences: Vec::new(),
        audience_strict: false,
        extra_fields: crozier::settings::ExtraFields::Allow,
    })
    .expect("render succeeds");
    files
        .into_iter()
        .map(|f| (f.path.to_string_lossy().into_owned(), f.contents))
        .collect()
}

fn render_package(spec: &str, package: &str) -> HashMap<String, String> {
    let dir = tempfile::tempdir().expect("tempdir");
    let path = dir.path().join("api.yml");
    std::fs::write(&path, spec).unwrap();
    render_files(GenerateArgs {
        spec: path,
        output: PathBuf::from("unused"),
        package_name: Some(package.to_string()),
        project_name: Some(package.to_string()),
        client_class_name: None,
        audiences: Vec::new(),
        audience_strict: false,
        extra_fields: crozier::settings::ExtraFields::Allow,
    })
    .expect("render succeeds")
    .into_iter()
    .map(|f| (f.path.to_string_lossy().into_owned(), f.contents))
    .collect()
}

#[test]
fn openapi_31_marimo_shapes_drive_fern_520_generation_paths() {
    let files = render(
        r#"openapi: 3.1.0
info: { title: Marimo shapes, version: 1.0.0 }
paths:
  /@file/{filename_and_length}:
    get:
      parameters:
        - { in: path, name: filename_and_length, required: true, schema: { type: string } }
      responses:
        '200':
          description: file
          content: { application/octet-stream: { schema: { type: string } } }
  /chat:
    post:
      parameters:
        - { in: header, name: Marimo-Session-Id, required: true, schema: { type: string } }
      requestBody:
        content: { application/json: { schema: { $ref: '#/components/schemas/ChatRequest' } } }
  /empty:
    post:
      requestBody:
        content: { application/json: { schema: { $ref: '#/components/schemas/EmptyRequest' } } }
      responses: { '204': { description: cleared } }
  /save:
    post:
      parameters:
        - { in: header, name: Marimo-Session-Id, required: true, schema: { type: string } }
      requestBody:
        content: { application/json: { schema: { $ref: '#/components/schemas/SaveRequest' } } }
      responses:
        '200':
          description: saved
          content: { text/plain: { schema: { type: string } } }
  /upload:
    post:
      requestBody:
        content: { multipart/form-data: { schema: { $ref: '#/components/schemas/UploadRequest' } } }
      responses: { '204': { description: uploaded } }
  /tutorial:
    post:
      requestBody:
        content: { application/json: { schema: { $ref: '#/components/schemas/TutorialRequest' } } }
      responses:
        '200':
          description: tuple map
          content: { application/json: { schema: { $ref: '#/components/schemas/TupleMap' } } }
  /wild:
    post:
      parameters:
        - { in: header, name: X-Required, required: true, schema: { type: string } }
        - { in: header, name: X-Optional, schema: { type: string }, example: optional }
        - { in: query, name: requiredQuery, required: true, schema: { type: string } }
      requestBody:
        content: { '*/*': { schema: { type: string } } }
      responses:
        '200':
          description: text
          content: { text/html: { schema: { type: string } } }
  /binary-query:
    get:
      parameters:
        - { in: header, name: Download-Token, required: true, schema: { type: string } }
        - { in: query, name: ids, required: true, schema: { type: array, items: { type: string } } }
      responses:
        '200':
          description: bytes
          content: { application/octet-stream: { schema: { type: string } } }
  /known:
    get:
      responses:
        '200':
          description: known union
          content: { application/json: { schema: { $ref: '#/components/schemas/KnownUnion' } } }
components:
  schemas:
    EmptyRequest: { type: object, properties: {}, required: [] }
    Base64String: { type: string, contentEncoding: base64 }
    ChatRequest:
      type: object
      required: [values]
      properties: { values: { type: array } }
    SaveRequest:
      type: object
      required: [config, names]
      properties:
        config: { type: object }
        names: { type: array, items: { type: string } }
    UploadRequest:
      type: object
      required: [type, name]
      properties:
        type: { type: string, enum: [file, directory] }
        name: { type: string }
        file: { type: [string, 'null'], format: binary }
    KnownUnion:
      anyOf:
        - type: object
          required: [kind]
          properties: { kind: { const: first }, value: { type: string } }
        - type: object
          required: [kind]
          properties: { kind: { const: second }, count: { type: integer } }
      discriminator: { propertyName: kind }
    TutorialRequest:
      type: object
      required: [tutorialId]
      properties:
        tutorialId:
          anyOf:
            - { type: string, enum: [dataflow, intro] }
            - { type: string, enum: [markdown-format] }
    TupleMap:
      type: object
      properties:
        values:
          type: object
          additionalProperties:
            type: array
            items: false
            prefixItems: [{ type: string }, {}]
    MalformedProperty:
      type: object
      properties: { value: null }
"#,
    );

    let client = &files["src/acme/client.py"];
    assert!(
        client.contains("filename_and_length=\"filename_and_length\""),
        "{client}"
    );
    assert!(
        client.contains("marimo_session_id=\"marimoSessionId\""),
        "{client}"
    );
    assert!(client.contains("names=[\"names\", \"names\"]"), "{client}");
    assert!(
        client.contains("config={\"config\": {\"key\": \"value\"}}"),
        "{client}"
    );
    assert!(
        client.contains("TutorialRequestTutorialIdZero.DATAFLOW"),
        "{client}"
    );
    assert!(!client.contains("request: EmptyRequest"), "{client}");
    assert!(!files["src/acme/types/__init__.py"].contains("from .upload_request_type"));
    assert!(files["src/acme/types/__init__.py"].contains("Base64String"));
}

#[test]
fn referenced_examples_cover_multipart_aliases_and_digit_leading_fields() {
    let files = render(
        r##"
openapi: 3.0.0
info:
  title: Referenced examples
  version: 1.0.0
paths:
  /parents/{parent}/children/{child}:
    parameters:
      - { in: path, name: child, required: true, schema: { type: string } }
      - { in: path, name: parent, required: true, schema: { type: string } }
    get:
      operationId: children.get
      responses:
        '204': { description: found }
  /contexts:
    post:
      operationId: contexts.create
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ContextRequest'
          multipart/related:
            encoding:
              binaryData:
                contentType: application/octet-stream
            schema:
              $ref: '#/components/schemas/ContextMultipart'
      responses:
        '200':
          description: created
          content:
            application/json:
              schema:
                type: string
  /upload:
    post:
      operationId: uploads.create
      requestBody:
        required: true
        content:
          multipart/related:
            encoding:
              jsonData:
                contentType: application/json
              binaryData:
                contentType: application/octet-stream
            schema:
              $ref: '#/components/schemas/ContextMultipart'
      responses:
        '204':
          description: uploaded
  /wild:
    post:
      operationId: wild.send
      parameters:
        - in: query
          name: tags
          required: true
          schema:
            type: array
            items:
              type: string
        - in: header
          name: X-Trace
          required: true
          example: trace-1
          schema:
            type: string
      requestBody:
        required: true
        content:
          '*/*':
            schema:
              type: string
      responses:
        '204':
          description: sent
webhooks:
  context.changed:
    post:
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required: [id]
              properties:
                id:
                  type: string
                tags:
                  type: array
                  items:
                    type: string
      responses:
        '204':
          description: accepted
components:
  schemas:
    BearerContainer:
      type: string
    BaseContext:
      type: object
      properties:
        inherited:
          type: string
    ContextRequest:
      example:
        bearerSetup: [null, null]
        5gCauseValue: 0
      allOf:
        - $ref: '#/components/schemas/BaseContext'
        - type: object
          properties:
            bearerSetup:
              type: array
              items:
                $ref: '#/components/schemas/BearerContainer'
            5gCauseValue:
              type: integer
    ContextMultipart:
      type: object
      properties:
        jsonData:
          $ref: '#/components/schemas/ContextRequest'
        binaryData:
          type: string
          format: binary
"##,
    );

    let client = &files["src/acme/contexts/client.py"];
    assert!(client.contains("f_5g_cause_value=0"), "{client}");
    assert!(
        client.contains("bearer_setup=[\"bearerSetup\", \"bearerSetup\"]"),
        "{client}"
    );
    let reference = &files["reference.md"];
    assert!(reference.contains("f_value=0"), "{reference}");

    let root_stream = render(
        r#"
openapi: 3.1.0
info: { title: Root stream, version: 1.0.0 }
paths:
  /events:
    get:
      operationId: stream
      responses:
        '200':
          description: events
          content:
            text/event-stream:
              schema: { type: string }
"#,
    );
    assert!(root_stream["src/acme/client.py"].contains("def stream"));
}

fn python_files_below(dir: &std::path::Path, out: &mut Vec<PathBuf>) {
    for entry in std::fs::read_dir(dir).unwrap() {
        let path = entry.unwrap().path();
        if path.is_dir() {
            python_files_below(&path, out);
        } else if path.extension().and_then(std::ffi::OsStr::to_str) == Some("py") {
            out.push(path);
        }
    }
}

/// A spec touching every type-mapping branch the emitter supports.
const RICH_SPEC: &str = r##"
openapi: 3.0.1
info:
  title: Rich API
components:
  schemas:
    Widget:
      type: object
      required:
        - id
      description: A widget with many field shapes.
      properties:
        id:
          type: string
        described:
          type: string
          description: A described optional field.
        list:
          type: array
          items:
            type: string
        when:
          type: string
          format: date-time
        day:
          type: string
          format: date
        ident:
          type: string
          format: uuid
        amount:
          type: number
        flag:
          type: boolean
        count:
          type: integer
        attributes:
          type: object
          additionalProperties:
            type: string
        owner:
          $ref: "#/components/schemas/Owner"
    Owner:
      type: object
      properties:
        name:
          type: string
    Color:
      type: string
      enum:
        - red
        - green
    Shape:
      description: A documented union.
      oneOf:
        - $ref: "#/components/schemas/Owner"
        - type: string
    Alias:
      type: string
"##;

#[test]
fn renders_all_expected_type_files() {
    let files = render(RICH_SPEC);
    for module in ["widget", "owner", "color", "shape", "alias"] {
        assert!(
            files.contains_key(&format!("src/acme/types/{module}.py")),
            "expected a file for {module}; got {:?}",
            files.keys().collect::<Vec<_>>()
        );
    }
    assert!(files.contains_key("src/acme/version.py"));
    assert!(files.contains_key("src/acme/py.typed"));
}

#[test]
fn object_fields_render_with_fern_conventions() {
    let files = render(RICH_SPEC);
    let widget = &files["src/acme/types/widget.py"];

    // Required field: no Optional, no default.
    assert!(widget.contains("\n    id: str\n"), "required id: {widget}");
    // Optional primitive: Optional + None default.
    assert!(widget.contains("count: typing.Optional[int] = None"));
    // Described field: pydantic.Field(default=None) + docstring line.
    assert!(widget.contains("described: typing.Optional[str] = pydantic.Field(default=None)"));
    assert!(widget.contains("A described optional field."));
    // Reserved name is munged and aliased; Fern 5.20 carries the wire alias in
    // both its serialization metadata and pydantic's field metadata.
    assert!(widget.contains(
        "list_: typing_extensions.Annotated[\n        typing.Optional[typing.List[str]], FieldMetadata(alias=\"list\"), pydantic.Field(alias=\"list\")\n    ] = None"
    ), "aliased list field: {widget}");
    // Primitive mappings.
    assert!(widget.contains("when: typing.Optional[dt.datetime] = None"));
    assert!(widget.contains("day: typing.Optional[dt.date] = None"));
    // Fern's OpenAPI importer maps `format: uuid` to plain `str`.
    assert!(widget.contains("ident: typing.Optional[str] = None"));
    assert!(widget.contains("amount: typing.Optional[float] = None"));
    assert!(widget.contains("flag: typing.Optional[bool] = None"));
    assert!(widget.contains("attributes: typing.Optional[typing.Dict[str, str]] = None"));
    assert!(widget.contains("owner: typing.Optional[Owner] = None"));
}

#[test]
fn import_block_follows_ferns_two_group_order() {
    let files = render(RICH_SPEC);
    let widget = &files["src/acme/types/widget.py"];
    // Stdlib group first (datetime/typing/uuid), blank line, then third-party +
    // local froms with no blank line between them.
    let expected_head = "\
import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .owner import Owner
";
    assert!(
        widget.contains(expected_head),
        "import ordering mismatch:\n{widget}"
    );
}

#[test]
fn union_alias_and_scalar_alias_render() {
    let files = render(RICH_SPEC);
    let shape = &files["src/acme/types/shape.py"];
    assert!(shape.contains("Shape = typing.Union[Owner, str]"));
    assert!(!shape.contains("A documented union."), "{shape}");
    assert!(files["src/acme/types/alias.py"].contains("Alias = str"));
}

#[test]
fn string_enum_renders_as_enum_class() {
    // crozier renders an OpenAPI string enum as Fern's compatibility `StrEnum`
    // `enum_type: python_enums` shape), with SCREAMING_SNAKE members over the wire
    // values and a `visit` dispatch method — not an open `Literal` union.
    let files = render(RICH_SPEC);
    let color = &files["src/acme/types/color.py"];
    assert!(color.contains("from ..core import enum"), "{color}");
    assert!(color.contains("class Color(enum.StrEnum):"), "{color}");
    assert!(color.contains("    RED = \"red\"\n"), "{color}");
    assert!(color.contains("    GREEN = \"green\"\n"), "{color}");
    assert!(
        color.contains("    def visit(self, red: typing.Callable[[], T_Result], green: typing.Callable[[], T_Result]) -> T_Result:"),
        "{color}"
    );
    assert!(
        color.contains("        if self is Color.RED:\n            return red()\n"),
        "{color}"
    );
    assert!(
        !color.contains("typing.Literal"),
        "no Literal union: {color}"
    );
}

#[test]
fn version_uses_project_name() {
    let files = render(RICH_SPEC);
    assert_eq!(
        files["src/acme/version.py"],
        "from importlib import metadata\n\n__version__ = metadata.version(\"acme\")\n"
    );
}

#[test]
fn generate_writes_files_to_disk() {
    let dir = tempfile::tempdir().expect("tempdir");
    let spec = dir.path().join("api.yml");
    std::fs::write(&spec, RICH_SPEC).unwrap();
    let out = dir.path().join("out");
    let files = generate(GenerateArgs {
        spec,
        output: out.clone(),
        package_name: Some("acme".to_string()),
        project_name: None,
        client_class_name: None,
        audiences: Vec::new(),
        audience_strict: false,
        extra_fields: crozier::settings::ExtraFields::Allow,
    })
    .expect("generate succeeds");
    assert!(!files.is_empty());
    assert!(out.join("src/acme/types/widget.py").is_file());
    // project_name defaults to package_name when omitted.
    let version = std::fs::read_to_string(out.join("src/acme/version.py")).unwrap();
    assert!(version.contains("metadata.version(\"acme\")"));
}

#[test]
fn default_package_name_derives_from_title() {
    // No package/project override: names come from the title.
    let dir = tempfile::tempdir().expect("tempdir");
    let spec = dir.path().join("api.yml");
    std::fs::write(&spec, "openapi: 3.0.0\ninfo:\n  title: My Cool API\ncomponents:\n  schemas:\n    A:\n      type: string\n").unwrap();
    let files = render_files(GenerateArgs {
        spec,
        output: PathBuf::from("unused"),
        package_name: None,
        project_name: None,
        client_class_name: None,
        audiences: Vec::new(),
        audience_strict: false,
        extra_fields: crozier::settings::ExtraFields::Allow,
    })
    .unwrap();
    assert!(files.iter().any(|f| f.path.starts_with("src/my_cool_api")));
}

#[test]
fn unique_items_array_keeps_list_semantics_with_or_without_an_array_default() {
    let files = render(
        "openapi: 3.0.0\ninfo:\n  title: S\ncomponents:\n  schemas:\n    Obj:\n      type: object\n      properties:\n        tags:\n          type: array\n          uniqueItems: true\n          items:\n            type: string\n        status:\n          type: array\n          uniqueItems: true\n          default: []\n          items:\n            type: string\n",
    );
    assert!(
        files["src/acme/types/obj.py"].contains("tags: typing.Optional[typing.List[str]] = None")
    );
    assert!(
        files["src/acme/types/obj.py"].contains("status: typing.Optional[typing.List[str]] = None")
    );
}

#[test]
fn any_of_named_schema_renders_union_alias() {
    let files = render(
        "openapi: 3.0.0\ninfo:\n  title: U\ncomponents:\n  schemas:\n    Leaf:\n      type: object\n      properties:\n        v:\n          type: string\n    Either:\n      anyOf:\n        - $ref: \"#/components/schemas/Leaf\"\n        - type: integer\n",
    );
    assert!(files["src/acme/types/either.py"].contains("Either = typing.Union[Leaf, int]"));
}

#[test]
fn enum_with_non_string_type_is_not_an_enum_class() {
    // An enum on a non-string type falls through to the scalar/alias path rather
    // than an enum class.
    let files = render(
        "openapi: 3.0.0\ninfo:\n  title: E\ncomponents:\n  schemas:\n    Level:\n      type: integer\n      enum: [1, 2, 3]\n",
    );
    assert!(!files["src/acme/types/level.py"].contains("enum.Enum"));
}

#[test]
fn openapi_31_nullable_type_list_uses_primary() {
    // OpenAPI 3.1 `type: [string, "null"]` — the primary type is `string`.
    let files = render(
        "openapi: 3.1.0\ninfo:\n  title: N\ncomponents:\n  schemas:\n    Obj:\n      type: object\n      properties:\n        maybe:\n          type: [string, \"null\"]\n",
    );
    assert!(files["src/acme/types/obj.py"].contains("maybe: typing.Optional[str] = None"));
}

#[test]
fn additional_properties_true_maps_to_open_dict() {
    let files = render(
        "openapi: 3.0.0\ninfo:\n  title: A\ncomponents:\n  schemas:\n    Bag:\n      type: object\n      properties:\n        data:\n          type: object\n          additionalProperties: true\n",
    );
    // Fern types an open map (`additionalProperties: true`) as a dict to unknown.
    assert!(files["src/acme/types/bag.py"]
        .contains("data: typing.Optional[typing.Dict[str, typing.Any]] = None"));
}

#[test]
fn required_documented_field_uses_empty_pydantic_field() {
    // A required field with a description carries `pydantic.Field()` (no default),
    // unlike an optional documented field (`pydantic.Field(default=None)`).
    let files = render(
        "openapi: 3.0.0\ninfo:\n  title: D\ncomponents:\n  schemas:\n    Obj:\n      type: object\n      required: [name]\n      properties:\n        name:\n          type: string\n          description: The name.\n",
    );
    let obj = &files["src/acme/types/obj.py"];
    assert!(obj.contains("name: str = pydantic.Field()"), "{obj}");
    assert!(obj.contains("The name."));
}

#[test]
fn nullable_scalar_alias_is_optional() {
    // A top-level `nullable` scalar becomes an `Optional[..]` alias.
    let files = render(
        "openapi: 3.0.0\ninfo:\n  title: N\ncomponents:\n  schemas:\n    Maybe:\n      type: string\n      nullable: true\n",
    );
    assert!(files["src/acme/types/maybe.py"].contains("Maybe = typing.Optional[str]"));
}

#[test]
fn unknown_schema_maps_to_any_with_field_absence_modeled_separately() {
    // Fern 5.20 renders an empty alias and a required unknown field as bare `Any`.
    // A containing field adds one Optional only when the property may be absent.
    let files = render(
        "openapi: 3.0.0\ninfo:\n  title: U\ncomponents:\n  schemas:\n    Unknown: {}\n    Holder:\n      type: object\n      required: [value]\n      properties:\n        value: {}\n        other: {}\n    Patch:\n      type: object\n      properties:\n        value: {}\n",
    );
    assert!(files["src/acme/types/unknown.py"].contains("Unknown = typing.Any"));
    assert!(
        files["src/acme/types/holder.py"].contains("value: typing.Any\n"),
        "{}",
        files["src/acme/types/holder.py"]
    );
    assert!(
        files["src/acme/types/holder.py"].contains("other: typing.Optional[typing.Any] = None"),
        "{}",
        files["src/acme/types/holder.py"]
    );
    assert!(
        files["src/acme/types/patch.py"].contains("value: typing.Optional[typing.Any] = None"),
        "{}",
        files["src/acme/types/patch.py"]
    );
}

#[test]
fn nullable_map_makes_value_type_optional() {
    // Fern makes a nullable map's value optional too.
    let files = render(
        "openapi: 3.0.0\ninfo:\n  title: M\ncomponents:\n  schemas:\n    Obj:\n      type: object\n      properties:\n        m:\n          type: object\n          additionalProperties:\n            type: string\n          nullable: true\n",
    );
    assert!(
        files["src/acme/types/obj.py"]
            .contains("m: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None"),
        "{}",
        files["src/acme/types/obj.py"]
    );
}

#[test]
fn wide_string_enum_wraps_like_ruff() {
    // A string enum with many members: the members list one-per-line, and the
    // `visit` signature — too wide for ruff's 120-col limit — explodes one callback
    // parameter per line.
    let members: Vec<String> = (0..12)
        .map(|i| format!("        - VALUE_NUMBER_{i:02}_WITH_PADDING\n"))
        .collect();
    let spec = format!(
        "openapi: 3.0.0\ninfo:\n  title: W\ncomponents:\n  schemas:\n    Big:\n      type: string\n      enum:\n{}",
        members.concat()
    );
    let big = render(&spec)["src/acme/types/big.py"].clone();
    assert!(big.contains("class Big(enum.StrEnum):"), "{big}");
    assert!(
        big.contains("    VALUE_NUMBER_00_WITH_PADDING = \"VALUE_NUMBER_00_WITH_PADDING\"\n"),
        "{big}"
    );
    // ruff explodes the wide `visit` signature: `def visit(` then `self,` and each
    // callback parameter on its own line.
    assert!(
        big.contains("    def visit(\n        self,\n"),
        "exploded visit: {big}"
    );
    assert!(
        big.contains("        value_number_00_with_padding: typing.Callable[[], T_Result],\n"),
        "{big}"
    );
    assert!(
        big.contains("        if self is Big.VALUE_NUMBER_00_WITH_PADDING:\n"),
        "{big}"
    );
}

#[test]
fn emits_endpoint_package_markers_with_fern_module_names() {
    // An underscore-bearing operationId groups by its prefix (snake-cased) only when
    // that prefix *is* the tag (`my_group_doThing` under `MyGroup`); when the prefix
    // differs from the tag, Fern groups by the **tag** instead (`soloThing_doOther`
    // under `Solo` → `solo`, not `solothing` — bunq's `SCREAMING_Mixed` operationIds).
    // A groupless operationId is grouped by its first tag. With no tag, Fern keeps
    // the operation on the package-root client.
    let spec = "\
openapi: 3.0.0
info:
  title: E
paths:
  /a:
    post:
      operationId: my_group_doThing
      tags: [MyGroup]
  /b:
    get:
      operationId: soloThing_doOther
      tags: [Solo]
  /c:
    get:
      operationId: getWidgets
      tags: [Bare Things]
  /d:
    get:
      operationId: bareid
";
    let files = render(spec);
    // grouped-prefix==tag→prefix, grouped-prefix≠tag→tag, groupless→tag.
    for module in ["my_group", "solo", "bare_things"] {
        let init = files
            .get(&format!("src/acme/{module}/__init__.py"))
            .unwrap_or_else(|| panic!("expected {module}/__init__.py; got {:?}", files.keys()));
        assert_eq!(init, "\n\n\n\n", "{module} marker");
    }
    assert!(!files.contains_key("src/acme/bareid/__init__.py"));
}

/// A spec whose paths exercise the raw-client emitter: one emittable module
/// (`things`, two no-body operations — a path-param GET returning a model and a
/// described GET returning a scalar) alongside modules that are *not* emittable
/// (a query param, a request body, a non-2xx response, an empty response), so
/// only the supported module produces a `raw_client.py`.
const ENDPOINTS_SPEC: &str = r##"
openapi: 3.0.0
info:
  title: Ep API
components:
  schemas:
    Thing:
      type: object
      properties:
        name:
          type: string
paths:
  /things/{id}:
    get:
      operationId: things_getById
      tags: [Things]
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
      responses:
        "200":
          description: ""
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Thing"
  /things:
    get:
      description: Count the things.
      operationId: things_count
      tags: [Things]
      responses:
        "200":
          content:
            application/json:
              schema:
                type: integer
  /search:
    get:
      operationId: query_run
      tags: [Query]
      parameters:
        - name: q
          in: query
          schema:
            type: string
      responses:
        "200":
          content:
            application/json:
              schema:
                type: string
  /create:
    post:
      operationId: body_create
      tags: [Body]
      requestBody:
        content:
          application/json:
            schema:
              type: string
      responses:
        "200":
          content:
            application/json:
              schema:
                type: string
  /boom:
    get:
      operationId: err_get
      tags: [Err]
      responses:
        "404":
          content:
            application/json:
              schema:
                type: string
  /ping:
    get:
      operationId: noresp_get
      tags: [Noresp]
      responses:
        "204":
          description: no content
"##;

#[test]
fn emits_raw_client_only_for_supported_modules() {
    let files = render(ENDPOINTS_SPEC);

    let raw = files
        .get("src/acme/things/raw_client.py")
        .expect("things raw_client");
    // `err` declares only a non-2xx (404) response. It used to be silently dropped
    // (issue #43); now it emits a raw client whose method raises the typed
    // `NotFoundError` over the `ApiError` fallback.
    let err = files
        .get("src/acme/err/raw_client.py")
        .expect("err raw_client");
    assert!(err.contains("if _response.status_code == 404:"), "{err}");
    assert!(err.contains("raise NotFoundError("), "{err}");
    assert!(files.contains_key("src/acme/err/__init__.py"));

    // A 2xx response with no content (204) is supported and returns `None`.
    let noresp = files
        .get("src/acme/noresp/raw_client.py")
        .expect("noresp raw_client");
    assert!(noresp.contains("-> HttpResponse[None]:"), "{noresp}");
    assert!(
        noresp.contains("return HttpResponse(response=_response, data=None)"),
        "{noresp}"
    );

    // A query-parameter-only operation is now supported: the param becomes a
    // keyword-only optional argument and a `params={...}` entry.
    let query = files
        .get("src/acme/query/raw_client.py")
        .expect("query raw_client");
    assert!(query.contains("def run("), "{query}");
    assert!(query.contains("q: typing.Optional[str] = None,"), "{query}");
    assert!(query.contains("params={"), "{query}");
    assert!(query.contains("\"q\": q,"), "{query}");

    // A bare scalar request body serializes as `json=request` with the `OMIT`
    // sentinel and — being a scalar — no content-type header.
    let body = files
        .get("src/acme/body/raw_client.py")
        .expect("body raw_client");
    assert!(
        body.contains("OMIT = typing.cast(typing.Any, ...)"),
        "{body}"
    );
    // Fern treats a schema-bearing JSON body as required unless the document
    // explicitly marks it optional.
    assert!(body.contains("request: str"), "{body}");
    assert!(!body.contains("request: typing.Optional[str]"), "{body}");
    assert!(body.contains("json=request,"), "{body}");
    assert!(body.contains("omit=OMIT,"), "{body}");
    assert!(!body.contains("content-type"), "{body}");

    // Sync + async classes, both operations, the path-param f-string URL and the
    // response-type import, and the scalar return.
    assert!(raw.contains("class RawThingsClient:"), "{raw}");
    assert!(raw.contains("class AsyncRawThingsClient:"), "{raw}");
    assert!(raw.contains("from ..types.thing import Thing"), "{raw}");
    assert!(raw.contains("from ..core.jsonable_encoder import encode_path_param"));
    // `things_getById`: a single-segment group, so the method name is the
    // lowercased suffix; the path param drives an f-string URL and `HttpResponse[Thing]`.
    assert!(raw.contains("def getbyid("), "{raw}");
    assert!(raw.contains("f\"things/{encode_path_param(id)}\""), "{raw}");
    assert!(raw.contains("-> HttpResponse[Thing]:"), "{raw}");
    assert!(raw.contains("async def getbyid("), "{raw}");
    // `things_count`: no params, a scalar `int` response, and its description
    // becomes the docstring summary line.
    assert!(raw.contains("def count("), "{raw}");
    assert!(raw.contains("\"things\""), "{raw}");
    assert!(raw.contains("-> HttpResponse[int]:"), "{raw}");
    assert!(raw.contains("Count the things."), "{raw}");
}

/// A `$ref` enum body (content-type header) plus a `uuid` scalar body (gated out,
/// so its module never emits).
const BODY_SPEC: &str = r##"
openapi: 3.0.0
info:
  title: Body API
components:
  schemas:
    Weather:
      type: string
      enum: [SUNNY, RAINING]
    Pet:
      oneOf:
        - type: object
          properties: {bark: {type: string}}
        - type: object
          properties: {meow: {type: string}}
paths:
  /enum:
    post:
      operationId: enum_send
      tags: [Enum]
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/Weather"
      responses:
        "200":
          content:
            application/json:
              schema:
                type: string
  /union:
    post:
      operationId: union_send
      tags: [Union]
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/Pet"
      responses:
        "200":
          content:
            application/json:
              schema:
                type: string
  /uid:
    post:
      operationId: uid_send
      tags: [Uid]
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: string
              format: uuid
      responses:
        "200":
          content:
            application/json:
              schema:
                type: string
"##;

#[test]
fn named_enum_and_uuid_bodies_carry_content_type() {
    let files = render(BODY_SPEC);

    // A `$ref` enum body: `request: Weather`, `json=request`, and the
    // content-type header (named types get it, unlike bare scalars).
    let enum_client = files
        .get("src/acme/enum/raw_client.py")
        .expect("enum raw_client");
    assert!(
        enum_client.contains("*, request: Weather,"),
        "{enum_client}"
    );
    assert!(
        enum_client.contains("from ..types.weather import Weather"),
        "{enum_client}"
    );
    assert!(enum_client.contains("json=request,"), "{enum_client}");
    assert!(
        enum_client.contains("\"content-type\": \"application/json\","),
        "{enum_client}"
    );

    // A `$ref` union body serializes through the convert wrapper (write
    // direction), with the annotation naming the union type.
    let union = files
        .get("src/acme/union/raw_client.py")
        .expect("union raw_client");
    assert!(union.contains("*, request: Pet,"), "{union}");
    assert!(
        union.contains(
            "json=convert_and_respect_annotation_metadata(object_=request, annotation=Pet, direction=\"write\"),"
        ),
        "{union}"
    );
    assert!(
        union.contains("from ..core.serialization import convert_and_respect_annotation_metadata"),
        "{union}"
    );

    // A `format: uuid` body renders as `str` but — unlike a plain scalar — carries
    // the content-type header.
    let uid = files
        .get("src/acme/uid/raw_client.py")
        .expect("uid raw_client");
    assert!(uid.contains("*, request: str,"), "{uid}");
    assert!(uid.contains("json=request,"), "{uid}");
    assert!(
        uid.contains("\"content-type\": \"application/json\","),
        "{uid}"
    );
}

/// A header parameter (with the `X-` custom-header prefix) plus a scalar body and
/// a 204 response.
const HEADER_SPEC: &str = r##"
openapi: 3.0.0
info:
  title: Header API
paths:
  /h:
    post:
      operationId: hdr_send
      tags: [Hdr]
      parameters:
        - name: X-My-Header
          in: header
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: string
      responses:
        "204":
          description: ""
"##;

#[test]
fn header_param_strips_x_prefix_and_forces_content_type() {
    let files = render(HEADER_SPEC);
    let hdr = files
        .get("src/acme/hdr/raw_client.py")
        .expect("hdr raw_client");

    // The `X-` prefix is dropped for the Python name; the wire name stays the key.
    assert!(hdr.contains("my_header: str,"), "{hdr}");
    assert!(
        hdr.contains("\"X-My-Header\": str(my_header) if my_header is not None else None,"),
        "{hdr}"
    );
    // A scalar body would normally omit the content-type header, but an
    // accompanying header param forces it on.
    assert!(
        hdr.contains("\"content-type\": \"application/json\","),
        "{hdr}"
    );
    // The 204 response returns `None`.
    assert!(hdr.contains("-> HttpResponse[None]:"), "{hdr}");
}

#[test]
fn emits_core_runtime_with_substituted_sdk_name() {
    let files = render(RICH_SPEC);
    // The static core runtime is emitted alongside the type layer.
    assert!(files.contains_key("src/acme/core/http_client.py"));
    assert!(files.contains_key("src/acme/core/pydantic_utilities.py"));
    assert!(files.contains_key("src/acme/core/http_sse/_api.py"));
    // client_wrapper carries the substituted SDK name (project name) and version
    // under crozier's own header prefix; no placeholder remains.
    let cw = &files["src/acme/core/client_wrapper.py"];
    assert!(cw.contains("\"X-Crozier-SDK-Name\": \"acme\""), "{cw}");
    assert!(cw.contains("\"X-Crozier-SDK-Version\": \"0.0.0\""), "{cw}");
    assert!(
        !cw.contains("@@CROZIER"),
        "placeholder left unsubstituted: {cw}"
    );
    assert!(cw.contains("\"X-Crozier-Runtime\""), "{cw}");
    assert!(cw.contains("\"X-Crozier-Platform\""), "{cw}");
    assert!(
        cw.contains("base_max_retries=self.get_max_retries()"),
        "{cw}"
    );
    assert!(cw.contains("logging_config=self._logging"), "{cw}");
    assert!(
        cw.contains("async_base_headers=self.async_get_headers"),
        "{cw}"
    );

    let client_files = render(HEADER_SPEC);
    let client = &client_files["src/acme/client.py"];
    assert!(
        client.contains("max_retries: typing.Optional[int] = None"),
        "{client}"
    );
    assert!(
        client.contains("stream_reconnection_enabled: typing.Optional[bool] = None"),
        "{client}"
    );
    assert!(
        client.contains("logging: typing.Optional[typing.Union[LogConfig, Logger]] = None"),
        "{client}"
    );
    assert!(
        client.contains("def _make_default_async_client("),
        "{client}"
    );

    let init = &client_files["src/acme/__init__.py"];
    assert!(init.contains("DefaultAioHttpClient"), "{init}");
    assert!(init.contains("DefaultAsyncHttpxClient"), "{init}");
}

#[test]
fn oneof_hoists_inline_object_variants() {
    // A oneOf with inline-object variants: each is hoisted using its distinguishing
    // property when one exists, otherwise `{Name}{Ordinal}`.
    // Variant 0 uses allOf (a $ref base + an inline enum property); variant 1 is
    // a plain inline object.
    let spec = "\
openapi: 3.0.0
info:
  title: H
components:
  schemas:
    Dog:
      type: object
      properties:
        name:
          type: string
    Pet:
      oneOf:
        - type: object
          required:
            - kind
          allOf:
            - type: object
              properties:
                kind:
                  type: string
                  enum:
                    - dog
            - $ref: \"#/components/schemas/Dog\"
        - type: object
          properties:
            meow:
              type: boolean
        - $ref: \"#/components/schemas/Dog\"
        - type: string
";
    let files = render(spec);
    // Inline-object variants are hoisted; a $ref variant and a scalar variant
    // stay inline in the union.
    assert!(
        files["src/acme/types/pet.py"].contains("Pet = typing.Union[PetZero, PetMeow, Dog, str]"),
        "{}",
        files["src/acme/types/pet.py"]
    );
    // Variant 0: inherits its $ref base, with the inline enum hoisted and required.
    let zero = &files["src/acme/types/pet_zero.py"];
    assert!(zero.contains("class PetZero(Dog):"), "{zero}");
    assert!(zero.contains("    kind: PetZeroKind\n"), "{zero}");
    let kind = &files["src/acme/types/pet_zero_kind.py"];
    assert!(kind.contains("class PetZeroKind(enum.StrEnum):"), "{kind}");
    assert!(kind.contains("    DOG = \"dog\"\n"), "{kind}");
    // Variant 1: no base, so it extends UniversalBaseModel; its field is optional.
    let one = &files["src/acme/types/pet_meow.py"];
    assert!(one.contains("class PetMeow(UniversalBaseModel):"), "{one}");
    assert!(one.contains("meow: typing.Optional[bool] = None"), "{one}");
}

#[test]
fn object_with_only_additional_properties_is_a_dict_alias() {
    // A `type: object` with `additionalProperties` and no declared properties is
    // a map alias, not an (empty) model.
    let files = render(
        "openapi: 3.0.0\ninfo:\n  title: M\ncomponents:\n  schemas:\n    Bag:\n      type: object\n      additionalProperties:\n        type: string\n",
    );
    assert!(files["src/acme/types/bag.py"].contains("Bag = typing.Dict[str, str]"));
}

#[test]
fn named_explicit_empty_properties_is_model_while_omitted_is_dict_alias() {
    let files = render(
        "openapi: 3.0.0\ninfo:\n  title: M\ncomponents:\n  schemas:\n    Closed:\n      type: object\n      properties: {}\n    Open:\n      type: object\n",
    );
    let closed = &files["src/acme/types/closed.py"];
    assert!(
        closed.contains("class Closed(UniversalBaseModel):"),
        "{closed}"
    );
    assert!(closed.contains("extra=\"allow\""), "{closed}");
    assert!(files["src/acme/types/open.py"].contains("Open = typing.Dict[str, typing.Any]"));
}

#[test]
fn empty_title_falls_back_to_client_package() {
    let dir = tempfile::tempdir().expect("tempdir");
    let spec = dir.path().join("api.yml");
    std::fs::write(
        &spec,
        "openapi: 3.0.0\ninfo:\n  title: \"\"\ncomponents:\n  schemas:\n    A:\n      type: string\n",
    )
    .unwrap();
    let files = render_files(GenerateArgs {
        spec,
        output: PathBuf::from("unused"),
        package_name: None,
        project_name: None,
        client_class_name: None,
        audiences: Vec::new(),
        audience_strict: false,
        extra_fields: crozier::settings::ExtraFields::Allow,
    })
    .unwrap();
    assert!(files.iter().any(|f| f.path.starts_with("src/client")));
}

/// Render the real exhaustive spec in-process so the endpoint/error/scaffolding
/// branches (exercised only by the binary e2e, which coverage skips) are measured
/// here too. Byte-exactness is the e2e's job; this asserts the shapes are present.
#[test]
fn renders_exhaustive_endpoint_layer_in_process() {
    let spec = std::fs::read_to_string(
        std::path::Path::new(env!("CARGO_MANIFEST_DIR"))
            .join("tests/fixtures/exhaustive/openapi.yml"),
    )
    .expect("read exhaustive spec");
    let files = render(&spec);

    // Errors package + scaffolding.
    assert!(files.contains_key("src/acme/errors/bad_request_error.py"));
    let errors_init = &files["src/acme/errors/__init__.py"];
    assert!(errors_init.contains("_dynamic_imports"));
    assert!(errors_init.contains("\"BadRequestError\""));
    assert!(files["pyproject.toml"].contains("name = \"acme\""));
    assert!(files.contains_key("requirements.txt"));
    assert!(files.contains_key(".fern/metadata.json"));

    // Inline object body: hoisted fields, `json={...}`, per-field convert.
    let obj = &files["src/acme/endpoints_object/raw_client.py"];
    assert!(obj.contains("json={"));
    assert!(obj.contains("convert_and_respect_annotation_metadata"));
    assert!(obj.contains("long_: typing.Optional[int] = OMIT"));
    assert!(obj.contains("typing.Sequence[str]"));

    // Container bodies: plain maps and the convert wrapper for maps of objects.
    let container = &files["src/acme/endpoints_container/raw_client.py"];
    assert!(container.contains("json=request,"));
    assert!(container.contains("annotation=typing.Dict[str, TypesObjectWithRequiredField]"));

    // Mixed path/body: bytes body via `content=` and an array query param.
    let params = &files["src/acme/endpoints_params/raw_client.py"];
    assert!(params.contains("content=request,"));
    assert!(params.contains("\"content-type\": \"application/octet-stream\","));
    assert!(params.contains("typing.Optional[typing.Union[str, typing.Sequence[str]]]"));

    // Unknown body + a declared 400 raising the generated exception. The `{}` body
    // is declared `required: true` and carries no `nullable`, so the argument is a
    // required `typing.Any` — matching Fern's `noauth` client pair exactly.
    let noauth = &files["src/acme/noauth/raw_client.py"];
    assert!(noauth.contains("request: typing.Any,"), "{noauth}");
    assert!(!noauth.contains("request: typing.Optional[typing.Any] = None"));
    assert!(noauth.contains("if _response.status_code == 400:"));
    assert!(noauth.contains("raise BadRequestError("));
}

/// A non-2xx status crozier cannot name (a non-standard `460`) never suppresses the
/// method (issue #43): the module still emits, a mapped status (`404`) raises its
/// typed exception, and the unmapped status is skipped so the operation falls
/// through to the generic `ApiError`.
#[test]
fn unmapped_error_status_is_skipped_but_the_module_still_emits() {
    let files = render(
        "openapi: 3.0.0\ninfo:\n  title: E\npaths:\n  /x:\n    get:\n      operationId: things_get\n      responses:\n        \"200\":\n          content:\n            application/json:\n              schema:\n                type: string\n        \"404\":\n          content:\n            application/json:\n              schema:\n                $ref: \"#/components/schemas/Err\"\n        \"460\":\n          description: nonstandard\ncomponents:\n  schemas:\n    Err:\n      type: object\n      properties:\n        message:\n          type: string\n",
    );
    // The untagged operation is emitted on the package-root client.
    let raw = &files["src/acme/raw_client.py"];
    // The mapped 404 raises its typed exception with the declared body type.
    assert!(raw.contains("if _response.status_code == 404:"), "{raw}");
    assert!(raw.contains("raise NotFoundError("), "{raw}");
    // The unmapped 460 gets no branch — it falls through to the generic ApiError.
    assert!(!raw.contains("== 460"), "{raw}");
    assert!(
        raw.contains("raise ApiError(status_code=_response.status_code"),
        "{raw}"
    );
}

/// Every status Fern names maps to its exception (issue #43) — the IANA 4xx/5xx
/// registry plus the three widely deployed codes outside it. One operation
/// declaring them all emits a `raise` branch per status and a generated `errors/`
/// module per class, exercising the full status→name map.
#[test]
fn every_error_status_fern_names_maps_to_its_exception() {
    // (status, class name, module file stem) — the complete Fern map.
    let cases: &[(u16, &str, &str)] = &[
        (400, "BadRequestError", "bad_request_error"),
        (401, "UnauthorizedError", "unauthorized_error"),
        (402, "PaymentRequiredError", "payment_required_error"),
        (403, "ForbiddenError", "forbidden_error"),
        (404, "NotFoundError", "not_found_error"),
        (405, "MethodNotAllowedError", "method_not_allowed_error"),
        (406, "NotAcceptableError", "not_acceptable_error"),
        (
            407,
            "ProxyAuthenticationRequiredError",
            "proxy_authentication_required_error",
        ),
        (408, "RequestTimeoutError", "request_timeout_error"),
        (409, "ConflictError", "conflict_error"),
        (410, "GoneError", "gone_error"),
        (411, "LengthRequiredError", "length_required_error"),
        (412, "PreconditionFailedError", "precondition_failed_error"),
        (413, "ContentTooLargeError", "content_too_large_error"),
        (414, "UriTooLongError", "uri_too_long_error"),
        (
            415,
            "UnsupportedMediaTypeError",
            "unsupported_media_type_error",
        ),
        (
            416,
            "RangeNotSatisfiableError",
            "range_not_satisfiable_error",
        ),
        (417, "ExpectationFailedError", "expectation_failed_error"),
        (418, "ImATeapotError", "im_a_teapot_error"),
        (421, "MisdirectedRequestError", "misdirected_request_error"),
        (
            422,
            "UnprocessableEntityError",
            "unprocessable_entity_error",
        ),
        (423, "LockedError", "locked_error"),
        (424, "FailedDependencyError", "failed_dependency_error"),
        (425, "TooEarlyError", "too_early_error"),
        (426, "UpgradeRequiredError", "upgrade_required_error"),
        (428, "PreconditionError", "precondition_error"),
        (429, "TooManyRequestsError", "too_many_requests_error"),
        (
            431,
            "RequestHeaderFieldsTooLargeError",
            "request_header_fields_too_large_error",
        ),
        (
            451,
            "UnavailableForLegalReasonsError",
            "unavailable_for_legal_reasons_error",
        ),
        // Outside the IANA registry, but Fern names them: Esri's 498, nginx's 499,
        // and Apache's 509.
        (498, "InvalidTokenError", "invalid_token_error"),
        (
            499,
            "ClientClosedRequestError",
            "client_closed_request_error",
        ),
        (500, "InternalServerError", "internal_server_error"),
        (501, "NotImplementedError", "not_implemented_error"),
        (502, "BadGatewayError", "bad_gateway_error"),
        (503, "ServiceUnavailableError", "service_unavailable_error"),
        (504, "GatewayTimeoutError", "gateway_timeout_error"),
        (
            505,
            "HttpVersionNotSupportedError",
            "http_version_not_supported_error",
        ),
        (
            506,
            "VariantAlsoNegotiatesError",
            "variant_also_negotiates_error",
        ),
        (
            507,
            "InsufficientStorageError",
            "insufficient_storage_error",
        ),
        (508, "LoopDetectedError", "loop_detected_error"),
        (
            509,
            "BandwidthLimitExceededError",
            "bandwidth_limit_exceeded_error",
        ),
        (510, "NotExtendedError", "not_extended_error"),
        (
            511,
            "NetworkAuthenticationRequiredError",
            "network_authentication_required_error",
        ),
    ];
    let mut spec = String::from(
        "openapi: 3.0.0\ninfo:\n  title: E\npaths:\n  /x:\n    get:\n      operationId: things_get\n      responses:\n        \"200\":\n          content:\n            application/json:\n              schema:\n                type: string\n",
    );
    for (code, _, _) in cases {
        spec.push_str(&format!(
            "        \"{code}\":\n          description: err\n"
        ));
    }
    let files = render(&spec);
    let raw = &files["src/acme/raw_client.py"];
    for (code, class, module) in cases {
        assert!(
            raw.contains(&format!("if _response.status_code == {code}:")),
            "missing branch for {code}"
        );
        assert!(
            raw.contains(&format!("raise {class}(")),
            "missing raise for {class}"
        );
        let err_module = format!("src/acme/errors/{module}.py");
        let err = files
            .get(&err_module)
            .unwrap_or_else(|| panic!("missing {err_module}"));
        assert!(err.contains(&format!("class {class}(ApiError):")), "{err}");
        assert!(err.contains(&format!("status_code={code}")), "{err}");
    }
}

/// A `text/event-stream` (SSE) response generates Fern's context-managed streaming
/// shape (issue #43): the raw client is a sync/async context manager over
/// `httpx_client.stream(...)` decoding events into an iterator of chunks, and the
/// high-level client yields each chunk.
#[test]
fn sse_response_generates_a_streaming_client() {
    let files = render(
        "openapi: 3.0.0\ninfo:\n  title: E\npaths:\n  /stream:\n    post:\n      operationId: messages_stream\n      responses:\n        \"200\":\n          description: SSE stream\n          content:\n            text/event-stream: {}\n",
    );
    let raw = &files["src/acme/raw_client.py"];
    // Sync + async context managers over the streaming request, decoding via the
    // `core/http_sse` runtime into an (Async)Iterator of Any chunks.
    assert!(raw.contains("@contextlib.contextmanager"), "{raw}");
    assert!(raw.contains("@contextlib.asynccontextmanager"), "{raw}");
    assert!(
        raw.contains("self._client_wrapper.httpx_client.stream("),
        "{raw}"
    );
    assert!(
        raw.contains("_event_source = EventSource(_response)"),
        "{raw}"
    );
    assert!(
        raw.contains("for _sse in _event_source.iter_sse():"),
        "{raw}"
    );
    assert!(
        raw.contains("async for _sse in _event_source.aiter_sse():"),
        "{raw}"
    );
    assert!(
        raw.contains("-> typing.Iterator[HttpResponse[typing.Iterator[typing.Any]]]:"),
        "{raw}"
    );
    assert!(raw.contains("parse_sse_obj("), "{raw}");
    assert!(raw.contains("Yields"), "{raw}");
    // The high-level client yields each decoded chunk from the raw stream.
    let client = &files["src/acme/client.py"];
    assert!(
        client.contains("-> typing.Iterator[typing.Any]:"),
        "{client}"
    );
    assert!(client.contains("yield from r.data"), "{client}");
    assert!(client.contains("async for _chunk in r.data:"), "{client}");
}

/// Fern selects the JSON representation when a success response advertises the
/// same model as both JSON and SSE, rather than turning the method into a stream.
#[test]
fn json_response_takes_precedence_over_an_sse_alternative() {
    let files = render(
        r##"openapi: 3.0.0
info: { title: E }
paths:
  /stats:
    get:
      operationId: getStats
      responses:
        "200":
          description: Current stats.
          content:
            application/json:
              schema: { $ref: "#/components/schemas/Stats" }
            text/event-stream:
              schema: { $ref: "#/components/schemas/Stats" }
components:
  schemas:
    Stats:
      type: object
      properties:
        calls: { type: integer }
"##,
    );
    let raw = &files["src/acme/raw_client.py"];
    assert!(
        raw.contains("def get_stats(") && raw.contains("-> HttpResponse[Stats]:"),
        "{raw}"
    );
    assert!(
        raw.contains("self._client_wrapper.httpx_client.request("),
        "{raw}"
    );
    assert!(!raw.contains("@contextlib.contextmanager"), "{raw}");
    let client = &files["src/acme/client.py"];
    assert!(
        client.contains("def get_stats(") && client.contains("-> Stats:"),
        "{client}"
    );
    assert!(client.contains("return _response.data"), "{client}");
}

/// An inline-object success response on an untagged operation is hoisted into the
/// package-root `types/` package, and the root client becomes emittable.
#[test]
fn inline_object_response_is_hoisted_into_a_tag_type() {
    let files = render(
        "openapi: 3.0.0\ninfo:\n  title: E\npaths:\n  /y:\n    get:\n      operationId: widgets_get\n      responses:\n        \"200\":\n          content:\n            application/json:\n              schema:\n                type: object\n                properties:\n                  name:\n                    type: string\n",
    );
    // The response object is hoisted under the root `types/` package and the raw
    // client returns it.
    let hoisted = "src/acme/types/widgets_get_response.py";
    assert!(files.contains_key(hoisted), "expected {hoisted}");
    assert!(files[hoisted].contains("class WidgetsGetResponse"));
    let raw = &files["src/acme/raw_client.py"];
    assert!(raw.contains("HttpResponse[WidgetsGetResponse]"));
    assert!(raw.contains("from .types.widgets_get_response import WidgetsGetResponse"));
}

/// A discriminated `oneOf` with a `mapping` emits per-variant wrapper models over
/// a union alias, strips the discriminant from each member's own model, and does
/// not hoist the discriminant enum. The default (all-authenticated) bearer wrapper
/// is exercised alongside.
const DISCRIMINATED_SPEC: &str = r##"
openapi: 3.0.1
info:
  title: Shapes
paths:
  /shape:
    post:
      operationId: shapes_create
      responses:
        "200":
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Shape"
      security:
        - BearerAuth: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/Shape"
components:
  schemas:
    Shape:
      oneOf:
        - $ref: "#/components/schemas/Circle"
        - $ref: "#/components/schemas/Square"
      discriminator:
        propertyName: type
        mapping:
          circle: "#/components/schemas/Circle"
          square: "#/components/schemas/Square"
    Circle:
      type: object
      properties:
        type:
          type: string
          enum:
            - circle
        radius:
          type: number
      required:
        - type
        - radius
    Square:
      type: object
      properties:
        type:
          type: string
          enum:
            - square
        side:
          type: number
      required:
        - type
        - side
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
"##;

#[test]
fn discriminated_union_emits_variant_wrappers_and_strips_discriminant() {
    let files = render(DISCRIMINATED_SPEC);

    let shape = &files["src/acme/types/shape.py"];
    assert!(shape.contains("class Shape_Circle(UniversalBaseModel):"));
    assert!(shape.contains("type: typing.Literal[\"circle\"] = \"circle\""));
    // The alias is wrapped in `Annotated[..., pydantic.Field(discriminator=...)]`
    // so pydantic dispatches on the tag (issue #50 part 2; Fern 4.35.0+).
    assert!(shape.contains(
        "Shape = typing_extensions.Annotated[typing.Union[Shape_Circle, Shape_Square], \
         pydantic.Field(discriminator=\"type\")]"
    ));
    assert!(shape.contains("import typing_extensions"));
    assert!(shape.contains("from __future__ import annotations"));

    // The member model keeps its own (non-discriminant) fields and drops `type`;
    // the discriminant enum is never hoisted to a separate module.
    let circle = &files["src/acme/types/circle.py"];
    assert!(circle.contains("radius: float"));
    // The `type` field is gone (the `# type: ignore` config comment doesn't count).
    assert!(!circle.contains("\n    type:"));
    assert!(!circle.contains("Literal"));
    assert!(!files.contains_key("src/acme/types/circle_type.py"));

    // The aggregator groups all three names on the `.shape` import line.
    let init = &files["src/acme/types/__init__.py"];
    assert!(init.contains("from .shape import Shape, Shape_Circle, Shape_Square"));

    // All operations are authenticated, so the bearer token is required.
    let wrapper = &files["src/acme/core/client_wrapper.py"];
    assert!(wrapper.contains("token: typing.Union[str, typing.Callable[[], str]],"));
    assert!(wrapper.contains("headers[\"Authorization\"] = f\"Bearer {self._get_token()}\""));
}

/// An api-key header scheme shapes the client wrapper (public `api_key`, the
/// scheme's header, no token helper) and the root client's credential argument.
#[test]
fn api_key_scheme_shapes_client_wrapper_and_root_client() {
    let files = render(
        "openapi: 3.0.1\ninfo:\n  title: Keyed\npaths:\n  /me:\n    get:\n      operationId: users_me\n      responses:\n        \"200\":\n          content:\n            application/json:\n              schema:\n                type: string\n      security:\n        - ApiKeyAuth: []\ncomponents:\n  securitySchemes:\n    ApiKeyAuth:\n      type: apiKey\n      in: header\n      name: X-API-Key\n",
    );
    let wrapper = &files["src/acme/core/client_wrapper.py"];
    assert!(wrapper.contains("api_key: str,"));
    assert!(wrapper.contains("headers[\"X-API-Key\"] = self.api_key"));
    assert!(!wrapper.contains("_get_token"));

    let client = &files["src/acme/client.py"];
    assert!(client.contains("api_key=api_key,"));
    assert!(client.contains("api_key=\"YOUR_API_KEY\","));
}

/// When some operation is unauthenticated, the bearer token is optional (Fern's
/// default wrapper) — exercising the `all_operations_authenticated` false branch.
#[test]
fn unauthenticated_operation_makes_the_token_optional() {
    let files = render(
        "openapi: 3.0.1\ninfo:\n  title: Mixed\npaths:\n  /a:\n    get:\n      operationId: a_get\n      responses:\n        \"200\":\n          content:\n            application/json:\n              schema:\n                type: string\n      security:\n        - BearerAuth: []\n  /b:\n    get:\n      operationId: b_get\n      security: []\n      responses:\n        \"200\":\n          content:\n            application/json:\n              schema:\n                type: string\ncomponents:\n  securitySchemes:\n    BearerAuth:\n      type: http\n      scheme: bearer\n",
    );
    let wrapper = &files["src/acme/core/client_wrapper.py"];
    assert!(wrapper
        .contains("token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,"));
    let client = &files["src/acme/client.py"];
    assert!(
        client.contains(
            "async_token: typing.Optional[typing.Callable[[], typing.Awaitable[str]]] = None,"
        ),
        "{client}"
    );
    assert!(client.contains("async_token=async_token,"), "{client}");
}

/// An integer `enum` becomes a plain `int` alias, and a `$ref` integer-enum
/// request body is emittable (json=request + content-type header).
#[test]
fn integer_enum_alias_and_ref_body_are_emittable() {
    let files = render(
        "openapi: 3.0.1\ninfo:\n  title: Levels\npaths:\n  /p:\n    post:\n      operationId: levels_set\n      responses:\n        \"200\":\n          content:\n            application/json:\n              schema:\n                type: string\n      requestBody:\n        required: true\n        content:\n          application/json:\n            schema:\n              $ref: \"#/components/schemas/Level\"\ncomponents:\n  schemas:\n    Level:\n      type: integer\n      enum:\n        - 1\n        - 2\n",
    );
    assert!(files["src/acme/types/level.py"].contains("Level = int"));
    let raw = &files["src/acme/raw_client.py"];
    assert!(raw.contains("request: Level"));
    assert!(raw.contains("\"content-type\": \"application/json\""));
}

/// A multipart form body splits into `data=`/`files=` with `force_multipart`, and
/// a urlencoded form uses `data=` with the form content-type header.
#[test]
fn form_bodies_split_data_and_files() {
    let files = render(
        "openapi: 3.0.1\ninfo:\n  title: F\npaths:\n  /up:\n    post:\n      operationId: uploads_send\n      responses:\n        \"204\":\n          description: \"\"\n      requestBody:\n        required: true\n        content:\n          multipart/form-data:\n            schema:\n              type: object\n              required:\n                - doc\n              properties:\n                doc:\n                  type: string\n                  format: binary\n                note:\n                  type: string\n  /form:\n    post:\n      operationId: uploads_form\n      responses:\n        \"204\":\n          description: \"\"\n      requestBody:\n        required: true\n        content:\n          application/x-www-form-urlencoded:\n            schema:\n              type: object\n              properties:\n                q:\n                  type: string\n",
    );
    let raw = &files["src/acme/raw_client.py"];
    // Multipart: the binary field is a `core.File` in `files=`, the rest in `data=`.
    assert!(raw.contains("doc: core.File"));
    assert!(raw.contains("from . import core"), "{raw}");
    assert!(raw.contains("files={"));
    assert!(raw.contains("force_multipart=True,"));
    // Urlencoded: all fields in `data=` with the form content-type, no multipart.
    assert!(raw.contains("\"content-type\": \"application/x-www-form-urlencoded\""));
}

#[test]
fn multipart_reference_examples_put_files_before_other_required_fields() {
    let files = render(
        r#"openapi: 3.0.1
info: { title: Upload }
paths:
  /up:
    post:
      operationId: uploads_send
      requestBody:
        required: true
        content:
          multipart/form-data:
            schema:
              type: object
              required: [prompt, doc]
              properties:
                prompt: { type: string }
                doc: { type: string, format: binary }
      responses: { "204": { description: "" } }
"#,
    );
    let reference = &files["reference.md"];
    let file = reference
        .find("doc=\"example_doc\"")
        .expect("reference example includes the required file");
    let prompt = reference
        .find("prompt=\"prompt\"")
        .expect("reference example includes the required prompt");
    assert!(
        file < prompt,
        "multipart reference files come first: {reference}"
    );
}

/// The README example is the first endpoint with a request body, and its
/// abbreviated snippets show `...` for a fully-required body (here a container).
#[test]
fn readme_shows_dots_for_a_container_body_endpoint() {
    let files = render(
        "openapi: 3.0.1\ninfo:\n  title: R\npaths:\n  /ping:\n    get:\n      operationId: health_ping\n      responses:\n        \"200\":\n          content:\n            application/json:\n              schema:\n                type: string\n  /bulk:\n    post:\n      operationId: items_bulk\n      responses:\n        \"200\":\n          content:\n            application/json:\n              schema:\n                type: string\n      requestBody:\n        required: true\n        content:\n          application/json:\n            schema:\n              type: array\n              items:\n                type: string\n",
    );
    let readme = &files["README.md"];
    // Skips the no-body `health_ping` for the body-carrying `items_bulk`.
    assert!(readme.contains("client.items_bulk(...)"));
    assert!(readme.contains("client.items_bulk(..., request_options={"));
    assert!(!readme.contains("health_ping"));
}

#[test]
fn readme_abbreviates_a_body_endpoint_with_required_path_arguments() {
    let files = render(
        r#"openapi: 3.0.3
info: { title: Path Body, version: 1.0.0 }
paths:
  /groups/{groupId}/items:
    post:
      operationId: items_create
      tags: [Items]
      parameters:
        - { name: groupId, in: path, required: true, schema: { type: string } }
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties: { label: { type: string } }
      responses: { '204': { description: Created } }
"#,
    );
    let readme = &files["README.md"];
    assert!(readme.contains("client.items.create(..."), "{readme}");
    assert!(
        readme.contains("client.items.with_raw_response.create(..."),
        "{readme}"
    );
}

/// A `readOnly` property is optional even when listed in `required` (it is
/// server-populated), and `additionalProperties: true` maps to an open dict.
#[test]
fn read_only_field_is_optional_and_open_map_is_dict() {
    let files = render(
        "openapi: 3.0.1\ninfo:\n  title: R\ncomponents:\n  schemas:\n    Rec:\n      type: object\n      required:\n        - id\n        - name\n      properties:\n        id:\n          type: string\n          readOnly: true\n        name:\n          type: string\n        extra:\n          type: object\n          additionalProperties: true\n",
    );
    let rec = &files["src/acme/types/rec.py"];
    // `id` is readOnly → optional despite being required; `name` stays required.
    assert!(rec.contains("id: typing.Optional[str] = None"));
    assert!(rec.contains("name: str\n"));
    assert!(rec.contains("extra: typing.Optional[typing.Dict[str, typing.Any]] = None"));
}

/// A schema used only as an inlined (`$ref`-object) request body is not emitted as
/// a standalone type; one also used elsewhere (a response) is kept.
#[test]
fn request_body_only_type_is_dropped_but_reused_type_is_kept() {
    let files = render(
        "openapi: 3.0.1\ninfo:\n  title: B\npaths:\n  /a:\n    post:\n      operationId: things_make\n      responses:\n        \"200\":\n          content:\n            application/json:\n              schema:\n                $ref: \"#/components/schemas/Thing\"\n      requestBody:\n        required: true\n        content:\n          application/json:\n            schema:\n              $ref: \"#/components/schemas/MakeRequest\"\ncomponents:\n  schemas:\n    Thing:\n      type: object\n      properties:\n        id:\n          type: string\n    MakeRequest:\n      type: object\n      properties:\n        name:\n          type: string\n",
    );
    // `Thing` is a response type — kept; `MakeRequest` is only an inlined body — dropped.
    assert!(files.contains_key("src/acme/types/thing.py"));
    assert!(!files.contains_key("src/acme/types/make_request.py"));
    // Its fields were still hoisted onto the request method.
    assert!(files["src/acme/raw_client.py"].contains("name:"));
    // The aggregator omits the dropped type.
    assert!(!files["src/acme/types/__init__.py"].contains("MakeRequest"));
}

/// An `apiKey` scheme without its required `name` is rejected at the boundary
/// (rather than emitting a client with an empty header name).
#[test]
fn api_key_scheme_without_name_is_rejected() {
    let dir = tempfile::tempdir().expect("tempdir");
    let path = dir.path().join("api.yml");
    std::fs::write(
        &path,
        "openapi: 3.0.1\ninfo:\n  title: K\ncomponents:\n  securitySchemes:\n    ApiKeyAuth:\n      type: apiKey\n      in: header\n",
    )
    .unwrap();
    let err = render_files(GenerateArgs {
        spec: path,
        output: PathBuf::from("unused"),
        package_name: Some("acme".to_string()),
        project_name: Some("acme".to_string()),
        client_class_name: None,
        audiences: Vec::new(),
        audience_strict: false,
        extra_fields: crozier::settings::ExtraFields::Allow,
    })
    .expect_err("missing apiKey name must fail");
    assert!(err.to_string().contains("apiKey security scheme"));
}

/// Document-level `servers` generate `environment.py` (an `enum.Enum` with Fern's
/// single member — the first server, named from its description) and thread an
/// `environment`/`_get_base_url` through the root client and the package `__init__`.
#[test]
fn servers_generate_environment_and_thread_root_client() {
    let files = render(
        "openapi: 3.0.1\ninfo:\n  title: Srv\nservers:\n  - url: https://api.example.com\n    description: Production\n  - url: https://staging.example.com\n    description: Staging\npaths:\n  /session:\n    get:\n      operationId: cookies_getSession\n      tags: [Cookies]\n      responses:\n        \"200\":\n          content:\n            application/json:\n              schema: { $ref: \"#/components/schemas/Session\" }\n      security:\n        - BearerAuth: []\ncomponents:\n  schemas:\n    Session:\n      type: object\n      required: [id]\n      properties:\n        id: { type: string }\n  securitySchemes:\n    BearerAuth: { type: http, scheme: bearer }\n",
    );
    let env = &files["src/acme/environment.py"];
    assert!(env.contains("class AcmeApiEnvironment(enum.Enum):"));
    // Fern emits only the first server, named from its description.
    assert!(env.contains("PRODUCTION = \"https://api.example.com\""));
    assert!(!env.contains("STAGING"));

    let client = &files["src/acme/client.py"];
    assert!(client.contains("def _get_base_url("));
    assert!(client.contains("environment: AcmeApiEnvironment = AcmeApiEnvironment.PRODUCTION"));
    assert!(client.contains("_get_base_url(base_url=base_url, environment=environment)"));
    assert!(client.contains("from .environment import AcmeApiEnvironment"));
    // The example drops the hardcoded base_url once an environment exists.
    assert!(!client.contains("https://yourhost.com/path/to/api"));

    assert!(files["src/acme/__init__.py"].contains("AcmeApiEnvironment"));
}

#[test]
fn provider_named_server_description_uses_default_environment() {
    let files = render(
        "openapi: 3.0.1\ninfo:\n  title: Livepeer AI Runner\nservers:\n  - url: https://gateway.example.com\n    description: Livepeer Cloud Community Gateway\npaths:\n  /health:\n    get:\n      operationId: health\n      responses:\n        \"204\": { description: healthy }\n",
    );
    assert!(files["src/acme/environment.py"].contains("DEFAULT = \"https://gateway.example.com\""));
    assert!(files["src/acme/client.py"]
        .contains("environment: AcmeApiEnvironment = AcmeApiEnvironment.DEFAULT"));
}

/// `--client-class-name` (Fern's `client_class_name`) overrides the root client
/// class name, which otherwise derives from the package name as `{Pascal}Api`.
/// The override replaces the base name everywhere it flows: the root `client.py`
/// sync/async classes, the package `__init__` re-exports, and — with servers in
/// play — the `{ClientName}Environment` enum keyed off it.
#[test]
fn client_class_name_overrides_derived_root_client_name() {
    let dir = tempfile::tempdir().expect("tempdir");
    let path = dir.path().join("api.yml");
    std::fs::write(
        &path,
        "openapi: 3.0.1\ninfo:\n  title: Srv\nservers:\n  - url: https://api.example.com\n    description: Production\npaths:\n  /session:\n    get:\n      operationId: cookies_getSession\n      tags: [Cookies]\n      responses:\n        \"200\":\n          content:\n            application/json:\n              schema: { $ref: \"#/components/schemas/Session\" }\n      security:\n        - BearerAuth: []\ncomponents:\n  schemas:\n    Session:\n      type: object\n      required: [id]\n      properties:\n        id: { type: string }\n  securitySchemes:\n    BearerAuth: { type: http, scheme: bearer }\n",
    )
    .unwrap();
    let files: HashMap<String, String> = render_files(GenerateArgs {
        spec: path,
        output: PathBuf::from("unused"),
        package_name: Some("acme".to_string()),
        project_name: Some("acme".to_string()),
        client_class_name: Some("AcmeSdk".to_string()),
        audiences: Vec::new(),
        audience_strict: false,
        extra_fields: crozier::settings::ExtraFields::Allow,
    })
    .expect("render succeeds")
    .into_iter()
    .map(|f| (f.path.to_string_lossy().into_owned(), f.contents))
    .collect();

    let client = &files["src/acme/client.py"];
    assert!(client.contains("class AcmeSdk:"), "{client}");
    assert!(client.contains("class AsyncAcmeSdk:"), "{client}");
    // The package-derived default name is gone entirely.
    assert!(!client.contains("AcmeApi"), "{client}");

    // The re-exports and the environment enum both key off the overridden name.
    let init = &files["src/acme/__init__.py"];
    assert!(
        init.contains("AcmeSdk") && init.contains("AsyncAcmeSdk"),
        "{init}"
    );
    assert!(files["src/acme/environment.py"].contains("class AcmeSdkEnvironment(enum.Enum):"));
    assert!(!init.contains("AcmeApi"), "{init}");
}

/// A `cookie` parameter is dropped from the method signature entirely, and an
/// *optional* operation header is promoted to a client-wrapper-level `tenant`
/// field (set once at construction), threaded through the root client too.
#[test]
fn cookie_dropped_and_optional_header_promoted_to_client_wrapper() {
    let files = render(
        "openapi: 3.0.1\ninfo:\n  title: Ck\npaths:\n  /session:\n    get:\n      operationId: cookies_getSession\n      tags: [Cookies]\n      parameters:\n        - name: sid\n          in: cookie\n          required: true\n          schema: { type: string }\n        - name: X-Tenant\n          in: header\n          required: false\n          schema: { type: string }\n      responses:\n        \"200\":\n          content:\n            application/json:\n              schema: { $ref: \"#/components/schemas/Session\" }\n      security:\n        - BearerAuth: []\ncomponents:\n  schemas:\n    Session:\n      type: object\n      required: [id]\n      properties:\n        id: { type: string }\n  securitySchemes:\n    BearerAuth: { type: http, scheme: bearer }\n",
    );
    // The operation is emittable even though it carries a cookie param.
    let raw = &files["src/acme/cookies/raw_client.py"];
    // Neither the cookie nor the promoted header appears in the method signature.
    assert!(raw.contains("def getsession(self, *, request_options"));
    assert!(!raw.contains("sid"));
    assert!(!raw.contains("tenant"));
    assert!(!raw.contains("X-Tenant"));

    // The header is promoted to a global client-wrapper field.
    let wrapper = &files["src/acme/core/client_wrapper.py"];
    assert!(wrapper.contains("tenant: typing.Optional[str] = None,"));
    assert!(wrapper.contains("self._tenant = tenant"));
    assert!(wrapper.contains("if self._tenant is not None:"));
    assert!(wrapper.contains("headers[\"X-Tenant\"] = self._tenant"));
    assert!(wrapper.contains("tenant=tenant,\n            token=token,"));

    // And threaded through the root client (ctor, example, wrapper call).
    let client = &files["src/acme/client.py"];
    assert!(client.contains("tenant: typing.Optional[str] = None,"));
    assert!(client.contains("tenant=\"YOUR_TENANT\","));
    assert!(client.contains("tenant=tenant,"));
}

/// A required operation header is *not* promoted — it stays a per-method parameter
/// and no `tenant`-style global field appears on the client wrapper.
#[test]
fn required_header_is_not_promoted() {
    let files = render(
        "openapi: 3.0.1\ninfo:\n  title: Rh\npaths:\n  /ping:\n    get:\n      operationId: pings_get\n      tags: [Pings]\n      parameters:\n        - name: X-Trace\n          in: header\n          required: true\n          schema: { type: string }\n      responses:\n        \"200\":\n          content:\n            application/json:\n              schema: { $ref: \"#/components/schemas/Pong\" }\ncomponents:\n  schemas:\n    Pong:\n      type: object\n      required: [ok]\n      properties:\n        ok: { type: boolean }\n",
    );
    let raw = &files["src/acme/pings/raw_client.py"];
    assert!(raw.contains("trace: str"));
    // The required header is not lifted to a client-wrapper field.
    assert!(!files["src/acme/core/client_wrapper.py"].contains("self._trace"));
}

/// An inline (non-`$ref`) request body hoists its nested inline objects into the
/// tag's own `types/` package, and the inline response hoists too — including a
/// nested inline object (a sibling tag-type reference) and a `$ref` to a
/// package-root type (which resolves back up to the root `types/` package).
#[test]
fn inline_request_body_hoists_nested_objects_into_tag_types() {
    let files = render(
        "openapi: 3.0.1\ninfo:\n  title: In\npaths:\n  /search:\n    post:\n      operationId: inlined_search\n      tags: [Inlined]\n      responses:\n        \"200\":\n          content:\n            application/json:\n              schema:\n                type: object\n                properties:\n                  neighbor:\n                    type: object\n                    properties:\n                      id: { type: string }\n                    required: [id]\n                  hit:\n                    $ref: \"#/components/schemas/Hit\"\n                required: [neighbor]\n      requestBody:\n        required: true\n        content:\n          application/json:\n            schema:\n              type: object\n              properties:\n                filter:\n                  type: object\n                  properties:\n                    field: { type: string }\n                  required: [field]\n              required: [filter]\ncomponents:\n  schemas:\n    Hit:\n      type: object\n      required: [score]\n      properties:\n        score: { type: number }\n",
    );
    // Response hoisted to {Tag}{Method}Response, request nested object to
    // {Tag}{Method}Request{Prop}, both under the tag's `types/` package.
    let resp = "src/acme/inlined/types/inlined_search_response.py";
    let filt = "src/acme/inlined/types/inlined_search_request_filter.py";
    let neighbor = "src/acme/inlined/types/inlined_search_response_neighbor.py";
    assert!(files.contains_key(resp));
    assert!(files[resp].contains("class InlinedSearchResponse"));
    // Nested inline object → sibling tag-type import; `$ref` → root `types/`.
    assert!(files[resp]
        .contains("from .inlined_search_response_neighbor import InlinedSearchResponseNeighbor"));
    assert!(files[resp].contains("from ...types.hit import Hit"));
    assert!(files.contains_key(neighbor));
    assert!(files.contains_key(filt));
    assert!(files[filt].contains("class InlinedSearchRequestFilter"));
    // The tag's `types/__init__` and the tag package `__init__` re-export them.
    assert!(files.contains_key("src/acme/inlined/types/__init__.py"));
    assert!(files["src/acme/inlined/__init__.py"].contains("InlinedSearchRequestFilter"));
    // The raw client imports the hoisted types from the tag's `types/` package.
    let raw = &files["src/acme/inlined/raw_client.py"];
    assert!(raw.contains("from .types.inlined_search_response import InlinedSearchResponse"));
    assert!(
        raw.contains("from .types.inlined_search_request_filter import InlinedSearchRequestFilter")
    );
    // The package root re-exports the hoisted types through the tag submodule.
    assert!(files["src/acme/__init__.py"].contains("InlinedSearchResponse"));
}

/// Render a spec with an `x-crozier-audiences` filter, returning path -> contents.
fn render_with_audiences(spec: &str, audiences: &[&str]) -> HashMap<String, String> {
    render_with_audiences_mode(spec, audiences, false)
}

/// As [`render_with_audiences`], but toggles the strict flag (`--audience-strict`).
fn render_with_audiences_mode(
    spec: &str,
    audiences: &[&str],
    strict: bool,
) -> HashMap<String, String> {
    let dir = tempfile::tempdir().expect("tempdir");
    let path = dir.path().join("api.yml");
    std::fs::write(&path, spec).unwrap();
    let files = render_files(GenerateArgs {
        spec: path,
        output: PathBuf::from("unused"),
        package_name: Some("acme".to_string()),
        project_name: Some("acme".to_string()),
        client_class_name: None,
        audiences: audiences.iter().map(|s| s.to_string()).collect(),
        audience_strict: strict,
        extra_fields: crozier::settings::ExtraFields::Allow,
    })
    .expect("render succeeds");
    files
        .into_iter()
        .map(|f| (f.path.to_string_lossy().into_owned(), f.contents))
        .collect()
}

/// `x-crozier-audiences` spec (issue #41 gap 3): a public op referencing
/// `Widget`→`WidgetDetail`, an internal op referencing `Stats`, and an *unlabelled*
/// op referencing `Thing`.
const AUDIENCE_SPEC: &str = r##"
openapi: 3.0.1
info:
  title: Aud
paths:
  /widgets:
    get:
      operationId: widgets_list
      tags: [widgets]
      x-crozier-audiences: [public]
      responses:
        "200":
          content:
            application/json:
              schema: { $ref: "#/components/schemas/Widget" }
  /stats:
    get:
      operationId: admin_stats
      tags: [admin]
      x-crozier-audiences: [internal]
      responses:
        "200":
          content:
            application/json:
              schema: { $ref: "#/components/schemas/Stats" }
  /things:
    get:
      operationId: things_list
      tags: [things]
      responses:
        "200":
          content:
            application/json:
              schema: { $ref: "#/components/schemas/Thing" }
components:
  schemas:
    Widget:
      type: object
      properties:
        detail: { $ref: "#/components/schemas/WidgetDetail" }
    WidgetDetail:
      type: object
      properties:
        note: { type: string }
    Stats:
      type: object
      properties:
        count: { type: integer }
    Thing:
      type: object
      properties:
        id: { type: string }
"##;

#[test]
fn audience_filter_prunes_to_matching_ops_and_closure() {
    // Filtering to `public` keeps the public op and the unlabelled op (unlabelled
    // ops survive any filter), plus the transitive schema closure they reference
    // (Widget -> WidgetDetail, Thing) — and drops the internal op's client and its
    // internal-only Stats type.
    let files = render_with_audiences(AUDIENCE_SPEC, &["public"]);
    assert!(
        files.contains_key("src/acme/widgets/client.py"),
        "public op kept"
    );
    assert!(
        files.contains_key("src/acme/things/client.py"),
        "unlabelled op kept"
    );
    assert!(
        !files.contains_key("src/acme/admin/client.py"),
        "internal op dropped"
    );
    assert!(
        files.contains_key("src/acme/types/widget.py"),
        "referenced type kept"
    );
    assert!(
        files.contains_key("src/acme/types/widget_detail.py"),
        "transitively referenced type kept"
    );
    assert!(
        files.contains_key("src/acme/types/thing.py"),
        "unlabelled op's type kept"
    );
    assert!(
        !files.contains_key("src/acme/types/stats.py"),
        "type only the dropped op referenced is pruned"
    );
}

#[test]
fn strict_audience_filter_excludes_unlabelled_ops() {
    // Strict mode (`--audience-strict`) carves a *minimal* subset: only ops
    // carrying a matching audience survive. Unlike the permissive default, the
    // unlabelled `things` op — and its `Thing` type, which no surviving op reaches
    // — are pruned, matching Fern's exclusive filtering (issue #62).
    let files = render_with_audiences_mode(AUDIENCE_SPEC, &["public"], true);
    assert!(
        files.contains_key("src/acme/widgets/client.py"),
        "public op kept"
    );
    assert!(
        !files.contains_key("src/acme/things/client.py"),
        "unlabelled op dropped under strict"
    );
    assert!(
        !files.contains_key("src/acme/admin/client.py"),
        "internal op dropped"
    );
    assert!(
        files.contains_key("src/acme/types/widget.py"),
        "referenced type kept"
    );
    assert!(
        files.contains_key("src/acme/types/widget_detail.py"),
        "transitively referenced type kept"
    );
    assert!(
        !files.contains_key("src/acme/types/thing.py"),
        "unlabelled op's type pruned under strict"
    );
    assert!(
        !files.contains_key("src/acme/types/stats.py"),
        "internal-only type pruned"
    );
}

#[test]
fn no_audience_filter_generates_the_whole_api() {
    // Without a filter, every operation and schema is generated.
    let files = render_with_audiences(AUDIENCE_SPEC, &[]);
    for m in ["widgets", "admin", "things"] {
        assert!(
            files.contains_key(&format!("src/acme/{m}/client.py")),
            "{m} present"
        );
    }
    for t in ["widget", "widget_detail", "stats", "thing"] {
        assert!(
            files.contains_key(&format!("src/acme/types/{t}.py")),
            "{t} present"
        );
    }
}

#[test]
fn audience_closure_follows_every_ref_shape() {
    // The transitive closure must walk a `$ref` through every schema construct:
    // a property, an array `items`, `additionalProperties`, `allOf`/`oneOf`/`anyOf`
    // members, and a discriminator mapping. A public op references `Root`, which
    // reaches one type through each; all must survive `--audience public`.
    let spec = r##"
openapi: 3.0.1
info:
  title: Cl
paths:
  /root:
    get:
      operationId: root_get
      tags: [root]
      x-crozier-audiences: [public]
      responses:
        "200":
          content:
            application/json:
              schema: { $ref: "#/components/schemas/Root" }
components:
  schemas:
    Root:
      allOf:
        - $ref: "#/components/schemas/ViaAllOf"
      properties:
        prop: { $ref: "#/components/schemas/ViaProp" }
        list:
          type: array
          items: { $ref: "#/components/schemas/ViaItems" }
        map:
          type: object
          additionalProperties: { $ref: "#/components/schemas/ViaAddl" }
        choice:
          oneOf:
            - $ref: "#/components/schemas/ViaOneOf"
        alt:
          anyOf:
            - $ref: "#/components/schemas/ViaAnyOf"
        shape: { $ref: "#/components/schemas/Shape" }
    ViaAllOf: { type: object, properties: { a: { type: string } } }
    ViaProp: { type: object, properties: { a: { type: string } } }
    ViaItems: { type: object, properties: { a: { type: string } } }
    ViaAddl: { type: object, properties: { a: { type: string } } }
    ViaOneOf: { type: object, properties: { a: { type: string } } }
    ViaAnyOf: { type: object, properties: { a: { type: string } } }
    Shape:
      oneOf:
        - $ref: "#/components/schemas/Circle"
      discriminator:
        propertyName: kind
        mapping:
          circle: "#/components/schemas/Circle"
    Circle:
      type: object
      properties:
        kind: { type: string }
    Unreached: { type: object, properties: { a: { type: string } } }
"##;
    let files = render_with_audiences(spec, &["public"]);
    for t in [
        "via_all_of",
        "via_prop",
        "via_items",
        "via_addl",
        "via_one_of",
        "via_any_of",
        "circle",
    ] {
        assert!(
            files.contains_key(&format!("src/acme/types/{t}.py")),
            "closure should reach {t}; got {:?}",
            files
                .keys()
                .filter(|k| k.contains("types/"))
                .collect::<Vec<_>>()
        );
    }
    // A type no surviving operation references is pruned even though unlabelled.
    assert!(!files.contains_key("src/acme/types/unreached.py"));
}

/// Ignore extension (issue #78): a kept op, a `x-fern-ignore` op, and a
/// `x-crozier-ignore` op, each referencing an otherwise-unshared type. Both ignore
/// spellings must drop the op *and* its exclusive type.
const IGNORE_SPEC: &str = r##"
openapi: 3.0.1
info:
  title: Ign
paths:
  /keep:
    get:
      operationId: keep_list
      tags: [keep]
      responses:
        "200":
          content:
            application/json:
              schema: { $ref: "#/components/schemas/Keep" }
  /fern:
    get:
      operationId: fern_list
      tags: [fern]
      x-fern-ignore: true
      responses:
        "200":
          content:
            application/json:
              schema: { $ref: "#/components/schemas/OnlyFern" }
  /crozier:
    get:
      operationId: crozier_list
      tags: [crozier]
      x-crozier-ignore: true
      responses:
        "200":
          content:
            application/json:
              schema: { $ref: "#/components/schemas/OnlyCrozier" }
components:
  schemas:
    Keep: { type: object, properties: { note: { type: string } } }
    OnlyFern: { type: object, properties: { note: { type: string } } }
    OnlyCrozier: { type: object, properties: { note: { type: string } } }
"##;

#[test]
fn ignore_extension_drops_ops_and_their_exclusive_types_through_the_pipeline() {
    let files = render(IGNORE_SPEC);
    // The kept op's client and type are generated.
    assert!(files.contains_key("src/acme/keep/client.py"), "kept op");
    assert!(files.contains_key("src/acme/types/keep.py"), "kept type");
    // Both ignore spellings drop their client...
    assert!(
        !files.contains_key("src/acme/fern/client.py"),
        "x-fern-ignore op dropped"
    );
    assert!(
        !files.contains_key("src/acme/crozier/client.py"),
        "x-crozier-ignore op dropped"
    );
    // ...and the type each ignored op was the sole reference to.
    assert!(
        !files.contains_key("src/acme/types/only_fern.py"),
        "x-fern-ignore op's exclusive type pruned"
    );
    assert!(
        !files.contains_key("src/acme/types/only_crozier.py"),
        "x-crozier-ignore op's exclusive type pruned"
    );
}

#[test]
fn crozier_ignore_false_overrides_fern_ignore_true_through_the_pipeline() {
    // The Overlay "ignore-all-then-un-ignore-a-few" pattern: `x-fern-ignore: true`
    // marks the op ignored, but an explicit `x-crozier-ignore: false` keeps it.
    let spec = r##"
openapi: 3.0.1
info:
  title: Ign
paths:
  /keep:
    get:
      operationId: keep_list
      tags: [keep]
      x-fern-ignore: true
      x-crozier-ignore: false
      responses:
        "200":
          content:
            application/json:
              schema: { $ref: "#/components/schemas/Keep" }
components:
  schemas:
    Keep: { type: object, properties: { note: { type: string } } }
"##;
    let files = render(spec);
    assert!(
        files.contains_key("src/acme/keep/client.py"),
        "op kept by x-crozier-ignore: false despite x-fern-ignore: true"
    );
    assert!(files.contains_key("src/acme/types/keep.py"), "type kept");
}

#[test]
fn schema_level_ignore_drops_the_component_but_keeps_standalone_types() {
    // A component marked `x-crozier-ignore` is not emitted; a standalone component
    // no operation references is still emitted (a full generation would emit it).
    let spec = r##"
openapi: 3.0.1
info:
  title: Ign
paths:
  /keep:
    get:
      operationId: keep_list
      tags: [keep]
      responses:
        "200":
          content:
            application/json:
              schema: { $ref: "#/components/schemas/Keep" }
components:
  schemas:
    Keep: { type: object, properties: { note: { type: string } } }
    Internal:
      x-fern-ignore: true
      type: object
      properties: { note: { type: string } }
    Standalone: { type: object, properties: { note: { type: string } } }
"##;
    let files = render(spec);
    assert!(
        files.contains_key("src/acme/types/keep.py"),
        "referenced type kept"
    );
    assert!(
        files.contains_key("src/acme/types/standalone.py"),
        "standalone unreferenced type still emitted"
    );
    assert!(
        !files.contains_key("src/acme/types/internal.py"),
        "schema-level ignore drops the component"
    );
}

#[test]
fn fern_audiences_spelling_filters_like_the_crozier_one() {
    // Dual-header policy applied to `--audience`: a spec annotated only with
    // `x-fern-audiences` filters exactly as the `x-crozier-audiences` spelling would.
    let spec = r##"
openapi: 3.0.1
info:
  title: Aud
paths:
  /widgets:
    get:
      operationId: widgets_list
      tags: [widgets]
      x-fern-audiences: [public]
      responses:
        "200":
          content:
            application/json:
              schema: { $ref: "#/components/schemas/Widget" }
  /stats:
    get:
      operationId: admin_stats
      tags: [admin]
      x-fern-audiences: [internal]
      responses:
        "200":
          content:
            application/json:
              schema: { $ref: "#/components/schemas/Stats" }
components:
  schemas:
    Widget: { type: object, properties: { id: { type: string } } }
    Stats: { type: object, properties: { count: { type: integer } } }
"##;
    let files = render_with_audiences(spec, &["public"]);
    assert!(
        files.contains_key("src/acme/widgets/client.py"),
        "public op kept"
    );
    assert!(
        !files.contains_key("src/acme/admin/client.py"),
        "internal op dropped via x-fern-audiences"
    );
    assert!(
        !files.contains_key("src/acme/types/stats.py"),
        "internal type pruned"
    );
}

/// A self-referential model renders the recursive field as a string forward
/// reference, opts into deferred annotations, and repairs the model with
/// `update_forward_refs` — never a self-import (issue #84).
#[test]
fn self_referential_model_uses_forward_references() {
    let spec = r##"
openapi: 3.0.3
info: { title: Rec API }
paths:
  /tree:
    post:
      operationId: put_tree
      requestBody:
        content:
          application/json:
            schema: { $ref: "#/components/schemas/TreeNode" }
      responses: { "200": { description: ok } }
components:
  schemas:
    TreeNode:
      type: object
      properties:
        value: { type: string }
        children:
          type: array
          items: { $ref: "#/components/schemas/TreeNode" }
"##;
    let files = render(spec);
    let tree = &files["src/acme/types/tree_node.py"];
    assert!(
        tree.contains("from __future__ import annotations"),
        "recursive model opts into deferred annotations:\n{tree}"
    );
    assert!(
        tree.contains(r#"typing.List["TreeNode"]"#),
        "the recursive field is a string forward ref:\n{tree}"
    );
    assert!(
        tree.contains("update_forward_refs(TreeNode)"),
        "the forward ref is repaired at load time:\n{tree}"
    );
    assert!(
        !tree.contains("from .tree_node import TreeNode"),
        "a module never imports the name it defines:\n{tree}"
    );
}

/// A recursive discriminated union: the variant that references the union renders
/// it as a forward ref (a same-file union needs no import) and repairs only that
/// wrapper; the referenced schema defers its cross-module import (issue #84).
#[test]
fn recursive_discriminated_union_uses_forward_references() {
    let spec = r##"
openapi: 3.0.3
info: { title: Rec API }
paths:
  /pred:
    post:
      operationId: put_pred
      requestBody:
        content:
          application/json:
            schema: { $ref: "#/components/schemas/Node" }
      responses: { "200": { description: ok } }
components:
  schemas:
    Node:
      oneOf:
        - $ref: "#/components/schemas/AndNode"
        - $ref: "#/components/schemas/LeafNode"
      discriminator:
        propertyName: kind
        mapping:
          and: "#/components/schemas/AndNode"
          leaf: "#/components/schemas/LeafNode"
    AndNode:
      type: object
      required: [kind, children]
      properties:
        kind: { type: string, enum: [and] }
        children:
          type: array
          items: { $ref: "#/components/schemas/Node" }
    LeafNode:
      type: object
      required: [kind, name]
      properties:
        kind: { type: string, enum: [leaf] }
        name: { type: string }
"##;
    let files = render(spec);
    let node = &files["src/acme/types/node.py"];
    // The wrapper is named after the discriminant value, not the target schema.
    assert!(
        node.contains("class Node_And("),
        "value-named wrapper:\n{node}"
    );
    assert!(
        node.contains(r#"typing.List["Node"]"#),
        "the recursive variant field is a same-file forward ref:\n{node}"
    );
    assert!(
        node.contains("update_forward_refs(Node_And, Node=Node)")
            && !node.contains("update_forward_refs(Node_Leaf)"),
        "only the recursive wrapper is repaired with the full cycle closure:\n{node}"
    );
    // The referenced schema defers its cross-module import to after the class.
    let and_node = &files["src/acme/types/and_node.py"];
    let (before_class, after_class) = and_node
        .split_once("class AndNode(")
        .expect("AndNode class body");
    assert!(
        !before_class.contains("from .node import Node"),
        "the cross-module cyclic import is not eager:\n{and_node}"
    );
    assert!(
        after_class.contains("from .node import Node")
            && after_class.contains("update_forward_refs(AndNode, Node=Node)"),
        "the cyclic import is deferred and repaired:\n{and_node}"
    );
}

/// A property whose schema node is a JSON array (a `required` list misplaced
/// inside `properties`) degrades to `Optional[Any]` rather than synthesizing a
/// bogus type and a dangling import (issue #86).
#[test]
fn malformed_property_schema_degrades_to_any() {
    let spec = r##"
openapi: 3.1.0
info: { title: Bad API }
paths:
  /search:
    get:
      operationId: search
      responses:
        "200":
          description: ok
          content:
            application/json:
              schema:
                type: object
                properties:
                  widgets:
                    type: array
                    items: { type: string }
                  required: [widgets]
                  stringNode: not-a-schema
                  boolNode: true
                  negativeNode: -1
                  positiveNode: 1
                  floatNode: 1.5
                  nullNode: null
"##;
    let files = render(spec);
    let resp = &files["src/acme/types/search_response.py"];
    assert!(
        resp.contains("required: typing.Optional[typing.Any] = None")
            && !resp.contains("typing.Optional[typing.Optional[typing.Any]]"),
        "the array-valued node degrades to the unknown type:\n{resp}"
    );
    assert!(
        !resp.contains("import Required") && !files.contains_key("src/acme/types/widgets.py"),
        "no bogus type is synthesized or imported:\n{resp}"
    );
    for (field, wire_name) in [
        ("string_node", "stringNode"),
        ("bool_node", "boolNode"),
        ("negative_node", "negativeNode"),
        ("positive_node", "positiveNode"),
        ("float_node", "floatNode"),
        ("null_node", "nullNode"),
    ] {
        assert!(
            resp.contains(&format!("{field}: typing_extensions.Annotated["))
                && resp.contains(&format!("FieldMetadata(alias=\"{wire_name}\")"))
                && resp.contains(&format!("pydantic.Field(alias=\"{wire_name}\")")),
            "the malformed scalar property {field} must degrade independently:\n{resp}"
        );
    }
}

/// A root-operation nested type reaches the package-root `core` package at the
/// correct relative depth from `{pkg}/types/…` (issue #85).
#[test]
fn nested_operation_type_imports_core_at_correct_depth() {
    let spec = r##"
openapi: 3.0.3
info: { title: Nested API }
paths:
  /widgets/update:
    post:
      operationId: update_widget
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                details:
                  type: object
                  properties:
                    displayName: { type: string }
      responses: { "200": { description: ok } }
"##;
    let files = render(spec);
    let nested = &files["src/acme/types/update_widget_request_details.py"];
    assert!(
        nested.contains("from ..core.serialization import FieldMetadata"),
        "an aliased field reaches core.serialization from root types:\n{nested}"
    );
    assert!(
        nested.contains("from ..core.pydantic_utilities import"),
        "core.pydantic_utilities uses the same depth:\n{nested}"
    );
    assert!(
        !nested.contains("from ...core."),
        "no import uses the depth-wrong three-dot prefix:\n{nested}"
    );
}

/// A real-world-shaped API in one spec: `components.parameters` header refs shared
/// on the path item (a required and an optional one, both riding *every* operation,
/// so both promote to the client wrapper), a `components.responses` `$ref`, a
/// tag-prefixed camelCase `operationId` (`activitiesAll` → `all`), inline schema
/// hoisting (object property, array-of-objects, property `anyOf`), an inline
/// string-enum query param, an object query param, and spec `example`s on scalar
/// fields and a query param — the shapes the apideck corpus exercises, distilled so
/// the offline suite measures them. Mirrors [`docs/matching.md`].
const CATALOG_SPEC: &str = r##"
openapi: 3.0.1
info:
  title: Catalog
paths:
  /activities:
    parameters:
      - $ref: "#/components/parameters/AppId"
      - $ref: "#/components/parameters/Tenant"
    get:
      operationId: activitiesAll
      tags: [Activities]
      parameters:
        - name: level
          in: query
          schema:
            type: string
            enum: [low, high]
        - name: filter
          in: query
          schema:
            $ref: "#/components/schemas/WidgetFilter"
        - name: limit
          in: query
          required: true
          schema:
            type: integer
          example: 25
      responses:
        "200":
          $ref: "#/components/responses/WidgetList"
    post:
      operationId: activitiesAdd
      tags: [Activities]
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/Widget"
      responses:
        "200":
          $ref: "#/components/responses/OneWidget"
components:
  parameters:
    AppId:
      name: X-App-Id
      in: header
      required: true
      schema:
        type: string
    Tenant:
      name: X-Tenant
      in: header
      required: false
      schema:
        type: string
  responses:
    WidgetList:
      description: A page of widgets
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/Widget"
    OneWidget:
      description: One widget
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/Widget"
  schemas:
    WidgetFilter:
      type: object
      properties:
        status:
          type: string
    Widget:
      type: object
      required: [id, name, active, count]
      properties:
        id:
          type: string
          example: "wid_123"
        name:
          type: string
          example: "Gadget"
        active:
          type: boolean
          example: true
        count:
          type: integer
          example: 5
        meta:
          type: object
          properties:
            cursor:
              type: string
        stages:
          type: array
          items:
            type: object
            properties:
              label:
                type: string
        value:
          anyOf:
            - type: string
            - type: object
"##;

#[test]
fn catalog_spec_resolves_refs_hoists_inline_schemas_and_promotes_headers() {
    let files = render(CATALOG_SPEC);

    // Both ubiquitous headers promote to the client wrapper: the required one as a
    // plain `str`, the optional one as `typing.Optional[str]`.
    let wrapper = &files["src/acme/core/client_wrapper.py"];
    assert!(wrapper.contains("app_id: str"), "{wrapper}");
    assert!(
        wrapper.contains("tenant: typing.Optional[str]"),
        "{wrapper}"
    );
    // The promoted headers become wire keys on the outgoing request headers dict.
    assert!(
        wrapper.contains("headers[\"X-App-Id\"] = self._app_id"),
        "{wrapper}"
    );

    // The tag-prefixed camelCase operationId drops the tag: `activitiesAll` → `all`
    // (not `activities_all`), under the `activities` client.
    let client = &files["src/acme/activities/client.py"];
    assert!(
        client.contains("def all(") || client.contains("def all_("),
        "{client}"
    );
    assert!(client.contains("def add("), "{client}");

    // Inline schemas hoist into named tag types.
    assert!(
        files.contains_key("src/acme/types/widget_meta.py"),
        "inline object property hoisted to WidgetMeta"
    );
    assert!(
        files.contains_key("src/acme/types/widget_stages_item.py"),
        "array-of-inline-objects hoisted to WidgetStagesItem"
    );
    assert!(
        files.contains_key("src/acme/types/widget_value.py"),
        "property anyOf hoisted to a WidgetValue union alias"
    );
    let widget = &files["src/acme/types/widget.py"];
    assert!(
        widget.contains("meta: typing.Optional[WidgetMeta]"),
        "{widget}"
    );
    assert!(
        widget.contains("stages: typing.Optional[typing.List[WidgetStagesItem]]"),
        "{widget}"
    );

    // A spec `example` on a scalar field is shown verbatim in the worked example;
    // the request body's required fields carry theirs.
    let reference = &files["reference.md"];
    assert!(reference.contains("id=\"wid_123\""), "{reference}");
    assert!(reference.contains("name=\"Gadget\""), "{reference}");
    assert!(reference.contains("active=True"), "{reference}");
    assert!(reference.contains("count=5"), "{reference}");
    // `limit`'s example is declared on the *parameter*, not its schema, and the
    // parameter is `type: integer` — Fern 5.20.0 discards a parameter-level example
    // on anything but a `type: string` parameter, then fills the required argument
    // with its synthesized integer instead (probed directly; a schema-level example
    // on the same parameter would have been used verbatim, as `limit=7` and
    // `limit=15` below are).
    assert!(reference.contains("limit=1"), "{reference}");
}

/// Operations with neither an `operationId` nor a summary fall back to the lowercase
/// HTTP method plus every path segment. A declared name colliding with a Python
/// builtin still gets Fern's trailing-underscore munge.
const SYNTH_NAMING_SPEC: &str = r##"
openapi: 3.0.1
info:
  title: Synth
paths:
  /inventory:
    put:
      responses:
        "204":
          description: ""
  /{id}:
    delete:
      responses:
        "204":
          description: ""
  /reports:
    get:
      operationId: list
      responses:
        "204":
          description: ""
"##;

#[test]
fn synthesized_names_cover_verb_resource_and_reserved_munge() {
    let files = render(SYNTH_NAMING_SPEC);
    // Untagged operations stay on Fern's package-root client.
    let client = &files["src/acme/client.py"];
    assert!(client.contains("def put_inventory("), "{client}");
    assert!(client.contains("def delete_id("), "{client}");
    // A groupless `list` operationId collides with the builtin and becomes `list_`.
    assert!(client.contains("def list_("), "{client}");
}

/// Binary success responses use Fern's context-managed byte-stream API in both
/// clients, including typed error handling inside the stream lifetime.
#[test]
fn binary_response_emits_sync_and_async_byte_streams_with_typed_errors() {
    let files = render(
        r##"openapi: 3.0.1
info:
  title: Downloads
paths:
  /files/{file_id}:
    get:
      operationId: files_download
      tags: [Files]
      parameters:
        - in: path
          name: file_id
          required: true
          schema: { type: string }
      responses:
        "200":
          description: File contents.
          content:
            application/octet-stream:
              schema: { type: string, format: binary }
        "404":
          description: Missing file.
          content:
            application/json:
              schema: { $ref: "#/components/schemas/Problem" }
components:
  schemas:
    Problem:
      type: object
      required: [message]
      properties:
        message: { type: string }
"##,
    );

    let raw = &files["src/acme/files/raw_client.py"];
    assert!(raw.contains("@contextlib.contextmanager"), "{raw}");
    assert!(raw.contains("@contextlib.asynccontextmanager"), "{raw}");
    assert!(
        raw.contains("typing.Iterator[HttpResponse[typing.Iterator[bytes]]]"),
        "{raw}"
    );
    assert!(
        raw.contains("typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]"),
        "{raw}"
    );
    assert!(
        raw.contains("_response.iter_bytes(chunk_size=_chunk_size)"),
        "{raw}"
    );
    assert!(
        raw.contains("_response.aiter_bytes(chunk_size=_chunk_size)"),
        "{raw}"
    );
    assert!(raw.contains("if _response.status_code == 404:"), "{raw}");
    assert!(raw.contains("raise NotFoundError("), "{raw}");

    let client = &files["src/acme/files/client.py"];
    assert!(
        client.contains("with self._raw_client.download("),
        "{client}"
    );
    assert!(
        client.contains("async with self._raw_client.download("),
        "{client}"
    );
}

/// A shared HTTP error class must have one stable body annotation. If operations
/// disagree about that body, generation deliberately normalizes every occurrence
/// to `Any` rather than emitting an exception class whose annotation depends on
/// endpoint order.
#[test]
fn conflicting_error_bodies_normalize_to_any_across_endpoints() {
    let files = render(
        r##"openapi: 3.0.1
info:
  title: Errors
paths:
  /alpha:
    get:
      operationId: alpha_get
      tags: [Alpha]
      responses:
        "204": { description: done }
        "400":
          description: bad alpha
          content:
            application/json:
              schema: { $ref: "#/components/schemas/AlphaProblem" }
  /beta:
    get:
      operationId: beta_get
      tags: [Beta]
      responses:
        "204": { description: done }
        "400":
          description: bad beta
          content:
            application/json:
              schema: { $ref: "#/components/schemas/BetaProblem" }
components:
  schemas:
    AlphaProblem:
      type: object
      properties:
        alpha: { type: string }
    BetaProblem:
      type: object
      properties:
        beta: { type: integer, format: int64 }
"##,
    );

    let error = &files["src/acme/errors/bad_request_error.py"];
    assert!(error.contains("body: typing.Any"), "{error}");
    for raw_path in [
        "src/acme/alpha/raw_client.py",
        "src/acme/beta/raw_client.py",
    ] {
        let raw = &files[raw_path];
        assert!(raw.contains("typing.Any,"), "{raw_path}:\n{raw}");
        assert!(raw.contains("type_=typing.Any"), "{raw_path}:\n{raw}");
    }
}

/// A referenced request schema composed with `allOf` is flattened into endpoint
/// arguments, while its nested inline enum is moved beside the tag client.
#[test]
fn referenced_all_of_body_flattens_fields_and_moves_inline_enum() {
    let files = render(
        r##"openapi: 3.0.1
info:
  title: Jobs
paths:
  /jobs:
    post:
      operationId: jobs_create
      tags: [Jobs]
      requestBody:
        required: true
        content:
          application/json:
            schema: { $ref: "#/components/schemas/CreateJob" }
      responses:
        "200":
          description: created
          content:
            application/json:
              schema: { $ref: "#/components/schemas/Job" }
components:
  schemas:
    JobBase:
      type: object
      required: [name]
      properties:
        name: { type: string }
    CreateJob:
      allOf:
        - { $ref: "#/components/schemas/JobBase" }
        - type: object
          required: [priority]
          properties:
            priority:
              type: string
              enum: [low, high]
    Job:
      allOf:
        - { $ref: "#/components/schemas/JobBase" }
        - type: object
          properties:
            id: { type: integer, format: int64 }
"##,
    );

    let raw = &files["src/acme/jobs/raw_client.py"];
    assert!(raw.contains("name: str"), "{raw}");
    assert!(raw.contains("priority: CreateJobPriority"), "{raw}");
    assert!(raw.contains("\"name\": name"), "{raw}");
    assert!(raw.contains("\"priority\": priority"), "{raw}");
    assert!(files.contains_key("src/acme/jobs/types/create_job_priority.py"));
    assert!(!files.contains_key("src/acme/types/create_job.py"));
    assert!(files["src/acme/types/job.py"].contains("id: typing.Optional[int]"));
}

#[test]
fn response_hoisting_covers_numeric_names_nested_arrays_and_closed_objects() {
    let files = render(
        r#"openapi: 3.0.3
info: { title: Shapes, version: 1.0.0 }
paths:
  /shape:
    get:
      operationId: shapes_get
      tags: [Shapes]
      responses:
        '200':
          description: Found
          content:
            application/json:
              schema:
                type: object
                required: [day_0_end_time, items, metadata]
                properties:
                  day_0_end_time: { type: integer }
                  metadata:
                    type: object
                    properties: {}
                    additionalProperties: false
                  items:
                    type: array
                    items:
                      type: object
                      required: [details]
                      properties:
                        details:
                          type: object
                          required: [name]
                          properties:
                            name: { type: string }
"#,
    );
    let response = &files["src/acme/shapes/types/shapes_get_response.py"];
    assert!(response.contains("day0end_time: typing_extensions.Annotated[\n        int, FieldMetadata(alias=\"day_0_end_time\"), pydantic.Field(alias=\"day_0_end_time\")\n    ]"), "{response}");
    assert!(
        response.contains("metadata: ShapesGetResponseMetadata"),
        "{response}"
    );
    assert!(
        response.contains("items: typing.List[ShapesGetResponseItemsItem]"),
        "{response}"
    );
    let item = &files["src/acme/shapes/types/shapes_get_response_items_item.py"];
    assert!(
        item.contains("details: ShapesGetResponseItemsItemDetails"),
        "{item}"
    );
    assert!(files.contains_key("src/acme/shapes/types/shapes_get_response_metadata.py"));
}

#[test]
fn openapi_31_type_arrays_preserve_nullability_and_unknown_fallbacks() {
    let files = render(
        r#"openapi: 3.1.0
info: { title: Nullable, version: 1.0.0 }
paths:
  /value:
    get:
      operationId: nullable_get
      tags: [Nullable]
      responses:
        '200':
          description: Found
          content:
            application/json:
              schema:
                type: object
                required: [name, values, unconstrained]
                properties:
                  name: { type: [string, 'null'] }
                  values:
                    type: array
                    items: { type: ['null'] }
                  unconstrained: { type: array }
"#,
    );
    let model = &files["src/acme/nullable/types/nullable_get_response.py"];
    assert!(
        model.contains("name: typing.Optional[str] = None"),
        "{model}"
    );
    assert_eq!(
        model.matches("typing.List[typing.Any]").count(),
        2,
        "null-only and missing item schemas both use the unknown fallback: {model}"
    );
}

#[test]
fn worked_examples_render_media_component_scalar_and_composite_values() {
    let files = render(
        r##"openapi: 3.1.0
info: { title: Examples, version: 1.0.0 }
paths:
  /widgets:
    post:
      operationId: widgets_create
      tags: [Widgets]
      parameters:
        - name: limit
          in: query
          required: true
          schema: { type: integer, examples: [7] }
      requestBody:
        content:
          application/json:
            example: { active: true }
            schema: { $ref: "#/components/schemas/CreateWidget" }
      responses:
        '204': { description: Created }
components:
  schemas:
    WidgetState: { type: string, enum: [ACTIVE, DISABLED] }
    CreateWidget:
      type: object
      example:
        name: Example Widget
        state: DISABLED
        labels: [regional, global]
        properties: { custom: value }
      properties:
        name: { type: string }
        active: { type: boolean }
        state: { $ref: "#/components/schemas/WidgetState" }
        labels: { type: array, items: { type: string } }
        properties: { type: object, additionalProperties: { type: string } }
"##,
    );
    let client = &files["src/acme/widgets/client.py"];
    assert!(client.contains("limit=7"), "{client}");
    assert!(client.contains("active=True"), "{client}");
    assert!(client.contains("name=\"Example Widget\""), "{client}");
    assert!(client.contains("state=WidgetState.DISABLED"), "{client}");
    assert!(
        client.contains("labels=[\"regional\", \"global\"]"),
        "{client}"
    );
    assert!(
        client.contains("properties={\"custom\": \"value\"}"),
        "{client}"
    );
}

#[test]
fn multipart_fallbacks_emit_optional_unknown_and_file_only_empty_data() {
    let files = render(
        r#"openapi: 3.1.0
info: { title: Uploads, version: 1.0.0 }
paths:
  /unknown:
    post:
      operationId: uploads_unknown
      tags: [Uploads]
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                payload: {}
                labels: { type: array, items: { type: string } }
                note: { type: string }
      responses:
        '204': { description: Created }
  /file:
    post:
      operationId: uploads_file
      tags: [Uploads]
      requestBody:
        required: true
        content:
          multipart/form-data:
            schema:
              type: object
              required: [document]
              properties:
                document: { type: string, format: binary }
      responses:
        '204': { description: Created }
"#,
    );
    let raw = &files["src/acme/uploads/raw_client.py"];
    assert!(
        raw.contains("payload: typing.Optional[typing.Any] = OMIT"),
        "{raw}"
    );
    assert!(
        raw.contains(
            r#""payload": json.dumps(jsonable_encoder(payload)) if payload is not OMIT else OMIT"#
        ) && raw.contains(
            r#""labels": json.dumps(jsonable_encoder(labels)) if labels is not OMIT else OMIT"#
        ),
        "unknown and collection form values must be JSON encoded: {raw}"
    );
    assert!(
        raw.contains(r#""note": note"#),
        "scalar form values stay unencoded: {raw}"
    );
    assert!(raw.contains("document: core.File"), "{raw}");
    assert!(
        raw.contains("data={},"),
        "file-only multipart must retain an empty data map: {raw}"
    );
    assert!(
        raw.contains("files={\n                \"document\": document,"),
        "{raw}"
    );
    assert!(raw.contains("force_multipart=True"), "{raw}");
}

#[test]
fn multipart_related_uses_declared_part_content_types_when_json_is_absent() {
    let files = render(
        r#"openapi: 3.1.0
info: { title: Related Upload, version: 1.0.0 }
paths:
  /upload:
    post:
      operationId: uploads_create
      tags: [Uploads]
      requestBody:
        content:
          multipart/related:
            encoding:
              metadata: { contentType: application/json }
              document: { contentType: application/pdf }
            schema:
              type: object
              properties:
                metadata: { $ref: '#/components/schemas/Metadata' }
                document: { type: string, format: binary }
      responses: { '204': { description: Created } }
components:
  schemas:
    Metadata: { type: object, properties: { name: { type: string } } }
"#,
    );
    let raw = &files["src/acme/uploads/raw_client.py"];
    assert!(
        raw.contains("json.dumps(jsonable_encoder(metadata))"),
        "{raw}"
    );
    assert!(raw.contains("\"application/json\""), "{raw}");
    assert!(
        raw.contains(
            "core.with_content_type(file=document, default_content_type=\"application/pdf\")"
        ),
        "{raw}"
    );
    assert!(raw.contains("force_multipart=True"), "{raw}");
}

#[test]
fn untagged_tag_named_and_ignored_body_operations_choose_the_right_surface() {
    let files = render(
        r#"openapi: 3.0.3
info: { title: Routing, version: 1.0.0 }
paths:
  /root:
    get:
      operationId: root_get
      responses:
        '200': { description: OK, content: { application/json: { schema: { type: string } } } }
      requestBody:
        content:
          application/json:
            schema: { type: string }
  /widgets:
    post:
      operationId: widgets
      tags: [widgets]
      requestBody:
        content:
          text/plain:
            schema: { type: string }
      responses:
        '204': { description: Done }
"#,
    );
    let root = &files["src/acme/raw_client.py"];
    assert!(root.contains("def root_get("), "{root}");
    assert!(
        !root.contains("request:"),
        "GET request bodies must be ignored: {root}"
    );
    assert!(
        root.contains("def widgets("),
        "tag-equal operation IDs remain on the root surface: {root}"
    );
    assert!(!files.contains_key("src/acme/widgets/raw_client.py"));
    let client = &files["src/acme/client.py"];
    assert!(
        client.contains("def root_get("),
        "untagged operation must be available on the root client: {client}"
    );
    assert!(
        client.contains("def widgets("),
        "tag-equal operation must be available on the root client: {client}"
    );
}

#[test]
fn component_request_body_refs_and_vendor_json_maps_reach_normalized_media_paths() {
    let files = render(
        r##"openapi: 3.0.3
info: { title: Media, version: 1.0.0 }
paths:
  /credentials:
    post:
      operationId: identity_add
      tags: [Identity]
      requestBody: { $ref: "#/components/requestBodies/CredentialBody" }
      responses:
        '204': { description: Added }
  /manifests/{id}:
    post:
      operationId: imports_manifest
      tags: [Imports]
      parameters:
        - { name: id, in: path, required: true, schema: { type: string } }
      requestBody:
        required: true
        content:
          application/vnd.example+json:
            schema: { type: object }
      responses:
        '204': { description: Imported }
components:
  requestBodies:
    CredentialBody:
      required: true
      content:
        application/json:
          schema: { $ref: "#/components/schemas/Credential" }
  schemas:
    Credential:
      type: object
      required: [username]
      properties:
        username: { type: string }
"##,
    );
    let identity = &files["src/acme/identity/raw_client.py"];
    assert!(identity.contains("username: str"), "{identity}");
    assert!(
        identity.contains("json={\n                \"username\": username,"),
        "{identity}"
    );
    let imports = &files["src/acme/imports/raw_client.py"];
    assert!(
        imports.contains("request: typing.Dict[str, typing.Any]"),
        "{imports}"
    );
    assert!(
        imports.contains("\"content-type\": \"application/vnd.example+json\""),
        "{imports}"
    );
}

#[test]
fn binary_request_media_selection_covers_exact_wildcard_and_vendor_json() {
    let files = render(
        r##"openapi: 3.0.3
info: { title: Binary, version: 1.0.0 }
paths:
  /import:
    post:
      operationId: widgets_upload
      tags: [Widgets]
      requestBody:
        content:
          application/zip:
            schema: { $ref: "#/components/schemas/FileContent" }
      responses:
        '204': { description: Imported }
  /create:
    post:
      operationId: widgets_create
      tags: [Widgets]
      requestBody:
        content:
          '*/*':
            schema: { $ref: "#/components/schemas/FileContent" }
          application/vnd.create+json:
            schema: { $ref: "#/components/schemas/CreateWidget" }
      responses:
        '204': { description: Created }
  /raw:
    post:
      operationId: widgets_raw
      tags: [Widgets]
      requestBody:
        required: true
        content:
          '*/*':
            schema: { type: string, format: binary }
      responses:
        '204': { description: Accepted }
  /export:
    get:
      operationId: widgets_export
      tags: [Widgets]
      description: Exports all widgets.
      responses:
        '200':
          description: Export
          content:
            application/zip:
              schema: { $ref: "#/components/schemas/FileContent" }
components:
  schemas:
    FileContent: { type: string, format: binary }
    CreateWidget:
      type: object
      properties:
        name: { type: string }
"##,
    );
    let raw = &files["src/acme/widgets/raw_client.py"];
    let upload = raw.split("def upload(").nth(1).expect("ZIP upload method");
    assert!(upload.contains("content=request,\n            headers={\n                \"content-type\": \"application/zip\""), "{upload}");
    assert!(
        upload.contains("request: typing.Optional[FileContent] = None"),
        "{upload}"
    );
    let create = raw
        .split("def create(")
        .nth(1)
        .expect("wildcard request method");
    assert!(
        create.contains("json=request,") && !create.contains("\"content-type\": \"*/*\""),
        "wildcard selection uses the JSON-compatible request path: {create}"
    );
    let raw_upload = raw
        .split("def raw(")
        .nth(1)
        .expect("inline wildcard request method");
    assert!(
        raw_upload.contains("request: bytes") && raw_upload.contains("json=request,"),
        "inline wildcard binary bodies use Fern's bytes contract: {raw_upload}"
    );
    let client = &files["src/acme/widgets/client.py"];
    let raw_example = client
        .split("def raw(")
        .nth(1)
        .expect("inline wildcard high-level method");
    assert!(
        raw_example.contains("request: bytes")
            && raw_example.contains("request=\"string\"")
            && !raw_example.contains("request=b\"string\""),
        "Fern's high-level bytes contract keeps its string example: {raw_example}"
    );
    let reference = &files["reference.md"];
    assert!(
        reference.contains("**request:** `str`"),
        "Fern's reference writer retains the OpenAPI string type: {reference}"
    );
    assert!(
        raw.contains("@contextlib.contextmanager"),
        "referenced binary responses stream: {raw}"
    );
    assert!(
        !raw.contains("HttpResponse[FileContent]"),
        "binary aliases are not used as response models: {raw}"
    );
    assert!(
        raw.contains("Exports all widgets.\n\n        Parameters"),
        "{raw}"
    );
}

#[test]
fn referenced_unknown_response_keeps_empty_body_guard() {
    let files = render(
        r##"openapi: 3.0.3
info: { title: Proxy, version: 1.0.0 }
paths:
  /proxy:
    get:
      operationId: proxy_get
      tags: [Proxy]
      responses:
        '200': { $ref: "#/components/responses/Ok" }
components:
  responses:
    Ok:
      description: Arbitrary JSON
      content:
        application/json:
          schema: {}
"##,
    );
    let raw = &files["src/acme/proxy/raw_client.py"];
    assert!(raw.contains("HttpResponse[typing.Any]"), "{raw}");
    assert!(
        raw.contains("if _response is None or not _response.text.strip():"),
        "a referenced unknown response keeps Fern's empty-body guard: {raw}"
    );
}

#[test]
fn octet_stream_request_uses_bytes_transport() {
    let files = render(
        r#"openapi: 3.0.3
info: { title: Octets, version: 1.0.0 }
paths:
  /upload:
    post:
      operationId: octets_upload
      tags: [Octets]
      requestBody:
        content:
          application/octet-stream: { schema: { type: string, format: binary } }
      responses: { '204': { description: Uploaded } }
"#,
    );
    let raw = &files["src/acme/octets/raw_client.py"];
    assert!(
        raw.contains(
            "request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]"
        ),
        "{raw}"
    );
    assert!(raw.contains("content=request,"), "{raw}");
    assert!(
        raw.contains("\"content-type\": \"application/octet-stream\""),
        "{raw}"
    );
}

#[test]
fn optional_basic_auth_and_parameter_enums_emit_all_specialized_fragments() {
    let files = render(
        r#"openapi: 3.0.3
info: { title: Auth, version: 1.0.0 }
security: []
paths:
  /widgets/{state}:
    post:
      operationId: widgets_update
      tags: [Widgets]
      parameters:
        - name: state
          in: path
          required: true
          schema: { type: string, enum: [ACTIVE, DISABLED] }
        - name: X-Widget-Mode
          in: header
          required: true
          schema: { type: string, enum: [FAST, SAFE] }
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              required: [action]
              properties:
                action: { type: string, enum: [START, STOP] }
                file: { type: string, format: binary }
      responses:
        '204': { description: Updated }
components:
  securitySchemes:
    Basic:
      type: http
      scheme: basic
"#,
    );
    let root = &files["src/acme/client.py"];
    assert!(
        root.contains(
            "username: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None"
        ),
        "{root}"
    );
    assert!(
        root.contains(
            "password: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None"
        ),
        "{root}"
    );
    let wrapper = &files["src/acme/core/client_wrapper.py"];
    assert!(
        wrapper.contains("if username is not None and password is not None:"),
        "{wrapper}"
    );
    assert!(
        wrapper.contains("httpx.BasicAuth(username, password)._auth_header"),
        "{wrapper}"
    );
    let raw = &files["src/acme/widgets/raw_client.py"];
    assert!(raw.contains("state: WidgetsUpdateRequestState"), "{raw}");
    assert!(
        raw.contains("widget_mode: WidgetsUpdateRequestXWidgetMode"),
        "{raw}"
    );
    assert!(raw.contains("action: WidgetsUpdateRequestAction"), "{raw}");
    // `file` is outside `required`, and Fern spreads an optional multipart part in
    // conditionally rather than sending a `None` one — DaniWeb's `csv` is the
    // corpus's witness; `a_required_multipart_file_part_is_passed_unconditionally`
    // below covers the other half.
    assert!(
        raw.contains("files={\n                **({\"file\": file} if file is not None else {}),"),
        "{raw}"
    );
    for module in [
        "widgets_update_request_state.py",
        "widgets_update_request_x_widget_mode.py",
        "widgets_update_request_action.py",
    ] {
        assert!(
            files.contains_key(&format!("src/acme/widgets/types/{module}")),
            "missing {module}"
        );
    }
}

/// Drive every committed feature fixture through the library boundary. The
/// binary fixture tests pin these files too, but subprocess execution does not
/// contribute coverage; this test compares every non-aggregator Python module
/// in-process so the same production branches are measured by llvm-cov.
#[test]
fn committed_feature_fixture_python_matches_in_process() {
    let root = std::path::Path::new(env!("CARGO_MANIFEST_DIR")).join("tests/fixtures");
    let mut fixtures = Vec::new();
    for entry in std::fs::read_dir(&root).unwrap() {
        let entry = entry.unwrap();
        if entry.path().join("openapi.yml").is_file() && entry.path().join("expected").is_dir() {
            fixtures.push(entry.path());
        }
    }
    fixtures.sort();
    assert!(fixtures.len() >= 25, "fixture corpus unexpectedly shrank");

    for fixture in fixtures {
        let name = fixture.file_name().unwrap().to_string_lossy();
        let spec = std::fs::read_to_string(fixture.join("openapi.yml")).unwrap();
        let expected_src_root = fixture.join("expected/src");
        let expected_src = std::fs::read_dir(&expected_src_root)
            .unwrap()
            .filter_map(Result::ok)
            .map(|entry| entry.path())
            .find(|path| path.is_dir())
            .unwrap();
        let package = expected_src.file_name().unwrap().to_str().unwrap();
        let files = render_package(&spec, package);
        let mut compared = 0;
        let mut expected_files = Vec::new();
        python_files_below(&expected_src, &mut expected_files);
        for path in expected_files {
            if path.file_name().and_then(std::ffi::OsStr::to_str) == Some("__init__.py") {
                continue;
            }
            let rel = path
                .strip_prefix(fixture.join("expected"))
                .unwrap()
                .to_string_lossy()
                .replace('\\', "/");
            let Some(actual) = files.get(&rel) else {
                continue;
            };
            let expected = std::fs::read_to_string(&path).unwrap();
            if crozier::strip_python_comments(actual) == crozier::strip_python_comments(&expected) {
                compared += 1;
            }
        }
        assert!(
            compared >= 5,
            "fixture {name} had only {compared} byte-matched concrete Python modules"
        );
    }
}

#[test]
fn reference_and_docstring_alignment_covers_wrapping_order_and_blank_paragraphs() {
    let files = render(
        r##"openapi: 3.0.3
info: { title: Docs, version: 1.0.0 }
servers:
  - url: /api/v1
    description: Stable API
paths:
  /widgets/{second}/{first}:
    get:
      operationId: widgets_list
      tags: [Widgets]
      description: |
        Lists widgets.

        Preserves the second paragraph.

      parameters:
        - name: first
          in: path
          required: true
          description: |
            First identifier.
            Continued detail.
          schema: { type: string }
        - name: second
          in: path
          required: true
          description: Second identifier.
          schema: { type: string }
        - name: status
          in: query
          description: |
            Status filter.
            May be repeated.
          schema:
            type: array
            items: { $ref: "#/components/schemas/WidgetStatus" }
      responses:
        '200':
          description: Matching widgets.
          content:
            application/json:
              schema:
                type: array
                items: { $ref: "#/components/schemas/Widget" }
components:
  schemas:
    WidgetStatus: { type: string, enum: [ACTIVE, DISABLED] }
    Widget:
      type: object
      required: [id]
      properties: { id: { type: string } }
"##,
    );
    let raw = &files["src/acme/widgets/raw_client.py"];
    let second = raw.find("second: str").unwrap();
    let first = raw.find("first: str").unwrap();
    assert!(
        second < first,
        "path arguments follow URL placeholder order: {raw}"
    );
    assert!(
        raw.contains("            First identifier.\n            Continued detail."),
        "{raw}"
    );
    assert!(
        raw.contains("            Status filter.\n            May be repeated."),
        "{raw}"
    );
    assert!(
        raw.contains("typing.Union[WidgetStatus, typing.Sequence[WidgetStatus]]"),
        "{raw}"
    );
    let reference = &files["reference.md"];
    assert!(
        reference.contains("Lists widgets.\n\nPreserves the second paragraph."),
        "{reference}"
    );
    assert!(
        reference.contains("typing.Sequence[WidgetStatus]"),
        "{reference}"
    );
    assert!(
        reference.contains("First identifier.\nContinued detail."),
        "{reference}"
    );
    let environment = &files["src/acme/environment.py"];
    assert!(
        environment.contains("DEFAULT = \"/api/v1\""),
        "{environment}"
    );
    assert!(files["src/acme/client.py"].contains("AcmeApiEnvironment.DEFAULT"));
}

/// The five parameter-style corpus rows (114-118) each pinned a rule about bytes
/// a caller sees; these drive the same shapes through the real generator.
#[test]
fn a_number_schema_with_an_integer_format_is_a_python_int() {
    let files = render(
        r##"openapi: 3.0.3
info: { title: Counts, version: 1.0.0 }
paths:
  /widgets:
    get:
      operationId: widgets_list
      tags: [Widgets]
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema: { $ref: "#/components/schemas/Counts" }
components:
  schemas:
    Counts:
      type: object
      required: [id]
      properties:
        id: { type: number, format: int32 }
        big: { type: number, format: int64 }
        ratio: { type: number, format: float }
        plain: { type: number }
"##,
    );
    let model = &files["src/acme/types/counts.py"];
    assert!(model.contains("id: int"), "{model}");
    assert!(
        model.contains("big: typing.Optional[int] = None"),
        "{model}"
    );
    assert!(
        model.contains("ratio: typing.Optional[float] = None"),
        "{model}"
    );
    assert!(
        model.contains("plain: typing.Optional[float] = None"),
        "{model}"
    );
}

#[test]
fn an_apostrophe_in_an_enum_value_is_a_contraction_not_a_word_boundary() {
    let files = render(
        r#"openapi: 3.0.3
info: { title: Sizes, version: 1.0.0 }
paths:
  /widgets:
    get:
      operationId: widgets_list
      tags: [Widgets]
      parameters:
        - name: size
          in: query
          schema: { type: string, enum: ["Don't Know", "Self-employed"] }
      responses: { '204': { description: OK } }
"#,
    );
    let module = &files["src/acme/widgets/types/widgets_list_request_size.py"];
    assert!(module.contains("DONT_KNOW = \"Don't Know\""), "{module}");
    assert!(!module.contains("DON_T_KNOW"), "{module}");
}

#[test]
fn a_path_segment_no_identifier_can_hold_is_folded_before_the_type_context() {
    let files = render(
        r#"openapi: 3.0.3
info: { title: Users, version: 1.0.0 }
paths:
  /users/~:
    patch:
      tags: [Users]
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                company_size: { type: string, enum: [SMALL, LARGE] }
      responses: { '204': { description: Updated } }
"#,
    );
    assert!(
        files.contains_key("src/acme/users/types/patch_users_request_company_size.py"),
        "hoisted module names: {:?}",
        files
            .keys()
            .filter(|k| k.contains("users/types"))
            .collect::<Vec<_>>()
    );
    let raw = &files["src/acme/users/raw_client.py"];
    assert!(raw.contains("\"users/~\""), "{raw}");
}

#[test]
fn a_property_whose_all_of_holds_one_inline_member_is_that_member() {
    let files = render(
        r##"openapi: 3.0.3
info: { title: Wrapped, version: 1.0.0 }
paths:
  /widgets:
    get:
      operationId: widgets_list
      tags: [Widgets]
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    allOf:
                      - type: array
                        items: { $ref: "#/components/schemas/Widget" }
components:
  schemas:
    Widget:
      type: object
      properties: { name: { type: string } }
"##,
    );
    let model = &files["src/acme/widgets/types/widgets_list_response.py"];
    assert!(
        model.contains("data: typing.Optional[typing.List[Widget]] = None"),
        "{model}"
    );
    assert!(
        !files
            .keys()
            .any(|name| name.ends_with("widgets_list_response_data.py")),
        "a one-member allOf coined a wrapper model: {:?}",
        files.keys().collect::<Vec<_>>()
    );
}

#[test]
fn an_authorization_parameter_stays_per_method_and_content_type_is_dropped() {
    let files = render(
        r#"openapi: 3.0.3
info: { title: Gateway, version: 1.0.0 }
paths:
  /alpha:
    post:
      operationId: alpha_run
      tags: [Alpha]
      parameters:
        - { name: Authorization, in: header, required: true, schema: { type: string } }
        - { name: Content-Type, in: header, required: true, schema: { type: string } }
      responses: { '204': { description: OK } }
  /beta:
    post:
      operationId: beta_run
      tags: [Beta]
      parameters:
        - { name: Authorization, in: header, required: true, schema: { type: string } }
      responses: { '204': { description: OK } }
"#,
    );
    let wrapper = &files["src/acme/core/client_wrapper.py"];
    assert!(!wrapper.contains("authorization"), "{wrapper}");
    let raw = &files["src/acme/alpha/raw_client.py"];
    assert!(raw.contains("authorization: str"), "{raw}");
    assert!(!raw.contains("content_type"), "{raw}");
}

#[test]
fn a_description_keeps_its_trailing_carriage_return_in_the_markdown_writers() {
    let files = render(
        "openapi: 3.0.3\ninfo: { title: Notes, version: 1.0.0 }\npaths:\n  /notes:\n    get:\n      operationId: notes_list\n      tags: [Notes]\n      description: \"Reads the notes.\\r\\n\"\n      responses: { '204': { description: OK } }\n",
    );
    let reference = &files["reference.md"];
    assert!(reference.contains("Reads the notes.\r\n"), "{reference:?}");
}

#[test]
fn an_http_scheme_no_requirement_selects_leaves_the_client_unauthenticated() {
    let unreferenced = render(
        r#"openapi: 3.0.3
info: { title: Open, version: 1.0.0 }
paths:
  /widgets:
    get:
      operationId: widgets_list
      tags: [Widgets]
      responses: { '204': { description: OK } }
components:
  securitySchemes:
    basic_auth: { type: http, scheme: basic }
"#,
    );
    let wrapper = &unreferenced["src/acme/core/client_wrapper.py"];
    assert!(!wrapper.contains("BasicAuth"), "{wrapper}");
    assert!(!wrapper.contains("username"), "{wrapper}");

    let requested = render(
        r#"openapi: 3.0.3
info: { title: Closed, version: 1.0.0 }
security: []
paths:
  /widgets:
    get:
      operationId: widgets_list
      tags: [Widgets]
      responses: { '204': { description: OK } }
components:
  securitySchemes:
    basic_auth: { type: http, scheme: basic }
"#,
    );
    let wrapper = &requested["src/acme/core/client_wrapper.py"];
    assert!(
        wrapper.contains("httpx.BasicAuth(username, password)"),
        "{wrapper}"
    );
}

#[test]
fn a_shared_undescribed_request_body_drops_the_explicit_content_type() {
    let files = render(
        r##"openapi: 3.0.3
info: { title: Secrets, version: 1.0.0 }
paths:
  /secrets:
    post:
      operationId: secrets_create
      tags: [Secrets]
      requestBody:
        content:
          application/json:
            schema: { $ref: "#/components/schemas/MutableSecret" }
      responses: { '204': { description: Created } }
  /secrets/replace:
    post:
      operationId: secrets_replace
      tags: [Secrets]
      requestBody:
        content:
          application/json:
            schema: { $ref: "#/components/schemas/MutableSecret" }
      responses: { '204': { description: Replaced } }
  /solo:
    post:
      operationId: solo_create
      tags: [Solo]
      requestBody:
        content:
          application/json:
            schema: { $ref: "#/components/schemas/GrantInfo" }
      responses: { '204': { description: Created } }
components:
  schemas:
    MutableSecret:
      type: object
      required: [name]
      properties:
        name: { type: string, description: The secret name. }
        tenant: { type: string }
    GrantInfo:
      type: object
      required: [grant_account_id]
      properties:
        grant_account_id: { type: string, description: The account. }
        counterparty: { type: string }
"##,
    );
    let shared = &files["src/acme/secrets/raw_client.py"];
    assert!(
        !shared.contains("\"content-type\": \"application/json\""),
        "a body two operations post, described nowhere, drops the header: {shared}"
    );
    let solo = &files["src/acme/solo/raw_client.py"];
    assert!(
        solo.contains("\"content-type\": \"application/json\""),
        "a body one operation posts keeps it: {solo}"
    );
}

#[test]
fn a_union_variants_own_discriminant_enum_reaches_the_worked_example() {
    let files = render(
        r##"openapi: 3.0.3
info: { title: Clients, version: 1.0.0 }
paths:
  /clients:
    post:
      operationId: clients_create
      tags: [Clients]
      requestBody:
        required: true
        content:
          application/json:
            schema: { $ref: "#/components/schemas/MutableAuthClient" }
      responses: { '204': { description: Created } }
  /clients/two-legged:
    get:
      operationId: clients_two_legged
      tags: [Clients]
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema: { $ref: "#/components/schemas/TwoLegged" }
components:
  schemas:
    MutableAuthClient:
      oneOf:
        - $ref: "#/components/schemas/TwoLegged"
        - $ref: "#/components/schemas/ThreeLegged"
      discriminator:
        propertyName: type
        mapping:
          TWO_LEGGED: "#/components/schemas/TwoLegged"
          THREE_LEGGED: "#/components/schemas/ThreeLegged"
    TwoLegged:
      type: object
      required: [name, type, consumer_key]
      properties:
        name: { type: string }
        type: { type: string, enum: [TWO_LEGGED, THREE_LEGGED] }
        consumer_key: { type: string }
    ThreeLegged:
      type: object
      required: [name, type]
      properties:
        name: { type: string }
        type: { type: string, enum: [TWO_LEGGED, THREE_LEGGED] }
"##,
    );
    // The docstring writer puts the tag back in its schema position …
    let client = &files["src/acme/clients/client.py"];
    assert!(
        client.contains(
            "name=\"name\",\n                type=TwoLeggedType.TWO_LEGGED,\n                consumer_key=\"consumer_key\","
        ),
        "{client}"
    );
    // … while the Markdown writers append it after every other argument.
    let reference = &files["reference.md"];
    assert!(
        reference
            .contains("consumer_key=\"consumer_key\",\n        type=TwoLeggedType.TWO_LEGGED,"),
        "{reference}"
    );
}

#[test]
fn a_required_multipart_file_part_is_passed_unconditionally() {
    let files = render(
        r#"openapi: 3.0.3
info: { title: Upload, version: 1.0.0 }
paths:
  /archives:
    post:
      operationId: archives_create
      tags: [Archives]
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              required: [archive_file]
              properties:
                archive_file: { type: string, format: binary }
      responses:
        '204': { description: Created }
"#,
    );
    let raw = &files["src/acme/archives/raw_client.py"];
    assert!(
        raw.contains("files={\n                \"archive_file\": archive_file,"),
        "{raw}"
    );
    assert!(
        !raw.contains("if archive_file is not None else {}"),
        "{raw}"
    );
}

#[test]
fn multiple_api_keys_promote_each_declared_header() {
    let files = render(
        r#"openapi: 3.0.3
info: { title: Keys, version: 1.0.0 }
security:
  - Primary: []
    Secondary: []
    Transport: []
paths:
  /widgets:
    get:
      operationId: widgets_list
      tags: [Widgets]
      responses: { '204': { description: OK } }
components:
  securitySchemes:
    Primary: { type: apiKey, in: header, name: X-Primary-Key }
    Secondary: { type: apiKey, in: header, name: X-Secondary-Key }
    Transport: { type: apiKey, in: header, name: Content-Type }
"#,
    );
    let client = &files["src/acme/client.py"];
    assert!(client.contains("api_key: str"), "{client}");
    assert!(client.contains("secondary_key: str"), "{client}");
    assert!(client.contains("content_type: str"), "{client}");
    let wrapper = &files["src/acme/core/client_wrapper.py"];
    assert!(wrapper.contains("\"X-Primary-Key\""), "{wrapper}");
    assert!(wrapper.contains("\"X-Secondary-Key\""), "{wrapper}");
    assert!(wrapper.contains("\"Content-Type\""), "{wrapper}");
}

#[test]
fn worked_examples_construct_named_models_and_formatted_scalar_values() {
    let files = render(
        r##"openapi: 3.0.3
info: { title: Example Shapes, version: 1.0.0 }
paths:
  /events:
    post:
      operationId: events_create
      tags: [Events]
      requestBody:
        required: true
        content:
          application/json:
            schema: { $ref: "#/components/schemas/CreateEvent" }
      responses: { '204': { description: Created } }
components:
  schemas:
    Location:
      type: object
      required: [city, coordinates]
      properties:
        city: { type: string }
        coordinates:
          type: array
          items: { type: number }
    CreateEvent:
      type: object
      required: [location, starts_at, day, event_id]
      example:
        location: { city: Paris, coordinates: [48.8566, 2.3522] }
        starts_at: '2025-04-03T12:30:00Z'
        day: '2025-04-03'
        event_id: '123e4567-e89b-12d3-a456-426614174000'
      properties:
        location: { $ref: "#/components/schemas/Location" }
        starts_at: { type: string, format: date-time }
        day: { type: string, format: date }
        event_id: { type: string, format: uuid }
"##,
    );
    let client = &files["src/acme/events/client.py"];
    // The body schema's own `example` supplies every field, the object-typed one
    // included: corpus row 110's `GroupUserUpdate` declares a schema-level
    // example whose `accessRights` is an object, and its Fern 5.20.0 golden
    // renders that object's declared values rather than synthesized placeholders.
    assert!(client.contains("location=Location("), "{client}");
    assert!(client.contains("city=\"Paris\""), "{client}");
    assert!(client.contains("coordinates=[48.8566, 2.3522]"), "{client}");
    assert!(
        client.contains("starts_at=datetime.datetime.fromisoformat("),
        "{client}"
    );
    assert!(
        client.contains("day=datetime.date.fromisoformat("),
        "{client}"
    );
    assert!(
        client.contains("event_id=\"123e4567-e89b-12d3-a456-426614174000\""),
        "{client}"
    );
    assert!(
        client.contains("from acme import AcmeApi, Location"),
        "{client}"
    );
}

#[test]
fn in_process_openapi_boundary_reports_each_input_failure() {
    fn error_for(path: PathBuf) -> String {
        crozier::openapi::load(&path).unwrap_err().to_string()
    }

    let dir = tempfile::tempdir().unwrap();
    let missing = error_for(dir.path().join("missing.yml"));
    assert!(missing.contains("could not read spec"), "{missing}");

    let unsupported = dir.path().join("api.txt");
    std::fs::write(&unsupported, "openapi: 3.0.3").unwrap();
    let unsupported_error = error_for(unsupported);
    assert!(
        unsupported_error.contains("unsupported spec extension"),
        "{unsupported_error}"
    );

    let malformed_yaml = dir.path().join("malformed.yml");
    std::fs::write(&malformed_yaml, "openapi: [\n").unwrap();
    let yaml_error = error_for(malformed_yaml);
    assert!(
        yaml_error.contains("could not parse OpenAPI document"),
        "{yaml_error}"
    );

    let malformed_json = dir.path().join("malformed.json");
    std::fs::write(&malformed_json, "{\"openapi\":").unwrap();
    let json_error = error_for(malformed_json);
    assert!(
        json_error.contains("could not parse OpenAPI document"),
        "{json_error}"
    );

    let old = dir.path().join("old.yaml");
    std::fs::write(&old, "openapi: 2.0\ninfo: { title: Old }\npaths: {}\n").unwrap();
    let version_error = error_for(old);
    assert!(
        version_error.contains("unsupported OpenAPI version `2.0`"),
        "{version_error}"
    );
}

#[test]
fn untagged_binary_and_sse_streams_emit_on_root_sync_and_async_clients() {
    let files = render(
        r##"openapi: 3.0.3
info: { title: Root Streams, version: 1.0.0 }
paths:
  /download/{id}:
    get:
      operationId: download
      parameters:
        - { name: id, in: path, required: true, description: File identifier., schema: { type: string } }
      responses:
        '200':
          description: Archive bytes.
          content:
            application/octet-stream:
              schema: { type: string, format: binary }
        '404':
          description: Missing.
          content:
            application/json:
              schema: { $ref: "#/components/schemas/Problem" }
  /events:
    get:
      operationId: events
      responses:
        '200':
          description: Event stream.
          content:
            text/event-stream: {}
components:
  schemas:
    Problem:
      type: object
      properties: { message: { type: string } }
"##,
    );
    let raw = &files["src/acme/raw_client.py"];
    assert!(raw.contains("class RawAcmeApi:"), "{raw}");
    assert!(
        raw.contains("@contextlib.contextmanager\n    def download("),
        "{raw}"
    );
    assert!(
        raw.contains("@contextlib.asynccontextmanager\n    async def download("),
        "{raw}"
    );
    assert!(raw.contains("raise NotFoundError("), "{raw}");
    assert!(
        raw.contains("def events(") && raw.contains("typing.Iterator[typing.Any]"),
        "{raw}"
    );
    assert!(
        raw.contains("async def events(") && raw.contains("typing.AsyncIterator[typing.Any]"),
        "{raw}"
    );
    let client = &files["src/acme/client.py"];
    assert!(
        client.contains("def download(") && client.contains("with self._raw_client.download("),
        "{client}"
    );
    assert!(
        client.contains("async def download(")
            && client.contains("async with self._raw_client.download("),
        "{client}"
    );
    assert!(
        client.contains("def events(")
            && client
                .contains("with self._raw_client.events(request_options=request_options) as r:"),
        "{client}"
    );
    assert!(
        client.contains("async def events(")
            && client.contains(
                "async with self._raw_client.events(request_options=request_options) as r:"
            ),
        "{client}"
    );
    assert!(files["src/acme/__init__.py"].contains("AcmeApi"));
}

#[cfg(unix)]
fn with_fake_ruff(script: &str, run: impl FnOnce()) {
    use std::os::unix::fs::PermissionsExt;
    let dir = tempfile::tempdir().unwrap();
    let ruff = dir.path().join("ruff");
    std::fs::write(&ruff, script).unwrap();
    std::fs::set_permissions(&ruff, std::fs::Permissions::from_mode(0o755)).unwrap();
    let old = std::env::var_os("PATH");
    unsafe { std::env::set_var("PATH", dir.path()) };
    run();
    match old {
        Some(value) => unsafe { std::env::set_var("PATH", value) },
        None => unsafe { std::env::remove_var("PATH") },
    }
}

#[cfg(unix)]
#[test]
fn formatter_reports_missing_permission_and_non_utf8_process_failures() {
    let old = std::env::var_os("PATH");
    unsafe { std::env::set_var("PATH", "") };
    let missing = crozier::pyfmt::format_source("sdk.py", "x = 1\n", 120).unwrap_err();
    assert!(missing.to_string().contains("`ruff` was not found on PATH"));
    match old {
        Some(value) => unsafe { std::env::set_var("PATH", value) },
        None => unsafe { std::env::remove_var("PATH") },
    }

    let dir = tempfile::tempdir().unwrap();
    std::fs::create_dir(dir.path().join("ruff")).unwrap();
    let old = std::env::var_os("PATH");
    unsafe { std::env::set_var("PATH", dir.path()) };
    let denied = crozier::pyfmt::format_source("sdk.py", "x = 1\n", 120).unwrap_err();
    assert!(denied.to_string().contains("could not run `ruff`"));
    match old {
        Some(value) => unsafe { std::env::set_var("PATH", value) },
        None => unsafe { std::env::remove_var("PATH") },
    }

    with_fake_ruff(
        "#!/bin/sh\nwhile IFS= read -r line; do :; done\nprintf '\\377'\n",
        || {
            let invalid = crozier::pyfmt::format_source("sdk.py", "x = 1\n", 120).unwrap_err();
            assert!(invalid
                .to_string()
                .contains("ruff produced non-UTF-8 output"));
        },
    );

    with_fake_ruff(
        "#!/bin/sh\nexec 0<&-\ni=0\nwhile [ \"$i\" -lt 100000 ]; do i=$((i + 1)); done\n",
        || {
            let huge = "x".repeat(1024 * 1024);
            let broken = crozier::pyfmt::format_source("sdk.py", &huge, 120).unwrap_err();
            assert!(broken
                .to_string()
                .contains("could not write source to ruff"));
        },
    );
}

#[test]
fn server_variable_defaults_expand_into_environment_urls() {
    let files = render(
        r#"openapi: 3.0.3
info: { title: Variable Servers, version: 1.0.0 }
servers:
  - url: https://{region}.example.com/{version}
    description: Regional API
    variables:
      region: { default: us-east }
      version: { default: v2 }
  - url: /
paths:
  /health:
    get:
      operationId: health_get
      responses: { '204': { description: Healthy } }
"#,
    );
    let environment = &files["src/acme/environment.py"];
    assert!(
        environment.contains("DEFAULT = \"https://us-east.example.com/v2\""),
        "{environment}"
    );
    let client = &files["src/acme/client.py"];
    assert!(client.contains("AcmeApiEnvironment.DEFAULT"), "{client}");
    assert!(
        client.contains("def _get_base_url(*, base_url: typing.Optional[str] = None, environment:"),
        "{client}"
    );
    assert!(
        client.contains("region : typing.Optional[str]\n        Server URL variable for 'region'. Defaults to 'us-east'.")
            && client.contains("version : typing.Optional[str]\n        Server URL variable for 'version'. Defaults to 'v2'.")
            && client.contains("if region is not None or version is not None:")
            && client.contains("_region = region if region is not None else \"us-east\"")
            && client.contains("_version = version if version is not None else \"v2\"")
            && client.contains(
                "base_url = \"https://{region}.example.com/{version}\".format(region=_region, version=_version)"
            ),
        "all server variables should be documented and resolved together: {client}"
    );
}

#[test]
fn same_request_response_ref_omits_content_type_only_when_unauthenticated() {
    let files = render(
        r##"openapi: 3.0.3
info: { title: Echo, version: 1.0.0 }
paths:
  /public:
    post:
      operationId: public_echo
      tags: [Public]
      security: []
      requestBody:
        content:
          application/json:
            schema: { $ref: "#/components/schemas/Message" }
      responses:
        '200':
          description: Echo
          content:
            application/json:
              schema: { $ref: "#/components/schemas/Message" }
  /private:
    post:
      operationId: private_echo
      tags: [Private]
      security: [ { Bearer: [] } ]
      requestBody:
        content:
          application/json:
            schema: { $ref: "#/components/schemas/Message" }
      responses:
        '200':
          description: Echo
          content:
            application/json:
              schema: { $ref: "#/components/schemas/Message" }
  /basic:
    post:
      operationId: basic_create
      tags: [Basic]
      security: [ { Basic: [] } ]
      requestBody:
        content:
          application/json:
            schema: { $ref: "#/components/schemas/Message" }
      responses: { '204': { description: Created } }
  /basic-described:
    post:
      operationId: basic_described_create
      tags: [BasicDescribed]
      security: [ { Basic: [] } ]
      requestBody:
        description: A documented request.
        content:
          application/json:
            schema: { $ref: "#/components/schemas/Message" }
      responses: { '204': { description: Created } }
components:
  securitySchemes:
    Bearer: { type: http, scheme: bearer }
    Basic: { type: http, scheme: basic }
  schemas:
    Message:
      type: object
      description: An echo message.
      properties: { text: { type: string } }
"##,
    );
    let public = &files["src/acme/public/raw_client.py"];
    assert!(public.contains("json={"), "{public}");
    assert!(
        !public.contains("\"content-type\": \"application/json\""),
        "same-ref public echo omits the redundant header: {public}"
    );
    let private = &files["src/acme/private/raw_client.py"];
    assert!(private.contains("json={"), "{private}");
    assert!(
        private.contains("\"content-type\": \"application/json\""),
        "secured same-ref echo retains the header: {private}"
    );
    assert!(files["src/acme/client.py"]
        .contains("token: typing.Optional[typing.Union[str, typing.Callable[[], str]]]"));
    let basic = &files["src/acme/basic/raw_client.py"];
    assert!(
        !basic.contains("\"content-type\": \"application/json\""),
        "Basic-auth JSON bodies without transport parameters leave the header to httpx: {basic}"
    );
    let basic_described = &files["src/acme/basic_described/raw_client.py"];
    assert!(
        basic_described.contains("\"content-type\": \"application/json\""),
        "documented Basic-auth JSON bodies retain the header: {basic_described}"
    );
}

#[test]
fn in_process_cli_schema_and_init_write_failure_are_actionable() {
    crozier::cli::run_from(["crozier", "schema"]).expect("schema command succeeds in process");

    let dir = tempfile::tempdir().unwrap();
    let output_is_directory = dir.path().join("config-dir");
    std::fs::create_dir(&output_is_directory).unwrap();
    let error = crozier::cli::run_from([
        "crozier",
        "init",
        "--output",
        output_is_directory.to_str().unwrap(),
        "--force",
    ])
    .unwrap_err();
    assert!(error.contains("could not write"), "{error}");
    assert!(error.contains("config-dir"), "{error}");
}

#[test]
fn additional_api_key_headers_filter_primary_invalid_and_transport_schemes() {
    let files = render(
        r#"openapi: 3.0.3
info: { title: Header Filters, version: 1.0.0 }
security:
  - Primary: []
    Secondary: []
components:
  securitySchemes:
    Primary: { type: apiKey, in: header, name: X-Primary }
    QueryKey: { type: apiKey, in: query, name: query_key }
    UserAgent: { type: apiKey, in: header, name: User-Agent }
    Secondary: { type: apiKey, in: header, name: X-Secondary-Key }
paths:
  /items:
    get:
      operationId: getItems
      security: [{ Primary: [], Secondary: [] }]
      responses:
        '204': { description: Empty }
"#,
    );
    let client = &files["src/acme/client.py"];
    assert!(
        client.contains("api_key: str"),
        "the first header api key remains the primary credential: {client}"
    );
    assert!(
        client.contains("secondary_key: str"),
        "a valid later header api key is promoted: {client}"
    );
    for excluded in ["query_key:", "user_agent:", "primary:"] {
        assert!(
            !client.contains(excluded),
            "filtered api-key scheme {excluded} leaked into the constructor: {client}"
        );
    }
    assert!(
        client.contains("secondary_key=secondary_key"),
        "the promoted header is forwarded to the raw client: {client}"
    );
}

#[test]
fn nullable_union_and_closed_object_cover_type_fallback_branches() {
    let files = render(
        r#"openapi: 3.0.3
info: { title: Alias Fallbacks, version: 1.0.0 }
components:
  schemas:
    MaybeScalar:
      nullable: true
      anyOf:
        - { type: string }
        - { type: integer }
    ClosedMap:
      type: object
      additionalProperties: false
"#,
    );
    let maybe = &files["src/acme/types/maybe_scalar.py"];
    assert!(
        maybe.contains("MaybeScalar = typing.Union[str, typing.Optional[int]]"),
        "nullable unions apply Optional to Fern's final variant: {maybe}"
    );
    let closed = &files["src/acme/types/closed_map.py"];
    assert!(
        closed.contains("class ClosedMap(UniversalBaseModel):"),
        "{closed}"
    );
    assert!(closed.contains("extra=\"allow\""), "{closed}");
}

#[test]
fn unknown_alias_variants_collapse_to_any() {
    let files = render(
        r#"openapi: 3.1.0
info: { title: Unknown Aliases, version: 1.0.0 }
components:
  schemas:
    NullOnly:
      type: ['null']
    NullableUnknown:
      nullable: true
"#,
    );
    for (name, alias) in [
        ("null_only", "NullOnly = typing.Any"),
        ("nullable_unknown", "NullableUnknown = typing.Any"),
    ] {
        let path = format!("src/acme/types/{name}.py");
        let module = &files[&path];
        assert!(
            module.contains(alias),
            "{name} must use the Fern 5.20 unknown fallback: {module}"
        );
    }
}

#[test]
fn response_modes_cover_head_text_bodyless_and_default_fallbacks() {
    let files = render(
        r##"openapi: 3.0.3
info: { title: Response Modes, version: 1.0.0 }
paths:
  /headers:
    head:
      summary: Inspect headers
      tags: [Probes]
      responses: { '200': { description: Headers } }
  /text:
    get:
      operationId: probes_getText
      tags: [Probes]
      responses:
        '200':
          description: Plain text
          content: { text/plain: { schema: { type: string } } }
  /maybe:
    post:
      operationId: probes_maybe
      tags: [Probes]
      responses:
        '200':
          description: Value
          content: { application/json: { schema: { type: string } } }
        '204': { description: Empty }
  /fallback:
    post:
      operationId: probes_fallback
      tags: [Probes]
      responses:
        default:
          description: JWT fallback
          content: { application/jwt: { schema: { type: string } } }
"##,
    );
    let raw = &files["src/acme/probes/raw_client.py"];
    let client = &files["src/acme/probes/client.py"];
    assert!(raw.contains("def inspect_headers("), "{raw}");
    assert!(client.contains(") -> typing.Dict[str, str]:"), "{client}");
    assert!(client.contains("return _response.headers"), "{client}");
    assert!(raw.contains("data=_response.text"), "{raw}");
    assert!(
        raw.contains("if _response is None or not _response.text.strip():"),
        "{raw}"
    );
    assert!(raw.contains("typing.Optional[str]"), "{raw}");
    assert!(raw.contains("def fallback("), "{raw}");
}

#[test]
fn off_string_parameter_examples_are_discarded_and_serialization_styles_survive() {
    let files = render(
        r##"openapi: 3.0.3
info: { title: Parameter Examples, version: 1.0.0 }
paths:
  /search/{ids}:
    get:
      operationId: search_run
      tags: [Search]
      parameters:
        - { name: ids, in: path, required: true, schema: { type: array, items: { type: string } } }
        - name: page
          in: query
          required: true
          example: 0
          schema: { type: integer, minimum: 0 }
        - name: ratio
          in: query
          required: true
          examples: { common: { value: 2 } }
          schema: { type: number }
        - name: filters
          in: query
          style: deepObject
          explode: true
          schema: { type: object, additionalProperties: true }
        - name: labels
          in: query
          style: spaceDelimited
          explode: false
          schema: { type: array, items: { type: string } }
        - name: term
          in: query
          explode: false
          schema: { type: string }
        - name: X-Limit
          in: header
          required: true
          example: 7
          schema: { type: integer }
      responses: { '204': { description: Done } }
"##,
    );
    let raw = &files["src/acme/search/raw_client.py"];
    let client = &files["src/acme/search/client.py"];
    assert!(raw.contains("page: int"), "{raw}");
    assert!(raw.contains("ratio: float"), "{raw}");
    assert!(
        raw.contains("filters: typing.Optional[typing.Dict"),
        "{raw}"
    );
    assert!(raw.contains("\"filters\": filters"), "{raw}");
    assert!(raw.contains("\"labels\": labels"), "{raw}");
    assert!(raw.contains("\"term\": term"), "{raw}");
    assert!(
        !raw.contains("join(map(str, labels))") && !raw.contains("join(map(str, term))"),
        "only form-style arrays use comma serialization: {raw}"
    );
    assert!(client.contains("ids=\"ids\""), "{client}");
    // Every example here is declared on the *parameter* rather than its schema, and
    // no parameter is `type: string` — Fern 5.20.0 discards a parameter-level example
    // in that case and synthesizes the required argument instead, identically for
    // query, header and path parameters (probed directly against the generator). A
    // schema-level example on the same parameter is used verbatim, whatever its type.
    assert!(client.contains("page=1"), "{client}");
    assert!(client.contains("ratio=1.1"), "{client}");
    assert!(client.contains("limit=1"), "{client}");
}

#[test]
fn unsupported_query_styles_are_discarded_before_standard_serialization() {
    let spec = |style: &str| {
        format!(
            r#"openapi: 3.0.3
info: {{ title: Query Style, version: 1.0.0 }}
paths:
  /search:
    get:
      operationId: search_run
      tags: [Search]
      parameters:
        - name: value
          in: query
          {style}
          schema: {{ type: object, additionalProperties: true }}
      responses: {{ '204': {{ description: Done }} }}
"#
        )
    };
    let unstyled = render(&spec(""));
    let deep_object = render(&spec("style: deepObject\n          explode: true"));
    let space_delimited = render(&spec("style: spaceDelimited"));
    let path = "src/acme/search/raw_client.py";
    assert_eq!(deep_object[path], unstyled[path]);
    assert_eq!(space_delimited[path], unstyled[path]);
    assert!(unstyled[path].contains("value: typing.Optional[typing.Dict"));
    assert!(unstyled[path].contains("params={\n                \"value\": value,"));
}

#[test]
fn integer_formats_drive_distinct_synthesized_examples() {
    let files = render(
        r#"openapi: 3.0.3
info: { title: Integer Formats, version: 1.0.0 }
paths:
  /numbers:
    get:
      operationId: numbers_get
      tags: [Numbers]
      parameters:
        - { name: regular, in: query, required: true, schema: { type: integer } }
        - { name: unsigned, in: query, required: true, schema: { type: integer, format: uint32 } }
        - { name: long_value, in: query, required: true, schema: { type: integer, format: int64 } }
      responses: { '204': { description: Done } }
"#,
    );
    let client = &files["src/acme/numbers/client.py"];
    assert!(client.contains("regular=1"), "{client}");
    assert!(client.contains("unsigned=1"), "{client}");
    assert!(client.contains("long_value=1000000"), "{client}");
}

#[test]
fn anonymous_request_metadata_and_schema_examples_drive_fern_shapes() {
    let files = render(
        r##"openapi: 3.0.3
info: { title: Request Ownership, version: 1.0.0 }
components:
  securitySchemes:
    Bearer: { type: http, scheme: bearer }
  schemas:
    Configuration:
      example: { user: charles }
    SchemaDocument:
      type: object
      description: Describes arbitrary fields.
      example: { user: { type: string } }
    SharedRequest:
      type: object
      properties:
        configuration: { $ref: '#/components/schemas/Configuration' }
        workspaceId: { type: string }
      required: [configuration, workspaceId]
    Echo:
      type: object
      properties: { text: { type: string } }
paths:
  /one:
    post:
      operationId: jobs_one
      tags: [Jobs]
      requestBody:
        content: { application/json: { schema: { $ref: '#/components/schemas/SharedRequest' } } }
      responses: { '204': { description: Done } }
  /two:
    post:
      operationId: jobs_two
      tags: [Jobs]
      requestBody:
        content: { application/json: { schema: { $ref: '#/components/schemas/SharedRequest' } } }
      responses: { '204': { description: Done } }
  /private-echo:
    post:
      operationId: jobs_privateEcho
      tags: [Jobs]
      security: [ { Bearer: [] } ]
      requestBody:
        content: { application/json: { schema: { $ref: '#/components/schemas/Echo' } } }
      responses:
        '200':
          description: Echo
          content: { application/json: { schema: { $ref: '#/components/schemas/Echo' } } }
"##,
    );
    let raw = &files["src/acme/jobs/raw_client.py"];
    let client = &files["src/acme/jobs/client.py"];
    assert!(files["src/acme/types/schema_document.py"].contains("typing.Dict[str, typing.Any]"));
    assert!(
        client.contains("configuration={\"user\": \"charles\"}"),
        "{client}"
    );
    assert_eq!(
        raw.matches("\"content-type\": \"application/json\"")
            .count(),
        2,
        "{raw}"
    );
    let private = raw
        .split("def privateecho(")
        .nth(1)
        .expect("private method");
    assert!(
        private.contains("\"content-type\": \"application/json\""),
        "{private}"
    );
}

#[test]
fn reusable_request_examples_and_date_queries_keep_fern_semantics() {
    let files = render(
        r##"openapi: 3.1.0
info: { title: Museum, version: 1.0.0 }
paths:
  /events:
    get:
      operationId: events_list
      tags: [Events]
      parameters:
        - name: startDate
          in: query
          schema: { type: string, format: date, example: '2024-02-03' }
        - name: page
          in: query
          schema: { type: integer, example: 2 }
        - name: limit
          in: query
          schema: { type: integer, example: 15 }
        - name: updatedAfter
          in: query
          schema: { type: string, format: date-time }
      responses: { '204': { description: Found } }
    post:
      operationId: events_create
      tags: [Events]
      requestBody:
        required: true
        content:
          application/json:
            schema: { $ref: '#/components/schemas/CreateEvent' }
            examples:
              primary: { $ref: '#/components/examples/PrimaryEvent' }
              alternate: { $ref: '#/components/examples/AlternateEvent' }
      responses: { '204': { description: Created } }
components:
  schemas:
    Date: { type: string, format: date }
    Dates: { type: array, items: { $ref: '#/components/schemas/Date' } }
    Price: { type: number, format: float }
    BaseEvent:
      type: object
      required: [dates, price]
      properties:
        dates: { $ref: '#/components/schemas/Dates' }
        price: { $ref: '#/components/schemas/Price' }
    CreateEvent:
      allOf:
        - { $ref: '#/components/schemas/BaseEvent' }
        - type: object
          properties:
            note: { type: string }
            code: { type: string }
  examples:
    PrimaryEvent:
      value:
        dates: ['2024-02-03', '2024-02-03', '2024-02-04']
        price: 0
        note: Primary
    AlternateEvent:
      value:
        dates: ['2024-03-05']
        price: 15
        code: ALT-1
        note: Alternate
"##,
    );

    let client = &files["src/acme/events/client.py"];
    let raw = &files["src/acme/events/raw_client.py"];
    let reference = &files["reference.md"];
    assert_eq!(client.matches("\"2024-02-03\"").count(), 4, "{client}");
    assert!(
        client.contains("price=0.0") && client.contains("note=\"Primary\""),
        "{client}"
    );
    assert!(
        client.contains("start_date=datetime.date.fromisoformat(")
            && client.contains("page=2")
            && client.contains("limit=15"),
        "{client}"
    );
    assert!(
        raw.contains("\"startDate\": str(start_date) if start_date is not None else None,")
            && raw.contains(
                "\"updatedAfter\": serialize_datetime(updated_after) if updated_after is not None else None,"
            )
            && raw.matches("\"content-type\": \"application/json\"").count() == 2,
        "{raw}"
    );
    assert!(
        reference.contains("price=0") && reference.contains("note=\"Primary\""),
        "{reference}"
    );
    assert!(!reference.contains("code=\"ALT-1\""), "{reference}");
}

#[test]
fn single_use_request_components_move_their_synthetic_type_graph_to_the_tag() {
    let files = render(
        r##"openapi: 3.0.3
info: { title: Request Graph, version: 1.0.0 }
paths:
  /imports:
    post:
      operationId: imports_create
      tags: [Imports]
      requestBody:
        required: true
        content: { application/json: { schema: { $ref: '#/components/schemas/ImportRequest' } } }
      responses: { '204': { description: Imported } }
components:
  schemas:
    ImportRequest:
      type: object
      required: [settings, choice, modes]
      properties:
        settings:
          type: object
          required: [credentials]
          properties:
            credentials:
              type: object
              required: [token]
              properties: { token: { type: string } }
        choice:
          oneOf:
            - type: object
              required: [name]
              properties: { name: { type: string } }
            - type: object
              required: [count]
              properties: { count: { type: integer } }
        modes:
          type: array
          items: { type: string, enum: [fast, safe] }
"##,
    );
    let type_paths: Vec<&str> = files
        .keys()
        .map(String::as_str)
        .filter(|path| path.starts_with("src/acme/imports/types/"))
        .collect();
    assert!(type_paths.len() >= 4, "{type_paths:#?}");
    assert!(!files.contains_key("src/acme/types/import_request.py"));
    let raw = &files["src/acme/imports/raw_client.py"];
    assert!(raw.contains("settings: ImportRequestSettings"), "{raw}");
    assert!(raw.contains("choice: ImportRequestChoice"), "{raw}");
    assert!(
        raw.contains("modes: typing.Sequence[ImportRequestModesItem]"),
        "{raw}"
    );
}

#[test]
fn no_argument_binary_download_omits_method_examples_but_stays_in_reference() {
    let files = render(
        r##"openapi: 3.0.3
info: { title: Binary Probe, version: 1.0.0 }
paths:
  /archive:
    get:
      operationId: archives_download
      tags: [Archives]
      responses:
        '200':
          description: Zip archive
          content: { application/zip: { schema: { type: string, format: binary } } }
"##,
    );
    let raw = &files["src/acme/archives/raw_client.py"];
    let client = &files["src/acme/archives/client.py"];
    assert!(
        raw.contains("typing.Iterator[HttpResponse[typing.Iterator[bytes]]]"),
        "{raw}"
    );
    assert!(!raw.contains("parse_obj_as"), "{raw}");
    assert!(!client.contains("Examples\n"), "{client}");
    let reference = &files["reference.md"];
    assert!(reference.contains("## Archives"), "{reference}");
    assert!(reference.contains("download</a>()"), "{reference}");
    assert!(
        reference.contains("client.archives.download()"),
        "{reference}"
    );
}

#[test]
fn indexed_allof_and_recursive_composition_emit_models_with_forward_refs() {
    let files = render(
        r##"openapi: 3.0.3
info: { title: Indexed Composition, version: 1.0.0 }
components:
  schemas:
    Base:
      type: object
      required: [id]
      properties: { id: { type: string } }
    Combined:
      allOf:
        '3':
          type: object
          required: [count]
          properties: { count: { type: integer, format: uint32 } }
        '1': { $ref: '#/components/schemas/Base' }
    Recursive:
      allOf:
        - type: object
          properties:
            next: { $ref: '#/components/schemas/Recursive' }
paths:
  /combined:
    get:
      operationId: models_combined
      tags: [Models]
      responses:
        '200':
          description: Combined
          content: { application/json: { schema: { $ref: '#/components/schemas/Combined' } } }
  /recursive:
    get:
      operationId: models_recursive
      tags: [Models]
      responses:
        '200':
          description: Recursive
          content: { application/json: { schema: { $ref: '#/components/schemas/Recursive' } } }
"##,
    );
    let combined = &files["src/acme/types/combined.py"];
    let recursive = &files["src/acme/types/recursive.py"];
    assert!(combined.contains("class Combined(Base):"), "{combined}");
    assert!(combined.contains("count: int"), "{combined}");
    assert!(
        recursive.contains("from __future__ import annotations"),
        "{recursive}"
    );
    assert!(
        recursive.contains("next: typing.Optional[\"Recursive\"]"),
        "{recursive}"
    );
}

#[test]
fn inline_oneof_and_anyof_request_bodies_emit_tag_union_inputs() {
    let files = render(
        r##"openapi: 3.0.3
info: { title: Inline Request Unions, version: 1.0.0 }
paths:
  /one:
    post:
      operationId: unions_one
      tags: [Unions]
      requestBody:
        content:
          application/json:
            schema:
              oneOf:
                - { type: string }
                - { type: integer, format: int64 }
      responses: { '204': { description: Done } }
  /any/{id}:
    post:
      operationId: unions_any
      tags: [Unions]
      parameters:
        - { name: id, in: path, required: true, schema: { type: string } }
      requestBody:
        content:
          application/json:
            schema:
              anyOf:
                - { type: boolean }
                - { type: object, additionalProperties: true }
      responses: { '204': { description: Done } }
"##,
    );
    let raw = &files["src/acme/unions/raw_client.py"];
    let one = &files["src/acme/unions/types/unions_one_request.py"];
    let any = &files["src/acme/unions/types/unions_any_request_body.py"];
    assert!(one.contains("typing.Union[str, int]"), "{one}");
    assert!(any.contains("typing.Union[bool, typing.Dict"), "{any}");
    assert!(raw.contains("request: UnionsOneRequest"), "{raw}");
    assert!(raw.contains("request: UnionsAnyRequestBody"), "{raw}");
    assert!(
        raw.contains("object_=request, annotation=UnionsOneRequest"),
        "{raw}"
    );
}

#[test]
fn keyword_methods_jwt_and_wildcard_media_generate_valid_python() {
    let files = render(
        r##"openapi: 3.0.3
info: { title: Media Keywords, version: 1.0.0 }
paths:
  /tokens:
    post:
      operationId: del
      tags: [Tokens]
      requestBody:
        content: { application/jwt: { schema: { type: string } } }
      responses:
        '200':
          description: JWT
          content: { application/jwt: { schema: { type: string } } }
        '400':
          description: Invalid JWT
          content: { application/jwt: { schema: { type: string } } }
  /wild:
    post:
      operationId: tokens_wild
      tags: [Tokens]
      requestBody:
        content:
          '*/*': { schema: { type: object, additionalProperties: true } }
      responses:
        '200':
          description: Wildcard
          content: { '*/*': { schema: { type: integer, format: uint32 } } }
"##,
    );
    let raw = &files["src/acme/tokens/raw_client.py"];
    let client = &files["src/acme/tokens/client.py"];
    assert!(raw.contains("def del_("), "{raw}");
    assert!(client.contains("def del_("), "{client}");
    let del_method = raw.split("def del_(").nth(1).expect("del_ raw method");
    assert!(
        del_method.contains("self, *, request_options")
            && del_method.contains(") -> HttpResponse[None]:"),
        "{del_method}"
    );
    assert!(
        del_method.contains("if _response.status_code == 400:")
            && del_method.contains("raise BadRequestError(")
            && del_method.contains("type_=str,"),
        "{del_method}"
    );
    let wild_method = raw.split("def wild(").nth(1).expect("wild raw method");
    assert!(
        wild_method.contains("request: typing.Dict[str, typing.Any]"),
        "{wild_method}"
    );
    assert!(wild_method.contains("json=request"), "{wild_method}");
    assert!(
        !wild_method.contains("\"content-type\": \"*/*\""),
        "{wild_method}"
    );
    assert!(
        wild_method.contains(") -> HttpResponse[int]:") && wild_method.contains("type_=int,"),
        "{wild_method}"
    );
}

#[test]
fn ndjson_request_bodies_use_the_json_compatible_request_path() {
    let files = render(
        r#"openapi: 3.0.3
info: { title: NDJSON, version: 1.0.0 }
paths:
  /bulk:
    post:
      operationId: records_create_bulk
      tags: [Records]
      requestBody:
        content:
          application/ndjson:
            schema:
              $ref: '#/components/schemas/Record'
      responses: { '204': { description: Done } }
  /vendor:
    post:
      operationId: records_create_vendor
      tags: [Records]
      requestBody:
        content:
          application/vnd.acme+json:
            schema:
              type: object
              properties:
                name: { type: string }
      responses: { '204': { description: Done } }
components:
  schemas:
    Record:
      type: object
      properties:
        name: { type: string }
"#,
    );
    let raw = &files["src/acme/records/raw_client.py"];
    assert!(raw.contains("name: typing.Optional[str] = OMIT"), "{raw}");
    assert!(
        raw.contains("json={\n                \"name\": name,"),
        "{raw}"
    );
    assert!(
        raw.contains("\"content-type\": \"application/ndjson\""),
        "{raw}"
    );
    assert!(
        !raw.contains("\"content-type\": \"application/vnd.acme+json\""),
        "{raw}"
    );
}

#[test]
fn standard_json_request_media_wins_over_earlier_ndjson() {
    let files = render(
        r#"openapi: 3.0.3
info: { title: Mixed JSON Media, version: 1.0.0 }
paths:
  /records:
    post:
      operationId: records_create
      tags: [Records]
      requestBody:
        required: true
        content:
          application/ndjson:
            schema:
              type: object
              required: [ndjson_value]
              properties:
                ndjson_value: { type: integer }
          application/json:
            schema:
              type: object
              required: [json_value]
              properties:
                json_value: { type: string }
      responses: { '204': { description: Done } }
"#,
    );
    let raw = &files["src/acme/records/raw_client.py"];
    assert!(raw.contains("json_value: str"), "{raw}");
    assert!(
        raw.contains("json={\n                \"json_value\": json_value,"),
        "{raw}"
    );
    assert!(!raw.contains("ndjson_value"), "{raw}");
    assert!(
        raw.contains("\"content-type\": \"application/json\""),
        "{raw}"
    );
    assert!(!raw.contains("application/ndjson"), "{raw}");
}

#[test]
fn array_item_examples_seed_generated_calls() {
    let files = render(
        r#"openapi: 3.0.3
info: { title: Item Examples, version: 1.0.0 }
paths:
  /config:
    put:
      operationId: config_update
      tags: [Config]
      requestBody:
        content:
          application/json:
            schema: { $ref: '#/components/schemas/Config' }
      responses: { '204': { description: Done } }
components:
  schemas:
    Config:
      type: object
      required: [emails]
      properties:
        emails:
          type: array
          items: { type: string, example: admin@example.com }
"#,
    );
    let client = &files["src/acme/config/client.py"];
    assert!(
        client.contains("emails=[\"admin@example.com\"]"),
        "{client}"
    );
}

#[test]
fn missing_operation_id_uses_summary_for_method_name() {
    let files = render(
        r#"openapi: 3.0.3
info: { title: Summary Naming, version: 1.0.0 }
paths:
  /things/{id}:
    get:
      summary: Fetch Thing
      tags: [Things]
      parameters:
        - { name: id, in: path, required: true, schema: { type: string } }
      responses: { '204': { description: Done } }
"#,
    );
    let raw = &files["src/acme/things/raw_client.py"];
    let client = &files["src/acme/things/client.py"];
    assert!(raw.contains("def fetch_thing("), "{raw}");
    assert!(client.contains("def fetch_thing("), "{client}");
}

#[test]
fn readme_keeps_bodyless_dictionary_get_simple() {
    let files = render(
        r#"openapi: 3.0.3
info: { title: Dictionary Readme, version: 1.0.0 }
paths:
  /settings:
    get:
      operationId: settings
      responses:
        '200':
          description: Settings
          content:
            application/json:
              schema: { type: object, additionalProperties: true }
"#,
    );
    let readme = &files["README.md"];
    assert!(readme.matches("client.settings()").count() >= 2, "{readme}");
}

#[test]
fn response_path_refs_resolve_escaped_nested_schema_pointers() {
    let files = render(
        r##"openapi: 3.0.3
info: { title: Path Response Refs, version: 1.0.0 }
paths:
  /source/~data:
    get:
      operationId: sources_get
      tags: [Sources]
      responses:
        '200':
          description: Source shapes
          content:
            application/vnd.test+json:
              schema:
                type: object
                properties:
                  scalar/name~: { type: string }
                  nested:
                    type: object
                    properties:
                      code: { type: integer }
                  list:
                    type: array
                    items: { type: boolean }
                  map:
                    type: object
                    additionalProperties: { type: number }
                  choice:
                    oneOf:
                      - { type: string }
                      - { type: integer }
                  alternate:
                    anyOf:
                      - { type: boolean }
                      - { type: string }
                  combined:
                    allOf:
                      - type: object
                        properties:
                          id: { type: string }
  /consumer:
    get:
      operationId: consumers_get
      tags: [Consumers]
      responses:
        '200':
          description: Resolved shapes
          content:
            application/json:
              schema:
                type: object
                properties:
                  direct:
                    $ref: '#/paths/~1source~1~0data/get/responses/200/content/application~1vnd.test+json/schema/properties/scalar~1name~0'
                  nested:
                    type: object
                    properties:
                      code_ref:
                        $ref: '#/paths/~1source~1~0data/get/responses/200/content/application~1vnd.test+json/schema/properties/nested/properties/code'
                  list_refs:
                    type: array
                    items:
                      $ref: '#/paths/~1source~1~0data/get/responses/200/content/application~1vnd.test+json/schema/properties/list/items'
                  map_refs:
                    type: object
                    additionalProperties:
                      $ref: '#/paths/~1source~1~0data/get/responses/200/content/application~1vnd.test+json/schema/properties/map/additionalProperties'
                  choice_ref:
                    oneOf:
                      - $ref: '#/paths/~1source~1~0data/get/responses/200/content/application~1vnd.test+json/schema/properties/choice/oneOf/0'
                      - $ref: '#/paths/~1source~1~0data/get/responses/200/content/application~1vnd.test+json/schema/properties/choice/oneOf/1'
                  alternate_ref:
                    anyOf:
                      - $ref: '#/paths/~1source~1~0data/get/responses/200/content/application~1vnd.test+json/schema/properties/alternate/anyOf/0'
                      - $ref: '#/paths/~1source~1~0data/get/responses/200/content/application~1vnd.test+json/schema/properties/alternate/anyOf/1'
                  combined_ref:
                    allOf:
                      - $ref: '#/paths/~1source~1~0data/get/responses/200/content/application~1vnd.test+json/schema/properties/combined/allOf/0'
"##,
    );
    let rendered = files
        .values()
        .map(String::as_str)
        .collect::<Vec<_>>()
        .join("\n");
    assert!(
        rendered.contains("direct: typing.Optional[str]"),
        "{rendered}"
    );
    assert!(
        rendered.contains("code_ref: typing.Optional[int]"),
        "{rendered}"
    );
    assert!(
        rendered.contains("list_refs: typing.Optional[typing.List[bool]]"),
        "{rendered}"
    );
    assert!(
        rendered.contains("map_refs: typing.Optional[typing.Dict[str, float]]"),
        "{rendered}"
    );
    assert!(rendered.contains("typing.Union[str, int]"), "{rendered}");
    assert!(rendered.contains("typing.Union[bool, str]"), "{rendered}");
    assert!(rendered.contains("id: typing.Optional[str]"), "{rendered}");
}

#[test]
fn explicit_empty_properties_and_omitted_properties_have_distinct_request_shapes() {
    let files = render(
        r#"openapi: 3.0.3
info: { title: Empty Objects, version: 1.0.0 }
paths:
  /closed:
    post:
      operationId: bodies_closed
      tags: [Bodies]
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties: {}
      responses: { '204': { description: Done } }
  /open:
    post:
      operationId: bodies_open
      tags: [Bodies]
      requestBody:
        content:
          application/json:
            schema:
              type: object
      responses: { '204': { description: Done } }
"#,
    );
    let raw = &files["src/acme/bodies/raw_client.py"];
    let closed_start = raw.find("def closed(").expect("closed method");
    let open_start = raw.find("def open(").expect("open method");
    let closed = &raw[closed_start..open_start];
    assert!(!closed.contains("request:"), "{closed}");
    assert!(
        raw[open_start..].contains("request: typing.Dict[str, typing.Any]"),
        "{raw}"
    );
}

#[test]
fn default_package_name_sanitizes_title_punctuation_in_process() {
    let dir = tempfile::tempdir().expect("tempdir");
    let spec = dir.path().join("api.yml");
    std::fs::write(
        &spec,
        "openapi: 3.0.3\ninfo: { title: 'Airflow API (Stable)', version: 1.0.0 }\npaths: {}\n",
    )
    .unwrap();
    let files = render_files(GenerateArgs {
        spec,
        output: PathBuf::from("unused"),
        package_name: None,
        project_name: None,
        client_class_name: None,
        audiences: Vec::new(),
        audience_strict: false,
        extra_fields: crozier::settings::ExtraFields::Allow,
    })
    .expect("render succeeds");
    assert!(files
        .iter()
        .any(|file| file.path.starts_with("src/airflow_api_stable")));
    let pyproject = files
        .iter()
        .find(|file| file.path.as_path() == Path::new("pyproject.toml"))
        .expect("pyproject emitted");
    assert!(
        pyproject.contents.contains("name = \"airflow_api_stable\""),
        "{}",
        pyproject.contents
    );
    let version = files
        .iter()
        .find(|file| file.path.as_path() == Path::new("src/airflow_api_stable/version.py"))
        .expect("version module emitted");
    assert!(
        version
            .contents
            .contains("metadata.version(\"airflow_api_stable\")"),
        "{}",
        version.contents
    );
}

#[test]
fn relative_server_urls_use_the_default_environment_member() {
    let files = render(
        r#"openapi: 3.0.3
info: { title: Relative Server, version: 1.0.0 }
servers:
  - url: api/v1/
    description: Internal route
paths:
  /health:
    get:
      operationId: health_get
      responses: { '204': { description: Healthy } }
"#,
    );
    let environment = &files["src/acme/environment.py"];
    assert!(
        environment.contains("DEFAULT = \"api/v1\""),
        "{environment}"
    );
    let client = &files["src/acme/client.py"];
    assert!(client.contains("AcmeApiEnvironment.DEFAULT"), "{client}");
}

#[test]
fn explicit_empty_operation_id_is_distinct_and_keeps_readme_body_fields() {
    let files = render(
        r#"openapi: 3.0.3
info: { title: Empty Operation Id, version: 1.0.0 }
paths:
  /explicit:
    post:
      operationId: ''
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required: [left, right]
              properties:
                left: { type: string }
                right: { type: string }
      responses: { '204': { description: Done } }
  /widgets:
    get:
      responses: { '204': { description: Done } }
"#,
    );
    let client = &files["src/acme/client.py"];
    assert!(client.contains("def _("), "{client}");
    assert!(client.contains("def get_widgets("), "{client}");
    let readme = &files["README.md"];
    assert!(
        readme.contains("client._(\n    left=\"left\",\n    right=\"right\",\n)"),
        "{readme}"
    );
}

#[test]
fn reference_preserves_a_terminal_description_space() {
    let files = render(
        r#"openapi: 3.0.3
info: { title: Reference Spacing, version: 1.0.0 }
paths:
  /notes:
    get:
      operationId: notes_get
      tags: [Notes]
      description: "Preserve this space "
      responses: { '204': { description: Done } }
"#,
    );
    let reference = &files["reference.md"];
    assert!(
        reference.contains("Preserve this space \n</dd>"),
        "{reference}"
    );
}

#[test]
fn root_client_future_annotations_follow_subclient_presence() {
    let root_only = render(
        r#"openapi: 3.0.3
info: { title: Root Only, version: 1.0.0 }
paths:
  /status:
    get:
      operationId: status
      responses: { '204': { description: Done } }
"#,
    );
    assert!(
        !root_only["src/acme/client.py"].contains("from __future__ import annotations"),
        "{}",
        root_only["src/acme/client.py"]
    );

    let with_subclient = render(
        r#"openapi: 3.0.3
info: { title: With Subclient, version: 1.0.0 }
paths:
  /widgets:
    get:
      operationId: widgets_list
      tags: [Widgets]
      responses: { '204': { description: Done } }
"#,
    );
    assert!(
        with_subclient["src/acme/client.py"].contains("from __future__ import annotations"),
        "{}",
        with_subclient["src/acme/client.py"]
    );
}

/// A component alias over an array of arrays names its leaf element with one
/// `Item` per nesting level, whatever that leaf is — an `anyOf` of `$ref`s
/// (WithSecure's `RequiredAuth`), a discriminated `oneOf`, or an inline object
/// three levels down. A leaf that is itself a plain `$ref` names nothing, so the
/// alias keeps the referenced model inline.
#[test]
fn nested_array_aliases_name_their_leaf_element_once_per_level() {
    let files = render(
        r#"openapi: 3.0.3
info: { title: Nested Arrays, version: 1.0.0 }
paths:
  /grids:
    get:
      operationId: grids_list
      tags: [Grids]
      responses: { '204': { description: Done } }
components:
  schemas:
    Ping:
      type: object
      properties: { id: { type: string } }
    Pong:
      type: object
      properties: { name: { type: string } }
    Started:
      type: object
      required: [kind]
      properties:
        kind: { type: string }
        at: { type: string }
    Stopped:
      type: object
      required: [kind]
      properties:
        kind: { type: string }
        why: { type: string }
    RequiredAuth:
      description: Nested anyOf leaf.
      type: array
      items:
        type: array
        items:
          anyOf:
            - { $ref: '#/components/schemas/Ping' }
            - { $ref: '#/components/schemas/Pong' }
    Matrix:
      type: array
      items:
        type: array
        items:
          type: array
          items:
            type: object
            properties: { cell: { type: string } }
    RefGrid:
      type: array
      items:
        type: array
        items: { $ref: '#/components/schemas/Ping' }
    Timeline:
      type: array
      items:
        type: array
        items:
          oneOf:
            - { $ref: '#/components/schemas/Started' }
            - { $ref: '#/components/schemas/Stopped' }
          discriminator:
            propertyName: kind
            mapping:
              started: '#/components/schemas/Started'
              stopped: '#/components/schemas/Stopped'
"#,
    );

    let required_auth = &files["src/acme/types/required_auth.py"];
    assert!(
        required_auth.contains("RequiredAuth = typing.List[typing.List[RequiredAuthItemItem]]"),
        "{required_auth}"
    );
    assert!(
        files["src/acme/types/required_auth_item_item.py"]
            .contains("RequiredAuthItemItem = typing.Union[Ping, Pong]"),
        "{}",
        files["src/acme/types/required_auth_item_item.py"]
    );

    let matrix = &files["src/acme/types/matrix.py"];
    assert!(
        matrix.contains("Matrix = typing.List[typing.List[typing.List[MatrixItemItemItem]]]"),
        "{matrix}"
    );
    assert!(
        files["src/acme/types/matrix_item_item_item.py"].contains("class MatrixItemItemItem("),
        "{}",
        files["src/acme/types/matrix_item_item_item.py"]
    );

    // A `$ref` leaf already has a name, so nothing is hoisted for it.
    let ref_grid = &files["src/acme/types/ref_grid.py"];
    assert!(
        ref_grid.contains("RefGrid = typing.List[typing.List[Ping]]"),
        "{ref_grid}"
    );
    assert!(!files.contains_key("src/acme/types/ref_grid_item_item.py"));

    let timeline = &files["src/acme/types/timeline.py"];
    assert!(
        timeline.contains("Timeline = typing.List[typing.List[TimelineItemItem]]"),
        "{timeline}"
    );
    let timeline_item = &files["src/acme/types/timeline_item_item.py"];
    assert!(
        timeline_item.contains("class TimelineItemItem_Started(")
            && timeline_item.contains(r#"pydantic.Field(discriminator="kind")"#),
        "{timeline_item}"
    );
}

/// The same one-`Item`-per-level rule applies to an element hoisted out of an
/// operation's inline response, alongside the two other element shapes that
/// path hoists: a multi-member `anyOf` becomes a `{Ctx}Item` union alias, and a
/// nullable inline object element stays `Optional` inside the list.
#[test]
fn hoisted_response_array_elements_nest_and_carry_their_own_optionality() {
    let files = render(
        r#"openapi: 3.0.3
info: { title: Hoisted Items, version: 1.0.0 }
paths:
  /grids:
    get:
      operationId: grids_list
      tags: [Grids]
      responses:
        '200':
          description: Grids
          content:
            application/json:
              schema:
                type: object
                properties:
                  result:
                    type: array
                    items:
                      type: array
                      items:
                        type: object
                        properties:
                          port: { type: integer }
                  mixed:
                    type: array
                    items:
                      anyOf:
                        - { $ref: '#/components/schemas/Ping' }
                        - { type: string }
                  optionals:
                    type: array
                    items:
                      type: object
                      nullable: true
                      properties:
                        note: { type: string }
components:
  schemas:
    Ping:
      type: object
      properties: { id: { type: string } }
"#,
    );

    let response = &files["src/acme/grids/types/grids_list_response.py"];
    assert!(
        response.contains(
            "result: typing.Optional[typing.List[typing.List[GridsListResponseResultItemItem]]]"
        ),
        "{response}"
    );
    assert!(
        response.contains("mixed: typing.Optional[typing.List[GridsListResponseMixedItem]]"),
        "{response}"
    );
    assert!(
        response.contains(
            "optionals: typing.Optional[typing.List[typing.Optional[GridsListResponseOptionalsItem]]]"
        ),
        "{response}"
    );
    assert!(
        files["src/acme/grids/types/grids_list_response_result_item_item.py"]
            .contains("class GridsListResponseResultItemItem("),
        "{}",
        files["src/acme/grids/types/grids_list_response_result_item_item.py"]
    );
    assert!(
        files["src/acme/grids/types/grids_list_response_mixed_item.py"]
            .contains("GridsListResponseMixedItem = typing.Union[Ping, str]"),
        "{}",
        files["src/acme/grids/types/grids_list_response_mixed_item.py"]
    );
}

/// An `allOf: [$ref, { annotation }]` is a use-site copy rather than a subclass,
/// and the copy cascades through array elements: CloudFront's `SignerList` copies
/// its annotated element into `SignerListItem`, and a property that annotates
/// `SignerList` in turn copies the element again under its own name. An annotated
/// `$ref` to a scalar resolves straight to that scalar.
#[test]
fn an_annotated_ref_copies_itself_through_array_elements() {
    let files = render(
        r#"openapi: 3.0.3
info: { title: Annotated Refs, version: 1.0.0 }
paths:
  /distributions:
    get:
      operationId: distributions_get
      tags: [Distributions]
      responses:
        '200':
          description: Distribution
          content:
            application/json:
              schema: { $ref: '#/components/schemas/Distribution' }
components:
  schemas:
    AwsAccountNumber:
      type: string
    Signer:
      type: object
      properties:
        awsAccountNumber:
          allOf:
            - { $ref: '#/components/schemas/AwsAccountNumber' }
            - { description: The account that signs. }
    SignerList:
      type: array
      items:
        allOf:
          - { $ref: '#/components/schemas/Signer' }
          - { xml: { name: Signer } }
    Distribution:
      type: object
      properties:
        signers:
          allOf:
            - { $ref: '#/components/schemas/SignerList' }
            - { description: The trusted signers. }
"#,
    );

    let signer_list = &files["src/acme/types/signer_list.py"];
    assert!(
        signer_list.contains("SignerList = typing.List[SignerListItem]"),
        "{signer_list}"
    );
    assert!(
        files["src/acme/types/signer_list_item.py"].contains("class SignerListItem("),
        "{}",
        files["src/acme/types/signer_list_item.py"]
    );

    let distribution = &files["src/acme/types/distribution.py"];
    assert!(
        distribution.contains("signers: typing.Optional[typing.List[DistributionSignersItem]]"),
        "{distribution}"
    );
    assert!(
        files["src/acme/types/distribution_signers_item.py"]
            .contains("class DistributionSignersItem("),
        "{}",
        files["src/acme/types/distribution_signers_item.py"]
    );

    // The scalar target is copied as the scalar, not as its `String` alias.
    let signer = &files["src/acme/types/signer.py"];
    assert!(
        signer.contains(
            "aws_account_number: typing_extensions.Annotated[\n        typing.Optional[str],"
        ),
        "{signer}"
    );
}

/// A query value that reaches nothing but scalars goes onto the URL as text, so
/// it is passed through without the annotation converter, while a sibling union
/// that can hold a list is converted. The same document pins how a `null`
/// alternative collapses: one surviving member becomes `Optional`, two or more
/// stay an undiscriminated union that carries nullability at its use sites.
#[test]
fn a_scalar_only_query_union_skips_the_annotation_converter() {
    let files = render(
        r#"openapi: 3.1.0
info: { title: Scalar Queries, version: 1.0.0 }
paths:
  /blocks:
    get:
      operationId: blocks_get
      tags: [Blocks]
      parameters:
        - name: block
          in: query
          required: true
          schema: { $ref: '#/components/schemas/BlockId' }
        - name: address
          in: query
          required: true
          schema: { $ref: '#/components/schemas/AddressFilter' }
      responses:
        '200':
          description: Block
          content:
            application/json:
              schema: { $ref: '#/components/schemas/Block' }
components:
  schemas:
    Uint: { type: string }
    Hash32: { type: string }
    Address: { type: string }
    BlockTag:
      type: string
      enum: [earliest, latest, pending]
    Addresses:
      type: array
      items: { $ref: '#/components/schemas/Address' }
    BlockId:
      anyOf:
        - { $ref: '#/components/schemas/Uint' }
        - { $ref: '#/components/schemas/BlockTag' }
        - { $ref: '#/components/schemas/Hash32' }
    AddressFilter:
      anyOf:
        - { $ref: '#/components/schemas/Address' }
        - { $ref: '#/components/schemas/Addresses' }
    FilterTopic:
      anyOf:
        - { $ref: '#/components/schemas/Hash32' }
        - { type: array, items: { $ref: '#/components/schemas/Hash32' } }
        - { type: 'null' }
    MaybeHash:
      anyOf:
        - { $ref: '#/components/schemas/Hash32' }
        - { type: 'null' }
    Block:
      type: object
      properties:
        id: { $ref: '#/components/schemas/BlockId' }
        topic: { $ref: '#/components/schemas/FilterTopic' }
        parent: { $ref: '#/components/schemas/MaybeHash' }
"#,
    );

    let raw = &files["src/acme/blocks/raw_client.py"];
    assert!(raw.contains("\"block\": block,"), "{raw}");
    assert!(
        raw.contains("\"address\": convert_and_respect_annotation_metadata("),
        "{raw}"
    );

    assert!(
        files["src/acme/types/filter_topic.py"]
            .contains("FilterTopic = typing.Union[Hash32, typing.List[Hash32]]"),
        "{}",
        files["src/acme/types/filter_topic.py"]
    );
    assert!(
        files["src/acme/types/maybe_hash.py"].contains("MaybeHash = typing.Optional[Hash32]"),
        "{}",
        files["src/acme/types/maybe_hash.py"]
    );
}

#[test]
fn consent_shapes_drive_the_form_convert_and_documentation_dict_paths() {
    // The shapes the `mosip-esignet` and `openbankingproject-ch-kundenbeziehung`
    // goldens pin, in one operation: a urlencoded field that is a `$ref` to a named
    // model, an enum query parameter whose example names no member, and a body
    // example carrying an empty array, an empty object, and a map wide enough to
    // wrap.
    let files = render(
        r#"openapi: 3.0.1
info: { title: Consent, version: 1.0.0 }
paths:
  /token:
    post:
      operationId: token
      tags: [oidc]
      parameters:
        - in: query
          name: scope
          required: true
          example: openid profile
          schema: { type: string, enum: [openid, profile] }
      requestBody:
        required: true
        content:
          application/x-www-form-urlencoded:
            schema: { $ref: '#/components/schemas/TokenRequest' }
            example:
              grant_type: authorization_code
              claims:
                permittedAuthorizeScopes: []
                userClaims: {}
                labels:
                  aVeryLongLabelKeyThatForcesWrapping: a rather long label value string
                  second: value
      responses:
        '200':
          description: ok
          content: { application/json: { schema: { $ref: '#/components/schemas/Consent' } } }
components:
  schemas:
    UserClaim:
      type: object
      properties:
        essential: { type: boolean }
    Claim:
      type: object
      required: [permittedAuthorizeScopes, labels]
      properties:
        permittedAuthorizeScopes: { type: array, items: { type: string } }
        userClaims: { $ref: '#/components/schemas/UserClaim' }
        labels: { type: object, additionalProperties: { type: string } }
    TokenRequest:
      type: object
      required: [grant_type, claims, metadata]
      properties:
        grant_type: { type: string }
        claims: { $ref: '#/components/schemas/Claim' }
        metadata: { type: object, additionalProperties: { type: string } }
        subject: { allOf: [{ $ref: '#/components/schemas/UserClaim' }], nullable: true }
    Consent:
      type: object
      required: [status]
      properties:
        status: { type: string }
"#,
    );

    // The urlencoded `claims` field is a `$ref` to `Claim`, so it serializes
    // through the annotation converter exactly as a JSON body field would, while
    // the scalar `grant_type` beside it goes onto the wire raw.
    let raw = &files["src/acme/oidc/raw_client.py"];
    assert!(
        raw.contains(
            "\"claims\": convert_and_respect_annotation_metadata(object_=claims, annotation=Claim, direction=\"write\"),"
        ),
        "{raw}"
    );
    assert!(raw.contains("\"grant_type\": grant_type,"), "{raw}");
    // A nullable model field carries the `Optional` wrapper into the annotation.
    assert!(
        raw.contains(
            "object_=subject, annotation=typing.Optional[TokenRequestSubject], direction=\"write\""
        ),
        "{raw}"
    );

    let readme = &files["README.md"];
    // An enum query parameter whose example (`openid profile`) names no member
    // takes the enum's own synthesized value rather than the raw literal.
    assert!(
        readme.contains("    scope=TokenRequestScope.OPENID,\n"),
        "{readme}"
    );
    assert!(!readme.contains("openid profile"), "{readme}");
    // An empty array carries no value, so the example is synthesized from the
    // field name; an empty object selects nothing, so `user_claims` is absent.
    assert!(
        readme.contains("        permitted_authorize_scopes=[\n            \"permittedAuthorizeScopes\"\n        ],\n"),
        "{readme}"
    );
    assert!(!readme.contains("user_claims"), "{readme}");
    // The markdown writers end a length-wrapped dict without Python's magic
    // trailing comma.
    assert!(
        readme.contains(concat!(
            "        labels={\n",
            "            \"aVeryLongLabelKeyThatForcesWrapping\": \"a rather long label value string\",\n",
            "            \"second\": \"value\"\n",
            "        },\n",
        )),
        "{readme}"
    );

    // The reference writer expands a map example even where it would fit on one
    // line, and that flavor survives the markdown dict conversion.
    let reference = &files["reference.md"];
    assert!(
        reference.contains("    metadata={\n        \"key\": \"value\"\n    },\n"),
        "{reference}"
    );
}

#[test]
fn oauth_admin_shapes_pin_the_basic_auth_header_and_documentation_list_paths() {
    // The `blackadi-oauth2` golden's own shapes, which no other registered source
    // carries: a Basic-auth operation whose undocumented body is written inline
    // and flattened field by field keeps the JSON content-type header, while a
    // bare `type: object` body carries it only where the schema is documented,
    // and a status two operations both declare downgrades its error class to
    // `typing.Any` while the merged body model keeps both operations' fields.
    // Beside them the example writer's two list paths: a map example whose value
    // is a JSON array, and a list of a string alias whose example carries `null`.
    let files = render(
        r#"openapi: 3.0.1
info: { title: Admin, version: 1.0.0 }
paths:
  /backchannel_logout/issue:
    post:
      operationId: issueBackchannelLogoutToken
      security: [{ basicAuth: [] }]
      requestBody:
        content:
          application/json:
            schema:
              type: object
              required: [clientIdentifier]
              properties:
                clientIdentifier: { type: string }
                sessionId: { type: string }
      responses:
        '204': { description: issued }
        '400':
          description: bad
          content:
            application/json:
              schema:
                type: object
                properties:
                  error: { type: string }
  /client/dcr/register:
    post:
      operationId: registerClient
      security: [{ basicAuth: [] }]
      requestBody:
        content: { application/json: { schema: { type: object } } }
      responses:
        '204': { description: registered }
        '400':
          description: bad
          content:
            application/json:
              schema:
                type: object
                required: [errorDescription]
                properties:
                  errorDescription: { type: string }
  /federation/registration:
    post:
      operationId: registerFederationEntity
      requestBody:
        content:
          application/json:
            schema: { type: object, description: Federation registration request }
      responses: { '204': { description: registered } }
  /entities:
    post:
      operationId: createEntity
      requestBody:
        content:
          application/json:
            schema: { $ref: '#/components/schemas/Entity' }
            example:
              scopes: ["openid", null]
              roles: ["ADMIN", null]
              labels: { roles: ["admin"] }
      responses: { '204': { description: created } }
components:
  securitySchemes:
    basicAuth: { type: http, scheme: basic }
  schemas:
    Scope: { type: string }
    Role: { type: string, enum: [ADMIN, USER] }
    Entity:
      type: object
      required: [scopes, roles, labels]
      properties:
        scopes:
          type: array
          items: { $ref: '#/components/schemas/Scope' }
        roles:
          type: array
          items: { $ref: '#/components/schemas/Role' }
        labels:
          type: object
          additionalProperties: { type: array, items: { type: string } }
"#,
    );

    let raw = &files["src/acme/raw_client.py"];
    // The Basic-auth body written inline and flattened field by field keeps the
    // header; the bare `type: object` body beside it, undocumented, does not.
    let issue = raw.split("\"backchannel_logout/issue\",").nth(1).unwrap();
    assert!(
        issue.starts_with(concat!(
            "\n            method=\"POST\",\n",
            "            json={\n",
            "                \"clientIdentifier\": client_identifier,\n",
            "                \"sessionId\": session_id,\n",
            "            },\n",
            "            headers={\n",
            "                \"content-type\": \"application/json\",\n",
            "            },\n",
        )),
        "{issue}"
    );
    let register = raw.split("\"client/dcr/register\",").nth(1).unwrap();
    assert!(
        register.starts_with(concat!(
            "\n            method=\"POST\",\n",
            "            json=request,\n",
            "            request_options=request_options,\n",
        )),
        "{register}"
    );
    // The same bare object, documented, does carry it.
    let federation = raw.split("\"federation/registration\",").nth(1).unwrap();
    assert!(
        federation.starts_with(concat!(
            "\n            method=\"POST\",\n",
            "            json=request,\n",
            "            headers={\n",
            "                \"content-type\": \"application/json\",\n",
            "            },\n",
        )),
        "{federation}"
    );

    // Two operations declare `400`, so the error class's body is `typing.Any`
    // while the merged `BadRequestErrorBody` still carries both their fields.
    assert!(
        raw.contains("                        type_=typing.Any,\n"),
        "{raw}"
    );
    let body = &files["src/acme/types/bad_request_error_body.py"];
    // The second operation's `required` merges in, so `error_description` is the
    // one non-optional field on the shared model.
    assert!(
        body.contains(concat!(
            "    error: typing.Optional[str] = None\n",
            "    error_description: typing_extensions.Annotated[\n",
            "        str, FieldMetadata(alias=\"errorDescription\"), pydantic.Field(alias=\"errorDescription\")\n",
            "    ]\n",
        )),
        "{body}"
    );

    // A `null` in a list whose items are a string alias is filled from the field
    // name; the same `null` in a list of an enum is not — it takes the enum's own
    // synthesized member. A map example whose value is a JSON array keeps that
    // array.
    let reference = &files["reference.md"];
    assert!(
        reference.contains(concat!(
            "client.create_entity(\n",
            "    scopes=[\n",
            "        \"openid\",\n",
            "        \"scopes\"\n",
            "    ],\n",
            "    roles=[\n",
            "        Role.ADMIN,\n",
            "        Role.ADMIN\n",
            "    ],\n",
            "    labels={\n",
            "        \"roles\": [\"admin\"]\n",
            "    },\n",
            ")\n",
        )),
        "{reference}"
    );
}

/// A property that declares a scalar `type` beside an `allOf` of constraint-only
/// subschemas is that scalar, not a hoisted model: VolView's `TaskSpec.id` is
/// `type: string` with two `pattern` members, and Fern types it `str`.
#[test]
fn a_scalar_typed_property_with_a_constraint_all_of_stays_a_scalar() {
    let files = render(
        r##"openapi: 3.1.0
info: { title: Tasks, version: 1.0.0 }
paths:
  /tasks:
    get:
      operationId: tasks_list
      responses:
        "200":
          content:
            application/json:
              schema: { $ref: "#/components/schemas/TaskSpec" }
components:
  schemas:
    TaskSpec:
      type: object
      required: [id]
      properties:
        id:
          type: string
          minLength: 1
          allOf:
            - { pattern: "^(?!\\.{1,2}$)" }
            - { pattern: "\\S" }
"##,
    );
    assert!(files["src/acme/types/task_spec.py"].contains("    id: str\n"));
    assert!(!files.contains_key("src/acme/types/task_spec_id.py"));
}

/// A server URL variable whose snake-case spelling collides with the root
/// client's own `base_url` parameter is prefixed `server_url_`, the way Fern
/// names VolView's `{baseUrl}` template; a non-colliding one is left alone.
#[test]
fn a_server_variable_colliding_with_base_url_is_prefixed() {
    let files = render(
        r##"openapi: 3.1.0
info: { title: Neutral, version: 1.0.0 }
servers:
  - url: "{baseUrl}"
    variables:
      baseUrl: { default: "/" }
paths:
  /ping:
    get:
      operationId: health_ping
      responses:
        "200":
          content:
            application/json:
              schema: { type: string }
"##,
    );
    let client = &files["src/acme/client.py"];
    assert!(
        client.contains("server_url_base_url: typing.Optional[str] = None,"),
        "{client}"
    );
    assert!(
        client.contains("base_url = \"{baseUrl}\".format(baseUrl=_server_url_base_url)"),
        "{client}"
    );

    let named = render(
        r##"openapi: 3.1.0
info: { title: Regional, version: 1.0.0 }
servers:
  - url: "https://{region}.example.com"
    variables:
      region: { default: us-east-1 }
paths:
  /ping:
    get:
      operationId: health_ping
      responses:
        "200":
          content:
            application/json:
              schema: { type: string }
"##,
    );
    assert!(named["src/acme/client.py"].contains("region: typing.Optional[str] = None,"));
}

/// A map whose `additionalProperties` value declares its own structure hoists
/// that value to `{Owner}{Prop}Value` — a model for an inline object, a union
/// alias for a `oneOf` — and a `null` member of that union leaves the alias and
/// makes the map's value `Optional`.
#[test]
fn structured_additional_properties_hoist_a_value_type() {
    let files = render(
        r##"openapi: 3.1.0
info: { title: Labels, version: 1.0.0 }
paths:
  /annotations:
    get:
      operationId: annotations_get
      responses:
        "200":
          content:
            application/json:
              schema: { $ref: "#/components/schemas/AnnotationsFile" }
components:
  schemas:
    InputValue:
      type: object
      required: [type]
      properties:
        type: { type: string }
    AnnotationsFile:
      type: object
      properties:
        rulers:
          type: object
          additionalProperties:
            type: object
            properties:
              color: { type: string }
        values:
          type: object
          additionalProperties:
            oneOf:
              - { $ref: "#/components/schemas/InputValue" }
              - { type: string }
              - { type: "null" }
"##,
    );
    let annotations = &files["src/acme/types/annotations_file.py"];
    assert!(
        annotations
            .contains("rulers: typing.Optional[typing.Dict[str, AnnotationsFileRulersValue]]"),
        "{annotations}"
    );
    assert!(
        annotations.contains(
            "values: typing.Optional[typing.Dict[str, typing.Optional[AnnotationsFileValuesValue]]]"
        ),
        "{annotations}"
    );
    assert!(files["src/acme/types/annotations_file_rulers_value.py"]
        .contains("class AnnotationsFileRulersValue(UniversalBaseModel):"));
    assert!(files["src/acme/types/annotations_file_values_value.py"]
        .contains("AnnotationsFileValuesValue = typing.Union[InputValue, str]"));
}

/// A union member that is itself an inline composition is a *named* union to
/// Fern: VolView's `ResultIntent.anyOf[0]` is a `oneOf` of `intent`-const
/// objects, hoisted to the discriminated union `ResultIntentZero` the enclosing
/// alias then references by name.
#[test]
fn a_composition_union_member_hoists_to_its_own_named_union() {
    let files = render(
        r##"openapi: 3.1.0
info: { title: Intents, version: 1.0.0 }
paths:
  /results:
    get:
      operationId: results_get
      responses:
        "200":
          content:
            application/json:
              schema: { $ref: "#/components/schemas/ResultIntent" }
components:
  schemas:
    ResultIntentId:
      type: object
      required: [id]
      properties:
        id: { type: string }
    ResultIntent:
      anyOf:
        - oneOf:
            - type: object
              required: [intent, name]
              properties:
                intent: { type: string, const: add-layer }
                name: { type: string }
            - type: object
              required: [intent, url]
              properties:
                intent: { type: string, const: add-base-image }
                url: { type: string }
        - $ref: "#/components/schemas/ResultIntentId"
"##,
    );
    assert!(files["src/acme/types/result_intent.py"]
        .contains("ResultIntent = typing.Union[ResultIntentZero, ResultIntentId]"));
    let zero = &files["src/acme/types/result_intent_zero.py"];
    assert!(
        zero.contains("class ResultIntentZero_AddLayer(UniversalBaseModel):"),
        "{zero}"
    );
    assert!(
        zero.contains("pydantic.Field(discriminator=\"intent\")"),
        "{zero}"
    );
}

/// An optional map value has no value to show, so its example is the empty map —
/// where a required one takes the `{"key": ...}` pair.
#[test]
fn an_optional_map_value_examples_as_an_empty_map() {
    let files = render(
        r##"openapi: 3.1.0
info: { title: Bindings, version: 1.0.0 }
paths:
  /run:
    post:
      operationId: tasks_run
      requestBody:
        required: true
        content:
          application/json:
            schema: { $ref: "#/components/schemas/RunTaskRequest" }
      responses: { "204": { description: "" } }
components:
  schemas:
    InputValue:
      type: object
      required: [type]
      properties:
        type: { type: string }
    RunTaskRequest:
      type: object
      required: [values]
      properties:
        values:
          type: object
          additionalProperties:
            oneOf:
              - { $ref: "#/components/schemas/InputValue" }
              - { type: string }
              - { type: "null" }
"##,
    );
    let reference = &files["reference.md"];
    assert!(reference.contains("values={},"), "{reference}");
    assert!(files["src/acme/client.py"].contains("values={},"));
}

/// Example imports order a discriminated-union variant before the models named
/// after it, the way Fern writes `StageInputDescriptor_Labelmap` ahead of
/// `StageInputDescriptorLabelmap…`, where a plain sort puts the underscore last.
#[test]
fn example_imports_put_a_union_variant_before_its_prefixed_siblings() {
    let files = render(
        r##"openapi: 3.1.0
info: { title: Staging, version: 1.0.0 }
paths:
  /stage:
    post:
      operationId: context_stage_input
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required: [descriptor]
              properties:
                descriptor: { $ref: "#/components/schemas/StageInputDescriptor" }
      responses: { "204": { description: "" } }
components:
  schemas:
    StageInputDescriptor:
      oneOf:
        - type: object
          required: [type, labelmapReferenceImage, labelmapReferenceImageOwner]
          properties:
            type: { type: string, const: labelmap }
            labelmapReferenceImage:
              type: object
              required: [uri]
              properties:
                uri: { type: string }
            labelmapReferenceImageOwner:
              type: object
              required: [name]
              properties:
                name: { type: string }
"##,
    );
    let client = &files["src/acme/client.py"];
    let variant = client
        .find("    StageInputDescriptor_Labelmap,")
        .expect("the variant is imported");
    let sibling = client
        .find("    StageInputDescriptorLabelmapLabelmapReferenceImage,")
        .expect("the prefixed sibling is imported");
    assert!(variant < sibling, "{client}");
}

/// The two remaining shapes of the same two rules: a map value union with no
/// `null` member keeps the map value required, and a composition member Fern
/// cannot discriminate becomes a plain named union alias rather than a
/// discriminated one.
#[test]
fn undiscriminated_nested_compositions_still_hoist_a_named_union() {
    let files = render(
        r##"openapi: 3.1.0
info: { title: Bindings, version: 1.0.0 }
paths:
  /bindings:
    get:
      operationId: bindings_get
      responses:
        "200":
          content:
            application/json:
              schema: { $ref: "#/components/schemas/Bindings" }
components:
  schemas:
    InputValue:
      type: object
      required: [type]
      properties:
        type: { type: string }
    Bindings:
      type: object
      properties:
        values:
          type: object
          additionalProperties:
            oneOf:
              - { $ref: "#/components/schemas/InputValue" }
              - { type: string }
        choice: { $ref: "#/components/schemas/Choice" }
    Choice:
      anyOf:
        - oneOf:
            - { type: string }
            - { type: integer }
        - { $ref: "#/components/schemas/InputValue" }
"##,
    );
    let bindings = &files["src/acme/types/bindings.py"];
    assert!(
        bindings.contains("values: typing.Optional[typing.Dict[str, BindingsValuesValue]]"),
        "{bindings}"
    );
    assert!(files["src/acme/types/bindings_values_value.py"]
        .contains("BindingsValuesValue = typing.Union[InputValue, str]"));
    assert!(files["src/acme/types/choice_zero.py"].contains("ChoiceZero = typing.Union[str, int]"));
    assert!(
        files["src/acme/types/choice.py"].contains("Choice = typing.Union[ChoiceZero, InputValue]")
    );
}

/// Two composition paths the corpus goldens reach and no in-process journey did:
/// an array of arrays whose innermost items are a union hoists to
/// `{Owner}{Prop}ItemItem`, and a union member that is itself a multi-member
/// `type` list becomes its own named alias the enclosing union references.
#[test]
fn nested_array_and_multi_type_union_members_hoist_named_aliases() {
    let files = render(
        r##"openapi: 3.1.0
info: { title: Grids, version: 1.0.0 }
paths:
  /grids:
    get:
      operationId: grids_get
      responses:
        "200":
          content:
            application/json:
              schema: { $ref: "#/components/schemas/Grid" }
    put:
      operationId: grids_put
      requestBody:
        required: true
        content:
          application/json:
            schema: { $ref: "#/components/schemas/MultiValued" }
      responses: { "204": { description: "" } }
components:
  schemas:
    Grid:
      type: object
      properties:
        cells:
          type: array
          items:
            type: array
            items:
              oneOf:
                - { type: string }
                - { type: integer }
    MultiValued:
      anyOf:
        - type: [string, number, boolean]
        - { type: array, items: { type: string } }
"##,
    );
    assert!(files["src/acme/types/grid.py"]
        .contains("cells: typing.Optional[typing.List[typing.List[GridCellsItemItem]]]"));
    assert!(files["src/acme/types/grid_cells_item_item.py"]
        .contains("GridCellsItemItem = typing.Union[str, int]"));
    assert!(files["src/acme/types/multi_valued_zero.py"]
        .contains("MultiValuedZero = typing.Union[str, float, bool]"));
    assert!(files["src/acme/types/multi_valued.py"]
        .contains("MultiValued = typing.Union[MultiValuedZero, typing.List[str]]"));
}

/// A request body written as a one-member `oneOf` is that member, and a header
/// carried by three quarters of the operations becomes a client-wrapper field.
///
/// Corpus row 112, `flowdapt`, declares both: its `update_config` body is
/// `{"oneOf": [{"$ref": …}]}` and its Fern 5.20.0 golden spreads the referenced
/// component's properties as method arguments with no union alias beside them,
/// and its `x-api-version` header rides 24 of its 26 operations and is
/// promoted as an optional constructor argument.
#[test]
fn a_sole_composition_member_body_inlines_and_a_prevalent_header_promotes() {
    let files = render(
        r##"openapi: 3.1.0
info: { title: Prevalent, version: 1.0.0 }
paths:
  /configs:
    put:
      operationId: configs_update
      tags: [Configs]
      parameters:
        - { name: x-api-version, in: header, required: false, schema: { type: string } }
      requestBody:
        required: true
        content:
          application/json:
            schema:
              oneOf:
                - { $ref: "#/components/schemas/ConfigUpdate" }
      responses: { '204': { description: OK } }
  /configs/status:
    get:
      operationId: configs_status
      tags: [Configs]
      parameters:
        - { name: x-api-version, in: header, required: false, schema: { type: string } }
      responses: { '204': { description: OK } }
  /configs/health:
    get:
      operationId: configs_health
      tags: [Configs]
      parameters:
        - { name: x-api-version, in: header, required: false, schema: { type: string } }
      responses: { '204': { description: OK } }
  /ping:
    get:
      operationId: configs_ping
      tags: [Configs]
      responses: { '204': { description: OK } }
components:
  schemas:
    ConfigUpdate:
      type: object
      required: [name]
      properties:
        name: { type: string }
        note: { type: string }
"##,
    );
    let client = &files["src/acme/configs/client.py"];
    assert!(client.contains("name: str,"), "{client}");
    assert!(!client.contains("ConfigUpdate"), "{client}");
    assert!(
        !files.contains_key("src/acme/configs/types/configs_update_request_body.py"),
        "a one-member composition body coins no union alias"
    );
    let wrapper = &files["src/acme/core/client_wrapper.py"];
    assert!(
        wrapper.contains("api_version: typing.Optional[str] = None"),
        "{wrapper}"
    );
    assert!(wrapper.contains("\"x-api-version\""), "{wrapper}");
    assert!(
        !client.contains("api_version: typing.Optional[str] = None,\n"),
        "a promoted header is no longer a per-method argument: {client}"
    );
}

/// A one-member composition that carries a `discriminator` beside it is not a
/// bare alternative, so it keeps its union shape and its `request` argument.
///
/// The collapse reads a wrapper whose *whole* content is the composition;
/// dropping a sibling keyword would lose what that keyword says.
#[test]
fn a_sole_composition_member_beside_another_keyword_is_left_alone() {
    let files = render(
        r##"openapi: 3.1.0
info: { title: Guarded, version: 1.0.0 }
paths:
  /shapes:
    post:
      operationId: shapes_create
      tags: [Shapes]
      responses: { '204': { description: OK } }
      requestBody:
        required: true
        content:
          application/json:
            schema:
              discriminator:
                propertyName: kind
                mapping:
                  circle: "#/components/schemas/Circle"
              oneOf:
                - { $ref: "#/components/schemas/Circle" }
components:
  schemas:
    Circle:
      type: object
      required: [kind, radius]
      properties:
        kind: { type: string, const: circle }
        radius: { type: number }
"##,
    );
    let client = &files["src/acme/shapes/client.py"];
    assert!(client.contains("request:"), "{client}");
    assert!(!client.contains("radius: float,"), "{client}");
}

/// A two-member composition body with no other parameter collapses to its bare
/// type, which carries no content type at all.
///
/// Corpus row 112's `create_config` is exactly that shape and its golden sends
/// no `content-type` header, where the same body beside a path parameter does.
#[test]
fn a_bare_composition_body_argument_sends_no_content_type() {
    let spec = r##"openapi: 3.1.0
info: { title: Bare, version: 1.0.0 }
paths:
  /configs:
    post:
      operationId: configs_create
      tags: [Configs]
      responses: { '204': { description: OK } }
      requestBody:
        required: true
        content:
          application/json:
            schema:
              oneOf:
                - { $ref: "#/components/schemas/Alpha" }
                - { $ref: "#/components/schemas/Beta" }
  /configs/{identifier}:
    post:
      operationId: configs_replace
      tags: [Configs]
      parameters:
        - { name: identifier, in: path, required: true, schema: { type: string } }
      responses: { '204': { description: OK } }
      requestBody:
        required: true
        content:
          application/json:
            schema:
              oneOf:
                - { $ref: "#/components/schemas/Alpha" }
                - { $ref: "#/components/schemas/Beta" }
components:
  schemas:
    Alpha: { type: object, required: [a], properties: { a: { type: string } } }
    Beta: { type: object, required: [b], properties: { b: { type: string } } }
"##;
    let files = render(spec);
    let raw = &files["src/acme/configs/raw_client.py"];
    let create = raw.split("def create(").nth(1).expect("create method");
    let create = create.split("def ").next().expect("method body");
    assert!(!create.contains("content-type"), "{create}");
    let replace = raw.split("def replace(").nth(1).expect("replace method");
    let replace = replace.split("def ").next().expect("method body");
    assert!(
        replace.contains("\"content-type\": \"application/json\""),
        "{replace}"
    );
}

/// A map whose value is an array of an inline union hoists the union under the
/// value slot's own name, and a `$ref` to a nullable component in a map value
/// slot is optional at that use site.
///
/// Corpus row 112 declares the first (`V1Alpha1Metrics`) and corpus row 111 the
/// second (`QueryParameters`), and both goldens byte-match.
#[test]
fn a_map_value_hoists_its_array_item_union_and_carries_ref_nullability() {
    let files = render(
        r##"openapi: 3.1.0
info: { title: Maps, version: 1.0.0 }
paths:
  /metrics:
    get:
      operationId: metrics_read
      tags: [Metrics]
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema: { $ref: "#/components/schemas/Metrics" }
components:
  schemas:
    Counter: { type: object, required: [count], properties: { count: { type: integer } } }
    Bucket: { type: object, required: [bounds], properties: { bounds: { type: string } } }
    Metrics:
      type: object
      additionalProperties:
        type: array
        items:
          anyOf:
            - { $ref: "#/components/schemas/Counter" }
            - { $ref: "#/components/schemas/Bucket" }
    Nullable:
      anyOf:
        - { type: "null" }
        - { type: string }
    Holder:
      type: object
      additionalProperties: { $ref: "#/components/schemas/Nullable" }
"##,
    );
    let metrics = &files["src/acme/types/metrics.py"];
    assert!(
        metrics.contains("Metrics = typing.Dict[str, typing.List[MetricsValueItem]]"),
        "{metrics}"
    );
    let item = &files["src/acme/types/metrics_value_item.py"];
    assert!(
        item.contains("MetricsValueItem = typing.Union[Counter, Bucket]"),
        "{item}"
    );
    let holder = &files["src/acme/types/holder.py"];
    assert!(
        holder.contains("Holder = typing.Dict[str, typing.Optional[Nullable]]"),
        "{holder}"
    );
}

/// A parameter composition's `type: null` alternative is nullability, its
/// inline enum alternative is an ordinal-suffixed enum of its own, and a
/// composition whose members all lower to one type hoists nothing.
///
/// Corpus row 110, `osparc-simcore-webserver`, declares all three — `file_size`,
/// `product_name` and `folder_id` — and corpus row 112 the fourth,
/// `identifier`.
#[test]
fn a_parameter_composition_reads_null_as_nullability_and_hoists_its_enum() {
    let files = render(
        r##"openapi: 3.1.0
info: { title: Params, version: 1.0.0 }
paths:
  /files/{folder_id}:
    put:
      operationId: files_upload
      tags: [Files]
      parameters:
        - name: folder_id
          in: path
          required: true
          schema:
            anyOf:
              - { type: integer }
              - { type: "null" }
        - name: file_size
          in: query
          required: true
          schema:
            anyOf:
              - { type: string }
              - { type: integer }
              - { type: "null" }
        - name: product_name
          in: query
          required: false
          schema:
            title: Product Name
            anyOf:
              - { type: string }
              - { type: string, const: current }
        - name: identifier
          in: query
          required: false
          schema:
            anyOf:
              - { type: string }
              - { type: string, format: uuid }
        - name: tags
          in: query
          required: false
          schema:
            anyOf:
              - { type: array, items: { type: string } }
              - { type: "null" }
      responses: { '204': { description: OK } }
"##,
    );
    let raw = &files["src/acme/files/raw_client.py"];
    assert!(raw.contains("folder_id: typing.Optional[int]"), "{raw}");
    assert!(
        raw.contains("file_size: typing.Optional[FilesUploadRequestFileSize] = None"),
        "{raw}"
    );
    assert!(
        raw.contains("identifier: typing.Optional[str] = None"),
        "{raw}"
    );
    assert!(
        raw.contains("tags: typing.Optional[typing.Sequence[str]] = None"),
        "{raw}"
    );
    assert!(
        raw.contains("\"file_size\": file_size,"),
        "a scalar union reaches the URL raw: {raw}"
    );
    let size = &files["src/acme/types/files_upload_request_file_size.py"];
    assert!(
        size.contains("FilesUploadRequestFileSize = typing.Union[str, int]"),
        "{size}"
    );
    let product = &files["src/acme/files/types/files_upload_request_product_name.py"];
    assert!(
        product.contains(
            "FilesUploadRequestProductName = typing.Union[str, FilesUploadRequestProductNameOne]"
        ),
        "{product}"
    );
    assert!(
        files.contains_key("src/acme/files/types/files_upload_request_product_name_one.py"),
        "the enum alternative is hoisted under its ordinal name"
    );
    assert!(
        !files.contains_key("src/acme/types/files_upload_request_identifier.py"),
        "a composition whose members lower to one type hoists nothing"
    );
    let client = &files["src/acme/files/client.py"];
    assert!(
        client.contains("file_size=\"file_size\","),
        "a required-but-nullable parameter is still passed in the worked call: {client}"
    );
}

/// A map to unknown takes Fern's placeholder example whatever the schema
/// declares, and an object with a *required* unknown field cannot be exampled
/// at all, so a list of it renders empty.
///
/// Corpus row 111's `OperationTree` is the first and corpus row 110's
/// `ProjectInputUpdate` the second; both goldens byte-match.
#[test]
fn an_unknown_map_takes_the_placeholder_and_an_unexampleable_list_renders_empty() {
    let files = render(
        r##"openapi: 3.1.0
info: { title: Unknowns, version: 1.0.0 }
paths:
  /queries:
    post:
      operationId: queries_run
      tags: [Queries]
      responses: { '204': { description: OK } }
      requestBody:
        required: true
        content:
          application/json:
            schema: { $ref: "#/components/schemas/RunRequest" }
  /inputs:
    patch:
      operationId: inputs_update
      tags: [Inputs]
      responses: { '204': { description: OK } }
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: array
              items: { $ref: "#/components/schemas/InputUpdate" }
components:
  schemas:
    OperationTree:
      type: object
      additionalProperties: true
      examples:
        - { nodes: { reference: all } }
    NamedQuery:
      type: object
      required: [root]
      properties:
        root: { $ref: "#/components/schemas/OperationTree" }
    RunRequest:
      type: object
      required: [query]
      properties:
        query: { $ref: "#/components/schemas/NamedQuery" }
    InputUpdate:
      type: object
      required: [key, value]
      properties:
        key: { type: string }
        value: { title: Value, description: Value assigned to this port }
"##,
    );
    let queries = &files["src/acme/queries/client.py"];
    assert!(queries.contains("root={\"key\": \"value\"}"), "{queries}");
    assert!(!queries.contains("nodes"), "{queries}");
    assert!(queries.contains("query=NamedQuery("), "{queries}");
    let inputs = &files["src/acme/inputs/client.py"];
    assert!(inputs.contains("request=[],"), "{inputs}");
    let update = &files["src/acme/types/input_update.py"];
    assert!(
        update.contains("value: typing.Any\n"),
        "a bare unknown carries no docstring: {update}"
    );
    assert!(!update.contains("Value assigned to this port"), "{update}");
}

/// A binary media type loses to an `application/json` declared beside it, and a
/// binary *schema* wins either way.
///
/// Corpus row 110's `create_captcha` is `image/png: {}` beside an
/// `application/json` and returns `typing.Any`; corpus row 112's
/// `get_plugin_file` is a schemaless `application/octet-stream` alone and
/// streams.
#[test]
fn a_binary_media_type_loses_to_json_beside_it() {
    let files = render(
        r##"openapi: 3.1.0
info: { title: Media, version: 1.0.0 }
paths:
  /captcha:
    get:
      operationId: media_captcha
      tags: [Media]
      responses:
        '200':
          description: OK
          content:
            application/json: { schema: {} }
            image/png: {}
  /file:
    get:
      operationId: media_file
      tags: [Media]
      responses:
        '200':
          description: OK
          content:
            application/octet-stream: {}
"##,
    );
    let raw = &files["src/acme/media/raw_client.py"];
    let captcha = raw.split("def captcha(").nth(1).expect("captcha method");
    assert!(
        captcha
            .split("def ")
            .next()
            .unwrap()
            .contains("HttpResponse[typing.Any]"),
        "{captcha}"
    );
    let file = raw.split("def file(").nth(1).expect("file method");
    assert!(
        file.split("def ")
            .next()
            .unwrap()
            .contains("typing.Iterator[bytes]"),
        "{file}"
    );
}

/// `x-enum-varnames` names a string enum's members positionally, and a keyed
/// `x-fern-enum` declaration wins over it for the same value.
///
/// Corpus row 113's `Error.type` enumerates seven RFC 9457 problem-type URIs and
/// names them `INVALIDARGUMENT`, `NOTFOUND`, … that way; its Fern 5.20.0 golden
/// emits those members rather than the identifiers derived from the URIs, which
/// would spell the whole scheme and host.
#[test]
fn an_enum_takes_its_member_names_from_x_enum_varnames() {
    let files = render(
        r##"openapi: 3.0.4
info: { title: Problems, version: 1.0.0 }
paths:
  /errors:
    get:
      operationId: errors_get
      tags: [Errors]
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema: { $ref: "#/components/schemas/Error" }
components:
  schemas:
    Error:
      type: object
      properties:
        type:
          type: string
          description: URI reference identifying the error type
          enum:
            - https://example.test/problems/invalid-argument
            - https://example.test/problems/not-found
          x-enum-varnames:
            - INVALIDARGUMENT
            - NOTFOUND
        unit:
          type: string
          enum: ["$", "%"]
          x-enum-varnames:
            - DOLLAR
            - PERCENT
          x-fern-enum:
            "$": { name: USD }
"##,
    );
    let error_type = &files["src/acme/types/error_type.py"];
    assert!(
        error_type.contains("INVALIDARGUMENT = \"https://example.test/problems/invalid-argument\""),
        "{error_type}"
    );
    assert!(
        error_type.contains("NOTFOUND = \"https://example.test/problems/not-found\""),
        "{error_type}"
    );
    assert!(
        !error_type.contains("HTTPS_EXAMPLE_TEST"),
        "a named member does not fall back to the identifier derived from the URI: {error_type}"
    );
    assert!(
        error_type.contains("invalidargument: typing.Callable[[], T_Result]"),
        "the `visit` parameter is the declared name cased down: {error_type}"
    );
    let unit = &files["src/acme/types/error_unit.py"];
    assert!(
        unit.contains("USD = \"$\""),
        "a keyed declaration wins over the positional one: {unit}"
    );
    assert!(unit.contains("PERCENT = \"%\""), "{unit}");
    assert!(!unit.contains("DOLLAR"), "{unit}");
}

/// A documented, mostly-`readOnly` body schema with exactly one required member
/// keeps its explicit `content-type` header; the same shape undocumented drops
/// it.
///
/// Corpus row 113's `create_container` sends a `Container` whose six `readOnly`
/// properties surround the single required `spec`, and whose request and 201
/// response name the same component — two shapes that each otherwise drop the
/// header — and its Fern 5.20.0 golden sends `content-type: application/json`.
#[test]
fn a_documented_resource_envelope_keeps_its_content_type_header() {
    let files = render(
        r##"openapi: 3.0.4
info: { title: Envelopes, version: 1.0.0 }
paths:
  /containers:
    post:
      operationId: resources_create_container
      tags: [Resources]
      requestBody:
        required: true
        content:
          application/json:
            schema: { $ref: "#/components/schemas/Container" }
      responses:
        '201':
          description: OK
          content:
            application/json:
              schema: { $ref: "#/components/schemas/Container" }
  /widgets:
    post:
      operationId: resources_create_widget
      tags: [Resources]
      requestBody:
        required: true
        content:
          application/json:
            schema: { $ref: "#/components/schemas/Widget" }
      responses:
        '201':
          description: OK
          content:
            application/json:
              schema: { $ref: "#/components/schemas/Widget" }
components:
  schemas:
    Container:
      type: object
      description: Container resource representing a container instance
      required: [spec]
      properties:
        id: { type: string, readOnly: true }
        path: { type: string, readOnly: true }
        spec: { type: string }
        create_time: { type: string, readOnly: true }
    Widget:
      type: object
      required: [spec]
      properties:
        id: { type: string, readOnly: true }
        path: { type: string, readOnly: true }
        spec: { type: string }
        create_time: { type: string, readOnly: true }
"##,
    );
    let raw = &files["src/acme/resources/raw_client.py"];
    let container = raw
        .split("def create_container(")
        .nth(1)
        .expect("create_container method");
    assert!(
        container
            .split("\n    def ")
            .next()
            .unwrap()
            .contains("\"content-type\": \"application/json\","),
        "{container}"
    );
    let widget = raw
        .split("def create_widget(")
        .nth(1)
        .expect("create_widget method");
    assert!(
        !widget
            .split("\n    def ")
            .next()
            .unwrap()
            .contains("\"content-type\""),
        "an undocumented envelope drops the header: {widget}"
    );
}
