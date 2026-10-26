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
use crate::example_values::{mechanism, python_value, ValueConstraints, Verdict};
use crate::openapi::{AdditionalProperties, OpenApi, Schema};

/// For each `(mechanism, Fern's value as JSON)`, the JSON of every value
/// crozier may write in its place.
pub(super) type Index = BTreeMap<(&'static str, String), BTreeSet<String>>;

/// One value a source node documents: the names Fern may spell it by, and its
/// constraints.
struct Node {
    names: Vec<String>,
    constraints: Box<ValueConstraints>,
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
                constraints,
            });
        }
        for (name, property) in &schema.properties {
            walk(property, &[name.clone()], schemas, out, depth + 1);
        }
        if let Some(items) = &schema.items {
            walk(items, names, schemas, out, depth + 1);
        }
        if let Some(AdditionalProperties::Schema(value)) = &schema.additional_properties {
            walk(value, &[], schemas, out, depth + 1);
        }
        for members in [
            &schema.one_of,
            &schema.any_of,
            &schema.all_of,
            &schema.discarded_all_of,
        ] {
            for member in members.iter().flatten() {
                walk(member, names, schemas, out, depth + 1);
            }
        }
    }
    for (name, schema) in schemas {
        walk(schema, &[name.clone()], schemas, &mut out, 0);
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
        if let Some(constraints) = ValueConstraints::of_parameter(parameter, source) {
            out.push(Node {
                names: names.clone(),
                constraints,
            });
        }
        if let Some(schema) = &parameter.schema {
            walk(schema, &names, schemas, &mut out, 1);
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
    for body in bodies {
        for schema in body
            .content
            .values()
            .filter_map(|media| media.schema.as_ref())
        {
            walk(schema, &["request".to_string()], schemas, &mut out, 0);
        }
    }
    out
}

/// The index of `source`; empty without one.
pub(super) fn index(source: Option<&OpenApi>) -> Index {
    let mut index = Index::new();
    let Some(source) = source else {
        return index;
    };
    let mut seen = BTreeSet::new();
    for node in nodes(source) {
        let constraints = &node.constraints;
        let mut constructions: Vec<(&'static str, Value)> = node
            .names
            .iter()
            .map(|name| (mechanism::NAME, Value::String(name.clone())))
            .collect();
        constructions.push((mechanism::PLACEHOLDER, Value::from("string")));
        constructions.push((mechanism::PLACEHOLDER, Value::from("value")));
        let (min, max) = constraints
            .keywords
            .iter()
            .fold((None, None), |(min, max), keyword| match keyword {
                crate::example_values::Keyword::MinLength(n) => (Some(*n), max),
                crate::example_values::Keyword::MaxLength(n) => (min, Some(*n)),
                _ => (min, max),
            });
        if let Some(sample) = crate::ir::fallback_string_sample(min, max) {
            constructions.push((mechanism::SIZED, Value::String(sample)));
        }
        for number in [Value::from(1), Value::from(1_000_000), Value::from(1.1)] {
            constructions.push((mechanism::NUMBER, number));
        }
        for (id, fern) in constructions {
            if !seen.insert((id, fern.to_string(), format!("{constraints:?}"))) {
                continue;
            }
            if !matches!(constraints.verdict(&fern), Verdict::Rejected(_)) {
                continue;
            }
            if let Some(choice) = constraints.choose(&fern) {
                index
                    .entry((id, key(&fern)))
                    .or_default()
                    .insert(key(choice.value()));
            }
        }
    }
    index
}

/// One token of a Python example line.
#[derive(Debug, PartialEq, Eq)]
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
fn literal_changes<'a>(fern: &'a str, crozier: &'a str) -> Option<Vec<(&'a str, &'a str)>> {
    let (left, right) = (tokens(fern)?, tokens(crozier)?);
    if left.len() != right.len() {
        return None;
    }
    let mut changes = Vec::new();
    for (a, b) in left.iter().zip(&right) {
        match (a, b) {
            _ if a == b => {}
            (Token::Literal(fern), Token::Literal(crozier)) => changes.push((*fern, *crozier)),
            _ => return None,
        }
    }
    (!changes.is_empty()).then_some(changes)
}

/// A value as the index keys it: a number by its numeric value, so the `7`
/// crozier writes for a float matches the `7.0` constructed for it.
fn key(value: &Value) -> String {
    match value {
        Value::Number(number) => number
            .as_f64()
            .map_or_else(|| number.to_string(), |n| format!("{n}")),
        other => other.to_string(),
    }
}

/// Whether the pair's file holds worked examples: `README.md`, `reference.md`
/// or a generated client module.
fn example_file(rel: &str) -> bool {
    rel == "README.md" || rel == "reference.md" || high_level_client(rel)
}

/// Whether the two lines differ only in literals, each of which the index
/// says `id` repairs (a list's items share a line), read without placing the
/// lines in a documented example.
fn indexed(id: &'static str, pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    let Some(changes) = literal_changes(fern, crozier) else {
        return false;
    };
    let index = pair
        .context
        .source_rejected_examples
        .get_or_init(|| index(pair.context.source_document.as_ref()));
    changes.into_iter().all(|(fern_literal, crozier_literal)| {
        let (Some(fern_value), Some(crozier_value)) =
            (python_value(fern_literal), python_value(crozier_literal))
        else {
            return false;
        };
        index
            .get(&(id, key(&fern_value)))
            .is_some_and(|choices| choices.contains(&key(&crozier_value)))
    })
}

