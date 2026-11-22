//! The rules of the `schema-rejected-*-example` departures: a worked-example
//! line where Fern's value is the one its construction gives, a schema the
//! parsed source document declares rejects it, and crozier's value is the one
//! [`ValueConstraints::choose`] picks for that schema.
//!
//! The source is read once per comparison into an index of every value a
//! parameter or property node of the document can document — each with the
//! names Fern's construction may spell it by and the in-scope keywords it must
//! satisfy — keyed by mechanism and Fern's value, giving the values crozier
//! may write instead.

use std::collections::{BTreeMap, BTreeSet};

use serde_json::Value;

use super::{documented_example_line, high_level_client, Pair, Region};
use crate::example_values::{python_value, Choice, Mechanism, ValueConstraints, Verdict};
use crate::openapi::{AdditionalProperties, OpenApi, Schema};

/// What the source document's schemas let crozier write in place of Fern's
/// constructions.
#[derive(Debug, Default)]
pub(super) struct Index {
    /// For each scalar mechanism, argument and Fern's value, every value
    /// crozier may write in its place. A list's items and a map's values are
    /// keyed by the argument that passes them and by the empty argument, an
    /// item written on a line of its own.
    scalars: BTreeMap<(Mechanism, Argument, ValueKey), BTreeSet<ValueKey>>,
    /// For each list Fern writes with its count of items, every count crozier
    /// may cut or pad it to with copies of its first item.
    lists: BTreeMap<ListKey, BTreeSet<usize>>,
    /// For a `uniqueItems` list: each count crozier may pad Fern's to, with
    /// the item schema its distinct items satisfy.
    unique: BTreeMap<ListKey, Vec<(usize, Box<ValueConstraints>)>>,
    /// For each list keyword, the items a schema's own shape builds where Fern
    /// writes the list empty ([`ValueConstraints::seeded_items`]).
    seeded: BTreeMap<String, Vec<Vec<Value>>>,
    /// Every scalar the document declares: each leaf of an `example`,
    /// `examples` or `default` at any level, a media type's or parameter's,
    /// and each `components.examples` value.
    declared: BTreeSet<ValueKey>,
    /// The constraints of every node, by each argument it is passed as, for
    /// a declared value ([`Mechanism::Declared`]), whose replacement is
    /// chosen when a line is read rather than in advance.
    by_argument: BTreeMap<Argument, Vec<Documented>>,
}

/// One node's constraints and the names Fern's construction spells its value
/// by, as [`Index::by_argument`] keeps them.
#[derive(Debug, PartialEq)]
struct Documented {
    constraints: Box<ValueConstraints>,
    names: Vec<String>,
}

impl Documented {
    /// Whether `value` is one of Fern's own scalar constructions for this
    /// node: a name it documents its value by, the `"string"` or `"value"`
    /// placeholder, the sample Fern's fallback writer sizes by its declared
    /// lengths, or the fixed `1`, `1000000` or `1.1`.
    fn constructed(&self, value: &Value) -> bool {
        match value {
            Value::String(text) => {
                let (min, max) =
                    self.constraints
                        .keywords
                        .iter()
                        .fold((None, None), |(min, max), keyword| match keyword {
                            crate::example_values::Keyword::MinLength(n) => (Some(*n), max),
                            crate::example_values::Keyword::MaxLength(n) => (min, Some(*n)),
                            _ => (min, max),
                        });
                text == "string"
                    || text == "value"
                    || self.names.iter().any(|name| name == text)
                    || crate::ir::fallback_string_sample(min, max).as_deref() == Some(text)
            }
            Value::Number(number) => number
                .as_f64()
                .is_some_and(|n| [1.0, 1_000_000.0, 1.1].contains(&n)),
            _ => false,
        }
    }
}

/// A value as the index keys it: a number by its numeric value, so the `7`
/// crozier writes for a float matches the `7.0` constructed for it.
#[derive(Debug, Clone, PartialEq, Eq, PartialOrd, Ord)]
struct ValueKey(String);

impl ValueKey {
    fn of(value: &Value) -> Self {
        Self(match value {
            Value::Number(number) => number
                .as_f64()
                .map_or_else(|| number.to_string(), |n| format!("{n}")),
            other => other.to_string(),
        })
    }
}

/// What a worked example passes a value as.
#[derive(Debug, Clone, PartialEq, Eq, PartialOrd, Ord)]
enum Argument {
    /// A keyword argument, a model field or a JSON body's key.
    Named(String),
    /// A list's item or a map's value written on a line of its own, whose
    /// argument stands on an earlier line.
    Contained,
}

/// A list argument as Fern writes it: the keyword or key it is passed as, and
/// its count of items.
#[derive(Debug, Clone, PartialEq, Eq, PartialOrd, Ord)]
struct ListKey {
    keyword: String,
    count: usize,
}

/// One value a source node documents: the names Fern may spell it by, and its
/// constraints.
struct Node {
    names: Vec<String>,
    /// The arguments a worked example passes the value as.
    arguments: BTreeSet<Argument>,
    constraints: Box<ValueConstraints>,
}

/// The keywords and keys a value of the wire name `name` is passed as: the
/// name itself (a JSON body's key) and each Python spelling the generator
/// gives an argument or field of it.
fn arguments_of(name: &str) -> BTreeSet<Argument> {
    [
        name.to_owned(),
        crate::naming::field_name(name),
        crate::naming::request_field_name(name),
        crate::naming::model_field_name(name),
    ]
    .into_iter()
    .map(Argument::Named)
    .collect()
}

