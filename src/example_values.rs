//! Worked-example values a schema rejects, and the value crozier writes in
//! their place.
//!
//! Fern constructs a worked example's value without checking the schema it
//! documents: a string is written as its own parameter or property name, so
//! discord's `guild_id` is `"guild_id"` beneath `pattern: ^(0|[1-9][0-9]*)$`.
//! [`ValueConstraints`] holds the in-scope validation keywords of the schema one
//! value documents, read once from the parsed document; [`ValueConstraints::verdict`]
//! decides whether a value satisfies them, and [`ValueConstraints::choose`] picks
//! the value crozier writes instead: the schema's own declared example, else its
//! `default`, each only when the schema accepts it, else a value constructed
//! deterministically to satisfy every keyword. `docs/departures/evidence/invalid-example-values/`
//! records every such value in the committed Fern trees.
//!
//! The keywords in scope are a string's `pattern`, `minLength`, `maxLength`,
//! `enum` and `const`; a number's `minimum`, `maximum`, `exclusiveMinimum`,
//! `exclusiveMaximum` and `multipleOf`; an array's `minItems` and `maxItems`;
//! and the formats [`Format`] names. Any other keyword or format is out of scope:
//! it neither rejects a value here nor blocks a repair.

use std::fmt;

use serde_json::Value;

use indexmap::IndexMap;

use crate::openapi::{OpenApi, Schema};

/// A `format` whose violation rejects a value; every other format is an
/// annotation here.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum Format {
    /// RFC 3339 `full-date`.
    Date,
    /// RFC 3339 `date-time`.
    DateTime,
    /// RFC 3339 `full-time`.
    Time,
    /// RFC 4122's hyphenated UUID.
    Uuid,
    /// An address `local@domain`.
    Email,
    /// RFC 3986 `URI`.
    Uri,
    /// A dotted-quad IPv4 address.
    Ipv4,
    /// An IPv6 address.
    Ipv6,
    /// RFC 1123 host name.
    Hostname,
    /// The signed 32-bit integer range.
    Int32,
    /// The signed 64-bit integer range.
    Int64,
}

impl Format {
    /// Every format in scope.
    pub const ALL: [Format; 11] = [
        Format::Date,
        Format::DateTime,
        Format::Time,
        Format::Uuid,
        Format::Email,
        Format::Uri,
        Format::Ipv4,
        Format::Ipv6,
        Format::Hostname,
        Format::Int32,
        Format::Int64,
    ];

    /// The format as a schema spells it.
    #[must_use]
    pub fn as_str(self) -> &'static str {
        match self {
            Format::Date => "date",
            Format::DateTime => "date-time",
            Format::Time => "time",
            Format::Uuid => "uuid",
            Format::Email => "email",
            Format::Uri => "uri",
            Format::Ipv4 => "ipv4",
            Format::Ipv6 => "ipv6",
            Format::Hostname => "hostname",
            Format::Int32 => "int32",
            Format::Int64 => "int64",
        }
    }

    /// The format in scope spelled `text`, if one is.
    #[must_use]
    pub fn parse(text: &str) -> Option<Self> {
        Self::ALL.into_iter().find(|format| format.as_str() == text)
    }
}

/// One in-scope validation keyword and its declared value.
#[derive(Debug, Clone, PartialEq)]
pub enum Keyword {
    /// `enum`: the value is one of these.
    Enum(Vec<Value>),
    /// `const`: the value is this one.
    Const(Value),
    /// `pattern`: an ECMA-262 regular expression a string matches somewhere.
    Pattern(String),
    /// `minLength`, in code points.
    MinLength(u64),
    /// `maxLength`, in code points.
    MaxLength(u64),
    /// `format`, one in scope.
    Format(Format),
    /// `minimum`, inclusive.
    Minimum(f64),
    /// `maximum`, inclusive.
    Maximum(f64),
    /// `exclusiveMinimum` (3.1's number, or 3.0's `true` beside `minimum`).
    ExclusiveMinimum(f64),
    /// `exclusiveMaximum`, likewise.
    ExclusiveMaximum(f64),
    /// `multipleOf`, positive.
    MultipleOf(f64),
    /// `minItems`.
    MinItems(u64),
    /// `maxItems`.
    MaxItems(u64),
}

impl Keyword {
    /// The keyword a `constraint` spelling names, as [`fmt::Display`] writes
    /// it; `None` for any other text.
    #[must_use]
    pub fn parse(text: &str) -> Option<Self> {
        let (name, value) = text.split_once('=')?;
        let number = || value.parse::<f64>().ok().filter(|n| n.is_finite());
        let count = || value.parse::<u64>().ok();
        Some(match name {
            "enum" => Keyword::Enum(serde_json::from_str(value).ok()?),
            "const" => Keyword::Const(serde_json::from_str(value).ok()?),
            "pattern" => Keyword::Pattern(value.to_owned()),
            "minLength" => Keyword::MinLength(count()?),
            "maxLength" => Keyword::MaxLength(count()?),
            "format" => Keyword::Format(Format::parse(value)?),
            "minimum" => Keyword::Minimum(number()?),
            "maximum" => Keyword::Maximum(number()?),
            "exclusiveMinimum" => Keyword::ExclusiveMinimum(number()?),
            "exclusiveMaximum" => Keyword::ExclusiveMaximum(number()?),
            "multipleOf" => Keyword::MultipleOf(number()?),
            "minItems" => Keyword::MinItems(count()?),
            "maxItems" => Keyword::MaxItems(count()?),
            _ => return None,
        })
    }
}

impl fmt::Display for Keyword {
    /// The keyword as the inventory's `constraint` column spells it:
    /// `pattern=^(0|[1-9][0-9]*)$`, `minLength=7`, `enum=["a","b"]`.
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        let number = |value: f64| {
            if value.fract() == 0.0 && value.abs() < 1e15 {
                format!("{value:.0}")
            } else {
                Value::from(value).to_string()
            }
        };
        match self {
            Keyword::Enum(values) => write!(f, "enum={}", Value::Array(values.clone())),
            Keyword::Const(value) => write!(f, "const={value}"),
            Keyword::Pattern(pattern) => write!(f, "pattern={pattern}"),
            Keyword::MinLength(n) => write!(f, "minLength={n}"),
            Keyword::MaxLength(n) => write!(f, "maxLength={n}"),
            Keyword::Format(format) => write!(f, "format={}", format.as_str()),
            Keyword::Minimum(n) => write!(f, "minimum={}", number(*n)),
            Keyword::Maximum(n) => write!(f, "maximum={}", number(*n)),
            Keyword::ExclusiveMinimum(n) => write!(f, "exclusiveMinimum={}", number(*n)),
            Keyword::ExclusiveMaximum(n) => write!(f, "exclusiveMaximum={}", number(*n)),
            Keyword::MultipleOf(n) => write!(f, "multipleOf={}", number(*n)),
            Keyword::MinItems(n) => write!(f, "minItems={n}"),
            Keyword::MaxItems(n) => write!(f, "maxItems={n}"),
        }
    }
}

/// How one keyword reads one value.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
enum Reading {
    /// The keyword does not apply to the value's type, or it holds.
    Admits,
    /// The keyword rejects the value.
    Rejects,
    /// crozier cannot decide: a pattern it cannot compile.
    Undecided,
}

