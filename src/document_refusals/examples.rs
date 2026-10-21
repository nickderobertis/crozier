//! The example-value refusals: `fern check` validating an example value against
//! the type it is an example of.
//!
//! Fern validates the examples it attaches to every endpoint: the ones a
//! document writes (`x-fern-examples`, media-type `example`/`examples`, schema and
//! parameter `example`s) and the ones its importer assembles from them. Which
//! value reaches which check is measured, not inferred; each rule below covers
//! only the shapes pinned Fern controls refuse, and stops (reporting nothing)
//! wherever a near miss was not measured. `x-crozier-examples` is never read:
//! Fern does not see it, so it can never make Fern refuse a document.

use std::collections::HashSet;

use serde_json::Value;

use super::{ignored_reference_node, yaml_pointer, Class};

const METHODS: [&str; 8] = [
    "get", "put", "post", "delete", "options", "head", "patch", "trace",
];

/// The first example value Fern's check rejects, as the class it reports and
/// the offending element.
#[cfg(test)]
pub(super) fn first_violation(root: &Value) -> Option<(Class, String)> {
    first_violation_in(root, "")
}

/// [`first_violation`] over a document whose source text is `text`.
pub(super) fn first_violation_in(root: &Value, text: &str) -> Option<(Class, String)> {
    let doc = Doc {
        root,
        plain: plain_timestamps(root, text),
    };
    for operation in doc.operations() {
        let element = format!(
            "{} {}",
            operation.method.to_ascii_uppercase(),
            operation.route
        );
        let found = doc
            .version_header_redeclared(&operation)
            .or_else(|| doc.header_default_override(&operation))
            .or_else(|| doc.header_name_fallback(&operation))
            .or_else(|| doc.nullable_parent_example(&operation))
            .or_else(|| doc.read_only_shadows_required_parent(&operation))
            .or_else(|| doc.discriminant_required_by_grandparent(&operation))
            .or_else(|| doc.schema_scalar_example(&operation))
            .or_else(|| doc.media_scalar_example(&operation))
            .or_else(|| doc.shadowed_union_property(&operation))
            .or_else(|| doc.fern_examples(&operation))
            .or_else(|| doc.error_examples(&operation))
            .or_else(|| doc.non_object_error_examples(&operation));
        if let Some((class, detail)) = found {
            return Some((class, format!("{element} {detail}")));
        }
    }
    doc.colliding_component()
        .or_else(|| doc.colliding_property())
        .or_else(|| doc.scalar_taken_by_inline_object())
        .or_else(|| doc.merged_member_enum())
}

struct Operation<'a> {
    route: &'a str,
    method: &'a str,
    item: &'a Value,
    op: &'a Value,
}

struct Doc<'a> {
    root: &'a Value,
    /// The nodes of `root` the source writes as plain YAML timestamps (see
    /// [`plain_timestamps`]), by address: one occurrence each, never a value.
    plain: HashSet<*const Value>,
}

/// Every node of `root` that its YAML source `text` writes as a plain
/// (unquoted) timestamp scalar, decided per occurrence from that scalar's own
/// style: a quoted copy of the same text elsewhere is not one, and neither is
/// timestamp-like text inside a comment, a block scalar or a quoted string. A
/// node an alias or a `<<` merge places is one where its anchored scalar is.
///
/// Fern's YAML parser reads such a scalar as a timestamp, not a string, so a
/// `date` example written that way is no string it rejects: measured at Fern
/// CLI 5.163.1, the class probe's quoted `"2006-01-02T15:04:05+00:00"` is
/// refused and the same value unquoted generates (`unquoted-date-example`
/// control; Asana's `due_at`, `2019-09-15T02:06:58.147Z`). crozier's parser
/// reads both as one string, so the plain ones are found in the source.
fn plain_timestamps(root: &Value, text: &str) -> HashSet<*const Value> {
    plain_timestamp_paths(text)
        .iter()
        .filter_map(|path| {
            path.iter().try_fold(root, |node, step| match node {
                Value::Object(fields) => fields.get(step),
                Value::Array(items) => items.get(step.parse::<usize>().ok()?),
                _ => None,
            })
        })
        .map(std::ptr::from_ref)
        .collect()
}

/// Where [`plain_timestamp_paths`] stands in a collection: a mapping awaiting
/// its next key, a mapping awaiting the value of the key just read (`None` for a
/// key with no path of its own: an alias or a collection), or a sequence at its
/// next index.
enum Frame {
    MapKey,
    MapValue(Option<String>),
    Seq(usize),
}

/// An anchored collection being read: what its anchor will hold once it closes.
struct Recording {
    anchor: usize,
    /// How many frames enclosed it when it opened.
    depth: usize,
    /// The length of its own path, which the paths it holds are relative to.
    base: usize,
    held: Vec<Vec<String>>,
}

/// The paths (mapping keys and sequence indices) of every plain timestamp
/// scalar in `text`'s first document; see [`plain_timestamps`].
fn plain_timestamp_paths(text: &str) -> Vec<Vec<String>> {
    use serde_saphyr::granit_parser::{Event, Parser, ScalarStyle};
    static TIMESTAMP: std::sync::OnceLock<fancy_regex::Regex> = std::sync::OnceLock::new();
    let timestamp = TIMESTAMP.get_or_init(|| {
        fancy_regex::Regex::new(
            r"^\d{4}-\d{1,2}-\d{1,2}(?:[Tt]|[ \t]+)\d{1,2}:\d{2}:\d{2}(?:\.\d*)?(?:[ \t]*(?:Z|[-+]\d{1,2}(?::\d{2})?))?$",
        )
        .expect("the YAML timestamp pattern compiles")
    });
    let mut frames: Vec<Frame> = Vec::new();
    let mut found: Vec<Vec<String>> = Vec::new();
    // The plain timestamps under each anchor, relative to the anchored node.
    let mut anchors: std::collections::HashMap<usize, Vec<Vec<String>>> =
        std::collections::HashMap::new();
    let mut recording: Vec<Recording> = Vec::new();
    // Depth inside a collection used as a mapping key, whose content has no path.
    let mut in_key = 0usize;
    // The path of the node about to be read; `None` under a key with no path.
    let path_of = |frames: &[Frame]| -> Option<Vec<String>> {
        frames
            .iter()
            .map(|frame| match frame {
                Frame::MapValue(key) => key.clone(),
                Frame::Seq(index) => Some(index.to_string()),
                Frame::MapKey => None,
            })
            .collect()
    };
    let mut record = |path: Vec<String>, recording: &mut Vec<Recording>| {
        for open in recording.iter_mut() {
            if path.len() >= open.base {
                open.held.push(path[open.base..].to_vec());
            }
        }
        found.push(path);
    };
    // The key just read (`None`: one with no path); its value comes next.
    let keyed = |frames: &mut Vec<Frame>, key: Option<String>| {
        if let Some(frame) = frames.last_mut() {
            *frame = Frame::MapValue(key);
        }
    };
    // A value is complete: the next node is its mapping's next key, or its
    // sequence's next item.
    let advance = |frames: &mut Vec<Frame>| match frames.last_mut() {
        Some(frame @ Frame::MapValue(_)) => *frame = Frame::MapKey,
        Some(Frame::Seq(index)) => *index += 1,
        Some(Frame::MapKey) | None => {}
    };
    let mut parser = Parser::new_from_str(text);
    while let Some(Ok((event, _span))) = parser.next_event() {
        if in_key > 0 {
            match event {
                Event::MappingStart(..) | Event::SequenceStart(..) => in_key += 1,
                Event::MappingEnd | Event::SequenceEnd => {
                    in_key -= 1;
                    if in_key == 0 {
                        keyed(&mut frames, None);
                    }
                }
                _ => {}
            }
            continue;
        }
        let at_key = matches!(frames.last(), Some(Frame::MapKey));
        match event {
            Event::DocumentEnd => break,
            Event::Scalar(value, _, _, _) if at_key => keyed(&mut frames, Some(value.into_owned())),
            Event::Alias(_) if at_key => keyed(&mut frames, None),
            Event::MappingStart(..) | Event::SequenceStart(..) if at_key => in_key = 1,
            Event::Scalar(value, style, anchor, _tag) => {
                let plain =
                    style == ScalarStyle::Plain && timestamp.is_match(&value).unwrap_or(false);
                if anchor != 0 {
                    anchors.insert(anchor, if plain { vec![Vec::new()] } else { Vec::new() });
                }
                if plain {
                    if let Some(path) = path_of(&frames) {
                        record(path, &mut recording);
                    }
                }
                advance(&mut frames);
            }
            Event::Alias(anchor) => {
                // A `<<` merge (one alias, or a sequence of them) places the
                // anchored mapping's members beside the merging mapping's own.
                let merged = |frame: Option<&Frame>| matches!(frame, Some(Frame::MapValue(Some(key))) if key == "<<");
                let depth = frames.len();
                let base = if merged(frames.last()) {
                    path_of(&frames[..depth - 1])
                } else if matches!(frames.last(), Some(Frame::Seq(_)))
                    && depth >= 2
                    && merged(frames.get(depth - 2))
                {
                    path_of(&frames[..depth - 2])
                } else {
                    path_of(&frames)
                };
                if let (Some(base), Some(held)) = (base, anchors.get(&anchor).cloned()) {
                    for relative in held {
                        record([base.clone(), relative].concat(), &mut recording);
                    }
                }
                advance(&mut frames);
            }
            Event::MappingStart(_, anchor, _) | Event::SequenceStart(_, anchor, _) => {
                if anchor != 0 {
                    if let Some(path) = path_of(&frames) {
                        recording.push(Recording {
                            anchor,
                            depth: frames.len(),
                            base: path.len(),
                            held: Vec::new(),
                        });
                    }
                }
                frames.push(if matches!(event, Event::MappingStart(..)) {
                    Frame::MapKey
                } else {
                    Frame::Seq(0)
                });
            }
            Event::MappingEnd | Event::SequenceEnd => {
                frames.pop();
                while let Some(open) = recording.pop_if(|open| open.depth == frames.len()) {
                    anchors.insert(open.anchor, open.held);
                }
                advance(&mut frames);
            }
            _ => {}
        }
    }
    found
}

