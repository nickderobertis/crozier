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

use std::ops::{Deref, DerefMut};
use std::path::Path;

use indexmap::IndexMap;
use serde::de::{IgnoredAny, MapAccess, Visitor};
use serde::Deserialize;

use crate::error::{Error, Result};

/// A parsed OpenAPI document.
#[derive(Debug, Deserialize)]
pub struct OpenApi {
    /// For a YAML document, the timestamp-like scalars its text writes unquoted
    /// somewhere; `None` for JSON, which cannot spell one. Fern's parser resolves
    /// an unquoted YAML timestamp to a date rather than to a string, so an example
    /// written that way is no string example (VTEX's `dateRange`), while a quoted
    /// one stays a string: Zulip quotes `"1909-04-05"` inside a flow mapping and
    /// its golden keeps it. Set by [`load`], never deserialized.
    #[serde(skip)]
    pub yaml_unquoted_timestamps: Option<std::collections::BTreeSet<String>>,
    /// The `openapi` version string (e.g. `3.0.1`).
    #[serde(default)]
    pub openapi: String,
    /// `x-crozier-pagination` / `x-fern-pagination` at the document root: the
    /// contract an operation's `x-fern-pagination: true` takes.
    #[serde(rename = "x-crozier-pagination", default)]
    pub(crate) pagination_crozier: Option<Pagination>,
    #[serde(rename = "x-fern-pagination", default)]
    pub(crate) pagination_fern: Option<Pagination>,
    /// `x-crozier-idempotency-headers` / `x-fern-idempotency-headers`: the headers
    /// an idempotent operation takes. Read through [`OpenApi::idempotency_headers`].
    #[serde(rename = "x-crozier-idempotency-headers", default)]
    pub(crate) idempotency_headers_crozier: Option<serde_json::Value>,
    #[serde(rename = "x-fern-idempotency-headers", default)]
    pub(crate) idempotency_headers_fern: Option<serde_json::Value>,
    /// Document metadata.
    #[serde(default)]
    pub info: Info,
    /// Reusable components; crozier reads `components.schemas`.
    #[serde(default)]
    pub components: Components,
    /// API operations, keyed by URL path, in document order.
    #[serde(default, deserialize_with = "deserialize_paths")]
    pub paths: IndexMap<String, PathItem>,
    /// OpenAPI 3.1 webhook operations, keyed by event name in document order.
    #[serde(default)]
    pub webhooks: IndexMap<String, PathItem>,
    /// Document-wide default security requirement; an operation without its own
    /// `security` inherits this.
    #[serde(default)]
    pub security: Option<Vec<SecurityRequirement>>,
    /// Declared API servers; the first drives the generated environment enum.
    #[serde(default, deserialize_with = "de_servers")]
    pub servers: Vec<Server>,
    /// Declared operation tags. Fern sometimes preserves the declared tag spelling
    /// in generated docs rather than title-casing an operation-only tag.
    #[serde(default)]
    pub tags: Vec<ApiTag>,
    /// `x-crozier-base-path`: the base path every operation's route sits under
    /// (canonical spelling; see [`OpenApi::base_path`]).
    #[serde(rename = "x-crozier-base-path", default)]
    pub base_path_crozier: Option<BasePath>,
    /// `x-fern-base-path`: the Fern spelling of the base path, superseded by
    /// `x-crozier-base-path` when both appear.
    #[serde(rename = "x-fern-base-path", default)]
    pub base_path_fern: Option<BasePath>,
}

/// A document-level base path (`x-crozier-base-path` / `x-fern-base-path`): a
/// path prefixed to every operation's route, whose `{placeholders}` are lifted
/// out of every method into client constructor arguments.
#[derive(Debug, Clone, Deserialize)]
#[serde(untagged)]
pub enum BasePath {
    /// `x-fern-base-path: /v1`.
    Path(String),
    /// The object form.
    Object {
        /// The base path itself, e.g. `/{api_version}`.
        #[serde(default)]
        path: String,
        /// Whether the document's routes already begin with `path`, so it is
        /// not prefixed again.
        #[serde(rename = "paths-include-base-path", default)]
        paths_include_base_path: bool,
        /// The lifted parameters' schemas.
        #[serde(default)]
        parameters: Option<BasePathParameters>,
    },
}

/// The object form's `parameters`. Only the map form gives a parameter a
/// default; Fern reads a list of Parameter Objects as naming no defaults.
#[derive(Debug, Clone, Deserialize)]
#[serde(untagged)]
pub enum BasePathParameters {
    /// `name: schema`, each schema read for its `default`.
    Map(IndexMap<String, BasePathParameterSchema>),
    /// A list of Parameter Objects.
    List(Vec<serde_json::Value>),
    /// Anything else, which names no defaults rather than failing the document.
    Other(serde_json::Value),
}

/// The part of a map-form parameter schema a lifted parameter reads.
#[derive(Debug, Clone, Deserialize)]
pub struct BasePathParameterSchema {
    /// The schema's `default`, which makes the argument optional when it is a
    /// string.
    #[serde(default)]
    pub default: Option<serde_json::Value>,
}

/// A placeholder of the base path, lifted to a client constructor argument.
#[derive(Debug, Clone, PartialEq, Eq)]
pub struct BasePathParameter {
    /// The placeholder's name, e.g. `api_version`.
    pub name: String,
    /// The string `default` its map-form schema declares, which makes the
    /// argument optional with that default.
    pub default: Option<String>,
}

impl BasePath {
    /// The path, and whether the routes already include it.
    #[must_use]
    pub fn path(&self) -> (&str, bool) {
        match self {
            Self::Path(path) => (path, false),
            Self::Object {
                path,
                paths_include_base_path,
                ..
            } => (path, *paths_include_base_path),
        }
    }

    /// The prefix to put before every route: the path without a trailing `/`,
    /// or nothing when the routes already include it.
    #[must_use]
    pub fn route_prefix(&self) -> &str {
        match self.path() {
            (_, true) => "",
            (path, false) => path.trim_end_matches('/'),
        }
    }

    /// Every `{placeholder}` of the path, in order, with its default. Fern
    /// refuses the string form when it names one (`File has missing
    /// path-parameter`); crozier lifts it as a required argument, as it does
    /// for an object form that declares no schema for it.
    #[must_use]
    pub fn parameters(&self) -> Vec<BasePathParameter> {
        let declared = match self {
            Self::Object {
                parameters: Some(BasePathParameters::Map(map)),
                ..
            } => Some(map),
            _ => None,
        };
        let mut rest = self.path().0;
        let mut out = Vec::new();
        while let Some(open) = rest.find('{') {
            let Some(close) = rest[open..].find('}') else {
                break;
            };
            let name = &rest[open + 1..open + close];
            let default = declared
                .and_then(|map| map.get(name))
                .and_then(|schema| schema.default.as_ref())
                .and_then(serde_json::Value::as_str)
                .map(str::to_owned);
            if !name.is_empty() && out.iter().all(|p: &BasePathParameter| p.name != name) {
                out.push(BasePathParameter {
                    name: name.to_owned(),
                    default,
                });
            }
            rest = &rest[open + close + 1..];
        }
        out
    }
}

impl OpenApi {
    /// The idempotency headers an idempotent operation takes, each its wire
    /// name: `x-crozier-idempotency-headers` over `x-fern-idempotency-headers`, a
    /// list of `{header: …}` entries; an entry without a string `header` is
    /// skipped.
    #[must_use]
    pub fn idempotency_headers(&self) -> Vec<&str> {
        self.idempotency_headers_crozier
            .as_ref()
            .or(self.idempotency_headers_fern.as_ref())
            .and_then(serde_json::Value::as_array)
            .map(|entries| {
                entries
                    .iter()
                    .filter_map(|entry| entry.get("header")?.as_str())
                    .map(str::trim)
                    .filter(|header| !header.is_empty())
                    .collect()
            })
            .unwrap_or_default()
    }

    /// The document's base path: `x-crozier-base-path` when present, else
    /// `x-fern-base-path` (the [dual-header policy](self#fern-compatible-extensions)).
    #[must_use]
    pub fn base_path(&self) -> Option<&BasePath> {
        self.base_path_crozier
            .as_ref()
            .or(self.base_path_fern.as_ref())
    }
}

/// One entry from the document's top-level `tags` list.
#[derive(Debug, Default, Clone, Deserialize)]
pub struct ApiTag {
    /// The tag name used by operations.
    #[serde(default)]
    pub name: String,
}

/// One entry from the document's `servers` list: a base URL and an optional
/// human description (which names the generated environment member).
#[derive(Debug, Default, Clone, Deserialize)]
pub struct Server {
    /// The server base URL (the environment member's value). May contain `{var}`
    /// placeholders resolved from `variables`.
    #[serde(default)]
    pub url: String,
    /// A human description; uppercased, it names the environment member.
    #[serde(default)]
    pub description: Option<String>,
    /// URL template variables, each with a `default` Fern substitutes into the URL.
    #[serde(default)]
    pub variables: IndexMap<String, ServerVariable>,
    /// `x-crozier-server-name` / `x-fern-server-name`: the environment member's
    /// name. Read through [`Server::server_name`].
    #[serde(rename = "x-crozier-server-name", default)]
    pub(crate) server_name_crozier: Option<serde_json::Value>,
    #[serde(rename = "x-fern-server-name", default)]
    pub(crate) server_name_fern: Option<serde_json::Value>,
    /// `x-crozier-default-url` / `x-fern-default-url`: the environment member's
    /// value in place of the expanded `url`. Read through [`Server::default_url`].
    #[serde(rename = "x-crozier-default-url", default)]
    pub(crate) default_url_crozier: Option<serde_json::Value>,
    #[serde(rename = "x-fern-default-url", default)]
    pub(crate) default_url_fern: Option<serde_json::Value>,
}

impl Server {
    fn extension_text<'a>(
        crozier: Option<&'a serde_json::Value>,
        fern: Option<&'a serde_json::Value>,
    ) -> Option<&'a str> {
        crozier
            .or(fern)
            .and_then(serde_json::Value::as_str)
            .map(str::trim)
            .filter(|text| !text.is_empty())
    }

    /// The environment member name this server declares, canonicalizing on
    /// `x-crozier-server-name` over `x-fern-server-name` (see the [dual-header
    /// policy](self#fern-compatible-extensions)).
    #[must_use]
    pub fn server_name(&self) -> Option<&str> {
        Self::extension_text(
            self.server_name_crozier.as_ref(),
            self.server_name_fern.as_ref(),
        )
    }

    /// The URL this server's environment member takes in place of its expanded
    /// `url`: `x-crozier-default-url` over `x-fern-default-url`.
    #[must_use]
    pub fn default_url(&self) -> Option<&str> {
        Self::extension_text(
            self.default_url_crozier.as_ref(),
            self.default_url_fern.as_ref(),
        )
    }
}

/// A server URL template variable. Only the `default` is modeled — Fern substitutes
/// it into the URL (`{basePath}` → `v1`).
#[derive(Debug, Clone, Deserialize)]
pub struct ServerVariable {
    #[serde(default)]
    pub default: String,
}

fn deserialize_paths<'de, D>(
    deserializer: D,
) -> std::result::Result<IndexMap<String, PathItem>, D::Error>
where
    D: serde::Deserializer<'de>,
{
    struct PathsVisitor;

    impl<'de> Visitor<'de> for PathsVisitor {
        type Value = IndexMap<String, PathItem>;

        fn expecting(&self, formatter: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
            formatter.write_str("an OpenAPI paths object")
        }

        fn visit_map<A>(self, mut map: A) -> std::result::Result<Self::Value, A::Error>
        where
            A: MapAccess<'de>,
        {
            let mut paths = IndexMap::new();
            while let Some(key) = map.next_key::<String>()? {
                if key.starts_with("x-") {
                    map.next_value::<IgnoredAny>()?;
                } else {
                    paths.insert(key, map.next_value()?);
                }
            }
            Ok(paths)
        }
    }

    deserializer.deserialize_map(PathsVisitor)
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
    /// `$ref`: the map may hold a Reference Object here instead of a Security
    /// Scheme Object. `crate::refs::resolve` resolves one naming another local
    /// document and `normalize_security_scheme_refs` the in-document spelling at
    /// load time, so downstream sees this field set only on one neither follows.
    #[serde(rename = "$ref", default)]
    pub reference: Option<String>,
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
    /// For `type: oauth2`, the available flows and their scope descriptions.
    #[serde(default)]
    pub flows: Option<OAuthFlows>,
    /// `x-crozier-header` / `x-fern-header`: a header `apiKey` credential's
    /// parameter `name`, the `prefix` its value is sent with, and the `env`
    /// variable it defaults to. Read through [`SecurityScheme::header_credential`].
    #[serde(rename = "x-crozier-header", default)]
    pub(crate) header_crozier: Option<serde_json::Value>,
    #[serde(rename = "x-fern-header", default)]
    pub(crate) header_fern: Option<serde_json::Value>,
    /// `x-crozier-bearer` / `x-fern-bearer`: a bearer credential's parameter
    /// `name` and `env` variable. Read through [`SecurityScheme::bearer_credential`].
    #[serde(rename = "x-crozier-bearer", default)]
    pub(crate) bearer_crozier: Option<serde_json::Value>,
    #[serde(rename = "x-fern-bearer", default)]
    pub(crate) bearer_fern: Option<serde_json::Value>,
    /// `x-crozier-basic` / `x-fern-basic`: the `username` and `password`
    /// credentials' `name` and `env`. Read through [`SecurityScheme::basic_credentials`].
    #[serde(rename = "x-crozier-basic", default)]
    pub(crate) basic_crozier: Option<serde_json::Value>,
    #[serde(rename = "x-fern-basic", default)]
    pub(crate) basic_fern: Option<serde_json::Value>,
    /// `x-crozier-token-variable-name` / `x-fern-token-variable-name`: a bearer
    /// credential's parameter name. Read through [`SecurityScheme::bearer_credential`].
    #[serde(rename = "x-crozier-token-variable-name", default)]
    pub(crate) token_variable_name_crozier: Option<serde_json::Value>,
    #[serde(rename = "x-fern-token-variable-name", default)]
    pub(crate) token_variable_name_fern: Option<serde_json::Value>,
}

/// How a security scheme's credential is named in the generated client: the
/// declared parameter `name`, the `env` variable it defaults to, and (for a
/// header key) the `prefix` its value is sent behind. Each is `None` when the
/// extension leaves it out or gives it a blank or non-string value.
#[derive(Debug, Default, Clone, PartialEq, Eq)]
pub struct CredentialNaming {
    pub name: Option<String>,
    pub env: Option<String>,
    pub prefix: Option<String>,
}

impl CredentialNaming {
    fn from_value(value: Option<&serde_json::Value>) -> Self {
        let field = |key: &str| {
            value
                .and_then(|value| value.get(key))
                .and_then(serde_json::Value::as_str)
                .map(str::trim)
                .filter(|text| !text.is_empty())
                .map(str::to_string)
        };
        CredentialNaming {
            name: field("name"),
            env: field("env"),
            prefix: field("prefix"),
        }
    }
}

impl SecurityScheme {
    /// The header `apiKey` credential's naming, canonicalizing on
    /// `x-crozier-header` over `x-fern-header` (see the [dual-header
    /// policy](self#fern-compatible-extensions)).
    #[must_use]
    pub fn header_credential(&self) -> CredentialNaming {
        CredentialNaming::from_value(self.header_crozier.as_ref().or(self.header_fern.as_ref()))
    }

    /// The bearer credential's naming: `x-crozier-bearer` over `x-fern-bearer`,
    /// whose `name` outranks `x-crozier-token-variable-name` over
    /// `x-fern-token-variable-name`.
    #[must_use]
    pub fn bearer_credential(&self) -> CredentialNaming {
        let mut naming = CredentialNaming::from_value(
            self.bearer_crozier.as_ref().or(self.bearer_fern.as_ref()),
        );
        naming.prefix = None;
        if naming.name.is_none() {
            naming.name = self
                .token_variable_name_crozier
                .as_ref()
                .or(self.token_variable_name_fern.as_ref())
                .and_then(serde_json::Value::as_str)
                .map(str::trim)
                .filter(|text| !text.is_empty())
                .map(str::to_string);
        }
        naming
    }

    /// The basic credentials' naming, `(username, password)`: `x-crozier-basic`
    /// over `x-fern-basic`, each part's `name` and `env`.
    #[must_use]
    pub fn basic_credentials(&self) -> (CredentialNaming, CredentialNaming) {
        let declared = self.basic_crozier.as_ref().or(self.basic_fern.as_ref());
        let part = |key: &str| {
            let mut naming =
                CredentialNaming::from_value(declared.and_then(|value| value.get(key)));
            naming.prefix = None;
            naming
        };
        (part("username"), part("password"))
    }
}

/// OAuth2 flow declarations. crozier only needs the scope maps to reproduce
/// Fern's generated `OauthScope` enum.
#[derive(Debug, Default, Clone, Deserialize)]
pub struct OAuthFlows {
    #[serde(rename = "authorizationCode", default)]
    pub authorization_code: Option<OAuthFlow>,
    #[serde(rename = "clientCredentials", default)]
    pub client_credentials: Option<OAuthFlow>,
    #[serde(default)]
    pub implicit: Option<OAuthFlow>,
    #[serde(default)]
    pub password: Option<OAuthFlow>,
}

/// One OAuth2 flow.
#[derive(Debug, Default, Clone, Deserialize)]
pub struct OAuthFlow {
    /// Scope value → human description.
    #[serde(default, deserialize_with = "de_oauth_scopes")]
    pub scopes: IndexMap<String, String>,
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
/// HTTP authentication scheme names are case-insensitive, and Fern reads them
/// so: `scheme: Bearer` generates exactly what `bearer` does.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum HttpAuthScheme {
    /// `bearer`.
    Bearer,
    /// `basic`.
    Basic,
    /// Any other HTTP auth scheme.
    Other,
}

impl<'de> Deserialize<'de> for HttpAuthScheme {
    fn deserialize<D: serde::Deserializer<'de>>(
        deserializer: D,
    ) -> std::result::Result<Self, D::Error> {
        let name = String::deserialize(deserializer)?;
        Ok(match name.to_ascii_lowercase().as_str() {
            "bearer" => HttpAuthScheme::Bearer,
            "basic" => HttpAuthScheme::Basic,
            _ => HttpAuthScheme::Other,
        })
    }
}

/// One path's operations, keyed by HTTP method. Only the methods crozier
/// generates are modeled.
#[derive(Debug, Default, Deserialize)]
pub struct PathItem {
    /// A Path Item supplied by a sibling OpenAPI document.
    #[serde(rename = "$ref", default)]
    pub reference: Option<String>,
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
    /// `HEAD` operation.
    #[serde(default)]
    pub head: Option<Operation>,
    /// Parameters declared once on the path item and shared by every operation
    /// under it (a common real-world pattern for path params). Merged into each
    /// operation at load time by `normalize_parameters`; empty after that pass.
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
            ("HEAD", &self.head),
        ]
        .into_iter()
        .filter_map(|(method, op)| op.as_ref().map(|o| (method, o)))
        .collect()
    }

    /// Mutable references to each method slot, in the same stable order as
    /// [`PathItem::operations`], for filters that clear operations in place.
    pub(crate) fn operation_slots(&mut self) -> [&mut Option<Operation>; 6] {
        [
            &mut self.get,
            &mut self.post,
            &mut self.put,
            &mut self.delete,
            &mut self.patch,
            &mut self.head,
        ]
    }
}