impl Keyword {
    /// How this keyword reads `value`, by JSON Schema's rules: each keyword
    /// applies only to instances of its own type.
    fn read(&self, value: &Value) -> Reading {
        let admits = |holds: bool| {
            if holds {
                Reading::Admits
            } else {
                Reading::Rejects
            }
        };
        match (self, value) {
            (Keyword::Enum(values), _) => admits(values.iter().any(|item| json_equal(item, value))),
            (Keyword::Const(constant), _) => admits(json_equal(constant, value)),
            (Keyword::Pattern(pattern), Value::String(text)) => {
                match crate::ir::string_keywords_admit(text, None, None, Some(pattern), None, None)
                {
                    Some(holds) => admits(holds),
                    None => Reading::Undecided,
                }
            }
            (Keyword::MinLength(n), Value::String(text)) => admits(
                crate::ir::string_keywords_admit(text, None, None, None, Some(*n), None)
                    .unwrap_or(true),
            ),
            (Keyword::MaxLength(n), Value::String(text)) => admits(
                crate::ir::string_keywords_admit(text, None, None, None, None, Some(*n))
                    .unwrap_or(true),
            ),
            (Keyword::Format(format), Value::String(text)) => admits(format_admits(*format, text)),
            (Keyword::Format(format), Value::Number(number)) => match format {
                Format::Int32 => admits(number.as_i64().is_some_and(|n| i32::try_from(n).is_ok())),
                // A literal past the signed 64-bit range reads as a `u64`, or
                // as a double where it fits neither; one inside reads as `i64`.
                Format::Int64 => admits(
                    number.is_i64()
                        || number
                            .as_f64()
                            .is_some_and(|n| n.fract() != 0.0 && n.abs() < 2f64.powi(63)),
                ),
                _ => Reading::Admits,
            },
            (Keyword::Minimum(bound), Value::Number(n)) => {
                admits(n.as_f64().is_some_and(|n| n >= *bound))
            }
            (Keyword::Maximum(bound), Value::Number(n)) => {
                admits(n.as_f64().is_some_and(|n| n <= *bound))
            }
            (Keyword::ExclusiveMinimum(bound), Value::Number(n)) => {
                admits(n.as_f64().is_some_and(|n| n > *bound))
            }
            (Keyword::ExclusiveMaximum(bound), Value::Number(n)) => {
                admits(n.as_f64().is_some_and(|n| n < *bound))
            }
            (Keyword::MultipleOf(step), Value::Number(n)) => {
                admits(n.as_f64().is_some_and(|n| is_multiple(n, *step)))
            }
            (Keyword::MinItems(n), Value::Array(items)) => admits(items.len() as u64 >= *n),
            (Keyword::MaxItems(n), Value::Array(items)) => admits(items.len() as u64 <= *n),
            _ => Reading::Admits,
        }
    }
}

/// JSON Schema equality: numbers compare by value — integers exactly, so `1`
/// equals `1.0` and no two integers past 2^53 are confused — and arrays and
/// objects by their members' equality.
fn json_equal(left: &Value, right: &Value) -> bool {
    let integer = |n: &serde_json::Number| {
        n.as_i64()
            .map(i128::from)
            .or_else(|| n.as_u64().map(i128::from))
    };
    match (left, right) {
        (Value::Number(a), Value::Number(b)) => match (integer(a), integer(b)) {
            (Some(a), Some(b)) => a == b,
            _ => a.as_f64() == b.as_f64(),
        },
        (Value::Array(a), Value::Array(b)) => {
            a.len() == b.len() && a.iter().zip(b).all(|(a, b)| json_equal(a, b))
        }
        (Value::Object(a), Value::Object(b)) => {
            a.len() == b.len()
                && a.iter()
                    .all(|(key, value)| b.get(key).is_some_and(|other| json_equal(value, other)))
        }
        _ => left == right,
    }
}

/// Whether `value` is an integer multiple of `step`, to a relative tolerance
/// that absorbs binary floating point (`0.3` is a multiple of `0.1`).
fn is_multiple(value: f64, step: f64) -> bool {
    if step <= 0.0 || !step.is_finite() || !value.is_finite() {
        return true;
    }
    let quotient = value / step;
    (quotient - quotient.round()).abs() <= 1e-9 * quotient.abs().max(1.0)
}

/// What the in-scope keywords say about one value.
#[derive(Debug, Clone, PartialEq)]
pub enum Verdict {
    /// Every keyword admits the value, and nothing out of view could reject it.
    Accepted,
    /// This keyword, the first in declaration order, rejects it.
    Rejected(Keyword),
    /// No keyword in view rejects it, but crozier cannot decide all of them:
    /// this keyword (a pattern it cannot compile), or, with none, a
    /// composition load normalization discarded whose constraints still bind.
    Undecided(Option<Keyword>),
}

/// The in-scope keywords of the schema one worked-example value documents,
/// and the values that schema declares for itself.
#[derive(Debug, Clone, Default, PartialEq)]
pub struct ValueConstraints {
    /// Every keyword the value must satisfy: the node's own, its `$ref`
    /// target's and its `allOf` members', in that order.
    pub keywords: Vec<Keyword>,
    /// The keywords of an array's items.
    pub items: Option<Box<ValueConstraints>>,
    /// The keywords of a map's values (`additionalProperties`).
    pub values: Option<Box<ValueConstraints>>,
    /// The examples the document declares for the value, in preference order:
    /// a parameter's own, then its schema's `example`, then its `examples`.
    pub examples: Vec<Value>,
    /// The schema's declared `default`.
    pub default: Option<Value>,
    /// Whether an array declares `uniqueItems: true`. Out of scope as a
    /// keyword that rejects a value, it still bounds a repair: crozier never
    /// pads such an array with an item it already holds.
    pub unique_items: bool,
    /// Whether an in-scope keyword may bind the value out of view: behind a
    /// reference that does not resolve, or past the depth followed. A value
    /// can still be rejected, but never accepted, by an incomplete view.
    pub incomplete: bool,
}

/// How deep a `$ref`/`allOf` chain is followed before the rest is treated as
/// out of view.
const MAX_DEPTH: usize = 16;

impl ValueConstraints {
    /// The constraints of `schema`, whose `$ref`s name `schemas`, or `None`
    /// when it declares no in-scope keyword at any depth an example reaches.
    #[must_use]
    pub fn of(schema: &Schema, schemas: &IndexMap<String, Schema>) -> Option<Box<Self>> {
        let mut constraints = Self::default();
        constraints.collect(schema, schemas, 0);
        constraints.has_keywords().then(|| Box::new(constraints))
    }

    /// [`Self::of`] for a parameter, whose own `example` precedes its schema's.
    #[must_use]
    pub fn of_parameter(parameter: &crate::openapi::Parameter, doc: &OpenApi) -> Option<Box<Self>> {
        let mut constraints = Self::of(parameter.schema.as_ref()?, &doc.components.schemas)?;
        if let Some(example) = &parameter.example {
            constraints.examples.insert(0, example.clone());
        }
        Some(constraints)
    }

    /// These constraints as a list's length reads them: without its items' or
    /// map values' own, which a list of placeholder items is not checked
    /// against.
    #[must_use]
    pub fn list_view(&self) -> Self {
        Self {
            items: None,
            values: None,
            ..self.clone()
        }
    }

    /// [`Self::of`] where the components may be out of view: `None` then.
    #[must_use]
    pub fn of_in(schema: &Schema, schemas: Option<&IndexMap<String, Schema>>) -> Option<Box<Self>> {
        Self::of(schema, schemas?)
    }

    /// [`Self::of_parameter`] for a query parameter read through `schema`, the
    /// one its other readings take (a one-or-many composition's array).
    #[must_use]
    pub fn of_query_parameter(
        parameter: &crate::openapi::Parameter,
        schema: Option<&Schema>,
        doc: &OpenApi,
    ) -> Option<Box<Self>> {
        let mut constraints = Self::of(schema?, &doc.components.schemas)?;
        constraints
            .examples
            .splice(0..0, parameter.example.iter().cloned());
        Some(constraints)
    }

    /// Whether any keyword applies anywhere a value reaches.
    fn has_keywords(&self) -> bool {
        !self.keywords.is_empty()
            || self
                .items
                .as_ref()
                .is_some_and(|items| items.has_keywords())
            || self
                .values
                .as_ref()
                .is_some_and(|values| values.has_keywords())
    }

