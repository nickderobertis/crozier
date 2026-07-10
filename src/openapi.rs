//! A pragmatic serde model of the subset of OpenAPI 3.x that crozier reads.
//!
//! Ordering matters for byte-exact output: object properties and component
//! schemas are [`IndexMap`]s so their document order survives into generated
//! field order and file order. Only the fields crozier consumes are modeled;
//! unknown keys are ignored so real-world specs still parse.

use std::path::Path;

use indexmap::IndexMap;
use serde::Deserialize;

use crate::error::{Error, Result};

/// A parsed OpenAPI document.
#[derive(Debug, Deserialize)]
pub struct OpenApi {
    /// The `openapi` version string (e.g. `3.0.1`).
    #[serde(default)]
    pub openapi: String,
    /// Document metadata.
    #[serde(default)]
    pub info: Info,
    /// Reusable components; crozier reads `components.schemas`.
    #[serde(default)]
    pub components: Components,
}

/// The `info` block.
#[derive(Debug, Default, Deserialize)]
pub struct Info {
    /// API title — the default basis for the generated package name.
    #[serde(default)]
    pub title: String,
    /// API version string (unused by generation today).
    #[serde(default)]
    pub version: String,
}

/// The `components` block.
#[derive(Debug, Default, Deserialize)]
pub struct Components {
    /// Named schemas, in document order.
    #[serde(default)]
    pub schemas: IndexMap<String, Schema>,
}

/// A JSON-Schema-ish node. A node is either a `$ref` (when [`Schema::reference`]
/// is set) or an inline schema described by the remaining fields.
#[derive(Debug, Default, Clone, Deserialize)]
pub struct Schema {
    /// A `$ref` pointer, e.g. `#/components/schemas/User`.
    #[serde(rename = "$ref", default)]
    pub reference: Option<String>,
    /// The schema `type` (`object`, `string`, `array`, ...). A single string in
    /// 3.0; the first entry is used if a 3.1 list is given.
    #[serde(rename = "type", default)]
    pub ty: Option<TypeField>,
    /// Format qualifier (`date-time`, `uuid`, `base64`, ...).
    #[serde(default)]
    pub format: Option<String>,
    /// Object properties, in document order.
    #[serde(default)]
    pub properties: IndexMap<String, Schema>,
    /// Required property names.
    #[serde(default)]
    pub required: Vec<String>,
    /// Array item schema.
    #[serde(default)]
    pub items: Option<Box<Schema>>,
    /// `additionalProperties` — a bool or a schema.
    #[serde(rename = "additionalProperties", default)]
    pub additional_properties: Option<AdditionalProperties>,
    /// Enum values (strings for the cases crozier generates).
    #[serde(rename = "enum", default)]
    pub enum_values: Option<Vec<serde_json::Value>>,
    /// `oneOf` variants.
    #[serde(rename = "oneOf", default)]
    pub one_of: Option<Vec<Schema>>,
    /// `anyOf` variants.
    #[serde(rename = "anyOf", default)]
    pub any_of: Option<Vec<Schema>>,
    /// `allOf` members.
    #[serde(rename = "allOf", default)]
    pub all_of: Option<Vec<Schema>>,
    /// Human description; becomes a docstring.
    #[serde(default)]
    pub description: Option<String>,
    /// OpenAPI 3.0 nullability.
    #[serde(default)]
    pub nullable: Option<bool>,
}

/// `type` as a single string or (3.1) a list of strings.
#[derive(Debug, Clone, Deserialize)]
#[serde(untagged)]
pub enum TypeField {
    /// A single type name.
    Single(String),
    /// A list of type names (3.1); crozier uses the first non-`null` entry.
    Multiple(Vec<String>),
}

impl TypeField {
    /// The primary type name, ignoring a `null` companion in 3.1 lists.
    #[must_use]
    pub fn primary(&self) -> Option<&str> {
        match self {
            TypeField::Single(s) => Some(s.as_str()),
            TypeField::Multiple(v) => v.iter().find(|s| *s != "null").map(String::as_str),
        }
    }
}

/// `additionalProperties`: either a boolean flag or a value schema.
#[derive(Debug, Clone, Deserialize)]
#[serde(untagged)]
pub enum AdditionalProperties {
    /// `true`/`false`.
    Bool(bool),
    /// A schema describing the map's values.
    Schema(Box<Schema>),
}

impl Schema {
    /// Is this node a `$ref`?
    #[must_use]
    pub fn is_ref(&self) -> bool {
        self.reference.is_some()
    }
}

/// Load and parse an OpenAPI document, dispatching on the file extension.
pub fn load(path: &Path) -> Result<OpenApi> {
    let text = std::fs::read_to_string(path).map_err(|source| Error::ReadSpec {
        path: path.to_path_buf(),
        source,
    })?;

    let ext = path
        .extension()
        .and_then(|e| e.to_str())
        .map(str::to_ascii_lowercase);

    let doc: OpenApi = match ext.as_deref() {
        Some("yml" | "yaml") => {
            serde_yaml_ng::from_str(&text).map_err(|e| Error::ParseSpec {
                path: path.to_path_buf(),
                message: e.to_string(),
            })?
        }
        Some("json") => serde_json::from_str(&text).map_err(|e| Error::ParseSpec {
            path: path.to_path_buf(),
            message: e.to_string(),
        })?,
        _ => {
            return Err(Error::UnknownSpecFormat {
                path: path.to_path_buf(),
            })
        }
    };

    if doc.openapi.is_empty() {
        return Err(Error::InvalidSpec {
            path: path.to_path_buf(),
            message: "missing `openapi` version field; is this an OpenAPI document?".to_string(),
        });
    }
    if !doc.openapi.starts_with('3') {
        return Err(Error::InvalidSpec {
            path: path.to_path_buf(),
            message: format!(
                "unsupported OpenAPI version `{}`; crozier supports 3.x",
                doc.openapi
            ),
        });
    }

    Ok(doc)
}