/// Every value node of `source`: parameters by their names (headers also by
/// Fern's camelCase spelling), properties by theirs, an array's items by the
/// array's name, and a map's values by none (Fern writes its fixed `"value"`).
fn nodes(source: &OpenApi) -> Vec<Node> {
    let schemas = &source.components.schemas;
    let mut out = Vec::new();
    fn walk(
        schema: &Schema,
        names: &[String],
        arguments: &BTreeSet<Argument>,
        schemas: &indexmap::IndexMap<String, Schema>,
        out: &mut Vec<Node>,
        depth: usize,
    ) {
        if depth > 32 {
            return;
        }
        if let Some(constraints) = ValueConstraints::of(schema, schemas) {
            out.push(Node {
                names: names.to_vec(),
                arguments: arguments.clone(),
                constraints,
            });
        }
        walk_inside(schema, names, arguments, schemas, out, depth);
    }
    /// The nodes inside `schema`: its properties, items and map values, and
    /// those of its composition members, which are no value of their own — an
    /// `allOf` member's keywords are already the value's, and a `oneOf` or
    /// `anyOf` member's are an alternative, out of scope.
    fn walk_inside(
        schema: &Schema,
        names: &[String],
        arguments: &BTreeSet<Argument>,
        schemas: &indexmap::IndexMap<String, Schema>,
        out: &mut Vec<Node>,
        depth: usize,
    ) {
        for (name, property) in &schema.properties {
            let mut passed = arguments_of(name);
            passed.extend(
                property
                    .property_name()
                    .map(arguments_of)
                    .unwrap_or_default(),
            );
            walk(
                property,
                std::slice::from_ref(name),
                &passed,
                schemas,
                out,
                depth + 1,
            );
        }
        let mut contained = arguments.clone();
        contained.insert(Argument::Contained);
        if let Some(items) = &schema.items {
            walk(items, names, &contained, schemas, out, depth + 1);
        }
        if let Some(AdditionalProperties::Schema(value)) = &schema.additional_properties {
            walk(value, &[], &contained, schemas, out, depth + 1);
        }
        for members in [
            &schema.one_of,
            &schema.any_of,
            &schema.all_of,
            &schema.discarded_all_of,
        ] {
            for member in members.iter().flatten() {
                walk_inside(member, names, arguments, schemas, out, depth + 1);
            }
        }
    }
    for (name, schema) in schemas {
        walk(
            schema,
            std::slice::from_ref(name),
            &BTreeSet::new(),
            schemas,
            &mut out,
            0,
        );
    }
    let parameters = source
        .components
        .parameters
        .values()
        .chain(source.paths.values().flat_map(|item| {
            item.parameters.iter().chain(
                item.operations()
                    .into_iter()
                    .flat_map(|(_, op)| &op.parameters),
            )
        }));
    for parameter in parameters {
        let mut words = crate::naming::split_words(&parameter.name).into_iter();
        let mut camel = words.next().unwrap_or_default();
        for word in words {
            camel.push_str(&crate::naming::to_pascal_case(&word));
        }
        let names = vec![parameter.name.clone(), camel];
        let mut arguments = arguments_of(&parameter.name);
        arguments.extend(arguments_of(parameter.sdk_name()));
        arguments.insert(Argument::Named(crate::naming::field_name(
            crate::ir::header_param_stem(&parameter.name),
        )));
        // A path parameter named like a body property it spreads beside takes
        // a trailing underscore.
        arguments.insert(Argument::Named(format!(
            "{}_",
            crate::naming::field_name(&parameter.name)
        )));
        if let Some(constraints) = ValueConstraints::of_parameter(parameter, source) {
            out.push(Node {
                names: names.clone(),
                arguments: arguments.clone(),
                constraints,
            });
        }
        if let Some(schema) = &parameter.schema {
            walk_inside(schema, &names, &arguments, schemas, &mut out, 1);
        }
    }
    let bodies = source
        .components
        .request_bodies
        .values()
        .chain(source.paths.values().flat_map(|item| {
            item.operations()
                .into_iter()
                .filter_map(|(_, op)| op.request_body.as_ref())
        }));
    let request: BTreeSet<Argument> = [Argument::Named("request".to_string())]
        .into_iter()
        .collect();
    for body in bodies {
        for schema in body
            .content
            .values()
            .filter_map(|media| media.schema.as_ref())
        {
            walk(
                schema,
                &["request".to_string()],
                &request,
                schemas,
                &mut out,
                0,
            );
        }
    }
    out
}

/// The index of `source`; empty without one.
pub(super) fn index(source: Option<&OpenApi>) -> Index {
    let mut index = Index::default();
    let Some(source) = source else {
        return index;
    };
    let mut seen = BTreeSet::new();
    index.declared = declared_scalars(source);
    for node in nodes(source) {
        let constraints = &node.constraints;
        for argument in &node.arguments {
            let documented = Documented {
                constraints: constraints.clone(),
                names: node.names.clone(),
            };
            let kept = index.by_argument.entry(argument.clone()).or_default();
            if !kept.contains(&documented) {
                kept.push(documented);
            }
        }
        // An empty list's construction: the items its schema's shape builds.
        if matches!(
            constraints.list_view().verdict(&Value::Array(Vec::new())),
            Verdict::Rejected(_)
        ) {
            if let Some(items) = constraints.seeded_items() {
                // A map's values are passed as Fern's fixed `"key"` entry.
                let keywords: Vec<String> = if node.names.is_empty() {
                    vec!["key".to_string()]
                } else {
                    node.names
                        .iter()
                        .flat_map(|name| [name.clone(), crate::naming::field_name(name)])
                        .collect()
                };
                for keyword in keywords {
                    let seeds = index.seeded.entry(keyword).or_default();
                    if !seeds.contains(&items) {
                        seeds.push(items.clone());
                    }
                }
            }
        }
        let mut constructions: Vec<(Mechanism, Value)> = node
            .names
            .iter()
            .map(|name| (Mechanism::Name, Value::String(name.clone())))
            .collect();
        constructions.push((Mechanism::Placeholder, Value::from("string")));
        constructions.push((Mechanism::Placeholder, Value::from("value")));
        let (min, max) = constraints
            .keywords
            .iter()
            .fold((None, None), |(min, max), keyword| match keyword {
                crate::example_values::Keyword::MinLength(n) => (Some(*n), max),
                crate::example_values::Keyword::MaxLength(n) => (min, Some(*n)),
                _ => (min, max),
            });
        if let Some(sample) = crate::ir::fallback_string_sample(min, max) {
            constructions.push((Mechanism::Sized, Value::String(sample)));
        }
        for number in [Value::from(1), Value::from(1_000_000), Value::from(1.1)] {
            constructions.push((Mechanism::Number, number));
        }
        // A list's construction: Fern's one item, or two in its fallback.
        for count in [1usize, 2] {
            let shape = Value::Array(vec![Value::Null; count]);
            let list_view = constraints.list_view();
            if !matches!(list_view.verdict(&shape), Verdict::Rejected(_)) {
                continue;
            }
            if let Some(Choice::Constructed(Value::Array(target))) = list_view.choose(&shape) {
                for name in &node.names {
                    for keyword in [name.clone(), crate::naming::field_name(name)] {
                        let list = ListKey { keyword, count };
                        if constraints.unique_items && target.len() > count {
                            index.unique.entry(list).or_default().push((
                                target.len(),
                                constraints.items.clone().unwrap_or_default(),
                            ));
                        } else {
                            index.lists.entry(list).or_default().insert(target.len());
                        }
                    }
                }
            }
        }
        for (id, fern) in constructions {
            if !seen.insert((
                id,
                fern.to_string(),
                format!("{:?}{constraints:?}", node.arguments),
            )) {
                continue;
            }
            if !matches!(constraints.verdict(&fern), Verdict::Rejected(_)) {
                continue;
            }
            if let Some(choice) = constraints.choose(&fern) {
                for argument in &node.arguments {
                    index
                        .scalars
                        .entry((id, argument.clone(), ValueKey::of(&fern)))
                        .or_default()
                        .insert(ValueKey::of(choice.value()));
                }
            }
        }
    }
    index
}

/// One token of a Python example line.
#[derive(Debug, Clone, PartialEq, Eq)]
enum Token<'a> {
    /// A string or number literal.
    Literal(&'a str),
    /// Anything else, byte for byte.
    Other(&'a str),
}

/// `line` as literal and other tokens: a quoted string (escapes honoured), a
/// number (a `-` that opens a value included), or one character.
fn tokens(line: &str) -> Option<Vec<Token<'_>>> {
    let bytes = line.as_bytes();
    let mut out = Vec::new();
    let mut at = 0;
    while at < bytes.len() {
        let start = at;
        let opens_value = out
            .iter()
            .rev()
            .find(|token| !matches!(token, Token::Other(" ")))
            .is_none_or(|token| matches!(token, Token::Other("=" | "(" | "[" | "," | ":")));
        match bytes[at] {
            quote @ (b'"' | b'\'') => {
                at += 1;
                while at < bytes.len() && bytes[at] != quote {
                    at += if bytes[at] == b'\\' { 2 } else { 1 };
                }
                if at >= bytes.len() {
                    return None;
                }
                at += 1;
                out.push(Token::Literal(&line[start..at]));
            }
            b'0'..=b'9' | b'-'
                if opens_value
                    && (bytes[at] != b'-' || bytes.get(at + 1).is_some_and(u8::is_ascii_digit)) =>
            {
                at += 1;
                while at < bytes.len()
                    && (bytes[at].is_ascii_alphanumeric() || matches!(bytes[at], b'.' | b'_'))
                {
                    at += 1;
                }
                out.push(Token::Literal(&line[start..at]));
            }
            _ => {
                at += line[at..].chars().next().map_or(1, char::len_utf8);
                out.push(Token::Other(&line[start..at]));
            }
        }
    }
    Some(out)
}

