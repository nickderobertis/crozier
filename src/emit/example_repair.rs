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
    mechanism, python_value, Choice, Disposition, ExampleValue, ValueConstraints, Verdict,
};
use crate::ir::{Endpoint, RequestBody, TypeDecl, TypeRef};

/// Fern's own construction for one value, or `None` where the value is not
/// one (a declared example, a value from the specification).
fn construction(
    value: &Value,
    names: &[String],
    lengths: &[(Option<u64>, Option<u64>)],
) -> Option<&'static str> {
    match value {
        Value::String(text) => {
            if names.iter().any(|name| name == text) {
                Some(mechanism::NAME)
            } else if text == "string" || text == "value" {
                Some(mechanism::PLACEHOLDER)
            } else if lengths.iter().any(|(min, max)| {
                crate::ir::fallback_string_sample(*min, *max).as_deref() == Some(text.as_str())
            }) {
                Some(mechanism::SIZED)
            } else {
                None
            }
        }
        Value::Number(number) => {
            let fixed = [1.0, 1_000_000.0, 1.1];
            number
                .as_f64()
                .is_some_and(|n| fixed.contains(&n))
                .then_some(mechanism::NUMBER)
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
    value: ExampleValue,
}

/// One example block a writer produced, with its rejected values.
struct Block {
    /// `None` for a docstring; `Some(true)` for `reference.md`, `Some(false)`
    /// for `README.md`.
    markdown: Option<bool>,
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
pub(super) fn record(documentation: bool, reference: bool, lines: &[String], values: Vec<Pending>) {
    if values.is_empty() {
        return;
    }
    BLOCKS.with(|blocks| {
        if let Some(blocks) = blocks.borrow_mut().as_mut() {
            blocks.push(Block {
                markdown: documentation.then_some(reference),
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
    let mut out = std::collections::BTreeSet::new();
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
            let belongs = match block.markdown {
                Some(true) => path == "reference.md",
                Some(false) => path == "README.md",
                None => path.ends_with(".py"),
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
                    // opening line.
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
                                    !own.is_empty()
                                        && line.ends_with('[')
                                        && holds_at_boundary(line, &opening)
                                })
                            })?
                        })
                        .map(|found| from + found)
                    else {
                        continue;
                    };
                    cursor.insert(needle, offset + 1);
                    out.insert(ExampleValue {
                        file: path.clone(),
                        line: start + offset + 1,
                        ..pending.value.clone()
                    });
                }
            }
        }
    }
    out.into_iter().collect()
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
    }
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
                                value: ExampleValue {
                                    file: String::new(),
                                    line: 0,
                                    argument: path.to_string(),
                                    fern: rounded,
                                    crozier: literal.clone(),
                                    constraint: keyword.to_string(),
                                    mechanism: Some(mechanism::ROUNDED),
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
                            value: ExampleValue {
                                file: String::new(),
                                line: 0,
                                argument: path.to_string(),
                                fern: literal.clone(),
                                crozier: literal.clone(),
                                constraint: keyword.to_string(),
                                mechanism: construction(&value, names, &lengths),
                                disposition: Disposition::ResidualUndecidable,
                            },
                        });
                        return;
                    }
                    Verdict::Rejected(keyword) => keyword.to_string(),
                };
                let fern = literal.clone();
                let mechanism = construction(&value, names, &lengths);
                let declared = combined.examples.contains(&value) || mechanism.is_none();
                let (crozier, disposition) = if declared {
                    (fern.clone(), Disposition::DeclaredInSpec)
                } else {
                    match combined.choose(&value) {
                        Some(choice) => match self.rendered(&resolved, &choice) {
                            Some(rendered) => (rendered, Disposition::Repaired),
                            None => (fern.clone(), Disposition::ResidualUnconstructible),
                        },
                        None if combined.incomplete => {
                            (fern.clone(), Disposition::ResidualUndecidable)
                        }
                        None => (fern.clone(), Disposition::ResidualUnconstructible),
                    }
                };
                if disposition == Disposition::Repaired {
                    literal.clone_from(&crozier);
                }
                pending.push(Pending {
                    needles: needles.to_vec(),
                    value: ExampleValue {
                        file: String::new(),
                        line: 0,
                        argument: path.to_string(),
                        fern,
                        crozier,
                        constraint,
                        mechanism: if declared { None } else { mechanism },
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
                let declared = matches!(example, Example::ExplicitList(_));
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
                self.repair_length(example, &lists, fern, declared, path, needles, pending);
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
        declared: bool,
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
        let choice = (!declared && !items.is_empty())
            .then(|| merged(sets).choose(&shape))
            .flatten();
        let disposition = if declared {
            Disposition::DeclaredInSpec
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
            value: ExampleValue {
                file: String::new(),
                line: 0,
                argument: path.to_string(),
                crozier: if disposition == Disposition::Repaired {
                    example.flat()
                } else {
                    fern.clone()
                },
                fern,
                constraint: keyword.to_string(),
                mechanism: (!declared).then_some(mechanism::ARRAY),
                disposition,
            },
        });
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
    /// still writes is a residual, undecidable where some member satisfies the
    /// schema but the enum's own selection could not decide it, unconstructible
    /// where none does.
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
        let disposition = if written.value != first.value {
            Disposition::Repaired
        } else if declaration
            .members
            .iter()
            .any(|member| combined.verdict(&wire(member)) == Verdict::Accepted)
            || combined.incomplete
        {
            Disposition::ResidualUndecidable
        } else {
            Disposition::ResidualUnconstructible
        };
        pending.push(Pending {
            needles: needles.to_vec(),
            value: ExampleValue {
                file: String::new(),
                line: 0,
                argument: path.to_string(),
                fern: spell(first),
                crozier: literal.to_string(),
                constraint: keyword.to_string(),
                mechanism: Some(mechanism::ENUM_MEMBER),
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
    use crate::example_values::{mechanism, Disposition, ExampleValue};

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
        let zone: Vec<&ExampleValue> = values.iter().filter(|v| v.argument == "zone").collect();
        assert!(!zone.is_empty());
        for value in zone {
            assert_eq!(
                (
                    value.fern.as_str(),
                    value.crozier.as_str(),
                    value.constraint.as_str()
                ),
                ("\"zone\"", "\"eu-1\"", "pattern=^[a-z]{2}-[0-9]$")
            );
            assert_eq!(value.mechanism, Some(mechanism::NAME));
            assert_eq!(value.disposition, Disposition::Repaired);
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
                    && values.iter().all(|value| value.fern == "\"zone\""
                        && value.mechanism == Some(mechanism::NAME)
                        && value.disposition == Disposition::Repaired),
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
            let count_values: Vec<_> = values.iter().filter(|v| v.argument == "count").collect();
            assert!(!count_values.is_empty(), "{count}");
            assert!(
                count_values
                    .iter()
                    .all(|value| value.mechanism == Some(mechanism::NUMBER)
                        && value.disposition == Disposition::Repaired),
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

    #[test]
    fn a_value_crozier_cannot_satisfy_stays_fern_s_and_is_recorded_as_a_residual() {
        let (files, values) = generated(document(
            serde_json::json!({"type": "string", "minLength": 9, "maxLength": 3}),
            serde_json::json!({"type": "integer"}),
            false,
        ));
        assert_eq!(docstring_arguments(&files)[0], "zone=\"zone\",");
        assert!(!values.is_empty());
        assert!(values.iter().all(|value| value.disposition
            == Disposition::ResidualUnconstructible
            && value.crozier == value.fern));
    }
}
