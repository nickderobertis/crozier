//! The intermediate representation: a small, generation-ready model built from
//! the OpenAPI document, decoupling parsing from emission. Schema and property
//! order is preserved from the document so generated output is deterministic.

use indexmap::IndexMap;

use crate::config::GenerateConfig;
use crate::naming;
use crate::openapi::{
    AdditionalProperties, OpenApi, Operation, ParameterLocation, Response, Schema, TypeField,
};

/// A fully-resolved SDK model ready to emit.
#[derive(Debug)]
pub struct Ir {
    /// Whether the source uses the OpenAPI 3.1 importer behavior.
    pub openapi_31: bool,
    /// Python import package name (directory under `src/`).
    pub package_name: String,
    /// Distribution name recorded in `version.py`.
    pub project_name: String,
    /// The root client class name (`FernApi`), from which the async name
    /// (`AsyncFernApi`) is derived. Fern names it from the workspace
    /// organization; crozier's closest input is the package name, so it is
    /// `PascalCase(package_name) + "Api"` (matching the vendored fixture, whose
    /// organization and package are both `fern`).
    pub client_name: String,
    /// Generated types, in document order.
    pub types: Vec<TypeDecl>,
    /// Types hoisted out of an operation's inline request/response body, each
    /// scoped to its tag's own `types/` package (Fern's `inlined/types/` layout).
    pub tag_types: Vec<TagTypeDecl>,
    /// Endpoint client module (directory) names, one per operation group, in
    /// first-seen order.
    pub endpoint_modules: Vec<String>,
    /// The `reference.md` section title for each module, keyed by module name.
    /// Verbatim tag (`attachment-public`) for an underscore-style operationId,
    /// PascalCase tag (`Widgets`) for a camelCase one, PascalCase group when
    /// untagged (`EndpointsContainer`) — see `module_title` for the full rule.
    pub endpoint_module_titles: std::collections::BTreeMap<String, String>,
    /// Every operation, in document-traversal order, resolved for emission.
    pub endpoints: Vec<Endpoint>,
    /// Generated exception classes, one per distinct declared error response.
    pub errors: Vec<ErrorClass>,
    /// The authentication model that shapes the client wrapper and root client.
    pub auth: Auth,
    /// Operation headers promoted to client-wrapper-level "global" fields (Fern
    /// lifts an optional operation header, e.g. `X-Tenant` → `tenant`, out of the
    /// method signature and sets it once at client construction).
    pub global_headers: Vec<GlobalHeader>,
    /// The server-environment model, when the document declares `servers`. Drives
    /// `environment.py` and threads an `environment`/optional-`base_url` through
    /// the root client.
    pub environment: Option<Environment>,
    /// How generated pydantic models treat unknown fields (Fern's
    /// `pydantic_config.extra_fields`); drives every model's `extra` config.
    pub extra_fields: crate::settings::ExtraFields,
}

/// The generated server-environment enum (`environment.py`). Fern maps the
/// document's `servers` to an `enum.Enum`, but its OpenAPI importer emits only a
/// single member — the first server, named from its description — even when the
/// document lists several (the "2 servers → only `PRODUCTION`" oddity noted in
/// issue #14). crozier reproduces that observed behavior.
#[derive(Debug, Clone)]
pub struct Environment {
    /// The enum class name (`{ClientName}Environment`, e.g. `FernApiEnvironment`).
    pub enum_name: String,
    /// The single emitted member: (member name, URL value).
    pub member: (String, String),
}

impl Environment {
    /// The default member reference used in the root client (`FernApiEnvironment.DEFAULT`).
    #[must_use]
    pub fn default_ref(&self) -> String {
        format!("{}.{}", self.enum_name, self.member.0)
    }
}

/// Derive the [`Environment`] model from the document's `servers`. Reproduces
/// Fern's single-member behavior: the first server only, its member named by
/// uppercasing the description (non-identifier characters → `_`). A templated
/// server, or a single concrete server with no usable description, is `DEFAULT`;
/// described concrete servers keep their description-derived name.
fn environment_model(doc: &OpenApi, client_name: &str) -> Option<Environment> {
    let first = doc.servers.first()?;
    // A server with a templated URL (`{basePath}` variables) is named `DEFAULT` — its
    // member value is the variables resolved to their defaults (bunq). A concrete-URL
    // server takes its member name from its description, even across several servers
    // (the `servers-webhooks` seed's Production/Staging pair keeps `PRODUCTION`).
    let member_name = if !first.variables.is_empty() || first.url.starts_with('/') {
        "DEFAULT".to_string()
    } else {
        first
            .description
            .as_deref()
            .map(env_member_name)
            .filter(|n| !n.is_empty())
            .unwrap_or_else(|| "DEFAULT".to_string())
    };
    Some(Environment {
        enum_name: format!("{client_name}Environment"),
        member: (member_name, resolve_server_url(first)),
    })
}

/// Substitute a server URL's `{var}` placeholders with each variable's `default`
/// (`https://.../{basePath}` → `https://.../v1`), matching Fern.
fn resolve_server_url(server: &crate::openapi::Server) -> String {
    let mut url = server.url.clone();
    for (name, var) in &server.variables {
        url = url.replace(&format!("{{{name}}}"), &var.default);
    }
    if url == "/" {
        return String::new();
    }
    url
}

/// Turn a server description into a Python enum member identifier: uppercased,
/// with each run of non-alphanumeric characters collapsed to a single `_`.
fn env_member_name(description: &str) -> String {
    let mut out = String::new();
    let mut prev_underscore = false;
    for ch in description.chars() {
        if ch.is_ascii_alphanumeric() {
            out.push(ch.to_ascii_uppercase());
            prev_underscore = false;
        } else if !prev_underscore && !out.is_empty() {
            out.push('_');
            prev_underscore = true;
        }
    }
    out.trim_end_matches('_').to_string()
}

/// An operation header promoted to a client-wrapper-level field. Fern lifts a
/// header carried by *every* operation out of the methods and applies it once at
/// client construction — `X-Tenant` becomes the `tenant` constructor field. A
/// header on only some operations stays a per-method parameter (e.g. exhaustive's
/// `X-TEST-ENDPOINT-HEADER`). `required` drives the rendering: a required global
/// header is a mandatory `str` constructor arg set unconditionally, an optional one
/// is `Optional[str] = None` set only when provided.
#[derive(Debug, Clone)]
pub struct GlobalHeader {
    /// The wire header name (the `headers` dict key), e.g. `X-Tenant`.
    pub wire_name: String,
    /// The Python field/parameter name, e.g. `tenant` (the `X-` prefix dropped).
    pub py_name: String,
    /// Whether the header is required on every operation (so the constructor arg is
    /// mandatory and the `get_headers` assignment is unconditional).
    pub required: bool,
}

/// Collect the operation headers Fern promotes to client-wrapper-level fields: a
/// header present on **every** operation (a ubiquitous header like `X-App-Id` is an
/// SDK-wide setting, not a per-call argument). A header on a subset of operations
/// stays a per-method parameter. Fern orders the promoted headers optional-first —
/// keeping the optional group in the spec's first-appearance order, and the required
/// group by field name — and never promotes a transport-managed header (`User-Agent`,
/// which the HTTP client sets itself), even when it rides every operation.
fn global_headers(doc: &OpenApi) -> Vec<GlobalHeader> {
    let mut total = 0usize;
    // wire name → (operations carrying it, required in every one so far), first-seen.
    let mut seen: IndexMap<String, (usize, bool)> = IndexMap::new();
    for item in doc.paths.values() {
        for (_, op) in item.operations() {
            total += 1;
            let mut in_op: std::collections::HashSet<&str> = std::collections::HashSet::new();
            for p in &op.parameters {
                if p.location == Some(ParameterLocation::Header) && in_op.insert(p.name.as_str()) {
                    let entry = seen.entry(p.name.clone()).or_insert((0, true));
                    entry.0 += 1;
                    entry.1 = entry.1 && p.required == Some(true);
                }
            }
        }
    }
    // Promote a header that rides *every* operation. A required header on a
    // *single* operation is that call's own argument, not an SDK-wide setting, so
    // it stays a per-method parameter (Fern only promotes a solo header when it is
    // optional). With more than one operation, "on every one" is a deliberate
    // cross-cutting header and promotes regardless of required-ness. `User-Agent` is
    // never promoted — the client owns it — so it is dropped even when ubiquitous.
    let mut headers: Vec<GlobalHeader> = seen
        .into_iter()
        .filter(|(wire_name, (count, required))| {
            total > 0
                && *count == total
                && (!*required || total > 1)
                && !is_transport_managed_header(wire_name)
        })
        .map(|(wire_name, (_, required))| GlobalHeader {
            py_name: naming::field_name(header_param_stem(&wire_name)),
            wire_name,
            required,
        })
        .collect();
    // Fern also treats additional header apiKey security schemes as SDK-wide
    // constructor fields. The first apiKey scheme is the auth credential
    // (`api_key`); subsequent header schemes are named from their wire header.
    // Skip any already promoted above: apideck's `app_id`/`consumer_id` ride every
    // operation, so they are promoted from `seen` too — re-adding them here would
    // emit the constructor field twice (invalid Python: duplicate parameter).
    let promoted: std::collections::HashSet<String> =
        headers.iter().map(|h| h.py_name.clone()).collect();
    headers.extend(
        additional_api_key_global_headers(doc)
            .into_iter()
            .filter(|h| !promoted.contains(&h.py_name)),
    );
    // Optional-first. The `sort_by` is stable, so optional headers keep the
    // first-appearance order they already carry from `seen` (an insertion-ordered
    // map); required headers sort by field name (apideck's `app_id`/`consumer_id`,
    // appwrite's `appwrite_key`/`appwrite_locale`/`appwrite_project`).
    headers.sort_by(|a, b| {
        a.required.cmp(&b.required).then_with(|| {
            if a.required {
                a.py_name.cmp(&b.py_name)
            } else {
                std::cmp::Ordering::Equal
            }
        })
    });
    headers
}

fn additional_api_key_global_headers(doc: &OpenApi) -> Vec<GlobalHeader> {
    use crate::openapi::SecuritySchemeType;

    let mut skipped_primary = false;
    doc.components
        .security_schemes
        .values()
        .filter_map(|scheme| {
            if scheme.ty != SecuritySchemeType::ApiKey
                || scheme.location != Some(ParameterLocation::Header)
            {
                return None;
            }
            if !skipped_primary {
                skipped_primary = true;
                return None;
            }
            let wire_name = scheme.name.as_ref()?;
            if is_transport_managed_header(wire_name) {
                return None;
            }
            Some(GlobalHeader {
                py_name: naming::field_name(header_param_stem(wire_name)),
                wire_name: wire_name.clone(),
                required: true,
            })
        })
        .collect()
}

/// Whether a header is managed by the HTTP transport itself and so is never surfaced
/// as an SDK parameter — Fern excludes `User-Agent` from global-header promotion even
/// when it rides every operation (the generated client sets its own).
fn is_transport_managed_header(wire_name: &str) -> bool {
    wire_name.eq_ignore_ascii_case("user-agent")
}

/// The SDK's authentication model, derived from `components.securitySchemes` and
/// how operations reference them. Only the schemes crozier reproduces byte-for-byte
/// are distinguished; anything else (oauth2 or no scheme) falls back to an optional
/// bearer `token`, matching Fern's default client wrapper.
#[derive(Debug, Clone)]
pub enum Auth {
    /// A `type: apiKey` header credential: a required-or-optional `api_key: str`
    /// added to the named header.
    ApiKey {
        /// The header the key is sent in (the scheme's `name`).
        header: String,
        /// Whether every operation is authenticated (the credential is required).
        required: bool,
    },
    /// A bearer `token` (str or callable), sent as `Authorization: Bearer`.
    Bearer {
        /// Whether every operation is authenticated (the token is required).
        required: bool,
    },
    /// HTTP `basic` credentials: a required `username`/`password` pair (each a
    /// `str` or callable), sent via `httpx.BasicAuth` as `Authorization: Basic`.
    Basic {
        /// Whether every operation requires Basic auth.
        required: bool,
    },
    /// No authentication: the document declares no security schemes, so the client
    /// wrapper carries no credential and adds no `Authorization` header — matching
    /// Fern's wrapper for an unauthenticated API.
    None,
}

/// Derive the [`Auth`] model: the first declared scheme selects the credential
/// shape, and the credential is required when every operation is authenticated.
fn auth_model(doc: &OpenApi) -> Auth {
    use crate::openapi::{HttpAuthScheme, SecuritySchemeType};
    // A document with no declared security scheme is unauthenticated: Fern emits a
    // credential-free wrapper (no token, no `Authorization`), not a default bearer.
    if doc.components.security_schemes.is_empty() {
        return Auth::None;
    }
    match doc.components.security_schemes.values().next() {
        // `name` is validated non-empty at the boundary (see `openapi::load`).
        Some(s)
            if s.ty == SecuritySchemeType::ApiKey
                && s.location == Some(ParameterLocation::Header) =>
        {
            Auth::ApiKey {
                header: s.name.clone().unwrap_or_default(),
                required: all_operations_authenticated(doc) || doc.security.is_none(),
            }
        }
        Some(s) if s.ty == SecuritySchemeType::Http && s.scheme == Some(HttpAuthScheme::Bearer) => {
            let required = all_operations_authenticated(doc);
            Auth::Bearer { required }
        }
        Some(s) if s.ty == SecuritySchemeType::Http && s.scheme == Some(HttpAuthScheme::Basic) => {
            Auth::Basic {
                required: all_operations_authenticated(doc),
            }
        }
        // oauth2/unknown/no scheme → Fern's default optional bearer token.
        _ => Auth::Bearer { required: false },
    }
}

fn oauth_scope_enum(doc: &OpenApi) -> Option<EnumType> {
    use crate::openapi::SecuritySchemeType;
    let scopes = doc
        .components
        .security_schemes
        .values()
        .find(|scheme| scheme.ty == SecuritySchemeType::OAuth2)
        .and_then(|scheme| scheme.flows.as_ref())
        .and_then(|flows| {
            flows
                .authorization_code
                .as_ref()
                .or(flows.client_credentials.as_ref())
                .or(flows.implicit.as_ref())
                .or(flows.password.as_ref())
        })
        .map(|flow| &flow.scopes)?;
    if scopes.is_empty() {
        return None;
    }

    let mut seen_members: std::collections::HashMap<String, usize> =
        std::collections::HashMap::new();
    let mut seen_params: std::collections::HashMap<String, usize> =
        std::collections::HashMap::new();
    let members = scopes
        .iter()
        .map(|(value, doc)| EnumMember {
            name: dedupe(naming::enum_member_name(value), &mut seen_members),
            visit_param: dedupe(naming::enum_visit_param(value), &mut seen_params),
            value: value.clone(),
            docstring: clean_doc(Some(doc)),
        })
        .collect();
    Some(EnumType {
        name: "OauthScope".to_string(),
        module: "oauth_scope".to_string(),
        members,
        docstring: None,
    })
}

/// Collect every generated-type name a [`TypeRef`] references, descending through
/// optionals, collections, and unions.
fn collect_named(t: &TypeRef, set: &mut std::collections::HashSet<String>) {
    match t {
        TypeRef::Named(n) => {
            set.insert(n.clone());
        }
        TypeRef::Optional(i) | TypeRef::List(i) | TypeRef::Set(i) => collect_named(i, set),
        TypeRef::Dict(k, v) => {
            collect_named(k, set);
            collect_named(v, set);
        }
        TypeRef::Union(vs) => vs.iter().for_each(|v| collect_named(v, set)),
        TypeRef::Primitive(_) | TypeRef::Literal(_) => {}
    }
}

/// Class names referenced by anything other than an inlined request body: type
/// fields/bases/alias targets/union members, and endpoint responses, parameters,
/// error bodies, single (non-inlined) bodies, and inlined-body field types.
fn referenced_type_names(
    types: &[TypeDecl],
    endpoints: &[Endpoint],
) -> std::collections::HashSet<String> {
    let mut set = std::collections::HashSet::new();
    for decl in types {
        match decl {
            TypeDecl::Object(o) => {
                o.bases.iter().for_each(|b| {
                    set.insert(b.clone());
                });
                o.fields
                    .iter()
                    .for_each(|f| collect_named(&f.type_ref, &mut set));
            }
            TypeDecl::Alias(a) => collect_named(&a.target, &mut set),
            // An enum references no other generated types (its members are strings).
            TypeDecl::Enum(_) => {}
            TypeDecl::DiscriminatedUnion(u) => u
                .members
                .iter()
                .flat_map(|m| &m.fields)
                .for_each(|f| collect_named(&f.type_ref, &mut set)),
        }
    }
    for ep in endpoints {
        if let Some(r) = &ep.response {
            collect_named(r, &mut set);
        }
        ep.path_params
            .iter()
            .for_each(|p| collect_named(&p.type_ref, &mut set));
        ep.query_params
            .iter()
            .for_each(|p| collect_named(&p.type_ref, &mut set));
        ep.header_params
            .iter()
            .for_each(|p| collect_named(&p.type_ref, &mut set));
        ep.errors
            .iter()
            .for_each(|e| collect_named(&e.body_type, &mut set));
        match &ep.request_body {
            Some(RequestBody::Single(s)) => collect_named(&s.type_ref, &mut set),
            Some(RequestBody::Inline(fields)) => {
                fields
                    .iter()
                    .for_each(|f| collect_named(&f.type_ref, &mut set));
            }
            Some(RequestBody::Form(form)) => {
                form.fields
                    .iter()
                    .for_each(|f| collect_named(&f.type_ref, &mut set));
            }
            Some(RequestBody::Bytes { .. }) | None => {}
        }
    }
    set
}

/// Class names of schemas used as an inlined (plain-object `$ref`) request body by
/// **exactly one** operation — the candidates Fern omits from the type layer.
/// Mirrors the `$ref`-object branch of [`resolve_request_body`]. A schema shared as
/// the body of two or more operations (bunq's create+update pairs share
/// `PermittedIp`, `CardGeneratedCvc2`, …) is kept as a standalone type even though it
/// is still inlined into each method, so only single-use bodies are returned.
fn inline_body_source_names(doc: &OpenApi) -> std::collections::HashSet<String> {
    let mut counts: std::collections::HashMap<String, usize> = std::collections::HashMap::new();
    for item in doc.paths.values() {
        for (_, op) in item.operations() {
            let Some(rb) = &op.request_body else { continue };
            let Some(schema) = rb
                .content
                .get("application/json")
                .and_then(|mt| mt.schema.as_ref())
            else {
                continue;
            };
            let Some(reference) = &schema.reference else {
                continue;
            };
            let Some(target) = resolve_ref(doc, reference) else {
                continue;
            };
            let is_enum = string_enum_values(target).is_some() || is_int_enum(target);
            let is_union = target.one_of.is_some() || target.any_of.is_some();
            if !is_enum
                && !is_union
                && !is_map(target)
                && (!target.properties.is_empty() || target.all_of.is_some())
            {
                *counts.entry(ref_to_class(reference)).or_default() += 1;
            }
        }
    }
    counts
        .into_iter()
        .filter_map(|(name, uses)| (uses == 1).then_some(name))
        .collect()
}

