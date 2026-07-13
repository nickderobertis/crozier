//! A pragmatic serde model of the subset of OpenAPI 3.x that crozier reads.
//!
//! Ordering matters for byte-exact output: object properties and component
//! schemas are [`IndexMap`]s so their document order survives into generated
//! field order and file order. Only the fields crozier consumes are modeled;
//! unknown keys are ignored so real-world specs still parse.
//!
//! # Fern-compatible extensions
//!
//! crozier honours a handful of `x-*` vendor extensions that steer generation
//! (audience labels, per-node ignore). Every one follows a single **dual-header
//! policy** so a spec authored for Fern works against crozier unchanged:
//!
//! - **Input is permissive.** Both the `x-crozier-*` and the Fern `x-fern-*`
//!   spelling are read for every supported extension.
//! - **`x-crozier-*` is canonical.** It is the form crozier documents and the form
//!   that *wins* when both spellings appear on the same node — the `x-fern-*`
//!   value applies only as a fallback when the `x-crozier-*` one is absent. This is
//!   what lets an explicit `x-crozier-ignore: false` override an `x-fern-ignore:
//!   true`.
//! - **crozier only ever emits the crozier variant.** It never writes `x-fern-*`,
//!   mirroring how it renders `X-Crozier-*` SDK headers where Fern emits `X-Fern-*`.
//!
//! The precedence is applied in the field accessors ([`Operation::audiences`],
//! [`Operation::ignored`], [`Schema::ignored`]); the paired serde fields exist only
//! to carry the two raw spellings.

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
    /// Declared API servers; the first drives the generated environment enum.
    #[serde(default)]
    pub servers: Vec<Server>,
}

/// One entry from the document's `servers` list: a base URL and an optional
/// human description (which names the generated environment member).
#[derive(Debug, Default, Clone, Deserialize)]
pub struct Server {
    /// The server base URL (the environment member's value).
    #[serde(default)]
    pub url: String,
    /// A human description; uppercased, it names the environment member.
    #[serde(default)]
    pub description: Option<String>,
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
    /// Parameters declared once on the path item and shared by every operation
    /// under it (a common real-world pattern for path params). Merged into each
    /// operation at load time by [`normalize_parameters`]; empty after that pass.
    #[serde(default)]
    pub parameters: Vec<Parameter>,
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