/// Fern's and crozier's literals, in order, at every place the two lines
/// differ, when they differ only in literals: `None` when any other token
/// differs, or when nothing does.
fn literal_changes<'a>(fern: &'a str, crozier: &'a str) -> Option<Vec<Change<'a>>> {
    let (left, right) = (tokens(fern)?, tokens(crozier)?);
    if left.len() != right.len() {
        return None;
    }
    let mut changes = Vec::new();
    for (at, (a, b)) in left.iter().zip(&right).enumerate() {
        match (a, b) {
            _ if a == b => {}
            (Token::Literal(fern), Token::Literal(crozier)) => changes.push(Change {
                arguments: arguments_at(&left, at),
                fern,
                crozier,
            }),
            _ => return None,
        }
    }
    (!changes.is_empty()).then_some(changes)
}

/// Fern's literal where the two lines differ in that one literal alone.
pub(super) fn single_literal_change(fern: &str, crozier: &str) -> Option<String> {
    match literal_changes(fern, crozier)?.as_slice() {
        [change] => Some(change.fern.to_owned()),
        _ => None,
    }
}

/// One literal two lines differ in, with the arguments its line passes it as.
#[derive(Debug, PartialEq, Eq)]
struct Change<'a> {
    arguments: Vec<Argument>,
    fern: &'a str,
    crozier: &'a str,
}

