//! The worked-example values a schema rejects, repaired and recorded.
//!
//! [`ExampleCtx::repair_example_args`] walks one finished example's keyword
//! arguments against the constraints of the parameters, fields and aliases
//! they document ([`crate::example_values`]). A value Fern's own construction
//! gives that a constraint rejects — a string spelled as its name, a fixed
//! number, a one-item list — is replaced by the value
//! [`ValueConstraints::choose`] picks. Every rejected value, repaired or not,
//! is recorded with its example block, and [`locate`] finds each block in the
//! formatted files to give it its line.

use std::cell::RefCell;

use serde_json::Value;

use super::{Example, ExampleCtx, GeneratedFile};
use crate::example_values::{
    python_value, Choice, Disposition, ExampleValue, Finding, Mechanism, ValueConstraints, Verdict,
};
use crate::ir::{Endpoint, RequestBody, TypeDecl, TypeRef};

/// Fern's own construction for one value, or `None` where the value is not
/// one (a declared example, a value from the specification).
fn construction(
    value: &Value,
    names: &[String],
    lengths: &[(Option<u64>, Option<u64>)],
) -> Option<Mechanism> {
    match value {
        Value::String(text) => {
            if names.iter().any(|name| name == text) {
                Some(Mechanism::Name)
            } else if text == "string" || text == "value" {
                Some(Mechanism::Placeholder)
            } else if lengths.iter().any(|(min, max)| {
                crate::ir::fallback_string_sample(*min, *max).as_deref() == Some(text.as_str())
            }) {
                Some(Mechanism::Sized)
            } else {
                None
            }
        }
        Value::Number(number) => {
            let fixed = [1.0, 1_000_000.0, 1.1];
            number
                .as_f64()
                .is_some_and(|n| fixed.contains(&n))
                .then_some(Mechanism::Number)
        }
        _ => None,
    }
}

/// One rejected value found while walking a block, before it has a line.
pub(super) struct Pending {
    /// What precedes each enclosing argument on its line, outermost first, then
    /// what precedes the value itself: `name=`, `"key": ` or nothing. The value
    /// is found on the first line holding it at or after its anchors' lines.
    needles: Vec<String>,
    value: Finding,
}

/// The file an example block is written into.
#[derive(Clone, Copy)]
pub(super) enum Destination {
    /// A client method's docstring, in a `.py` module.
    Docstring,
    /// `README.md`.
    Readme,
    /// `reference.md`.
    Reference,
}

/// One example block a writer produced, with its rejected values.
struct Block {
    destination: Destination,
    lines: Vec<String>,
    values: Vec<Pending>,
}

thread_local! {
    /// The blocks of the generation in progress on this thread.
    static BLOCKS: RefCell<Option<Vec<Block>>> = const { RefCell::new(None) };
}

/// Start recording this thread's example blocks.
pub(super) fn start() {
    BLOCKS.with(|blocks| *blocks.borrow_mut() = Some(Vec::new()));
}

/// Record a finished block, if recording.
pub(super) fn record(destination: Destination, lines: &[String], values: Vec<Pending>) {
    if values.is_empty() {
        return;
    }
    BLOCKS.with(|blocks| {
        if let Some(blocks) = blocks.borrow_mut().as_mut() {
            blocks.push(Block {
                destination,
                lines: lines.to_vec(),
                values,
            });
        }
    });
}

/// Every recorded value at its line in `files`, then stop recording. A block
/// is found wherever its lines stand, trimmed, in a file its writer writes:
/// `README.md`, `reference.md`, or a `.py` module's docstring.
pub(super) fn locate(files: &[GeneratedFile]) -> Vec<ExampleValue> {
    let blocks = BLOCKS
        .with(|blocks| blocks.borrow_mut().take())
        .unwrap_or_default();
    let mut out: Vec<ExampleValue> = Vec::new();
    let texts: Vec<(String, Vec<&str>)> = files
        .iter()
        .map(|file| {
            (
                file.path.to_string_lossy().replace('\\', "/"),
                file.contents.lines().map(str::trim).collect(),
            )
        })
        .collect();
    for block in &blocks {
        let wanted: Vec<&str> = block.lines.iter().map(|line| line.trim()).collect();
        let Some(first) = wanted.first() else {
            continue;
        };
        for (path, lines) in &texts {
            let belongs = match block.destination {
                Destination::Reference => path == "reference.md",
                Destination::Readme => path == "README.md",
                Destination::Docstring => path.ends_with(".py"),
            };
            if !belongs || lines.len() < wanted.len() {
                continue;
            }
            for start in 0..=lines.len() - wanted.len() {
                if lines[start] != *first || lines[start..start + wanted.len()] != wanted[..] {
                    continue;
                }
                let mut cursor = std::collections::BTreeMap::<String, usize>::new();
                for pending in &block.values {
                    let Some((own, anchors)) = pending.needles.split_last() else {
                        continue;
                    };
                    let mut from = 0;
                    for anchor in anchors.iter().filter(|anchor| !anchor.is_empty()) {
                        match wanted[from..]
                            .iter()
                            .position(|line| holds_at_boundary(line, anchor))
                        {
                            Some(found) => from += found,
                            None => break,
                        }
                    }
                    let needle = format!(
                        "{}{own}{}",
                        pending.needles.join("\u{0}"),
                        pending.value.crozier
                    );
                    let from = cursor.get(&needle).copied().unwrap_or(0).max(from);
                    let find = format!("{own}{}", pending.value.crozier);
                    // The Markdown writers spell an integral float without its
                    // `.0` where another item follows (`1,` beside a last `1.0`).
                    let integral = pending
                        .value
                        .crozier
                        .strip_suffix(".0")
                        .filter(|digits| digits.bytes().all(|b| b.is_ascii_digit() || b == b'-'))
                        .map(|digits| format!("{own}{digits},"));
                    // A list the writer spreads over lines is found by its
                    // opening line; a list that is itself an item of one opens
                    // on a bare `[` (RS-Server's `interval=[[None, None]]`).
                    let opening = format!("{own}[");
                    let Some(offset) = wanted[from..]
                        .iter()
                        .position(|line| {
                            holds_at_boundary(line, &find)
                                || integral
                                    .as_deref()
                                    .is_some_and(|spelled| holds_at_boundary(line, spelled))
                        })
                        .or_else(|| {
                            pending.value.crozier.starts_with('[').then(|| {
                                wanted[from..].iter().position(|line| {
                                    if own.is_empty() {
                                        *line == "["
                                    } else {
                                        line.ends_with('[') && holds_at_boundary(line, &opening)
                                    }
                                })
                            })?
                        })
                        .map(|found| from + found)
                    else {
                        continue;
                    };
                    cursor.insert(needle, offset + 1);
                    out.push(ExampleValue {
                        file: path.clone(),
                        line: std::num::NonZeroUsize::MIN.saturating_add(start + offset),
                        finding: pending.value.clone(),
                    });
                }
            }
        }
    }
    // A block written twice in one file is one set of values.
    out.sort_by(|a, b| {
        (&a.file, a.line, &a.finding.argument).cmp(&(&b.file, b.line, &b.finding.argument))
    });
    out.dedup_by(|a, b| a.render() == b.render());
    out
}

