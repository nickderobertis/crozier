//! The worked-example values crozier keeps where the certified pair discards a
//! value the API's author declared for a placeholder of its own. Each rule is
//! one `kind: usefulness` entry the 2026-11-01 design review grants:
//!
//! - `declared-example-over-placeholder` (ruling 2, `falsy-property-example`,
//!   and its principle): a parameter's falsy example, a multipart form part's or a header parameter's
//!   declared example, a query parameter example on an operation answering no JSON, a path
//!   parameter's example on an operation whose other path parameter declares an
//!   empty schema, and an enum's declared example member.
//! - `unquoted-timestamp-parameter-example` (ruling 3,
//!   `yaml-timestamp-parameter-example`): a parameter example YAML reads as a
//!   timestamp.
//! - `declared-timestamp-property-example` (ruling 3's principle): a date-time
//!   property's unquoted timestamp in a schema-level object example.
//! - `declared-examples-array-parameter-value` (ruling 5,
//!   `declared-examples-array`): a parameter's value from its schema's
//!   `examples` array or its own `examples` map.
//!
//! Every rule checks the source document, so a value is admitted only where the
//! document declares exactly the value crozier writes for that argument.

use super::{
    argument_names, example_file, keyword_argument_line, list_argument_at, source_operations,
    visit_source_schemas, Pair,
};
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

/// A schema declaring no type, reference, format, composition, enum, `const`,
/// properties or items (circleci's `schema: {}`); keywords outside that list,
/// which such a schema has no use for, are not read.
fn untyped_unstructured_schema(schema: &Schema) -> bool {
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
                && parameter
                    .schema
                    .as_ref()
                    .is_some_and(untyped_unstructured_schema)
        });
        let non_json = non_json_success(operation);
        for parameter in &parameters {
            // Ruling 2 itself names a falsy example (`""`, `0`) on any argument,
            // its own or the first of its `examples` map (unicourt's `q`).
            if let Some(value) = first_map_example(parameter).filter(|value| falsy(value)) {
                out.push(Declared {
                    wire: &parameter.name,
                    value,
                });
            }
            let Some(value) = parameter.example.as_ref() else {
                continue;
            };
            let kept = falsy(value)
                || match parameter.location {
                    Some(ParameterLocation::Header) => true,
                    Some(ParameterLocation::Query) => non_json,
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
            multipart_examples(source, resolve(source, schema), &mut out, 0);
        }
    }
    out
}

/// A multipart form's parts' declared examples, and those of an object part's
/// own properties (runZero's `importTask.name`): the certified pair writes its
/// placeholder for each.
fn multipart_examples<'a>(
    source: &'a OpenApi,
    schema: &'a Schema,
    out: &mut Vec<Declared<'a>>,
    depth: usize,
) {
    if depth > 4 {
        return;
    }
    for (wire, property) in &schema.properties {
        let property = resolve(source, property);
        if let Some(value) = property.example.as_ref() {
            out.push(Declared { wire, value });
        }
        if !property.properties.is_empty() {
            multipart_examples(source, property, out, depth + 1);
        }
    }
}

/// Whether a declared value is falsy: `""` or zero.
fn falsy(value: &Value) -> bool {
    value.as_str() == Some("") || value.as_f64() == Some(0.0)
}

/// The first non-null value of a parameter's `examples` map.
fn first_map_example(parameter: &Parameter) -> Option<&Value> {
    parameter
        .examples
        .values()
        .find_map(|example| example.value.as_ref())
}

/// A worked-example argument line only crozier writes, passing an optional
/// parameter's falsy declared example the certified pair leaves out of the
/// call (ruling 2; unicourt's `q=""`).
pub(super) fn kept_falsy_optional_line(pair: &Pair<'_>, crozier: &str) -> bool {
    if !example_file(pair.rel) {
        return false;
    }
    let (Some((_, name, value)), Some(source)) = (
        keyword_argument_line(crozier),
        pair.context.source_document.as_ref(),
    ) else {
        return false;
    };
    source_operations(source)
        .flat_map(|(_, parameters)| parameters)
        .any(|parameter| {
            parameter.required != Some(true)
                && parameter_keyword(parameter, name)
                && parameter
                    .example
                    .as_ref()
                    .or_else(|| first_map_example(parameter))
                    .filter(|declared| falsy(declared))
                    .and_then(crate::ir::example_literal)
                    .as_deref()
                    == Some(value)
        })
}

