//! The worked-example values crozier keeps where the certified pair discards a
//! value the API's author declared for a placeholder of its own. Each rule is
//! one `kind: usefulness` entry the 2026-11-01 design review grants:
//!
//! - `declared-example-over-placeholder` (ruling 2, `falsy-property-example`,
//!   and its principle): a parameter's falsy example, a multipart form part's or a header parameter's
//!   declared example, a binary download's query parameter example, a path
//!   parameter's example on an operation whose other path parameter declares an
//!   empty schema, and an enum's declared example member.
//! - `unquoted-timestamp-parameter-example` (ruling 3,
//!   `yaml-timestamp-parameter-example`): a parameter example YAML reads as a
//!   timestamp.
//! - `declared-examples-array-parameter-value` (ruling 5,
//!   `declared-examples-array`): a parameter's value from its schema's
//!   `examples` array or its own `examples` map.
//!
//! Every rule checks the source document, so a value is admitted only where the
//! document declares exactly the value crozier writes for that argument.

use super::{argument_names, example_file, keyword_argument_line, source_operations, Pair};
use crate::openapi::{OpenApi, Operation, Parameter, ParameterLocation, Schema};
use serde_json::Value;

/// Fern's date-time placeholder as a worked call writes it.
const FERN_DATETIME: &str = "datetime.datetime.fromisoformat(\"2024-01-15T09:30:00+00:00\")";
/// The same placeholder as a wrapped docstring call's string line.
const FERN_DATETIME_WRAPPED: &str = "\"2024-01-15 09:30:00+00:00\",";

/// Whether `value` is the placeholder the certified pair writes for an argument
/// whose wire name is `wire`: the wire name itself, or a numeric placeholder.
fn placeholder_for(wire: &str, value: &str) -> bool {
    value == format!("{wire:?}") || matches!(value, "1" | "1000000" | "1.1" | "True")
}

/// A schema declaring nothing at all (`schema: {}`).
fn empty_schema(schema: &Schema) -> bool {
    schema.ty.is_none()
        && schema.reference.is_none()
        && schema.format.is_none()
        && schema.properties.is_empty()
        && schema.items.is_none()
        && schema.all_of.is_none()
        && schema.one_of.is_none()
        && schema.any_of.is_none()
        && schema.enum_values.is_none()
        && schema.const_value.is_none()
}

/// Whether every successful response with content answers something other than
/// JSON (a binary download, a text answer).
fn non_json_success(operation: &Operation) -> bool {
    let mut media = operation
        .responses
        .iter()
        .filter(|(status, _)| status.starts_with('2'))
        .flat_map(|(_, response)| response.content.keys())
        .peekable();
    media.peek().is_some() && media.all(|media| !crate::ir::is_json_like_media_type(media))
}

fn resolve<'a>(source: &'a OpenApi, schema: &'a Schema) -> &'a Schema {
    schema
        .reference
        .as_deref()
        .and_then(|reference| reference.strip_prefix("#/components/schemas/"))
        .and_then(|name| source.components.schemas.get(name))
        .unwrap_or(schema)
}

/// Whether `keyword` is the argument a parameter is passed as.
fn parameter_keyword(parameter: &Parameter, keyword: &str) -> bool {
    argument_names(&parameter.name, keyword)
        || (parameter.location == Some(ParameterLocation::Header)
            && argument_names(crate::ir::header_param_stem(&parameter.name), keyword))
}

/// One argument whose declared value a rule admits: its wire name and the value
/// the document declares for it.
struct Declared<'a> {
    wire: &'a str,
    value: &'a Value,
}

/// The declared values ruling 2 and its principle keep (see the module docs).
fn kept_declared_values(source: &OpenApi) -> Vec<Declared<'_>> {
    let mut out = Vec::new();
    for (operation, parameters) in source_operations(source) {
        let empty_path_schema = parameters.iter().any(|parameter| {
            parameter.location == Some(ParameterLocation::Path)
                && parameter.schema.as_ref().is_some_and(empty_schema)
        });
        let binary = non_json_success(operation);
        for parameter in &parameters {
            let Some(value) = parameter.example.as_ref() else {
                continue;
            };
            // Ruling 2 itself names a falsy example (`""`, `0`) on any argument.
            let falsy = value.as_str() == Some("")
                || value.as_i64() == Some(0)
                || value.as_f64() == Some(0.0);
            let kept = falsy
                || match parameter.location {
                    Some(ParameterLocation::Header) => true,
                    Some(ParameterLocation::Query) => binary,
                    Some(ParameterLocation::Path) => empty_path_schema,
                    _ => false,
                };
            if kept {
                out.push(Declared {
                    wire: &parameter.name,
                    value,
                });
            }
        }
        let Some(body) = operation.request_body.as_ref() else {
            continue;
        };
        for (media, content) in &body.content {
            if !media.starts_with("multipart/form-data") {
                continue;
            }
            let Some(schema) = content.schema.as_ref() else {
                continue;
            };
            for (wire, property) in &resolve(source, schema).properties {
                if let Some(value) = resolve(source, property).example.as_ref() {
                    out.push(Declared { wire, value });
                }
            }
        }
    }
    out
}