/// Where a list example's items came from, which decides whether it may be
/// repaired.
#[derive(Clone, Copy, PartialEq, Eq)]
enum Origin {
    /// The specification spells the list out: its own, and kept.
    Declared,
    /// Fern's construction: repaired where its schema rejects it.
    Constructed,
}

/// The schemas a list value documents: the list's type and constraint sets,
/// and its items'.
struct ListSchemas<'s> {
    list: &'s TypeRef,
    sets: &'s [&'s ValueConstraints],
    item: &'s TypeRef,
    items: &'s [&'s ValueConstraints],
}

/// Whether `needle` occurs in `line` where no identifier character precedes
/// it: `id="0"` is not found inside `webhook_id="0"`.
fn holds_at_boundary(line: &str, needle: &str) -> bool {
    line.match_indices(needle).any(|(at, _)| {
        line[..at]
            .chars()
            .next_back()
            .is_none_or(|before| !(before.is_alphanumeric() || before == '_'))
    })
}

/// What one argument documents: its type, its own constraints, and the names
/// Fern's construction may spell it by.
struct Documented<'e> {
    type_ref: &'e TypeRef,
    constraints: Option<&'e ValueConstraints>,
    names: Vec<String>,
}

/// The parameter or field each keyword argument of `ep`'s example documents.
fn documented(ep: &Endpoint) -> Vec<(String, Documented<'_>)> {
    let mut out = Vec::new();
    for pp in &ep.path_params {
        out.push((
            pp.py_name.clone(),
            Documented {
                type_ref: &pp.type_ref,
                constraints: pp.constraints.as_deref(),
                names: vec![pp.wire_name.clone()],
            },
        ));
    }
    for qp in &ep.query_params {
        out.push((
            qp.py_name.clone(),
            Documented {
                type_ref: &qp.type_ref,
                constraints: qp.constraints.as_deref(),
                names: vec![qp.wire_name.clone()],
            },
        ));
    }
    for hp in ep
        .header_params
        .iter()
        .chain(&ep.extensions.idempotency_headers)
    {
        let mut words = crate::naming::split_words(&hp.wire_name).into_iter();
        let mut camel = words.next().unwrap_or_default();
        for word in words {
            camel.push_str(&crate::naming::to_pascal_case(&word));
        }
        out.push((
            hp.py_name.clone(),
            Documented {
                type_ref: &hp.type_ref,
                constraints: hp.constraints.as_deref(),
                names: vec![hp.wire_name.clone(), camel],
            },
        ));
    }
    match &ep.request_body {
        Some(RequestBody::Single(single)) => out.push((
            "request".to_string(),
            Documented {
                type_ref: &single.type_ref,
                constraints: None,
                names: vec!["request".to_string()],
            },
        )),
        Some(RequestBody::Inline(fields)) => {
            for f in fields {
                for keyword in [
                    f.py_name.clone(),
                    crate::naming::model_field_name(&f.wire_name),
                ] {
                    out.push((
                        keyword,
                        Documented {
                            type_ref: &f.type_ref,
                            constraints: f.constraints.as_deref(),
                            names: vec![f.wire_name.clone()],
                        },
                    ));
                }
            }
        }
        Some(RequestBody::Form(form)) => {
            for f in &form.fields {
                out.push((
                    f.py_name.clone(),
                    Documented {
                        type_ref: &f.type_ref,
                        constraints: f.constraints.as_deref(),
                        names: vec![f.wire_name.clone()],
                    },
                ));
            }
        }
        _ => {}
    }
    out
}

/// One merged view of every constraint set a value must satisfy.
fn merged(sets: &[&ValueConstraints]) -> ValueConstraints {
    let mut out = ValueConstraints::default();
    for set in sets {
        out.keywords.extend(set.keywords.iter().cloned());
        out.examples.extend(set.examples.iter().cloned());
        if out.default.is_none() {
            out.default.clone_from(&set.default);
        }
        out.incomplete |= set.incomplete;
        out.unique_items |= set.unique_items;
        out.excluded.extend(set.excluded.iter().cloned());
        if out.seed.is_none() {
            out.seed.clone_from(&set.seed);
        }
    }
    let nested = |part: fn(&ValueConstraints) -> Option<&ValueConstraints>| {
        let parts: Vec<&ValueConstraints> = sets.iter().filter_map(|set| part(set)).collect();
        (!parts.is_empty()).then(|| Box::new(merged(&parts)))
    };
    out.items = nested(|set| set.items.as_deref());
    out.values = nested(|set| set.values.as_deref());
    out
}