/// A single API operation.
#[derive(Debug, Clone, Deserialize)]
pub struct Operation {
    /// Whether path-item parameters were merged into this operation.
    #[serde(skip)]
    pub path_level_parameters: bool,
    /// The operation identifier, `{group}_{camelMethodName}`. `None` distinguishes
    /// an omitted identifier from an explicitly empty one, which Fern names `_`.
    #[serde(rename = "operationId", default)]
    pub operation_id: Option<String>,
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
    /// `x-crozier-sdk-group-name`: the sub-client this operation belongs to,
    /// overriding the tag/`operationId` grouping (canonical spelling). One name, or
    /// a list naming a nested path (`["catalogs", "mcpServers"]`). Read via
    /// [`Operation::sdk_group_name`], which also honours the
    /// `x-fern-sdk-group-name` variant per the
    /// [dual-header policy](self#fern-compatible-extensions).
    #[serde(rename = "x-crozier-sdk-group-name", default)]
    sdk_group_name_crozier: Option<SdkGroupName>,
    /// `x-fern-sdk-group-name`: the Fern spelling of the group override. Superseded
    /// by `x-crozier-sdk-group-name` when both appear (see
    /// [`Operation::sdk_group_name`]).
    #[serde(rename = "x-fern-sdk-group-name", default)]
    sdk_group_name_fern: Option<SdkGroupName>,
    /// `x-crozier-idempotent` / `x-fern-idempotent`: whether the operation takes
    /// the document's idempotency headers. Read through [`Operation::idempotent`].
    #[serde(rename = "x-crozier-idempotent", default)]
    pub(crate) idempotent_crozier: Option<serde_json::Value>,
    #[serde(rename = "x-fern-idempotent", default)]
    pub(crate) idempotent_fern: Option<serde_json::Value>,
    /// `servers`: the base URLs this operation alone is served from, in place of
    /// the document's. Fern reads a named one (`x-fern-server-name`) as a field
    /// of a multi-URL environment.
    #[serde(default, deserialize_with = "de_servers")]
    pub servers: Vec<Server>,
    /// `x-crozier-webhook` / `x-fern-webhook`: the operation describes a webhook
    /// the API sends rather than an endpoint the SDK calls. Read through
    /// [`Operation::webhook_marked`].
    #[serde(rename = "x-crozier-webhook", default)]
    pub(crate) webhook_crozier: Option<serde_json::Value>,
    #[serde(rename = "x-fern-webhook", default)]
    pub(crate) webhook_fern: Option<serde_json::Value>,
    /// `x-crozier-retries` / `x-fern-retries`: the operation's retry policy.
    /// Read through [`Operation::retries_disabled`].
    #[serde(rename = "x-crozier-retries", default)]
    pub(crate) retries_crozier: Option<serde_json::Value>,
    #[serde(rename = "x-fern-retries", default)]
    pub(crate) retries_fern: Option<serde_json::Value>,
    /// `x-crozier-sdk-method-name`: the generated method's name, overriding the one
    /// derived from `operationId`/summary/route (canonical spelling). Read via
    /// [`Operation::sdk_method_name`], which also honours the
    /// `x-fern-sdk-method-name` variant per the
    /// [dual-header policy](self#fern-compatible-extensions).
    #[serde(
        rename = "x-crozier-sdk-method-name",
        default,
        deserialize_with = "de_sdk_method_name"
    )]
    sdk_method_name_crozier: Option<String>,
    /// `x-fern-sdk-method-name`: the Fern spelling of the method-name override.
    /// Superseded by `x-crozier-sdk-method-name` when both appear (see
    /// [`Operation::sdk_method_name`]).
    #[serde(
        rename = "x-fern-sdk-method-name",
        default,
        deserialize_with = "de_sdk_method_name"
    )]
    sdk_method_name_fern: Option<String>,
    /// `x-crozier-streaming`: how this operation streams, and (when it declares a
    /// `stream-condition`) the request property that selects between the streaming
    /// and buffered forms. Read via [`Operation::streaming`], which also honours
    /// the `x-fern-streaming` variant per the
    /// [dual-header policy](self#fern-compatible-extensions).
    ///
    /// Boxed: `Streaming` embeds two inline `Option<Schema>` and is rarely present,
    /// while `PathItem` holds an `Option<Operation>` per method — see
    /// [`path_item_stays_small_enough_for_a_1mib_windows_stack`](self::tests).
    #[serde(rename = "x-crozier-streaming", default)]
    streaming_crozier: Option<Box<Streaming>>,
    /// `x-fern-streaming`: the Fern spelling of the streaming contract. Superseded
    /// by `x-crozier-streaming` when both appear (see [`Operation::streaming`]).
    #[serde(rename = "x-fern-streaming", default)]
    streaming_fern: Option<Box<Streaming>>,
    /// `x-crozier-pagination`: the cursor/offset pagination contract this operation
    /// implements (canonical spelling). Read via [`Operation::pagination`], which
    /// also honours the `x-fern-pagination` variant per the
    /// [dual-header policy](self#fern-compatible-extensions).
    #[serde(rename = "x-crozier-pagination", default)]
    pagination_crozier: Option<DeclaredPagination>,
    /// `x-fern-pagination`: the Fern spelling of the pagination contract. Superseded
    /// by `x-crozier-pagination` when both appear (see [`Operation::pagination`]).
    #[serde(rename = "x-fern-pagination", default)]
    pagination_fern: Option<DeclaredPagination>,
    /// A human description; becomes the method docstring's summary line.
    #[serde(default)]
    pub description: Option<String>,
    /// Short operation summary. Fern uses it as the method name when no
    /// `operationId` is declared.
    #[serde(default)]
    pub summary: Option<String>,
    /// Path/query/header parameters, in document order.
    #[serde(default)]
    pub parameters: Vec<Parameter>,
    /// The request body, if any.
    #[serde(rename = "requestBody", default)]
    pub request_body: Option<RequestBody>,
    /// Legacy OpenAPI Generator body-name hint. Fern's importer preserves the
    /// body semantics of Swagger-derived operations carrying this extension.
    #[serde(rename = "x-codegen-request-body-name", default)]
    pub codegen_request_body_name: Option<String>,
    /// Responses, keyed by status code (or `default`), in document order.
    #[serde(default, deserialize_with = "deserialize_responses")]
    pub responses: IndexMap<String, Response>,
    /// Per-operation security requirement. `Some(vec![])` opts out of the
    /// document default (no auth); `None` inherits it.
    #[serde(default)]
    pub security: Option<Vec<SecurityRequirement>>,
}

/// A Responses Object permits `x-*` members beside status codes. They carry
/// metadata, not response definitions, so skip them before decoding responses.
fn deserialize_responses<'de, D>(
    deserializer: D,
) -> std::result::Result<IndexMap<String, Response>, D::Error>
where
    D: serde::Deserializer<'de>,
{
    struct ResponsesVisitor;

    impl<'de> Visitor<'de> for ResponsesVisitor {
        type Value = IndexMap<String, Response>;

        fn expecting(&self, formatter: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
            formatter.write_str("an OpenAPI responses object")
        }

        fn visit_map<A>(self, mut map: A) -> std::result::Result<Self::Value, A::Error>
        where
            A: MapAccess<'de>,
        {
            let mut responses = IndexMap::new();
            while let Some(key) = map.next_key::<String>()? {
                if key.starts_with("x-") {
                    map.next_value::<IgnoredAny>()?;
                } else {
                    responses.insert(key, map.next_value()?);
                }
            }
            Ok(responses)
        }
    }

    deserializer.deserialize_map(ResponsesVisitor)
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

    /// The sub-client path this operation is grouped into, canonicalizing on the
    /// `x-crozier-sdk-group-name` spelling (see the [dual-header
    /// policy](self#fern-compatible-extensions)). A bare string is a one-segment
    /// path; a list names a nested one. Empty segments are dropped, so a group that
    /// is only whitespace reads as no override at all.
    #[must_use]
    pub fn sdk_group_name(&self) -> Option<Vec<&str>> {
        let declared = self
            .sdk_group_name_crozier
            .as_ref()
            .or(self.sdk_group_name_fern.as_ref())?;
        let segments: Vec<&str> = match declared {
            SdkGroupName::One(name) => vec![name.trim()],
            SdkGroupName::Nested(names) => names.iter().map(|name| name.trim()).collect(),
        };
        let segments: Vec<&str> = segments
            .into_iter()
            .filter(|segment| !segment.is_empty())
            .collect();
        (!segments.is_empty()).then_some(segments)
    }

    /// Whether the operation is idempotent (`x-crozier-idempotent` over
    /// `x-fern-idempotent`, see the [dual-header
    /// policy](self#fern-compatible-extensions)): only the boolean `true` is.
    #[must_use]
    pub fn idempotent(&self) -> bool {
        self.idempotent_crozier
            .as_ref()
            .or(self.idempotent_fern.as_ref())
            == Some(&serde_json::Value::Bool(true))
    }

    /// Whether the operation is marked a webhook (`x-crozier-webhook` over
    /// `x-fern-webhook`): only the boolean `true` marks it.
    #[must_use]
    pub fn webhook_marked(&self) -> bool {
        self.webhook_crozier.as_ref().or(self.webhook_fern.as_ref())
            == Some(&serde_json::Value::Bool(true))
    }

    /// Whether the operation disables retries: `x-crozier-retries` over
    /// `x-fern-retries` is a mapping whose `disabled` is `true`.
    #[must_use]
    pub fn retries_disabled(&self) -> bool {
        self.retries_crozier
            .as_ref()
            .or(self.retries_fern.as_ref())
            .and_then(|retries| retries.get("disabled"))
            == Some(&serde_json::Value::Bool(true))
    }

    /// The declared method-name override, canonicalizing on the
    /// `x-crozier-sdk-method-name` spelling (see the [dual-header
    /// policy](self#fern-compatible-extensions)). A blank value is no override.
    #[must_use]
    pub fn sdk_method_name(&self) -> Option<&str> {
        self.sdk_method_name_crozier
            .as_deref()
            .or(self.sdk_method_name_fern.as_deref())
            .map(str::trim)
            .filter(|name| !name.is_empty())
    }

    /// The declared pagination contract, canonicalizing on the
    /// `x-crozier-pagination` spelling (see the [dual-header
    /// policy](self#fern-compatible-extensions)).
    #[must_use]
    pub fn pagination(&self) -> Option<&Pagination> {
        match self
            .pagination_crozier
            .as_ref()
            .or(self.pagination_fern.as_ref())?
        {
            DeclaredPagination::Contract(contract) => Some(contract),
            // Resolved against the root contract at load time
            // (`normalize_root_pagination`); a boolean left here names none.
            DeclaredPagination::Root(_) => None,
        }
    }

    /// The declared streaming contract, canonicalizing on the
    /// `x-crozier-streaming` spelling (see the [dual-header
    /// policy](self#fern-compatible-extensions)).
    #[must_use]
    pub fn streaming(&self) -> Option<&Streaming> {
        self.streaming_crozier
            .as_deref()
            .or(self.streaming_fern.as_deref())
    }

    /// Take out the `x-crozier-sdk-group-name` / `x-crozier-sdk-method-name`
    /// overrides, which pinned Fern does not read, so the operation names as
    /// Fern names it; `None` when it carries neither. Refusal detectors use this
    /// read-only view and hand the overrides back through
    /// [`Operation::restore_crozier_naming`] before anything is emitted.
    pub(crate) fn take_crozier_naming(&mut self) -> Option<CrozierNaming> {
        if self.sdk_group_name_crozier.is_none() && self.sdk_method_name_crozier.is_none() {
            return None;
        }
        Some(CrozierNaming {
            group: self.sdk_group_name_crozier.take(),
            method: self.sdk_method_name_crozier.take(),
        })
    }

    /// Restore what [`Operation::take_crozier_naming`] took out.
    pub(crate) fn restore_crozier_naming(&mut self, naming: CrozierNaming) {
        self.sdk_group_name_crozier = naming.group;
        self.sdk_method_name_crozier = naming.method;
    }
}

/// An operation's crozier-only naming overrides, held aside while a refusal
/// detector reads the document as pinned Fern does.
pub(crate) struct CrozierNaming {
    group: Option<SdkGroupName>,
    method: Option<String>,
}

/// The value of `x-crozier-streaming` / `x-fern-streaming`: how an operation
/// streams. An operation that declares a `stream-condition` generates *two*
/// methods — one that sets the condition and streams, one that clears it and
/// returns the buffered response.
#[derive(Debug, Default, Clone, Deserialize)]
pub struct Streaming {
    /// The stream encoding (`sse`).
    #[serde(default)]
    pub format: Option<String>,
    /// The buffered response schema, used when the condition is cleared.
    #[serde(default)]
    pub response: Option<Schema>,
    /// The streamed chunk schema, used when the condition is set.
    #[serde(rename = "response-stream", default)]
    pub response_stream: Option<Schema>,
    /// The request property that selects between the two forms
    /// (`$request.stream`).
    #[serde(rename = "stream-condition", default)]
    pub stream_condition: Option<String>,
}

impl Streaming {
    /// The request property the condition names, with its `$request.` prefix
    /// stripped. `None` when the operation streams unconditionally.
    #[must_use]
    pub fn condition_property(&self) -> Option<&str> {
        self.stream_condition
            .as_deref()
            .map(strip_selector_prefix)
            .filter(|property| !property.is_empty())
    }
}

/// The value of `x-crozier-sdk-group-name` / `x-fern-sdk-group-name`: one group
/// name, or a list naming a nested path of them.
#[derive(Debug, Clone, Deserialize)]
#[serde(untagged)]
pub enum SdkGroupName {
    /// A single group name (`sessions`).
    One(String),
    /// A nested path of group names (`["catalogs", "mcpServers"]`).
    Nested(Vec<String>),
}

/// One entry of `x-crozier-enum` / `x-fern-enum`: the Python member name a wire
/// value is given, in place of the identifier derived from the value itself.
#[derive(Debug, Default, Clone, Deserialize)]
pub struct EnumValueName {
    /// The member name (`USD` for the value `$`).
    #[serde(default)]
    pub name: Option<String>,
}

/// An operation's `x-crozier-pagination` / `x-fern-pagination`: a contract of
/// its own, or a boolean, `true` taking the document's root contract (Fern's
/// `x-fern-pagination: true`) and `false` declaring none.
#[derive(Debug, Clone)]
pub(crate) enum DeclaredPagination {
    Contract(Pagination),
    Root(bool),
}

impl<'de> Deserialize<'de> for DeclaredPagination {
    fn deserialize<D: serde::Deserializer<'de>>(
        deserializer: D,
    ) -> std::result::Result<Self, D::Error> {
        struct Declared;
        impl<'de> serde::de::Visitor<'de> for Declared {
            type Value = DeclaredPagination;
            fn expecting(&self, formatter: &mut std::fmt::Formatter) -> std::fmt::Result {
                formatter.write_str(
                    "a pagination contract, or a boolean taking the document's root contract",
                )
            }
            fn visit_bool<E: serde::de::Error>(
                self,
                value: bool,
            ) -> std::result::Result<Self::Value, E> {
                Ok(DeclaredPagination::Root(value))
            }
            fn visit_map<A: serde::de::MapAccess<'de>>(
                self,
                map: A,
            ) -> std::result::Result<Self::Value, A::Error> {
                Pagination::deserialize(serde::de::value::MapAccessDeserializer::new(map))
                    .map(DeclaredPagination::Contract)
            }
        }
        deserializer.deserialize_any(Declared)
    }
}

/// The value of `x-crozier-pagination` / `x-fern-pagination`: the response and
/// request members that drive a generated pager: the cursor form, or the offset
/// form (`offset` with no `cursor`).
#[derive(Debug, Default, Clone, Deserialize)]
pub struct Pagination {
    /// The request property holding the cursor, as a dotted path
    /// (`$request.starting_after`).
    #[serde(default)]
    pub cursor: Option<String>,
    /// The response property holding the next cursor
    /// (`$response.next_cursor`).
    #[serde(default)]
    pub next_cursor: Option<String>,
    /// The response property holding the page's items (`$response.data`).
    #[serde(default)]
    pub results: Option<String>,
    /// The request property holding the page offset, for the offset form.
    #[serde(default)]
    pub offset: Option<String>,
}

impl Pagination {
    /// The request-side cursor property name, with the `$request.` prefix stripped.
    #[must_use]
    pub fn cursor_property(&self) -> Option<&str> {
        self.cursor.as_deref().map(strip_selector_prefix)
    }

    /// The response-side next-cursor property name, with `$response.` stripped.
    #[must_use]
    pub fn next_cursor_property(&self) -> Option<&str> {
        self.next_cursor.as_deref().map(strip_selector_prefix)
    }

    /// The response-side results property name, with `$response.` stripped.
    #[must_use]
    pub fn results_property(&self) -> Option<&str> {
        self.results.as_deref().map(strip_selector_prefix)
    }

    /// The request-side offset property name, with `$request.` stripped.
    #[must_use]
    pub fn offset_property(&self) -> Option<&str> {
        self.offset.as_deref().map(strip_selector_prefix)
    }
}

/// Strip the `$request.` / `$response.` prefix a selector path carries — the
/// spelling both `x-crozier-pagination`'s cursor paths and
/// `x-crozier-streaming`'s `stream-condition` use.
fn strip_selector_prefix(path: &str) -> &str {
    path.split_once('.').map_or(path, |(_, rest)| rest)
}

/// An operation parameter (path/query/header/cookie). A `$ref` parameter carries
/// its pointer in [`Parameter::reference`] and is resolved against
/// `components.parameters` at load time (see `normalize_parameters`); after that
/// pass every surviving parameter is inline.
#[derive(Debug, Default, Clone, Deserialize)]
pub struct Parameter {
    /// A `$ref` pointer to a `components.parameters` entry, e.g.
    /// `#/components/parameters/consumerId`. Resolved to the referenced parameter
    /// by `normalize_parameters`; `None` for an inline parameter.
    #[serde(rename = "$ref", default)]
    pub reference: Option<String>,
    /// True when this body was resolved from `components.requestBodies`.
    #[serde(skip)]
    pub component_ref: bool,
    /// Parameter name (the wire name; also the path placeholder for `in: path`).
    #[serde(default)]
    pub name: String,
    /// Location (`in`). `None` when absent (e.g. a `$ref` parameter).
    #[serde(rename = "in", default)]
    pub location: Option<ParameterLocation>,
    /// Whether the parameter is required.
    #[serde(default)]
    pub required: Option<bool>,
    /// Whether an array parameter is exploded into repeated values. Fern treats
    /// explicit `false` on a `form` query array as a comma-separated value.
    #[serde(default)]
    pub explode: Option<bool>,
    /// OpenAPI parameter serialization style (`form`, `spaceDelimited`, …).
    /// Query parameters default to `form` when omitted.
    #[serde(default)]
    pub style: Option<String>,
    /// Human-readable description, surfaced in the method docstring.
    #[serde(default)]
    pub description: Option<String>,
    /// The parameter's value schema. Deserialized leniently through the same
    /// boundary as object properties: `short-io` writes `"schema": "object"` on
    /// two header parameters, and Fern reads that bare string as the type it
    /// names (`typing.Dict[str, typing.Any]` in its golden) rather than refusing
    /// the document.
    #[serde(default, deserialize_with = "de_optional_schema")]
    pub schema: Option<Schema>,
    /// Content-based parameter representation, used instead of `schema` by some
    /// JSON-valued headers. Fern exposes these headers as string arguments.
    #[serde(default)]
    pub content: IndexMap<String, MediaType>,
    /// A parameter-level `example` value (Fern shows it in the worked snippet).
    #[serde(default)]
    pub example: Option<serde_json::Value>,
    /// Named OpenAPI examples, in declaration order.
    #[serde(default)]
    pub examples: IndexMap<String, ParameterExample>,
}