/// `declared-example-over-placeholder`: a worked-example argument line where
/// Fern writes its placeholder and crozier the value ruling 2 keeps.
pub(super) fn declared_example_over_placeholder(
    pair: &Pair<'_>,
    fern: &str,
    crozier: &str,
) -> bool {
    if !example_file(pair.rel) {
        return false;
    }
    if declared_enum_member(pair, fern, crozier) {
        return true;
    }
    let (Some((fern_indent, fern_name, fern_value)), Some((indent, name, value))) =
        (keyword_argument_line(fern), keyword_argument_line(crozier))
    else {
        return false;
    };
    if fern_indent != indent || fern_name != name || fern_value == value {
        return false;
    }
    let Some(source) = pair.context.source_document.as_ref() else {
        return false;
    };
    kept_declared_values(source).iter().any(|declared| {
        argument_names(declared.wire, name)
            || argument_names(crate::ir::header_param_stem(declared.wire), name)
    } && placeholder_for(declared.wire, fern_value)
        && crate::ir::example_literal(declared.value).as_deref() == Some(value))
}

/// The enum schemas declaring an `example` other than their first member: the
/// class name, the first value and the declared one.
fn enum_examples(source: &OpenApi) -> Vec<(String, &str, &str)> {
    source
        .components
        .schemas
        .iter()
        .filter_map(|(name, schema)| {
            let values = schema.enum_values.as_ref()?;
            let first = values.first()?.as_str()?;
            let declared = schema.example.as_ref()?.as_str()?;
            (declared != first && values.iter().any(|value| value.as_str() == Some(declared)))
                .then(|| (crate::naming::class_name(name), first, declared))
        })
        .collect()
}

/// The enum half of `declared-example-over-placeholder` (example-enum-member,
/// ruling 2's principle): a list item naming an enum's first member where
/// crozier names the member its schema declares as its example, in either enum
/// mode, on its own line or as a one-line `<name>=[<item>],`.
fn declared_enum_member(pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    let Some(source) = pair.context.source_document.as_ref() else {
        return false;
    };
    let strip = |line: &str| -> Option<(String, String)> {
        let trimmed = line.trim_start();
        let indent = line[..line.len() - trimmed.len()].to_string();
        if let Some((name, value)) = trimmed
            .strip_suffix("],")
            .and_then(|rest| rest.split_once("=["))
        {
            return Some((format!("{indent}{name}"), value.to_string()));
        }
        Some((indent, trimmed.trim_end_matches(',').to_string()))
    };
    let (Some((fern_prefix, fern_item)), Some((prefix, item))) = (strip(fern), strip(crozier))
    else {
        return false;
    };
    fern_prefix == prefix
        && enum_examples(source)
            .iter()
            .any(|(class, first, declared)| {
                let member = |value: &str| crate::naming::enum_member_name(value);
                (fern_item == format!("{class}.{}", member(first))
                    && item == format!("{class}.{}", member(declared)))
                    || (fern_item == format!("{first:?}") && item == format!("{declared:?}"))
            })
}

/// A parameter's declared values that YAML reads as timestamps: its own
/// `example`, else its (referenced) schema's `example` or first `examples`
/// entry, each only where the document writes it unquoted.
fn unquoted_timestamps<'a>(source: &'a OpenApi, parameter: &'a Parameter) -> Option<&'a str> {
    let unquoted = source.yaml_unquoted_timestamps.as_ref()?;
    let declared = parameter.example.as_ref().or_else(|| {
        let schema = resolve(source, parameter.schema.as_ref()?);
        schema.example.as_ref().or_else(|| schema.examples.first())
    })?;
    declared
        .as_str()
        .filter(|value| unquoted.contains(*value))
        .filter(|value| crate::emit::yaml_resolves_as_timestamp(value))
}

