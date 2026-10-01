//! Structural refusals for the document-family Fern registry.
//!
//! These checks decide whether generation is allowed; they never rewrite the
//! document or repair the output measured in `docs/fern-refusals/`.

use std::path::Path;

use crate::openapi::{HttpAuthScheme, OpenApi, ParameterLocation, SecuritySchemeType};
use crate::{Error, Result};

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

fn check_version(version: &str, path: &Path, strict: bool) -> Result<()> {
    if version.starts_with("3.") && !version.starts_with("3.0.") && !version.starts_with("3.1.") {
        return refusal(
            path,
            strict,
            "unsupported-openapi-version",
            &format!("openapi {version}"),
        );
    }
    Ok(())
}

/// Reject an evaluated class before rendering or writing an SDK.
pub fn check(doc: &OpenApi, path: &Path, strict: bool) -> Result<()> {
    check_version(&doc.openapi, path, strict)?;
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
            return refusal(path, strict, "service-auth-undefined", &element);
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
                    return refusal(path, strict, "endpoint-auth-undefined", &element);
                }
            }
        }
    }
    Ok(())
}

fn refusal(path: &Path, strict: bool, class: &str, element: &str) -> Result<()> {
    Err(Error::InvalidSpec {
        path: path.to_path_buf(),
        message: format!(
            "{class}: {element}{}",
            if strict { " (fern-strict refusal)" } else { "" }
        ),
    })
}

#[cfg(test)]
mod tests {
    use super::*;

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