/// Whether every operation carries a non-empty security requirement (its own, or
/// the document default). An SDK with any unauthenticated operation makes the
/// credential optional. Returns `false` for a spec with no operations.
fn all_operations_authenticated(doc: &OpenApi) -> bool {
    let mut any = false;
    for item in doc.paths.values() {
        for (_, op) in item.operations() {
            any = true;
            let effective = op.security.as_ref().or(doc.security.as_ref());
            let authed = effective.is_some_and(|reqs| reqs.iter().any(|r| !r.is_empty()));
            if !authed {
                return false;
            }
        }
    }
    any
}

/// One API operation, resolved into the shape the raw client needs.
#[derive(Debug)]
pub struct Endpoint {
    /// The client module (directory) this operation belongs to.
    pub module: String,
    /// The generated Python method name.
    pub method_name: String,
    /// The uppercase HTTP method (`GET`, `POST`, ...).
    pub http_method: &'static str,
    /// The URL path from the document (e.g. `/urls/{id}`), leading slash and all.
    pub path: String,
    /// Path parameters, in declaration order.
    pub path_params: Vec<PathParam>,
    /// Query parameters, in declaration order.
    pub query_params: Vec<QueryParam>,
    /// Header parameters, in declaration order.
    pub header_params: Vec<HeaderParam>,
    /// The JSON request body, when the operation has one crozier can emit.
    pub request_body: Option<RequestBody>,
    /// Whether the spec's `requestBody` declared a `description` (even an empty one).
    /// Fern omits the explicit `content-type` header for a documented JSON body with
    /// no path/header params, and keeps it for an undocumented one — bunq documents
    /// every body (`description: ""`), the synthetic seeds document none.
    pub body_documented: bool,
    /// Whether the body came through `components.requestBodies`, which Fern treats
    /// like a reusable declaration for content-type emission.
    pub body_component_ref: bool,
    /// Whether the selected request media schema was declared by component `$ref`.
    pub body_schema_ref: bool,
    /// Whether the referenced request schema declares an example payload.
    pub body_schema_has_example: bool,
    /// Whether the referenced request schema has a substantive description.
    pub body_schema_documented: bool,
    /// Whether an inline request object was inferred from properties with no type.
    pub body_schema_implicit_object: bool,
    /// Whether a referenced request schema is composed with `allOf`.
    pub body_all_of: bool,
    /// Whether the JSON request body and success response point at the same schema.
    pub body_response_same_ref: bool,
    /// The success response body type, or `None` when the endpoint returns no
    /// content.
    pub response: Option<TypeRef>,
    /// The success response's description, shown in the docstring's `Returns`
    /// section (Fern emits an indented line under the return type).
    pub response_doc: Option<String>,
    /// Declared error (non-2xx) responses, each raising a generated exception.
    pub errors: Vec<ErrorResponse>,
    /// A short description shown as the docstring's summary line.
    pub docstring: Option<String>,
    /// Whether the source description ended with a blank paragraph, which Fern
    /// preserves in reference documentation after trimming method docstrings.
    pub reference_description_trailing_blank: bool,
    /// Whether the success response is a Server-Sent-Events stream
    /// (`text/event-stream`). A streaming operation is emitted as a
    /// context-managed iterator of chunks rather than a buffered response.
    pub streaming: bool,
    /// Whether the success response is a binary download (`format: binary`).
    /// Fern emits these as context-managed byte streams instead of buffering.
    pub binary_response: bool,
    /// Whether crozier can emit this operation's raw client today. A module is
    /// only emitted when every one of its operations is emittable.
    pub emittable: bool,
}

/// A resolved path parameter.
#[derive(Debug)]
pub struct PathParam {
    /// The wire name (matches the `{placeholder}` in the path).
    pub wire_name: String,
    /// The Python parameter identifier.
    pub py_name: String,
    /// The parameter's type.
    pub type_ref: TypeRef,
    /// Optional description, shown under the parameter in the docstring.
    pub docstring: Option<String>,
    /// Example literal resolved from the parameter or its component schema.
    pub example: Option<String>,
}

/// A resolved query parameter, rendered as a keyword-only method argument and a
/// `params={...}` entry.
#[derive(Debug)]
pub struct QueryParam {
    /// The wire name (the `params` dict key).
    pub wire_name: String,
    /// The Python parameter identifier.
    pub py_name: String,
    /// The parameter's base type (optionality is carried by `required`).
    pub type_ref: TypeRef,
    /// Whether the parameter is required; optional params get `Optional[..] = None`.
    pub required: bool,
    /// Whether the value serializes through `convert_and_respect_annotation_metadata`
    /// in the `params` dict — true for an object/union type carrying field aliases,
    /// as Fern wraps an object-typed query parameter.
    pub convert: bool,
    /// The parameter's `example` as a Python literal; when set, the parameter is
    /// shown in a worked snippet even if optional (`example_literal`).
    pub example: Option<String>,
    /// Whether the OpenAPI schema resolves to a scalar whose example can be used
    /// directly, including named scalar aliases.
    pub example_is_scalar: bool,
    /// Optional description, shown under the parameter in the docstring.
    pub docstring: Option<String>,
}

/// A resolved header parameter, rendered as a keyword-only method argument and a
/// `headers={...}` entry (`str(x) if x is not None else None`).
#[derive(Debug)]
pub struct HeaderParam {
    /// The wire name (the `headers` dict key, e.g. `X-TEST-ENDPOINT-HEADER`).
    pub wire_name: String,
    /// The Python parameter identifier.
    pub py_name: String,
    /// The parameter's base type (optionality is carried by `required`).
    pub type_ref: TypeRef,
    /// Whether the parameter is required; optional params get `Optional[..] = None`.
    pub required: bool,
    /// Optional description, shown under the parameter in the docstring.
    pub docstring: Option<String>,
    /// Example literal resolved from the parameter or its component schema.
    pub example: Option<String>,
}

/// A resolved JSON request body. Fern renders a body one of two ways: as a single
/// `request` keyword argument (a scalar, a named enum/union/map), or — for a
/// plain-object `$ref` — *inlined*, each field hoisted into its own keyword-only
/// argument.
#[derive(Debug)]
pub enum RequestBody {
    /// A single `request` argument serialized into the `json=` entry.
    Single(SingleBody),
    /// A plain-object body inlined field-by-field: each field becomes a
    /// keyword-only `= OMIT` argument and a `json={...}` entry mapping its wire
    /// name to the argument. Always carries the content-type header.
    Inline(Vec<BodyField>),
    /// A raw `application/octet-stream` body: a `request` argument typed
    /// `Union[bytes, Iterator[bytes], AsyncIterator[bytes]]`, sent as `content=`
    /// with a `content-type: application/octet-stream` header.
    Bytes { content_type: String },
    /// A form body (`multipart/form-data` or `application/x-www-form-urlencoded`):
    /// each property is a keyword-only argument; non-file fields serialize into
    /// `data={...}` and file fields into `files={...}`. Multipart bodies set
    /// `force_multipart=True`; urlencoded bodies carry the form content-type header.
    Form(FormBody),
}

/// A resolved form request body.
#[derive(Debug)]
pub struct FormBody {
    /// The form fields, in document order.
    pub fields: Vec<BodyField>,
    /// True for `multipart/form-data` (`force_multipart=True`), false for
    /// `application/x-www-form-urlencoded` (a form content-type header).
    pub multipart: bool,
}

impl RequestBody {
    /// Whether this body came from a wildcard media declaration.
    pub fn is_wildcard_media(&self) -> bool {
        matches!(self, Self::Single(body) if body.content_type_override.as_deref() == Some("*/*"))
    }

    /// Whether the request emits the `content-type: application/json` header.
    /// Inlined object bodies always do; a single body carries its own flag; a raw
    /// bytes body carries its own (octet-stream) header instead, handled at emit.
    /// Form bodies carry their own (urlencoded) header or `force_multipart`.
    #[must_use]
    pub fn content_type_header(&self) -> bool {
        match self {
            RequestBody::Single(s) => s.content_type,
            RequestBody::Inline(_) => true,
            RequestBody::Bytes { .. } | RequestBody::Form(_) => false,
        }
    }

    /// Whether the body is *always sent whole* — an inline body every one of whose
    /// fields is required, so no field is `OMIT`ted. Fern keeps the explicit
    /// `content-type` header for such a body even when it is documented; a documented
    /// body with any optional field (a possible empty payload) drops it.
    pub fn all_fields_required(&self) -> bool {
        matches!(self, RequestBody::Inline(fields) if !fields.is_empty() && fields.iter().all(|f| !f.optional))
    }
}

/// A request body passed as one `request` argument.
#[derive(Debug)]
pub struct SingleBody {
    /// The `request` argument's type (collections render in request context, i.e.
    /// `typing.Sequence` rather than `typing.List`).
    pub type_ref: TypeRef,
    /// Whether the body is required; optional bodies get `Optional[..] = None`.
    pub required: bool,
    /// `json=convert_and_respect_annotation_metadata(...)` when true (a union or a
    /// container of objects, whose members carry field aliases to respect), else
    /// a plain `json=request`.
    pub convert: bool,
    /// Whether Fern emits the `content-type: application/json` header. Present for
    /// named (`$ref`) enum/union/map bodies and the `uuid`/`byte` scalar formats;
    /// absent for a plain scalar or an inline container.
    pub content_type: bool,
    /// Exact content type to emit instead of `application/json` for vendor JSON
    /// media types.
    pub content_type_override: Option<String>,
}

/// A declared error (non-2xx) response, rendered as a `raise` branch keyed on the
/// status code.
#[derive(Debug, Clone)]
pub struct ErrorResponse {
    /// The HTTP status code that triggers this error.
    pub status_code: u16,
    /// The generated exception class name (e.g. `BadRequestError`).
    pub class_name: String,
    /// The error body type parsed into the exception (`$ref` to a named type).
    pub body_type: TypeRef,
}

/// A generated exception class under `errors/`, one per distinct declared error.
#[derive(Debug, Clone)]
pub struct ErrorClass {
    /// The HTTP status code passed to `ApiError`.
    pub status_code: u16,
    /// The exception class name (e.g. `BadRequestError`).
    pub class_name: String,
    /// The error body type accepted by the constructor.
    pub body_type: TypeRef,
}

/// One field of an inlined (hoisted) object request body, rendered as a
/// keyword-only argument and a `json={...}` entry.
#[derive(Debug)]
pub struct BodyField {
    /// The wire (JSON) property name (the `json` dict key).
    pub wire_name: String,
    /// The Python argument identifier (snake_case, reserved-munged).
    pub py_name: String,
    /// The field's base type (optionality is carried by `optional`); collections
    /// render in request context (`typing.Sequence`).
    pub type_ref: TypeRef,
    /// Whether the field is optional; optional fields get `Optional[..] = OMIT`.
    pub optional: bool,
    /// Whether the schema itself accepts null, distinct from being omittable.
    pub nullable: bool,
    /// Whether the property is in the schema's `required` set (see
    /// [`Field::spec_required`]); drives whether a synthesized example includes it.
    pub spec_required: bool,
    /// Optional description, shown under the argument in the docstring.
    pub docstring: Option<String>,
    /// Whether the field serializes through `convert_and_respect_annotation_metadata`
    /// (its type references an object or union carrying field aliases).
    pub convert: bool,
    /// Whether this is a file upload field (`format: binary` in a form body),
    /// which renders as `core.File` and serializes into `files={...}`.
    pub is_file: bool,
    /// Prefix Fern applies when this field's argument name collides with another
    /// method parameter (e.g. query `tags` plus DAG body `tags` -> `dag_tags`).
    pub collision_prefix: Option<String>,
    /// The field's `example` as a Python literal, shown in a worked snippet instead
    /// of a synthesized placeholder (`example_literal`).
    pub example: Option<String>,
    /// Whether a request media example explicitly selected this field.
    pub media_example: bool,
}

/// A type hoisted out of an operation's inline request/response body. Unlike a
/// top-level [`TypeDecl`] (which lives in the package-root `types/`), a tag type
/// lives in its owning tag's own `types/` package — Fern's
/// `inlined/types/inlined_search_response.py` layout.
#[derive(Debug)]
pub struct TagTypeDecl {
    /// The owning tag's client-module (directory) name, e.g. `inlined`.
    pub module: String,
    /// The generated type.
    pub decl: TypeDecl,
}

/// A generated top-level type.
#[derive(Debug)]
pub enum TypeDecl {
    /// A pydantic model.
    Object(ObjectType),
    /// A type alias (`Name = <expr>`), e.g. a union, a scalar alias, or an
    /// integer enum (`Name = int`).
    Alias(AliasType),
    /// A string enum rendered as a real `enum.Enum` class.
    Enum(EnumType),
    /// A discriminated union: a set of per-variant wrapper models plus a
    /// `Name = typing.Union[..]` alias, all in one module (Fern's `Shape_Circle`
    /// / `Shape_Square` pattern).
    DiscriminatedUnion(DiscriminatedUnion),
}

impl TypeDecl {
    /// The primary class/alias name (the union alias name for a discriminated
    /// union).
    #[must_use]
    pub fn name(&self) -> &str {
        match self {
            TypeDecl::Object(o) => &o.name,
            TypeDecl::Alias(a) => &a.name,
            TypeDecl::Enum(e) => &e.name,
            TypeDecl::DiscriminatedUnion(d) => &d.name,
        }
    }

    /// The module (file stem) the type lives in.
    #[must_use]
    pub fn module(&self) -> &str {
        match self {
            TypeDecl::Object(o) => &o.module,
            TypeDecl::Alias(a) => &a.module,
            TypeDecl::Enum(e) => &e.module,
            TypeDecl::DiscriminatedUnion(d) => &d.module,
        }
    }

    /// Every public name this declaration exports, in declaration order. All but
    /// a discriminated union export exactly their [`TypeDecl::name`]; a
    /// discriminated union also exports each variant wrapper class.
    #[must_use]
    pub fn exported_names(&self) -> Vec<&str> {
        match self {
            TypeDecl::DiscriminatedUnion(d) => std::iter::once(d.name.as_str())
                .chain(d.members.iter().map(|m| m.class_name.as_str()))
                .collect(),
            other => vec![other.name()],
        }
    }
}

/// A discriminated `oneOf`/`anyOf`: Fern emits a wrapper model per variant
/// (`{Union}_{Variant}`) carrying the discriminant as a `Literal` field, then a
/// `{Union} = typing.Union[..]` alias over the wrappers.
#[derive(Debug)]
pub struct DiscriminatedUnion {
    /// The union alias name (e.g. `Shape`).
    pub name: String,
    /// Module (file stem).
    pub module: String,
    /// The property whose value selects the variant (e.g. `type`).
    pub discriminant_property: String,
    /// The variant wrapper models, in mapping order.
    pub members: Vec<UnionMember>,
    /// The class names of the schemas the discriminator maps to (e.g. `AndNode`,
    /// `LeafNode`). Kept so the recursion analysis can see that the union can *be*
    /// one of those schemas — the edge that reveals a recursive variant (issue #84).
    pub variant_targets: Vec<String>,
    /// Optional docstring.
    pub docstring: Option<String>,
}

/// One variant wrapper of a [`DiscriminatedUnion`].
#[derive(Debug)]
pub struct UnionMember {
    /// The wrapper class name (e.g. `Shape_Circle`).
    pub class_name: String,
    /// The discriminant literal value (e.g. `circle`).
    pub discriminant: String,
    /// The variant's fields, with the discriminant property removed.
    pub fields: Vec<Field>,
}

/// A pydantic model type.
#[derive(Debug)]
pub struct ObjectType {
    /// Class name.
    pub name: String,
    /// Module (file stem).
    pub module: String,
    /// Base classes. Empty means `UniversalBaseModel`; non-empty comes from an
    /// `allOf` whose `$ref` members become superclasses.
    pub bases: Vec<String>,
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
    /// Whether the schema itself accepts null, distinct from being non-required.
    pub nullable: bool,
    /// Whether the property is in the schema's `required` set. Distinct from
    /// `optional` (an unknown/nullable required field is still `Optional[..]` in
    /// Python); drives whether a synthesized example includes the field.
    pub spec_required: bool,
    /// Optional field docstring (from the property `description`).
    pub docstring: Option<String>,
    /// The property's `example` as a Python literal, shown in a worked snippet
    /// instead of a synthesized placeholder (`example_literal`).
    pub example: Option<String>,
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

/// A named string enum rendered as a real `enum.Enum` class (Fern's
/// `enum_type: python_enums` mode, which crozier targets — see docs/matching.md).
/// Each member's Python name is the SCREAMING_SNAKE form of its wire value and its
/// `visit` callback parameter the snake_case form; the wire value is preserved.
#[derive(Debug)]
pub struct EnumType {
    /// Enum class name.
    pub name: String,
    /// Module (file stem).
    pub module: String,
    /// The members, in declaration order.
    pub members: Vec<EnumMember>,
    /// Optional docstring.
    pub docstring: Option<String>,
}

/// One member of an [`EnumType`].
#[derive(Debug)]
pub struct EnumMember {
    /// The Python member identifier (`SCREAMING_SNAKE` of the value).
    pub name: String,
    /// The wire value (the enum's string).
    pub value: String,
    /// The `visit` callback parameter name (`snake_case` of the value).
    pub visit_param: String,
    /// Optional member docstring.
    pub docstring: Option<String>,
}

/// Return `ident` unchanged the first time it is seen, or a `_{n}`-suffixed
/// variant on a repeat, so a set of enum members/parameters stays unique (and
/// thus valid Python) even when two wire values sanitize to the same identifier.
fn dedupe(ident: String, seen: &mut std::collections::HashMap<String, usize>) -> String {
    let count = seen.entry(ident.clone()).or_insert(0);
    *count += 1;
    if *count == 1 {
        ident
    } else {
        format!("{ident}_{}", *count - 1)
    }
}

/// Build an [`EnumType`] from a schema's string-enum values, deriving each
/// member's Python name and `visit` parameter from its wire value.
fn build_enum(name: &str, values: Vec<String>, docstring: Option<String>) -> EnumType {
    // Fern derives the member name and `visit` parameter from each wire value,
    // sanitizing both into legal Python identifiers (issue #50): `global` →
    // `GLOBAL`/`global_`, `0: Active` → `ZERO_ACTIVE`/`zero_active`. Two values
    // that collapse to the same identifier would emit duplicate members/params
    // (invalid Python), so a suffix disambiguates any collision.
    let mut seen_members: std::collections::HashMap<String, usize> =
        std::collections::HashMap::new();
    let mut seen_params: std::collections::HashMap<String, usize> =
        std::collections::HashMap::new();
    let members = values
        .into_iter()
        .map(|value| EnumMember {
            name: dedupe(naming::enum_member_name(&value), &mut seen_members),
            visit_param: dedupe(naming::enum_visit_param(&value), &mut seen_params),
            value,
            docstring: None,
        })
        .collect();
    EnumType {
        name: name.to_string(),
        module: naming::module_name(name),
        members,
        docstring,
    }
}

/// A resolved type reference.
#[derive(Debug, Clone, PartialEq, Eq)]
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
    /// `int` from `format: int64`. Renders as `int` like [`Prim::Int`]; kept
    /// distinct only so a synthesized example matches Fern's larger placeholder.
    Long,
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
    let mut builder = Builder {
        types: Vec::new(),
        schemas: &doc.components.schemas,
        strip_discriminant: discriminant_strips(&doc.components.schemas),
    };
    for (key, schema) in &doc.components.schemas {
        builder.add_named(&naming::class_name(key), schema);
    }
    if let Some(oauth_scope) = oauth_scope_enum(doc) {
        builder.types.push(TypeDecl::Enum(oauth_scope));
    }
    // Endpoint resolution consults the built types to hoist a plain-object `$ref`
    // body's fields and to decide which of them serialize through the convert
    // wrapper, so it runs after the type layer is built. It also hoists inline
    // request/response bodies into their tags' own `types/` packages.
    let global = global_headers(doc);
    let (mut endpoints, mut tag_types) = endpoints(doc, &builder.types, &global);
    let root_tag_types: Vec<TypeDecl> = tag_types
        .extract_if(.., |tag_type| tag_type.module.is_empty())
        .map(|tag_type| tag_type.decl)
        .collect();
    builder.types.extend(root_tag_types);
    normalize_error_body_types(&mut endpoints);
    let errors = error_classes(&endpoints);

