//! Structural refusals for the document-family Fern registry.
//!
//! These checks decide whether generation is allowed; they never rewrite the
//! document or repair the output measured in `docs/fern-refusals/`.

use std::path::Path;

use crate::openapi::{
    HttpAuthScheme, OpenApi, ParameterLocation, SecurityScheme, SecuritySchemeType,
};
use crate::{Error, Result};

#[derive(Clone, Copy)]
enum Class {
    UnsupportedOpenapiVersion,
    ServiceAuthUndefined,
    EndpointAuthUndefined,
    UnresolvedReference,
    PathWithoutLeadingSlash,
    PathParameterUnreferenced,
    UndefinedComponentReference,
    DefaultNotValidForType,
    ListDefaultNotArray,
    ObjectExtendsNonObject,
    GeneratorMissingType,
    NamedTypeDefault,
    ExtensionReferenceCycle,
    UnresolvedSchemaReference,
}

impl Class {
    fn id(self) -> &'static str {
        match self {
            Self::UnsupportedOpenapiVersion => "unsupported-openapi-version",
            Self::ServiceAuthUndefined => "service-auth-undefined",
            Self::EndpointAuthUndefined => "endpoint-auth-undefined",
            Self::UnresolvedReference => "unresolved-reference",
            Self::PathWithoutLeadingSlash => "path-without-leading-slash",
            Self::PathParameterUnreferenced => "path-parameter-unreferenced",
            Self::UndefinedComponentReference => "undefined-component-reference",
            Self::DefaultNotValidForType => "default-not-valid-for-type",
            Self::ListDefaultNotArray => "list-default-not-array",
            Self::ObjectExtendsNonObject => "object-extends-non-object",
            Self::GeneratorMissingType => "generator-missing-type",
            Self::NamedTypeDefault => "named-type-default",
            Self::ExtensionReferenceCycle => "extension-reference-cycle",
            Self::UnresolvedSchemaReference => "unresolved-schema-reference",
        }
    }
}

/// Version refusal precedes normalizations that might themselves reject a new
/// OpenAPI construct. Other parse/read errors retain the loader's diagnostics.
pub fn check_version_file(path: &Path, strict: bool) -> Result<()> {
    let extension = path
        .extension()
        .and_then(|v| v.to_str())
        .map(str::to_ascii_lowercase);
    if !matches!(extension.as_deref(), Some("json" | "yml" | "yaml")) {
        return Ok(());
    }
    #[derive(serde::Deserialize)]
    struct Version {
        #[serde(default)]
        openapi: String,
    }
    let Ok(text) = std::fs::read_to_string(path) else {
        return Ok(());
    };
    let version = if extension.as_deref() == Some("json") {
        serde_json::from_str::<Version>(&text).ok()
    } else {
        serde_yaml_ng::from_str::<Version>(&text).ok()
    };
    if let Some(version) = version {
        check_version(&version.openapi, path, strict)?;
    }
    Ok(())
}

/// Check document structure before normalization can replace or discard it.
/// Schema and Path Item references have separate Fern behavior and are excluded.
pub fn check_structure_file(path: &Path, strict: bool) -> Result<()> {
    if !path.extension().and_then(|s| s.to_str()).is_some_and(|s| {
        ["json", "yaml", "yml"]
            .iter()
            .any(|ext| s.eq_ignore_ascii_case(ext))
    }) {
        return Ok(());
    }
    let Ok(text) = std::fs::read_to_string(path) else {
        return Ok(());
    };
    let Ok(root) = serde_yaml_ng::from_str::<ReferenceDocument>(&text).map(|document| document.0)
    else {
        return Ok(());
    };
    if let Some(paths) = root.get("paths").and_then(serde_yaml_ng::Value::as_mapping) {
        for (route, item) in paths {
            let Some(route) = route.as_str() else {
                continue;
            };
            let has_operation = [
                "get", "put", "post", "delete", "options", "head", "patch", "trace",
            ]
            .iter()
            .any(|method| {
                item.get(method)
                    .is_some_and(|operation| !ignored_reference_node(operation))
            });
            if has_operation && !route.starts_with('/') && !route.starts_with("x-") {
                return refusal(
                    path,
                    strict,
                    Class::PathWithoutLeadingSlash,
                    &format!("paths/{route}"),
                );
            }
        }
    }
    if let Some(components) = root.get("components") {
        for name in ["securitySchemes", "requestBodies", "headers"] {
            if let Some(value) = components.get(name) {
                check_reference_objects(value, &root, path, strict, &format!("components/{name}"))?;
            }
        }
    }
    if let Some(paths) = root.get("paths").and_then(serde_yaml_ng::Value::as_mapping) {
        for (route, item) in paths {
            let Some(route) = route.as_str() else {
                continue;
            };
            for name in [
                "get",
                "put",
                "post",
                "delete",
                "options",
                "head",
                "patch",
                "trace",
                "parameters",
            ] {
                if let Some(value) = item.get(name) {
                    check_reference_objects(
                        value,
                        &root,
                        path,
                        strict,
                        &format!("paths/{route}/{name}"),
                    )?;
                }
            }
        }
    }
    // Resolve missing Reference Objects before checking their parameter uses.
    if let Some(paths) = root.get("paths").and_then(serde_yaml_ng::Value::as_mapping) {
        for (route, item) in paths {
            let Some(route) = route.as_str() else {
                continue;
            };
            for method in [
                "get", "put", "post", "delete", "options", "head", "patch", "trace",
            ] {
                let Some(operation) = item.get(method) else {
                    continue;
                };
                if ignored_reference_node(operation) {
                    continue;
                }
                let shared = item
                    .get("parameters")
                    .and_then(serde_yaml_ng::Value::as_sequence);
                let local = operation
                    .get("parameters")
                    .and_then(serde_yaml_ng::Value::as_sequence);
                for parameter in shared
                    .into_iter()
                    .flatten()
                    .chain(local.into_iter().flatten())
                {
                    let parameter = parameter
                        .get("$ref")
                        .and_then(serde_yaml_ng::Value::as_str)
                        .and_then(|reference| reference.strip_prefix('#'))
                        .and_then(|pointer| yaml_pointer(&root, pointer))
                        .unwrap_or(parameter);
                    if parameter.get("in").and_then(serde_yaml_ng::Value::as_str) == Some("path") {
                        if let Some(name) =
                            parameter.get("name").and_then(serde_yaml_ng::Value::as_str)
                        {
                            if !route.contains(&format!("{{{name}}}")) {
                                return refusal(
                                    path,
                                    strict,
                                    Class::PathParameterUnreferenced,
                                    &format!(
                                        "{} {route} parameter {name}",
                                        method.to_ascii_uppercase()
                                    ),
                                );
                            }
                        }
                    }
                }
            }
        }
    }
    if let Some(element) = cyclic_extension(&root, &root, "", &mut ExtensionCycles::default()) {
        return refusal(path, strict, Class::ExtensionReferenceCycle, &element);
    }
    check_document_schemas(&root, path, strict)?;
    Ok(())
}