/// The arguments the literal at `at` of a line's `tokens` is passed as: the
/// keyword its `name=` names; else the key of its `"key": ` entry and the
/// keyword of the bracket it stands in on this line, or, where that bracket
/// opens on an earlier line, the empty argument every list's items and map's
/// values are keyed by too.
fn arguments_at(tokens: &[Token<'_>], at: usize) -> Vec<Argument> {
    let before: Vec<&Token<'_>> = tokens[..at]
        .iter()
        .filter(|token| !matches!(token, Token::Other(" ")))
        .collect();
    let keyword = |end: usize| -> Option<String> {
        let name: String = before[..end]
            .iter()
            .rev()
            .map_while(|token| match token {
                Token::Other(c) if c.chars().all(|c| c.is_alphanumeric() || c == '_') => Some(*c),
                _ => None,
            })
            .collect::<Vec<_>>()
            .into_iter()
            .rev()
            .collect();
        (!name.is_empty()).then_some(name)
    };
    if let Some(Token::Other("=")) = before.last() {
        return keyword(before.len() - 1)
            .map(Argument::Named)
            .into_iter()
            .collect();
    }
    let mut out = Vec::new();
    if let (Some(Token::Other(":")), Some(Token::Literal(key))) = (
        before.last(),
        before.len().checked_sub(2).map(|k| before[k]),
    ) {
        if let Some(Value::String(key)) = python_value(key) {
            out.push(Argument::Named(key));
        }
    }
    let mut depth = 0usize;
    let mut enclosing = None;
    for (index, token) in before.iter().enumerate().rev() {
        match token {
            Token::Other("]" | ")" | "}") => depth += 1,
            Token::Other("[" | "(" | "{") if depth > 0 => depth -= 1,
            Token::Other("[" | "(" | "{") => {
                if let (Some(Token::Other("=")), Some(name)) = (
                    index.checked_sub(1).map(|k| before[k]),
                    keyword(index.saturating_sub(1)),
                ) {
                    enclosing = Some(name);
                }
                break;
            }
            _ => {}
        }
    }
    // Only where the line names no argument around the literal does it stand
    // on a line of its own, an item or entry of an argument named above.
    out.push(enclosing.map_or(Argument::Contained, Argument::Named));
    out
}

/// Whether the pair's file holds worked examples: `README.md`, `reference.md`
/// or a generated client module.
fn example_file(rel: &str) -> bool {
    rel == "README.md" || rel == "reference.md" || high_level_client(rel)
}

/// Whether the two lines differ only in literals, each of which the index
/// says `id` repairs (a list's items share a line), read without placing the
/// lines in a documented example.
fn indexed(id: Mechanism, pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    let Some(changes) = literal_changes(fern, crozier) else {
        return false;
    };
    let index = pair
        .context
        .source_rejected_examples
        .get_or_init(|| index(pair.context.source_document.as_ref()));
    changes
        .into_iter()
        .all(|change| index.scalar(id, &change.arguments, change.fern, change.crozier))
}

/// Every scalar `source` declares as a value: the leaves of each `example`,
/// `examples` and `default` of its schemas, parameters and media types, and of
/// its `components.examples`.
fn declared_scalars(source: &OpenApi) -> BTreeSet<ValueKey> {
    fn leaves(value: &Value, out: &mut BTreeSet<ValueKey>) {
        match value {
            Value::Array(items) => items.iter().for_each(|item| leaves(item, out)),
            Value::Object(entries) => entries.values().for_each(|entry| leaves(entry, out)),
            scalar => {
                out.insert(ValueKey::of(scalar));
            }
        }
    }
    let mut out = BTreeSet::new();
    super::visit_source_schemas(Some(source), &mut |schema| {
        for value in schema
            .example
            .iter()
            .chain(&schema.examples)
            .chain(&schema.default)
        {
            leaves(value, &mut out);
        }
    });
    let named = |examples: &indexmap::IndexMap<String, crate::openapi::ParameterExample>,
                 out: &mut BTreeSet<ValueKey>| {
        for example in examples
            .values()
            .filter_map(|example| example.value.as_ref())
        {
            leaves(example, out);
        }
    };
    let media = |content: &indexmap::IndexMap<String, crate::openapi::MediaType>,
                 out: &mut BTreeSet<ValueKey>| {
        for media in content.values() {
            if let Some(example) = &media.example {
                leaves(example, out);
            }
            named(&media.examples, out);
        }
    };
    named(&source.components.examples, &mut out);
    let parameters = source
        .components
        .parameters
        .values()
        .chain(source.paths.values().flat_map(|item| {
            item.parameters.iter().chain(
                item.operations()
                    .into_iter()
                    .flat_map(|(_, op)| &op.parameters),
            )
        }));
    for parameter in parameters {
        if let Some(example) = &parameter.example {
            leaves(example, &mut out);
        }
        named(&parameter.examples, &mut out);
        media(&parameter.content, &mut out);
    }
    for body in source.components.request_bodies.values() {
        media(&body.content, &mut out);
    }
    for response in source.components.responses.values() {
        media(&response.content, &mut out);
    }
    for item in source.paths.values() {
        for (_, operation) in item.operations() {
            if let Some(body) = &operation.request_body {
                media(&body.content, &mut out);
            }
            for response in operation.responses.values() {
                media(&response.content, &mut out);
            }
        }
    }
    out
}

impl Index {
    /// Whether crozier's literal is a value `id`'s repair writes in place of
    /// Fern's for a schema one of `arguments` documents.
    fn scalar(&self, id: Mechanism, arguments: &[Argument], fern: &str, crozier: &str) -> bool {
        let (Some(fern), Some(crozier)) = (python_value(fern), python_value(crozier)) else {
            return false;
        };
        if id == Mechanism::Declared {
            return self.declared_holds(arguments, &fern, &crozier);
        }
        arguments.iter().any(|argument| {
            self.scalars
                .get(&(id, argument.clone(), ValueKey::of(&fern)))
                .is_some_and(|choices| choices.contains(&ValueKey::of(&crozier)))
        })
    }
}

impl Index {
    /// See [`super::Context::admits_nothing`].
    pub(super) fn admits_nothing(&self, argument: &str, value: &str) -> bool {
        let leaf = argument.rsplit('.').next().unwrap_or(argument);
        let leaf = leaf.split('[').next().unwrap_or(leaf);
        let kind = python_value(value).unwrap_or_else(|| Value::String(value.to_owned()));
        self.by_argument
            .get(&Argument::Named(leaf.to_owned()))
            .is_some_and(|nodes| {
                nodes
                    .iter()
                    .any(|node| node.constraints.admits_nothing(&kind))
            })
    }

    /// [`Mechanism::Declared`]: Fern's value is one the document declares and
    /// no construction of Fern's for the node, the node's schema (one of
    /// `arguments` documents) rejects it, and crozier's is the value
    /// [`ValueConstraints::choose`] picks for that schema, or Fern's own
    /// construction for the node where the schema accepts that.
    fn declared_holds(&self, arguments: &[Argument], fern: &Value, crozier: &Value) -> bool {
        self.declared.contains(&ValueKey::of(fern))
            && arguments.iter().any(|argument| {
                self.by_argument.get(argument).is_some_and(|nodes| {
                    nodes.iter().any(|node| {
                        let constraints = &node.constraints;
                        // A value that is also a construction of Fern's for the
                        // node is that construction's to account for.
                        !node.constructed(fern)
                            && matches!(constraints.verdict(fern), Verdict::Rejected(_))
                            && (constraints.choose(fern).is_some_and(|choice| {
                                ValueKey::of(choice.value()) == ValueKey::of(crozier)
                            }) || node.constructed(crozier)
                                && std::mem::discriminant(fern) == std::mem::discriminant(crozier)
                                && constraints.verdict(crozier) == Verdict::Accepted)
                    })
                })
            })
    }

    /// Whether crozier's items of the list passed as `keyword`, which Fern
    /// writes empty, are those a schema of that keyword's shape builds.
    fn seeded_holds(&self, keyword: &str, crozier: &[Vec<Tree<'_>>]) -> bool {
        self.seeded.get(keyword).is_some_and(|choices| {
            choices.iter().any(|seed| {
                seed.len() == crozier.len()
                    && seed
                        .iter()
                        .zip(crozier)
                        .all(|(value, item)| tree_matches(item, value))
            })
        })
    }
}

/// Whether an example item's trees spell `value`, as the writer spells a
/// JSON value: a literal, `None`, `True` or `False`; a list item by item; a
/// dict, or a model's constructor, entry by entry (its keywords the
/// properties' Python names); an enum's member (`Kind.EQ`) for its string.
fn tree_matches(trees: &[Tree<'_>], value: &Value) -> bool {
    let words: Option<String> = trees
        .iter()
        .map(|tree| match tree {
            Tree::Token(Token::Other(text)) => Some(*text),
            _ => None,
        })
        .collect();
    match (trees, value) {
        ([Tree::Token(Token::Literal(literal))], _) => {
            python_value(literal).is_some_and(|parsed| ValueKey::of(&parsed) == ValueKey::of(value))
        }
        ([Tree::Group(Bracket::Square, elements)], Value::Array(items)) => {
            elements.len() == items.len()
                && elements
                    .iter()
                    .zip(items)
                    .all(|(element, item)| tree_matches(element, item))
        }
        ([Tree::Group(Bracket::Curly, elements)], Value::Object(entries)) => {
            elements.len() == entries.len()
                && elements.iter().all(|element| match element.as_slice() {
                    [Tree::Token(Token::Literal(key)), Tree::Token(Token::Other(":")), rest @ ..] =>
                    {
                        matches!(python_value(key), Some(Value::String(key))
                            if entries.get(&key).is_some_and(|entry| tree_matches(rest, entry)))
                    }
                    _ => false,
                })
        }
        (_, Value::Object(entries)) => {
            let Some((Tree::Group(Bracket::Round, elements), name)) = trees.split_last() else {
                return false;
            };
            let constructor = name.iter().all(|tree| {
                matches!(tree, Tree::Token(Token::Other(text))
                    if text.chars().all(|c| c.is_alphanumeric() || c == '_' || c == '.'))
            });
            constructor
                && !name.is_empty()
                && elements.len() == entries.len()
                && elements.iter().all(|element| {
                    let Some(at) = element
                        .iter()
                        .position(|tree| matches!(tree, Tree::Token(Token::Other("="))))
                    else {
                        return false;
                    };
                    let Some(keyword) = keyword_before(element, at + 1) else {
                        return false;
                    };
                    entries.iter().any(|(key, entry)| {
                        (crate::naming::field_name(key) == keyword
                            || crate::naming::model_field_name(key) == keyword)
                            && tree_matches(&element[at + 1..], entry)
                    })
                })
        }
        (_, Value::String(text)) => words.is_some_and(|words| {
            words.rsplit_once('.').is_some_and(|(owner, member)| {
                !owner.is_empty() && member == crate::naming::enum_member_name(text)
            })
        }),
        (_, Value::Null) => words.as_deref() == Some("None"),
        (_, Value::Bool(flag)) => words.as_deref() == Some(if *flag { "True" } else { "False" }),
        _ => false,
    }
}

/// Whether `fern` and `crozier` are an example line where Fern's value is the
/// one `id`'s construction gives, a source schema rejects it, and crozier's is
/// the value [`ValueConstraints::choose`] picks for that schema.
pub(super) fn holds(id: Mechanism, pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    example_file(pair.rel)
        && indexed(id, pair, fern, crozier)
        // A value the document declares for the argument is kept, not repaired,
        // even where a same-named schema elsewhere would repair Fern's placeholder
        // to it: crystalshards' multipart `version` is exampled `1.0.0`.
        && !super::declared_values::declared_example_over_placeholder(pair, fern, crozier)
        && documented_example_line(pair.rel, pair.fern, fern)
        && documented_example_line(pair.rel, pair.crozier, crozier)
}

/// The repairs of one file pair, as aligned when last read: each Fern and
/// crozier line pair a mechanism repairs, and whether any other difference
/// stands beside them.
#[derive(Debug, Clone, Default)]
pub(super) struct Repairs {
    /// The lengths of the two sides the alignment was read at.
    lengths: (usize, usize),
    /// A digest of Fern's lines, which no region changes.
    reference: u64,
    pairs: Vec<(usize, usize, Mechanism)>,
    /// The list arguments `schema-rejected-array-length-example` repairs,
    /// each with crozier's lines as they were read.
    arrays: Vec<(Region, Vec<String>)>,
    /// Each crozier line's Fern counterpart in the alignment.
    counterpart: Vec<Option<usize>>,
    foreign: bool,
}

/// A digest of Fern's side of a pair, which no region changes: a cached
/// analysis is reused only for the same reference file.
fn digest(lines: &[&str]) -> u64 {
    use std::hash::{Hash, Hasher};
    let mut hasher = std::collections::hash_map::DefaultHasher::new();
    lines.hash(&mut hasher);
    hasher.finish()
}

/// Align the pair as the engine does and read its repairs: inside each run of
/// differing lines, a Fern line and a crozier line pair as a repair where they
/// differ only in literals some mechanism repairs; every other line in the run
/// is a foreign difference.
fn read_repairs(pair: &Pair<'_>) -> Repairs {
    let (fern, crozier) = (pair.fern, pair.crozier);
    let mut repairs = Repairs {
        lengths: (fern.len(), crozier.len()),
        reference: digest(fern),
        ..Repairs::default()
    };
    let ops = crate::parity::align_lines(fern, crozier);
    let mut runs = Vec::new();
    // Each crozier line's Fern counterpart: an equal line, or the line at the
    // same place in a run of lines that differ.
    let mut counterpart = vec![None; crozier.len()];
    let mut index = 0;
    while index < ops.len() {
        if let crate::parity::Op::Equal(i, j) = ops[index] {
            counterpart[j] = Some(i);
            index += 1;
            continue;
        }
        let (mut removed, mut added) = (Vec::new(), Vec::new());
        while let Some(op) = ops.get(index) {
            match *op {
                crate::parity::Op::Delete(i) => removed.push(i),
                crate::parity::Op::Insert(j) => added.push(j),
                crate::parity::Op::Equal(..) => break,
            }
            index += 1;
        }
        for (&j, &i) in added.iter().zip(&removed) {
            counterpart[j] = Some(i);
        }
        runs.push((removed, added));
    }
    repairs.counterpart.clone_from(&counterpart);
    repairs.arrays = array_regions(pair, &counterpart)
        .into_iter()
        .map(|region| {
            let lines = crozier[region.crozier.clone()]
                .iter()
                .map(|line| (*line).to_string())
                .collect();
            (region, lines)
        })
        .collect();
    let in_array = |line: usize, crozier_side: bool| {
        repairs.arrays.iter().any(|(region, _)| {
            let range = if crozier_side {
                &region.crozier
            } else {
                &region.fern
            };
            range.contains(&line)
        })
    };
    for (removed, added) in runs {
        let removed: Vec<usize> = removed
            .into_iter()
            .filter(|i| !in_array(*i, false))
            .collect();
        let added: Vec<usize> = added.into_iter().filter(|j| !in_array(*j, true)).collect();
        let mut next = 0;
        let mut pairs = Vec::new();
        let mut foreign = false;
        for i in removed {
            let found = added[next..].iter().enumerate().find_map(|(offset, &j)| {
                Mechanism::SCALAR
                    .into_iter()
                    .find(|id| indexed(*id, pair, fern[i], crozier[j]))
                    .map(|id| (offset, j, id))
            });
            match found {
                Some((offset, j, id)) => {
                    foreign |= offset > 0;
                    pairs.push((i, j, id));
                    next += offset + 1;
                }
                None => foreign = true,
            }
        }
        repairs.foreign |= foreign || next < added.len();
        repairs.pairs.extend(pairs);
    }
    repairs
}

/// The file pair's analysis, read once per alignment: kept while the two
/// sides keep their lengths, which a one-line region does, and read again
/// once a region changes one.
fn analysis(pair: &Pair<'_>, fresh: bool) -> Result<Repairs, String> {
    let lengths = (pair.fern.len(), pair.crozier.len());
    let mut cache = pair
        .context
        .rejected_example_repairs
        .lock()
        .map_err(|_| "the rejected-example cache was poisoned".to_string())?;
    if !fresh {
        if let Some(repairs) = cache
            .get(pair.rel)
            .filter(|repairs| repairs.lengths == lengths && repairs.reference == digest(pair.fern))
        {
            return Ok(repairs.clone());
        }
    }
    let repairs = read_repairs(pair);
    cache.insert(pair.rel.to_string(), repairs.clone());
    Ok(repairs)
}

/// The same departure as a one-line region, for a file where another
/// difference stands beside the repairs: a region rule that holds the rest of
/// the file to Fern's (as `multipart-object-required-file-example` does) sees
/// a repair as a difference of its own, and region rules apply before line
/// rules. The first line pair `id` repairs is replaced; the engine repeats
/// until none is left. A file whose only differences are repairs is left to
/// the line rule. Replacing one line keeps every other pair's place, so the
/// alignment is read once per file and kept until a pair no longer holds.
pub(super) fn region(id: Mechanism, pair: &Pair<'_>) -> Result<Option<Region>, String> {
    if !example_file(pair.rel) || pair.fern == pair.crozier {
        return Ok(None);
    }
    for fresh in [false, true] {
        let repairs = analysis(pair, fresh)?;
        if !repairs.foreign {
            break;
        }
        let pending = repairs
            .pairs
            .iter()
            .find(|(i, j, found)| *found == id && pair.fern[*i] != pair.crozier[*j]);
        match pending {
            None => break,
            Some(&(i, j, _)) if holds(id, pair, pair.fern[i], pair.crozier[j]) => {
                return Ok(Some(Region {
                    fern: i..i + 1,
                    crozier: j..j + 1,
                }));
            }
            Some(_) => {}
        }
    }
    Ok(wrapped_single_item_region(id, pair))
}

/// A one-item list whose repaired value is too long for one line: Fern's
/// `<indent>name=["name"],` where crozier's formatter wraps
/// `<indent>name=[`, `<indent>    "repaired"`, `<indent>],` (walletd's
/// `addresses`, whose `Hash256` pattern rejects the name). The repair is
/// judged as if crozier's value stood on Fern's one line.
fn wrapped_single_item_region(id: Mechanism, pair: &Pair<'_>) -> Option<Region> {
    let (fern, crozier) = (pair.fern, pair.crozier);
    (1..crozier.len().saturating_sub(2)).find_map(|at| {
        let open = crozier[at];
        if !open.ends_with("=[") || crozier[at + 2].trim() != "]," {
            return None;
        }
        let value = crozier[at + 1].trim();
        let unwrapped = format!("{open}{value}],");
        let line = (1..fern.len()).find(|&line| {
            fern[line - 1] == crozier[at - 1]
                && fern.get(line + 1) == crozier.get(at + 3)
                && fern[line] != unwrapped
                && indexed(id, pair, fern[line], &unwrapped)
                // What `holds` asks of a one-line repair: no value the document
                // declares, and an example line on both sides, never runtime code.
                && !super::declared_values::declared_example_over_placeholder(
                    pair,
                    fern[line],
                    &unwrapped,
                )
                && documented_example_line(pair.rel, pair.fern, fern[line])
                && documented_example_line(pair.rel, pair.crozier, open)
        })?;
        Some(Region {
            fern: line..line + 1,
            crozier: at..at + 3,
        })
    })
}

/// One item of a list argument: its text with whitespace outside literals
/// dropped, and the lines (0-based) its first and last characters stand on.
#[derive(Debug, Clone, PartialEq, Eq)]
struct ListItem {
    text: String,
    first: usize,
    last: usize,
}

/// A list passed as a keyword argument or a dict entry: what precedes its
/// `[` on its opening line, its items, and the line its `]` closes on.
#[derive(Debug, Clone, PartialEq, Eq)]
struct ListArgument {
    keyword: String,
    items: Vec<ListItem>,
    close: usize,
}

/// The list argument opening on line `start` of `lines`, if one does: the
/// text before its first `[` outside a literal is `name=` or `"key": `.
fn list_argument(lines: &[&str], start: usize) -> Option<ListArgument> {
    let line = lines.get(start)?;
    let mut quote = None;
    let mut escaped = false;
    let mut open = None;
    for (at, character) in line.char_indices() {
        if let Some(delimiter) = quote {
            if escaped {
                escaped = false;
            } else if character == '\\' {
                escaped = true;
            } else if character == delimiter {
                quote = None;
            }
        } else if matches!(character, '"' | '\'') {
            quote = Some(character);
        } else if character == '[' {
            open = Some(at);
            break;
        }
    }
    let open = open?;
    let prefix = line[..open].trim();
    // A list on a line of its own is an item of the list enclosing it, and its
    // schema is that list's item schema, which the index files under the same
    // name: RS-Server's `interval=[[None]]` spans lines with the inner `[` bare.
    let keyword = if prefix.is_empty() {
        enclosing_list(lines, start)
            .and_then(|outer| list_argument(lines, outer))?
            .keyword
    } else if let Some(name) = prefix.strip_suffix('=') {
        name.chars()
            .all(|c| c.is_alphanumeric() || c == '_')
            .then(|| name.to_string())?
    } else {
        // A dict entry's key, the dict opening on this line or not:
        // `cell_ids_to_output={"key": [...]}`.
        let entry = prefix.rsplit(['{', ',']).next().unwrap_or(prefix);
        serde_json::from_str::<String>(entry.trim().strip_suffix(':')?.trim()).ok()?
    };
    let mut items = Vec::new();
    let mut current: Option<ListItem> = None;
    let (mut depth, mut quote, mut escaped) = (0usize, None, false);
    let mut position = (start, open + 1);
    loop {
        let (index, from) = position;
        let text = lines.get(index)?;
        for character in text[from..].chars() {
            let push = |current: &mut Option<ListItem>, character: char| {
                let item = current.get_or_insert_with(|| ListItem {
                    text: String::new(),
                    first: index,
                    last: index,
                });
                item.text.push(character);
                item.last = index;
            };
            if let Some(delimiter) = quote {
                push(&mut current, character);
                if escaped {
                    escaped = false;
                } else if character == '\\' {
                    escaped = true;
                } else if character == delimiter {
                    quote = None;
                }
                continue;
            }
            match character {
                '"' | '\'' => {
                    quote = Some(character);
                    push(&mut current, character);
                }
                '[' | '(' | '{' => {
                    depth += 1;
                    push(&mut current, character);
                }
                ']' if depth == 0 => {
                    items.extend(current.take());
                    return Some(ListArgument {
                        keyword,
                        items,
                        close: index,
                    });
                }
                ']' | ')' | '}' => {
                    depth = depth.checked_sub(1)?;
                    push(&mut current, character);
                }
                ',' if depth == 0 => items.extend(current.take()),
                c if c.is_whitespace() => {}
                c => push(&mut current, c),
            }
        }
        position = (index + 1, 0);
    }
}

/// The line opening the list that holds line `start` as an item: the nearest
/// earlier line leaving more `[` open than the lines between it and `start`
/// close. Brackets inside a literal do not count.
fn enclosing_list(lines: &[&str], start: usize) -> Option<usize> {
    let mut open = 0isize;
    for at in (0..start).rev() {
        let (mut quote, mut escaped) = (None, false);
        for character in lines[at].chars() {
            if let Some(delimiter) = quote {
                if escaped {
                    escaped = false;
                } else if character == '\\' {
                    escaped = true;
                } else if character == delimiter {
                    quote = None;
                }
            } else if matches!(character, '"' | '\'') {
                quote = Some(character);
            } else if character == '[' {
                open += 1;
            } else if character == ']' {
                open -= 1;
            }
        }
        if open > 0 {
            return Some(at);
        }
    }
    None
}

/// An example value read as nested brackets: tokens, and bracketed groups of
/// comma-separated elements.
#[derive(Debug, Clone, PartialEq, Eq)]
enum Tree<'a> {
    Token(Token<'a>),
    Group(Bracket, Vec<Vec<Tree<'a>>>),
}

/// The bracket a group opens with.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
enum Bracket {
    /// `[`, a list.
    Square,
    /// `(`, a call or tuple.
    Round,
    /// `{`, a dict.
    Curly,
}

/// The comma-separated elements from `at` up to the token `close` (the end of
/// `tokens` where `None`); `None` where the brackets do not balance. A
/// trailing comma ends no element.
fn elements<'a>(
    tokens: &[Token<'a>],
    at: &mut usize,
    close: Option<&str>,
) -> Option<Vec<Vec<Tree<'a>>>> {
    let mut out = vec![Vec::new()];
    while let Some(token) = tokens.get(*at) {
        *at += 1;
        match token {
            Token::Other(other) if Some(*other) == close => {
                out.retain(|element| !element.is_empty());
                return Some(out);
            }
            Token::Other(open @ ("[" | "(" | "{")) => {
                let (bracket, closer) = match *open {
                    "[" => (Bracket::Square, "]"),
                    "(" => (Bracket::Round, ")"),
                    _ => (Bracket::Curly, "}"),
                };
                let inner = elements(tokens, at, Some(closer))?;
                out.last_mut()?.push(Tree::Group(bracket, inner));
            }
            Token::Other("]" | ")" | "}") => return None,
            Token::Other(",") if close.is_some() => out.push(Vec::new()),
            other => out.last_mut()?.push(Tree::Token(other.clone())),
        }
    }
    close.is_none().then(|| {
        out.retain(|element| !element.is_empty());
        out
    })
}

/// One list item's trees; `None` where its brackets do not balance or it
/// holds more than one top-level element.
fn tree(text: &str) -> Option<Vec<Tree<'_>>> {
    let tokens = tokens(text)?;
    let mut elements = elements(&tokens, &mut 0, None)?;
    match elements.len() {
        0 => Some(Vec::new()),
        1 => elements.pop(),
        _ => None,
    }
}

/// The keyword (`name=`) or dict key (`"key": `) whose value the tree at
/// `at` of `trees` is.
fn keyword_before(trees: &[Tree<'_>], at: usize) -> Option<String> {
    match trees.get(at.checked_sub(1)?)? {
        Tree::Token(Token::Other("=")) => {
            let name: String = trees[..at - 1]
                .iter()
                .rev()
                .map_while(|tree| match tree {
                    Tree::Token(Token::Other(c))
                        if c.chars().all(|c| c.is_alphanumeric() || c == '_') =>
                    {
                        Some(*c)
                    }
                    _ => None,
                })
                .collect::<Vec<_>>()
                .into_iter()
                .rev()
                .collect();
            (!name.is_empty()).then_some(name)
        }
        Tree::Token(Token::Other(":")) => match trees.get(at.checked_sub(2)?)? {
            Tree::Token(Token::Literal(key)) => match python_value(key)? {
                Value::String(key) => Some(key),
                _ => None,
            },
            _ => None,
        },
        _ => None,
    }
}

/// Whether Fern's literal and crozier's are a repair some scalar mechanism
/// makes: Fern's that construction's value, crozier's the one its schema's
/// repair chooses.
fn scalar_holds(index: &Index, arguments: &[Argument], fern: &str, crozier: &str) -> bool {
    Mechanism::SCALAR
        .into_iter()
        .any(|id| index.scalar(id, arguments, fern, crozier))
}

/// Whether crozier's value differs from Fern's only by repairs: literals a
/// scalar mechanism repairs, and lists [`list_holds`] accounts for, at any
/// depth.
fn trees_hold(index: &Index, passed: &str, fern: &[Tree<'_>], crozier: &[Tree<'_>]) -> bool {
    fern.len() == crozier.len()
        && fern
            .iter()
            .zip(crozier)
            .enumerate()
            .all(|(at, pair)| match pair {
                (left, right) if left == right => true,
                (Tree::Token(Token::Literal(left)), Tree::Token(Token::Literal(right))) => {
                    let arguments = vec![Argument::Named(
                        keyword_before(fern, at).unwrap_or_else(|| passed.to_owned()),
                    )];
                    scalar_holds(index, &arguments, left, right)
                }
                (Tree::Group(open, left), Tree::Group(other, right)) if open == other => {
                    let keyword = keyword_before(fern, at).unwrap_or_else(|| passed.to_owned());
                    if left.len() == right.len() {
                        left.iter()
                            .zip(right)
                            .all(|(l, r)| trees_hold(index, &keyword, l, r))
                    } else {
                        *open == Bracket::Square && list_holds(index, &keyword, left, right)
                    }
                }
                _ => false,
            })
}

/// Whether, at any depth, a list Fern writes empty stands where crozier's
/// holds items.
fn seeds_a_nested_list(fern: &[Tree<'_>], crozier: &[Tree<'_>]) -> bool {
    fern.len() == crozier.len()
        && fern.iter().zip(crozier).any(|pair| match pair {
            (Tree::Group(Bracket::Square, left), Tree::Group(Bracket::Square, right)) => {
                (left.is_empty() && !right.is_empty())
                    || left.len() == right.len()
                        && left
                            .iter()
                            .zip(right)
                            .any(|(l, r)| seeds_a_nested_list(l, r))
            }
            (Tree::Group(_, left), Tree::Group(_, right)) if left.len() == right.len() => left
                .iter()
                .zip(right)
                .any(|(l, r)| seeds_a_nested_list(l, r)),
            _ => false,
        })
}

/// Whether crozier's items of the list passed as `keyword` are Fern's, cut
/// or padded to the count a source schema chooses for it: Fern's kept items
/// hold ([`trees_hold`]), and every added one is a copy of the first or,
/// beneath `uniqueItems`, exactly the distinct items the item schema builds.
fn list_holds(
    index: &Index,
    keyword: &str,
    fern: &[Vec<Tree<'_>>],
    crozier: &[Vec<Tree<'_>>],
) -> bool {
    let (count, target) = (fern.len(), crozier.len());
    if count == target {
        return false;
    }
    if count == 0 {
        return index.seeded_holds(keyword, crozier);
    }
    let kept = fern
        .iter()
        .zip(crozier)
        .all(|(f, c)| trees_hold(index, keyword, f, c));
    let list = ListKey {
        keyword: keyword.to_owned(),
        count,
    };
    let copies = crozier[count.min(target)..]
        .iter()
        .all(|item| crozier.first().is_some_and(|first| item == first))
        && index
            .lists
            .get(&list)
            .is_some_and(|targets| targets.contains(&target));
    let distinct = || {
        let values: Option<Vec<Value>> = crozier
            .iter()
            .map(|item| match item.as_slice() {
                [Tree::Token(Token::Literal(literal))] => python_value(literal),
                _ => None,
            })
            .collect();
        let Some(values) = values else {
            return false;
        };
        index.unique.get(&list).is_some_and(|choices| {
            choices.iter().any(|(length, items)| {
                *length == target
                    && items
                        .distinct_items(&values[..count.min(target)], target)
                        .is_some_and(|built| {
                            built.iter().map(ValueKey::of).collect::<Vec<_>>()
                                == values.iter().map(ValueKey::of).collect::<Vec<_>>()
                        })
            })
        })
    };
    kept && (copies || distinct())
}

/// The list arguments `schema-rejected-array-length-example` accounts for:
/// a list of an example whose item count a source schema's `minItems` or
/// `maxItems` rejects, where crozier keeps Fern's items (each the same, or
/// differing only in literals another mechanism repairs) cut or padded to the
/// count the schema's repair chooses, every added item a copy of the first.
/// Where the list spans lines, only its added items are the region, so the
/// first item's own repairs stay lines of their own; a list on one line, or
/// one cut short, is the whole list.
fn array_regions(pair: &Pair<'_>, counterpart: &[Option<usize>]) -> Vec<Region> {
    let (fern, crozier) = (pair.fern, pair.crozier);
    let index = pair
        .context
        .source_rejected_examples
        .get_or_init(|| self::index(pair.context.source_document.as_ref()));
    let mut regions = Vec::new();
    for (j, line) in crozier.iter().enumerate() {
        if !line.contains('[') {
            continue;
        }
        let Some(i) = counterpart[j] else {
            continue;
        };
        let (Some(theirs), Some(ours)) = (list_argument(fern, i), list_argument(crozier, j)) else {
            continue;
        };
        let (count, target) = (theirs.items.len(), ours.items.len());
        if theirs.keyword != ours.keyword
            || theirs
                .items
                .iter()
                .map(|item| &item.text)
                .eq(ours.items.iter().map(|item| &item.text))
        {
            continue;
        }
        let fern_items: Option<Vec<Vec<Tree<'_>>>> =
            theirs.items.iter().map(|item| tree(&item.text)).collect();
        let crozier_items: Option<Vec<Vec<Tree<'_>>>> =
            ours.items.iter().map(|item| tree(&item.text)).collect();
        let (Some(fern_items), Some(crozier_items)) = (fern_items, crozier_items) else {
            continue;
        };
        let holds = if count == target {
            // Same count, but an item is itself a list padded from nothing:
            // `windows=[[]]` beside `windows=[[None, None]]`.
            fern_items != crozier_items
                && fern_items
                    .iter()
                    .zip(&crozier_items)
                    .any(|(f, c)| seeds_a_nested_list(f, c))
                && fern_items
                    .iter()
                    .zip(&crozier_items)
                    .all(|(f, c)| trees_hold(index, &ours.keyword, f, c))
        } else {
            list_holds(index, &ours.keyword, &fern_items, &crozier_items)
        };
        if !(holds && documented_example_line(pair.rel, crozier, line)) {
            continue;
        }
        let whole_list = Region {
            fern: i..theirs.close + 1,
            crozier: j..ours.close + 1,
        };
        if count == 0 || target <= count || (i == theirs.close && j == ours.close) {
            regions.push(whole_list);
            continue;
        }
        let (last, ours_last) = (&theirs.items[count - 1], &ours.items[count - 1]);
        regions.push(if last.first == i || ours_last.first == j {
            whole_list
        } else {
            Region {
                fern: last.last..last.last + 1,
                crozier: ours_last.last..ours.items[target - 1].last + 1,
            }
        });
    }
    regions
}

/// The names a `from <module> import <names>` line imports, with its module.
fn imported_names(line: &str) -> Option<(&str, Vec<&str>)> {
    let rest = line.trim().strip_prefix("from ")?;
    let (module, names) = rest.split_once(" import ")?;
    let names: Vec<&str> = names.split(',').map(str::trim).collect();
    names
        .iter()
        .all(|name| !name.is_empty() && name.chars().all(|c| c.is_alphanumeric() || c == '_'))
        .then_some((module, names))
}

/// Whether `name` occurs in `line` as a whole identifier.
fn holds_identifier(line: &str, name: &str) -> bool {
    let word = |c: char| c.is_alphanumeric() || c == '_';
    line.match_indices(name).any(|(at, _)| {
        !line[..at].chars().next_back().is_some_and(word)
            && !line[at + name.len()..].chars().next().is_some_and(word)
    })
}

/// `schema-rejected-array-length-example`'s example import line: a worked
/// example's `from <package> import …` where crozier's line keeps every name
/// Fern's imports, from the same module, and each name it adds is one a list
/// this departure seeds from nothing writes (sim-tables'
/// `TablePredicateAllAllItemField`, constructed in `all_=[…]` where Fern's
/// list is empty).
/// `opening` is crozier's line the import opens on, which is `crozier` itself
/// unless the formatter wrapped it.
fn seeded_import(pair: &Pair<'_>, fern: &str, crozier: &str, opening: &str) -> bool {
    let (Some((module, theirs)), Some((other, ours))) =
        (imported_names(fern), imported_names(crozier))
    else {
        return false;
    };
    if module != other
        || !example_file(pair.rel)
        || !theirs.iter().all(|name| ours.contains(name))
        || ours.len() == theirs.len()
    {
        return false;
    }
    let Ok(repairs) = analysis(pair, false) else {
        return false;
    };
    let seeded: Vec<&str> = repairs
        .arrays
        .iter()
        .filter(|(region, _)| {
            pair.fern
                .get(region.fern.clone())
                .is_some_and(|lines| lines.iter().any(|line| line.contains("[]")))
        })
        .flat_map(|(_, lines)| lines.iter().map(String::as_str))
        .collect();
    ours.iter()
        .filter(|name| !theirs.contains(name))
        .all(|name| seeded.iter().any(|line| holds_identifier(line, name)))
        && documented_example_line(pair.rel, pair.fern, fern)
        && documented_example_line(pair.rel, pair.crozier, opening)
}

/// The example import line [`seeded_import`] accounts for, as a region read
/// before the lists it names are: Fern's one line beside crozier's, which its
/// formatter may wrap in parentheses one name a line (`from <module> import
/// (` to its `)`), paired as the comparison aligns them.
fn seeded_import_region(pair: &Pair<'_>) -> Option<Region> {
    let (fern, crozier) = (pair.fern, pair.crozier);
    if !example_file(pair.rel) || fern == crozier {
        return None;
    }
    let counterpart = analysis(pair, false).ok()?.counterpart;
    (1..crozier.len()).find_map(|open| {
        let text = crozier[open].trim();
        let indent = &crozier[open][..crozier[open].len() - crozier[open].trim_start().len()];
        let (close, joined) = match text.strip_suffix(" import (") {
            Some(head) => {
                let module = head.strip_prefix("from ")?;
                let close = (open + 1..crozier.len()).find(|&at| crozier[at].trim() == ")")?;
                let names: Vec<&str> = crozier[open + 1..close]
                    .iter()
                    .map(|line| line.trim().trim_end_matches(','))
                    .collect();
                (
                    close,
                    format!("{indent}from {module} import {}", names.join(", ")),
                )
            }
            None => {
                imported_names(text)?;
                (open, crozier[open].to_string())
            }
        };
        let line = counterpart.get(open).copied().flatten()?;
        if !(fern[line] != joined && seeded_import(pair, fern[line], &joined, crozier[open])) {
            return None;
        }
        Some(Region {
            fern: line..line + 1,
            crozier: open..close + 1,
        })
    })
}

/// `schema-rejected-array-length-example`'s region rule: the first list
/// [`array_regions`] found that still differs.
pub(super) fn array_region(pair: &Pair<'_>) -> Result<Option<Region>, String> {
    if !example_file(pair.rel) || pair.fern == pair.crozier {
        return Ok(None);
    }
    // The import of a model a seeded list constructs is read while the list
    // still stands.
    if let Some(region) = seeded_import_region(pair) {
        return Ok(Some(region));
    }
    // A one-line region keeps both sides' lengths and every list's place, so
    // the analysis stands until a region changes a length; a list whose lines
    // are neither what was read nor Fern's is read again.
    for fresh in [false, true] {
        let mut stale = false;
        for (region, read) in analysis(pair, fresh)?.arrays {
            let current = pair.crozier.get(region.crozier.clone());
            if current == pair.fern.get(region.fern.clone()) {
                continue;
            }
            if current
                .is_some_and(|lines| lines.iter().copied().eq(read.iter().map(String::as_str)))
            {
                return Ok(Some(region));
            }
            stale = true;
            break;
        }
        if !stale {
            return Ok(None);
        }
    }
    Ok(None)
}

#[cfg(test)]
mod tests {
    use super::*;

    /// The literals two lines differ in, each with the arguments it is read as.
    fn changes(fern: &str, crozier: &str) -> Option<Vec<(Vec<Argument>, String, String)>> {
        literal_changes(fern, crozier).map(|changes| {
            changes
                .into_iter()
                .map(|change| {
                    (
                        change.arguments,
                        change.fern.to_owned(),
                        change.crozier.to_owned(),
                    )
                })
                .collect()
        })
    }

    /// The arguments `items` name, the empty one a contained value's.
    fn strings(items: &[&str]) -> Vec<Argument> {
        items
            .iter()
            .map(|item| {
                if item.is_empty() {
                    Argument::Contained
                } else {
                    Argument::Named((*item).to_owned())
                }
            })
            .collect()
    }

    #[test]
    fn a_line_pair_differs_in_literals_only_or_not_at_all() {
        assert_eq!(
            changes("    guild_id=\"guild_id\",", "    guild_id=\"0\","),
            Some(vec![(
                strings(&["guild_id"]),
                "\"guild_id\"".into(),
                "\"0\"".into()
            )])
        );
        assert_eq!(
            changes("    limit=1,", "    limit=-5,"),
            Some(vec![(strings(&["limit"]), "1".into(), "-5".into())])
        );
        // A list's items are read as its argument's, or as a bare item.
        assert_eq!(
            changes("    w=[0.2, 1.1],", "    w=[0.2, 1.0],"),
            Some(vec![(strings(&["w"]), "1.1".into(), "1.0".into())])
        );
        // An entry by its key; an item on a line of its own as a bare item.
        assert_eq!(
            changes("        \"key\": \"value\",", "        \"key\": \"0\","),
            Some(vec![(
                strings(&["key", ""]),
                "\"value\"".into(),
                "\"0\"".into()
            )])
        );
        assert_eq!(
            changes("        \"ids\",", "        \"0\","),
            Some(vec![(strings(&[""]), "\"ids\"".into(), "\"0\"".into())])
        );
        assert_eq!(
            changes("    name=\"name\",", "    name='\"a\"',"),
            Some(vec![(
                strings(&["name"]),
                "\"name\"".into(),
                "'\"a\"'".into()
            )])
        );
        // A changed keyword is no such pair, nor are equal lines.
        assert_eq!(changes("    a=\"a\",", "    b=\"0\","), None);
        assert_eq!(changes("    a=\"a\",", "    a=\"a\","), None);
    }
}