    // Fern does not emit a standalone type for a schema used *only* as an inlined
    // (plain-object `$ref`) request body — its fields live on the request method
    // instead. Drop such a type unless it is referenced elsewhere (a response, a
    // field, a parameter, a non-inlined body, ...).
    let referenced = referenced_type_names(&builder.types, &endpoints);
    let inline_sources = inline_body_source_names(doc);
    let dropped_sources: std::collections::HashSet<String> = inline_sources
        .iter()
        .filter(|name| !referenced.contains(*name))
        .cloned()
        .collect();
    let moved_enums =
        move_inline_body_enums_to_tags(doc, &builder.types, &dropped_sources, &mut tag_types);
    builder
        .types
        .retain(|d| !dropped_sources.contains(d.name()) && !moved_enums.contains(d.name()));

    // Fern also emits a standalone package-root type for each error response whose
    // body is an inline object, named `{ErrorClassName}Body` (bunq's 400
    // `GenericError` → `BadRequestErrorBody`). The error *class* still types its body
    // as `Any`; this model is referenced only through the `types/` aggregators.
    hoist_error_body_types(doc, &mut builder);

    // The root client class name is Fern's `client_class_name` when given
    // (issue #61), else derived from the package name as `{PascalCase}Api`.
    let client_name = config.client_class_name.clone().unwrap_or_else(|| {
        format!(
            "{}Api",
            naming::to_pascal_case(config.package_name.as_str())
        )
    });
    let environment = environment_model(doc, &client_name);

    Ir {
        openapi_31: doc.openapi.starts_with("3.1"),
        package_name: config.package_name.as_str().to_string(),
        project_name: config.project_name.clone(),
        client_name,
        types: builder.types,
        tag_types,
        endpoint_modules: endpoint_modules(doc),
        endpoint_module_titles: endpoint_module_titles(doc),
        endpoints,
        errors,
        auth: auth_model(doc),
        global_headers: global,
        environment,
        extra_fields: config.extra_fields,
    }
}

fn move_inline_body_enums_to_tags(
    doc: &OpenApi,
    types: &[TypeDecl],
    dropped_sources: &std::collections::HashSet<String>,
    tag_types: &mut Vec<TagTypeDecl>,
) -> std::collections::HashSet<String> {
    let mut moved = std::collections::HashSet::new();
    let mut enum_owner_counts: std::collections::HashMap<&str, usize> =
        std::collections::HashMap::new();
    let mut retained_enum_refs = std::collections::HashSet::new();
    for decl in types {
        if dropped_sources.contains(decl.name()) {
            continue;
        }
        let TypeDecl::Object(object) = decl else {
            continue;
        };
        for field in &object.fields {
            let TypeRef::Named(name) = &field.type_ref else {
                continue;
            };
            if types
                .iter()
                .any(|decl| matches!(decl, TypeDecl::Enum(e) if e.name == *name))
            {
                retained_enum_refs.insert(name.as_str());
            }
        }
    }
    for source in dropped_sources {
        let Some(object) = types.iter().find_map(|decl| match decl {
            TypeDecl::Object(object) if object.name == *source => Some(object),
            _ => None,
        }) else {
            continue;
        };
        for field in &object.fields {
            let TypeRef::Named(name) = &field.type_ref else {
                continue;
            };
            if types
                .iter()
                .any(|decl| matches!(decl, TypeDecl::Enum(e) if e.name == *name))
            {
                *enum_owner_counts.entry(name).or_default() += 1;
            }
        }
    }
    for (path, item) in &doc.paths {
        for (_, op) in item.operations() {
            let Some(schema) = op
                .request_body
                .as_ref()
                .and_then(|body| body.content.get("application/json"))
                .and_then(|media| media.schema.as_ref())
            else {
                continue;
            };
            let Some(source) = schema.reference.as_deref().map(ref_to_class) else {
                continue;
            };
            if !dropped_sources.contains(&source) {
                continue;
            }
            let Some(object) = types.iter().find_map(|decl| match decl {
                TypeDecl::Object(object) if object.name == source => Some(object),
                _ => None,
            }) else {
                continue;
            };
            for field in &object.fields {
                let TypeRef::Named(name) = &field.type_ref else {
                    continue;
                };
                if enum_owner_counts.get(name.as_str()) != Some(&1) {
                    continue;
                }
                if retained_enum_refs.contains(name.as_str()) {
                    continue;
                }
                let Some(source_enum) = types.iter().find_map(|decl| match decl {
                    TypeDecl::Enum(enum_type) if enum_type.name == *name => Some(enum_type),
                    _ => None,
                }) else {
                    continue;
                };
                tag_types.push(TagTypeDecl {
                    module: endpoint_module(op, path),
                    decl: TypeDecl::Enum(EnumType {
                        name: source_enum.name.clone(),
                        module: source_enum.module.clone(),
                        members: source_enum
                            .members
                            .iter()
                            .map(|member| EnumMember {
                                name: member.name.clone(),
                                value: member.value.clone(),
                                visit_param: member.visit_param.clone(),
                                docstring: member.docstring.clone(),
                            })
                            .collect(),
                        docstring: source_enum.docstring.clone(),
                    }),
                });
                moved.insert(name.clone());
            }
        }
    }
    moved
}

/// Collect the distinct exception classes an SDK needs, one per error class name
/// used across its (emittable) endpoints, sorted by class name so the `errors/`
/// package `__init__` aggregator is deterministic.
fn error_classes(endpoints: &[Endpoint]) -> Vec<ErrorClass> {
    let mut classes: Vec<ErrorClass> = Vec::new();
    for ep in endpoints.iter().filter(|e| e.emittable) {
        for err in &ep.errors {
            if !classes.iter().any(|c| c.class_name == err.class_name) {
                classes.push(ErrorClass {
                    status_code: err.status_code,
                    class_name: err.class_name.clone(),
                    body_type: err.body_type.clone(),
                });
            }
        }
    }
    classes.sort_by(|a, b| a.class_name.cmp(&b.class_name));
    classes
}

fn normalize_error_body_types(endpoints: &mut [Endpoint]) {
    let mut downgrade = std::collections::HashSet::new();
    let mut first_by_class: std::collections::HashMap<String, TypeRef> =
        std::collections::HashMap::new();
    for ep in endpoints.iter() {
        for err in &ep.errors {
            if matches!(
                err.body_type,
                TypeRef::Optional(ref inner) if matches!(&**inner, TypeRef::Primitive(Prim::Any))
            ) {
                downgrade.insert(err.class_name.clone());
            }
            match first_by_class.get(&err.class_name) {
                Some(first) if first != &err.body_type => {
                    downgrade.insert(err.class_name.clone());
                }
                None => {
                    first_by_class.insert(err.class_name.clone(), err.body_type.clone());
                }
                _ => {}
            }
        }
    }
    for ep in endpoints {
        for err in &mut ep.errors {
            if downgrade.contains(&err.class_name) {
                err.body_type = TypeRef::Optional(Box::new(TypeRef::Primitive(Prim::Any)));
            }
        }
    }
}

/// Resolve every operation into an [`Endpoint`], in document-traversal order
/// (paths in document order, methods in a stable per-path order). Inline
/// request/response bodies are hoisted into per-tag types, collected alongside.
fn endpoints(
    doc: &OpenApi,
    types: &[TypeDecl],
    global: &[GlobalHeader],
) -> (Vec<Endpoint>, Vec<TagTypeDecl>) {
    let global_names: std::collections::HashSet<&str> =
        global.iter().map(|h| h.wire_name.as_str()).collect();
    let mut out = Vec::new();
    let mut tag_types = Vec::new();
    for (path, item) in &doc.paths {
        for (http_method, op) in item.operations() {
            out.push(build_endpoint(
                doc,
                types,
                path,
                http_method,
                op,
                &mut tag_types,
                &global_names,
            ));
        }
    }
    (out, tag_types)
}

/// Resolve one operation, deciding whether it is within the subset crozier can
/// emit today (no request body, only path parameters, a single JSON success
/// response whose type is a named model or a scalar).
fn build_endpoint(
    doc: &OpenApi,
    types: &[TypeDecl],
    path: &str,
    http_method: &'static str,
    op: &Operation,
    tag_types: &mut Vec<TagTypeDecl>,
    global_headers: &std::collections::HashSet<&str>,
) -> Endpoint {
    let module = endpoint_module(op, path);
    let method = endpoint_method_name(op, http_method, path);
    // Inline (non-`$ref`) request/response objects hoist into this tag's own
    // `types/` package; the hoister accumulates them, keyed to the tag below.
    let mut hoister = InlineHoister {
        root_types: types,
        out: Vec::new(),
    };
    // The operation's PascalCase context (from the operationId, never the tag) —
    // hoisted request/response types derive from it. `{ctx}Request` scopes the
    // types Fern synthesizes for the request: nested inline bodies and, below,
    // inline enums on request parameters.
    let pascal_ctx = endpoint_pascal_context(op, http_method, path);
    let request_ctx = format!("{pascal_ctx}Request");
    let mut path_params: Vec<PathParam> = op
        .parameters
        .iter()
        .filter(|p| p.location == Some(ParameterLocation::Path))
        .map(|p| PathParam {
            wire_name: p.name.clone(),
            py_name: naming::field_name(&p.name),
            type_ref: p
                .schema
                .as_ref()
                .map_or(TypeRef::Primitive(Prim::Any), |schema| {
                    hoister.hoist_param_enum(&request_ctx, &p.name, schema)
                }),
            docstring: declared_doc(p.description.as_deref()),
            example: parameter_example(doc, p),
        })
        .collect();
    if !doc.openapi.starts_with("3.1") {
        path_params.sort_by(|a, b| {
            path_param_position(path, &a.wire_name)
                .cmp(&path_param_position(path, &b.wire_name))
                .then_with(|| a.wire_name.cmp(&b.wire_name))
        });
    }

    let query_params: Vec<QueryParam> = op
        .parameters
        .iter()
        .filter(|p| p.location == Some(ParameterLocation::Query))
        .map(|p| {
            // An inline string enum hoists to a named `{ctx}Request{Prop}` alias in
            // the tag's `types/` package (Fern's `ListWidgetsRequestLevel`); a
            // `$ref`/scalar passes through `base_type_ref`.
            let type_ref = p
                .schema
                .as_ref()
                .map_or(TypeRef::Primitive(Prim::Any), |s| {
                    hoister.hoist_param_enum(&request_ctx, &p.name, s)
                });
            let convert = type_needs_convert(&type_ref, types);
            // A parameter-level `example` wins; otherwise the schema's own.
            let example = parameter_example(doc, p);
            let example_is_scalar = p.schema.as_ref().is_some_and(|schema| {
                let schema = schema
                    .reference
                    .as_deref()
                    .and_then(|reference| resolve_ref(doc, reference))
                    .unwrap_or(schema);
                matches!(
                    schema.ty.as_ref().and_then(|ty| ty.primary()),
                    Some("string" | "integer" | "number" | "boolean")
                )
            });
            QueryParam {
                wire_name: p.name.clone(),
                py_name: naming::field_name(&p.name),
                type_ref,
                required: p.required == Some(true),
                convert,
                example,
                example_is_scalar,
                docstring: clean_doc(p.description.as_deref()),
            }
        })
        .collect();

    let mut header_params: Vec<HeaderParam> = op
        .parameters
        .iter()
        // A header promoted to a client-wrapper-level global field is dropped from
        // the method signature entirely (it is set once at client construction), as
        // is a transport-managed header (`User-Agent`) — Fern never surfaces either
        // as a per-call argument.
        .filter(|p| {
            p.location == Some(ParameterLocation::Header)
                && !global_headers.contains(p.name.as_str())
                && !is_transport_managed_header(&p.name)
        })
        .map(|p| HeaderParam {
            wire_name: p.name.clone(),
            py_name: naming::field_name(header_param_stem(&p.name)),
            type_ref: p
                .schema
                .as_ref()
                .map_or(TypeRef::Primitive(Prim::Any), |schema| {
                    hoister.hoist_param_enum(&request_ctx, &p.name, schema)
                }),
            required: p.required == Some(true),
            docstring: clean_doc(p.description.as_deref()),
            example: parameter_example(doc, p),
        })
        .collect();

    // crozier handles path, query, and header parameters, and drops `cookie`
    // parameters (Fern omits them from the method signature entirely). Any other
    // kind (an unknown location, or a `$ref` with no location) puts the operation
    // outside the emittable subset.
    let has_unsupported_params = op.parameters.iter().any(|p| {
        !matches!(
            p.location,
            Some(
                ParameterLocation::Path
                    | ParameterLocation::Query
                    | ParameterLocation::Header
                    | ParameterLocation::Cookie
            )
        )
    });
    // Error (non-2xx) responses each become a `raise` branch. They never suppress
    // method generation (issue #43): a status Fern does not name is skipped and the
    // operation falls through to the generic `ApiError`.
    let errors = resolve_errors(op);
    // The success response: a `$ref`/scalar/container passes straight through; an
    // inline object body is hoisted into a `{Ctx}Response` model, where `Ctx` is
    // the operation's PascalCase context (computed above, from the operationId).
    let response = match success_response_schema(op) {
        Some(schema) if is_inline_struct(schema) => {
            let name = format!("{pascal_ctx}Response");
            hoister.hoist_object(&name, schema);
            Some(TypeRef::Named(name))
        }
        Some(schema) if schema.reference.is_none() => hoister
            .hoist_array_item_enum(&format!("{pascal_ctx}Response"), schema)
            .or_else(|| {
                hoister
                    .hoist_response_array_item_object(&format!("{pascal_ctx}ResponseItem"), schema)
            })
            .or_else(|| success_response(op)),
        _ => success_response(op),
    };

    // A request body is either absent, within the subset crozier can render, or
    // unsupported. Its inline nested objects hoist under the `{Ctx}Request` context.
    let mut request_body = if http_method == "GET" {
        None
    } else {
        op.request_body
            .as_ref()
            .and_then(|rb| resolve_request_body(doc, types, rb, &mut hoister, &request_ctx))
    };
    if matches!(request_body, Some(RequestBody::Bytes { .. })) {
        header_params.clear();
    }
    let body_ok = http_method == "GET"
        || op.request_body.is_none()
        || request_body.is_some()
        || op.request_body.as_ref().is_some_and(request_body_ignored);

    // Register the hoisted inline types under this tag's `types/` package.
    for decl in hoister.out {
        tag_types.push(TagTypeDecl {
            module: module.clone(),
            decl,
        });
    }

    // Resolve Python argument-name collisions across parameter locations and an
    // inlined body. Path params get the historical trailing `_`; body fields that
    // collide with query/header/path params get Fern's body-context prefix.
    if let Some(RequestBody::Inline(fields)) = &request_body {
        let field_names: std::collections::HashSet<&str> =
            fields.iter().map(|f| f.py_name.as_str()).collect();
        for pp in &mut path_params {
            if field_names.contains(pp.py_name.as_str()) {
                pp.py_name.push('_');
            }
        }
    }
    if let Some(RequestBody::Inline(fields)) = &mut request_body {
        let parameter_names: std::collections::HashSet<&str> = path_params
            .iter()
            .map(|p| p.py_name.as_str())
            .chain(query_params.iter().map(|p| p.py_name.as_str()))
            .chain(header_params.iter().map(|p| p.py_name.as_str()))
            .collect();
        for field in fields {
            if parameter_names.contains(field.py_name.as_str()) {
                if let Some(prefix) = &field.collision_prefix {
                    field.py_name = format!("{prefix}_{}", field.py_name);
                }
            } else {
                field.collision_prefix = None;
            }
        }
    }

    // Today's subset: a supported (or absent) body, path/query/header params only,
    // at least one response, and a success response crozier knows how to render (any
    // resolved shape but an un-hoisted inline object). Error responses never gate
    // emittability (issue #43).
    let emittable =
        body_ok && !has_unsupported_params && !op.responses.is_empty() && response_supported(op);

    Endpoint {
        module,
        method_name: method,
        http_method,
        path: path.to_string(),
        path_params,
        query_params,
        header_params,
        request_body,
        body_documented: op
            .request_body
            .as_ref()
            .is_some_and(|rb| rb.description.is_some()),
        body_component_ref: op.request_body.as_ref().is_some_and(|rb| rb.component_ref),
        body_schema_ref: op
            .request_body
            .as_ref()
            .and_then(|body| {
                body.content
                    .values()
                    .find_map(|media| media.schema.as_ref())
            })
            .is_some_and(|schema| schema.reference.is_some()),
        body_schema_has_example: op
            .request_body
            .as_ref()
            .and_then(|body| {
                body.content
                    .values()
                    .find_map(|media| media.schema.as_ref())
            })
            .and_then(|schema| schema.reference.as_deref())
            .and_then(|reference| resolve_ref(doc, reference))
            .is_some_and(|schema| schema_example(schema).is_some()),
        body_schema_documented: op
            .request_body
            .as_ref()
            .and_then(|body| {
                body.content
                    .values()
                    .find_map(|media| media.schema.as_ref())
            })
            .and_then(|schema| schema.reference.as_deref())
            .and_then(|reference| resolve_ref(doc, reference))
            .and_then(|schema| schema.description.as_deref())
            .is_some_and(|description| !description.trim().is_empty()),
        body_schema_implicit_object: op
            .request_body
            .as_ref()
            .and_then(|body| {
                body.content
                    .values()
                    .find_map(|media| media.schema.as_ref())
            })
            .is_some_and(|schema| schema.ty.is_none() && !schema.properties.is_empty()),
        body_all_of: request_body_has_all_of(doc, op),
        body_response_same_ref: body_response_same_ref(doc, op),
        response,
        response_doc: success_response_doc(op),
        errors,
        docstring: operation_doc(op.description.as_deref()),
        reference_description_trailing_blank: op
            .description
            .as_deref()
            .is_some_and(|description| description.ends_with("\n\n")),
        streaming: is_streaming(op),
        binary_response: is_binary_response(doc, op),
        emittable,
    }
}

