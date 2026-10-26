//! Refuse name shapes whose baseline SDK fails the refusal registry's bar.

use crate::openapi::{document_boolean, AdditionalProperties, OpenApi, Schema};
use crate::{Error, Result};
use std::path::Path;

/// The name-family refusal classes this module detects, as registered in
/// `docs/fern-refusals/classes.tsv`.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
enum Class {
    DiscriminantValueUnsuitable,
    DuplicatePathParameter,
    EnumNameUnsuitable,
    EnumValueUnnameable,
    GeneratedFileNameTooLong,
    ObjectPropertyNameCollision,
    RequestPropertyCamelcaseCollision,
    RequestPropertyNameCollision,
    SdkMethodCollision,
    TypeNameCollision,
    TypeNameNotLetterLed,
}

impl Class {
    /// The class id every refusal line names.
    const fn id(self) -> &'static str {
        match self {
            Self::DiscriminantValueUnsuitable => "discriminant-value-unsuitable",
            Self::DuplicatePathParameter => "duplicate-path-parameter",
            Self::EnumNameUnsuitable => "enum-name-unsuitable",
            Self::EnumValueUnnameable => "enum-value-unnameable",
            Self::GeneratedFileNameTooLong => "generated-file-name-too-long",
            Self::ObjectPropertyNameCollision => "object-property-name-collision",
            Self::RequestPropertyCamelcaseCollision => "request-property-camelcase-collision",
            Self::RequestPropertyNameCollision => "request-property-name-collision",
            Self::SdkMethodCollision => "sdk-method-collision",
            Self::TypeNameCollision => "type-name-collision",
            Self::TypeNameNotLetterLed => "type-name-not-letter-led",
        }
    }
}

/// A refusal of `class` at the offending element `detail`.
fn refusal(path: &Path, class: Class, detail: String) -> Error {
    Error::InvalidSpec {
        path: path.to_owned(),
        message: format!("{}: {detail}", class.id()),
    }
}

/// Validate before rendering or touching the output tree.
pub(crate) fn validate(doc: &OpenApi, path: &Path, strict: bool, ir: &crate::ir::Ir) -> Result<()> {
    validate_names(doc, path, ir).map_err(|error| refusal_error(error, strict))
}

fn refusal_error(error: Error, strict: bool) -> Error {
    match error {
        Error::InvalidSpec { path, message } => {
            let message = message.replace('\n', "\\n").replace('\r', "\\r");
            Error::InvalidSpec {
                path,
                message: if strict {
                    format!("{message} (fern-strict: Fern refuses this document)")
                } else {
                    message
                },
            }
        }
        other => other,
    }
}

/// Retain a measured name refusal when another malformed field prevents lowering.
/// This classifies the source without making its malformed field valid.
pub(crate) fn load(args: &crate::GenerateArgs) -> Result<OpenApi> {
    match crate::openapi::load(&args.spec) {
        Ok(doc) => Ok(doc),
        Err(error) => {
            if let Ok(source) = source_document(&args.spec) {
                source_refusals(&source, args)
                    .map_err(|error| refusal_error(error, args.fern_strict))?;
            }
            Err(error)
        }
    }
}

fn source_refusals(source: &serde_json::Value, args: &crate::GenerateArgs) -> Result<()> {
    let mut filtered = OpenApi {
        yaml_unquoted_timestamps: None,
        openapi: String::new(),
        info: Default::default(),
        components: Default::default(),
        paths: Default::default(),
        webhooks: Default::default(),
        security: None,
        servers: Vec::new(),
        tags: Vec::new(),
        base_path_crozier: None,
        base_path_fern: None,
        idempotency_headers_crozier: None,
        idempotency_headers_fern: None,
        pagination_crozier: None,
        pagination_fern: None,
        global_headers_crozier: None,
        global_headers_fern: None,
        sdk_variables_crozier: None,
        sdk_variables_fern: None,
    };
    for (route, item) in source["paths"].as_object().into_iter().flatten() {
        let route = route.as_str();
        let mut metadata = serde_json::Map::new();
        for (method, op) in item.as_object().into_iter().flatten() {
            let Some(fields) = op.as_object() else {
                continue;
            };
            let extensions = fields
                .iter()
                .filter(|(key, _)| key.starts_with("x-"))
                .map(|(key, value)| (key.clone(), value.clone()))
                .collect();
            metadata.insert(method.clone(), serde_json::Value::Object(extensions));
        }
        if let Ok(item) =
            serde_json::from_value::<crate::openapi::PathItem>(serde_json::Value::Object(metadata))
        {
            filtered.paths.insert(route.to_owned(), item);
        }
    }
    crate::openapi::filter_ignored(&mut filtered);
    crate::openapi::filter_by_audience(&mut filtered, &args.audiences, args.audience_strict);
    source_type_names(source, &filtered, &args.spec)?;
    for (route, item) in &filtered.paths {
        for (method, _) in item.operations() {
            let op = &source["paths"][route][method.to_ascii_lowercase()];
            let body = source_target(source, &op["requestBody"]);
            for media in body["content"]
                .as_object()
                .into_iter()
                .flat_map(|mapping| mapping.values())
            {
                // A property an `allOf` member or a second parent redeclares is
                // one request property at Fern CLI 5.163.1, as `validate_names`
                // holds; only an own property beside a parent's collides.
                // The flattened inline shape also refuses a readOnly parent field
                // an own property redeclares, as `validate_names` does.
                let target = source_target(source, &media["schema"]);
                let mut own = Vec::new();
                for (key, property) in target["properties"].as_object().into_iter().flatten() {
                    if document_boolean(&source_target(source, property)["readOnly"]) != Some(true)
                    {
                        let wire = key.as_str();
                        own.push(request_property_name(property).unwrap_or(wire).to_owned());
                    }
                }
                let mut parents = Vec::new();
                for member in target["allOf"]
                    .as_array()
                    .into_iter()
                    .flatten()
                    .filter(|member| member["$ref"].is_string())
                {
                    source_request_properties(
                        source,
                        member,
                        &mut std::collections::HashSet::new(),
                        &mut parents,
                        false,
                    );
                }
                if let Some(name) = own
                    .iter()
                    .find(|name| parents.iter().any(|(_, parent)| parent == *name))
                {
                    return Err(refusal(&args.spec, Class::RequestPropertyNameCollision, format!("{} {route} body property {name:?} collides with another request property; give the properties distinct declared names", method.to_ascii_uppercase())));
                }
            }
        }
    }
    Ok(())
}

fn source_request_properties(
    source: &serde_json::Value,
    node: &serde_json::Value,
    visited: &mut std::collections::HashSet<String>,
    fields: &mut Vec<(String, String)>,
    request_only: bool,
) {
    if let Some(reference) = node["$ref"].as_str() {
        if !visited.insert(reference.to_owned()) {
            return;
        }
    }
    let node = source_target(source, node);
    if crate::openapi::refusal_node_ignored(node) {
        return;
    }
    for (key, property) in node["properties"].as_object().into_iter().flatten() {
        if request_only
            && document_boolean(&source_target(source, property)["readOnly"]) == Some(true)
        {
            continue;
        }
        let wire = key.as_str();
        fields.push((
            wire.to_owned(),
            request_property_name(property).unwrap_or(wire).to_owned(),
        ));
    }
    for member in node["allOf"].as_array().into_iter().flatten() {
        source_request_properties(source, member, visited, fields, request_only);
    }
}

