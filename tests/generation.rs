//! In-process integration tests over the generation pipeline. Unlike the binary
//! e2e (`tests/e2e.rs`), these call the library directly so they are measured by
//! coverage; they exercise the type-mapping and emit branches a single fixture
//! cannot, while still driving real parsing over real temp files.

use std::collections::HashMap;
use std::path::PathBuf;

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
    })
    .expect("render succeeds");
    files
        .into_iter()
        .map(|f| (f.path.to_string_lossy().into_owned(), f.contents))
        .collect()
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
    // Reserved name is munged and aliased.
    assert!(widget.contains(
        "list_: typing_extensions.Annotated[typing.Optional[typing.List[str]], FieldMetadata(alias=\"list\"), pydantic.Field(alias=\"list\")] = None"
    ), "aliased list field: {widget}");
    // Primitive mappings.
    assert!(widget.contains("when: typing.Optional[dt.datetime] = None"));
    assert!(widget.contains("day: typing.Optional[dt.date] = None"));
    assert!(widget.contains("ident: typing.Optional[uuid.UUID] = None"));
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
import uuid

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
    assert!(files["src/acme/types/shape.py"].contains("Shape = typing.Union[Owner, str]"));
    assert!(files["src/acme/types/alias.py"].contains("Alias = str"));
}

#[test]
fn enum_file_lists_members() {
    let files = render(RICH_SPEC);
    let color = &files["src/acme/types/color.py"];
    assert!(color.contains("class Color(str, enum.Enum):"));
    assert!(color.contains("RED = \"red\""));
    assert!(color.contains("GREEN = \"green\""));
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
    })
    .unwrap();
    assert!(files.iter().any(|f| f.path.starts_with("src/my_cool_api")));
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
fn additional_properties_true_maps_to_any() {
    let files = render(
        "openapi: 3.0.0\ninfo:\n  title: A\ncomponents:\n  schemas:\n    Bag:\n      type: object\n      properties:\n        data:\n          type: object\n          additionalProperties: true\n",
    );
    assert!(files["src/acme/types/bag.py"].contains("data: typing.Optional[typing.Any] = None"));
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
    })
    .unwrap();
    assert!(files.iter().any(|f| f.path.starts_with("src/client")));
}