#[derive(Default)]
struct ExtensionCycles {
    active: std::collections::HashSet<String>,
    complete: std::collections::HashSet<String>,
}

fn extension_reference_cycle(
    node: &serde_yaml_ng::Value,
    root: &serde_yaml_ng::Value,
    state: &mut ExtensionCycles,
) -> bool {
    if let Some(reference) = node.get("$ref").and_then(serde_yaml_ng::Value::as_str) {
        let Some(pointer) = reference.strip_prefix('#') else {
            return false;
        };
        if state.complete.contains(reference) {
            return false;
        }
        if !state.active.insert(reference.to_owned()) {
            return true;
        }
        let cycle = yaml_pointer(root, pointer)
            .is_some_and(|target| cyclic_extension(target, root, "", state).is_some());
        state.active.remove(reference);
        if !cycle {
            state.complete.insert(reference.to_owned());
        }
        return cycle;
    }
    match node {
        serde_yaml_ng::Value::Mapping(values) => values
            .values()
            .any(|value| extension_reference_cycle(value, root, state)),
        serde_yaml_ng::Value::Sequence(values) => values
            .iter()
            .any(|value| extension_reference_cycle(value, root, state)),
        _ => false,
    }
}

fn cyclic_extension(
    node: &serde_yaml_ng::Value,
    root: &serde_yaml_ng::Value,
    element: &str,
    state: &mut ExtensionCycles,
) -> Option<String> {
    if ignored_reference_node(node) {
        return None;
    }
    match node {
        serde_yaml_ng::Value::Mapping(values) => {
            for (key, value) in values {
                let Some(key) = key.as_str() else { continue };
                let child_element = if element.is_empty() {
                    key.to_owned()
                } else {
                    format!("{element}/{key}")
                };
                if key.starts_with("x-") {
                    if extension_reference_cycle(value, root, state) {
                        return Some(child_element);
                    }
                } else if !matches!(key, "example" | "examples" | "default" | "enum" | "const") {
                    if let Some(cycle) = cyclic_extension(value, root, &child_element, state) {
                        return Some(cycle);
                    }
                }
            }
        }
        serde_yaml_ng::Value::Sequence(values) => {
            for (index, value) in values.iter().enumerate() {
                if let Some(cycle) =
                    cyclic_extension(value, root, &format!("{element}/{index}"), state)
                {
                    return Some(cycle);
                }
            }
        }
        _ => {}
    }
    None
}

#[derive(Clone, Copy)]
enum SchemaLocation {
    Type,
    Field,
    Parameter,
    Query,
}

struct SchemaContext<'a> {
    root: &'a serde_yaml_ng::Value,
    path: &'a Path,
    strict: bool,
    names: indexmap::IndexMap<String, bool>,
    default_names: indexmap::IndexMap<String, bool>,
}

fn schema_declaration_names(
    root: &serde_yaml_ng::Value,
    include_literals: bool,
    declaration_kind: fn(&serde_yaml_ng::Value, &serde_yaml_ng::Value) -> bool,
) -> indexmap::IndexMap<String, bool> {
    let mut names = indexmap::IndexMap::new();
    if let Some(schemas) = root
        .get("components")
        .and_then(|value| value.get("schemas"))
        .and_then(serde_yaml_ng::Value::as_mapping)
    {
        for (key, schema) in schemas {
            if let Some(key) = key.as_str() {
                if ignored_reference_node(schema) {
                    continue;
                }
                let name = crate::naming::class_name(key);
                names.insert(name.clone(), declaration_kind(schema, root));
                register_inline_declarations(
                    schema,
                    &name,
                    root,
                    &mut names,
                    include_literals,
                    declaration_kind,
                );
            }
        }
    }
    names
}

fn register_inline_declarations(
    schema: &serde_yaml_ng::Value,
    parent: &str,
    root: &serde_yaml_ng::Value,
    names: &mut indexmap::IndexMap<String, bool>,
    include_literals: bool,
    declaration_kind: fn(&serde_yaml_ng::Value, &serde_yaml_ng::Value) -> bool,
) {
    if ignored_reference_node(schema) {
        return;
    }
    if let Some(properties) = schema
        .get("properties")
        .and_then(serde_yaml_ng::Value::as_mapping)
    {
        for (key, child) in properties {
            let Some(key) = key.as_str() else { continue };
            if ignored_reference_node(child) || child.get("$ref").is_some() {
                continue;
            }
            let name = crate::naming::child_class_name(parent, key);
            let union = ["oneOf", "anyOf"].iter().any(|key| {
                child
                    .get(key)
                    .and_then(serde_yaml_ng::Value::as_sequence)
                    .is_some_and(|variants| {
                        variants
                            .iter()
                            .filter(|value| {
                                value.get("type").and_then(serde_yaml_ng::Value::as_str)
                                    != Some("null")
                            })
                            .count()
                            > 1
                    })
            });
            let enumeration = child
                .get("enum")
                .and_then(serde_yaml_ng::Value::as_sequence)
                .is_some_and(|values| values.len() > usize::from(!include_literals))
                || include_literals && child.get("const").is_some();
            if union || enumeration {
                names.insert(name.clone(), declaration_kind(child, root));
            }
            register_inline_declarations(
                child,
                &name,
                root,
                names,
                include_literals,
                declaration_kind,
            );
        }
    }
    for key in ["oneOf", "anyOf", "allOf"] {
        if let Some(children) = schema.get(key).and_then(serde_yaml_ng::Value::as_sequence) {
            for child in children {
                register_inline_declarations(
                    child,
                    parent,
                    root,
                    names,
                    include_literals,
                    declaration_kind,
                );
            }
        }
    }
}

