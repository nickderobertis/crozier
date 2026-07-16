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
/// server, a single concrete server with no usable description, or a description
/// that merely repeats the API title, or a numbered demo-server description is
/// `DEFAULT`; other described concrete servers keep their description-derived name.
fn environment_model(doc: &OpenApi, client_name: &str) -> Option<Environment> {
    let first = doc.servers.first()?;
    // A server with a templated URL (`{basePath}` variables) is named `DEFAULT` — its
    // member value is the variables resolved to their defaults (bunq). A concrete-URL
    // server takes its member name from its description, even across several servers
    // (the `servers-webhooks` seed's Production/Staging pair keeps `PRODUCTION`).
    let member_name = if !first.variables.is_empty()
        || first.url.starts_with('/')
        || !first.url.contains("://")
        || first
            .description
            .as_deref()
            .is_some_and(|description| description.to_ascii_lowercase().starts_with("demo server"))
    {
        "DEFAULT".to_string()
    } else {
        first
            .description
            .as_deref()
            .filter(|description| {
                !description.eq_ignore_ascii_case("production server")
                    && !description.eq_ignore_ascii_case(&doc.info.title)
            })
            .map(env_member_name)
            .filter(|n| !n.is_empty())
            .unwrap_or_else(|| "DEFAULT".to_string())
    };
    Some(Environment {
        enum_name: format!("{client_name}Environment"),
        member: (member_name, resolve_server_url(first)),
    })
}

/// Substitute a server URL's `{var}` placeholders with each percent-encoded
/// variable `default` (`https://.../{basePath}` + `/v1` →
/// `https://.../%2Fv1`), matching Fern's URI-template expansion.
fn resolve_server_url(server: &crate::openapi::Server) -> String {
    let mut url = server.url.clone();
    for (name, var) in &server.variables {
        url = url.replace(
            &format!("{{{name}}}"),
            &percent_encode_server_variable(&var.default),
        );
    }
    if url == "/" {
        return String::new();
    }
    if url.ends_with('/') && !url.ends_with("://") {
        url.pop();
    }
    url
}

/// Percent-encode a server-variable value as one URI-template expression. RFC 3986
/// unreserved bytes remain literal; every other UTF-8 byte uses uppercase hex.
fn percent_encode_server_variable(value: &str) -> String {
    const HEX: &[u8; 16] = b"0123456789ABCDEF";
    let mut encoded = String::with_capacity(value.len());
    for byte in value.bytes() {
        if byte.is_ascii_alphanumeric() || matches!(byte, b'-' | b'.' | b'_' | b'~') {
            encoded.push(char::from(byte));
        } else {
            encoded.push('%');
            encoded.push(char::from(HEX[usize::from(byte >> 4)]));
            encoded.push(char::from(HEX[usize::from(byte & 0x0f)]));
        }
    }
    encoded
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
/// stays a per-method parameter. Ordinary promoted headers retain first-appearance
/// order; header api-key schemes follow them in scheme declaration order. Fern never
/// promotes a transport-managed header (`User-Agent`, which the HTTP client sets
/// itself), or an `Authorization` parameter already supplied by the selected auth
/// scheme, even when it rides every operation.
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
    let api_key_headers = additional_api_key_global_headers(doc);
    let api_key_wire_names: std::collections::HashSet<&str> = api_key_headers
        .iter()
        .map(|header| header.wire_name.as_str())
        .collect();
    let mut headers: Vec<GlobalHeader> = seen
        .into_iter()
        .filter(|(wire_name, (count, required))| {
            total > 0
                && *count == total
                && (!*required || total > 1)
                && !is_transport_managed_header(wire_name)
                && !is_auth_managed_header(doc, wire_name)
                && !api_key_wire_names.contains(wire_name.as_str())
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
    // An api-key header may also ride every operation as an explicit parameter.
    // Removing it from `seen` above and appending the scheme-derived field here
    // avoids a duplicate while preserving Fern's grouping (ordinary headers,
    // then security headers).
    headers.extend(api_key_headers);
    headers
}

fn additional_api_key_global_headers(doc: &OpenApi) -> Vec<GlobalHeader> {
    use crate::openapi::SecuritySchemeType;

    // Only the first *declared scheme* is the primary auth credential. If that
    // scheme is OAuth/HTTP auth, every later header apiKey is an additional
    // constructor field (Square declares OAuth first and an Authorization apiKey
    // second). When the first scheme itself is a header apiKey, it is represented
    // by `Auth::ApiKey` and must be skipped here to avoid a duplicate field.
    let skip_first_api_key =
        doc.components
            .security_schemes
            .values()
            .next()
            .is_some_and(|scheme| {
                scheme.ty == SecuritySchemeType::ApiKey
                    && scheme.location == Some(ParameterLocation::Header)
            });
    let mut skipped_primary = !skip_first_api_key;
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

/// Whether the SDK's auth credential already owns this header. OAuth and HTTP
/// auth schemes write `Authorization` through the client wrapper, so an explicit
/// operation parameter with that wire name must not become a second constructor
/// or method argument. A declared `apiKey` scheme named `Authorization` remains a
/// distinct global header (Square uses it alongside OAuth), matching Fern.
fn is_auth_managed_header(doc: &OpenApi, wire_name: &str) -> bool {
    use crate::openapi::SecuritySchemeType;

    if !wire_name.eq_ignore_ascii_case("authorization") {
        return false;
    }
    let schemes = doc.components.security_schemes.values();
    let declared_api_key = schemes.clone().any(|scheme| {
        scheme.ty == SecuritySchemeType::ApiKey
            && scheme.location == Some(ParameterLocation::Header)
            && scheme
                .name
                .as_deref()
                .is_some_and(|name| name.eq_ignore_ascii_case(wire_name))
    });
    !declared_api_key && matches!(auth_model(doc), Auth::Bearer { .. } | Auth::Basic { .. })
}

/// The SDK's authentication model, derived from `components.securitySchemes` and
/// how operations reference them. Only the schemes crozier reproduces byte-for-byte
/// are distinguished; OAuth2 uses the bearer-token surface, and anything else
/// falls back to an optional bearer `token`, matching Fern's default client wrapper.
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
                required: doc
                    .security
                    .as_ref()
                    .is_some_and(|requirements| requirements.iter().any(|r| !r.is_empty()))
                    || all_operations_authenticated(doc)
                    || doc.security.is_none(),
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
        Some(s) if s.ty == SecuritySchemeType::OAuth2 => Auth::Bearer {
            required: all_operations_authenticated(doc),
        },
        // Unknown scheme → Fern's default optional bearer token.
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
            // OAuth scope descriptions are map values, so even an empty string is
            // explicitly declared. Fern preserves that as an empty member docstring.
            docstring: if doc.trim().is_empty() {
                Some(String::new())
            } else {
                clean_doc(Some(doc))
            },
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
/// Mirrors the `$ref`-object and form branches of [`resolve_request_body`]. A schema
/// shared as the body of two or more operations (bunq's create+update pairs share
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
                .or_else(|| rb.content.get("multipart/form-data"))
                .or_else(|| rb.content.get("application/x-www-form-urlencoded"))
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

fn request_schema_use_count(doc: &OpenApi, reference: &str) -> usize {
    doc.paths
        .values()
        .flat_map(crate::openapi::PathItem::operations)
        .filter(|(_, operation)| {
            operation
                .request_body
                .as_ref()
                .and_then(|body| {
                    body.content
                        .values()
                        .find_map(|media| media.schema.as_ref())
                })
                .and_then(|schema| schema.reference.as_deref())
                == Some(reference)
        })
        .count()
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
    /// Whether the operation carried the legacy OpenAPI Generator body-name hint.
    pub body_codegen_named: bool,
    /// Whether `requestBody.description` is explicitly present but empty. Fern
    /// treats that importer sentinel as suppressing an explicit JSON content type.
    pub body_description_empty: bool,
    /// Whether the request body omits a description entirely.
    pub body_description_missing: bool,
    /// Whether the body came through `components.requestBodies`, which Fern treats
    /// like a reusable declaration for content-type emission.
    pub body_component_ref: bool,
    /// A JSON-compatible request media type that must be emitted verbatim instead
    /// of `application/json` (for example `application/ndjson`).
    pub body_content_type_override: Option<String>,
    /// Whether the operation uses HTTP Basic authentication. Fern leaves the
    /// ordinary JSON content type to httpx for undocumented Basic-auth bodies
    /// without a path/header parameter.
    pub basic_auth: bool,
    /// Whether the selected request media schema was declared by component `$ref`.
    pub body_schema_ref: bool,
    /// Whether that referenced schema is omitted from the public type layer
    /// because it is used only as this flattened request body.
    pub body_schema_dropped: bool,
    /// Whether two or more operations flatten the same referenced request schema.
    pub body_schema_shared: bool,
    /// Whether the referenced request schema has neither a title nor a
    /// description. Fern's importer treats these anonymous reusable shapes as
    /// transport-level request declarations rather than documented models.
    pub body_schema_metadata_missing: bool,
    /// Whether the referenced request schema declares an example payload.
    pub body_schema_has_example: bool,
    /// Whether the schema example uses the legacy Square wrapper shape
    /// (`{ "request_body": ... }`). Fern's importer uses that wrapper as request
    /// declaration metadata when deciding whether to emit an explicit JSON header.
    pub body_schema_example_wrapped: bool,
    /// Whether the referenced request schema carries Square's legacy beta marker.
    /// Fern uses unwrapped schema examples for worked calls only on this shape.
    pub body_schema_is_beta: bool,
    /// Whether that wrapped `request_body` example supplies every declared
    /// request property. Fern uses this as another request-declaration sentinel,
    /// but does not use the wrapped values in worked Python examples.
    pub body_schema_example_covers_all_fields: bool,
    /// Whether the selected request media declares an example payload. A multipart
    /// upload example is an opaque HTTP transcript to Fern and suppresses worked
    /// examples for that endpoint.
    pub body_media_has_example: bool,
    /// The request media example Fern selects for `reference.md`. When a media
    /// type declares multiple named examples, reference documentation uses the
    /// last one while method docstrings and README examples use the first.
    pub reference_body_example: Option<serde_json::Value>,
    /// Whether the referenced request schema has a substantive description.
    pub body_schema_documented: bool,
    /// Whether the referenced request schema also contains server-populated fields.
    pub body_schema_is_response_heavy: bool,
    /// Whether the referenced request object leaves `additionalProperties` open.
    pub body_schema_is_open: bool,
    /// Whether an inline request object was inferred from properties with no type.
    pub body_schema_implicit_object: bool,
    /// Whether a referenced request schema is composed with `allOf`.
    pub body_all_of: bool,
    /// Whether the JSON request body and success response point at the same schema.
    pub body_response_same_ref: bool,
    /// Whether request and success response reference the same schema regardless
    /// of operation authentication.
    pub body_schema_is_success_response: bool,
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
    /// Whitespace from the end of the source description that Fern preserves in
    /// reference documentation after trimming method docstrings.
    pub reference_description_suffix: String,
    /// Whether the success response is a Server-Sent-Events stream
    /// (`text/event-stream`). A streaming operation is emitted as a
    /// context-managed iterator of chunks rather than a buffered response.
    pub streaming: bool,
    /// Whether the selected success response uses `text/plain` media.
    pub text_response: bool,
    /// Whether the success body is Markdown text. Fern types it as `str` but
    /// omits path arguments from the generated worked example.
    pub markdown_response: bool,
    /// Whether the success response is a binary download (`format: binary`).
    /// Fern emits these as context-managed byte streams instead of buffering.
    pub binary_response: bool,
    /// Whether a binary download uses wildcard (`*/*`) media. Fern omits all
    /// method arguments from these generated worked examples.
    pub wildcard_binary_response: bool,
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
    /// A request-body example used by Fern's worked snippets. Currently populated
    /// for wildcard binary payloads, whose schema may supply a binary placeholder.
    pub example: Option<String>,
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
    /// Whether the field's body-level example came from the component schema
    /// rather than request media. Fern uses schema examples for scalar and
    /// container fields but still synthesizes nested model constructors.
    pub schema_body_example: bool,
}

/// A type hoisted out of an operation's inline request/response body. Unlike a
/// top-level [`TypeDecl`] (which lives in the package-root `types/`), a tag type
/// lives in its owning tag's own `types/` package — Fern's
/// `inlined/types/inlined_search_response.py` layout.
#[derive(Debug, Clone)]
pub struct TagTypeDecl {
    /// The owning tag's client-module (directory) name, e.g. `inlined`.
    pub module: String,
    /// The generated type.
    pub decl: TypeDecl,
}

/// A generated top-level type.
#[derive(Debug, Clone)]
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
#[derive(Debug, Clone)]
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
#[derive(Debug, Clone)]
pub struct UnionMember {
    /// The wrapper class name (e.g. `Shape_Circle`).
    pub class_name: String,
    /// The discriminant literal value (e.g. `circle`).
    pub discriminant: String,
    /// The variant's fields, with the discriminant property removed.
    pub fields: Vec<Field>,
    /// Optional wrapper class docstring.
    pub docstring: Option<String>,
}

/// A pydantic model type.
#[derive(Debug, Clone)]
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
#[derive(Debug, Clone)]
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
#[derive(Debug, Clone)]
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
#[derive(Debug, Clone)]
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
#[derive(Debug, Clone)]
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
    // `GLOBAL`/`global_`, `0: Active` → `ZERO_ACTIVE`/`zero_active`. Exact duplicate
    // wire values are omitted; distinct values that collapse to the same identifier
    // are suffixed so the generated members and parameters remain valid Python.
    let mut seen_members: std::collections::HashMap<String, usize> =
        std::collections::HashMap::new();
    let mut seen_params: std::collections::HashMap<String, usize> =
        std::collections::HashMap::new();
    let mut seen_values = std::collections::HashSet::new();
    let members = values
        .into_iter()
        .filter(|value| seen_values.insert(value.clone()))
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
        building_types: Default::default(),
    };
    for (key, schema) in &doc.components.schemas {
        builder.add_named(&naming::class_name(key), schema);
    }
    if let Some(oauth_scope) = oauth_scope_enum(doc) {
        builder.types.push(TypeDecl::Enum(oauth_scope));
    }
    deduplicate_type_names(&mut builder.types);
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
    for endpoint in &mut endpoints {
        let body_schema = doc
            .paths
            .get(&endpoint.path)
            .and_then(|item| {
                item.operations()
                    .into_iter()
                    .find(|(method, _)| *method == endpoint.http_method)
                    .map(|(_, operation)| operation)
            })
            .and_then(|operation| operation.request_body.as_ref())
            .and_then(|body| {
                body.content
                    .values()
                    .find_map(|media| media.schema.as_ref())
            });
        endpoint.body_schema_dropped = body_schema
            .and_then(|schema| schema.reference.as_deref())
            .map(ref_to_class)
            .is_some_and(|name| dropped_sources.contains(&name));
        if endpoint.body_schema_dropped {
            let source = body_schema
                .and_then(|schema| schema.reference.as_deref())
                .and_then(|reference| resolve_ref(doc, reference));
            if let (Some(source), Some(RequestBody::Inline(fields))) =
                (source, &mut endpoint.request_body)
            {
                fields.retain(|field| !schema_property_is_read_only(doc, source, &field.wire_name));
                let field_names: std::collections::HashSet<&str> =
                    fields.iter().map(|field| field.py_name.as_str()).collect();
                for path_param in &mut endpoint.path_params {
                    if let Some(base) = path_param.py_name.strip_suffix('_') {
                        if !field_names.contains(base) {
                            path_param.py_name = base.to_string();
                        }
                    }
                }
            }
        }
    }
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
    let component_names: std::collections::HashSet<String> = doc
        .components
        .schemas
        .keys()
        .map(|key| naming::class_name(key))
        .collect();
    let mut retained_refs = std::collections::HashSet::new();
    for decl in types {
        if dropped_sources.contains(decl.name()) || !component_names.contains(decl.name()) {
            continue;
        }
        match decl {
            TypeDecl::Object(object) => {
                object.fields.iter().for_each(|field| {
                    collect_named(&field.type_ref, &mut retained_refs);
                });
            }
            TypeDecl::Alias(alias) => collect_named(&alias.target, &mut retained_refs),
            TypeDecl::DiscriminatedUnion(union) => union
                .members
                .iter()
                .flat_map(|member| &member.fields)
                .for_each(|field| collect_named(&field.type_ref, &mut retained_refs)),
            TypeDecl::Enum(_) => {}
        }
    }

    let mut owners: std::collections::HashMap<String, Vec<String>> =
        std::collections::HashMap::new();
    for (path, item) in &doc.paths {
        for (_, op) in item.operations() {
            let Some(source) = op
                .request_body
                .as_ref()
                .and_then(|body| body.content.get("application/json"))
                .and_then(|media| media.schema.as_ref())
                .and_then(|schema| schema.reference.as_deref())
                .map(ref_to_class)
            else {
                continue;
            };
            if dropped_sources.contains(&source) {
                owners
                    .entry(source)
                    .or_default()
                    .push(endpoint_module(op, path));
            }
        }
    }

    let mut owner_counts: std::collections::HashMap<String, usize> =
        std::collections::HashMap::new();
    for source in dropped_sources {
        let Some(object) = types.iter().find_map(|decl| match decl {
            TypeDecl::Object(object) if object.name == *source => Some(object),
            _ => None,
        }) else {
            continue;
        };
        for field in &object.fields {
            let mut names = std::collections::HashSet::new();
            collect_named(&field.type_ref, &mut names);
            names
                .into_iter()
                .for_each(|name| *owner_counts.entry(name).or_default() += 1);
        }
    }

    let mut pending = Vec::new();
    for source in dropped_sources {
        let Some(module) = owners.get(source).and_then(|modules| modules.first()) else {
            continue;
        };
        let Some(object) = types.iter().find_map(|decl| match decl {
            TypeDecl::Object(object) if object.name == *source => Some(object),
            _ => None,
        }) else {
            continue;
        };
        for field in &object.fields {
            let mut names = std::collections::HashSet::new();
            collect_named(&field.type_ref, &mut names);
            pending.extend(names.into_iter().map(|name| (module.clone(), name)));
        }
    }

    let mut moved = std::collections::HashSet::new();
    while let Some((module, name)) = pending.pop() {
        if moved.contains(&name)
            || component_names.contains(&name)
            || retained_refs.contains(&name)
            || owner_counts.get(&name).is_some_and(|count| *count > 1)
        {
            continue;
        }
        let Some(decl) = types.iter().find(|decl| decl.name() == name) else {
            continue;
        };
        let mut dependencies = std::collections::HashSet::new();
        match decl {
            TypeDecl::Object(object) => object
                .fields
                .iter()
                .for_each(|field| collect_named(&field.type_ref, &mut dependencies)),
            TypeDecl::Alias(alias) => collect_named(&alias.target, &mut dependencies),
            TypeDecl::DiscriminatedUnion(union) => union
                .members
                .iter()
                .flat_map(|member| &member.fields)
                .for_each(|field| collect_named(&field.type_ref, &mut dependencies)),
            TypeDecl::Enum(_) => {}
        }
        moved.insert(name.clone());
        tag_types.push(TagTypeDecl {
            module: module.clone(),
            decl: decl.clone(),
        });
        pending.extend(dependencies.into_iter().map(|name| (module.clone(), name)));
    }
    moved
}

/// Collapse schemas whose source names normalize to the same Python class name.
/// Fern keeps the later declaration, which is also the file that wins when both
/// declarations map to the same module path; removing the earlier declaration
/// keeps lazy-loader exports and type analysis aligned with that winning file.
fn deduplicate_type_names(types: &mut Vec<TypeDecl>) {
    let mut seen = std::collections::HashSet::new();
    types.reverse();
    types.retain(|decl| seen.insert(decl.name().to_string()));
    types.reverse();
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
            let endpoint = build_endpoint(
                doc,
                types,
                path,
                http_method,
                op,
                &mut tag_types,
                &global_names,
            );
            // Fern exposes one method for duplicate synthesized/declared names in
            // the same client, with the later operation replacing the earlier one's
            // contents while retaining its first-seen position. Keep all
            // already-hoisted response types, but only the winning endpoint.
            if let Some(index) = out.iter().position(|existing: &Endpoint| {
                existing.module == endpoint.module && existing.method_name == endpoint.method_name
            }) {
                out[index] = endpoint;
            } else {
                out.push(endpoint);
            }
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
        schemas: Some(&doc.components.schemas),
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
            let convert = hoister.needs_convert(&type_ref);
            // A parameter-level `example` wins; otherwise the schema's own.
            let without_declared_example = parameter_example_value(doc, p).is_none();
            let omit_synthesized_example = without_declared_example
                && (p.required != Some(true) || success_response(op).is_none());
            let optional_referenced_enum = p.required != Some(true)
                && p.example.is_none()
                && p.examples.is_empty()
                && p.schema
                    .as_ref()
                    .and_then(|schema| schema.reference.as_deref())
                    .and_then(|reference| resolve_ref(doc, reference))
                    .is_some_and(|schema| string_enum_values(schema).is_some());
            let example = if omit_synthesized_example || optional_referenced_enum {
                None
            } else {
                query_parameter_example(doc, p)
            };
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
                docstring: declared_doc(p.description.as_deref()),
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
                && !is_auth_managed_header(doc, &p.name)
        })
        .map(|p| {
            let type_ref = if p.schema.is_none() && !p.content.is_empty() {
                TypeRef::Primitive(Prim::Str)
            } else {
                p.schema
                    .as_ref()
                    .map_or(TypeRef::Primitive(Prim::Any), |schema| {
                        hoister.hoist_param_enum(&request_ctx, &p.name, schema)
                    })
            };
            HeaderParam {
                wire_name: p.name.clone(),
                py_name: naming::field_name(header_param_stem(&p.name)),
                type_ref,
                required: p.required == Some(true),
                docstring: declared_doc(p.description.as_deref()),
                example: parameter_example(doc, p),
            }
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
        Some(schema)
            if schema.reference.is_none()
                && (schema.one_of.is_some() || schema.any_of.is_some()) =>
        {
            let name = format!("{pascal_ctx}Response");
            let variants = schema
                .one_of
                .as_ref()
                .or(schema.any_of.as_ref())
                .expect("union branch checked above");
            let target = TypeRef::Union(
                variants
                    .iter()
                    .enumerate()
                    .map(|(index, variant)| {
                        hoister.hoist_union_variant(&name, index, variant, variants)
                    })
                    .collect(),
            );
            hoister.out.push(TypeDecl::Alias(AliasType {
                name: name.clone(),
                module: naming::module_name(&name),
                target,
                docstring: clean_doc(schema.description.as_deref()),
            }));
            Some(TypeRef::Named(name))
        }
        Some(schema) if is_inline_struct(schema) => {
            let name = format!("{pascal_ctx}Response");
            hoister.hoist_object(&name, schema);
            Some(TypeRef::Named(name))
        }
        Some(schema) if schema.reference.is_none() => hoister
            .hoist_array_item_enum(&format!("{pascal_ctx}Response"), schema)
            .or_else(|| {
                hoister
                    .hoist_response_array_item_union(&format!("{pascal_ctx}ResponseItem"), schema)
            })
            .or_else(|| {
                hoister
                    .hoist_response_array_item_object(&format!("{pascal_ctx}ResponseItem"), schema)
            })
            .or_else(|| success_response(op)),
        _ => success_response(op),
    };
    let response = response.map(|response| {
        if has_bodyless_success(op) && !has_text_response(op) {
            optional_type_ref(response)
        } else {
            response
        }
    });

    // A request body is either absent, within the subset crozier can render, or
    // unsupported. Its inline nested objects hoist under the `{Ctx}Request` context.
    let mut request_body = if matches!(http_method, "GET" | "HEAD") {
        None
    } else {
        op.request_body.as_ref().and_then(|rb| {
            resolve_request_body(
                doc,
                types,
                rb,
                &mut hoister,
                &request_ctx,
                !op.parameters.is_empty()
                    || !path_params.is_empty()
                    || !query_params.is_empty()
                    || !header_params.is_empty(),
            )
        })
    };
    if matches!(request_body, Some(RequestBody::Bytes { .. })) {
        header_params.clear();
    }
    let body_ok = matches!(http_method, "GET" | "HEAD")
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
        body_codegen_named: op.codegen_request_body_name.is_some(),
        body_description_empty: op.request_body.as_ref().is_some_and(|body| {
            body.description
                .as_deref()
                .is_some_and(|description| description.trim().is_empty())
        }),
        body_description_missing: op
            .request_body
            .as_ref()
            .is_some_and(|body| body.description.is_none()),
        body_component_ref: op.request_body.as_ref().is_some_and(|rb| rb.component_ref),
        body_content_type_override: op
            .request_body
            .as_ref()
            .and_then(selected_json_request_media)
            .and_then(|(media_type, _)| {
                media_type
                    .ends_with("/ndjson")
                    .then(|| media_type.to_string())
            }),
        basic_auth: operation_uses_basic_auth(doc, op),
        body_schema_ref: op
            .request_body
            .as_ref()
            .and_then(|body| {
                body.content
                    .values()
                    .find_map(|media| media.schema.as_ref())
            })
            .is_some_and(|schema| schema.reference.is_some()),
        body_schema_dropped: false,
        body_schema_shared: op
            .request_body
            .as_ref()
            .and_then(|body| {
                body.content
                    .values()
                    .find_map(|media| media.schema.as_ref())
            })
            .and_then(|schema| schema.reference.as_deref())
            .is_some_and(|reference| request_schema_use_count(doc, reference) > 1),
        body_schema_metadata_missing: op
            .request_body
            .as_ref()
            .and_then(|body| {
                body.content
                    .values()
                    .find_map(|media| media.schema.as_ref())
            })
            .and_then(|schema| schema.reference.as_deref())
            .and_then(|reference| resolve_ref(doc, reference))
            .is_some_and(|schema| {
                schema.title.is_none()
                    && schema.description.is_none()
                    && schema
                        .properties
                        .values()
                        .all(|property| property.title.is_none() && property.description.is_none())
            }),
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
        body_schema_example_wrapped: op
            .request_body
            .as_ref()
            .and_then(|body| {
                body.content
                    .values()
                    .find_map(|media| media.schema.as_ref())
            })
            .and_then(|schema| schema.reference.as_deref())
            .and_then(|reference| resolve_ref(doc, reference))
            .and_then(schema_example)
            .and_then(serde_json::Value::as_object)
            .is_some_and(|example| example.contains_key("request_body")),
        body_schema_is_beta: op
            .request_body
            .as_ref()
            .and_then(|body| {
                body.content
                    .values()
                    .find_map(|media| media.schema.as_ref())
            })
            .and_then(|schema| schema.reference.as_deref())
            .and_then(|reference| resolve_ref(doc, reference))
            .is_some_and(|schema| schema.is_beta == Some(true)),
        body_schema_example_covers_all_fields: op
            .request_body
            .as_ref()
            .and_then(|body| {
                body.content
                    .values()
                    .find_map(|media| media.schema.as_ref())
            })
            .and_then(|schema| schema.reference.as_deref())
            .and_then(|reference| resolve_ref(doc, reference))
            .is_some_and(|schema| {
                let Some(request_body) = schema_example(schema)
                    .and_then(serde_json::Value::as_object)
                    .and_then(|example| example.get("request_body"))
                    .and_then(serde_json::Value::as_object)
                else {
                    return false;
                };
                !schema.properties.is_empty()
                    && schema
                        .properties
                        .keys()
                        .all(|property| request_body.contains_key(property))
            }),
        body_media_has_example: op.request_body.as_ref().is_some_and(|body| {
            body.content
                .values()
                .any(|media| media.example.is_some() || !media.examples.is_empty())
        }),
        reference_body_example: op
            .request_body
            .as_ref()
            .and_then(reference_body_example)
            .cloned(),
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
        body_schema_is_response_heavy: op
            .request_body
            .as_ref()
            .and_then(|body| {
                body.content
                    .values()
                    .find_map(|media| media.schema.as_ref())
            })
            .and_then(|schema| schema.reference.as_deref())
            .and_then(|reference| resolve_ref(doc, reference))
            .is_some_and(|schema| {
                let read_only = schema
                    .properties
                    .values()
                    .filter(|property| property.read_only == Some(true))
                    .count();
                read_only * 2 > schema.properties.len()
            }),
        body_schema_is_open: op
            .request_body
            .as_ref()
            .and_then(|body| {
                body.content
                    .values()
                    .find_map(|media| media.schema.as_ref())
            })
            .and_then(|schema| schema.reference.as_deref())
            .and_then(|reference| resolve_ref(doc, reference))
            .is_some_and(|schema| schema.additional_properties.is_none()),
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
        body_schema_is_success_response: request_and_response_refs_match(op),
        response,
        response_doc: success_response_doc(op),
        errors,
        docstring: operation_doc(op.description.as_deref()),
        reference_description_suffix: op
            .description
            .as_deref()
            .map_or_else(String::new, reference_description_suffix),
        streaming: is_streaming(op),
        text_response: has_text_response(op),
        markdown_response: has_markdown_response(op),
        binary_response: is_binary_response(doc, op),
        wildcard_binary_response: has_wildcard_binary_response(doc, op),
        emittable,
    }
}