/// An importer-declined operation's single request body (every successful
/// response answers something other than JSON, so the certified pair's
/// importer builds no example and its fallback writes placeholders): the
/// region where Fern's `request=` holds nothing but placeholders
/// (`{"string": {"key": "value"}}`, `[{"key": "value"}, …]`, `[StoreLine(), …]`)
/// and crozier's holds only values the operation's body examples declare
/// (ihulsbus's ingredient amounts, SeekStorm's documents; ruling 2's principle).
pub(super) fn declared_body_over_fallback(
    pair: &Pair<'_>,
) -> Result<Option<super::Region>, String> {
    if !example_file(pair.rel) {
        return Ok(None);
    }
    let Some(source) = pair.context.source_document.as_ref() else {
        return Ok(None);
    };
    let fern = request_blocks(pair.fern);
    let crozier = request_blocks(pair.crozier);
    if fern.len() != crozier.len() {
        return Ok(None);
    }
    let declared = declined_body_tokens(source);
    if declared.strings.is_empty() && declared.numbers.is_empty() {
        return Ok(None);
    }
    for (fern_block, crozier_block) in fern.iter().zip(&crozier) {
        let fern_text = pair.fern[fern_block.clone()].join("\n");
        let crozier_text = pair.crozier[crozier_block.clone()].join("\n");
        if fern_text == crozier_text {
            continue;
        }
        let (fern_strings, fern_numbers) = literal_tokens(&fern_text);
        let (strings, numbers) = literal_tokens(&crozier_text);
        // Fern's side holds only placeholders: no keyword argument inside the
        // value, its strings `string`/`key`/`value`, its numbers `1`/`1000000`.
        let fern_value = fern_text.trim_start().trim_start_matches("request=");
        let placeholder = !fern_value.contains('=')
            && fern_strings
                .iter()
                .all(|text| matches!(text.as_str(), "string" | "key" | "value"))
            && fern_numbers
                .iter()
                .all(|number| *number == 1.0 || *number == 1_000_000.0);
        let declared_only = !strings.is_empty() || !numbers.is_empty();
        let declared_only = declared_only
            && strings
                .iter()
                .all(|text| declared.strings.contains(text) || text.parse::<usize>().is_ok())
            && numbers.iter().all(|number| {
                declared
                    .numbers
                    .iter()
                    .any(|known| (known - number).abs() < 1e-9)
            });
        if placeholder && declared_only {
            return Ok(Some(super::Region {
                fern: fern_block.clone(),
                crozier: crozier_block.clone(),
            }));
        }
        return Ok(None);
    }
    Ok(None)
}