fn schema_is_model(
    schema: &serde_yaml_ng::Value,
    root: &serde_yaml_ng::Value,
    seen: &mut Vec<String>,
) -> bool {
    if let Some(reference) = schema.get("$ref").and_then(serde_yaml_ng::Value::as_str) {
        if seen.iter().any(|value| value == reference) {
            return false;
        }
        seen.push(reference.into());
        let result = reference
            .strip_prefix('#')
            .and_then(|pointer| yaml_pointer(root, pointer))
            .is_some_and(|target| schema_is_model(target, root, seen));
        seen.pop();
        return result;
    }
    let ty = schema_type(schema);
    if schema.get("enum").is_some()
        || matches!(
            ty.as_ref().and_then(crate::openapi::TypeField::primary),
            Some("string" | "number" | "integer" | "boolean" | "array" | "null")
        )
    {
        return false;
    }
    if schema
        .get("properties")
        .and_then(serde_yaml_ng::Value::as_mapping)
        .is_some()
    {
        return true;
    }
    if schema.get("oneOf").is_some() || schema.get("anyOf").is_some() {
        return false;
    }
    schema
        .get("allOf")
        .and_then(serde_yaml_ng::Value::as_sequence)
        .is_some_and(|children| {
            children
                .iter()
                .any(|child| schema_is_model(child, root, seen))
        })
}

fn schema_type(schema: &serde_yaml_ng::Value) -> Option<crate::openapi::TypeField> {
    schema
        .get("type")
        .and_then(|value| serde_yaml_ng::from_value(value.clone()).ok())
}

fn check_object_extension(
    schema: &serde_yaml_ng::Value,
    context: &SchemaContext<'_>,
    element: &str,
) -> Result<()> {
    let Some(children) = schema
        .get("allOf")
        .and_then(serde_yaml_ng::Value::as_sequence)
    else {
        return Ok(());
    };
    let references = children
        .iter()
        .filter_map(|child| child.get("$ref").and_then(serde_yaml_ng::Value::as_str))
        .collect::<Vec<_>>();
    let ty = schema_type(schema);
    let primary = ty.as_ref().and_then(crate::openapi::TypeField::primary);
    if matches!(
        primary,
        Some("string" | "number" | "integer" | "boolean" | "array" | "null")
    ) {
        return Ok(());
    }
    let object = primary == Some("object")
        || schema
            .get("properties")
            .and_then(serde_yaml_ng::Value::as_mapping)
            .is_some()
        || references.len() > 1
        || children
            .iter()
            .filter(|child| child.get("$ref").is_none())
            .any(|child| schema_is_model(child, context.root, &mut Vec::new()));
    if !object {
        return Ok(());
    }
    for reference in references {
        let Some(target) = reference
            .strip_prefix('#')
            .and_then(|pointer| yaml_pointer(context.root, pointer))
        else {
            continue;
        };
        if ignored_reference_node(target) {
            continue;
        }
        let named = reference
            .strip_prefix("#/components/schemas/")
            .filter(|key| !key.contains('/'))
            .map(|key| crate::naming::class_name(&key.replace("~1", "/").replace("~0", "~")));
        let model = named
            .as_ref()
            .and_then(|name| context.names.get(name))
            .copied()
            .unwrap_or_else(|| schema_is_model(target, context.root, &mut Vec::new()));
        if !model {
            return refusal(
                context.path,
                context.strict,
                Class::ObjectExtendsNonObject,
                &format!("{element}/allOf extends {reference}"),
            );
        }
    }
    Ok(())
}

fn named_default_unsupported(schema: &serde_yaml_ng::Value, root: &serde_yaml_ng::Value) -> bool {
    if schema.get("enum").is_some()
        || schema.get("const").is_some()
        || matches!(
            schema_type(schema)
                .as_ref()
                .and_then(crate::openapi::TypeField::primary),
            Some("string" | "number" | "integer" | "boolean" | "array" | "null")
        )
    {
        return false;
    }
    schema_is_model(schema, root, &mut Vec::new())
        || ["oneOf", "anyOf"].iter().any(|key| {
            schema
                .get(key)
                .and_then(serde_yaml_ng::Value::as_sequence)
                .is_some_and(|variants| {
                    variants
                        .iter()
                        .filter(|variant| {
                            variant.get("type").and_then(serde_yaml_ng::Value::as_str)
                                != Some("null")
                        })
                        .count()
                        > 1
                })
        })
}

fn check_named_type_defaults(
    schema: &serde_yaml_ng::Value,
    parent: &str,
    context: &SchemaContext<'_>,
    element: &str,
) -> Result<()> {
    if ignored_reference_node(schema) {
        return Ok(());
    }
    if let Some(properties) = schema
        .get("properties")
        .and_then(serde_yaml_ng::Value::as_mapping)
    {
        for (key, child) in properties {
            let Some(key) = key.as_str() else { continue };
            if ignored_reference_node(child) || child.get("$ref").is_some() {
                continue;
            }
            let name = crate::naming::child_class_name(parent, key);
            let child_element = format!("{element}/properties/{key}");
            let enumeration = child
                .get("enum")
                .and_then(serde_yaml_ng::Value::as_sequence)
                .is_some_and(|values| !values.is_empty())
                || child.get("const").is_some();
            if child.get("default").is_some_and(|value| !value.is_null())
                && enumeration
                && context.default_names.get(&name).copied().unwrap_or(false)
            {
                return refusal(
                    context.path,
                    context.strict,
                    Class::NamedTypeDefault,
                    &format!("{child_element}/default"),
                );
            }
            check_named_type_defaults(child, &name, context, &child_element)?;
        }
    }
    for key in ["oneOf", "anyOf", "allOf"] {
        if let Some(variants) = schema.get(key).and_then(serde_yaml_ng::Value::as_sequence) {
            for (index, child) in variants.iter().enumerate() {
                check_named_type_defaults(
                    child,
                    parent,
                    context,
                    &format!("{element}/{key}/{index}"),
                )?;
            }
        }
    }
    Ok(())
}

