//! The intermediate representation: a small, generation-ready model built from
//! the OpenAPI document, decoupling parsing from emission. Schema and property
//! order is preserved from the document so generated output is deterministic.

use crate::config::GenerateConfig;
use crate::naming;
use crate::openapi::{AdditionalProperties, OpenApi, Schema};

/// A fully-resolved SDK model ready to emit.
#[derive(Debug)]
pub struct Ir {
    /// Python import package name (directory under `src/`).
    pub package_name: String,
    /// Distribution name recorded in `version.py`.
    pub project_name: String,
    /// Generated types, in document order.
    pub types: Vec<TypeDecl>,
}

/// A generated top-level type.
#[derive(Debug)]
pub enum TypeDecl {
    /// A pydantic model.
    Object(ObjectType),
    /// A type alias (`Name = <expr>`), e.g. a union, an extensible enum, or a
    /// scalar alias.
    Alias(AliasType),
}

impl TypeDecl {
    /// The class/alias name.
    #[must_use]
    pub fn name(&self) -> &str {
        match self {
            TypeDecl::Object(o) => &o.name,
            TypeDecl::Alias(a) => &a.name,
        }
    }

    /// The module (file stem) the type lives in.
    #[must_use]
    pub fn module(&self) -> &str {
        match self {
            TypeDecl::Object(o) => &o.module,
            TypeDecl::Alias(a) => &a.module,
        }
    }
}

/// A pydantic model type.
#[derive(Debug)]
pub struct ObjectType {
    /// Class name.
    pub name: String,
    /// Module (file stem).
    pub module: String,
    /// Fields, in document order.
    pub fields: Vec<Field>,
    /// Optional class docstring.
    pub docstring: Option<String>,
}

/// One model field.
#[derive(Debug)]
pub struct Field {
    /// The wire (JSON) property name.
    pub wire_name: String,
    /// The Python identifier (snake_case, reserved-munged).
    pub py_name: String,
    /// The field's value type.
    pub type_ref: TypeRef,
    /// Whether the field is optional (wrapped in `typing.Optional`, default None).
    pub optional: bool,
    /// Optional field docstring (from the property `description`).
    pub docstring: Option<String>,
}

impl Field {
    /// True when the Python name differs from the wire name, requiring an alias.
    #[must_use]
    pub fn needs_alias(&self) -> bool {
        self.py_name != self.wire_name
    }
}

/// A type alias declaration.
#[derive(Debug)]
pub struct AliasType {
    /// Alias name.
    pub name: String,
    /// Module (file stem).
    pub module: String,
    /// The aliased type expression.
    pub target: TypeRef,
    /// Optional docstring.
    pub docstring: Option<String>,
}

/// A resolved type reference.
#[derive(Debug, Clone)]
pub enum TypeRef {
    /// A primitive Python type.
    Primitive(Prim),
    /// A reference to another generated type, by class name.
    Named(String),
    /// `typing.Optional[..]`.
    Optional(Box<TypeRef>),
    /// `typing.List[..]`.
    List(Box<TypeRef>),
    /// `typing.Set[..]`.
    Set(Box<TypeRef>),
    /// `typing.Dict[K, V]`.
    Dict(Box<TypeRef>, Box<TypeRef>),
    /// `typing.Union[..]`.
    Union(Vec<TypeRef>),
    /// `typing.Literal["a", "b", ...]`.
    Literal(Vec<String>),
}

/// Primitive leaf types.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum Prim {
    /// `str`.
    Str,
    /// `int`.
    Int,
    /// `float`.
    Float,
    /// `bool`.
    Bool,
    /// `dt.datetime`.
    Datetime,
    /// `dt.date`.
    Date,
    /// `typing.Any`.
    Any,
}

/// Build the IR from a parsed document and config.
#[must_use]
pub fn build(doc: &OpenApi, config: &GenerateConfig) -> Ir {
    let mut types = Vec::new();
    for (key, schema) in &doc.components.schemas {
        types.push(build_type(key, schema));
    }
    Ir {
        package_name: config.package_name.clone(),
        project_name: config.project_name.clone(),
        types,
    }
}

/// Classify and build one named schema into a top-level type.
fn build_type(key: &str, schema: &Schema) -> TypeDecl {
    let name = naming::class_name(key);
    let module = naming::module_name(&name);
    let docstring = clean_doc(schema.description.as_deref());

    // An object with `additionalProperties` but no declared properties is a map,
    // which Fern emits as a `Dict[..]` alias rather than an empty model.
    let is_map = is_object_type(schema)
        && schema.properties.is_empty()
        && matches!(
            schema.additional_properties,
            Some(AdditionalProperties::Schema(_))
        );

    // Object with properties (and not a bare map).
    if !is_map && (!schema.properties.is_empty() || is_object_type(schema)) {
        let fields = schema
            .properties
            .iter()
            .map(|(prop, prop_schema)| build_field(prop, prop_schema, schema))
            .collect();
        return TypeDecl::Object(ObjectType {
            name,
            module,
            fields,
            docstring,
        });
    }

    // Everything else is an alias: a union, an extensible enum, a map, a scalar,
    // or an unknown type. `full_type_ref` carries any `Optional` wrapping.
    TypeDecl::Alias(AliasType {
        name,
        module,
        target: full_type_ref(schema),
        docstring,
    })
}

