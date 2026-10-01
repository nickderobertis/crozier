// llmlint: ignore[new_code_lands_in_a_project] This Rust module is registered through src/lib.rs in the existing Cargo crate; this repository has no Nx workspace or project definitions.
//! Refuse name shapes whose baseline SDK fails the refusal registry's bar.

use crate::openapi::{AdditionalProperties, OpenApi, Schema};
use crate::{Error, Result};
use std::path::Path;

/// Validate before rendering or touching the output tree.
pub(crate) fn validate(doc: &OpenApi, path: &Path, strict: bool) -> Result<()> {
    validate_names(doc, path).map_err(|error| refusal_error(error, strict))
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
                source_body_collisions(&source, args)
                    .map_err(|error| refusal_error(error, args.fern_strict))?;
            }
            Err(error)
        }
    }
}

fn source_body_collisions(source: &serde_yaml_ng::Value, args: &crate::GenerateArgs) -> Result<()> {
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
                );
                let mut names = std::collections::HashSet::new();
                for (_, name) in fields {
                    if !names.insert(name.clone()) {
                        return Err(Error::InvalidSpec { path: args.spec.clone(),
                            message: format!("request-property-name-collision: {} {route} body property {name:?} collides with another request property; give the properties distinct declared names", method.to_ascii_uppercase()) });
                    }
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
        if let Some(wire) = key.as_str() {
            fields.push((
                wire.to_owned(),
                crate::openapi::refusal_parameter_name(property)
                    .unwrap_or(wire)
                    .to_owned(),
            ));
        }
    }
    for member in node["allOf"].as_sequence().into_iter().flatten() {
        source_request_properties(source, member, visited, fields);
    }
}

fn validate_names(doc: &OpenApi, path: &Path) -> Result<()> {
    let source = source_document(path)?;
    for (route, _) in &doc.paths {
        let mut placeholders = std::collections::HashSet::new();
        for segment in route.split('{').skip(1) {
            if let Some((name, _)) = segment.split_once('}') {
                if !placeholders.insert(name) {
                    return Err(Error::InvalidSpec {
                        path: path.to_owned(),
                        message: format!("duplicate-path-parameter: route {route} repeats path parameter {name:?}; give each path position a distinct name"),
                    });
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
    for (route, item) in &doc.paths {
        for (method, op) in item.operations() {
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
                                header_request_name(&parameter.name)
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
                            "request-property-camelcase-collision"
                        } else {
                            "request-property-name-collision"
                        };
                        return Err(Error::InvalidSpec {
                            path: path.to_owned(),
                            message: format!("{class}: {location} parameters {:?} and {:?} in different locations declare the same request name {:?}; give them distinct names", parameter.name, other.name, names[index]),
                        });
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
                        let mut properties = Vec::new();
                        request_properties(
                            schema,
                            &doc.components.schemas,
                            &mut std::collections::HashSet::new(),
                            &mut properties,
                        );
                        let mut body_names = std::collections::HashSet::new();
                        for name in properties {
                            let name = body_hints
                                .get(name)
                                .cloned()
                                .unwrap_or_else(|| name.to_owned());
                            if path_names.contains(&name) || !body_names.insert(name.clone()) {
                                return Err(Error::InvalidSpec {
                                    path: path.to_owned(),
                                    message: format!("request-property-name-collision: {location} body property {name:?} collides with another request property; give the properties distinct declared names"),
                                });
                            }
                            names.push(name);
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
                        return Err(Error::InvalidSpec {
                            path: path.to_owned(),
                            message: format!("request-property-camelcase-collision: {location} parameters {previous:?} and {name:?} normalize to the same identifier; give them distinct names"),
                        });
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

fn header_request_name(wire: &str) -> String {
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
        let mut target = source;
        for part in reference[2..].split('/') {
            let key = part.replace("~1", "/").replace("~0", "~");
            target = match target {
                serde_yaml_ng::Value::Sequence(items) => {
                    key.parse::<usize>().ok().and_then(|index| items.get(index))
                }
                _ => target.get(key.as_str()),
            }
            .unwrap_or(&serde_yaml_ng::Value::Null);
        }
        if target.is_null() {
            break;
        }
        node = target;
    }
    node
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
            if let Some(name) = crate::openapi::refusal_parameter_name(property) {
                names.insert(wire.to_owned(), name.to_owned());
            }
        }
    }
    for member in node["allOf"].as_sequence().into_iter().flatten() {
        source_property_names(source, member, visited, names);
    }
}

fn request_properties<'a>(
    schema: &'a Schema,
    schemas: &'a indexmap::IndexMap<String, Schema>,
    visited: &mut std::collections::HashSet<&'a str>,
    names: &mut Vec<&'a str>,
) {
    if let Some(reference) = &schema.reference {
        if let Some(name) = reference.strip_prefix("#/components/schemas/") {
            if visited.insert(name) {
                if let Some(target) = schemas.get(name) {
                    request_properties(target, schemas, visited, names);
                }
            }
        }
    }
    names.extend(schema.properties.keys().map(String::as_str));
    for member in schema.all_of.iter().flatten() {
        request_properties(member, schemas, visited, names);
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
    let explicit = schema.discriminator.as_ref().filter(|_| {
        schema
            .ty
            .as_ref()
            .map_or(schema.enum_values.is_none(), |ty| {
                ty.primary() == Some("object")
            })
    });
    let discriminant = explicit
        .map(|tag| tag.property_name.clone())
        .or_else(|| crate::ir::inferred_discriminant_property(schema, schemas));
    if let Some(discriminant) = discriminant.filter(|name| !usable_name(name)) {
        return Err(Error::InvalidSpec {
            path: path.to_owned(),
            message: format!(
                "discriminant-value-unsuitable: {location} discriminant {discriminant:?}; use a letter-led identifier containing letters, numbers and underscores"
            ),
        });
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
                return Err(Error::InvalidSpec {
                    path: path.to_owned(),
                    message: format!(
                        "enum-value-unnameable: {location} enum value {value:?}; declare a usable name with x-crozier-enum"
                    ),
                });
            }
            let starts_with_unspelled_digit = !value.starts_with(|ch: char| ch.is_ascii_digit())
                && value
                    .trim_start_matches(|ch: char| !ch.is_alphanumeric())
                    .starts_with(|ch: char| ch.is_ascii_digit());
            if member.starts_with('_') || starts_with_unspelled_digit {
                return Err(Error::InvalidSpec {
                    path: path.to_owned(),
                    message: format!(
                        "enum-name-unsuitable: {location} enum value {value:?}; declare a usable name with x-crozier-enum"
                    ),
                });
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

#[cfg(test)]
mod tests {
    use super::*;

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