fn check_document_schemas(root: &serde_yaml_ng::Value, path: &Path, strict: bool) -> Result<()> {
    let context = SchemaContext {
        root,
        path,
        strict,
        names: schema_declaration_names(root, false, |schema, root| {
            schema_is_model(schema, root, &mut Vec::new())
        }),
        default_names: schema_declaration_names(root, true, named_default_unsupported),
    };
    if let Some(schemas) = root
        .get("components")
        .and_then(|value| value.get("schemas"))
        .and_then(serde_yaml_ng::Value::as_mapping)
    {
        for (name, schema) in schemas {
            if let Some(name) = name.as_str() {
                check_named_type_defaults(
                    schema,
                    &crate::naming::class_name(name),
                    &context,
                    &format!("components/schemas/{name}"),
                )?;
                check_schema(
                    schema,
                    &context,
                    &format!("components/schemas/{name}"),
                    SchemaLocation::Type,
                    &mut std::collections::HashSet::new(),
                )?;
            }
        }
    }
    if let Some(paths) = root.get("paths").and_then(serde_yaml_ng::Value::as_mapping) {
        for (route, item) in paths {
            let Some(route) = route.as_str() else {
                continue;
            };
            for method in [
                "get", "put", "post", "delete", "options", "head", "patch", "trace",
            ] {
                let Some(operation) = item.get(method) else {
                    continue;
                };
                if ignored_reference_node(operation) {
                    continue;
                }
                let mut seen = std::collections::HashSet::new();
                if let Some(parameters) = item.get("parameters") {
                    check_bound_schemas(
                        parameters,
                        &context,
                        &format!("paths/{route}/parameters"),
                        &mut seen,
                    )?;
                }
                for key in ["parameters", "requestBody", "responses"] {
                    if let Some(value) = operation.get(key) {
                        check_bound_schemas(
                            value,
                            &context,
                            &format!("paths/{route}/{method}/{key}"),
                            &mut seen,
                        )?;
                    }
                }
            }
        }
    }
    Ok(())
}

fn check_bound_schemas(
    node: &serde_yaml_ng::Value,
    context: &SchemaContext<'_>,
    element: &str,
    seen: &mut std::collections::HashSet<String>,
) -> Result<()> {
    if ignored_reference_node(node) {
        return Ok(());
    }
    if let Some(reference) = node.get("$ref").and_then(serde_yaml_ng::Value::as_str) {
        if let Some(pointer) = reference.strip_prefix('#') {
            if seen.insert(reference.to_owned()) {
                if let Some(target) = yaml_pointer(context.root, pointer) {
                    check_bound_schemas(target, context, reference, seen)?;
                }
            }
        }
        return Ok(());
    }
    match node {
        serde_yaml_ng::Value::Mapping(values) => {
            for (key, value) in values {
                let key = key
                    .as_str()
                    .map(str::to_owned)
                    .or_else(|| key.as_i64().map(|key| key.to_string()));
                let Some(key) = key else { continue };
                if key == "schema" {
                    let location = match node.get("in").and_then(serde_yaml_ng::Value::as_str) {
                        Some("query") => SchemaLocation::Query,
                        Some(_) => SchemaLocation::Parameter,
                        None => SchemaLocation::Type,
                    };
                    let name = node.get("name").and_then(serde_yaml_ng::Value::as_str);
                    let schema_element = name.map_or_else(
                        || format!("{element}/schema"),
                        |name| format!("{element}/{name}/schema"),
                    );
                    if node.get("in").and_then(serde_yaml_ng::Value::as_str) == Some("header")
                        // llmlint: ignore[contracts_have_one_source_or_a_drift_gate] These are Fern's inline-header declaration exceptions, measured in generator-missing-type/evaluation-logs/fern-*-header.log, not SDK transport ownership. In particular Authorization is a per-method SDK parameter without an auth scheme (ir::is_auth_managed_header), while Fern declares its inline enum successfully. Changing SDK header ownership must not change this refusal classification; the CLI controls preserve all three measured exceptions.
                        && name.is_some_and(|name| {
                            !["Authorization", "User-Agent", "Content-Type"]
                                .iter()
                                .any(|exception| name.eq_ignore_ascii_case(exception))
                        })
                        && !ignored_reference_node(value)
                        && value.get("$ref").is_none()
                        && value
                            .get("type")
                            .is_none_or(|kind| kind.as_str() == Some("string"))
                        && (value
                            .get("enum")
                            .and_then(serde_yaml_ng::Value::as_sequence)
                            .is_some_and(|values| {
                                !values.is_empty()
                                    && values.iter().all(|value| value.as_str().is_some())
                            })
                            || value
                                .get("const")
                                .is_some_and(|value| value.as_str().is_some()))
                    {
                        return refusal(
                            context.path,
                            context.strict,
                            Class::GeneratorMissingType,
                            &schema_element,
                        );
                    }
                    check_schema_resolution(
                        value,
                        context,
                        &schema_element,
                        false,
                        &mut std::collections::HashSet::new(),
                    )?;
                    check_schema(value, context, &schema_element, location, seen)?;
                } else if !matches!(
                    key.as_str(),
                    "example" | "examples" | "default" | "enum" | "links" | "headers" | "encoding"
                ) && !key.starts_with("x-")
                {
                    check_bound_schemas(value, context, &format!("{element}/{key}"), seen)?;
                }
            }
        }
        serde_yaml_ng::Value::Sequence(values) => {
            for (index, value) in values.iter().enumerate() {
                check_bound_schemas(value, context, &format!("{element}/{index}"), seen)?;
            }
        }
        _ => {}
    }
    Ok(())
}

fn check_schema_resolution(
    schema: &serde_yaml_ng::Value,
    context: &SchemaContext<'_>,
    element: &str,
    required: bool,
    seen: &mut std::collections::HashSet<String>,
) -> Result<()> {
    if ignored_reference_node(schema) {
        return Ok(());
    }
    if let Some(reference) = schema.get("$ref").and_then(serde_yaml_ng::Value::as_str) {
        let Some(pointer) = reference.strip_prefix('#') else {
            return Ok(());
        };
        let target = yaml_pointer(context.root, pointer);
        let schema_reference = reference.strip_prefix("#/components/schemas/");
        let unsupported_definition = schema_reference.is_some_and(|suffix| {
            let mut parts = suffix.split('/').skip(1);
            while let Some(part) = parts.next() {
                match part {
                    "definitions" | "$defs" => return true,
                    "properties" | "patternProperties" | "dependentSchemas" | "allOf" | "oneOf"
                    | "anyOf" | "prefixItems" => {
                        parts.next();
                    }
                    _ => {}
                }
            }
            false
        });
        if required && schema_reference.is_some() && (target.is_none() || unsupported_definition) {
            return refusal(
                context.path,
                context.strict,
                Class::UnresolvedSchemaReference,
                &format!("{element} reference {reference}"),
            );
        }
        if !unsupported_definition && seen.insert(reference.to_owned()) {
            if let Some(target) = target {
                check_schema_resolution(target, context, element, required, seen)?;
            }
        }
        return Ok(());
    }
    if let Some(properties) = schema
        .get("properties")
        .and_then(serde_yaml_ng::Value::as_mapping)
    {
        let required_fields = schema
            .get("required")
            .and_then(serde_yaml_ng::Value::as_sequence);
        for (name, child) in properties {
            let Some(name) = name.as_str() else { continue };
            let required = required_fields
                .is_some_and(|fields| fields.iter().any(|field| field.as_str() == Some(name)));
            check_schema_resolution(
                child,
                context,
                &format!("{element}/properties/{name}"),
                required,
                seen,
            )?;
        }
    }
    for key in ["items", "additionalProperties"] {
        if let Some(child) = schema.get(key) {
            check_schema_resolution(child, context, &format!("{element}/{key}"), false, seen)?;
        }
    }
    for key in ["allOf", "oneOf", "anyOf"] {
        if let Some(children) = schema.get(key).and_then(serde_yaml_ng::Value::as_sequence) {
            for (index, child) in children.iter().enumerate() {
                check_schema_resolution(
                    child,
                    context,
                    &format!("{element}/{key}/{index}"),
                    false,
                    seen,
                )?;
            }
        }
    }
    Ok(())
}

