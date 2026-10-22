//! Conservative validation for declared examples retained in worked calls.

use crate::emit::DeclaredExampleMode;
use crate::openapi::example_validation::matches;
use crate::openapi::{OpenApi, Schema};
use serde_json::Value;

struct Substitution {
    keyword: String,
    values: crate::emit::DeclaredExampleSubstitution,
}

// The richer-content rule cannot justify values synthesized by the renderer.
// Restrict it to inline scalar/object examples whose written fields are complete.
fn renders_only_declared_values(source: &OpenApi, schema: &Schema, value: &Value) -> bool {
    if schema.reference.is_some()
        || schema.discriminator.is_some()
        || schema.type_crozier.is_some()
        || schema.type_fern.is_some()
        || schema.ignored()
        || value.is_null()
        || value.is_array()
    {
        return false;
    }
    if let Some(members) = &schema.one_of {
        return members.iter().any(|member| {
            matches(&source.components.schemas, member, value, 0) == Some(true)
                && renders_only_declared_values(source, member, value)
        });
    }
    if schema.all_of.is_some() || schema.any_of.is_some() {
        return false;
    }
    if let Some(fields) = value.as_object() {
        return fields.len() == schema.properties.len()
            && fields.iter().all(|(name, value)| {
                schema
                    .properties
                    .get(name)
                    .is_some_and(|property| renders_only_declared_values(source, property, value))
            });
    }
    true
}

fn substitutions(source: &OpenApi, rendering: DeclaredExampleMode) -> Vec<Substitution> {
    let Ok(mut config) = crate::config::GenerateConfig::new(
        std::path::PathBuf::new(),
        std::path::PathBuf::new(),
        Some("parity".into()),
        Some("parity".into()),
        Some("ParityClient".into()),
        crate::settings::ExtraFields::Allow,
        &source.info.title,
    ) else {
        return Vec::new();
    };
    let mut out = Vec::new();
    for mode in [
        crate::settings::EnumType::PythonEnums,
        crate::settings::EnumType::Literals,
    ] {
        config.enum_type = mode;
        let ir = crate::ir::build(source, &config);
        super::visit_source_schemas(Some(source), &mut |schema| {
            for (wire, property) in &schema.properties {
                let Some(key) = property
                    .reference
                    .as_deref()
                    .and_then(|reference| reference.strip_prefix("#/components/schemas/"))
                else {
                    continue;
                };
                let Some(target) = source.components.schemas.get(key) else {
                    continue;
                };
                let Some(example) = target.example.as_ref() else {
                    continue;
                };
                if !schema.required.contains(wire)
                    || property.example.is_some()
                    || target.one_of.is_none()
                    || matches(&source.components.schemas, target, example, 0) != Some(true)
                    || !renders_only_declared_values(source, target, example)
                {
                    continue;
                }
                let type_ref = crate::ir::TypeRef::Named(crate::naming::class_name(key));
                if let Some(values) =
                    crate::emit::declared_example_substitution(&ir, &type_ref, example, rendering)
                        .filter(|values| values.fallback != values.declared)
                {
                    out.push(Substitution {
                        keyword: crate::naming::model_field_name(wire),
                        values,
                    });
                }
            }
        });
    }
    out
}

fn example_blocks(lines: &[&str]) -> Vec<std::ops::Range<usize>> {
    let mut out = Vec::new();
    let mut index = 0;
    while index < lines.len() {
        let fenced = lines[index].trim() == "```python";
        let docstring = lines[index].trim() == "Examples"
            && lines
                .get(index + 1)
                .is_some_and(|line| line.trim() == "--------");
        if !fenced && !docstring {
            index += 1;
            continue;
        }
        let start = index + if fenced { 1 } else { 2 };
        let terminator = if fenced { "```" } else { "\"\"\"" };
        let Some(end) = (start..lines.len()).find(|position| lines[*position].trim() == terminator)
        else {
            break;
        };
        out.push(start..end);
        index = end + 1;
    }
    out
}

/// Ignore only formatter trailing commas, preserving quoted values and token order.
fn expression(text: &str) -> String {
    let compact = super::compact_python(&[text]);
    let mut chars = compact.chars().peekable();
    let mut quote = None;
    let mut escaped = false;
    let mut out = String::new();
    while let Some(character) = chars.next() {
        if let Some(delimiter) = quote {
            out.push(character);
            if escaped {
                escaped = false;
            } else if character == '\\' {
                escaped = true;
            } else if character == delimiter {
                quote = None;
            }
        } else if matches!(character, '\'' | '"') {
            quote = Some(character);
            out.push(character);
        } else if character != ','
            || !chars
                .peek()
                .is_some_and(|next| matches!(next, ')' | ']' | '}'))
        {
            out.push(character);
        }
    }
    out
}

struct Import {
    end: usize,
    prefix: String,
    module: String,
    names: Vec<String>,
}