/// The value-bearing portion of an OpenAPI parameter example.
#[derive(Debug, Default, Clone, Deserialize)]
pub struct ParameterExample {
    /// A local `$ref` to a reusable `components.examples` entry.
    #[serde(rename = "$ref", default)]
    pub reference: Option<String>,
    /// The example value. External examples have no inline value.
    #[serde(default)]
    pub value: Option<serde_json::Value>,
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
#[derive(Debug, Default, Clone, Deserialize)]
pub struct RequestBody {
    /// A `$ref` pointer to a `components.requestBodies` entry. Resolved by
    /// `normalize_request_bodies`; `None` for an inline body.
    #[serde(rename = "$ref", default)]
    pub reference: Option<String>,
    /// True when this body was resolved from `components.requestBodies`.
    #[serde(skip)]
    pub component_ref: bool,
    /// Whether the body is required.
    #[serde(default)]
    pub required: Option<bool>,
    /// A human description of the body. Its mere *presence* (even empty) changes
    /// Fern's output: an undocumented JSON body emits an explicit `content-type`
    /// header, a documented one leaves it to the transport (see
    /// [`crate::ir`]'s endpoint content-type logic).
    #[serde(default)]
    pub description: Option<String>,
    /// Content, keyed by media type (e.g. `application/json`).
    #[serde(default)]
    pub content: IndexMap<String, MediaType>,
}

/// One response entry.
#[derive(Debug, Default, Clone, Deserialize)]
pub struct Response {
    /// A `$ref` pointer to a `components.responses` entry, e.g.
    /// `#/components/responses/GetActivitiesResponse`. Resolved to the referenced
    /// response by `normalize_responses`; `None` for an inline response.
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
    /// Optional example value for the media payload.
    #[serde(default)]
    pub example: Option<serde_json::Value>,
    /// Named examples for the media payload, in declaration order.
    #[serde(default)]
    pub examples: IndexMap<String, ParameterExample>,
    /// Per-part multipart serialization metadata.
    #[serde(default)]
    pub encoding: IndexMap<String, Encoding>,
}

/// Serialization metadata for one multipart property.
#[derive(Debug, Default, Clone, Deserialize)]
pub struct Encoding {
    /// Explicit MIME type for the part.
    #[serde(rename = "contentType", default)]
    pub content_type: Option<String>,
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
    /// `normalize_parameters`).
    #[serde(default)]
    pub parameters: IndexMap<String, Parameter>,
    /// Reusable responses (`components.responses`), in document order. A `$ref`
    /// response on an operation resolves against this map at load time (see
    /// `normalize_responses`).
    #[serde(default)]
    pub responses: IndexMap<String, Response>,
    /// Reusable request bodies (`components.requestBodies`), in document order.
    /// A `$ref` request body on an operation resolves against this map at load time.
    #[serde(rename = "requestBodies", default)]
    pub request_bodies: IndexMap<String, RequestBody>,
    /// Reusable examples (`components.examples`), in document order. Named media
    /// and parameter examples may refer to these entries with a local `$ref`.
    #[serde(default)]
    pub examples: IndexMap<String, ParameterExample>,
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
    /// Optional schema title used by importers as declaration metadata.
    #[serde(default)]
    pub title: Option<String>,
    /// The schema `type` (`object`, `string`, `array`, ...). A single string in
    /// 3.0; the first entry is used if a 3.1 list is given.
    #[serde(rename = "type", default)]
    pub ty: Option<TypeField>,
    /// Format qualifier (`date-time`, `uuid`, `base64`, ...).
    #[serde(default)]
    pub format: Option<String>,
    /// The 3.1 `contentMediaType` of a string's content: `application/octet-stream`
    /// is how a 3.1 document spells a binary string that 3.0 spells `format: binary`.
    #[serde(rename = "contentMediaType", default)]
    pub content_media_type: Option<String>,
    /// Object properties, in document order. Deserialized leniently: a property
    /// whose value is not a schema object degrades to a malformed unknown node
    /// rather than aborting the parse (issue #86), and an explicit `null` map
    /// reads as the absent key.
    #[serde(default, deserialize_with = "de_properties")]
    pub properties: SchemaProperties,
    /// Required property names.
    #[serde(default, deserialize_with = "de_required")]
    pub required: RequiredNames,
    /// Array item schema.
    #[serde(default, deserialize_with = "de_items")]
    pub items: Option<Box<Schema>>,
    /// The 2020-12 `$defs` map. Nothing is generated from it; it is kept only as
    /// a target a `properties` pointer walks through (see
    /// `properties_reference_target`).
    #[serde(rename = "$defs", default, deserialize_with = "de_defs")]
    pub defs: IndexMap<String, Schema>,
    /// `uniqueItems` is accepted at the boundary; Fern's OpenAPI importer still
    /// emits a list, so generation does not change collection type for this flag.
    #[serde(rename = "uniqueItems", default)]
    pub unique_items: Option<bool>,
    /// Schema default.
    #[serde(default)]
    pub default: Option<serde_json::Value>,
    /// `additionalProperties` — a bool or a schema.
    #[serde(rename = "additionalProperties", default)]
    pub additional_properties: Option<AdditionalProperties>,
    /// `patternProperties`, kept as written: nothing is generated from it, and
    /// it is read only to decide whether a closed object with no `properties`
    /// can hold a string-valued key (see `admits_only_empty_object` in `ir.rs`).
    #[serde(rename = "patternProperties", default)]
    pub pattern_properties: Option<serde_json::Value>,
    /// Enum values (strings for the cases crozier generates).
    #[serde(rename = "enum", default)]
    pub enum_values: Option<Vec<serde_json::Value>>,
    /// JSON Schema `const`, treated as a single-value enum by Fern's importer.
    #[serde(rename = "const", default)]
    pub const_value: Option<serde_json::Value>,
    /// `oneOf` variants.
    #[serde(rename = "oneOf", default, deserialize_with = "de_composition")]
    pub one_of: Option<Vec<Schema>>,
    /// `anyOf` variants.
    #[serde(rename = "anyOf", default, deserialize_with = "de_composition")]
    pub any_of: Option<Vec<Schema>>,
    /// `allOf` members.
    #[serde(rename = "allOf", default, deserialize_with = "de_composition")]
    pub all_of: Option<Vec<Schema>>,
    /// Human description; becomes a docstring.
    #[serde(default)]
    pub description: Option<String>,
    /// A schema-level `example` value (Fern shows it in the worked snippet).
    #[serde(default)]
    pub example: Option<serde_json::Value>,
    /// OpenAPI 3.1 schema examples. Fern uses the first value when synthesizing
    /// worked calls, after the singular `example` when both are present. JSON
    /// Schema spells this as a sequence of values, but a document may write the
    /// Media Type Object's *map* of named Example Objects here instead — Webflow's
    /// `well_known` body does — and Fern reads that map's entries in declaration
    /// order, taking each one's `value`: its golden's worked call for that
    /// operation carries the first entry's
    /// `file_name="apple-app-site-association.txt"`.
    #[serde(default, deserialize_with = "de_schema_examples")]
    pub examples: Vec<serde_json::Value>,
    /// Inclusive lower bound used when Fern synthesizes integer examples.
    #[serde(default)]
    pub minimum: Option<serde_json::Value>,
    /// Minimum string length. Fern uses `"x"` for constrained request-string
    /// examples instead of repeating the field name.
    #[serde(rename = "minLength", default)]
    pub min_length: Option<u64>,
    /// Maximum string length, paired with `minLength` for Fern's constrained
    /// request-example placeholder heuristic.
    #[serde(rename = "maxLength", default)]
    pub max_length: Option<u64>,
    /// A string's regular-expression constraint. crozier never emits it — it
    /// reads only as the second half of the "is this string constrained at all?"
    /// question Fern's synthesized query-parameter example turns on.
    #[serde(default)]
    pub pattern: Option<String>,
    /// Legacy Square beta marker. Its importer uses constrained placeholder
    /// values in worked request examples for these schemas.
    #[serde(rename = "x-is-beta", default)]
    pub is_beta: Option<bool>,
    /// OpenAPI 3.0 nullability.
    #[serde(default)]
    pub nullable: Option<bool>,
    /// `deprecated: true`. Fern's worked examples leave out an optional property
    /// whose own schema is marked deprecated. Read leniently: any value but the
    /// boolean `true` is no mark, so a document spelling it otherwise still loads.
    #[serde(default, deserialize_with = "de_deprecated")]
    pub deprecated: bool,
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
    /// `x-crozier-type-name`: the SDK type name a component schema declares
    /// (canonical spelling). Read via [`Schema::declared_type_name`], which also
    /// honours the `x-fern-type-name` variant per the
    /// [dual-header policy](self#fern-compatible-extensions).
    #[serde(rename = "x-crozier-type-name", default)]
    pub(crate) type_name_crozier: Option<String>,
    /// `x-fern-type-name`: the Fern spelling of the declared type name. Superseded
    /// by `x-crozier-type-name` when both appear (see [`Schema::declared_type_name`]).
    #[serde(rename = "x-fern-type-name", default)]
    pub(crate) type_name_fern: Option<String>,
    /// `x-crozier-sdk-group-name` / `x-fern-sdk-group-name` on a component: the
    /// group package its type is written into. Read through
    /// [`Schema::sdk_group_name`].
    #[serde(rename = "x-crozier-sdk-group-name", default)]
    pub(crate) sdk_group_name_crozier: Option<serde_json::Value>,
    #[serde(rename = "x-fern-sdk-group-name", default)]
    pub(crate) sdk_group_name_fern: Option<serde_json::Value>,
    /// `x-tags`: the tags a component belongs to, the first naming the package
    /// its type is written into. Read through [`Schema::placement_tag`].
    #[serde(rename = "x-tags", default)]
    pub(crate) x_tags: Option<serde_json::Value>,
    /// `x-crozier-enum`: per-value member names for a string enum, keyed by wire
    /// value (canonical spelling). Read via [`Schema::enum_member_names`], which
    /// also honours the `x-fern-enum` variant per the
    /// [dual-header policy](self#fern-compatible-extensions).
    #[serde(rename = "x-crozier-enum", default)]
    pub(crate) enum_names_crozier: Option<IndexMap<String, EnumValueName>>,
    /// `x-fern-enum`: the Fern spelling of the per-value member names. Superseded by
    /// `x-crozier-enum` when both appear (see [`Schema::enum_member_names`]).
    #[serde(rename = "x-fern-enum", default)]
    pub(crate) enum_names_fern: Option<IndexMap<String, EnumValueName>>,
    /// `x-enum-varnames`: the OpenAPI-Generator community spelling of per-value
    /// member names — a list read *positionally* against `enum`, where
    /// `x-crozier-enum`/`x-fern-enum` are maps keyed by wire value. It is a
    /// third-party extension Fern reads rather than one of Fern's own, so the
    /// dual-header policy does not apply and there is no `x-crozier-` spelling of
    /// it; the two keyed forms supersede it (see [`Schema::enum_member_names`]).
    #[serde(rename = "x-enum-varnames", default)]
    pub(crate) enum_varnames: Option<Vec<String>>,
    /// `x-crozier-property-name`: the Python name of the object property this
    /// node is the value of — its model field and request keyword argument —
    /// while its JSON key stays the property's key (canonical spelling). Read via
    /// [`Schema::property_name`], which also honours the `x-fern-property-name`
    /// variant per the [dual-header policy](self#fern-compatible-extensions).
    #[serde(rename = "x-crozier-property-name", default)]
    pub(crate) property_name_crozier: Option<String>,
    /// `x-fern-property-name`: the Fern spelling of the property-name override.
    /// Superseded by `x-crozier-property-name` when both appear (see
    /// [`Schema::property_name`]).
    #[serde(rename = "x-fern-property-name", default)]
    pub(crate) property_name_fern: Option<String>,
    /// Set when this node's `type` was a list with more than one non-`null` member,
    /// which `normalize_multi_type_schemas` rewrote into the equivalent `anyOf`.
    /// Not a wire field. Fern names such a union rather than inlining it — EN
    /// 18222's `MultiValuedDataElement.value.items.anyOf[0]` generates the alias
    /// `MultiValuedDataElementValueItemZero` where a hand-written `anyOf` in the
    /// same position is inlined — so the origin has to outlive the rewrite.
    #[serde(skip)]
    pub multi_type_union: bool,
    /// The `$ref` this node was copied from by `normalize_schema_pointer_refs`,
    /// when that reference named `properties` and so was one Fern's importer
    /// converts as a copy at its use site. Not a wire field: a discriminated-union
    /// variant copied this way is declared under a name read off the reference
    /// itself, as Fern's variant conversion names it (the hand-written
    /// `ref-pointer-walk` fixture's `ComponentsSchemasRoutePropertiesFromOneOf0`).
    #[serde(skip)]
    pub ref_origin: Option<String>,
    /// Set when this node stood where a schema object was expected but the document
    /// carried a non-object value there (e.g. a JSON array, from a `required` list
    /// misplaced inside `properties`). Not a wire field — the `properties`
    /// deserializer sets it so the node degrades to Fern's unknown type
    /// (`Optional[Any]`) instead of serde positionally parsing the sequence into a
    /// bogus `$ref` (issue #86).
    #[serde(skip)]
    pub malformed: bool,
    /// Set when this node's `$ref` named a component schema the document never
    /// declares, which `normalize_unresolvable_schema_refs` degraded to the
    /// unknown type. Not a wire field. Fern guards such a success body against an
    /// empty response where a written `{}` in a 3.0 document is not guarded, so
    /// the origin has to outlive the rewrite.
    #[serde(skip)]
    pub unresolved_reference: bool,
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

    /// The declared Python name of the property this node is the value of,
    /// canonicalizing on the `x-crozier-property-name` spelling (see the
    /// [dual-header policy](self#fern-compatible-extensions)). The name is cased
    /// as a property key would be; the wire key is unchanged. A blank value is no
    /// override.
    #[must_use]
    pub fn property_name(&self) -> Option<&str> {
        self.property_name_crozier
            .as_deref()
            .or(self.property_name_fern.as_deref())
            .map(str::trim)
            .filter(|name| !name.is_empty())
    }

    /// The SDK group a component declares (`x-crozier-sdk-group-name` over
    /// `x-fern-sdk-group-name`, see the [dual-header
    /// policy](self#fern-compatible-extensions)): a string or a list of
    /// segments; blank segments drop.
    #[must_use]
    pub fn sdk_group_name(&self) -> Option<Vec<&str>> {
        let declared = self
            .sdk_group_name_crozier
            .as_ref()
            .or(self.sdk_group_name_fern.as_ref())?;
        let segments: Vec<&str> = match declared {
            serde_json::Value::String(name) => vec![name.trim()],
            serde_json::Value::Array(names) => names
                .iter()
                .filter_map(serde_json::Value::as_str)
                .map(str::trim)
                .collect(),
            _ => Vec::new(),
        };
        let segments: Vec<&str> = segments.into_iter().filter(|s| !s.is_empty()).collect();
        (!segments.is_empty()).then_some(segments)
    }

    /// The first non-blank `x-tags` entry of a component, the tag whose package
    /// Fern writes its type into.
    #[must_use]
    pub fn placement_tag(&self) -> Option<&str> {
        self.x_tags
            .as_ref()?
            .as_array()?
            .iter()
            .filter_map(serde_json::Value::as_str)
            .map(str::trim)
            .find(|tag| !tag.is_empty())
    }

    /// The SDK type name this schema declares, canonicalizing on the
    /// `x-crozier-type-name` spelling (see the [dual-header
    /// policy](self#fern-compatible-extensions)). A blank declaration declares
    /// nothing.
    #[must_use]
    pub fn declared_type_name(&self) -> Option<&str> {
        [&self.type_name_crozier, &self.type_name_fern]
            .into_iter()
            .flatten()
            .map(String::as_str)
            .find(|name| !name.trim().is_empty())
    }

    /// The declared Python member name for each enum value, canonicalizing on the
    /// `x-crozier-enum` spelling (see the [dual-header
    /// policy](self#fern-compatible-extensions)). A value no declaration names, or
    /// names blankly, keeps the identifier derived from the value itself.
    ///
    /// `x-enum-varnames` is read too, positionally against `enum` — the k8s
    /// Container Service Provider document names its RFC 9457 problem-type URIs
    /// that way and Fern honours them (`INVALIDARGUMENT` for
    /// `https://…/problems/invalid-argument`, where the derived identifier would
    /// spell the whole URI). A keyed declaration wins over the positional one for
    /// the same value.
    ///
    /// Fern first strips the prefix every positional name shares, character by
    /// character (its importer's `stripCommonPrefix`): HuaTuo's `OperationKind`
    /// names `OperationKindProfiling` and `OperationKindTracing`, and its golden's
    /// members are `PROFILING` and `TRACING`.
    pub fn enum_member_names(&self) -> impl Iterator<Item = (&str, &str)> {
        let varnames = self.enum_varnames.as_deref().unwrap_or_default();
        let shared = match varnames {
            [first, _, ..] => first
                .char_indices()
                .find(|&(index, ch)| {
                    varnames.iter().any(|name| {
                        name.get(index..).and_then(|rest| rest.chars().next()) != Some(ch)
                    })
                })
                .map_or(first.len(), |(index, _)| index),
            _ => 0,
        };
        let mut names: IndexMap<&str, &str> = self
            .enum_values
            .iter()
            .flatten()
            .zip(
                varnames
                    .iter()
                    .map(|name| name.get(shared..).unwrap_or_default()),
            )
            .filter_map(|(value, name)| Some((value.as_str()?, name.trim())))
            .filter(|(_, name)| !name.is_empty())
            .collect();
        names.extend(
            self.enum_names_crozier
                .as_ref()
                .or(self.enum_names_fern.as_ref())
                .into_iter()
                .flatten()
                .filter_map(|(value, declared)| {
                    let name = declared.name.as_deref()?.trim();
                    (!name.is_empty()).then_some((value.as_str(), name))
                }),
        );
        names.into_iter()
    }

    /// Whether the document says this schema admits `null`: the 3.0 `nullable`
    /// flag, a 3.1 `type` list carrying `null`, or a composition with an explicit
    /// `type: null` alternative.
    #[must_use]
    pub fn explicitly_nullable(&self) -> bool {
        // A map's alternatives are unread, and so is a `type: null` among them:
        // Hasura's `GraphQLValue_Name` is `additionalProperties: true` beside an
        // `anyOf` offering `null`, and Fern's alias is a bare `Dict[str, Any]`.
        let map_first = self.properties.is_empty()
            && self
                .ty
                .as_ref()
                .is_none_or(|ty| ty.primary() == Some("object"))
            && matches!(
                self.additional_properties,
                Some(AdditionalProperties::Bool(true) | AdditionalProperties::Schema(_))
            );
        self.nullable == Some(true)
            || matches!(
                self.ty.as_ref(),
                Some(TypeField::Multiple(types)) if types.iter().any(|ty| ty == "null")
            )
            || !map_first
                && self
                    .one_of
                    .as_ref()
                    .or(self.any_of.as_ref())
                    .is_some_and(|members| {
                        members.iter().any(|member| {
                            member.ty.as_ref().and_then(TypeField::primary) == Some("null")
                        })
                    })
    }
}

/// An object schema's ordered properties plus whether the source explicitly
/// declared the `properties` key. Fern distinguishes `properties: {}` (a closed,
/// argument-free request payload) from an object with no `properties` key (an
/// open-map request argument), even though both maps are empty after parsing.
#[derive(Debug, Default, Clone)]
pub struct SchemaProperties {
    values: IndexMap<String, Schema>,
    declared: bool,
}

impl SchemaProperties {
    /// Whether the source schema explicitly carried a `properties` key.
    #[must_use]
    pub fn declared(&self) -> bool {
        self.declared
    }
}

impl Deref for SchemaProperties {
    type Target = IndexMap<String, Schema>;

    fn deref(&self) -> &Self::Target {
        &self.values
    }
}

impl DerefMut for SchemaProperties {
    fn deref_mut(&mut self) -> &mut Self::Target {
        &mut self.values
    }
}

impl<'a> IntoIterator for &'a SchemaProperties {
    type Item = (&'a String, &'a Schema);
    type IntoIter = indexmap::map::Iter<'a, String, Schema>;

    fn into_iter(self) -> Self::IntoIter {
        self.values.iter()
    }
}

fn de_composition<'de, D>(deserializer: D) -> std::result::Result<Option<Vec<Schema>>, D::Error>
where
    D: serde::Deserializer<'de>,
{
    use serde::de::Error as _;
    #[derive(Deserialize)]
    #[serde(untagged)]
    enum Composition {
        Sequence(Vec<Schema>),
        Indexed(IndexMap<String, Schema>),
    }
    match Option::<Composition>::deserialize(deserializer)? {
        None => Ok(None),
        Some(Composition::Sequence(members)) => Ok(Some(members)),
        Some(Composition::Indexed(members)) => {
            let mut indexed = members
                .into_iter()
                .map(|(index, schema)| {
                    index.parse::<usize>().map(|i| (i, schema)).map_err(|_| {
                        D::Error::custom(format!(
                            "composition map key {index:?} is not a non-negative integer"
                        ))
                    })
                })
                .collect::<std::result::Result<Vec<_>, D::Error>>()?;
            indexed.sort_by_key(|(index, _)| *index);
            Ok(Some(
                indexed.into_iter().map(|(_, schema)| schema).collect(),
            ))
        }
    }
}

/// Deserialize an OAuth Flow Object's `scopes`, tolerating an explicit `null`.
///
/// The specification makes the map required, but a real document writes
/// `scopes: null` where it grants none — SteamInputDB's `Steam OpenID` implicit
/// flow does — and Fern reads that document. An explicit `null` therefore reads
/// as the absent key does: no scopes at all.
fn de_oauth_scopes<'de, D>(
    deserializer: D,
) -> std::result::Result<IndexMap<String, String>, D::Error>
where
    D: serde::Deserializer<'de>,
{
    Ok(Option::<IndexMap<String, String>>::deserialize(deserializer)?.unwrap_or_default())
}

/// Deserialize an SDK method-name override. Fern also accepts it written as a
/// sequence of strings and reads the sequence the way JavaScript stringifies an
/// array, its members joined by `,`: `[fetch]` names the method `fetch` and
/// `[fetch, grab]` names it `fetch_grab`. An empty sequence, which Fern fails
/// on, is refused.
fn de_sdk_method_name<'de, D>(deserializer: D) -> std::result::Result<Option<String>, D::Error>
where
    D: serde::Deserializer<'de>,
{
    struct MethodName;
    impl<'de> serde::de::Visitor<'de> for MethodName {
        type Value = Option<String>;
        fn expecting(&self, formatter: &mut std::fmt::Formatter) -> std::fmt::Result {
            formatter.write_str("a method name: a string, or a sequence of strings")
        }
        fn visit_str<E: serde::de::Error>(self, name: &str) -> std::result::Result<Self::Value, E> {
            Ok(Some(name.to_string()))
        }
        fn visit_unit<E: serde::de::Error>(self) -> std::result::Result<Self::Value, E> {
            Ok(None)
        }
        fn visit_none<E: serde::de::Error>(self) -> std::result::Result<Self::Value, E> {
            Ok(None)
        }
        fn visit_some<S: serde::Deserializer<'de>>(
            self,
            deserializer: S,
        ) -> std::result::Result<Self::Value, S::Error> {
            deserializer.deserialize_any(self)
        }
        fn visit_seq<A: serde::de::SeqAccess<'de>>(
            self,
            mut sequence: A,
        ) -> std::result::Result<Self::Value, A::Error> {
            let mut names = Vec::new();
            while let Some(name) = sequence.next_element::<String>()? {
                names.push(name);
            }
            if names.is_empty() {
                // Fern fails on an empty sequence too, so it names no method
                // crozier could match.
                return Err(serde::de::Error::invalid_length(0, &self));
            }
            Ok(Some(names.join(",")))
        }
    }
    deserializer.deserialize_any(MethodName)
}

/// Deserialize a schema's `deprecated` mark: `true` only for the boolean `true`.
fn de_deprecated<'de, D>(deserializer: D) -> std::result::Result<bool, D::Error>
where
    D: serde::Deserializer<'de>,
{
    Ok(serde_json::Value::deserialize(deserializer)? == serde_json::Value::Bool(true))
}

/// Deserialize the document's `servers`, tolerating an explicit `null`.
///
/// Palo Alto's `code/Technologies.json` writes `"servers": null`, and Fern
/// generates it as a document declaring no servers, so `null` reads as the
/// absent key does.
fn de_servers<'de, D>(deserializer: D) -> std::result::Result<Vec<Server>, D::Error>
where
    D: serde::Deserializer<'de>,
{
    Ok(Option::<Vec<Server>>::deserialize(deserializer)?.unwrap_or_default())
}

/// Deserialize an object's `properties` map, tolerating a value that is not a
/// schema object. serde's derived struct deserialization fills fields positionally
/// from a JSON/YAML sequence, so a `required: [..]` list misplaced *inside*
/// `properties` would otherwise be read as a property whose first element becomes a
/// bogus `$ref` (issue #86). Instead, any non-map value degrades to a malformed
/// node that renders as Fern's unknown type — matching Fern's tolerance of the
/// same document.
fn de_properties<'de, D>(deserializer: D) -> std::result::Result<SchemaProperties, D::Error>
where
    D: serde::Deserializer<'de>,
{
    // An explicit `properties: null` declares no property map at all — Webflow's
    // DOM node schema writes one beside its `oneOf` — so it reads as the absent
    // key rather than as the closed, argument-free `properties: {}`.
    let Some(raw) = Option::<IndexMap<String, MaybeSchema>>::deserialize(deserializer)? else {
        return Ok(SchemaProperties::default());
    };
    Ok(SchemaProperties {
        values: raw.into_iter().map(|(k, v)| (k, v.0)).collect(),
        declared: true,
    })
}

/// Deserialize a Schema Object's `$defs`, which is read only as a pointer walk's
/// target. A value that is not a map defines nothing and is dropped rather than
/// failing the document, and an entry that is not a schema object degrades as a
/// property does in [`de_properties`].
fn de_defs<'de, D>(deserializer: D) -> std::result::Result<IndexMap<String, Schema>, D::Error>
where
    D: serde::Deserializer<'de>,
{
    #[derive(Deserialize)]
    #[serde(untagged)]
    enum Defs {
        Map(IndexMap<String, MaybeSchema>),
        Other(serde::de::IgnoredAny),
    }
    Ok(match Defs::deserialize(deserializer)? {
        Defs::Map(defs) => defs.into_iter().map(|(k, v)| (k, v.0)).collect(),
        Defs::Other(_) => IndexMap::new(),
    })
}