    fn collect(&mut self, schema: &Schema, schemas: &IndexMap<String, Schema>, depth: usize) {
        if depth > MAX_DEPTH {
            self.incomplete = true;
            return;
        }
        if depth == 0 || self.examples.is_empty() {
            self.examples.extend(schema.example.iter().cloned());
            self.examples.extend(schema.examples.iter().cloned());
        }
        if self.default.is_none() {
            self.default.clone_from(&schema.default);
        }
        // `oneOf`, `anyOf`, `not` and the conditional applicators are keywords
        // out of scope, which neither reject nor block a repair; an `allOf`
        // load normalization discarded is still read, below.
        self.incomplete |= schema.unresolved_reference;
        self.keywords.extend(own_keywords(schema));
        self.unique_items |= schema.unique_items == Some(true);
        if let Some(items) = &schema.items {
            let mut inner = self.items.take().map_or_else(Self::default, |boxed| *boxed);
            inner.collect(items, schemas, depth + 1);
            self.items = Some(Box::new(inner));
        }
        if let Some(crate::openapi::AdditionalProperties::Schema(values)) =
            &schema.additional_properties
        {
            let mut inner = self
                .values
                .take()
                .map_or_else(Self::default, |boxed| *boxed);
            inner.collect(values, schemas, depth + 1);
            self.values = Some(Box::new(inner));
        }
        if let Some(reference) = &schema.reference {
            match reference
                .strip_prefix("#/components/schemas/")
                .and_then(|key| schemas.get(key))
            {
                Some(target) => self.collect(target, schemas, depth + 1),
                None => self.incomplete = true,
            }
        }
        for member in schema
            .all_of
            .iter()
            .chain(&schema.discarded_all_of)
            .flatten()
        {
            self.collect(member, schemas, depth + 1);
        }
    }

    /// What the keywords say about `value`.
    #[must_use]
    pub fn verdict(&self, value: &Value) -> Verdict {
        let mut undecided: Option<Option<Keyword>> = self.incomplete.then_some(None);
        let mut note = |found: Option<Keyword>| {
            if !matches!(undecided, Some(Some(_))) {
                undecided = Some(found);
            }
        };
        for keyword in &self.keywords {
            match keyword.read(value) {
                Reading::Rejects => return Verdict::Rejected(keyword.clone()),
                Reading::Undecided => note(Some(keyword.clone())),
                Reading::Admits => {}
            }
        }
        let nested = match (value, &self.items, &self.values) {
            (Value::Array(values), Some(items), _) => {
                values.iter().map(|v| (v, &**items)).collect()
            }
            (Value::Object(entries), _, Some(inner)) => {
                entries.values().map(|v| (v, &**inner)).collect()
            }
            _ => Vec::new(),
        };
        for (item, constraints) in nested {
            match constraints.verdict(item) {
                Verdict::Accepted => {}
                Verdict::Undecided(found) => note(found),
                rejected @ Verdict::Rejected(_) => return rejected,
            }
        }
        match undecided {
            Some(found) => Verdict::Undecided(found),
            None => Verdict::Accepted,
        }
    }

    /// The value crozier writes where Fern writes `fern`, which these keywords
    /// reject: the first declared example they accept, else the declared
    /// `default` when they accept it, else a value constructed to satisfy
    /// every keyword. `None` when none of those exists or can be decided.
    #[must_use]
    pub fn choose(&self, fern: &Value) -> Option<Choice> {
        let accepted = |candidate: &Value| {
            same_kind(candidate, fern) && self.verdict(candidate) == Verdict::Accepted
        };
        if let Some(example) = self.examples.iter().find(|example| accepted(example)) {
            return Some(Choice::Example(example.clone()));
        }
        if let Some(default) = self.default.as_ref().filter(|default| accepted(default)) {
            return Some(Choice::Default(default.clone()));
        }
        self.construct(fern)
            .filter(|value| accepted(value))
            .map(Choice::Constructed)
    }

    /// A value of `fern`'s kind built to satisfy every keyword.
    fn construct(&self, fern: &Value) -> Option<Value> {
        match fern {
            Value::String(name) => self.construct_string(name),
            Value::Number(number) => self.construct_number(number),
            Value::Array(items) => self.construct_array(items),
            _ => None,
        }
    }

    fn construct_string(&self, name: &str) -> Option<Value> {
        let accepts =
            |text: &str| self.verdict(&Value::String(text.to_owned())) == Verdict::Accepted;
        let mut candidates: Vec<String> = Vec::new();
        for keyword in &self.keywords {
            match keyword {
                Keyword::Const(Value::String(value)) => candidates.push(value.clone()),
                Keyword::Enum(values) => {
                    candidates.extend(values.iter().filter_map(Value::as_str).map(str::to_owned))
                }
                _ => {}
            }
        }
        for keyword in &self.keywords {
            if let Keyword::Format(format) = keyword {
                candidates.extend(format_sample(*format).map(str::to_owned));
            }
        }
        if let Some(found) = candidates.iter().find(|candidate| accepts(candidate)) {
            return Some(Value::String(found.clone()));
        }
        let (min, max) = self.lengths();
        for keyword in &self.keywords {
            if let Keyword::Pattern(pattern) = keyword {
                if let Some(found) =
                    pattern_samples(pattern, min, max).find(|sample| accepts(sample))
                {
                    return Some(Value::String(found));
                }
            }
        }
        if self
            .keywords
            .iter()
            .any(|keyword| matches!(keyword, Keyword::Pattern(_)))
        {
            return None;
        }
        let length = name.chars().count() as u64;
        let resized = if max.is_some_and(|max| length > max) {
            name.chars().take(usize::try_from(max?).ok()?).collect()
        } else if min.is_some_and(|min| length < min) {
            crate::ir::sample_string_of_length(min?)
        } else {
            return None;
        };
        accepts(&resized).then_some(Value::String(resized))
    }

