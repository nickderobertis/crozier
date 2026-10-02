//! `type-not-defined`: references pinned Fern writes into its definition but
//! then fails to resolve. Two measured mechanisms, both recorded with their
//! Fern controls in `docs/fern-refusals/type-not-defined/evaluation.md`:
//!
//! - An operation whose first tag Fern files as `api.yml` (the name of its
//!   definition's root file) loses every type and error reference in it.
//! - A union Fern discriminates from its members' single-value property
//!   names a member that a JSON request body also `$ref`s; Fern turns that body
//!   into an inline request and the union's reference to the member dangles.

use super::{ignored_reference_node, yaml_pointer};
use serde_yaml_ng::Value;

const METHODS: [&str; 8] = [
    "get", "put", "post", "delete", "options", "head", "patch", "trace",
];

/// The first offending element, or `None` when Fern resolves every reference.
pub(super) fn undefined_type_reference(root: &Value) -> Option<String> {
    let paths = root.get("paths").and_then(Value::as_mapping);
    for (route, item) in paths.into_iter().flatten() {
        let Some(route) = route.as_str() else {
            continue;
        };
        for method in METHODS {
            let Some(operation) = item.get(method) else {
                continue;
            };
            if ignored_reference_node(operation) || !filed_as_api(operation) {
                continue;
            }
            let prefix = format!("{} {route}", method.to_ascii_uppercase());
            if let Some(element) = api_file_reference(root, item, operation) {
                return Some(format!("{prefix} {element}"));
            }
        }
    }
    body_member_union(root)
}

/// Fern names a tag's definition file by camel-casing the tag, so separators
/// around a single `api` word still land in `api.yml` while `ApI` (two words)
/// or `api1` do not. `x-fern-sdk-group-name` does not move the file.
fn filed_as_api(operation: &Value) -> bool {
    let Some(tag) = operation
        .get("tags")
        .and_then(Value::as_sequence)
        .and_then(|tags| tags.first())
        .and_then(Value::as_str)
    else {
        return false;
    };
    matches!(
        tag.trim_matches(|c: char| !c.is_alphanumeric()),
        "api" | "Api" | "API"
    )
}

fn api_file_reference(root: &Value, item: &Value, operation: &Value) -> Option<String> {
    let responses = operation.get("responses").and_then(Value::as_mapping);
    for (code, _) in responses.into_iter().flatten() {
        let code = status_text(code);
        if fern_error_status(&code) {
            return Some(format!("responses/{code}"));
        }
    }
    if let Some((code, response)) = fern_response(operation) {
        let response = resolve(root, response);
        if single_media(response, |media| {
            media.to_ascii_lowercase().contains("json")
        })
        .is_some_and(declares_type)
        {
            return Some(format!("responses/{code}"));
        }
    }
    let shared = item.get("parameters").and_then(Value::as_sequence);
    let local = operation.get("parameters").and_then(Value::as_sequence);
    for parameter in shared.into_iter().chain(local).flatten() {
        let parameter = resolve(root, parameter);
        let located = matches!(
            parameter.get("in").and_then(Value::as_str),
            Some("query" | "path")
        );
        if located && parameter.get("schema").is_some_and(declares_type) {
            let name = parameter.get("name").and_then(Value::as_str).unwrap_or("");
            return Some(format!("parameter {name}"));
        }
    }
    let body = operation.get("requestBody").map(|body| resolve(root, body));
    if let Some(schema) = body.and_then(|body| single_media(body, |_| true)) {
        let media = body
            .and_then(|body| body.get("content"))
            .and_then(Value::as_mapping)
            .and_then(|content| content.keys().next())
            .and_then(Value::as_str)
            .unwrap_or("")
            .to_ascii_lowercase();
        if body_declares_type(root, &media, schema) {
            return Some("requestBody".into());
        }
    }
    None
}

fn status_text(code: &Value) -> String {
    match code {
        Value::Number(number) => number.to_string(),
        _ => code.as_str().unwrap_or("").to_owned(),
    }
}

/// The statuses Fern names an error for, measured one operation per status
/// from 100 to 599; any other status (`427`, `520`, `4XX`, …) is skipped.
fn fern_error_status(code: &str) -> bool {
    code.len() == 3
        && code.parse::<u16>().is_ok_and(
            |status| matches!(status, 400..=426 | 428..=431 | 444 | 449..=451 | 498..=511),
        )
}