/// The ways crozier writes the declared timestamp `value`: a string argument,
/// a one-line `fromisoformat` call, and the string line of a wrapped one.
fn timestamp_spellings(value: &str) -> [String; 3] {
    let iso = crate::emit::datetime_example(value);
    [
        format!("{value:?}"),
        format!("datetime.datetime.fromisoformat({iso:?})"),
        format!("{:?},", iso.replacen('T', " ", 1)),
    ]
}

/// Every parameter carrying an unquoted timestamp example, with it.
fn timestamp_parameters(source: &OpenApi) -> Vec<(&Parameter, &str)> {
    source_operations(source)
        .flat_map(|(_, parameters)| parameters)
        .filter_map(|parameter| Some((parameter, unquoted_timestamps(source, parameter)?)))
        .collect()
}

/// `unquoted-timestamp-parameter-example`: Fern's placeholder line beside
/// crozier's line passing the timestamp the document declares.
pub(super) fn unquoted_timestamp_parameter_example(
    pair: &Pair<'_>,
    fern: &str,
    crozier: &str,
) -> bool {
    if !example_file(pair.rel) {
        return false;
    }
    let Some(source) = pair.context.source_document.as_ref() else {
        return false;
    };
    let parameters = timestamp_parameters(source);
    // The string line of a wrapped `fromisoformat` call.
    if fern.trim_start() == FERN_DATETIME_WRAPPED {
        let indent = &fern[..fern.len() - fern.trim_start().len()];
        return parameters
            .iter()
            .any(|(_, value)| crozier == format!("{indent}{}", timestamp_spellings(value)[2]));
    }
    let (Some((fern_indent, fern_name, fern_value)), Some((indent, name, value))) =
        (keyword_argument_line(fern), keyword_argument_line(crozier))
    else {
        return false;
    };
    if fern_indent != indent || fern_name != name || fern_value == value {
        return false;
    }
    parameters.iter().any(|(parameter, declared)| {
        parameter_keyword(parameter, name)
            && (fern_value == FERN_DATETIME || fern_value == format!("{:?}", parameter.name))
            && timestamp_spellings(declared)[..2]
                .iter()
                .any(|spelled| spelled == value)
    })
}

/// The lines only crozier writes for an optional parameter whose timestamp
/// example Fern drops: `<name>=<value>,`, the three lines of a wrapped
/// `fromisoformat` call, and the `import datetime` it needs.
pub(super) fn unquoted_timestamp_parameter_line(pair: &Pair<'_>, at: usize) -> bool {
    if !example_file(pair.rel) {
        return false;
    }
    let Some(source) = pair.context.source_document.as_ref() else {
        return false;
    };
    let optional: Vec<_> = timestamp_parameters(source)
        .into_iter()
        .filter(|(parameter, _)| parameter.required != Some(true))
        .collect();
    let lines = pair.crozier;
    let Some(line) = lines.get(at) else {
        return false;
    };
    let passes = |index: usize| -> bool {
        let Some(line) = lines.get(index) else {
            return false;
        };
        if let Some((_, name, value)) = keyword_argument_line(line) {
            return optional.iter().any(|(parameter, declared)| {
                parameter_keyword(parameter, name)
                    && timestamp_spellings(declared)[..2]
                        .iter()
                        .any(|spelled| spelled == value)
            });
        }
        // `<name>=datetime.datetime.fromisoformat(`, `"<iso>",`, `),`.
        let Some(name) = line
            .trim_start()
            .strip_suffix("=datetime.datetime.fromisoformat(")
        else {
            return false;
        };
        let indent = &line[..line.len() - line.trim_start().len()];
        optional.iter().any(|(parameter, declared)| {
            parameter_keyword(parameter, name)
                && lines.get(index + 1).is_some_and(|next| {
                    *next == format!("{indent}    {}", timestamp_spellings(declared)[2])
                })
                && lines.get(index + 2) == Some(&format!("{indent}),").as_str())
        })
    };
    if line.trim() == "import datetime" {
        // Needed only by a timestamp line this rule admits.
        return (0..lines.len()).any(|index| index != at && passes(index));
    }
    passes(at) || (at >= 1 && passes(at - 1)) || (at >= 2 && passes(at - 2))
}

/// The value ruling 5 keeps for a parameter: its (referenced) schema's first
/// `examples` entry where the schema declares no `example`, else the first value
/// of its own `examples` map.
fn examples_array_values(source: &OpenApi) -> Vec<(&Parameter, &Value)> {
    let mut out = Vec::new();
    for (_, parameters) in source_operations(source) {
        for parameter in parameters {
            let schema = parameter
                .schema
                .as_ref()
                .map(|schema| resolve(source, schema));
            if let Some(entry) = schema
                .filter(|schema| schema.example.is_none())
                .and_then(|schema| schema.examples.first())
            {
                out.push((parameter, entry));
            }
            if let Some(value) = parameter
                .examples
                .values()
                .find_map(|example| example.value.as_ref())
            {
                out.push((parameter, value));
            }
        }
    }
    out
}

