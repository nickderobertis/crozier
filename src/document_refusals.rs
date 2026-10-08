//! Structural refusals for the document-family Fern registry.
//!
//! These checks decide whether generation is allowed; they never rewrite the
//! document or repair the output measured in `docs/fern-refusals/`.

use std::path::Path;

use crate::openapi::{
    HttpAuthScheme, OpenApi, ParameterLocation, SecurityScheme, SecuritySchemeType,
};
use crate::{Error, Result};

mod type_not_defined;
use type_not_defined::undefined_type_reference;

mod examples;

#[derive(Clone, Copy)]
enum Class {
    UnsupportedOpenapiVersion,
    HeadRequestBody,
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
    HeapExhausted,
    DefaultNotEnumValue,
    GeneratorLintFailure,
    TypeNotDefined,
    MissingDiscriminantProperty,
    DuplicateExampleName,
    ExampleMissingRequiredQueryParameter,
    ExampleTypeMismatch,
    ExampleNotEnumValue,
    ExampleUnexpectedProperty,
    ExampleMissingRequiredProperty,
    HeaderDefaultDiffersAcrossOperations,
    VersionHeaderRedeclaredAsParameter,
}

impl Class {
    fn id(self) -> &'static str {
        match self {
            Self::UnsupportedOpenapiVersion => "unsupported-openapi-version",
            Self::HeadRequestBody => "head-request-body",
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
            Self::HeapExhausted => "heap-exhausted",
            Self::DefaultNotEnumValue => "default-not-enum-value",
            Self::GeneratorLintFailure => "generator-lint-failure",
            Self::TypeNotDefined => "type-not-defined",
            Self::MissingDiscriminantProperty => "missing-discriminant-property",
            Self::DuplicateExampleName => "duplicate-example-name",
            Self::ExampleMissingRequiredQueryParameter => {
                "example-missing-required-query-parameter"
            }
            Self::ExampleTypeMismatch => "example-type-mismatch",
            Self::ExampleNotEnumValue => "example-not-enum-value",
            Self::ExampleUnexpectedProperty => "example-unexpected-property",
            Self::ExampleMissingRequiredProperty => "example-missing-required-property",
            Self::HeaderDefaultDiffersAcrossOperations => {
                "header-default-differs-across-operations"
            }
            Self::VersionHeaderRedeclaredAsParameter => "version-header-redeclared-as-parameter",
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
    if let Some(element) =
        cyclic_extension(&root, &root, "", &mut ExtensionCycles::default(), false)
    {
        return refusal(path, strict, Class::ExtensionReferenceCycle, &element);
    }
    check_document_schemas(&root, path, strict)?;
    if let Some(element) = undefined_type_reference(&root) {
        return refusal(path, strict, Class::TypeNotDefined, &element);
    }
    check_discriminant_examples(&root, path, strict)?;
    check_example_names(&root, path, strict)?;
    check_example_query_parameters(&root, path, strict)?;
    if let Some((class, element)) = examples::first_violation(&root) {
        return refusal(path, strict, class, &element);
    }
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
            .is_some_and(|target| cyclic_extension(target, root, "", state, false).is_some());
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
    property_schema: bool,
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
                    if !(property_schema && value.get("$ref").is_some())
                        && extension_reference_cycle(value, root, state)
                    {
                        return Some(child_element);
                    }
                } else if key == "properties" {
                    if let Some(properties) = value.as_mapping() {
                        for (name, schema) in properties {
                            let Some(name) = name.as_str() else { continue };
                            if let Some(cycle) = cyclic_extension(
                                schema,
                                root,
                                &format!("{child_element}/{name}"),
                                state,
                                true,
                            ) {
                                return Some(cycle);
                            }
                        }
                    }
                } else if !matches!(key, "example" | "examples" | "default" | "enum" | "const") {
                    if let Some(cycle) = cyclic_extension(value, root, &child_element, state, false)
                    {
                        return Some(cycle);
                    }
                }
            }
        }
        serde_yaml_ng::Value::Sequence(values) => {
            for (index, value) in values.iter().enumerate() {
                if let Some(cycle) =
                    cyclic_extension(value, root, &format!("{element}/{index}"), state, false)
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
    missing_header_types: std::collections::HashSet<String>,
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

fn missing_header_types(root: &serde_yaml_ng::Value) -> std::collections::HashSet<String> {
    let mut total = 0usize;
    let mut headers: indexmap::IndexMap<String, (usize, String)> = indexmap::IndexMap::new();
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
                total += 1;
                // An operation crozier cannot read fails its own loader later.
                let Ok(parsed) =
                    serde_yaml_ng::from_value::<crate::openapi::Operation>(operation.clone())
                else {
                    continue;
                };
                let request_ctx = &crate::ir::request_context(&parsed, method, route);
                let mut in_operation = std::collections::HashSet::new();
                for parameters in [item.get("parameters"), operation.get("parameters")]
                    .into_iter()
                    .flatten()
                {
                    let Some(parameters) = parameters.as_sequence() else {
                        continue;
                    };
                    for parameter in parameters {
                        let parameter = parameter
                            .get("$ref")
                            .and_then(serde_yaml_ng::Value::as_str)
                            .and_then(|reference| reference.strip_prefix('#'))
                            .and_then(|pointer| yaml_pointer(root, pointer))
                            .unwrap_or(parameter);
                        if ignored_reference_node(parameter)
                            || parameter.get("in").and_then(serde_yaml_ng::Value::as_str)
                                != Some("header")
                        {
                            continue;
                        }
                        let Some(name) =
                            parameter.get("name").and_then(serde_yaml_ng::Value::as_str)
                        else {
                            continue;
                        };
                        if !in_operation.insert(name) {
                            continue;
                        }
                        let declaration = crate::ir::request_parameter_type_name(request_ctx, name);
                        let entry = headers.entry(name.to_owned()).or_insert((0, declaration));
                        entry.0 += 1;
                    }
                }
            }
        }
    }
    let declarations = schema_declaration_names(root, true, named_default_unsupported);
    headers
        .into_iter()
        .filter_map(|(name, (count, declaration))| {
            (total > 0 && count * 4 >= total * 3 && !declarations.contains_key(&declaration))
                .then_some(name)
        })
        .collect()
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
        missing_header_types: missing_header_types(root),
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

