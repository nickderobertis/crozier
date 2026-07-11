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
    /// API operations, keyed by URL path, in document order.
    #[serde(default)]
    pub paths: IndexMap<String, PathItem>,
    /// Document-wide default security requirement; an operation without its own
    /// `security` inherits this.
    #[serde(default)]
    pub security: Option<Vec<SecurityRequirement>>,
}

/// One security requirement: a map of scheme name → scopes. An empty map (`{}`)
/// means optional auth; an empty list at the operation means no auth.
pub type SecurityRequirement = IndexMap<String, Vec<String>>;

/// A declared authentication scheme (`components.securitySchemes`). Only the
/// fields crozier needs to shape the client wrapper are modeled. The closed
/// vocabularies (`type`, `scheme`, `in`) are enums with an `Other` fallback so an
/// unknown value is explicit rather than a stray string compared downstream.
#[derive(Debug, Default, Clone, Deserialize)]
pub struct SecurityScheme {
    /// `type`: `apiKey`, `http`, `oauth2`, ...
    #[serde(rename = "type", default)]
    pub ty: SecuritySchemeType,
    /// For `type: http`, the scheme (`bearer`, `basic`).
    #[serde(default)]
    pub scheme: Option<HttpAuthScheme>,
    /// For `type: apiKey`, the header/query/cookie name carrying the key.
    #[serde(default)]
    pub name: Option<String>,
    /// For `type: apiKey`, the location (`header`, `query`, `cookie`); reuses the
    /// parameter `in` vocabulary.
    #[serde(rename = "in", default)]
    pub location: Option<ParameterLocation>,
}

/// The `type` of a security scheme, per OpenAPI's closed vocabulary. An unknown
/// value deserializes to [`SecuritySchemeType::Other`] so a malformed spec parses.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Default, Deserialize)]
pub enum SecuritySchemeType {
    /// `apiKey`.
    #[serde(rename = "apiKey")]
    ApiKey,
    /// `http`.
    #[serde(rename = "http")]
    Http,
    /// `oauth2`.
    #[serde(rename = "oauth2")]
    OAuth2,
    /// `openIdConnect`.
    #[serde(rename = "openIdConnect")]
    OpenIdConnect,
    /// `mutualTLS`.
    #[serde(rename = "mutualTLS")]
    MutualTls,
    /// Any other/unrecognized (or absent) type.
    #[serde(other)]
    #[default]
    Other,
}

/// The `scheme` of an `http` security scheme. Only `bearer` (which crozier
/// reproduces) and `basic` are named; anything else is [`HttpAuthScheme::Other`].
#[derive(Debug, Clone, Copy, PartialEq, Eq, Deserialize)]
#[serde(rename_all = "lowercase")]
pub enum HttpAuthScheme {
    /// `bearer`.
    Bearer,
    /// `basic`.
    Basic,
    /// Any other HTTP auth scheme.
    #[serde(other)]
    Other,
}

/// One path's operations, keyed by HTTP method. Only the methods crozier
/// generates are modeled.
#[derive(Debug, Default, Deserialize)]
pub struct PathItem {
    /// `GET` operation.
    #[serde(default)]
    pub get: Option<Operation>,
    /// `POST` operation.
    #[serde(default)]
    pub post: Option<Operation>,
    /// `PUT` operation.
    #[serde(default)]
    pub put: Option<Operation>,
    /// `DELETE` operation.
    #[serde(default)]
    pub delete: Option<Operation>,
    /// `PATCH` operation.
    #[serde(default)]
    pub patch: Option<Operation>,
}

impl PathItem {
    /// The operations present on this path, paired with their HTTP method (in a
    /// stable method order).
    #[must_use]
    pub fn operations(&self) -> Vec<(&'static str, &Operation)> {
        [
            ("GET", &self.get),
            ("POST", &self.post),
            ("PUT", &self.put),
            ("DELETE", &self.delete),
            ("PATCH", &self.patch),
        ]
        .into_iter()
        .filter_map(|(method, op)| op.as_ref().map(|o| (method, o)))
        .collect()
    }
}

/// A single API operation.
#[derive(Debug, Deserialize)]
pub struct Operation {
    /// The operation identifier, `{group}_{camelMethodName}`.
    #[serde(rename = "operationId", default)]
    pub operation_id: String,
    /// Tags; the first groups the operation into a client.
    #[serde(default)]
    pub tags: Vec<String>,
    /// A human description; becomes the method docstring's summary line.
    #[serde(default)]
    pub description: Option<String>,
    /// Path/query/header parameters, in document order.
    #[serde(default)]
    pub parameters: Vec<Parameter>,
    /// The request body, if any.
    #[serde(rename = "requestBody", default)]
    pub request_body: Option<RequestBody>,
    /// Responses, keyed by status code (or `default`), in document order.
    #[serde(default)]
    pub responses: IndexMap<String, Response>,
    /// Per-operation security requirement. `Some(vec![])` opts out of the
    /// document default (no auth); `None` inherits it.
    #[serde(default)]
    pub security: Option<Vec<SecurityRequirement>>,
}

