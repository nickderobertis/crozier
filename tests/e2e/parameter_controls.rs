// llmlint: ignore-file[new_code_lands_in_a_project] crozier is a Cargo/just repository with no Nx. This helper is compiled through #[path] into the e2e and generation Cargo test binaries, exercised by sdk_env_parameter_lifting_controls_reach_the_wire and parameter_lifting_controls_render_through_the_public_boundary.
//! Shared independently authored controls for the real CLI and library boundary.

pub const CASES: &[&str] = &[
    "promoted-header",
    "security-header",
    "missing-variable",
    "repeated-variable",
    "base-collision",
    "renamed-path",
];

pub fn document(case: &str) -> serde_json::Value {
    let source = match case {
        "promoted-header" | "security-header" => include_str!(
            "../../docs/openapi-surface/handwritten/observatory-client-headers/openapi.yml"
        ),
        "base-collision" => {
            include_str!("../../docs/openapi-surface/handwritten/observatory-base-path/openapi.yml")
        }
        _ => include_str!(
            "../../docs/openapi-surface/handwritten/observatory-client-variable/openapi.yml"
        ),
    };
    let mut doc: serde_json::Value = serde_json::from_str(source).unwrap();
    match case {
        "promoted-header" => {
            doc["paths"]["/signals"]["get"]["parameters"] = serde_json::json!([
                {"name": "X-Station", "in": "header", "required": true, "schema": {"type": "string"}}
            ]);
        }
        "security-header" => {
            doc["components"]["securitySchemes"] = serde_json::json!({
                "primary": {"type": "apiKey", "in": "header", "name": "X-Primary"},
                "station": {"type": "apiKey", "in": "header", "name": "X-Station"}
            });
            doc["security"] = serde_json::json!([{"primary": [], "station": []}]);
        }
        "missing-variable" | "renamed-path" => {
            doc.as_object_mut().unwrap().remove("x-fern-sdk-variables");
            if case == "renamed-path" {
                let parameter =
                    &mut doc["paths"]["/stations/{station_code}/signals"]["get"]["parameters"][0];
                parameter
                    .as_object_mut()
                    .unwrap()
                    .remove("x-fern-sdk-variable");
                parameter["x-fern-parameter-name"] = "areaCode".into();
            }
        }
        "repeated-variable" => {
            let mut item = doc["paths"]["/stations/{station_code}/signals"].clone();
            item["get"]["operationId"] = "listReadings".into();
            doc["paths"]["/stations/{station_code}/readings"] = item;
        }
        "base-collision" => {
            doc["x-fern-sdk-variables"] = serde_json::json!({"cycle": {"type": "string"}});
            doc["paths"]["/{cycle}/signals"]["get"]["parameters"][0]["x-fern-sdk-variable"] =
                "cycle".into();
        }
        _ => panic!("unknown parameter control {case}"),
    }
    doc
}