fn validate_names(doc: &OpenApi, path: &Path, ir: &crate::ir::Ir) -> Result<()> {
    let source = source_document(path)?;
    source_type_names(&source, doc, path)?;
    for (route, _) in &doc.paths {
        let mut placeholders = std::collections::HashSet::new();
        for segment in route.split('{').skip(1) {
            if let Some((name, _)) = segment.split_once('}') {
                if !placeholders.insert(name) {
                    return Err(refusal(path, Class::DuplicatePathParameter, format!("route {route} repeats path parameter {name:?}; give each path position a distinct name")));
                }
            }
        }
    }
    for (name, schema) in &doc.components.schemas {
        check_schema(
            schema,
            &format!("#/components/schemas/{name}"),
            path,
            &doc.components.schemas,
        )?;
    }
    check_shared_parent_properties(doc, path)?;
    let mut methods = std::collections::HashSet::new();
    for (route, item) in &doc.paths {
        for (method, op) in item.operations() {
            if let (Some(group), Some(name)) = (op.sdk_group_name(), op.sdk_method_name()) {
                let qualified = format!("{}.{}", group.join("."), name);
                if !methods.insert(qualified.clone()) {
                    return Err(refusal(path, Class::SdkMethodCollision, format!("{method} {route} declares duplicate SDK method {qualified}; give the methods distinct declared names")));
                }
            }
            let location = format!("{method} {route}");
            let raw_operation = &source["paths"][route][method.to_ascii_lowercase()];
            let (mut names, declared): (Vec<String>, Vec<bool>) = op
                .parameters
                .iter()
                .map(|parameter| {
                    let raw = raw_operation["parameters"]
                        .as_array()
                        .into_iter()
                        .flatten()
                        .chain(
                            source["paths"][route]["parameters"]
                                .as_array()
                                .into_iter()
                                .flatten(),
                        )
                        .map(|node| source_target(&source, node))
                        .find(|node| {
                            node["name"].as_str() == Some(parameter.name.as_str())
                                && serde_json::from_value::<crate::openapi::ParameterLocation>(
                                    node["in"].clone(),
                                )
                                .ok()
                                    == parameter.location
                        });
                    let declared = raw.and_then(crate::openapi::refusal_parameter_name);
                    let name = declared.map(str::to_owned).unwrap_or_else(|| {
                        if parameter.location == Some(crate::openapi::ParameterLocation::Header) {
                            fern_header_declaration_name(&parameter.name)
                        } else {
                            parameter.name.clone()
                        }
                    });
                    (name, declared.is_some())
                })
                .unzip();
            // Fern's OpenAPI importer renames a path parameter that declares no
            // name of its own to `{name}PathParam` when a body property claims
            // its name (`ir::rename_claimed_path_params`), so only a path
            // parameter with a declared name still collides with a body
            // property. Measured at Fern CLI 5.163.1 / fern-python-sdk 5.41.3
            // (authored probe 549-request-property-name-collision); Fern CLI
            // 5.67.1 refused every such pair. The cross-location pairs below
            // are measured at the new pair too: those Fern generates past are
            // `generated_location_pair`'s, and the rest still refuse.
            // The rename reaches only the names Fern reserves (the body's own and
            // its `allOf` parents' own), so a path parameter the endpoint keeps
            // under its own name still collides with a grandparent's property:
            // measured at Fern CLI 5.163.1 / fern-python-sdk 5.41.3 (this
            // class's probe).
            let kept = |wire: &str| {
                ir.endpoints
                    .iter()
                    .find(|endpoint| endpoint.path == *route && endpoint.http_method == method)
                    .and_then(|endpoint| {
                        endpoint
                            .path_params
                            .iter()
                            .find(|param| param.wire_name == wire)
                    })
                    .is_some_and(|param| param.py_name == crate::naming::field_name(wire))
            };
            let path_names: std::collections::HashSet<String> = (0..op.parameters.len())
                .filter(|&index| {
                    op.parameters[index].location == Some(crate::openapi::ParameterLocation::Path)
                        && (declared[index] || kept(&op.parameters[index].name))
                })
                .map(|index| names[index].clone())
                .collect();
            // A header the client wrapper carries is no request property, so it
            // claims no name: measured at Fern CLI 5.163.1 / fern-python-sdk
            // 5.41.3, `X-Namespace` beside a `namespace` query parameter
            // collides only on a document where the header rides too few
            // operations to be promoted (this class's `header-query-*` shapes).
            let promoted = |parameter: &crate::openapi::Parameter| {
                parameter.location == Some(crate::openapi::ParameterLocation::Header)
                    && ir
                        .global_headers
                        .iter()
                        .any(|header| header.wire_name == parameter.name)
            };
            for (index, parameter) in op.parameters.iter().enumerate() {
                for (other_index, other) in op.parameters.iter().enumerate().take(index) {
                    if parameter.location != other.location
                        && names[index] == names[other_index]
                        && !promoted(parameter)
                        && !promoted(other)
                        && !generated_location_pair(
                            (parameter, declared[index]),
                            (other, declared[other_index]),
                        )
                    {
                        let class = if parameter.name == other.name {
                            Class::RequestPropertyCamelcaseCollision
                        } else {
                            Class::RequestPropertyNameCollision
                        };
                        return Err(refusal(path, class, format!("{location} parameters {:?} and {:?} in different locations declare the same request name {:?}; give them distinct names", parameter.name, other.name, names[index])));
                    }
                }
            }
            // A multipart body's properties are request properties beside the
            // operation's query and header parameters, and Fern renames neither
            // side: measured at Fern CLI 5.163.1 / fern-python-sdk 5.41.3, a
            // `deck` header or query parameter beside a multipart `deck` property
            // is refused (`Multiple request properties have the name deck`, this
            // class's `multipart-*` shapes), where a JSON body's field takes a
            // prefix instead.
            if let Some(body) = op.request_body.as_ref().filter(|body| {
                !body.content.keys().any(|media| {
                    let media = media.split(';').next().unwrap_or_default().trim();
                    media == "application/json" || media.ends_with("+json")
                })
            }) {
                for (media_type, media) in &body.content {
                    let Some(schema) = media
                        .schema
                        .as_ref()
                        .filter(|_| media_type.starts_with("multipart/form-data"))
                    else {
                        continue;
                    };
                    let mut properties = Vec::new();
                    collect_property_names(
                        schema,
                        &doc.components.schemas,
                        &mut std::collections::HashSet::new(),
                        &mut properties,
                        true,
                    );
                    if let Some((index, parameter)) =
                        op.parameters.iter().enumerate().find(|(index, parameter)| {
                            matches!(
                                parameter.location,
                                Some(
                                    crate::openapi::ParameterLocation::Query
                                        | crate::openapi::ParameterLocation::Header
                                )
                            ) && !promoted(parameter)
                                && properties.contains(&names[*index].as_str())
                        })
                    {
                        return Err(refusal(path, Class::RequestPropertyNameCollision, format!("{location} multipart body property {:?} collides with the {} parameter {:?}; give them distinct declared names", names[index], if parameter.location == Some(crate::openapi::ParameterLocation::Query) { "query" } else { "header" }, parameter.name)));
                    }
                }
            }
            // A placeholder no parameter declares has no declared name either.
            for segment in route.split('{').skip(1) {
                if let Some((name, _)) = segment.split_once('}') {
                    if !op.parameters.iter().any(|parameter| parameter.name == name) {
                        names.push(name.to_owned());
                    }
                }
            }
            let mut body_hints = std::collections::HashMap::new();
            let raw_body = source_target(&source, &raw_operation["requestBody"]);
            for media in raw_body["content"]
                .as_object()
                .into_iter()
                .flat_map(|mapping| mapping.values())
            {
                source_property_names(
                    &source,
                    &media["schema"],
                    &mut std::collections::HashSet::new(),
                    &mut body_hints,
                );
            }
            if let Some(body) = &op.request_body {
                for media in body.content.values() {
                    if let Some(schema) = &media.schema {
                        if schema.reference.is_some()
                            && !ir.endpoints.iter().any(|endpoint| {
                                endpoint.path == *route
                                    && endpoint.http_method == method
                                    && endpoint.body_schema_dropped
                            })
                        {
                            continue;
                        }
                        let mut properties = Vec::new();
                        collect_property_names(
                            schema,
                            &doc.components.schemas,
                            &mut std::collections::HashSet::new(),
                            &mut properties,
                            true,
                        );
                        let resolved = schema
                            .reference
                            .as_deref()
                            .and_then(|reference| reference.strip_prefix("#/components/schemas/"))
                            .and_then(|name| doc.components.schemas.get(name))
                            .unwrap_or(schema);
                        // A property an `allOf` member or a second parent
                        // redeclares is one request property: measured at Fern
                        // CLI 5.163.1 / fern-python-sdk 5.41.3 (this class's
                        // `body-*` controls; Mistral's `stream`), where 5.67.1
                        // refused it. An own property beside a parent's is
                        // refused below.
                        let mut body_names = std::collections::HashSet::new();
                        for name in properties {
                            let name = body_hints
                                .get(name)
                                .cloned()
                                .unwrap_or_else(|| name.to_owned());
                            if path_names.contains(&name) {
                                return Err(refusal(path, Class::RequestPropertyNameCollision, format!("{location} body property {name:?} collides with another request property; give the properties distinct declared names")));
                            }
                            if body_names.insert(name.clone()) {
                                names.push(name);
                            }
                        }
                        // An inline body with its own properties flattens its
                        // `$ref` parents' fields beside them. Fern refuses an own
                        // property a parent redeclares even when the parent's is
                        // readOnly (bodies-responses inline-body-overlap-refusals).
                        if !resolved.properties.is_empty() {
                            let mut parent_names = Vec::new();
                            for member in resolved
                                .all_of
                                .iter()
                                .flatten()
                                .filter(|member| member.reference.is_some())
                            {
                                collect_property_names(
                                    member,
                                    &doc.components.schemas,
                                    &mut std::collections::HashSet::new(),
                                    &mut parent_names,
                                    false,
                                );
                            }
                            let declared = |name: &str| {
                                body_hints
                                    .get(name)
                                    .cloned()
                                    .unwrap_or_else(|| name.to_owned())
                            };
                            let parent_names: std::collections::HashSet<String> =
                                parent_names.into_iter().map(declared).collect();
                            if let Some((name, _)) =
                                resolved.properties.iter().find(|(name, property)| {
                                    property.read_only != Some(true)
                                        && property
                                            .reference
                                            .as_deref()
                                            .and_then(|reference| {
                                                reference.strip_prefix("#/components/schemas/")
                                            })
                                            .and_then(|name| doc.components.schemas.get(name))
                                            .is_none_or(|target| target.read_only != Some(true))
                                        && parent_names.contains(&declared(name))
                                })
                            {
                                return Err(refusal(path, Class::RequestPropertyNameCollision, format!("{location} body property {:?} collides with another request property; give the properties distinct declared names", declared(name))));
                            }
                        }
                    }
                }
            }
            let mut parameter_names = std::collections::HashMap::new();
            // A header the client carries is no request property here either:
            // measured at Fern CLI 5.163.1 / fern-python-sdk 5.41.3, a lifted
            // `Page-Size` beside a `page_size` query parameter generates
            // (docs/fern-measurements/output-defects/612-parameter-location-collision),
            // where a `page-size` header on one operation is refused.
            // `names` holds the parameters' names, then the body properties'.
            for (index, name) in names.iter().enumerate() {
                if op.parameters.get(index).is_some_and(promoted) {
                    continue;
                }
                let identifier = crate::naming::to_snake_case(name)
                    .trim_matches('_')
                    .to_owned();
                if let Some(previous) = parameter_names.insert(identifier, name) {
                    if previous != name {
                        return Err(refusal(path, Class::RequestPropertyCamelcaseCollision, format!("{location} parameters {previous:?} and {name:?} normalize to the same identifier; give them distinct names")));
                    }
                }
            }
            for parameter in &op.parameters {
                if let Some(schema) = &parameter.schema {
                    check_schema(
                        schema,
                        &format!("{location} parameter {}", parameter.name),
                        path,
                        &doc.components.schemas,
                    )?;
                }
                for media in parameter.content.values() {
                    if let Some(schema) = &media.schema {
                        check_schema(
                            schema,
                            &format!("{location} parameter {}", parameter.name),
                            path,
                            &doc.components.schemas,
                        )?;
                    }
                }
            }
            if let Some(body) = &op.request_body {
                for media in body.content.values() {
                    if let Some(schema) = &media.schema {
                        // Fern emits a direct singleton scalar body as a literal,
                        // without forming an enum member. Descendants still need names.
                        let literal_body = schema.reference.is_none()
                            && schema
                                .enum_values
                                .as_ref()
                                .is_some_and(|values| values.len() == 1);
                        check_schema_names(
                            schema,
                            &format!("{location} request body"),
                            path,
                            &doc.components.schemas,
                            !literal_body,
                        )?;
                    }
                }
            }
            for (status, response) in &op.responses {
                for media in response.content.values() {
                    if let Some(schema) = &media.schema {
                        check_schema(
                            schema,
                            &format!("{location} response {status}"),
                            path,
                            &doc.components.schemas,
                        )?;
                    }
                }
            }
        }
    }
    Ok(())
}