    /// `count` pairwise-distinct values these item keywords accept: `kept`
    /// first (themselves distinct and accepted), then values built from the
    /// first of them, deterministically — the strings a `pattern` matches, an
    /// `enum`'s members, numbered variants of a string with neither within its
    /// lengths, or numbers stepped up within the bounds and onto any
    /// `multipleOf` grid. `None` where `kept` is empty, holds anything but
    /// strings or numbers, or not enough such values are found.
    #[must_use]
    pub fn distinct_items(&self, kept: &[Value], count: usize) -> Option<Vec<Value>> {
        let accepted = |value: &Value| self.verdict(value) == Verdict::Accepted;
        let mut out: Vec<Value> = Vec::new();
        for value in kept.iter().take(count) {
            if !accepted(value) || out.iter().any(|seen| json_equal(seen, value)) {
                return None;
            }
            out.push(value.clone());
        }
        let first = kept.first()?;
        let candidates: Box<dyn Iterator<Item = Value>> = match first {
            Value::String(text) => {
                let pattern = self.keywords.iter().find_map(|keyword| match keyword {
                    Keyword::Pattern(pattern) => Some(pattern.clone()),
                    _ => None,
                });
                let members: Vec<Value> = self
                    .keywords
                    .iter()
                    .flat_map(|keyword| match keyword {
                        Keyword::Enum(values) => values.clone(),
                        Keyword::Const(value) => vec![value.clone()],
                        _ => Vec::new(),
                    })
                    .collect();
                let (min, max) = self.lengths();
                if let Some(pattern) = pattern {
                    Box::new(pattern_samples(&pattern, min, max).map(Value::String))
                } else if !members.is_empty() {
                    Box::new(members.into_iter())
                } else if self
                    .keywords
                    .iter()
                    .any(|keyword| matches!(keyword, Keyword::Format(_)))
                {
                    return None;
                } else {
                    let text = text.clone();
                    Box::new((2..=count + 64).map(move |n| {
                        let suffix = n.to_string();
                        let room = max.map_or(usize::MAX, |max| {
                            usize::try_from(max)
                                .unwrap_or(usize::MAX)
                                .saturating_sub(suffix.len())
                        });
                        Value::String(format!(
                            "{}{suffix}",
                            text.chars().take(room).collect::<String>()
                        ))
                    }))
                }
            }
            Value::Number(number) => {
                let start = number.as_f64()?;
                let integer = number.is_i64() || number.is_u64();
                let step = self
                    .keywords
                    .iter()
                    .find_map(|keyword| match keyword {
                        Keyword::MultipleOf(step) => {
                            Some(if integer { lcm_step(*step) } else { *step })
                        }
                        _ => None,
                    })
                    .unwrap_or(1.0);
                Box::new((1..=count + 64).filter_map(move |n| {
                    #[allow(clippy::cast_precision_loss, reason = "a handful of steps")]
                    let value = start + step * n as f64;
                    if integer {
                        #[allow(
                            clippy::cast_possible_truncation,
                            reason = "integral by construction"
                        )]
                        Some(Value::from(value.round() as i64))
                    } else {
                        serde_json::Number::from_f64(value).map(Value::Number)
                    }
                }))
            }
            _ => return None,
        };
        for candidate in candidates {
            if out.len() >= count {
                break;
            }
            if same_kind(&candidate, first)
                && accepted(&candidate)
                && !out.iter().any(|seen| json_equal(seen, &candidate))
            {
                out.push(candidate);
            }
        }
        (out.len() == count).then_some(out)
    }

    /// The tightest declared `minLength` and `maxLength`.
    fn lengths(&self) -> (Option<u64>, Option<u64>) {
        let mut min: Option<u64> = None;
        let mut max: Option<u64> = None;
        for keyword in &self.keywords {
            match keyword {
                Keyword::MinLength(n) => min = Some(min.map_or(*n, |m| m.max(*n))),
                Keyword::MaxLength(n) => max = Some(max.map_or(*n, |m| m.min(*n))),
                _ => {}
            }
        }
        (min, max)
    }

    fn construct_number(&self, fern: &serde_json::Number) -> Option<Value> {
        let value = fern.as_f64()?;
        let integer_format = self
            .keywords
            .iter()
            .any(|keyword| matches!(keyword, Keyword::Format(Format::Int32 | Format::Int64)));
        let integer = fern.is_i64() || fern.is_u64() || (integer_format && value.fract() == 0.0);
        let mut low = f64::NEG_INFINITY;
        let mut high = f64::INFINITY;
        let mut steps = Vec::new();
        let step_up = if integer { 1.0 } else { 0.1 };
        for keyword in &self.keywords {
            match keyword {
                Keyword::Minimum(n) => low = low.max(*n),
                Keyword::ExclusiveMinimum(n) => low = low.max(*n + step_up),
                Keyword::Maximum(n) => high = high.min(*n),
                Keyword::ExclusiveMaximum(n) => high = high.min(*n - step_up),
                Keyword::MultipleOf(n) => steps.push(*n),
                Keyword::Format(Format::Int32) => {
                    low = low.max(f64::from(i32::MIN));
                    high = high.min(f64::from(i32::MAX));
                }
                // The nearest doubles inside the signed 64-bit range.
                Keyword::Format(Format::Int64) => {
                    low = low.max(-(2f64.powi(63)));
                    high = high.min(2f64.powi(63) - 1024.0);
                }
                _ => {}
            }
        }
        let declared = self.keywords.iter().flat_map(|keyword| match keyword {
            Keyword::Const(value) => vec![value.clone()],
            Keyword::Enum(values) => values.clone(),
            _ => Vec::new(),
        });
        for value in declared {
            let kind_matches = if integer {
                value.is_i64() || value.is_u64()
            } else {
                value.is_number()
            };
            if kind_matches && self.verdict(&value) == Verdict::Accepted {
                return Some(value);
            }
        }
        if integer {
            low = low.ceil();
            high = high.floor();
        }
        let mut candidate = value.clamp(low.min(high), high.max(low));
        if let Some(step) = steps.first().copied().filter(|step| *step > 0.0) {
            let unit = if integer { lcm_step(step) } else { step };
            candidate = (candidate / unit).ceil() * unit;
            if candidate > high {
                candidate = (high / unit).floor() * unit;
            }
        }
        let number = if integer {
            #[allow(
                clippy::cast_possible_truncation,
                reason = "the bounds were checked finite and integral"
            )]
            serde_json::Number::from(candidate.round() as i64)
        } else {
            serde_json::Number::from_f64((candidate * 1e9).round() / 1e9)?
        };
        Some(Value::Number(number))
    }

    fn construct_array(&self, items: &[Value]) -> Option<Value> {
        let mut min = 0u64;
        let mut max = u64::MAX;
        for keyword in &self.keywords {
            match keyword {
                Keyword::MinItems(n) => min = min.max(*n),
                Keyword::MaxItems(n) => max = max.min(*n),
                _ => {}
            }
        }
        let length = items.len() as u64;
        let target = usize::try_from(length.clamp(min, max.max(min))).ok()?;
        let first = items.first()?;
        let mut out: Vec<Value> = items.iter().take(target).cloned().collect();
        out.resize(target, first.clone());
        Some(Value::Array(out))
    }
}

/// The smallest integer multiple of `step`: an integer instance of a
/// fractional `multipleOf` is a multiple of its integer multiples.
fn lcm_step(step: f64) -> f64 {
    let mut unit = step;
    for _ in 0..1000 {
        if (unit - unit.round()).abs() < 1e-9 {
            return unit.round().max(1.0);
        }
        unit += step;
    }
    step.ceil()
}

/// Whether two values are the same JSON kind, numbers of either form alike.
fn same_kind(left: &Value, right: &Value) -> bool {
    std::mem::discriminant(left) == std::mem::discriminant(right)
}

/// Where crozier's value came from.
#[derive(Debug, Clone, PartialEq)]
pub enum Choice {
    /// The specification's own declared example.
    Example(Value),
    /// The schema's declared `default`.
    Default(Value),
    /// A value built to satisfy every keyword.
    Constructed(Value),
}

impl Choice {
    /// The chosen value.
    #[must_use]
    pub fn value(&self) -> &Value {
        match self {
            Choice::Example(value) | Choice::Default(value) | Choice::Constructed(value) => value,
        }
    }
}

/// The in-scope keywords `schema` itself declares, in a fixed order.
fn own_keywords(schema: &Schema) -> Vec<Keyword> {
    let unmodeled = &schema.unmodeled_keywords;
    let number = |key: &str| unmodeled.get(key).and_then(Value::as_f64);
    let count = |key: &str| unmodeled.get(key).and_then(Value::as_u64);
    let mut keywords = Vec::new();
    if let Some(values) = &schema.enum_values {
        keywords.push(Keyword::Enum(values.clone()));
    }
    if let Some(value) = &schema.const_value {
        keywords.push(Keyword::Const(value.clone()));
    }
    if let Some(pattern) = &schema.pattern {
        keywords.push(Keyword::Pattern(pattern.clone()));
    }
    if let Some(n) = schema.min_length {
        keywords.push(Keyword::MinLength(n));
    }
    if let Some(n) = schema.max_length {
        keywords.push(Keyword::MaxLength(n));
    }
    if let Some(format) = schema.format.as_deref().and_then(Format::parse) {
        keywords.push(Keyword::Format(format));
    }
    // OpenAPI 3.0 spells an exclusive bound as `exclusiveMinimum: true` beside
    // `minimum`; 3.1 as the number itself.
    let exclusive = |key: &str| unmodeled.get(key).and_then(Value::as_bool) == Some(true);
    if let Some(n) = schema.minimum.as_ref().and_then(Value::as_f64) {
        keywords.push(if exclusive("exclusiveMinimum") {
            Keyword::ExclusiveMinimum(n)
        } else {
            Keyword::Minimum(n)
        });
    }
    if let Some(n) = number("maximum") {
        keywords.push(if exclusive("exclusiveMaximum") {
            Keyword::ExclusiveMaximum(n)
        } else {
            Keyword::Maximum(n)
        });
    }
    if let Some(n) = number("exclusiveMinimum") {
        keywords.push(Keyword::ExclusiveMinimum(n));
    }
    if let Some(n) = number("exclusiveMaximum") {
        keywords.push(Keyword::ExclusiveMaximum(n));
    }
    if let Some(n) = number("multipleOf").filter(|n| *n > 0.0) {
        keywords.push(Keyword::MultipleOf(n));
    }
    if let Some(n) = count("minItems") {
        keywords.push(Keyword::MinItems(n));
    }
    if let Some(n) = count("maxItems") {
        keywords.push(Keyword::MaxItems(n));
    }
    keywords
}

