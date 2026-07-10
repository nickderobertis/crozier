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
    /// A string enum.
    Enum(EnumType),
    /// A type alias (`Name = <expr>`), e.g. a union or a scalar alias.
    Alias(AliasType),
}

impl TypeDecl {
    /// The class/alias name.
    #[must_use]
    pub fn name(&self) -> &str {
        match self {
            TypeDecl::Object(o) => &o.name,
            TypeDecl::Enum(e) => &e.name,
            TypeDecl::Alias(a) => &a.name,
        }
    }

    /// The module (file stem) the type lives in.
    #[must_use]
    pub fn module(&self) -> &str {
        match self {
            TypeDecl::Object(o) => &o.module,
            TypeDecl::Enum(e) => &e.module,
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

/// A string enum.
#[derive(Debug)]
pub struct EnumType {
    /// Class name.
    pub name: String,
    /// Module (file stem).
    pub module: String,
    /// Enum members: (python member value string, wire value).
    pub variants: Vec<String>,
    /// Optional docstring.
    pub docstring: Option<String>,
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
    /// `typing.List[..]`.
    List(Box<TypeRef>),
    /// `typing.Set[..]`.
    Set(Box<TypeRef>),
    /// `typing.Dict[K, V]`.
    Dict(Box<TypeRef>, Box<TypeRef>),
    /// `typing.Union[..]`.
    Union(Vec<TypeRef>),
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
    /// `uuid.UUID`.
    Uuid,
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

    // Enum: a string schema with enum values.
    if let Some(values) = &schema.enum_values {
        if is_string_type(schema) {
            let variants = values
                .iter()
                .filter_map(|v| v.as_str().map(str::to_string))
                .collect();
            return TypeDecl::Enum(EnumType {
                name,
                module,
                variants,
                docstring,
            });
        }
    }

    // Union alias: oneOf/anyOf without object properties.
    if schema.properties.is_empty() {
        if let Some(variants) = union_variants(schema) {
            return TypeDecl::Alias(AliasType {
                name,
                module,
                target: TypeRef::Union(variants),
                docstring,
            });
        }
    }

    // Object with properties.
    if !schema.properties.is_empty() || is_object_type(schema) {
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

    // Fallback: a scalar alias to the mapped type.
    TypeDecl::Alias(AliasType {
        name,
        module,
        target: schema_to_type_ref(schema),
        docstring,
    })
}

/// Build one field from a property schema.
fn build_field(prop: &str, prop_schema: &Schema, parent: &Schema) -> Field {
    Field {
        wire_name: prop.to_string(),
        py_name: naming::field_name(prop),
        type_ref: schema_to_type_ref(prop_schema),
        optional: !parent.required.iter().any(|r| r == prop),
        docstring: clean_doc(prop_schema.description.as_deref()),
    }
}

/// Map a schema node to a resolved [`TypeRef`].
fn schema_to_type_ref(schema: &Schema) -> TypeRef {
    if let Some(reference) = &schema.reference {
        return TypeRef::Named(ref_to_class(reference));
    }
    if let Some(variants) = union_variants(schema) {
        return TypeRef::Union(variants);
    }
    match schema.ty.as_ref().and_then(|t| t.primary()) {
        Some("string") => match schema.format.as_deref() {
            Some("date-time") => TypeRef::Primitive(Prim::Datetime),
            Some("date") => TypeRef::Primitive(Prim::Date),
            Some("uuid") => TypeRef::Primitive(Prim::Uuid),
            _ => TypeRef::Primitive(Prim::Str),
        },
        Some("integer") => TypeRef::Primitive(Prim::Int),
        Some("number") => TypeRef::Primitive(Prim::Float),
        Some("boolean") => TypeRef::Primitive(Prim::Bool),
        Some("array") => {
            let item = schema
                .items
                .as_ref()
                .map_or(TypeRef::Primitive(Prim::Any), |i| schema_to_type_ref(i));
            TypeRef::List(Box::new(item))
        }
        Some("object") => match &schema.additional_properties {
            Some(AdditionalProperties::Schema(value)) => TypeRef::Dict(
                Box::new(TypeRef::Primitive(Prim::Str)),
                Box::new(schema_to_type_ref(value)),
            ),
            _ => TypeRef::Primitive(Prim::Any),
        },
        _ => TypeRef::Primitive(Prim::Any),
    }
}

/// Extract union variants from a `oneOf`/`anyOf` schema, if present.
fn union_variants(schema: &Schema) -> Option<Vec<TypeRef>> {
    let variants = schema.one_of.as_ref().or(schema.any_of.as_ref())?;
    Some(variants.iter().map(schema_to_type_ref).collect())
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