fn parameter_example(doc: &OpenApi, parameter: &crate::openapi::Parameter) -> Option<String> {
    parameter
        .example
        .as_ref()
        .or_else(|| parameter.schema.as_ref().and_then(schema_example))
        .or_else(|| {
            parameter
                .schema
                .as_ref()
                .and_then(|schema| schema.reference.as_deref())
                .and_then(|reference| resolve_ref(doc, reference))
                .and_then(schema_example)
        })
        .and_then(example_literal)
}

fn schema_example(schema: &Schema) -> Option<&serde_json::Value> {
    schema.example.as_ref().or_else(|| schema.examples.first())
}

fn request_body_has_all_of(doc: &OpenApi, op: &Operation) -> bool {
    op.request_body
        .as_ref()
        .and_then(|body| body.content.get("application/json"))
        .and_then(|media| media.schema.as_ref())
        .and_then(|schema| schema.reference.as_deref())
        .and_then(|reference| resolve_ref(doc, reference))
        .is_some_and(|schema| schema.all_of.is_some())
}

/// Whether the operation's success response is a Server-Sent-Events stream. Fern
/// models a `text/event-stream` 2xx response as an iterator of chunks; crozier
/// keys off the same content type (the `x-fern-streaming` extension is not needed —
/// Fern's OpenAPI importer does not resolve its `chunk-schema-ref`, so the chunk is
/// `typing.Optional[typing.Any]` regardless).
fn is_streaming(op: &Operation) -> bool {
    op.responses
        .iter()
        .any(|(code, resp)| code.starts_with('2') && resp.content.contains_key("text/event-stream"))
}

fn body_response_same_ref(doc: &OpenApi, op: &Operation) -> bool {
    let effective_security = op.security.as_ref().or(doc.security.as_ref());
    if effective_security.is_some_and(|reqs| reqs.iter().any(|r| !r.is_empty())) {
        return false;
    }
    let request_ref = op
        .request_body
        .as_ref()
        .and_then(|rb| rb.content.get("application/json"))
        .and_then(|media| media.schema.as_ref())
        .and_then(|schema| schema.reference.as_deref());
    let response_ref = success_response_schema(op).and_then(|schema| schema.reference.as_deref());
    request_ref.is_some() && request_ref == response_ref
}

fn is_binary_response(doc: &OpenApi, op: &Operation) -> bool {
    op.responses.iter().any(|(code, resp)| {
        code.starts_with('2')
            && resp.content.iter().any(|(_, media)| {
                media.schema.as_ref().is_some_and(|schema| {
                    let schema = schema
                        .reference
                        .as_deref()
                        .and_then(|reference| resolve_ref(doc, reference))
                        .unwrap_or(schema);
                    schema.ty.as_ref().and_then(|t| t.primary()) == Some("string")
                        && schema.format.as_deref() == Some("binary")
                })
            })
    })
}

/// Position of a path parameter's placeholder for OpenAPI 3.0 importer ordering.
fn path_param_position(path: &str, name: &str) -> Option<usize> {
    path.split('/')
        .filter(|segment| segment.starts_with('{') && segment.ends_with('}'))
        .position(|segment| &segment[1..segment.len() - 1] == name)
}

/// The success (2xx) response's description, cleaned for the `Returns` docstring.
fn success_response_doc(op: &Operation) -> Option<String> {
    let (_, response) = op
        .responses
        .iter()
        .find(|(code, _)| code.starts_with('2'))?;
    clean_doc(response.description.as_deref())
}

/// The generated exception class name for an HTTP status code, reproducing Fern's
/// status-code → exception map (every standard 4xx/5xx code). A status Fern does
/// not name (a non-standard code such as `460`) returns `None`: crozier then omits
/// its `raise` branch and lets the operation fall through to the generic
/// `ApiError`, exactly as Fern does — it never suppresses the whole method.
///
/// The table was read off Fern's own generator output (running it across the full
/// status range under Docker, `scripts/generate-fern-fixture.sh`). Its drift gates:
/// the `error-responses` corpus pins the shape byte-for-byte for the common statuses
/// (400/404/422/500/503), and the exhaustive
/// `every_standard_error_status_maps_to_its_fern_exception` test
/// (`tests/generation.rs`) locks every entry's class name, `errors/` module filename,
/// and `status_code`, so an accidental edit here fails loudly. See `docs/matching.md`.
fn error_class_name(status: u16) -> Option<&'static str> {
    Some(match status {
        400 => "BadRequestError",
        401 => "UnauthorizedError",
        402 => "PaymentRequiredError",
        403 => "ForbiddenError",
        404 => "NotFoundError",
        405 => "MethodNotAllowedError",
        406 => "NotAcceptableError",
        407 => "ProxyAuthenticationRequiredError",
        408 => "RequestTimeoutError",
        409 => "ConflictError",
        410 => "GoneError",
        411 => "LengthRequiredError",
        412 => "PreconditionFailedError",
        413 => "ContentTooLargeError",
        414 => "UriTooLongError",
        415 => "UnsupportedMediaTypeError",
        416 => "RangeNotSatisfiableError",
        417 => "ExpectationFailedError",
        418 => "ImATeapotError",
        421 => "MisdirectedRequestError",
        422 => "UnprocessableEntityError",
        423 => "LockedError",
        424 => "FailedDependencyError",
        425 => "TooEarlyError",
        426 => "UpgradeRequiredError",
        428 => "PreconditionError",
        429 => "TooManyRequestsError",
        431 => "RequestHeaderFieldsTooLargeError",
        451 => "UnavailableForLegalReasonsError",
        500 => "InternalServerError",
        501 => "NotImplementedError",
        502 => "BadGatewayError",
        503 => "ServiceUnavailableError",
        504 => "GatewayTimeoutError",
        505 => "HttpVersionNotSupportedError",
        506 => "VariantAlsoNegotiatesError",
        507 => "InsufficientStorageError",
        508 => "LoopDetectedError",
        510 => "NotExtendedError",
        511 => "NetworkAuthenticationRequiredError",
        _ => return None,
    })
}

/// The exception body type for an error response. A `$ref`/scalar/container body
/// resolves through [`base_type_ref`] (in response context — `List`/`Dict`, never
/// `Sequence`); an error with no `application/json` body takes Fern's
/// `typing.Optional[typing.Any]`.
fn error_body_type(resp: &Response) -> TypeRef {
    match resp
        .content
        .get("application/json")
        .and_then(|c| c.schema.as_ref())
    {
        // A named `$ref`, scalar, or container keeps its resolved type. An inline
        // object (bunq's `GenericError`, `{Error: ...}`) or an otherwise-untyped body
        // resolves to bare `Any`, which Fern renders as `Optional[Any]` — the same as
        // a body-less error.
        Some(schema) => match base_type_ref(schema) {
            TypeRef::Primitive(Prim::Any) => {
                TypeRef::Optional(Box::new(TypeRef::Primitive(Prim::Any)))
            }
            other => other,
        },
        None => TypeRef::Optional(Box::new(TypeRef::Primitive(Prim::Any))),
    }
}

/// Hoist a standalone `{ErrorClassName}Body` model for each error response whose
/// body is an inline object (bunq's shared 400 `GenericError` → `BadRequestErrorBody`),
/// deduplicated by name so a body reused across every endpoint is emitted once. The
/// error class itself keeps its `Any` body (see [`error_body_type`]); this type lives
/// in the package-root `types/`, reachable only through the aggregators.
fn hoist_error_body_types(doc: &OpenApi, builder: &mut Builder) {
    let mut seen = std::collections::HashSet::new();
    for (_, item) in &doc.paths {
        for (_, op) in item.operations() {
            for (code, resp) in &op.responses {
                if code.starts_with('2') {
                    continue;
                }
                let Ok(status) = code.parse::<u16>() else {
                    continue;
                };
                let Some(class) = error_class_name(status) else {
                    continue;
                };
                let Some(schema) = resp
                    .content
                    .get("application/json")
                    .and_then(|c| c.schema.as_ref())
                else {
                    continue;
                };
                if is_inline_struct(schema) {
                    let name = format!("{class}Body");
                    if seen.insert(name.clone()) {
                        builder.add_named(&name, schema);
                    }
                }
            }
        }
    }
}

/// Resolve an operation's declared error (non-2xx) responses into `raise` branches.
/// An error response **never** suppresses method generation (issue #43): a status
/// Fern does not name is simply skipped (it falls through to the generic
/// `ApiError`), and any renderable body shape is accepted.
fn resolve_errors(op: &Operation) -> Vec<ErrorResponse> {
    let mut out = Vec::new();
    for (code, resp) in &op.responses {
        if code.starts_with('2') {
            continue;
        }
        let Ok(status) = code.parse::<u16>() else {
            continue;
        };
        let Some(class) = error_class_name(status) else {
            continue;
        };
        out.push(ErrorResponse {
            status_code: status,
            class_name: class.to_string(),
            body_type: error_body_type(resp),
        });
    }
    out
}

/// The stem crozier snake-cases into a header parameter's Python name. Fern drops
/// the conventional `X-` custom-header prefix (`X-TEST-ENDPOINT-HEADER` becomes
/// `test_endpoint_header`), while the wire name stays the `headers` dict key.
fn header_param_stem(wire_name: &str) -> &str {
    wire_name
        .strip_prefix("X-")
        .or_else(|| wire_name.strip_prefix("x-"))
        .unwrap_or(wire_name)
}

/// Resolve an operation's `application/json` request body into the subset crozier
/// renders today. Returns `None` for shapes still outside that subset (which keeps
/// the whole module unemittable rather than emitting a wrong client).
///
/// - A `$ref` to a plain object → [`RequestBody::Inline`]: each field is hoisted
///   into its own argument (`json={...}`, content-type header).
/// - A `$ref` to a string enum or a map → a single `request` arg, `json=request`,
///   content-type header.
/// - A `$ref` to a union → a single `request` arg through the convert wrapper,
///   content-type header.
/// - An inline array → a single `request` arg (`typing.Sequence`), through the
///   convert wrapper when its items are objects, and *no* content-type header.
/// - A bare scalar → a single `request` arg, `json=request`; the content-type
///   header only for the `uuid`/`byte` formats.
fn resolve_request_body(
    doc: &OpenApi,
    types: &[TypeDecl],
    rb: &crate::openapi::RequestBody,
    hoister: &mut InlineHoister,
    request_ctx: &str,
) -> Option<RequestBody> {
    // A raw `application/octet-stream` body is a bytes stream, independent of its
    // schema — Fern types it as a fixed `Union[bytes, ...]` and sends `content=`.
    if rb.content.contains_key("application/octet-stream") {
        return Some(RequestBody::Bytes {
            content_type: "application/octet-stream".to_string(),
        });
    }
    // A form body: `multipart/form-data` (file uploads via `files=`) or
    // `application/x-www-form-urlencoded` (all fields via `data=`).
    for (media_type, multipart) in [
        ("multipart/form-data", true),
        ("application/x-www-form-urlencoded", false),
    ] {
        if let Some(media) = rb.content.get(media_type) {
            let schema = media.schema.as_ref()?;
            let obj = schema
                .reference
                .as_deref()
                .and_then(|r| resolve_ref(doc, r))
                .unwrap_or(schema);
            return Some(RequestBody::Form(FormBody {
                fields: hoist_form_object(obj, hoister, request_ctx),
                multipart,
            }));
        }
    }
    if let Some((media_type, _)) = rb.content.iter().find(|(media_type, media)| {
        *media_type != "*/*"
            && media.schema.as_ref().is_some_and(|schema| {
                let schema = schema
                    .reference
                    .as_deref()
                    .and_then(|reference| resolve_ref(doc, reference))
                    .unwrap_or(schema);
                schema.ty.as_ref().and_then(|ty| ty.primary()) == Some("string")
                    && schema.format.as_deref() == Some("binary")
            })
    }) {
        return Some(RequestBody::Bytes {
            content_type: media_type.clone(),
        });
    }
    let (media_type, media) = rb
        .content
        .get_key_value("application/json")
        .or_else(|| rb.content.get_key_value("*/*"))
        .or_else(|| {
            rb.content
                .iter()
                .find(|(media_type, _)| is_json_like_media_type(media_type))
        })?;
    let schema = media.schema.as_ref()?;
    let required = rb.required == Some(true);
    let content_type_override =
        (media_type != "application/json" && media_type != "*/*").then(|| media_type.to_string());
    if let Some(reference) = &schema.reference {
        let target = resolve_ref(doc, reference)?;
        let class = ref_to_class(reference);
        // A `$ref` to an enum — string (extensible) or integer (a plain `int`
        // alias) — serializes as a plain `json=request` with the content-type
        // header.
        if string_enum_values(target).is_some() || is_int_enum(target) {
            return Some(single(TypeRef::Named(class), required, false, true));
        }
        if target.ty.as_ref().and_then(|ty| ty.primary()) == Some("string")
            && target.format.as_deref() == Some("binary")
        {
            return Some(single_with_override(
                TypeRef::Named(class),
                required,
                false,
                false,
                (media_type == "*/*").then(|| media_type.to_string()),
            ));
        }
        // A `$ref` to a union goes through the convert wrapper (its object
        // variants carry field aliases that must be respected on write).
        if target.one_of.is_some() || target.any_of.is_some() {
            return Some(single(TypeRef::Named(class), required, true, true));
        }
        // A `$ref` to a map (object with `additionalProperties`, no declared
        // properties) is passed straight through as `json=request`.
        if is_map(target) {
            return Some(single(TypeRef::Named(class), required, false, true));
        }
        if target.ty.as_ref().and_then(|t| t.primary()) == Some("array") {
            let type_ref = TypeRef::Named(class);
            let convert = type_needs_convert(&type_ref, types);
            return Some(single(type_ref, required, convert, false));
        }
        // A `$ref` to a plain object is inlined field-by-field.
        if !target.properties.is_empty() || target.all_of.is_some() {
            return hoist_fields(&class, types).map(|mut fields| {
                apply_body_example(&mut fields, target.example.as_ref());
                apply_body_example(&mut fields, media.example.as_ref());
                RequestBody::Inline(fields)
            });
        }
        // A `$ref` to a bare object (no properties/`allOf` — a free-form `Dict`
        // alias, e.g. bunq's `AttachmentPublic`) is passed straight through as a
        // single `json=request` arg, like a map.
        if is_bare_object(target) {
            return Some(single_with_override(
                TypeRef::Named(class),
                required,
                false,
                true,
                content_type_override,
            ));
        }
        return None;
    }
    // An inline object body (properties written directly, not behind a `$ref`) is
    // inlined field-by-field, exactly like a `$ref` object. Its own nested inline
    // objects hoist into `{request_ctx}{Prop}` models.
    if !schema.properties.is_empty() {
        return hoist_inline_object(schema, hoister, request_ctx).map(RequestBody::Inline);
    }
    // An inline map body (`type: object` + `additionalProperties`): a single
    // `request` argument, convert-wrapped when its values are objects/unions. Like
    // any inline container, it carries no content-type header.
    if is_map(schema) {
        let type_ref = base_type_ref(schema);
        let convert = type_needs_convert(&type_ref, types);
        return Some(single_with_override(
            type_ref,
            required,
            convert,
            content_type_override.is_some(),
            content_type_override,
        ));
    }
    // An inline array body: a single `request` argument. A container of objects
    // serializes through the convert wrapper; either way, no content-type header.
    if schema.ty.as_ref().and_then(|t| t.primary()) == Some("array") {
        let items = schema.items.as_ref()?;
        // An array of *inline* objects hoists its element into `{request_ctx}Item`
        // (Fern's structural name for an array body's element) in the tag's `types/`
        // package, so the argument is `Sequence[{Ctx}Item]` rather than
        // `Sequence[Any]`. An array of `$ref`/scalar items passes through unchanged.
        let item = if items.reference.is_none() && is_inline_struct(items) {
            let name = format!("{request_ctx}Item");
            hoister.hoist_object(&name, items);
            TypeRef::Named(name)
        } else {
            base_type_ref(items)
        };
        let convert = hoister.needs_convert(&item);
        return Some(single(
            TypeRef::List(Box::new(item)),
            required,
            convert,
            false,
        ));
    }
    if is_bare_object(schema) {
        return Some(single_with_override(
            base_type_ref(schema),
            required,
            false,
            true,
            content_type_override,
        ));
    }
    // An unknown (empty `{}`) body — Fern renders it as an optional `typing.Any`
    // argument with a plain `json=request` and no content-type header.
    if is_unknown(schema) {
        return Some(single(TypeRef::Primitive(Prim::Any), false, false, false));
    }
    scalar_body(schema).map(|(type_ref, content_type)| {
        single_with_override(
            type_ref,
            required,
            false,
            content_type,
            content_type_override,
        )
    })
}

fn apply_body_example(fields: &mut [BodyField], example: Option<&serde_json::Value>) {
    let Some(values) = example.and_then(serde_json::Value::as_object) else {
        return;
    };
    for field in fields {
        if let Some(value) = values.get(&field.wire_name).and_then(example_literal) {
            field.example = Some(value);
            field.media_example = true;
        }
    }
}

fn is_json_like_media_type(media_type: &str) -> bool {
    media_type.ends_with("+json")
}

fn request_body_ignored(rb: &crate::openapi::RequestBody) -> bool {
    !rb.content.contains_key("application/json")
        && !rb.content.contains_key("application/octet-stream")
        && !rb.content.contains_key("multipart/form-data")
        && !rb.content.contains_key("application/x-www-form-urlencoded")
}

/// Hoist an inline object body's properties into request [`BodyField`]s. Mirrors
/// [`hoist_fields`] but resolves an unnamed schema directly. A nested inline
/// object property hoists into a `{ctx}{Prop}` model via `hoister`; an inline
/// string enum similarly becomes a request-scoped enum.
fn hoist_inline_object(
    schema: &Schema,
    hoister: &mut InlineHoister,
    ctx: &str,
) -> Option<Vec<BodyField>> {
    let required: Vec<&str> = schema.required.iter().map(String::as_str).collect();
    let mut fields = Vec::new();
    for (prop, prop_schema) in &schema.properties {
        let spec_required = required.contains(&prop.as_str());
        let optional = is_optional(prop_schema) || !spec_required;
        let type_ref = hoister.prop_type_ref(ctx, prop, prop_schema);
        fields.push(BodyField {
            wire_name: prop.clone(),
            py_name: naming::field_name(prop),
            convert: hoister.needs_convert(&type_ref),
            type_ref,
            optional,
            nullable: false,
            spec_required,
            example: schema_example(prop_schema).and_then(example_literal),
            media_example: false,
            docstring: clean_doc(prop_schema.description.as_deref()),
            is_file: false,
            collision_prefix: Some(naming::field_name(ctx)),
        });
    }
    Some(fields)
}