/// A value of each string format that format accepts: the sample a constructed
/// value starts from.
fn format_sample(format: Format) -> Option<&'static str> {
    Some(match format {
        Format::Date => "2023-01-15",
        Format::DateTime => "2024-01-15T09:30:00Z",
        Format::Time => "09:30:00Z",
        Format::Uuid => "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        Format::Email => "user@example.com",
        Format::Uri => "https://example.com",
        Format::Ipv4 => "192.0.2.1",
        Format::Ipv6 => "2001:db8::1",
        Format::Hostname => "example.com",
        Format::Int32 | Format::Int64 => return None,
    })
}

/// Whether `text` is valid as a string of `format`; an integer format admits
/// every string.
#[must_use]
pub fn format_admits(format: Format, text: &str) -> bool {
    match format {
        Format::Date => full_date(text),
        Format::DateTime => text
            .split_once(['T', 't'])
            .is_some_and(|(date, time)| full_date(date) && full_time(time)),
        Format::Time => full_time(text),
        Format::Uuid => uuid(text),
        Format::Email => email(text),
        Format::Uri => uri(text),
        Format::Ipv4 => ipv4(text),
        Format::Ipv6 => text.parse::<std::net::Ipv6Addr>().is_ok(),
        Format::Hostname => hostname(text),
        Format::Int32 | Format::Int64 => true,
    }
}

fn digits(text: &str, count: usize) -> Option<u32> {
    (text.len() == count && text.bytes().all(|byte| byte.is_ascii_digit()))
        .then(|| text.parse().ok())
        .flatten()
}

/// RFC 3339 `full-date`.
fn full_date(text: &str) -> bool {
    let mut parts = text.split('-');
    let (Some(year), Some(month), Some(day), None) =
        (parts.next(), parts.next(), parts.next(), parts.next())
    else {
        return false;
    };
    let (Some(year), Some(month), Some(day)) = (digits(year, 4), digits(month, 2), digits(day, 2))
    else {
        return false;
    };
    let leap = year % 4 == 0 && (year % 100 != 0 || year % 400 == 0);
    let days = match month {
        1 | 3 | 5 | 7 | 8 | 10 | 12 => 31,
        4 | 6 | 9 | 11 => 30,
        2 if leap => 29,
        2 => 28,
        _ => return false,
    };
    (1..=days).contains(&day)
}

/// RFC 3339 `full-time`: `partial-time` and a `Z` or numeric offset.
fn full_time(text: &str) -> bool {
    let (time, offset) = if let Some(time) = text.strip_suffix(['Z', 'z']) {
        (time, None)
    } else {
        match text.rfind(['+', '-']) {
            Some(at) => (&text[..at], Some(&text[at + 1..])),
            None => return false,
        }
    };
    if let Some(offset) = offset {
        let Some((hours, minutes)) = offset.split_once(':') else {
            return false;
        };
        if digits(hours, 2).is_none_or(|h| h >= 24) || digits(minutes, 2).is_none_or(|m| m >= 60) {
            return false;
        }
    }
    let (whole, fraction) = time
        .split_once('.')
        .map_or((time, None), |(w, f)| (w, Some(f)));
    if fraction.is_some_and(|f| f.is_empty() || !f.bytes().all(|byte| byte.is_ascii_digit())) {
        return false;
    }
    let mut parts = whole.split(':');
    let (Some(hour), Some(minute), Some(second), None) =
        (parts.next(), parts.next(), parts.next(), parts.next())
    else {
        return false;
    };
    digits(hour, 2).is_some_and(|h| h < 24)
        && digits(minute, 2).is_some_and(|m| m < 60)
        && digits(second, 2).is_some_and(|s| s <= 60)
}

fn uuid(text: &str) -> bool {
    let groups: Vec<&str> = text.split('-').collect();
    groups.len() == 5
        && groups.iter().zip([8, 4, 4, 4, 12]).all(|(group, length)| {
            group.len() == length && group.bytes().all(|b| b.is_ascii_hexdigit())
        })
}

fn email(text: &str) -> bool {
    let Some((local, domain)) = text.rsplit_once('@') else {
        return false;
    };
    const SPECIALS: &str = "!#$%&'*+/=?^_`{|}~.-";
    !local.is_empty()
        && !local.starts_with('.')
        && !local.ends_with('.')
        && !local.contains("..")
        && local
            .chars()
            .all(|c| c.is_ascii_alphanumeric() || SPECIALS.contains(c))
        && (hostname(domain)
            || domain
                .strip_prefix('[')
                .and_then(|rest| rest.strip_suffix(']'))
                .is_some_and(|address| {
                    ipv4(address)
                        || address
                            .strip_prefix("IPv6:")
                            .is_some_and(|v6| v6.parse::<std::net::Ipv6Addr>().is_ok())
                }))
}

/// An RFC 3986 URI: a scheme, a colon, and only characters a URI may hold.
fn uri(text: &str) -> bool {
    let Some((scheme, rest)) = text.split_once(':') else {
        return false;
    };
    let mut scheme_chars = scheme.chars();
    scheme_chars.next().is_some_and(|c| c.is_ascii_alphabetic())
        && scheme_chars.all(|c| c.is_ascii_alphanumeric() || "+-.".contains(c))
        && rest
            .chars()
            .all(|c| c.is_ascii_alphanumeric() || "-._~:/?#[]@!$&'()*+,;=%".contains(c))
        && rest.match_indices('%').all(|(at, _)| {
            rest.get(at + 1..at + 3)
                .is_some_and(|hex| hex.bytes().all(|b| b.is_ascii_hexdigit()))
        })
}

fn ipv4(text: &str) -> bool {
    let octets: Vec<&str> = text.split('.').collect();
    octets.len() == 4
        && octets.iter().all(|octet| {
            !octet.is_empty()
                && octet.len() <= 3
                && octet.bytes().all(|b| b.is_ascii_digit())
                && (octet.len() == 1 || !octet.starts_with('0'))
                && octet.parse::<u16>().is_ok_and(|n| n <= 255)
        })
}

/// An RFC 1123 host name: dot-separated labels of letters, digits and inner
/// hyphens, each at most 63 long, at most 253 in all.
fn hostname(text: &str) -> bool {
    let text = text.strip_suffix('.').unwrap_or(text);
    !text.is_empty()
        && text.len() <= 253
        && text.split('.').all(|label| {
            !label.is_empty()
                && label.len() <= 63
                && !label.starts_with('-')
                && !label.ends_with('-')
                && label
                    .bytes()
                    .all(|b| b.is_ascii_alphanumeric() || b == b'-')
        })
}

/// Strings `pattern` matches, shortest first, deterministically: each
/// repetition is stretched by the same number of extra rounds, from none up,
/// under each choice of alternative (first, then last). Empty when crozier
/// cannot read the pattern (a lookaround, a backreference).
fn pattern_samples(
    pattern: &str,
    min: Option<u64>,
    max: Option<u64>,
) -> impl Iterator<Item = String> {
    let hir = regex_syntax::ParserBuilder::new()
        .build()
        .parse(pattern)
        .ok();
    let limit = usize::try_from(
        min.unwrap_or(0)
            .max(16)
            .min(max.unwrap_or(u64::MAX))
            .min(256),
    )
    .unwrap_or(16);
    [false, true].into_iter().flat_map(move |last| {
        let hir = hir.clone();
        (0..=limit).filter_map(move |extra| {
            let mut out = String::new();
            sample(hir.as_ref()?, extra, last, &mut out).then_some(out)
        })
    })
}