impl ExampleCtx<'_> {
    /// Repair and record the rejected values among one example's keyword
    /// arguments; see the module documentation.
    pub(super) fn repair_example_args(
        &mut self,
        ep: &Endpoint,
        args: &mut [(Option<String>, Example)],
    ) -> Vec<Pending> {
        let documented = documented(ep);
        let mut pending = Vec::new();
        for (keyword, value) in args.iter_mut() {
            let Some(keyword) = keyword.clone() else {
                continue;
            };
            let Some((_, doc)) = documented.iter().find(|(name, _)| *name == keyword) else {
                continue;
            };
            let own: Vec<&ValueConstraints> = doc.constraints.into_iter().collect();
            self.repair_value(
                value,
                doc.type_ref,
                &own,
                &doc.names,
                &keyword,
                &[format!("{keyword}=")],
                &mut pending,
            );
        }
        pending
    }

    /// The constraint sets the aliases `t` names carry, outermost first.
    fn alias_constraints(&self, t: &TypeRef) -> Vec<ValueConstraints> {
        let mut out = Vec::new();
        let mut current = t;
        for _ in 0..16 {
            match current {
                TypeRef::Optional(inner) => current = inner,
                TypeRef::Named(name) => match self.find(name) {
                    Some(TypeDecl::Alias(alias)) => {
                        out.extend(alias.constraints.as_deref().cloned());
                        current = &alias.target;
                    }
                    _ => break,
                },
                _ => break,
            }
        }
        out
    }

    /// `t` with its optional wrappers and scalar aliases resolved.
    fn resolved<'t>(&'t self, t: &'t TypeRef) -> &'t TypeRef {
        let mut current = t;
        for _ in 0..16 {
            match current {
                TypeRef::Optional(inner) => current = inner,
                TypeRef::Named(name) => match self.find(name) {
                    Some(TypeDecl::Alias(alias)) => current = &alias.target,
                    _ => break,
                },
                _ => break,
            }
        }
        current
    }

    #[allow(
        clippy::too_many_arguments,
        reason = "a value's place is its type, constraints, names, path and line needles"
    )]
    fn repair_value(
        &mut self,
        example: &mut Example,
        t: &TypeRef,
        own: &[&ValueConstraints],
        names: &[String],
        path: &str,
        needles: &[String],
        pending: &mut Vec<Pending>,
    ) {
        let aliased = self.alias_constraints(t);
        let mut sets: Vec<&ValueConstraints> = own.to_vec();
        sets.extend(aliased.iter());
        let sets: Vec<ValueConstraints> = sets.into_iter().cloned().collect();
        let sets: Vec<&ValueConstraints> = sets.iter().collect();
        let resolved = self.resolved(t).clone();
        if let (Example::Atom(literal), TypeRef::Named(name)) = (&*example, &resolved) {
            if let Some(TypeDecl::Enum(declaration)) = self.find(name) {
                if !sets.is_empty() {
                    let combined = merged(&sets);
                    self.record_enum_member(
                        declaration,
                        literal,
                        &combined,
                        path,
                        needles,
                        pending,
                    );
                }
                return;
            }
        }
        match example {
            Example::Atom(literal) => {
                if sets.is_empty() {
                    return;
                }
                let Some(value) = python_value(literal) else {
                    return;
                };
                let combined = merged(&sets);
                let lengths = [combined.keywords.iter().fold(
                    (None, None),
                    |(min, max), keyword| match keyword {
                        crate::example_values::Keyword::MinLength(n) => (Some(*n), max),
                        crate::example_values::Keyword::MaxLength(n) => (min, Some(*n)),
                        _ => (min, max),
                    },
                )];
                // Fern writes a declared integer past 2^53 as the double nearest
                // it; where that leaves the schema's range, the earlier
                // `int64-example-rounded-out-of-range` departure writes it exactly.
                // Only an integer literal past 2^53 has a nearer double to
                // round to.
                let past_doubles = value.as_number().is_some_and(|number| {
                    number
                        .as_i64()
                        .map(i64::unsigned_abs)
                        .or_else(|| number.as_u64())
                        .is_some_and(|magnitude| magnitude > 1 << 53)
                });
                if let (true, Value::Number(number)) = (past_doubles, &value) {
                    let rounded = crate::ir::js_integer_literal(number);
                    if rounded != *literal {
                        if let Some(Verdict::Rejected(keyword)) =
                            python_value(&rounded).map(|fern| combined.verdict(&fern))
                        {
                            pending.push(Pending {
                                needles: needles.to_vec(),
                                value: Finding {
                                    argument: path.to_string(),
                                    fern: rounded,
                                    crozier: literal.clone(),
                                    constraint: keyword.clone(),
                                    mechanism: Some(Mechanism::Rounded),
                                    disposition: Disposition::Repaired,
                                },
                            });
                            return;
                        }
                    }
                }
                let constraint = match combined.verdict(&value) {
                    Verdict::Accepted | Verdict::Undecided(None) => return,
                    Verdict::Undecided(Some(keyword)) => {
                        pending.push(Pending {
                            needles: needles.to_vec(),
                            value: Finding {
                                argument: path.to_string(),
                                fern: literal.clone(),
                                crozier: literal.clone(),
                                constraint: keyword.clone(),
                                mechanism: construction(&value, names, &lengths),
                                disposition: Disposition::ResidualUndecidable,
                            },
                        });
                        return;
                    }
                    Verdict::Rejected(keyword) => keyword,
                };
                let fern = literal.clone();
                // A value that is no construction of Fern's is one the
                // specification declares, which its own schema rejects: the
                // `schema-rejected-declared-example` departure repairs it as
                // it does a construction.
                let mechanism =
                    construction(&value, names, &lengths).unwrap_or(Mechanism::Declared);
                // A declared value its schema rejects gives way to Fern's own
                // construction for the slot where the schema accepts that, so
                // crozier writes what Fern writes wherever Fern's is valid;
                // else to the schema's repair.
                let constructed = (mechanism == Mechanism::Declared)
                    .then(|| self.accepted_construction(&resolved, names, &value, &combined))
                    .flatten();
                let (crozier, disposition) = match constructed {
                    Some(text) => (text, Disposition::Repaired),
                    None => match combined.choose(&value) {
                        Some(choice) => match self.rendered(&resolved, &choice) {
                            Some(rendered) => (rendered, Disposition::Repaired),
                            None => (fern.clone(), Disposition::ResidualUnconstructible),
                        },
                        None if combined.incomplete => {
                            (fern.clone(), Disposition::ResidualUndecidable)
                        }
                        None if combined.admits_nothing(&value) => {
                            (fern.clone(), Disposition::UnsatisfiableSchema)
                        }
                        None => (fern.clone(), Disposition::ResidualUnconstructible),
                    },
                };
                if disposition == Disposition::Repaired {
                    literal.clone_from(&crozier);
                }
                pending.push(Pending {
                    needles: needles.to_vec(),
                    value: Finding {
                        argument: path.to_string(),
                        fern,
                        crozier,
                        constraint,
                        mechanism: Some(mechanism),
                        disposition,
                    },
                });
            }
            Example::List(_) | Example::ExplicitList(_) | Example::ReferenceList(_) => {
                let item_type = match &resolved {
                    TypeRef::List(inner) | TypeRef::Set(inner) => (**inner).clone(),
                    _ => return,
                };
                let fern = example.flat();
                let origin = if matches!(example, Example::ExplicitList(_)) {
                    Origin::Declared
                } else {
                    Origin::Constructed
                };
                let (Example::List(items)
                | Example::ExplicitList(items)
                | Example::ReferenceList(items)) = &mut *example
                else {
                    return;
                };
                let item_sets: Vec<&ValueConstraints> =
                    sets.iter().filter_map(|set| set.items.as_deref()).collect();
                for (index, item) in items.iter_mut().enumerate() {
                    self.repair_value(
                        item,
                        &item_type,
                        &item_sets,
                        names,
                        &format!("{path}[{index}]"),
                        &[needles, &[String::new()]].concat(),
                        pending,
                    );
                }
                let lists = ListSchemas {
                    list: &resolved,
                    sets: &sets,
                    item: &item_type,
                    items: &item_sets,
                };
                self.repair_length(example, &lists, fern, origin, path, needles, pending);
            }
            Example::Call(name, call_args) => {
                let fields = self.constructor_fields(name);
                for (keyword, value) in call_args.iter_mut() {
                    let Some(keyword) = keyword.clone() else {
                        continue;
                    };
                    let Some(field) = fields.iter().find(|f| {
                        f.py_name == keyword || crate::naming::field_name(&f.wire_name) == keyword
                    }) else {
                        continue;
                    };
                    let own: Vec<&ValueConstraints> =
                        field.constraints.as_deref().into_iter().collect();
                    let field_type = field.type_ref.clone();
                    let field_names = vec![field.wire_name.clone()];
                    self.repair_value(
                        value,
                        &field_type,
                        &own,
                        &field_names,
                        &format!("{path}.{keyword}"),
                        &[needles, &[format!("{keyword}=")]].concat(),
                        pending,
                    );
                }
            }
            Example::Dict(pairs) | Example::DocDict(pairs) | Example::ReferenceDict(pairs) => {
                let value_type = match &resolved {
                    TypeRef::Dict(_, value) => (**value).clone(),
                    _ => return,
                };
                let value_sets: Vec<&ValueConstraints> = sets
                    .iter()
                    .filter_map(|set| set.values.as_deref())
                    .collect();
                for (key, value) in pairs.iter_mut() {
                    self.repair_value(
                        value,
                        &value_type,
                        &value_sets,
                        &[],
                        &format!("{path}.{key}"),
                        &[needles, &[format!("{key:?}: ")]].concat(),
                        pending,
                    );
                }
            }
            Example::Wrapped(..) => {}
        }
    }

    /// Repair and record a list whose item count its schema's `minItems` or
    /// `maxItems` rejects, after its items were walked. Fern's list is its
    /// construction (one item, two in its fallback, none where it can write no
    /// item); crozier writes the declared example, else the default, each
    /// where the schema accepts it, else Fern's items cut to `maxItems` or
    /// padded to `minItems` with copies of the first. A list the specification
    /// spells out is its own; an empty one has no item to copy.
    #[allow(
        clippy::too_many_arguments,
        reason = "a list's place is its example, schemas, Fern's spelling, path and needles"
    )]
    fn repair_length(
        &mut self,
        example: &mut Example,
        lists: &ListSchemas<'_>,
        fern: String,
        origin: Origin,
        path: &str,
        needles: &[String],
        pending: &mut Vec<Pending>,
    ) {
        let (t, sets) = (lists.list, lists.sets);
        let (Example::List(items) | Example::ExplicitList(items) | Example::ReferenceList(items)) =
            &mut *example
        else {
            return;
        };
        let lengths = ValueConstraints {
            keywords: sets
                .iter()
                .flat_map(|set| set.keywords.iter())
                .filter(|keyword| {
                    matches!(
                        keyword,
                        crate::example_values::Keyword::MinItems(_)
                            | crate::example_values::Keyword::MaxItems(_)
                    )
                })
                .cloned()
                .collect(),
            examples: sets
                .iter()
                .flat_map(|set| set.examples.iter().cloned())
                .collect(),
            default: sets.iter().find_map(|set| set.default.clone()),
            ..ValueConstraints::default()
        };
        let shape = Value::Array(vec![Value::Null; items.len()]);
        let Verdict::Rejected(keyword) = lengths.verdict(&shape) else {
            return;
        };
        let choice = (origin == Origin::Constructed && !items.is_empty())
            .then(|| merged(sets).list_view().choose(&shape))
            .flatten();
        // Fern writes no item where it has none to show (a tuple's
        // `prefixItems`, a nullable item an executable docstring leaves out);
        // crozier writes the items the schema's own shape builds.
        let seeded = (origin == Origin::Constructed && items.is_empty())
            .then(|| merged(sets).seeded_items())
            .flatten();
        let disposition = if origin == Origin::Declared {
            Disposition::DeclaredInSpec
        } else if let Some(seeds) = seeded {
            let nested = |items: Vec<Example>| match &*example {
                Example::ReferenceList(_) => Example::ReferenceList(items),
                Example::ExplicitList(_) => Example::ExplicitList(items),
                _ => Example::List(items),
            };
            let built: Option<Vec<Example>> = seeds
                .iter()
                .map(|seed| self.seeded_item(lists.item, seed, &nested))
                .collect();
            match built {
                Some(built) => {
                    if let Example::List(items)
                    | Example::ExplicitList(items)
                    | Example::ReferenceList(items) = example
                    {
                        *items = built;
                    }
                    Disposition::Repaired
                }
                None => Disposition::ResidualUnconstructible,
            }
        } else {
            match &choice {
                Some(Choice::Constructed(Value::Array(target))) => {
                    let target = target.len();
                    if target <= items.len() {
                        items.truncate(target);
                        Disposition::Repaired
                    } else if sets.iter().any(|set| set.unique_items) {
                        match self.distinct_items(items, lists, target) {
                            Some(padding) => {
                                items.extend(padding);
                                Disposition::Repaired
                            }
                            None => Disposition::ResidualUnconstructible,
                        }
                    } else {
                        let first = items[0].clone();
                        items.resize(target, first);
                        Disposition::Repaired
                    }
                }
                Some(chosen) => match self.value_from_example(t, &chosen.value().to_string()) {
                    Some(
                        rendered @ (Example::List(_)
                        | Example::ExplicitList(_)
                        | Example::ReferenceList(_)),
                    ) => {
                        *example = rendered;
                        Disposition::Repaired
                    }
                    _ => Disposition::ResidualUnconstructible,
                },
                None => Disposition::ResidualUnconstructible,
            }
        };
        pending.push(Pending {
            needles: needles.to_vec(),
            value: Finding {
                argument: path.to_string(),
                crozier: if disposition == Disposition::Repaired {
                    example.flat()
                } else {
                    fern.clone()
                },
                fern,
                constraint: keyword.clone(),
                mechanism: (origin == Origin::Constructed).then_some(Mechanism::Array),
                disposition,
            },
        });
    }

    /// One seeded item of an empty list ([`ValueConstraints::seeded_items`]) as
    /// the writer spells a value of the item type `t`: through the type where
    /// it is one (`None` for a nullable item, an enum's member), and as the
    /// JSON value itself, lists spelled by `nested`, where the item is free
    /// form. `None` where the type does not take the value.
    fn seeded_item(
        &mut self,
        t: &TypeRef,
        seed: &Value,
        nested: &dyn Fn(Vec<Example>) -> Example,
    ) -> Option<Example> {
        fn literal(value: &Value, nested: &dyn Fn(Vec<Example>) -> Example) -> Option<Example> {
            Some(match value {
                Value::Null => Example::Atom("None".to_string()),
                Value::Bool(flag) => {
                    Example::Atom(if *flag { "True" } else { "False" }.to_string())
                }
                Value::Number(_) | Value::String(_) => {
                    Example::Atom(crate::ir::example_literal(value)?)
                }
                Value::Array(items) => nested(
                    items
                        .iter()
                        .map(|item| literal(item, nested))
                        .collect::<Option<_>>()?,
                ),
                Value::Object(entries) => Example::Dict(
                    entries
                        .iter()
                        .map(|(key, entry)| Some((key.clone(), literal(entry, nested)?)))
                        .collect::<Option<_>>()?,
                ),
            })
        }
        let resolved = self.resolved(t).clone();
        if matches!(resolved, TypeRef::Primitive(crate::ir::Prim::Any)) {
            return literal(seed, nested);
        }
        if seed.is_null() {
            return matches!(self.unaliased(t), TypeRef::Optional(_))
                .then(|| Example::Atom("None".to_string()));
        }
        self.value_from_example(t, &seed.to_string())
    }

    /// Fern's own construction for a value of `t` passed by `names` (its
    /// name, `"value"` in a map, a fixed number), as the writer spells it,
    /// when it is a scalar of `value`'s kind that `constraints` accept.
    fn accepted_construction(
        &mut self,
        t: &TypeRef,
        names: &[String],
        value: &Value,
        constraints: &ValueConstraints,
    ) -> Option<String> {
        let slot = names
            .first()
            .map_or(super::Slot::Map, |name| super::Slot::Named(name));
        let Example::Atom(text) = self.without_recording(|ctx| ctx.value(t, slot)) else {
            return None;
        };
        let built = python_value(&text)?;
        (std::mem::discriminant(&built) == std::mem::discriminant(value)
            && constraints.verdict(&built) == Verdict::Accepted)
            .then_some(text)
    }

    /// `t` with its scalar aliases resolved but its `Optional` kept.
    fn unaliased<'t>(&'t self, t: &'t TypeRef) -> &'t TypeRef {
        let mut current = t;
        for _ in 0..16 {
            match current {
                TypeRef::Named(name) => match self.find(name) {
                    Some(TypeDecl::Alias(alias)) => current = &alias.target,
                    _ => break,
                },
                _ => break,
            }
        }
        current
    }

    /// The items that pad a `uniqueItems` list of scalars to `target`, each
    /// pairwise distinct and accepted by the item schema
    /// ([`ValueConstraints::distinct_items`]), as the writer spells them;
    /// `None` where its items are not all scalars or no such values exist.
    fn distinct_items(
        &mut self,
        items: &[Example],
        lists: &ListSchemas<'_>,
        target: usize,
    ) -> Option<Vec<Example>> {
        let kept: Vec<Value> = items
            .iter()
            .map(|item| match item {
                Example::Atom(literal) => python_value(literal),
                _ => None,
            })
            .collect::<Option<_>>()?;
        let aliased = self.alias_constraints(lists.item);
        let mut sets: Vec<&ValueConstraints> = lists.items.to_vec();
        sets.extend(aliased.iter());
        let values = merged(&sets).distinct_items(&kept, target)?;
        let resolved = self.resolved(lists.item).clone();
        values[kept.len()..]
            .iter()
            .map(|value| {
                match self
                    .without_recording(|ctx| ctx.value_from_example(&resolved, &value.to_string()))
                {
                    Some(atom @ Example::Atom(_)) => Some(atom),
                    _ => None,
                }
            })
            .collect()
    }

    /// Record an enum member a schema rejects. Fern's value is the enum's first
    /// member; where `pattern-narrowed-enum-example` chose another, crozier's
    /// is that one. An enum is never repaired here: a rejected member crozier
    /// still writes is a residual, unconstructible where the enum's selection
    /// found no member the whole schema accepts, undecidable where an in-scope
    /// keyword was out of view.
    fn record_enum_member(
        &self,
        declaration: &crate::ir::EnumType,
        literal: &str,
        combined: &ValueConstraints,
        path: &str,
        needles: &[String],
        pending: &mut Vec<Pending>,
    ) {
        let literals = self.enum_type == crate::settings::EnumType::Literals;
        let spell = |member: &crate::ir::EnumMember| {
            if literals {
                let text = super::literal_enum_value(&member.value);
                if self.documentation {
                    text.replace('\'', "\\'")
                } else {
                    text
                }
            } else {
                format!("{}.{}", declaration.name, member.name)
            }
        };
        let Some(first) = declaration.members.first() else {
            return;
        };
        let wire = |member: &crate::ir::EnumMember| Value::String(member.value.clone());
        let Some(written) = declaration
            .members
            .iter()
            .find(|member| spell(member) == literal)
        else {
            return;
        };
        let Verdict::Rejected(keyword) = combined.verdict(&wire(first)) else {
            return;
        };
        // The enum's own selection reads the whole schema, a `not` beside the
        // keywords in scope included: where it keeps Fern's member, no member
        // satisfies that schema, unless an in-scope keyword was out of view.
        let disposition = if written.value != first.value {
            Disposition::Repaired
        } else if combined.incomplete {
            Disposition::ResidualUndecidable
        } else if combined.admits_nothing(&wire(first)) {
            Disposition::UnsatisfiableSchema
        } else {
            Disposition::ResidualUnconstructible
        };
        pending.push(Pending {
            needles: needles.to_vec(),
            value: Finding {
                argument: path.to_string(),
                fern: spell(first),
                crozier: literal.to_string(),
                constraint: keyword.clone(),
                mechanism: Some(Mechanism::EnumMember),
                disposition,
            },
        });
    }

    /// The fields a constructor named `name` takes, its bases' first.
    fn constructor_fields(&self, name: &str) -> Vec<crate::ir::Field> {
        match self.find(name) {
            Some(TypeDecl::Object(object)) => {
                let mut out = Vec::new();
                for base in &object.bases {
                    out.extend(self.constructor_fields(base));
                }
                out.extend(object.fields.iter().cloned());
                out
            }
            _ => self
                .types
                .iter()
                .chain(self.tag_decls.iter().map(|tag| &tag.decl))
                .find_map(|decl| match decl {
                    TypeDecl::DiscriminatedUnion(union) => union
                        .members
                        .iter()
                        .find(|member| member.class_name == name)
                        .map(|member| member.fields.clone()),
                    _ => None,
                })
                .unwrap_or_default(),
        }
    }

    /// The chosen value as the writer spells a value of type `t`.
    fn rendered(&mut self, t: &TypeRef, choice: &Choice) -> Option<String> {
        let json = choice.value().to_string();
        match self.without_recording(|ctx| ctx.value_from_example(t, &json))? {
            Example::Atom(text) => Some(text),
            _ => None,
        }
    }
}