/// Fern validates each endpoint's example against its discriminated unions: a
/// `discriminator` with a non-empty `mapping` on a schema without `anyOf`. With
/// no `x-fern-examples` the example is Fern's own, which is `{}` at a union whose
/// every mapping target is missing; otherwise each `x-fern-examples` value is
/// checked. Plain OpenAPI examples and `x-crozier-examples` play no part: Fern
/// discards the first and never reads the second. Measured in
/// `docs/fern-refusals/missing-discriminant-property/evaluation.md`.
fn check_discriminant_examples(
    root: &serde_yaml_ng::Value,
    path: &Path,
    strict: bool,
) -> Result<()> {
    let Some(paths) = root.get("paths").and_then(serde_yaml_ng::Value::as_mapping) else {
        return Ok(());
    };
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
            let operation_element = format!("{} {route}", method.to_ascii_uppercase());
            let request = operation
                .get("requestBody")
                .map(|body| resolved_node(body, root))
                .and_then(json_schema)
                .map(|schema| (format!("{operation_element} request"), schema));
            let responses = operation
                .get("responses")
                .and_then(serde_yaml_ng::Value::as_mapping);
            let mut codes: Vec<(String, &serde_yaml_ng::Value)> = responses
                .into_iter()
                .flatten()
                .filter_map(|(code, response)| {
                    let code = code
                        .as_str()
                        .map(str::to_owned)
                        .or_else(|| code.as_u64().map(|code| code.to_string()))?;
                    let schema = json_schema(resolved_node(response, root))?;
                    (code.len() == 3 && code.bytes().all(|b| b.is_ascii_digit()))
                        .then_some((code, schema))
                })
                .collect();
            codes.sort_by(|left, right| left.0.cmp(&right.0));
            // Fern's endpoint response is the first 2xx body; 4xx and 5xx bodies are errors.
            let success = codes
                .iter()
                .find(|(code, _)| code.starts_with('2'))
                .map(|(code, schema)| (format!("{operation_element} response {code}"), *schema));
            let errors = codes
                .iter()
                .filter(|(code, _)| code.starts_with('4') || code.starts_with('5'))
                .map(|(code, schema)| (format!("{operation_element} response {code}"), *schema));
            if let Some(examples) = operation
                .get("x-fern-examples")
                .and_then(serde_yaml_ng::Value::as_sequence)
            {
                for (index, example) in examples.iter().enumerate() {
                    let checks = [
                        (example.get("request"), request.as_ref()),
                        (
                            example.get("response").and_then(|value| value.get("body")),
                            success.as_ref(),
                        ),
                    ];
                    for (value, schema) in checks {
                        let (Some(value), Some((element, schema))) = (value, schema) else {
                            continue;
                        };
                        if let Some(union) = example_without_discriminant(
                            value,
                            schema,
                            root,
                            &format!("{element} x-fern-examples/{index}"),
                            &mut std::collections::HashSet::new(),
                        ) {
                            return refusal(
                                path,
                                strict,
                                Class::MissingDiscriminantProperty,
                                &union,
                            );
                        }
                    }
                }
                continue;
            }
            for (element, schema) in request.into_iter().chain(success).chain(errors) {
                if let Some(union) = unmapped_union(
                    schema,
                    root,
                    "schema",
                    0,
                    &mut std::collections::HashSet::new(),
                ) {
                    return refusal(
                        path,
                        strict,
                        Class::MissingDiscriminantProperty,
                        &format!("{element} {union}"),
                    );
                }
            }
        }
    }
    Ok(())
}

fn resolved_node<'a>(
    node: &'a serde_yaml_ng::Value,
    root: &'a serde_yaml_ng::Value,
) -> &'a serde_yaml_ng::Value {
    node.get("$ref")
        .and_then(serde_yaml_ng::Value::as_str)
        .and_then(|reference| reference.strip_prefix('#'))
        .and_then(|pointer| yaml_pointer(root, pointer))
        .unwrap_or(node)
}

fn json_schema(body: &serde_yaml_ng::Value) -> Option<&serde_yaml_ng::Value> {
    if ignored_reference_node(body) {
        return None;
    }
    body.get("content")?.get("application/json")?.get("schema")
}

/// The property a discriminated union requires of its example, and its mapping.
fn discriminated_union(schema: &serde_yaml_ng::Value) -> Option<(&str, &serde_yaml_ng::Mapping)> {
    let discriminator = schema.get("discriminator")?;
    let property = discriminator
        .get("propertyName")
        .and_then(serde_yaml_ng::Value::as_str)?;
    let mapping = discriminator
        .get("mapping")
        .and_then(serde_yaml_ng::Value::as_mapping)
        .filter(|mapping| !mapping.is_empty())?;
    // Fern imports an `anyOf` discriminator as an undiscriminated union.
    schema.get("anyOf").is_none().then_some((property, mapping))
}

/// Fern omits an optional property from its example below three object levels.
const EXAMPLE_OPTIONAL_LEVELS: usize = 3;
/// The deepest required chain measured to carry Fern's example to a union.
const EXAMPLE_REQUIRED_LEVELS: usize = 12;

/// The union Fern's own example reaches with every mapping target missing: each
/// variant is then unknown and the example `{}` has no discriminant.
fn unmapped_union(
    schema: &serde_yaml_ng::Value,
    root: &serde_yaml_ng::Value,
    element: &str,
    levels: usize,
    seen: &mut std::collections::HashSet<(String, usize)>,
) -> Option<String> {
    if ignored_reference_node(schema) {
        return None;
    }
    if let Some(reference) = schema.get("$ref").and_then(serde_yaml_ng::Value::as_str) {
        let pointer = reference.strip_prefix('#')?;
        if !seen.insert((reference.to_owned(), levels)) {
            return None;
        }
        let target = yaml_pointer(root, pointer)?;
        return unmapped_union(
            target,
            root,
            reference.trim_start_matches("#/"),
            levels,
            seen,
        );
    }
    if let Some((property, mapping)) = discriminated_union(schema) {
        let missing = mapping.values().all(|target| {
            target
                .as_str()
                .and_then(|target| target.strip_prefix('#'))
                .is_some_and(|pointer| yaml_pointer(root, pointer).is_none())
        });
        // A resolved variant becomes Fern's example, so nothing below is reached.
        return missing.then(|| format!("{element} discriminator {property}"));
    }
    if levels < EXAMPLE_REQUIRED_LEVELS {
        if let Some(properties) = schema
            .get("properties")
            .and_then(serde_yaml_ng::Value::as_mapping)
        {
            let required = schema
                .get("required")
                .and_then(serde_yaml_ng::Value::as_sequence);
            for (name, child) in properties {
                let Some(name) = name.as_str() else { continue };
                let is_required = required
                    .is_some_and(|fields| fields.iter().any(|field| field.as_str() == Some(name)));
                if !is_required && levels >= EXAMPLE_OPTIONAL_LEVELS {
                    continue;
                }
                let child_element = format!("{element}/properties/{name}");
                if let Some(union) = unmapped_union(child, root, &child_element, levels + 1, seen) {
                    return Some(union);
                }
            }
        }
        for key in ["items", "additionalProperties"] {
            if let Some(child) = schema.get(key).filter(|child| child.is_mapping()) {
                let child_element = format!("{element}/{key}");
                if let Some(union) = unmapped_union(child, root, &child_element, levels + 1, seen) {
                    return Some(union);
                }
            }
        }
    }
    for key in ["allOf", "oneOf", "anyOf"] {
        if let Some(children) = schema.get(key).and_then(serde_yaml_ng::Value::as_sequence) {
            // Fern's example of an undiscriminated union is its first member's.
            let members = if key == "allOf" { children.len() } else { 1 };
            for (index, child) in children.iter().enumerate().take(members) {
                let child_element = format!("{element}/{key}/{index}");
                if let Some(union) = unmapped_union(child, root, &child_element, levels, seen) {
                    return Some(union);
                }
            }
        }
    }
    None
}