/// Append one string `hir` matches to `out`; `false` when it holds a class
/// with no character to pick.
fn sample(hir: &regex_syntax::hir::Hir, extra: usize, last: bool, out: &mut String) -> bool {
    use regex_syntax::hir::{Class, HirKind};
    match hir.kind() {
        HirKind::Empty | HirKind::Look(_) => true,
        HirKind::Literal(literal) => match std::str::from_utf8(&literal.0) {
            Ok(text) => {
                out.push_str(text);
                true
            }
            Err(_) => false,
        },
        HirKind::Class(Class::Unicode(class)) => {
            let ranges: Vec<(char, char)> = class
                .ranges()
                .iter()
                .map(|r| (r.start(), r.end()))
                .collect();
            match pick(&ranges) {
                Some(c) => {
                    out.push(c);
                    true
                }
                None => false,
            }
        }
        HirKind::Class(Class::Bytes(class)) => {
            let ranges: Vec<(char, char)> = class
                .ranges()
                .iter()
                .filter(|r| r.start() < 0x80)
                .map(|r| (char::from(r.start()), char::from(r.end().min(0x7f))))
                .collect();
            match pick(&ranges) {
                Some(c) => {
                    out.push(c);
                    true
                }
                None => false,
            }
        }
        HirKind::Repetition(repetition) => {
            let wanted = u64::from(repetition.min).saturating_add(extra as u64);
            let count = repetition
                .max
                .map_or(wanted, |max| wanted.min(u64::from(max)));
            (0..count).all(|_| sample(&repetition.sub, extra, last, out))
        }
        HirKind::Capture(capture) => sample(&capture.sub, extra, last, out),
        HirKind::Concat(parts) => parts.iter().all(|part| sample(part, extra, last, out)),
        HirKind::Alternation(branches) => {
            let branch = if last {
                branches.last()
            } else {
                branches.first()
            };
            branch.is_some_and(|branch| sample(branch, extra, last, out))
        }
    }
}

/// The character a constructed string takes from a class: a letter or digit
/// people read as a placeholder where the class holds one, else a space where
/// it holds one (`\s`), else its first printable ASCII character, else its
/// first character.
fn pick(ranges: &[(char, char)]) -> Option<char> {
    let holds = |c: char| {
        ranges
            .iter()
            .any(|(start, end)| (*start..=*end).contains(&c))
    };
    ['a', 'A', '0', '1', 'x', '_', '-', '.', ' ']
        .into_iter()
        .find(|c| holds(*c))
        .or_else(|| (' '..='~').find(|c| holds(*c)))
        .or_else(|| ranges.first().map(|(start, _)| *start))
}

/// A worked-example scalar as Python source spells it, read as the JSON value
/// it stands for: a string literal, a number, `True` or `False`. `None` for
/// anything else (a list, a constructor call, a member access, a bytes
/// literal, `None` itself).
#[must_use]
pub fn python_value(literal: &str) -> Option<Value> {
    let literal = literal.trim();
    match literal {
        "True" => return Some(Value::Bool(true)),
        "False" => return Some(Value::Bool(false)),
        _ => {}
    }
    for quote in ['"', '\''] {
        if let Some(body) = literal
            .strip_prefix(quote)
            .and_then(|rest| rest.strip_suffix(quote))
        {
            return python_string_body(body).map(Value::String);
        }
    }
    if literal.starts_with(|c: char| c.is_ascii_digit() || c == '-') {
        return serde_json::from_str::<serde_json::Number>(literal)
            .ok()
            .map(Value::Number);
    }
    None
}

/// Fern's construction of a worked-example value a schema can reject, named
/// by the catalog id of the departure that corrects it.
#[derive(Debug, Clone, Copy, PartialEq, Eq, PartialOrd, Ord, Hash)]
pub enum Mechanism {
    /// A string written as the name of the parameter or property it fills.
    Name,
    /// A string written as Fern's fixed `"string"` or `"value"` placeholder.
    Placeholder,
    /// A string Fern's IR fallback sizes by the declared lengths alone.
    Sized,
    /// A number written as Fern's fixed `1`, `1000000` or `1.1`.
    Number,
    /// A list written with Fern's fixed number of items.
    Array,
    /// A string enum's first member, which the earlier
    /// `pattern-narrowed-enum-example` departure corrects.
    EnumMember,
    /// A declared integer past 2^53 written as the double nearest it, which
    /// the earlier `int64-example-rounded-out-of-range` departure corrects.
    Rounded,
}

impl Mechanism {
    /// Every mechanism an inventory row may name.
    pub const ALL: [Mechanism; 7] = [
        Mechanism::Name,
        Mechanism::Placeholder,
        Mechanism::Sized,
        Mechanism::Number,
        Mechanism::Array,
        Mechanism::EnumMember,
        Mechanism::Rounded,
    ];

    /// The mechanisms the `schema-rejected-*` departures repair.
    pub const REPAIRED: [Mechanism; 5] = [
        Mechanism::Name,
        Mechanism::Placeholder,
        Mechanism::Sized,
        Mechanism::Number,
        Mechanism::Array,
    ];

    /// The repaired mechanisms that write one scalar.
    pub const SCALAR: [Mechanism; 4] = [
        Mechanism::Name,
        Mechanism::Placeholder,
        Mechanism::Sized,
        Mechanism::Number,
    ];

    /// The catalog id of the departure that corrects this construction.
    #[must_use]
    pub fn id(self) -> &'static str {
        match self {
            Mechanism::Name => "schema-rejected-name-example",
            Mechanism::Placeholder => "schema-rejected-placeholder-string-example",
            Mechanism::Sized => "schema-rejected-sized-string-example",
            Mechanism::Number => "schema-rejected-number-example",
            Mechanism::Array => "schema-rejected-array-length-example",
            Mechanism::EnumMember => "pattern-narrowed-enum-example",
            Mechanism::Rounded => "int64-example-rounded-out-of-range",
        }
    }

    /// The mechanism whose departure is the catalog id `id`, if one is.
    #[must_use]
    pub fn parse(id: &str) -> Option<Self> {
        Self::ALL.into_iter().find(|mechanism| mechanism.id() == id)
    }
}

/// Why an inventoried value is, or is not, written differently from Fern.
#[derive(Debug, Clone, Copy, PartialEq, Eq, PartialOrd, Ord)]
pub enum Disposition {
    /// crozier writes a value the schema accepts instead.
    Repaired,
    /// The value is the specification's own declared example, which stays.
    DeclaredInSpec,
    /// Only a keyword or format outside the set in scope rejects the value.
    OutOfScopeKeyword,
    /// crozier cannot decide whether a replacement is valid.
    ResidualUndecidable,
    /// No value satisfies every keyword, or crozier cannot build one.
    ResidualUnconstructible,
}

impl Disposition {
    /// Every disposition, in the inventory's vocabulary order.
    pub const ALL: [Disposition; 5] = [
        Disposition::Repaired,
        Disposition::DeclaredInSpec,
        Disposition::OutOfScopeKeyword,
        Disposition::ResidualUndecidable,
        Disposition::ResidualUnconstructible,
    ];

    /// The disposition as the inventory spells it.
    #[must_use]
    pub fn as_str(self) -> &'static str {
        match self {
            Disposition::Repaired => "repaired",
            Disposition::DeclaredInSpec => "declared-in-spec",
            Disposition::OutOfScopeKeyword => "out-of-scope-keyword",
            Disposition::ResidualUndecidable => "residual-undecidable",
            Disposition::ResidualUnconstructible => "residual-unconstructible",
        }
    }

    /// The disposition spelled `text`.
    #[must_use]
    pub fn parse(text: &str) -> Option<Self> {
        Self::ALL.into_iter().find(|d| d.as_str() == text)
    }
}

/// One worked-example value a schema rejects, wherever it stands.
#[derive(Debug, Clone, PartialEq)]
pub struct Finding {
    /// The keyword argument and, inside a body, the dotted path to the value.
    pub argument: String,
    /// The value as Fern's construction writes it.
    pub fern: String,
    /// The value as crozier writes it: `fern` unless repaired.
    pub crozier: String,
    /// The rejecting keyword and its declared value.
    pub constraint: Keyword,
    /// The construction the value is, where it is Fern's own.
    pub mechanism: Option<Mechanism>,
    /// What crozier does about it.
    pub disposition: Disposition,
}

/// A [`Finding`] at the line crozier wrote it.
#[derive(Debug, Clone, PartialEq)]
pub struct ExampleValue {
    /// The generated file's `/`-separated path relative to the SDK root.
    pub file: String,
    /// crozier's 1-based line in that file.
    pub line: std::num::NonZeroUsize,
    /// The value, its constraint and what crozier does about it.
    pub finding: Finding,
}