/// `declared-examples-array-parameter-value`: Fern's placeholder, or its schema
/// `example`, beside crozier's value from the `examples` array or map.
pub(super) fn declared_examples_array_parameter_value(
    pair: &Pair<'_>,
    fern: &str,
    crozier: &str,
) -> bool {
    if !example_file(pair.rel) {
        return false;
    }
    let (Some((fern_indent, fern_name, fern_value)), Some((indent, name, value))) =
        (keyword_argument_line(fern), keyword_argument_line(crozier))
    else {
        return false;
    };
    if fern_indent != indent || fern_name != name || fern_value == value {
        return false;
    }
    let Some(source) = pair.context.source_document.as_ref() else {
        return false;
    };
    examples_array_values(source)
        .iter()
        .any(|(parameter, declared)| {
            let schema_example = parameter
                .schema
                .as_ref()
                .map(|schema| resolve(source, schema))
                .and_then(|schema| schema.example.as_ref())
                .and_then(crate::ir::example_literal);
            parameter_keyword(parameter, name)
                && (placeholder_for(&parameter.name, fern_value)
                    || schema_example.as_deref() == Some(fern_value))
                && crate::ir::example_literal(declared).as_deref() == Some(value)
        })
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::departures::Context;

    fn context(document: serde_json::Value) -> Context {
        with_source(serde_json::from_value(document).expect("a document"))
    }

    fn with_source(source: OpenApi) -> Context {
        Context::from_sources([], std::iter::empty()).with_source_document(source)
    }

    fn pair<'a>(rel: &'a str, crozier: &'a [&'a str], context: &'a Context) -> Pair<'a> {
        Pair {
            rel,
            fern: &[],
            crozier,
            context,
        }
    }

    #[test]
    fn a_multipart_part_and_header_example_is_kept_only_for_its_own_argument() {
        let context = context(
            serde_json::json!({"openapi": "3.0.3", "paths": {"/buoys/{item_id}": {"post": {
                "parameters": [{"name": "X-Survey-Ref", "in": "header", "required": true,
                    "schema": {"type": "string"}, "example": ""},
                    {"name": "item_id", "in": "path", "required": true,
                        "schema": {"type": "string"}, "example": ""}],
                "requestBody": {"content": {"multipart/form-data": {"schema": {"type": "object",
                    "properties": {"label": {"type": "string", "example": ""},
                        "depth_metres": {"type": "integer", "example": 0}}}}}},
                "responses": {}
            }}}}),
        );
        let rule = declared_example_over_placeholder;
        for rel in ["README.md", "reference.md", "src/fern/buoys/client.py"] {
            let pair = pair(rel, &[], &context);
            assert!(
                rule(&pair, "    item_id=\"item_id\",", "    item_id=\"\","),
                "{rel}"
            );
            assert!(
                rule(&pair, "    label=\"label\",", "    label=\"\","),
                "{rel}"
            );
            assert!(
                rule(&pair, "    depth_metres=1,", "    depth_metres=0,"),
                "{rel}"
            );
            assert!(
                rule(
                    &pair,
                    "    survey_ref=\"X-Survey-Ref\",",
                    "    survey_ref=\"\","
                ),
                "{rel}"
            );
        }
        let pair = pair("README.md", &[], &context);
        // Another value, another argument, Fern's line naming something else, a
        // raw client: no departure.
        assert!(!rule(&pair, "    label=\"label\",", "    label=\"x\","));
        assert!(!rule(&pair, "    title=\"title\",", "    title=\"\","));
        assert!(!rule(&pair, "    label=\"other\",", "    label=\"\","));
        assert!(!rule(
            &Pair {
                rel: "src/fern/buoys/raw_client.py",
                ..pair
            },
            "    label=\"label\",",
            "    label=\"\","
        ));
    }

    #[test]
    fn an_enum_example_member_is_kept_in_both_enum_modes() {
        let context = context(serde_json::json!({"openapi": "3.0.3", "paths": {},
            "components": {"schemas": {"AlertKind": {"type": "string", "example": "beacon_lit",
                "enum": ["*", "beacon_lit", "beacon_out"]}}}}));
        let pair = pair("reference.md", &[], &context);
        let rule = declared_example_over_placeholder;
        assert!(rule(
            &pair,
            "        AlertKind.ALL",
            "        AlertKind.BEACON_LIT"
        ));
        assert!(rule(
            &pair,
            "            kinds=[AlertKind.ALL],",
            "            kinds=[AlertKind.BEACON_LIT],"
        ));
        assert!(rule(&pair, "        \"*\"", "        \"beacon_lit\""));
        assert!(!rule(
            &pair,
            "        AlertKind.ALL",
            "        AlertKind.BEACON_OUT"
        ));
    }

    #[test]
    fn an_unquoted_timestamp_is_kept_on_one_line_wrapped_and_where_fern_omits_it() {
        let mut source: OpenApi = serde_json::from_value(serde_json::json!({"openapi": "3.1.0",
            "paths": {"/tides": {"get": {"parameters": [
                {"name": "since", "in": "query", "required": true,
                    "schema": {"type": "string", "format": "date-time"}, "example": "2031-04-02T08:15:00Z"},
                {"name": "until", "in": "query",
                    "schema": {"type": "string", "format": "date-time"}, "example": "2031-04-03T08:15:00Z"}],
                "responses": {}}}}}))
        .expect("a document");
        source.yaml_unquoted_timestamps = Some(
            ["2031-04-02T08:15:00Z", "2031-04-03T08:15:00Z"]
                .into_iter()
                .map(String::from)
                .collect(),
        );
        let context = with_source(source);
        let rule = unquoted_timestamp_parameter_example;
        let pair_at = pair("reference.md", &[], &context);
        assert!(rule(
            &pair_at,
            "    since=datetime.datetime.fromisoformat(\"2024-01-15T09:30:00+00:00\"),",
            "    since=datetime.datetime.fromisoformat(\"2031-04-02T08:15:00+00:00\"),"
        ));
        assert!(rule(
            &pair_at,
            "                \"2024-01-15 09:30:00+00:00\",",
            "                \"2031-04-02 08:15:00+00:00\","
        ));
        assert!(!rule(
            &pair_at,
            "    since=datetime.datetime.fromisoformat(\"2024-01-15T09:30:00+00:00\"),",
            "    since=datetime.datetime.fromisoformat(\"2031-04-09T08:15:00+00:00\"),"
        ));
        let lines = [
            "import datetime",
            "client.tides.list_tides(",
            "    until=datetime.datetime.fromisoformat(",
            "        \"2031-04-03 08:15:00+00:00\",",
            "    ),",
            ")",
        ];
        let added = pair("src/fern/tides/client.py", &lines, &context);
        for at in [0, 2, 3, 4] {
            assert!(unquoted_timestamp_parameter_line(&added, at), "{at}");
        }
        assert!(!unquoted_timestamp_parameter_line(&added, 1));
        // The required parameter's line is never one Fern omits.
        let required =
            ["    since=datetime.datetime.fromisoformat(\"2031-04-02T08:15:00+00:00\"),"];
        assert!(!unquoted_timestamp_parameter_line(
            &pair("README.md", &required, &context),
            0
        ));
    }

    #[test]
    fn an_examples_array_or_map_value_is_kept_for_its_parameter_only() {
        let context = context(serde_json::json!({"openapi": "3.1.0", "paths": {
            "/lamps/{lampId}": {"get": {"parameters": [
                {"name": "lampId", "in": "path", "required": true,
                    "schema": {"type": "string", "examples": ["lmp_8f2kq"]}}], "responses": {}}},
            "/keepers/{keeperId}": {"get": {"parameters": [
                {"name": "keeperId", "in": "path", "required": true,
                    "schema": {"type": "string", "example": "KPR-from-schema"},
                    "examples": {"first": {"value": "KPR-from-map"}}}], "responses": {}}}}}));
        let pair = pair("README.md", &[], &context);
        let rule = declared_examples_array_parameter_value;
        assert!(rule(
            &pair,
            "    lamp_id=\"lampId\",",
            "    lamp_id=\"lmp_8f2kq\","
        ));
        assert!(rule(
            &pair,
            "    keeper_id=\"KPR-from-schema\",",
            "    keeper_id=\"KPR-from-map\","
        ));
        assert!(!rule(
            &pair,
            "    lamp_id=\"lampId\",",
            "    lamp_id=\"other\","
        ));
        assert!(!rule(
            &pair,
            "    keeper_id=\"x\",",
            "    keeper_id=\"KPR-from-map\","
        ));
    }
}
