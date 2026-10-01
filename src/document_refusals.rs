//! Structural refusals for the document-family Fern registry.
//!
//! These checks decide whether generation is allowed; they never rewrite the
//! document or repair the output measured in `docs/fern-refusals/`.

use std::path::Path;

use crate::openapi::{HttpAuthScheme, OpenApi, ParameterLocation, SecuritySchemeType};
use crate::{Error, Result};

#[derive(Clone, Copy)]
enum Class {
    UnsupportedOpenapiVersion,
    ServiceAuthUndefined,
    EndpointAuthUndefined,
    UnresolvedReference,
    PathWithoutLeadingSlash,
    PathParameterUnreferenced,
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

/// Inspect Reference Objects before normalization can replace or discard them.
/// Schema and Path Item references have separate Fern behavior and are excluded.
pub fn check_reference_file(path: &Path, strict: bool) -> Result<()> {
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
    if let Some(components) = root.get("components") {
        for name in [
            "securitySchemes",
            "responses",
            "requestBodies",
            "parameters",
            "headers",
        ] {
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
                    !reference.starts_with("#/components/parameters/")
                        && (expected.is_some_and(|kind| {
                            !reference.starts_with(&format!("#/components/{kind}/"))
                        }) || yaml_pointer(root, pointer).is_none())
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

/// Reject an evaluated class before rendering or writing an SDK.
pub fn check(doc: &OpenApi, path: &Path, strict: bool) -> Result<()> {
    check_version(&doc.openapi, path, strict)?;
    // The imported_auth_agrees_with_sdk_ir test reconciles this predicate with the actual importer.
    let imported_auth = doc.components.security_schemes.values().any(|scheme| {
        (scheme.ty == SecuritySchemeType::ApiKey
            && scheme.location == Some(ParameterLocation::Header))
            || (scheme.ty == SecuritySchemeType::Http
                && matches!(
                    scheme.scheme,
                    Some(HttpAuthScheme::Bearer | HttpAuthScheme::Basic)
                ))
            || matches!(
                scheme.ty,
                SecuritySchemeType::OAuth2 | SecuritySchemeType::OpenIdConnect
            )
    });
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
            check_reference_file(&file, true).unwrap();
        }
        std::fs::write(&file, "components: {securitySchemes: {Bearer: {x-crozier-ignore: false, x-fern-ignore: true, $ref: 'absent.yml#/Bearer'}}}").unwrap();
        let error = check_reference_file(&file, true).unwrap_err().to_string();
        assert!(error.contains("unresolved-reference: components/securitySchemes/Bearer"));
        assert!(error.contains("fern-strict"));
        std::fs::write(
            dir.path().join("absent.yml"),
            "Bearer: {type: http, scheme: bearer}",
        )
        .unwrap();
        check_reference_file(&file, false).unwrap();
        std::fs::write(&file, "paths: {/probe: {get: {responses: {401: {$ref: '#/$defs/Denied'}}}}}\n$defs: {Denied: {description: Unauthorized}}\ncomponents: {schemas: {Bound: {maximum: 18446744073709552000}}}").unwrap();
        let error = check_reference_file(&file, false).unwrap_err().to_string();
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
}