#[cfg(test)]
mod tests {
    use crate::example_values::{Disposition, ExampleValue, Mechanism};

    /// Generate `document` as the CLI does, with every rejected example value.
    fn generated(document: serde_json::Value) -> (Vec<(String, String)>, Vec<ExampleValue>) {
        let doc: crate::openapi::OpenApi =
            serde_json::from_value(document).expect("document deserializes");
        let config = crate::config::GenerateConfig::new(
            std::path::PathBuf::from("openapi.yml"),
            std::path::PathBuf::from("out"),
            Some("api".to_string()),
            None,
            None,
            crate::settings::ExtraFields::default(),
            "Api",
        )
        .expect("the config is well formed");
        let (files, values) = super::super::generate_recording(&crate::ir::build(&doc, &config))
            .expect("the document generates");
        let files = files
            .into_iter()
            .map(|file| {
                (
                    file.path.to_string_lossy().replace('\\', "/"),
                    file.contents,
                )
            })
            .collect();
        (files, values)
    }

    /// A document whose one operation takes the path parameter `zone` under
    /// `zone`'s schema and a required query parameter `count` under `count`'s.
    /// Answering text, Fern's example writer passes `zone` by its name even
    /// where its schema declares an example; answering JSON, it does so only
    /// where none is declared.
    fn document(
        zone: serde_json::Value,
        count: serde_json::Value,
        text: bool,
    ) -> serde_json::Value {
        let media = if text {
            "text/plain"
        } else {
            "application/json"
        };
        serde_json::json!({
            "openapi": "3.0.3",
            "info": {"title": "Api", "version": "1"},
            "paths": {"/zones/{zone}": {"get": {
                "operationId": "readZone",
                "parameters": [
                    {"name": "zone", "in": "path", "required": true,
                        "schema": {"$ref": "#/components/schemas/Zone"}},
                    {"name": "count", "in": "query", "required": true, "schema": count}
                ],
                "responses": {"200": {"description": "OK",
                    "content": {media: {"schema": {"type": "string"}}}}}
            }}},
            "components": {"schemas": {"Zone": zone}}
        })
    }