/// Whether `fern` and `crozier` are an example line where Fern's value is the
/// one `id`'s construction gives, a source schema rejects it, and crozier's is
/// the value [`ValueConstraints::choose`] picks for that schema.
pub(super) fn holds(id: &'static str, pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
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
    pairs: Vec<(usize, usize, &'static str)>,
    foreign: bool,
}

/// Align the pair as the engine does and read its repairs: inside each run of
/// differing lines, a Fern line and a crozier line pair as a repair where they
/// differ only in literals some mechanism repairs; every other line in the run
/// is a foreign difference.
fn read_repairs(pair: &Pair<'_>) -> Repairs {
    let (fern, crozier) = (pair.fern, pair.crozier);
    let mut repairs = Repairs {
        lengths: (fern.len(), crozier.len()),
        ..Repairs::default()
    };
    let ops = crate::parity::align_lines(fern, crozier);
    let mut index = 0;
    while index < ops.len() {
        if matches!(ops[index], crate::parity::Op::Equal(..)) {
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
        let mut next = 0;
        for i in removed {
            let found = added[next..].iter().enumerate().find_map(|(offset, &j)| {
                mechanism::ALL
                    .into_iter()
                    .find(|id| indexed(id, pair, fern[i], crozier[j]))
                    .map(|id| (offset, j, id))
            });
            match found {
                Some((offset, j, id)) => {
                    repairs.foreign |= offset > 0;
                    repairs.pairs.push((i, j, id));
                    next += offset + 1;
                }
                None => repairs.foreign = true,
            }
        }
        repairs.foreign |= next < added.len();
    }
    repairs
}

/// The same departure as a one-line region, for a file where another
/// difference stands beside the repairs: a region rule that holds the rest of
/// the file to Fern's (as `multipart-object-required-file-example` does) sees
/// a repair as a difference of its own, and region rules apply before line
/// rules. The first line pair `id` repairs is replaced; the engine repeats
/// until none is left. A file whose only differences are repairs is left to
/// the line rule. Replacing one line keeps every other pair's place, so the
/// alignment is read once per file and kept until a pair no longer holds.
pub(super) fn region(id: &'static str, pair: &Pair<'_>) -> Result<Option<Region>, String> {
    if !example_file(pair.rel) || pair.fern == pair.crozier {
        return Ok(None);
    }
    let lengths = (pair.fern.len(), pair.crozier.len());
    let mut cache = pair
        .context
        .rejected_example_repairs
        .lock()
        .map_err(|_| "the rejected-example cache was poisoned".to_string())?;
    for attempt in 0..2 {
        let repairs = match cache.get(pair.rel) {
            Some(repairs) if attempt == 0 && repairs.lengths == lengths => repairs.clone(),
            _ => {
                let repairs = read_repairs(pair);
                cache.insert(pair.rel.to_string(), repairs.clone());
                repairs
            }
        };
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

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn a_line_pair_differs_in_literals_only_or_not_at_all() {
        assert_eq!(
            literal_changes("    guild_id=\"guild_id\",", "    guild_id=\"0\","),
            Some(vec![("\"guild_id\"", "\"0\"")])
        );
        assert_eq!(
            literal_changes("    limit=1,", "    limit=-5,"),
            Some(vec![("1", "-5")])
        );
        assert_eq!(
            literal_changes("    w=[0.2, 1.1, 1.1],", "    w=[0.2, 1.0, 1.0],"),
            Some(vec![("1.1", "1.0"), ("1.1", "1.0")])
        );
        assert_eq!(
            literal_changes("    name=\"name\",", "    name='\"a\"',"),
            Some(vec![("\"name\"", "'\"a\"'")])
        );
        // A changed keyword is no such pair, nor are equal lines.
        assert_eq!(literal_changes("    a=\"a\",", "    b=\"0\","), None);
        assert_eq!(literal_changes("    a=\"a\",", "    a=\"a\","), None);
    }
}