    /// Mutable references to each method slot, in the same stable order as
    /// [`PathItem::operations`], for filters that clear operations in place.
    fn operation_slots(&mut self) -> [&mut Option<Operation>; 5] {
        [
            &mut self.get,
            &mut self.post,
            &mut self.put,
            &mut self.delete,
            &mut self.patch,
        ]
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
    /// `x-crozier-audiences`: audience labels this operation belongs to (canonical
    /// spelling). Read via [`Operation::audiences`], which also honours the
    /// `x-fern-audiences` variant per the [dual-header policy](self#fern-compatible-extensions).
    #[serde(rename = "x-crozier-audiences", default)]
    audiences_crozier: Option<Vec<String>>,
    /// `x-fern-audiences`: the Fern spelling of the audience labels, accepted so a
    /// spec authored for Fern filters unchanged. Superseded by
    /// `x-crozier-audiences` when both appear (see [`Operation::audiences`]).
    #[serde(rename = "x-fern-audiences", default)]
    audiences_fern: Option<Vec<String>>,
    /// `x-crozier-ignore`: exclude this operation from generation (canonical
    /// spelling). Read via [`Operation::ignored`], which also honours the
    /// `x-fern-ignore` variant per the [dual-header policy](self#fern-compatible-extensions).
    #[serde(rename = "x-crozier-ignore", default)]
    ignore_crozier: Option<bool>,
    /// `x-fern-ignore`: the Fern spelling of the ignore flag, accepted so a
    /// Fern-annotated spec drops the same operations. Superseded by
    /// `x-crozier-ignore` when both appear (see [`Operation::ignored`]).
    #[serde(rename = "x-fern-ignore", default)]
    ignore_fern: Option<bool>,
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

impl Operation {
    /// The operation's audience labels, canonicalizing on the `x-crozier-audiences`
    /// spelling: it wins outright when present, and only when it is absent does the
    /// `x-fern-audiences` fallback apply (see the [dual-header
    /// policy](self#fern-compatible-extensions)). Empty means unlabelled.
    #[must_use]
    pub fn audiences(&self) -> &[String] {
        self.audiences_crozier
            .as_deref()
            .or(self.audiences_fern.as_deref())
            .unwrap_or(&[])
    }

    /// Whether this operation is marked ignored and must be excluded from
    /// generation. The `x-crozier-ignore` flag is canonical — an explicit
    /// `x-crozier-ignore: false` keeps the operation even when `x-fern-ignore: true`
    /// is also present, which is what makes the Overlay-driven "ignore all, then
    /// un-ignore a few" pattern work (see the [dual-header
    /// policy](self#fern-compatible-extensions)).
    #[must_use]
    pub fn ignored(&self) -> bool {
        self.ignore_crozier.or(self.ignore_fern).unwrap_or(false)
    }
}

/// An operation parameter (path/query/header/cookie). A `$ref` parameter carries
/// its pointer in [`Parameter::reference`] and is resolved against
/// `components.parameters` at load time (see [`normalize_parameters`]); after that
/// pass every surviving parameter is inline.
#[derive(Debug, Default, Clone, Deserialize)]
pub struct Parameter {
    /// A `$ref` pointer to a `components.parameters` entry, e.g.
    /// `#/components/parameters/consumerId`. Resolved to the referenced parameter
    /// by [`normalize_parameters`]; `None` for an inline parameter.
    #[serde(rename = "$ref", default)]
    pub reference: Option<String>,
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
    /// A parameter-level `example` value (Fern shows it in the worked snippet).
    #[serde(default)]
    pub example: Option<serde_json::Value>,
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
#[derive(Debug, Default, Clone, Deserialize)]
pub struct Response {
    /// A `$ref` pointer to a `components.responses` entry, e.g.
    /// `#/components/responses/GetActivitiesResponse`. Resolved to the referenced
    /// response by [`normalize_responses`]; `None` for an inline response.
    #[serde(rename = "$ref", default)]
    pub reference: Option<String>,
    /// Human description of the response; Fern surfaces it in the method
    /// docstring's `Returns` section.
    #[serde(default)]
    pub description: Option<String>,
    /// Content, keyed by media type.
    #[serde(default)]
    pub content: IndexMap<String, MediaType>,
}

/// A media-type object carrying the body/response schema.
#[derive(Debug, Default, Clone, Deserialize)]
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
    /// Reusable parameters (`components.parameters`), in document order. A `$ref`
    /// parameter on an operation resolves against this map at load time (see
    /// [`normalize_parameters`]).
    #[serde(default)]
    pub parameters: IndexMap<String, Parameter>,
    /// Reusable responses (`components.responses`), in document order. A `$ref`
    /// response on an operation resolves against this map at load time (see
    /// [`normalize_responses`]).
    #[serde(default)]
    pub responses: IndexMap<String, Response>,
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
    /// Object properties, in document order. Deserialized leniently: a property
    /// whose value is not a schema object degrades to a malformed unknown node
    /// rather than aborting the parse (issue #86).
    #[serde(default, deserialize_with = "de_properties")]
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
    /// A schema-level `example` value (Fern shows it in the worked snippet).
    #[serde(default)]
    pub example: Option<serde_json::Value>,
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
    /// `x-crozier-ignore`: exclude this component schema from generation (canonical
    /// spelling). Read via [`Schema::ignored`] rather than directly — that accessor
    /// applies the precedence — which also honours the `x-fern-ignore` variant per
    /// the [dual-header policy](self#fern-compatible-extensions).
    #[serde(rename = "x-crozier-ignore", default)]
    pub ignore_crozier: Option<bool>,
    /// `x-fern-ignore`: the Fern spelling of the ignore flag on a schema. Superseded
    /// by `x-crozier-ignore` when both appear (see [`Schema::ignored`]).
    #[serde(rename = "x-fern-ignore", default)]
    pub ignore_fern: Option<bool>,
    /// Set when this node stood where a schema object was expected but the document
    /// carried a non-object value there (e.g. a JSON array, from a `required` list
    /// misplaced inside `properties`). Not a wire field — the `properties`
    /// deserializer sets it so the node degrades to Fern's unknown type
    /// (`Optional[Any]`) instead of serde positionally parsing the sequence into a
    /// bogus `$ref` (issue #86).
    #[serde(skip)]
    pub malformed: bool,
}

impl Schema {
    /// Whether this component schema is marked ignored and must not be emitted. The
    /// `x-crozier-ignore` flag is canonical: an explicit `false` keeps the schema
    /// even when `x-fern-ignore: true` is present (see the [dual-header
    /// policy](self#fern-compatible-extensions)).
    #[must_use]
    pub fn ignored(&self) -> bool {
        self.ignore_crozier.or(self.ignore_fern).unwrap_or(false)
    }
}

/// Deserialize an object's `properties` map, tolerating a value that is not a
/// schema object. serde's derived struct deserialization fills fields positionally
/// from a JSON/YAML sequence, so a `required: [..]` list misplaced *inside*
/// `properties` would otherwise be read as a property whose first element becomes a
/// bogus `$ref` (issue #86). Instead, any non-map value degrades to a malformed
/// node that renders as Fern's unknown type — matching Fern's tolerance of the
/// same document.
fn de_properties<'de, D>(deserializer: D) -> std::result::Result<IndexMap<String, Schema>, D::Error>
where
    D: serde::Deserializer<'de>,
{
    let raw: IndexMap<String, MaybeSchema> = IndexMap::deserialize(deserializer)?;
    Ok(raw.into_iter().map(|(k, v)| (k, v.0)).collect())
}

/// A property value that is either a real schema object or — when the document put
/// a non-object there — a [`Schema::malformed`] degrade-to-unknown node.
struct MaybeSchema(Schema);

impl<'de> Deserialize<'de> for MaybeSchema {
    fn deserialize<D>(deserializer: D) -> std::result::Result<Self, D::Error>
    where
        D: serde::Deserializer<'de>,
    {
        deserializer.deserialize_any(MaybeSchemaVisitor)
    }
}

struct MaybeSchemaVisitor;

impl<'de> serde::de::Visitor<'de> for MaybeSchemaVisitor {
    type Value = MaybeSchema;

    fn expecting(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        f.write_str("a schema object or a non-object value to degrade")
    }

    /// A map is a real schema — delegate to the derived struct deserializer.
    fn visit_map<A>(self, map: A) -> std::result::Result<Self::Value, A::Error>
    where
        A: serde::de::MapAccess<'de>,
    {
        Schema::deserialize(serde::de::value::MapAccessDeserializer::new(map)).map(MaybeSchema)
    }

    /// A sequence where a schema was expected: drain it and degrade.
    fn visit_seq<A>(self, mut seq: A) -> std::result::Result<Self::Value, A::Error>
    where
        A: serde::de::SeqAccess<'de>,
    {
        while seq.next_element::<serde::de::IgnoredAny>()?.is_some() {}
        Ok(MaybeSchema(malformed_schema()))
    }

    // Any other scalar standing in for a schema degrades the same way.
    fn visit_str<E>(self, _v: &str) -> std::result::Result<Self::Value, E> {
        Ok(MaybeSchema(malformed_schema()))
    }
    fn visit_bool<E>(self, _v: bool) -> std::result::Result<Self::Value, E> {
        Ok(MaybeSchema(malformed_schema()))
    }
    fn visit_i64<E>(self, _v: i64) -> std::result::Result<Self::Value, E> {
        Ok(MaybeSchema(malformed_schema()))
    }
    fn visit_u64<E>(self, _v: u64) -> std::result::Result<Self::Value, E> {
        Ok(MaybeSchema(malformed_schema()))
    }
    fn visit_f64<E>(self, _v: f64) -> std::result::Result<Self::Value, E> {
        Ok(MaybeSchema(malformed_schema()))
    }
    fn visit_none<E>(self) -> std::result::Result<Self::Value, E> {
        Ok(MaybeSchema(malformed_schema()))
    }
    fn visit_unit<E>(self) -> std::result::Result<Self::Value, E> {
        Ok(MaybeSchema(malformed_schema()))
    }
}

/// A schema node flagged [`Schema::malformed`]: an unknown value in every other
/// respect, so it renders as Fern's `Optional[Any]`.
fn malformed_schema() -> Schema {
    Schema {
        malformed: true,
        ..Schema::default()
    }
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

    let mut doc: OpenApi = match ext.as_deref() {
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
    // `operationId` is optional in OpenAPI and real specs omit it. crozier no
    // longer requires it: the IR's endpoint naming synthesizes a client group and
    // method from the operation's tag and route when it is absent (see
    // `crate::ir::endpoint_method_name`), so a spec without one still generates.
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

    normalize_parameters(&mut doc);
    normalize_responses(&mut doc);

    Ok(doc)
}

/// Resolve a response that is a `$ref` into `components.responses` to the
/// referenced response; an inline response (or an unresolvable pointer) is returned
/// unchanged. Only `#/components/responses/*` pointers are resolved, one level deep.
fn resolve_response(response: &Response, defs: &IndexMap<String, Response>) -> Response {
    if let Some(name) = response
        .reference
        .as_deref()
        .and_then(|r| r.strip_prefix("#/components/responses/"))
    {
        if let Some(target) = defs.get(name) {
            return target.clone();
        }
    }
    response.clone()
}

/// Inline every `components.responses` `$ref` an operation points at, so generation
/// sees each response's real `content` (and thus its response model) rather than an
/// empty `$ref` shell.
///
/// Real specs frequently declare a status → response mapping as
/// `"200": { $ref: "#/components/responses/GetActivitiesResponse" }`, sharing one
/// response across operations. crozier reads only an inline `Response`, so an
/// unresolved `$ref` looks like a response with no body — the endpoint generates
/// `-> None` and the response schema is never reached (and, if it was only reachable
/// through such a response, never generated). Resolving here restores both. Inert on
/// specs that inline every response (every synthetic fixture).
fn normalize_responses(doc: &mut OpenApi) {
    let defs = doc.components.responses.clone();
    for item in doc.paths.values_mut() {
        for slot in item.operation_slots() {
            let Some(op) = slot else { continue };
            for response in op.responses.values_mut() {
                *response = resolve_response(response, &defs);
            }
        }
    }
}

/// Resolve a parameter that is a `$ref` into `components.parameters` to the
/// referenced parameter; an inline parameter (or an unresolvable pointer) is
/// returned unchanged. Only `#/components/parameters/*` pointers are resolved, one
/// level deep — the shape real specs use.
fn resolve_parameter(param: &Parameter, defs: &IndexMap<String, Parameter>) -> Parameter {
    if let Some(name) = param
        .reference
        .as_deref()
        .and_then(|r| r.strip_prefix("#/components/parameters/"))
    {
        if let Some(target) = defs.get(name) {
            return target.clone();
        }
    }
    param.clone()
}

/// Fold `components.parameters` `$ref`s and path-item-level parameters into each
/// operation's own parameter list, so downstream generation sees one flat, inline
/// list per operation.
///
/// OpenAPI lets any parameter be a `$ref` into `components.parameters` (real specs
/// share common query/header params like `raw` or `consumerId` this way) and lets
/// parameters be declared once on a path item, shared by every method on that path
/// (the usual home for path params like `{id}`). crozier's generation reads only
/// `operation.parameters` and only inline entries, so without this pass a shared or
/// referenced parameter is dropped — the endpoint loses it entirely, or a path
/// parameter's `{placeholder}` is interpolated against a name that never made it
/// into the method signature. Here every path-level and operation-level `$ref` is
/// resolved, then the resolved path-level parameters are merged into each
/// operation, with an operation-level parameter overriding a path-level one of the
/// same name and location (per the spec). Inert on specs that already inline every
/// parameter per operation (every synthetic fixture), so it changes no existing
/// output.
fn normalize_parameters(doc: &mut OpenApi) {
    let defs = doc.components.parameters.clone();
    for item in doc.paths.values_mut() {
        let shared: Vec<Parameter> = item
            .parameters
            .iter()
            .map(|p| resolve_parameter(p, &defs))
            .collect();
        for slot in item.operation_slots() {
            let Some(op) = slot else { continue };
            let mut merged = shared.clone();
            for own in &op.parameters {
                let own = resolve_parameter(own, &defs);
                if let Some(existing) = merged
                    .iter_mut()
                    .find(|p| p.name == own.name && p.location == own.location)
                {
                    *existing = own;
                } else {
                    merged.push(own);
                }
            }
            op.parameters = merged;
        }
        item.parameters = Vec::new();
    }
}

/// Prune the document to a set of audiences (the `x-crozier-audiences` /
/// `x-fern-audiences` filter, issue #41 gap 3, read via [`Operation::audiences`]).
/// No-op when `audiences` is empty (the whole API is generated).
///
/// The default (permissive) mode keeps an operation when it carries a matching
/// audience **or** carries none at all (unlabelled operations are always kept),
/// dropping only ops labelled solely with non-matching audiences. When `strict` is
/// set, un-annotated operations are also excluded, so **only** operations carrying
/// a matching audience survive — Fern's exclusive filtering, the way to carve a
/// minimal, self-contained SDK out of a mostly-un-annotated API (issue #62).
///
/// Either way, crozier then emits just the **transitive `$ref` closure** of the
/// surviving operations' parameter, request, and response schemas — every other
/// `components.schemas` entry (even unlabelled ones no surviving operation reaches,
/// like an internal-only type) is removed, so
/// the pruned SDK is self-contained. Property/schema-level `x-crozier-audiences`
/// are not yet honoured (a follow-up); only operation-level filtering is applied.
pub fn filter_by_audience(doc: &mut OpenApi, audiences: &[String], strict: bool) {
    if audiences.is_empty() {
        return;
    }
    let keep = |op: &Operation| {
        let labels = op.audiences();
        if labels.is_empty() {
            // Un-annotated ops: kept in permissive mode, excluded in strict mode.
            !strict
        } else {
            labels.iter().any(|a| audiences.contains(a))
        }
    };
    for item in doc.paths.values_mut() {
        for slot in item.operation_slots() {
            if slot.as_ref().is_some_and(|op| !keep(op)) {
                *slot = None;
            }
        }
    }
    // Drop paths whose every operation was filtered out.
    doc.paths.retain(|_, item| !item.operations().is_empty());

    // Emit only the transitive `$ref` closure of the surviving operations.
    let seed = operation_schema_seed(doc.paths.values().flat_map(|i| i.operations()));
    let reached = expand_schema_closure(doc, seed);
    doc.components.schemas.retain(|k, _| reached.contains(k));
}

/// Drop operations and component schemas marked with the ignore extension
/// (`x-crozier-ignore` / `x-fern-ignore`, issue #78), along with any schema that is
/// no longer reachable once the ignored operations are gone.
///
/// An operation whose [`Operation::ignored`] is set is removed (and its path with
/// it, if it becomes empty); a component whose [`Schema::ignored`] is set is never
/// emitted. Beyond those explicit removals, a schema is pruned when it *was*
/// reachable from a removed operation (or an ignored schema's own `$ref`s) yet is
/// *not* reachable from any surviving operation — i.e. it fell out of the SDK's
/// transitive closure as a result of the ignore. Standalone component schemas that
/// no operation references are left untouched, so this is inert on a spec with no
/// ignore markers and never changes a full, unfiltered generation.
///
/// Unlike [`filter_by_audience`], the ignore honours **both** operation- and
/// schema-level markers, per the [dual-header policy](self#fern-compatible-extensions).
pub fn filter_ignored(doc: &mut OpenApi) {
    let ignored_schemas: std::collections::BTreeSet<String> = doc
        .components
        .schemas
        .iter()
        .filter(|(_, s)| s.ignored())
        .map(|(k, _)| k.clone())
        .collect();
    let has_ignored_op = doc
        .paths
        .values()
        .flat_map(|i| i.operations())
        .any(|(_, op)| op.ignored());
    if ignored_schemas.is_empty() && !has_ignored_op {
        return;
    }

    // Schemas reachable from the operations (and schemas) that are being removed.
    let mut removed_seed = operation_schema_seed(
        doc.paths
            .values()
            .flat_map(|i| i.operations())
            .filter(|(_, op)| op.ignored()),
    );
    for key in &ignored_schemas {
        removed_seed.insert(key.clone());
        if let Some(s) = doc.components.schemas.get(key) {
            collect_schema_refs(s, &mut removed_seed);
        }
    }
    let reachable_from_removed = expand_schema_closure(doc, removed_seed);

    // Remove the ignored operations, then drop paths that are now empty.
    for item in doc.paths.values_mut() {
        for slot in item.operation_slots() {
            if slot.as_ref().is_some_and(|op| op.ignored()) {
                *slot = None;
            }
        }
    }
    doc.paths.retain(|_, item| !item.operations().is_empty());

    // Schemas still reachable from the operations that survived.
    let kept_seed = operation_schema_seed(doc.paths.values().flat_map(|i| i.operations()));
    let reachable_from_kept = expand_schema_closure(doc, kept_seed);

    doc.components.schemas.retain(|key, _| {
        if ignored_schemas.contains(key) {
            return false;
        }
        // Prune a schema that became unreferenced because an ignored op/schema was
        // its only path in; keep everything a surviving op still reaches and every
        // standalone schema no operation referenced in the first place.
        let became_unreferenced =
            reachable_from_removed.contains(key) && !reachable_from_kept.contains(key);
        !became_unreferenced
    });
}

/// Seed a schema-closure walk with every `#/components/schemas/*` key the given
/// operations reference directly through their parameter, request-body, and
/// response schemas.
fn operation_schema_seed<'a>(
    ops: impl IntoIterator<Item = (&'static str, &'a Operation)>,
) -> std::collections::BTreeSet<String> {
    let mut seed = std::collections::BTreeSet::new();
    for (_, op) in ops {
        for p in &op.parameters {
            if let Some(s) = &p.schema {
                collect_schema_refs(s, &mut seed);
            }
        }
        let bodies = op
            .request_body
            .iter()
            .flat_map(|rb| rb.content.values())
            .chain(op.responses.values().flat_map(|r| r.content.values()));
        for mt in bodies {
            if let Some(s) = &mt.schema {
                collect_schema_refs(s, &mut seed);
            }
        }
    }
    seed
}

/// Expand a seed set of schema keys to its transitive `$ref` closure through
/// `components.schemas`.
fn expand_schema_closure(
    doc: &OpenApi,
    seed: std::collections::BTreeSet<String>,
) -> std::collections::BTreeSet<String> {
    let mut reached = std::collections::BTreeSet::new();
    let mut queue: Vec<String> = seed.into_iter().collect();
    while let Some(key) = queue.pop() {
        if !reached.insert(key.clone()) {
            continue;
        }
        if let Some(schema) = doc.components.schemas.get(&key) {
            let mut refs = std::collections::BTreeSet::new();
            collect_schema_refs(schema, &mut refs);
            queue.extend(refs.into_iter().filter(|r| !reached.contains(r)));
        }
    }
    reached
}

/// Collect every `#/components/schemas/*` reference reachable within a schema
/// node (the node itself if it is a `$ref`, plus nested properties, array items,
/// `additionalProperties`, `allOf`/`oneOf`/`anyOf` members, and discriminator
/// mappings), inserting each target's schema key into `out`.
fn collect_schema_refs(schema: &Schema, out: &mut std::collections::BTreeSet<String>) {
    const PREFIX: &str = "#/components/schemas/";
    if let Some(key) = schema
        .reference
        .as_deref()
        .and_then(|r| r.strip_prefix(PREFIX))
    {
        out.insert(key.to_string());
    }
    for s in schema.properties.values() {
        collect_schema_refs(s, out);
    }
    if let Some(items) = &schema.items {
        collect_schema_refs(items, out);
    }
    if let Some(AdditionalProperties::Schema(s)) = &schema.additional_properties {
        collect_schema_refs(s, out);
    }
    for member in [&schema.one_of, &schema.any_of, &schema.all_of]
        .into_iter()
        .flatten()
        .flatten()
    {
        collect_schema_refs(member, out);
    }
    if let Some(disc) = &schema.discriminator {
        for key in disc.mapping.values().filter_map(|r| r.strip_prefix(PREFIX)) {
            out.insert(key.to_string());
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    /// Parse a YAML spec string into an [`OpenApi`] for the pure-filter unit tests.
    fn parse(spec: &str) -> OpenApi {
        serde_yaml_ng::from_str(spec).expect("valid spec")
    }

    fn op_ids(doc: &OpenApi) -> Vec<String> {
        doc.paths
            .values()
            .flat_map(|i| i.operations())
            .map(|(_, op)| op.operation_id.clone())
            .collect()
    }

    fn schema_keys(doc: &OpenApi) -> Vec<String> {
        doc.components.schemas.keys().cloned().collect()
    }

    const IGNORE_SPEC: &str = r##"
openapi: 3.0.3
info: { title: Widget API }
paths:
  /keep:
    get:
      operationId: keepOp
      responses:
        "200": { description: OK, content: { application/json: { schema: { $ref: "#/components/schemas/Keep" } } } }
  /fern:
    get:
      operationId: fernIgnoredOp
      x-fern-ignore: true
      responses:
        "200": { description: OK, content: { application/json: { schema: { $ref: "#/components/schemas/OnlyFern" } } } }
  /crozier:
    get:
      operationId: crozierIgnoredOp
      x-crozier-ignore: true
      responses:
        "200": { description: OK, content: { application/json: { schema: { $ref: "#/components/schemas/OnlyCrozier" } } } }
components:
  schemas:
    Keep: { type: object, properties: { note: { type: string } } }
    OnlyFern: { type: object, properties: { note: { type: string } } }
    OnlyCrozier: { type: object, properties: { note: { type: string } } }
"##;

    #[test]
    fn ignore_extension_drops_ops_via_both_spellings_and_their_exclusive_schemas() {
        let mut doc = parse(IGNORE_SPEC);
        filter_ignored(&mut doc);
        // Both `x-fern-ignore` and `x-crozier-ignore` operations are gone.
        assert_eq!(op_ids(&doc), ["keepOp"]);
        // The paths of the ignored ops are removed entirely.
        assert_eq!(doc.paths.keys().cloned().collect::<Vec<_>>(), ["/keep"]);
        // Schemas only the ignored ops referenced fell out of the closure; the
        // kept op's schema stays.
        assert_eq!(schema_keys(&doc), ["Keep"]);
    }

    #[test]
    fn crozier_ignore_false_overrides_fern_ignore_true() {
        // The Overlay pattern: `x-fern-ignore: true` marks the op ignored, but an
        // explicit `x-crozier-ignore: false` on the same node keeps it.
        let mut doc = parse(
            r##"
openapi: 3.0.3
info: { title: T }
paths:
  /keep:
    get:
      operationId: keptDespiteFern
      x-fern-ignore: true
      x-crozier-ignore: false
      responses: { "200": { description: OK } }
"##,
        );
        filter_ignored(&mut doc);
        assert_eq!(op_ids(&doc), ["keptDespiteFern"]);
    }

    #[test]
    fn schema_level_ignore_drops_the_component_but_keeps_referenced_ones() {
        // `Internal` is ignored outright; `Shared` is referenced by both a kept and
        // an ignored op, so it survives; `OrphanKept` is a standalone schema no op
        // references and must be left untouched (a full generation would emit it).
        let mut doc = parse(
            r##"
openapi: 3.0.3
info: { title: T }
paths:
  /keep:
    get:
      operationId: keepOp
      responses:
        "200": { description: OK, content: { application/json: { schema: { $ref: "#/components/schemas/Shared" } } } }
  /drop:
    get:
      operationId: dropOp
      x-crozier-ignore: true
      responses:
        "200": { description: OK, content: { application/json: { schema: { $ref: "#/components/schemas/Internal" } } } }
components:
  schemas:
    Shared: { type: object, properties: { note: { type: string } } }
    Internal:
      x-crozier-ignore: true
      type: object
      properties: { note: { type: string } }
    OrphanKept: { type: object, properties: { note: { type: string } } }
"##,
        );
        filter_ignored(&mut doc);
        assert_eq!(op_ids(&doc), ["keepOp"]);
        let mut kept = schema_keys(&doc);
        kept.sort();
        assert_eq!(kept, ["OrphanKept", "Shared"]);
    }

    #[test]
    fn ignore_is_a_no_op_without_any_markers() {
        // No ignore markers → the doc is untouched, including standalone schemas
        // that no operation references (so a full generation still emits them).
        let mut doc = parse(
            r##"
openapi: 3.0.3
info: { title: T }
paths:
  /keep:
    get: { operationId: keepOp, responses: { "200": { description: OK } } }
components:
  schemas:
    Standalone: { type: object, properties: { note: { type: string } } }
"##,
        );
        filter_ignored(&mut doc);
        assert_eq!(op_ids(&doc), ["keepOp"]);
        assert_eq!(schema_keys(&doc), ["Standalone"]);
    }

    #[test]
    fn audiences_accessor_prefers_crozier_then_falls_back_to_fern() {
        let both = parse(
            r##"
openapi: 3.0.3
info: { title: T }
paths:
  /a:
    get:
      operationId: a
      x-crozier-audiences: [public]
      x-fern-audiences: [internal]
      responses: { "200": { description: OK } }
"##,
        );
        let op = both.paths["/a"].get.as_ref().unwrap();
        // Canonical spelling wins outright when both are present.
        assert_eq!(op.audiences(), ["public"]);

        let fern_only = parse(
            r##"
openapi: 3.0.3
info: { title: T }
paths:
  /a:
    get:
      operationId: a
      x-fern-audiences: [internal]
      responses: { "200": { description: OK } }
"##,
        );
        // Fern spelling is the fallback when the crozier one is absent.
        let op = fern_only.paths["/a"].get.as_ref().unwrap();
        assert_eq!(op.audiences(), ["internal"]);
    }

    #[test]
    fn fern_audiences_filter_prunes_like_the_crozier_spelling() {
        // A spec annotated only for Fern filters under `--audience` unchanged.
        let mut doc = parse(
            r##"
openapi: 3.0.3
info: { title: T }
paths:
  /pub:
    get:
      operationId: pub
      x-fern-audiences: [public]
      responses:
        "200": { description: OK, content: { application/json: { schema: { $ref: "#/components/schemas/Pub" } } } }
  /int:
    get:
      operationId: int
      x-fern-audiences: [internal]
      responses:
        "200": { description: OK, content: { application/json: { schema: { $ref: "#/components/schemas/Int" } } } }
components:
  schemas:
    Pub: { type: object, properties: { note: { type: string } } }
    Int: { type: object, properties: { note: { type: string } } }
"##,
        );
        filter_by_audience(&mut doc, &["public".to_string()], false);
        assert_eq!(op_ids(&doc), ["pub"]);
        assert_eq!(schema_keys(&doc), ["Pub"]);
    }

    const REF_PARAMS_SPEC: &str = r##"
openapi: 3.0.0
info: { title: T }
paths:
  /items/{itemId}:
    parameters:
      - $ref: "#/components/parameters/ItemId"
    get:
      operationId: getItem
      parameters:
        - $ref: "#/components/parameters/Verbose"
        - name: inline
          in: query
          schema: { type: string }
      responses:
        "200": { description: OK }
components:
  parameters:
    ItemId: { name: itemId, in: path, required: true, schema: { type: string } }
    Verbose: { name: verbose, in: query, required: false, schema: { type: boolean } }
"##;

    /// `normalize_parameters` folds a path-item-level `$ref` parameter and an
    /// operation-level `$ref` parameter into the operation, resolving both against
    /// `components.parameters`, while an inline parameter is left as-is. Without
    /// this the operation would generate with none of its declared parameters (a
    /// broken client), which is why real specs that lean on parameter indirection
    /// need it. Path-level parameters lead, then the operation's own, in order.
    #[test]
    fn normalize_parameters_resolves_and_merges_refs() {
        let mut doc = parse(REF_PARAMS_SPEC);
        normalize_parameters(&mut doc);
        let op = doc.paths["/items/{itemId}"].get.as_ref().unwrap();
        let resolved: Vec<(&str, Option<ParameterLocation>)> = op
            .parameters
            .iter()
            .map(|p| (p.name.as_str(), p.location))
            .collect();
        assert_eq!(
            resolved,
            [
                ("itemId", Some(ParameterLocation::Path)),
                ("verbose", Some(ParameterLocation::Query)),
                ("inline", Some(ParameterLocation::Query)),
            ]
        );
        // The shared path-item parameter list is consumed once merged.
        assert!(doc.paths["/items/{itemId}"].parameters.is_empty());
    }

    /// `normalize_responses` inlines a `$ref` into `components.responses`, so the
    /// operation's `"200"` carries the referenced response's `content` (and thus its
    /// model) instead of an empty `$ref` shell — without which the endpoint would
    /// generate `-> None`.
    #[test]
    fn normalize_responses_resolves_component_refs() {
        let mut doc = parse(
            r##"
openapi: 3.0.0
info: { title: T }
paths:
  /items:
    get:
      operationId: getItems
      responses:
        "200": { $ref: "#/components/responses/ItemsResponse" }
components:
  responses:
    ItemsResponse:
      description: A list of items
      content:
        application/json: { schema: { $ref: "#/components/schemas/Items" } }
"##,
        );
        normalize_responses(&mut doc);
        let op = doc.paths["/items"].get.as_ref().unwrap();
        let ok = &op.responses["200"];
        assert_eq!(ok.description.as_deref(), Some("A list of items"));
        assert!(ok.content.contains_key("application/json"));
    }

    /// An operation-level parameter overrides a path-level one sharing its name and
    /// location (OpenAPI's rule), rather than appearing twice.
    #[test]
    fn normalize_parameters_operation_overrides_path_level() {
        let mut doc = parse(
            r##"
openapi: 3.0.0
info: { title: T }
paths:
  /x/{id}:
    parameters:
      - { name: id, in: path, required: true, description: shared, schema: { type: string } }
    get:
      operationId: getX
      parameters:
        - { name: id, in: path, required: true, description: overridden, schema: { type: string } }
      responses:
        "200": { description: OK }
"##,
        );
        normalize_parameters(&mut doc);
        let op = doc.paths["/x/{id}"].get.as_ref().unwrap();
        assert_eq!(op.parameters.len(), 1);
        assert_eq!(op.parameters[0].description.as_deref(), Some("overridden"));
    }
}