/// The union an `x-fern-examples` object reaches through `$ref`s and object
/// properties without naming the union's discriminant.
fn example_without_discriminant(
    example: &serde_yaml_ng::Value,
    schema: &serde_yaml_ng::Value,
    root: &serde_yaml_ng::Value,
    element: &str,
    seen: &mut std::collections::HashSet<String>,
) -> Option<String> {
    if ignored_reference_node(schema) {
        return None;
    }
    if let Some(reference) = schema.get("$ref").and_then(serde_yaml_ng::Value::as_str) {
        let pointer = reference.strip_prefix('#')?;
        if !seen.insert(reference.to_owned()) {
            return None;
        }
        let target = yaml_pointer(root, pointer)?;
        let union = example_without_discriminant(example, target, root, element, seen);
        seen.remove(reference);
        return union;
    }
    let example = example.as_mapping()?;
    if let Some((property, _)) = discriminated_union(schema) {
        return (schema.get("oneOf").is_some() && !example.contains_key(property))
            .then(|| format!("{element} discriminator {property}"));
    }
    let properties = schema
        .get("properties")
        .and_then(serde_yaml_ng::Value::as_mapping)?;
    example.iter().find_map(|(name, value)| {
        let child = properties.get(name)?;
        let name = name.as_str()?;
        example_without_discriminant(value, child, root, &format!("{element}/{name}"), seen)
    })
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
                            context.missing_header_types.contains(name)
                                && !["Authorization", "User-Agent", "Content-Type"]
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
        // A pointer naming `properties` is walked rather than resolved, and Fern
        // types one that reaches nothing as unknown rather than failing: a
        // required property pointing at `Named/properties/absent`, or at an
        // undeclared `Missing/properties/absent`, is a bare `Any`, and one
        // through `Named/properties/label/$defs/inner` is that `$defs` member
        // (the `358-absent-required-property`,
        // `358-undeclared-head-properties-required` and
        // `356-defs-required-property` authored probes).
        let walked = reference.contains("properties");
        if required
            && !walked
            && schema_reference.is_some()
            && (target.is_none() || unsupported_definition)
        {
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
            // Fern resolves only a union's first member's required fields.
            let members = if key == "allOf" { children.len() } else { 1 };
            for (index, child) in children.iter().enumerate().take(members) {
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

fn expanding_union_cycle(
    schema: &serde_yaml_ng::Value,
    root: &serde_yaml_ng::Value,
    extends: bool,
    expansions: usize,
    active: &mut std::collections::HashMap<String, usize>,
) -> bool {
    if ignored_reference_node(schema) {
        return false;
    }
    if let Some(reference) = schema.get("$ref").and_then(serde_yaml_ng::Value::as_str) {
        let Some(pointer) = reference.strip_prefix('#') else {
            return false;
        };
        let Some(target) = yaml_pointer(root, pointer) else {
            return false;
        };
        let partial = reference
            .strip_prefix("#/components/schemas/")
            .is_some_and(|suffix| suffix.split('/').count() > 1);
        let union_base = extends
            && ["oneOf", "anyOf"].iter().any(|key| {
                target
                    .get(key)
                    .and_then(serde_yaml_ng::Value::as_sequence)
                    .is_some_and(|variants| variants.len() > 1)
            })
            && !schema_is_model(target, root, &mut Vec::new());
        let expansions = expansions + usize::from(partial || union_base);
        if let Some(previous) = active.get(reference) {
            return expansions > *previous;
        }
        active.insert(reference.to_owned(), expansions);
        let cycle = expanding_union_cycle(target, root, false, expansions, active);
        active.remove(reference);
        return cycle;
    }
    if let Some(properties) = schema
        .get("properties")
        .and_then(serde_yaml_ng::Value::as_mapping)
    {
        if properties
            .values()
            .any(|property| expanding_union_cycle(property, root, false, expansions, active))
        {
            return true;
        }
    }
    for key in ["items", "additionalProperties"] {
        if let Some(child) = schema.get(key) {
            if expanding_union_cycle(child, root, false, expansions, active) {
                return true;
            }
        }
    }
    for key in ["allOf", "oneOf", "anyOf"] {
        if let Some(children) = schema.get(key).and_then(serde_yaml_ng::Value::as_sequence) {
            if children
                .iter()
                .any(|child| expanding_union_cycle(child, root, key == "allOf", expansions, active))
            {
                return true;
            }
        }
    }
    false
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
    if ["oneOf", "anyOf"].iter().any(|key| {
        schema
            .get(key)
            .and_then(serde_yaml_ng::Value::as_sequence)
            .is_some_and(|variants| variants.len() > 1)
    }) && expanding_union_cycle(
        schema,
        context.root,
        false,
        0,
        &mut std::collections::HashMap::new(),
    ) {
        return refusal(context.path, context.strict, Class::HeapExhausted, element);
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
    if let Some(default) = schema.get("default").and_then(serde_yaml_ng::Value::as_str) {
        let query_array = matches!(location, SchemaLocation::Query)
            && schema.get("type").and_then(serde_yaml_ng::Value::as_str) == Some("array");
        let candidate = if query_array {
            schema.get("items").unwrap_or(schema)
        } else {
            schema
        };
        if let Some(values) = candidate
            .get("enum")
            .and_then(serde_yaml_ng::Value::as_sequence)
        {
            // Fern ignores scalar defaults outside the declared enum. Query
            // arrays become an enum-or-list union and validate their scalar default.
            let declared = values.iter().any(|value| value.as_str() == Some(default));
            if !values.is_empty()
                && values.iter().all(|value| value.as_str().is_some())
                && ((query_array && !declared)
                    || (declared && !retained_enum_default(candidate, default, context.path)?))
            {
                return refusal(
                    context.path,
                    context.strict,
                    Class::DefaultNotEnumValue,
                    &format!("{element} default {default:?}"),
                );
            }
        }
    }
    // Fern renders a string enum with no non-null member as an enum class whose
    // `visit` method has no body, which its own `ruff check` cannot parse.
    if schema.get("type").and_then(serde_yaml_ng::Value::as_str) == Some("string")
        && schema
            .get("enum")
            .and_then(serde_yaml_ng::Value::as_sequence)
            .is_some_and(|values| values.iter().all(serde_yaml_ng::Value::is_null))
    {
        return refusal(
            context.path,
            context.strict,
            Class::GeneratorLintFailure,
            &format!("{element} enum has no non-null value"),
        );
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

/// Whether the IR's own enum builder keeps the member a declared default
/// names. It reads the schema as pinned Fern does: `x-crozier-*` extensions,
/// which Fern ignores, are dropped first, so a canonical extension never makes
/// a document Fern accepts into a refusal.
fn retained_enum_default(
    schema: &serde_yaml_ng::Value,
    default: &str,
    path: &Path,
) -> Result<bool> {
    let mut schema = schema.clone();
    if let Some(mapping) = schema.as_mapping_mut() {
        mapping.retain(|key, _| {
            !key.as_str()
                .is_some_and(|key| key.starts_with("x-crozier-"))
        });
        mapping.insert("type".into(), "string".into());
    }
    let mut schemas = serde_yaml_ng::Mapping::new();
    schemas.insert("EnumDefaultProbe".into(), schema);
    let mut components = serde_yaml_ng::Mapping::new();
    components.insert("schemas".into(), schemas.into());
    let mut document = serde_yaml_ng::Mapping::new();
    document.insert("openapi".into(), "3.0.3".into());
    document.insert("components".into(), components.into());
    let Ok(doc) = serde_yaml_ng::from_value::<OpenApi>(document.into()) else {
        return Ok(true);
    };
    let config = crate::config::GenerateConfig::new(
        path.to_path_buf(),
        Default::default(),
        Some("enum_probe".into()),
        None,
        None,
        crate::settings::ExtraFields::default(),
        "Enum probe",
    )?;
    Ok(crate::ir::build(&doc, &config)
        .types
        .iter()
        .any(|declaration| {
            matches!(declaration, crate::ir::TypeDecl::Enum(enum_type)
            if enum_type.members.iter().any(|member| member.value == default))
        }))
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
    for (route, item) in &doc.paths {
        if let Some(operation) = &item.head {
            if !operation.ignored() && operation.request_body.is_some() {
                return refusal(
                    path,
                    strict,
                    Class::HeadRequestBody,
                    &format!("HEAD {route}"),
                );
            }
        }
    }
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

/// Reject an SDK whose generated Python pinned Fern's own `ruff check` rejects
/// (`generator-lint-failure`). crozier's IR names clients, methods, union
/// variants, fields and server variables as Fern does, so each shape is read
/// from it; operation naming is read without the `x-crozier-*` overrides Fern
/// never sees.
pub fn check_sdk(
    doc: &mut OpenApi,
    ir: &crate::ir::Ir,
    config: &crate::config::GenerateConfig,
    path: &Path,
    strict: bool,
) -> Result<()> {
    let fern_ir = fern_naming_ir(doc, config);
    let ir = fern_ir.as_ref().unwrap_or(ir);
    if let Some(element) = promoted_optional_array_header(doc, ir) {
        return refusal(path, strict, Class::ExampleTypeMismatch, &element);
    }
    let class = Class::GeneratorLintFailure;
    for decl in ir
        .types
        .iter()
        .chain(ir.tag_types.iter().map(|tagged| &tagged.decl))
    {
        let fields: Vec<&crate::ir::Field> = match decl {
            crate::ir::TypeDecl::Object(object) => object.fields.iter().collect(),
            crate::ir::TypeDecl::DiscriminatedUnion(union) => {
                // F811: two discriminant values that name one wrapper class.
                for (index, member) in union.members.iter().enumerate() {
                    if let Some(earlier) = union.members[..index].iter().find(|earlier| {
                        earlier.class_name == member.class_name
                            && earlier.discriminant != member.discriminant
                    }) {
                        return refusal(
                            path,
                            strict,
                            class,
                            &format!(
                                "type {} variants {:?} and {:?} are both {}",
                                union.name,
                                earlier.discriminant,
                                member.discriminant,
                                member.class_name
                            ),
                        );
                    }
                }
                union
                    .base_fields
                    .iter()
                    .chain(union.members.iter().flat_map(|member| &member.fields))
                    .collect()
            }
            crate::ir::TypeDecl::Alias(_) | crate::ir::TypeDecl::Enum(_) => Vec::new(),
        };
        // A syntax error: a property whose Python name is empty (`/`).
        if let Some(field) = fields.iter().find(|field| field.py_name.is_empty()) {
            return refusal(
                path,
                strict,
                class,
                &format!("type {} property {:?}", decl.name(), field.wire_name),
            );
        }
    }
    for endpoint in ir.endpoints.iter().filter(|endpoint| endpoint.emittable) {
        let route = format!("{} {}", endpoint.http_method, endpoint.path);
        // F811: a root-client method and a sub-client property of one name.
        if endpoint.module.is_empty()
            && ir.endpoint_modules.iter().any(|module| {
                module.split('/').next() == Some(endpoint.method_name.as_str())
                    && !(ir.empty_endpoint_namespace && module == "_")
            })
        {
            return refusal(
                path,
                strict,
                class,
                &format!(
                    "{route} root method and sub-client {}",
                    endpoint.method_name
                ),
            );
        }
        // A syntax error: a method with no name. Fern empties one named from a
        // summary with no ASCII word. An operationId that only repeats its tag
        // is hoisted to the root by the IR, so the collision check above names
        // it; a name still left empty refuses only beside another operation of
        // its sub-client.
        if endpoint.method_name.is_empty() {
            let named_by_summary = doc
                .paths
                .get(&endpoint.path)
                .and_then(|item| {
                    item.operations()
                        .into_iter()
                        .find(|(method, _)| *method == endpoint.http_method)
                })
                .is_some_and(|(_, op)| op.operation_id.is_none() && op.sdk_method_name().is_none());
            let shares_sub_client = ir
                .endpoints
                .iter()
                .filter(|other| other.module == endpoint.module)
                .count()
                > 1;
            if named_by_summary || shares_sub_client {
                return refusal(
                    path,
                    strict,
                    class,
                    &format!("{route} method name is empty"),
                );
            }
        }
    }
    if let Some(environment) = &ir.environment {
        let template = &environment.url_template;
        let variables = &environment.variables;
        // A syntax error: `str.format` keyword arguments are the variable names.
        if let Some(variable) = variables
            .iter()
            .find(|variable| !python_identifier(&variable.wire_name))
        {
            return refusal(
                path,
                strict,
                class,
                &format!("server {template} variable {:?}", variable.wire_name),
            );
        }
        // F524: a placeholder `str.format` is given no argument for.
        if !variables.is_empty() {
            let mut rest = template.as_str();
            while let Some((_, after)) = rest.split_once('{') {
                let Some((placeholder, after)) = after.split_once('}') else {
                    break;
                };
                if !variables
                    .iter()
                    .any(|variable| variable.wire_name == placeholder)
                {
                    return refusal(
                        path,
                        strict,
                        class,
                        &format!("server {template} placeholder {placeholder:?}"),
                    );
                }
                rest = after;
            }
        }
    }
    Ok(())
}

/// The IR for the document as pinned Fern names its operations, or `None`
/// when no operation carries an `x-crozier-*` naming override (the emitted IR
/// already is that view). The overrides are restored before returning.
fn fern_naming_ir(
    doc: &mut OpenApi,
    config: &crate::config::GenerateConfig,
) -> Option<crate::ir::Ir> {
    let mut taken = Vec::new();
    for (item_index, item) in doc.paths.values_mut().enumerate() {
        for (slot_index, slot) in item.operation_slots().into_iter().enumerate() {
            if let Some(naming) = slot
                .as_mut()
                .and_then(crate::openapi::Operation::take_crozier_naming)
            {
                taken.push((item_index, slot_index, naming));
            }
        }
    }
    if taken.is_empty() {
        return None;
    }
    let ir = crate::ir::build(doc, config);
    for (item_index, slot_index, naming) in taken {
        if let Some((_, item)) = doc.paths.get_index_mut(item_index) {
            if let Some(op) = item.operation_slots()[slot_index].as_mut() {
                op.restore_crozier_naming(naming);
            }
        }
    }
    Some(ir)
}

/// Whether `name` can be a Python keyword argument: an identifier that is not
/// a keyword.
fn python_identifier(name: &str) -> bool {
    const KEYWORDS: [&str; 35] = [
        "False", "None", "True", "and", "as", "assert", "async", "await", "break", "class",
        "continue", "def", "del", "elif", "else", "except", "finally", "for", "from", "global",
        "if", "import", "in", "is", "lambda", "nonlocal", "not", "or", "pass", "raise", "return",
        "try", "while", "with", "yield",
    ];
    let mut chars = name.chars();
    chars
        .next()
        .is_some_and(|first| first == '_' || first.is_alphabetic())
        && chars.all(|c| c == '_' || c.is_alphanumeric())
        && !KEYWORDS.contains(&name)
}

const OPERATION_METHODS: [&str; 8] = [
    "get", "put", "post", "delete", "options", "head", "patch", "trace",
];

/// Every operation Fern imports, with its method and route. Pinned Fern skips
/// an ignored Path Item or operation before it reads the operation's examples.
fn imported_operations(
    root: &serde_yaml_ng::Value,
) -> impl Iterator<Item = (&'static str, &str, &serde_yaml_ng::Value)> {
    root.get("paths")
        .and_then(serde_yaml_ng::Value::as_mapping)
        .into_iter()
        .flatten()
        .filter(|(_, item)| !ignored_reference_node(item))
        .filter_map(|(route, item)| Some((route.as_str()?, item)))
        .flat_map(|(route, item)| {
            OPERATION_METHODS.iter().filter_map(move |method| {
                let operation = item.get(*method)?;
                (operation.is_mapping() && !ignored_reference_node(operation))
                    .then_some((*method, route, operation))
            })
        })
}

/// A node with its local `$ref` chain followed; `None` for a reference that
/// cannot be followed here (other classes own those).
fn local_target<'a>(
    root: &'a serde_yaml_ng::Value,
    mut node: &'a serde_yaml_ng::Value,
) -> Option<&'a serde_yaml_ng::Value> {
    for _ in 0..32 {
        let Some(reference) = node.get("$ref").and_then(serde_yaml_ng::Value::as_str) else {
            return Some(node);
        };
        node = yaml_pointer(root, reference.strip_prefix('#')?)?;
    }
    None
}

/// A media type whose examples pinned Fern reads as JSON: a case-sensitive
/// `json` anywhere in the key (`text/json`, `application/problem+json`,
/// `application/x-ndjson`) or the `*/*` wildcard, the first in document order.
/// `Application/JSON` is not one.
fn json_examples_media(media_type: &str) -> bool {
    media_type == "*/*" || media_type.contains("json")
}

/// The request examples Fern names: the first JSON media type's, else a form
/// body's. Multipart, XML, text and binary examples are never read.
fn request_examples<'a>(
    root: &'a serde_yaml_ng::Value,
    operation: &'a serde_yaml_ng::Value,
) -> Option<&'a serde_yaml_ng::Value> {
    let content = local_target(root, operation.get("requestBody")?)?
        .get("content")?
        .as_mapping()?;
    content
        .iter()
        .find(|(media_type, _)| media_type.as_str().is_some_and(json_examples_media))
        .map(|(_, media)| media)
        .or_else(|| content.get("application/x-www-form-urlencoded"))?
        .get("examples")
}

/// The response examples Fern names. Its success response is the lowest
/// numeric 2xx code (`default` only when the operation declares none): a `204`
/// ends the search, a response with no content or only `application/xml`
/// passes it to the next code, and a JSON media type's examples are read. Any
/// other content (text, HTML, PDF, binary) ends the search unread.
fn response_examples<'a>(
    root: &'a serde_yaml_ng::Value,
    operation: &'a serde_yaml_ng::Value,
) -> Option<&'a serde_yaml_ng::Value> {
    let responses = operation.get("responses")?.as_mapping()?;
    let mut candidates: Vec<(u64, &serde_yaml_ng::Value)> = responses
        .iter()
        .filter_map(|(code, response)| {
            let code = code
                .as_u64()
                .or_else(|| code.as_str().and_then(|code| code.parse().ok()))?;
            (200..300).contains(&code).then_some((code, response))
        })
        .collect();
    candidates.sort_by_key(|(code, _)| *code);
    if candidates.is_empty() {
        // Code 0 stands for `default`, which never passes the search on.
        candidates.extend(responses.get("default").map(|response| (0, response)));
    }
    for (code, response) in candidates {
        if code == 204 {
            return None;
        }
        let content = local_target(root, response)?
            .get("content")
            .and_then(serde_yaml_ng::Value::as_mapping)
            .filter(|content| !content.is_empty());
        let Some(content) = content else {
            if code == 0 {
                return None;
            }
            continue;
        };
        if let Some((_, media)) = content
            .iter()
            .find(|(media_type, _)| media_type.as_str().is_some_and(json_examples_media))
        {
            return media.get("examples");
        }
        if code == 0
            || !content
                .keys()
                .all(|media_type| media_type.as_str() == Some("application/xml"))
        {
            return None;
        }
    }
    None
}

/// A named example's name as Fern compares it: the referenced Example Object's
/// `summary` when it has a non-null one (an empty string included, compared
/// with its YAML type, so `1` and `"1"` differ), else the map key as a string.
/// A `summary` beside a `$ref` is not read.
fn example_name(
    root: &serde_yaml_ng::Value,
    key: &serde_yaml_ng::Value,
    example: &serde_yaml_ng::Value,
) -> Option<serde_yaml_ng::Value> {
    if let Some(summary) = local_target(root, example)?
        .get("summary")
        .filter(|summary| !summary.is_null())
    {
        return Some(summary.clone());
    }
    let key = match key {
        serde_yaml_ng::Value::String(key) => key.clone(),
        serde_yaml_ng::Value::Number(key) => key.to_string(),
        serde_yaml_ng::Value::Bool(key) => key.to_string(),
        _ => return None,
    };
    Some(serde_yaml_ng::Value::String(key))
}

fn name_label(name: &serde_yaml_ng::Value) -> String {
    name.as_str().map_or_else(
        || {
            serde_yaml_ng::to_string(name)
                .unwrap_or_default()
                .trim_end()
                .to_owned()
        },
        str::to_owned,
    )
}

fn first_duplicate(
    names: impl IntoIterator<Item = serde_yaml_ng::Value>,
) -> Option<serde_yaml_ng::Value> {
    let mut seen = Vec::new();
    for name in names {
        if seen.contains(&name) {
            return Some(name);
        }
        seen.push(name);
    }
    None
}

/// Pinned Fern names each endpoint example and refuses two of one name. A
/// non-empty `x-fern-examples` list replaces the OpenAPI examples, so only its
/// `name`s are compared; otherwise the request examples and the success
/// response examples are each compared within themselves, never with each
/// other or across operations. `x-crozier-examples` is not read: Fern never
/// reads it, so its content cannot make Fern refuse a document.
fn check_example_names(root: &serde_yaml_ng::Value, path: &Path, strict: bool) -> Result<()> {
    for (method, route, operation) in imported_operations(root) {
        let element = format!("{} {route}", method.to_ascii_uppercase());
        if let Some(examples) = operation.get("x-fern-examples") {
            let Some(examples) = examples.as_sequence() else {
                continue;
            };
            if !examples.is_empty() {
                let names = examples
                    .iter()
                    .filter_map(|example| example.get("name"))
                    .filter(|name| !name.is_null())
                    .cloned();
                if let Some(name) = first_duplicate(names) {
                    let element = format!("{element} x-fern-examples name {}", name_label(&name));
                    return refusal(path, strict, Class::DuplicateExampleName, &element);
                }
                continue;
            }
        }
        for (side, examples) in [
            ("request", request_examples(root, operation)),
            ("response", response_examples(root, operation)),
        ] {
            let Some(examples) = examples.and_then(serde_yaml_ng::Value::as_mapping) else {
                continue;
            };
            let names = examples
                .iter()
                .filter_map(|(key, example)| example_name(root, key, example));
            if let Some(name) = first_duplicate(names) {
                let element = format!("{element} {side} example name {}", name_label(&name));
                return refusal(path, strict, Class::DuplicateExampleName, &element);
            }
        }
    }
    Ok(())
}

/// The operation's query parameters as Fern imports them: Path Item
/// parameters overridden by the operation's own of the same name, references
/// followed, ignored parameters dropped.
fn query_parameters<'a>(
    root: &'a serde_yaml_ng::Value,
    item: &'a serde_yaml_ng::Value,
    operation: &'a serde_yaml_ng::Value,
) -> Vec<(&'a str, &'a serde_yaml_ng::Value)> {
    let mut parameters: Vec<(&str, &serde_yaml_ng::Value)> = Vec::new();
    for parameter in [item, operation]
        .into_iter()
        .filter_map(|node| node.get("parameters")?.as_sequence())
        .flatten()
    {
        let Some(parameter) = local_target(root, parameter) else {
            continue;
        };
        if parameter.get("in").and_then(serde_yaml_ng::Value::as_str) != Some("query") {
            continue;
        }
        let Some(name) = parameter.get("name").and_then(serde_yaml_ng::Value::as_str) else {
            continue;
        };
        parameters.retain(|(declared, _)| *declared != name);
        if !ignored_reference_node(parameter) {
            parameters.push((name, parameter));
        }
    }
    parameters
}