fn check_schema(
    schema: &serde_yaml_ng::Value,
    context: &SchemaContext<'_>,
    element: &str,
    location: SchemaLocation,
    seen: &mut std::collections::HashSet<String>,
) -> Result<()> {
    if ignored_reference_node(schema) {
        return Ok(());
    }
    if let Some(reference) = schema.get("$ref").and_then(serde_yaml_ng::Value::as_str) {
        if let Some(pointer) = reference.strip_prefix('#') {
            if seen.insert(reference.to_owned()) {
                if let Some(target) = yaml_pointer(context.root, pointer) {
                    check_schema(
                        target,
                        context,
                        reference.trim_start_matches("#/"),
                        SchemaLocation::Type,
                        seen,
                    )?;
                }
            }
        }
    }
    check_object_extension(schema, context, element)?;
    if let Some(default) = schema
        .get("default")
        .filter(|value| !value.is_null() && !matches!(location, SchemaLocation::Type))
    {
        if matches!(location, SchemaLocation::Field)
            && schema.get("type").and_then(serde_yaml_ng::Value::as_str) == Some("array")
            && default.as_sequence().is_none()
        {
            return refusal(
                context.path,
                context.strict,
                Class::ListDefaultNotArray,
                &format!("{element} default {default:?}"),
            );
        }
        let invalid = match schema.get("type").and_then(serde_yaml_ng::Value::as_str) {
            Some("integer") => default.as_f64().is_none_or(|value| value.fract() != 0.0),
            Some("number") => default.as_f64().is_none(),
            _ => false,
        };
        if invalid {
            return refusal(
                context.path,
                context.strict,
                Class::DefaultNotValidForType,
                &format!("{element} default {default:?}"),
            );
        }
    }
    if let Some(properties) = schema
        .get("properties")
        .and_then(serde_yaml_ng::Value::as_mapping)
    {
        for (name, child) in properties {
            if let Some(name) = name.as_str() {
                check_schema(
                    child,
                    context,
                    &format!("{element}/properties/{name}"),
                    SchemaLocation::Field,
                    seen,
                )?;
            }
        }
    }
    for key in ["items", "additionalProperties"] {
        if let Some(child) = schema.get(key) {
            check_schema(
                child,
                context,
                &format!("{element}/{key}"),
                SchemaLocation::Type,
                seen,
            )?;
        }
    }
    for key in ["allOf", "oneOf", "anyOf"] {
        if let Some(children) = schema.get(key).and_then(serde_yaml_ng::Value::as_sequence) {
            for (index, child) in children.iter().enumerate() {
                check_schema(
                    child,
                    context,
                    &format!("{element}/{key}/{index}"),
                    SchemaLocation::Type,
                    seen,
                )?;
            }
        }
    }
    Ok(())
}

// Schema numeric bounds can exceed u64 in refused documents. Preserve the
// reference structure without requiring the SDK loader to accept those bounds.
struct ReferenceDocument(serde_yaml_ng::Value);

impl<'de> serde::Deserialize<'de> for ReferenceDocument {
    fn deserialize<D: serde::Deserializer<'de>>(
        deserializer: D,
    ) -> std::result::Result<Self, D::Error> {
        struct Visitor;
        impl<'de> serde::de::Visitor<'de> for Visitor {
            type Value = ReferenceDocument;
            fn expecting(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
                f.write_str("an OpenAPI reference document")
            }
            fn visit_unit<E: serde::de::Error>(self) -> std::result::Result<Self::Value, E> {
                Ok(ReferenceDocument(serde_yaml_ng::Value::Null))
            }
            fn visit_bool<E: serde::de::Error>(
                self,
                value: bool,
            ) -> std::result::Result<Self::Value, E> {
                Ok(ReferenceDocument(value.into()))
            }
            fn visit_i64<E: serde::de::Error>(
                self,
                value: i64,
            ) -> std::result::Result<Self::Value, E> {
                Ok(ReferenceDocument(value.into()))
            }
            fn visit_u64<E: serde::de::Error>(
                self,
                value: u64,
            ) -> std::result::Result<Self::Value, E> {
                Ok(ReferenceDocument(value.into()))
            }
            fn visit_i128<E: serde::de::Error>(
                self,
                _value: i128,
            ) -> std::result::Result<Self::Value, E> {
                Ok(ReferenceDocument(serde_yaml_ng::Value::Null))
            }
            fn visit_u128<E: serde::de::Error>(
                self,
                _value: u128,
            ) -> std::result::Result<Self::Value, E> {
                Ok(ReferenceDocument(serde_yaml_ng::Value::Null))
            }
            fn visit_f64<E: serde::de::Error>(
                self,
                value: f64,
            ) -> std::result::Result<Self::Value, E> {
                Ok(ReferenceDocument(value.into()))
            }
            fn visit_str<E: serde::de::Error>(
                self,
                value: &str,
            ) -> std::result::Result<Self::Value, E> {
                Ok(ReferenceDocument(value.into()))
            }
            fn visit_string<E: serde::de::Error>(
                self,
                value: String,
            ) -> std::result::Result<Self::Value, E> {
                Ok(ReferenceDocument(value.into()))
            }
            fn visit_seq<A: serde::de::SeqAccess<'de>>(
                self,
                mut sequence: A,
            ) -> std::result::Result<Self::Value, A::Error> {
                let mut values = Vec::new();
                while let Some(ReferenceDocument(value)) = sequence.next_element()? {
                    values.push(value);
                }
                Ok(ReferenceDocument(serde_yaml_ng::Value::Sequence(values)))
            }
            fn visit_map<A: serde::de::MapAccess<'de>>(
                self,
                mut map: A,
            ) -> std::result::Result<Self::Value, A::Error> {
                let mut values = serde_yaml_ng::Mapping::new();
                while let Some((ReferenceDocument(key), ReferenceDocument(value))) =
                    map.next_entry()?
                {
                    if values.insert(key, value).is_some() {
                        return Err(serde::de::Error::custom("duplicate document key"));
                    }
                }
                Ok(ReferenceDocument(serde_yaml_ng::Value::Mapping(values)))
            }
        }
        deserializer.deserialize_any(Visitor)
    }
}

