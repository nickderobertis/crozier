//! Conservative validity checks for declared examples; unsupported assertions abstain.

use super::{AdditionalProperties, Schema, TypeField};
use serde_json::Value;

fn annotation(key: &str) -> bool {
    key.starts_with("x-")
        || matches!(
            key,
            "$schema" | "$id" | "$comment" | "readOnly" | "writeOnly"
        )
}

/// `None` means the schema writes an assertion this validator cannot establish.
pub(crate) fn matches(
    schemas: &indexmap::IndexMap<String, Schema>,
    schema: &Schema,
    value: &Value,
    depth: usize,
) -> Option<bool> {
    if depth > 32
        || schema.unmodeled_keywords.keys().any(|key| !annotation(key))
        || schema.drops_applicator()
        || schema.discarded_composition
        || schema.malformed
        || schema.pattern.is_some()
        || schema.pattern_properties.is_some()
        || schema.not_schema.is_some()
        || schema.format.is_some()
        || schema.minimum.is_some()
    {
        return None;
    }
    if let Some(reference) = &schema.reference {
        let target = reference.strip_prefix("#/components/schemas/")?;
        if !matches(schemas, schemas.get(target)?, value, depth + 1)? {
            return Some(false);
        }
    }
    if schema
        .enum_values
        .as_ref()
        .is_some_and(|values| !values.contains(value))
        || schema
            .const_value
            .as_ref()
            .is_some_and(|constant| constant != value)
    {
        return Some(false);
    }
    for (members, kind) in [
        (&schema.one_of, 1),
        (&schema.any_of, 0),
        (&schema.all_of, -1),
    ] {
        if let Some(members) = members {
            let answers = members
                .iter()
                .map(|member| matches(schemas, member, value, depth + 1))
                .collect::<Option<Vec<_>>>()?;
            let count = answers.iter().filter(|answer| **answer).count();
            let accepted = match kind {
                1 => count == 1,
                0 => count > 0,
                _ => count == answers.len(),
            };
            if !accepted {
                return Some(false);
            }
        }
    }
    if value.is_null() && schema.nullable == Some(true) {
        return Some(true);
    }
    if let Some(ty) = schema.ty.as_ref().and_then(TypeField::primary) {
        let accepted = match ty {
            "string" => value.is_string(),
            "object" => value.is_object(),
            "array" => value.is_array(),
            "integer" => value.as_i64().is_some() || value.as_u64().is_some(),
            "number" => value.is_number(),
            "boolean" => value.is_boolean(),
            "null" => value.is_null(),
            _ => return None,
        };
        if !accepted {
            return Some(false);
        }
    }
    if let Some(text) = value.as_str() {
        let length = u64::try_from(text.chars().count()).ok()?;
        if schema.min_length.is_some_and(|min| length < min)
            || schema.max_length.is_some_and(|max| length > max)
        {
            return Some(false);
        }
    }
    if let Some(values) = value.as_array() {
        if let Some(items) = &schema.items {
            for value in values {
                if !matches(schemas, items, value, depth + 1)? {
                    return Some(false);
                }
            }
        }
    }
    if let Some(values) = value.as_object() {
        if schema
            .required
            .iter()
            .any(|name| !values.contains_key(name))
        {
            return Some(false);
        }
        for (key, value) in values {
            if let Some(property) = schema.properties.get(key) {
                if !matches(schemas, property, value, depth + 1)? {
                    return Some(false);
                }
            } else {
                match &schema.additional_properties {
                    Some(AdditionalProperties::Bool(false)) => return Some(false),
                    Some(AdditionalProperties::Schema(additional))
                        if !matches(schemas, additional, value, depth + 1)? =>
                    {
                        return Some(false);
                    }
                    _ => {}
                }
            }
        }
    }
    Some(true)
}
