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
    scalars: BTreeMap<(Mechanism, String, ValueKey), BTreeSet<ValueKey>>,
    /// For each list Fern writes with its count of items, every count crozier
    /// may cut or pad it to with copies of its first item.
    lists: BTreeMap<ListKey, BTreeSet<usize>>,
    /// For a `uniqueItems` list: each count crozier may pad Fern's to, with
    /// the item schema its distinct items satisfy.
    unique: BTreeMap<ListKey, Vec<(usize, Box<ValueConstraints>)>>,
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
    arguments: BTreeSet<String>,
    constraints: Box<ValueConstraints>,
}

/// The keywords and keys a value of the wire name `name` is passed as: the
/// name itself (a JSON body's key) and each Python spelling the generator
/// gives an argument or field of it.
fn arguments_of(name: &str) -> BTreeSet<String> {
    [
        name.to_owned(),
        crate::naming::field_name(name),
        crate::naming::request_field_name(name),
        crate::naming::model_field_name(name),
    ]
    .into_iter()
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
        arguments: &BTreeSet<String>,
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
        arguments: &BTreeSet<String>,
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
        contained.insert(String::new());
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
        arguments.insert(crate::naming::field_name(crate::ir::header_param_stem(
            &parameter.name,
        )));
        // A path parameter named like a body property it spreads beside takes
        // a trailing underscore.
        arguments.insert(format!("{}_", crate::naming::field_name(&parameter.name)));
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
    let request: BTreeSet<String> = ["request".to_string()].into_iter().collect();
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
    for node in nodes(source) {
        let constraints = &node.constraints;
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

/// One literal two lines differ in, with the arguments its line passes it as.
#[derive(Debug, PartialEq, Eq)]
struct Change<'a> {
    arguments: Vec<String>,
    fern: &'a str,
    crozier: &'a str,
}

/// The arguments the literal at `at` of a line's `tokens` is passed as: the
/// keyword its `name=` names; else the key of its `"key": ` entry and the
/// keyword of the bracket it stands in on this line, or, where that bracket
/// opens on an earlier line, the empty argument every list's items and map's
/// values are keyed by too.
fn arguments_at(tokens: &[Token<'_>], at: usize) -> Vec<String> {
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
        return keyword(before.len() - 1).into_iter().collect();
    }
    let mut out = Vec::new();
    if let (Some(Token::Other(":")), Some(Token::Literal(key))) = (
        before.last(),
        before.len().checked_sub(2).map(|k| before[k]),
    ) {
        if let Some(Value::String(key)) = python_value(key) {
            out.push(key);
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
    out.push(enclosing.unwrap_or_default());
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

impl Index {
    /// Whether crozier's literal is a value `id`'s repair writes in place of
    /// Fern's for a schema one of `arguments` documents.
    fn scalar(&self, id: Mechanism, arguments: &[String], fern: &str, crozier: &str) -> bool {
        let (Some(fern), Some(crozier)) = (python_value(fern), python_value(crozier)) else {
            return false;
        };
        arguments.iter().any(|argument| {
            self.scalars
                .get(&(id, argument.clone(), ValueKey::of(&fern)))
                .is_some_and(|choices| choices.contains(&ValueKey::of(&crozier)))
        })
    }
}

/// Whether `fern` and `crozier` are an example line where Fern's value is the
/// one `id`'s construction gives, a source schema rejects it, and crozier's is
/// the value [`ValueConstraints::choose`] picks for that schema.
pub(super) fn holds(id: Mechanism, pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    example_file(pair.rel)
        && indexed(id, pair, fern, crozier)
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
            return Ok(None);
        }
        let pending = repairs
            .pairs
            .iter()
            .find(|(i, j, found)| *found == id && pair.fern[*i] != pair.crozier[*j]);
        match pending {
            None => return Ok(None),
            Some(&(i, j, _)) if holds(id, pair, pair.fern[i], pair.crozier[j]) => {
                return Ok(Some(Region {
                    fern: i..i + 1,
                    crozier: j..j + 1,
                }));
            }
            Some(_) => {}
        }
    }
    Ok(None)
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
    let keyword = if let Some(name) = prefix.strip_suffix('=') {
        name.chars()
            .all(|c| c.is_alphanumeric() || c == '_')
            .then(|| name.to_string())?
    } else {
        serde_json::from_str::<String>(prefix.strip_suffix(':')?.trim()).ok()?
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
fn scalar_holds(index: &Index, arguments: &[String], fern: &str, crozier: &str) -> bool {
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
                    let arguments =
                        vec![keyword_before(fern, at).unwrap_or_else(|| passed.to_owned())];
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
    if count == 0 || count == target {
        return false;
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
        if theirs.keyword != ours.keyword || count == target || count == 0 {
            continue;
        }
        let fern_items: Option<Vec<Vec<Tree<'_>>>> =
            theirs.items.iter().map(|item| tree(&item.text)).collect();
        let crozier_items: Option<Vec<Vec<Tree<'_>>>> =
            ours.items.iter().map(|item| tree(&item.text)).collect();
        let (Some(fern_items), Some(crozier_items)) = (fern_items, crozier_items) else {
            continue;
        };
        if !(list_holds(index, &ours.keyword, &fern_items, &crozier_items)
            && documented_example_line(pair.rel, crozier, line))
        {
            continue;
        }
        let whole_list = Region {
            fern: i..theirs.close + 1,
            crozier: j..ours.close + 1,
        };
        if target < count || (i == theirs.close && j == ours.close) {
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

/// `schema-rejected-array-length-example`'s region rule: the first list
/// [`array_regions`] found that still differs.
pub(super) fn array_region(pair: &Pair<'_>) -> Result<Option<Region>, String> {
    if !example_file(pair.rel) || pair.fern == pair.crozier {
        return Ok(None);
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
    fn changes(fern: &str, crozier: &str) -> Option<Vec<(Vec<String>, String, String)>> {
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

    fn strings(items: &[&str]) -> Vec<String> {
        items.iter().map(|item| (*item).to_owned()).collect()
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