// llmlint: ignore[contracts_have_one_source_or_a_drift_gate] Fern checks camelCase declaration names here, while IR emits snake_case Python parameters. Only X-prefix removal is shared through ir::header_param_stem; Python casing changes must not change the measured Fern declaration contract.
fn fern_header_declaration_name(wire: &str) -> String {
    let mut name = crate::naming::to_pascal_case(crate::ir::header_param_stem(wire));
    if let Some(first) = name.get_mut(..1) {
        first.make_ascii_lowercase();
    }
    name
}

fn source_document(path: &Path) -> Result<serde_json::Value> {
    let text = std::fs::read_to_string(path).map_err(|source| Error::ReadSpec {
        path: path.to_owned(),
        source,
    })?;
    crate::yaml::from_str(&text).map_err(|error| Error::ParseSpec {
        path: path.to_owned(),
        message: error.to_string(),
    })
}

fn source_target<'a>(
    source: &'a serde_json::Value,
    mut node: &'a serde_json::Value,
) -> &'a serde_json::Value {
    let mut visited = std::collections::HashSet::new();
    while let Some(reference) = node["$ref"]
        .as_str()
        .filter(|reference| reference.starts_with("#/"))
    {
        if !visited.insert(reference) {
            break;
        }
        let Some(target) = source_pointer_target(source, reference) else {
            break;
        };
        node = target;
    }
    node
}

fn source_pointer_target<'a>(
    source: &'a serde_json::Value,
    reference: &str,
) -> Option<&'a serde_json::Value> {
    let mut target = source;
    for part in reference.strip_prefix("#/")?.split('/') {
        let key = part.replace("~1", "/").replace("~0", "~");
        target = match target {
            serde_json::Value::Array(items) => {
                key.parse::<usize>().ok().and_then(|index| items.get(index))
            }
            _ => target.get(key.as_str()),
        }?;
    }
    (!target.is_null()).then_some(target)
}

fn source_property_names(
    source: &serde_json::Value,
    node: &serde_json::Value,
    visited: &mut std::collections::HashSet<String>,
    names: &mut std::collections::HashMap<String, String>,
) {
    if let Some(reference) = node["$ref"].as_str() {
        if !visited.insert(reference.to_owned()) {
            return;
        }
    }
    let node = source_target(source, node);
    for (key, property) in node["properties"].as_object().into_iter().flatten() {
        let wire = key.as_str();
        if let Some(name) = request_property_name(property) {
            names.insert(wire.to_owned(), name.to_owned());
        }
    }
    for member in node["allOf"].as_array().into_iter().flatten() {
        source_property_names(source, member, visited, names);
    }
}

/// Whether Fern generates past two parameters in different locations that share
/// a request name, so neither is refused. Measured at Fern CLI 5.163.1 /
/// fern-python-sdk 5.41.3
/// (`docs/fern-measurements/output-defects/612-parameter-location-collision/`):
/// `fern check` reports the pair, but `fern generate` writes an SDK past it.
/// A cookie parameter never reaches the signature, so it collides with
/// nothing; and the importer renames a path parameter declaring no name of its
/// own to `{name}PathParam` when a query parameter or header has its very wire
/// name (`ir::rename_claimed_path_params`). Two names that only normalize alike
/// (`shelf_id` beside `shelfId`) still refuse: Fern refuses them too.
fn generated_location_pair(
    (parameter, declared): (&crate::openapi::Parameter, bool),
    (other, other_declared): (&crate::openapi::Parameter, bool),
) -> bool {
    use crate::openapi::ParameterLocation::{Cookie, Header, Path, Query};
    let renamed_path = |path: &crate::openapi::Parameter,
                        path_declared: bool,
                        claimant: &crate::openapi::Parameter| {
        path.location == Some(Path)
            && !path_declared
            && matches!(claimant.location, Some(Query | Header))
            && claimant.name == path.name
    };
    parameter.location == Some(Cookie)
        || other.location == Some(Cookie)
        || renamed_path(parameter, declared, other)
        || renamed_path(other, other_declared, parameter)
}

/// The request name a body property declares: its `x-crozier-property-name` /
/// `x-fern-property-name` — the Fern definition `name` the collision check
/// compares — else the parameter-name spelling this validator also reads.
fn request_property_name(property: &serde_json::Value) -> Option<&str> {
    crate::openapi::refusal_property_name(property)
        .or_else(|| crate::openapi::refusal_parameter_name(property))
}

