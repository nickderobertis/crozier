// llmlint: ignore[new_code_lands_in_a_project] This Rust module is registered through src/lib.rs in the existing Cargo crate; this repository has no Nx workspace or project definitions.
//! Refuse name shapes whose baseline SDK fails the refusal registry's bar.

use crate::openapi::{AdditionalProperties, OpenApi, Schema};
use crate::{Error, Result};
use std::path::Path;

/// Validate before rendering or touching the output tree.
pub(crate) fn validate(doc: &OpenApi, path: &Path, strict: bool) -> Result<()> {
    validate_names(doc, path).map_err(|error| match error {
        Error::InvalidSpec { path, message } if strict => Error::InvalidSpec {
            path,
            message: format!("{message} (fern-strict: Fern refuses this document)"),
        },
        other => other,
    })
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
                        .find(|node| node["name"].as_str() == Some(parameter.name.as_str()));
                    raw.and_then(crate::openapi::refusal_parameter_name)
                        .unwrap_or(&parameter.name)
                        .to_owned()
                })
                .collect();
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
                        names.extend(properties.into_iter().map(|name| {
                            body_hints
                                .get(name)
                                .cloned()
                                .unwrap_or_else(|| name.to_owned())
                        }));
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