/// The response Fern types the endpoint with: `200` when present, otherwise
/// a sole 2xx, otherwise `default` when no 2xx exists. Other combinations are
/// unmeasured and left alone.
fn fern_response(operation: &Value) -> Option<(String, &Value)> {
    let responses = operation.get("responses").and_then(Value::as_mapping)?;
    let success: Vec<(String, &Value)> = responses
        .iter()
        .map(|(code, response)| (status_text(code), response))
        .filter(|(code, _)| code.len() == 3 && code.starts_with('2'))
        .collect();
    if let Some(found) = success.iter().find(|(code, _)| code == "200") {
        return Some(found.clone());
    }
    match success.as_slice() {
        [only] => Some(only.clone()),
        [] => responses
            .get("default")
            .map(|response| ("default".to_owned(), response)),
        _ => None,
    }
}

/// The schema of a node's only media type, when that media type passes `accept`.
fn single_media(node: &Value, accept: impl Fn(&str) -> bool) -> Option<&Value> {
    let content = node.get("content").and_then(Value::as_mapping)?;
    let mut media = content.iter();
    let (Some((name, value)), None) = (media.next(), media.next()) else {
        return None;
    };
    accept(name.as_str()?).then(|| value.get("schema"))?
}

fn body_declares_type(root: &Value, media: &str, schema: &Value) -> bool {
    let properties_declare = |schema: &Value| {
        schema
            .get("properties")
            .and_then(Value::as_mapping)
            .is_some_and(|properties| properties.values().any(declares_type))
    };
    if media == "application/x-www-form-urlencoded" || media == "multipart/form-data" {
        return properties_declare(schema);
    }
    if !media.contains("json") {
        return false;
    }
    if schema.get("$ref").is_some() {
        // A named object body becomes an inline request Fern resolves; a named
        // scalar or enum stays a type reference.
        let target = resolve(root, schema);
        return target.get("enum").is_some()
            || target.get("const").is_some()
            || matches!(
                target.get("type").and_then(Value::as_str),
                Some("string" | "integer" | "number" | "boolean")
            );
    }
    if schema_type_is(schema, "array") {
        return schema.get("items").is_some_and(declares_type);
    }
    properties_declare(schema)
}

/// Whether Fern writes this schema as a type reference (a named schema, an
/// enum, an object with properties, a union) rather than a primitive or a
/// container of primitives.
fn declares_type(schema: &Value) -> bool {
    if schema.get("$ref").is_some() || schema.get("enum").is_some() || schema.get("const").is_some()
    {
        return true;
    }
    for key in ["oneOf", "anyOf"] {
        if let Some(members) = schema.get(key).and_then(Value::as_sequence) {
            let members: Vec<&Value> = members
                .iter()
                .filter(|member| member.get("type").and_then(Value::as_str) != Some("null"))
                .collect();
            return match members.as_slice() {
                [only] => declares_type(only),
                [] => false,
                _ => true,
            };
        }
    }
    if let Some(members) = schema.get("allOf").and_then(Value::as_sequence) {
        return members.iter().any(declares_type);
    }
    if schema_type_is(schema, "array") {
        return schema.get("items").is_some_and(declares_type);
    }
    if schema
        .get("properties")
        .and_then(Value::as_mapping)
        .is_some_and(|properties| !properties.is_empty())
    {
        return true;
    }
    schema
        .get("additionalProperties")
        .is_some_and(|value| value.is_mapping() && declares_type(value))
}

fn schema_type_is(schema: &Value, name: &str) -> bool {
    match schema.get("type") {
        Some(Value::String(found)) => found == name,
        Some(Value::Sequence(types)) => types.iter().any(|found| found.as_str() == Some(name)),
        _ => false,
    }
}

fn resolve<'a>(root: &'a Value, node: &'a Value) -> &'a Value {
    node.get("$ref")
        .and_then(Value::as_str)
        .and_then(|reference| reference.strip_prefix('#'))
        .and_then(|pointer| yaml_pointer(root, pointer))
        .unwrap_or(node)
}

const SCHEMA_PREFIX: &str = "#/components/schemas/";