/// A Schema Object's `required`: the property names it lists, or the mark that
/// the document wrote something there that is not a list at all.
#[derive(Debug, Clone, PartialEq, Eq)]
pub enum RequiredNames {
    /// A list, keeping its string entries.
    Listed(Vec<String>),
    /// A boolean, number or map rather than a list, which names nothing — see
    /// `normalize_unlisted_required`, which the loader runs over every schema.
    Unlisted,
}

impl Default for RequiredNames {
    fn default() -> Self {
        Self::Listed(Vec::new())
    }
}

impl RequiredNames {
    /// Whether the document wrote something other than a list.
    #[must_use]
    pub fn is_unlisted(&self) -> bool {
        matches!(self, Self::Unlisted)
    }

    /// Require one more property. A `required` that was not a list becomes a
    /// list of that one name, as a merge of lists makes it.
    pub fn push(&mut self, name: String) {
        match self {
            Self::Listed(names) => names.push(name),
            Self::Unlisted => *self = Self::Listed(vec![name]),
        }
    }
}

impl std::ops::Deref for RequiredNames {
    type Target = [String];
    fn deref(&self) -> &[String] {
        match self {
            Self::Listed(names) => names,
            Self::Unlisted => &[],
        }
    }
}

impl<'a> IntoIterator for &'a RequiredNames {
    type Item = &'a String;
    type IntoIter = std::slice::Iter<'a, String>;
    fn into_iter(self) -> Self::IntoIter {
        self.iter()
    }
}

impl From<Vec<String>> for RequiredNames {
    fn from(names: Vec<String>) -> Self {
        Self::Listed(names)
    }
}

/// Deserialize `required`, keeping only its string entries. A non-string entry
/// names no property, and Fern reads the list as-is, so it requires nothing:
/// Groupe PSA's `RemoteLights` declares `required: [true]` beside a property named
/// `"true"`, and the golden's `true` field is optional.
fn de_required<'de, D>(deserializer: D) -> std::result::Result<RequiredNames, D::Error>
where
    D: serde::Deserializer<'de>,
{
    Ok(match serde_json::Value::deserialize(deserializer)? {
        serde_json::Value::Array(values) => values
            .into_iter()
            .filter_map(|value| match value {
                serde_json::Value::String(name) => Some(name),
                _ => None,
            })
            .collect::<Vec<_>>()
            .into(),
        serde_json::Value::Bool(_)
        | serde_json::Value::Number(_)
        | serde_json::Value::Object(_) => RequiredNames::Unlisted,
        _ => RequiredNames::default(),
    })
}

/// Deserialize a Schema Object's `examples` from either spelling: JSON Schema's
/// sequence of values, or a map of named Example Objects whose `value` each entry
/// carries. Both flatten to the values in declaration order.
fn de_schema_examples<'de, D>(
    deserializer: D,
) -> std::result::Result<Vec<serde_json::Value>, D::Error>
where
    D: serde::Deserializer<'de>,
{
    match serde_json::Value::deserialize(deserializer)? {
        serde_json::Value::Array(values) => Ok(values),
        serde_json::Value::Object(named) => Ok(named
            .into_iter()
            .map(|(_, example)| match example {
                serde_json::Value::Object(mut fields) => {
                    fields.remove("value").unwrap_or(serde_json::Value::Null)
                }
                other => other,
            })
            .collect()),
        serde_json::Value::Null => Ok(Vec::new()),
        other => Ok(vec![other]),
    }
}

/// Deserialize array `items` through the same tolerant schema boundary as object
/// properties. OpenAPI 3.1 admits boolean JSON Schemas here (`items: false`),
/// which Fern accepts; Crozier degrades that non-object constraint to its unknown
/// item type instead of rejecting the entire otherwise valid document.
fn de_items<'de, D>(deserializer: D) -> std::result::Result<Option<Box<Schema>>, D::Error>
where
    D: serde::Deserializer<'de>,
{
    Option::<MaybeSchema>::deserialize(deserializer)
        .map(|value| value.map(|schema| Box::new(schema.0)))
}

/// Deserialize an optional schema through the same tolerant boundary as object
/// properties and array `items`, so a non-object standing in for a schema names a
/// type or degrades rather than aborting the parse.
fn de_optional_schema<'de, D>(deserializer: D) -> std::result::Result<Option<Schema>, D::Error>
where
    D: serde::Deserializer<'de>,
{
    Option::<MaybeSchema>::deserialize(deserializer).map(|value| value.map(|schema| schema.0))
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

    /// A bare string where a schema was expected names the `type`. `short-io`'s
    /// `{"schema": "object", "in": "header", "name": "type"}` reaches Fern's
    /// golden as `typing.Dict[str, typing.Any]` — what the open map `type: object`
    /// renders as — rather than as the unknown a degrade would give.
    fn visit_str<E>(self, v: &str) -> std::result::Result<Self::Value, E> {
        Ok(MaybeSchema(Schema {
            ty: Some(TypeField::Single(v.to_string())),
            ..Schema::default()
        }))
    }

    // Any other scalar standing in for a schema degrades to the unknown node.
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

/// The declared SDK parameter name used by refusal validation only.
/// Keep the dual-header precedence here with the other extension accessors.
pub(crate) fn refusal_parameter_name(node: &serde_yaml_ng::Value) -> Option<&str> {
    node.get("x-crozier-parameter-name")
        .and_then(serde_yaml_ng::Value::as_str)
        .or_else(|| {
            node.get("x-fern-parameter-name")
                .and_then(serde_yaml_ng::Value::as_str)
        })
}

/// The declared Python name of an object property, read off its source node for
/// refusal validation with [`Schema::property_name`]'s precedence.
pub(crate) fn refusal_property_name(node: &serde_yaml_ng::Value) -> Option<&str> {
    node.get("x-crozier-property-name")
        .and_then(serde_yaml_ng::Value::as_str)
        .or_else(|| {
            node.get("x-fern-property-name")
                .and_then(serde_yaml_ng::Value::as_str)
        })
        .map(str::trim)
        .filter(|name| !name.is_empty())
}

/// Declared SDK type name read off the raw source node, for the refusals
/// classified before the typed parse; emission reads [`Schema::declared_type_name`].
pub(crate) fn refusal_type_name(node: &serde_yaml_ng::Value) -> Option<&str> {
    ["x-crozier-type-name", "x-fern-type-name"]
        .into_iter()
        .filter_map(|key| node.get(key).and_then(serde_yaml_ng::Value::as_str))
        .find(|name| !name.trim().is_empty())
}

/// Read a source node's ignore flag through the ordinary schema accessor,
/// without asking the typed parser to lower its possibly malformed shape.
pub(crate) fn refusal_node_ignored(node: &serde_yaml_ng::Value) -> bool {
    let mut metadata = serde_yaml_ng::Mapping::new();
    for (key, value) in node.as_mapping().into_iter().flatten() {
        if key.as_str().is_some_and(|key| key.starts_with("x-")) {
            metadata.insert(key.clone(), value.clone());
        }
    }
    serde_yaml_ng::from_value::<Schema>(serde_yaml_ng::Value::Mapping(metadata))
        .is_ok_and(|schema| schema.ignored())
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

    let is_yaml = matches!(ext.as_deref(), Some("yml" | "yaml"));
    let mut doc: OpenApi = match ext.as_deref() {
        Some("yml" | "yaml") => serde_yaml_ng::from_str(&text).map_err(|e| Error::ParseSpec {
            path: path.to_path_buf(),
            message: e.to_string(),
        })?,
        // A float literal past `f64::MAX` is out of range to serde_json, which
        // refuses the whole document; JavaScript reads it as `Infinity`, and so
        // Fern generates from it. Hasura's metadata schema bounds
        // `Limit_MaxTime.global` by `maximum: 1.7976931348623159…e308`. JSON is
        // YAML, whose reader takes the literal as the infinite float, so the
        // document is read again that way — only for that refusal.
        Some("json") => serde_json::from_str(&text)
            .or_else(|error| {
                if error.to_string().starts_with("number out of range") {
                    serde_yaml_ng::from_str(&text).map_err(|_| error)
                } else {
                    Err(error)
                }
            })
            .map_err(|e| Error::ParseSpec {
                path: path.to_path_buf(),
                message: e.to_string(),
            })?,
        _ => {
            return Err(Error::UnknownSpecFormat {
                path: path.to_path_buf(),
            })
        }
    };

    doc.yaml_unquoted_timestamps = is_yaml.then(|| unquoted_yaml_timestamps(&text));
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
    // A Reference Object in the `components.securitySchemes` position is resolved
    // before anything reads the map, so the validation below and every later pass
    // see the Security Scheme Object the reference names.
    normalize_security_scheme_refs(&mut doc);
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

    // A `$ref` into another document is fetched and resolved before the local
    // normalizations run, so every later pass sees one self-contained document.
    let remote_origin = crate::refs::resolve(&mut doc, &crate::refs::CurlFetcher, path)?;

    normalize_float_type(&mut doc);
    normalize_parameter_schema_refs(&mut doc);
    normalize_webhook_operations(&mut doc);
    normalize_root_pagination(&mut doc);
    normalize_declared_type_names(&mut doc);
    normalize_inline_declared_type_names(&mut doc);
    normalize_schema_pointer_refs(&mut doc);
    normalize_empty_compositions(&mut doc);
    normalize_unresolvable_schema_refs(&mut doc);
    normalize_unresolved_schema_pointers(&mut doc);
    normalize_error_class_schema_names(&mut doc);
    normalize_same_primitive_unions(&mut doc);
    normalize_multi_type_schemas(&mut doc);
    normalize_unlisted_required(&mut doc);
    normalize_nullable_schema_refs(&mut doc);
    normalize_parameters(&mut doc);
    reject_unemittable_parameters(&doc, path)?;
    reject_unemittable_operation_ids(&doc, path)?;
    normalize_responses(&mut doc);
    normalize_fetched_response_alias_refs(&mut doc, &remote_origin);
    normalize_response_schema_refs(&mut doc);
    normalize_request_bodies(&mut doc);

    Ok(doc)
}

/// Fern's pinned Python generator crashes while lowering inline object headers
/// with properties. Bare `schema: object` headers generate in a registered corpus
/// spec (Short.io), so preserve those. Array headers generate too; the one Fern
/// refuses is a registry class (`example-type-mismatch`, in
/// `document_refusals::check_sdk`).
fn reject_unemittable_parameters(doc: &OpenApi, path: &Path) -> Result<()> {
    for (route, item) in &doc.paths {
        for (method, operation) in item.operations() {
            for parameter in item.parameters.iter().chain(&operation.parameters) {
                if parameter.location != Some(ParameterLocation::Header) {
                    continue;
                }
                let kind = parameter
                    .schema
                    .as_ref()
                    .and_then(|schema| schema.ty.as_ref())
                    .and_then(TypeField::primary);
                let refused = match kind {
                    Some("object") => parameter
                        .schema
                        .as_ref()
                        .is_some_and(|schema| schema.properties.declared()),
                    _ => false,
                };
                if refused {
                    let kind = kind.expect("refused header has a schema kind");
                    return Err(Error::InvalidSpec {
                        path: path.to_path_buf(),
                        message: format!(
                            "{method} {route}: header parameter `{}` has an unsupported {kind} schema in Fern's Python generator",
                            parameter.name
                        ),
                    });
                }
            }
        }
    }
    Ok(())
}

/// The pinned Fern generator emits unparsable Python for an operationId made
/// entirely of non-ASCII letters. Reject that input before writing a partial
/// SDK, with the operation's route in the diagnostic.
fn reject_unemittable_operation_ids(doc: &OpenApi, path: &Path) -> Result<()> {
    for (route, item) in &doc.paths {
        for (method, operation) in item.operations() {
            if let Some(id) = operation.operation_id.as_deref() {
                if !id.is_ascii()
                    && !id
                        .chars()
                        .any(|character| character.is_ascii_alphanumeric())
                {
                    return Err(Error::InvalidSpec {
                        path: path.to_path_buf(),
                        message: format!(
                            "{method} {route}: operationId `{id}` has no ASCII identifier characters; Fern's Python generator emits invalid source"
                        ),
                    });
                }
            }
        }
    }
    Ok(())
}

/// Resolve a Reference Object sitting in `components.securitySchemes`.
///
/// OpenAPI lets that map hold a Reference Object where a Security Scheme Object
/// is expected. Fern follows the in-document spelling —
/// `#/components/securitySchemes/<name>` — and imports the referenced scheme under
/// the *referencing* key, which is a second credential where the target is also
/// declared under its own name. A reference into another local document was
/// already resolved by `crate::refs::resolve` (Fern follows it when that document
/// is present, as HuaTuo's `../components.yaml` shows, and the
/// `unresolved-reference` class refuses it when absent). So only the in-document
/// form is followed here; any other reference is left as the unrecognized scheme
/// it deserialized to.
fn normalize_security_scheme_refs(doc: &mut OpenApi) {
    const PREFIX: &str = "#/components/securitySchemes/";
    let resolved: Vec<(String, SecurityScheme)> = doc
        .components
        .security_schemes
        .iter()
        .filter_map(|(name, scheme)| {
            let target = scheme.reference.as_deref()?.strip_prefix(PREFIX)?;
            let target = doc.components.security_schemes.get(target)?;
            // A reference naming another reference resolves to nothing importable,
            // and one naming itself would resolve to itself forever; neither is
            // followed, so a single pass is the whole of the resolution.
            target
                .reference
                .is_none()
                .then(|| (name.clone(), target.clone()))
        })
        .collect();
    for (name, scheme) in resolved {
        doc.components.security_schemes[&name] = scheme;
    }
}

/// Visit every schema the document declares, wherever it sits: the component
/// maps, the path-level and operation parameters, and the request and response
/// bodies. Nested schemas are reached by the visitor itself.
pub(crate) fn for_each_root_schema<F: FnMut(&mut Schema)>(doc: &mut OpenApi, visit: &mut F) {
    for schema in doc.components.schemas.values_mut() {
        visit(schema);
    }
    for parameter in doc.components.parameters.values_mut() {
        parameter_schemas(parameter, visit);
    }
    for response in doc.components.responses.values_mut() {
        media_schemas(&mut response.content, visit);
    }
    for body in doc.components.request_bodies.values_mut() {
        media_schemas(&mut body.content, visit);
    }
    for item in doc.paths.values_mut() {
        for_each_path_item_schema(item, visit);
    }
}

/// Visit schemas written in one Path Item and its operations.
pub(crate) fn for_each_path_item_schema<F: FnMut(&mut Schema)>(item: &mut PathItem, visit: &mut F) {
    for parameter in &mut item.parameters {
        parameter_schemas(parameter, visit);
    }
    for slot in item.operation_slots() {
        if let Some(operation) = slot.as_mut() {
            operation_schemas(operation, visit);
        }
    }
}

fn operation_schemas<F: FnMut(&mut Schema)>(operation: &mut Operation, visit: &mut F) {
    for parameter in &mut operation.parameters {
        parameter_schemas(parameter, visit);
    }
    if let Some(body) = &mut operation.request_body {
        request_body_schemas(body, visit);
    }
    for response in operation.responses.values_mut() {
        response_schemas(response, visit);
    }
}

fn parameter_schemas<F: FnMut(&mut Schema)>(parameter: &mut Parameter, visit: &mut F) {
    if let Some(schema) = &mut parameter.schema {
        visit(schema);
    }
    media_schemas(&mut parameter.content, visit);
}

fn request_body_schemas<F: FnMut(&mut Schema)>(body: &mut RequestBody, visit: &mut F) {
    media_schemas(&mut body.content, visit);
}

fn response_schemas<F: FnMut(&mut Schema)>(response: &mut Response, visit: &mut F) {
    media_schemas(&mut response.content, visit);
}

fn media_schemas<F: FnMut(&mut Schema)>(content: &mut IndexMap<String, MediaType>, visit: &mut F) {
    for media in content.values_mut() {
        if let Some(schema) = &mut media.schema {
            visit(schema);
        }
    }
}

/// Apply `visit` to `schema` and to every schema nested inside it.
pub(crate) fn for_each_schema_in<F: FnMut(&mut Schema)>(schema: &mut Schema, visit: &mut F) {
    visit(schema);
    for property in schema.properties.values_mut() {
        for_each_schema_in(property, visit);
    }
    if let Some(items) = &mut schema.items {
        for_each_schema_in(items, visit);
    }
    if let Some(AdditionalProperties::Schema(value)) = &mut schema.additional_properties {
        for_each_schema_in(value, visit);
    }
    for members in [&mut schema.one_of, &mut schema.any_of, &mut schema.all_of] {
        for member in members.iter_mut().flatten() {
            for_each_schema_in(member, visit);
        }
    }
}

/// The component-schema name a local `$ref` points at, ignoring any deeper
/// pointer into that schema (`#/components/schemas/User/properties/name`).
pub(crate) fn referenced_component_schema(reference: &str) -> Option<&str> {
    reference
        .strip_prefix("#/components/schemas/")
        .map(|pointer| pointer.split('/').next().unwrap_or(pointer))
}

/// Drop an empty `oneOf`/`anyOf`/`allOf` list.
///
/// An empty composition constrains nothing, and every later pass reads
/// `Some(vec![])` as "this node is a union" — which renders as an empty
/// `typing.Union[]` that `ruff` refuses to parse. Discord's
/// `ApplicationCommandHandler` writes `{type: integer, oneOf: [], format: int32}`
/// and Fern generates the plain `int` its `type` names, so the list is discarded
/// here rather than guarded against at each use site.
fn normalize_empty_compositions(doc: &mut OpenApi) {
    for_each_root_schema(doc, &mut |schema| {
        for_each_schema_in(schema, &mut |node| {
            for members in [&mut node.one_of, &mut node.any_of, &mut node.all_of] {
                if members.as_ref().is_some_and(Vec::is_empty) {
                    *members = None;
                }
            }
            if matches!(
                node.ty.as_ref().and_then(TypeField::primary),
                Some("string" | "integer" | "number" | "boolean")
            ) {
                node.one_of = None;
                node.any_of = None;
                node.all_of = None;
            }
        });
    });
}

/// Replace every `$ref` that points *inside* a component schema — past its name,
/// through `properties`, `items`, `additionalProperties` or a composition
/// member — with a copy of the schema it points at, as though the document had
/// written that schema at the reference. Fern's importer resolves such a
/// pointer by walking the document (`resolveSchemaReference`) and converts what
/// it finds at the referencing position, so the copy is named for where it is
/// used: dnd5eapi's `Monster.legendary_actions` points its items at
/// `Monster/allOf/3/properties/actions/items` and the golden declares
/// `MonsterLegendaryActionsItem`, and CloudPDF's `…AffectedPagesItem.revision
/// .page` points at the sibling `page` and is `…AffectedPagesItemRevisionPage`,
/// where a string target is plain `str`.
///
/// A pointer that ends *on* a composition member, one through a segment no
/// schema is named by (a `$defs` member, outside a pointer naming `properties`),
/// and one that names nothing are left for the lowering to type as unknown,
/// which is what Fern makes of each of them (the `array-item-pointer-walk-*` and
/// `ref-pointer-unnamed-segment` probes). A pointer met again while its own copy is being expanded is left
/// in place too, so a self-referencing subtree terminates.
fn normalize_schema_pointer_refs(doc: &mut OpenApi) {
    let components = doc.components.schemas.clone();
    let mut expanding = Vec::new();
    for_each_root_schema(doc, &mut |schema| {
        inline_schema_pointers(schema, &components, &mut expanding);
    });
}

fn inline_schema_pointers(
    schema: &mut Schema,
    components: &IndexMap<String, Schema>,
    expanding: &mut Vec<String>,
) {
    // A pointer that is the lone `allOf` member of a node adding only annotations
    // is that node's schema: CloudPDF's annotation `inReplyTo` is `allOf: [→ the
    // sibling `ref` union], nullable: true`, and the golden declares the union
    // itself under `…InReplyTo`.
    if schema.reference.is_none()
        && schema.ty.is_none()
        && schema.properties.is_empty()
        && schema.one_of.is_none()
        && schema.any_of.is_none()
    {
        if let Some([member]) = schema.all_of.as_deref() {
            if let Some(reference) = member.reference.clone() {
                if !expanding.contains(&reference) {
                    if let Some(target) = schema_pointer_target(components, &reference) {
                        let description = schema.description.take();
                        let nullable = schema.nullable;
                        *schema = target.clone();
                        schema.description = description.or(schema.description.take());
                        schema.nullable = nullable.or(schema.nullable);
                        expanding.push(reference);
                        inline_schema_pointers(schema, components, expanding);
                        expanding.pop();
                        return;
                    }
                }
            }
        }
    }
    if let Some(reference) = schema.reference.clone() {
        // A pointer met again inside its own expansion names the node it is
        // being copied from, and copying it once more would never end: the
        // STAC-style `intersectsFilter` geometry union lists a
        // `GeometryCollection` whose `geometries` point back at
        // `#/components/schemas/intersectsFilter/properties/intersects`. Left a
        // reference, it was expanded again wherever it was used; it is the
        // unknown type instead, as an unresolvable reference is. A plain
        // component reference stays one: it names a class and terminates.
        if expanding.contains(&reference) && schema_pointer_target(components, &reference).is_some()
        {
            *schema = Schema {
                description: schema.description.take(),
                ..Schema::default()
            };
            return;
        }
        if !expanding.contains(&reference) {
            if let Some(target) = schema_pointer_target(components, &reference) {
                *schema = target.clone();
                expanding.push(reference);
                inline_schema_pointers(schema, components, expanding);
                expanding.pop();
                return;
            }
            // Fern's v1 importer converts *any* reference whose text names
            // `properties` as a copy at the reference (`$ref.includes("properties")`
            // in its `convertSchema`), walking the whole pointer: a plain
            // component named `route_properties` and a pointer that ends on a
            // composition member (the hand-written `ref-pointer-walk` fixture's
            // `…/Route/properties/from/oneOf/0`) are copied like the pointers
            // above, where one without the word keeps its reference.
            if reference.contains("properties") {
                if let Some(target) = properties_reference_target(components, &reference) {
                    *schema = target.clone();
                    schema.ref_origin = Some(reference.clone());
                    expanding.push(reference);
                    inline_schema_pointers(schema, components, expanding);
                    expanding.pop();
                    return;
                }
            }
        }
    }
    for property in schema.properties.values_mut() {
        inline_schema_pointers(property, components, expanding);
    }
    if let Some(items) = &mut schema.items {
        inline_schema_pointers(items, components, expanding);
    }
    if let Some(AdditionalProperties::Schema(value)) = &mut schema.additional_properties {
        inline_schema_pointers(value, components, expanding);
    }
    for members in [&mut schema.one_of, &mut schema.any_of, &mut schema.all_of] {
        for member in members.iter_mut().flatten() {
            inline_schema_pointers(member, components, expanding);
        }
    }
}

/// The schema a pointer names *inside* a component, or `None` for a pointer to a
/// component itself, one ending on a composition member, or one through any
/// segment other than the Schema Object's own subschema positions.
fn schema_pointer_target<'a>(
    components: &'a IndexMap<String, Schema>,
    reference: &str,
) -> Option<&'a Schema> {
    let pointer = reference.strip_prefix("#/components/schemas/")?;
    let segments: Vec<String> = pointer
        .split('/')
        .map(|segment| segment.replace("~1", "/").replace("~0", "~"))
        .collect();
    let (name, path) = segments.split_first()?;
    if path.is_empty() {
        return None;
    }
    let mut schema = components.get(name)?;
    let mut index = 0;
    let mut ends_on_member = false;
    while index < path.len() {
        ends_on_member = false;
        schema = match path[index].as_str() {
            "properties" => {
                index += 1;
                schema.properties.get(path.get(index)?)?
            }
            "items" => schema.items.as_deref()?,
            "additionalProperties" => match &schema.additional_properties {
                Some(AdditionalProperties::Schema(value)) => value,
                _ => return None,
            },
            composition @ ("allOf" | "oneOf" | "anyOf") => {
                index += 1;
                let members = match composition {
                    "allOf" => &schema.all_of,
                    "oneOf" => &schema.one_of,
                    _ => &schema.any_of,
                };
                ends_on_member = true;
                members
                    .as_ref()?
                    .get(path.get(index)?.parse::<usize>().ok()?)?
            }
            _ => return None,
        };
        index += 1;
    }
    (!ends_on_member).then_some(schema)
}