/// Hoists inline (non-`$ref`) request/response objects into named tag-scoped
/// [`ObjectType`]s. Nested inline objects hoist recursively as
/// `{parent}{PascalCase(prop)}`; `$ref`s and scalars pass through unchanged. Fern
/// derives these names structurally from the operation and property path, ignoring
/// any `title` on the inline schema.
struct InlineHoister<'a> {
    /// The package-root types, consulted to decide whether a `$ref` field needs
    /// the `convert_and_respect_annotation_metadata` wrapper.
    root_types: &'a [TypeDecl],
    /// The hoisted object types accumulated for the current operation's tag.
    out: Vec<TypeDecl>,
}

impl InlineHoister<'_> {
    /// Hoist an inline object used as a top-level response array item. Fern coins
    /// `{Operation}ResponseItem` and exposes the response as a list of that model.
    fn hoist_response_array_item_object(
        &mut self,
        item_name: &str,
        schema: &Schema,
    ) -> Option<TypeRef> {
        if schema.ty.as_ref().and_then(|ty| ty.primary()) != Some("array") {
            return None;
        }
        let item_schema = schema.items.as_deref()?;
        if item_schema.reference.is_some() || !is_inline_struct(item_schema) {
            return None;
        }
        self.hoist_object(item_name, item_schema);
        Some(TypeRef::List(Box::new(TypeRef::Named(
            item_name.to_string(),
        ))))
    }

    /// Build a named [`ObjectType`] from an inline object schema, recursively
    /// hoisting its nested inline-object properties, and push it to `out`.
    fn hoist_object(&mut self, name: &str, schema: &Schema) {
        let required: Vec<&str> = schema
            .required
            .iter()
            .chain(schema.all_of.iter().flatten().flat_map(|m| &m.required))
            .map(String::as_str)
            .collect();
        let bases = schema
            .all_of
            .iter()
            .flatten()
            .filter_map(|member| member.reference.as_deref().map(ref_to_class))
            .collect();
        let mut fields = Vec::new();
        for member in schema.all_of.iter().flatten() {
            if member.reference.is_none() {
                self.hoist_object_fields(name, member, &required, &mut fields);
            }
        }
        self.hoist_object_fields(name, schema, &required, &mut fields);
        self.out.push(TypeDecl::Object(ObjectType {
            name: name.to_string(),
            module: naming::module_name(name),
            bases,
            fields,
            docstring: clean_doc(schema.description.as_deref()),
        }));
    }

    fn hoist_object_fields(
        &mut self,
        owner: &str,
        schema: &Schema,
        required: &[&str],
        fields: &mut Vec<Field>,
    ) {
        for (prop, prop_schema) in &schema.properties {
            let spec_required =
                required.contains(&prop.as_str()) && prop_schema.read_only != Some(true);
            let optional = is_optional(prop_schema) || !spec_required;
            fields.push(Field {
                wire_name: prop.clone(),
                py_name: naming::model_field_name(prop),
                type_ref: self.prop_type_ref(owner, prop, prop_schema),
                optional,
                nullable: is_optional(prop_schema) && prop_schema.read_only == Some(true),
                spec_required,
                docstring: declared_doc(prop_schema.description.as_deref()),
                example: schema_example(prop_schema).and_then(example_literal),
            });
        }
    }

    /// The type of a property, hoisting an inline object (directly or as an array
    /// item) into `{parent}{PascalCase(prop)}`. A `$ref` or scalar passes through
    /// [`base_type_ref`].
    fn prop_type_ref(&mut self, parent: &str, prop: &str, prop_schema: &Schema) -> TypeRef {
        if prop_schema.reference.is_none() {
            if let Some(values) = string_enum_values(prop_schema) {
                let name = format!("{parent}{}", naming::class_name(prop));
                self.out.push(TypeDecl::Enum(build_enum(
                    &name,
                    values,
                    clean_doc(prop_schema.description.as_deref()),
                )));
                return TypeRef::Named(name);
            }
        }
        if prop_schema.reference.is_none() && is_inline_struct(prop_schema) {
            let nested = format!("{parent}{}", naming::class_name(prop));
            self.hoist_object(&nested, prop_schema);
            return TypeRef::Named(nested);
        }
        if prop_schema.ty.as_ref().and_then(|ty| ty.primary()) == Some("array") {
            if let Some(item_schema) = prop_schema.items.as_deref() {
                if item_schema.reference.is_none() && is_inline_struct(item_schema) {
                    let item_name = format!("{parent}{}Item", naming::class_name(prop));
                    self.hoist_object(&item_name, item_schema);
                    let item = TypeRef::Named(item_name);
                    let item = if is_optional(item_schema) {
                        TypeRef::Optional(Box::new(item))
                    } else {
                        item
                    };
                    return if prop_schema.unique_items == Some(true) {
                        TypeRef::Set(Box::new(item))
                    } else {
                        TypeRef::List(Box::new(item))
                    };
                }
            }
        }
        // A `$ref`, scalar, or container of `$ref`/scalar items passes through.
        base_type_ref(prop_schema)
    }

    /// Hoist an inline string enum on a request parameter's schema into a named
    /// extensible-enum alias `{request_ctx}{Prop}` in the tag's `types/` package,
    /// matching Fern (a `level` query param on `listWidgets` →
    /// `ListWidgetsRequestLevel`). Array item enums hoist to
    /// `{request_ctx}{Param}Item`. A `$ref` or non-enum schema passes through
    /// [`base_type_ref`] unchanged.
    fn hoist_param_enum(&mut self, request_ctx: &str, param: &str, schema: &Schema) -> TypeRef {
        if schema.reference.is_none() {
            if let Some(values) = string_enum_values(schema) {
                let name = format!("{request_ctx}{}", naming::class_name(param));
                self.out.push(TypeDecl::Enum(build_enum(
                    &name,
                    values,
                    clean_doc(schema.description.as_deref()),
                )));
                return TypeRef::Named(name);
            }
            if let Some(array) = self.hoist_array_item_enum(
                &format!("{request_ctx}{}", naming::class_name(param)),
                schema,
            ) {
                return array;
            }
        }
        base_type_ref(schema)
    }

    /// Hoist an inline string enum array item to `{ctx}Item`, preserving the
    /// container shape around the named enum.
    fn hoist_array_item_enum(&mut self, ctx: &str, schema: &Schema) -> Option<TypeRef> {
        if schema.ty.as_ref().and_then(|t| t.primary()) != Some("array") {
            return None;
        }
        let item = schema.items.as_deref()?;
        if item.reference.is_some() {
            return None;
        }
        let values = string_enum_values(item)?;
        let name = format!("{ctx}Item");
        self.out.push(TypeDecl::Enum(build_enum(
            &name,
            values,
            clean_doc(item.description.as_deref()),
        )));
        let item = Box::new(TypeRef::Named(name));
        if schema.unique_items == Some(true) {
            Some(TypeRef::Set(item))
        } else {
            Some(TypeRef::List(item))
        }
    }

    /// Whether a type serializes through the convert wrapper — true when it
    /// references a generated object/union, whether a package-root type or one of
    /// the inline types just hoisted.
    fn needs_convert(&self, t: &TypeRef) -> bool {
        type_needs_convert(t, self.root_types) || type_needs_convert(t, &self.out)
    }
}

/// Hoist a form body's properties into [`BodyField`]s, marking `format: binary`
/// fields as file uploads. Unlike a JSON object body these carry no convert
/// wrapper (they serialize into `data=`/`files=`, not `json=`).
fn hoist_form_object(
    schema: &Schema,
    hoister: &mut InlineHoister,
    request_ctx: &str,
) -> Vec<BodyField> {
    let required: Vec<&str> = schema.required.iter().map(String::as_str).collect();
    schema
        .properties
        .iter()
        .map(|(prop, prop_schema)| {
            let spec_required = required.contains(&prop.as_str());
            let is_file = prop_schema.ty.as_ref().and_then(|t| t.primary()) == Some("string")
                && prop_schema.format.as_deref() == Some("binary");
            BodyField {
                wire_name: prop.clone(),
                py_name: naming::field_name(prop),
                type_ref: if is_unknown(prop_schema) {
                    TypeRef::Optional(Box::new(TypeRef::Primitive(Prim::Any)))
                } else if is_file {
                    base_type_ref(prop_schema)
                } else {
                    hoister.prop_type_ref(request_ctx, prop, prop_schema)
                },
                optional: is_optional(prop_schema) || !spec_required,
                nullable: is_optional(prop_schema),
                spec_required,
                docstring: clean_doc(prop_schema.description.as_deref()),
                convert: false,
                is_file,
                collision_prefix: None,
                example: schema_example(prop_schema).and_then(example_literal),
                media_example: false,
            }
        })
        .collect()
}

/// A one-argument request body.
fn single(type_ref: TypeRef, required: bool, convert: bool, content_type: bool) -> RequestBody {
    single_with_override(type_ref, required, convert, content_type, None)
}

fn single_with_override(
    type_ref: TypeRef,
    required: bool,
    convert: bool,
    content_type: bool,
    content_type_override: Option<String>,
) -> RequestBody {
    RequestBody::Single(SingleBody {
        type_ref,
        required,
        convert,
        content_type,
        content_type_override,
    })
}

/// Hoist a plain object's fields (already resolved in the type layer) into request
/// [`BodyField`]s, deciding per field whether it serializes through the convert
/// wrapper. Returns `None` if the object is not among the built types.
fn hoist_fields(class: &str, types: &[TypeDecl]) -> Option<Vec<BodyField>> {
    let obj = types.iter().find_map(|d| match d {
        TypeDecl::Object(o) if o.name == class => Some(o),
        _ => None,
    })?;
    let mut fields = Vec::new();
    let mut seen = std::collections::HashSet::new();
    append_request_fields(obj, class, types, &mut seen, &mut fields);
    Some(fields)
}

fn append_request_fields(
    obj: &ObjectType,
    request_class: &str,
    types: &[TypeDecl],
    seen: &mut std::collections::HashSet<String>,
    out: &mut Vec<BodyField>,
) {
    if !seen.insert(obj.name.clone()) {
        return;
    }
    out.extend(obj.fields.iter().map(|f| BodyField {
        wire_name: f.wire_name.clone(),
        py_name: naming::field_name(&f.wire_name),
        type_ref: f.type_ref.clone(),
        optional: f.optional,
        nullable: f.nullable || type_ref_allows_none(&f.type_ref, types),
        spec_required: f.spec_required,
        docstring: f.docstring.clone(),
        convert: type_needs_convert(&f.type_ref, types),
        is_file: false,
        collision_prefix: Some(naming::field_name(request_class)),
        example: f.example.clone(),
        media_example: false,
    }));
    for base in &obj.bases {
        if let Some(base_obj) = types.iter().find_map(|decl| match decl {
            TypeDecl::Object(candidate) if candidate.name == *base => Some(candidate),
            _ => None,
        }) {
            append_request_fields(base_obj, request_class, types, seen, out);
        }
    }
}

/// Whether a type serializes through `convert_and_respect_annotation_metadata` —
/// true when it references (through collections/optionals) a generated object or a
/// union alias, whose members carry field aliases that must be respected on write.
fn type_needs_convert(t: &TypeRef, types: &[TypeDecl]) -> bool {
    match t {
        TypeRef::Named(name) => types.iter().any(|d| match d {
            TypeDecl::Object(o) => o.name == *name,
            // A union alias always converts; any other alias converts when its target
            // does — e.g. `Error = List[ErrorItem]` converts because `ErrorItem`
            // carries field aliases (bunq's `Sequence[Error]` body field).
            TypeDecl::Alias(a) => {
                a.name == *name
                    && (matches!(a.target, TypeRef::Union(_))
                        || type_needs_convert(&a.target, types))
            }
            // A discriminated union's wrapper models carry field aliases too.
            TypeDecl::DiscriminatedUnion(u) => u.name == *name,
            // An enum is a plain `str` value — no field aliases to respect.
            TypeDecl::Enum(_) => false,
        }),
        TypeRef::Optional(inner) | TypeRef::List(inner) | TypeRef::Set(inner) => {
            type_needs_convert(inner, types)
        }
        TypeRef::Dict(_, value) => type_needs_convert(value, types),
        _ => false,
    }
}

fn type_ref_allows_none(t: &TypeRef, types: &[TypeDecl]) -> bool {
    match t {
        TypeRef::Optional(_) => true,
        TypeRef::Union(variants) => variants
            .iter()
            .any(|variant| type_ref_allows_none(variant, types)),
        TypeRef::Named(name) => types.iter().any(|decl| match decl {
            TypeDecl::Alias(alias) if alias.name == *name => {
                type_ref_allows_none(&alias.target, types)
            }
            _ => false,
        }),
        TypeRef::Primitive(_)
        | TypeRef::List(_)
        | TypeRef::Set(_)
        | TypeRef::Dict(_, _)
        | TypeRef::Literal(_) => false,
    }
}

/// A bare scalar request-body type Fern serializes with a plain `json=request`,
/// paired with whether it carries the content-type header. Plain scalars and the
/// date formats omit it; the `uuid`/`byte` string formats (still rendered as
/// `str`) carry it. Non-scalar shapes and other string formats return `None`.
fn scalar_body(schema: &Schema) -> Option<(TypeRef, bool)> {
    let type_ref = match schema.ty.as_ref().and_then(|t| t.primary())? {
        "string" => match schema.format.as_deref() {
            None => TypeRef::Primitive(Prim::Str),
            Some("date-time") => TypeRef::Primitive(Prim::Datetime),
            Some("date") => TypeRef::Primitive(Prim::Date),
            // `uuid`/`byte` render as `str` but carry a content-type header.
            Some("uuid" | "byte") => return Some((TypeRef::Primitive(Prim::Str), true)),
            _ => return None,
        },
        "integer" => TypeRef::Primitive(int_prim(schema)),
        "number" => TypeRef::Primitive(Prim::Float),
        "boolean" => TypeRef::Primitive(Prim::Bool),
        _ => return None,
    };
    Some((type_ref, false))
}

/// The integer primitive for a schema: `Long` for `format: int64`, else `Int`.
/// Both render as Python `int`; the split only distinguishes the example value.
fn int_prim(schema: &Schema) -> Prim {
    if schema.format.as_deref() == Some("int64") {
        Prim::Long
    } else {
        Prim::Int
    }
}

/// Resolve a local `#/components/schemas/{key}` reference to its schema.
fn resolve_ref<'a>(doc: &'a OpenApi, reference: &str) -> Option<&'a Schema> {
    let key = reference.rsplit('/').next()?;
    doc.components.schemas.get(key)
}

/// The success (2xx) response's JSON body type, if any.
fn success_response(op: &Operation) -> Option<TypeRef> {
    success_response_schema(op).map(base_type_ref)
}

/// The success (2xx) response's JSON body schema, if any. Fern treats a wildcard
/// `*/*` response body as JSON when no explicit `application/json` media type is
/// present; public specs such as bungie.net use that shape for standard response
/// envelopes.
fn success_response_schema(op: &Operation) -> Option<&Schema> {
    let response = op
        .responses
        .iter()
        .find(|(code, _)| code.starts_with('2'))
        .map(|(_, r)| r)?;
    response
        .content
        .get("application/json")
        .or_else(|| response.content.get("*/*"))?
        .schema
        .as_ref()
}

/// Whether crozier can render an operation's success response. Every resolved
/// shape works: a named model, a scalar, a container, or an inline object (now
/// hoisted into a named `{Tag}{Method}Response` model, see [`InlineHoister`]).
fn response_supported(_op: &Operation) -> bool {
    true
}

/// The first non-empty, trimmed tag on an operation. Fern uses it to group an
/// operation whose `operationId` carries no `group_` prefix into a client.
fn first_tag(op: &Operation) -> Option<&str> {
    op.tags.iter().map(|t| t.trim()).find(|t| !t.is_empty())
}

/// The generated Python method name for an operation.
///
/// Fern derives it from the `operationId` when there is one, and synthesizes it
/// from the route otherwise:
/// - `group_method` (grouped): the method is the suffix after the final `_`,
///   flattened to lowercase for a single-segment group (`noAuth_postWithNoAuth`
///   → `postwithnoauth`) or the whole id snake-cased for a multi-segment group
///   (`endpoints_put_add`);
/// - groupless (`get-all-widgets`, `verify code`, `getThing`): the whole id is
///   `snake_case`d (→ `get_all_widgets`, `verify_code`, `get_thing`);
/// - missing: [`synthesized_method_name`] infers a verb from the HTTP method and
///   route (`GET /widgets` → `list_widgets`).
fn endpoint_method_name(op: &Operation, http_method: &str, url: &str) -> String {
    let id = op.operation_id.trim();
    if id.is_empty() {
        return synthesized_method_name(http_method, url);
    }
    if id.contains('.') {
        return method_from_dotted_id(id);
    }
    if id.contains('_') {
        if first_tag(op).is_none() {
            return naming::sanitize_identifier(&naming::to_snake_case(id));
        }
        if first_segment_is_tag(op, id) {
            return method_after_first_segment(id);
        }
        // A `group_method` operationId whose prefix *is* the group (matches the tag,
        // or there is no tag) has its group stripped, Fern-style (`widgets_getWidget`
        // → `getwidget`, `endpoints_container_get…` → `endpoints_container_get…`).
        // When the prefix is unrelated to the tag (bunq's `CREATE_AttachmentPublic`
        // under `attachment-public` — a verb, not the group), the tag is the group
        // and the whole id, snake-cased, is the method (`create_attachment_public`).
        if group_prefix_is_tag(op, id) {
            return method_from_grouped_id(id);
        }
        return naming::sanitize_identifier(&naming::to_snake_case(id));
    }
    method_from_groupless_id(id, first_tag(op))
}

/// The method name for a `group_method` operationId (one that contains `_`). Fern
/// takes the method segment verbatim here — an explicit `users_list` stays `list`,
/// not `list_` — so no reserved-word munging is applied (contrast
/// [`method_from_groupless_id`], where the name is *derived* and safe-named).
fn method_from_grouped_id(id: &str) -> String {
    let (group, rest) = id.rsplit_once('_').unwrap_or(("", id));
    let name = if group.contains('_') {
        naming::to_snake_case(id)
    } else {
        rest.to_lowercase()
    };
    naming::sanitize_identifier(&name)
}

/// The method name for a dotted operationId (`Group.Method`). Fern treats the
/// dotted prefix as the group and lowercases the final segment verbatim, without
/// snake-casing camel boundaries (`App.GetUsage` → `getusage`).
fn method_from_dotted_id(id: &str) -> String {
    let method = id.rsplit_once('.').map_or(id, |(_, rest)| rest);
    naming::sanitize_identifier(&method.to_ascii_lowercase())
}