/// The record a recording `crozier generate` writes: the environment variable
/// naming the directory, under [`record_file_name`] of the output directory.
pub const RECORD_ENV: &str = "CROZIER_RECORD_EXAMPLE_VALUES";

/// The file, inside [`RECORD_ENV`]'s directory, holding the values generated
/// into `output`: a digest of its canonical path, so a test that knows only
/// the directory it generated into finds the record.
#[must_use]
pub fn record_file_name(output: &std::path::Path) -> String {
    let canonical = output
        .canonicalize()
        .unwrap_or_else(|_| output.to_path_buf());
    let mut hash: u64 = 0xcbf2_9ce4_8422_2325;
    for byte in canonical.to_string_lossy().bytes() {
        hash ^= u64::from(byte);
        hash = hash.wrapping_mul(0x0100_0000_01b3);
    }
    format!("{hash:016x}.tsv")
}

/// A field as a record writes it: tabs, newlines and backslashes escaped.
fn escape(text: &str) -> String {
    text.replace('\\', "\\\\")
        .replace('\t', "\\t")
        .replace('\n', "\\n")
}

fn unescape(text: &str) -> String {
    let mut out = String::new();
    let mut chars = text.chars();
    while let Some(c) = chars.next() {
        if c == '\\' {
            match chars.next() {
                Some('t') => out.push('\t'),
                Some('n') => out.push('\n'),
                Some(other) => out.push(other),
                None => out.push('\\'),
            }
        } else {
            out.push(c);
        }
    }
    out
}

impl ExampleValue {
    /// The value as one tab-separated record line.
    #[must_use]
    pub fn render(&self) -> String {
        let finding = &self.finding;
        [
            escape(&self.file),
            self.line.to_string(),
            escape(&finding.argument),
            escape(&finding.fern),
            escape(&finding.crozier),
            escape(&finding.constraint.to_string()),
            finding.mechanism.map_or("-", Mechanism::id).to_string(),
            finding.disposition.as_str().to_string(),
        ]
        .join("\t")
    }

    /// The value a record line holds; `None` for a line that is not one, a
    /// line number of zero or a constraint no keyword spells included.
    #[must_use]
    pub fn parse(line: &str) -> Option<Self> {
        let fields: Vec<&str> = line.split('\t').collect();
        let [file, number, argument, fern, crozier, constraint, mechanism, disposition] =
            fields.as_slice()
        else {
            return None;
        };
        Some(Self {
            file: unescape(file),
            line: number.parse().ok()?,
            finding: Finding {
                argument: unescape(argument),
                fern: unescape(fern),
                crozier: unescape(crozier),
                constraint: Keyword::parse(&unescape(constraint))?,
                mechanism: match *mechanism {
                    "-" => None,
                    id => Some(Mechanism::parse(id)?),
                },
                disposition: Disposition::parse(disposition)?,
            },
        })
    }
}

/// The text a Python string literal's body (between its quotes) spells:
/// the escapes crozier's writers emit decoded, any other backslash refused.
fn python_string_body(body: &str) -> Option<String> {
    let mut out = String::new();
    let mut chars = body.chars();
    while let Some(c) = chars.next() {
        if c != '\\' {
            out.push(c);
            continue;
        }
        match chars.next()? {
            '\\' => out.push('\\'),
            '\'' => out.push('\''),
            '"' => out.push('"'),
            'n' => out.push('\n'),
            'r' => out.push('\r'),
            't' => out.push('\t'),
            'u' => {
                let hex: String = chars.by_ref().take(4).collect();
                out.push(char::from_u32(u32::from_str_radix(&hex, 16).ok()?)?);
            }
            'x' => {
                let hex: String = chars.by_ref().take(2).collect();
                out.push(char::from_u32(u32::from_str_radix(&hex, 16).ok()?)?);
            }
            _ => return None,
        }
    }
    Some(out)
}

#[cfg(test)]
mod tests {
    use super::*;

    fn constraints(schema: serde_json::Value) -> Box<ValueConstraints> {
        let doc: OpenApi = serde_json::from_value(serde_json::json!({
            "openapi": "3.1.0",
            "info": {"title": "t", "version": "1"},
            "paths": {},
            "components": {"schemas": {"Snowflake": {
                "type": "string", "pattern": "^(0|[1-9][0-9]*)$", "format": "snowflake"
            }}}
        }))
        .unwrap();
        let schema: Schema = serde_json::from_value(schema).unwrap();
        ValueConstraints::of(&schema, &doc.components.schemas).expect("constrained")
    }

    fn rejected_by(c: &ValueConstraints, value: Value) -> String {
        match c.verdict(&value) {
            Verdict::Rejected(keyword) => keyword.to_string(),
            other => panic!("{value} was not rejected: {other:?}"),
        }
    }

    #[test]
    fn a_name_placeholder_is_rejected_by_the_referenced_pattern_and_repaired() {
        let c = constraints(serde_json::json!({"$ref": "#/components/schemas/Snowflake"}));
        assert_eq!(
            rejected_by(&c, Value::from("guild_id")),
            "pattern=^(0|[1-9][0-9]*)$"
        );
        // The unknown `snowflake` format is an annotation, not a rejection.
        assert_eq!(c.verdict(&Value::from("0")), Verdict::Accepted);
        assert_eq!(
            c.choose(&Value::from("guild_id")),
            Some(Choice::Constructed(Value::from("0")))
        );
    }

    #[test]
    fn the_declared_example_comes_first_then_the_default_each_only_when_accepted() {
        let c = constraints(serde_json::json!({
            "type": "string", "pattern": "^[0-9]+$", "example": "12", "default": "7"
        }));
        assert_eq!(
            c.choose(&Value::from("id")),
            Some(Choice::Example(Value::from("12")))
        );
        let c = constraints(serde_json::json!({
            "type": "string", "pattern": "^[0-9]+$", "example": "twelve", "default": "7"
        }));
        assert_eq!(
            c.choose(&Value::from("id")),
            Some(Choice::Default(Value::from("7")))
        );
        let c = constraints(serde_json::json!({
            "type": "string", "pattern": "^[0-9]+$", "example": "twelve", "default": "seven"
        }));
        assert_eq!(
            c.choose(&Value::from("id")),
            Some(Choice::Constructed(Value::from("0")))
        );
    }