/// Refuse an `allOf` whose `$ref` parents Fern flattens into one object that
/// redeclares a property one of them inherits. Measured at Fern CLI 5.163.1 /
/// fern-python-sdk 5.41.3 (this class's probe and shapes): a response
/// `allOf: [CollectionResponse, CommonFailure]`, where both parents declare
/// `result` and `CollectionResponse` also inherits it from its own `$ref`
/// parent, fails `fern check` and `fern generate` with `Object has multiple
/// properties named "result"`. Two parents declaring it with no inheritance, a
/// second parent not declaring it, a single parent, and an object redeclaring
/// its one parent's property all generate.
fn check_shared_parent_properties(doc: &OpenApi, path: &Path) -> Result<()> {
    let schemas = &doc.components.schemas;
    let refuse = |schema: &Schema, location: &str| {
        match shared_parent_property(schema, schemas) {
        Some(name) => Err(refusal(path, Class::ObjectPropertyNameCollision, format!("{location} property {name:?} is declared by two `allOf` parents and inherited by one; give the parents distinct property names"))),
        None => Ok(()),
    }
    };
    for (name, schema) in schemas {
        refuse(schema, &format!("#/components/schemas/{name}"))?;
    }
    for (route, item) in &doc.paths {
        for (method, op) in item.operations() {
            for (code, response) in &op.responses {
                for media in response.content.values() {
                    if let Some(schema) = &media.schema {
                        refuse(schema, &format!("{method} {route} response {code}"))?;
                    }
                }
            }
            for media in op
                .request_body
                .iter()
                .flat_map(|body| body.content.values())
            {
                if let Some(schema) = &media.schema {
                    refuse(schema, &format!("{method} {route} request body"))?;
                }
            }
        }
    }
    Ok(())
}

/// The property two or more of `schema`'s `$ref` parents declare (at any depth)
/// where one of them reaches it through a `$ref` parent of its own.
fn shared_parent_property(
    schema: &Schema,
    schemas: &indexmap::IndexMap<String, Schema>,
) -> Option<String> {
    let parents: Vec<&Schema> = schema
        .all_of
        .iter()
        .flatten()
        .filter_map(|member| {
            schemas.get(
                member
                    .reference
                    .as_deref()?
                    .strip_prefix("#/components/schemas/")?,
            )
        })
        .collect();
    if parents.len() < 2 {
        return None;
    }
    let declared: Vec<Vec<&str>> = parents
        .iter()
        .map(|parent| {
            let mut names = Vec::new();
            collect_property_names(
                parent,
                schemas,
                &mut std::collections::HashSet::new(),
                &mut names,
                false,
            );
            names
        })
        .collect();
    for (index, parent) in parents.iter().enumerate() {
        let mut inherited = Vec::new();
        for member in parent
            .all_of
            .iter()
            .flatten()
            .filter(|member| member.reference.is_some())
        {
            collect_property_names(
                member,
                schemas,
                &mut std::collections::HashSet::new(),
                &mut inherited,
                false,
            );
        }
        if let Some(name) = inherited.into_iter().find(|name| {
            declared
                .iter()
                .enumerate()
                .any(|(other, names)| other != index && names.contains(name))
        }) {
            return Some(name.to_owned());
        }
    }
    None
}

fn collect_property_names<'a>(
    schema: &'a Schema,
    schemas: &'a indexmap::IndexMap<String, Schema>,
    visited: &mut std::collections::HashSet<&'a str>,
    names: &mut Vec<&'a str>,
    request_only: bool,
) {
    if let Some(reference) = &schema.reference {
        if let Some(name) = reference.strip_prefix("#/components/schemas/") {
            if visited.insert(name) {
                if let Some(target) = schemas.get(name) {
                    collect_property_names(target, schemas, visited, names, request_only);
                }
            }
        }
    }
    names.extend(
        schema
            .properties
            .iter()
            .filter(|(_, property)| {
                !request_only
                    || (property.read_only != Some(true)
                        && property
                            .reference
                            .as_deref()
                            .and_then(|reference| reference.strip_prefix("#/components/schemas/"))
                            .and_then(|name| schemas.get(name))
                            .is_none_or(|target| target.read_only != Some(true)))
            })
            .map(|(name, _)| name.as_str()),
    );
    for member in schema.all_of.iter().flatten() {
        collect_property_names(member, schemas, visited, names, request_only);
    }
}

fn check_schema(
    schema: &Schema,
    location: &str,
    path: &Path,
    schemas: &indexmap::IndexMap<String, Schema>,
) -> Result<()> {
    check_schema_names(schema, location, path, schemas, true)
}

fn check_schema_names(
    schema: &Schema,
    location: &str,
    path: &Path,
    schemas: &indexmap::IndexMap<String, Schema>,
    check_enum: bool,
) -> Result<()> {
    // An object redeclaring a property its nullable `allOf` base declares is
    // generated, one field per name, since Fern CLI 5.163.1 (authored probe
    // 549-object-property-name-collision); Fern CLI 5.67.1 refused it.
    let explicit = schema.discriminator.as_ref().filter(|_| {
        schema.ty.as_ref().map_or(
            schema.enum_values.is_none() && (schema.any_of.is_none() || schema.one_of.is_some()),
            |ty| ty.primary() == Some("object"),
        )
    });
    // A discriminator that declares the tag's Python name is named by that:
    // the hand-written `telescope-renamed-discriminant` fixture renames `$class`
    // with `x-fern-property-name`, and Fern generates the union.
    let discriminant = explicit
        .map(|tag| {
            tag.declared_property_name()
                .unwrap_or(&tag.property_name)
                .to_string()
        })
        .or_else(|| crate::ir::inferred_discriminant_property(schema, schemas));
    if let Some(discriminant) = discriminant.filter(|name| !usable_name(name)) {
        return Err(refusal(path, Class::DiscriminantValueUnsuitable, format!(
                "{location} discriminant {discriminant:?}; use a letter-led identifier containing letters, numbers and underscores"
            )));
    }
    // Measured at Fern CLI 5.67.1 (not re-measured at the certified pair):
    // invalid overrides warn and fall back to the original value, so they
    // cannot rescue a value Fern cannot name.
    let names: std::collections::BTreeMap<_, _> = schema
        .enum_member_names()
        .filter(|(_, name)| usable_name(name))
        .collect();
    if let Some(values) = schema.enum_values.as_ref().filter(|_| check_enum) {
        // Integer enums and mixed-kind enums do not declare string enum members
        // in Fern. Bungie's integer bit flags even spell their values as strings.
        let string_enum = schema.ty.as_ref().map_or_else(
            || values.iter().all(serde_json::Value::is_string),
            |ty| {
                ty.primary() == Some("string")
                    && values
                        .iter()
                        .all(|value| value.is_string() || value.is_null())
            },
        );
        if !string_enum {
            return check_children(schema, location, path, schemas);
        }
        for value in values.iter().filter_map(serde_json::Value::as_str) {
            if names.contains_key(value) {
                continue;
            }
            let member = crate::naming::enum_member_name(value);
            let bare_number = !value.is_empty() && value.bytes().all(|byte| byte.is_ascii_digit());
            if (member == "_" && !value.is_ascii()) || (bare_number && member.starts_with('_')) {
                return Err(refusal(
                    path,
                    Class::EnumValueUnnameable,
                    format!(
                        "{location} enum value {value:?}; declare a usable name with x-crozier-enum"
                    ),
                ));
            }
            let starts_with_unspelled_digit = !value.starts_with(|ch: char| ch.is_ascii_digit())
                && value
                    .trim_start_matches(|ch: char| !ch.is_alphanumeric())
                    .starts_with(|ch: char| ch.is_ascii_digit());
            if member.starts_with('_') || starts_with_unspelled_digit {
                return Err(refusal(
                    path,
                    Class::EnumNameUnsuitable,
                    format!(
                        "{location} enum value {value:?}; declare a usable name with x-crozier-enum"
                    ),
                ));
            }
        }
    }
    check_children(schema, location, path, schemas)
}

fn usable_name(name: &str) -> bool {
    name.starts_with(|ch: char| ch.is_ascii_alphabetic())
        && name
            .bytes()
            .all(|byte| byte.is_ascii_alphanumeric() || byte == b'_')
}