/// A parameter's schema, from `schema` or its first `content` media type.
fn parameter_schema(parameter: &serde_yaml_ng::Value) -> Option<&serde_yaml_ng::Value> {
    parameter.get("schema").or_else(|| {
        parameter
            .get("content")?
            .as_mapping()?
            .values()
            .next()?
            .get("schema")
    })
}

/// Whether a schema is `nullable` or a list, the shapes an example may omit —
/// or cannot be followed, which is never refused.
fn omittable_schema(root: &serde_yaml_ng::Value, schema: Option<&serde_yaml_ng::Value>) -> bool {
    let Some(schema) = schema else {
        return false;
    };
    let Some(schema) = local_target(root, schema) else {
        return true;
    };
    let type_is = |name: &str| match schema.get("type") {
        Some(serde_yaml_ng::Value::String(value)) => value == name,
        Some(serde_yaml_ng::Value::Sequence(values)) => {
            values.iter().any(|value| value.as_str() == Some(name))
        }
        _ => false,
    };
    schema
        .get("nullable")
        .and_then(serde_yaml_ng::Value::as_bool)
        == Some(true)
        || type_is("null")
        || type_is("array")
}

/// Pinned Fern checks every endpoint example against the endpoint's required
/// query parameters. An `x-fern-examples` entry is checked when it declares
/// `query-parameters` as a map, or declares a `response` without them; the
/// key is the wire name, case-sensitive, and a `null` value is missing. A
/// `nullable` or list parameter may be omitted; a default does not excuse
/// one. `x-crozier-examples` is not read.
///
/// Fern also reports this for an optional named-type query parameter of an
/// operation it files into `api.yml`; that is the `type-not-defined` mechanism,
/// whose detector refuses it first.
fn check_example_query_parameters(
    root: &serde_yaml_ng::Value,
    path: &Path,
    strict: bool,
) -> Result<()> {
    for (method, route, operation) in imported_operations(root) {
        let element = format!("{} {route}", method.to_ascii_uppercase());
        let Some(item) = root.get("paths").and_then(|paths| paths.get(route)) else {
            continue;
        };
        let parameters = query_parameters(root, item, operation);
        let examples = operation
            .get("x-fern-examples")
            .and_then(serde_yaml_ng::Value::as_sequence)
            .filter(|examples| !examples.is_empty());
        if let Some(examples) = examples {
            for (index, example) in examples.iter().enumerate() {
                let given = match example.get("query-parameters") {
                    Some(serde_yaml_ng::Value::Mapping(given)) => given.clone(),
                    None if example.get("response").is_some() => serde_yaml_ng::Mapping::new(),
                    _ => continue,
                };
                let missing = parameters.iter().find(|(name, parameter)| {
                    parameter
                        .get("required")
                        .and_then(serde_yaml_ng::Value::as_bool)
                        == Some(true)
                        && !omittable_schema(root, parameter_schema(parameter))
                        && given.get(*name).is_none_or(serde_yaml_ng::Value::is_null)
                });
                if let Some((name, _)) = missing {
                    let element =
                        format!("{element} x-fern-examples/{index} query parameter {name}");
                    return refusal(
                        path,
                        strict,
                        Class::ExampleMissingRequiredQueryParameter,
                        &element,
                    );
                }
            }
        }
    }
    Ok(())
}