fn ignored_reference_node(value: &serde_yaml_ng::Value) -> bool {
    // Keep the dual-header decision in the existing canonical accessor.
    let mut extensions = serde_yaml_ng::Mapping::new();
    for name in ["x-crozier-ignore", "x-fern-ignore"] {
        if let Some(value) = value.get(name) {
            extensions.insert(serde_yaml_ng::Value::String(name.into()), value.clone());
        }
    }
    serde_yaml_ng::from_value::<crate::openapi::Schema>(serde_yaml_ng::Value::Mapping(extensions))
        .is_ok_and(|schema| schema.ignored())
}

fn check_named_examples(
    examples: &serde_yaml_ng::Value,
    root: &serde_yaml_ng::Value,
    path: &Path,
    strict: bool,
    element: &str,
) -> Result<()> {
    let Some(examples) = examples.as_mapping() else {
        return Ok(());
    };
    for (name, example) in examples {
        let Some(name) = name.as_str() else {
            continue;
        };
        let Some(reference) = example.get("$ref").and_then(serde_yaml_ng::Value::as_str) else {
            continue;
        };
        if let Some(target) = reference.strip_prefix("#/components/examples/") {
            if target.contains('/') || yaml_pointer(root, &reference[1..]).is_none() {
                return refusal(
                    path,
                    strict,
                    Class::UndefinedComponentReference,
                    &format!("{element}/{name}: {reference}"),
                );
            }
        }
        // `value` is example data, so a $ref inside it is never traversed.
    }
    Ok(())
}

fn check_reference_objects(
    value: &serde_yaml_ng::Value,
    root: &serde_yaml_ng::Value,
    path: &Path,
    strict: bool,
    element: &str,
) -> Result<()> {
    use serde_yaml_ng::Value;
    match value {
        Value::Mapping(mapping) => {
            if ignored_reference_node(value) {
                return Ok(());
            }
            if let Some(reference) = value.get("$ref").and_then(Value::as_str) {
                let expected = [
                    ("/securitySchemes/", "securitySchemes"),
                    ("/responses/", "responses"),
                    ("/requestBodies/", "requestBodies"),
                    ("/requestBody", "requestBodies"),
                    ("/parameters/", "parameters"),
                    ("/headers/", "headers"),
                ]
                .into_iter()
                .filter_map(|(marker, kind)| element.rfind(marker).map(|index| (index, kind)))
                .max_by_key(|(index, _)| *index)
                .map(|(_, kind)| kind);
                let missing = if let Some(pointer) = reference.strip_prefix('#') {
                    if expected == Some("parameters")
                        && reference.starts_with("#/components/parameters/")
                        && yaml_pointer(root, pointer).is_none()
                    {
                        return refusal(
                            path,
                            strict,
                            Class::UndefinedComponentReference,
                            &format!("{element}: {reference}"),
                        );
                    }
                    expected.is_some_and(|kind| {
                        !reference.starts_with(&format!("#/components/{kind}/"))
                    }) || yaml_pointer(root, pointer).is_none()
                } else if let Some((file, _)) = reference.split_once('#') {
                    !file.contains("://")
                        && !path
                            .parent()
                            .unwrap_or_else(|| Path::new("."))
                            .join(file)
                            .is_file()
                } else {
                    false
                };
                if missing {
                    return refusal(
                        path,
                        strict,
                        Class::UnresolvedReference,
                        &format!("{element}: {reference}"),
                    );
                }
            }
            for (key, child) in mapping {
                let key = if let Some(key) = key.as_str() {
                    key.to_owned()
                } else if let Some(key) = key.as_i64() {
                    key.to_string()
                } else {
                    continue;
                };
                if key == "examples" {
                    check_named_examples(
                        child,
                        root,
                        path,
                        strict,
                        &format!("{element}/examples"),
                    )?;
                    continue;
                }
                if matches!(
                    key.as_str(),
                    "schema" | "schemas" | "example" | "examples" | "default" | "enum" | "const"
                ) || key.starts_with("x-")
                {
                    continue;
                }
                check_reference_objects(child, root, path, strict, &format!("{element}/{key}"))?;
            }
        }
        Value::Sequence(values) => {
            for (index, child) in values.iter().enumerate() {
                check_reference_objects(child, root, path, strict, &format!("{element}/{index}"))?;
            }
        }
        _ => {}
    }
    Ok(())
}

fn yaml_pointer<'a>(
    root: &'a serde_yaml_ng::Value,
    pointer: &str,
) -> Option<&'a serde_yaml_ng::Value> {
    if pointer.is_empty() {
        return Some(root);
    }
    let mut value = root;
    for token in pointer.strip_prefix('/')?.split('/') {
        let token = token.replace("~1", "/").replace("~0", "~");
        value = match value {
            serde_yaml_ng::Value::Sequence(sequence) => {
                sequence.get(token.parse::<usize>().ok()?)?
            }
            _ => value.get(token.as_str())?,
        };
    }
    Some(value)
}

fn check_version(version: &str, path: &Path, strict: bool) -> Result<()> {
    if version.starts_with("3.") && !version.starts_with("3.0.") && !version.starts_with("3.1.") {
        return refusal(
            path,
            strict,
            Class::UnsupportedOpenapiVersion,
            &format!("openapi {version}"),
        );
    }
    Ok(())
}

fn imported_scheme(scheme: &SecurityScheme) -> bool {
    (scheme.ty == SecuritySchemeType::ApiKey && scheme.location == Some(ParameterLocation::Header))
        || (scheme.ty == SecuritySchemeType::Http
            && matches!(
                scheme.scheme,
                Some(HttpAuthScheme::Bearer | HttpAuthScheme::Basic)
            ))
        || matches!(
            scheme.ty,
            SecuritySchemeType::OAuth2 | SecuritySchemeType::OpenIdConnect
        )
}