/// A component union whose members all carry one property with a single
/// string value (Fern infers that property as the discriminant), one member of
/// which is also the whole `application/json` body of an operation.
fn body_member_union(root: &Value) -> Option<String> {
    let mut bodies = std::collections::HashSet::new();
    let paths = root.get("paths").and_then(Value::as_mapping);
    for item in paths.into_iter().flatten().map(|(_, item)| item) {
        for operation in METHODS.iter().filter_map(|method| item.get(*method)) {
            if ignored_reference_node(operation) {
                continue;
            }
            let name = operation
                .get("requestBody")
                .map(|body| resolve(root, body))
                .and_then(|body| body.get("content"))
                .and_then(|content| content.get("application/json"))
                .and_then(|media| media.get("schema"))
                .and_then(|schema| schema.get("$ref"))
                .and_then(Value::as_str)
                .and_then(|reference| reference.strip_prefix(SCHEMA_PREFIX));
            bodies.extend(name);
        }
    }
    if bodies.is_empty() {
        return None;
    }
    let schemas = root
        .get("components")
        .and_then(|components| components.get("schemas"))
        .and_then(Value::as_mapping)?;
    schemas.iter().find_map(|(name, schema)| {
        find_union(
            root,
            schema,
            &format!("components/schemas/{}", name.as_str()?),
            &bodies,
        )
    })
}

fn find_union(
    root: &Value,
    schema: &Value,
    pointer: &str,
    bodies: &std::collections::HashSet<&str>,
) -> Option<String> {
    for key in ["oneOf", "anyOf"] {
        if let Some(members) = schema.get(key).and_then(Value::as_sequence) {
            if inferred_discriminant(root, members) {
                let body_member = members.iter().position(|member| {
                    member
                        .get("$ref")
                        .and_then(Value::as_str)
                        .and_then(|reference| reference.strip_prefix(SCHEMA_PREFIX))
                        .is_some_and(|name| bodies.contains(name))
                });
                if let Some(index) = body_member {
                    return Some(format!("{pointer}/{key}/{index}"));
                }
            }
        }
    }
    let mut children: Vec<(String, &Value)> = Vec::new();
    for key in ["items", "additionalProperties"] {
        if let Some(child) = schema.get(key).filter(|child| child.is_mapping()) {
            children.push((format!("{pointer}/{key}"), child));
        }
    }
    for key in ["oneOf", "anyOf", "allOf"] {
        for (index, child) in schema
            .get(key)
            .and_then(Value::as_sequence)
            .into_iter()
            .flatten()
            .enumerate()
        {
            children.push((format!("{pointer}/{key}/{index}"), child));
        }
    }
    let properties = schema.get("properties").and_then(Value::as_mapping);
    for (name, child) in properties.into_iter().flatten() {
        if let Some(name) = name.as_str() {
            children.push((format!("{pointer}/properties/{name}"), child));
        }
    }
    children
        .into_iter()
        .find_map(|(pointer, child)| find_union(root, child, &pointer, bodies))
}

/// At least two members, every one an object sharing a property whose only
/// value is a string (`enum` of one, or `const`).
pub(super) fn inferred_discriminant(root: &Value, members: &[Value]) -> bool {
    let objects: Vec<&serde_yaml_ng::Mapping> = members
        .iter()
        .filter_map(|member| resolve(root, member).get("properties"))
        .filter_map(Value::as_mapping)
        .collect();
    if members.len() < 2 || objects.len() != members.len() {
        return false;
    }
    let single_value = |property: &Value| match property.get("enum") {
        Some(values) => values
            .as_sequence()
            .is_some_and(|values| values.len() == 1 && values[0].is_string()),
        None => property.get("const").is_some_and(Value::is_string),
    };
    objects[0].iter().any(|(name, property)| {
        single_value(property)
            && objects[1..]
                .iter()
                .all(|other| other.get(name).is_some_and(&single_value))
    })
}

#[cfg(test)]
mod tests {
    use super::*;

    fn element(text: &str) -> Option<String> {
        undefined_type_reference(&serde_yaml_ng::from_str(text).unwrap())
    }

    const COMPONENTS: &str = "components:\n  schemas:\n    Thing: {type: object, properties: {id: {type: string}}}\n    Color: {type: string, enum: [red, blue]}\n";

    fn api_operation(tag: &str, body: &str) -> String {
        format!("paths:\n  /users:\n    post:\n      tags: [{tag}]\n{body}{COMPONENTS}")
    }