/// Build one field from a property schema.
fn build_field(prop: &str, prop_schema: &Schema, parent: &Schema) -> Field {
    let optional = is_optional(prop_schema) || !parent.required.iter().any(|r| r == prop);
    Field {
        wire_name: prop.to_string(),
        py_name: naming::field_name(prop),
        type_ref: base_type_ref(prop_schema),
        optional,
        docstring: clean_doc(prop_schema.description.as_deref()),
    }
}

/// Map a schema to its full type expression, wrapping in `Optional` when the
/// schema is nullable or an unknown (untyped) schema. Used for aliases, where
/// optionality lives in the type itself rather than a separate field flag.
fn full_type_ref(schema: &Schema) -> TypeRef {
    let base = base_type_ref(schema);
    if is_optional(schema) {
        TypeRef::Optional(Box::new(base))
    } else {
        base
    }
}

/// Map a schema to its base type expression, never adding a top-level
/// `Optional` (the caller decides optionality for fields).
fn base_type_ref(schema: &Schema) -> TypeRef {
    if let Some(reference) = &schema.reference {
        return TypeRef::Named(ref_to_class(reference));
    }
    if let Some(values) = string_enum_values(schema) {
        // Fern renders an OpenAPI string enum as an extensible enum:
        // `Union[Literal["a", "b", ...], Any]`.
        return TypeRef::Union(vec![
            TypeRef::Literal(values),
            TypeRef::Primitive(Prim::Any),
        ]);
    }
    if let Some(variants) = union_variants(schema) {
        return TypeRef::Union(variants);
    }
    match schema.ty.as_ref().and_then(|t| t.primary()) {
        Some("string") => match schema.format.as_deref() {
            Some("date-time") => TypeRef::Primitive(Prim::Datetime),
            Some("date") => TypeRef::Primitive(Prim::Date),
            // Fern's OpenAPI importer maps other string formats (uuid, byte, ...)
            // to plain `str`.
            _ => TypeRef::Primitive(Prim::Str),
        },
        Some("integer") => TypeRef::Primitive(Prim::Int),
        Some("number") => TypeRef::Primitive(Prim::Float),
        Some("boolean") => TypeRef::Primitive(Prim::Bool),
        Some("array") => {
            let item = schema
                .items
                .as_ref()
                .map_or(TypeRef::Primitive(Prim::Any), |i| base_type_ref(i));
            if schema.unique_items == Some(true) {
                TypeRef::Set(Box::new(item))
            } else {
                TypeRef::List(Box::new(item))
            }
        }
        Some("object") => match &schema.additional_properties {
            Some(AdditionalProperties::Schema(value)) => TypeRef::Dict(
                Box::new(TypeRef::Primitive(Prim::Str)),
                Box::new(base_type_ref(value)),
            ),
            _ => TypeRef::Primitive(Prim::Any),
        },
        _ => TypeRef::Primitive(Prim::Any),
    }
}

/// Is a schema optional? A schema is optional when it is explicitly `nullable`
/// or when it is an unknown (untyped) schema, which Fern always renders as
/// `Optional[Any]`.
fn is_optional(schema: &Schema) -> bool {
    schema.nullable == Some(true) || is_unknown(schema)
}

/// A schema that carries nothing to determine a type — Fern treats it as an
/// unknown value (`Optional[Any]`).
fn is_unknown(schema: &Schema) -> bool {
    schema.reference.is_none()
        && schema.ty.is_none()
        && schema.one_of.is_none()
        && schema.any_of.is_none()
        && schema.all_of.is_none()
        && schema.enum_values.is_none()
        && schema.properties.is_empty()
        && schema.additional_properties.is_none()
        && schema.items.is_none()
}

/// The string values of a `type: string` enum schema, if it is one.
fn string_enum_values(schema: &Schema) -> Option<Vec<String>> {
    if !is_string_type(schema) {
        return None;
    }
    let values = schema.enum_values.as_ref()?;
    Some(
        values
            .iter()
            .filter_map(|v| v.as_str().map(str::to_string))
            .collect(),
    )
}

/// Extract union variants from a `oneOf`/`anyOf` schema, if present.
fn union_variants(schema: &Schema) -> Option<Vec<TypeRef>> {
    let variants = schema.one_of.as_ref().or(schema.any_of.as_ref())?;
    Some(variants.iter().map(base_type_ref).collect())
}

/// Resolve a `$ref` to the class name it points at.
fn ref_to_class(reference: &str) -> String {
    let last = reference.rsplit('/').next().unwrap_or(reference);
    naming::class_name(last)
}

/// Is this schema declared as `type: string`?
fn is_string_type(schema: &Schema) -> bool {
    schema.ty.as_ref().and_then(|t| t.primary()) == Some("string")
}

/// Is this schema declared as `type: object`?
fn is_object_type(schema: &Schema) -> bool {
    schema.ty.as_ref().and_then(|t| t.primary()) == Some("object")
}

/// Normalize a description into a docstring, dropping empty ones.
fn clean_doc(desc: Option<&str>) -> Option<String> {
    let text = desc?.trim();
    if text.is_empty() {
        None
    } else {
        Some(text.to_string())
    }
}