/// An operation parameter (path/query/header/cookie). Only inline parameters are
/// modeled; a `$ref` parameter deserializes with an empty name and no location.
#[derive(Debug, Default, Deserialize)]
pub struct Parameter {
    /// Parameter name (the wire name; also the path placeholder for `in: path`).
    #[serde(default)]
    pub name: String,
    /// Location (`in`). `None` when absent (e.g. a `$ref` parameter).
    #[serde(rename = "in", default)]
    pub location: Option<ParameterLocation>,
    /// Whether the parameter is required.
    #[serde(default)]
    pub required: Option<bool>,
    /// Human-readable description, surfaced in the method docstring.
    #[serde(default)]
    pub description: Option<String>,
    /// The parameter's value schema.
    #[serde(default)]
    pub schema: Option<Schema>,
}

/// A parameter's location, per OpenAPI's closed `in` vocabulary. Modeling it as
/// an enum (rather than a bare string) makes an invalid location unrepresentable
/// and forces exhaustive handling downstream; an unknown or non-standard value
/// deserializes to [`ParameterLocation::Other`] so a malformed spec still parses.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Deserialize)]
#[serde(rename_all = "lowercase")]
pub enum ParameterLocation {
    /// `in: path`.
    Path,
    /// `in: query`.
    Query,
    /// `in: header`.
    Header,
    /// `in: cookie`.
    Cookie,
    /// Any other/unrecognized location.
    #[serde(other)]
    Other,
}

/// A request body: a content-type → media-type map plus a required flag.
#[derive(Debug, Default, Deserialize)]
pub struct RequestBody {
    /// Whether the body is required.
    #[serde(default)]
    pub required: Option<bool>,
    /// Content, keyed by media type (e.g. `application/json`).
    #[serde(default)]
    pub content: IndexMap<String, MediaType>,
}

/// One response entry.
#[derive(Debug, Default, Deserialize)]
pub struct Response {
    /// Content, keyed by media type.
    #[serde(default)]
    pub content: IndexMap<String, MediaType>,
}

/// A media-type object carrying the body/response schema.
#[derive(Debug, Default, Deserialize)]
pub struct MediaType {
    /// The schema for this media type.
    #[serde(default)]
    pub schema: Option<Schema>,
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
    /// Declared authentication schemes, in document order.
    #[serde(rename = "securitySchemes", default)]
    pub security_schemes: IndexMap<String, SecurityScheme>,
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
    /// `uniqueItems` — a `true` array maps to `typing.Set` rather than `List`.
    #[serde(rename = "uniqueItems", default)]
    pub unique_items: Option<bool>,
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
    /// `readOnly`: a server-populated property. Fern renders it as an optional
    /// field even when listed in `required`.
    #[serde(rename = "readOnly", default)]
    pub read_only: Option<bool>,
    /// A `oneOf`/`anyOf` discriminator: the property that selects the variant and
    /// (optionally) an explicit value → `$ref` mapping.
    #[serde(default)]
    pub discriminator: Option<Discriminator>,
}

/// A `oneOf`/`anyOf` discriminator object.
#[derive(Debug, Default, Clone, Deserialize)]
pub struct Discriminator {
    /// The property whose value selects the union variant.
    #[serde(rename = "propertyName", default)]
    pub property_name: String,
    /// Explicit value → `$ref` mapping, in document order. When absent, the value
    /// is inferred from each variant's own discriminator-property enum.
    #[serde(default)]
    pub mapping: IndexMap<String, String>,
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
        Some("yml" | "yaml") => serde_yaml_ng::from_str(&text).map_err(|e| Error::ParseSpec {
            path: path.to_path_buf(),
            message: e.to_string(),
        })?,
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
    // crozier derives each client's module and method names from `operationId`,
    // so require it on every operation rather than emitting a malformed path.
    for (url, item) in &doc.paths {
        for (method, op) in item.operations() {
            if op.operation_id.trim().is_empty() {
                return Err(Error::InvalidSpec {
                    path: path.to_path_buf(),
                    message: format!(
                        "operation `{method} {url}` has no `operationId`; crozier requires one to name the client"
                    ),
                });
            }
        }
    }
    // An apiKey scheme's `name` (the header/query/cookie carrying the key) is
    // required by OpenAPI; without it the generated header name would be empty.
    // Fail at the boundary rather than emit a broken client.
    for (scheme_name, scheme) in &doc.components.security_schemes {
        if scheme.ty == SecuritySchemeType::ApiKey
            && scheme.name.as_deref().unwrap_or("").trim().is_empty()
        {
            return Err(Error::InvalidSpec {
                path: path.to_path_buf(),
                message: format!(
                    "apiKey security scheme `{scheme_name}` is missing its required `name` (the parameter carrying the key)"
                ),
            });
        }
    }

    Ok(doc)
}
