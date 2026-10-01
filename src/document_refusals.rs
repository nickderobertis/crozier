//! Structural refusals for the document-family Fern registry.
//!
//! These checks decide whether generation is allowed; they never rewrite the
//! document or repair the output measured in `docs/fern-refusals/`.

use std::path::Path;

use crate::openapi::{HttpAuthScheme, OpenApi, ParameterLocation, SecuritySchemeType};
use crate::{Error, Result};

/// Reject an evaluated class before rendering or writing an SDK.
pub fn check(doc: &OpenApi, path: &Path, strict: bool) -> Result<()> {
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
    if let Some(requirements) = &doc.security {
        if !requirements.is_empty() {
            let scheme = requirements.iter().flat_map(|r| r.keys()).next();
            let element = scheme.map_or_else(|| "security/0".into(), |s| format!("security/{s}"));
            return refusal(path, strict, "service-auth-undefined", &element);
        }
    }
    for (route, item) in &doc.paths {
        for (method, op) in item.operations() {
            if let Some(requirements) = &op.security {
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