/// The schema a reference naming `properties` resolves to by a walk of the whole
/// pointer, a composition member at its end included — Fern's
/// `resolveSchemaReference` — or `None` where no component or segment names one.
/// The walk enters a `$defs` member too: pinned Fern types an array item
/// pointing at `#/components/schemas/Named/properties/label/$defs/inner`, an
/// `inner` of `type: string`, as `List[str]` (the `356-defs-pointer` authored
/// probe), where a pointer without the word, `…/Named/$defs/inner`, is never
/// walked and stays unknown.
fn properties_reference_target<'a>(
    components: &'a IndexMap<String, Schema>,
    reference: &str,
) -> Option<&'a Schema> {
    let pointer = reference.strip_prefix("#/components/schemas/")?;
    let segments: Vec<String> = pointer
        .split('/')
        .map(|segment| segment.replace("~1", "/").replace("~0", "~"))
        .collect();
    let (name, path) = segments.split_first()?;
    let mut schema = components.get(name)?;
    let mut index = 0;
    while index < path.len() {
        schema = match path[index].as_str() {
            "properties" => {
                index += 1;
                schema.properties.get(path.get(index)?)?
            }
            "items" => schema.items.as_deref()?,
            "additionalProperties" => match &schema.additional_properties {
                Some(AdditionalProperties::Schema(value)) => value,
                _ => return None,
            },
            "$defs" => {
                index += 1;
                schema.defs.get(path.get(index)?)?
            }
            composition @ ("allOf" | "oneOf" | "anyOf") => {
                index += 1;
                let members = match composition {
                    "allOf" => &schema.all_of,
                    "oneOf" => &schema.one_of,
                    _ => &schema.any_of,
                };
                members
                    .as_ref()?
                    .get(path.get(index)?.parse::<usize>().ok()?)?
            }
            _ => return None,
        };
        index += 1;
    }
    Some(schema)
}

/// An object schema whose `required` is not a list is Fern's unknown type: its
/// importer iterates `required` while converting the object, and a boolean there
/// fails the conversion. NPQ's `ApplicationAcceptRequest.data.attributes` is an
/// object with properties and `required: false`, and its golden field is a bare
/// `typing.Any`. A scalar with a stray `required: true` is no object and is
/// unaffected (the same document's `data.type` stays `str`).
fn normalize_unlisted_required(doc: &mut OpenApi) {
    for_each_root_schema(doc, &mut |schema| {
        for_each_schema_in(schema, &mut |node| {
            if node.required.is_unlisted()
                && node.reference.is_none()
                && (node.ty.as_ref().and_then(TypeField::primary) == Some("object")
                    || !node.properties.is_empty())
            {
                // The mark stays, because the failure also costs the operation
                // its worked example (see `ir::fern_imports_no_endpoint_example`).
                *node = Schema {
                    description: node.description.take(),
                    nullable: node.nullable,
                    required: RequiredNames::Unlisted,
                    ..Schema::default()
                };
            } else if node.required.is_unlisted() {
                node.required = RequiredNames::default();
            }
        });
    });
}

/// Read the non-standard `type: float` as Fern does: a `number` whose `format`
/// no longer narrows it. Fern types `{type: float}` as `float` wherever it
/// appears, and keeps `float` (and a float example) under `format: int32` or
/// `int64` too, where a real `number` would become an `int`. Every other
/// misspelled type name (`int`, `double`, `bool`, `decimal`, …) stays unknown
/// on both sides, so only this one is rewritten.
fn normalize_float_type(doc: &mut OpenApi) {
    for_each_root_schema(doc, &mut |schema| {
        for_each_schema_in(schema, &mut |node| {
            let renamed = match node.ty.as_mut() {
                Some(TypeField::Single(ty)) if ty == "float" => {
                    *ty = "number".to_string();
                    true
                }
                Some(TypeField::Multiple(types)) if types.iter().any(|ty| ty == "float") => {
                    for ty in types.iter_mut().filter(|ty| *ty == "float") {
                        *ty = "number".to_string();
                    }
                    true
                }
                _ => false,
            };
            if renamed {
                node.format = None;
            }
        });
    });
}

/// Rewrite a `type` list with more than one non-`null` member into the `anyOf`
/// Fern reads it as.
///
/// A single non-`null` member is nullability and nothing else (`type: [string,
/// null]` is an optional string), which is why [`TypeField::primary`] answers
/// every other caller. Two or more are a union of those types, and Fern imports
/// them as exactly that: EN 18222's `value: {type: [string, number, boolean]}`
/// generates the hoisted alias `SingleValuedDataElementValue = typing.Union[str,
/// float, bool]` in its own module — the same treatment an inline `anyOf` gets,
/// down to the name. Normalizing here rather than at the use site means the
/// union hoisting, naming, and forward-reference passes need no second spelling
/// of the same shape. A `null` member stays optionality: it leaves the union and
/// sets `nullable`, matching the `typing.Optional[ReadModelSummaryValue]` Fern
/// emits for a five-member list ending in `null`.
fn normalize_multi_type_schemas(doc: &mut OpenApi) {
    for_each_root_schema(doc, &mut |schema| {
        for_each_schema_in(schema, &mut |node| {
            let Some(TypeField::Multiple(types)) = node.ty.as_ref() else {
                return;
            };
            // A node that already composes carries its own union; the `type` list
            // there constrains that composition rather than replacing it.
            if node.one_of.is_some() || node.any_of.is_some() || node.all_of.is_some() {
                return;
            }
            let nullable = types.iter().any(|ty| ty == "null");
            let members: Vec<Schema> = types
                .iter()
                .filter(|ty| *ty != "null")
                .map(|ty| Schema {
                    ty: Some(TypeField::Single(ty.clone())),
                    ..Schema::default()
                })
                .collect();
            if members.len() < 2 {
                return;
            }
            node.ty = None;
            node.any_of = Some(members);
            node.multi_type_union = true;
            if nullable {
                node.nullable = Some(true);
            }
        });
    });
}

/// Rename a component schema whose class name is an error class the document
/// raises, to `{Name}Body`, rewriting every reference to it.
///
/// Fern's error class and the model it would generate for the schema would share
/// one Python name, and Fern keeps the error class: OpenCodeUI declares
/// `BadRequestError` and `NotFoundError` schemas as the bodies of its `400` and
/// `404` responses, and its golden generates `errors/bad_request_error.py`'s
/// `BadRequestError` over `types/bad_request_error_body.py`'s
/// `BadRequestErrorBody`, the renamed schema's own hoisted members following it
/// (`NotFoundErrorBodyData`). A schema named for an error class no response of the
/// document raises collides with nothing and keeps its name.
fn normalize_error_class_schema_names(doc: &mut OpenApi) {
    let raised: std::collections::BTreeSet<&str> = doc
        .paths
        .values()
        .flat_map(PathItem::operations)
        .flat_map(|(_, operation)| operation.responses.keys())
        .filter(|code| !code.starts_with('2'))
        .filter_map(|code| crate::ir::response_key_status(code))
        .filter_map(crate::ir::error_class_name)
        .collect();
    let renames: IndexMap<String, String> = doc
        .components
        .schemas
        .keys()
        .filter(|name| raised.contains(crate::naming::class_name(name).as_str()))
        .map(|name| (name.clone(), format!("{name}Body")))
        .filter(|(_, renamed)| !doc.components.schemas.contains_key(renamed))
        .collect();
    rename_component_schemas(doc, &renames);
}

/// A component schema whose `oneOf`/`anyOf` alternatives all convert to one
/// primitive is that primitive under its LAST alternative's name, as Fern
/// declares it: `ShelfCode: anyOf: [two pattern strings]` is `ShelfCodeOne =
/// str`, which every use site names and a request body sends unconverted. So
/// the component is renamed `{name} {Ordinal}` (a space is a word break to
/// [`crate::naming::class_name`]) and becomes that alternative. Measured at
/// 5.20.0 on the hand-written `same-primitive-union-components` fixture; a
/// `null` alternative, or alternatives converting to different types, leave
/// the component its name.
fn normalize_same_primitive_unions(doc: &mut OpenApi) {
    let mut renames = IndexMap::new();
    for (name, schema) in &doc.components.schemas {
        let Some(last) = crate::ir::same_primitive_union_last(schema) else {
            continue;
        };
        let renamed = format!("{name} {}", crate::ir::ordinal_word(last));
        if !doc.components.schemas.contains_key(&renamed) {
            renames.insert(name.clone(), renamed);
        }
    }
    for name in renames.keys() {
        if let Some(schema) = doc.components.schemas.get_mut(name) {
            let alternatives = schema.one_of.take().or_else(|| schema.any_of.take());
            if let Some(last) = alternatives.and_then(|mut alternatives| alternatives.pop()) {
                *schema = last;
            }
        }
    }
    rename_component_schemas(doc, &renames);
}

/// Rename each component schema that declares an SDK type name
/// (`x-crozier-type-name`, or its Fern spelling `x-fern-type-name`) to that
/// name, rewriting every reference to it, so the class, its module and every
/// annotation naming it follow the declaration as Fern's do: the authored
/// probe `376-350-declared-type-name` declares `Gadget` on `Widget` and
/// `Thing` on `123456`, and Fern generates `types/gadget.py`'s `Gadget` and
/// `types/thing.py`'s `Thing`.
///
/// A declared name another component also resolves to merges the two into one
/// type, as Fern does; `name_refusals` refuses that merge unless the schemas are
/// the same. A `/` or `~` in a declared name is a word break to Fern
/// (`Gad/get` is `GadGet`) and would split a `$ref` pointer here, so the key
/// spells it as a space, which [`crate::naming::class_name`] reads the same way.
fn normalize_declared_type_names(doc: &mut OpenApi) {
    let renames: IndexMap<String, String> = doc
        .components
        .schemas
        .iter()
        .filter_map(|(name, schema)| {
            let declared = declared_type_key(schema.declared_type_name()?);
            (declared != *name).then(|| (name.clone(), declared))
        })
        .collect();
    rename_component_schemas(doc, &renames);
}

/// Resolve each operation's `x-fern-pagination: true` (or crozier's spelling)
/// to the document root's contract, `x-crozier-pagination` over
/// `x-fern-pagination`, as Fern reads it; with no root contract, or `false`, the
/// operation declares none.
fn normalize_root_pagination(doc: &mut OpenApi) {
    let root = doc
        .pagination_crozier
        .clone()
        .or_else(|| doc.pagination_fern.clone());
    for item in doc.paths.values_mut().chain(doc.webhooks.values_mut()) {
        for op in item.operation_slots().into_iter().flatten() {
            // The crozier spelling, once declared, decides alone: its `false`
            // (or a `true` with no root contract) leaves no Fern contract behind.
            if op.pagination_crozier.is_some() {
                op.pagination_fern = None;
            }
            for declared in [&mut op.pagination_crozier, &mut op.pagination_fern] {
                if let Some(DeclaredPagination::Root(take)) = declared {
                    *declared = take
                        .then(|| root.clone())
                        .flatten()
                        .map(DeclaredPagination::Contract);
                }
            }
        }
    }
}

/// Drop every path operation marked `x-fern-webhook: true` (or crozier's
/// spelling): it describes a request the API sends, so Fern gives the client no
/// method for it, while the schemas it names stay ordinary types (a `$ref` body
/// `Bid` is still `types/bid.py`, no longer folded into a method's arguments).
fn normalize_webhook_operations(doc: &mut OpenApi) {
    for item in doc.paths.values_mut() {
        for slot in item.operation_slots() {
            if slot.as_ref().is_some_and(Operation::webhook_marked) {
                *slot = None;
            }
        }
    }
}

/// Lift every inline schema that declares a type name (`x-crozier-type-name`,
/// or `x-fern-type-name`) into a component of that name, leaving a `$ref` where
/// it stood, wherever Fern's type for it is a root type: under a component, or
/// in an operation the root client carries. Fern names such a schema by the
/// declaration — a response property's inline enum declaring `ShotSize` is
/// `types/shot_size.py`, not `GetSettingsResponseMode` — as it would a
/// component. An operation grouped into a sub-client keeps its inline schemas,
/// whose types Fern writes into that sub-client's own `types/`; and a name a
/// component already holds stays inline, so nothing a document declares is
/// overwritten.
fn normalize_inline_declared_type_names(doc: &mut OpenApi) {
    fn lift(schema: &mut Schema, taken: &mut IndexMap<String, Option<Schema>>) {
        let lift_child = |child: &mut Schema, taken: &mut IndexMap<String, Option<Schema>>| {
            if child.reference.is_none() {
                if let Some(key) = child.declared_type_name().map(declared_type_key) {
                    if !taken.contains_key(&key) {
                        let reference = Schema {
                            reference: Some(format!("#/components/schemas/{key}")),
                            ..Schema::default()
                        };
                        let mut lifted = std::mem::replace(child, reference);
                        taken.insert(key.clone(), None);
                        lift(&mut lifted, taken);
                        taken.insert(key, Some(lifted));
                        return;
                    }
                }
            }
            lift(child, taken);
        };
        for child in schema.properties.values_mut() {
            lift_child(child, taken);
        }
        if let Some(items) = schema.items.as_deref_mut() {
            lift_child(items, taken);
        }
        if let Some(AdditionalProperties::Schema(values)) = schema.additional_properties.as_mut() {
            lift_child(values, taken);
        }
        for members in [&mut schema.one_of, &mut schema.any_of, &mut schema.all_of]
            .into_iter()
            .flatten()
        {
            for member in members {
                lift_child(member, taken);
            }
        }
    }
    let mut taken: IndexMap<String, Option<Schema>> = doc
        .components
        .schemas
        .keys()
        .map(|key| (key.clone(), None))
        .collect();
    for schema in doc.components.schemas.values_mut() {
        lift(schema, &mut taken);
    }
    for (url, item) in &mut doc.paths {
        for op in item.operation_slots().into_iter().flatten() {
            if !crate::ir::endpoint_module(op, url).is_empty() {
                continue;
            }
            let bodies = op
                .request_body
                .iter_mut()
                .flat_map(|body| body.content.values_mut())
                .chain(
                    op.responses
                        .values_mut()
                        .flat_map(|response| response.content.values_mut()),
                );
            for media in bodies {
                if let Some(schema) = media.schema.as_mut() {
                    lift(schema, &mut taken);
                }
            }
        }
    }
    for (key, lifted) in taken {
        if let Some(schema) = lifted {
            doc.components.schemas.insert(key, schema);
        }
    }
}

/// The component key a declared type name is renamed to: the name itself, with
/// each `/` or `~` (a word break to Fern, which would split a `$ref` pointer
/// here) spelled as a space.
pub(crate) fn declared_type_key(declared: &str) -> String {
    declared.replace(['/', '~'], " ")
}

/// Rename component schemas by `renames` (old key to new key), keeping their
/// document order, and point every `$ref` and discriminator mapping that named
/// an old key at its new one. Two schemas renamed to one key are one type, kept
/// where and as the first of them stands.
fn rename_component_schemas(doc: &mut OpenApi, renames: &IndexMap<String, String>) {
    if renames.is_empty() {
        return;
    }
    let mut schemas = IndexMap::new();
    for (name, schema) in std::mem::take(&mut doc.components.schemas) {
        schemas
            .entry(renames.get(&name).cloned().unwrap_or(name))
            .or_insert(schema);
    }
    doc.components.schemas = schemas;
    let rewrite = |reference: &mut String| {
        let Some(name) = referenced_component_schema(reference) else {
            return;
        };
        if let Some(renamed) = renames.get(name) {
            let rest = &reference["#/components/schemas/".len() + name.len()..];
            *reference = format!("#/components/schemas/{renamed}{rest}");
        }
    };
    let mut visit = |schema: &mut Schema| {
        for_each_schema_in(schema, &mut |node| {
            if let Some(reference) = node.reference.as_mut() {
                rewrite(reference);
            }
            if let Some(discriminator) = node.discriminator.as_mut() {
                for target in discriminator.mapping.values_mut() {
                    rewrite(target);
                }
            }
        });
    };
    for_each_root_schema(doc, &mut visit);
    // A webhook's payload is lowered to a type too, so its references follow.
    for item in doc.webhooks.values_mut() {
        for_each_path_item_schema(item, &mut visit);
    }
}

/// Carry a component schema's nullability to every reference to it.
///
/// Fern keeps nullability at the use site rather than in the declaration: helios'
/// `FilterTopic` declares `Union[Bytes32, List[Bytes32]]` — its `type: null`
/// alternative left the union — and every reference to it generates as
/// `Optional[FilterTopic]`.
fn normalize_nullable_schema_refs(doc: &mut OpenApi) {
    let nullable: std::collections::BTreeSet<String> = doc
        .components
        .schemas
        .iter()
        // A component that is only `type: "null"` is nullable too: a `$ref` to
        // marimo-plugins' `marimo-chatbot.cancel_prompt.output` answers
        // `typing.Optional[MarimoChatbotCancelPromptOutput]`.
        .filter(|(_, schema)| {
            schema.explicitly_nullable()
                || matches!(&schema.ty, Some(TypeField::Single(ty)) if ty == "null")
        })
        .map(|(name, _)| name.clone())
        .collect();
    if nullable.is_empty() {
        return;
    }
    for_each_root_schema(doc, &mut |schema| {
        for_each_schema_in(schema, &mut |node| {
            let names = node
                .reference
                .as_deref()
                .and_then(referenced_component_schema)
                .is_some_and(|name| nullable.contains(name));
            if names {
                node.nullable = Some(true);
            }
        });
    });
}

/// Resolve an operation response that names a component schema which is nothing
/// but a `$ref` to a schema a **remote** `$ref` declared.
///
/// Fern follows such an alias when it types an endpoint's response:
/// `helios-verifiable-api` declares `BlockResponse: {$ref: #/components/schemas/Block}`
/// over `Block: {$ref: <execution-apis URL>#/Block}`, and its byte-matching golden
/// still declares `BlockResponse = Block` while generating
/// `get_block_information` as returning `Block`.
///
/// **The remote origin is the whole of the rule, and it was measured.** A local
/// alias to an ordinary local schema is *not* followed. Probed at
/// `fernapi/fern-python-sdk:5.20.0` on four spellings — `AliasOfThing: {$ref:
/// Thing}` bare, and the same `$ref` beside a `title`, a `description` and an
/// `unevaluatedProperties` — with the alias declared before and after its target
/// and with the target referenced elsewhere as well: every one exits 0 at both
/// stages and returns `AliasOfThing`. So the rewrite is confined to the names
/// [`crate::refs::resolve`] reports as remotely declared. A reference from inside
/// another schema keeps the alias name in either case (Airbyte's
/// `DestinationAuthSpecification` stays itself on the property that carries it),
/// so the rewrite is confined to response media schemas too.
fn normalize_fetched_response_alias_refs(
    doc: &mut OpenApi,
    remote_origin: &std::collections::BTreeSet<String>,
) {
    if remote_origin.is_empty() {
        return;
    }
    let mut targets: IndexMap<String, String> = IndexMap::new();
    for name in doc.components.schemas.keys() {
        let mut seen = std::collections::BTreeSet::new();
        let mut current = name.as_str();
        while let Some(next) = doc
            .components
            .schemas
            .get(current)
            .and_then(|schema| schema.reference.as_deref())
            .and_then(referenced_component_schema)
        {
            if next == name || !seen.insert(next.to_string()) {
                break;
            }
            current = next;
        }
        if current != name && remote_origin.contains(current) {
            targets.insert(name.clone(), current.to_string());
        }
    }
    if targets.is_empty() {
        return;
    }
    for item in doc.paths.values_mut() {
        for slot in item.operation_slots() {
            let Some(operation) = slot.as_mut() else {
                continue;
            };
            for response in operation.responses.values_mut() {
                for media in response.content.values_mut() {
                    let Some(schema) = &mut media.schema else {
                        continue;
                    };
                    let Some(target) = schema
                        .reference
                        .as_deref()
                        .filter(|reference| reference.starts_with("#/components/schemas/"))
                        .and_then(referenced_component_schema)
                        .and_then(|name| targets.get(name))
                    else {
                        continue;
                    };
                    schema.reference = Some(format!("#/components/schemas/{target}"));
                }
            }
        }
    }
}