    /// The keyword values `client.read_zone(...)` passes in the docstring of
    /// the generated client.
    fn docstring_arguments(files: &[(String, String)]) -> Vec<String> {
        let client = &files
            .iter()
            .find(|(path, _)| path == "src/api/client.py")
            .expect("a root client")
            .1;
        let start = client.find("client.read_zone(").expect("an example call");
        client[start..]
            .lines()
            .skip(1)
            .take_while(|line| line.trim() != ")")
            .map(|line| line.trim().to_string())
            .collect()
    }

    #[test]
    fn the_declared_example_is_written_where_the_schema_accepts_it() {
        let (files, values) = generated(document(
            serde_json::json!({"type": "string", "pattern": "^[a-z]{2}-[0-9]$",
                "example": "eu-1", "default": "us-1"}),
            serde_json::json!({"type": "integer"}),
            true,
        ));
        assert_eq!(docstring_arguments(&files), ["zone=\"eu-1\",", "count=1,"]);
        let zone: Vec<&ExampleValue> = values
            .iter()
            .filter(|v| v.finding.argument == "zone")
            .collect();
        assert!(!zone.is_empty());
        for value in zone {
            assert_eq!(
                (
                    value.finding.fern.as_str(),
                    value.finding.crozier.as_str(),
                    value.finding.constraint.to_string()
                ),
                (
                    "\"zone\"",
                    "\"eu-1\"",
                    "pattern=^[a-z]{2}-[0-9]$".to_string()
                )
            );
            assert_eq!(value.finding.mechanism, Some(Mechanism::Name));
            assert_eq!(value.finding.disposition, Disposition::Repaired);
        }
    }

