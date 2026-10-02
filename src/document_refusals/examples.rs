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

use serde_yaml_ng::Value;

use super::{ignored_reference_node, yaml_pointer, Class};

const METHODS: [&str; 8] = [
    "get", "put", "post", "delete", "options", "head", "patch", "trace",
];

/// The first example value Fern's check rejects, as the class it reports and
/// the offending element.
pub(super) fn first_violation(root: &Value) -> Option<(Class, String)> {
    let doc = Doc { root };
    for operation in doc.operations() {
        let element = format!(
            "{} {}",
            operation.method.to_ascii_uppercase(),
            operation.route
        );
        let found = doc
            .empty_body_request_examples(&operation)
            .or_else(|| doc.header_name_fallback(&operation))
            .or_else(|| doc.nullable_parent_example(&operation))
            .or_else(|| doc.discriminant_required_by_grandparent(&operation))
            .or_else(|| doc.schema_scalar_example(&operation))
            .or_else(|| doc.media_scalar_example(&operation))
            .or_else(|| doc.fern_examples(&operation))
            .or_else(|| doc.error_examples(&operation));
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

fn has_composition(schema: &Value) -> bool {
    ["allOf", "oneOf", "anyOf"]
        .iter()
        .any(|key| schema.get(*key).is_some())
}

fn non_empty_mapping(value: Option<&Value>) -> bool {
    value
        .and_then(Value::as_mapping)
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
    !matches!(
        value,
        Value::Mapping(_) | Value::Sequence(_) | Value::Null | Value::Tagged(_)
    )
}

fn literal(value: &Value) -> String {
    serde_json::to_string(value).unwrap_or_else(|_| format!("{value:?}"))
}

/// The first `*json*` media type of a `content` map.
fn json_media(content: Option<&Value>) -> Option<&Value> {
    content?.as_mapping()?.iter().find_map(|(media, value)| {
        (media.as_str().is_some_and(|media| media.contains("json")) && value.is_mapping())
            .then_some(value)
    })
}

fn response_code(key: &Value) -> Option<String> {
    match key {
        Value::String(code) => Some(code.clone()),
        Value::Number(code) => Some(code.to_string()),
        _ => None,
    }
}

impl<'a> Doc<'a> {
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
        let Some(paths) = self.root.get("paths").and_then(Value::as_mapping) else {
            return operations;
        };
        for (route, item) in paths {
            let Some(route) = route.as_str() else {
                continue;
            };
            for method in METHODS {
                if let Some(op) = item.get(method) {
                    if op.is_mapping() && !ignored_reference_node(op) {
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
            .and_then(Value::as_mapping)
            .into_iter()
            .flatten()
            .filter_map(|(code, response)| {
                let code = response_code(code)?;
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

    fn parameters(&self, operation: &Operation<'a>) -> Vec<&'a Value> {
        [operation.item, operation.op]
            .into_iter()
            .filter_map(|node| node.get("parameters").and_then(Value::as_sequence))
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
        if !schema.is_mapping() || !seen.insert(std::ptr::from_ref(schema)) {
            return None;
        }
        if let Some(found) = visit(schema) {
            return Some(found);
        }
        for key in ["allOf", "oneOf", "anyOf"] {
            for member in schema
                .get(key)
                .and_then(Value::as_sequence)
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
            .and_then(Value::as_mapping)
            .into_iter()
            .flatten()
        {
            if required_only && !name.as_str().is_some_and(|name| required.contains(&name)) {
                continue;
            }
            if let Some(found) = self.reach_from(property, required_only, visit, seen, depth + 1) {
                return Some(found);
            }
        }
        for key in ["items", "additionalProperties"] {
            if let Some(child) = schema.get(key).filter(|child| child.is_mapping()) {
                if let Some(found) = self.reach_from(child, required_only, visit, seen, depth + 1) {
                    return Some(found);
                }
            }
        }
        None
    }

    /// GitHub's `convertMemberToOutsideCollaborator`: two or more named request
    /// examples, a `204`, and another `2XX` whose JSON body is an object with an
    /// explicitly empty `properties` map. Fern pairs the request examples so that
    /// `examples[0] -> request` is `undefined` (*Expected example to be an
    /// object. Example is: undefined*), whatever the examples hold. One named
    /// example, no `204`, a `205`/`201` in its place, `type: object` without
    /// `properties`, a declared property or `additionalProperties: true` are
    /// each measured accepted.
    fn empty_body_request_examples(&self, operation: &Operation<'a>) -> Option<(Class, String)> {
        let named = self
            .request_media(operation)?
            .get("examples")
            .and_then(Value::as_mapping)?;
        if named.len() < 2 {
            return None;
        }
        let successes = self.successes(operation);
        if !successes.iter().any(|(code, _)| code == "204") {
            return None;
        }
        successes
            .iter()
            .filter(|(code, _)| code != "204")
            .filter_map(|(_, response)| json_media(response.get("content"))?.get("schema"))
            .filter_map(|schema| self.resolve(schema))
            .any(|schema| {
                schema
                    .get("properties")
                    .and_then(Value::as_mapping)
                    .is_some_and(serde_yaml_ng::Mapping::is_empty)
                    && matches!(
                        schema.get("additionalProperties"),
                        None | Some(Value::Bool(false))
                    )
                    && object_or_untyped(schema)
                    && !has_composition(schema)
            })
            .then(|| {
                (
                    Class::ExampleTypeMismatch,
                    "requestBody examples".to_owned(),
                )
            })
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
            .and_then(Value::as_sequence)
            .and_then(|tags| tags.first())?;
        if tag.as_str() == str_of(op, "operationId")
            || op.as_mapping().is_some_and(|mapping| {
                mapping.keys().any(|key| {
                    key.as_str()
                        .is_some_and(|key| key.starts_with("x-fern-sdk"))
                })
            })
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
                if let Some(values) = target.get("enum").and_then(Value::as_sequence) {
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
            let members = node.get("allOf").and_then(Value::as_sequence)?;
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
                .and_then(Value::as_sequence)?;
            members.iter().find_map(|member| {
                let reference = str_of(member, "$ref")?;
                let parents = self.resolve(member)?.get("allOf")?.as_sequence()?;
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
                            .and_then(Value::as_sequence)
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
            (scalar(example) && bad_scalar(node, example))
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
                (scalar(example) && bad_scalar(schema, example)).then(|| {
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
                    let first = media.get("examples")?.as_mapping()?.values().next()?;
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
            Value::Mapping(fields) => fields.iter().find_map(|(name, field)| {
                let name = name.as_str()?;
                let property = std::iter::once(schema)
                    .chain(
                        schema
                            .get("allOf")
                            .and_then(Value::as_sequence)
                            .into_iter()
                            .flatten()
                            .filter_map(|member| self.resolve(member)),
                    )
                    .find_map(|owner| owner.get("properties")?.get(name))?;
                self.written_scalar(property, field, depth + 1)
            }),
            Value::Sequence(items) => {
                let item_schema = schema.get("items").filter(|items| items.is_mapping())?;
                items
                    .iter()
                    .find_map(|item| self.written_scalar(item_schema, item, depth + 1))
            }
            _ => (scalar(value) && bad_scalar(schema, value))
                .then(|| format!("example {}", literal(value))),
        }
    }

    /// `x-fern-examples`, which Fern validates in full: each entry's response
    /// body against the first success response, its request against the JSON
    /// request body and its query parameters against theirs.
    fn fern_examples(&self, operation: &Operation<'a>) -> Option<(Class, String)> {
        let entries = operation.op.get("x-fern-examples")?.as_sequence()?;
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
                .and_then(Value::as_mapping)
                .into_iter()
                .flatten()
            {
                let Some(schema) = queries
                    .iter()
                    .find(|(query, _)| Some(*query) == name.as_str())
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
            .and_then(Value::as_mapping)
            .into_iter()
            .flatten()
            .find_map(|(code, response)| {
                let code = response_code(code)?;
                if code.len() != 3 || !(code.starts_with('4') || code.starts_with('5')) {
                    return None;
                }
                let media = json_media(self.resolve(response)?.get("content"))?;
                let example = media.get("example")?;
                let schema = self.resolve(media.get("schema")?)?;
                (matches!(example, Value::Mapping(_) | Value::Sequence(_))
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

    /// Every JSON body schema the document declares for one error status code.
    fn error_bodies(&self, code: &str) -> impl Iterator<Item = &'a Value> + '_ {
        let code = code.to_owned();
        self.operations().into_iter().filter_map(move |operation| {
            let responses = operation.op.get("responses")?.as_mapping()?;
            let response = responses
                .iter()
                .find(|(key, _)| response_code(key).as_deref() == Some(code.as_str()))?
                .1;
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
            if let Some(values) = schema.get("enum").and_then(Value::as_sequence) {
                let text = value.as_str()?;
                return (!values.iter().any(|member| member.as_str() == Some(text)))
                    .then(|| (Class::ExampleNotEnumValue, literal(value)));
            }
            let Some(text) = value.as_str() else {
                return Some((Class::ExampleTypeMismatch, literal(value)));
            };
            return (str_of(schema, "format") == Some("date") && !is_date(text))
                .then(|| (Class::ExampleTypeMismatch, literal(value)));
        }
        if is_type(schema, "integer") {
            return (!is_integral(value)).then(|| (Class::ExampleTypeMismatch, literal(value)));
        }
        if is_type(schema, "array") {
            let item_schema = schema.get("items").filter(|items| items.is_mapping())?;
            return value
                .as_sequence()?
                .iter()
                .find_map(|item| self.validate(item_schema, item, depth + 1));
        }
        let properties = schema.get("properties").and_then(Value::as_mapping);
        if !(is_type(schema, "object") || (schema.get("type").is_none() && properties.is_some())) {
            return None;
        }
        let Some(fields) = value.as_mapping() else {
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
                    return Some((
                        Class::ExampleUnexpectedProperty,
                        name.as_str().unwrap_or_default().to_owned(),
                    ));
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
            .and_then(Value::as_mapping)
            .into_iter()
            .flatten()
            .filter_map(|(key, schema)| Some((key.as_str()?, schema)))
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
            if has_composition(loser) {
                continue;
            }
            let Some(class) = collision_class(loser, winner) else {
                continue;
            };
            if let Some(element) = self.response_reaching(loser) {
                return Some((
                    class,
                    format!("{element} components/schemas/{key} collides with {winner_key}"),
                ));
            }
        }
        None
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
                .and_then(Value::as_mapping)
                .into_iter()
                .flatten()
            {
                let Some(property) = property.as_str() else {
                    continue;
                };
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
                            .and_then(Value::as_mapping)?
                            .iter()
                            .find_map(|(property, schema)| {
                                let property = property.as_str()?;
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
                .and_then(Value::as_sequence)
                .into_iter()
                .flatten()
                .filter_map(|member| member.get("oneOf").and_then(Value::as_sequence))
                .flatten()
                .filter(|member| str_of(member, "$ref").is_some())
                .filter_map(|member| self.resolve(member));
            for member in members {
                for (property, schema) in member
                    .get("properties")
                    .and_then(Value::as_mapping)
                    .into_iter()
                    .flatten()
                {
                    let (Some(property), Some(first)) = (
                        property.as_str(),
                        schema
                            .get("enum")
                            .and_then(Value::as_sequence)
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
                                && winner.get("enum").and_then(Value::as_sequence).is_some_and(
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
        .and_then(Value::as_sequence)
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
    let own = loser.get("properties").and_then(Value::as_mapping)?;
    let theirs = winner.get("properties").and_then(Value::as_mapping)?;
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
        .and_then(Value::as_sequence)
        .into_iter()
        .flatten()
        .filter_map(Value::as_str)
        .collect()
}

#[cfg(test)]
mod tests {
    use super::*;

    fn yaml(text: &str) -> Value {
        serde_yaml_ng::from_str(text).unwrap()
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
        let doc = Doc { root: &root };
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