fn import(lines: &[&str], start: usize) -> Option<Import> {
    let line = lines.get(start)?;
    let trimmed = line.trim_start();
    let (module, names) = trimmed.strip_prefix("from ")?.split_once(" import ")?;
    let end = if names.trim() == "(" {
        (start + 1..lines.len()).find(|position| lines[*position].trim() == ")")? + 1
    } else {
        start + 1
    };
    let names = if end == start + 1 {
        names.to_string()
    } else {
        lines[start + 1..end - 1].join("")
    };
    let names = names
        .split(',')
        .map(str::trim)
        .filter(|name| !name.is_empty())
        .map(str::to_string)
        .collect::<Vec<_>>();
    if names.iter().any(|name| !super::python_identifier(name)) {
        return None;
    }
    Some(Import {
        end,
        prefix: line[..line.len() - trimmed.len()].into(),
        module: module.into(),
        names,
    })
}

fn import_module(lines: &[&str], names: &std::collections::BTreeSet<String>) -> Option<String> {
    if names.is_empty() {
        return None;
    }
    (0..lines.len())
        .filter_map(|index| import(lines, index))
        .find(|item| names.iter().all(|name| item.names.contains(name)))
        .map(|item| item.module)
}

fn normalize_block(
    lines: &[&str],
    substitution: &Substitution,
    corrected: bool,
    module: &str,
) -> Option<Vec<String>> {
    let values = &substitution.values;
    let (value, imports) = if corrected {
        (&values.declared, &values.declared_imports)
    } else {
        (&values.fallback, &values.fallback_imports)
    };
    let wanted = expression(&format!("{}={value}", substitution.keyword));
    let mut out = Vec::new();
    let mut index = 0;
    let mut found = false;
    let mut found_import = imports.is_empty();
    while index < lines.len() {
        if let Some(item) = import(lines, index).filter(|item| item.module == module) {
            if !imports.iter().all(|name| item.names.contains(name)) {
                return None;
            }
            let kept = item
                .names
                .iter()
                .filter(|name| !imports.contains(*name))
                .cloned()
                .collect::<Vec<_>>();
            out.push(format!(
                "{}from {module} import {}",
                item.prefix,
                kept.join(", ")
            ));
            found_import = true;
            index = item.end;
            continue;
        }
        if lines[index]
            .trim_start()
            .starts_with(&format!("{}=", substitution.keyword))
        {
            if found {
                return None;
            }
            let end = (index + 1..=lines.len().min(index + 64)).find(|end| {
                let text = lines[index..*end].join("\n");
                expression(text.trim_end().trim_end_matches(',')) == wanted
            })?;
            let indent = lines[index].len() - lines[index].trim_start().len();
            out.push(format!(
                "{}{}=<declared-example>",
                " ".repeat(indent),
                substitution.keyword
            ));
            found = true;
            index = end;
        } else {
            out.push(lines[index].to_string());
            index += 1;
        }
    }
    (found && found_import).then_some(out)
}

/// One verified example block, leaving every adjacent example and byte intact.
pub(super) fn region(pair: &super::Pair<'_>) -> Result<Option<super::Region>, String> {
    if !super::example_file(pair.rel) {
        return Ok(None);
    }
    let Some(source) = pair.context.source_document.as_ref() else {
        return Ok(None);
    };
    let rendering = if pair.rel == "reference.md" {
        DeclaredExampleMode::Reference
    } else if pair.rel.ends_with(".py") {
        DeclaredExampleMode::Docstring
    } else {
        DeclaredExampleMode::Readme
    };
    let candidates = substitutions(source, rendering);
    let before = example_blocks(pair.fern);
    let after = example_blocks(pair.crozier);
    if before.len() != after.len() {
        return Ok(None);
    }
    for (fern, crozier) in before.into_iter().zip(after) {
        let a = &pair.fern[fern.clone()];
        let b = &pair.crozier[crozier.clone()];
        if a == b {
            continue;
        }
        for candidate in &candidates {
            let module = import_module(a, &candidate.values.fallback_imports)
                .or_else(|| import_module(b, &candidate.values.declared_imports));
            let Some(module) = module else {
                continue;
            };
            if let (Some(reference), Some(corrected)) = (
                normalize_block(a, candidate, false, &module),
                normalize_block(b, candidate, true, &module),
            ) {
                if reference == corrected {
                    return Ok(Some(super::Region { fern, crozier }));
                }
            }
        }
    }
    Ok(None)
}

#[cfg(test)]
mod tests {
    use super::*;