fn check_children(
    schema: &Schema,
    location: &str,
    path: &Path,
    schemas: &indexmap::IndexMap<String, Schema>,
) -> Result<()> {
    for (name, child) in &schema.properties {
        check_schema(
            child,
            &format!("{location}/properties/{name}"),
            path,
            schemas,
        )?;
    }
    if let Some(child) = &schema.items {
        check_schema(child, &format!("{location}/items"), path, schemas)?;
    }
    if let Some(AdditionalProperties::Schema(child)) = &schema.additional_properties {
        check_schema(
            child,
            &format!("{location}/additionalProperties"),
            path,
            schemas,
        )?;
    }
    for (kind, children) in [
        ("allOf", &schema.all_of),
        ("oneOf", &schema.one_of),
        ("anyOf", &schema.any_of),
    ] {
        if let Some(children) = children {
            for (index, child) in children.iter().enumerate() {
                check_schema(child, &format!("{location}/{kind}/{index}"), path, schemas)?;
            }
        }
    }
    Ok(())
}

/// Compare names after lowering, before any output directory is created.
pub(crate) fn validate_ir(
    ir: &crate::ir::Ir,
    doc: &OpenApi,
    path: &Path,
    strict: bool,
) -> Result<()> {
    for decl in ir
        .types
        .iter()
        .chain(ir.tag_types.iter().map(|tag| &tag.decl))
    {
        if decl.module().len() + ".py".len() > 255 {
            return Err(refusal_error(refusal(path, Class::GeneratedFileNameTooLong, format!("type {} would write {}.py, exceeding the filename limit; shorten its declared name or nested property names", decl.name(), decl.module())), strict));
        }
    }
    let mut component_names = std::collections::HashMap::new();
    for (name, schema) in &doc.components.schemas {
        if schema
            .ty
            .as_ref()
            .and_then(|ty| ty.primary())
            .is_some_and(|ty| ty != "object")
            && schema.enum_values.is_none()
        {
            continue;
        }
        let normalized = crate::naming::class_name(name);
        if let Some(previous) = component_names.insert(normalized.clone(), name) {
            if previous.get(1..) != name.get(1..) {
                continue;
            }
            return Err(refusal_error(refusal(path, Class::TypeNameCollision, format!("component schemas {previous:?} and {name:?} both declare type {normalized}; give them distinct names")), strict));
        }
    }
    let roots: std::collections::HashSet<_> = doc
        .components
        .schemas
        .keys()
        .map(|name| crate::naming::class_name(name))
        .collect();
    let mut request_names = std::collections::HashMap::new();
    for (route, item) in &doc.paths {
        for (method, op) in item.operations() {
            if ir.endpoints.iter().any(|endpoint| {
                endpoint.path == *route
                    && endpoint.http_method == method
                    && endpoint.body_schema_dropped
            }) {
                for body in op.request_body.iter() {
                    for media in body.content.values() {
                        if let Some(reference) = media
                            .schema
                            .as_ref()
                            .and_then(|schema| schema.reference.as_deref())
                        {
                            if let Some((parent, schema)) = reference
                                .strip_prefix("#/components/schemas/")
                                .and_then(|name| {
                                    doc.components
                                        .schemas
                                        .get(name)
                                        .map(|schema| (name, schema))
                                })
                            {
                                for (property, field) in &schema.properties {
                                    let name = crate::naming::child_class_name(parent, property);
                                    if field.enum_values.as_ref().is_some_and(|values| {
                                        values.len() > 1
                                            && values.iter().all(serde_json::Value::is_string)
                                    }) && roots.contains(&name)
                                    {
                                        return Err(refusal_error(refusal(path, Class::TypeNameCollision, format!("{method} {route} body property {property:?} declares enum {name}, already declared by a component schema; give the declarations distinct names")), strict));
                                    }
                                }
                            }
                        }
                    }
                }
            }
            // A `stream-condition` operation's two halves each take a request
            // type Fern synthesizes: `{Ctx}Request` and `{Ctx}StreamRequest`. A
            // component schema of either name, the body's own or any other, is
            // "already declared in this file" to pinned Fern, which
            // refuses rather than renames:
            // docs/fern-refusals/type-name-collision/evidence/stream-split-*.
            if op.request_body.is_some()
                && op
                    .streaming()
                    .and_then(crate::openapi::Streaming::condition_property)
                    .is_some()
            {
                let context = crate::ir::endpoint_pascal_context(op, method, route);
                for name in [
                    format!("{context}Request"),
                    format!("{context}StreamRequest"),
                ] {
                    if let Some(component) = doc
                        .components
                        .schemas
                        .keys()
                        .find(|component| crate::naming::class_name(component) == name)
                    {
                        return Err(refusal_error(refusal(path, Class::TypeNameCollision, format!("{method} {route} stream-condition request type {name} collides with component schema {component:?}; give the schema another name, or the method another x-fern-sdk-method-name")), strict));
                    }
                }
            }
            let inline_body = op.request_body.as_ref().is_some_and(|body| {
                body.content.values().any(|media| {
                    media.schema.as_ref().is_some_and(|schema| {
                        schema.reference.is_none() && !schema.properties.is_empty()
                    })
                })
            });
            let has_request =
                (!op.parameters.is_empty() && op.request_body.is_none()) || inline_body;
            if has_request {
                let name = format!(
                    "{}Request",
                    crate::ir::endpoint_pascal_context(op, method, route)
                );
                let namespace = crate::ir::endpoint_module(op, route);
                let duplicate = op.sdk_method_name().is_none()
                    && op.operation_id.as_deref().is_some_and(|id| {
                        request_names
                            .insert(id.to_owned(), namespace.clone())
                            .is_some_and(|previous| previous != namespace)
                    });
                // A multipart field uses this existing component; no second
                // whole-request type is declared for its flattened form.
                let request_collision = inline_body
                    && roots.contains(&name)
                    && ir.types.iter().any(|decl| decl.name() == name);
                let multipart_existing_request = request_collision
                    && ir.types.iter().any(|decl| {
                        matches!(decl, crate::ir::TypeDecl::Object(object) if object.name == name)
                    })
                    && op.request_body.as_ref().is_some_and(|body| {
                        body.content.len() == 1
                            && body
                                .content
                                .get("multipart/form-data")
                                .is_some_and(|media| {
                                    media.schema.as_ref().is_some_and(|schema| {
                                        schema.reference.is_none()
                                            && schema.properties.values().any(|field| {
                                                field.reference.as_deref().is_some_and(
                                                    |reference| {
                                                        reference
                                                            .strip_prefix("#/components/schemas/")
                                                            == Some(name.as_str())
                                                    },
                                                )
                                            })
                                    })
                                })
                    });
                if (request_collision && !multipart_existing_request) || duplicate {
                    return Err(refusal_error(refusal(path, Class::TypeNameCollision, format!("{method} {route} request type {name} collides with another declaration; give the types distinct declared names")), strict));
                }
            }
        }
    }
    // Pinned Fern accepts a header parameter's enum named like a root
    // schema (it checks and generates), while a query parameter's is "already
    // declared": docs/fern-refusals/type-name-collision/evidence/
    // namespaced-header-enum-*.pinned-fern.log.
    let header_enums: std::collections::HashSet<String> = doc
        .paths
        .iter()
        .flat_map(|(route, item)| {
            item.operations().into_iter().flat_map(move |(method, op)| {
                let context = crate::ir::request_context(op, method, route);
                op.parameters
                    .iter()
                    .filter(|parameter| {
                        parameter.location == Some(crate::openapi::ParameterLocation::Header)
                    })
                    .map(move |parameter| {
                        crate::ir::request_parameter_type_name(&context, &parameter.name)
                    })
            })
        })
        .collect();
    for tag in &ir.tag_types {
        if matches!(tag.decl, crate::ir::TypeDecl::Enum(_))
            && !tag.module.is_empty()
            && !tag.module.contains('/')
            && roots.contains(tag.decl.name())
            && !header_enums.contains(tag.decl.name())
        {
            return Err(refusal_error(refusal(path, Class::TypeNameCollision, format!("enum {} in namespace {} collides with a schema declaration; give the types distinct declared names", tag.decl.name(), tag.module)), strict));
        }
    }
    let mut names = std::collections::HashMap::new();
    for (namespace, decl) in ir.types.iter().map(|decl| ("", decl)).chain(
        ir.tag_types
            .iter()
            .map(|tag| (tag.module.as_str(), &tag.decl)),
    ) {
        if let Some(previous) = names.insert(decl.name(), namespace) {
            if previous != namespace
                && !(header_enums.contains(decl.name())
                    && (previous.is_empty() || namespace.is_empty()))
                && previous
                    .rsplit_once('/')
                    .map(|(parent, _)| parent)
                    .unwrap_or("")
                    == namespace
                        .rsplit_once('/')
                        .map(|(parent, _)| parent)
                        .unwrap_or("")
            {
                return Err(refusal_error(refusal(path, Class::TypeNameCollision, format!("type {} is declared in namespaces {previous:?} and {namespace:?}; give the types distinct declared names", decl.name())), strict));
            }
        }
    }
    Ok(())
}