fn schema_property_is_read_only(doc: &OpenApi, schema: &Schema, property: &str) -> bool {
    schema.properties.get(property).is_some_and(|property| {
        property
            .reference
            .as_deref()
            .and_then(|reference| resolve_ref(doc, reference))
            .is_some_and(|schema| schema.read_only == Some(true))
    })
}

fn parameter_example_value<'a>(
    doc: &'a OpenApi,
    parameter: &'a crate::openapi::Parameter,
) -> Option<&'a serde_json::Value> {
    parameter
        .example
        .as_ref()
        .or_else(|| {
            parameter
                .examples
                .values()
                .find_map(|example| example.value.as_ref())
        })
        .or_else(|| parameter.schema.as_ref().and_then(schema_example))
        .or_else(|| {
            parameter
                .schema
                .as_ref()
                .and_then(|schema| schema.reference.as_deref())
                .and_then(|reference| resolve_ref(doc, reference))
                .and_then(schema_example)
        })
}

fn parameter_example(doc: &OpenApi, parameter: &crate::openapi::Parameter) -> Option<String> {
    let value = parameter_example_value(doc, parameter)?;
    let schema = parameter.schema.as_ref();
    // Fern discards an example whose JSON kind contradicts the declared scalar
    // type instead of rendering invalid Python for the generated annotation (for
    // example, a numeric OpenAPI example on a `type: string` query parameter).
    if schema.and_then(|schema| schema.ty.as_ref()?.primary()) == Some("string")
        && !value.is_string()
    {
        return None;
    }
    if schema.and_then(|schema| schema.ty.as_ref()?.primary()) == Some("integer") {
        if let Some(minimum) = schema.and_then(|schema| schema.minimum.as_ref()) {
            return example_literal(minimum)
                .map(|value| if value == "0" { "1".into() } else { value });
        }
    }
    if schema.and_then(|schema| schema.ty.as_ref()?.primary()) == Some("number") {
        return example_literal(value).map(|literal| {
            if literal.parse::<i64>().is_ok() {
                format!("{literal}.0")
            } else {
                literal
            }
        });
    }
    example_literal(value)
}

fn query_parameter_example(doc: &OpenApi, parameter: &crate::openapi::Parameter) -> Option<String> {
    parameter_example(doc, parameter).or_else(|| {
        // Fern synthesizes constrained query-string placeholders from the
        // minimum length: its short `"x"` sample or a ten-character sample.
        let minimum = parameter
            .schema
            .as_ref()
            .filter(|schema| schema.ty.as_ref().and_then(TypeField::primary) == Some("string"))
            .and_then(|schema| schema.min_length)?;
        Some(if minimum > 1 {
            "\"strawberry\"".to_string()
        } else {
            "\"x\"".to_string()
        })
    })
}

fn schema_example(schema: &Schema) -> Option<&serde_json::Value> {
    schema.example.as_ref().or_else(|| schema.examples.first())
}