    #[test]
    fn every_keyword_in_scope_rejects_and_a_constructed_value_satisfies_it() {
        let cases = [
            (
                serde_json::json!({"type": "string", "minLength": 12}),
                Value::from("id"),
                "minLength=12",
            ),
            (
                serde_json::json!({"type": "string", "maxLength": 3}),
                Value::from("name"),
                "maxLength=3",
            ),
            (
                serde_json::json!({"type": "string", "pattern": "^[A-Z]{2}-\\d{4}$"}),
                Value::from("code"),
                "pattern=^[A-Z]{2}-\\d{4}$",
            ),
            (
                serde_json::json!({"type": "string", "enum": ["on", "off"]}),
                Value::from("state"),
                "enum=[\"on\",\"off\"]",
            ),
            (
                serde_json::json!({"type": "string", "const": "fixed"}),
                Value::from("kind"),
                "const=\"fixed\"",
            ),
            (
                serde_json::json!({"type": "string", "format": "uuid"}),
                Value::from("id"),
                "format=uuid",
            ),
            (
                serde_json::json!({"type": "string", "format": "email"}),
                Value::from("email"),
                "format=email",
            ),
            (
                serde_json::json!({"type": "string", "format": "uri"}),
                Value::from("url"),
                "format=uri",
            ),
            (
                serde_json::json!({"type": "string", "format": "date"}),
                Value::from("day"),
                "format=date",
            ),
            (
                serde_json::json!({"type": "string", "format": "date-time"}),
                Value::from("at"),
                "format=date-time",
            ),
            (
                serde_json::json!({"type": "string", "format": "time"}),
                Value::from("at"),
                "format=time",
            ),
            (
                serde_json::json!({"type": "string", "format": "ipv4"}),
                Value::from("ip"),
                "format=ipv4",
            ),
            (
                serde_json::json!({"type": "string", "format": "ipv6"}),
                Value::from("ip"),
                "format=ipv6",
            ),
            (
                serde_json::json!({"type": "string", "format": "hostname"}),
                Value::from("host_name"),
                "format=hostname",
            ),
            (
                serde_json::json!({"type": "integer", "minimum": 5}),
                Value::from(1),
                "minimum=5",
            ),
            (
                serde_json::json!({"type": "integer", "maximum": 0}),
                Value::from(1),
                "maximum=0",
            ),
            (
                serde_json::json!({"type": "integer", "exclusiveMinimum": 1}),
                Value::from(1),
                "exclusiveMinimum=1",
            ),
            (
                serde_json::json!({"type": "integer", "minimum": 1, "exclusiveMinimum": true}),
                Value::from(1),
                "exclusiveMinimum=1",
            ),
            (
                serde_json::json!({"type": "integer", "exclusiveMaximum": 1}),
                Value::from(1),
                "exclusiveMaximum=1",
            ),
            (
                serde_json::json!({"type": "integer", "multipleOf": 10}),
                Value::from(1),
                "multipleOf=10",
            ),
            (
                serde_json::json!({"type": "integer", "enum": [4]}),
                Value::from(1),
                "enum=[4]",
            ),
            (
                serde_json::json!({"type": "number", "multipleOf": 0.25}),
                Value::from(1.1),
                "multipleOf=0.25",
            ),
            (
                serde_json::json!({"type": "integer", "format": "int32"}),
                Value::from(4_000_000_000_i64),
                "format=int32",
            ),
            (
                serde_json::json!({"type": "integer", "format": "int64"}),
                python_value("-9223372036854776000").unwrap(),
                "format=int64",
            ),
            (
                serde_json::json!({"type": "integer", "format": "int64"}),
                python_value("9223372036854776000").unwrap(),
                "format=int64",
            ),
            (
                serde_json::json!({"type": "array", "items": {"type": "string"}, "minItems": 2}),
                serde_json::json!(["a"]),
                "minItems=2",
            ),
            (
                serde_json::json!({"type": "array", "items": {"type": "string"}, "maxItems": 0}),
                serde_json::json!(["a"]),
                "maxItems=0",
            ),
        ];
        for (schema, fern, keyword) in cases {
            let c = constraints(schema.clone());
            assert_eq!(rejected_by(&c, fern.clone()), keyword, "{schema}");
            let choice = c
                .choose(&fern)
                .unwrap_or_else(|| panic!("no value for {schema}"));
            assert_eq!(
                c.verdict(choice.value()),
                Verdict::Accepted,
                "{schema}: {choice:?}"
            );
        }
    }

    #[test]
    fn distinct_items_are_deterministic_accepted_and_never_repeat() {
        let snowflake = constraints(serde_json::json!({"$ref": "#/components/schemas/Snowflake"}));
        assert_eq!(
            snowflake.distinct_items(&[Value::from("0")], 3),
            Some(vec![Value::from("0"), Value::from("1"), Value::from("10")])
        );
        let tags = constraints(serde_json::json!({"type": "string", "maxLength": 4}));
        assert_eq!(
            tags.distinct_items(&[Value::from("tags")], 2),
            Some(vec![Value::from("tags"), Value::from("tag2")])
        );
        let counts = constraints(serde_json::json!({"type": "integer", "maximum": 2}));
        assert_eq!(
            counts.distinct_items(&[Value::from(1)], 2),
            Some(vec![Value::from(1), Value::from(2)])
        );
        // Not enough distinct values, a format, or no first item: no padding.
        assert_eq!(counts.distinct_items(&[Value::from(1)], 3), None);
        let ids = constraints(serde_json::json!({"type": "string", "format": "uuid"}));
        assert_eq!(
            ids.distinct_items(&[Value::from(format_sample(Format::Uuid).unwrap())], 2),
            None
        );
        assert_eq!(tags.distinct_items(&[], 2), None);
    }

    #[test]
    fn construction_is_deterministic_and_respects_combined_constraints() {
        let schema = serde_json::json!({
            "type": "string", "pattern": "^[a-z]+$", "minLength": 5, "maxLength": 8
        });
        let first = constraints(schema.clone()).choose(&Value::from("id"));
        assert_eq!(first, constraints(schema).choose(&Value::from("id")));
        assert_eq!(first, Some(Choice::Constructed(Value::from("aaaaa"))));
    }

    #[test]
    fn what_crozier_cannot_decide_or_build_stays_a_residual() {
        // A lookahead the pattern reader cannot construct from.
        let c = constraints(serde_json::json!({"type": "string", "pattern": "^(?=x)[a-z]{3}$"}));
        assert_eq!(
            rejected_by(&c, Value::from("id")),
            "pattern=^(?=x)[a-z]{3}$"
        );
        assert_eq!(c.choose(&Value::from("id")), None);
        // Contradictory lengths admit no value.
        let c = constraints(serde_json::json!({"type": "string", "minLength": 5, "maxLength": 2}));
        assert_eq!(c.choose(&Value::from("id")), None);
        // Out-of-scope keywords neither reject nor block: `not` is one.
        let c = constraints(serde_json::json!({
            "type": "string", "pattern": "^[0-9]+$", "not": {"const": "0"}
        }));
        assert_eq!(c.verdict(&Value::from("0")), Verdict::Accepted);
        // A reference that does not resolve can reject but never accept.
        let c = constraints(serde_json::json!({
            "type": "string", "pattern": "^[0-9]+$", "allOf": [{"$ref": "#/components/schemas/Gone"}]
        }));
        assert_eq!(c.verdict(&Value::from("0")), Verdict::Undecided(None));
        assert_eq!(c.choose(&Value::from("id")), None);
    }

    #[test]
    fn every_keyword_reads_back_as_it_is_written() {
        let keywords = [
            Keyword::Enum(vec![Value::from("a"), Value::from(2)]),
            Keyword::Const(Value::from("x=y")),
            Keyword::Pattern("^a=b\\t$".to_string()),
            Keyword::MinLength(3),
            Keyword::MaxLength(4),
            Keyword::Format(Format::DateTime),
            Keyword::Minimum(-2.5),
            Keyword::Maximum(10.0),
            Keyword::ExclusiveMinimum(0.0),
            Keyword::ExclusiveMaximum(1e3),
            Keyword::MultipleOf(0.25),
            Keyword::MinItems(2),
            Keyword::MaxItems(0),
        ];
        for keyword in keywords {
            assert_eq!(
                Keyword::parse(&keyword.to_string()),
                Some(keyword.clone()),
                "{keyword}"
            );
        }
        for text in ["pattern", "minLength=-1", "format=snowflake", "tooLong=3"] {
            assert_eq!(Keyword::parse(text), None, "{text}");
        }
    }

    #[test]
    fn integers_past_doubles_and_nested_values_compare_exactly() {
        let near = serde_json::from_str::<Value>("9007199254740993").unwrap();
        let rounded = serde_json::from_str::<Value>("9007199254740992").unwrap();
        assert!(!json_equal(&near, &rounded));
        assert!(json_equal(&Value::from(1), &Value::from(1.0)));
        assert!(json_equal(
            &serde_json::json!({"a": [1, 2.0]}),
            &serde_json::json!({"a": [1.0, 2]})
        ));
        assert!(!json_equal(
            &serde_json::json!([1]),
            &serde_json::json!([1, 1])
        ));
    }

    #[test]
    fn python_literals_read_as_the_json_values_they_stand_for() {
        assert_eq!(python_value("\"guild_id\""), Some(Value::from("guild_id")));
        assert_eq!(python_value("\"You\\'ll\""), Some(Value::from("You'll")));
        assert_eq!(python_value("1000000"), Some(Value::from(1_000_000)));
        assert_eq!(python_value("1.1"), Some(Value::from(1.1)));
        assert_eq!(python_value("True"), Some(Value::Bool(true)));
        assert_eq!(python_value("'\"a\"'"), Some(Value::from("\"a\"")));
        assert_eq!(
            python_value("\"tab\\there\""),
            Some(Value::from("tab\there"))
        );
        assert_eq!(python_value("Kind.A"), None);
        assert_eq!(python_value("b\"string\""), None);
    }
}