/// A component schema's source node without its declared type name, so two
/// declarations of one name compare on the schema they declare.
fn without_type_names(node: &serde_json::Value) -> serde_json::Value {
    let mut node = node.clone();
    if let Some(fields) = node.as_object_mut() {
        fields.remove("x-crozier-type-name");
        fields.remove("x-fern-type-name");
    }
    node
}

fn source_type_names(source: &serde_json::Value, doc: &OpenApi, path: &Path) -> Result<()> {
    let mut types: std::collections::HashMap<String, (&str, bool, serde_json::Value)> =
        std::collections::HashMap::new();
    for (name, node) in source["components"]["schemas"]
        .as_object()
        .into_iter()
        .flatten()
    {
        let name = name.as_str();
        if crate::openapi::refusal_node_ignored(node) {
            continue;
        }
        let declared = crate::openapi::refusal_type_name(node).unwrap_or(name);
        // A type name declared by one component and resolved to by another
        // (its own key or declaration) is one type to Fern, which merges them;
        // it generates the merge of two identical schemas and refuses two that
        // differ (the authored probe `376-350-declared-type-name-shared`; the
        // refusals are this class's `evidence/376-350-declared-type-name-*`).
        let hinted = crate::openapi::refusal_type_name(node).is_some();
        let body = without_type_names(node);
        let resolved = crate::openapi::declared_type_key(declared);
        if let Some((previous, previous_hinted, previous_body)) = types.get(&resolved) {
            if (hinted || *previous_hinted) && *previous_body != body {
                return Err(refusal(path, Class::TypeNameCollision, format!("component schemas {previous:?} and {name:?} both declare type {resolved} with different schemas; give them distinct names")));
            }
        } else {
            types.insert(resolved, (name, hinted, body));
        }
        let numeric = declared.chars().all(|ch| ch.is_ascii_digit())
            && declared.parse::<u64>().is_ok_and(|number| number > 9999);
        let relative_alias = node["$ref"].as_str().is_some_and(|reference| {
            !reference.starts_with('#')
                && !reference.contains("://")
                && !path
                    .parent()
                    .unwrap_or_else(|| Path::new("."))
                    .join(reference.split('#').next().unwrap_or(reference))
                    .is_file()
        });
        if numeric || relative_alias {
            return Err(refusal(path, Class::TypeNameNotLetterLed, format!("#/components/schemas/{name} cannot form a letter-led type name; give it a valid declared type name")));
        }
        if property_reference_cycle(source, node, &mut std::collections::HashSet::new()) {
            return Err(refusal(path, Class::GeneratedFileNameTooLong, format!("#/components/schemas/{name} has a recursive inline property reference whose generated filename grows without bound; use a named component reference")));
        }
        source_reference_names(source, node, &format!("#/components/schemas/{name}"), path)?;
    }
    // An inline schema declaring a type name is lifted into that type (see
    // `openapi::normalize_inline_declared_type_names`), so a name already held
    // by a component or an earlier inline declaration is one type to Fern: it
    // generates the merge of an identical schema and refuses one that differs
    // (this class's `evidence/inline-declared-type-name-*`).
    let mut held: std::collections::HashMap<String, (String, serde_json::Value)> = types
        .iter()
        .map(|(key, (name, _, body))| {
            (
                key.clone(),
                (format!("component schema {name:?}"), body.clone()),
            )
        })
        .collect();
    for (name, node) in source["components"]["schemas"]
        .as_object()
        .into_iter()
        .flatten()
    {
        let name = name.as_str();
        inline_type_names(
            node,
            &format!("#/components/schemas/{name}"),
            &mut held,
            path,
        )?;
    }
    for (route, item) in &doc.paths {
        for (method, op) in item.operations() {
            if !crate::ir::endpoint_module(op, route).is_empty() {
                continue;
            }
            let operation = &source["paths"][route][method.to_ascii_lowercase()];
            let mut bodies = vec![source_target(source, &operation["requestBody"])];
            bodies.extend(
                operation["responses"]
                    .as_object()
                    .into_iter()
                    .flat_map(|mapping| mapping.values())
                    .map(|response| source_target(source, response)),
            );
            for media in bodies.into_iter().flat_map(|body| {
                body["content"]
                    .as_object()
                    .into_iter()
                    .flat_map(|mapping| mapping.values())
            }) {
                inline_type_names(
                    &media["schema"],
                    &format!("{method} {route}"),
                    &mut held,
                    path,
                )?;
            }
        }
    }
    for (route, item) in &doc.paths {
        for (method, _) in item.operations() {
            let operation = &source["paths"][route][method.to_ascii_lowercase()];
            let mut schemas = Vec::new();
            for parameter in operation["parameters"].as_array().into_iter().flatten() {
                schemas.push(&source_target(source, parameter)["schema"]);
            }
            let body = source_target(source, &operation["requestBody"]);
            for media in body["content"]
                .as_object()
                .into_iter()
                .flat_map(|mapping| mapping.values())
            {
                schemas.push(&media["schema"]);
            }
            for response in operation["responses"]
                .as_object()
                .into_iter()
                .flat_map(|mapping| mapping.values())
            {
                for media in source_target(source, response)["content"]
                    .as_object()
                    .into_iter()
                    .flat_map(|mapping| mapping.values())
                {
                    schemas.push(&media["schema"]);
                }
            }
            for schema in schemas {
                source_reference_names(source, schema, &format!("{method} {route}"), path)?;
            }
        }
    }
    for (event, item) in &doc.webhooks {
        for (method, _) in item.operations() {
            let operation = &source["webhooks"][event][method.to_ascii_lowercase()];
            let body = source_target(source, &operation["requestBody"]);
            for media in body["content"]
                .as_object()
                .into_iter()
                .flat_map(|mapping| mapping.values())
            {
                source_reference_names(
                    source,
                    &media["schema"],
                    &format!("webhook {event}"),
                    path,
                )?;
            }
        }
    }
    Ok(())
}

/// Refuse an inline schema under `node` whose declared type name is already
/// held by a different schema, recording each new declaration in `held` in the
/// order the lifting reads them: properties, items, map values, then members.
fn inline_type_names(
    node: &serde_json::Value,
    location: &str,
    held: &mut std::collections::HashMap<String, (String, serde_json::Value)>,
    path: &Path,
) -> Result<()> {
    if node.get("$ref").is_some() || crate::openapi::refusal_node_ignored(node) {
        return Ok(());
    }
    let mut children: Vec<&serde_json::Value> = node["properties"]
        .as_object()
        .into_iter()
        .flat_map(|mapping| mapping.values())
        .collect();
    children.push(&node["items"]);
    children.push(&node["additionalProperties"]);
    for members in ["oneOf", "anyOf", "allOf"] {
        children.extend(node[members].as_array().into_iter().flatten());
    }
    for child in children {
        if !child.is_object() || child.get("$ref").is_some() {
            continue;
        }
        if let Some(declared) = crate::openapi::refusal_type_name(child) {
            let key = crate::openapi::declared_type_key(declared);
            let body = without_type_names(child);
            match held.get(&key) {
                Some((holder, held_body)) if *held_body != body => {
                    return Err(refusal(path, Class::TypeNameCollision, format!("{location} declares type {key} inline with a different schema than {holder}; give them distinct declared type names")));
                }
                Some(_) => {}
                None => {
                    held.insert(key, (format!("the inline declaration in {location}"), body));
                }
            }
        }
        inline_type_names(child, location, held, path)?;
    }
    Ok(())
}