/// Render a schema example for a generated call. Arrays commonly put the example
/// on `items` rather than on the array itself; Fern promotes that to a one-element
/// list in worked examples.
fn schema_example_literal(schema: &Schema) -> Option<String> {
    schema_example(schema)
        .and_then(example_literal)
        .or_else(|| {
            let item = schema.items.as_deref().and_then(schema_example)?;
            Some(format!("[{}]", example_literal(item)?))
        })
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

/// Whether the operation's selected success response is a Server-Sent-Events
/// stream. Fern prefers an `application/json` representation when a response
/// advertises both it and `text/event-stream`; an SSE-only response becomes an
/// iterator of chunks. The `x-fern-streaming` extension is not needed — Fern's
/// OpenAPI importer does not resolve its `chunk-schema-ref`, so the chunk is
/// `typing.Optional[typing.Any]` regardless.
fn is_streaming(op: &Operation) -> bool {
    success_response_entry(op).is_some_and(|response| {
        response.content.contains_key("text/event-stream")
            && !response.content.contains_key("application/json")
    })
}

fn body_response_same_ref(doc: &OpenApi, op: &Operation) -> bool {
    let effective_security = op.security.as_ref().or(doc.security.as_ref());
    // Fern's OAuth2 importer treats an echo schema as a shared model even on an
    // authenticated operation; HTTP bearer/API-key importers retain their older
    // content-type behavior. Check the schemes the operation actually names so an
    // unrelated OAuth2 declaration cannot change a bearer-authenticated endpoint.
    let oauth2 = effective_security.is_some_and(|requirements| {
        requirements.iter().any(|requirement| {
            requirement.keys().any(|name| {
                doc.components
                    .security_schemes
                    .get(name)
                    .is_some_and(|scheme| scheme.ty == crate::openapi::SecuritySchemeType::OAuth2)
            })
        })
    });
    if !oauth2 && effective_security.is_some_and(|reqs| reqs.iter().any(|r| !r.is_empty())) {
        return false;
    }
    request_and_response_refs_match(op)
}

fn operation_uses_basic_auth(doc: &OpenApi, op: &Operation) -> bool {
    op.security
        .as_ref()
        .or(doc.security.as_ref())
        .is_some_and(|requirements| {
            requirements.iter().any(|requirement| {
                requirement.keys().any(|name| {
                    doc.components
                        .security_schemes
                        .get(name)
                        .is_some_and(|scheme| {
                            scheme.ty == crate::openapi::SecuritySchemeType::Http
                                && scheme.scheme == Some(crate::openapi::HttpAuthScheme::Basic)
                        })
                })
            })
        })
}

fn request_and_response_refs_match(op: &Operation) -> bool {
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
            && resp.content.iter().any(|(media_type, media)| {
                media_type.starts_with("image/")
                    || media.schema.as_ref().is_some_and(|schema| {
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

fn has_wildcard_binary_response(_doc: &OpenApi, op: &Operation) -> bool {
    success_response_entry(op)
        .and_then(|response| response.content.get("*/*"))
        .and_then(|media| media.schema.as_ref())
        .is_some_and(|schema| {
            schema.reference.is_none()
                && schema.ty.as_ref().and_then(|ty| ty.primary()) == Some("string")
                && schema.format.as_deref() == Some("binary")
        })
}

/// Position of a path parameter's placeholder for OpenAPI 3.0 importer ordering.
fn path_param_position(path: &str, name: &str) -> Option<usize> {
    path.find(&format!("{{{name}}}"))
}

/// The success (2xx) response's description, cleaned for the `Returns` docstring.
fn success_response_doc(op: &Operation) -> Option<String> {
    let response = success_response_entry(op)?;
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
    match response_schema(resp) {
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
    union_body_suffix: bool,
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
    let (media_type, media) = selected_json_request_media(rb)?;
    let schema = media.schema.as_ref()?;
    // Fern treats a schema-bearing request body as required unless the document
    // explicitly opts out. Wildcard request schemas remain required even when the
    // OpenAPI wrapper says otherwise: the importer models the wildcard payload
    // itself as the endpoint input.
    let required = media_type == "*/*" || rb.required != Some(false);
    let content_type_override = (media_type != "application/json").then(|| media_type.to_string());
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
                rb.required == Some(true),
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
                for field in &mut fields {
                    if field.example.is_none()
                        && target.is_beta == Some(true)
                        && target.properties.len() > 1
                        && target
                            .properties
                            .get(&field.wire_name)
                            .is_some_and(|property| {
                                property.ty.as_ref().and_then(|ty| ty.primary()) == Some("string")
                                    && property.min_length.is_some_and(|minimum| minimum > 0)
                                    && property.max_length.is_none_or(|maximum| maximum <= 128)
                            })
                    {
                        field.example = Some("\"x\"".to_string());
                    }
                }
                apply_body_example(&mut fields, target.example.as_ref(), false);
                apply_body_example(&mut fields, media_example(media), true);
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
    // An inline top-level union is named from the operation and emitted in the
    // tag's `types/` package. The request accepts that alias as one argument and
    // serializes its selected model variant through the annotation converter.
    if schema.one_of.is_some() || schema.any_of.is_some() {
        let request_body_name = if union_body_suffix {
            format!("{request_ctx}Body")
        } else {
            request_ctx.to_string()
        };
        let variants = schema
            .one_of
            .as_ref()
            .or(schema.any_of.as_ref())
            .expect("union branch checked above");
        let target = TypeRef::Union(
            variants
                .iter()
                .enumerate()
                .map(|(index, variant)| {
                    hoister.hoist_union_variant(&request_body_name, index, variant, variants)
                })
                .collect(),
        );
        hoister.out.push(TypeDecl::Alias(AliasType {
            name: request_body_name.clone(),
            module: naming::module_name(&request_body_name),
            target,
            docstring: clean_doc(schema.description.as_deref()),
        }));
        let mut body = single_with_override(
            TypeRef::Named(request_body_name),
            required,
            true,
            true,
            (media_type == "*/*").then(|| media_type.to_string()),
        );
        if let RequestBody::Single(single) = &mut body {
            single.example = media_example(media).and_then(example_literal);
        }
        return Some(body);
    }
    if schema.ty.as_ref().and_then(|ty| ty.primary()) == Some("object")
        && schema.properties.is_empty()
        && (schema.properties.declared()
            || matches!(
                schema.additional_properties,
                Some(AdditionalProperties::Bool(false))
            ))
    {
        return Some(RequestBody::Inline(Vec::new()));
    }
    // An inline object body (properties written directly, not behind a `$ref`) is
    // inlined field-by-field, exactly like a `$ref` object. Its own nested inline
    // objects hoist into `{request_ctx}{Prop}` models.
    if !schema.properties.is_empty() {
        return hoist_inline_object(schema, hoister, request_ctx).map(|mut fields| {
            apply_body_example(&mut fields, media_example(media), true);
            RequestBody::Inline(fields)
        });
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
    if media_type == "*/*"
        && schema.ty.as_ref().and_then(|ty| ty.primary()) == Some("string")
        && schema.format.as_deref() == Some("binary")
    {
        let mut body = single_with_override(
            TypeRef::Primitive(Prim::Str),
            required,
            false,
            false,
            content_type_override,
        );
        if let RequestBody::Single(single) = &mut body {
            single.example = media
                .example
                .as_ref()
                .or_else(|| schema_example(schema))
                .and_then(example_literal);
        }
        return Some(body);
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

fn apply_body_example(
    fields: &mut [BodyField],
    example: Option<&serde_json::Value>,
    media_example: bool,
) {
    let Some(values) = example.and_then(serde_json::Value::as_object) else {
        return;
    };
    for field in fields {
        if let Some(value) = values.get(&field.wire_name) {
            field.example = Some(value.to_string());
            field.media_example = true;
            field.schema_body_example = !media_example;
        }
    }
}

fn media_example(media: &crate::openapi::MediaType) -> Option<&serde_json::Value> {
    media.example.as_ref().or_else(|| {
        media
            .examples
            .values()
            .find_map(|example| example.value.as_ref())
    })
}

/// Select the example Fern uses in `reference.md`. Unlike generated method
/// docstrings and README snippets, Fern's reference writer selects the second
/// value when exactly two named examples are present; other cardinalities use
/// the first value.
fn reference_body_example(body: &crate::openapi::RequestBody) -> Option<&serde_json::Value> {
    let media = body.content.get("application/json").or_else(|| {
        body.content
            .iter()
            .find(|(media_type, _)| is_json_like_media_type(media_type))
            .map(|(_, media)| media)
    })?;
    let examples = &media.examples;
    if examples.len() == 2 {
        examples
            .values()
            .nth(1)
            .and_then(|example| example.value.as_ref())
    } else {
        examples.values().find_map(|example| example.value.as_ref())
    }
}

fn is_json_like_media_type(media_type: &str) -> bool {
    media_type.ends_with("+json") || media_type.ends_with("/ndjson")
}

fn selected_json_request_media(
    body: &crate::openapi::RequestBody,
) -> Option<(&str, &crate::openapi::MediaType)> {
    body.content
        .get("application/json")
        .map(|media| ("application/json", media))
        .or_else(|| body.content.get("*/*").map(|media| ("*/*", media)))
        .or_else(|| {
            body.content
                .iter()
                .find(|(media_type, _)| is_json_like_media_type(media_type))
                .map(|(media_type, media)| (media_type.as_str(), media))
        })
}

fn request_body_ignored(rb: &crate::openapi::RequestBody) -> bool {
    !rb.content.contains_key("application/json")
        && !rb.content.contains_key("application/octet-stream")
        && !rb.content.contains_key("multipart/form-data")
        && !rb.content.contains_key("application/x-www-form-urlencoded")
        && !rb
            .content
            .keys()
            .any(|media| is_json_like_media_type(media))
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
            example: schema_example_literal(prop_schema),
            media_example: false,
            schema_body_example: false,
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
    /// Component schemas, available in real generation so annotation-only
    /// `allOf` property references can be resolved at their use site. Focused
    /// unit helpers that do not exercise references leave this as `None`.
    schemas: Option<&'a IndexMap<String, Schema>>,
    /// The hoisted object types accumulated for the current operation's tag.
    out: Vec<TypeDecl>,
}

impl InlineHoister<'_> {
    /// Hoist an inline union used as a top-level response array item. Fern coins
    /// `{Operation}ResponseItem` and exposes the response as a list of that alias.
    fn hoist_response_array_item_union(
        &mut self,
        item_name: &str,
        schema: &Schema,
    ) -> Option<TypeRef> {
        if schema.ty.as_ref().and_then(|ty| ty.primary()) != Some("array") {
            return None;
        }
        let item_schema = schema.items.as_deref()?;
        let variants = item_schema
            .one_of
            .as_ref()
            .or(item_schema.any_of.as_ref())?;
        let target = TypeRef::Union(
            variants
                .iter()
                .enumerate()
                .map(|(index, variant)| {
                    self.hoist_union_variant(item_name, index, variant, variants)
                })
                .collect(),
        );
        self.out.push(TypeDecl::Alias(AliasType {
            name: item_name.to_string(),
            module: naming::module_name(item_name),
            target,
            docstring: clean_doc(item_schema.description.as_deref()),
        }));
        Some(TypeRef::List(Box::new(TypeRef::Named(
            item_name.to_string(),
        ))))
    }

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
        self.hoist_object_with_doc(name, schema, clean_doc(schema.description.as_deref()));
    }

    fn hoist_object_with_doc(&mut self, name: &str, schema: &Schema, docstring: Option<String>) {
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
            docstring,
        }));
    }

    /// Resolve an inline union variant, hoisting an object member to
    /// `{parent}{Ordinal}` in the operation's tag-scoped `types/` package.
    fn hoist_union_variant(
        &mut self,
        parent: &str,
        index: usize,
        variant: &Schema,
        siblings: &[Schema],
    ) -> TypeRef {
        if let Some(reference) = &variant.reference {
            return TypeRef::Named(ref_to_class(reference));
        }
        if is_inline_object(variant)
            || is_bare_object(variant)
                && schema_example(variant).is_some_and(|example| {
                    example.is_object() && !example_is_schema_definition(example)
                })
        {
            let name = variant_class_name(parent, index, variant, siblings);
            self.hoist_object(&name, variant);
            return TypeRef::Named(name);
        }
        base_type_ref(variant)
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
            let referenced_nullable = self
                .schemas
                .and_then(|schemas| {
                    described_all_of_ref(prop_schema)
                        .and_then(|(reference, _)| resolve_ref_from_schemas(schemas, reference))
                        .map(|target| schema_accepts_none(target, schemas))
                })
                .unwrap_or(false);
            let optional = is_optional(prop_schema) || referenced_nullable || !spec_required;
            fields.push(Field {
                wire_name: prop.clone(),
                py_name: naming::model_field_name(prop),
                type_ref: self.prop_type_ref(owner, prop, prop_schema),
                optional,
                nullable: referenced_nullable
                    || (is_optional(prop_schema) && prop_schema.read_only == Some(true)),
                spec_required,
                docstring: declared_doc(property_description(prop_schema)),
                example: schema_example_literal(prop_schema),
            });
        }
    }

    /// The type of a property, hoisting an inline object (directly or as an array
    /// item) into `{parent}{PascalCase(prop)}`. A `$ref` or scalar passes through
    /// [`base_type_ref`].
    fn prop_type_ref(&mut self, parent: &str, prop: &str, prop_schema: &Schema) -> TypeRef {
        if let (Some(schemas), Some((reference, description))) =
            (self.schemas, described_all_of_ref(prop_schema))
        {
            if let Some(target) = resolve_ref_from_schemas(schemas, reference).cloned() {
                let name = format!("{parent}{}", naming::class_name(prop));
                if let Some(values) = string_enum_values(&target) {
                    self.out.push(TypeDecl::Enum(build_enum(
                        &name,
                        values,
                        clean_doc(description),
                    )));
                    return TypeRef::Named(name);
                }
                if !is_map(&target)
                    && !is_bare_object(&target)
                    && (!target.properties.is_empty()
                        || target.all_of.is_some()
                        || is_object_type(&target))
                {
                    self.hoist_object_with_doc(&name, &target, clean_doc(description));
                    return TypeRef::Named(name);
                }
                return full_type_ref_resolved(&target, schemas);
            }
        }
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
                    return if array_uses_set(prop_schema) {
                        TypeRef::Set(Box::new(item))
                    } else {
                        TypeRef::List(Box::new(item))
                    };
                }
                if item_schema.reference.is_none() {
                    if let Some(members) =
                        item_schema.one_of.as_ref().or(item_schema.any_of.as_ref())
                    {
                        let item_name = format!("{parent}{}Item", naming::class_name(prop));
                        let mut variants: Vec<TypeRef> =
                            members.iter().map(base_type_ref).collect();
                        variants.dedup();
                        self.out.push(TypeDecl::Alias(AliasType {
                            name: item_name.clone(),
                            module: naming::module_name(&item_name),
                            target: TypeRef::Union(variants),
                            docstring: clean_doc(item_schema.description.as_deref()),
                        }));
                        let item = Box::new(TypeRef::Named(item_name));
                        return if array_uses_set(prop_schema) {
                            TypeRef::Set(item)
                        } else {
                            TypeRef::List(item)
                        };
                    }
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
            if is_object_type(schema) && is_inline_struct(schema) {
                let name = format!("{request_ctx}{}", naming::class_name(param));
                self.hoist_object(&name, schema);
                return TypeRef::Named(name);
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
        if array_uses_set(schema) {
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
                example: schema_example_literal(prop_schema),
                media_example: false,
                schema_body_example: false,
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
        example: None,
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
        schema_body_example: false,
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
/// date formats omit it; the `uuid`/`byte` string formats (still rendered as `str`)
/// carry it. Non-scalar shapes and other string formats return `None`.
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
    success_response_schema(op)
        .map(|schema| {
            if is_unknown(schema) {
                full_type_ref(schema)
            } else {
                base_type_ref(schema)
            }
        })
        .or_else(|| {
            let response = success_response_entry(op)?;
            response
                .content
                .get("text/plain")
                .or_else(|| response.content.get("text/markdown"))
                .or_else(|| response.content.get("text/xml"))
                .and_then(|media| media.schema.as_ref())
                .map(|_| TypeRef::Primitive(Prim::Str))
        })
        .or_else(|| {
            success_response_entry(op)?
                .content
                .get("application/json")
                .filter(|media| media.schema.is_none())?;
            Some(TypeRef::Optional(Box::new(TypeRef::Primitive(Prim::Any))))
        })
}

fn has_text_response(op: &Operation) -> bool {
    success_response_entry(op).is_some_and(|response| {
        !response.content.contains_key("application/json")
            && !response.content.contains_key("*/*")
            && (response.content.contains_key("text/plain")
                || response.content.contains_key("text/markdown")
                || response.content.contains_key("text/xml"))
    })
}

fn has_markdown_response(op: &Operation) -> bool {
    success_response_entry(op)
        .is_some_and(|response| response.content.contains_key("text/markdown"))
}

fn has_bodyless_success(op: &Operation) -> bool {
    op.responses.iter().any(|(code, response)| {
        code.starts_with('2')
            && !response
                .content
                .values()
                .any(|media| media.schema.is_some())
    })
}

/// The success (2xx) response's JSON body schema, if any. Fern treats a wildcard
/// `*/*` response body as JSON when no explicit `application/json` media type is
/// present; public specs such as bungie.net use that shape for standard response
/// envelopes.
fn success_response_schema(op: &Operation) -> Option<&Schema> {
    let response = success_response_entry(op)?;
    response
        .content
        .get("application/json")
        .or_else(|| response.content.get("*/*"))?
        .schema
        .as_ref()
}

fn success_response_entry(op: &Operation) -> Option<&Response> {
    op.responses
        .iter()
        .find(|(code, _)| code.starts_with('2'))
        .or_else(|| {
            op.responses
                .iter()
                .find(|(code, _)| code.as_str() == "default")
        })
        .map(|(_, response)| response)
}

fn response_schema(response: &Response) -> Option<&Schema> {
    response
        .content
        .get("application/json")
        .or_else(|| response.content.get("application/jwt"))
        .or_else(|| response.content.get("*/*"))
        .or_else(|| response.content.values().next())?
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
/// - missing: a non-empty summary becomes the method name; without one,
///   [`synthesized_method_name`] joins the HTTP method and full route
///   (`GET /widgets/{id}` → `get_widgets_id`).
fn endpoint_method_name(op: &Operation, http_method: &str, url: &str) -> String {
    let id = op.operation_id.as_deref().unwrap_or_default().trim();
    let method = if op
        .operation_id
        .as_deref()
        .is_some_and(|operation_id| operation_id.trim().is_empty())
    {
        "_".to_string()
    } else if id.is_empty() {
        op.summary
            .as_deref()
            .filter(|summary| !summary.trim().is_empty())
            .map_or_else(
                || synthesized_method_name(http_method, url),
                naming::prose_identifier,
            )
    } else if id.contains('.') {
        method_from_dotted_id(id)
    } else if id.contains('_') {
        if first_tag(op).is_none() {
            naming::sanitize_identifier(&naming::to_snake_case(id))
        } else if first_segment_is_tag(op, id) {
            method_after_first_segment(id)
        } else if group_prefix_is_tag(op, id) {
            // A `group_method` operationId whose prefix *is* the group has its group
            // stripped, Fern-style (`widgets_getWidget` → `getwidget`).
            method_from_grouped_id(id)
        } else {
            // When the prefix is unrelated to the tag, the tag is the group and the
            // whole id is the method (bunq's `CREATE_AttachmentPublic`).
            naming::sanitize_identifier(&naming::to_snake_case(id))
        }
    } else {
        method_from_groupless_id(id, first_tag(op))
    };
    naming::escape_python_keyword(method)
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
    let tag_suffix = tag.and_then(|tag| operation_id_tag_prefix(id, tag));
    let method = if tag_snake.is_empty()
        || stripped_suffix_has_acronym(id, tag)
        // Fern retains the group on a generic `Info` method (`CatalogInfo` →
        // `catalog_info`) instead of producing the overly broad `info`.
        || tag_suffix.is_some_and(|(_, suffix)| suffix.eq_ignore_ascii_case("info"))
    {
        snake.clone()
    } else if let Some((_, suffix)) = tag_suffix {
        naming::to_snake_case(suffix)
    } else {
        snake
            .strip_prefix(&format!("{tag_snake}_"))
            .unwrap_or(&snake)
            .to_string()
    };
    // This name is *derived* (a tag prefix stripped off a camelCase id), so — unlike
    // the verbatim `method_from_grouped_id` — reserved words are safe-named the way
    // Fern does it: a "list all" endpoint under tag `Activities` becomes `all_`, not
    // the builtin-shadowing `all`. Uses the method-specific reserved set (keywords +
    // `all`), so appwrite's derived `list` stays `list`, matching Fern.
    let ident = naming::sanitize_identifier(&method);
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

/// Split a camelCase operation id whose leading characters spell its tag. The
/// actual operation-id casing is retained so an acronym tag such as `APIs` paired
/// with `apisAll` groups as `apis` rather than the generic tag spelling `ap_is`.
fn operation_id_tag_prefix<'a>(id: &'a str, tag: &str) -> Option<(&'a str, &'a str)> {
    let prefix = id.get(..tag.len())?;
    let suffix = id.get(tag.len()..)?;
    if suffix.is_empty()
        || !operation_id_matches_tag_spelling(prefix, tag)
        || !suffix
            .chars()
            .next()
            .is_some_and(|ch| ch.is_ascii_uppercase())
    {
        return None;
    }
    Some((prefix, suffix))
}

/// Case-insensitive tag matching is valid when the tag itself records word
/// boundaries (`Activities`, `APIs`) or both spellings snake-case identically.
/// An all-lowercase tag does not invent boundaries: `apiKeys` under `apikeys`
/// remains the full method name in the `apikeys` client.
fn operation_id_matches_tag_spelling(id: &str, tag: &str) -> bool {
    id.eq_ignore_ascii_case(tag)
        && (tag.chars().any(|ch| ch.is_ascii_uppercase())
            || naming::to_snake_case(id) == naming::to_snake_case(tag))
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
    let id = op.operation_id.as_deref().unwrap_or_default().trim();
    if id.is_empty() {
        let path = url
            .split('/')
            .filter(|segment| !segment.is_empty())
            .map(|segment| segment.trim_matches(['{', '}']))
            .collect::<Vec<_>>()
            .join("_");
        format!(
            "{}{}",
            naming::to_pascal_case(http_method),
            naming::to_pascal_case(&path)
        )
    } else {
        naming::sanitize_identifier(&naming::to_pascal_case(id))
    }
}

/// Fern's fallback endpoint name for an operation that declares neither an
/// `operationId` nor a summary: the lowercase HTTP method followed by every path
/// segment, including path-parameter names (`POST /mapping` → `post_mapping`,
/// `GET /mapping/values/{key}` → `get_mapping_values_key`).
fn synthesized_method_name(http_method: &str, url: &str) -> String {
    let path = url
        .split('/')
        .filter(|segment| !segment.is_empty())
        .map(|segment| segment.trim_matches(['{', '}']))
        .collect::<Vec<_>>()
        .join("_");
    let method = http_method.to_ascii_lowercase();
    if path.is_empty() {
        naming::sanitize_identifier(&method)
    } else {
        naming::sanitize_identifier(&format!("{method}_{}", naming::to_snake_case(&path)))
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
    let id = op.operation_id.as_deref().unwrap_or_default().trim();
    if id.is_empty() {
        if let Some(tag) = first_tag(op) {
            return tag_pascal(tag);
        }
    }
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
        return title_from_tag(doc, first_tag(op).expect("mismatch implies a tag"));
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
        tag_pascal(tag)
    }
}

fn tag_pascal(tag: &str) -> String {
    naming::to_pascal_case(&naming::prose_identifier(tag))
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
    let id = op.operation_id.as_deref().unwrap_or_default().trim();
    if first_tag(op).is_some_and(|tag| operation_id_matches_tag_spelling(id, tag)) {
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
        if let Some((prefix, _)) = operation_id_tag_prefix(id, tag) {
            return snake_module(prefix);
        }
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
    let name = naming::prose_identifier(tag);
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
    /// Names currently being expanded, preventing recursive inline schemas from
    /// recursively rebuilding the same declaration before it is pushed.
    building_types: std::collections::HashSet<String>,
}

fn discriminant_value(schema: &Schema) -> Option<String> {
    string_enum_values(schema)
        .and_then(|values| (values.len() == 1).then(|| values[0].clone()))
        .or_else(|| schema_example(schema)?.as_str().map(str::to_string))
}

fn inferred_discriminant_property(
    schema: &Schema,
    schemas: &IndexMap<String, Schema>,
) -> Option<String> {
    let variants = schema.one_of.as_ref().or(schema.any_of.as_ref())?;
    let references_components = variants.iter().any(|variant| variant.reference.is_some());
    let resolved: Vec<&Schema> = variants
        .iter()
        .map(|variant| {
            variant
                .reference
                .as_deref()
                .and_then(|reference| resolve_ref_from_schemas(schemas, reference))
                .unwrap_or(variant)
        })
        .collect();
    let first = resolved.first()?;
    first.properties.keys().find_map(|property| {
        let values: Option<Vec<String>> = resolved
            .iter()
            .map(|variant| {
                let field = variant.properties.get(property)?;
                let singleton_enum =
                    string_enum_values(field).is_some_and(|values| values.len() == 1);
                if references_components {
                    if property != "type"
                        || !variant.required.contains(property)
                        || schema_example(field)
                            .and_then(serde_json::Value::as_str)
                            .is_none()
                    {
                        return None;
                    }
                } else if !singleton_enum {
                    return None;
                }
                discriminant_value(field)
            })
            .collect();
        let values = values?;
        let distinct: std::collections::HashSet<&str> = values.iter().map(String::as_str).collect();
        (distinct.len() == values.len()).then(|| property.clone())
    })
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
        collect_discriminant_strips(schema, schemas, &mut strips);
    }
    strips
}

fn collect_discriminant_strips(
    schema: &Schema,
    schemas: &IndexMap<String, Schema>,
    strips: &mut std::collections::HashMap<String, String>,
) {
    let property = schema
        .discriminator
        .as_ref()
        .map(|disc| disc.property_name.clone())
        .filter(|property| !property.is_empty())
        .or_else(|| inferred_discriminant_property(schema, schemas));
    if let Some(property) = property {
        if schema.discriminator.is_none() {
            if let Some(variants) = schema.one_of.as_ref().or(schema.any_of.as_ref()) {
                for variant in variants {
                    if let Some(reference) = &variant.reference {
                        strips.insert(ref_to_class(reference), property.clone());
                    }
                }
            }
        }
        if let Some(discriminator) = &schema.discriminator {
            for reference in discriminator.mapping.values() {
                strips.insert(ref_to_class(reference), property.clone());
            }
        }
    }

    for child in schema
        .properties
        .values()
        .chain(schema.items.iter().map(Box::as_ref))
        .chain(schema.one_of.iter().flatten())
        .chain(schema.any_of.iter().flatten())
        .chain(schema.all_of.iter().flatten())
    {
        collect_discriminant_strips(child, schemas, strips);
    }
}

/// Collect a discriminated-union member's fields (the referenced model's
/// properties minus the discriminant). Inline hoisting is intentionally skipped:
/// the member model is emitted separately and owns any hoisted property types.
fn member_fields(
    schema: &Schema,
    discriminant: &str,
    schemas: &IndexMap<String, Schema>,
) -> Vec<Field> {
    let required: Vec<&str> = schema
        .required
        .iter()
        .chain(schema.all_of.iter().flatten().flat_map(|m| &m.required))
        .map(String::as_str)
        .collect();
    let mut fields = Vec::new();
    for member in schema.all_of.iter().flatten() {
        if let Some(base) = member
            .reference
            .as_deref()
            .and_then(|reference| resolve_ref_from_schemas(schemas, reference))
        {
            let base_required: Vec<&str> = base.required.iter().map(String::as_str).collect();
            let base_name = member.reference.as_deref().map(ref_to_class);
            append_member_fields(base, "", &base_required, base_name.as_deref(), &mut fields);
        } else {
            append_member_fields(member, discriminant, &required, None, &mut fields);
        }
    }
    append_member_fields(schema, discriminant, &required, None, &mut fields);
    fields
}

/// Append a schema's own properties (minus the discriminant) to `fields`.
fn append_member_fields(
    schema: &Schema,
    discriminant: &str,
    required: &[&str],
    enum_owner: Option<&str>,
    fields: &mut Vec<Field>,
) {
    for (prop, prop_schema) in &schema.properties {
        if prop == discriminant {
            continue;
        }
        let spec_required = required.contains(&prop.as_str());
        let type_ref = if string_enum_values(prop_schema).is_some() {
            enum_owner.map_or_else(
                || base_type_ref(prop_schema),
                |owner| TypeRef::Named(format!("{owner}{}", naming::class_name(prop))),
            )
        } else {
            base_type_ref(prop_schema)
        };
        fields.push(Field {
            wire_name: prop.clone(),
            py_name: naming::model_field_name(prop),
            type_ref,
            optional: is_optional(prop_schema) || !spec_required,
            nullable: is_optional(prop_schema) && prop_schema.read_only == Some(true),
            spec_required,
            docstring: None,
            example: schema_example_literal(prop_schema),
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
                            .map(|(i, v)| self.variant_ref(name, i, v, variants))
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
        if is_bare_object(schema)
            && !schema.properties.declared()
            && !schema_example(schema).is_some_and(|example| {
                example.is_object() && !example_is_schema_definition(example)
            })
        {
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
                let item_name = format!("{name}Item");
                let item_module = naming::module_name(&item_name);
                if let Some(decl) = self.discriminated_union(&item_name, &item_module, items, None)
                {
                    self.types.push(TypeDecl::DiscriminatedUnion(decl));
                    let collection = if array_uses_set(schema) {
                        TypeRef::Set(Box::new(TypeRef::Named(item_name)))
                    } else {
                        TypeRef::List(Box::new(TypeRef::Named(item_name)))
                    };
                    let target = if schema_accepts_none(schema, self.schemas) {
                        TypeRef::Optional(Box::new(collection))
                    } else {
                        collection
                    };
                    self.push_alias(name, module, target, docstring);
                    return;
                }
                if is_inline_struct(items) {
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
        self.push_alias(
            name,
            module,
            full_type_ref_resolved(schema, self.schemas),
            docstring,
        );
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
        if !self.building_types.insert(name.to_string()) {
            return;
        }
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
        self.building_types.remove(name);
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
            let referenced_read_only = prop_schema
                .reference
                .as_deref()
                .and_then(|reference| reference.rsplit('/').next())
                .and_then(|key| self.schemas.get(key))
                .is_some_and(|schema| schema.read_only == Some(true));
            let spec_required = required.contains(&prop.as_str())
                && prop_schema.read_only != Some(true)
                && !referenced_read_only;
            let referenced_nullable = prop_schema.reference.is_some()
                && referenced_schema_accepts_none(prop_schema, self.schemas)
                || described_all_of_ref(prop_schema)
                    .and_then(|(reference, _)| resolve_ref_from_schemas(self.schemas, reference))
                    .is_some_and(|target| schema_accepts_none(target, self.schemas));
            let optional = is_optional(prop_schema) || referenced_nullable || !spec_required;
            fields.push(Field {
                wire_name: prop.clone(),
                py_name: naming::model_field_name(prop),
                type_ref: self.field_type_ref(owner, prop, prop_schema),
                optional,
                nullable: referenced_nullable
                    || (is_optional(prop_schema)
                        && (prop_schema.reference.is_none()
                            || prop_schema.read_only == Some(true))),
                spec_required,
                docstring: declared_doc(property_description(prop_schema)),
                example: schema_example_literal(prop_schema).or_else(|| {
                    prop_schema
                        .reference
                        .as_deref()
                        .and_then(|reference| reference.rsplit('/').next())
                        .and_then(|key| self.schemas.get(key))
                        .and_then(schema_example_literal)
                }),
            });
        }
    }

    /// Build a [`DiscriminatedUnion`] from a schema, or `None` if it is not a
    /// discriminated `oneOf`/`anyOf` with an explicit `mapping`. Each mapping
    /// entry `value → $ref` becomes a `{Name}_{Variant}` wrapper carrying the
    /// discriminant literal plus the referenced model's (stripped) fields.
    fn discriminated_union(
        &mut self,
        name: &str,
        module: &str,
        schema: &Schema,
        docstring: Option<String>,
    ) -> Option<DiscriminatedUnion> {
        let variants = schema.one_of.as_ref().or(schema.any_of.as_ref())?;
        let property_name = schema
            .discriminator
            .as_ref()
            .map(|disc| disc.property_name.as_str())
            .filter(|property| !property.is_empty())
            .map(str::to_string)
            .or_else(|| inferred_discriminant_property(schema, self.schemas))?;
        let mapping = schema
            .discriminator
            .as_ref()
            .map(|disc| &disc.mapping)
            .filter(|mapping| !mapping.is_empty());
        if mapping.is_none() {
            let mut members = Vec::new();
            let mut variant_targets = Vec::new();
            for variant in variants {
                let (target, target_name) = if let Some(reference) = &variant.reference {
                    (
                        resolve_ref_from_schemas(self.schemas, reference)?,
                        Some(ref_to_class(reference)),
                    )
                } else {
                    (variant, None)
                };
                let value = target
                    .properties
                    .get(&property_name)
                    .and_then(discriminant_value)?;
                let variant_name = format!("{name}{}", naming::class_name(&value));
                if let Some(target_name) = target_name {
                    variant_targets.push(target_name);
                } else {
                    let mut standalone = variant.clone();
                    standalone.properties.shift_remove(&property_name);
                    self.add_object(
                        &variant_name,
                        naming::module_name(&variant_name),
                        &standalone,
                        None,
                    );
                }
                members.push(UnionMember {
                    class_name: format!("{name}_{}", naming::class_name(&value)),
                    discriminant: value,
                    fields: member_fields(target, &property_name, self.schemas),
                    docstring: variant
                        .reference
                        .is_none()
                        .then(|| docstring.clone())
                        .flatten(),
                });
            }
            return Some(DiscriminatedUnion {
                name: name.to_string(),
                module: module.to_string(),
                discriminant_property: property_name,
                members,
                variant_targets,
                docstring,
            });
        }
        let mut members = Vec::new();
        let mut variant_targets = Vec::new();
        for (value, reference) in mapping? {
            let target_key = reference.rsplit('/').next().unwrap_or(reference);
            let target = self.schemas.get(target_key)?;
            members.push(UnionMember {
                // Fern names the wrapper after the discriminant *value*
                // (`Node_And`), not the referenced schema (`AndNode`) — the two
                // coincide only when the mapping key equals the schema name.
                class_name: format!("{name}_{}", naming::class_name(value)),
                discriminant: value.clone(),
                fields: member_fields(target, &property_name, self.schemas),
                docstring: docstring.clone(),
            });
            variant_targets.push(naming::class_name(target_key));
        }
        Some(DiscriminatedUnion {
            name: name.to_string(),
            module: module.to_string(),
            discriminant_property: property_name,
            members,
            variant_targets,
            docstring,
        })
    }

    /// The type of a property, hoisting an inline string enum to a named
    /// `enum.Enum` class `{Owner}{Prop}` (as Fern does for `typesAnimal`).
    fn field_type_ref(&mut self, owner: &str, prop: &str, prop_schema: &Schema) -> TypeRef {
        // Fern preserves the unknown schema's intrinsic `Optional[Any]` for a
        // handful of semantic catch-all fields. Property absence then adds the
        // outer `Optional`; ordinary unknown fields stay `Any` here so they do
        // not become double-optional.
        if matches!(prop, "metadata" | "value") && is_unknown(prop_schema) {
            return TypeRef::Optional(Box::new(TypeRef::Primitive(Prim::Any)));
        }
        // AWS-style OpenAPI documents commonly decorate a property reference as
        // `allOf: [$ref, { description }]`. Fern treats that as a use-site copy:
        // scalar/collection aliases resolve to their underlying type, while enums
        // and object models are cloned under `{Owner}{Property}` so the contextual
        // description belongs to the generated type. It is not inheritance.
        if let Some((reference, description)) = described_all_of_ref(prop_schema) {
            if let Some(target) = resolve_ref_from_schemas(self.schemas, reference).cloned() {
                let name = format!("{owner}{}", naming::class_name(prop));
                if let Some(values) = string_enum_values(&target) {
                    self.types.push(TypeDecl::Enum(build_enum(
                        &name,
                        values,
                        clean_doc(description),
                    )));
                    return TypeRef::Named(name);
                }
                if !is_map(&target)
                    && !is_bare_object(&target)
                    && (!target.properties.is_empty()
                        || target.all_of.is_some()
                        || is_object_type(&target))
                {
                    self.add_object(
                        &name,
                        naming::module_name(&name),
                        &target,
                        clean_doc(description),
                    );
                    return TypeRef::Named(name);
                }
                return full_type_ref_resolved(&target, self.schemas);
            }
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
            // An inline object with declared structure — including an explicitly
            // empty `properties: {}` — hoists to its own named model
            // `{Owner}{Prop}` (Fern: `Meta.cursors` → `MetaCursors`), rather than
            // degrading to `typing.Any`. A bare `type: object` map (no properties
            // declaration) is left to `base_type_ref`.
            if is_inline_struct(prop_schema) && single_all_of_ref(prop_schema).is_none() {
                let name = format!("{owner}{}", naming::class_name(prop));
                let module = naming::module_name(&name);
                self.add_object(
                    &name,
                    module,
                    prop_schema,
                    prop_schema
                        .all_of
                        .is_none()
                        .then(|| clean_doc(prop_schema.description.as_deref()))
                        .flatten(),
                );
                return TypeRef::Named(name);
            }
            // An array of inline objects hoists the item to `{Owner}{Prop}Item` and
            // types the property as a sequence of it (Fern: `Pipeline.stages` →
            // `List[PipelineStagesItem]`).
            if prop_schema.ty.as_ref().and_then(|t| t.primary()) == Some("array") {
                if let Some(items) = &prop_schema.items {
                    let resolved_items = items.reference.as_deref().and_then(|reference| {
                        reference
                            .starts_with("#/components/schemas/")
                            .then(|| resolve_schema_pointer(self.schemas, reference))
                            .flatten()
                    });
                    // A nullable component used as an array item remains nullable in
                    // the collection (`List[Optional[Language]]`), even though the
                    // `$ref` node itself carries no `nullable` flag.
                    if let (Some(reference), Some(resolved)) = (
                        items.reference.as_deref(),
                        items.reference.as_deref().and_then(|reference| {
                            resolve_ref_from_schemas(self.schemas, reference)
                        }),
                    ) {
                        if is_optional(resolved) {
                            let item = Box::new(TypeRef::Optional(Box::new(TypeRef::Named(
                                ref_to_class(reference),
                            ))));
                            return if array_uses_set(prop_schema) {
                                TypeRef::Set(item)
                            } else {
                                TypeRef::List(item)
                            };
                        }
                    }
                    let items = resolved_items.unwrap_or(items);
                    if let Some(values) = string_enum_values(items) {
                        let name = format!("{owner}{}Item", naming::class_name(prop));
                        self.types.push(TypeDecl::Enum(build_enum(
                            &name,
                            values,
                            clean_doc(items.description.as_deref()),
                        )));
                        return TypeRef::List(Box::new(TypeRef::Named(name)));
                    }
                    if let Some(members) = items.one_of.as_ref().or(items.any_of.as_ref()) {
                        let name = format!("{owner}{}Item", naming::class_name(prop));
                        let module = naming::module_name(&name);
                        if let Some(decl) = self.discriminated_union(
                            &name,
                            &module,
                            items,
                            clean_doc(items.description.as_deref()),
                        ) {
                            self.types.push(TypeDecl::DiscriminatedUnion(decl));
                            return TypeRef::List(Box::new(TypeRef::Named(name)));
                        }
                        let variants = members
                            .iter()
                            .enumerate()
                            .map(|(index, variant)| {
                                self.variant_ref(&name, index, variant, members)
                            })
                            .collect();
                        self.push_alias(
                            &name,
                            module,
                            TypeRef::Union(variants),
                            clean_doc(items.description.as_deref()),
                        );
                        return TypeRef::List(Box::new(TypeRef::Named(name)));
                    }
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
                        return if array_uses_set(prop_schema) {
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
                    let name = format!("{owner}{}", naming::class_name(prop));
                    let mut variants: Vec<TypeRef> = members
                        .iter()
                        .enumerate()
                        .map(|(index, m)| {
                            if is_inline_object(m) {
                                return self.variant_ref(&name, index, m, members);
                            }
                            if m.ty.as_ref().and_then(|ty| ty.primary()) == Some("array") {
                                if let Some(item_members) = m.items.as_deref().and_then(|items| {
                                    items.any_of.as_ref().or(items.one_of.as_ref())
                                }) {
                                    let item_name = format!("{name}{}Item", ordinal_word(index));
                                    let item_variants = item_members
                                        .iter()
                                        .enumerate()
                                        .map(|(item_index, variant)| {
                                            self.variant_ref(
                                                &item_name,
                                                item_index,
                                                variant,
                                                item_members,
                                            )
                                        })
                                        .collect();
                                    self.push_alias(
                                        &item_name,
                                        naming::module_name(&item_name),
                                        TypeRef::Union(item_variants),
                                        clean_doc(
                                            m.items
                                                .as_deref()
                                                .and_then(|items| items.description.as_deref()),
                                        ),
                                    );
                                    return TypeRef::List(Box::new(TypeRef::Named(item_name)));
                                }
                            }
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
                    variants.dedup();
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
    fn variant_ref(
        &mut self,
        parent: &str,
        index: usize,
        variant: &Schema,
        siblings: &[Schema],
    ) -> TypeRef {
        if let Some(reference) = &variant.reference {
            return TypeRef::Named(ref_to_class(reference));
        }
        if is_inline_object(variant) {
            let name = variant_class_name(parent, index, variant, siblings);
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

fn variant_class_name(parent: &str, index: usize, variant: &Schema, siblings: &[Schema]) -> String {
    let shared_first = variant.properties.keys().next().filter(|candidate| {
        siblings
            .iter()
            .all(|sibling| sibling.properties.contains_key(*candidate))
    });
    let unique = variant
        .properties
        .values()
        .find_map(|property| {
            string_enum_values(property)
                .filter(|values| values.len() == 1)
                .and_then(|values| values.into_iter().next())
        })
        .or_else(|| {
            variant
                .properties
                .keys()
                .find(|candidate| {
                    candidate.as_str() != "resource_list"
                        && siblings
                            .iter()
                            .filter(|sibling| sibling.properties.contains_key(*candidate))
                            .count()
                            == 1
                })
                .cloned()
        });
    let unique = if siblings.len() > 2
        && index + 1 == siblings.len()
        && shared_first.map(String::as_str) == Some("assets")
        && unique
            .as_deref()
            .is_some_and(|name| name.starts_with("assets"))
    {
        Some("assets".to_string())
    } else {
        unique
    };
    let fallback = shared_first.and_then(|shared| {
        if shared == "portfolios" {
            return None;
        }
        if shared == "assets" {
            let same_shape_precedes = siblings[..index]
                .iter()
                .any(|sibling| sibling.properties.keys().eq(variant.properties.keys()));
            return same_shape_precedes.then(|| shared.clone());
        }
        Some(shared.clone())
    });
    let suffix = unique
        .or(fallback)
        .or_else(|| {
            variant
                .properties
                .keys()
                .next()
                .filter(|name| name.as_str() == "resource_list")
                .cloned()
        })
        .map_or_else(
            || ordinal_word(index).to_string(),
            |name| naming::class_name(&name),
        );
    format!("{parent}{suffix}")
}

fn resolve_schema_pointer<'a>(
    schemas: &'a IndexMap<String, Schema>,
    reference: &str,
) -> Option<&'a Schema> {
    let mut parts = reference.strip_prefix("#/components/schemas/")?.split('/');
    let mut schema = schemas.get(parts.next()?)?;
    let mut next = Some(parts.next()?);
    while let Some(part) = next {
        schema = match part {
            "allOf" => schema
                .all_of
                .as_ref()?
                .get(parts.next()?.parse::<usize>().ok()?)?,
            "oneOf" => schema
                .one_of
                .as_ref()?
                .get(parts.next()?.parse::<usize>().ok()?)?,
            "anyOf" => schema
                .any_of
                .as_ref()?
                .get(parts.next()?.parse::<usize>().ok()?)?,
            "properties" => schema.properties.get(parts.next()?)?,
            "items" => schema.items.as_deref()?,
            _ => return None,
        };
        next = parts.next();
    }
    Some(schema)
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
    schema.reference.is_none() && (!schema.properties.is_empty() || schema.all_of.is_some())
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

/// Whether an object example describes the shape of arbitrary values rather than
/// providing a concrete object instance. OpenAPI documents sometimes use
/// `{ "field": { "type": ... } }` as an example for a free-form schema; Fern
/// keeps those declarations as map aliases instead of coining empty models.
fn example_is_schema_definition(example: &serde_json::Value) -> bool {
    let Some(values) = example.as_object() else {
        return false;
    };
    !values.is_empty()
        && values.values().all(|value| {
            value.as_object().is_some_and(|definition| {
                ["type", "$ref", "properties", "allOf", "oneOf", "anyOf"]
                    .iter()
                    .any(|key| definition.contains_key(*key))
            })
        })
}

/// An inline (not `$ref`) object with *declared structure* — properties (including
/// an explicitly empty, non-map `properties: {}`), an `allOf`, or a closed-object
/// marker. Unlike [`is_inline_object`] this excludes a bare `type: object` map
/// (which Fern renders as a `Dict`, not a hoisted model), so it is the test for
/// hoisting an inline request/response body into a named type.
fn is_inline_struct(schema: &Schema) -> bool {
    schema.reference.is_none()
        && (!schema.properties.is_empty()
            || schema.all_of.is_some()
            || (is_object_type(schema)
                && schema.properties.declared()
                && schema.additional_properties.is_none())
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
        optional_type_ref(base)
    } else {
        base
    }
}

fn full_type_ref_resolved(schema: &Schema, schemas: &IndexMap<String, Schema>) -> TypeRef {
    let base = base_type_ref(schema);
    if schema_accepts_none(schema, schemas) {
        optional_type_ref(base)
    } else {
        base
    }
}

fn optional_type_ref(base: TypeRef) -> TypeRef {
    match base {
        TypeRef::Optional(_) => base,
        TypeRef::Union(mut variants) if !variants.is_empty() => {
            let last = variants.pop().expect("non-empty union checked above");
            variants.push(TypeRef::Optional(Box::new(last)));
            TypeRef::Union(variants)
        }
        other => TypeRef::Optional(Box::new(other)),
    }
}

fn schema_accepts_none(schema: &Schema, schemas: &IndexMap<String, Schema>) -> bool {
    is_optional(schema) || referenced_schema_accepts_none(schema, schemas)
}

fn referenced_schema_accepts_none(schema: &Schema, schemas: &IndexMap<String, Schema>) -> bool {
    let mut current = schema;
    let mut seen = std::collections::HashSet::new();
    loop {
        let Some(reference) = current.reference.as_deref() else {
            return false;
        };
        if !seen.insert(reference) {
            return false;
        }
        let Some(target) = resolve_ref_from_schemas(schemas, reference) else {
            return false;
        };
        if is_explicitly_nullable(target) {
            return true;
        }
        current = target;
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
        return if reference.starts_with("#/components/schemas/") {
            TypeRef::Named(ref_to_class(reference))
        } else {
            TypeRef::Optional(Box::new(TypeRef::Primitive(Prim::Any)))
        };
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
                if schema.nullable == Some(true) || is_unknown(value) {
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
                        array_item_type_ref(i)
                    }
                },
            );
            if array_uses_set(schema) {
                TypeRef::Set(Box::new(item))
            } else {
                TypeRef::List(Box::new(item))
            }
        }
        Some("object") => TypeRef::Primitive(Prim::Any),
        _ => TypeRef::Primitive(Prim::Any),
    }
}

/// Fern keeps an array nested inside another array as a list even when the inner
/// schema declares `uniqueItems`; only a directly modeled array becomes a set.
fn array_item_type_ref(schema: &Schema) -> TypeRef {
    match full_type_ref(schema) {
        TypeRef::Set(item) => TypeRef::List(item),
        TypeRef::Optional(inner) => match *inner {
            TypeRef::Set(item) => TypeRef::Optional(Box::new(TypeRef::List(item))),
            other => TypeRef::Optional(Box::new(other)),
        },
        other => other,
    }
}

/// Fern's OpenAPI importer keeps arrays as lists even when `uniqueItems` is true;
/// the constraint does not change the generated Python collection type.
fn array_uses_set(_schema: &Schema) -> bool {
    false
}

fn single_all_of_ref(schema: &Schema) -> Option<&str> {
    let members = schema.all_of.as_ref()?;
    match members.as_slice() {
        [member] => member.reference.as_deref(),
        _ => None,
    }
}

/// A property-level `allOf` that adds annotations to exactly one `$ref` without
/// adding any shape of its own. Swagger-generated AWS specs use this form for
/// nearly every documented property.
fn described_all_of_ref(schema: &Schema) -> Option<(&str, Option<&str>)> {
    let members = schema.all_of.as_ref()?;
    if members.len() < 2 {
        return None;
    }
    let mut reference = None;
    let mut description = schema.description.as_deref();
    for member in members {
        if let Some(candidate) = member.reference.as_deref() {
            if reference.replace(candidate).is_some() {
                return None;
            }
        } else if is_unknown(member) {
            description = description.or(member.description.as_deref());
        } else {
            return None;
        }
    }
    reference.map(|reference| (reference, description))
}

fn property_description(schema: &Schema) -> Option<&str> {
    schema
        .description
        .as_deref()
        .or_else(|| described_all_of_ref(schema).and_then(|(_, description)| description))
}

/// Is a schema optional? A schema is optional when it is explicitly `nullable`
/// or when it is an unknown (untyped) schema, which Fern always renders as
/// `Optional[Any]`.
fn is_optional(schema: &Schema) -> bool {
    is_explicitly_nullable(schema) || is_unknown(schema)
}

fn is_explicitly_nullable(schema: &Schema) -> bool {
    schema.nullable == Some(true)
        || matches!(
            schema.ty.as_ref(),
            Some(TypeField::Multiple(types)) if types.iter().any(|ty| ty == "null")
        )
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
    let mut types = Vec::new();
    for variant in variants {
        let ty = base_type_ref(variant);
        if !types.contains(&ty) {
            types.push(ty);
        }
    }
    Some(types)
}

/// Resolve a `$ref` to the class name it points at.
fn ref_to_class(reference: &str) -> String {
    let Some(pointer) = reference.strip_prefix("#/components/schemas/") else {
        return naming::class_name(reference.rsplit('/').next().unwrap_or(reference));
    };
    let parts: Vec<&str> = pointer.split('/').collect();
    let mut name = naming::class_name(parts[0]);
    let mut index = 1;
    while index < parts.len() {
        match parts[index] {
            "properties" if index + 1 < parts.len() => {
                name.push_str(&naming::class_name(parts[index + 1]));
                index += 2;
            }
            "items" => {
                name.push_str("Item");
                index += 1;
            }
            "allOf" | "oneOf" | "anyOf" => index += 2,
            _ => index += 1,
        }
    }
    name
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
    let text = desc?.trim_end();
    if text.trim_start().is_empty() {
        None
    } else {
        // A single intentional leading space in legacy specs is preserved by
        // Fern, while ordinary multi-space indentation is trimmed. Tabs in prose
        // are expanded to four spaces by its importer.
        let text = if text.starts_with(' ')
            && text
                .get(1..)
                .is_some_and(|rest| rest.chars().next().is_some_and(|ch| !ch.is_whitespace()))
        {
            text
        } else {
            text.trim_start()
        };
        Some(text.replace('\t', "    "))
    }
}

/// Operation descriptions preserve `description: ""` as an empty summary slot in
/// method docs, while still trimming non-empty prose like [`clean_doc`].
fn operation_doc(desc: Option<&str>) -> Option<String> {
    let text = desc?;
    let trimmed = text.trim_end();
    if trimmed.trim_start().is_empty() {
        Some(String::new())
    } else {
        let trimmed = if trimmed.starts_with(' ')
            && trimmed
                .get(1..)
                .is_some_and(|rest| rest.chars().next().is_some_and(|ch| !ch.is_whitespace()))
        {
            trimmed
        } else {
            trimmed.trim_start()
        };
        Some(trimmed.replace('\t', "    "))
    }
}

/// Whitespace Fern retains at the end of an operation description in
/// `reference.md`. Terminal line endings are importer formatting, but spaces
/// immediately before the final line ending are meaningful Markdown, and a
/// terminal blank paragraph is preserved as one newline.
fn reference_description_suffix(description: &str) -> String {
    let without_line_endings = description.trim_end_matches(['\r', '\n']);
    let spaces = &without_line_endings[without_line_endings.trim_end_matches(' ').len()..];
    if !spaces.is_empty() {
        spaces.to_string()
    } else if description.ends_with("\n\n") || description.ends_with("\r\n\r\n") {
        "\n".to_string()
    } else {
        String::new()
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
        array_item_type_ref, auth_model, base_type_ref, build_endpoint, build_enum,
        described_all_of_ref, endpoint_module, environment_model, extensible_enum,
        full_type_ref_resolved, global_headers, int_prim, method_from_grouped_id,
        module_from_grouped_id, module_identifier, oauth_scope_enum, optional_type_ref,
        parameter_example, path_group, property_description, query_parameter_example, ref_to_class,
        request_and_response_refs_match, request_schema_use_count, resolve_request_body,
        resolve_schema_pointer, response_schema, scalar_body, success_response_entry,
        synthesized_method_name, title_from_tag, variant_class_name, Auth, Builder, InlineHoister,
        Prim, RequestBody, TypeDecl, TypeRef,
    };
    use crate::openapi::{OpenApi, Operation, Parameter, Response, Schema, TypeField};

    #[test]
    fn integer_formats_select_distinct_ir_primitives() {
        let schema = |format: &str| Schema {
            ty: Some(TypeField::Single("integer".to_string())),
            format: Some(format.to_string()),
            ..Schema::default()
        };
        assert_eq!(int_prim(&schema("int64")), Prim::Long);
        assert_eq!(int_prim(&schema("uint32")), Prim::Int);
        assert_eq!(int_prim(&schema("int32")), Prim::Int);
    }

    #[test]
    fn build_enum_omits_duplicate_values_and_disambiguates_colliding_names() {
        // Fern omits exact duplicate wire values. Distinct values that sanitize to
        // the same identifier still need unique members/`visit` params.
        let e = build_enum(
            "Color",
            vec![
                "a-b".to_string(),
                "a-b".to_string(),
                "a b".to_string(),
                "a.b".to_string(),
            ],
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
    fn server_description_repeating_api_title_defaults_to_default_environment() {
        let doc: crate::openapi::OpenApi = serde_json::from_value(serde_json::json!({
            "info": { "title": "Payroll API" },
            "servers": [{
                "description": "Payroll API",
                "url": "https://api.example.com"
            }]
        }))
        .expect("document deserializes");
        let env = environment_model(&doc, "FernApi").expect("server yields environment");
        assert_eq!(env.member.0, "DEFAULT");
        assert_eq!(env.default_ref(), "FernApiEnvironment.DEFAULT");
    }

    #[test]
    fn parameter_example_rejects_a_value_with_the_wrong_scalar_kind() {
        let doc: OpenApi =
            serde_json::from_value(serde_json::json!({})).expect("document deserializes");
        let mut parameter = Parameter {
            schema: Some(Schema {
                ty: Some(TypeField::Single("string".to_string())),
                ..Schema::default()
            }),
            example: Some(serde_json::json!(40022701955_u64)),
            ..Parameter::default()
        };
        assert_eq!(parameter_example(&doc, &parameter), None);

        parameter.example = Some(serde_json::json!("OSF0001AU"));
        assert_eq!(
            parameter_example(&doc, &parameter).as_deref(),
            Some("\"OSF0001AU\"")
        );

        parameter.example = None;
        parameter.schema.as_mut().expect("schema").min_length = Some(1);
        assert_eq!(parameter_example(&doc, &parameter), None);
        assert_eq!(
            query_parameter_example(&doc, &parameter).as_deref(),
            Some("\"x\"")
        );
        parameter.schema.as_mut().expect("schema").min_length = Some(10);
        assert_eq!(
            query_parameter_example(&doc, &parameter).as_deref(),
            Some("\"strawberry\"")
        );
    }

    #[test]
    fn server_variable_defaults_are_percent_encoded_before_substitution() {
        let doc: crate::openapi::OpenApi = serde_json::from_value(serde_json::json!({
            "servers": [{
                "url": "https://api.example.com/{basePath}",
                "variables": { "basePath": { "default": "/api/v1" } }
            }]
        }))
        .expect("document deserializes");
        let env = environment_model(&doc, "FernApi").expect("server yields environment");
        assert_eq!(env.member.1, "https://api.example.com/%2Fapi%2Fv1");
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
    fn header_api_key_after_oauth_is_an_additional_global_header() {
        // Deserialize directly from text so the security-scheme declaration order
        // reaches the IndexMap (a serde_json::Value map is key-sorted by default).
        let doc: crate::openapi::OpenApi = serde_json::from_str(
            r#"{
                "components": {
                    "securitySchemes": {
                        "oauth2": {
                            "type": "oauth2",
                            "flows": { "authorizationCode": { "scopes": {} } }
                        },
                        "clientSecret": {
                            "type": "apiKey",
                            "in": "header",
                            "name": "Authorization"
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
            }"#,
        )
        .expect("document deserializes");

        let headers = global_headers(&doc);
        assert_eq!(headers.len(), 1);
        assert_eq!(headers[0].py_name, "authorization");
        assert_eq!(headers[0].wire_name, "Authorization");
        assert!(headers[0].required);
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
                                    "Public": "",
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
                ("PUBLIC", "Public", Some("")),
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

        // A lowercase tag does not infer camel-case word boundaries it did not
        // declare: Otoroshi keeps both operations in `apikeys` and retains the
        // full `api_keys...` method name.
        let o = op("apiKeysFromGroup", "apikeys");
        assert_eq!(endpoint_module(&o, "/x"), "apikeys");
        assert_eq!(endpoint_method_name(&o, "GET", "/x"), "api_keys_from_group");
        let o = op("apiKeys", "apikeys");
        assert_eq!(endpoint_module(&o, "/x"), "apikeys");
        assert_eq!(endpoint_method_name(&o, "GET", "/x"), "api_keys");

        let o = op("CatalogInfo", "Catalog");
        assert_eq!(endpoint_module(&o, "/v2/catalog/info"), "catalog");
        assert_eq!(
            endpoint_method_name(&o, "GET", "/v2/catalog/info"),
            "catalog_info"
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
    fn tag_titles_distinguish_declared_labels_from_derived_names() {
        let declared: OpenApi = serde_json::from_value(serde_json::json!({
            "tags": [{ "name": "lower-case" }]
        }))
        .expect("document deserializes");
        assert_eq!(title_from_tag(&declared, "lower-case"), "lower-case");

        let undeclared: OpenApi =
            serde_json::from_value(serde_json::json!({})).expect("document deserializes");
        assert_eq!(title_from_tag(&undeclared, "lower-case"), "LowerCase");
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
            building_types: Default::default(),
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
            "/widgets/{first}/{second}.json",
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
    fn synthesized_names_use_method_and_full_route() {
        // Fern's fallback naming when both operationId and summary are absent.
        assert_eq!(synthesized_method_name("GET", "/widgets"), "get_widgets");
        assert_eq!(
            synthesized_method_name("GET", "/widgets/{id}"),
            "get_widgets_id"
        );
        assert_eq!(synthesized_method_name("POST", "/widgets"), "post_widgets");
        assert_eq!(
            synthesized_method_name("DELETE", "/widgets/{id}"),
            "delete_widgets_id"
        );
        assert_eq!(
            synthesized_method_name("PUT", "/widgets/{id}"),
            "put_widgets_id"
        );
    }

    #[test]
    fn duplicate_endpoint_replaces_contents_in_first_seen_position() {
        let doc: OpenApi = serde_json::from_value(serde_json::json!({
            "paths": {
                "/a-first": {
                    "post": {
                        "tags": ["widgets"],
                        "summary": "Same method",
                        "responses": { "200": { "description": "OK" } }
                    }
                },
                "/b-between": {
                    "get": {
                        "tags": ["widgets"],
                        "summary": "Between",
                        "responses": { "200": { "description": "OK" } }
                    }
                },
                "/c-last": {
                    "post": {
                        "tags": ["widgets"],
                        "summary": "Same method",
                        "responses": { "200": { "description": "OK" } }
                    }
                }
            }
        }))
        .expect("document deserializes");

        let (endpoints, _) = super::endpoints(&doc, &[], &[]);
        assert_eq!(
            endpoints
                .iter()
                .map(|endpoint| endpoint.path.as_str())
                .collect::<Vec<_>>(),
            ["/c-last", "/b-between"]
        );
    }

    fn operation(value: serde_json::Value) -> Operation {
        serde_json::from_value(value).expect("operation deserializes")
    }

    fn schema(value: serde_json::Value) -> Schema {
        serde_json::from_value(value).expect("schema deserializes")
    }

    #[test]
    fn response_helpers_cover_media_precedence_and_empty_successes() {
        let text = operation(serde_json::json!({
            "responses": {
                "200": { "content": { "text/plain": { "schema": { "type": "string" } } } }
            }
        }));
        assert!(super::has_text_response(&text));
        assert!(!super::has_bodyless_success(&text));
        assert_eq!(success_response_entry(&text).unwrap().content.len(), 1);

        for media_type in ["application/json", "*/*"] {
            let mixed = operation(serde_json::json!({
                "responses": {
                    "201": { "content": {
                        "text/plain": { "schema": { "type": "string" } },
                        media_type: { "schema": { "type": "integer" } }
                    } }
                }
            }));
            assert!(!super::has_text_response(&mixed));
            assert!(!super::has_bodyless_success(&mixed));
        }

        let bodyless = operation(serde_json::json!({
            "responses": {
                "199": { "content": {} },
                "204": { "content": {} },
                "400": { "content": { "application/json": { "schema": { "type": "string" } } } }
            }
        }));
        assert!(super::has_bodyless_success(&bodyless));
        assert!(!super::has_text_response(&bodyless));

        let default_only = operation(serde_json::json!({
            "responses": { "default": { "content": {} } }
        }));
        assert!(std::ptr::eq(
            success_response_entry(&default_only).unwrap(),
            default_only.responses.get("default").unwrap()
        ));
        let none = operation(serde_json::json!({ "responses": { "404": {} } }));
        assert!(success_response_entry(&none).is_none());
        assert!(!super::has_bodyless_success(&none));
    }

    #[test]
    fn response_schema_checks_each_supported_media_and_missing_schema() {
        let response = |content: serde_json::Value| -> Response {
            serde_json::from_value(serde_json::json!({ "content": content }))
                .expect("response deserializes")
        };
        for media_type in ["application/json", "application/jwt", "*/*", "text/csv"] {
            let response = response(serde_json::json!({
                media_type: { "schema": { "type": "string", "title": media_type } }
            }));
            assert_eq!(
                response_schema(&response).unwrap().title.as_deref(),
                Some(media_type)
            );
        }
        let precedence = response(serde_json::json!({
            "text/csv": { "schema": { "title": "fallback" } },
            "application/jwt": { "schema": { "title": "jwt" } },
            "application/json": { "schema": { "title": "json" } }
        }));
        assert_eq!(
            response_schema(&precedence).unwrap().title.as_deref(),
            Some("json")
        );
        assert!(response_schema(&response(serde_json::json!({}))).is_none());
        assert!(response_schema(&response(serde_json::json!({
            "application/json": {}
        })))
        .is_none());
    }

    #[test]
    fn request_reference_helpers_cover_absent_mismatched_and_reused_schemas() {
        let reference = "#/components/schemas/Input";
        let doc: OpenApi = serde_json::from_value(serde_json::json!({
            "paths": {
                "/one": { "post": {
                    "requestBody": { "content": { "application/json": {
                        "schema": { "$ref": reference }
                    } } },
                    "responses": { "200": {} }
                } },
                "/two": { "put": {
                    "requestBody": { "content": {
                        "text/plain": {},
                        "application/json": { "schema": { "$ref": reference } }
                    } },
                    "responses": { "200": {} }
                } },
                "/other": { "post": {
                    "requestBody": { "content": { "application/json": {
                        "schema": { "$ref": "#/components/schemas/Other" }
                    } } },
                    "responses": { "200": {} }
                } },
                "/empty": { "post": { "responses": { "204": {} } } }
            }
        }))
        .expect("document deserializes");
        assert_eq!(request_schema_use_count(&doc, reference), 2);
        assert_eq!(
            request_schema_use_count(&doc, "#/components/schemas/Missing"),
            0
        );

        let matching = operation(serde_json::json!({
            "requestBody": { "content": { "application/json": {
                "schema": { "$ref": reference }
            } } },
            "responses": { "200": { "content": { "application/json": {
                "schema": { "$ref": reference }
            } } } }
        }));
        assert!(request_and_response_refs_match(&matching));
        let mismatched = operation(serde_json::json!({
            "requestBody": { "content": { "application/json": {
                "schema": { "$ref": reference }
            } } },
            "responses": { "200": { "content": { "application/json": {
                "schema": { "$ref": "#/components/schemas/Other" }
            } } } }
        }));
        assert!(!request_and_response_refs_match(&mismatched));
        assert!(!request_and_response_refs_match(&operation(
            serde_json::json!({
                "responses": { "200": {} }
            })
        )));
    }

    #[test]
    fn schema_pointer_resolution_covers_every_segment_and_failure() {
        let doc: OpenApi = serde_json::from_value(serde_json::json!({
            "components": { "schemas": {
                "Root": {
                    "allOf": [{ "title": "all" }],
                    "oneOf": [{ "title": "one" }],
                    "anyOf": [{ "title": "any" }],
                    "properties": { "field": { "title": "property" } },
                    "items": { "title": "item" }
                },
                "Plain": { "type": "string" }
            } }
        }))
        .expect("document deserializes");
        let schemas = &doc.components.schemas;
        for (suffix, title) in [
            ("allOf/0", "all"),
            ("oneOf/0", "one"),
            ("anyOf/0", "any"),
            ("properties/field", "property"),
            ("items", "item"),
        ] {
            assert_eq!(
                resolve_schema_pointer(schemas, &format!("#/components/schemas/Root/{suffix}"))
                    .unwrap()
                    .title
                    .as_deref(),
                Some(title)
            );
        }
        for reference in [
            "Root",
            "#/components/schemas/Root",
            "#/components/schemas/Missing/items",
            "#/components/schemas/Root/unknown",
            "#/components/schemas/Root/allOf",
            "#/components/schemas/Root/allOf/nope",
            "#/components/schemas/Root/allOf/9",
            "#/components/schemas/Root/properties/missing",
            "#/components/schemas/Root/items/properties/missing",
            "#/components/schemas/Plain/allOf/0",
            "#/components/schemas/Plain/oneOf/0",
            "#/components/schemas/Plain/anyOf/0",
            "#/components/schemas/Plain/items",
        ] {
            assert!(
                resolve_schema_pointer(schemas, reference).is_none(),
                "{reference}"
            );
        }
    }

    #[test]
    fn schema_definition_examples_require_nonempty_schema_shaped_objects() {
        for value in [
            serde_json::json!(null),
            serde_json::json!([]),
            serde_json::json!({}),
            serde_json::json!({ "field": "value" }),
            serde_json::json!({ "field": {} }),
            serde_json::json!({ "field": { "description": "only metadata" } }),
            serde_json::json!({ "good": { "type": "string" }, "bad": {} }),
        ] {
            assert!(!super::example_is_schema_definition(&value), "{value}");
        }
        for keyword in ["type", "$ref", "properties", "allOf", "oneOf", "anyOf"] {
            let value = serde_json::json!({ "field": { keyword: {} } });
            assert!(super::example_is_schema_definition(&value), "{keyword}");
        }
    }

    #[test]
    fn variant_names_cover_enum_unique_shared_first_and_ordinal_fallbacks() {
        let enum_variant = schema(serde_json::json!({
            "properties": { "kind": { "type": "string", "enum": ["cat"] } }
        }));
        assert_eq!(variant_class_name("Pet", 0, &enum_variant, &[]), "PetCat");

        let unique = schema(serde_json::json!({
            "properties": { "resource_list": { "type": "string" }, "whiskers": { "type": "integer" } }
        }));
        let sibling = schema(serde_json::json!({
            "properties": { "resource_list": { "type": "string" }, "bark": { "type": "boolean" } }
        }));
        assert_eq!(
            variant_class_name("Pet", 0, &unique, &[unique.clone(), sibling]),
            "PetWhiskers"
        );

        let shared = schema(serde_json::json!({
            "properties": { "common": { "type": "string" } }
        }));
        assert_eq!(
            variant_class_name("Pet", 0, &shared, &[shared.clone(), shared.clone()]),
            "PetCommon"
        );
        assert_eq!(
            variant_class_name("Pet", 1, &Schema::default(), &[]),
            "PetOne"
        );
        let resource_only = schema(serde_json::json!({
            "properties": { "resource_list": { "type": "string" } }
        }));
        assert_eq!(
            variant_class_name(
                "Pet",
                0,
                &resource_only,
                &[resource_only.clone(), Schema::default()]
            ),
            "PetResourceList"
        );
    }

    #[test]
    fn variant_ref_covers_references_inline_objects_and_scalar_fallback() {
        let schemas = indexmap::IndexMap::new();
        let mut builder = Builder {
            types: Vec::new(),
            schemas: &schemas,
            strip_discriminant: std::collections::HashMap::new(),
            building_types: std::collections::HashSet::new(),
        };
        let referenced = schema(serde_json::json!({ "$ref": "#/components/schemas/Pet" }));
        assert_eq!(
            builder.variant_ref("Animal", 0, &referenced, &[]),
            TypeRef::Named("Pet".to_string())
        );
        assert!(builder.types.is_empty());

        let inline = schema(serde_json::json!({
            "description": "A cat.",
            "properties": { "kind": { "type": "string", "enum": ["cat"] } }
        }));
        assert_eq!(
            builder.variant_ref("Animal", 0, &inline, std::slice::from_ref(&inline)),
            TypeRef::Named("AnimalCat".to_string())
        );
        assert!(builder.types.iter().any(
            |declaration| matches!(declaration, TypeDecl::Object(object) if object.name == "AnimalCat")
        ));
        let emitted = builder.types.len();

        let scalar = schema(serde_json::json!({ "type": "integer", "format": "int64" }));
        assert_eq!(
            builder.variant_ref("Animal", 1, &scalar, &[]),
            TypeRef::Primitive(Prim::Long)
        );
        assert_eq!(builder.types.len(), emitted);
    }

    #[test]
    fn builder_hoists_top_level_inline_array_items() {
        let schemas = indexmap::IndexMap::new();
        let mut builder = Builder {
            types: Vec::new(),
            schemas: &schemas,
            strip_discriminant: std::collections::HashMap::new(),
            building_types: std::collections::HashSet::new(),
        };
        let array = schema(serde_json::json!({
            "type": "array",
            "items": {
                "description": "One result.",
                "type": "object",
                "properties": { "id": { "type": "string" } }
            }
        }));
        builder.add_named("Results", &array);
        assert!(builder.types.iter().any(
            |declaration| matches!(declaration, TypeDecl::Object(object) if object.name == "ResultsItem")
        ));
        assert!(builder.types.iter().any(|declaration| matches!(
            declaration,
            TypeDecl::Alias(alias)
                if alias.name == "Results"
                    && alias.target == TypeRef::List(Box::new(TypeRef::Named("ResultsItem".to_string())))
        )));
    }

    #[test]
    fn builder_constructs_inferred_and_explicit_discriminated_unions() {
        let schemas = indexmap::IndexMap::new();
        let mut inferred_builder = Builder {
            types: Vec::new(),
            schemas: &schemas,
            strip_discriminant: std::collections::HashMap::new(),
            building_types: std::collections::HashSet::new(),
        };
        let inferred = schema(serde_json::json!({
            "oneOf": [
                { "type": "object", "properties": {
                    "kind": { "type": "string", "enum": ["cat"] },
                    "whiskers": { "type": "integer" }
                } },
                { "type": "object", "properties": {
                    "kind": { "type": "string", "enum": ["dog"] },
                    "bark": { "type": "boolean" }
                } }
            ]
        }));
        let union = inferred_builder
            .discriminated_union("Pet", "pet", &inferred, Some("A pet.".to_string()))
            .expect("singleton enum property infers a discriminator");
        assert_eq!(union.discriminant_property, "kind");
        assert_eq!(
            union
                .members
                .iter()
                .map(|member| member.discriminant.as_str())
                .collect::<Vec<_>>(),
            ["cat", "dog"]
        );
        assert!(union.variant_targets.is_empty());
        assert_eq!(inferred_builder.types.len(), 2);

        let components: OpenApi = serde_json::from_value(serde_json::json!({
            "components": { "schemas": {
                "Cat": { "type": "object", "properties": { "lives": { "type": "integer" } } },
                "Dog": { "type": "object", "properties": { "bark": { "type": "boolean" } } }
            } }
        }))
        .expect("components deserialize");
        let mut mapped_builder = Builder {
            types: Vec::new(),
            schemas: &components.components.schemas,
            strip_discriminant: std::collections::HashMap::new(),
            building_types: std::collections::HashSet::new(),
        };
        let mapped = schema(serde_json::json!({
            "oneOf": [
                { "$ref": "#/components/schemas/Cat" },
                { "$ref": "#/components/schemas/Dog" }
            ],
            "discriminator": {
                "propertyName": "kind",
                "mapping": {
                    "feline": "#/components/schemas/Cat",
                    "canine": "#/components/schemas/Dog"
                }
            }
        }));
        let union = mapped_builder
            .discriminated_union("Pet", "pet", &mapped, None)
            .expect("explicit mapping resolves components");
        assert_eq!(union.members.len(), 2);
        let mut targets = union.variant_targets;
        targets.sort();
        assert_eq!(targets, ["Cat", "Dog"]);

        let missing_target = schema(serde_json::json!({
            "oneOf": [{ "$ref": "#/components/schemas/Missing" }],
            "discriminator": {
                "propertyName": "kind",
                "mapping": { "missing": "#/components/schemas/Missing" }
            }
        }));
        assert!(mapped_builder
            .discriminated_union("Missing", "missing", &missing_target, None)
            .is_none());
    }

    #[test]
    fn field_type_ref_hoists_array_and_nested_property_unions() {
        let schemas = indexmap::IndexMap::new();
        let mut builder = Builder {
            types: Vec::new(),
            schemas: &schemas,
            strip_discriminant: std::collections::HashMap::new(),
            building_types: std::collections::HashSet::new(),
        };
        let array_union = schema(serde_json::json!({
            "type": "array",
            "items": {
                "description": "Mixed values.",
                "oneOf": [{ "type": "string" }, { "type": "integer" }]
            }
        }));
        assert_eq!(
            builder.field_type_ref("Record", "values", &array_union),
            TypeRef::List(Box::new(TypeRef::Named("RecordValuesItem".to_string())))
        );
        assert!(builder.types.iter().any(|declaration| matches!(
            declaration,
            TypeDecl::Alias(alias)
                if alias.name == "RecordValuesItem"
                    && matches!(&alias.target, TypeRef::Union(variants) if variants.len() == 2)
        )));

        let nested_union = schema(serde_json::json!({
            "anyOf": [
                { "type": "array", "items": {
                    "description": "Nested alternatives.",
                    "anyOf": [{ "type": "string" }, { "type": "boolean" }]
                } },
                { "type": "object" },
                { "type": "integer", "nullable": true }
            ]
        }));
        assert_eq!(
            builder.field_type_ref("Record", "choice", &nested_union),
            TypeRef::Named("RecordChoice".to_string())
        );
        assert!(builder.types.iter().any(|declaration| matches!(
            declaration,
            TypeDecl::Alias(alias) if alias.name == "RecordChoiceZeroItem"
        )));
        assert!(builder.types.iter().any(|declaration| matches!(
            declaration,
            TypeDecl::Alias(alias)
                if alias.name == "RecordChoice"
                    && matches!(&alias.target, TypeRef::Union(variants)
                        if variants.iter().any(|variant| matches!(variant, TypeRef::Dict(..)))
                            && variants.iter().any(|variant| matches!(variant, TypeRef::Optional(_))))
        )));
    }

    #[test]
    fn inline_hoister_handles_enum_array_shapes_and_defensive_inputs() {
        let mut hoister = InlineHoister {
            root_types: &[],
            schemas: None,
            out: Vec::new(),
        };
        for invalid in [
            schema(serde_json::json!({ "type": "string" })),
            schema(serde_json::json!({ "type": "array" })),
            schema(serde_json::json!({
                "type": "array", "items": { "$ref": "#/components/schemas/Kind" }
            })),
            schema(serde_json::json!({
                "type": "array", "items": { "type": "string" }
            })),
        ] {
            assert!(hoister.hoist_array_item_enum("Choice", &invalid).is_none());
        }
        let list = schema(serde_json::json!({
            "type": "array",
            "items": { "type": "string", "enum": ["a", "b"] }
        }));
        assert_eq!(
            hoister.hoist_array_item_enum("Choice", &list),
            Some(TypeRef::List(Box::new(TypeRef::Named(
                "ChoiceItem".to_string()
            ))))
        );
        let unique = schema(serde_json::json!({
            "type": "array", "uniqueItems": true,
            "items": { "type": "string", "enum": ["x"] }
        }));
        assert_eq!(
            hoister.hoist_array_item_enum("Unique", &unique),
            Some(TypeRef::List(Box::new(TypeRef::Named(
                "UniqueItem".to_string()
            ))))
        );
        assert_eq!(hoister.out.len(), 2);
    }

    #[test]
    fn reference_class_names_walk_properties_items_and_compositions() {
        assert_eq!(ref_to_class("external/path-name"), "PathName");
        assert_eq!(
            ref_to_class(
                "#/components/schemas/Root/properties/child/items/oneOf/0/properties/name"
            ),
            "RootChildItemName"
        );
        assert_eq!(
            ref_to_class("#/components/schemas/Root/allOf/0/anyOf/1/items"),
            "RootItem"
        );
        assert_eq!(module_identifier("list"), "list_");
        assert_eq!(module_identifier("records"), "records");
    }

    #[test]
    fn request_body_resolution_handles_referenced_arrays_bare_objects_and_wildcards() {
        let doc: OpenApi = serde_json::from_value(serde_json::json!({
            "components": { "schemas": {
                "Names": { "type": "array", "items": { "type": "string" } },
                "OpenBag": { "type": "object" }
            } }
        }))
        .expect("components deserialize");
        let types = Vec::new();

        let referenced_array: crate::openapi::RequestBody =
            serde_json::from_value(serde_json::json!({
                "required": false,
                "content": { "application/json": {
                    "schema": { "$ref": "#/components/schemas/Names" }
                } }
            }))
            .expect("request body deserializes");
        let mut hoister = InlineHoister {
            root_types: &types,
            schemas: None,
            out: Vec::new(),
        };
        let RequestBody::Single(array) = resolve_request_body(
            &doc,
            &types,
            &referenced_array,
            &mut hoister,
            "ListNamesRequest",
            true,
        )
        .expect("referenced array is supported") else {
            panic!("referenced array should be a single request argument")
        };
        assert_eq!(array.type_ref, TypeRef::Named("Names".to_string()));
        assert!(!array.required);
        assert!(!array.convert);
        assert!(!array.content_type);

        let vendor_bag: crate::openapi::RequestBody = serde_json::from_value(serde_json::json!({
            "required": false,
            "content": { "application/vnd.acme+json": {
                "schema": { "$ref": "#/components/schemas/OpenBag" }
            } }
        }))
        .expect("request body deserializes");
        let RequestBody::Single(bag) = resolve_request_body(
            &doc,
            &types,
            &vendor_bag,
            &mut hoister,
            "PutBagRequest",
            true,
        )
        .expect("bare object is supported") else {
            panic!("bare object should be a single request argument")
        };
        assert_eq!(bag.type_ref, TypeRef::Named("OpenBag".to_string()));
        assert_eq!(
            bag.content_type_override.as_deref(),
            Some("application/vnd.acme+json")
        );
        assert!(bag.content_type);

        let wildcard_binary: crate::openapi::RequestBody =
            serde_json::from_value(serde_json::json!({
                "required": false,
                "content": { "*/*": {
                    "schema": { "type": "string", "format": "binary", "example": "blob.bin" }
                } }
            }))
            .expect("request body deserializes");
        let RequestBody::Single(binary) = resolve_request_body(
            &doc,
            &types,
            &wildcard_binary,
            &mut hoister,
            "UploadRequest",
            true,
        )
        .expect("wildcard binary is supported") else {
            panic!("wildcard binary should be a single request argument")
        };
        assert_eq!(binary.type_ref, TypeRef::Primitive(Prim::Str));
        assert!(binary.required);
        assert_eq!(binary.content_type_override.as_deref(), Some("*/*"));
        assert_eq!(binary.example.as_deref(), Some("\"blob.bin\""));
    }

    #[test]
    fn inline_hoister_builds_response_items_allof_objects_and_union_variants() {
        let mut hoister = InlineHoister {
            root_types: &[],
            schemas: None,
            out: Vec::new(),
        };
        assert!(hoister
            .hoist_response_array_item_object(
                "ResultItem",
                &schema(serde_json::json!({ "type": "string" })),
            )
            .is_none());
        assert!(hoister
            .hoist_response_array_item_object(
                "ResultItem",
                &schema(serde_json::json!({ "type": "array" })),
            )
            .is_none());

        let response = schema(serde_json::json!({
            "type": "array",
            "items": {
                "type": "object",
                "description": "A result.",
                "required": ["id", "label"],
                "allOf": [
                    { "$ref": "#/components/schemas/Base" },
                    { "type": "object", "properties": { "id": { "type": "integer" } } }
                ],
                "properties": { "label": { "type": "string" } }
            }
        }));
        assert_eq!(
            hoister.hoist_response_array_item_object("ResultItem", &response),
            Some(TypeRef::List(Box::new(TypeRef::Named(
                "ResultItem".to_string()
            ))))
        );
        let result = hoister
            .out
            .iter()
            .find_map(|decl| match decl {
                TypeDecl::Object(object) if object.name == "ResultItem" => Some(object),
                _ => None,
            })
            .expect("response item object was hoisted");
        assert_eq!(result.bases, ["Base"]);
        assert_eq!(
            result
                .fields
                .iter()
                .map(|field| field.wire_name.as_str())
                .collect::<Vec<_>>(),
            ["id", "label"]
        );
        assert!(result.fields.iter().all(|field| field.spec_required));

        let referenced = schema(serde_json::json!({ "$ref": "#/components/schemas/Base" }));
        assert_eq!(
            hoister.hoist_union_variant("Choice", 0, &referenced, &[]),
            TypeRef::Named("Base".to_string())
        );
        let bare_with_instance = schema(serde_json::json!({
            "type": "object",
            "example": { "value": "sample" }
        }));
        assert_eq!(
            hoister.hoist_union_variant(
                "Choice",
                1,
                &bare_with_instance,
                std::slice::from_ref(&bare_with_instance),
            ),
            TypeRef::Named("ChoiceOne".to_string())
        );
        assert_eq!(
            hoister.hoist_union_variant(
                "Choice",
                2,
                &schema(serde_json::json!({ "type": "boolean" })),
                &[],
            ),
            TypeRef::Primitive(Prim::Bool)
        );
    }

    #[test]
    fn builder_handles_discriminated_unique_items_and_flattens_overlapping_bases() {
        let schemas = indexmap::IndexMap::new();
        let mut builder = Builder {
            types: Vec::new(),
            schemas: &schemas,
            strip_discriminant: std::collections::HashMap::new(),
            building_types: std::collections::HashSet::new(),
        };
        let events = schema(serde_json::json!({
            "type": ["array", "null"],
            "uniqueItems": true,
            "items": {
                "oneOf": [
                    { "type": "object", "required": ["kind", "value"], "properties": {
                        "kind": { "type": "string", "enum": ["created"] },
                        "value": { "type": "integer" }
                    } },
                    { "type": "object", "required": ["kind", "reason"], "properties": {
                        "kind": { "type": "string", "enum": ["deleted"] },
                        "reason": { "type": "string" }
                    } }
                ]
            }
        }));
        builder.add_named("Events", &events);
        assert!(builder.types.iter().any(|decl| matches!(
            decl,
            TypeDecl::DiscriminatedUnion(union)
                if union.name == "EventsItem" && union.members.len() == 2
        )));
        assert!(builder.types.iter().any(|decl| matches!(
            decl,
            TypeDecl::Alias(alias)
                if alias.name == "Events"
                    && matches!(&alias.target,
                        TypeRef::Optional(inner)
                            if matches!(inner.as_ref(), TypeRef::List(item)
                                if matches!(item.as_ref(), TypeRef::Named(name) if name == "EventsItem")))
        )));

        let doc: OpenApi = serde_json::from_value(serde_json::json!({
            "components": { "schemas": {
                "Base": {
                    "type": "object",
                    "required": ["shared", "inherited"],
                    "properties": {
                        "shared": { "type": "string", "description": "Inherited docs." },
                        "inherited": { "type": "integer" }
                    }
                },
                "Child": {
                    "allOf": [
                        { "$ref": "#/components/schemas/Base" },
                        { "type": "object", "required": ["shared"], "properties": {
                            "shared": { "type": "string" }
                        } }
                    ]
                }
            } }
        }))
        .expect("components deserialize");
        let mut flattening = Builder {
            types: Vec::new(),
            schemas: &doc.components.schemas,
            strip_discriminant: std::collections::HashMap::new(),
            building_types: std::collections::HashSet::new(),
        };
        flattening.add_named("Child", &doc.components.schemas["Child"]);
        let child = flattening
            .types
            .iter()
            .find_map(|decl| match decl {
                TypeDecl::Object(object) if object.name == "Child" => Some(object),
                _ => None,
            })
            .expect("child object emitted");
        assert!(child.bases.is_empty());
        assert_eq!(
            child
                .fields
                .iter()
                .map(|field| field.wire_name.as_str())
                .collect::<Vec<_>>(),
            ["shared", "inherited"]
        );
        assert_eq!(
            child.fields[0].docstring.as_deref(),
            Some("Inherited docs.")
        );

        flattening.building_types.insert("Loop".to_string());
        flattening.add_object(
            "Loop",
            "loop".to_string(),
            &schema(serde_json::json!({ "type": "object" })),
            None,
        );
        assert!(!flattening.types.iter().any(|decl| decl.name() == "Loop"));
    }

    #[test]
    fn field_type_resolution_handles_metadata_nullable_components_and_array_models() {
        let doc: OpenApi = serde_json::from_value(serde_json::json!({
            "components": { "schemas": {
                "NullableName": { "type": "string", "nullable": true }
            } }
        }))
        .expect("components deserialize");
        let mut builder = Builder {
            types: Vec::new(),
            schemas: &doc.components.schemas,
            strip_discriminant: std::collections::HashMap::new(),
            building_types: std::collections::HashSet::new(),
        };
        assert_eq!(
            builder.field_type_ref("Record", "metadata", &Schema::default()),
            TypeRef::Optional(Box::new(TypeRef::Primitive(Prim::Any)))
        );

        let nullable_refs = schema(serde_json::json!({
            "type": "array",
            "uniqueItems": true,
            "items": { "$ref": "#/components/schemas/NullableName" }
        }));
        assert_eq!(
            builder.field_type_ref("Record", "names", &nullable_refs),
            TypeRef::List(Box::new(TypeRef::Optional(Box::new(TypeRef::Named(
                "NullableName".to_string()
            )))))
        );

        let inline_items = schema(serde_json::json!({
            "type": "array",
            "uniqueItems": true,
            "items": {
                "type": "object",
                "nullable": true,
                "properties": { "id": { "type": "string" } }
            }
        }));
        assert_eq!(
            builder.field_type_ref("Record", "entries", &inline_items),
            TypeRef::List(Box::new(TypeRef::Optional(Box::new(TypeRef::Named(
                "RecordEntriesItem".to_string()
            )))))
        );

        let union_items = schema(serde_json::json!({
            "type": "array",
            "items": {
                "oneOf": [
                    { "type": "object", "required": ["kind"], "properties": {
                        "kind": { "type": "string", "enum": ["one"] }
                    } },
                    { "type": "object", "required": ["kind"], "properties": {
                        "kind": { "type": "string", "enum": ["two"] }
                    } }
                ]
            }
        }));
        assert_eq!(
            builder.field_type_ref("Record", "events", &union_items),
            TypeRef::List(Box::new(TypeRef::Named("RecordEventsItem".to_string())))
        );
        assert!(builder.types.iter().any(|decl| matches!(
            decl,
            TypeDecl::DiscriminatedUnion(union) if union.name == "RecordEventsItem"
        )));
    }

    #[test]
    fn described_allof_validates_annotation_only_compositions() {
        let valid = schema(serde_json::json!({
            "allOf": [
                { "$ref": "#/components/schemas/Target" },
                { "description": "Use-site docs." }
            ]
        }));
        assert_eq!(
            described_all_of_ref(&valid),
            Some(("#/components/schemas/Target", Some("Use-site docs.")))
        );
        assert_eq!(property_description(&valid), Some("Use-site docs."));

        let outer_description = schema(serde_json::json!({
            "description": "Outer docs.",
            "allOf": [
                { "description": "Inner docs." },
                { "$ref": "#/components/schemas/Target" },
                {}
            ]
        }));
        assert_eq!(
            described_all_of_ref(&outer_description),
            Some(("#/components/schemas/Target", Some("Outer docs.")))
        );

        for invalid in [
            serde_json::json!({}),
            serde_json::json!({ "allOf": [{ "$ref": "#/components/schemas/Target" }] }),
            serde_json::json!({ "allOf": [{}, { "description": "No reference." }] }),
            serde_json::json!({
                "allOf": [
                    { "$ref": "#/components/schemas/One" },
                    { "$ref": "#/components/schemas/Two" }
                ]
            }),
            serde_json::json!({
                "allOf": [
                    { "$ref": "#/components/schemas/Target" },
                    { "type": "string", "description": "Adds a shape." }
                ]
            }),
        ] {
            assert!(described_all_of_ref(&schema(invalid)).is_none());
        }

        assert_eq!(
            array_item_type_ref(&schema(serde_json::json!({
                "type": "string",
                "nullable": true
            }))),
            TypeRef::Optional(Box::new(TypeRef::Primitive(Prim::Str)))
        );
        assert_eq!(
            array_item_type_ref(&schema(serde_json::json!({ "type": "integer" }))),
            TypeRef::Primitive(Prim::Int)
        );
    }

    #[test]
    fn described_allof_clones_object_enum_and_alias_targets_at_each_use_site() {
        let doc: OpenApi = serde_json::from_value(serde_json::json!({
            "components": { "schemas": {
                "Details": {
                    "type": "object",
                    "nullable": true,
                    "required": ["id"],
                    "properties": { "id": { "type": "integer" } }
                },
                "State": { "type": "string", "enum": ["ready", "done"] },
                "Token": { "type": "string" },
                "Labels": {
                    "type": "object",
                    "additionalProperties": { "type": "string" }
                },
                "Envelope": {
                    "type": "object",
                    "required": ["details", "state", "token", "labels"],
                    "properties": {
                        "details": {
                            "allOf": [
                                { "$ref": "#/components/schemas/Details" },
                                { "description": "Contextual details." }
                            ]
                        },
                        "state": {
                            "allOf": [
                                { "$ref": "#/components/schemas/State" },
                                { "description": "Contextual state." }
                            ]
                        },
                        "token": {
                            "allOf": [
                                { "$ref": "#/components/schemas/Token" },
                                { "description": "Contextual token." }
                            ]
                        },
                        "labels": {
                            "allOf": [
                                { "$ref": "#/components/schemas/Labels" },
                                { "description": "Contextual labels." }
                            ]
                        }
                    }
                }
            } }
        }))
        .expect("components deserialize");
        let schemas = &doc.components.schemas;
        let mut builder = Builder {
            types: Vec::new(),
            schemas,
            strip_discriminant: std::collections::HashMap::new(),
            building_types: std::collections::HashSet::new(),
        };
        builder.add_named("Envelope", &schemas["Envelope"]);

        let envelope = builder
            .types
            .iter()
            .find_map(|decl| match decl {
                TypeDecl::Object(object) if object.name == "Envelope" => Some(object),
                _ => None,
            })
            .expect("envelope object is built");
        assert_eq!(
            envelope
                .fields
                .iter()
                .map(|field| {
                    (
                        field.wire_name.as_str(),
                        field.type_ref.clone(),
                        field.optional,
                        field.nullable,
                    )
                })
                .collect::<Vec<_>>(),
            [
                (
                    "details",
                    TypeRef::Named("EnvelopeDetails".to_string()),
                    true,
                    true,
                ),
                (
                    "labels",
                    TypeRef::Dict(
                        Box::new(TypeRef::Primitive(Prim::Str)),
                        Box::new(TypeRef::Primitive(Prim::Str)),
                    ),
                    false,
                    false,
                ),
                (
                    "state",
                    TypeRef::Named("EnvelopeState".to_string()),
                    false,
                    false,
                ),
                ("token", TypeRef::Primitive(Prim::Str), false, false,),
            ]
        );
        assert!(builder.types.iter().any(|decl| matches!(
            decl,
            TypeDecl::Object(object)
                if object.name == "EnvelopeDetails"
                    && object.docstring.as_deref() == Some("Contextual details.")
        )));
        assert!(builder.types.iter().any(|decl| matches!(
            decl,
            TypeDecl::Enum(enum_type)
                if enum_type.name == "EnvelopeState"
                    && enum_type.docstring.as_deref() == Some("Contextual state.")
        )));

        let mut hoister = InlineHoister {
            root_types: &[],
            schemas: Some(schemas),
            out: Vec::new(),
        };
        hoister.hoist_object("Request", &schemas["Envelope"]);
        let request = hoister
            .out
            .iter()
            .find_map(|decl| match decl {
                TypeDecl::Object(object) if object.name == "Request" => Some(object),
                _ => None,
            })
            .expect("request object is hoisted");
        assert_eq!(
            request
                .fields
                .iter()
                .map(|field| {
                    (
                        field.wire_name.as_str(),
                        field.type_ref.clone(),
                        field.optional,
                        field.nullable,
                    )
                })
                .collect::<Vec<_>>(),
            [
                (
                    "details",
                    TypeRef::Named("RequestDetails".to_string()),
                    true,
                    true,
                ),
                (
                    "labels",
                    TypeRef::Dict(
                        Box::new(TypeRef::Primitive(Prim::Str)),
                        Box::new(TypeRef::Primitive(Prim::Str)),
                    ),
                    false,
                    false,
                ),
                (
                    "state",
                    TypeRef::Named("RequestState".to_string()),
                    false,
                    false,
                ),
                ("token", TypeRef::Primitive(Prim::Str), false, false,),
            ]
        );
        assert!(hoister.out.iter().any(|decl| matches!(
            decl,
            TypeDecl::Object(object)
                if object.name == "RequestDetails"
                    && object.docstring.as_deref() == Some("Contextual details.")
        )));
        assert!(hoister.out.iter().any(|decl| matches!(
            decl,
            TypeDecl::Enum(enum_type)
                if enum_type.name == "RequestState"
                    && enum_type.docstring.as_deref() == Some("Contextual state.")
        )));
    }

    #[test]
    fn type_resolution_edges_preserve_optional_union_order_and_ref_nullability() {
        assert_eq!(
            extensible_enum(vec!["a".to_string(), "b".to_string()]),
            TypeRef::Union(vec![
                TypeRef::Literal(vec!["a".to_string(), "b".to_string()]),
                TypeRef::Primitive(Prim::Any),
            ])
        );
        let already_optional = TypeRef::Optional(Box::new(TypeRef::Primitive(Prim::Str)));
        assert_eq!(
            optional_type_ref(already_optional.clone()),
            already_optional
        );
        assert_eq!(
            optional_type_ref(TypeRef::Union(vec![
                TypeRef::Primitive(Prim::Str),
                TypeRef::Primitive(Prim::Int),
            ])),
            TypeRef::Union(vec![
                TypeRef::Primitive(Prim::Str),
                TypeRef::Optional(Box::new(TypeRef::Primitive(Prim::Int))),
            ])
        );

        let doc: OpenApi = serde_json::from_value(serde_json::json!({
            "components": { "schemas": {
                "Nullable": { "type": "string", "nullable": true },
                "Middle": { "$ref": "#/components/schemas/Nullable" },
                "CycleA": { "$ref": "#/components/schemas/CycleB" },
                "CycleB": { "$ref": "#/components/schemas/CycleA" }
            } }
        }))
        .expect("components deserialize");
        assert_eq!(
            full_type_ref_resolved(
                &schema(serde_json::json!({ "$ref": "#/components/schemas/Middle" })),
                &doc.components.schemas,
            ),
            TypeRef::Optional(Box::new(TypeRef::Named("Middle".to_string())))
        );
        assert_eq!(
            full_type_ref_resolved(
                &schema(serde_json::json!({ "$ref": "#/components/schemas/CycleA" })),
                &doc.components.schemas,
            ),
            TypeRef::Named("CycleA".to_string())
        );
        assert_eq!(
            full_type_ref_resolved(
                &schema(serde_json::json!({ "$ref": "#/components/schemas/Missing" })),
                &doc.components.schemas,
            ),
            TypeRef::Named("Missing".to_string())
        );

        assert_eq!(
            base_type_ref(&schema(
                serde_json::json!({ "$ref": "external.json#/Thing" })
            )),
            TypeRef::Optional(Box::new(TypeRef::Primitive(Prim::Any)))
        );
        assert_eq!(
            base_type_ref(&schema(serde_json::json!({
                "allOf": [{ "$ref": "#/components/schemas/Nullable" }]
            }))),
            TypeRef::Named("Nullable".to_string())
        );
        assert_eq!(
            base_type_ref(&schema(serde_json::json!({ "type": "array" }))),
            TypeRef::List(Box::new(TypeRef::Optional(Box::new(TypeRef::Primitive(
                Prim::Any
            )))))
        );
        assert_eq!(
            base_type_ref(&schema(serde_json::json!({
                "type": "object", "additionalProperties": true
            }))),
            TypeRef::Dict(
                Box::new(TypeRef::Primitive(Prim::Str)),
                Box::new(TypeRef::Optional(Box::new(TypeRef::Primitive(Prim::Any))))
            )
        );

        assert_eq!(super::clean_doc(Some("  docs  ")), Some("docs".to_string()));
        assert_eq!(
            super::clean_doc(Some(" leading")),
            Some(" leading".to_string())
        );
        assert_eq!(super::clean_doc(Some("a\tb")), Some("a    b".to_string()));
        assert_eq!(super::clean_doc(Some(" \n")), None);
        assert_eq!(super::operation_doc(Some(" \n")), Some(String::new()));
        assert_eq!(
            super::operation_doc(Some(" leading")),
            Some(" leading".to_string())
        );
        assert_eq!(super::operation_doc(None), None);
        assert_eq!(
            super::declared_doc(Some("keeps spaces  \n\n")),
            Some("keeps spaces  ".to_string())
        );
        assert_eq!(super::declared_doc(Some("a\tb")), Some("a\tb".to_string()));
        assert_eq!(
            super::example_literal(&serde_json::json!("a \"quote\"")),
            Some("'a \"quote\"'".to_string())
        );
        assert_eq!(
            super::example_literal(&serde_json::json!([1, true, "x"])),
            Some("[1, True, \"x\"]".to_string())
        );
        assert_eq!(
            super::example_literal(&serde_json::json!({ "x": null })),
            None
        );
    }

    #[test]
    fn endpoint_grouping_and_fallback_names_cover_head_dotted_and_path_routes() {
        assert_eq!(
            synthesized_method_name("HEAD", "/widgets/{widget_id}/status"),
            "head_widgets_widget_id_status"
        );
        assert_eq!(synthesized_method_name("OPTIONS", "/{id}"), "options_id");
        assert_eq!(path_group("/{tenant}/{id}"), "service");
        assert_eq!(path_group("/{tenant}/WidgetGroups/{id}"), "WidgetGroups");

        assert_eq!(
            endpoint_module(
                &operation(serde_json::json!({
                    "operationId": ".status",
                    "tags": ["Ignored"]
                })),
                "/status"
            ),
            "_"
        );
        assert_eq!(
            endpoint_module(
                &operation(serde_json::json!({
                    "operationId": "GroupV2.GetGroup",
                    "tags": ["GroupV2"]
                })),
                "/groups"
            ),
            "groupv2"
        );
        assert_eq!(
            endpoint_module(
                &operation(serde_json::json!({
                    "operationId": "admin-users.get",
                    "tags": []
                })),
                "/users"
            ),
            "admin_users"
        );
        assert_eq!(
            endpoint_module(
                &operation(serde_json::json!({
                    "operationId": "Widgets_get_by_id_now",
                    "tags": ["Widgets"]
                })),
                "/widgets/{id}"
            ),
            "widgets"
        );
        assert_eq!(
            endpoint_module(
                &operation(serde_json::json!({
                    "operationId": "CREATE_AttachmentPublic",
                    "tags": ["attachment-public"]
                })),
                "/attachments"
            ),
            "attachment_public"
        );
        assert_eq!(
            endpoint_module(
                &operation(serde_json::json!({
                    "operationId": "searchWidgets",
                    "tags": ["Search"]
                })),
                "/widgets"
            ),
            "search"
        );
    }
}