/// A call Fern writes empty on one line, `<prefix>()`, where crozier opens it
/// over lines every one of which `admit` accepts (an optional argument a
/// ruling keeps and Fern leaves out), and closes it with `<indent>)`.
fn kept_arguments_call(
    pair: &Pair<'_>,
    admit: &dyn Fn(&Pair<'_>, usize) -> bool,
) -> Option<super::Region> {
    if !example_file(pair.rel) {
        return None;
    }
    pair.fern.iter().enumerate().find_map(|(at, fern)| {
        let opener = fern.strip_suffix("()").map(|head| format!("{head}("))?;
        if !fern.contains("client.") || pair.crozier.contains(fern) {
            return None;
        }
        let indent = &fern[..fern.len() - fern.trim_start().len()];
        let start = pair.crozier.iter().position(|line| *line == opener)?;
        let close = (start + 1..pair.crozier.len())
            .find(|&index| pair.crozier[index] == format!("{indent})"))?;
        (close > start + 1 && (start + 1..close).all(|index| admit(pair, index))).then(|| {
            super::Region {
                fern: at..at + 1,
                crozier: start..close + 1,
            }
        })
    })
}

/// [`kept_arguments_call`] for falsy optional examples (ruling 2), then
/// [`declared_body_over_fallback`]: the `declared-example-over-placeholder`
/// regions.
pub(super) fn declared_example_regions(pair: &Pair<'_>) -> Result<Option<super::Region>, String> {
    if let Some(region) = kept_arguments_call(pair, &|pair, index| {
        pair.crozier
            .get(index)
            .is_some_and(|line| kept_falsy_optional_line(pair, line))
    }) {
        return Ok(Some(region));
    }
    declared_body_over_fallback(pair)
}

/// [`kept_arguments_call`] for optional timestamp examples (ruling 3).
pub(super) fn unquoted_timestamp_call(pair: &Pair<'_>) -> Result<Option<super::Region>, String> {
    Ok(kept_arguments_call(pair, &|pair, index| {
        unquoted_timestamp_parameter_line(pair, index)
    }))
}

/// The string and number values (keys included) every request body example
/// of an importer-declined operation declares.
#[derive(Default)]
struct DeclaredTokens {
    strings: std::collections::BTreeSet<String>,
    numbers: Vec<f64>,
}

fn declined_body_tokens(source: &OpenApi) -> DeclaredTokens {
    fn walk(value: &Value, out: &mut DeclaredTokens) {
        match value {
            Value::String(text) => {
                out.strings.insert(text.clone());
            }
            Value::Number(number) => out.numbers.extend(number.as_f64()),
            Value::Array(items) => items.iter().for_each(|item| walk(item, out)),
            Value::Object(fields) => {
                for (key, field) in fields {
                    out.strings.insert(key.clone());
                    walk(field, out);
                }
            }
            _ => {}
        }
    }
    let mut out = DeclaredTokens::default();
    for (operation, _) in source_operations(source) {
        if !non_json_success(operation) {
            continue;
        }
        let Some(body) = operation.request_body.as_ref() else {
            continue;
        };
        for media in body.content.values() {
            media.example.iter().for_each(|value| walk(value, &mut out));
            for example in media.examples.values() {
                example.value.iter().for_each(|value| walk(value, &mut out));
            }
        }
    }
    out
}

/// Each `request=` argument of a worked call, as the range of lines it spans:
/// one line, or an opener through the line closing its brackets.
fn request_blocks(lines: &[&str]) -> Vec<std::ops::Range<usize>> {
    let mut out = Vec::new();
    let mut index = 0;
    while index < lines.len() {
        let line = lines[index];
        if !line.trim_start().starts_with("request=") {
            index += 1;
            continue;
        }
        let mut depth = 0i32;
        let mut end = index;
        loop {
            depth += bracket_depth(lines[end]);
            if depth <= 0 || end + 1 >= lines.len() {
                break;
            }
            end += 1;
        }
        out.push(index..end + 1);
        index = end + 1;
    }
    out
}

/// The net bracket depth a line opens, outside string literals.
fn bracket_depth(line: &str) -> i32 {
    let mut depth = 0;
    let mut quote = None;
    let mut escaped = false;
    for character in line.chars() {
        match quote {
            Some(delimiter) => {
                if escaped {
                    escaped = false;
                } else if character == '\\' {
                    escaped = true;
                } else if character == delimiter {
                    quote = None;
                }
            }
            None => match character {
                '"' | '\'' => quote = Some(character),
                '[' | '{' | '(' => depth += 1,
                ']' | '}' | ')' => depth -= 1,
                _ => {}
            },
        }
    }
    depth
}

/// The string and number literals of the Python a worked-example `request=`
/// region writes: each quoted string with its escapes decoded (`\n`, `\t`,
/// `\r`, `\xHH`, `\uHHHH`, and a backslash before any other character
/// kept, as Python keeps it), and each decimal number with its unary `-` sign
/// and exponent. Names, keywords and operators are skipped; it reads only what
/// [`declared_body_over_fallback`] compares against a body's declared values,
/// never Python beyond the literals crozier and Fern write there.
fn literal_tokens(text: &str) -> (Vec<String>, Vec<f64>) {
    let mut strings = Vec::new();
    let mut numbers = Vec::new();
    let chars: Vec<char> = text.chars().collect();
    let mut index = 0;
    while index < chars.len() {
        let character = chars[index];
        if character == '"' || character == '\'' {
            let (value, next) = string_literal(&chars, index + 1, character);
            strings.push(value);
            index = next;
            continue;
        }
        let operand_before = index > 0
            && (chars[index - 1].is_alphanumeric()
                || matches!(chars[index - 1], '_' | ')' | ']' | '.'));
        let signed = character == '-'
            && chars.get(index + 1).is_some_and(char::is_ascii_digit)
            && !operand_before;
        if (character.is_ascii_digit() && !operand_before) || signed {
            let start = index;
            index += 1;
            while index < chars.len() && (chars[index].is_ascii_digit() || chars[index] == '.') {
                index += 1;
            }
            if matches!(chars.get(index), Some('e' | 'E')) {
                let digits = match chars.get(index + 1) {
                    Some('+' | '-') => index + 2,
                    _ => index + 1,
                };
                if chars.get(digits).is_some_and(char::is_ascii_digit) {
                    index = digits;
                    while index < chars.len() && chars[index].is_ascii_digit() {
                        index += 1;
                    }
                }
            }
            let literal: String = chars[start..index].iter().collect();
            numbers.extend(literal.parse::<f64>().ok());
            continue;
        }
        index += 1;
    }
    (strings, numbers)
}

/// The decoded body of a string literal opened just before `index` by
/// `delimiter`, and the index after its closing delimiter.
fn string_literal(chars: &[char], mut index: usize, delimiter: char) -> (String, usize) {
    let hex = |digits: &[char]| -> Option<char> {
        let text: String = digits.iter().collect();
        u32::from_str_radix(&text, 16).ok().and_then(char::from_u32)
    };
    let mut value = String::new();
    while index < chars.len() && chars[index] != delimiter {
        if chars[index] != '\\' || index + 1 >= chars.len() {
            value.push(chars[index]);
            index += 1;
            continue;
        }
        let escape = chars[index + 1];
        index += 2;
        let width = match escape {
            'x' => 2,
            'u' => 4,
            _ => 0,
        };
        if width > 0 {
            if let Some(decoded) = chars.get(index..index + width).and_then(hex) {
                value.push(decoded);
                index += width;
                continue;
            }
        }
        match escape {
            'n' => value.push('\n'),
            't' => value.push('\t'),
            'r' => value.push('\r'),
            '\\' | '\'' | '"' => value.push(escape),
            other => {
                value.push('\\');
                value.push(other);
            }
        }
    }
    (value, index + 1)
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
    if declared_enum_member(pair, fern, crozier) || kept_wrapped_list(pair, fern, crozier) {
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
    kept_value(source, name, fern_value, value)
}

/// Whether `value` is a kept declared value of the argument `name`, beside
/// Fern's placeholder `fern_value` for it.
fn kept_value(source: &OpenApi, name: &str, fern_value: &str, value: &str) -> bool {
    let kept = |wire: &str, declared: &Value| {
        (argument_names(wire, name) || argument_names(crate::ir::header_param_stem(wire), name))
            && placeholder_for(wire, fern_value)
            && crate::ir::example_literal(declared).as_deref() == Some(value)
    };
    kept_declared_values(source)
        .iter()
        .any(|declared| kept(declared.wire, declared.value))
        || union_property_examples(source)
            .iter()
            .any(|(wire, declared)| kept(wire, declared))
}

/// Every property whose schema is a `oneOf` or `anyOf` and declares its own
/// `example` (guardian's `filterValue`, `oneOf: [string, array of string]`
/// exampled `[type]`), which the certified pair works as its first
/// alternative's placeholder: the union-typed sub-rule of example-value-source.
fn union_property_examples(source: &OpenApi) -> Vec<(String, Value)> {
    let mut out = Vec::new();
    visit_source_schemas(Some(source), &mut |schema| {
        for (wire, property) in &schema.properties {
            if property.one_of.is_some() || property.any_of.is_some() {
                if let Some(example) = &property.example {
                    out.push((wire.clone(), example.clone()));
                }
            }
        }
    });
    out
}

/// The opener of a wrapped list crozier writes for a kept union-typed value,
/// `<name>=[`, beside Fern's one-line placeholder: the list it opens (read from
/// crozier's lines) must be the declared example.
fn kept_wrapped_list(pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    let (Some((fern_indent, fern_name, fern_value)), Some(source)) = (
        keyword_argument_line(fern),
        pair.context.source_document.as_ref(),
    ) else {
        return false;
    };
    let Some(name) = crozier
        .strip_prefix(fern_indent)
        .and_then(|rest| rest.strip_suffix("=["))
        .filter(|name| *name == fern_name)
    else {
        return false;
    };
    pair.crozier.iter().enumerate().any(|(at, line)| {
        *line == crozier
            && list_argument_at(pair.crozier, at).is_some_and(|(_, items)| {
                kept_value(source, name, fern_value, &format!("[{}]", items.join(", ")))
            })
    })
}

/// An item or the closer of a wrapped list [`kept_wrapped_list`] admits, the
/// lines only crozier writes.
pub(super) fn kept_wrapped_list_line(pair: &Pair<'_>, at: usize) -> bool {
    if !example_file(pair.rel)
        || pair
            .crozier
            .get(at)
            .is_some_and(|line| line.ends_with("=["))
    {
        return false;
    }
    let Some(source) = pair.context.source_document.as_ref() else {
        return false;
    };
    list_argument_at(pair.crozier, at).is_some_and(|(name, items)| {
        let value = format!("[{}]", items.join(", "));
        union_property_examples(source)
            .iter()
            .any(|(wire, declared)| {
                argument_names(wire, name)
                    && crate::ir::example_literal(declared).as_deref() == Some(value.as_str())
            })
    })
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
    let declared = parameter
        .example
        .as_ref()
        .or_else(|| first_map_example(parameter))
        .or_else(|| {
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
    let all = timestamp_parameters(source);
    let optional: Vec<_> = all
        .iter()
        .filter(|(parameter, _)| parameter.required != Some(true))
        .copied()
        .collect();
    let lines = pair.crozier;
    let Some(line) = lines.get(at) else {
        return false;
    };
    // `<name>=datetime.datetime.fromisoformat(`, `"<iso>",`, `),` for one of
    // `parameters`.
    let wrapped = |index: usize, parameters: &[(&Parameter, &str)]| -> bool {
        let Some(line) = lines.get(index) else {
            return false;
        };
        let Some(name) = line
            .trim_start()
            .strip_suffix("=datetime.datetime.fromisoformat(")
        else {
            return false;
        };
        let indent = &line[..line.len() - line.trim_start().len()];
        parameters.iter().any(|(parameter, declared)| {
            parameter_keyword(parameter, name)
                && lines.get(index + 1).is_some_and(|next| {
                    *next == format!("{indent}    {}", timestamp_spellings(declared)[2])
                })
                && lines.get(index + 2) == Some(&format!("{indent}),").as_str())
        })
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
    let imports = |index: usize| {
        lines
            .get(index)
            .is_some_and(|line| line.trim() == "import datetime")
            && (0..lines.len()).any(|other| other != index && passes(other))
    };
    if line.trim() == "import datetime" {
        // Needed only by a timestamp line this rule admits.
        return imports(at);
    }
    // A docstring separates the import it adds from the next one by a blank
    // line.
    if line.trim().is_empty() {
        return at >= 1 && imports(at - 1);
    }
    // The string and closing lines of any declared-timestamp call: the line
    // alignment may pair Fern's one wrapped call with either of crozier's.
    passes(at) || (at >= 1 && wrapped(at - 1, &all)) || (at >= 2 && wrapped(at - 2, &all))
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

/// Every date-time property a schema-level object example gives an unquoted
/// timestamp, other than the `2000-01-23T04:56:07` sentinel the certified pair
/// and crozier both drop: its wire name and the declared value.
fn timestamp_properties(source: &OpenApi) -> Vec<(String, String)> {
    let Some(unquoted) = source.yaml_unquoted_timestamps.as_ref() else {
        return Vec::new();
    };
    let mut out = Vec::new();
    visit_source_schemas(Some(source), &mut |schema| {
        let Some(example) = schema.example.as_ref().and_then(Value::as_object) else {
            return;
        };
        for (wire, property) in &schema.properties {
            let Some(value) = example.get(wire).and_then(Value::as_str) else {
                continue;
            };
            if resolve(source, property).format.as_deref() == Some("date-time")
                && unquoted.contains(value)
                && crate::emit::yaml_resolves_as_timestamp(value)
                && !value.starts_with("2000-01-23T04:56:07")
            {
                out.push((wire.clone(), value.to_string()));
            }
        }
    });
    out
}

/// `declared-timestamp-property-example`: Fern's date-time placeholder beside
/// crozier's line passing the timestamp a schema-level object example declares
/// for that same date-time property, as a keyword argument or as the string
/// line of a wrapped `fromisoformat` call.
pub(super) fn declared_timestamp_property_example(
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
    let properties = timestamp_properties(source);
    if fern.trim_start() == FERN_DATETIME_WRAPPED {
        let indent = &fern[..fern.len() - fern.trim_start().len()];
        return properties
            .iter()
            .any(|(_, value)| crozier == format!("{indent}{}", timestamp_spellings(value)[2]));
    }
    let (Some((fern_indent, fern_name, fern_value)), Some((indent, name, value))) =
        (keyword_argument_line(fern), keyword_argument_line(crozier))
    else {
        return false;
    };
    fern_indent == indent
        && fern_name == name
        && fern_value == FERN_DATETIME
        && properties.iter().any(|(wire, declared)| {
            argument_names(wire, name) && timestamp_spellings(declared)[1] == value
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
    fn literal_tokens_reads_signed_and_exponent_numbers_and_decodes_string_escapes() {
        let (strings, numbers) = literal_tokens(
            r#"Store(depth=-4, scale=1e3, tiny=-2.5E-2, ratio=0.75, name="a\"b\\c\n\u00e9\x41\q", tag='it\'s', item_2=7)"#,
        );
        assert_eq!(numbers, vec![-4.0, 1000.0, -0.025, 0.75, 7.0]);
        assert_eq!(
            strings,
            vec!["a\"b\\c\n\u{e9}A\\q".to_owned(), "it's".to_owned()]
        );
        // A minus after an operand (`x`, `]`) is subtraction, not a sign, and
        // digits inside a name (`v2`) are no literal of their own.
        let (_, numbers) = literal_tokens("call(x-4, items[0]-1, v2)");
        assert_eq!(numbers, vec![4.0, 0.0, 1.0]);
    }

    #[test]
    fn an_importer_declined_body_example_is_kept_only_over_fallback_placeholders() {
        let context = context(
            serde_json::json!({"openapi": "3.0.3", "paths": {"/stores": {"delete": {
                "requestBody": {"content": {"application/json": {"schema": {"type": "array",
                    "items": {"type": "object"}},
                    "examples": {"one": {"value": [{"itemId": "a-1", "crates": 4}]}}}}},
                "responses": {"204": {"description": "ok", "content": {"text/plain": {"schema": {"type": "string"}}}}}
            }}}}),
        );
        let region = |fern: &[&str], crozier: &[&str]| {
            declared_body_over_fallback(&Pair {
                rel: "reference.md",
                fern,
                crozier,
                context: &context,
            })
            .expect("no engine error")
        };
        let fern = [
            "call(",
            "    request=[",
            "        Store(),",
            "        Store()",
            "    ],",
            ")",
        ];
        let kept = [
            "call(",
            "    request=[",
            "        Store(",
            "            item_id=\"a-1\",",
            "            crates=4,",
            "        )",
            "    ],",
            ")",
        ];
        assert_eq!(
            region(&fern, &kept),
            Some(super::super::Region {
                fern: 1..5,
                crozier: 1..7
            })
        );
        // A value the document never declares, or Fern writing anything but
        // placeholders, is no departure.
        let other = [
            "call(",
            "    request=[",
            "        Store(",
            "            item_id=\"b-2\",",
            "        )",
            "    ],",
            ")",
        ];
        assert_eq!(region(&fern, &other), None);
        let fern_declared = [
            "call(",
            "    request=[",
            "        Store(item_id=\"a-1\"),",
            "    ],",
            ")",
        ];
        assert_eq!(region(&fern_declared, &kept), None);
        // A sign the document never declares is a different value: `-4` is not
        // the declared `4`.
        let negated = kept.map(|line| line.replace("crates=4", "crates=-4"));
        let negated: Vec<&str> = negated.iter().map(String::as_str).collect();
        assert_eq!(region(&fern, &negated), None);
    }

    #[test]
    fn a_falsy_optional_example_and_an_empty_call_are_kept() {
        let context = context(
            serde_json::json!({"openapi": "3.0.3", "paths": {"/search": {"get": {
                "parameters": [{"name": "q", "in": "query", "schema": {"type": "string"},
                    "examples": {"blank": {"value": ""}}}],
                "responses": {}
            }}}}),
        );
        let lines = ["client.keepers.search(", "    q=\"\",", ")"];
        let crozier = pair("reference.md", &lines, &context);
        assert!(kept_falsy_optional_line(&crozier, "    q=\"\","));
        assert!(!kept_falsy_optional_line(&crozier, "    q=\"x\","));
        let fern = ["client.keepers.search()"];
        let both = Pair {
            rel: "reference.md",
            fern: &fern,
            crozier: &lines,
            context: &context,
        };
        assert_eq!(
            declared_example_regions(&both).expect("no engine error"),
            Some(super::super::Region {
                fern: 0..1,
                crozier: 0..3
            })
        );
        let other = ["client.keepers.search(", "    q=\"x\",", ")"];
        let neither = Pair {
            rel: "reference.md",
            fern: &fern,
            crozier: &other,
            context: &context,
        };
        assert_eq!(
            declared_example_regions(&neither).expect("no engine error"),
            None
        );
    }

    #[test]
    fn a_nested_multipart_property_example_is_kept() {
        let context = context(
            serde_json::json!({"openapi": "3.0.3", "paths": {"/import": {"post": {
                "requestBody": {"content": {"multipart/form-data": {"schema": {"type": "object",
                    "properties": {"task": {"type": "object", "properties": {
                        "label": {"type": "string", "example": "spring refit"}}}}}}}},
                "responses": {}
            }}}}),
        );
        let pair = pair("reference.md", &[], &context);
        assert!(declared_example_over_placeholder(
            &pair,
            "        label=\"label\",",
            "        label=\"spring refit\","
        ));
        assert!(!declared_example_over_placeholder(
            &pair,
            "        label=\"label\",",
            "        label=\"autumn\","
        ));
    }

    #[test]
    fn a_union_property_example_is_kept_on_one_line_or_wrapped() {
        let context = context(serde_json::json!({"openapi": "3.0.3", "paths": {},
            "components": {"schemas": {"Layer": {"type": "object", "properties": {
                "match": {"oneOf": [{"type": "string"},
                    {"type": "array", "items": {"type": "string"}}], "example": ["depth"]}}}}}}));
        let rule = declared_example_over_placeholder;
        let one = pair("src/fern/charts/client.py", &[], &context);
        assert!(rule(
            &one,
            "            match=\"match\",",
            "            match=[\"depth\"],"
        ));
        assert!(!rule(
            &one,
            "            match=\"match\",",
            "            match=[\"other\"],"
        ));
        let wrapped = ["    match=[", "        \"depth\"", "    ],"];
        let wrapped_pair = pair("reference.md", &wrapped, &context);
        assert!(rule(&wrapped_pair, "    match=\"match\",", "    match=["));
        assert!(kept_wrapped_list_line(&wrapped_pair, 1));
        assert!(kept_wrapped_list_line(&wrapped_pair, 2));
        let other = ["    match=[", "        \"other\"", "    ],"];
        let other_pair = pair("reference.md", &other, &context);
        assert!(!rule(&other_pair, "    match=\"match\",", "    match=["));
        assert!(!kept_wrapped_list_line(&other_pair, 1));
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
            "",
            "client.tides.list_tides(",
            "    until=datetime.datetime.fromisoformat(",
            "        \"2031-04-03 08:15:00+00:00\",",
            "    ),",
            ")",
        ];
        let added = pair("src/fern/tides/client.py", &lines, &context);
        for at in [0, 1, 3, 4, 5] {
            assert!(unquoted_timestamp_parameter_line(&added, at), "{at}");
        }
        assert!(!unquoted_timestamp_parameter_line(&added, 2));
        // A blank line after anything but the admitted import is no departure.
        let blank = ["client.tides.list_tides(", "", ")"];
        assert!(!unquoted_timestamp_parameter_line(
            &pair("src/fern/tides/client.py", &blank, &context),
            1
        ));
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

    #[test]
    fn a_declared_timestamp_property_is_admitted_only_with_its_declaration() {
        let document = |quoted: bool| {
            let mut source: OpenApi = serde_json::from_value(serde_json::json!({"openapi": "3.0.3",
                "paths": {}, "components": {"schemas": {"TideReading": {"type": "object",
                    "example": {"highWaterAt": "2031-04-02T08:15:00Z", "level": "2031-04-02T08:15:00Z",
                        "calibratedAt": "2000-01-23T04:56:07.000+00:00"},
                    "properties": {
                        "highWaterAt": {"type": "string", "format": "date-time"},
                        "level": {"type": "string"},
                        "calibratedAt": {"type": "string", "format": "date-time"}}}}}}))
            .expect("a document");
            source.yaml_unquoted_timestamps = (!quoted).then(|| {
                ["2031-04-02T08:15:00Z", "2000-01-23T04:56:07.000+00:00"]
                    .into_iter()
                    .map(String::from)
                    .collect()
            });
            with_source(source)
        };
        let fern =
            "    high_water_at=datetime.datetime.fromisoformat(\"2024-01-15T09:30:00+00:00\"),";
        let kept =
            "    high_water_at=datetime.datetime.fromisoformat(\"2031-04-02T08:15:00+00:00\"),";
        let rule = declared_timestamp_property_example;
        let context = document(false);
        for rel in ["README.md", "reference.md", "src/fern/tides/client.py"] {
            assert!(rule(&pair(rel, &[], &context), fern, kept), "{rel}");
        }
        let at = pair("src/fern/tides/client.py", &[], &context);
        assert!(rule(
            &at,
            "                \"2024-01-15 09:30:00+00:00\",",
            "                \"2031-04-02 08:15:00+00:00\","
        ));
        // Another instant, another keyword, a property that is not date-time,
        // the sentinel, a file that is no example and a quoted value all fail.
        assert!(!rule(
            &at,
            fern,
            "    high_water_at=datetime.datetime.fromisoformat(\"2031-04-03T08:15:00+00:00\"),"
        ));
        assert!(!rule(
            &at,
            "    low_water_at=datetime.datetime.fromisoformat(\"2024-01-15T09:30:00+00:00\"),",
            "    low_water_at=datetime.datetime.fromisoformat(\"2031-04-02T08:15:00+00:00\"),"
        ));
        assert!(!rule(
            &at,
            "    level=\"level\",",
            "    level=\"2031-04-02T08:15:00Z\","
        ));
        assert!(!rule(
            &at,
            "    calibrated_at=datetime.datetime.fromisoformat(\"2024-01-15T09:30:00+00:00\"),",
            "    calibrated_at=datetime.datetime.fromisoformat(\"2000-01-23T04:56:07+00:00\"),"
        ));
        assert!(!rule(
            &pair("src/fern/core/http_client.py", &[], &context),
            fern,
            kept
        ));
        let quoted = document(true);
        assert!(!rule(&pair("reference.md", &[], &quoted), fern, kept));
    }
}