/// The `yyyy-mm-dd`-led scalars a YAML text writes without quotes, each up to the
/// next flow or block delimiter. A quoted occurrence is a string to every YAML
/// parser; an unquoted one may be a timestamp.
fn unquoted_yaml_timestamps(text: &str) -> std::collections::BTreeSet<String> {
    let bytes = text.as_bytes();
    let mut found = std::collections::BTreeSet::new();
    let mut index = 0;
    while index + 10 <= bytes.len() {
        let date = bytes[index..index + 10]
            .iter()
            .enumerate()
            .all(|(offset, byte)| {
                if offset == 4 || offset == 7 {
                    *byte == b'-'
                } else {
                    byte.is_ascii_digit()
                }
            });
        let boundary = index == 0 || !bytes[index - 1].is_ascii_alphanumeric();
        let quoted = index > 0 && matches!(bytes[index - 1], b'"' | b'\'');
        if date && boundary && !quoted {
            let end = text[index..]
                .find([',', '}', ']', '\n', '\r', '#', '"', '\''])
                .map_or(text.len(), |offset| index + offset);
            found.insert(text[index..end].trim_end().to_string());
            index = end;
        } else {
            index += 1;
        }
    }
    found
}

/// Degrade a `$ref` to a component schema the document never declares.
///
/// Fern resolves what it can and treats the rest as an unknown value: an
/// unresolvable property reference generates `Optional[Any]` and an unresolvable
/// `allOf` member contributes nothing. Real documents reach this through
/// [`crate::refs`] — a fetched schema fragment may name a sibling the root does
/// not assemble — but a hand-written spec with a typo lands here too, and
/// inventing a class for a schema that was never declared would emit Python that
/// imports a module crozier never wrote.
fn normalize_unresolvable_schema_refs(doc: &mut OpenApi) {
    let declared: std::collections::BTreeSet<String> =
        doc.components.schemas.keys().cloned().collect();
    for_each_root_schema(doc, &mut |schema| {
        for_each_schema_in(schema, &mut |node| {
            let unresolvable = node
                .reference
                .as_deref()
                .and_then(referenced_component_schema)
                .is_some_and(|name| !declared.contains(name));
            if unresolvable {
                node.reference = None;
                node.unresolved_reference = true;
            }
        });
    });
}

/// Degrade a pointer *past* a declared component's head that names nothing —
/// `#/components/schemas/Named/properties/absent` where `Named` declares no
/// `absent` — to the unknown type, as [`normalize_unresolvable_schema_refs`]
/// degrades an undeclared head.
///
/// Pinned Fern types such a pointer `Any` wherever it stands (the `358-absent-*`
/// authored probes): an optional or required property, a map value, a lone
/// `allOf` member, a request body and a response body. Left a reference, the
/// lowering named a class for it that nothing declares and imported its module.
/// An array's `items` keeps its pointer: the element lowering resolves it again
/// and types what it cannot resolve unknown, the same `List[Any]` Fern emits (the
/// hand-written `ref-pointer-walk` fixture).
fn normalize_unresolved_schema_pointers(doc: &mut OpenApi) {
    let mut references = std::collections::BTreeSet::new();
    for_each_root_schema(doc, &mut |schema| {
        for_each_schema_in(schema, &mut |node| {
            references.extend(node.reference.clone());
        });
    });
    let unresolved: std::collections::BTreeSet<String> = references
        .into_iter()
        .filter(|reference| declared_head_walk_misses(&doc.components.schemas, reference))
        .collect();
    if unresolved.is_empty() {
        return;
    }
    for_each_root_schema(doc, &mut |schema| {
        degrade_unresolved_pointers(schema, &unresolved, false);
    });
}

fn degrade_unresolved_pointers(
    schema: &mut Schema,
    unresolved: &std::collections::BTreeSet<String>,
    array_item: bool,
) {
    // A lone `allOf` member beside nothing but annotations is its holder's
    // schema, as `inline_schema_pointers` reads it, so the holder is what is
    // unknown: Fern's `merged: {allOf: [→ Named/properties/absent]}` is
    // `Optional[Any]`, not an empty model.
    let lone_member = match schema.all_of.as_deref() {
        Some([member]) => member.reference.as_ref(),
        _ => None,
    };
    if schema.reference.is_none()
        && schema.ty.is_none()
        && schema.properties.is_empty()
        && schema.one_of.is_none()
        && schema.any_of.is_none()
        && lone_member.is_some_and(|reference| unresolved.contains(reference))
    {
        schema.all_of = None;
        schema.unresolved_reference = true;
    }
    if !array_item
        && schema
            .reference
            .as_ref()
            .is_some_and(|reference| unresolved.contains(reference))
    {
        schema.reference = None;
        schema.unresolved_reference = true;
    }
    for property in schema.properties.values_mut() {
        degrade_unresolved_pointers(property, unresolved, false);
    }
    if let Some(items) = &mut schema.items {
        degrade_unresolved_pointers(items, unresolved, true);
    }
    if let Some(AdditionalProperties::Schema(value)) = &mut schema.additional_properties {
        degrade_unresolved_pointers(value, unresolved, false);
    }
    for members in [&mut schema.one_of, &mut schema.any_of, &mut schema.all_of] {
        for member in members.iter_mut().flatten() {
            degrade_unresolved_pointers(member, unresolved, false);
        }
    }
}

/// Whether a component pointer's walk from a *declared* head, through nothing
/// but `properties` keys, `items` and composition indexes with a segment after
/// them, misses: some step names a schema that is not there. It answers `false`
/// for every other pointer, including others that name nothing, because each of
/// those is handled elsewhere: one carrying any other segment, or ending on a
/// composition member, the lowering types unknown
/// (`ir::pointer_has_unnamed_segment`), and an undeclared head is
/// [`normalize_unresolvable_schema_refs`]'s.
fn declared_head_walk_misses(components: &IndexMap<String, Schema>, reference: &str) -> bool {
    let Some(pointer) = reference.strip_prefix("#/components/schemas/") else {
        return false;
    };
    let segments: Vec<String> = pointer
        .split('/')
        .map(|segment| segment.replace("~1", "/").replace("~0", "~"))
        .collect();
    let Some((name, path)) = segments.split_first() else {
        return false;
    };
    let Some(mut schema) = components.get(name) else {
        return false;
    };
    let mut index = 0;
    while index < path.len() {
        match path[index].as_str() {
            "properties" if index + 1 < path.len() => index += 2,
            "items" => index += 1,
            "allOf" | "oneOf" | "anyOf" if index + 2 < path.len() => index += 2,
            _ => return false,
        }
    }
    let mut index = 0;
    while index < path.len() {
        let next = match path[index].as_str() {
            "properties" => {
                index += 1;
                schema.properties.get(&path[index])
            }
            "items" => schema.items.as_deref(),
            composition => {
                index += 1;
                let members = match composition {
                    "allOf" => &schema.all_of,
                    "oneOf" => &schema.one_of,
                    _ => &schema.any_of,
                };
                path[index]
                    .parse::<usize>()
                    .ok()
                    .and_then(|member| members.as_ref()?.get(member))
            }
        };
        let Some(next) = next else {
            return true;
        };
        schema = next;
        index += 1;
    }
    false
}

/// Resolve response-schema `$ref`s that point into another operation response
/// rather than `components.schemas`. OpenAPI permits any local JSON Pointer, and
/// EOS uses this form to share string constraints among inline response models.
fn normalize_response_schema_refs(doc: &mut OpenApi) {
    let mut schemas = IndexMap::new();
    for (path, item) in &doc.paths {
        for (method, operation) in item.operations() {
            for (status, response) in &operation.responses {
                for (media_type, media) in &response.content {
                    let Some(schema) = &media.schema else {
                        continue;
                    };
                    let pointer = format!(
                        "#/paths/{}/{}/responses/{}/content/{}/schema",
                        json_pointer_segment(path),
                        method.to_ascii_lowercase(),
                        json_pointer_segment(status),
                        json_pointer_segment(media_type),
                    );
                    index_schema_pointers(schema, &pointer, &mut schemas);
                }
            }
        }
    }

    for item in doc.paths.values_mut() {
        for slot in item.operation_slots() {
            let Some(operation) = slot else { continue };
            for response in operation.responses.values_mut() {
                for media in response.content.values_mut() {
                    if let Some(schema) = &mut media.schema {
                        resolve_indexed_schema_refs(
                            schema,
                            "#/paths/",
                            &schemas,
                            &mut std::collections::BTreeSet::new(),
                        );
                    }
                }
            }
        }
    }
}

/// Resolve schema `$ref`s that point into a component parameter's schema
/// (`#/components/parameters/companyId/schema`) as a copy at the reference, the
/// way Fern's importer resolves any local pointer: Codat's webhook bodies share
/// their identifier fields' type and description with the path parameters.
fn normalize_parameter_schema_refs(doc: &mut OpenApi) {
    let mut schemas = IndexMap::new();
    for (name, parameter) in &doc.components.parameters {
        if let Some(schema) = &parameter.schema {
            let pointer = format!(
                "#/components/parameters/{}/schema",
                json_pointer_segment(name)
            );
            index_schema_pointers(schema, &pointer, &mut schemas);
        }
    }
    if schemas.is_empty() {
        return;
    }
    for_each_root_schema(doc, &mut |schema| {
        resolve_indexed_schema_refs(
            schema,
            "#/components/parameters/",
            &schemas,
            &mut std::collections::BTreeSet::new(),
        );
    });
}

fn json_pointer_segment(segment: &str) -> String {
    segment.replace('~', "~0").replace('/', "~1")
}

fn index_schema_pointers(schema: &Schema, pointer: &str, schemas: &mut IndexMap<String, Schema>) {
    schemas.insert(pointer.to_string(), schema.clone());
    for (name, property) in &schema.properties {
        index_schema_pointers(
            property,
            &format!("{pointer}/properties/{}", json_pointer_segment(name)),
            schemas,
        );
    }
    if let Some(items) = &schema.items {
        index_schema_pointers(items, &format!("{pointer}/items"), schemas);
    }
    if let Some(AdditionalProperties::Schema(value)) = &schema.additional_properties {
        index_schema_pointers(value, &format!("{pointer}/additionalProperties"), schemas);
    }
    for (name, members) in [
        ("oneOf", &schema.one_of),
        ("anyOf", &schema.any_of),
        ("allOf", &schema.all_of),
    ] {
        for (index, member) in members.iter().flatten().enumerate() {
            index_schema_pointers(member, &format!("{pointer}/{name}/{index}"), schemas);
        }
    }
}

fn resolve_indexed_schema_refs(
    schema: &mut Schema,
    prefix: &str,
    schemas: &IndexMap<String, Schema>,
    resolving: &mut std::collections::BTreeSet<String>,
) {
    if let Some(reference) = schema
        .reference
        .as_deref()
        .filter(|reference| reference.starts_with(prefix))
        .map(str::to_string)
    {
        if resolving.insert(reference.clone()) {
            if let Some(target) = schemas.get(&reference) {
                *schema = target.clone();
                resolve_indexed_schema_refs(schema, prefix, schemas, resolving);
            }
            resolving.remove(&reference);
        }
        return;
    }
    for property in schema.properties.values_mut() {
        resolve_indexed_schema_refs(property, prefix, schemas, resolving);
    }
    if let Some(items) = &mut schema.items {
        resolve_indexed_schema_refs(items, prefix, schemas, resolving);
    }
    if let Some(AdditionalProperties::Schema(value)) = &mut schema.additional_properties {
        resolve_indexed_schema_refs(value, prefix, schemas, resolving);
    }
    for member in [&mut schema.one_of, &mut schema.any_of, &mut schema.all_of]
        .into_iter()
        .flatten()
        .flatten()
    {
        resolve_indexed_schema_refs(member, prefix, schemas, resolving);
    }
}

fn resolve_request_body(
    request_body: &RequestBody,
    defs: &IndexMap<String, RequestBody>,
) -> RequestBody {
    if let Some(name) = request_body
        .reference
        .as_deref()
        .and_then(|r| r.strip_prefix("#/components/requestBodies/"))
    {
        if let Some(target) = defs.get(name) {
            let mut resolved = target.clone();
            resolved.component_ref = true;
            return resolved;
        }
    }
    request_body.clone()
}

fn normalize_request_bodies(doc: &mut OpenApi) {
    let defs = doc.components.request_bodies.clone();
    for item in doc.paths.values_mut() {
        for slot in item.operation_slots() {
            let Some(op) = slot else { continue };
            if let Some(request_body) = &mut op.request_body {
                *request_body = resolve_request_body(request_body, &defs);
                for media in request_body.content.values_mut() {
                    if let Some(schema) = &mut media.schema {
                        collapse_sole_composition_member(schema);
                    }
                }
            }
        }
    }
}

/// A request-body schema whose whole content is a one-member `oneOf`/`anyOf`
/// *is* that member to Fern: Flowdapt declares
/// `{"oneOf": [{"$ref": "…V1Alpha1WorkflowResourceUpdateRequest"}]}` and its
/// golden inlines that component's properties as method arguments and emits no
/// union alias, exactly as it does for the bare `$ref` spelling. A composition
/// with two or more members stays a union (Flowdapt's own two-member
/// `create_config` body is the `CreateConfigRequestBody` alias in the same
/// golden), and a wrapper carrying any other schema field is left alone because
/// collapsing it would drop that field.
fn collapse_sole_composition_member(schema: &mut Schema) {
    let sole = |members: &Option<Vec<Schema>>| {
        members
            .as_ref()
            .filter(|members| members.len() == 1)
            .map(|members| members[0].clone())
    };
    let Some(member) = sole(&schema.one_of).or_else(|| sole(&schema.any_of)) else {
        return;
    };
    if schema.reference.is_some()
        || schema.all_of.is_some()
        || schema.ty.is_some()
        || schema.properties.declared()
        || schema.additional_properties.is_some()
        || schema.items.is_some()
        || schema.enum_values.is_some()
        || schema.const_value.is_some()
        || schema.discriminator.is_some()
    {
        return;
    }
    *schema = member;
}