/// The method name for a groupless camelCase operationId (no `_`). Fern drops a
/// leading run of words matching the operation's tag before deriving the method,
/// so `activitiesAdd` under tag `Activities` becomes `add`, not `activities_add`
/// (the tag already names the client the method hangs off). When the id does not
/// begin with the tag — or the operation has no tag — the whole id is used.
fn method_from_groupless_id(id: &str, tag: Option<&str>) -> String {
    let snake = naming::to_snake_case(id);
    let tag_snake = tag.map(naming::to_snake_case).unwrap_or_default();
    let method = if tag_snake.is_empty() || stripped_suffix_has_acronym(id, tag) {
        &snake
    } else {
        snake
            .strip_prefix(&format!("{tag_snake}_"))
            .unwrap_or(&snake)
    };
    // This name is *derived* (a tag prefix stripped off a camelCase id), so — unlike
    // the verbatim `method_from_grouped_id` — reserved words are safe-named the way
    // Fern does it: a "list all" endpoint under tag `Activities` becomes `all_`, not
    // the builtin-shadowing `all`. Uses the method-specific reserved set (keywords +
    // `all`), so appwrite's derived `list` stays `list`, matching Fern.
    let ident = naming::sanitize_identifier(method);
    let reserved = tag.map_or_else(
        || naming::is_reserved(&ident),
        |_| naming::is_reserved_method(&ident),
    );
    if reserved {
        format!("{ident}_")
    } else {
        ident
    }
}

fn stripped_suffix_has_acronym(id: &str, tag: Option<&str>) -> bool {
    let Some(tag) = tag else {
        return false;
    };
    if id.len() <= tag.len() || !id[..tag.len()].eq_ignore_ascii_case(tag) {
        return false;
    }
    id.as_bytes()[tag.len()..]
        .windows(2)
        .any(|pair| pair[0].is_ascii_uppercase() && pair[1].is_ascii_uppercase())
}

/// The `PascalCase` context that names an operation's hoisted inline
/// request/response types (`{Ctx}Request`/`{Ctx}Response`). Fern derives it from
/// the `operationId` alone — `inlined_search` → `InlinedSearch`, `verify code` →
/// `VerifyCode` — never prefixing the tag, so a tag-grouped operation's hoisted
/// type stays `VerifyCodeResponse`, not `WidgetsVerifyCodeResponse`.
fn endpoint_pascal_context(op: &Operation, http_method: &str, url: &str) -> String {
    let id = op.operation_id.trim();
    if id.is_empty() {
        naming::to_pascal_case(&synthesized_method_name(http_method, url))
    } else {
        naming::sanitize_identifier(&naming::to_pascal_case(id))
    }
}

/// Fern's fallback endpoint name for an operation that declares no `operationId`:
/// an action verb inferred from the HTTP method and whether the route addresses a
/// collection or a single item, joined to the trailing resource. `GET /widgets` →
/// `list_widgets`, `GET /widgets/{id}` → `get_widget`, `POST /widgets` →
/// `create_widget`. Item routes (ending in a `{param}`) singularize the noun.
fn synthesized_method_name(http_method: &str, url: &str) -> String {
    let is_param = |s: &str| s.starts_with('{') && s.ends_with('}');
    let segments: Vec<&str> = url.split('/').filter(|s| !s.is_empty()).collect();
    let ends_with_param = segments.last().is_some_and(|s| is_param(s));
    let verb = match http_method.to_ascii_uppercase().as_str() {
        "GET" => {
            if ends_with_param {
                "get"
            } else {
                "list"
            }
        }
        "POST" => "create",
        "PUT" | "PATCH" => "update",
        "DELETE" => "delete",
        _ => "call",
    };
    match segments.iter().rev().find(|s| !is_param(s)) {
        Some(resource) => {
            let noun = naming::to_snake_case(resource);
            let noun = if ends_with_param {
                singularize(&noun)
            } else {
                noun
            };
            naming::sanitize_identifier(&format!("{verb}_{noun}"))
        }
        None => verb.to_string(),
    }
}

/// A naive English singularizer for the resource noun of an inferred item-route
/// name (`users` → `user`, `entries` → `entry`). Only exercised for operations
/// with no `operationId` on a `{param}`-terminated route.
fn singularize(word: &str) -> String {
    if let Some(stem) = word.strip_suffix("ies") {
        format!("{stem}y")
    } else if word.ends_with("ss") || !word.ends_with('s') {
        word.to_string()
    } else {
        word[..word.len() - 1].to_string()
    }
}

/// Collect the endpoint client module names, one per operation group, in the
/// order groups first appear across the document's paths.
fn endpoint_modules(doc: &OpenApi) -> Vec<String> {
    let mut modules = Vec::new();
    let mut seen = std::collections::HashSet::new();
    for (url, item) in &doc.paths {
        for (_, op) in item.operations() {
            let module = endpoint_module(op, url);
            if !module.is_empty() && seen.insert(module.clone()) {
                modules.push(module);
            }
        }
    }
    modules
}

/// The `reference.md` / sub-client section title for each module. Keyed by module
/// name, first title wins. See [`module_title`] for the casing rule.
fn endpoint_module_titles(doc: &OpenApi) -> std::collections::BTreeMap<String, String> {
    let mut titles = std::collections::BTreeMap::new();
    for (url, item) in &doc.paths {
        for (_, op) in item.operations() {
            titles
                .entry(endpoint_module(op, url))
                .or_insert_with(|| module_title(doc, op, url));
        }
    }
    titles
}

/// The section title for one operation's module.
///
/// Fern's casing depends on how the operation was grouped. When the group comes
/// from a plain camelCase operationId or the tag alone (`searchWidgets`+`widgets`,
/// `companiesAdd`+`Companies`), Fern titles the section with the **PascalCase** tag
/// (`Widgets`, `Companies`). But when the operationId carries an underscore
/// separator (bunq's `CREATE_AttachmentPublic`), Fern keeps the tag **verbatim**
/// (`attachment-public`, `content`). An untagged group falls back to the PascalCase
/// operationId/path prefix (`EndpointsContainer`).
fn module_title(doc: &OpenApi, op: &Operation, url: &str) -> String {
    let id = op.operation_id.trim();
    if id.contains('.') {
        if let Some((group, _)) = id.split_once('.') {
            if group.is_empty() {
                return String::new();
            }
        }
        if let Some(tag) = first_tag(op) {
            return naming::to_pascal_case(tag);
        }
    }
    if id.contains('_') {
        // Grouped by the operationId prefix → PascalCase; grouped by tag → verbatim.
        if group_prefix_is_tag(op, id) {
            return naming::to_pascal_case(&module_from_grouped_id(id));
        }
        return first_tag(op).expect("mismatch implies a tag").to_string();
    }
    if let Some(tag) = first_tag(op) {
        return title_from_tag(doc, tag);
    }
    naming::to_pascal_case(&endpoint_module(op, url))
}

fn title_from_tag(doc: &OpenApi, tag: &str) -> String {
    let declared = doc.tags.iter().any(|t| t.name == tag);
    if declared {
        tag.to_string()
    } else {
        naming::to_pascal_case(tag)
    }
}

/// The client module (directory) name for an operation.
///
/// Fern groups by the first **tag** whenever the operation has one — even if the
/// operationId also contains an underscore. bunq's `CREATE_AttachmentPublic` under
/// tag `attachment-public` groups as `attachment_public`, not `create`; the
/// underscore prefix there is a verb, not the SDK group. Only an untagged operation
/// falls back to the `group_method` operationId prefix (`endpoints_content_type`,
/// `inlinedrequests`), then the whole id, then the leading path segment. Where the
/// operationId prefix *does* equal the tag (`widgets_getWidget` under `Widgets`),
/// both rules agree, so tag-grouped corpora already matched stay byte-identical.
fn endpoint_module(op: &Operation, url: &str) -> String {
    let id = op.operation_id.trim();
    if first_tag(op).is_some_and(|tag| alnum_lower(tag) == alnum_lower(id)) {
        return String::new();
    }
    if first_tag(op).is_none() && !id.contains('.') {
        return String::new();
    }
    if id.contains('.') {
        if let Some((group, _)) = id.split_once('.') {
            if group.is_empty() {
                return "_".to_string();
            }
        }
        if let Some(tag) = first_tag(op) {
            return compact_module(tag);
        }
        return naming::sanitize_identifier(&naming::to_snake_case(
            id.split_once('.').map_or(id, |(group, _)| group),
        ));
    }
    if id.contains('_') {
        if first_segment_is_tag(op, id) {
            return snake_module(first_tag(op).expect("first segment match implies a tag"));
        }
        // Untagged, or the prefix is the group → group by the operationId prefix.
        // Otherwise the prefix is unrelated to the tag (bunq) → the tag is the group.
        if group_prefix_is_tag(op, id) {
            return module_from_grouped_id(id);
        }
        return snake_module(first_tag(op).expect("mismatch implies a tag"));
    }
    if let Some(tag) = first_tag(op) {
        return snake_module(tag);
    }
    if !id.is_empty() {
        return naming::sanitize_identifier(&naming::to_snake_case(id));
    }
    naming::sanitize_identifier(&naming::to_snake_case(&path_group(url)))
}

/// The snake-cased, identifier-safe module name a tag maps to (`attachment-public`
/// → `attachment_public`, `DagRun` → `dag_run`).
fn snake_module(tag: &str) -> String {
    let name = naming::sanitize_identifier(&naming::to_snake_case(tag));
    module_identifier(&name)
}

/// The compact module name Fern uses for a dotted operation namespace
/// (`GroupV2.GetGroup` -> `groupv2`). Punctuation still becomes a word boundary.
fn compact_module(tag: &str) -> String {
    let name = if tag.chars().all(|c| c.is_ascii_alphanumeric()) {
        naming::sanitize_identifier(&tag.to_ascii_lowercase())
    } else {
        naming::sanitize_identifier(&naming::to_snake_case(tag))
    };
    module_identifier(&name)
}

/// Whether an operation should be grouped by its `group_method` operationId prefix
/// rather than by its tag. True when the operation has no tag (the prefix is all we
/// have), or when the prefix *is* the tag — the operationId genuinely encodes the
/// group (`inlinedRequests_post…` under tag `InlinedRequests`, `endpoints_container_…`
/// under `EndpointsContainer`). False when a tag is present but the prefix is
/// unrelated to it (bunq's `CREATE_…`/`READ_…` verbs under resource tags), where Fern
/// groups by the tag and keeps the whole operationId as the method. Comparison is on
/// the alphanumeric-only lowercasing of each, so `inlinedrequests` ≡ `InlinedRequests`
/// and `endpoints_container` ≡ `EndpointsContainer` but `create` ≢ `attachment-public`.
fn group_prefix_is_tag(op: &Operation, id: &str) -> bool {
    match first_tag(op) {
        None => true,
        Some(tag) => alnum_lower(&module_from_grouped_id(id)) == alnum_lower(tag),
    }
}

fn first_segment_is_tag(op: &Operation, id: &str) -> bool {
    let Some(tag) = first_tag(op) else {
        return false;
    };
    let Some((first, rest)) = id.split_once('_') else {
        return false;
    };
    rest.contains('_') && alnum_lower(first) == alnum_lower(tag)
}

fn method_after_first_segment(id: &str) -> String {
    let rest = id.split_once('_').map_or(id, |(_, rest)| rest);
    naming::sanitize_identifier(&naming::to_snake_case(rest))
}

/// Lowercase, keeping only ASCII alphanumerics — the separator-insensitive key used
/// to test whether an operationId's group prefix and a tag name the same group.
fn alnum_lower(s: &str) -> String {
    s.chars()
        .filter(char::is_ascii_alphanumeric)
        .flat_map(char::to_lowercase)
        .collect()
}

/// The module name from a `group_method` operationId (one that contains `_`):
/// the prefix, snake-cased when itself multi-segment, else lowercased.
fn module_from_grouped_id(id: &str) -> String {
    let prefix = id.rsplit_once('_').map_or(id, |(prefix, _)| prefix);
    let name = if prefix.contains('_') {
        naming::to_snake_case(prefix)
    } else {
        prefix.to_lowercase()
    };
    module_identifier(&naming::sanitize_identifier(&name))
}

fn module_identifier(name: &str) -> String {
    if naming::is_reserved(name) {
        format!("{name}_")
    } else {
        name.to_string()
    }
}

/// The leading static (non-`{param}`) path segment, the last-resort client group
/// for an operation with neither an `operationId` nor a tag; `service` if the
/// route has no static segment.
fn path_group(url: &str) -> String {
    url.split('/')
        .filter(|s| !s.is_empty())
        .find(|s| !(s.starts_with('{') && s.ends_with('}')))
        .unwrap_or("service")
        .to_string()
}

/// Accumulates generated types. Some schemas produce more than one type: an
/// inline schema (a `oneOf` object variant, or an inline enum property) is
/// *hoisted* into its own named type and referenced by name, matching Fern.
struct Builder<'a> {
    types: Vec<TypeDecl>,
    /// The document's component schemas, for resolving discriminated-union member
    /// `$ref`s to their field sets.
    schemas: &'a IndexMap<String, Schema>,
    /// class name → discriminant property to strip from that class's model,
    /// because it is a member of a discriminated union (Fern re-declares the
    /// discriminant on the union wrapper instead).
    strip_discriminant: std::collections::HashMap<String, String>,
}

/// Scan every schema for a discriminated `oneOf`/`anyOf` and record, per member
/// class, the discriminant property to strip from its model. Keyed by class name
/// (post-`class_name` normalization), matching the `owner` passed to
/// [`Builder::collect_fields`].
fn discriminant_strips(
    schemas: &IndexMap<String, Schema>,
) -> std::collections::HashMap<String, String> {
    let mut strips = std::collections::HashMap::new();
    for schema in schemas.values() {
        let Some(disc) = &schema.discriminator else {
            continue;
        };
        if disc.property_name.is_empty() {
            continue;
        }
        for reference in disc.mapping.values() {
            let key = reference.rsplit('/').next().unwrap_or(reference);
            strips.insert(naming::class_name(key), disc.property_name.clone());
        }
    }
    strips
}

/// Collect a discriminated-union member's fields (the referenced model's
/// properties minus the discriminant). Inline hoisting is intentionally skipped:
/// the member model is emitted separately and owns any hoisted property types.
fn member_fields(schema: &Schema, discriminant: &str) -> Vec<Field> {
    let required: Vec<&str> = schema
        .required
        .iter()
        .chain(schema.all_of.iter().flatten().flat_map(|m| &m.required))
        .map(String::as_str)
        .collect();
    let mut fields = Vec::new();
    for member in schema.all_of.iter().flatten() {
        if member.reference.is_none() {
            append_member_fields(member, discriminant, &required, &mut fields);
        }
    }
    append_member_fields(schema, discriminant, &required, &mut fields);
    fields
}

/// Append a schema's own properties (minus the discriminant) to `fields`.
fn append_member_fields(
    schema: &Schema,
    discriminant: &str,
    required: &[&str],
    fields: &mut Vec<Field>,
) {
    for (prop, prop_schema) in &schema.properties {
        if prop == discriminant {
            continue;
        }
        let spec_required = required.contains(&prop.as_str());
        fields.push(Field {
            wire_name: prop.clone(),
            py_name: naming::model_field_name(prop),
            type_ref: base_type_ref(prop_schema),
            optional: is_optional(prop_schema) || !spec_required,
            nullable: is_optional(prop_schema) && prop_schema.read_only == Some(true),
            spec_required,
            docstring: declared_doc(prop_schema.description.as_deref()),
            example: schema_example(prop_schema).and_then(example_literal),
        });
    }
}