    #[test]
    fn api_file_errors_responses_parameters_and_bodies_are_refused() {
        for (body, expected) in [
            ("      responses: {'403': {description: F}}\n", "POST /users responses/403"),
            ("      responses: {499: {description: F}}\n", "POST /users responses/499"),
            ("      responses: {'200': {description: OK, content: {application/json: {schema: {$ref: '#/components/schemas/Thing'}}}}}\n", "POST /users responses/200"),
            ("      responses: {default: {description: OK, content: {application/json: {schema: {oneOf: [{type: string}, {type: integer}]}}}}}\n", "POST /users responses/default"),
            ("      parameters: [{name: f, in: query, schema: {type: array, items: {enum: [a]}}}]\n      responses: {}\n", "POST /users parameter f"),
            ("      requestBody: {content: {application/json: {schema: {$ref: '#/components/schemas/Color'}}}}\n      responses: {}\n", "POST /users requestBody"),
            ("      requestBody: {content: {multipart/form-data: {schema: {properties: {t: {$ref: '#/components/schemas/Thing'}}}}}}\n      responses: {}\n", "POST /users requestBody"),
        ] {
            for tag in ["api", "API", "Api_", "' API '"] {
                assert_eq!(element(&api_operation(tag, body)).as_deref(), Some(expected), "{tag}: {body}");
            }
        }
    }

    #[test]
    fn api_file_near_misses_are_accepted() {
        for body in [
            "      responses: {'204': {description: N}, '427': {description: R}, '520': {description: R}, 4XX: {description: R}, default: {description: R}}\n",
            "      responses: {'200': {description: OK, content: {application/json: {schema: {type: object, additionalProperties: {type: string}}}}}}\n",
            "      responses: {'200': {description: OK, content: {application/json: {schema: {anyOf: [{type: string}, {type: 'null'}]}}}}}\n",
            "      responses: {'200': {description: OK, content: {text/plain: {schema: {$ref: '#/components/schemas/Color'}}}}}\n",
            "      responses: {'202': {description: OK, content: {application/json: {schema: {$ref: '#/components/schemas/Thing'}}}}, '200': {description: OK}}\n",
            "      parameters: [{name: f, in: header, schema: {enum: [a]}}, {name: g, in: query, schema: {type: array, items: {type: string}}}]\n      responses: {}\n",
            "      requestBody: {content: {application/json: {schema: {$ref: '#/components/schemas/Thing'}}}}\n      responses: {}\n",
            "      x-fern-ignore: true\n      responses: {'403': {description: F}}\n",
        ] {
            assert_eq!(element(&api_operation("api", body)), None, "{body}");
        }
        let refused = "      responses: {'403': {description: F}}\n";
        for tag in ["ApI", "aPI", "api1", "'a pi'", "APIs", "users, api"] {
            assert_eq!(element(&api_operation(tag, refused)), None, "{tag}");
        }
    }

    const UNION: &str = "paths:\n  /a:\n    post:\n      requestBody: {content: {application/json: {schema: {$ref: '#/components/schemas/A'}}}}\n      responses: {}\ncomponents:\n  schemas:\n    Holder: {properties: {events: {type: array, items: {oneOf: [{$ref: '#/components/schemas/A'}, {$ref: '#/components/schemas/B'}]}}}}\n    A: {properties: {type: {enum: [A]}}}\n    B: {properties: {type: {enum: [B]}}}\n";

    #[test]
    fn a_discriminated_union_over_a_body_schema_is_refused() {
        assert_eq!(
            element(UNION).as_deref(),
            Some("components/schemas/Holder/properties/events/items/oneOf/0")
        );
        let constant = UNION.replace("{enum: [A]}", "{const: A}");
        assert!(element(&constant).is_some());
        for near_miss in [
            UNION.replace("{enum: [B]}", "{type: string}"),
            UNION.replace("{enum: [B]}", "{enum: [B, C]}"),
            UNION.replace("B: {properties: {type:", "B: {properties: {kind:"),
            UNION.replace("application/json", "application/x-www-form-urlencoded"),
            UNION.replace(
                "      responses: {}\n",
                "      x-fern-ignore: true\n      responses: {}\n",
            ),
            UNION.replace(", {$ref: '#/components/schemas/B'}", ""),
        ] {
            assert_eq!(element(&near_miss), None, "{near_miss}");
        }
    }
}