fn source_reference_names(
    source: &serde_json::Value,
    node: &serde_json::Value,
    location: &str,
    path: &Path,
) -> Result<()> {
    if crate::openapi::refusal_node_ignored(node) {
        return Ok(());
    }
    if let Some(reference) = node["$ref"].as_str() {
        // Only a reference that resolves: measured at Fern CLI 5.163.1, one into a
        // document with no such `definitions` member generates
        // (`missing-definitions-ref` control; Gestor's `#/definitions/Contacto`).
        if (reference.starts_with("#/definitions/") || reference.starts_with("#/webhooks/"))
            && source_pointer_target(source, reference).is_some()
        {
            let target = source_target(source, node);
            if target["type"].as_str() == Some("object") || target["properties"].is_object() {
                return Err(refusal(path, Class::TypeNameNotLetterLed, format!("{location} reference {reference:?} forms an empty object type name; use a component schema reference")));
            }
        }
        return Ok(());
    }
    for property in node["properties"]
        .as_object()
        .into_iter()
        .flat_map(|mapping| mapping.values())
    {
        source_reference_names(source, property, location, path)?;
    }
    for key in ["items", "additionalProperties"] {
        if node[key].is_object() {
            source_reference_names(source, &node[key], location, path)?;
        }
    }
    for key in ["allOf", "oneOf", "anyOf"] {
        for member in node[key].as_array().into_iter().flatten() {
            source_reference_names(source, member, location, path)?;
        }
    }
    Ok(())
}

