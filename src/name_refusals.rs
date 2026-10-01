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
    let names: std::collections::BTreeMap<_, _> = schema.enum_member_names().collect();
    if let Some(values) = &schema.enum_values {
        for value in values.iter().filter_map(serde_json::Value::as_str) {
            if names.contains_key(value) {
                continue;
            }
            let member = crate::naming::enum_member_name(value);
            let bare_number = !value.is_empty() && value.bytes().all(|byte| byte.is_ascii_digit());
            if member == "_"
                || (bare_number && member.starts_with('_'))
                || (member == "UNDEFINED" && value.starts_with(|ch: char| ch.is_ascii_digit()))
            {
                return Err(Error::InvalidSpec {
                    path: path.to_owned(),
                    message: format!(
                        "enum-value-unnameable: {location} enum value {value:?}; declare a usable name with x-crozier-enum"
                    ),
                });
            }
        }
    }
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
            ("10001+", true),
            ("20000+", true),
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
    }
}
