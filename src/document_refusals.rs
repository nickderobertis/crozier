//! Structural refusals for the document-family Fern registry.
//!
//! These checks decide whether generation is allowed; they never rewrite the
//! document or repair the output measured in `docs/fern-refusals/`.

use std::path::Path;

use crate::openapi::{
    document_boolean, HttpAuthScheme, OpenApi, ParameterLocation, SecurityScheme,
    SecuritySchemeType,
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
    GeneratedFileNameTooLong,
    DefaultNotEnumValue,
    GeneratorLintFailure,
    TypeNotDefined,
    MissingDiscriminantProperty,
    DuplicateExampleName,
    ExampleSummaryNotString,
    ExampleMissingRequiredQueryParameter,
    ExampleTypeMismatch,
    ExampleNotEnumValue,
    ExampleUnexpectedProperty,
    ExampleMissingRequiredProperty,
    PaginatedNullableResponse,
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
            Self::GeneratedFileNameTooLong => "generated-file-name-too-long",
            Self::DefaultNotEnumValue => "default-not-enum-value",
            Self::GeneratorLintFailure => "generator-lint-failure",
            Self::TypeNotDefined => "type-not-defined",
            Self::MissingDiscriminantProperty => "missing-discriminant-property",
            Self::DuplicateExampleName => "duplicate-example-name",
            Self::ExampleSummaryNotString => "example-summary-not-string",
            Self::ExampleMissingRequiredQueryParameter => {
                "example-missing-required-query-parameter"
            }
            Self::ExampleTypeMismatch => "example-type-mismatch",
            Self::ExampleNotEnumValue => "example-not-enum-value",
            Self::ExampleUnexpectedProperty => "example-unexpected-property",
            Self::ExampleMissingRequiredProperty => "example-missing-required-property",
            Self::PaginatedNullableResponse => "paginated-nullable-response",
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
        crate::yaml::from_str::<Version>(&text).ok()
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
    let Ok(root) = crate::yaml::from_str::<serde_json::Value>(&text) else {
        return Ok(());
    };
    if let Some(paths) = root.get("paths").and_then(serde_json::Value::as_object) {
        for (route, item) in paths {
            let route = route.as_str();
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
    if let Some(paths) = root.get("paths").and_then(serde_json::Value::as_object) {
        for (route, item) in paths {
            let route = route.as_str();
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
        // A success response Fern builds a type from follows its response
        // component's own `$ref`, which must stay among the response
        // components: measured at Fern CLI 5.163.1 / fern-python-sdk 5.41.3, a
        // `204` aliasing `#/x-fragment/base` through `components/responses`
        // fails to resolve (`response-fragment` probe), where a `default`
        // response aliasing it generates (`response-fragment-default` control;
        // the Groupe PSA golden).
        for item in paths.values() {
            for method in [
                "get", "put", "post", "delete", "options", "head", "patch", "trace",
            ] {
                let Some(operation) = item.get(method) else {
                    continue;
                };
                if ignored_reference_node(operation) {
                    continue;
                }
                for (code, response) in operation
                    .get("responses")
                    .and_then(serde_json::Value::as_object)
                    .into_iter()
                    .flatten()
                {
                    let Some(name) = code
                        .starts_with('2')
                        .then(|| response.get("$ref").and_then(serde_json::Value::as_str))
                        .flatten()
                        .and_then(|reference| reference.strip_prefix("#/components/responses/"))
                    else {
                        continue;
                    };
                    if let Some(component) =
                        yaml_pointer(&root, &format!("/components/responses/{name}"))
                            .filter(|component| component.get("$ref").is_some())
                    {
                        check_reference_objects(
                            component,
                            &root,
                            path,
                            strict,
                            &format!("components/responses/{name}"),
                        )?;
                    }
                }
            }
        }
    }
    // Resolve missing Reference Objects before checking their parameter uses.
    if let Some(paths) = root.get("paths").and_then(serde_json::Value::as_object) {
        for (route, item) in paths {
            let route = route.as_str();
            for method in [
                "get", "put", "post", "delete", "options", "head", "patch", "trace",
            ] {
                let Some(operation) = item.get(method) else {
                    continue;
                };
                if ignored_reference_node(operation) {
                    continue;
                }
                let shared = item.get("parameters").and_then(serde_json::Value::as_array);
                let local = operation
                    .get("parameters")
                    .and_then(serde_json::Value::as_array);
                for parameter in shared
                    .into_iter()
                    .flatten()
                    .chain(local.into_iter().flatten())
                {
                    let parameter = parameter
                        .get("$ref")
                        .and_then(serde_json::Value::as_str)
                        .and_then(|reference| reference.strip_prefix('#'))
                        .and_then(|pointer| yaml_pointer(&root, pointer))
                        .unwrap_or(parameter);
                    if parameter.get("in").and_then(serde_json::Value::as_str) == Some("path") {
                        if let Some(name) =
                            parameter.get("name").and_then(serde_json::Value::as_str)
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
    if let Some((class, element)) = examples::first_violation_in(&root, &text) {
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
    node: &serde_json::Value,
    root: &serde_json::Value,
    state: &mut ExtensionCycles,
) -> bool {
    if let Some(reference) = node.get("$ref").and_then(serde_json::Value::as_str) {
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
    // Fern follows an extension's reference through its object members only: a
    // reference under an array (Stripe's `x-expansionResources: {oneOf: [...]}`)
    // never overflows its stack (the `*-oneof-link-control` and
    // `expandable-field-control` shapes).
    match node {
        serde_json::Value::Object(values) => values
            .values()
            .any(|value| extension_reference_cycle(value, root, state)),
        _ => false,
    }
}

fn cyclic_extension(
    node: &serde_json::Value,
    root: &serde_json::Value,
    element: &str,
    state: &mut ExtensionCycles,
    property_schema: bool,
) -> Option<String> {
    if ignored_reference_node(node) {
        return None;
    }
    match node {
        serde_json::Value::Object(values) => {
            for (key, value) in values {
                let key = key.as_str();
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
                    if let Some(properties) = value.as_object() {
                        for (name, schema) in properties {
                            let name = name.as_str();
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
        serde_json::Value::Array(values) => {
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
    root: &'a serde_json::Value,
    path: &'a Path,
    strict: bool,
    names: indexmap::IndexMap<String, bool>,
    default_names: indexmap::IndexMap<String, bool>,
    missing_header_types: std::collections::HashSet<String>,
    expanding: std::cell::OnceCell<ExpandingCycles>,
}

fn schema_declaration_names(
    root: &serde_json::Value,
    include_literals: bool,
    declaration_kind: fn(&serde_json::Value, &serde_json::Value) -> bool,
) -> indexmap::IndexMap<String, bool> {
    let mut names = indexmap::IndexMap::new();
    if let Some(schemas) = root
        .get("components")
        .and_then(|value| value.get("schemas"))
        .and_then(serde_json::Value::as_object)
    {
        for (key, schema) in schemas {
            let key = key.as_str();
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
    names
}

fn register_inline_declarations(
    schema: &serde_json::Value,
    parent: &str,
    root: &serde_json::Value,
    names: &mut indexmap::IndexMap<String, bool>,
    include_literals: bool,
    declaration_kind: fn(&serde_json::Value, &serde_json::Value) -> bool,
) {
    if ignored_reference_node(schema) {
        return;
    }
    if let Some(properties) = schema
        .get("properties")
        .and_then(serde_json::Value::as_object)
    {
        for (key, child) in properties {
            let key = key.as_str();
            if ignored_reference_node(child) || child.get("$ref").is_some() {
                continue;
            }
            let name = crate::naming::child_class_name(parent, key);
            let union = ["oneOf", "anyOf"].iter().any(|key| {
                child
                    .get(key)
                    .and_then(serde_json::Value::as_array)
                    .is_some_and(|variants| {
                        variants
                            .iter()
                            .filter(|value| {
                                value.get("type").and_then(serde_json::Value::as_str)
                                    != Some("null")
                            })
                            .count()
                            > 1
                    })
            });
            let enumeration = child
                .get("enum")
                .and_then(serde_json::Value::as_array)
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
        if let Some(children) = schema.get(key).and_then(serde_json::Value::as_array) {
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
    schema: &serde_json::Value,
    root: &serde_json::Value,
    seen: &mut Vec<String>,
) -> bool {
    if let Some(reference) = schema.get("$ref").and_then(serde_json::Value::as_str) {
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
        .and_then(serde_json::Value::as_object)
        .is_some()
    {
        return true;
    }
    if schema.get("oneOf").is_some() || schema.get("anyOf").is_some() {
        return false;
    }
    schema
        .get("allOf")
        .and_then(serde_json::Value::as_array)
        .is_some_and(|children| {
            children
                .iter()
                .any(|child| schema_is_model(child, root, seen))
        })
}

fn schema_type(schema: &serde_json::Value) -> Option<crate::openapi::TypeField> {
    schema
        .get("type")
        .and_then(|value| serde_json::from_value(value.clone()).ok())
}

fn check_object_extension(
    schema: &serde_json::Value,
    context: &SchemaContext<'_>,
    element: &str,
) -> Result<()> {
    let Some(children) = schema.get("allOf").and_then(serde_json::Value::as_array) else {
        return Ok(());
    };
    let references = children
        .iter()
        .filter_map(|child| child.get("$ref").and_then(serde_json::Value::as_str))
        .collect::<Vec<_>>();
    let ty = schema_type(schema);
    let primary = ty.as_ref().and_then(crate::openapi::TypeField::primary);
    if matches!(
        primary,
        Some("string" | "number" | "integer" | "boolean" | "array" | "null")
    ) {
        return Ok(());
    }
    // One referenced member and no fields of its own is an alias of that
    // member, whatever `type` or `nullable` sits beside it: measured at Fern CLI
    // 5.163.1, `typed-scalar-alias` and `typed-nullable-scalar-alias` generate.
    let own_fields = schema
        .get("properties")
        .and_then(serde_json::Value::as_object)
        .is_some_and(|properties| !properties.is_empty());
    if children.len() == 1 && references.len() == 1 && !own_fields {
        return Ok(());
    }
    let object = primary == Some("object")
        || schema
            .get("properties")
            .and_then(serde_json::Value::as_object)
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
        if !model && !object_union_base(target) {
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

/// Whether `target` is a union: Fern extends any `oneOf` or `anyOf` base,
/// measured at Fern CLI 5.163.1 by the `union-base`, `nested-union-base`,
/// `conditional-base`, `untyped-ref-union-base`, `anyof-ref-union-base`,
/// `scalar-member-union-base` and `ordered-renamed-union` controls, whatever
/// its members. A base itself typed scalar or array stays refused.
fn object_union_base(target: &serde_json::Value) -> bool {
    let scalar = matches!(
        schema_type(target)
            .as_ref()
            .and_then(crate::openapi::TypeField::primary),
        Some("string" | "number" | "integer" | "boolean" | "array" | "null")
    );
    !scalar
        && ["oneOf", "anyOf"].iter().any(|key| {
            target
                .get(key)
                .and_then(serde_json::Value::as_array)
                .is_some_and(|members| !members.is_empty())
        })
}

fn named_default_unsupported(schema: &serde_json::Value, root: &serde_json::Value) -> bool {
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
                .and_then(serde_json::Value::as_array)
                .is_some_and(|variants| {
                    variants
                        .iter()
                        .filter(|variant| {
                            variant.get("type").and_then(serde_json::Value::as_str) != Some("null")
                        })
                        .count()
                        > 1
                })
        })
}

fn check_named_type_defaults(
    schema: &serde_json::Value,
    parent: &str,
    context: &SchemaContext<'_>,
    element: &str,
) -> Result<()> {
    if ignored_reference_node(schema) {
        return Ok(());
    }
    if let Some(properties) = schema
        .get("properties")
        .and_then(serde_json::Value::as_object)
    {
        for (key, child) in properties {
            let key = key.as_str();
            if ignored_reference_node(child) || child.get("$ref").is_some() {
                continue;
            }
            let name = crate::naming::child_class_name(parent, key);
            let child_element = format!("{element}/properties/{key}");
            // Measured at Fern CLI 5.163.1 / fern-python-sdk 5.41.3: a boolean
            // `enum` or `const` is no enum declaration, and generates
            // (`boolean-enum-collision` and `const-boolean-collision` shapes;
            // Mistral's `stream`), where a string `const` is refused as a
            // string `enum` is (`const-string-collision`).
            let boolean = child.get("type").and_then(serde_json::Value::as_str) == Some("boolean")
                || child
                    .get("const")
                    .is_some_and(serde_json::Value::is_boolean)
                || child
                    .get("enum")
                    .and_then(serde_json::Value::as_array)
                    .is_some_and(|values| {
                        !values.is_empty() && values.iter().all(serde_json::Value::is_boolean)
                    });
            let enumeration = !boolean
                && (child
                    .get("enum")
                    .and_then(serde_json::Value::as_array)
                    .is_some_and(|values| !values.is_empty())
                    || child.get("const").is_some());
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
        if let Some(variants) = schema.get(key).and_then(serde_json::Value::as_array) {
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

fn missing_header_types(root: &serde_json::Value) -> std::collections::HashSet<String> {
    let mut total = 0usize;
    let mut headers: indexmap::IndexMap<String, (usize, String)> = indexmap::IndexMap::new();
    if let Some(paths) = root.get("paths").and_then(serde_json::Value::as_object) {
        for (route, item) in paths {
            let route = route.as_str();
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
                    serde_json::from_value::<crate::openapi::Operation>(operation.clone())
                else {
                    continue;
                };
                let request_ctx = &crate::ir::request_context(&parsed, method, route);
                let mut in_operation = std::collections::HashSet::new();
                for parameters in [item.get("parameters"), operation.get("parameters")]
                    .into_iter()
                    .flatten()
                {
                    let Some(parameters) = parameters.as_array() else {
                        continue;
                    };
                    for parameter in parameters {
                        let parameter = parameter
                            .get("$ref")
                            .and_then(serde_json::Value::as_str)
                            .and_then(|reference| reference.strip_prefix('#'))
                            .and_then(|pointer| yaml_pointer(root, pointer))
                            .unwrap_or(parameter);
                        if ignored_reference_node(parameter)
                            || parameter.get("in").and_then(serde_json::Value::as_str)
                                != Some("header")
                        {
                            continue;
                        }
                        let Some(name) = parameter.get("name").and_then(serde_json::Value::as_str)
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

fn check_document_schemas(root: &serde_json::Value, path: &Path, strict: bool) -> Result<()> {
    let context = SchemaContext {
        root,
        path,
        strict,
        names: schema_declaration_names(root, false, |schema, root| {
            schema_is_model(schema, root, &mut Vec::new())
        }),
        default_names: schema_declaration_names(root, true, named_default_unsupported),
        missing_header_types: missing_header_types(root),
        expanding: std::cell::OnceCell::new(),
    };
    if let Some(schemas) = root
        .get("components")
        .and_then(|value| value.get("schemas"))
        .and_then(serde_json::Value::as_object)
    {
        for (name, schema) in schemas {
            let name = name.as_str();
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
    if let Some(paths) = root.get("paths").and_then(serde_json::Value::as_object) {
        for (route, item) in paths {
            let route = route.as_str();
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
/// every mapping target is missing or the union itself; otherwise each `x-fern-examples` value is
/// checked. Plain OpenAPI examples and `x-crozier-examples` play no part: Fern
/// discards the first and never reads the second. Measured in
/// `docs/fern-refusals/missing-discriminant-property/evaluation.md`.
fn check_discriminant_examples(root: &serde_json::Value, path: &Path, strict: bool) -> Result<()> {
    let Some(paths) = root.get("paths").and_then(serde_json::Value::as_object) else {
        return Ok(());
    };
    for (route, item) in paths {
        let route = route.as_str();
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
                .and_then(serde_json::Value::as_object);
            let mut codes: Vec<(String, &serde_json::Value)> = responses
                .into_iter()
                .flatten()
                .filter_map(|(code, response)| {
                    let code = code.clone();
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
                .and_then(serde_json::Value::as_array)
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
    node: &'a serde_json::Value,
    root: &'a serde_json::Value,
) -> &'a serde_json::Value {
    node.get("$ref")
        .and_then(serde_json::Value::as_str)
        .and_then(|reference| reference.strip_prefix('#'))
        .and_then(|pointer| yaml_pointer(root, pointer))
        .unwrap_or(node)
}

fn json_schema(body: &serde_json::Value) -> Option<&serde_json::Value> {
    if ignored_reference_node(body) {
        return None;
    }
    body.get("content")?.get("application/json")?.get("schema")
}

/// The property a discriminated union requires of its example, and its mapping.
fn discriminated_union(
    schema: &serde_json::Value,
) -> Option<(&str, &serde_json::Map<String, serde_json::Value>)> {
    let discriminator = schema.get("discriminator")?;
    let property = discriminator
        .get("propertyName")
        .and_then(serde_json::Value::as_str)?;
    let mapping = discriminator
        .get("mapping")
        .and_then(serde_json::Value::as_object)
        .filter(|mapping| !mapping.is_empty())?;
    // Fern imports an `anyOf` discriminator as an undiscriminated union.
    schema.get("anyOf").is_none().then_some((property, mapping))
}

/// Fern omits an optional property from its example below three object levels.
const EXAMPLE_OPTIONAL_LEVELS: usize = 3;
/// The deepest required chain measured to carry Fern's example to a union.
const EXAMPLE_REQUIRED_LEVELS: usize = 12;

/// The union Fern's own example reaches with every mapping target missing or
/// naming the union itself: no variant is then left to fill, and the example
/// `{}` has no discriminant.
fn unmapped_union(
    schema: &serde_json::Value,
    root: &serde_json::Value,
    element: &str,
    levels: usize,
    seen: &mut std::collections::HashSet<(String, usize)>,
) -> Option<String> {
    if ignored_reference_node(schema) {
        return None;
    }
    if let Some(reference) = schema.get("$ref").and_then(serde_json::Value::as_str) {
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
        // A target naming the union itself offers Fern's example no variant
        // either: Apple's SiriKit Cloud Media `AddMediaIntentHandlingInvocation`
        // maps all four of its `method` values to itself.
        let missing = mapping.values().all(|target| {
            target
                .as_str()
                .and_then(|target| target.strip_prefix('#'))
                .is_some_and(|pointer| {
                    yaml_pointer(root, pointer).is_none_or(|target| std::ptr::eq(target, schema))
                })
        });
        // A resolved variant becomes Fern's example, so nothing below is reached.
        return missing.then(|| format!("{element} discriminator {property}"));
    }
    if levels < EXAMPLE_REQUIRED_LEVELS {
        if let Some(properties) = schema
            .get("properties")
            .and_then(serde_json::Value::as_object)
        {
            let required = schema.get("required").and_then(serde_json::Value::as_array);
            for (name, child) in properties {
                let name = name.as_str();
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
            if let Some(child) = schema.get(key).filter(|child| child.is_object()) {
                let child_element = format!("{element}/{key}");
                if let Some(union) = unmapped_union(child, root, &child_element, levels + 1, seen) {
                    return Some(union);
                }
            }
        }
    }
    for key in ["allOf", "oneOf", "anyOf"] {
        if let Some(children) = schema.get(key).and_then(serde_json::Value::as_array) {
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
    example: &serde_json::Value,
    schema: &serde_json::Value,
    root: &serde_json::Value,
    element: &str,
    seen: &mut std::collections::HashSet<String>,
) -> Option<String> {
    if ignored_reference_node(schema) {
        return None;
    }
    if let Some(reference) = schema.get("$ref").and_then(serde_json::Value::as_str) {
        let pointer = reference.strip_prefix('#')?;
        if !seen.insert(reference.to_owned()) {
            return None;
        }
        let target = yaml_pointer(root, pointer)?;
        let union = example_without_discriminant(example, target, root, element, seen);
        seen.remove(reference);
        return union;
    }
    let example = example.as_object()?;
    if let Some((property, _)) = discriminated_union(schema) {
        return (schema.get("oneOf").is_some() && !example.contains_key(property))
            .then(|| format!("{element} discriminator {property}"));
    }
    let properties = schema
        .get("properties")
        .and_then(serde_json::Value::as_object)?;
    example.iter().find_map(|(name, value)| {
        let child = properties.get(name)?;
        let name = name.as_str();
        example_without_discriminant(value, child, root, &format!("{element}/{name}"), seen)
    })
}

fn check_bound_schemas(
    node: &serde_json::Value,
    context: &SchemaContext<'_>,
    element: &str,
    seen: &mut std::collections::HashSet<String>,
) -> Result<()> {
    if ignored_reference_node(node) {
        return Ok(());
    }
    if let Some(reference) = node.get("$ref").and_then(serde_json::Value::as_str) {
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
        serde_json::Value::Object(values) => {
            for (key, value) in values {
                let key = key.as_str();
                if key == "schema" {
                    let location = match node.get("in").and_then(serde_json::Value::as_str) {
                        Some("query") => SchemaLocation::Query,
                        Some(_) => SchemaLocation::Parameter,
                        None => SchemaLocation::Type,
                    };
                    let name = node.get("name").and_then(serde_json::Value::as_str);
                    let schema_element = name.map_or_else(
                        || format!("{element}/schema"),
                        |name| format!("{element}/{name}/schema"),
                    );
                    if node.get("in").and_then(serde_json::Value::as_str) == Some("header")
                        // llmlint: ignore[contracts_have_one_source_or_a_drift_gate] These are Fern's inline-header declaration exceptions, measured in generator-missing-type/evaluation-logs/fern-*-header.log, not SDK transport ownership. In particular Authorization is a per-method SDK parameter without an auth scheme (ir::is_auth_managed_header), while Fern declares its inline enum successfully. Changing SDK header ownership must not change this refusal classification; the CLI controls preserve all three measured exceptions.
                        && name.is_some_and(|name| {
                            context.missing_header_types.contains(name)
                                && !["Authorization", "User-Agent", "Content-Type"]
                                .iter()
                                .any(|exception| name.eq_ignore_ascii_case(exception))
                        })
                        && !ignored_reference_node(value)
                        && value.get("$ref").is_none()
                        // Measured at Fern CLI 5.163.1 / fern-python-sdk 5.41.3:
                        // a header enum with a default generates (the
                        // `*-default` shapes; AgenticDriver's
                        // `Accept-Optional-Events`).
                        && value.get("default").is_none()
                        && value
                            .get("type")
                            .is_none_or(|kind| kind.as_str() == Some("string"))
                        && (value
                            .get("enum")
                            .and_then(serde_json::Value::as_array)
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
                    key,
                    "example" | "examples" | "default" | "enum" | "links" | "headers" | "encoding"
                ) && !key.starts_with("x-")
                {
                    check_bound_schemas(value, context, &format!("{element}/{key}"), seen)?;
                }
            }
        }
        serde_json::Value::Array(values) => {
            for (index, value) in values.iter().enumerate() {
                check_bound_schemas(value, context, &format!("{element}/{index}"), seen)?;
            }
        }
        _ => {}
    }
    Ok(())
}

/// Whether `schema` admits `null`: a `null` type, `nullable: true`, or a
/// `oneOf`/`anyOf` member that does.
fn admits_null(schema: &serde_json::Value) -> bool {
    let typed_null = match schema.get("type") {
        Some(serde_json::Value::String(kind)) => kind == "null",
        Some(serde_json::Value::Array(kinds)) => kinds.iter().any(|kind| kind == "null"),
        _ => false,
    };
    typed_null
        || schema.get("nullable").and_then(document_boolean) == Some(true)
        || ["oneOf", "anyOf"].iter().any(|key| {
            schema
                .get(key)
                .and_then(serde_json::Value::as_array)
                .is_some_and(|members| members.iter().any(admits_null))
        })
}

fn check_schema_resolution(
    schema: &serde_json::Value,
    context: &SchemaContext<'_>,
    element: &str,
    required: bool,
    seen: &mut std::collections::HashSet<String>,
) -> Result<()> {
    if ignored_reference_node(schema) {
        return Ok(());
    }
    if let Some(reference) = schema.get("$ref").and_then(serde_json::Value::as_str) {
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
        // Measured at Fern CLI 5.163.1 / fern-python-sdk 5.41.3: a definition
        // that admits `null` leaves its required property nullable, which Fern
        // never resolves, so it generates (`defs-nullable-target` shape;
        // AgenticDriver's `$defs/__schema0`). A definition that does not is
        // still refused (`deep-defs-field`).
        let nullable_definition = unsupported_definition && target.is_some_and(admits_null);
        if required
            && !walked
            && schema_reference.is_some()
            && (target.is_none() || (unsupported_definition && !nullable_definition))
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
        .and_then(serde_json::Value::as_object)
    {
        let required_fields = schema.get("required").and_then(serde_json::Value::as_array);
        for (name, child) in properties {
            let name = name.as_str();
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
        if let Some(children) = schema.get(key).and_then(serde_json::Value::as_array) {
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

/// The references from which a cycle that grows on every turn is reachable.
///
/// A turn grows where one of its references points partway into a component
/// (anywhere but its `$defs`), or extends a union base through `allOf`. Fern
/// expands such a cycle without end: measured at Fern CLI 5.163.1, one growing
/// reference names each turn's type after the last until a file name is too
/// long (`single-child` and `recursive-union-allof` probes, Kibana's zod
/// schema), while two or more branch the expansion and exhaust its heap (the
/// class probe, Wiremock's and virtual-tools' documents). The answer is
/// computed once per document over the reference graph's strongly connected
/// components, so a densely recursive description (Stripe's) stays linear.
#[derive(Default)]
struct ExpandingCycles {
    /// References reaching a cycle with two or more growing references.
    branching: std::collections::HashSet<String>,
    /// References reaching a cycle with one growing reference.
    lengthening: std::collections::HashSet<String>,
}

/// A reference a schema reaches without following another, and whether that
/// step grows a cycle through it.
struct ReferenceStep {
    reference: String,
    grows: bool,
}

impl ExpandingCycles {
    fn of(root: &serde_json::Value) -> Self {
        let mut edges: indexmap::IndexMap<String, Vec<ReferenceStep>> = indexmap::IndexMap::new();
        // Every reference the document writes is a node, wherever a union
        // that reaches it sits.
        let mut queue = Vec::new();
        every_reference(root, &mut queue);
        while let Some(reference) = queue.pop() {
            if edges.contains_key(&reference) {
                continue;
            }
            let mut steps = Vec::new();
            if let Some(target) = reference
                .strip_prefix('#')
                .and_then(|pointer| yaml_pointer(root, pointer))
            {
                reference_steps(target, root, false, &mut steps);
            }
            queue.extend(steps.iter().map(|step| step.reference.clone()));
            edges.insert(reference, steps);
        }
        let components = strongly_connected(&edges);
        let mut component_of = std::collections::HashMap::new();
        for (index, members) in components.iter().enumerate() {
            for member in members {
                component_of.insert(member.as_str(), index);
            }
        }
        // Tarjan's order lists every component after the ones it reaches.
        let mut branches = vec![false; components.len()];
        let mut lengthens = vec![false; components.len()];
        for (index, members) in components.iter().enumerate() {
            let mut growing = 0;
            for member in members {
                for step in &edges[member] {
                    let next = component_of[step.reference.as_str()];
                    if next == index {
                        growing += usize::from(step.grows);
                    } else {
                        branches[index] |= branches[next];
                        lengthens[index] |= lengthens[next];
                    }
                }
            }
            branches[index] |= growing >= 2;
            lengthens[index] |= growing == 1;
        }
        let members_where = |flags: &[bool]| -> std::collections::HashSet<String> {
            components
                .iter()
                .zip(flags)
                .filter(|(_, flag)| **flag)
                .flat_map(|(members, _)| members.iter().cloned())
                .collect()
        };
        Self {
            branching: members_where(&branches),
            lengthening: members_where(&lengthens),
        }
    }
}

/// Every `$ref` string anywhere under `node`.
fn every_reference(node: &serde_json::Value, found: &mut Vec<String>) {
    match node {
        serde_json::Value::Object(values) => {
            if let Some(reference) = values.get("$ref").and_then(serde_json::Value::as_str) {
                found.push(reference.to_owned());
            }
            for value in values.values() {
                every_reference(value, found);
            }
        }
        serde_json::Value::Array(values) => {
            for value in values {
                every_reference(value, found);
            }
        }
        _ => {}
    }
}

/// Every reference `schema` reaches through its properties, items, map values
/// and `allOf`/`oneOf`/`anyOf` members, without following one.
fn reference_steps(
    schema: &serde_json::Value,
    root: &serde_json::Value,
    extends: bool,
    steps: &mut Vec<ReferenceStep>,
) {
    if ignored_reference_node(schema) {
        return;
    }
    if let Some(reference) = schema.get("$ref").and_then(serde_json::Value::as_str) {
        let Some(target) = reference
            .strip_prefix('#')
            .and_then(|pointer| yaml_pointer(root, pointer))
        else {
            return;
        };
        if ignored_reference_node(target) {
            return;
        }
        // A pointer into a component's `$defs` names a schema of its own, which
        // Fern follows as it does a component: measured at Fern CLI 5.163.1 /
        // fern-python-sdk 5.41.3, a JSON-value union recursing through
        // `$defs/__value` generates (`defs-json-value` shape).
        let partial = reference
            .strip_prefix("#/components/schemas/")
            .is_some_and(|suffix| {
                let mut segments = suffix.split('/');
                segments.next();
                segments.next().is_some_and(|segment| segment != "$defs")
            });
        let union_base = extends
            && ["oneOf", "anyOf"].iter().any(|key| {
                target
                    .get(key)
                    .and_then(serde_json::Value::as_array)
                    .is_some_and(|variants| variants.len() > 1)
            })
            && !schema_is_model(target, root, &mut Vec::new());
        steps.push(ReferenceStep {
            reference: reference.to_owned(),
            grows: partial || union_base,
        });
        return;
    }
    if let Some(properties) = schema
        .get("properties")
        .and_then(serde_json::Value::as_object)
    {
        for property in properties.values() {
            reference_steps(property, root, false, steps);
        }
    }
    for key in ["items", "additionalProperties"] {
        if let Some(child) = schema.get(key) {
            reference_steps(child, root, false, steps);
        }
    }
    // One referenced `allOf` member and no fields of its own is an alias of
    // that member, not an extension of it: measured at Fern CLI 5.163.1,
    // Helicone's nullable `allOf: [CustomerSource]` generates
    // (`nullable-union-alias` control).
    let own_fields = schema
        .get("properties")
        .and_then(serde_json::Value::as_object)
        .is_some_and(|properties| !properties.is_empty());
    for key in ["allOf", "oneOf", "anyOf"] {
        if let Some(children) = schema.get(key).and_then(serde_json::Value::as_array) {
            let extends = key == "allOf" && (children.len() > 1 || own_fields);
            for child in children {
                reference_steps(child, root, extends, steps);
            }
        }
    }
}

/// The strongly connected components of `edges` (Tarjan's, iterative), each
/// listed after every component it reaches.
fn strongly_connected(edges: &indexmap::IndexMap<String, Vec<ReferenceStep>>) -> Vec<Vec<String>> {
    let count = edges.len();
    let next: Vec<Vec<usize>> = edges
        .values()
        .map(|steps| {
            steps
                .iter()
                .map(|step| edges.get_index_of(&step.reference).unwrap_or(usize::MAX))
                .filter(|index| *index != usize::MAX)
                .collect()
        })
        .collect();
    let mut index = vec![usize::MAX; count];
    let mut low = vec![0; count];
    let mut on_stack = vec![false; count];
    let mut stack = Vec::new();
    let mut components = Vec::new();
    let mut counter = 0;
    for start in 0..count {
        if index[start] != usize::MAX {
            continue;
        }
        let mut frames = vec![(start, 0)];
        index[start] = counter;
        low[start] = counter;
        counter += 1;
        stack.push(start);
        on_stack[start] = true;
        while let Some(&mut (node, ref mut edge)) = frames.last_mut() {
            if let Some(&target) = next[node].get(*edge) {
                *edge += 1;
                if index[target] == usize::MAX {
                    index[target] = counter;
                    low[target] = counter;
                    counter += 1;
                    stack.push(target);
                    on_stack[target] = true;
                    frames.push((target, 0));
                } else if on_stack[target] {
                    low[node] = low[node].min(index[target]);
                }
                continue;
            }
            frames.pop();
            if let Some(&(parent, _)) = frames.last() {
                low[parent] = low[parent].min(low[node]);
            }
            if low[node] == index[node] {
                let mut members = Vec::new();
                while let Some(member) = stack.pop() {
                    on_stack[member] = false;
                    members.push(
                        edges
                            .get_index(member)
                            .map(|(key, _)| key.clone())
                            .unwrap_or_default(),
                    );
                    if member == node {
                        break;
                    }
                }
                components.push(members);
            }
        }
    }
    components
}

/// The class Fern refuses `schema` with when a cycle that grows on every turn
/// is reachable from it: `heap-exhausted` where one branches, else
/// `generated-file-name-too-long`.
fn expanding_union_cycle(schema: &serde_json::Value, context: &SchemaContext<'_>) -> Option<Class> {
    let cycles = context
        .expanding
        .get_or_init(|| ExpandingCycles::of(context.root));
    let mut steps = Vec::new();
    reference_steps(schema, context.root, false, &mut steps);
    let reaches = |set: &std::collections::HashSet<String>| {
        steps.iter().any(|step| set.contains(&step.reference))
    };
    if reaches(&cycles.branching) {
        Some(Class::HeapExhausted)
    } else if reaches(&cycles.lengthening) {
        Some(Class::GeneratedFileNameTooLong)
    } else {
        None
    }
}

fn check_schema(
    schema: &serde_json::Value,
    context: &SchemaContext<'_>,
    element: &str,
    location: SchemaLocation,
    seen: &mut std::collections::HashSet<String>,
) -> Result<()> {
    if ignored_reference_node(schema) {
        return Ok(());
    }
    if let Some(reference) = schema.get("$ref").and_then(serde_json::Value::as_str) {
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
            .and_then(serde_json::Value::as_array)
            .is_some_and(|variants| variants.len() > 1)
    }) {
        if let Some(class) = expanding_union_cycle(schema, context) {
            return refusal(context.path, context.strict, class, element);
        }
    }
    check_object_extension(schema, context, element)?;
    if let Some(default) = schema
        .get("default")
        .filter(|value| !value.is_null() && !matches!(location, SchemaLocation::Type))
    {
        if matches!(location, SchemaLocation::Field)
            && schema.get("type").and_then(serde_json::Value::as_str) == Some("array")
            && default.as_array().is_none()
        {
            return refusal(
                context.path,
                context.strict,
                Class::ListDefaultNotArray,
                &format!("{element} default {default:?}"),
            );
        }
        let invalid = match schema.get("type").and_then(serde_json::Value::as_str) {
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
    if let Some(default) = schema.get("default").and_then(serde_json::Value::as_str) {
        let query_array = matches!(location, SchemaLocation::Query)
            && schema.get("type").and_then(serde_json::Value::as_str) == Some("array");
        let candidate = if query_array {
            schema.get("items").unwrap_or(schema)
        } else {
            schema
        };
        if let Some(values) = candidate.get("enum").and_then(serde_json::Value::as_array) {
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
    // `visit` method has no body, which its own `ruff check` cannot parse; an
    // untyped one too, measured at Fern CLI 5.163.1 / fern-python-sdk 5.41.3
    // (`untyped-null-only-enum` probe; tunarr's `userId`).
    if schema
        .get("type")
        .is_none_or(|kind| kind.as_str() == Some("string"))
        && schema
            .get("enum")
            .and_then(serde_json::Value::as_array)
            .is_some_and(|values| values.iter().all(serde_json::Value::is_null))
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
        .and_then(serde_json::Value::as_object)
    {
        for (name, child) in properties {
            let name = name.as_str();
            check_schema(
                child,
                context,
                &format!("{element}/properties/{name}"),
                SchemaLocation::Field,
                seen,
            )?;
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
        if let Some(children) = schema.get(key).and_then(serde_json::Value::as_array) {
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
fn retained_enum_default(schema: &serde_json::Value, default: &str, path: &Path) -> Result<bool> {
    let mut schema = schema.clone();
    if let Some(mapping) = schema.as_object_mut() {
        mapping.retain(|key, _| !key.starts_with("x-crozier-"));
        mapping.insert("type".into(), "string".into());
    }
    let mut schemas = serde_json::Map::new();
    schemas.insert("EnumDefaultProbe".into(), schema);
    let mut components = serde_json::Map::new();
    components.insert("schemas".into(), schemas.into());
    let mut document = serde_json::Map::new();
    document.insert("openapi".into(), "3.0.3".into());
    document.insert("components".into(), components.into());
    let Ok(doc) = serde_json::from_value::<OpenApi>(document.into()) else {
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

fn ignored_reference_node(value: &serde_json::Value) -> bool {
    // Keep the dual-header decision in the existing canonical accessor.
    let mut extensions = serde_json::Map::new();
    for name in ["x-crozier-ignore", "x-fern-ignore"] {
        if let Some(value) = value.get(name) {
            extensions.insert(name.into(), value.clone());
        }
    }
    serde_json::from_value::<crate::openapi::Schema>(serde_json::Value::Object(extensions))
        .is_ok_and(|schema| schema.ignored())
}

fn check_named_examples(
    examples: &serde_json::Value,
    root: &serde_json::Value,
    path: &Path,
    strict: bool,
    element: &str,
) -> Result<()> {
    let Some(examples) = examples.as_object() else {
        return Ok(());
    };
    for (name, example) in examples {
        let name = name.as_str();
        let Some(reference) = example.get("$ref").and_then(serde_json::Value::as_str) else {
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
    value: &serde_json::Value,
    root: &serde_json::Value,
    path: &Path,
    strict: bool,
    element: &str,
) -> Result<()> {
    use serde_json::Value;
    match value {
        Value::Object(mapping) => {
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
                let key = key.as_str();
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
                // A schema slot is a Schema Object, not a Reference Object of the
                // enclosing kind: `itemSchema` is a sequential media type's
                // per-item schema, so a `#/components/schemas` reference there is
                // as valid as under `schema`.
                if matches!(
                    key,
                    "schema"
                        | "itemSchema"
                        | "schemas"
                        | "example"
                        | "examples"
                        | "default"
                        | "enum"
                        | "const"
                ) || key.starts_with("x-")
                {
                    continue;
                }
                check_reference_objects(child, root, path, strict, &format!("{element}/{key}"))?;
            }
        }
        Value::Array(values) => {
            for (index, child) in values.iter().enumerate() {
                check_reference_objects(child, root, path, strict, &format!("{element}/{index}"))?;
            }
        }
        _ => {}
    }
    Ok(())
}

fn yaml_pointer<'a>(root: &'a serde_json::Value, pointer: &str) -> Option<&'a serde_json::Value> {
    if pointer.is_empty() {
        return Some(root);
    }
    let mut value = root;
    for token in pointer.strip_prefix('/')?.split('/') {
        let token = token.replace("~1", "/").replace("~0", "~");
        value = match value {
            serde_json::Value::Array(sequence) => sequence.get(token.parse::<usize>().ok()?)?,
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
            .and_then(|text| crate::yaml::from_str::<serde_json::Value>(&text).ok())
        else {
            return false;
        };
        let Some(value) = yaml_pointer(&root, pointer) else {
            return false;
        };
        let Ok(resolved) = serde_json::from_value::<SecurityScheme>(value.clone()) else {
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
    if let Some(element) = paginated_nullable_response(doc) {
        return refusal(path, strict, Class::PaginatedNullableResponse, &element);
    }
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
    if let Some(header) = doc
        .global_header_extensions()
        .iter()
        .find(|header| crate::naming::field_name(&header.name).is_empty())
    {
        return refusal(
            path,
            strict,
            class,
            &format!(
                "global header {:?} constructor name {:?}",
                header.header, header.name
            ),
        );
    }
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
    // A syntax error: a sub-client class named from a tag led by a digit
    // (Hyperswitch's `3DS Decision Rule` → `class 3dsDecisionRuleClient`), which
    // Fern's own `ruff check` fails on at Fern CLI 5.163.1.
    if let Some(module) = ir
        .endpoint_modules
        .iter()
        .flat_map(|module| module.split('/'))
        .find(|segment| {
            crate::naming::to_pascal_case(segment).starts_with(|first: char| first.is_ascii_digit())
        })
    {
        return refusal(
            path,
            strict,
            class,
            &format!(
                "sub-client {module} class {}Client",
                crate::naming::to_pascal_case(module)
            ),
        );
    }
    for endpoint in ir.endpoints.iter().filter(|endpoint| endpoint.emittable) {
        let route = format!("{} {}", endpoint.http_method, endpoint.path);
        // F811: a root-client method and a sub-client property of one name.
        // The empty `_` namespace is a sub-client like any other; no root
        // method can be named `_` (method naming empties it), so it needs no
        // exemption here.
        // llmlint: ignore[changed_behavior_has_e2e] Dropping the `_` exemption changes no reachable behaviour: `x-fern-sdk-method-name: _` and `operationId: _` both name an empty method, never `_`, so no CLI input can drive a root method `_` beside the namespace. The empty-namespace goldens (lamp-room-log, bungie.net) and sdk_env_empty_namespace_package_imports_and_answers_its_documented_call cover the namespace generating.
        if endpoint.module.is_empty()
            && ir
                .endpoint_modules
                .iter()
                .any(|module| module.split('/').next() == Some(endpoint.method_name.as_str()))
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
        if let Some(element) = idempotency_argument_fault(endpoint) {
            return refusal(path, strict, class, &format!("{route} {element}"));
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
        // A placeholder no variable binds is not refused: fern-python-sdk
        // 5.41.3 formats the template through a variable
        // (`_url_template = _environment_url_templates.get(environment, "…")`
        // then `_url_template.format(…)`), which ruff's F524 cannot read, so
        // Fern's own `ruff check` passes it. Only 5.20.0's literal
        // `"…".format(…)` tripped F524.
    }
    Ok(())
}

/// The first idempotency header whose argument the method signature cannot
/// take: a syntax error when its Python name is empty (a header like `-`), and
/// a duplicate argument when it repeats another argument of the method (an
/// earlier idempotency header, or a path, query, header or body argument).
/// Pinned Fern's `ruff check` rejects all three, so the element names the
/// header and the argument it would have written.
fn idempotency_argument_fault(endpoint: &crate::ir::Endpoint) -> Option<String> {
    use crate::ir::RequestBody;
    let body: Vec<&str> = match &endpoint.request_body {
        None => Vec::new(),
        Some(RequestBody::Single(_) | RequestBody::Bytes { .. }) => vec!["request"],
        Some(RequestBody::Inline(fields)) => {
            fields.iter().map(|field| field.py_name.as_str()).collect()
        }
        Some(RequestBody::Form(form)) => form
            .fields
            .iter()
            .map(|field| field.py_name.as_str())
            .collect(),
    };
    let mut taken: Vec<&str> = endpoint
        .path_params
        .iter()
        .map(|param| param.py_name.as_str())
        .chain(
            endpoint
                .query_params
                .iter()
                .map(|param| param.py_name.as_str()),
        )
        .chain(
            endpoint
                .header_params
                .iter()
                .map(|param| param.py_name.as_str()),
        )
        .chain(body)
        .chain(["request_options"])
        .collect();
    for header in &endpoint.extensions.idempotency_headers {
        let name = header.py_name.as_str();
        if name.is_empty() || taken.contains(&name) {
            return Some(format!(
                "idempotency header {:?} argument {name:?}",
                header.wire_name
            ));
        }
        taken.push(name);
    }
    None
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
    root: &serde_json::Value,
) -> impl Iterator<Item = (&'static str, &str, &serde_json::Value)> {
    root.get("paths")
        .and_then(serde_json::Value::as_object)
        .into_iter()
        .flatten()
        .filter(|(_, item)| !ignored_reference_node(item))
        .map(|(route, item)| (route.as_str(), item))
        .flat_map(|(route, item)| {
            OPERATION_METHODS.iter().filter_map(move |method| {
                let operation = item.get(*method)?;
                (operation.is_object() && !ignored_reference_node(operation))
                    .then_some((*method, route, operation))
            })
        })
}

/// A node with its local `$ref` chain followed; `None` for a reference that
/// cannot be followed here (other classes own those).
fn local_target<'a>(
    root: &'a serde_json::Value,
    mut node: &'a serde_json::Value,
) -> Option<&'a serde_json::Value> {
    for _ in 0..32 {
        let Some(reference) = node.get("$ref").and_then(serde_json::Value::as_str) else {
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
    root: &'a serde_json::Value,
    operation: &'a serde_json::Value,
) -> Option<&'a serde_json::Value> {
    let content = local_target(root, operation.get("requestBody")?)?
        .get("content")?
        .as_object()?;
    content
        .iter()
        .find(|(media_type, _)| json_examples_media(media_type))
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
    root: &'a serde_json::Value,
    operation: &'a serde_json::Value,
) -> Option<&'a serde_json::Value> {
    let responses = operation.get("responses")?.as_object()?;
    let mut candidates: Vec<(u64, &serde_json::Value)> = responses
        .iter()
        .filter_map(|(code, response)| {
            let code = code.parse::<u64>().ok()?;
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
            .and_then(serde_json::Value::as_object)
            .filter(|content| !content.is_empty());
        let Some(content) = content else {
            if code == 0 {
                return None;
            }
            continue;
        };
        if let Some((_, media)) = content
            .iter()
            .find(|(media_type, _)| json_examples_media(media_type))
        {
            return media.get("examples");
        }
        if code == 0
            || !content
                .keys()
                .all(|media_type| media_type == "application/xml")
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
    root: &serde_json::Value,
    key: &str,
    example: &serde_json::Value,
) -> Option<serde_json::Value> {
    if let Some(summary) = local_target(root, example)?
        .get("summary")
        .filter(|summary| !summary.is_null())
    {
        return Some(summary.clone());
    }
    Some(serde_json::Value::String(key.to_owned()))
}

fn name_label(name: &serde_json::Value) -> String {
    match name {
        serde_json::Value::String(text) => text.clone(),
        serde_json::Value::Number(number) => number.to_string(),
        serde_json::Value::Bool(boolean) => boolean.to_string(),
        other => format!("{other:?}"),
    }
}

fn first_duplicate(
    names: impl IntoIterator<Item = serde_json::Value>,
) -> Option<serde_json::Value> {
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
fn check_example_names(root: &serde_json::Value, path: &Path, strict: bool) -> Result<()> {
    for (method, route, operation) in imported_operations(root) {
        let element = format!("{} {route}", method.to_ascii_uppercase());
        if let Some(examples) = operation.get("x-fern-examples") {
            let Some(examples) = examples.as_array() else {
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
            let Some(examples) = examples.and_then(serde_json::Value::as_object) else {
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
    // fern-python-sdk 5.41.3 crashes on a request example named by a summary
    // that is no string (`Cannot use 'in' operator to search for 'wireValue'
    // in 1`), after a clean `fern check`: measured at Fern CLI 5.163.1 (the
    // class's probe, and `duplicate-example-name`'s `number-vs-string-summary`
    // shape). OpenAPI declares `summary` a string, so the document is at fault.
    for (method, route, operation) in imported_operations(root) {
        if operation
            .get("x-fern-examples")
            .and_then(serde_json::Value::as_array)
            .is_some_and(|examples| !examples.is_empty())
        {
            continue;
        }
        let Some(examples) =
            request_examples(root, operation).and_then(serde_json::Value::as_object)
        else {
            continue;
        };
        for (key, example) in examples {
            if let Some(name) = example_name(root, key, example).filter(|name| !name.is_string()) {
                let element = format!(
                    "{} {route} request example {key} summary {}",
                    method.to_ascii_uppercase(),
                    name_label(&name)
                );
                return refusal(path, strict, Class::ExampleSummaryNotString, &element);
            }
        }
    }
    Ok(())
}

/// The operation's query parameters as Fern imports them: Path Item
/// parameters overridden by the operation's own of the same name, references
/// followed, ignored parameters dropped.
fn query_parameters<'a>(
    root: &'a serde_json::Value,
    item: &'a serde_json::Value,
    operation: &'a serde_json::Value,
) -> Vec<(&'a str, &'a serde_json::Value)> {
    let mut parameters: Vec<(&str, &serde_json::Value)> = Vec::new();
    for parameter in [item, operation]
        .into_iter()
        .filter_map(|node| node.get("parameters")?.as_array())
        .flatten()
    {
        let Some(parameter) = local_target(root, parameter) else {
            continue;
        };
        if parameter.get("in").and_then(serde_json::Value::as_str) != Some("query") {
            continue;
        }
        let Some(name) = parameter.get("name").and_then(serde_json::Value::as_str) else {
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
fn parameter_schema(parameter: &serde_json::Value) -> Option<&serde_json::Value> {
    parameter.get("schema").or_else(|| {
        parameter
            .get("content")?
            .as_object()?
            .values()
            .next()?
            .get("schema")
    })
}

/// Whether a schema is `nullable` or a list, the shapes an example may omit —
/// or cannot be followed, which is never refused.
fn omittable_schema(root: &serde_json::Value, schema: Option<&serde_json::Value>) -> bool {
    let Some(schema) = schema else {
        return false;
    };
    let Some(schema) = local_target(root, schema) else {
        return true;
    };
    let type_is = |name: &str| match schema.get("type") {
        Some(serde_json::Value::String(value)) => value == name,
        Some(serde_json::Value::Array(values)) => {
            values.iter().any(|value| value.as_str() == Some(name))
        }
        _ => false,
    };
    schema.get("nullable").and_then(document_boolean) == Some(true)
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
    root: &serde_json::Value,
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
            .and_then(serde_json::Value::as_array)
            .filter(|examples| !examples.is_empty());
        if let Some(examples) = examples {
            for (index, example) in examples.iter().enumerate() {
                let given = match example.get("query-parameters") {
                    Some(serde_json::Value::Object(given)) => given.clone(),
                    None if example.get("response").is_some() => serde_json::Map::new(),
                    _ => continue,
                };
                let missing = parameters.iter().find(|(name, parameter)| {
                    parameter.get("required").and_then(document_boolean) == Some(true)
                        && !omittable_schema(root, parameter_schema(parameter))
                        && given.get(*name).is_none_or(serde_json::Value::is_null)
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

/// The first operation whose pagination contract reads its page off a
/// response the document declares `nullable: true`: Fern refuses it ("Response
/// must be an object in order to return property next as a response"), and a
/// pager over a page that may be `null` has no page to read, so crozier refuses
/// it too rather than dropping the pager. The element names the operation, the
/// contract's response property and the nullable component.
fn paginated_nullable_response(doc: &OpenApi) -> Option<String> {
    for (route, item) in &doc.paths {
        for (method, op) in item.operations() {
            let Some(pagination) = op.pagination() else {
                continue;
            };
            let Some(property) = pagination
                .next_cursor_property()
                .or_else(|| pagination.results_property())
            else {
                continue;
            };
            let Some(reference) = op
                .responses
                .get("200")
                .and_then(|response| response.content.get("application/json"))
                .and_then(|media| media.schema.as_ref())
                .and_then(|schema| schema.reference.as_deref())
            else {
                continue;
            };
            let Some(name) = reference.strip_prefix("#/components/schemas/") else {
                continue;
            };
            if doc
                .components
                .schemas
                .get(name)
                .is_some_and(|schema| schema.nullable == Some(true))
            {
                return Some(format!(
                    "{method} {route} pagination reads $response.{property} off nullable {name}"
                ));
            }
        }
    }
    None
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
        let doc: OpenApi = crate::yaml::from_str(&spec).unwrap();
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

    /// The extension element `cyclic_extension` refuses among `schemas`, or `None`.
    fn extension_cycle(schemas: serde_json::Value) -> Option<String> {
        let root = serde_json::json!({"components": {"schemas": schemas}});
        cyclic_extension(&root, &root, "", &mut ExtensionCycles::default(), false)
    }

    #[test]
    fn an_extension_reaching_its_reference_through_an_array_is_no_cycle() {
        let node = serde_json::json!({"$ref": "#/components/schemas/Node"});
        // Stripe's expandable field: a string-or-object union whose
        // `x-expansionResources` lists the object it expands to.
        let expandable = serde_json::json!({"Node": {"type": "object", "properties": {"parent": {
            "anyOf": [{"type": "string"}, node],
            "x-expansionResources": {"oneOf": [node]},
        }}}});
        assert_eq!(extension_cycle(expandable), None);
        let root = serde_json::json!({"Node": {
            "type": "object",
            "x-link": {"oneOf": [node]},
            "properties": {"id": {"type": "string"}},
        }});
        assert_eq!(extension_cycle(root), None);
        // Through an object member the same field still cycles, union or not.
        let member = serde_json::json!({"Node": {"type": "object", "properties": {"parent": {
            "anyOf": [{"type": "string"}, node],
            "x-link": {"target": node},
        }}}});
        assert_eq!(
            extension_cycle(member).as_deref(),
            Some("components/schemas/Node/properties/parent/x-link")
        );
    }

    /// `check_document_schemas`'s verdict on `schemas`, as the refusal line it prints.
    fn schema_refusal(schemas: serde_json::Value) -> Option<String> {
        let root = serde_json::json!({
            "openapi": "3.1.0",
            "info": {"title": "t", "version": "1"},
            "paths": {},
            "components": {"schemas": schemas},
        });
        check_document_schemas(&root, Path::new("api.yml"), false)
            .err()
            .map(|error| error.to_string())
    }

    #[test]
    fn a_named_default_refuses_string_enums_and_consts_but_not_booleans() {
        // `ticket.type`'s inline schema is named `TicketType`, as `ticket_type` is.
        let collision = |property: serde_json::Value| {
            schema_refusal(serde_json::json!({
                "ticket": {"type": "object", "properties": {"type": property}},
                "ticket_type": {"type": "object", "properties": {"id": {"type": "string"}}},
            }))
        };
        for refused in [
            serde_json::json!({"type": "string", "enum": ["ticket"], "default": "ticket"}),
            serde_json::json!({"type": "string", "const": "ticket", "default": "ticket"}),
        ] {
            let error = collision(refused.clone()).unwrap_or_default();
            assert!(
                error.contains(
                    "named-type-default: components/schemas/ticket/properties/type/default"
                ),
                "{refused}: {error}"
            );
        }
        for generated in [
            serde_json::json!({"type": "boolean", "const": false, "default": false}),
            serde_json::json!({"type": "boolean", "enum": [false], "default": false}),
            serde_json::json!({"const": true, "default": true}),
            serde_json::json!({"type": "string", "enum": ["ticket"]}),
        ] {
            assert_eq!(collision(generated.clone()), None, "{generated}");
        }
    }

    #[test]
    fn a_union_recursing_through_component_defs_is_no_expanding_cycle() {
        let json_value = serde_json::json!({
            "anyOf": [
                {"type": "string"},
                {"type": "null"},
                {"type": "array", "items": {"$ref": "#/components/schemas/Call/$defs/value"}},
                {"type": "object", "additionalProperties": {"$ref": "#/components/schemas/Call/$defs/value"}},
            ]
        });
        assert_eq!(
            schema_refusal(serde_json::json!({"Call": {
                "type": "object",
                "properties": {"arguments": {"$ref": "#/components/schemas/Call/$defs/value"}},
                "$defs": {"value": json_value},
            }})),
            None
        );
        // The same union reached through a property pointer still expands, one
        // longer name a turn.
        let error = schema_refusal(serde_json::json!({"Tool": {
            "type": "object",
            "properties": {"composition": {"anyOf": [
                {"type": "object", "properties": {
                    "child": {"$ref": "#/components/schemas/Tool/properties/composition"},
                }},
                {"type": "string"},
            ]}},
        }}))
        .unwrap_or_default();
        assert!(
            error.contains(
                "generated-file-name-too-long: components/schemas/Tool/properties/composition"
            ),
            "{error}"
        );
    }

    /// `count` components, each with a property per component that is either a
    /// string or a reference to it: every component reaches every other, so a
    /// search over each path between them never finishes.
    fn densely_recursive(count: usize) -> serde_json::Value {
        let mut schemas = serde_json::Map::new();
        for index in 0..count {
            let properties: serde_json::Map<String, serde_json::Value> = (0..count)
                .map(|other| {
                    let reference = format!("#/components/schemas/S{other}");
                    (
                        format!("p{other}"),
                        serde_json::json!({"anyOf": [{"type": "string"}, {"$ref": reference}]}),
                    )
                })
                .collect();
            schemas.insert(
                format!("S{index}"),
                serde_json::json!({"type": "object", "properties": properties}),
            );
        }
        serde_json::Value::Object(schemas)
    }

    #[test]
    fn an_object_extends_a_union_of_objects_or_aliases_one_member_but_no_scalar() {
        let class = Path::new(env!("CARGO_MANIFEST_DIR"))
            .join("docs/fern-refusals/object-extends-non-object");
        let mut shapes: Vec<String> = std::fs::read_dir(&class)
            .unwrap()
            .filter_map(|entry| entry.ok()?.file_name().into_string().ok())
            .filter(|name| {
                name == "probe.yml" || name.contains("-probe.") || name.contains("-control.")
            })
            .collect();
        shapes.sort();
        for measured in [
            "union-base-control.yml",
            "nested-union-base-control.yml",
            "untyped-ref-union-base-control.yml",
            "anyof-ref-union-base-control.yml",
            "scalar-member-union-base-control.yml",
            "conditional-base-control.yml",
            "typed-scalar-alias-control.yml",
            "typed-nullable-scalar-alias-control.yml",
        ] {
            assert!(shapes.iter().any(|shape| shape == measured), "{measured}");
        }
        for shape in shapes {
            let error = registry_shape_refusal(&format!("object-extends-non-object/{shape}"));
            let refused = error
                .as_deref()
                .is_some_and(|error| error.contains("object-extends-non-object: "));
            assert_eq!(refused, !shape.contains("-control."), "{shape}: {error:?}");
        }
    }

    /// `check_sdk`'s refusal over `spec`, or `None`.
    fn sdk_refusal(spec: &str) -> Option<String> {
        let mut doc: OpenApi = crate::yaml::from_str(spec).unwrap();
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
        let ir = crate::ir::build(&doc, &config);
        check_sdk(&mut doc, &ir, &config, Path::new("openapi.yml"), true)
            .err()
            .map(|error| error.to_string())
    }

    #[test]
    fn a_sub_client_led_by_a_digit_is_a_lint_failure() {
        let spec = |tag: &str| {
            format!(
                "openapi: 3.0.3\ninfo: {{title: Api, version: '1'}}\npaths:\n  /rules:\n    get:\n      \
                 tags: ['{tag}']\n      operationId: listRules\n      responses: {{'204': {{description: OK}}}}\n"
            )
        };
        let error = sdk_refusal(&spec("3DS Decision Rule")).unwrap_or_default();
        assert!(
            error.contains(
                "generator-lint-failure: sub-client _3ds_decision_rule class 3DsDecisionRuleClient"
            ),
            "{error}"
        );
        assert_eq!(sdk_refusal(&spec("Decision Rule 3DS")), None);
    }

    #[test]
    fn a_densely_recursive_union_document_is_decided_once() {
        // Stripe's expandable fields: every object reaches every other through a
        // string-or-object union, with no turn that grows.
        assert_eq!(schema_refusal(densely_recursive(40)), None);
        // One pointer partway into a component makes a turn through it grow,
        // lengthening each turn's name; a second branches the expansion.
        let mut schemas = densely_recursive(40);
        schemas["S7"]["properties"]["deep"] =
            serde_json::json!({"$ref": "#/components/schemas/S3/properties/p7"});
        let error = schema_refusal(schemas.clone()).unwrap_or_default();
        assert!(error.contains("generated-file-name-too-long: "), "{error}");
        schemas["S9"]["properties"]["deep"] =
            serde_json::json!({"$ref": "#/components/schemas/S5/properties/p9"});
        let error = schema_refusal(schemas).unwrap_or_default();
        assert!(error.contains("heap-exhausted: "), "{error}");
    }

    #[test]
    fn a_cycle_grows_through_a_partial_pointer_or_an_extended_union_base() {
        // The class each shape's Fern measurement names, or `None` for a control.
        for (shape, class) in [
            ("probe.yml", Some("heap-exhausted")),
            (
                "single-child-probe.yml",
                Some("generated-file-name-too-long"),
            ),
            (
                "recursive-union-allof-probe.json",
                Some("generated-file-name-too-long"),
            ),
            ("defs-json-value-control.yml", None),
            ("named-binary-recursion-control.json", None),
            ("named-object-recursion-control.yml", None),
            ("nonrecursive-union-control.yml", None),
            ("nullable-union-alias-control.yml", None),
        ] {
            let error = registry_shape_refusal(&format!("heap-exhausted/{shape}"));
            match class {
                Some(class) => assert!(
                    error
                        .as_deref()
                        .is_some_and(|error| error.contains(&format!("{class}: "))),
                    "{shape}: {error:?}"
                ),
                None => assert_eq!(error, None, "{shape}"),
            }
        }
    }

    /// `check_structure_file`'s and `check_document`'s refusal over a committed
    /// registry shape, or `None` when it passes both.
    fn registry_shape_refusal(shape: &str) -> Option<String> {
        let path = Path::new(env!("CARGO_MANIFEST_DIR"))
            .join("docs/fern-refusals")
            .join(shape);
        let root: serde_json::Value =
            crate::yaml::from_str(&std::fs::read_to_string(&path).unwrap()).unwrap();
        check_structure_file(&path, false)
            .and_then(|()| check_document_schemas(&root, &path, false))
            .and_then(|()| check_example_names(&root, &path, false))
            .err()
            .map(|error| error.to_string())
    }

    #[test]
    fn a_required_reference_to_a_nullable_definition_is_resolved() {
        for control in [
            "defs-nullable-target-control.yml",
            "definitions-nullable-target-control.yml",
        ] {
            assert_eq!(
                registry_shape_refusal(&format!("unresolved-schema-reference/{control}")),
                None,
                "{control}"
            );
        }
        let error = registry_shape_refusal("unresolved-schema-reference/deep-defs-field-probe.yml")
            .unwrap_or_default();
        assert!(
            error.contains("unresolved-schema-reference: paths//contacts/post/requestBody"),
            "{error}"
        );
    }

    #[test]
    fn a_union_mapping_every_value_to_itself_leaves_fern_no_variant() {
        let error = registry_shape_refusal("missing-discriminant-property/self-mapped-probe.yml")
            .unwrap_or_default();
        assert!(
            error.contains(
                "missing-discriminant-property: POST /firings request \
                 components/schemas/FiringStep discriminator phase"
            ),
            "{error}"
        );
        // One subtype beside the self mapping, first or second, is Fern's example.
        for control in [
            "self-mapped-first-control.yml",
            "self-mapped-second-control.yml",
        ] {
            assert_eq!(
                registry_shape_refusal(&format!("missing-discriminant-property/{control}")),
                None,
                "{control}"
            );
        }
    }

    #[test]
    fn a_success_response_follows_its_response_components_reference() {
        let error = registry_shape_refusal("unresolved-reference/response-fragment-probe.yml")
            .unwrap_or_default();
        assert!(
            error.contains("unresolved-reference: components/responses/Empty: #/x-fragment/base"),
            "{error}"
        );
        assert_eq!(
            registry_shape_refusal("unresolved-reference/response-fragment-default-control.yml"),
            None
        );
    }

    #[test]
    fn a_non_string_request_example_summary_is_refused_after_duplicate_names() {
        let error =
            registry_shape_refusal("example-summary-not-string/probe.yml").unwrap_or_default();
        assert!(
            error.contains(
                "example-summary-not-string: POST /notes request example first summary 1"
            ),
            "{error}"
        );
        assert_eq!(
            registry_shape_refusal("example-summary-not-string/string-summary-control.yml"),
            None
        );
        // Two numeric summaries that match are the duplicate Fern's check reports first.
        let error = registry_shape_refusal("duplicate-example-name/numeric-summaries-probe.yml")
            .unwrap_or_default();
        assert!(error.contains("duplicate-example-name"), "{error}");
    }

    #[test]
    fn a_string_or_untyped_enum_with_no_non_null_value_is_a_lint_failure() {
        for probe in [
            "inline-null-only-enum-probe.yml",
            "untyped-null-only-enum-probe.yml",
        ] {
            let error = registry_shape_refusal(&format!("generator-lint-failure/{probe}"))
                .unwrap_or_default();
            assert!(
                error.contains("generator-lint-failure")
                    && error.contains("enum has no non-null value"),
                "{probe}: {error}"
            );
        }
        assert_eq!(
            registry_shape_refusal("generator-lint-failure/null-and-value-enum-control.yml"),
            None
        );
    }

    #[test]
    fn an_inline_header_enum_with_a_default_is_declared() {
        for control in [
            "two-values-default-control.yml",
            "optional-default-control.yml",
            "singleton-default-control.yml",
        ] {
            assert_eq!(
                registry_shape_refusal(&format!("generator-missing-type/{control}")),
                None,
                "{control}"
            );
        }
        let error = registry_shape_refusal("generator-missing-type/optional-two-values-probe.yml")
            .unwrap_or_default();
        assert!(error.contains("generator-missing-type"), "{error}");
    }

    #[test]
    fn a_pagination_contract_over_a_nullable_response_is_refused() {
        let doc = |nullable: bool| -> OpenApi {
            serde_json::from_value(serde_json::json!({
                "openapi": "3.0.3",
                "paths": {"/jobs": {"get": {
                    "x-fern-pagination": {"offset": "$request.page", "results": "$response.jobs"},
                    "responses": {"200": {"description": "ok", "content": {"application/json": {
                        "schema": {"$ref": "#/components/schemas/JobPage"}}}}},
                }}},
                "components": {"schemas": {"JobPage": {"type": "object", "nullable": nullable}}},
            }))
            .unwrap()
        };
        assert_eq!(
            paginated_nullable_response(&doc(true)).as_deref(),
            Some("GET /jobs pagination reads $response.jobs off nullable JobPage")
        );
        assert_eq!(paginated_nullable_response(&doc(false)), None);
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
        let root =
            crate::yaml::from_str("paths: {'/probe': {get: {parameters: [{name: id}]}}}").unwrap();
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
        crate::yaml::from_str(&format!(
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
        let bearer = crate::yaml::from_str("type: http\nscheme: bearer").unwrap();
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

    #[test]
    fn a_server_placeholder_no_variable_binds_is_not_refused() {
        let check = |variable: &str| {
            let mut doc: OpenApi = crate::yaml::from_str(&format!(
                "openapi: 3.0.3\nservers:\n  - url: https://{{extra}}.example.com/{{version}}\n    variables:\n      {variable}: {{default: v1}}\npaths:\n{OP}\n"
            ))
            .unwrap();
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
            assert!(ir.environment.is_some());
            check_sdk(&mut doc, &ir, &config, Path::new("api.yml"), true)
        };
        // `{extra}` is formatted through `_url_template`, which ruff's F524
        // cannot read, so Fern generates.
        assert!(check("version").is_ok());
        // A variable that is no keyword argument is still a syntax error.
        let error = check("api-version").unwrap_err().to_string();
        assert!(error.contains("variable \"api-version\""), "{error}");
    }

    fn example_name_refusal(document: &str) -> Option<String> {
        let root: serde_json::Value = crate::yaml::from_str(document).unwrap();
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
            let root: serde_json::Value = crate::yaml::from_str(&document).unwrap();
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
