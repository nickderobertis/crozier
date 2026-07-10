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
    // Reserved name is munged and aliased; the wire alias lives only in
    // FieldMetadata (not pydantic.Field).
    assert!(widget.contains(
        "list_: typing_extensions.Annotated[typing.Optional[typing.List[str]], FieldMetadata(alias=\"list\")] = None"
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
    assert!(files["src/acme/types/shape.py"].contains("Shape = typing.Union[Owner, str]"));
    assert!(files["src/acme/types/alias.py"].contains("Alias = str"));
}

#[test]
fn string_enum_renders_as_extensible_union() {
    // Fern renders an OpenAPI string enum as an extensible enum, not an
    // `enum.Enum` class.
    let files = render(RICH_SPEC);
    let color = &files["src/acme/types/color.py"];
    assert!(
        color.contains("Color = typing.Union[typing.Literal[\"red\", \"green\"], typing.Any]"),
        "extensible enum: {color}"
    );
    assert!(!color.contains("enum.Enum"));
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
fn unique_items_array_maps_to_set() {
    let files = render(
        "openapi: 3.0.0\ninfo:\n  title: S\ncomponents:\n  schemas:\n    Obj:\n      type: object\n      properties:\n        tags:\n          type: array\n          uniqueItems: true\n          items:\n            type: string\n",
    );
    assert!(
        files["src/acme/types/obj.py"].contains("tags: typing.Optional[typing.Set[str]] = None")
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
fn additional_properties_true_maps_to_any() {
    let files = render(
        "openapi: 3.0.0\ninfo:\n  title: A\ncomponents:\n  schemas:\n    Bag:\n      type: object\n      properties:\n        data:\n          type: object\n          additionalProperties: true\n",
    );
    assert!(files["src/acme/types/bag.py"].contains("data: typing.Optional[typing.Any] = None"));
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
fn unknown_schema_maps_to_optional_any() {
    // An empty schema is an unknown type: an `Optional[Any]` alias, and an
    // always-optional `Optional[Any]` field even when listed as required.
    let files = render(
        "openapi: 3.0.0\ninfo:\n  title: U\ncomponents:\n  schemas:\n    Unknown: {}\n    Holder:\n      type: object\n      required: [value]\n      properties:\n        value: {}\n",
    );
    assert!(files["src/acme/types/unknown.py"].contains("Unknown = typing.Optional[typing.Any]"));
    assert!(
        files["src/acme/types/holder.py"].contains("value: typing.Optional[typing.Any] = None"),
        "{}",
        files["src/acme/types/holder.py"]
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
    // A string enum whose one-line form exceeds ruff's 120-col limit is exploded:
    // the Union onto its own lines and the Literal one value per line.
    let members: Vec<String> = (0..12)
        .map(|i| format!("        - VALUE_NUMBER_{i:02}_WITH_PADDING\n"))
        .collect();
    let spec = format!(
        "openapi: 3.0.0\ninfo:\n  title: W\ncomponents:\n  schemas:\n    Big:\n      type: string\n      enum:\n{}",
        members.concat()
    );
    let big = render(&spec)["src/acme/types/big.py"].clone();
    assert!(
        big.contains("Big = typing.Union[\n    typing.Literal[\n"),
        "expected exploded union: {big}"
    );
    assert!(
        big.contains("        \"VALUE_NUMBER_00_WITH_PADDING\",\n"),
        "{big}"
    );
    assert!(big.contains("    ],\n    typing.Any,\n]"), "{big}");
}

#[test]
fn oneof_hoists_inline_object_variants() {
    // A oneOf with inline-object variants: each is hoisted to `{Name}{Ordinal}`.
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
        files["src/acme/types/pet.py"].contains("Pet = typing.Union[PetZero, PetOne, Dog, str]"),
        "{}",
        files["src/acme/types/pet.py"]
    );
    // Variant 0: inherits its $ref base, with the inline enum hoisted and required.
    let zero = &files["src/acme/types/pet_zero.py"];
    assert!(zero.contains("class PetZero(Dog):"), "{zero}");
    assert!(zero.contains("    kind: PetZeroKind\n"), "{zero}");
    assert!(files["src/acme/types/pet_zero_kind.py"]
        .contains("PetZeroKind = typing.Union[typing.Literal[\"dog\"], typing.Any]"));
    // Variant 1: no base, so it extends UniversalBaseModel; its field is optional.
    let one = &files["src/acme/types/pet_one.py"];
    assert!(one.contains("class PetOne(UniversalBaseModel):"), "{one}");
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