impl Builder<'_> {
    /// Classify one named schema and push it (plus any hoisted types).
    fn add_named(&mut self, name: &str, schema: &Schema) {
        let module = naming::module_name(name);
        let docstring = operation_doc(schema.description.as_deref());

        // A discriminated `oneOf`/`anyOf` (with an explicit `mapping`) becomes a
        // set of per-variant wrapper models plus a union alias.
        if let Some(decl) = self.discriminated_union(name, &module, schema, docstring.clone()) {
            self.types.push(TypeDecl::DiscriminatedUnion(decl));
            return;
        }

        // A `oneOf`/`anyOf` with an inline-object variant: hoist each such
        // variant to `{Name}{Ordinal}` and alias to the union of variant types.
        if schema.properties.is_empty() && !is_map(schema) {
            if let Some(variants) = schema.one_of.as_ref().or(schema.any_of.as_ref()) {
                if variants.iter().any(is_inline_object) {
                    let target = TypeRef::Union(
                        variants
                            .iter()
                            .enumerate()
                            .map(|(i, v)| self.variant_ref(name, i, v))
                            .collect(),
                    );
                    self.push_alias(name, module, target, docstring);
                    return;
                }
            }
        }

        // An object with `additionalProperties` but no declared properties is a
        // map, which Fern emits as a `Dict[..]` alias rather than an empty model.
        if is_map(schema) {
            self.push_alias(name, module, full_type_ref(schema), docstring);
            return;
        }

        // A `type: string` enum becomes a real `enum.Enum` class (integer enums
        // stay `Name = int` — see [`base_type_ref`] — and fall through to the alias).
        if let Some(values) = string_enum_values(schema) {
            self.types
                .push(TypeDecl::Enum(build_enum(name, values, docstring)));
            return;
        }

        // A bare `type: object` with no properties, `allOf`, or `additionalProperties`
        // is a free-form object: Fern aliases it to `Dict[str, Optional[Any]]` (bunq's
        // `AttachmentPublic`, `Whitelist`, …), not an empty model class.
        if is_bare_object(schema) {
            self.push_alias(
                name,
                module,
                TypeRef::Dict(
                    Box::new(TypeRef::Primitive(Prim::Str)),
                    Box::new(TypeRef::Optional(Box::new(TypeRef::Primitive(Prim::Any)))),
                ),
                docstring,
            );
            return;
        }

        // Object with properties, an `allOf`, or an explicit `type: object`.
        if !schema.properties.is_empty() || schema.all_of.is_some() || is_object_type(schema) {
            self.add_object(name, module, schema, docstring);
            return;
        }

        // A top-level array of inline objects: Fern hoists the element into its own
        // named `{Name}Item` model and aliases `Name = List[{Name}Item]` (bunq's
        // `Error` → `Error = typing.List[ErrorItem]`), rather than `List[Any]`.
        if schema.ty.as_ref().and_then(|t| t.primary()) == Some("array") {
            if let Some(items) = &schema.items {
                if is_inline_struct(items) {
                    let item_name = format!("{name}Item");
                    let item_module = naming::module_name(&item_name);
                    let item_doc = clean_doc(items.description.as_deref());
                    self.add_object(&item_name, item_module, items, item_doc);
                    self.push_alias(
                        name,
                        module,
                        TypeRef::List(Box::new(TypeRef::Named(item_name))),
                        docstring,
                    );
                    return;
                }
            }
        }

        // Everything else is an alias: a union, an extensible enum, a scalar, or
        // an unknown type. `full_type_ref` carries any `Optional` wrapping.
        self.push_alias(name, module, full_type_ref(schema), docstring);
    }

    /// Build an object model. `allOf` `$ref` members become base classes and
    /// their inline object members contribute fields, alongside the schema's own
    /// `properties`.
    fn add_object(
        &mut self,
        name: &str,
        module: String,
        schema: &Schema,
        docstring: Option<String>,
    ) {
        // `allOf` merges members: `$ref`s become base classes, inline members
        // contribute properties, and `required` applies across the whole set.
        let required: Vec<&str> = schema
            .required
            .iter()
            .chain(schema.all_of.iter().flatten().flat_map(|m| &m.required))
            .map(String::as_str)
            .collect();
        let declared_fields: std::collections::HashSet<&str> = schema
            .properties
            .keys()
            .chain(
                schema
                    .all_of
                    .iter()
                    .flatten()
                    .filter(|member| member.reference.is_none())
                    .flat_map(|member| member.properties.keys()),
            )
            .map(String::as_str)
            .collect();
        let flatten_bases = schema.all_of.iter().flatten().any(|member| {
            member
                .reference
                .as_deref()
                .and_then(|reference| resolve_ref_from_schemas(self.schemas, reference))
                .is_some_and(|base| {
                    base.properties
                        .keys()
                        .any(|field| declared_fields.contains(field.as_str()))
                })
        });
        let mut bases = Vec::new();
        let mut fields = Vec::new();
        for member in schema.all_of.iter().flatten() {
            if let Some(reference) = &member.reference {
                if !flatten_bases {
                    bases.push(ref_to_class(reference));
                }
            } else {
                self.collect_fields(name, member, &required, &mut fields);
            }
        }
        self.collect_fields(name, schema, &required, &mut fields);
        if flatten_bases {
            for member in schema.all_of.iter().flatten() {
                let Some(base) = member
                    .reference
                    .as_deref()
                    .and_then(|reference| resolve_ref_from_schemas(self.schemas, reference))
                else {
                    continue;
                };
                let mut inherited = Vec::new();
                let base_required: Vec<&str> = base.required.iter().map(String::as_str).collect();
                self.collect_fields(name, base, &base_required, &mut inherited);
                inherited.retain(|field| {
                    if let Some(existing) = fields
                        .iter_mut()
                        .find(|existing| existing.wire_name == field.wire_name)
                    {
                        if existing.docstring.is_none() {
                            existing.docstring.clone_from(&field.docstring);
                        }
                        false
                    } else {
                        true
                    }
                });
                fields.extend(inherited);
            }
        }
        self.types.push(TypeDecl::Object(ObjectType {
            name: name.to_string(),
            module,
            bases,
            fields,
            docstring,
        }));
    }

    /// Append `schema`'s properties to `fields`, hoisting inline property types.
    /// `required` is the effective required set (merged across any `allOf`).
    fn collect_fields(
        &mut self,
        owner: &str,
        schema: &Schema,
        required: &[&str],
        fields: &mut Vec<Field>,
    ) {
        let strip = self.strip_discriminant.get(owner).cloned();
        for (prop, prop_schema) in &schema.properties {
            // A discriminated-union member drops the discriminant property from
            // its own model; Fern re-declares it on the union wrapper instead.
            if strip.as_deref() == Some(prop.as_str()) {
                continue;
            }
            // A `readOnly` property is server-populated, so Fern treats it as
            // optional (and never a required input) even if listed in `required`.
            let spec_required =
                required.contains(&prop.as_str()) && prop_schema.read_only != Some(true);
            let optional = is_optional(prop_schema) || !spec_required;
            fields.push(Field {
                wire_name: prop.clone(),
                py_name: naming::model_field_name(prop),
                type_ref: self.field_type_ref(owner, prop, prop_schema),
                optional,
                nullable: is_optional(prop_schema) && prop_schema.read_only == Some(true),
                spec_required,
                docstring: declared_doc(prop_schema.description.as_deref()),
                example: schema_example(prop_schema).and_then(example_literal),
            });
        }
    }

    /// Build a [`DiscriminatedUnion`] from a schema, or `None` if it is not a
    /// discriminated `oneOf`/`anyOf` with an explicit `mapping`. Each mapping
    /// entry `value → $ref` becomes a `{Name}_{Variant}` wrapper carrying the
    /// discriminant literal plus the referenced model's (stripped) fields.
    fn discriminated_union(
        &self,
        name: &str,
        module: &str,
        schema: &Schema,
        docstring: Option<String>,
    ) -> Option<DiscriminatedUnion> {
        let disc = schema.discriminator.as_ref()?;
        // Only oneOf/anyOf schemas carry a discriminator, and we key generation
        // off the explicit mapping (value → variant `$ref`).
        schema.one_of.as_ref().or(schema.any_of.as_ref())?;
        if disc.property_name.is_empty() || disc.mapping.is_empty() {
            return None;
        }
        let mut members = Vec::new();
        let mut variant_targets = Vec::new();
        for (value, reference) in &disc.mapping {
            let target_key = reference.rsplit('/').next().unwrap_or(reference);
            let target = self.schemas.get(target_key)?;
            members.push(UnionMember {
                // Fern names the wrapper after the discriminant *value*
                // (`Node_And`), not the referenced schema (`AndNode`) — the two
                // coincide only when the mapping key equals the schema name.
                class_name: format!("{name}_{}", naming::class_name(value)),
                discriminant: value.clone(),
                fields: member_fields(target, &disc.property_name),
            });
            variant_targets.push(naming::class_name(target_key));
        }
        Some(DiscriminatedUnion {
            name: name.to_string(),
            module: module.to_string(),
            discriminant_property: disc.property_name.clone(),
            members,
            variant_targets,
            docstring,
        })
    }

    /// The type of a property, hoisting an inline string enum to a named
    /// `enum.Enum` class `{Owner}{Prop}` (as Fern does for `typesAnimal`).
    fn field_type_ref(&mut self, owner: &str, prop: &str, prop_schema: &Schema) -> TypeRef {
        if prop == "metadata" && is_unknown(prop_schema) {
            return TypeRef::Optional(Box::new(TypeRef::Primitive(Prim::Any)));
        }
        if prop_schema.reference.is_none() {
            if let Some(values) = string_enum_values(prop_schema) {
                let hoisted = format!("{owner}{}", naming::class_name(prop));
                self.types.push(TypeDecl::Enum(build_enum(
                    &hoisted,
                    values,
                    clean_doc(prop_schema.description.as_deref()),
                )));
                return TypeRef::Named(hoisted);
            }
            // An inline object *with declared properties* hoists to its own named
            // model `{Owner}{Prop}` (Fern: `Meta.cursors` → `MetaCursors`), rather
            // than degrading to `typing.Any`. A bare `type: object` map (no
            // properties) is left to `base_type_ref`.
            if !prop_schema.properties.is_empty() {
                let name = format!("{owner}{}", naming::class_name(prop));
                let module = naming::module_name(&name);
                self.add_object(
                    &name,
                    module,
                    prop_schema,
                    clean_doc(prop_schema.description.as_deref()),
                );
                return TypeRef::Named(name);
            }
            // An array of inline objects hoists the item to `{Owner}{Prop}Item` and
            // types the property as a sequence of it (Fern: `Pipeline.stages` →
            // `List[PipelineStagesItem]`).
            if prop_schema.ty.as_ref().and_then(|t| t.primary()) == Some("array") {
                if let Some(items) = &prop_schema.items {
                    if items.reference.is_none() && !items.properties.is_empty() {
                        let name = format!("{owner}{}Item", naming::class_name(prop));
                        let module = naming::module_name(&name);
                        self.add_object(
                            &name,
                            module,
                            items,
                            clean_doc(items.description.as_deref()),
                        );
                        let item = if is_optional(items) {
                            Box::new(TypeRef::Optional(Box::new(TypeRef::Named(name))))
                        } else {
                            Box::new(TypeRef::Named(name))
                        };
                        return if prop_schema.unique_items == Some(true) {
                            TypeRef::Set(item)
                        } else {
                            TypeRef::List(item)
                        };
                    }
                }
            }
            // A property-level `anyOf`/`oneOf` (undiscriminated) hoists to a named
            // `Union` alias `{Owner}{Prop}` (Fern: `CustomField.value` →
            // `CustomFieldValue`). A `nullable` member is wrapped `Optional`, as Fern
            // does for the alias — kept local to the hoist so inline unions elsewhere
            // are unchanged.
            if let Some(members) = prop_schema.any_of.as_ref().or(prop_schema.one_of.as_ref()) {
                if prop_schema.discriminator.is_none() {
                    let variants: Vec<TypeRef> = members
                        .iter()
                        .map(|m| {
                            // A bare `type: object` union member is an open map to
                            // Fern (`Dict[str, Optional[Any]]`), not `Any`.
                            let ty = if is_bare_object(m) {
                                TypeRef::Dict(
                                    Box::new(TypeRef::Primitive(Prim::Str)),
                                    Box::new(TypeRef::Optional(Box::new(TypeRef::Primitive(
                                        Prim::Any,
                                    )))),
                                )
                            } else {
                                base_type_ref(m)
                            };
                            if m.nullable == Some(true) {
                                TypeRef::Optional(Box::new(ty))
                            } else {
                                ty
                            }
                        })
                        .collect();
                    let name = format!("{owner}{}", naming::class_name(prop));
                    let module = naming::module_name(&name);
                    self.push_alias(
                        &name,
                        module,
                        TypeRef::Union(variants),
                        clean_doc(prop_schema.description.as_deref()),
                    );
                    return TypeRef::Named(name);
                }
            }
        }
        base_type_ref(prop_schema)
    }

    /// Resolve one `oneOf`/`anyOf` variant, hoisting an inline object to a
    /// `{parent}{Ordinal(index)}` model and returning a reference to it.
    fn variant_ref(&mut self, parent: &str, index: usize, variant: &Schema) -> TypeRef {
        if let Some(reference) = &variant.reference {
            return TypeRef::Named(ref_to_class(reference));
        }
        if is_inline_object(variant) {
            let name = format!("{parent}{}", ordinal_word(index));
            let module = naming::module_name(&name);
            self.add_object(
                &name,
                module,
                variant,
                clean_doc(variant.description.as_deref()),
            );
            return TypeRef::Named(name);
        }
        base_type_ref(variant)
    }

    fn push_alias(
        &mut self,
        name: &str,
        module: String,
        target: TypeRef,
        docstring: Option<String>,
    ) {
        self.types.push(TypeDecl::Alias(AliasType {
            name: name.to_string(),
            module,
            target,
            docstring,
        }));
    }
}

fn resolve_ref_from_schemas<'a>(
    schemas: &'a IndexMap<String, Schema>,
    reference: &str,
) -> Option<&'a Schema> {
    schemas.get(reference.rsplit('/').next()?)
}

/// Fern's extensible-enum rendering of a string enum: `Union[Literal[..], Any]`.
fn extensible_enum(values: Vec<String>) -> TypeRef {
    TypeRef::Union(vec![
        TypeRef::Literal(values),
        TypeRef::Primitive(Prim::Any),
    ])
}

/// An object with `additionalProperties` but no declared properties — a map.
fn is_map(schema: &Schema) -> bool {
    is_object_type(schema)
        && schema.properties.is_empty()
        && matches!(
            schema.additional_properties,
            Some(AdditionalProperties::Schema(_) | AdditionalProperties::Bool(true))
        )
}

/// An inline (not `$ref`) object-shaped schema that Fern hoists into its own
/// named type when it appears as a union variant.
fn is_inline_object(schema: &Schema) -> bool {
    schema.reference.is_none()
        && (!schema.properties.is_empty() || schema.all_of.is_some() || is_object_type(schema))
}

/// A bare `type: object` with no declared structure (no properties, `allOf`, or
/// `additionalProperties`) — an open map Fern types as `Dict[str, Optional[Any]]`.
fn is_bare_object(schema: &Schema) -> bool {
    schema.reference.is_none()
        && schema.properties.is_empty()
        && schema.all_of.is_none()
        && schema.additional_properties.is_none()
        && is_object_type(schema)
}

/// An inline (not `$ref`) object with *declared structure* — properties or an
/// `allOf`. Unlike [`is_inline_object`] this excludes a bare `type: object` map
/// (which Fern renders as a `Dict`, not a hoisted model), so it is the test for
/// hoisting an inline request/response body into a named type.
fn is_inline_struct(schema: &Schema) -> bool {
    schema.reference.is_none()
        && (!schema.properties.is_empty()
            || schema.all_of.is_some()
            || (is_object_type(schema)
                && matches!(
                    schema.additional_properties,
                    Some(AdditionalProperties::Bool(false))
                )))
}

/// The English word for a small ordinal, used to name hoisted union variants
/// (`TypesAnimalZero`, `TypesAnimalOne`, ...), matching Fern.
fn ordinal_word(n: usize) -> &'static str {
    const WORDS: [&str; 20] = [
        "Zero",
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Eleven",
        "Twelve",
        "Thirteen",
        "Fourteen",
        "Fifteen",
        "Sixteen",
        "Seventeen",
        "Eighteen",
        "Nineteen",
    ];
    WORDS.get(n).copied().unwrap_or("N")
}

/// Map a schema to its full type expression, wrapping in `Optional` when the
/// schema is nullable or an unknown (untyped) schema. Used for aliases, where
/// optionality lives in the type itself rather than a separate field flag.
fn full_type_ref(schema: &Schema) -> TypeRef {
    let base = base_type_ref(schema);
    if is_optional(schema) {
        match base {
            TypeRef::Optional(_) => base,
            TypeRef::Union(mut variants) if !variants.is_empty() => {
                let last = variants.pop().expect("non-empty union checked above");
                variants.push(TypeRef::Optional(Box::new(last)));
                TypeRef::Union(variants)
            }
            other => TypeRef::Optional(Box::new(other)),
        }
    } else {
        base
    }
}

/// Map a schema to its base type expression, never adding a top-level
/// `Optional` (the caller decides optionality for fields).
fn base_type_ref(schema: &Schema) -> TypeRef {
    // A node the document put where a schema object was expected but that carried a
    // non-object value (issue #86) degrades to Fern's unknown type, `Optional[Any]`.
    if schema.malformed {
        return TypeRef::Optional(Box::new(TypeRef::Primitive(Prim::Any)));
    }
    if let Some(reference) = &schema.reference {
        return TypeRef::Named(ref_to_class(reference));
    }
    if let Some(reference) = single_all_of_ref(schema) {
        return TypeRef::Named(ref_to_class(reference));
    }
    if let Some(values) = string_enum_values(schema) {
        // Fern renders an OpenAPI string enum as an extensible enum.
        return extensible_enum(values);
    }
    if let Some(variants) = union_variants(schema) {
        return TypeRef::Union(variants);
    }
    if is_bare_object(schema) {
        return TypeRef::Dict(
            Box::new(TypeRef::Primitive(Prim::Str)),
            Box::new(TypeRef::Optional(Box::new(TypeRef::Primitive(Prim::Any)))),
        );
    }
    if is_map(schema) {
        return match &schema.additional_properties {
            Some(AdditionalProperties::Schema(value)) => {
                let mut val = base_type_ref(value);
                // Fern makes a nullable map's value type optional too.
                if schema.nullable == Some(true) {
                    val = TypeRef::Optional(Box::new(val));
                }
                TypeRef::Dict(Box::new(TypeRef::Primitive(Prim::Str)), Box::new(val))
            }
            // `additionalProperties: true` is an open map to unknown values, which
            // Fern types as `Dict[str, Optional[Any]]`.
            Some(AdditionalProperties::Bool(true)) => TypeRef::Dict(
                Box::new(TypeRef::Primitive(Prim::Str)),
                Box::new(TypeRef::Optional(Box::new(TypeRef::Primitive(Prim::Any)))),
            ),
            _ => TypeRef::Primitive(Prim::Any),
        };
    }
    match schema.ty.as_ref().and_then(|t| t.primary()) {
        Some("string") => match schema.format.as_deref() {
            Some("date-time") => TypeRef::Primitive(Prim::Datetime),
            Some("date") => TypeRef::Primitive(Prim::Date),
            // Fern's OpenAPI importer maps other string formats (uuid, byte, ...)
            // to plain `str`.
            _ => TypeRef::Primitive(Prim::Str),
        },
        Some("integer") => TypeRef::Primitive(int_prim(schema)),
        Some("number") => TypeRef::Primitive(Prim::Float),
        Some("boolean") => TypeRef::Primitive(Prim::Bool),
        Some("array") => {
            let item = schema.items.as_ref().map_or(
                TypeRef::Optional(Box::new(TypeRef::Primitive(Prim::Any))),
                |i| {
                    if is_unknown(i) {
                        TypeRef::Optional(Box::new(TypeRef::Primitive(Prim::Any)))
                    } else {
                        full_type_ref(i)
                    }
                },
            );
            if schema.unique_items == Some(true) {
                TypeRef::Set(Box::new(item))
            } else {
                TypeRef::List(Box::new(item))
            }
        }
        Some("object") => TypeRef::Primitive(Prim::Any),
        _ => TypeRef::Primitive(Prim::Any),
    }
}

fn single_all_of_ref(schema: &Schema) -> Option<&str> {
    let members = schema.all_of.as_ref()?;
    match members.as_slice() {
        [member] => member.reference.as_deref(),
        _ => None,
    }
}

/// Is a schema optional? A schema is optional when it is explicitly `nullable`
/// or when it is an unknown (untyped) schema, which Fern always renders as
/// `Optional[Any]`.
fn is_optional(schema: &Schema) -> bool {
    schema.nullable == Some(true)
        || matches!(
            schema.ty.as_ref(),
            Some(TypeField::Multiple(types)) if types.iter().any(|ty| ty == "null")
        )
        || is_unknown(schema)
}

/// A schema that carries nothing to determine a type — Fern treats it as an
/// unknown value (`Optional[Any]`).
fn is_unknown(schema: &Schema) -> bool {
    schema.reference.is_none()
        && schema.ty.as_ref().is_none_or(|ty| ty.primary().is_none())
        && schema.one_of.is_none()
        && schema.any_of.is_none()
        && schema.all_of.is_none()
        && schema.enum_values.is_none()
        && schema.properties.is_empty()
        && schema.additional_properties.is_none()
        && schema.items.is_none()
}

