//! Refuse name shapes whose baseline SDK fails the refusal registry's bar.

use crate::openapi::{AdditionalProperties, OpenApi, Schema};
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

fn source_refusals(source: &serde_yaml_ng::Value, args: &crate::GenerateArgs) -> Result<()> {
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
        global_headers_crozier: None,
        global_headers_fern: None,
        sdk_variables_crozier: None,
        sdk_variables_fern: None,
    };
    for (route, item) in source["paths"].as_mapping().into_iter().flatten() {
        let Some(route) = route.as_str() else {
            continue;
        };
        let mut metadata = serde_yaml_ng::Mapping::new();
        for (method, op) in item.as_mapping().into_iter().flatten() {
            let Some(fields) = op.as_mapping() else {
                continue;
            };
            let extensions = fields
                .iter()
                .filter(|(key, _)| key.as_str().is_some_and(|key| key.starts_with("x-")))
                .map(|(key, value)| (key.clone(), value.clone()))
                .collect();
            metadata.insert(method.clone(), serde_yaml_ng::Value::Mapping(extensions));
        }
        if let Ok(item) = serde_yaml_ng::from_value::<crate::openapi::PathItem>(
            serde_yaml_ng::Value::Mapping(metadata),
        ) {
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
                .as_mapping()
                .into_iter()
                .flat_map(|mapping| mapping.values())
            {
                let mut fields = Vec::new();
                source_request_properties(
                    source,
                    &media["schema"],
                    &mut std::collections::HashSet::new(),
                    &mut fields,
                    true,
                );
                let inherited = source_target(source, &media["schema"])["allOf"]
                    .as_sequence()
                    .is_some_and(|members| members.iter().any(|member| member["$ref"].is_string()));
                let mut names = std::collections::HashSet::new();
                for (_, name) in fields {
                    if !names.insert(name.clone()) && inherited {
                        return Err(refusal(&args.spec, Class::RequestPropertyNameCollision, format!("{} {route} body property {name:?} collides with another request property; give the properties distinct declared names", method.to_ascii_uppercase())));
                    }
                }
                // The flattened inline shape also refuses a readOnly parent field
                // an own property redeclares, as `validate_names` does.
                let target = source_target(source, &media["schema"]);
                let mut own = Vec::new();
                for (key, property) in target["properties"].as_mapping().into_iter().flatten() {
                    if source_target(source, property)["readOnly"].as_bool() != Some(true) {
                        if let Some(wire) = key.as_str() {
                            own.push(request_property_name(property).unwrap_or(wire).to_owned());
                        }
                    }
                }
                let mut parents = Vec::new();
                for member in target["allOf"]
                    .as_sequence()
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
    source: &serde_yaml_ng::Value,
    node: &serde_yaml_ng::Value,
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
    for (key, property) in node["properties"].as_mapping().into_iter().flatten() {
        if request_only && source_target(source, property)["readOnly"].as_bool() == Some(true) {
            continue;
        }
        if let Some(wire) = key.as_str() {
            fields.push((
                wire.to_owned(),
                request_property_name(property).unwrap_or(wire).to_owned(),
            ));
        }
    }
    for member in node["allOf"].as_sequence().into_iter().flatten() {
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
            let mut names: Vec<String> = op
                .parameters
                .iter()
                .map(|parameter| {
                    let raw = raw_operation["parameters"]
                        .as_sequence()
                        .into_iter()
                        .flatten()
                        .chain(
                            source["paths"][route]["parameters"]
                                .as_sequence()
                                .into_iter()
                                .flatten(),
                        )
                        .map(|node| source_target(&source, node))
                        .find(|node| {
                            node["name"].as_str() == Some(parameter.name.as_str())
                                && serde_yaml_ng::from_value::<crate::openapi::ParameterLocation>(
                                    node["in"].clone(),
                                )
                                .ok()
                                    == parameter.location
                        });
                    raw.and_then(crate::openapi::refusal_parameter_name)
                        .map(str::to_owned)
                        .unwrap_or_else(|| {
                            if parameter.location == Some(crate::openapi::ParameterLocation::Header)
                            {
                                fern_header_declaration_name(&parameter.name)
                            } else {
                                parameter.name.clone()
                            }
                        })
                })
                .collect();
            let mut path_names: std::collections::HashSet<String> = op
                .parameters
                .iter()
                .zip(&names)
                .filter(|(parameter, _)| {
                    parameter.location == Some(crate::openapi::ParameterLocation::Path)
                })
                .map(|(_, name)| name.clone())
                .collect();
            for (index, parameter) in op.parameters.iter().enumerate() {
                for (other_index, other) in op.parameters.iter().enumerate().take(index) {
                    if parameter.location != other.location && names[index] == names[other_index] {
                        let class = if parameter.name == other.name {
                            Class::RequestPropertyCamelcaseCollision
                        } else {
                            Class::RequestPropertyNameCollision
                        };
                        return Err(refusal(path, class, format!("{location} parameters {:?} and {:?} in different locations declare the same request name {:?}; give them distinct names", parameter.name, other.name, names[index])));
                    }
                }
            }
            for segment in route.split('{').skip(1) {
                if let Some((name, _)) = segment.split_once('}') {
                    if !op.parameters.iter().any(|parameter| parameter.name == name) {
                        names.push(name.to_owned());
                        path_names.insert(name.to_owned());
                    }
                }
            }
            let mut body_hints = std::collections::HashMap::new();
            let raw_body = source_target(&source, &raw_operation["requestBody"]);
            for media in raw_body["content"]
                .as_mapping()
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
                        let inherited = resolved
                            .all_of
                            .iter()
                            .flatten()
                            .any(|member| member.reference.is_some());
                        let mut body_names = std::collections::HashSet::new();
                        for name in properties {
                            let name = body_hints
                                .get(name)
                                .cloned()
                                .unwrap_or_else(|| name.to_owned());
                            if path_names.contains(&name)
                                || (!body_names.insert(name.clone()) && inherited)
                            {
                                return Err(refusal(path, Class::RequestPropertyNameCollision, format!("{location} body property {name:?} collides with another request property; give the properties distinct declared names")));
                            }
                            names.push(name);
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
            for name in &names {
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

fn source_document(path: &Path) -> Result<serde_yaml_ng::Value> {
    let text = std::fs::read_to_string(path).map_err(|source| Error::ReadSpec {
        path: path.to_owned(),
        source,
    })?;
    // JSON's numeric visitor accepts large integers as floats; YAML Value's
    // visitor rejects u128. Neither number matters to name validation.
    if path
        .extension()
        .is_some_and(|extension| extension.eq_ignore_ascii_case("json"))
    {
        if let Ok(value) = serde_json::from_str::<serde_json::Value>(&text) {
            return serde_yaml_ng::to_value(value).map_err(|error| Error::ParseSpec {
                path: path.to_owned(),
                message: error.to_string(),
            });
        }
    }
    serde_yaml_ng::from_str(&text).map_err(|error| Error::ParseSpec {
        path: path.to_owned(),
        message: error.to_string(),
    })
}

fn source_target<'a>(
    source: &'a serde_yaml_ng::Value,
    mut node: &'a serde_yaml_ng::Value,
) -> &'a serde_yaml_ng::Value {
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
    source: &'a serde_yaml_ng::Value,
    reference: &str,
) -> Option<&'a serde_yaml_ng::Value> {
    let mut target = source;
    for part in reference.strip_prefix("#/")?.split('/') {
        let key = part.replace("~1", "/").replace("~0", "~");
        target = match target {
            serde_yaml_ng::Value::Sequence(items) => {
                key.parse::<usize>().ok().and_then(|index| items.get(index))
            }
            _ => target.get(key.as_str()),
        }?;
    }
    (!target.is_null()).then_some(target)
}

fn source_property_names(
    source: &serde_yaml_ng::Value,
    node: &serde_yaml_ng::Value,
    visited: &mut std::collections::HashSet<String>,
    names: &mut std::collections::HashMap<String, String>,
) {
    if let Some(reference) = node["$ref"].as_str() {
        if !visited.insert(reference.to_owned()) {
            return;
        }
    }
    let node = source_target(source, node);
    for (key, property) in node["properties"].as_mapping().into_iter().flatten() {
        if let Some(wire) = key.as_str() {
            if let Some(name) = request_property_name(property) {
                names.insert(wire.to_owned(), name.to_owned());
            }
        }
    }
    for member in node["allOf"].as_sequence().into_iter().flatten() {
        source_property_names(source, member, visited, names);
    }
}

/// The request name a body property declares: its `x-crozier-property-name` /
/// `x-fern-property-name` — the Fern definition `name` the collision check
/// compares — else the parameter-name spelling this validator also reads.
fn request_property_name(property: &serde_yaml_ng::Value) -> Option<&str> {
    crate::openapi::refusal_property_name(property)
        .or_else(|| crate::openapi::refusal_parameter_name(property))
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
    let nullable_base = schema.all_of.iter().flatten().any(|member| {
        member
            .reference
            .as_deref()
            .and_then(|reference| reference.strip_prefix("#/components/schemas/"))
            .and_then(|name| schemas.get(name))
            .is_some_and(|base| base.nullable == Some(true))
    });
    if nullable_base {
        let mut fields = Vec::new();
        collect_property_names(
            schema,
            schemas,
            &mut std::collections::HashSet::new(),
            &mut fields,
            false,
        );
        let mut seen = std::collections::HashSet::new();
        for field in fields {
            if !seen.insert(field) {
                return Err(refusal(path, Class::ObjectPropertyNameCollision, format!("{location} property {field:?} redeclares a nullable inherited property; give the declarations distinct names")));
            }
        }
    }
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
    // Measured at Fern 5.67.1: invalid overrides warn and fall back to the
    // original value, so they cannot rescue a value Fern cannot name.
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
            // "already declared in this file" to pinned Fern 5.67.1, which
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
    // Pinned Fern 5.67.1 accepts a header parameter's enum named like a root
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
fn without_type_names(node: &serde_yaml_ng::Value) -> serde_yaml_ng::Value {
    let mut node = node.clone();
    if let Some(fields) = node.as_mapping_mut() {
        fields.remove("x-crozier-type-name");
        fields.remove("x-fern-type-name");
    }
    node
}

fn source_type_names(source: &serde_yaml_ng::Value, doc: &OpenApi, path: &Path) -> Result<()> {
    let mut types: std::collections::HashMap<String, (&str, bool, serde_yaml_ng::Value)> =
        std::collections::HashMap::new();
    for (name, node) in source["components"]["schemas"]
        .as_mapping()
        .into_iter()
        .flatten()
    {
        let Some(name) = name.as_str() else {
            continue;
        };
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
    for (route, item) in &doc.paths {
        for (method, _) in item.operations() {
            let operation = &source["paths"][route][method.to_ascii_lowercase()];
            let mut schemas = Vec::new();
            for parameter in operation["parameters"].as_sequence().into_iter().flatten() {
                schemas.push(&source_target(source, parameter)["schema"]);
            }
            let body = source_target(source, &operation["requestBody"]);
            for media in body["content"]
                .as_mapping()
                .into_iter()
                .flat_map(|mapping| mapping.values())
            {
                schemas.push(&media["schema"]);
            }
            for response in operation["responses"]
                .as_mapping()
                .into_iter()
                .flat_map(|mapping| mapping.values())
            {
                for media in source_target(source, response)["content"]
                    .as_mapping()
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
                .as_mapping()
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

fn source_reference_names(
    source: &serde_yaml_ng::Value,
    node: &serde_yaml_ng::Value,
    location: &str,
    path: &Path,
) -> Result<()> {
    if crate::openapi::refusal_node_ignored(node) {
        return Ok(());
    }
    if let Some(reference) = node["$ref"].as_str() {
        if reference.starts_with("#/definitions/") || reference.starts_with("#/webhooks/") {
            let target = source_target(source, node);
            if target["type"].as_str() == Some("object") || target["properties"].is_mapping() {
                return Err(refusal(path, Class::TypeNameNotLetterLed, format!("{location} reference {reference:?} forms an empty object type name; use a component schema reference")));
            }
        }
        return Ok(());
    }
    for property in node["properties"]
        .as_mapping()
        .into_iter()
        .flat_map(|mapping| mapping.values())
    {
        source_reference_names(source, property, location, path)?;
    }
    for key in ["items", "additionalProperties"] {
        if node[key].is_mapping() {
            source_reference_names(source, &node[key], location, path)?;
        }
    }
    for key in ["allOf", "oneOf", "anyOf"] {
        for member in node[key].as_sequence().into_iter().flatten() {
            source_reference_names(source, member, location, path)?;
        }
    }
    Ok(())
}

fn property_reference_cycle(
    source: &serde_yaml_ng::Value,
    node: &serde_yaml_ng::Value,
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
        .as_mapping()
        .into_iter()
        .flat_map(|mapping| mapping.values())
        .any(|property| property_reference_cycle(source, property, stack))
        || (node["items"].is_mapping() && property_reference_cycle(source, &node["items"], stack))
}

#[cfg(test)]
mod tests {
    use super::*;

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
        *object = serde_yaml_ng::from_str("type: string\nenum: [blue, green]\n").unwrap();
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
            let source: serde_yaml_ng::Value = serde_yaml_ng::from_str(&format!(
                "openapi: 3.0.3\ninfo: {{title: t, version: '1'}}\npaths: {{}}\n\
                 components:\n  schemas:\n{components}"
            ))
            .unwrap();
            let doc: OpenApi = serde_yaml_ng::from_value(source.clone()).unwrap();
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
