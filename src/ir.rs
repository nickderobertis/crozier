//! The intermediate representation: a small, generation-ready model built from
//! the OpenAPI document, decoupling parsing from emission. Schema and property
//! order is preserved from the document so generated output is deterministic.

use crate::config::GenerateConfig;
use crate::naming;
use crate::openapi::{AdditionalProperties, OpenApi, Operation, ParameterLocation, Schema};

/// A fully-resolved SDK model ready to emit.
#[derive(Debug)]
pub struct Ir {
    /// Python import package name (directory under `src/`).
    pub package_name: String,
    /// Distribution name recorded in `version.py`.
    pub project_name: String,
    /// Generated types, in document order.
    pub types: Vec<TypeDecl>,
    /// Endpoint client module (directory) names, one per operation group, in
    /// first-seen order.
    pub endpoint_modules: Vec<String>,
    /// Every operation, in document-traversal order, resolved for emission.
    pub endpoints: Vec<Endpoint>,
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
    /// The success response body type, or `None` when the endpoint returns no
    /// content.
    pub response: Option<TypeRef>,
    /// A short description shown as the docstring's summary line.
    pub docstring: Option<String>,
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
}

impl RequestBody {
    /// Whether the request emits the `content-type: application/json` header.
    /// Inlined object bodies always do; a single body carries its own flag.
    #[must_use]
    pub fn content_type_header(&self) -> bool {
        match self {
            RequestBody::Single(s) => s.content_type,
            RequestBody::Inline(_) => true,
        }
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
    /// Optional description, shown under the argument in the docstring.
    pub docstring: Option<String>,
    /// Whether the field serializes through `convert_and_respect_annotation_metadata`
    /// (its type references an object or union carrying field aliases).
    pub convert: bool,
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
    let mut builder = Builder { types: Vec::new() };
    for (key, schema) in &doc.components.schemas {
        builder.add_named(&naming::class_name(key), schema);
    }
    // Endpoint resolution consults the built types to hoist a plain-object `$ref`
    // body's fields and to decide which of them serialize through the convert
    // wrapper, so it runs after the type layer is built.
    let endpoints = endpoints(doc, &builder.types);
    Ir {
        package_name: config.package_name.clone(),
        project_name: config.project_name.clone(),
        types: builder.types,
        endpoint_modules: endpoint_modules(doc),
        endpoints,
    }
}

/// Resolve every operation into an [`Endpoint`], in document-traversal order
/// (paths in document order, methods in a stable per-path order).
fn endpoints(doc: &OpenApi, types: &[TypeDecl]) -> Vec<Endpoint> {
    let mut out = Vec::new();
    for (path, item) in &doc.paths {
        for (http_method, op) in item.operations() {
            out.push(build_endpoint(doc, types, path, http_method, op));
        }
    }
    out
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
) -> Endpoint {
    let module = endpoint_module(&op.operation_id);
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
                .map_or(TypeRef::Primitive(Prim::Any), base_type_ref),
        })
        .collect();

    let query_params: Vec<QueryParam> = op
        .parameters
        .iter()
        .filter(|p| p.location == Some(ParameterLocation::Query))
        .map(|p| QueryParam {
            wire_name: p.name.clone(),
            py_name: naming::field_name(&p.name),
            type_ref: p
                .schema
                .as_ref()
                .map_or(TypeRef::Primitive(Prim::Any), base_type_ref),
            required: p.required == Some(true),
            docstring: clean_doc(p.description.as_deref()),
        })
        .collect();

    let header_params: Vec<HeaderParam> = op
        .parameters
        .iter()
        .filter(|p| p.location == Some(ParameterLocation::Header))
        .map(|p| HeaderParam {
            wire_name: p.name.clone(),
            py_name: naming::field_name(header_param_stem(&p.name)),
            type_ref: p
                .schema
                .as_ref()
                .map_or(TypeRef::Primitive(Prim::Any), base_type_ref),
            required: p.required == Some(true),
            docstring: clean_doc(p.description.as_deref()),
        })
        .collect();

    // Today crozier handles path, query, and header parameters; any other kind
    // (cookie, an unknown location, or a `$ref` with no location) puts the
    // operation outside the emittable subset.
    let has_unsupported_params = op.parameters.iter().any(|p| {
        !matches!(
            p.location,
            Some(ParameterLocation::Path | ParameterLocation::Query | ParameterLocation::Header)
        )
    });
    let only_success =
        !op.responses.is_empty() && op.responses.keys().all(|code| code.starts_with('2'));
    let response = success_response(op);

    // A request body is either absent, within the subset crozier can render, or
    // unsupported.
    let request_body = op
        .request_body
        .as_ref()
        .and_then(|rb| resolve_request_body(doc, types, rb));
    let body_ok = op.request_body.is_none() || request_body.is_some();

    // A path parameter whose Python name collides with a hoisted body field is
    // suffixed with `_` (the body field keeps the plain name), matching Fern.
    if let Some(RequestBody::Inline(fields)) = &request_body {
        let field_names: std::collections::HashSet<&str> =
            fields.iter().map(|f| f.py_name.as_str()).collect();
        for pp in &mut path_params {
            if field_names.contains(pp.py_name.as_str()) {
                pp.py_name.push('_');
            }
        }
    }

    // Today's subset: a supported (or absent) body, path/query/header params only,
    // only 2xx responses, and a response crozier knows how to render — a named
    // model, a scalar, or no content (a 2xx without a JSON body).
    let emittable = body_ok
        && !has_unsupported_params
        && only_success
        && matches!(
            response,
            None | Some(TypeRef::Named(_) | TypeRef::Primitive(_))
        );

    Endpoint {
        module,
        method_name: endpoint_method_name(&op.operation_id),
        http_method,
        path: path.to_string(),
        path_params,
        query_params,
        header_params,
        request_body,
        response,
        docstring: clean_doc(op.description.as_deref()),
        emittable,
    }
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
) -> Option<RequestBody> {
    let schema = rb.content.get("application/json")?.schema.as_ref()?;
    let required = rb.required == Some(true);
    if let Some(reference) = &schema.reference {
        let target = resolve_ref(doc, reference)?;
        let class = ref_to_class(reference);
        // A `$ref` to an extensible (string) enum serializes as a plain
        // `json=request` with the content-type header.
        if string_enum_values(target).is_some() {
            return Some(single(TypeRef::Named(class), required, false, true));
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
        // A `$ref` to a plain object is inlined field-by-field.
        if !target.properties.is_empty() || target.all_of.is_some() {
            return hoist_fields(&class, types).map(RequestBody::Inline);
        }
        return None;
    }
    // An inline array body: a single `request` argument. A container of objects
    // serializes through the convert wrapper; either way, no content-type header.
    if schema.ty.as_ref().and_then(|t| t.primary()) == Some("array") {
        let item = base_type_ref(schema.items.as_ref()?);
        let convert = type_needs_convert(&item, types);
        return Some(single(
            TypeRef::List(Box::new(item)),
            required,
            convert,
            false,
        ));
    }
    scalar_body(schema)
        .map(|(type_ref, content_type)| single(type_ref, required, false, content_type))
}

/// A one-argument request body.
fn single(type_ref: TypeRef, required: bool, convert: bool, content_type: bool) -> RequestBody {
    RequestBody::Single(SingleBody {
        type_ref,
        required,
        convert,
        content_type,
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
    Some(
        obj.fields
            .iter()
            .map(|f| BodyField {
                wire_name: f.wire_name.clone(),
                py_name: f.py_name.clone(),
                type_ref: f.type_ref.clone(),
                optional: f.optional,
                docstring: f.docstring.clone(),
                convert: type_needs_convert(&f.type_ref, types),
            })
            .collect(),
    )
}

/// Whether a type serializes through `convert_and_respect_annotation_metadata` —
/// true when it references (through collections/optionals) a generated object or a
/// union alias, whose members carry field aliases that must be respected on write.
fn type_needs_convert(t: &TypeRef, types: &[TypeDecl]) -> bool {
    match t {
        TypeRef::Named(name) => types.iter().any(|d| match d {
            TypeDecl::Object(o) => o.name == *name,
            TypeDecl::Alias(a) => a.name == *name && matches!(a.target, TypeRef::Union(_)),
        }),
        TypeRef::Optional(inner) | TypeRef::List(inner) | TypeRef::Set(inner) => {
            type_needs_convert(inner, types)
        }
        TypeRef::Dict(_, value) => type_needs_convert(value, types),
        _ => false,
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
        "integer" => TypeRef::Primitive(Prim::Int),
        "number" => TypeRef::Primitive(Prim::Float),
        "boolean" => TypeRef::Primitive(Prim::Bool),
        _ => return None,
    };
    Some((type_ref, false))
}

/// Resolve a local `#/components/schemas/{key}` reference to its schema.
fn resolve_ref<'a>(doc: &'a OpenApi, reference: &str) -> Option<&'a Schema> {
    let key = reference.rsplit('/').next()?;
    doc.components.schemas.get(key)
}

/// The success (2xx) response's `application/json` body type, if any.
fn success_response(op: &Operation) -> Option<TypeRef> {
    let response = op
        .responses
        .iter()
        .find(|(code, _)| code.starts_with('2'))
        .map(|(_, r)| r)?;
    let schema = response.content.get("application/json")?.schema.as_ref()?;
    Some(base_type_ref(schema))
}

/// The generated Python method name for an operation. Mirrors the module rule
/// (see [`endpoint_module`]): when the group prefix is itself multi-segment
/// (contains `_`), the whole operationId is snake-cased; otherwise only the
/// suffix after the final `_` is taken and lowercased (camel humps flattened),
/// matching Fern (`endpoints_put_add`, but `postwithnoauth`).
fn endpoint_method_name(operation_id: &str) -> String {
    let (group, rest) = operation_id.rsplit_once('_').unwrap_or(("", operation_id));
    if group.contains('_') {
        naming::to_snake_case(operation_id)
    } else {
        rest.to_lowercase()
    }
}

/// Collect the endpoint client module names, one per operation group, in the
/// order groups first appear across the document's paths.
fn endpoint_modules(doc: &OpenApi) -> Vec<String> {
    let mut modules = Vec::new();
    let mut seen = std::collections::HashSet::new();
    for item in doc.paths.values() {
        for (_, op) in item.operations() {
            let module = endpoint_module(&op.operation_id);
            if seen.insert(module.clone()) {
                modules.push(module);
            }
        }
    }
    modules
}

/// The client module (directory) name for an operation, derived from its
/// operationId's group prefix (everything before the final `_`): `snake_case`d
/// when the prefix itself contains an underscore, otherwise just lowercased.
/// This reproduces Fern's directory names (`endpoints_content_type`,
/// `inlinedrequests`).
fn endpoint_module(operation_id: &str) -> String {
    let prefix = operation_id
        .rsplit_once('_')
        .map_or(operation_id, |(prefix, _)| prefix);
    if prefix.contains('_') {
        naming::to_snake_case(prefix)
    } else {
        prefix.to_lowercase()
    }
}

/// Accumulates generated types. Some schemas produce more than one type: an
/// inline schema (a `oneOf` object variant, or an inline enum property) is
/// *hoisted* into its own named type and referenced by name, matching Fern.
struct Builder {
    types: Vec<TypeDecl>,
}

impl Builder {
    /// Classify one named schema and push it (plus any hoisted types).
    fn add_named(&mut self, name: &str, schema: &Schema) {
        let module = naming::module_name(name);
        let docstring = clean_doc(schema.description.as_deref());

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

        // Object with properties, an `allOf`, or an explicit `type: object`.
        if !schema.properties.is_empty() || schema.all_of.is_some() || is_object_type(schema) {
            self.add_object(name, module, schema, docstring);
            return;
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
        let mut bases = Vec::new();
        let mut fields = Vec::new();
        for member in schema.all_of.iter().flatten() {
            if let Some(reference) = &member.reference {
                bases.push(ref_to_class(reference));
            } else {
                self.collect_fields(name, member, &required, &mut fields);
            }
        }
        self.collect_fields(name, schema, &required, &mut fields);
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
        for (prop, prop_schema) in &schema.properties {
            let optional = is_optional(prop_schema) || !required.contains(&prop.as_str());
            fields.push(Field {
                wire_name: prop.clone(),
                py_name: naming::field_name(prop),
                type_ref: self.field_type_ref(owner, prop, prop_schema),
                optional,
                docstring: clean_doc(prop_schema.description.as_deref()),
            });
        }
    }

    /// The type of a property, hoisting an inline string enum to a named
    /// extensible-enum type `{Owner}{Prop}` (as Fern does for `typesAnimal`).
    fn field_type_ref(&mut self, owner: &str, prop: &str, prop_schema: &Schema) -> TypeRef {
        if prop_schema.reference.is_none() {
            if let Some(values) = string_enum_values(prop_schema) {
                let hoisted = format!("{owner}{}", naming::class_name(prop));
                let module = naming::module_name(&hoisted);
                let target = extensible_enum(values);
                self.push_alias(
                    &hoisted,
                    module,
                    target,
                    clean_doc(prop_schema.description.as_deref()),
                );
                return TypeRef::Named(hoisted);
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
            Some(AdditionalProperties::Schema(_))
        )
}

/// An inline (not `$ref`) object-shaped schema that Fern hoists into its own
/// named type when it appears as a union variant.
fn is_inline_object(schema: &Schema) -> bool {
    schema.reference.is_none()
        && (!schema.properties.is_empty() || schema.all_of.is_some() || is_object_type(schema))
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
        // Fern renders an OpenAPI string enum as an extensible enum.
        return extensible_enum(values);
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
            Some(AdditionalProperties::Schema(value)) => {
                let mut val = base_type_ref(value);
                // Fern makes a nullable map's value type optional too.
                if schema.nullable == Some(true) {
                    val = TypeRef::Optional(Box::new(val));
                }
                TypeRef::Dict(Box::new(TypeRef::Primitive(Prim::Str)), Box::new(val))
            }
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

#[cfg(test)]
mod tests {
    use super::{endpoint_method_name, endpoint_module, scalar_body, Prim, TypeRef};
    use crate::openapi::{Schema, TypeField};

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
            endpoint_method_name("endpoints_put_add"),
            "endpoints_put_add"
        );
        assert_eq!(
            endpoint_method_name("endpoints_urls_withMixedCase"),
            "endpoints_urls_with_mixed_case"
        );
        assert_eq!(
            endpoint_method_name("endpoints_httpMethods_testGet"),
            "endpoints_http_methods_test_get"
        );
    }

    #[test]
    fn method_name_lowercases_suffix_for_single_segment_groups() {
        // A single-segment group (`noReqBody`) contributes nothing to the method
        // name; only the suffix survives, flattened to lowercase.
        assert_eq!(
            endpoint_method_name("noReqBody_getWithNoRequestBody"),
            "getwithnorequestbody"
        );
        assert_eq!(
            endpoint_method_name("inlinedRequests_postWithObjectBodyandResponse"),
            "postwithobjectbodyandresponse"
        );
    }

    #[test]
    fn module_mirrors_the_group_naming() {
        assert_eq!(endpoint_module("endpoints_put_add"), "endpoints_put");
        assert_eq!(
            endpoint_module("endpoints_httpMethods_testGet"),
            "endpoints_http_methods"
        );
        assert_eq!(
            endpoint_module("noReqBody_getWithNoRequestBody"),
            "noreqbody"
        );
    }
}