/// An optional array header Fern promotes to a client field
/// (`example-type-mismatch`): its check fills the field's example with the
/// header's name and rejects that string as no list. A required one, one left on
/// a subset of operations as a method argument, and one whose string `default`
/// makes Fern type it `str` each generate, as
/// `docs/fern-refusals/example-type-mismatch/evaluation.md` records. The promotion
/// is read from the SDK IR, so it is decided by the one rule that emits it.
fn promoted_optional_array_header(doc: &OpenApi, ir: &crate::ir::Ir) -> Option<String> {
    let header = ir.global_headers.iter().find(
        |header| matches!(header.presence, crate::ir::HeaderPresence::Optional(ty) if ty.is_list()),
    )?;
    let (route, method) = doc.paths.iter().find_map(|(route, item)| {
        item.operations().into_iter().find_map(|(method, op)| {
            op.parameters
                .iter()
                .any(|parameter| {
                    parameter.location == Some(ParameterLocation::Header)
                        && parameter.name == header.wire_name
                })
                .then_some((route, method))
        })
    })?;
    Some(format!("{method} {route} header {}", header.wire_name))
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

    /// The header element `promoted_optional_array_header` reports for a
    /// document whose every operation carries `header`, or `None`.
    fn promoted_array_refusal(operations: usize, header: &str) -> Option<String> {
        let mut spec = String::from("openapi: 3.0.3\ninfo: {title: Api, version: '1'}\npaths:\n");
        for index in 0..operations {
            spec.push_str(&format!(
                "  /p{index}:\n    get:\n      parameters: [{header}]\n      responses: {{'204': {{description: OK}}}}\n"
            ));
        }
        let doc: OpenApi = serde_yaml_ng::from_str(&spec).unwrap();
        let config = crate::config::GenerateConfig::new(
            std::path::PathBuf::from("openapi.yml"),
            std::path::PathBuf::from("out"),
            Some("api".to_string()),
            None,
            None,
            crate::settings::ExtraFields::default(),
            "Api",
        )
        .unwrap();
        promoted_optional_array_header(&doc, &crate::ir::build(&doc, &config))
    }

    #[test]
    fn only_an_optional_promoted_array_header_without_a_string_default_is_refused() {
        let optional = "{name: X-Things, in: header, schema: {type: array, items: {type: string}}}";
        assert_eq!(
            promoted_array_refusal(2, optional).as_deref(),
            Some("GET /p0 header X-Things")
        );
        assert_eq!(
            promoted_array_refusal(1, "{name: X-Things, in: header, schema: {type: array, items: {type: integer}, default: [1]}}")
                .as_deref(),
            Some("GET /p0 header X-Things")
        );
        for generated in [
            "{name: X-Things, in: header, required: true, schema: {type: array, items: {type: string}}}",
            "{name: X-Things, in: header, schema: {type: array, items: {type: string}, default: all}}",
            "{name: X-Things, in: header, schema: {type: string}}",
        ] {
            assert_eq!(promoted_array_refusal(1, generated), None, "{generated}");
        }
        let dir = tempfile::tempdir().unwrap();
        let spec = dir.path().join("api.yml");
        let error = refusal(
            &spec,
            true,
            Class::ExampleTypeMismatch,
            "GET /p0 header X-Things",
        )
        .unwrap_err()
        .to_string();
        assert!(
            error.contains("example-type-mismatch: GET /p0 header X-Things (fern-strict refusal)")
        );
    }

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
    fn a_required_properties_pointer_is_walked_rather_than_refused() {
        let dir = tempfile::tempdir().unwrap();
        let file = dir.path().join("api.yml");
        let probe = |reference: &str| {
            format!(
                concat!(
                    "openapi: 3.0.3\npaths: {{/holder: {{post: {{requestBody: {{content: {{application/json: ",
                    "{{schema: {{type: object, required: [ghost], properties: {{ghost: {{$ref: '{reference}'}}}}}}}}}}}}, ",
                    "responses: {{'204': {{description: No Content}}}}}}}}}}\ncomponents: {{schemas: {{Named: {{type: object, ",
                    "$defs: {{id: {{type: string}}}}, properties: {{label: {{type: string, $defs: {{inner: {{type: string}}}}}}}}}}}}}}\n",
                ),
                reference = reference,
            )
        };
        // Pinned Fern walks a pointer naming `properties`, typing what it does
        // not reach as unknown, so these generate.
        for walked in [
            "#/components/schemas/Named/properties/absent",
            "#/components/schemas/Missing/properties/absent",
            "#/components/schemas/Named/properties/label/$defs/inner",
        ] {
            std::fs::write(&file, probe(walked)).unwrap();
            check_structure_file(&file, true).unwrap_or_else(|error| panic!("{walked}: {error}"));
        }
        // One without the word is resolved, and fails required.
        for refused in [
            "#/components/schemas/Named/items",
            "#/components/schemas/Named/$defs/id",
            "#/components/schemas/Missing",
        ] {
            std::fs::write(&file, probe(refused)).unwrap();
            let error = check_structure_file(&file, false).unwrap_err().to_string();
            assert!(
                error.contains(&format!("unresolved-schema-reference: paths//holder/post/requestBody/content/application/json/schema/properties/ghost reference {refused}")),
                "{error}"
            );
        }
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

    #[test]
    fn server_variables_must_be_python_keyword_arguments() {
        for name in ["apiVersion", "api_version", "_v", "région"] {
            assert!(python_identifier(name), "{name}");
        }
        for name in ["", "api-version", "api.version", "1st", "class", "None"] {
            assert!(!python_identifier(name), "{name}");
        }
    }

    fn example_name_refusal(document: &str) -> Option<String> {
        let root: serde_yaml_ng::Value = serde_yaml_ng::from_str(document).unwrap();
        check_example_names(&root, Path::new("api.yml"), false)
            .err()
            .map(|error| error.to_string())
    }

    #[test]
    fn duplicate_example_names_follow_the_examples_fern_reads() {
        let same = "{a: {summary: Same, value: {}}, b: {summary: Same, value: {}}}";
        let refused = |document: String, element: &str| {
            let error = example_name_refusal(&document).unwrap_or_else(|| panic!("{document}"));
            assert!(
                error.contains(&format!("duplicate-example-name: {element}")),
                "{error}"
            );
        };
        let accepted = |document: String| assert_eq!(example_name_refusal(&document), None);
        let body = |content: &str| {
            format!("paths: {{/p: {{post: {{requestBody: {{content: {content}}}, responses: {{'204': {{description: x}}}}}}}}}}")
        };
        let responses =
            |responses: &str| format!("paths: {{/p: {{get: {{responses: {responses}}}}}}}");
        refused(
            body(&format!("{{application/json: {{examples: {same}}}}}")),
            "POST /p request example name Same",
        );
        // The first JSON media type, in document order, else a form body.
        refused(
            body(&format!(
                "{{text/json: {{examples: {same}}}, application/json: {{}}}}"
            )),
            "POST /p request",
        );
        refused(
            body(&format!(
                "{{application/x-www-form-urlencoded: {{examples: {same}}}}}"
            )),
            "POST /p request",
        );
        accepted(body(&format!(
            "{{application/json: {{}}, '*/*': {{examples: {same}}}}}"
        )));
        accepted(body(&format!(
            "{{multipart/form-data: {{examples: {same}}}}}"
        )));
        accepted(body(&format!("{{Application/JSON: {{examples: {same}}}}}")));
        accepted(body(&format!(
            "{{application/x-www-form-urlencoded: {{examples: {same}}}, application/json: {{}}}}"
        )));
        // The lowest 2xx code with content; `default` only without one.
        let json =
            format!("{{description: x, content: {{application/json: {{examples: {same}}}}}}}");
        refused(
            responses(&format!(
                "{{'202': {{description: x, content: {{application/json: {{}}}}}}, '201': {json}}}"
            )),
            "GET /p response example name Same",
        );
        refused(
            responses(&format!("{{'200': {{description: x}}, '201': {json}}}")),
            "GET /p response",
        );
        refused(
            responses(&format!(
                "{{'200': {{description: x, content: {{application/xml: {{}}}}}}, '201': {json}}}"
            )),
            "GET /p response",
        );
        refused(
            responses(&format!("{{'400': {{description: x}}, default: {json}}}")),
            "GET /p response",
        );
        accepted(responses(&format!(
            "{{'204': {{description: x}}, '206': {json}}}"
        )));
        accepted(responses(&format!(
            "{{'201': {{description: x}}, default: {json}}}"
        )));
        accepted(responses(&format!(
            "{{'200': {{description: x, content: {{text/plain: {{}}}}}}, '201': {json}}}"
        )));
        accepted(responses(&format!("{{'400': {json}}}")));
        accepted(responses(&format!("{{'2XX': {json}}}")));
        // Names: a referenced summary, else the key; typed, null-skipping.
        let examples = |examples: &str| {
            format!("paths: {{/p: {{get: {{responses: {{'200': {{description: x, content: {{application/json: {{examples: {examples}}}}}}}}}}}}}}}\ncomponents: {{examples: {{E: {{summary: Same}}, K: {{value: 1}}}}}}")
        };
        refused(examples("{a: {$ref: '#/components/examples/E'}, b: {$ref: '#/components/examples/E', summary: Other}}"), "GET /p response example name Same");
        refused(
            examples("{a: {summary: b}, b: {value: 1}}"),
            "GET /p response example name b",
        );
        refused(
            examples("{a: {summary: ''}, b: {summary: ''}}"),
            "GET /p response example name ",
        );
        refused(
            examples("{a: {summary: 1}, b: {summary: 1}}"),
            "GET /p response example name 1",
        );
        accepted(examples("{a: {summary: 1}, b: {summary: '1'}}"));
        accepted(examples("{a: {summary: null}, b: {summary: null}}"));
        accepted(examples(
            "{a: {$ref: '#/components/examples/K'}, b: {$ref: '#/components/examples/K'}}",
        ));
        accepted(examples("{a: {summary: Same}, b: {summary: same}}"));
        // A non-empty x-fern-examples list replaces the OpenAPI examples.
        let fern = |list: &str, extension: &str| {
            format!("paths: {{/p: {{post: {{{extension}: {list}, requestBody: {{content: {{application/json: {{examples: {same}}}}}}}, responses: {{'204': {{description: x}}}}}}}}}}")
        };
        refused(
            fern("[{name: X}, {name: X}]", "x-fern-examples"),
            "POST /p x-fern-examples name X",
        );
        refused(
            fern("[]", "x-fern-examples"),
            "POST /p request example name Same",
        );
        accepted(fern("[{name: X}]", "x-fern-examples"));
        accepted(fern("[{request: {}}, {request: {}}]", "x-fern-examples"));
        // Fern never reads x-crozier-examples: its names cannot refuse, and
        // it does not replace the OpenAPI examples.
        accepted(
            "paths: {/p: {post: {x-crozier-examples: [{name: X}, {name: X}], responses: {}}}}"
                .to_owned(),
        );
        refused(
            fern("[{name: X}]", "x-crozier-examples"),
            "POST /p request example name Same",
        );
        // Ignored operations and Path Items are not imported; webhooks are not read.
        accepted(format!(
            "paths: {{/p: {{x-fern-ignore: true, get: {{responses: {{'200': {json}}}}}}}}}"
        ));
        accepted(format!(
            "paths: {{/p: {{get: {{x-fern-ignore: true, responses: {{'200': {json}}}}}}}}}"
        ));
        accepted(format!(
            "webhooks: {{h: {{post: {{responses: {{'200': {json}}}}}}}}}"
        ));
        accepted(format!("components: {{responses: {{R: {json}}}}}"));
    }

    #[test]
    fn example_query_parameters_follow_the_examples_fern_checks() {
        let check = |document: String| {
            let root: serde_yaml_ng::Value = serde_yaml_ng::from_str(&document).unwrap();
            check_example_query_parameters(&root, Path::new("api.yml"), true)
                .err()
                .map(|error| error.to_string())
        };
        let refused = |document: String, element: &str| {
            let error = check(document.clone()).unwrap_or_else(|| panic!("{document}"));
            assert!(
                error.contains("example-missing-required-query-parameter: GET /c ")
                    && error.contains(&format!("{element} (fern-strict refusal)")),
                "{error}"
            );
        };
        let accepted = |document: String| assert_eq!(check(document), None);
        let op = |parameter: &str, examples: &str| {
            format!("paths: {{/c: {{get: {{parameters: [{parameter}], x-fern-examples: {examples}, responses: {{}}}}}}}}")
        };
        let required = "{name: f, in: query, required: true, schema: {type: string}}";
        refused(
            op(required, "[{query-parameters: {}}]"),
            "GET /c x-fern-examples/0 query parameter f",
        );
        refused(
            op(
                required,
                "[{query-parameters: {f: x}}, {query-parameters: {f: null}}]",
            ),
            "GET /c x-fern-examples/1 query parameter f",
        );
        refused(
            op(required, "[{query-parameters: {F: x}}]"),
            "query parameter f",
        );
        refused(
            op(required, "[{response: {body: {}}}]"),
            "query parameter f",
        );
        refused(
            op(
                "{name: f, in: query, required: true, schema: {type: string, default: x}}",
                "[{query-parameters: {}}]",
            ),
            "query parameter f",
        );
        refused(
            format!(
                "{}\ncomponents: {{parameters: {{F: {required}}}}}",
                op(
                    "{$ref: '#/components/parameters/F'}",
                    "[{query-parameters: {}}]"
                )
            ),
            "query parameter f",
        );
        accepted(op(required, "[{query-parameters: {f: x}}]"));
        accepted(op(required, "[{name: only}]"));
        accepted(op(required, "[{query-parameters: null}]"));
        accepted(op(required, "[]"));
        accepted(op(
            "{name: f, in: query, required: false, schema: {type: string}}",
            "[{query-parameters: {}}]",
        ));
        for schema in [
            "{type: string, nullable: true}",
            "{type: [string, 'null']}",
            "{type: array, items: {type: string}}",
            "{$ref: '#/components/schemas/Absent'}",
        ] {
            accepted(op(
                &format!("{{name: f, in: query, required: true, schema: {schema}}}"),
                "[{query-parameters: {}}]",
            ));
        }
        accepted(op(
            "{name: f, in: query, required: true, x-fern-ignore: true}",
            "[{query-parameters: {}}]",
        ));
        accepted(
            "paths: {/c: {get: {parameters: [{name: f, in: query, required: true}], x-crozier-examples: [{query-parameters: {}}]}}}"
                .to_owned(),
        );
        accepted(
            "paths: {/c: {parameters: [{name: f, in: query, required: true}], get: {parameters: [{name: f, in: query}], x-fern-examples: [{query-parameters: {}}]}}}"
                .to_owned(),
        );
        refused(
            "paths: {/c: {parameters: [{name: f, in: query, required: true}], get: {x-fern-examples: [{query-parameters: {}}]}}}"
                .to_owned(),
            "query parameter f",
        );
    }
}