fn str_of<'a>(value: &'a Value, key: &str) -> Option<&'a str> {
    value.get(key).and_then(Value::as_str)
}

fn is_type(schema: &Value, ty: &str) -> bool {
    str_of(schema, "type") == Some(ty)
}

/// `type: object`, or no `type` at all.
fn object_or_untyped(schema: &Value) -> bool {
    schema.get("type").is_none() || is_type(schema, "object")
}

#[cfg(test)]
mod parameter_refusal_tests {
    use super::*;

    #[test]
    fn required_header_overrides_and_version_conflicts_name_the_element() {
        for (source, class, header) in [
            (
                include_str!(
                    "../../docs/fern-refusals/header-default-differs-across-operations/probe.yml"
                ),
                "header-default-differs-across-operations",
                "X-Projection",
            ),
            (
                include_str!(
                    "../../docs/fern-refusals/version-header-redeclared-as-parameter/probe.yml"
                ),
                "version-header-redeclared-as-parameter",
                "X-Calibration-Revision",
            ),
        ] {
            let root: Value = crate::yaml::from_str(source).unwrap();
            let (found, element) = first_violation(&root).expect("the measured refusal");
            assert_eq!(found.id(), class);
            assert!(element.contains(header), "{element}");
        }
    }

    #[test]
    fn matching_defaults_and_distinct_version_headers_are_valid_controls() {
        let mut defaults: Value = crate::yaml::from_str(include_str!(
            "../../docs/fern-refusals/header-default-differs-across-operations/probe.yml"
        ))
        .unwrap();
        defaults["paths"]["/measurements"]["put"]["parameters"][0]["schema"]["default"] =
            Value::String("radial".into());
        assert!(first_violation(&defaults).is_none());
        let mut version: Value = crate::yaml::from_str(include_str!(
            "../../docs/fern-refusals/version-header-redeclared-as-parameter/probe.yml"
        ))
        .unwrap();
        version["x-crozier-version"] = crate::yaml::from_str("header: X-Other-Revision").unwrap();
        assert!(first_violation(&version).is_none());
        version["x-crozier-version"] = version["x-fern-version"].clone();
        assert_eq!(
            first_violation(&version).unwrap().0.id(),
            "version-header-redeclared-as-parameter"
        );
        version["paths"]["/measurements"]["get"]["parameters"][0]["required"] = Value::Bool(false);
        assert!(first_violation(&version).is_none());
    }
}

fn has_composition(schema: &Value) -> bool {
    ["allOf", "oneOf", "anyOf"]
        .iter()
        .any(|key| schema.get(*key).is_some())
}

fn non_empty_mapping(value: Option<&Value>) -> bool {
    value
        .and_then(Value::as_object)
        .is_some_and(|mapping| !mapping.is_empty())
}

/// Fern's `date`: exactly `YYYY-MM-DD` digits. A value outside that shape
/// (`2006-01-02T15:04:05+00:00`, `20200101`, `2020-1-1`, a trailing space) is
/// measured refused; calendar validity is not judged here.
fn is_date(value: &str) -> bool {
    let bytes = value.as_bytes();
    bytes.len() == 10
        && bytes.iter().enumerate().all(|(index, byte)| {
            if index == 4 || index == 7 {
                *byte == b'-'
            } else {
                byte.is_ascii_digit()
            }
        })
}

fn is_integral(value: &Value) -> bool {
    match value {
        Value::Number(number) => {
            number.is_i64()
                || number.is_u64()
                || number.as_f64().is_some_and(|float| float.fract() == 0.0)
        }
        _ => false,
    }
}

/// A scalar example Fern keeps at import and then rejects: a fractional number
/// for an `integer`, or a non-`YYYY-MM-DD` string for a `date`. Examples of the
/// wrong JSON kind (`"7"` for an integer, `7` for a string) are dropped at import
/// and never checked.
fn bad_scalar(schema: &Value, value: &Value) -> bool {
    if is_type(schema, "integer") {
        return matches!(value, Value::Number(_)) && !is_integral(value);
    }
    is_type(schema, "string")
        && str_of(schema, "format") == Some("date")
        && value.as_str().is_some_and(|text| !is_date(text))
}

fn scalar(value: &Value) -> bool {
    !matches!(value, Value::Object(_) | Value::Array(_) | Value::Null)
}

fn literal(value: &Value) -> String {
    serde_json::to_string(value).unwrap_or_else(|_| format!("{value:?}"))
}

/// The first `*json*` media type of a `content` map.
fn json_media(content: Option<&Value>) -> Option<&Value> {
    content?
        .as_object()?
        .iter()
        .find_map(|(media, value)| (media.contains("json") && value.is_object()).then_some(value))
}

impl<'a> Doc<'a> {
    /// [`bad_scalar`], less a `date` example the source writes as a plain
    /// timestamp.
    fn bad_scalar(&self, schema: &Value, value: &Value) -> bool {
        bad_scalar(schema, value) && !self.plain.contains(&std::ptr::from_ref(value))
    }

    fn resolve(&self, mut node: &'a Value) -> Option<&'a Value> {
        for _ in 0..20 {
            let Some(reference) = str_of(node, "$ref") else {
                return Some(node);
            };
            node = yaml_pointer(self.root, reference.strip_prefix('#')?)?;
        }
        None
    }

    fn operations(&self) -> Vec<Operation<'a>> {
        let mut operations = Vec::new();
        let Some(paths) = self.root.get("paths").and_then(Value::as_object) else {
            return operations;
        };
        for (route, item) in paths {
            let route = route.as_str();
            for method in METHODS {
                if let Some(op) = item.get(method) {
                    if op.is_object() && !ignored_reference_node(op) {
                        operations.push(Operation {
                            route,
                            method,
                            item,
                            op,
                        });
                    }
                }
            }
        }
        operations
    }

