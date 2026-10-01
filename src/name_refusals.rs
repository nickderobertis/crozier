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
    for (name, schema) in &doc.components.schemas {
        check_schema(schema, &format!("#/components/schemas/{name}"), path)?;
    }
    for (route, item) in &doc.paths {
        for (method, op) in item.operations() {
            let location = format!("{method} {route}");
            for parameter in &op.parameters {
                if let Some(schema) = &parameter.schema {
                    check_schema(
                        schema,
                        &format!("{location} parameter {}", parameter.name),
                        path,
                    )?;
                }
                for media in parameter.content.values() {
                    if let Some(schema) = &media.schema {
                        check_schema(
                            schema,
                            &format!("{location} parameter {}", parameter.name),
                            path,
                        )?;
                    }
                }
            }
            if let Some(body) = &op.request_body {
                for media in body.content.values() {
                    if let Some(schema) = &media.schema {
                        check_schema(schema, &format!("{location} request body"), path)?;
                    }
                }
            }
            for (status, response) in &op.responses {
                for media in response.content.values() {
                    if let Some(schema) = &media.schema {
                        check_schema(schema, &format!("{location} response {status}"), path)?;
                    }
                }
            }
        }
    }
    Ok(())
}

fn check_schema(schema: &Schema, location: &str, path: &Path) -> Result<()> {
    // Measured at Fern 5.67.1: invalid overrides warn and fall back to the
    // original value, so they cannot rescue a value Fern cannot name.
    let names: std::collections::BTreeMap<_, _> = schema
        .enum_member_names()
        .filter(|(_, name)| {
            name.starts_with(|ch: char| ch.is_ascii_alphabetic())
                && name
                    .bytes()
                    .all(|byte| byte.is_ascii_alphanumeric() || byte == b'_')
        })
        .collect();
    if let Some(values) = &schema.enum_values {
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
            return check_children(schema, location, path);
        }
        for value in values.iter().filter_map(serde_json::Value::as_str) {
            if names.contains_key(value) {
                continue;
            }
            let member = crate::naming::enum_member_name(value);
            let bare_number = !value.is_empty() && value.bytes().all(|byte| byte.is_ascii_digit());
            if member == "_" || (bare_number && member.starts_with('_')) {
                return Err(Error::InvalidSpec {
                    path: path.to_owned(),
                    message: format!(
                        "enum-value-unnameable: {location} enum value {value:?}; declare a usable name with x-crozier-enum"
                    ),
                });
            }
        }
    }
    check_children(schema, location, path)
}

fn check_children(schema: &Schema, location: &str, path: &Path) -> Result<()> {
    for (name, child) in &schema.properties {
        check_schema(child, &format!("{location}/properties/{name}"), path)?;
    }
    if let Some(child) = &schema.items {
        check_schema(child, &format!("{location}/items"), path)?;
    }
    if let Some(AdditionalProperties::Schema(child)) = &schema.additional_properties {
        check_schema(child, &format!("{location}/additionalProperties"), path)?;
    }
    for (kind, children) in [
        ("allOf", &schema.all_of),
        ("oneOf", &schema.one_of),
        ("anyOf", &schema.any_of),
    ] {
        if let Some(children) = children {
            for (index, child) in children.iter().enumerate() {
                check_schema(child, &format!("{location}/{kind}/{index}"), path)?;
            }
        }
    }
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn numeric_names_refuse_only_unspellable_values_without_an_override() {
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
        ] {
            let schema: Schema = serde_json::from_value(serde_json::json!({
                "type": "string", "enum": [value]
            }))
            .unwrap();
            assert_eq!(
                check_schema(&schema, "Minutes", Path::new("api.yml")).is_err(),
                refused,
                "{value}"
            );
        }
        let schema: Schema = serde_json::from_value(serde_json::json!({
            "type": "string", "enum": ["10080"],
            "x-crozier-enum": {"10080": {"name": "WEEK"}}
        }))
        .unwrap();
        check_schema(&schema, "Minutes", Path::new("api.yml")).unwrap();
        let schema: Schema = serde_json::from_value(serde_json::json!({
            "type": "string", "enum": ["10080"],
            "x-crozier-enum": {"10080": {"name": "2fa"}}
        }))
        .unwrap();
        assert!(check_schema(&schema, "Minutes", Path::new("api.yml")).is_err());
        for ty in ["integer", "number", "boolean"] {
            let schema: Schema = serde_json::from_value(serde_json::json!({
                "type": ty, "enum": ["10080"]
            }))
            .unwrap();
            check_schema(&schema, "NonStringEnum", Path::new("api.yml")).unwrap();
        }
    }
}