    #[test]
    fn the_default_is_written_next_where_the_example_is_rejected() {
        let (files, _) = generated(document(
            serde_json::json!({"type": "string", "pattern": "^[a-z]{2}-[0-9]$",
                "example": "EU-1", "default": "us-1"}),
            serde_json::json!({"type": "integer"}),
            true,
        ));
        assert_eq!(docstring_arguments(&files), ["zone=\"us-1\",", "count=1,"]);
    }

    #[test]
    fn a_constructed_value_satisfies_each_constraint_kind_in_scope() {
        let string_cases = [
            (
                serde_json::json!({"type": "string", "pattern": "^(0|[1-9][0-9]*)$"}),
                "zone=\"0\",",
            ),
            (
                serde_json::json!({"type": "string", "minLength": 6}),
                "zone=\"banana\",",
            ),
            (
                serde_json::json!({"type": "string", "maxLength": 2}),
                "zone=\"zo\",",
            ),
            (
                serde_json::json!({"type": "string", "format": "uuid"}),
                "zone=\"d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32\",",
            ),
            (
                serde_json::json!({"type": "string", "format": "email"}),
                "zone=\"user@example.com\",",
            ),
            (
                serde_json::json!({"type": "string", "format": "uri"}),
                "zone=\"https://example.com\",",
            ),
            (
                serde_json::json!({"type": "string", "format": "ipv4"}),
                "zone=\"192.0.2.1\",",
            ),
            (
                serde_json::json!({"type": "string", "format": "ipv6"}),
                "zone=\"2001:db8::1\",",
            ),
            (
                serde_json::json!({"type": "string", "format": "time"}),
                "zone=\"09:30:00Z\",",
            ),
            (
                serde_json::json!({"type": "string", "format": "hostname", "pattern": "^[a-z.]+$",
                "minLength": 5}),
                "zone=\"example.com\",",
            ),
        ];
        for (zone, expected) in string_cases {
            let (files, values) = generated(document(
                zone.clone(),
                serde_json::json!({"type": "integer"}),
                false,
            ));
            assert_eq!(docstring_arguments(&files)[0], expected, "{zone}");
            assert!(
                !values.is_empty()
                    && values.iter().all(|value| value.finding.fern == "\"zone\""
                        && value.finding.mechanism == Some(Mechanism::Name)
                        && value.finding.disposition == Disposition::Repaired),
                "{zone}: {values:?}"
            );
        }
        let number_cases = [
            (
                serde_json::json!({"type": "integer", "minimum": 5}),
                "count=5,",
            ),
            (
                serde_json::json!({"type": "integer", "maximum": -3}),
                "count=-3,",
            ),
            (
                serde_json::json!({"type": "integer", "minimum": 1, "exclusiveMinimum": true}),
                "count=2,",
            ),
            (
                serde_json::json!({"type": "integer", "maximum": 1, "exclusiveMaximum": true}),
                "count=0,",
            ),
            (
                serde_json::json!({"type": "integer", "multipleOf": 25}),
                "count=25,",
            ),
            (
                serde_json::json!({"type": "integer", "enum": [4]}),
                "count=4,",
            ),
            (
                serde_json::json!({"type": "number", "minimum": 2.5}),
                "count=2.5,",
            ),
        ];
        for (count, expected) in number_cases {
            let (files, values) = generated(document(
                serde_json::json!({"type": "string"}),
                count.clone(),
                false,
            ));
            assert_eq!(docstring_arguments(&files)[1], expected, "{count}");
            let count_values: Vec<_> = values
                .iter()
                .filter(|v| v.finding.argument == "count")
                .collect();
            assert!(!count_values.is_empty(), "{count}");
            assert!(
                count_values
                    .iter()
                    .all(|value| value.finding.mechanism == Some(Mechanism::Number)
                        && value.finding.disposition == Disposition::Repaired),
                "{count}: {values:?}"
            );
        }
    }