    fn source(extra: Value, example: Value) -> OpenApi {
        let mut document = serde_json::json!({
            "openapi":"3.1.0", "info":{"title":"Harbor windows","version":"1"},
            "paths":{"/windows":{"post":{"operationId":"schedule", "requestBody":{
                "content":{"application/json":{"schema":{"$ref":"#/components/schemas/Plan"}}}},
                "responses":{"204":{"description":"Scheduled"}}}}},
            "components":{"schemas":{
                "Plan":{"type":"object","required":["choice"],"properties":{
                    "choice":{"$ref":"#/components/schemas/Choice"}}},
                "Choice":{"oneOf":[{"type":"string","enum":["North"]},
                    {"type":"object","required":["Window"],"properties":{
                        "Window":{"type":"object","required":["lookback"],"properties":{
                            "lookback":{"type":"integer"}}}}}],"example":example}
            }}
        });
        let field = &mut document["components"]["schemas"]["Choice"]["oneOf"][1]["properties"]
            ["Window"]["properties"]["lookback"];
        field
            .as_object_mut()
            .unwrap()
            .extend(extra.as_object().unwrap().clone());
        let directory = tempfile::tempdir().unwrap();
        let path = directory.path().join("openapi.json");
        std::fs::write(&path, document.to_string()).unwrap();
        crate::openapi::load(&path).unwrap()
    }

    #[test]
    fn loaded_union_examples_validate_and_unknown_assertions_abstain() {
        let example = serde_json::json!({"Window":{"lookback":20}});
        for annotation in [
            serde_json::json!({}),
            serde_json::json!({
                "title":"Lookback period", "description":"The number of earlier windows.", "x-harbor-unit":"days"
            }),
        ] {
            let doc = source(annotation, example.clone());
            assert_eq!(
                matches(
                    &doc.components.schemas,
                    &doc.components.schemas["Choice"],
                    &example,
                    0
                ),
                Some(true)
            );
            assert!(!substitutions(&doc, DeclaredExampleMode::Docstring).is_empty());
        }
        for assertion in [
            serde_json::json!({"maximum":10}),
            serde_json::json!({"multipleOf":3}),
        ] {
            let doc = source(assertion, example.clone());
            assert_eq!(
                matches(
                    &doc.components.schemas,
                    &doc.components.schemas["Choice"],
                    &example,
                    0
                ),
                None
            );
            assert!(substitutions(&doc, DeclaredExampleMode::Docstring).is_empty());
        }
        let invalid = serde_json::json!({"Window":{"lookback":"twenty"}});
        let doc = source(serde_json::json!({}), invalid.clone());
        assert_eq!(
            matches(
                &doc.components.schemas,
                &doc.components.schemas["Choice"],
                &invalid,
                0
            ),
            Some(false)
        );
        assert!(substitutions(&doc, DeclaredExampleMode::Docstring).is_empty());
    }

    #[test]
    fn union_departures_abstain_when_rendering_would_synthesize_array_items() {
        let mut doc = source(
            serde_json::json!({}),
            serde_json::json!({"Window":{"lookback":20}}),
        );
        let choice = doc.components.schemas.get_mut("Choice").unwrap();
        let window = choice.one_of.as_mut().unwrap()[1]
            .properties
            .get_mut("Window")
            .unwrap();
        window.properties.insert(
            "lookback".into(),
            serde_json::from_value(serde_json::json!({
                "type":"array", "items":{"type":"object", "properties":{"days":{"type":"integer"}}}
            }))
            .unwrap(),
        );
        choice.example = Some(serde_json::json!({"Window":{"lookback":[]}}));
        assert_eq!(
            matches(
                &doc.components.schemas,
                &doc.components.schemas["Choice"],
                doc.components.schemas["Choice"].example.as_ref().unwrap(),
                0
            ),
            Some(true)
        );
        assert!(substitutions(&doc, DeclaredExampleMode::Docstring).is_empty());
    }

    #[test]
    fn declared_union_region_requires_the_exact_source_constructor_and_adjacent_text() {
        let doc = source(
            serde_json::json!({}),
            serde_json::json!({"Window":{"lookback":20}}),
        );
        let candidates = substitutions(&doc, DeclaredExampleMode::Docstring);
        let candidate = &candidates[0];
        assert_eq!(candidate.values.fallback, "ChoiceZero.NORTH");
        assert_eq!(
            candidate.values.declared,
            "ChoiceWindow(window=ChoiceWindowWindow(lookback=20))"
        );
        let fern = "Examples\n--------\nfrom api import Root, ChoiceZero\nclient.schedule(\n    choice=ChoiceZero.NORTH,\n    label=\"glassware\",\n)\n\"\"\"";
        let crozier = "Examples\n--------\nfrom api import Root, ChoiceWindow, ChoiceWindowWindow\nclient.schedule(\n    choice=ChoiceWindow(\n        window=ChoiceWindowWindow(lookback=20),\n    ),\n    label=\"glassware\",\n)\n\"\"\"";
        let context = super::super::Context::default().with_source_document(doc);
        for text in [
            crozier.to_string(),
            crozier.replace("lookback=20", "lookback=21"),
            crozier.replace("label=\"glassware\"", "label=\"changed\""),
        ] {
            let reference = fern.lines().collect::<Vec<_>>();
            let generated = text.lines().collect::<Vec<_>>();
            let pair = super::super::Pair {
                rel: "src/api/client.py",
                fern: &reference,
                crozier: &generated,
                context: &context,
            };
            assert_eq!(region(&pair).unwrap().is_some(), text == crozier);
        }
    }
}