/// The string values of a string enum schema, if it is one. Public specs sometimes
/// omit `type: string` on an enum whose values are all strings; Fern still treats
/// that as a string enum.
fn string_enum_values(schema: &Schema) -> Option<Vec<String>> {
    let values = schema.enum_values.as_ref()?;
    if !is_string_type(schema) {
        let omitted_type = schema.ty.is_none();
        let all_strings = values.iter().all(serde_json::Value::is_string);
        if !omitted_type || !all_strings {
            return None;
        }
    }
    let strings: Vec<String> = values
        .iter()
        .filter_map(|v| v.as_str().map(str::to_string))
        .collect();
    // A `type: string` enum whose values are all the wrong type (e.g. the
    // integers `[100, 125, 175, 250]`) leaves nothing to enumerate. Fern drops
    // such members and falls back to the base type rather than emitting an empty
    // enum class with a body-less `visit()` (invalid Python); returning `None`
    // here makes every call site treat the schema as a plain `str` (issue #50).
    if strings.is_empty() {
        return None;
    }
    Some(strings)
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

/// Is this schema an integer `enum` (which Fern aliases to a plain `int`)?
fn is_int_enum(schema: &Schema) -> bool {
    schema.ty.as_ref().and_then(|t| t.primary()) == Some("integer") && schema.enum_values.is_some()
}

/// Is this schema declared as `type: object`?
fn is_object_type(schema: &Schema) -> bool {
    schema.ty.as_ref().and_then(|t| t.primary()) == Some("object")
        || (schema.ty.is_none()
            && (!schema.properties.is_empty() || schema.additional_properties.is_some()))
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

/// Operation descriptions preserve `description: ""` as an empty summary slot in
/// method docs, while still trimming non-empty prose like [`clean_doc`].
fn operation_doc(desc: Option<&str>) -> Option<String> {
    let text = desc?;
    let trimmed = text.trim();
    if trimmed.is_empty() {
        Some(String::new())
    } else {
        Some(trimmed.to_string())
    }
}

/// A description that preserves a distinction Fern renders but [`clean_doc`] erases:
/// `None` when the spec omits `description` entirely, `Some("")` when it declares an
/// empty one, `Some(text)` otherwise. The empty-vs-absent distinction is visible in
/// Fern's output for path parameters (a blank docstring slot vs none) and for model
/// fields (a `pydantic.Field(default=None)` + empty docstring vs a bare `= None`).
/// bunq declares `description: ""` on many nodes; the synthetic seeds omit it.
fn declared_doc(desc: Option<&str>) -> Option<String> {
    // Preserve the description verbatim (Fern does not trim it — a trailing space in
    // `"The URL to visit to "` survives into the docstring), but terminal line breaks
    // are importer formatting rather than docstring content.
    desc.map(|text| text.trim_end_matches(['\r', '\n']).to_string())
}

/// Render an OpenAPI `example` scalar as the Python literal Fern shows in a worked
/// snippet (`"SpaceX"`, `10`, `True`). Returns `None` for a value Fern does not
/// inline as a leaf — null, or a composite object/array.
fn example_literal(value: &serde_json::Value) -> Option<String> {
    match value {
        serde_json::Value::String(s) if s.contains('"') && !s.contains('\'') => Some(format!(
            "'{}'",
            s.replace('\\', "\\\\")
                .replace('\n', "\\n")
                .replace('\r', "\\r")
                .replace('\t', "\\t")
        )),
        serde_json::Value::String(s) => Some(format!(
            "\"{}\"",
            s.replace('\\', "\\\\")
                .replace('"', "\\\"")
                .replace('\n', "\\n")
                .replace('\r', "\\r")
                .replace('\t', "\\t")
        )),
        serde_json::Value::Bool(b) => Some(if *b { "True" } else { "False" }.to_string()),
        serde_json::Value::Number(n) => Some(n.to_string()),
        serde_json::Value::Array(values) => Some(format!(
            "[{}]",
            values
                .iter()
                .map(example_literal)
                .collect::<Option<Vec<_>>>()?
                .join(", ")
        )),
        serde_json::Value::Object(values) => Some(format!(
            "{{{}}}",
            values
                .iter()
                .map(|(key, value)| Some(format!("\"{key}\": {}", example_literal(value)?)))
                .collect::<Option<Vec<_>>>()?
                .join(", ")
        )),
        serde_json::Value::Null => None,
    }
}

#[cfg(test)]
mod tests {
    use super::{
        auth_model, base_type_ref, build_endpoint, build_enum, environment_model,
        method_from_grouped_id, module_from_grouped_id, oauth_scope_enum, scalar_body, singularize,
        synthesized_method_name, Auth, Prim, TypeDecl, TypeRef,
    };
    use crate::openapi::{OpenApi, Schema, TypeField};

    #[test]
    fn build_enum_disambiguates_colliding_member_names() {
        // Two wire values that sanitize to the same identifier must not emit
        // duplicate members/`visit` params (invalid Python); the second is
        // suffixed. (Fern rejects such a spec; crozier keeps generation legal.)
        let e = build_enum(
            "Color",
            vec!["a-b".to_string(), "a b".to_string(), "a.b".to_string()],
            None,
        );
        let members: Vec<&str> = e.members.iter().map(|m| m.name.as_str()).collect();
        assert_eq!(members, ["A_B", "A_B_1", "A_B_2"]);
        let params: Vec<&str> = e.members.iter().map(|m| m.visit_param.as_str()).collect();
        assert_eq!(params, ["a_b", "a_b_1", "a_b_2"]);
        // The wire values are preserved untouched for the `= "…"` initializers.
        let values: Vec<&str> = e.members.iter().map(|m| m.value.as_str()).collect();
        assert_eq!(values, ["a-b", "a b", "a.b"]);
    }

    #[test]
    fn undescribed_single_server_defaults_to_default_environment() {
        let doc: crate::openapi::OpenApi = serde_json::from_value(serde_json::json!({
            "servers": [{ "url": "https://api.example.com" }]
        }))
        .expect("document deserializes");
        let env = environment_model(&doc, "FernApi").expect("server yields environment");
        assert_eq!(env.member.0, "DEFAULT");
        assert_eq!(env.default_ref(), "FernApiEnvironment.DEFAULT");
    }

    #[test]
    fn header_api_key_without_root_security_is_still_required() {
        let doc: crate::openapi::OpenApi = serde_json::from_value(serde_json::json!({
            "components": {
                "securitySchemes": {
                    "apiKey": {
                        "type": "apiKey",
                        "in": "header",
                        "name": "X-API-Key"
                    }
                }
            },
            "paths": {
                "/widgets": {
                    "get": {
                        "operationId": "getWidgets",
                        "responses": { "200": { "description": "OK" } }
                    }
                }
            }
        }))
        .expect("document deserializes");
        let Auth::ApiKey { required, .. } = auth_model(&doc) else {
            panic!("header api key should select api-key auth");
        };
        assert!(required);
    }

    #[test]
    fn oauth2_scopes_emit_oauth_scope_enum() {
        let doc: crate::openapi::OpenApi = serde_json::from_value(serde_json::json!({
            "components": {
                "securitySchemes": {
                    "oauth2": {
                        "type": "oauth2",
                        "flows": {
                            "authorizationCode": {
                                "authorizationUrl": "https://example.com/auth",
                                "tokenUrl": "https://example.com/token",
                                "scopes": {
                                    "ReadData": "Read data",
                                    "WriteData": "Write data"
                                }
                            }
                        }
                    }
                }
            }
        }))
        .expect("document deserializes");
        let enum_type = oauth_scope_enum(&doc).expect("oauth scopes produce enum");
        assert_eq!(enum_type.name, "OauthScope");
        assert_eq!(
            enum_type
                .members
                .iter()
                .map(|m| (m.name.as_str(), m.value.as_str(), m.docstring.as_deref()))
                .collect::<Vec<_>>(),
            [
                ("READ_DATA", "ReadData", Some("Read data")),
                ("WRITE_DATA", "WriteData", Some("Write data")),
            ]
        );
    }

    #[test]
    fn bare_object_map_values_are_open_dicts() {
        let schema: Schema = serde_json::from_value(serde_json::json!({
            "type": "object",
            "additionalProperties": { "type": "object" }
        }))
        .expect("schema deserializes");
        assert!(matches!(
            base_type_ref(&schema),
            TypeRef::Dict(_, ref value)
                if matches!(
                    &**value,
                    TypeRef::Dict(_, inner)
                        if matches!(&**inner, TypeRef::Optional(any) if matches!(&**any, TypeRef::Primitive(Prim::Any)))
                )
        ));
    }

    #[test]
    fn bare_objects_are_open_dicts() {
        let schema: Schema = serde_json::from_value(serde_json::json!({ "type": "object" }))
            .expect("schema deserializes");
        assert!(matches!(
            base_type_ref(&schema),
            TypeRef::Dict(_, ref value)
                if matches!(&**value, TypeRef::Optional(any) if matches!(&**any, TypeRef::Primitive(Prim::Any)))
        ));
    }

    fn scalar(ty: &str, format: Option<&str>) -> Option<(TypeRef, bool)> {
        let schema = Schema {
            ty: Some(TypeField::Single(ty.to_string())),
            format: format.map(str::to_string),
            ..Schema::default()
        };
        scalar_body(&schema)
    }

    #[test]
    fn scalar_body_maps_primitives_and_flags_uuid_and_byte_content_type() {
        // Plain scalars and the date formats serialize with no content-type header.
        assert!(matches!(
            scalar("string", None),
            Some((TypeRef::Primitive(Prim::Str), false))
        ));
        assert!(matches!(
            scalar("string", Some("date-time")),
            Some((TypeRef::Primitive(Prim::Datetime), false))
        ));
        assert!(matches!(
            scalar("integer", None),
            Some((TypeRef::Primitive(Prim::Int), false))
        ));
        assert!(matches!(
            scalar("boolean", None),
            Some((TypeRef::Primitive(Prim::Bool), false))
        ));
        // `uuid`/`byte` render as `str` but carry the content-type header.
        assert!(matches!(
            scalar("string", Some("uuid")),
            Some((TypeRef::Primitive(Prim::Str), true))
        ));
        assert!(matches!(
            scalar("string", Some("byte")),
            Some((TypeRef::Primitive(Prim::Str), true))
        ));
        // Other string formats and non-scalar shapes are excluded.
        assert!(scalar("string", Some("binary")).is_none());
        assert!(scalar("object", None).is_none());
        assert!(scalar("array", None).is_none());
    }

    #[test]
    fn method_name_snakes_whole_id_for_multi_segment_groups() {
        // The group prefix (`endpoints_put`) is multi-segment, so the whole
        // operationId is snake-cased.
        assert_eq!(
            method_from_grouped_id("endpoints_put_add"),
            "endpoints_put_add"
        );
        assert_eq!(
            method_from_grouped_id("endpoints_urls_withMixedCase"),
            "endpoints_urls_with_mixed_case"
        );
        assert_eq!(
            method_from_grouped_id("endpoints_httpMethods_testGet"),
            "endpoints_http_methods_test_get"
        );
    }

    #[test]
    fn method_name_lowercases_suffix_for_single_segment_groups() {
        // A single-segment group (`noReqBody`) contributes nothing to the method
        // name; only the suffix survives, flattened to lowercase.
        assert_eq!(
            method_from_grouped_id("noReqBody_getWithNoRequestBody"),
            "getwithnorequestbody"
        );
        assert_eq!(
            method_from_grouped_id("inlinedRequests_postWithObjectBodyandResponse"),
            "postwithobjectbodyandresponse"
        );
    }

    #[test]
    fn module_mirrors_the_group_naming() {
        assert_eq!(module_from_grouped_id("endpoints_put_add"), "endpoints_put");
        assert_eq!(
            module_from_grouped_id("endpoints_httpMethods_testGet"),
            "endpoints_http_methods"
        );
        assert_eq!(
            module_from_grouped_id("noReqBody_getWithNoRequestBody"),
            "noreqbody"
        );
    }

    fn op(operation_id: &str, tag: &str) -> crate::openapi::Operation {
        serde_json::from_value(serde_json::json!({
            "operationId": operation_id,
            "tags": [tag],
        }))
        .expect("operation deserializes from operationId + tag")
    }

    #[test]
    fn tag_wins_over_a_verb_prefix_operationid() {
        use super::{endpoint_method_name, endpoint_module};
        // bunq: the operationId is `VERB_Resource` with an underscore, but the prefix
        // (`create`) is not the tag (`attachment-public`). Fern groups by the tag and
        // keeps the whole id, snake-cased, as the method.
        let o = op("CREATE_AttachmentPublic", "attachment-public");
        assert_eq!(
            endpoint_module(&o, "/attachment-public"),
            "attachment_public"
        );
        assert_eq!(
            endpoint_method_name(&o, "POST", "/attachment-public"),
            "create_attachment_public"
        );
        // A multi-word tag with hyphens still maps cleanly.
        let o = op("List_all_Content_for_AttachmentPublic", "content");
        assert_eq!(endpoint_module(&o, "/x"), "content");
        assert_eq!(
            endpoint_method_name(&o, "GET", "/x"),
            "list_all_content_for_attachment_public"
        );
    }

    #[test]
    fn operationid_prefix_that_is_the_tag_still_groups_by_the_prefix() {
        use super::{endpoint_method_name, endpoint_module};
        // The synthetic seeds: the operationId prefix *is* the tag, so grouping and
        // method-stripping are unchanged (both rules agree) — this is what keeps the
        // apideck/exhaustive corpora byte-identical after the tag-first change.
        let o = op(
            "inlinedRequests_postWithObjectBodyandResponse",
            "InlinedRequests",
        );
        assert_eq!(endpoint_module(&o, "/x"), "inlinedrequests");
        assert_eq!(
            endpoint_method_name(&o, "POST", "/x"),
            "postwithobjectbodyandresponse"
        );
        let o = op(
            "endpoints_container_getAndReturnListOfPrimitives",
            "EndpointsContainer",
        );
        assert_eq!(endpoint_module(&o, "/x"), "endpoints_container");
        assert_eq!(
            endpoint_method_name(&o, "GET", "/x"),
            "endpoints_container_get_and_return_list_of_primitives"
        );
    }

    #[test]
    fn dotted_operationids_strip_the_group_and_keep_flat_method_names() {
        use super::{endpoint_method_name, endpoint_module, module_title};

        let doc: OpenApi =
            serde_json::from_value(serde_json::json!({})).expect("empty document deserializes");
        let o = op("App.GetApplicationApiUsage", "App");
        assert_eq!(endpoint_module(&o, "/App/ApiUsage/{applicationId}/"), "app");
        assert_eq!(
            module_title(&doc, &o, "/App/ApiUsage/{applicationId}/"),
            "App"
        );
        assert_eq!(
            endpoint_method_name(&o, "GET", "/App/ApiUsage/{applicationId}/"),
            "getapplicationapiusage"
        );

        let o = op("CommunityContent.GetCommunityContent", "CommunityContent");
        assert_eq!(
            endpoint_module(&o, "/CommunityContent/Get/"),
            "communitycontent"
        );
        assert_eq!(
            endpoint_method_name(&o, "GET", "/CommunityContent/Get/"),
            "getcommunitycontent"
        );

        let o: crate::openapi::Operation = serde_json::from_value(serde_json::json!({
            "operationId": ".GetAvailableLocales",
        }))
        .expect("operation deserializes");
        assert_eq!(endpoint_module(&o, "/GetAvailableLocales/"), "_");
        assert_eq!(module_title(&doc, &o, "/GetAvailableLocales/"), "");
        assert_eq!(
            endpoint_method_name(&o, "GET", "/GetAvailableLocales/"),
            "getavailablelocales"
        );
    }

    #[test]
    fn declared_lowercase_tag_titles_stay_verbatim() {
        use super::module_title;

        let declared: OpenApi = serde_json::from_value(serde_json::json!({
            "tags": [{"name": "account"}],
        }))
        .expect("document with tags deserializes");
        let o = op("accountGet", "account");
        assert_eq!(module_title(&declared, &o, "/account"), "account");

        let undeclared: OpenApi =
            serde_json::from_value(serde_json::json!({})).expect("empty document deserializes");
        let o = op("searchWidgets", "widgets");
        assert_eq!(module_title(&undeclared, &o, "/widgets"), "Widgets");
    }

    #[test]
    fn wildcard_success_response_hoists_like_json() {
        let o: crate::openapi::Operation = serde_json::from_value(serde_json::json!({
            "operationId": "widgets_list",
            "tags": ["Widgets"],
            "responses": {
                "200": {
                    "description": "OK",
                    "content": {
                        "*/*": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "Response": { "type": "string" },
                                    "ErrorCode": { "type": "integer", "format": "int32" }
                                }
                            }
                        }
                    }
                }
            }
        }))
        .expect("operation deserializes");
        let mut tag_types = Vec::new();
        let global_headers = std::collections::HashSet::new();
        let doc: crate::openapi::OpenApi =
            serde_json::from_value(serde_json::json!({})).expect("empty document defaults");
        let ep = build_endpoint(
            &doc,
            &[],
            "/widgets",
            "GET",
            &o,
            &mut tag_types,
            &global_headers,
        );

        assert!(matches!(
            ep.response,
            Some(TypeRef::Named(ref name)) if name == "WidgetsListResponse"
        ));
        assert_eq!(tag_types.len(), 1);
        assert_eq!(tag_types[0].module, "widgets");
        let TypeDecl::Object(obj) = &tag_types[0].decl else {
            panic!("wildcard response should hoist to an object");
        };
        assert_eq!(obj.name, "WidgetsListResponse");
        assert_eq!(
            obj.fields
                .iter()
                .map(|field| field.wire_name.as_str())
                .collect::<Vec<_>>(),
            ["ErrorCode", "Response"]
        );
    }

    #[test]
    fn object_fields_treat_single_ref_allof_as_the_ref_type() {
        let mut builder = super::Builder {
            types: Vec::new(),
            schemas: &indexmap::IndexMap::new(),
            strip_discriminant: std::collections::HashMap::new(),
        };
        let schema: Schema = serde_json::from_value(serde_json::json!({
            "type": "object",
            "properties": {
                "wrapped": {
                    "type": "object",
                    "allOf": [
                        { "$ref": "#/components/schemas/WrappedThing" }
                    ]
                }
            }
        }))
        .expect("schema deserializes");

        builder.add_object("Owner", "owner".to_string(), &schema, None);
        let TypeDecl::Object(obj) = &builder.types[0] else {
            panic!("owner should be an object");
        };
        assert!(matches!(
            obj.fields[0].type_ref,
            TypeRef::Named(ref name) if name == "WrappedThing"
        ));
    }

    #[test]
    fn path_parameters_follow_url_placeholder_order() {
        let o: crate::openapi::Operation = serde_json::from_value(serde_json::json!({
            "operationId": "widgets_get",
            "parameters": [
                { "name": "second", "in": "path", "required": true, "schema": { "type": "integer" } },
                { "name": "first", "in": "path", "required": true, "schema": { "type": "integer" } }
            ],
            "responses": { "200": { "description": "OK" } }
        }))
        .expect("operation deserializes");
        let doc: crate::openapi::OpenApi =
            serde_json::from_value(serde_json::json!({})).expect("empty document defaults");
        let mut tag_types = Vec::new();
        let global_headers = std::collections::HashSet::new();
        let ep = build_endpoint(
            &doc,
            &[],
            "/widgets/{first}/{second}",
            "GET",
            &o,
            &mut tag_types,
            &global_headers,
        );

        assert_eq!(
            ep.path_params
                .iter()
                .map(|param| param.wire_name.as_str())
                .collect::<Vec<_>>(),
            ["first", "second"]
        );
    }

    #[test]
    fn synthesized_names_infer_verbs_from_method_and_route() {
        // Fern's fallback naming for an operation with no operationId.
        assert_eq!(synthesized_method_name("GET", "/widgets"), "list_widgets");
        assert_eq!(
            synthesized_method_name("GET", "/widgets/{id}"),
            "get_widget"
        );
        assert_eq!(
            synthesized_method_name("POST", "/widgets"),
            "create_widgets"
        );
        assert_eq!(
            synthesized_method_name("DELETE", "/widgets/{id}"),
            "delete_widget"
        );
        assert_eq!(
            synthesized_method_name("PUT", "/widgets/{id}"),
            "update_widget"
        );
    }

    #[test]
    fn singularize_handles_common_plurals() {
        assert_eq!(singularize("widgets"), "widget");
        assert_eq!(singularize("entries"), "entry");
        // Words ending in `ss` and already-singular nouns pass through.
        assert_eq!(singularize("address"), "address");
        assert_eq!(singularize("widget"), "widget");
    }
}