    #[test]
    fn the_same_document_generates_the_same_bytes_and_values_twice() {
        let input = document(
            serde_json::json!({"type": "string", "pattern": "^[A-Z]{3}-\\d{2}$", "maxLength": 6}),
            serde_json::json!({"type": "integer", "minimum": 7, "multipleOf": 3}),
            false,
        );
        let (first_files, first_values) = generated(input.clone());
        let (second_files, second_values) = generated(input);
        assert_eq!(first_files, second_files);
        assert_eq!(first_values, second_values);
        assert_eq!(
            docstring_arguments(&first_files),
            ["zone=\"AAA-00\",", "count=9,"]
        );
    }

    /// A document posting one body list `ids` under `items`, with
    /// `minItems: 2` and `uniqueItems: true`.
    fn unique_list_document(items: serde_json::Value) -> serde_json::Value {
        serde_json::json!({
            "openapi": "3.0.3",
            "info": {"title": "Api", "version": "1"},
            "paths": {"/batches": {"post": {
                "operationId": "createBatch",
                "requestBody": {"required": true, "content": {"application/json": {
                    "schema": {"type": "object", "required": ["ids"], "properties": {
                        "ids": {"type": "array", "minItems": 2, "uniqueItems": true,
                            "items": items}
                    }}
                }}},
                "responses": {"204": {"description": "Stored"}}
            }}}
        })
    }

    /// The `ids=` line of the generated client's docstring example.
    fn ids_line(files: &[(String, String)]) -> String {
        files
            .iter()
            .find(|(path, _)| path == "src/api/client.py")
            .and_then(|(_, client)| client.lines().find(|line| line.trim().starts_with("ids=")))
            .expect("an ids argument")
            .trim()
            .to_owned()
    }

    #[test]
    fn a_unique_list_is_padded_with_distinct_items_or_left_a_residual() {
        let (files, values) = generated(unique_list_document(
            serde_json::json!({"type": "string", "pattern": "^(0|[1-9][0-9]*)$"}),
        ));
        assert_eq!(ids_line(&files), "ids=[\"0\", \"1\"],");
        let lists: Vec<_> = values
            .iter()
            .filter(|value| value.finding.mechanism == Some(Mechanism::Array))
            .collect();
        assert!(!lists.is_empty());
        assert!(lists.iter().all(|value| value.finding.fern == "[\"ids\"]"
            && value.finding.disposition == Disposition::Repaired));
        // A uuid item has one constructed value, so no distinct second item:
        // the list keeps its one repaired item and is a residual.
        let (files, values) = generated(unique_list_document(
            serde_json::json!({"type": "string", "format": "uuid"}),
        ));
        assert_eq!(
            ids_line(&files),
            "ids=[\"d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32\"],"
        );
        let lists: Vec<_> = values
            .iter()
            .filter(|value| value.finding.mechanism == Some(Mechanism::Array))
            .collect();
        assert!(!lists.is_empty());
        assert!(lists.iter().all(|value| value.finding.disposition
            == Disposition::ResidualUnconstructible
            && value.finding.crozier == value.finding.fern));
    }

    /// The items of the generated `ids=[...]` example, read back as JSON.
    fn ids_items(files: &[(String, String)]) -> Vec<serde_json::Value> {
        let line = ids_line(files);
        let list = line
            .strip_prefix("ids=")
            .and_then(|rest| rest.strip_suffix(','))
            .expect("an ids list");
        serde_json::from_str(list).expect("a JSON-compatible list")
    }

    #[test]
    fn unique_list_padding_is_pairwise_distinct_and_each_item_accepted_or_a_residual() {
        use crate::example_values::{ValueConstraints, Verdict};
        let item_schemas = [
            serde_json::json!({"type": "string", "pattern": "^(0|[1-9][0-9]*)$"}),
            serde_json::json!({"type": "string", "minLength": 6}),
            serde_json::json!({"type": "integer", "minimum": 10, "maximum": 20}),
        ];
        for items in item_schemas {
            let (files, values) = generated(unique_list_document(items.clone()));
            let written = ids_items(&files);
            let item_schema: crate::openapi::Schema =
                serde_json::from_value(items.clone()).expect("an item schema");
            let constraints = ValueConstraints::of(&item_schema, &indexmap::IndexMap::new())
                .expect("in-scope item keywords");
            let lists: Vec<_> = values
                .iter()
                .filter(|value| value.finding.mechanism == Some(Mechanism::Array))
                .collect();
            assert!(!lists.is_empty(), "{items}");
            assert!(
                lists
                    .iter()
                    .all(|value| value.finding.disposition == Disposition::Repaired),
                "{items}: {lists:?}"
            );
            assert_eq!(written.len(), 2, "{items}: {written:?}");
            for item in &written {
                assert_eq!(
                    constraints.verdict(item),
                    Verdict::Accepted,
                    "{items}: {item}"
                );
            }
            for (at, item) in written.iter().enumerate() {
                assert!(!written[at + 1..].contains(item), "{items}: {written:?}");
            }
        }
        // Items with one admissible value, or a format crozier builds one
        // value for, cannot be distinct: Fern's list length stays, recorded
        // residual-unconstructible.
        for items in [
            serde_json::json!({"type": "string", "pattern": "^x$"}),
            serde_json::json!({"type": "string", "format": "uuid"}),
            serde_json::json!({"type": "string", "format": "email"}),
        ] {
            let (files, values) = generated(unique_list_document(items.clone()));
            assert_eq!(ids_items(&files).len(), 1, "{items}");
            let lists: Vec<_> = values
                .iter()
                .filter(|value| value.finding.mechanism == Some(Mechanism::Array))
                .collect();
            assert!(!lists.is_empty(), "{items}");
            assert!(
                lists.iter().all(|value| value.finding.disposition
                    == Disposition::ResidualUnconstructible
                    && value.finding.crozier == value.finding.fern),
                "{items}: {lists:?}"
            );
        }
    }