/// Resolve a response that is a `$ref` into `components.responses` to the
/// referenced response while preserving the pointer as provenance; an inline
/// response (or an unresolvable pointer) is returned unchanged. Only
/// `#/components/responses/*` pointers are resolved, one level deep.
fn resolve_response(response: &Response, defs: &IndexMap<String, Response>) -> Response {
    if let Some(name) = response
        .reference
        .as_deref()
        .and_then(|r| r.strip_prefix("#/components/responses/"))
    {
        if let Some(target) = defs.get(name) {
            let mut resolved = target.clone();
            resolved.reference.clone_from(&response.reference);
            return resolved;
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
            op.path_level_parameters = !shared.is_empty();
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
/// (`x-crozier-ignore` / `x-fern-ignore`, issue #78).
///
/// An operation whose [`Operation::ignored`] is set is removed (and its path with
/// it, if it becomes empty); a component whose [`Schema::ignored`] is set is never
/// emitted. Neither removal takes any other schema with it. Removing an operation
/// removes nothing from `components.schemas`: the TrueForge API ignores its three
/// `/api/internal/import/*` operations, and Fern's golden still declares
/// `ImportAgentsRequest`, `ImportSessionRequest` and every schema they reach,
/// though nothing else references them. Removing a schema keeps the schemas it
/// referenced the same way: Fern 5.20.0 still declares `LegacyPart` when its one
/// referrer `LegacyWidget` is ignored (the hand-written fixture
/// `x-fern-ignore-schema`). So the ignore is inert on a spec with no markers and
/// never changes a full, unfiltered generation.
///
/// Unlike [`filter_by_audience`], the ignore honours **both** operation- and
/// schema-level markers, per the [dual-header policy](self#fern-compatible-extensions).
pub fn filter_ignored(doc: &mut OpenApi) {
    // Remove the ignored operations, then drop paths that are now empty.
    for item in doc.paths.values_mut() {
        for slot in item.operation_slots() {
            if slot.as_ref().is_some_and(|op| op.ignored()) {
                *slot = None;
            }
        }
    }
    doc.paths.retain(|_, item| !item.operations().is_empty());
    let ignored_schemas: Vec<String> = doc
        .components
        .schemas
        .iter()
        .filter(|(_, schema)| schema.ignored())
        .map(|(key, _)| key.clone())
        .collect();
    for key in &ignored_schemas {
        doc.components.schemas.shift_remove(key);
    }
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

    #[test]
    fn a_component_reads_its_group_and_placement_tag() {
        let schema =
            |value: serde_json::Value| -> Schema { serde_json::from_value(value).unwrap() };
        let placed = schema(serde_json::json!({
            "x-fern-sdk-group-name": "lexicon",
            "x-crozier-sdk-group-name": [" glossary ", ""],
            "x-tags": [" ", "Fermentation", "Cellar"],
        }));
        assert_eq!(placed.sdk_group_name(), Some(vec!["glossary"]));
        assert_eq!(placed.placement_tag(), Some("Fermentation"));
        let plain = schema(serde_json::json!({"x-fern-sdk-group-name": 3, "x-tags": "Cellar"}));
        assert_eq!(plain.sdk_group_name(), None);
        assert_eq!(plain.placement_tag(), None);
    }

    #[test]
    fn a_boolean_pagination_takes_the_root_contract() {
        let mut doc: OpenApi = serde_json::from_value(serde_json::json!({
            "x-fern-pagination": {"offset": "$request.page", "results": "$response.items"},
            "paths": {"/p": {
                "get": {"x-fern-pagination": true, "responses": {}},
                "put": {"x-fern-pagination": false, "responses": {}},
                "post": {"x-crozier-pagination": {"cursor": "$request.c", "next_cursor": "$response.n",
                                                  "results": "$response.items"},
                         "x-fern-pagination": true, "responses": {}},
            }},
        }))
        .expect("a document");
        normalize_root_pagination(&mut doc);
        let item = &doc.paths["/p"];
        let get = item
            .get
            .as_ref()
            .unwrap()
            .pagination()
            .expect("the root contract");
        assert_eq!(get.offset_property(), Some("page"));
        assert!(item.put.as_ref().unwrap().pagination().is_none());
        let post = item
            .post
            .as_ref()
            .unwrap()
            .pagination()
            .expect("its own contract");
        assert_eq!(post.cursor_property(), Some("c"));
        let refused: std::result::Result<Operation, _> =
            serde_json::from_value(serde_json::json!({"x-fern-pagination": "yes"}));
        assert!(refused
            .expect_err("a string is no pagination")
            .to_string()
            .contains("a pagination contract, or a boolean"));
    }

    #[test]
    fn a_webhook_marked_operation_is_dropped_and_its_neighbour_kept() {
        let mut doc: OpenApi = serde_json::from_value(serde_json::json!({
            "paths": {"/hooks": {
                "post": {"x-fern-webhook": true, "responses": {}},
                "put": {"x-fern-webhook": true, "x-crozier-webhook": false, "responses": {}},
                "get": {"x-fern-webhook": "yes", "responses": {}},
            }},
        }))
        .expect("a document");
        normalize_webhook_operations(&mut doc);
        let methods: Vec<&str> = doc.paths["/hooks"]
            .operations()
            .into_iter()
            .map(|(m, _)| m)
            .collect();
        assert_eq!(methods, ["GET", "PUT"]);
    }

    #[test]
    fn an_inline_schema_declaring_a_type_name_is_lifted_to_that_component() {
        let mut doc: OpenApi = serde_json::from_value(serde_json::json!({
            "openapi": "3.0.3",
            "paths": {"/s": {"get": {"responses": {"200": {"description": "ok", "content": {
                "application/json": {"schema": {"type": "object", "properties": {
                    "mode": {"type": "string", "enum": ["a"], "x-fern-type-name": "ShotSize"},
                    "taken": {"type": "string", "enum": ["b"], "x-crozier-type-name": "Camera"},
                    "plain": {"type": "string", "enum": ["c"]},
                }}}}}}}}},
            "components": {"schemas": {"Camera": {"type": "object", "properties": {
                "iso": {"type": "array", "items": {"type": "string", "enum": ["low"],
                        "x-fern-type-name": "IsoBand"}},
            }}}},
        }))
        .expect("a document");
        normalize_inline_declared_type_names(&mut doc);
        let keys: Vec<&String> = doc.components.schemas.keys().collect();
        assert_eq!(keys, ["Camera", "IsoBand", "ShotSize"]);
        let response = &doc.paths["/s"].get.as_ref().unwrap().responses["200"].content
            ["application/json"]
            .schema
            .as_ref()
            .unwrap();
        assert_eq!(
            response.properties["mode"].reference.as_deref(),
            Some("#/components/schemas/ShotSize")
        );
        // A name a component already holds stays inline, as does an undeclared one.
        assert!(response.properties["taken"].reference.is_none());
        assert!(response.properties["plain"].reference.is_none());
        assert_eq!(
            doc.components.schemas["Camera"].properties["iso"]
                .items
                .as_ref()
                .unwrap()
                .reference
                .as_deref(),
            Some("#/components/schemas/IsoBand")
        );
    }

    #[test]
    fn idempotency_and_retry_extensions_canonicalize_on_the_crozier_spelling() {
        let op: Operation = serde_json::from_value(serde_json::json!({
            "x-fern-idempotent": false,
            "x-crozier-idempotent": true,
            "x-fern-retries": {"disabled": true},
            "x-crozier-retries": {"disabled": false},
        }))
        .expect("an operation");
        assert!(op.idempotent());
        assert!(!op.retries_disabled());
        let op: Operation =
            serde_json::from_value(serde_json::json!({"x-fern-retries": {"disabled": true}}))
                .expect("an operation");
        assert!(op.retries_disabled() && !op.idempotent());
        let doc: OpenApi = serde_json::from_value(serde_json::json!({
            "x-fern-idempotency-headers": [{"header": "X-Fern"}],
            "x-crozier-idempotency-headers": [{"header": " X-Dedupe "}, {"name": "no-header"}, 7],
        }))
        .expect("a document");
        assert_eq!(doc.idempotency_headers(), vec!["X-Dedupe"]);
    }

    #[test]
    fn server_extensions_canonicalize_on_the_crozier_spelling() {
        let server: Server = serde_json::from_value(serde_json::json!({
            "url": "https://{r}.a.test",
            "x-fern-server-name": "main",
            "x-crozier-server-name": " primary ",
            "x-fern-default-url": "https://fern.a.test",
        }))
        .expect("a server");
        assert_eq!(server.server_name(), Some("primary"));
        assert_eq!(server.default_url(), Some("https://fern.a.test"));
        let blank: Server = serde_json::from_value(serde_json::json!({
            "url": "https://a.test",
            "x-fern-server-name": " ",
            "x-crozier-default-url": 7,
        }))
        .expect("a server");
        assert_eq!(blank.server_name(), None);
        assert_eq!(blank.default_url(), None);
    }

    #[test]
    fn an_http_scheme_name_reads_case_insensitively() {
        let scheme = |name: &str| -> HttpAuthScheme {
            serde_json::from_value(serde_json::json!(name)).expect("a scheme name")
        };
        assert_eq!(scheme("Bearer"), HttpAuthScheme::Bearer);
        assert_eq!(scheme("BASIC"), HttpAuthScheme::Basic);
        assert_eq!(scheme("bearer"), HttpAuthScheme::Bearer);
        assert_eq!(scheme("Digest"), HttpAuthScheme::Other);
    }

    #[test]
    fn a_method_name_sequence_reads_joined_as_fern_reads_it() {
        let name = |extension: serde_json::Value| {
            let op: Operation = serde_json::from_value(serde_json::json!({
                "operationId": "getLockers",
                "x-fern-sdk-method-name": extension,
            }))
            .expect("operation deserializes");
            op.sdk_method_name().map(str::to_string)
        };
        assert_eq!(
            name(serde_json::json!("vacancies")).as_deref(),
            Some("vacancies")
        );
        assert_eq!(
            name(serde_json::json!(["vacancies"])).as_deref(),
            Some("vacancies")
        );
        assert_eq!(
            name(serde_json::json!(["claim", "now"])).as_deref(),
            Some("claim,now")
        );
        assert_eq!(name(serde_json::Value::Null), None);
        let empty: std::result::Result<Operation, _> =
            serde_json::from_value(serde_json::json!({"x-fern-sdk-method-name": []}));
        assert!(empty
            .expect_err("an empty sequence names no method")
            .to_string()
            .contains("invalid length 0"));
        let mapping: std::result::Result<Operation, _> =
            serde_json::from_value(serde_json::json!({
                "x-crozier-sdk-method-name": {"name": "vacancies"},
            }));
        assert!(mapping
            .expect_err("a mapping is no method name")
            .to_string()
            .contains("a string, or a sequence of strings"));
    }

    #[test]
    fn a_base_path_reads_its_placeholders_and_their_map_form_defaults() {
        let object: BasePath = serde_json::from_value(serde_json::json!({
            "path": "/{edition}/{realm}/{edition}/",
            "paths-include-base-path": true,
            "parameters": {"edition": {"type": "string", "default": "v2"}, "realm": {"type": "string"}}
        }))
        .expect("the object form deserializes");
        assert_eq!(object.route_prefix(), "");
        assert_eq!(
            object.parameters(),
            [
                BasePathParameter {
                    name: "edition".into(),
                    default: Some("v2".into())
                },
                BasePathParameter {
                    name: "realm".into(),
                    default: None
                },
            ]
        );
        // A list of Parameter Objects names no default, measured at Fern 5.20.0.
        let list: BasePath = serde_json::from_value(serde_json::json!({
            "path": "/{edition}",
            "parameters": [{"name": "edition", "in": "path", "schema": {"default": "v2"}}]
        }))
        .expect("the list form deserializes");
        assert_eq!(list.route_prefix(), "/{edition}");
        assert_eq!(list.parameters()[0].default, None);
        assert!(matches!(
            list,
            BasePath::Object {
                parameters: Some(BasePathParameters::List(_)),
                ..
            }
        ));
        // Any other spelling names no default rather than failing the document.
        let other: BasePath = serde_json::from_value(serde_json::json!({
            "path": "/{edition}",
            "parameters": "edition"
        }))
        .expect("another spelling deserializes");
        assert_eq!(
            other.parameters(),
            [BasePathParameter {
                name: "edition".into(),
                default: None
            }]
        );
        // The string form prefixes every route; an unclosed brace names nothing.
        let string: BasePath =
            serde_json::from_value(serde_json::json!("/v1/{open")).expect("string form");
        assert_eq!(string.route_prefix(), "/v1/{open");
        assert!(string.parameters().is_empty());
    }

    #[test]
    fn x_crozier_base_path_wins_over_x_fern_base_path() {
        let both: OpenApi = serde_yaml_ng::from_str(
            "openapi: 3.0.3\nx-fern-base-path: /fern\nx-crozier-base-path: /crozier\npaths: {}\n",
        )
        .expect("document deserializes");
        assert_eq!(
            both.base_path().map(BasePath::route_prefix),
            Some("/crozier")
        );
        let fern: OpenApi =
            serde_yaml_ng::from_str("openapi: 3.0.3\nx-fern-base-path: /fern\npaths: {}\n")
                .expect("document deserializes");
        assert_eq!(fern.base_path().map(BasePath::route_prefix), Some("/fern"));
    }

    #[test]
    fn null_schema_nodes_degrade_to_malformed_unknowns() {
        let parsed: MaybeSchema = serde_json::from_str("null").expect("null degrades");
        assert!(parsed.0.malformed);
        for value in ["1", "-1", "1.5", "true", "[]"] {
            assert!(
                serde_json::from_str::<MaybeSchema>(value)
                    .unwrap()
                    .0
                    .malformed
            );
        }
        // A bare STRING is the exception: it names the `type` it spells, which is
        // how Fern reads short-io's `{"schema": "object", "in": "header"}` (corpus
        // row 131) into a `typing.Dict[str, typing.Any]` argument.
        let named: MaybeSchema = serde_json::from_str("\"object\"").expect("a string names a type");
        assert!(!named.0.malformed);
        assert_eq!(
            named.0.ty.as_ref().and_then(TypeField::primary),
            Some("object")
        );
        let error = <serde::de::value::Error as serde::de::Error>::invalid_type(
            serde::de::Unexpected::Unit,
            &MaybeSchemaVisitor,
        );
        assert!(error.to_string().contains("schema object"));
    }

    /// Parse a YAML spec string into an [`OpenApi`] for the pure-filter unit tests.
    fn parse(spec: &str) -> OpenApi {
        serde_yaml_ng::from_str(spec).expect("valid spec")
    }

    fn op_ids(doc: &OpenApi) -> Vec<String> {
        doc.paths
            .values()
            .flat_map(|i| i.operations())
            .map(|(_, op)| op.operation_id.clone().unwrap_or_default())
            .collect()
    }

    fn schema_keys(doc: &OpenApi) -> Vec<String> {
        doc.components.schemas.keys().cloned().collect()
    }

    #[test]
    fn declared_type_name_prefers_the_canonical_spelling() {
        let schema = |value| serde_json::from_value::<Schema>(value).unwrap();
        let both = schema(serde_json::json!({
            "x-fern-type-name": "Decoy", "x-crozier-type-name": "Gadget"
        }));
        assert_eq!(both.declared_type_name(), Some("Gadget"));
        let fern = schema(serde_json::json!({ "x-fern-type-name": "Gadget" }));
        assert_eq!(fern.declared_type_name(), Some("Gadget"));
        let blank = schema(serde_json::json!({
            "x-crozier-type-name": " ", "x-fern-type-name": "Gadget"
        }));
        assert_eq!(blank.declared_type_name(), Some("Gadget"));
        assert_eq!(schema(serde_json::json!({})).declared_type_name(), None);
    }

    #[test]
    fn float_type_reads_as_an_unnarrowed_number_and_its_siblings_stay_unknown() {
        let mut doc = parse(
            r"
openapi: 3.1.0
info: { title: t, version: '1' }
paths:
  /gauges:
    get:
      parameters:
        - { name: tolerance, in: query, schema: { type: float } }
      responses:
        '200':
          description: ok
          content:
            application/json:
              schema: { type: array, items: { type: float } }
components:
  schemas:
    Gauge:
      type: object
      properties:
        plain: { type: float }
        narrowed: { type: float, format: int32 }
        nullable: { type: [float, 'null'] }
        counted: { type: int, format: int32 }
        real: { type: number, format: int64 }
",
        );
        normalize_float_type(&mut doc);
        let gauge = &doc.components.schemas["Gauge"];
        let field = |name: &str| {
            let schema = gauge.properties.get(name).expect("property");
            (
                schema
                    .ty
                    .as_ref()
                    .and_then(TypeField::primary)
                    .map(str::to_owned),
                schema.format.clone(),
            )
        };
        assert_eq!(field("plain"), (Some("number".to_owned()), None));
        assert_eq!(field("narrowed"), (Some("number".to_owned()), None));
        assert_eq!(field("nullable"), (Some("number".to_owned()), None));
        assert!(matches!(
            &gauge.properties.get("nullable").unwrap().ty,
            Some(TypeField::Multiple(types)) if types == &["number", "null"]
        ));
        // Another misspelled name, and a real `number`, are left exactly as written.
        assert_eq!(
            field("counted"),
            (Some("int".to_owned()), Some("int32".to_owned()))
        );
        assert_eq!(
            field("real"),
            (Some("number".to_owned()), Some("int64".to_owned()))
        );
        // Parameters and responses are rewritten as well as components.
        let operation = doc.paths["/gauges"].get.as_ref().expect("get");
        let parameter = operation.parameters[0].schema.as_ref().expect("schema");
        assert_eq!(
            parameter.ty.as_ref().and_then(TypeField::primary),
            Some("number")
        );
        let response = operation.responses["200"].content["application/json"]
            .schema
            .as_ref()
            .expect("schema");
        let item = response.items.as_deref().expect("items");
        assert_eq!(
            item.ty.as_ref().and_then(TypeField::primary),
            Some("number")
        );
    }

    #[test]
    fn same_primitive_unions_take_their_last_alternative_and_its_name() {
        let mut doc = parse(
            r"
openapi: 3.0.3
info: { title: t, version: '1' }
paths:
  /bins:
    post:
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                bin: { $ref: '#/components/schemas/BinLabel' }
      responses:
        '200':
          description: ok
          content:
            application/json:
              schema: { $ref: '#/components/schemas/Tally' }
components:
  schemas:
    BinLabel:
      anyOf:
        - { type: string, pattern: '^R[0-9]+$' }
        - { type: string, pattern: '^Q[0-9]+$' }
    Tally:
      oneOf:
        - { type: integer }
        - { type: integer, maximum: 10 }
        - { type: integer, minimum: 2 }
    Mixed:
      anyOf: [{ type: string }, { type: integer }]
    Nullable:
      anyOf: [{ type: string }, { type: string }, { nullable: true, type: string }]
    Taken:
      anyOf: [{ type: string }, { type: string }]
    Taken One:
      type: string
",
        );
        normalize_same_primitive_unions(&mut doc);
        // Renamed in place after the last alternative's ordinal, unless that
        // name is already a component's; a `null` or mixed composition keeps
        // its name.
        assert_eq!(
            schema_keys(&doc),
            [
                "BinLabel One",
                "Tally Two",
                "Mixed",
                "Nullable",
                "Taken",
                "Taken One"
            ]
        );
        let label = &doc.components.schemas["BinLabel One"];
        assert!(label.any_of.is_none());
        assert_eq!(label.pattern.as_deref(), Some("^Q[0-9]+$"));
        assert_eq!(
            doc.components.schemas["Tally Two"].minimum,
            Some(serde_json::json!(2))
        );
        let operation = doc.paths["/bins"].post.as_ref().unwrap();
        let body = operation.request_body.as_ref().unwrap().content["application/json"]
            .schema
            .as_ref()
            .unwrap();
        assert_eq!(
            body.properties["bin"].reference.as_deref(),
            Some("#/components/schemas/BinLabel One")
        );
        let response = operation.responses["200"].content["application/json"]
            .schema
            .as_ref()
            .unwrap();
        assert_eq!(
            response.reference.as_deref(),
            Some("#/components/schemas/Tally Two")
        );
    }

    #[test]
    fn declared_type_names_rename_components_and_every_reference() {
        let mut doc = parse(
            r"
openapi: 3.1.0
info: { title: t, version: '1' }
paths:
  /w:
    get:
      responses:
        '200':
          description: ok
          content:
            application/json:
              schema: { $ref: '#/components/schemas/Widget/properties/id' }
webhooks:
  made:
    post:
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                widget: { $ref: '#/components/schemas/Widget' }
components:
  schemas:
    Widget:
      x-fern-type-name: Gadget
      type: object
      properties:
        id: { type: string }
    Holder:
      type: object
      discriminator:
        propertyName: kind
        mapping: { w: '#/components/schemas/Widget' }
      properties:
        widgets: { type: array, items: { $ref: '#/components/schemas/Widget' } }
    Taken:
      x-crozier-type-name: Holder
      type: object
    Same:
      x-fern-type-name: Same
      type: object
    Slashed:
      x-fern-type-name: a/b~c
      type: object
    First:
      x-fern-type-name: Twin
      type: object
    Second:
      x-fern-type-name: Twin
      type: object
",
        );
        normalize_declared_type_names(&mut doc);
        // Renamed in place. A name another component resolves to is one type,
        // kept where and as the first stands (`name_refusals` refuses it unless
        // the schemas agree), and a pointer-splitting `/` or `~` is a space.
        assert_eq!(
            schema_keys(&doc),
            ["Gadget", "Holder", "Same", "a b c", "Twin"]
        );
        assert!(doc.components.schemas["Holder"].discriminator.is_some());
        let holder = &doc.components.schemas["Holder"];
        assert_eq!(
            holder.properties["widgets"]
                .items
                .as_ref()
                .and_then(|items| items.reference.as_deref()),
            Some("#/components/schemas/Gadget")
        );
        assert_eq!(
            holder.discriminator.as_ref().unwrap().mapping["w"],
            "#/components/schemas/Gadget"
        );
        let response = doc.paths["/w"].get.as_ref().unwrap().responses["200"].content
            ["application/json"]
            .schema
            .as_ref()
            .unwrap();
        assert_eq!(
            response.reference.as_deref(),
            Some("#/components/schemas/Gadget/properties/id")
        );
        let payload = doc.webhooks["made"]
            .post
            .as_ref()
            .unwrap()
            .request_body
            .as_ref()
            .unwrap()
            .content["application/json"]
            .schema
            .as_ref()
            .unwrap();
        assert_eq!(
            payload.properties["widget"].reference.as_deref(),
            Some("#/components/schemas/Gadget")
        );
    }

    #[test]
    fn indexed_compositions_are_sorted_and_preserved() {
        let schema: Schema = serde_json::from_value(serde_json::json!({
            "allOf": { "3": { "type": "string" }, "1": { "$ref": "#/components/schemas/Base" } }
        }))
        .expect("indexed allOf parses");
        let members = schema.all_of.expect("allOf is retained");
        assert_eq!(
            members[0].reference.as_deref(),
            Some("#/components/schemas/Base")
        );
        assert_eq!(
            members[1].ty.as_ref().and_then(TypeField::primary),
            Some("string")
        );
    }

    #[test]
    fn non_indexed_composition_maps_are_rejected() {
        let error = serde_json::from_value::<Schema>(serde_json::json!({
            "oneOf": { "variant": { "type": "string" } }
        }))
        .expect_err("non-indexed composition must fail");
        assert!(
            error.to_string().contains("not a non-negative integer"),
            "{error}"
        );
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
    fn ignore_extension_drops_ops_via_both_spellings_and_keeps_their_schemas() {
        let mut doc = parse(IGNORE_SPEC);
        filter_ignored(&mut doc);
        // Both `x-fern-ignore` and `x-crozier-ignore` operations are gone.
        assert_eq!(op_ids(&doc), ["keepOp"]);
        // The paths of the ignored ops are removed entirely.
        assert_eq!(doc.paths.keys().cloned().collect::<Vec<_>>(), ["/keep"]);
        // The schemas only the ignored ops referenced stay, as they do in Fern's
        // TrueForge golden.
        assert_eq!(schema_keys(&doc), ["Keep", "OnlyFern", "OnlyCrozier"]);
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
    fn schema_level_ignore_keeps_the_schemas_only_it_referenced() {
        // Fern 5.20.0 keeps `LegacyPart`, whose one referrer is the ignored
        // `LegacyWidget` (the hand-written fixture `x-fern-ignore-schema`).
        let mut doc = parse(
            r##"
openapi: 3.0.3
info: { title: T }
paths:
  /widgets:
    get:
      operationId: getWidget
      responses:
        "200": { description: OK, content: { application/json: { schema: { $ref: "#/components/schemas/Widget" } } } }
components:
  schemas:
    Widget: { type: object, properties: { id: { type: string } } }
    LegacyWidget:
      x-fern-ignore: true
      type: object
      properties: { part: { $ref: "#/components/schemas/LegacyPart" } }
    LegacyPart: { type: object, properties: { serial: { type: string } } }
"##,
        );
        filter_ignored(&mut doc);
        assert_eq!(schema_keys(&doc), ["Widget", "LegacyPart"]);
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
        assert_eq!(
            ok.reference.as_deref(),
            Some("#/components/responses/ItemsResponse")
        );
    }

    #[test]
    fn a_pointer_inside_a_component_is_copied_where_it_is_used() {
        let mut doc = parse(
            r##"
openapi: 3.1.0
info: { title: T }
paths: {}
components:
  schemas:
    Page:
      type: object
      properties:
        page:
          type: object
          properties:
            kind: { type: string }
        tags:
          type: array
          items: { type: string, enum: [a, b] }
        extra:
          type: object
          additionalProperties: { type: integer }
        closed:
          type: object
          additionalProperties: false
        choice:
          anyOf:
            - type: object
              properties:
                label: { type: string }
            - type: string
        revision:
          type: object
          properties:
            page: { $ref: '#/components/schemas/Page/properties/page' }
            tag: { $ref: '#/components/schemas/Page/properties/tags/items' }
            count: { $ref: '#/components/schemas/Page/properties/extra/additionalProperties' }
            label: { $ref: '#/components/schemas/Page/properties/choice/anyOf/0/properties/label' }
            member: { $ref: '#/components/schemas/Page/properties/choice/anyOf/1' }
            open: { $ref: '#/components/schemas/Page/properties/closed/additionalProperties' }
            missing: { $ref: '#/components/schemas/Page/properties/nothing' }
            defs: { $ref: '#/components/schemas/Page/$defs/thing' }
            whole: { $ref: '#/components/schemas/Page' }
            again:
              allOf:
                - $ref: '#/components/schemas/Page/properties/choice'
              nullable: true
              description: the reply
    Loop:
      type: object
      properties:
        next: { $ref: '#/components/schemas/Loop/properties/next' }
"##,
        );
        normalize_schema_pointer_refs(&mut doc);
        let revision = &doc.components.schemas["Page"].properties["revision"];
        // Walked through `properties`, `items`, `additionalProperties` and a
        // composition member, each copy is the schema the pointer reaches.
        assert!(revision.properties["page"].properties.contains_key("kind"));
        assert!(revision.properties["page"].reference.is_none());
        assert!(revision.properties["tag"].enum_values.is_some());
        assert_eq!(
            revision.properties["count"]
                .ty
                .as_ref()
                .and_then(TypeField::primary),
            Some("integer")
        );
        assert_eq!(
            revision.properties["label"]
                .ty
                .as_ref()
                .and_then(TypeField::primary),
            Some("string")
        );
        // A pointer whose text names `properties` is copied even where it ends
        // on a composition member, as Fern's importer copies the hand-written
        // `ref-pointer-walk` fixture's `…/Route/properties/from/oneOf/0`, and the copy
        // remembers the pointer it came from.
        let member = &revision.properties["member"];
        assert!(member.reference.is_none());
        assert_eq!(
            member.ty.as_ref().and_then(TypeField::primary),
            Some("string")
        );
        assert_eq!(
            member.ref_origin.as_deref(),
            Some("#/components/schemas/Page/properties/choice/anyOf/1")
        );
        // One through a non-schema `additionalProperties`, to nothing, through
        // `$defs`, or at a whole component is left for the lowering.
        for kept in ["open", "missing", "defs", "whole"] {
            assert!(
                revision.properties[kept].reference.is_some(),
                "{kept} should keep its $ref"
            );
        }
        // A lone pointer `allOf` member is its holder's schema, keeping the
        // holder's own annotations.
        let again = &revision.properties["again"];
        assert!(again.all_of.is_none());
        assert_eq!(again.any_of.as_ref().map(Vec::len), Some(2));
        assert_eq!(again.nullable, Some(true));
        assert_eq!(again.description.as_deref(), Some("the reply"));
        // A pointer met again while its own copy expands terminates, as the
        // unknown type: left a reference, the IR expanded it again wherever
        // it was used.
        let next = &doc.components.schemas["Loop"].properties["next"];
        assert!(next.reference.is_none());
        assert!(next.ty.is_none() && next.properties.is_empty() && next.one_of.is_none());
    }

    #[test]
    fn a_properties_pointer_walks_through_defs() {
        let mut doc = parse(
            r##"
openapi: 3.1.0
info: { title: T }
paths: {}
components:
  schemas:
    Named:
      type: object
      $defs:
        top: { type: integer }
      properties:
        label:
          type: string
          $defs:
            inner: { type: string }
        odd:
          type: string
          $defs: true
    Holder:
      type: object
      properties:
        names:
          type: array
          items: { $ref: '#/components/schemas/Named/properties/label/$defs/inner' }
        inner: { $ref: '#/components/schemas/Named/properties/label/$defs/inner' }
        missing: { $ref: '#/components/schemas/Named/properties/label/$defs/absent' }
        top: { $ref: '#/components/schemas/Named/$defs/top' }
"##,
        );
        // A `$defs` value that is no map defines nothing rather than failing.
        assert!(doc.components.schemas["Named"].properties["odd"]
            .defs
            .is_empty());
        normalize_schema_pointer_refs(&mut doc);
        let holder = &doc.components.schemas["Holder"];
        // Through `properties`, the walk enters a `$defs` member and copies it,
        // wherever the pointer stands.
        for copied in [
            holder.properties["names"].items.as_deref().unwrap(),
            &holder.properties["inner"],
        ] {
            assert!(copied.reference.is_none());
            assert_eq!(
                copied.ty.as_ref().and_then(TypeField::primary),
                Some("string")
            );
        }
        // A missing member, and a pointer without the word, are left alone.
        for kept in ["missing", "top"] {
            assert!(holder.properties[kept].reference.is_some(), "{kept}");
        }
    }

    #[test]
    fn a_nested_pointer_naming_nothing_is_unknown_except_as_an_array_item() {
        let mut doc = parse(
            r##"
openapi: 3.1.0
info: { title: T }
paths:
  /holder:
    post:
      requestBody:
        content:
          application/json:
            schema: { $ref: '#/components/schemas/Named/properties/absent' }
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema: { $ref: '#/components/schemas/Named/properties/absent' }
components:
  schemas:
    Named:
      type: object
      properties:
        label: { type: string }
    Choice:
      oneOf:
        - type: object
          properties:
            code: { type: integer }
    Holder:
      type: object
      properties:
        ghost: { $ref: '#/components/schemas/Named/properties/absent', description: gone }
        itemless: { $ref: '#/components/schemas/Named/items' }
        names:
          type: array
          items: { $ref: '#/components/schemas/Named/properties/absent' }
        byName:
          type: object
          additionalProperties: { $ref: '#/components/schemas/Named/properties/absent' }
        merged:
          description: kept
          allOf:
            - $ref: '#/components/schemas/Named/properties/absent'
        beside:
          type: object
          allOf:
            - $ref: '#/components/schemas/Named/properties/absent'
        outOfRange: { $ref: '#/components/schemas/Choice/oneOf/3/properties/code' }
        badIndex: { $ref: '#/components/schemas/Choice/oneOf/x/properties/code' }
        noComposition: { $ref: '#/components/schemas/Named/anyOf/0/properties/code' }
        member: { $ref: '#/components/schemas/Choice/oneOf/0' }
        defs: { $ref: '#/components/schemas/Named/$defs/thing' }
        trailing: { $ref: '#/components/schemas/Named/properties' }
        whole: { $ref: '#/components/schemas/Named' }
        undeclared: { $ref: '#/components/schemas/Missing/properties/absent' }
        found: { $ref: '#/components/schemas/Choice/oneOf/0/properties/code' }
        foreign: { $ref: '#/definitions/Named/properties/absent' }
"##,
        );
        // The copy pass runs first, as the loader runs it, so `found` resolves.
        normalize_schema_pointer_refs(&mut doc);
        normalize_unresolved_schema_pointers(&mut doc);
        let holder = &doc.components.schemas["Holder"];
        for unknown in [
            "ghost",
            "itemless",
            "outOfRange",
            "badIndex",
            "noComposition",
        ] {
            let node = &holder.properties[unknown];
            assert!(
                node.reference.is_none() && node.unresolved_reference,
                "{unknown}"
            );
        }
        assert_eq!(
            holder.properties["ghost"].description.as_deref(),
            Some("gone")
        );
        let value = match &holder.properties["byName"].additional_properties {
            Some(AdditionalProperties::Schema(value)) => value,
            other => panic!("{other:?}"),
        };
        assert!(value.reference.is_none() && value.unresolved_reference);
        // A lone member is its holder's schema, so the holder is unknown and
        // keeps its own annotations; beside a `type` it is only a member.
        let merged = &holder.properties["merged"];
        assert!(merged.all_of.is_none() && merged.unresolved_reference);
        assert_eq!(merged.description.as_deref(), Some("kept"));
        let beside = &holder.properties["beside"];
        assert!(!beside.unresolved_reference);
        let member = &beside.all_of.as_ref().unwrap()[0];
        assert!(member.reference.is_none() && member.unresolved_reference);
        // An array's element keeps its pointer for the element lowering.
        let names = holder.properties["names"].items.as_deref().unwrap();
        assert!(names.reference.is_some() && !names.unresolved_reference);
        // The lowering's unknown pointers, a whole component, an undeclared
        // head and a pointer outside the components are not this pass's.
        for kept in [
            "member",
            "defs",
            "trailing",
            "whole",
            "undeclared",
            "foreign",
        ] {
            let node = &holder.properties[kept];
            assert!(
                node.reference.is_some() && !node.unresolved_reference,
                "{kept}"
            );
        }
        assert!(
            holder.properties["found"].reference.is_none()
                && !holder.properties["found"].unresolved_reference
        );
        // Request and response bodies are degraded as any other position is.
        let operation = doc.paths["/holder"].post.as_ref().unwrap();
        let body = operation.request_body.as_ref().unwrap().content["application/json"]
            .schema
            .as_ref()
            .unwrap();
        assert!(body.reference.is_none() && body.unresolved_reference);
        let response = operation.responses["200"].content["application/json"]
            .schema
            .as_ref()
            .unwrap();
        assert!(response.reference.is_none() && response.unresolved_reference);
    }

    #[test]
    fn a_document_whose_pointers_all_resolve_is_untouched() {
        let mut doc = parse(
            r##"
openapi: 3.1.0
info: { title: T }
paths: {}
components:
  schemas:
    Named:
      type: object
      properties:
        label: { type: string }
    Holder:
      type: object
      properties:
        whole: { $ref: '#/components/schemas/Named' }
"##,
        );
        normalize_unresolved_schema_pointers(&mut doc);
        let whole = &doc.components.schemas["Holder"].properties["whole"];
        assert_eq!(
            whole.reference.as_deref(),
            Some("#/components/schemas/Named")
        );
    }

    #[test]
    fn an_object_whose_required_is_not_a_list_is_unknown() {
        let mut doc = parse(
            r##"
openapi: 3.0.0
info: { title: T }
paths: {}
components:
  schemas:
    Request:
      type: object
      required: [data]
      properties:
        data:
          type: object
          properties:
            kind: { type: string, required: true }
            attributes:
              description: the attributes
              type: object
              required: false
              properties:
                funded: { type: boolean }
            counted: { properties: { n: { type: integer } }, required: 3 }
            mapped: { type: object, required: { a: 1 } }
            nulled: { type: object, required: null }
"##,
        );
        normalize_unlisted_required(&mut doc);
        let data = &doc.components.schemas["Request"].properties["data"];
        let attributes = &data.properties["attributes"];
        assert!(attributes.ty.is_none() && attributes.properties.is_empty());
        assert_eq!(attributes.description.as_deref(), Some("the attributes"));
        assert!(attributes.required.is_unlisted());
        assert!(data.properties["counted"].properties.is_empty());
        assert!(data.properties["mapped"].required.is_unlisted());
        // A scalar's stray `required: true` changes nothing and leaves no mark;
        // neither does a `null`, nor a real list.
        let kind = &data.properties["kind"];
        assert_eq!(
            kind.ty.as_ref().and_then(TypeField::primary),
            Some("string")
        );
        assert!(!kind.required.is_unlisted());
        assert!(!data.properties["nulled"].required.is_unlisted());
        assert!(data.required.is_empty());
        assert_eq!(
            &doc.components.schemas["Request"].required[..],
            &["data".to_string()]
        );
        // Requiring a name of an unlisted `required` makes it a list of that name.
        let mut merged = RequiredNames::Unlisted;
        merged.push("id".to_string());
        assert_eq!(merged, RequiredNames::from(vec!["id".to_string()]));
    }

    #[test]
    fn enum_varnames_lose_the_prefix_every_name_shares() {
        let doc = parse(
            r##"
openapi: 3.0.0
info: { title: T }
paths: {}
components:
  schemas:
    OperationKind:
      type: string
      enum: [profiling, tracing]
      x-enum-varnames: [OperationKindProfiling, OperationKindTracing]
    Single:
      type: string
      enum: ["1.0"]
      x-enum-varnames: [WatchEventSpecVersion10]
    Uneven:
      type: string
      enum: [a, b]
      x-enum-varnames: [Ab, A]
"##,
        );
        let names = |name: &str| {
            doc.components.schemas[name]
                .enum_member_names()
                .map(|(value, name)| format!("{value}={name}"))
                .collect::<Vec<_>>()
        };
        assert_eq!(
            names("OperationKind"),
            ["profiling=Profiling", "tracing=Tracing"]
        );
        // One name has nothing to share; a name that is all prefix is blank and
        // names nothing.
        assert_eq!(names("Single"), ["1.0=WatchEventSpecVersion10"]);
        assert_eq!(names("Uneven"), ["a=b"]);
    }

    /// An empty `oneOf` constrains nothing. Left in place it reads downstream as
    /// "this node is a union" and renders `typing.Union[]`, which `ruff` refuses
    /// to parse — so the node keeps the plain `type` it also declares.
    #[test]
    fn normalize_empty_compositions_drops_the_empty_list() {
        let mut doc = parse(
            r##"
openapi: 3.0.0
info: { title: T }
paths: {}
components:
  schemas:
    ApplicationCommandHandler:
      type: integer
      format: int32
      oneOf: []
    Wrapper:
      type: object
      properties:
        handler:
          allOf: []
          anyOf: []
          type: string
"##,
        );
        normalize_empty_compositions(&mut doc);
        let handler = &doc.components.schemas["ApplicationCommandHandler"];
        assert!(handler.one_of.is_none());
        assert_eq!(
            handler.ty.as_ref().and_then(TypeField::primary),
            Some("integer")
        );
        let nested = &doc.components.schemas["Wrapper"].properties["handler"];
        assert!(nested.all_of.is_none() && nested.any_of.is_none());
    }

    #[test]
    fn only_unquoted_yaml_dates_are_recorded_as_timestamps() {
        let text = "a: 2022-01-23T19:00:00.000Z\nb: \"1909-04-05\"\nc: {x: 2001-02-03, y: 'x'}\nid: v2022-01-01\n";
        let found = unquoted_yaml_timestamps(text);
        assert!(found.contains("2022-01-23T19:00:00.000Z"));
        assert!(found.contains("2001-02-03"));
        assert!(!found.contains("1909-04-05"));
        assert_eq!(found.len(), 2);
    }

    /// A reference to a schema the document never declares is Fern's unknown
    /// value, not an invented class: crozier would otherwise emit Python that
    /// imports a module it never wrote. Reachable in practice through a fetched
    /// remote fragment naming a sibling the root document does not assemble.
    #[test]
    fn normalize_unresolvable_schema_refs_degrades_to_the_unknown_type() {
        let mut doc = parse(
            r##"
openapi: 3.0.0
info: { title: T }
paths:
  /items:
    get:
      operationId: getItems
      responses:
        "200":
          description: OK
          content:
            application/json: { schema: { $ref: "#/components/schemas/Missing" } }
components:
  schemas:
    Item:
      type: object
      properties:
        known: { $ref: "#/components/schemas/Known" }
        unknown: { $ref: "#/components/schemas/NeverDeclared" }
      allOf:
        - { $ref: "#/components/schemas/NeverDeclared" }
    Known:
      type: string
"##,
        );
        normalize_unresolvable_schema_refs(&mut doc);
        let item = &doc.components.schemas["Item"];
        assert_eq!(
            item.properties["known"].reference.as_deref(),
            Some("#/components/schemas/Known")
        );
        assert_eq!(item.properties["unknown"].reference, None);
        assert_eq!(item.all_of.as_ref().unwrap()[0].reference, None);
        let response = &doc.paths["/items"].get.as_ref().unwrap().responses["200"];
        assert_eq!(
            response.content["application/json"]
                .schema
                .as_ref()
                .unwrap()
                .reference,
            None
        );
    }

    /// Fern keeps a schema's nullability at its use sites rather than in the
    /// alias it declares, so a reference to one is optional wherever it appears.
    #[test]
    fn normalize_nullable_schema_refs_marks_every_reference_nullable() {
        let mut doc = parse(
            r##"
openapi: 3.0.0
info: { title: T }
components:
  schemas:
    Topic:
      oneOf:
        - { type: "null" }
        - { type: string }
    Solid:
      type: string
    Holder:
      type: object
      properties:
        topic: { $ref: "#/components/schemas/Topic" }
        solid: { $ref: "#/components/schemas/Solid" }
        topics:
          type: array
          items: { $ref: "#/components/schemas/Topic" }
"##,
        );
        normalize_nullable_schema_refs(&mut doc);
        let holder = &doc.components.schemas["Holder"];
        assert_eq!(holder.properties["topic"].nullable, Some(true));
        assert_eq!(holder.properties["solid"].nullable, None);
        assert_eq!(
            holder.properties["topics"]
                .items
                .as_ref()
                .expect("array items")
                .nullable,
            Some(true)
        );
    }

    /// A component schema that is nothing but a *local* `$ref` keeps its own name
    /// everywhere, including where an operation response names it.
    ///
    /// Probed directly at `fernapi/fern-python-sdk:5.20.0`: on a document
    /// declaring `AliasOfThing: {$ref: Thing}` and a response naming
    /// `AliasOfThing`, Fern generates `-> AliasOfThing` at exit 0 — with a
    /// sibling `title`, `description` or `unevaluatedProperties` on the alias
    /// too, with the alias declared either side of its target, and with the
    /// target referenced elsewhere as well. The response-alias rewrite is
    /// therefore confined to aliases of a *remotely* declared schema, which
    /// `a_response_alias_of_a_fetched_schema_resolves_to_the_fetched_name` covers.
    #[test]
    fn an_in_document_security_scheme_ref_resolves_to_the_scheme_it_names() {
        // Measured at fernapi/fern-python-sdk:5.20.0 on
        // docs/openapi-surface/probes/securityscheme-ref.yml: Fern follows a
        // `#/components/securitySchemes/…` reference and imports the referenced
        // scheme under the REFERENCING key, so the probe's two map entries emit two
        // credentials where its control's one entry emits one.
        let mut doc = parse(
            r##"
openapi: 3.0.3
info: { title: T }
paths: {}
components:
  securitySchemes:
    ProbeScheme: { $ref: "#/components/securitySchemes/ProbeApiKey" }
    ProbeApiKey: { type: apiKey, name: X-Probe-Key, in: header }
"##,
        );
        normalize_security_scheme_refs(&mut doc);
        let resolved = &doc.components.security_schemes["ProbeScheme"];
        assert_eq!(resolved.ty, SecuritySchemeType::ApiKey);
        assert_eq!(resolved.name.as_deref(), Some("X-Probe-Key"));
        assert_eq!(resolved.location, Some(ParameterLocation::Header));
        assert!(
            resolved.reference.is_none(),
            "the resolved entry is the scheme itself, not a reference to it"
        );
    }

    #[test]
    fn a_security_scheme_ref_crozier_cannot_follow_is_left_alone() {
        // Fern refuses a cross-document reference here — it prints `Failed to
        // resolve` out of `resolveSecuritySchemeReference` and parses nothing, which
        // is what `docs/openapi-surface/security.md`'s `securityscheme-ref` row
        // records of the Open-EO witness. A reference naming another reference, or
        // naming itself, resolves to nothing importable either. All three stay the
        // unrecognized scheme they deserialized to.
        let mut doc = parse(
            r##"
openapi: 3.0.3
info: { title: T }
paths: {}
components:
  securitySchemes:
    Across: { $ref: "../../openapi.yaml#/components/securitySchemes/Bearer" }
    Chained: { $ref: "#/components/securitySchemes/Across" }
    Itself: { $ref: "#/components/securitySchemes/Itself" }
    Missing: { $ref: "#/components/securitySchemes/Absent" }
"##,
        );
        normalize_security_scheme_refs(&mut doc);
        for name in ["Across", "Chained", "Itself", "Missing"] {
            let scheme = &doc.components.security_schemes[name];
            assert_eq!(
                scheme.ty,
                SecuritySchemeType::Other,
                "{name} names no scheme crozier can import"
            );
            assert!(scheme.reference.is_some(), "{name} keeps its reference");
        }
    }

    #[test]
    fn a_local_ref_alias_keeps_its_name_in_a_response() {
        let mut doc = parse(
            r##"
openapi: 3.0.0
info: { title: T }
paths:
  /block:
    get:
      operationId: getBlock
      responses:
        "200":
          description: OK
          content:
            application/json: { schema: { $ref: "#/components/schemas/BlockResponse" } }
components:
  schemas:
    BlockResponse: { $ref: "#/components/schemas/Block" }
    Block:
      type: object
      properties:
        hash: { type: string }
    Holder:
      type: object
      properties:
        block: { $ref: "#/components/schemas/BlockResponse" }
"##,
        );
        normalize_fetched_response_alias_refs(&mut doc, &std::collections::BTreeSet::new());
        let response = &doc.paths["/block"].get.as_ref().unwrap().responses["200"];
        assert_eq!(
            response.content["application/json"]
                .schema
                .as_ref()
                .unwrap()
                .reference
                .as_deref(),
            Some("#/components/schemas/BlockResponse")
        );
        assert_eq!(
            doc.components.schemas["BlockResponse"].reference.as_deref(),
            Some("#/components/schemas/Block")
        );
    }

    /// The other half of the same rule: where the alias target *was* declared by a
    /// remote `$ref`, the response resolves to it — `helios-verifiable-api`'s
    /// `BlockResponse` over its fetched `Block` — while a reference from inside
    /// another schema still keeps the alias name.
    #[test]
    fn a_response_alias_of_a_fetched_schema_resolves_to_the_fetched_name() {
        let mut doc = parse(
            r##"
openapi: 3.0.0
info: { title: T }
paths:
  /block:
    get:
      operationId: getBlock
      responses:
        "200":
          description: OK
          content:
            application/json: { schema: { $ref: "#/components/schemas/BlockResponse" } }
components:
  schemas:
    BlockResponse: { $ref: "#/components/schemas/Block" }
    Block:
      type: object
      properties:
        hash: { type: string }
    Holder:
      type: object
      properties:
        block: { $ref: "#/components/schemas/BlockResponse" }
"##,
        );
        let remote_origin = std::collections::BTreeSet::from(["Block".to_string()]);
        normalize_fetched_response_alias_refs(&mut doc, &remote_origin);
        let response = &doc.paths["/block"].get.as_ref().unwrap().responses["200"];
        assert_eq!(
            response.content["application/json"]
                .schema
                .as_ref()
                .unwrap()
                .reference
                .as_deref(),
            Some("#/components/schemas/Block")
        );
        assert_eq!(
            doc.components.schemas["Holder"].properties["block"]
                .reference
                .as_deref(),
            Some("#/components/schemas/BlockResponse")
        );
        assert_eq!(
            doc.components.schemas["BlockResponse"].reference.as_deref(),
            Some("#/components/schemas/Block")
        );
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

    /// `PathItem` holds one `Option<Operation>` per HTTP method, and serde's derived
    /// `visit_map` keeps a separate stack local for every field it may fill — so the
    /// deserializer's frame grows with `size_of::<PathItem>()`, not with document
    /// depth. Windows gives `main` a 1 MiB stack (Linux 8 MiB), so a `PathItem` that
    /// is merely large overflows there while passing everywhere else: two unboxed
    /// `Option<Streaming>` extension fields once took `Operation` to 4_696 bytes and
    /// `PathItem` to 28_200, and a debug build blew the Windows stack parsing an
    /// ordinary fixture. Keep large, rarely-present payloads behind a `Box`. This
    /// ceiling is a headroom check rather than an exact size — widen it only with a
    /// deliberate reason, and never by un-boxing.
    #[test]
    fn path_item_stays_small_enough_for_a_1mib_windows_stack() {
        let path_item = std::mem::size_of::<PathItem>();
        assert!(
            path_item <= 8_192,
            "PathItem grew to {path_item} bytes (Operation {}); serde's visit_map \
             frame scales with it and overflows the 1 MiB Windows main stack. Box a \
             large rarely-present field rather than raising this ceiling.",
            std::mem::size_of::<Operation>()
        );
    }
}

#[cfg(test)]
mod refusal_name_tests {
    #[test]
    fn declared_parameter_names_obey_dual_header_precedence() {
        for (text, expected) in [
            ("x-fern-parameter-name: fernName", Some("fernName")),
            (
                "x-crozier-parameter-name: crozierName\nx-fern-parameter-name: fernName",
                Some("crozierName"),
            ),
            (
                "x-crozier-parameter-name: null\nx-fern-parameter-name: fernName",
                Some("fernName"),
            ),
            ("type: string", None),
        ] {
            let node = serde_yaml_ng::from_str(text).unwrap();
            assert_eq!(super::refusal_parameter_name(&node), expected);
        }
    }

    /// The source-node reader and the typed accessor agree on every precedence
    /// case: canonical first, Fern as the fallback, a blank value no override.
    #[test]
    fn declared_property_names_obey_dual_header_precedence() {
        for (text, expected) in [
            ("x-fern-property-name: fern_name", Some("fern_name")),
            (
                "x-crozier-property-name: crozier_name",
                Some("crozier_name"),
            ),
            (
                "x-crozier-property-name: crozier_name\nx-fern-property-name: fern_name",
                Some("crozier_name"),
            ),
            (
                "x-crozier-property-name: null\nx-fern-property-name: fern_name",
                Some("fern_name"),
            ),
            ("x-fern-property-name: '  '", None),
            ("type: string", None),
        ] {
            let node: serde_yaml_ng::Value = serde_yaml_ng::from_str(text).unwrap();
            assert_eq!(super::refusal_property_name(&node), expected, "{text}");
            let schema: super::Schema = serde_yaml_ng::from_value(node).unwrap();
            assert_eq!(schema.property_name(), expected, "{text}");
        }
    }
}