// Relative security references remain untouched by the SDK loader. Inspect the
// referenced declaration only to distinguish Fern-importable auth from a refusal.
fn imported_reference_scheme(scheme: &SecurityScheme, path: &Path) -> bool {
    let mut reference = scheme.reference.clone();
    let mut origin = path.to_path_buf();
    let mut seen = std::collections::HashSet::new();
    while let Some(next) = reference {
        if !seen.insert((origin.clone(), next.clone())) {
            return false;
        }
        let (document, pointer) = next.split_once('#').unwrap_or((&next, ""));
        if document.starts_with("https://") || document.starts_with("http://") {
            return false;
        }
        let target = if document.is_empty() {
            origin.clone()
        } else {
            origin.parent().unwrap_or(Path::new(".")).join(document)
        };
        let Ok(target) = target.canonicalize() else {
            return false;
        };
        let Some(root) = std::fs::read_to_string(&target)
            .ok()
            .and_then(|text| serde_yaml_ng::from_str::<ReferenceDocument>(&text).ok())
        else {
            return false;
        };
        let Some(value) = yaml_pointer(&root.0, pointer) else {
            return false;
        };
        let Ok(resolved) = serde_yaml_ng::from_value::<SecurityScheme>(value.clone()) else {
            return false;
        };
        if resolved.reference.is_none() {
            return imported_scheme(&resolved);
        }
        origin = target;
        reference = resolved.reference;
    }
    false
}

/// Reject an evaluated class before rendering or writing an SDK.
pub fn check(doc: &OpenApi, path: &Path, strict: bool) -> Result<()> {
    check_version(&doc.openapi, path, strict)?;
    // Inline scheme support is reconciled with the SDK IR by imported_auth_agrees_with_sdk_ir.
    // Relative references use the separately measured Fern importer boundary.
    let imported_auth = doc
        .components
        .security_schemes
        .values()
        .any(|scheme| imported_scheme(scheme) || imported_reference_scheme(scheme, path));
    if imported_auth {
        return Ok(());
    }
    // A service is created from an operation, not an unresolved Path Item
    // Reference Object. The OneVoice golden has only the latter and Fern
    // accepts it despite its document-wide cookie security requirement.
    if doc.paths.values().all(|item| item.operations().is_empty()) {
        return Ok(());
    }
    // Fern lifts inherited authentication to a service only when every
    // operation in that service requires it. A public operation leaves the
    // private operations' requirements on the endpoints instead.
    let mut groups = std::collections::BTreeMap::<Vec<String>, bool>::new();
    // llmlint: ignore[contracts_have_one_source_or_a_drift_gate] These are Fern importer services, not SDK modules. IR endpoint_module intentionally flattens a tag when its operationId matches the tag and derives dotted-id groups for untagged operations; those emission choices must not change Fern's auth refusal classification. The mixed-service CLI journey and population class checks guard this measured distinction.
    for item in doc.paths.values() {
        for (_, op) in item.operations() {
            let group = op.sdk_group_name().unwrap_or_else(|| {
                op.tags
                    .first()
                    .map_or_else(Vec::new, |tag| vec![tag.as_str()])
            });
            let group: Vec<String> = group
                .into_iter()
                .map(crate::naming::to_snake_case)
                .collect();
            let required = op
                .security
                .as_ref()
                .or(doc.security.as_ref())
                .is_some_and(|requirements| !requirements.is_empty());
            groups
                .entry(group)
                .and_modify(|all| *all &= required)
                .or_insert(required);
        }
    }
    if let Some(requirements) = &doc.security {
        if !requirements.is_empty() && groups.values().any(|&required| required) {
            let scheme = requirements.iter().flat_map(|r| r.keys()).next();
            let element = scheme.map_or_else(|| "security/0".into(), |s| format!("security/{s}"));
            return refusal(path, strict, Class::ServiceAuthUndefined, &element);
        }
    }
    for (route, item) in &doc.paths {
        for (method, op) in item.operations() {
            if let Some(requirements) = op.security.as_ref().or(doc.security.as_ref()) {
                if !requirements.is_empty() {
                    let scheme = requirements.iter().flat_map(|r| r.keys()).next();
                    let element = scheme.map_or_else(
                        || format!("{method} {route} security/0"),
                        |s| format!("{method} {route} security/{s}"),
                    );
                    return refusal(path, strict, Class::EndpointAuthUndefined, &element);
                }
            }
        }
    }
    Ok(())
}