    #[test]
    fn a_value_crozier_cannot_satisfy_stays_fern_s_and_is_recorded_as_a_residual() {
        let (files, values) = generated(document(
            serde_json::json!({"type": "string", "minLength": 9, "maxLength": 3}),
            serde_json::json!({"type": "integer"}),
            false,
        ));
        assert_eq!(docstring_arguments(&files)[0], "zone=\"zone\",");
        assert!(!values.is_empty());
        assert!(values.iter().all(|value| value.finding.disposition
            == Disposition::ResidualUnconstructible
            && value.finding.crozier == value.finding.fern));
    }

    /// A document whose one operation posts a `Plan` body of `properties`, all
    /// required.
    fn body_document(properties: serde_json::Value) -> serde_json::Value {
        let required: Vec<String> = properties
            .as_object()
            .expect("properties")
            .keys()
            .cloned()
            .collect();
        serde_json::json!({
            "openapi": "3.1.0",
            "info": {"title": "Api", "version": "1"},
            "paths": {"/plans": {"post": {
                "operationId": "plan",
                "requestBody": {"required": true, "content": {"application/json": {
                    "schema": {"$ref": "#/components/schemas/Plan"}}}},
                "responses": {"204": {"description": "Done"}}
            }}},
            "components": {"schemas": {"Plan": {
                "type": "object", "required": required, "properties": properties
            }}}
        })
    }

    /// The keyword arguments `client.plan(...)` passes in the root client's
    /// first docstring, one trimmed line each.
    fn plan_arguments(files: &[(String, String)]) -> Vec<String> {
        let client = &files
            .iter()
            .find(|(path, _)| path == "src/api/client.py")
            .expect("a root client")
            .1;
        let start = client.find("client.plan(").expect("an example call");
        client[start..]
            .lines()
            .skip(1)
            .take_while(|line| line != &"        )")
            .map(|line| line.trim().to_string())
            .collect()
    }

    #[test]
    fn a_declared_value_its_schema_rejects_gives_way_to_fern_s_valid_construction_else_its_repair()
    {
        let (files, values) = generated(body_document(serde_json::json!({
            "share": {"type": "number", "maximum": 1, "example": 42},
            "ratio": {"type": "number", "maximum": 2, "example": 42},
            "code": {"type": "string", "pattern": "^[0-9a-f]{4}$", "example": "zz"},
            "kept": {"type": "number", "maximum": 50, "example": 42}
        })));
        assert_eq!(
            plan_arguments(&files),
            ["share=1.0,", "ratio=1.1,", "code=\"aaaa\",", "kept=42.0,"]
        );
        let found = |argument: &str| {
            values
                .iter()
                .find(|value| value.finding.argument == argument)
                .map(|value| {
                    (
                        value.finding.fern.clone(),
                        value.finding.mechanism,
                        value.finding.disposition,
                    )
                })
        };
        for argument in ["share", "ratio", "code"] {
            let (_, mechanism, disposition) = found(argument).expect("a recorded value");
            assert_eq!(
                (mechanism, disposition),
                (Some(Mechanism::Declared), Disposition::Repaired),
                "{argument}"
            );
        }
        assert_eq!(found("code").map(|f| f.0), Some("\"zz\"".to_string()));
        // A declared value its schema accepts is no finding at all.
        assert!(found("kept").is_none());
    }

    #[test]
    fn an_empty_list_takes_the_items_its_schema_s_shape_builds() {
        let (files, values) = generated(body_document(serde_json::json!({
            "bounds": {"type": "array", "items": false, "minItems": 2, "maxItems": 2,
                "prefixItems": [{"type": "number"}, {"type": "string", "enum": ["x", "y"]}]},
            "windows": {"type": "array", "items": {"type": "array", "minItems": 2,
                "maxItems": 2, "items": {"anyOf": [
                    {"type": "string", "format": "date-time"}, {"type": "null"}]}}},
            "loose": {"type": "array", "items": {"type": "array", "minItems": 1,
                "maxItems": 1, "prefixItems": [{}], "items": false}}
        })));
        assert_eq!(
            plan_arguments(&files),
            [
                "bounds=[1.1, \"x\"],",
                "windows=[[None, None]],",
                "loose=[[{\"key\": \"value\"}]],"
            ]
        );
        for argument in ["bounds", "windows[0]", "loose[0]"] {
            assert!(
                values.iter().any(|value| value.finding.argument == argument
                    && value.finding.fern == "[]"
                    && value.finding.mechanism == Some(Mechanism::Array)
                    && value.finding.disposition == Disposition::Repaired),
                "{argument}: {values:?}"
            );
        }
    }

    #[test]
    fn a_recursive_union_item_seeds_its_inline_member_not_itself() {
        let (files, _) = generated(body_document(serde_json::json!({
            "members": {"type": "array", "minItems": 1, "items": {"anyOf": [
                {"$ref": "#/components/schemas/Plan"},
                {"type": "object", "required": ["field"],
                    "properties": {"field": {"type": "string", "minLength": 1}}}
            ]}}
        })));
        let arguments = plan_arguments(&files).join("\n");
        assert!(
            arguments.contains("PlanMembersItemField(") && arguments.contains("field=\"string\","),
            "{arguments}"
        );
        assert!(
            !arguments.contains("members=[]"),
            "an empty list stays: {arguments}"
        );
    }

    #[test]
    fn a_schema_that_admits_no_value_keeps_fern_s_and_says_so() {
        // An integer whose `enum` lists only strings, and a string enum every
        // member of which the pattern, the length or the `not` rejects.
        let (files, values) = generated(body_document(serde_json::json!({
            "region": {"type": "integer", "format": "int32", "enum": ["101 (EastAsia)"]},
            "window": {"type": "string", "enum": ["slack", "flood", "ebb"],
                "maxLength": 4, "pattern": "^(?!slack$).*$", "not": {"enum": ["ebb"]}}
        })));
        assert_eq!(plan_arguments(&files)[0], "region=1,");
        for argument in ["region", "window"] {
            assert!(
                values.iter().any(|value| value.finding.argument == argument
                    && value.finding.disposition == Disposition::UnsatisfiableSchema
                    && value.finding.crozier == value.finding.fern),
                "{argument}: {values:?}"
            );
        }
        // One member the schema accepts is no contradiction: the enum's own
        // selection writes it.
        let mut document = body_document(serde_json::json!({
            "window": {"maxLength": 4, "allOf": [
                {"$ref": "#/components/schemas/Tide"},
                {"type": "string", "pattern": "^(?!slack$).*$"}
            ]}
        }));
        document["components"]["schemas"]["Tide"] =
            serde_json::json!({"type": "string", "enum": ["slack", "flood", "ebb"]});
        let (files, values) = generated(document);
        assert_eq!(plan_arguments(&files), ["window=PlanWindow.EBB,"]);
        assert!(values
            .iter()
            .all(|value| value.finding.disposition != Disposition::UnsatisfiableSchema));
    }
}