    /// The operation's `2XX` responses, resolved, in status-code order.
    fn successes(&self, operation: &Operation<'a>) -> Vec<(String, &'a Value)> {
        let mut successes: Vec<(String, &'a Value)> = operation
            .op
            .get("responses")
            .and_then(Value::as_object)
            .into_iter()
            .flatten()
            .filter_map(|(code, response)| {
                let code = code.clone();
                (code.len() == 3 && code.starts_with('2'))
                    .then(|| Some((code, self.resolve(response)?)))?
            })
            .collect();
        successes.sort_by(|left, right| left.0.cmp(&right.0));
        successes
    }

    /// The JSON media of the first success response: the one Fern pairs with the
    /// endpoint's examples (a second `2XX` is never measured to be read).
    fn response_media(&self, operation: &Operation<'a>) -> Option<&'a Value> {
        let (_, response) = self.successes(operation).into_iter().next()?;
        json_media(response.get("content"))
    }

    fn request_media(&self, operation: &Operation<'a>) -> Option<&'a Value> {
        let body = self.resolve(operation.op.get("requestBody")?)?;
        json_media(body.get("content"))
    }

    /// A version header and an ordinary parameter cannot own the same header.
    fn version_header_redeclared(&self, operation: &Operation<'a>) -> Option<(Class, String)> {
        let header = crate::openapi::refusal_version_header(self.root)?;
        self.parameters(operation)
            .into_iter()
            .find_map(|parameter| {
                (str_of(parameter, "in") == Some("header")
                    && str_of(parameter, "name") == Some(header)
                    && parameter.get("required").and_then(Value::as_bool) == Some(true))
                .then(|| {
                    (
                        Class::VersionHeaderRedeclaredAsParameter,
                        format!("header {header} conflicts with version header"),
                    )
                })
            })
    }

    /// Fern checks the path header's example against the operation override's
    /// default. Restrict this refusal to distinct declared string defaults.
    fn header_default_override(&self, operation: &Operation<'a>) -> Option<(Class, String)> {
        let inherited = operation.item.get("parameters")?.as_array()?;
        let local = operation.op.get("parameters")?.as_array()?;
        for parameter in inherited {
            let Some(parameter) = self.resolve(parameter) else {
                continue;
            };
            if str_of(parameter, "in") != Some("header")
                || parameter.get("required").and_then(Value::as_bool) != Some(true)
            {
                continue;
            }
            let Some(name) = str_of(parameter, "name") else {
                continue;
            };
            let Some(default) = parameter
                .get("schema")
                .and_then(|schema| str_of(schema, "default"))
            else {
                continue;
            };
            for replacement in local {
                let Some(replacement) = self.resolve(replacement) else {
                    continue;
                };
                if str_of(replacement, "in") == Some("header")
                    && str_of(replacement, "name") == Some(name)
                    && replacement
                        .get("schema")
                        .and_then(|schema| str_of(schema, "default"))
                        .is_some_and(|value| value != default)
                {
                    return Some((
                        Class::HeaderDefaultDiffersAcrossOperations,
                        format!("header {name} operation default overrides path default"),
                    ));
                }
            }
        }
        None
    }

    fn parameters(&self, operation: &Operation<'a>) -> Vec<&'a Value> {
        [operation.item, operation.op]
            .into_iter()
            .filter_map(|node| node.get("parameters").and_then(Value::as_array))
            .flatten()
            .filter_map(|parameter| self.resolve(parameter))
            .collect()
    }

    /// Every schema reachable from `schema` through `$ref`s, compositions,
    /// properties (only required ones when `required_only`), items and map
    /// values, each visited once; the first `visit` answer wins.
    fn reach(
        &self,
        schema: &'a Value,
        required_only: bool,
        visit: &mut dyn FnMut(&'a Value) -> Option<String>,
    ) -> Option<String> {
        let mut seen = HashSet::new();
        self.reach_from(schema, required_only, visit, &mut seen, 0)
    }

    fn reach_from(
        &self,
        schema: &'a Value,
        required_only: bool,
        visit: &mut dyn FnMut(&'a Value) -> Option<String>,
        seen: &mut HashSet<*const Value>,
        depth: usize,
    ) -> Option<String> {
        if depth > 40 {
            return None;
        }
        let schema = self.resolve(schema)?;
        if !schema.is_object() || !seen.insert(std::ptr::from_ref(schema)) {
            return None;
        }
        if let Some(found) = visit(schema) {
            return Some(found);
        }
        for key in ["allOf", "oneOf", "anyOf"] {
            for member in schema
                .get(key)
                .and_then(Value::as_array)
                .into_iter()
                .flatten()
            {
                if let Some(found) = self.reach_from(member, required_only, visit, seen, depth + 1)
                {
                    return Some(found);
                }
            }
        }
        let required = required_names(schema);
        for (name, property) in schema
            .get("properties")
            .and_then(Value::as_object)
            .into_iter()
            .flatten()
        {
            if required_only && !required.contains(&name.as_str()) {
                continue;
            }
            if let Some(found) = self.reach_from(property, required_only, visit, seen, depth + 1) {
                return Some(found);
            }
        }
        for key in ["items", "additionalProperties"] {
            if let Some(child) = schema.get(key).filter(|child| child.is_object()) {
                if let Some(found) = self.reach_from(child, required_only, visit, seen, depth + 1) {
                    return Some(found);
                }
            }
        }
        None
    }

    /// A tagged operation answering a `$ref`'d JSON object, with an optional
    /// header whose schema `$ref`s a component Fern cannot fill from the header's
    /// name: Fern's example passes the header its own name, then validates it
    /// against the component (Intercom's `Intercom-Version`, General
    /// Translation's `gt-api-version`). An untagged operation, a tag equal to the
    /// `operationId`, an `x-fern-sdk-*` grouping, a required header, an inline
    /// schema, a query or path parameter, a response with no JSON body or a
    /// string body, and a plain string component are each measured accepted; a
    /// declared example or default does not help.
    fn header_name_fallback(&self, operation: &Operation<'a>) -> Option<(Class, String)> {
        let op = operation.op;
        let tag = op
            .get("tags")
            .and_then(Value::as_array)
            .and_then(|tags| tags.first())?;
        if tag.as_str() == str_of(op, "operationId")
            || op
                .as_object()
                .is_some_and(|mapping| mapping.keys().any(|key| key.starts_with("x-fern-sdk")))
        {
            return None;
        }
        let body = self.response_media(operation)?.get("schema")?;
        if str_of(body, "$ref").is_none() || !self.resolve(body).is_some_and(object_or_untyped) {
            return None;
        }
        for parameter in self.parameters(operation) {
            if str_of(parameter, "in") != Some("header")
                || parameter.get("required").and_then(Value::as_bool) == Some(true)
            {
                continue;
            }
            let Some(schema) = parameter.get("schema") else {
                continue;
            };
            if str_of(schema, "$ref").is_none() {
                continue;
            }
            let (Some(target), Some(name)) = (self.resolve(schema), str_of(parameter, "name"))
            else {
                continue;
            };
            let detail = format!("header {name}");
            if is_type(target, "string") {
                if let Some(values) = target.get("enum").and_then(Value::as_array) {
                    if !values.iter().any(|value| value.as_str() == Some(name)) {
                        return Some((Class::ExampleNotEnumValue, detail));
                    }
                    continue;
                }
            }
            if is_type(target, "integer")
                || (is_type(target, "string") && str_of(target, "format") == Some("date"))
            {
                return Some((Class::ExampleTypeMismatch, detail));
            }
        }
        None
    }

    /// An object extending (`allOf`) a `nullable` object with required
    /// properties, while adding properties (its own, or another member's),
    /// anywhere under the first success response: Fern's example of it omits the
    /// parent's required properties, so the check reports them missing whatever
    /// example the document writes, nullable child or not. A non-nullable
    /// parent, a parent without `required` and an `allOf` that adds no
    /// properties are each measured accepted.
    fn nullable_parent_example(&self, operation: &Operation<'a>) -> Option<(Class, String)> {
        let schema = self.response_media(operation)?.get("schema")?;
        self.reach(schema, false, &mut |node| {
            let members = node.get("allOf").and_then(Value::as_array)?;
            let adds = non_empty_mapping(node.get("properties"))
                || members.iter().any(|member| {
                    !self.nullable_parent(member)
                        && self
                            .resolve(member)
                            .is_some_and(|member| non_empty_mapping(member.get("properties")))
                });
            if !adds {
                return None;
            }
            members.iter().find_map(|member| {
                let reference = str_of(member, "$ref")?;
                self.nullable_parent(member)
                    .then(|| format!("response extends nullable {reference}"))
            })
        })
        .map(|detail| (Class::ExampleMissingRequiredProperty, detail))
    }

    /// An inline JSON request body with its own `properties` and an `allOf`
    /// `$ref` parent, where an own `readOnly` property shadows a property the
    /// parent requires: Fern's request example omits the readOnly property yet
    /// validates against the parent's `required`
    /// (bodies-responses/inline-body-readonly-own-overlap). Measured refused
    /// with the request body required or not; the same shadow over an
    /// optional parent property generates.
    fn read_only_shadows_required_parent(
        &self,
        operation: &Operation<'a>,
    ) -> Option<(Class, String)> {
        let schema = self.request_media(operation)?.get("schema")?;
        let properties = schema.get("properties")?.as_object()?;
        let members = schema.get("allOf")?.as_array()?;
        properties.iter().find_map(|(name, property)| {
            let name = name.as_str();
            if property.get("readOnly").and_then(Value::as_bool) != Some(true) {
                return None;
            }
            members.iter().find_map(|member| {
                let reference = str_of(member, "$ref")?;
                let parent = self.resolve(member)?;
                (parent
                    .get("properties")
                    .is_some_and(|properties| properties.get(name).is_some())
                    && required_names(parent).contains(&name))
                .then(|| {
                    (
                        Class::ExampleMissingRequiredProperty,
                        format!(
                            "request property {name:?} is readOnly but required by {reference}"
                        ),
                    )
                })
            })
        })
    }

    /// A discriminated `oneOf`/`anyOf` under the first success response whose
    /// `$ref`'d member restates the discriminant inline while a grandparent
    /// reached through two `allOf` `$ref`s requires it: Fern's example of the
    /// member drops the discriminant yet validates against the required
    /// grandparent (Palo Alto's `ApplicationItem` → `CustomApplication` →
    /// `BaseApplicationWithUrls` → `BaseApplication`). A parent one level up,
    /// no discriminator and a member that does not restate the discriminant are
    /// each measured accepted.
    fn discriminant_required_by_grandparent(
        &self,
        operation: &Operation<'a>,
    ) -> Option<(Class, String)> {
        let schema = self.response_media(operation)?.get("schema")?;
        self.reach(schema, false, &mut |node| {
            let discriminant = node
                .get("discriminator")
                .and_then(|d| str_of(d, "propertyName"))?;
            let members = node
                .get("oneOf")
                .or_else(|| node.get("anyOf"))
                .and_then(Value::as_array)?;
            members.iter().find_map(|member| {
                let reference = str_of(member, "$ref")?;
                let parents = self.resolve(member)?.get("allOf")?.as_array()?;
                let restated = parents.iter().any(|parent| {
                    str_of(parent, "$ref").is_none()
                        && parent
                            .get("properties")
                            .is_some_and(|properties| properties.get(discriminant).is_some())
                });
                let grandparent_requires = parents.iter().any(|parent| {
                    str_of(parent, "$ref").is_some()
                        && self
                            .resolve(parent)
                            .and_then(|parent| parent.get("allOf"))
                            .and_then(Value::as_array)
                            .is_some_and(|grandparents| {
                                grandparents.iter().any(|grandparent| {
                                    str_of(grandparent, "$ref").is_some()
                                        && self.resolve(grandparent).is_some_and(|grandparent| {
                                            required_names(grandparent).contains(&discriminant)
                                        })
                                })
                            })
                });
                (restated && grandparent_requires)
                    .then(|| format!("response member {reference} discriminant {discriminant}"))
            })
        })
        .map(|detail| (Class::ExampleMissingRequiredProperty, detail))
    }

    /// A `$ref` to a `nullable` object that requires properties.
    fn nullable_parent(&self, member: &'a Value) -> bool {
        str_of(member, "$ref").is_some()
            && self.resolve(member).is_some_and(|parent| {
                parent.get("nullable").and_then(Value::as_bool) == Some(true)
                    && object_or_untyped(parent)
                    && !required_names(parent).is_empty()
            })
    }

    /// A schema-level scalar example Fern assembles into the endpoint's example
    /// and then rejects (see [`bad_scalar`]): anywhere under a first success
    /// response that writes no media example, under the required properties of a
    /// request body that writes none (an optional one is left out), and on a
    /// query, path or header parameter.
    fn schema_scalar_example(&self, operation: &Operation<'a>) -> Option<(Class, String)> {
        let mut visit = |node: &'a Value| {
            let example = node.get("example")?;
            (scalar(example) && self.bad_scalar(node, example))
                .then(|| format!("example {}", literal(example)))
        };
        let unexampled =
            |media: &&'a Value| media.get("example").is_none() && media.get("examples").is_none();
        if let Some(schema) = self
            .response_media(operation)
            .filter(unexampled)
            .and_then(|media| media.get("schema"))
        {
            if let Some(detail) = self.reach(schema, false, &mut visit) {
                return Some((Class::ExampleTypeMismatch, format!("response {detail}")));
            }
        }
        if let Some(schema) = self
            .request_media(operation)
            .filter(unexampled)
            .and_then(|media| media.get("schema"))
        {
            if let Some(detail) = self.reach(schema, true, &mut visit) {
                return Some((Class::ExampleTypeMismatch, format!("request {detail}")));
            }
        }
        self.parameters(operation)
            .into_iter()
            .find_map(|parameter| {
                if !matches!(str_of(parameter, "in"), Some("query" | "path" | "header")) {
                    return None;
                }
                let schema = self.resolve(parameter.get("schema")?)?;
                let example = parameter.get("example").or_else(|| schema.get("example"))?;
                (scalar(example) && self.bad_scalar(schema, example)).then(|| {
                    (
                        Class::ExampleTypeMismatch,
                        format!(
                            "parameter {} example {}",
                            str_of(parameter, "name").unwrap_or_default(),
                            literal(example)
                        ),
                    )
                })
            })
    }

    /// The first written media example of the first success response and of the
    /// request body, walked through object properties and array items to a
    /// rejected scalar (see [`bad_scalar`]). Fern lets a written example's
    /// unexpected, missing, non-enum or wrong-kind values through, so only these
    /// are judged.
    fn media_scalar_example(&self, operation: &Operation<'a>) -> Option<(Class, String)> {
        [
            ("response", self.response_media(operation)),
            ("request", self.request_media(operation)),
        ]
        .into_iter()
        .find_map(|(side, media)| {
            let media = media?;
            let schema = media.get("schema")?;
            let example = match media.get("example") {
                Some(example) => example,
                None => {
                    let first = media.get("examples")?.as_object()?.values().next()?;
                    self.resolve(first)?.get("value")?
                }
            };
            self.written_scalar(schema, example, 0)
                .map(|detail| (Class::ExampleTypeMismatch, format!("{side} {detail}")))
        })
    }

    fn written_scalar(&self, schema: &'a Value, value: &Value, depth: usize) -> Option<String> {
        if depth > 40 {
            return None;
        }
        let schema = self.resolve(schema)?;
        match value {
            // An `allOf` lends its members' properties (Zoom's `dashboardMeetings`).
            Value::Object(fields) => fields.iter().find_map(|(name, field)| {
                let name = name.as_str();
                let property = std::iter::once(schema)
                    .chain(
                        schema
                            .get("allOf")
                            .and_then(Value::as_array)
                            .into_iter()
                            .flatten()
                            .filter_map(|member| self.resolve(member)),
                    )
                    .find_map(|owner| owner.get("properties")?.get(name))?;
                self.written_scalar(property, field, depth + 1)
            }),
            Value::Array(items) => {
                let item_schema = schema.get("items").filter(|items| items.is_object())?;
                items
                    .iter()
                    .find_map(|item| self.written_scalar(item_schema, item, depth + 1))
            }
            _ => (scalar(value) && self.bad_scalar(schema, value))
                .then(|| format!("example {}", literal(value))),
        }
    }

    /// A request body declaring `properties` beside a `oneOf`/`anyOf` whose two
    /// or more object members Fern reads as discriminated (they share a
    /// single-value enum property): Fern takes an object property both declare
    /// from the members, so a written request example nesting a key no member
    /// declares there is unexpected, whatever the top level declares (Moffin's
    /// `serviceQueries.renapoCURP` against its members' `renapoCurp`). Measured
    /// accepted: a single member, members without the shared enum, no
    /// top-level `properties`, and a key some member declares.
    fn shadowed_union_property(&self, operation: &Operation<'a>) -> Option<(Class, String)> {
        let media = self.request_media(operation)?;
        let schema = self.resolve(media.get("schema")?)?;
        let top = schema.get("properties").and_then(Value::as_object)?;
        let members = schema
            .get("oneOf")
            .or_else(|| schema.get("anyOf"))
            .and_then(Value::as_array)?;
        if !super::type_not_defined::inferred_discriminant(self.root, members) {
            return None;
        }
        let mut written: Vec<(String, &Value)> = Vec::new();
        if let Some(value) = media.get("example") {
            written.push(("example".to_owned(), value));
        }
        for (name, example) in media
            .get("examples")
            .and_then(Value::as_object)
            .into_iter()
            .flatten()
        {
            if let (name, Some(value)) = (name.as_str(), self.resolve(example)?.get("value")) {
                written.push((format!("examples/{name}"), value));
            }
        }
        for (property, _) in top {
            let property = property.as_str();
            let Some(declared) = self.member_object_keys(members, property) else {
                continue;
            };
            if declared.is_empty() {
                continue;
            }
            for (name, value) in &written {
                let Some(keys) = value.get(property).and_then(Value::as_object) else {
                    continue;
                };
                if let Some(key) = keys.keys().find(|key| !declared.contains(key)) {
                    return Some((
                        Class::ExampleUnexpectedProperty,
                        format!(
                            "request {name} {property}.{}",
                            literal(&Value::String(key.clone()))
                        ),
                    ));
                }
            }
        }
        None
    }

    /// The property names the union members' object declarations of
    /// `property` give, or `None` when a member declares it as anything but a
    /// closed object of named properties.
    fn member_object_keys(&self, members: &'a [Value], property: &str) -> Option<Vec<&'a String>> {
        let mut declared = Vec::new();
        for member in members {
            let Some(nested) = self
                .resolve(member)?
                .get("properties")
                .and_then(|properties| properties.get(property))
            else {
                continue;
            };
            let nested = self.resolve(nested)?;
            if has_composition(nested)
                || !matches!(
                    nested.get("additionalProperties"),
                    None | Some(Value::Bool(false))
                )
            {
                return None;
            }
            declared.extend(nested.get("properties").and_then(Value::as_object)?.keys());
        }
        Some(declared)
    }

    /// `x-fern-examples`, which Fern validates in full: each entry's response
    /// body against the first success response, its request against the JSON
    /// request body and its query parameters against theirs.
    fn fern_examples(&self, operation: &Operation<'a>) -> Option<(Class, String)> {
        let entries = operation.op.get("x-fern-examples")?.as_array()?;
        let response = self
            .response_media(operation)
            .and_then(|media| media.get("schema"));
        let request = self
            .request_media(operation)
            .and_then(|media| media.get("schema"));
        let queries: Vec<(&str, &'a Value)> = self
            .parameters(operation)
            .into_iter()
            .filter(|parameter| str_of(parameter, "in") == Some("query"))
            .filter_map(|parameter| Some((str_of(parameter, "name")?, parameter.get("schema")?)))
            .collect();
        for entry in entries {
            if let (Some(schema), Some(body)) = (
                response,
                entry
                    .get("response")
                    .and_then(|response| response.get("body")),
            ) {
                if let Some((class, detail)) = self.validate(schema, body, 0) {
                    return Some((class, format!("x-fern-examples response {detail}")));
                }
            }
            if let (Some(schema), Some(body)) = (request, entry.get("request")) {
                if let Some((class, detail)) = self.validate(schema, body, 0) {
                    return Some((class, format!("x-fern-examples request {detail}")));
                }
            }
            for (name, value) in entry
                .get("query-parameters")
                .and_then(Value::as_object)
                .into_iter()
                .flatten()
            {
                let Some(schema) = queries
                    .iter()
                    .find(|(query, _)| *query == name.as_str())
                    .map(|(_, schema)| *schema)
                else {
                    continue;
                };
                if let Some((class, detail)) = self.validate(schema, value, 0) {
                    return Some((class, format!("x-fern-examples query {detail}")));
                }
            }
        }
        None
    }

    /// A map or list written as the media-level `example` of a `4XX`/`5XX`
    /// JSON response whose schema is a plain string: Fern validates it against
    /// the error's string type (agatha-budget writes a map of named examples
    /// there). Fern's error type is one per status code across the document, so
    /// this is judged only where every JSON body declared for the code is a
    /// plain string; Webflow's object error examples, whose enum values the same
    /// validation would reject, are accepted. A schema-level example there, and
    /// the same map under a success response, are measured accepted.
    fn error_examples(&self, operation: &Operation<'a>) -> Option<(Class, String)> {
        operation
            .op
            .get("responses")
            .and_then(Value::as_object)
            .into_iter()
            .flatten()
            .find_map(|(code, response)| {
                let code = code.clone();
                if code.len() != 3 || !(code.starts_with('4') || code.starts_with('5')) {
                    return None;
                }
                let media = json_media(self.resolve(response)?.get("content"))?;
                let example = media.get("example")?;
                let schema = self.resolve(media.get("schema")?)?;
                (matches!(example, Value::Object(_) | Value::Array(_))
                    && plain_string(schema)
                    && self.error_bodies(&code).all(plain_string))
                .then(|| {
                    (
                        Class::ExampleTypeMismatch,
                        format!("response {code} example {}", literal(example)),
                    )
                })
            })
    }

    /// A written example that is no object, media-level or named, of a `4xx`/`5xx`
    /// JSON response (a range like `4XX` included) whose schema is an object:
    /// measured at Fern CLI 5.163.1 / fern-python-sdk 5.41.3, `fern check` and
    /// `fern generate` refuse it with `Expected example to be an object`
    /// (`error-*-string-example` probes; Gumlet's JSON-in-a-string `401`
    /// examples). An object example there generates, and so does any example
    /// once another operation declares the code with no body or another schema
    /// (`error-response-*-sibling` controls; Jira's `403`s): Fern's one error
    /// type for the code then validates none.
    fn non_object_error_examples(&self, operation: &Operation<'a>) -> Option<(Class, String)> {
        operation
            .op
            .get("responses")
            .and_then(Value::as_object)
            .into_iter()
            .flatten()
            .find_map(|(code, response)| {
                if code.len() != 3 || !(code.starts_with('4') || code.starts_with('5')) {
                    return None;
                }
                let media = json_media(self.resolve(response)?.get("content"))?;
                let schema = self.resolve(media.get("schema")?)?;
                if !(is_type(schema, "object")
                    || (schema.get("type").is_none() && schema.get("properties").is_some()))
                    || has_composition(schema)
                    || !self
                        .error_body_schemas(code)
                        .all(|body| body.is_some_and(|body| std::ptr::eq(body, schema)))
                {
                    return None;
                }
                let named = media
                    .get("examples")
                    .and_then(Value::as_object)
                    .into_iter()
                    .flatten()
                    .filter_map(|(name, example)| {
                        Some((
                            format!("examples/{name}"),
                            self.resolve(example)?.get("value")?,
                        ))
                    });
                std::iter::once(("example".to_owned(), media.get("example")))
                    .filter_map(|(name, value)| Some((name, value?)))
                    .chain(named)
                    .find(|(_, value)| !value.is_object() && !value.is_null())
                    .map(|(name, value)| {
                        (
                            Class::ExampleTypeMismatch,
                            format!("response {code} {name} {}", literal(value)),
                        )
                    })
            })
    }

    /// The JSON body schema of every operation's response for one error status
    /// code, `None` where that response declares none.
    fn error_body_schemas(&self, code: &str) -> impl Iterator<Item = Option<&'a Value>> + '_ {
        let code = code.to_owned();
        self.operations().into_iter().filter_map(move |operation| {
            let responses = operation.op.get("responses")?.as_object()?;
            let response = responses.iter().find(|(key, _)| key.as_str() == code)?.1;
            Some(
                json_media(self.resolve(response)?.get("content"))
                    .and_then(|media| media.get("schema"))
                    .and_then(|schema| self.resolve(schema)),
            )
        })
    }

    /// Every JSON body schema the document declares for one error status code.
    fn error_bodies(&self, code: &str) -> impl Iterator<Item = &'a Value> + '_ {
        let code = code.to_owned();
        self.operations().into_iter().filter_map(move |operation| {
            let responses = operation.op.get("responses")?.as_object()?;
            let response = responses.iter().find(|(key, _)| key.as_str() == code)?.1;
            let schema = json_media(self.resolve(response)?.get("content"))?.get("schema")?;
            self.resolve(schema)
        })
    }

    /// Fern's validation of a written `x-fern-examples` value, judged only for
    /// the measured outcomes: a missing required property (checked first), an
    /// undeclared property of a closed object, a non-object for an object, a
    /// string outside a string enum, a non-string for a string, a non-integer for
    /// an integer and a non-date for a `date`. A composition, a `null` and every other type pass unjudged.
    fn validate(&self, schema: &'a Value, value: &Value, depth: usize) -> Option<(Class, String)> {
        if depth > 40 || value.is_null() {
            return None;
        }
        let schema = self.resolve(schema)?;
        if has_composition(schema) || schema.get("not").is_some() {
            return None;
        }
        if is_type(schema, "string") {
            if let Some(values) = schema.get("enum").and_then(Value::as_array) {
                let text = value.as_str()?;
                return (!values.iter().any(|member| member.as_str() == Some(text)))
                    .then(|| (Class::ExampleNotEnumValue, literal(value)));
            }
            let Some(text) = value.as_str() else {
                return Some((Class::ExampleTypeMismatch, literal(value)));
            };
            return (str_of(schema, "format") == Some("date")
                && !is_date(text)
                && !self.plain.contains(&std::ptr::from_ref(value)))
            .then(|| (Class::ExampleTypeMismatch, literal(value)));
        }
        if is_type(schema, "integer") {
            return (!is_integral(value)).then(|| (Class::ExampleTypeMismatch, literal(value)));
        }
        if is_type(schema, "array") {
            let item_schema = schema.get("items").filter(|items| items.is_object())?;
            return value
                .as_array()?
                .iter()
                .find_map(|item| self.validate(item_schema, item, depth + 1));
        }
        let properties = schema.get("properties").and_then(Value::as_object);
        if !(is_type(schema, "object") || (schema.get("type").is_none() && properties.is_some())) {
            return None;
        }
        let Some(fields) = value.as_object() else {
            return Some((Class::ExampleTypeMismatch, literal(value)));
        };
        if let Some(missing) = required_names(schema)
            .into_iter()
            .find(|name| !fields.contains_key(*name))
        {
            return Some((Class::ExampleMissingRequiredProperty, missing.to_owned()));
        }
        let closed = matches!(
            schema.get("additionalProperties"),
            None | Some(Value::Bool(false))
        );
        for (name, field) in fields {
            match properties.and_then(|properties| properties.get(name)) {
                Some(property) => {
                    if let Some(found) = self.validate(property, field, depth + 1) {
                        return Some(found);
                    }
                }
                None if closed => {
                    return Some((Class::ExampleUnexpectedProperty, name.as_str().to_owned()));
                }
                None => {}
            }
        }
        None
    }

    fn component_schemas(&self) -> Vec<(&'a str, &'a Value)> {
        self.root
            .get("components")
            .and_then(|components| components.get("schemas"))
            .and_then(Value::as_object)
            .into_iter()
            .flatten()
            .map(|(key, schema)| (key.as_str(), schema))
            .collect()
    }

    /// The first operation whose first success response reaches `target`.
    fn response_reaching(&self, target: &Value) -> Option<String> {
        self.operations().into_iter().find_map(|operation| {
            let schema = self.response_media(&operation)?.get("schema")?;
            self.reach(schema, false, &mut |node| {
                std::ptr::eq(node, target).then(String::new)
            })
            .map(|_| {
                format!(
                    "{} {}",
                    operation.method.to_ascii_uppercase(),
                    operation.route
                )
            })
        })
    }

    /// Two component objects Fern names alike (`Thing_Item`, `ThingItem`): the
    /// later declaration is the one type, and Fern's example of the earlier one,
    /// reached from a response, is validated against it (see
    /// [`collision_class`]). The winner declaring every property (or
    /// `additionalProperties: true`), a loser reached only from a request and an
    /// unreachable loser are measured accepted.
    fn colliding_component(&self) -> Option<(Class, String)> {
        let components = self.component_schemas();
        let names: Vec<String> = components
            .iter()
            .map(|(key, _)| crate::naming::class_name(key))
            .collect();
        for (index, (key, loser)) in components.iter().enumerate() {
            let Some(winner_index) = (index + 1..components.len())
                .rev()
                .find(|other| names[*other] == names[index])
            else {
                continue;
            };
            let (winner_key, winner) = components[winner_index];
            let declared = *loser;
            let merged;
            let loser = if has_composition(loser) {
                let Some(flat) = self.flattened_all_of(loser) else {
                    continue;
                };
                merged = flat;
                &merged
            } else {
                *loser
            };
            let Some(class) = collision_class(loser, winner) else {
                continue;
            };
            if let Some(element) = self.response_reaching(declared) {
                return Some((
                    class,
                    format!("{element} components/schemas/{key} collides with {winner_key}"),
                ));
            }
        }
        None
    }

    /// An `allOf` of plain objects as the one object Fern's example of it is:
    /// every member's properties and required names, members resolved by
    /// reference (Clio's `TaskTemplateList` against `TaskTemplate_List`).
    /// Anything else in the composition is not measured and yields `None`.
    fn flattened_all_of(&self, schema: &'a Value) -> Option<Value> {
        if ["oneOf", "anyOf"]
            .iter()
            .any(|key| schema.get(*key).is_some())
        {
            return None;
        }
        let mut properties = serde_json::Map::new();
        let mut required = Vec::new();
        for member in schema.get("allOf")?.as_array()? {
            let member = self.resolve(member)?;
            if has_composition(member) {
                return None;
            }
            if let Some(own) = member.get("properties").and_then(Value::as_object) {
                properties.extend(own.iter().map(|(key, value)| (key.clone(), value.clone())));
            }
            required.extend(required_names(member).into_iter().map(Value::from));
        }
        let mut flat = serde_json::Map::new();
        flat.insert("properties".into(), properties.into());
        flat.insert("required".into(), required.into());
        Some(flat.into())
    }

    /// A component object's inline property schema named (owner + property)
    /// like a component object declared after it: that component is the one
    /// type, and Fern's example of the inline schema, reached from a response, is
    /// validated against it. An inline `anyOf`/`oneOf` led by a plain string
    /// gives the property's name as a string (Stripe's `subscription.schedule`
    /// against `subscription_schedule`: a type mismatch), as an inline string
    /// enum gives a value (devopness's `CredentialProvider.type` against
    /// `CredentialProviderType`); an inline object is
    /// judged as [`collision_class`] judges a component (Storecove's
    /// `PurchaseInvoice.payment_means` against `PurchaseInvoicePaymentMeans`). A
    /// colliding component declared first, a string component, a union led by
    /// its object member and an unreached owner are measured not to refuse
    /// this way.
    fn colliding_property(&self) -> Option<(Class, String)> {
        let components = self.component_schemas();
        for (index, (key, owner)) in components.iter().enumerate() {
            for (property, schema) in owner
                .get("properties")
                .and_then(Value::as_object)
                .into_iter()
                .flatten()
            {
                let property = property.as_str();
                if str_of(schema, "$ref").is_some() {
                    continue;
                }
                let name = format!(
                    "{}{}",
                    crate::naming::class_name(key),
                    crate::naming::class_name(property)
                );
                let Some((winner_key, winner)) = components[index + 1..]
                    .iter()
                    .find(|(other, _)| crate::naming::class_name(other) == name)
                else {
                    continue;
                };
                if !object_or_untyped(winner)
                    || has_composition(winner)
                    || winner.get("enum").is_some()
                {
                    continue;
                }
                let inline_enum = is_type(schema, "string") && schema.get("enum").is_some();
                let class = if string_led_union(schema) || inline_enum {
                    (winner.get("properties").is_some()
                        || winner.get("additionalProperties").is_some())
                    .then_some(Class::ExampleTypeMismatch)
                } else if object_or_untyped(schema)
                    && !has_composition(schema)
                    && non_empty_mapping(schema.get("properties"))
                {
                    collision_class(schema, winner)
                } else {
                    None
                };
                let Some(class) = class else {
                    continue;
                };
                if let Some(element) = self.response_reaching(owner) {
                    return Some((
                        class,
                        format!(
                            "{element} components/schemas/{key}/properties/{property} collides with {winner_key}"
                        ),
                    ));
                }
            }
        }
        None
    }

    /// A scalar component named like an inline object property of a component
    /// declared after it: the inline object takes the name, so every reference
    /// to the scalar is that object, and Fern's example of the scalar (its
    /// `example`, else a sample) is not an object — PeerTube's `UserRole`
    /// integer enum against `User.role`. An unreferenced scalar is measured
    /// accepted.
    fn scalar_taken_by_inline_object(&self) -> Option<(Class, String)> {
        let components = self.component_schemas();
        for (index, (key, scalar)) in components.iter().enumerate() {
            if !["integer", "number", "string", "boolean"]
                .iter()
                .any(|ty| is_type(scalar, ty))
                || has_composition(scalar)
            {
                continue;
            }
            let name = crate::naming::class_name(key);
            let Some((owner_key, property)) =
                components[index + 1..]
                    .iter()
                    .find_map(|(owner_key, owner)| {
                        owner
                            .get("properties")
                            .and_then(Value::as_object)?
                            .iter()
                            .find_map(|(property, schema)| {
                                let property = property.as_str();
                                (str_of(schema, "$ref").is_none()
                                    && object_or_untyped(schema)
                                    && !has_composition(schema)
                                    && non_empty_mapping(schema.get("properties"))
                                    && format!(
                                        "{}{}",
                                        crate::naming::class_name(owner_key),
                                        crate::naming::class_name(property)
                                    ) == name)
                                    .then_some((*owner_key, property))
                            })
                    })
            else {
                continue;
            };
            if let Some(element) = self.response_reaching(scalar) {
                return Some((
                    Class::ExampleTypeMismatch,
                    format!(
                        "{element} components/schemas/{key} collides with components/schemas/{owner_key}/properties/{property}"
                    ),
                ));
            }
        }
        None
    }

    /// An object whose `allOf` holds a `oneOf` of `$ref`'d members, one of which
    /// declares an inline string enum property: Fern names that enum after the
    /// `allOf` owner (owner + property), so a string enum component of that name
    /// declared after the owner takes it, and Fern's example — the inline enum's
    /// first value, whatever `example` is written — is validated against the
    /// component's values (Alpaca's `Activity` with `TradeActivity.type` against
    /// `ActivityType`).
    fn merged_member_enum(&self) -> Option<(Class, String)> {
        let components = self.component_schemas();
        for (index, (key, owner)) in components.iter().enumerate() {
            let members = owner
                .get("allOf")
                .and_then(Value::as_array)
                .into_iter()
                .flatten()
                .filter_map(|member| member.get("oneOf").and_then(Value::as_array))
                .flatten()
                .filter(|member| str_of(member, "$ref").is_some())
                .filter_map(|member| self.resolve(member));
            for member in members {
                for (property, schema) in member
                    .get("properties")
                    .and_then(Value::as_object)
                    .into_iter()
                    .flatten()
                {
                    let (property, Some(first)) = (
                        property.as_str(),
                        schema
                            .get("enum")
                            .and_then(Value::as_array)
                            .and_then(|values| values.first())
                            .and_then(Value::as_str),
                    ) else {
                        continue;
                    };
                    if str_of(schema, "$ref").is_some() || !is_type(schema, "string") {
                        continue;
                    }
                    let name = format!(
                        "{}{}",
                        crate::naming::class_name(key),
                        crate::naming::class_name(property)
                    );
                    let Some((winner_key, _)) =
                        components[index + 1..].iter().find(|(other, winner)| {
                            crate::naming::class_name(other) == name
                                && is_type(winner, "string")
                                && winner.get("enum").and_then(Value::as_array).is_some_and(
                                    |values| {
                                        !values.iter().any(|value| value.as_str() == Some(first))
                                    },
                                )
                        })
                    else {
                        continue;
                    };
                    if let Some(element) = self.response_reaching(owner) {
                        return Some((
                            Class::ExampleNotEnumValue,
                            format!(
                                "{element} components/schemas/{key} member property {property} collides with {winner_key}"
                            ),
                        ));
                    }
                }
            }
        }
        None
    }
}

/// `type: string` with no enum, format or composition.
fn plain_string(schema: &Value) -> bool {
    is_type(schema, "string")
        && schema.get("enum").is_none()
        && schema.get("format").is_none()
        && !has_composition(schema)
}

/// An inline `anyOf`/`oneOf` of two or more members led by a plain string.
fn string_led_union(schema: &Value) -> bool {
    schema
        .get("anyOf")
        .or_else(|| schema.get("oneOf"))
        .and_then(Value::as_array)
        .filter(|members| members.len() >= 2)
        .is_some_and(|members| {
            let first = &members[0];
            is_type(first, "string")
                && str_of(first, "$ref").is_none()
                && first.get("enum").is_none()
                && first.get("format").is_none()
        })
}

/// Fern's example of the object `loser`, validated against the closed object
/// `winner` that took its name: a required property of the winner the loser
/// lacks is missing (reported first, as Fern reports it); otherwise a plain
/// string property the winner lacks is unexpected (Fern's response example
/// fills a string with its name; other property kinds are not measured).
fn collision_class(loser: &Value, winner: &Value) -> Option<Class> {
    let own = loser.get("properties").and_then(Value::as_object)?;
    let theirs = winner.get("properties").and_then(Value::as_object)?;
    if !matches!(
        winner.get("additionalProperties"),
        None | Some(Value::Bool(false))
    ) || has_composition(winner)
    {
        return None;
    }
    if required_names(winner)
        .into_iter()
        .any(|name| !own.contains_key(name))
    {
        return Some(Class::ExampleMissingRequiredProperty);
    }
    own.iter()
        .any(|(name, property)| {
            !theirs.contains_key(name)
                && str_of(property, "$ref").is_none()
                && is_type(property, "string")
                && property.get("enum").is_none()
                && !has_composition(property)
        })
        .then_some(Class::ExampleUnexpectedProperty)
}

fn required_names(schema: &Value) -> Vec<&str> {
    schema
        .get("required")
        .and_then(Value::as_array)
        .into_iter()
        .flatten()
        .filter_map(Value::as_str)
        .collect()
}

#[cfg(test)]
mod tests {
    use super::*;

    fn yaml(text: &str) -> Value {
        crate::yaml::from_str(text).unwrap()
    }

    #[test]
    fn an_error_example_is_judged_only_where_its_code_has_one_body_throughout() {
        let class = std::path::Path::new(env!("CARGO_MANIFEST_DIR"))
            .join("docs/fern-refusals/example-type-mismatch");
        let verdict = |shape: &str| {
            let text = std::fs::read_to_string(class.join(shape)).unwrap();
            first_violation_in(&yaml(&text), &text).map(|(class, _)| class.id())
        };
        for probe in [
            "error-response-string-example-probe.yml",
            "error-response-two-string-examples-probe.yml",
            "error-response-one-of-two-string-examples-probe.yml",
        ] {
            assert_eq!(verdict(probe), Some("example-type-mismatch"), "{probe}");
        }
        for control in [
            "error-response-bodiless-sibling-control.yml",
            "error-response-other-schema-sibling-control.yml",
        ] {
            assert_eq!(verdict(control), None, "{control}");
        }
    }

    /// The text of each node [`plain_timestamps`] finds in `text`, sorted.
    fn plain_texts(text: &str) -> Vec<String> {
        fn visit(node: &Value, plain: &HashSet<*const Value>, found: &mut Vec<String>) {
            if plain.contains(&std::ptr::from_ref(node)) {
                found.push(node.as_str().unwrap_or_default().to_owned());
            }
            match node {
                Value::Object(fields) => fields.values().for_each(|v| visit(v, plain, found)),
                Value::Array(items) => items.iter().for_each(|v| visit(v, plain, found)),
                _ => {}
            }
        }
        let root = yaml(text);
        let mut found = Vec::new();
        visit(&root, &plain_timestamps(&root, text), &mut found);
        found.sort_unstable();
        found
    }

    #[test]
    fn a_date_example_written_as_a_plain_timestamp_is_no_string_fern_rejects() {
        assert_eq!(
            plain_texts(
                "a:\n  example: 2019-09-15T02:06:58.147Z\n  b: [1706-01-17 00:00:00, x]\n  \
                 l:\n    - 2006-01-02T15:04:05+00:00 # comment\n  c: \"2001-02-03T04:05:06Z\"\n  \
                 d: '2001-02-03T04:05:07Z'\n  e: 2001-02-03T04:05:08Zsuffix\n  \
                 # example: 2001-02-03T04:05:09Z\n  f: x # g: 2001-02-03T04:05:10Z\n  \
                 h: |\n    example: 2001-02-03T04:05:11Z\n  i: 'a # b' # j: 2001-02-03T04:05:12Z\n  \
                 k: \"text: 2001-02-03T04:05:13Z\"\n  m: [\"x\", '2001-02-03T04:05:14Z']\n"
            ),
            [
                "1706-01-17 00:00:00",
                "2006-01-02T15:04:05+00:00",
                "2019-09-15T02:06:58.147Z"
            ]
        );
        // The class probe quotes its datetime; the control writes it plain.
        let class = std::path::Path::new(env!("CARGO_MANIFEST_DIR"))
            .join("docs/fern-refusals/example-type-mismatch");
        let verdict = |shape: &str| {
            let text = std::fs::read_to_string(class.join(shape)).unwrap();
            first_violation_in(&yaml(&text), &text).map(|(class, _)| class.id())
        };
        assert_eq!(verdict("probe.yml"), Some("example-type-mismatch"));
        assert_eq!(verdict("unquoted-date-example-control.yml"), None);
    }

    #[test]
    fn a_quoted_date_example_is_refused_beside_a_plain_copy_of_its_text() {
        // The probe's quoted example, with the same text written plain in a
        // vendor extension elsewhere: each occurrence is judged by its own style.
        let class = std::path::Path::new(env!("CARGO_MANIFEST_DIR"))
            .join("docs/fern-refusals/example-type-mismatch");
        let probe = std::fs::read_to_string(class.join("probe.yml")).unwrap();
        let mixed = probe.replace(
            "info:\n  title: probe\n",
            "info:\n  x-released: 2006-01-02T15:04:05+00:00\n  title: probe\n",
        );
        assert_ne!(mixed, probe);
        let root = yaml(&mixed);
        assert_eq!(
            first_violation_in(&root, &mixed).map(|(class, detail)| (class.id(), detail)),
            first_violation_in(&yaml(&probe), &probe).map(|(class, detail)| (class.id(), detail)),
        );
        assert_eq!(
            first_violation_in(&root, &mixed).map(|(class, _)| class.id()),
            Some("example-type-mismatch")
        );
        // The plain copy is the one occurrence found, and the quoted example is not.
        let plain = plain_timestamps(&root, &mixed);
        assert!(plain.contains(&std::ptr::from_ref(&root["info"]["x-released"])));
        let example = &root["components"]["schemas"]["Thing"]["properties"]["born"]["example"];
        assert!(!plain.contains(&std::ptr::from_ref(example)));
        // Written plain, the example itself is accepted, beside the other copy too.
        let unquoted = mixed.replace(
            "example: \"2006-01-02T15:04:05+00:00\"",
            "example: 2006-01-02T15:04:05+00:00",
        );
        assert_ne!(unquoted, mixed);
        assert_eq!(
            first_violation_in(&yaml(&unquoted), &unquoted).map(|(_, detail)| detail),
            None
        );
    }

    #[test]
    fn an_aliased_or_merged_plain_timestamp_is_plain_where_it_lands() {
        let text = "base: &base {at: 2001-02-03T04:05:06Z, note: x}\n\
                    one: &one 2001-02-03T04:05:07Z\n\
                    copy: *one\n\
                    merged:\n  <<: *base\n  own: '2001-02-03T04:05:08Z'\n\
                    listed:\n  <<: [*base]\n\
                    items: [x, 2001-02-03T04:05:09Z]\n";
        let root = yaml(text);
        let plain = plain_timestamps(&root, text);
        for path in [
            "/base/at",
            "/one",
            "/copy",
            "/merged/at",
            "/listed/at",
            "/items/1",
        ] {
            let node = root
                .pointer(path)
                .unwrap_or_else(|| panic!("{path} parses"));
            assert!(plain.contains(&std::ptr::from_ref(node)), "{path}");
        }
        let own = root.pointer("/merged/own").unwrap();
        assert!(!plain.contains(&std::ptr::from_ref(own)));
        assert_eq!(plain.len(), 6);
    }

    #[test]
    fn a_required_property_beside_a_definitions_member_is_no_unexpected_property() {
        // Measured at Fern CLI 5.163.1 / fern-python-sdk 5.41.3: Fern follows an
        // `allOf` member referenced into a component's own `definitions`, so
        // these shapes (and CommunityToolkit Datasync's `KitchenSink`) generate.
        let class = std::path::Path::new(env!("CARGO_MANIFEST_DIR"))
            .join("docs/fern-refusals/example-unexpected-property");
        for shape in [
            "definitions-member-control.yml",
            "definitions-member-direct-control.yml",
            "definitions-open-member-control.yml",
        ] {
            let root = yaml(&std::fs::read_to_string(class.join(shape)).unwrap());
            assert_eq!(
                first_violation(&root).map(|(_, detail)| detail),
                None,
                "{shape}"
            );
        }
        // The class's probe is still refused.
        let probe = yaml(&std::fs::read_to_string(class.join("probe.yml")).unwrap());
        assert!(
            matches!(
                first_violation(&probe),
                Some((Class::ExampleUnexpectedProperty, _))
            ),
            "{:?}",
            first_violation(&probe).map(|(_, detail)| detail)
        );
    }

    #[test]
    fn a_non_object_example_of_an_object_error_body_is_a_type_mismatch() {
        let class = std::path::Path::new(env!("CARGO_MANIFEST_DIR"))
            .join("docs/fern-refusals/example-type-mismatch");
        let verdict = |shape: &str| {
            first_violation(&yaml(&std::fs::read_to_string(class.join(shape)).unwrap()))
        };
        for (shape, detail) in [
            (
                "error-named-string-example-probe.json",
                "response 401 examples/Result",
            ),
            (
                "error-media-string-example-probe.json",
                "response 401 example",
            ),
            (
                "error-range-string-example-probe.json",
                "response 4XX examples/Result",
            ),
        ] {
            let found = verdict(shape);
            assert!(
                matches!(&found, Some((Class::ExampleTypeMismatch, text)) if text.contains(detail)),
                "{shape}: {:?}",
                found.map(|(_, text)| text)
            );
        }
        assert_eq!(
            verdict("error-object-example-control.json").map(|(_, text)| text),
            None
        );
    }

    #[test]
    fn dates_are_judged_by_shape_and_integers_by_their_fraction() {
        assert!(is_date("2006-01-02"));
        for text in [
            "2006-01-02T15:04:05+00:00",
            "20060102",
            "2006-1-2",
            "2006-01-02 ",
        ] {
            assert!(!is_date(text), "{text}");
        }
        assert!(is_integral(&yaml("7")));
        assert!(is_integral(&yaml("7.0")));
        assert!(!is_integral(&yaml("7.5")));
        assert!(!is_integral(&yaml("'7'")));
        let integer = yaml("{type: integer}");
        assert!(bad_scalar(&integer, &yaml("7.5")));
        // A wrong-kind example is dropped at import, never checked.
        assert!(!bad_scalar(&integer, &yaml("'7.5'")));
        let date = yaml("{type: string, format: date}");
        assert!(bad_scalar(&date, &yaml("'2006-01-02T15:04:05Z'")));
        assert!(!bad_scalar(&date, &yaml("20060102")));
        assert!(!bad_scalar(
            &yaml("{type: string, format: date-time}"),
            &yaml("yesterday")
        ));
    }

    #[test]
    fn written_fern_examples_are_validated_in_full() {
        let root = yaml(
            "components:\n  schemas:\n    Thing:\n      type: object\n      required: [id]\n      \
             properties:\n        id: {type: string}\n        kind: {type: string, enum: [A]}\n",
        );
        let doc = Doc {
            root: &root,
            plain: HashSet::new(),
        };
        let schema = yaml("{$ref: '#/components/schemas/Thing'}");
        let class = |value: &str| {
            doc.validate(&schema, &yaml(value), 0)
                .map(|(class, detail)| format!("{}: {detail}", class.id()))
        };
        assert_eq!(class("{id: a, kind: A}"), None);
        assert_eq!(
            class("{kind: A}").as_deref(),
            Some("example-missing-required-property: id")
        );
        assert_eq!(
            class("{id: a, zzz: 1}").as_deref(),
            Some("example-unexpected-property: zzz")
        );
        assert_eq!(
            class("{id: a, kind: B}").as_deref(),
            Some("example-not-enum-value: \"B\"")
        );
        assert_eq!(
            class("{id: 5}").as_deref(),
            Some("example-type-mismatch: 5")
        );
        assert_eq!(class("x").as_deref(), Some("example-type-mismatch: \"x\""));
        assert_eq!(class("null"), None);
    }
}