fn refusal(path: &Path, strict: bool, class: Class, element: &str) -> Result<()> {
    Err(Error::InvalidSpec {
        path: path.to_path_buf(),
        message: format!(
            "{}: {element}{}",
            class.id(),
            if strict { " (fern-strict refusal)" } else { "" }
        ),
    })
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn reference_objects_exclude_schemas_and_path_items_and_honor_ignores() {
        let dir = tempfile::tempdir().unwrap();
        let file = dir.path().join("api.yml");
        for content in [
            "paths: {/probe: {$ref: 'absent.yml#/item'}}",
            "components: {schemas: {Thing: {$ref: '#/components/schemas/Absent'}}}",
            "components: {responses: {Error: {content: {application/json: {schema: {$ref: '#/components/schemas/Absent'}}}}}}",
            "components: {securitySchemes: {Bearer: {x-crozier-ignore: true, $ref: 'absent.yml#/Bearer'}}}",
        ] {
            std::fs::write(&file, content).unwrap();
            check_structure_file(&file, true).unwrap();
        }
        std::fs::write(&file, "components: {securitySchemes: {Bearer: {x-crozier-ignore: false, x-fern-ignore: true, $ref: 'absent.yml#/Bearer'}}}").unwrap();
        let error = check_structure_file(&file, true).unwrap_err().to_string();
        assert!(error.contains("unresolved-reference: components/securitySchemes/Bearer"));
        assert!(error.contains("fern-strict"));
        std::fs::write(
            dir.path().join("absent.yml"),
            "Bearer: {type: http, scheme: bearer}",
        )
        .unwrap();
        check_structure_file(&file, false).unwrap();
        std::fs::write(&file, "paths: {/probe: {get: {responses: {401: {$ref: '#/$defs/Denied'}}}}}\n$defs: {Denied: {description: Unauthorized}}\ncomponents: {schemas: {Bound: {maximum: 18446744073709552000}}}").unwrap();
        let error = check_structure_file(&file, false).unwrap_err().to_string();
        assert!(error.contains("unresolved-reference: paths//probe/get/responses/401"));
    }

    #[test]
    fn reference_pointer_decodes_escaped_paths_and_array_indices() {
        let root = serde_yaml_ng::from_str("paths: {'/probe': {get: {parameters: [{name: id}]}}}")
            .unwrap();
        assert!(yaml_pointer(&root, "/paths/~1probe/get/parameters/0").is_some());
        assert!(yaml_pointer(&root, "/paths/~1probe/get/parameters/1").is_none());
    }

    #[test]
    fn imported_auth_agrees_with_sdk_ir() {
        use SecuritySchemeType::*;
        for ty in [ApiKey, Http, OAuth2, OpenIdConnect, MutualTls, Other] {
            let name = match ty {
                ApiKey => "apiKey",
                Http => "http",
                OAuth2 => "oauth2",
                OpenIdConnect => "openIdConnect",
                MutualTls => "mutualTLS",
                Other => "unknown",
            };
            for location in ["header", "cookie", "query"] {
                for scheme in [
                    HttpAuthScheme::Bearer,
                    HttpAuthScheme::Basic,
                    HttpAuthScheme::Other,
                ] {
                    let scheme = match scheme {
                        HttpAuthScheme::Bearer => "bearer",
                        HttpAuthScheme::Basic => "basic",
                        HttpAuthScheme::Other => "unknown",
                    };
                    let doc = document("security: [{session: []}]",
                        &format!("      type: {name}\n      in: {location}\n      name: SESSION\n      scheme: {scheme}"), OP);
                    let config = crate::config::GenerateConfig::new(
                        "api.yml".into(),
                        "sdk".into(),
                        Some("fern".into()),
                        None,
                        None,
                        crate::settings::ExtraFields::default(),
                        "Probe",
                    )
                    .unwrap();
                    let ir = crate::ir::build(&doc, &config);
                    assert_eq!(
                        check(&doc, Path::new("api.yml"), false).is_err(),
                        matches!(ir.auth, crate::ir::Auth::None),
                        "{name}/{location}/{scheme}"
                    );
                }
            }
        }
    }

    fn document(security: &str, scheme: &str, paths: &str) -> OpenApi {
        serde_yaml_ng::from_str(&format!(
            "openapi: 3.0.3\n{security}\ncomponents:\n  securitySchemes:\n    session:\n{scheme}\npaths:\n{paths}\n"
        ))
        .unwrap()
    }

    const COOKIE: &str = "      type: apiKey\n      in: cookie\n      name: SESSION";
    const OP: &str = "  /probe:\n    get:\n      operationId: probe\n      responses: {}";

    #[test]
    fn openapi_32_is_refused_but_30_and_31_are_accepted() {
        let mut doc = document("", COOKIE, OP);
        for version in ["3.0.3", "3.1.0", "3.1.1"] {
            doc.openapi = version.into();
            check(&doc, Path::new("api.yml"), true).unwrap();
        }
        doc.openapi = "3.2.0".into();
        for strict in [false, true] {
            let error = check(&doc, Path::new("api.yml"), strict).unwrap_err();
            assert!(error
                .to_string()
                .contains("unsupported-openapi-version: openapi 3.2.0"));
        }
    }

    #[test]
    fn security_without_imported_auth_names_the_service_and_strict_cause() {
        let doc = document("security: [{session: []}]", COOKIE, OP);
        let error = check(&doc, Path::new("api.yml"), true).unwrap_err();
        assert!(error
            .to_string()
            .contains("service-auth-undefined: security/session"));
        assert!(error.to_string().contains("fern-strict"));
    }

    #[test]
    fn unsupported_unselected_schemes_and_path_refs_create_no_refusal() {
        let doc = document("", COOKIE, OP);
        check(&doc, Path::new("api.yml"), false).unwrap();
        let doc = document(
            "security: [{session: []}]",
            COOKIE,
            "  /probe:\n    $ref: paths.yml#/probe",
        );
        check(&doc, Path::new("api.yml"), true).unwrap();
    }

    #[test]
    fn a_later_imported_scheme_prevents_an_auth_refusal() {
        let mut doc = document("security: [{session: []}]", COOKIE, OP);
        let bearer = serde_yaml_ng::from_str("type: http\nscheme: bearer").unwrap();
        doc.components
            .security_schemes
            .insert("bearer".into(), bearer);
        check(&doc, Path::new("api.yml"), true).unwrap();
    }

    #[test]
    fn a_public_operation_makes_inherited_auth_an_endpoint_requirement() {
        let doc = document(
            "security: [{session: []}]",
            COOKIE,
            &format!("{OP}\n  /public:\n    get:\n      security: []\n      responses: {{}}"),
        );
        let error = check(&doc, Path::new("api.yml"), false).unwrap_err();
        assert!(error
            .to_string()
            .contains("endpoint-auth-undefined: GET /probe security/session"));
    }

    #[test]
    fn endpoint_security_names_the_method_and_route() {
        let doc = document(
            "",
            COOKIE,
            &format!("{OP}\n      security: [{{session: []}}]"),
        );
        let error = check(&doc, Path::new("api.yml"), false).unwrap_err();
        assert!(error
            .to_string()
            .contains("endpoint-auth-undefined: GET /probe security/session"));
    }
    #[test]
    fn referenced_auth_reads_real_files_and_rejects_cycles_and_invalid_targets() {
        let dir = tempfile::tempdir().unwrap();
        let origin = dir.path().join("openapi.yml");
        let reference = SecurityScheme {
            reference: Some("./components.json#/components/securitySchemes/Auth".into()),
            ..SecurityScheme::default()
        };
        let target = dir.path().join("components.json");
        for (scheme, imported) in [
            (r#"{"type":"http","scheme":"bearer"}"#, true),
            (r#"{"type":"apiKey","in":"cookie","name":"SID"}"#, false),
            (
                r##"{"$ref":"./.././components.json#/components/securitySchemes/Auth"}"##,
                false,
            ),
            (r#"{"type":42}"#, false),
        ] {
            let scheme = if scheme.contains("./../") {
                // Return to this directory through its parent without growing
                // the path spelling on each cycle.
                format!(
                    r##"{{"$ref":"../{}/components.json#/components/securitySchemes/Auth"}}"##,
                    dir.path().file_name().unwrap().to_str().unwrap()
                )
            } else {
                scheme.to_owned()
            };
            std::fs::write(
                &target,
                format!(r#"{{"components":{{"securitySchemes":{{"Auth":{scheme}}}}}}}"#),
            )
            .unwrap();
            assert_eq!(
                imported_reference_scheme(&reference, &origin),
                imported,
                "{scheme}"
            );
        }
        for text in ["not a document", "{", "{}"] {
            std::fs::write(&target, text).unwrap();
            assert!(!imported_reference_scheme(&reference, &origin));
        }
        std::fs::remove_file(target).unwrap();
        assert!(!imported_reference_scheme(&reference, &origin));
    }
}