fn property_reference_cycle(
    source: &serde_json::Value,
    node: &serde_json::Value,
    stack: &mut std::collections::HashSet<String>,
) -> bool {
    if let Some(reference) = node["$ref"].as_str() {
        if !reference.starts_with("#/components/schemas/") || !reference.contains("/properties/") {
            return false;
        }
        if !stack.insert(reference.to_owned()) {
            return true;
        }
        let cycle = source_pointer_target(source, reference)
            .is_some_and(|target| property_reference_cycle(source, target, stack));
        stack.remove(reference);
        return cycle;
    }
    node["properties"]
        .as_object()
        .into_iter()
        .flat_map(|mapping| mapping.values())
        .any(|property| property_reference_cycle(source, property, stack))
        || (node["items"].is_object() && property_reference_cycle(source, &node["items"], stack))
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn a_legacy_definitions_reference_is_refused_only_where_it_resolves() {
        let class = Path::new(env!("CARGO_MANIFEST_DIR"))
            .join("docs/fern-refusals/type-name-not-letter-led");
        let verdict = |shape: &str| {
            let path = class.join(shape);
            let source: serde_json::Value =
                crate::yaml::from_str(&std::fs::read_to_string(&path).unwrap()).unwrap();
            let manager = &source["components"]["schemas"]["Manager"];
            source_reference_names(&source, manager, "#/components/schemas/Manager", &path)
                .err()
                .map(|error| error.to_string())
        };
        let error = verdict("legacy-definitions-ref-probe.yml").unwrap_or_default();
        assert!(
            error.contains("type-name-not-letter-led: #/components/schemas/Manager reference \"#/definitions/Contact\""),
            "{error}"
        );
        assert_eq!(verdict("missing-definitions-ref-control.yml"), None);
    }

    #[test]
    fn multipart_existing_request_component_is_not_a_second_declaration() {
        let fixture = Path::new(env!("CARGO_MANIFEST_DIR"))
            .join("docs/openapi-surface/handwritten/multipart-request-name/openapi.yml");
        let mut doc = crate::openapi::load(&fixture).unwrap();
        let config = crate::config::GenerateConfig::new(
            fixture.clone(),
            "out".into(),
            Some("fern".into()),
            None,
            None,
            crate::settings::ExtraFields::default(),
            "Cabinet",
        )
        .unwrap();
        let check =
            |doc: &OpenApi| validate_ir(&crate::ir::build(doc, &config), doc, &fixture, false);
        check(&doc).unwrap();
        let object = doc
            .components
            .schemas
            .get_mut("UploadEmblemRequest")
            .unwrap();
        let original = object.clone();
        *object = crate::yaml::from_str("type: string\nenum: [blue, green]\n").unwrap();
        let error = check(&doc).unwrap_err().to_string();
        assert!(error.contains("type-name-collision"), "{error}");
        doc.components
            .schemas
            .insert("UploadEmblemRequest".into(), original);
        let operation = doc
            .paths
            .get_mut("/emblems")
            .unwrap()
            .post
            .as_mut()
            .unwrap();
        let content = &mut operation.request_body.as_mut().unwrap().content;
        let media = content.shift_remove("multipart/form-data").unwrap();
        content.insert("application/json".into(), media);
        let error = check(&doc).unwrap_err().to_string();
        assert!(
            error.contains("type-name-collision") && error.contains("UploadEmblemRequest"),
            "{error}"
        );
    }

    /// `validate`'s refusal line over a committed registry shape, or `None` when it generates.
    fn shape_refusal(shape: &str) -> Option<String> {
        let path = Path::new(env!("CARGO_MANIFEST_DIR"))
            .join("docs/fern-refusals")
            .join(shape);
        let doc = crate::openapi::load(&path).unwrap();
        let config = crate::config::GenerateConfig::new(
            path.clone(),
            "out".into(),
            Some("fern".into()),
            None,
            None,
            crate::settings::ExtraFields::default(),
            "Api",
        )
        .unwrap();
        validate(&doc, &path, false, &crate::ir::build(&doc, &config))
            .err()
            .map(|error| error.to_string())
    }

    /// `validate`'s refusal line over `source`, or `None` when it generates.
    fn document_refusal(source: &str) -> Option<String> {
        let dir = tempfile::tempdir().unwrap();
        let path = dir.path().join("openapi.yml");
        std::fs::write(&path, source).unwrap();
        let doc = crate::openapi::load(&path).unwrap();
        let config = crate::config::GenerateConfig::new(
            path.clone(),
            "out".into(),
            Some("fern".into()),
            None,
            None,
            crate::settings::ExtraFields::default(),
            "Api",
        )
        .unwrap();
        validate(&doc, &path, false, &crate::ir::build(&doc, &config))
            .err()
            .map(|error| error.to_string())
    }

    /// Measured at Fern CLI 5.163.1 / fern-python-sdk 5.41.3
    /// (docs/fern-measurements/output-defects/612-parameter-location-collision):
    /// Fern generates past a path parameter sharing its wire name with a query
    /// parameter or a header, renaming the path parameter, and past any
    /// parameter sharing a name with a cookie, which it drops. A pair the
    /// importer does not rename is refused as before.
    #[test]
    fn parameters_fern_generates_past_in_different_locations_are_not_refused() {
        let source = std::fs::read_to_string(Path::new(env!("CARGO_MANIFEST_DIR")).join(
            "docs/fern-measurements/output-defects/612-parameter-location-collision/openapi.yml",
        ))
        .unwrap();
        assert_eq!(document_refusal(&source), None);
        // A path parameter declaring its own name is not renamed, so it collides.
        let declared = source.replacen(
            "        - name: shelf\n          in: path\n",
            "        - name: shelf\n          in: path\n          x-fern-parameter-name: shelf\n",
            1,
        );
        assert_ne!(declared, source, "the measurement's path parameter moved");
        let error = document_refusal(&declared).unwrap_or_default();
        assert!(
            error.contains(
                "request-property-camelcase-collision: GET /branches/{branch}/shelves/{shelf} parameters \"shelf\" and \"shelf\" in different locations"
            ),
            "{error}"
        );
        // A query parameter beside a header on one operation is not renamed.
        let query_header = source.replace("          in: cookie\n", "          in: header\n");
        let error = document_refusal(&query_header).unwrap_or_default();
        assert!(
            error
                .contains("GET /loans parameters \"patron\" and \"patron\" in different locations"),
            "{error}"
        );
        // A `Page-Size` header the client carries claims no request name, but
        // on one operation it is a request property `page_size` normalizes to.
        let page_size = "        - $ref: '#/components/parameters/PageSizeHeader'\n";
        let one_operation = source.replacen(page_size, "", 2);
        assert_eq!(one_operation.matches(page_size).count(), 1);
        let error = document_refusal(&one_operation).unwrap_or_default();
        assert!(
            error.contains("GET /loans parameters \"pageSize\" and \"page_size\" normalize to the same identifier"),
            "{error}"
        );
        // Names that only normalize alike are not renamed either.
        let normalized = source.replace(
            "        - name: shelf\n          in: query\n",
            "        - name: Shelf\n          in: query\n",
        );
        assert_ne!(
            normalized, source,
            "the measurement's query parameter moved"
        );
        assert!(document_refusal(&normalized).is_some());

        let parameter = |name: &str, location: &str| -> crate::openapi::Parameter {
            serde_json::from_value(serde_json::json!({"name": name, "in": location})).unwrap()
        };
        let pair = |a: (&str, &str, bool), b: (&str, &str, bool)| {
            generated_location_pair((&parameter(a.0, a.1), a.2), (&parameter(b.0, b.1), b.2))
        };
        assert!(pair(("shelf", "path", false), ("shelf", "query", false)));
        assert!(pair(("shelf", "header", false), ("shelf", "path", false)));
        assert!(pair(
            ("patron", "query", false),
            ("patron", "cookie", false)
        ));
        assert!(!pair(("shelf", "path", true), ("shelf", "query", false)));
        assert!(!pair(
            ("patron", "query", false),
            ("patron", "header", false)
        ));
        assert!(!pair(
            ("shelf_id", "path", false),
            ("shelfId", "query", false)
        ));
    }

    #[test]
    fn a_property_two_allof_parents_share_and_one_inherits_is_refused() {
        for (shape, location) in [
            ("probe.yml", "GET /hostnames response 200"),
            (
                "error-response-two-parents-probe.yml",
                "GET /hostnames response 4XX",
            ),
        ] {
            let error = shape_refusal(&format!("object-property-name-collision/{shape}"))
                .unwrap_or_default();
            assert!(
                error.contains(&format!(
                    "object-property-name-collision: {location} property \"errors\""
                )),
                "{shape}: {error}"
            );
        }
        for control in [
            "two-direct-parents-control.yml",
            "second-parent-unrelated-control.yml",
            "single-parent-control.yml",
            "redeclared-non-nullable-base-control.yml",
            "inherited-required-control.yml",
        ] {
            assert_eq!(
                shape_refusal(&format!("object-property-name-collision/{control}")),
                None,
                "{control}"
            );
        }
    }

    #[test]
    fn a_path_parameter_keeps_its_name_against_a_grandparents_body_property() {
        for shape in ["probe.yml", "path-reference-inline-body-probe.yml"] {
            let error = shape_refusal(&format!("request-property-name-collision/{shape}"))
                .unwrap_or_default();
            assert!(
                error.contains(
                    "request-property-name-collision: PATCH /requests/{id} body property \"id\""
                ),
                "{shape}: {error}"
            );
        }
        // A referenced body is sent whole, so its `id` claims no request name.
        assert_eq!(
            shape_refusal("request-property-name-collision/path-referenced-body-control.yml"),
            None
        );
    }

    #[test]
    fn a_multipart_property_sharing_a_query_or_header_name_is_refused() {
        for (shape, location) in [
            ("multipart-header-probe.yml", "header"),
            ("multipart-query-probe.yml", "query"),
        ] {
            let error = shape_refusal(&format!("request-property-name-collision/{shape}"))
                .unwrap_or_default();
            assert!(
                error.contains(&format!(
                    "request-property-name-collision: POST /sailings/{{sailingId}}/bookings \
                     multipart body property \"deck\" collides with the {location} parameter \"deck\""
                )),
                "{shape}: {error}"
            );
        }
        // A JSON body's colliding field takes a prefix instead.
        assert_eq!(
            shape_refusal("request-property-name-collision/json-body-header-control.yml"),
            None
        );
    }

    #[test]
    fn a_body_property_a_member_or_second_parent_redeclares_is_one_request_property() {
        for control in [
            "body-allof-member-redeclared-control.yml",
            "body-two-parents-shared-control.yml",
        ] {
            assert_eq!(
                shape_refusal(&format!("request-property-name-collision/{control}")),
                None,
                "{control}"
            );
        }
    }

    #[test]
    fn a_header_the_client_carries_claims_no_request_name() {
        let error = shape_refusal("request-property-name-collision/header-query-subset-probe.yml")
            .unwrap_or_default();
        assert!(
            error.contains("parameters \"X-Namespace\" and \"namespace\" in different locations"),
            "{error}"
        );
        assert_eq!(
            shape_refusal(
                "request-property-name-collision/header-query-every-operation-control.yml"
            ),
            None
        );
    }

    #[test]
    fn every_class_id_is_a_registered_names_class() {
        let registry = std::fs::read_to_string(
            Path::new(env!("CARGO_MANIFEST_DIR")).join("docs/fern-refusals/classes.tsv"),
        )
        .expect("read the refusal registry");
        let names: std::collections::HashSet<&str> = registry
            .lines()
            .skip(1)
            .filter_map(|row| {
                let mut fields = row.split('\t');
                let id = fields.next()?;
                (fields.next()? == "names").then_some(id)
            })
            .collect();
        for class in [
            Class::DiscriminantValueUnsuitable,
            Class::DuplicatePathParameter,
            Class::EnumNameUnsuitable,
            Class::EnumValueUnnameable,
            Class::GeneratedFileNameTooLong,
            Class::ObjectPropertyNameCollision,
            Class::RequestPropertyCamelcaseCollision,
            Class::RequestPropertyNameCollision,
            Class::SdkMethodCollision,
            Class::TypeNameCollision,
            Class::TypeNameNotLetterLed,
        ] {
            assert!(
                names.contains(class.id()),
                "{class:?} names {:?}, which is not a `names` row of classes.tsv",
                class.id()
            );
        }
    }

    #[test]
    fn a_declared_type_name_two_differing_schemas_resolve_to_is_refused() {
        let check = |components: &str| {
            let source: serde_json::Value = crate::yaml::from_str(&format!(
                "openapi: 3.0.3\ninfo: {{title: t, version: '1'}}\npaths: {{}}\n\
                 components:\n  schemas:\n{components}"
            ))
            .unwrap();
            let doc: OpenApi = serde_json::from_value(source.clone()).unwrap();
            source_type_names(&source, &doc, Path::new("api.yml"))
        };
        let widget = "    Widget: {x-fern-type-name: Gadget, type: object}\n";
        // Identical schemas under one name are one type, declared or keyed.
        check(&format!(
            "{widget}    Other: {{x-crozier-type-name: Gadget, type: object}}\n"
        ))
        .unwrap();
        check(&format!("{widget}    Gadget: {{type: object}}\n")).unwrap();
        // Two keys alone are the key-collision check's, not this one's.
        check("    A: {type: object}\n    B: {type: string}\n").unwrap();
        for second in [
            "    Other: {x-fern-type-name: Gadget, type: string}\n",
            "    Gadget: {type: string}\n",
            "    Gad~get: {x-fern-type-name: Gad/get, type: string}\n",
        ] {
            let first = if second.contains("Gad~get") {
                "    Widget: {x-fern-type-name: Gad get, type: object}\n"
            } else {
                widget
            };
            let error = check(&format!("{first}{second}")).unwrap_err().to_string();
            assert!(error.contains("type-name-collision"), "{error}");
            assert!(error.contains("\"Widget\""), "{error}");
        }
    }

    #[test]
    fn enum_name_refusals_respect_value_shapes_types_and_declared_names() {
        let schemas = indexmap::IndexMap::new();
        for (value, refused) in [
            ("10080", true),
            ("10001+", false),
            ("20000+", false),
            ("9999", false),
            ("007", false),
            ("1st", false),
            ("UNDEFINED", false),
            ("緊急", true),
            ("!!!", true),
            ("#0094FF", true),
            ("+1", true),
            ("_1", true),
            ("종합-00", true),
        ] {
            let schema: Schema = serde_json::from_value(serde_json::json!({
                "type": "string", "enum": [value]
            }))
            .unwrap();
            assert_eq!(
                check_schema(&schema, "Minutes", Path::new("api.yml"), &schemas).is_err(),
                refused,
                "{value}"
            );
        }
        let schema: Schema = serde_json::from_value(serde_json::json!({
            "type": "string", "enum": ["10080"],
            "x-crozier-enum": {"10080": {"name": "WEEK"}}
        }))
        .unwrap();
        check_schema(&schema, "Minutes", Path::new("api.yml"), &schemas).unwrap();
        let schema: Schema = serde_json::from_value(serde_json::json!({
            "type": "string", "enum": ["10080"],
            "x-crozier-enum": {"10080": {"name": "2fa"}}
        }))
        .unwrap();
        assert!(check_schema(&schema, "Minutes", Path::new("api.yml"), &schemas).is_err());
        for ty in ["integer", "number", "boolean"] {
            let schema: Schema = serde_json::from_value(serde_json::json!({
                "type": ty, "enum": ["10080"]
            }))
            .unwrap();
            check_schema(&schema, "NonStringEnum", Path::new("api.yml"), &schemas).unwrap();
        }
    }
}
