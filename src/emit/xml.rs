//! XML models: an object schema carrying an OpenAPI `xml` object reads and
//! writes itself as an XML element as well as JSON. The model keeps its pydantic
//! fields and gains `to_xml`/`from_xml`, the ordered-content bookkeeping behind
//! them, and fluent builders for its child elements, all over the vendored
//! `core/xml_utilities.py`; the SDK also gets a round-trip test module per model
//! under `tests/xml/`. The shapes follow fern-python-sdk 5.41's XML support
//! (Apache-2.0) member for member, so the methods below are written in the order
//! and with the exact argument layout Fern writes them — `ruff format` then
//! settles the line breaks the same way for both.

use std::collections::BTreeSet;
use std::path::PathBuf;

use super::{module_path, render_type, GeneratedFile, Imports, HEADER};
use crate::ir::{Field, ObjectType, Prim, TagTypeDecl, TypeDecl, TypeRef, XmlEncoding, XmlKind};
use crate::naming;

/// Fern's `core/xml_utilities.py`, shipped only with an SDK that has an XML model.
pub(super) const XML_UTILITIES: &str = include_str!("../../assets/core/xml_utilities.py");

/// Every declaration of the SDK (root and tag-scoped), the lookup an XML model
/// needs to tell which of its child element types are XML models themselves.
#[derive(Debug, Clone, Copy, Default)]
pub(super) struct XmlTypes<'a> {
    types: &'a [TypeDecl],
    tag_types: &'a [TagTypeDecl],
}

impl<'a> XmlTypes<'a> {
    pub(super) fn new(types: &'a [TypeDecl], tag_types: &'a [TagTypeDecl]) -> Self {
        XmlTypes { types, tag_types }
    }

    /// Every declaration with the tag directory a tag-scoped one lives in
    /// (`None` for a package-root type).
    fn all(&self) -> impl Iterator<Item = (&'a TypeDecl, Option<&'a str>)> {
        self.types.iter().map(|decl| (decl, None)).chain(
            self.tag_types
                .iter()
                .map(|tagged| (&tagged.decl, Some(tagged.module.as_str()))),
        )
    }

    fn find(&self, name: &str) -> Option<&'a TypeDecl> {
        self.all()
            .map(|(decl, _)| decl)
            .find(|decl| decl.name() == name)
    }

    fn object(&self, name: &str) -> Option<&'a ObjectType> {
        match self.find(name) {
            Some(TypeDecl::Object(obj)) => Some(obj),
            _ => None,
        }
    }

    /// Whether any model is an XML model — the condition for shipping
    /// `core/xml_utilities.py` and the `tests/xml/` modules.
    pub(super) fn any(&self) -> bool {
        self.all()
            .any(|(decl, _)| matches!(decl, TypeDecl::Object(obj) if obj.xml.is_some()))
    }

    /// The XML models a child element of type `t` can be: an XML model it names
    /// directly or inside a container, or a member of a union it names. Fern's
    /// order, duplicates kept.
    fn xml_object_names(&self, t: &TypeRef, depth: usize) -> Vec<String> {
        if depth > 32 {
            return Vec::new();
        }
        match t {
            TypeRef::Optional(inner) | TypeRef::List(inner) | TypeRef::Set(inner) => {
                self.xml_object_names(inner, depth + 1)
            }
            TypeRef::Dict(key, value) => {
                let mut names = self.xml_object_names(key, depth + 1);
                names.extend(self.xml_object_names(value, depth + 1));
                names
            }
            TypeRef::Union(members) => members
                .iter()
                .flat_map(|member| self.xml_object_names(member, depth + 1))
                .collect(),
            TypeRef::Named(name) => match self.find(name) {
                Some(TypeDecl::Object(obj)) if obj.xml.is_some() => vec![name.clone()],
                Some(TypeDecl::Alias(alias)) if matches!(alias.target, TypeRef::Union(_)) => {
                    self.xml_object_names(&alias.target, depth + 1)
                }
                _ => Vec::new(),
            },
            TypeRef::Primitive(_) | TypeRef::Literal(_) => Vec::new(),
        }
    }

    /// Every property of `obj`, its own first and then each base's, depth first
    /// — Fern's "all properties including extensions".
    fn all_fields(&self, obj: &ObjectType, depth: usize) -> Vec<Field> {
        let mut fields = obj.fields.clone();
        if depth < 32 {
            for base in &obj.bases {
                if let Some(parent) = self.object(base) {
                    fields.extend(self.all_fields(parent, depth + 1));
                }
            }
        }
        fields
    }

    /// The properties an object inherits, each base's own before its parents' —
    /// Fern's `extendedProperties`.
    fn extended_fields(&self, obj: &ObjectType) -> Vec<Field> {
        obj.bases
            .iter()
            .filter_map(|base| self.object(base))
            .flat_map(|parent| self.all_fields(parent, 1))
            .collect()
    }

    /// The wire values of the enum `t` names, if it names one.
    fn enum_values(&self, t: &TypeRef) -> Option<Vec<String>> {
        match t {
            TypeRef::Named(name) => match self.find(name) {
                Some(TypeDecl::Enum(e)) => {
                    Some(e.members.iter().map(|m| m.value.clone()).collect())
                }
                _ => None,
            },
            _ => None,
        }
    }
}

/// What an XML model adds to its class body.
#[derive(Debug, Default)]
pub(super) struct XmlMembers {
    /// The methods, rendered at class-body indentation, each followed by a blank
    /// line.
    pub(super) methods: Option<String>,
    /// Pydantic v1 must not copy nested models on validation, or a model's typed
    /// children and its ordered content stop being the same objects.
    pub(super) preserve_child_identity: bool,
}

const CONTENT: &str = "_content";
const COMMENTS_BEFORE: &str = "_comments_before";
const COMMENTS_AFTER: &str = "_comments_after";
const EXTRA_ATTRIBUTES: &str = "extra_attributes";

/// The method names a child builder must not take: the XML model's own API and
/// pydantic's `BaseModel` attributes.
const RESERVED_METHOD_NAMES: &[&str] = &[
    "to_xml",
    "from_xml",
    "append",
    "add_child",
    "add_text",
    "comment",
    "comment_before",
    "comment_after",
    "construct",
    "copy",
    "dict",
    "from_orm",
    "json",
    "model_computed_fields",
    "model_config",
    "model_construct",
    "model_copy",
    "model_dump",
    "model_dump_json",
    "model_extra",
    "model_fields",
    "model_fields_set",
    "model_json_schema",
    "model_parametrized_name",
    "model_post_init",
    "model_rebuild",
    "model_validate",
    "model_validate_json",
    "model_validate_strings",
    "parse_file",
    "parse_obj",
    "parse_raw",
    "schema",
    "schema_json",
    "update_forward_refs",
    "validate",
];

/// One XML model being rendered: its own fields, every field it serializes
/// (inherited ones included), and the names fixed up front for its builders and
/// its text attribute.
pub(super) struct XmlModel<'a> {
    obj: &'a ObjectType,
    xml: &'a XmlEncoding,
    types: XmlTypes<'a>,
    /// Own fields, then inherited ones.
    all: Vec<Field>,
    /// The attribute the text field is stored under when its own name is taken
    /// by a builder; `None` otherwise.
    text_attribute: Option<String>,
    /// Builder method names per list field (by field name): `(child class, name)`.
    builder_names: Vec<(String, Vec<(String, String)>)>,
}

fn kind(field: &Field) -> XmlKind {
    field
        .xml
        .as_ref()
        .map_or(XmlKind::Element { wrapped: false }, |xml| xml.kind)
}

fn is_attribute(field: &Field) -> bool {
    kind(field) == XmlKind::Attribute
}

fn is_text(field: &Field) -> bool {
    kind(field) == XmlKind::Text
}

fn is_element(field: &Field) -> bool {
    matches!(kind(field), XmlKind::Element { .. })
}

fn is_wrapped(field: &Field) -> bool {
    kind(field) == XmlKind::Element { wrapped: true }
}

fn separator(field: &Field) -> Option<&str> {
    field
        .xml
        .as_ref()
        .and_then(|xml| xml.list_separator.as_deref())
}

fn xml_name(field: &Field) -> &str {
    field
        .xml
        .as_ref()
        .and_then(|xml| xml.name.as_deref())
        .unwrap_or(&field.wire_name)
}

/// Whether the field's value may be absent (`Optional`/nullable).
fn is_optional(field: &Field) -> bool {
    field.optional || matches!(field.type_ref, TypeRef::Optional(_))
}

/// The item type of a (possibly optional) list field.
fn list_item(field: &Field) -> Option<&TypeRef> {
    let mut t = &field.type_ref;
    while let TypeRef::Optional(inner) = t {
        t = inner;
    }
    match t {
        TypeRef::List(item) => Some(item),
        _ => None,
    }
}

/// The type a child element of the field holds: the list item, or the value.
fn child_type(field: &Field) -> &TypeRef {
    list_item(field).unwrap_or(&field.type_ref)
}

/// Fern's initializer for a field's parameter: a required literal's value.
fn initializer(field: &Field) -> Option<String> {
    if is_optional(field) {
        return None;
    }
    match &field.type_ref {
        TypeRef::Literal(values) if values.len() == 1 => Some(py_double_quoted(&values[0])),
        TypeRef::Primitive(Prim::LiteralBool(value)) => {
            Some(if *value { "True" } else { "False" }.to_string())
        }
        _ => None,
    }
}

/// Python's `repr()` of a string, the literal Fern writes for every name: the
/// escapes Python gives a backslash, a quote and each character it does not
/// print as itself — controls, format characters, private-use characters, and
/// line, paragraph and space separators other than the space. An unassigned code
/// point, which Python also escapes, is written as itself: telling one apart
/// needs Unicode's tables, which crozier does not carry.
pub(super) fn py_repr(value: &str) -> String {
    let quote = if value.contains('\'') && !value.contains('"') {
        '"'
    } else {
        '\''
    };
    let mut out = String::with_capacity(value.len() + 2);
    out.push(quote);
    for c in value.chars() {
        match c {
            '\\' => out.push_str("\\\\"),
            '\n' => out.push_str("\\n"),
            '\r' => out.push_str("\\r"),
            '\t' => out.push_str("\\t"),
            c if c == quote => {
                out.push('\\');
                out.push(c);
            }
            c if c.is_control() || py_unprintable(c) => {
                let code = u32::from(c);
                if code <= 0xff {
                    out.push_str(&format!("\\x{code:02x}"));
                } else if code <= 0xffff {
                    out.push_str(&format!("\\u{code:04x}"));
                } else {
                    out.push_str(&format!("\\U{code:08x}"));
                }
            }
            c => out.push(c),
        }
    }
    out.push(quote);
    out
}

/// Whether Python's `str.isprintable()` is false for `c` by its general
/// category: a space separator other than the space (Zs), a line or paragraph
/// separator (Zl, Zp), a format character (Cf) or a private-use one (Co).
fn py_unprintable(c: char) -> bool {
    matches!(
        u32::from(c),
        // Zs, less U+0020, and Zl, Zp.
        0xa0 | 0x1680 | 0x2000..=0x200a | 0x2028 | 0x2029 | 0x202f | 0x205f | 0x3000
        // Cf.
        | 0xad | 0x600..=0x605 | 0x61c | 0x6dd | 0x70f | 0x890..=0x891 | 0x8e2 | 0x180e
        | 0x200b..=0x200f | 0x202a..=0x202e | 0x2060..=0x2064 | 0x2066..=0x206f | 0xfeff
        | 0xfff9..=0xfffb | 0x110bd | 0x110cd | 0x13430..=0x1343f | 0x1bca0..=0x1bca3
        | 0x1d173..=0x1d17a | 0xe0001 | 0xe0020..=0xe007f
        // Co.
        | 0xe000..=0xf8ff | 0xf0000..=0xffffd | 0x100000..=0x10fffd
    )
}

/// A double-quoted Python string literal of `value`, the spelling Fern gives a
/// literal's initializer, with its quotes, backslashes and controls escaped.
fn py_double_quoted(value: &str) -> String {
    let mut out = String::with_capacity(value.len() + 2);
    out.push('"');
    for c in value.chars() {
        match c {
            '\\' => out.push_str("\\\\"),
            '"' => out.push_str("\\\""),
            '\n' => out.push_str("\\n"),
            '\r' => out.push_str("\\r"),
            '\t' => out.push_str("\\t"),
            c if c.is_control() => out.push_str(&format!("\\u{:04x}", u32::from(c))),
            c => out.push(c),
        }
    }
    out.push('"');
    out
}

/// A `{'a', 'b'}` set literal of unique names, or `()` for none.
fn set_literal(names: &[String]) -> String {
    let mut seen = BTreeSet::new();
    let unique: Vec<String> = names
        .iter()
        .filter(|name| seen.insert(name.as_str()))
        .map(|name| py_repr(name))
        .collect();
    if unique.is_empty() {
        "()".to_string()
    } else {
        format!("{{{}}}", unique.join(", "))
    }
}

/// Fern's `escape_docstring`.
fn escape_docstring(text: &str) -> String {
    text.replace('\\', "\\\\").replace("\"\"\"", "\\\"\"\"")
}

/// The snake_case method name a tag or class name gives a builder.
fn snake_name(name: &str) -> String {
    naming::field_name(name)
}

/// A Python source writer with Fern's writer semantics: text written at the
/// start of a line takes the current indent (even empty text, which leaves a
/// whitespace-only line `ruff format` clears), and opening an indented block
/// mid-line breaks the line first.
struct Writer {
    out: String,
    indent: usize,
}

impl Writer {
    fn new(indent: usize) -> Self {
        Writer {
            out: String::new(),
            indent,
        }
    }

    fn pad(&self) -> String {
        " ".repeat(4 * self.indent)
    }

    fn at_line_start(&self) -> bool {
        self.out.is_empty() || self.out.ends_with('\n')
    }

    fn write(&mut self, content: &str) {
        let pad = self.pad();
        let (body, newline) = match content.strip_suffix('\n') {
            Some(body) => (body, true),
            None => (content, false),
        };
        let mut text = body.replace('\n', &format!("\n{pad}"));
        if self.at_line_start() {
            text.insert_str(0, &pad);
        }
        if newline {
            text.push('\n');
        }
        self.out.push_str(&text);
    }

    fn line(&mut self, content: &str) {
        self.write(content);
        self.newline_if_needed();
    }

    fn newline_if_needed(&mut self) {
        if !self.out.ends_with('\n') {
            self.write("\n");
        }
    }

    fn indent(&mut self) {
        self.indent += 1;
        if self.out.ends_with('\n') {
            let pad = self.pad();
            self.out.push_str(&pad);
        } else {
            self.write("\n");
        }
    }

    fn outdent(&mut self) {
        self.indent = self.indent.saturating_sub(1);
    }
}

/// One parameter of a generated method.
#[derive(Clone)]
struct Param {
    name: String,
    hint: String,
    initializer: Option<String>,
    docs: Option<String>,
}

impl Param {
    fn render(&self) -> String {
        match &self.initializer {
            Some(init) => format!("{}: {} = {init}", self.name, self.hint),
            None => format!("{}: {}", self.name, self.hint),
        }
    }
}

/// A method's signature: positional parameters after `self`/`cls`, keyword-only
/// ones after `*`, and Fern's `**extra_attributes: str` catch-all when asked.
struct Signature {
    receiver: &'static str,
    positional: Vec<Param>,
    named: Vec<Param>,
    kwargs: bool,
    returns: String,
}

impl Signature {
    fn render(&self) -> String {
        let mut parts = vec![self.receiver.to_string()];
        let mut seen: BTreeSet<&str> = BTreeSet::new();
        for param in &self.positional {
            if seen.insert(&param.name) {
                parts.push(param.render());
            }
        }
        if !self.named.is_empty() {
            parts.push("*".to_string());
        }
        for param in &self.named {
            if seen.insert(&param.name) {
                parts.push(param.render());
            }
        }
        if self.kwargs {
            parts.push(format!("**{EXTRA_ATTRIBUTES}: str"));
        }
        format!("({}) -> {}:", parts.join(", "), self.returns)
    }
}

/// Write one method at the writer's (class-body) indentation, as Fern's function
/// declaration writes it, then a blank line.
fn write_method(
    w: &mut Writer,
    decorator: Option<&str>,
    name: &str,
    signature: &Signature,
    docstring: Option<&dyn Fn(&mut Writer)>,
    body: &dyn Fn(&mut Writer),
) {
    if let Some(decorator) = decorator {
        w.line(&format!("@{decorator}"));
    }
    w.write(&format!("def {name}{}", signature.render()));
    w.indent();
    if let Some(docstring) = docstring {
        w.line("\"\"\"");
        docstring(w);
        w.newline_if_needed();
        w.line("\"\"\"");
    }
    body(w);
    w.outdent();
    w.newline_if_needed();
    w.out.push('\n');
}

/// Fern's numpydoc docstring for a builder or constructor: an optional summary,
/// then a `Parameters` section closing with the extra attributes.
fn write_parameter_docstring(w: &mut Writer, summary: Option<&str>, params: &[&Param]) {
    if let Some(summary) = summary {
        w.line(&escape_docstring(summary));
    }
    if params.is_empty() {
        return;
    }
    if summary.is_some() {
        w.line("");
    }
    w.line("Parameters");
    w.line("----------");
    for (index, param) in params.iter().enumerate() {
        if index > 0 {
            w.line("");
            w.line("");
        }
        w.write(&format!("{} : {}", param.name, param.hint));
        if let Some(docs) = &param.docs {
            let lines: Vec<&str> = docs.split('\n').collect();
            w.indent();
            for (j, line) in lines.iter().enumerate() {
                w.write(&escape_docstring(line));
                if j + 1 < lines.len() {
                    w.line("");
                }
            }
            w.outdent();
        }
    }
    w.line("");
    w.line("");
    w.write(&format!("**{EXTRA_ATTRIBUTES} : str"));
    w.indent();
    w.write("Additional XML attributes not declared in the API definition.");
    w.outdent();
    w.line("");
}

impl<'a> XmlModel<'a> {
    pub(super) fn new(obj: &'a ObjectType, xml: &'a XmlEncoding, types: XmlTypes<'a>) -> Self {
        let mut all = obj.fields.clone();
        for base in &obj.bases {
            if let Some(parent) = types.object(base) {
                all.extend(types.all_fields(parent, 1));
            }
        }
        let mut model = XmlModel {
            obj,
            xml,
            types,
            all,
            text_attribute: None,
            builder_names: Vec::new(),
        };
        model.compute_naming();
        model
    }

    /// Fix the builder names and the text field's attribute together: a builder
    /// named after the child tag wins over a text field of the same name, which
    /// then moves to a trailing-underscore attribute (an inherited text field
    /// cannot move, so the builder yields instead).
    fn compute_naming(&mut self) {
        let text = self.all.iter().position(is_text);
        let renamable = text.is_some_and(|index| index < self.obj.fields.len());
        let mut taken: BTreeSet<String> = self
            .all
            .iter()
            .enumerate()
            .filter(|(index, _)| !(renamable && Some(*index) == text))
            .map(|(_, field)| field.py_name.clone())
            .collect();
        taken.extend(RESERVED_METHOD_NAMES.iter().map(|name| (*name).to_string()));
        let mut builder_names = Vec::new();
        for field in &self.all {
            if !is_element(field) {
                continue;
            }
            let Some(item) = list_item(field) else {
                continue;
            };
            let names = self.builder_method_names(item, &taken);
            taken.extend(names.iter().map(|(_, name)| name.clone()));
            builder_names.push((field.py_name.clone(), names));
        }
        self.builder_names = builder_names;
        if let (true, Some(index)) = (renamable, text) {
            let name = &self.all[index].py_name;
            if taken.contains(name) {
                let mut attribute = format!("{name}_");
                while taken.contains(&attribute) {
                    attribute.push('_');
                }
                self.text_attribute = Some(attribute);
            }
        }
    }

    /// Each XML model a list field's item can be, mapped to a unique method name
    /// derived from its tag; a tag two children share falls back to the class
    /// name, and a taken name gains an `add_` prefix.
    fn builder_method_names(
        &self,
        item: &TypeRef,
        reserved: &BTreeSet<String>,
    ) -> Vec<(String, String)> {
        let mut candidates: Vec<(String, String)> = Vec::new();
        for class in self.types.xml_object_names(item, 0) {
            if candidates.iter().any(|(known, _)| *known == class) {
                continue;
            }
            let tag = self
                .types
                .object(&class)
                .and_then(|obj| obj.xml.as_ref())
                .map_or_else(|| class.clone(), |xml| xml.name.clone());
            candidates.push((class, snake_name(&tag)));
        }
        let mut taken = reserved.clone();
        let mut result = Vec::new();
        for (class, name) in &candidates {
            let shared = candidates.iter().filter(|(_, other)| other == name).count() > 1;
            let mut name = if shared {
                snake_name(class)
            } else {
                name.clone()
            };
            while taken.contains(&name) {
                name = format!("add_{name}");
            }
            taken.insert(name.clone());
            result.push((class.clone(), name));
        }
        result
    }

    /// The attribute a field's value is stored under.
    fn attribute_name(&self, field: &Field) -> String {
        match &self.text_attribute {
            Some(attribute) if is_text(field) => attribute.clone(),
            _ => field.py_name.clone(),
        }
    }

    /// The model's own fields as its class declares them: the text field under
    /// its moved attribute name when a builder took its own.
    pub(super) fn declared_fields(&self) -> Vec<Field> {
        let mut fields = self.obj.fields.clone();
        if let Some(attribute) = &self.text_attribute {
            if let Some(field) = fields.iter_mut().find(|field| is_text(field)) {
                field.py_name.clone_from(attribute);
            }
        }
        fields
    }

    /// Child element fields holding XML models that render inline (not inside a
    /// wrapper), so they live in the ordered content.
    fn inline_fields(&self) -> Vec<&Field> {
        self.all
            .iter()
            .filter(|field| {
                is_element(field)
                    && !is_wrapped(field)
                    && !self.types.xml_object_names(child_type(field), 0).is_empty()
            })
            .collect()
    }

    /// Each XML model reachable from `t`, keyed by its tag (a later class
    /// replaces an earlier one under the same tag, which keeps its position).
    fn child_type_map(&self, t: &TypeRef, imports: &mut Imports) -> Vec<(String, String)> {
        let mut map: Vec<(String, String)> = Vec::new();
        for class in self.types.xml_object_names(t, 0) {
            let Some(tag) = self
                .types
                .object(&class)
                .and_then(|obj| obj.xml.as_ref())
                .map(|xml| xml.name.clone())
            else {
                continue;
            };
            let local = self.class_reference(&class, imports);
            match map.iter_mut().find(|(known, _)| *known == tag) {
                Some(entry) => entry.1 = local,
                None => map.push((tag, local)),
            }
        }
        map
    }

    /// The name a generated class is written as inside a method body, importing
    /// it unless it is this model itself.
    fn class_reference(&self, class: &str, imports: &mut Imports) -> String {
        if class == self.obj.name {
            class.to_string()
        } else {
            imports.add_type(class)
        }
    }

    fn type_hint(field: &Field, imports: &mut Imports) -> String {
        let hint = render_type(&field.type_ref, imports).flat();
        if field.optional && !matches!(field.type_ref, TypeRef::Optional(_)) {
            imports.add_plain("typing");
            format!("typing.Optional[{hint}]")
        } else {
            hint
        }
    }

    fn param(field: &Field, imports: &mut Imports) -> Param {
        let hint = Self::type_hint(field, imports);
        let initializer = initializer(field).or_else(|| {
            hint.starts_with("typing.Optional[")
                .then(|| "None".to_string())
        });
        Param {
            name: field.py_name.clone(),
            hint,
            initializer,
            docs: field.docstring.clone(),
        }
    }

    /// `fields` with every literal-defaulted one moved last (stably).
    fn literal_defaulted_last(fields: Vec<&Field>) -> Vec<&Field> {
        let (plain, defaulted): (Vec<&Field>, Vec<&Field>) = fields
            .into_iter()
            .partition(|field| initializer(field).is_none());
        plain.into_iter().chain(defaulted).collect()
    }

    /// Everything the XML model adds to its class: the private content fields
    /// (appended to `fields`) and the methods.
    pub(super) fn members(
        &self,
        imports: &mut Imports,
        fields: &mut Vec<super::FieldView>,
    ) -> XmlMembers {
        imports.add_plain("typing");
        imports.add_plain("pydantic");
        let xml_util =
            |imports: &mut Imports, name: &str| imports.add_core_local("xml_utilities", name);
        let content_type = xml_util(imports, "XmlContent");
        let comment_type = xml_util(imports, "XmlComment");
        for (name, item) in [
            (CONTENT, &content_type),
            (COMMENTS_BEFORE, &comment_type),
            (COMMENTS_AFTER, &comment_type),
        ] {
            fields.push(super::FieldView {
                decl: format!(
                    "{name}: typing.List[{item}] = pydantic.PrivateAttr(default_factory=list)"
                ),
                docstring: None,
            });
        }
        let mut w = Writer::new(1);
        self.write_to_xml(&mut w, imports);
        self.write_str(&mut w);
        self.write_init(&mut w, imports);
        self.write_list_coercion(&mut w, imports);
        self.write_from_xml(&mut w, imports);
        self.write_content_methods(&mut w, imports);
        self.write_builders(&mut w, imports);
        let mut methods = w.out;
        while methods.ends_with("\n\n") {
            methods.pop();
        }
        XmlMembers {
            methods: Some(methods),
            preserve_child_identity: true,
        }
    }

    fn returns_self(&self) -> String {
        self.obj.name.clone()
    }

    fn write_to_xml(&self, w: &mut Writer, imports: &mut Imports) {
        let inline = self.inline_fields();
        let is_inline = |field: &Field| inline.iter().any(|known| std::ptr::eq(*known, field));
        let serialize = imports.add_core_local("xml_utilities", "serialize_xml_element");
        let attribute_class = if self.all.iter().any(is_attribute) {
            imports.add_core_local("xml_utilities", "XmlAttribute")
        } else {
            String::new()
        };
        let extra = imports.add_core_local("xml_utilities", "extra_xml_attributes");
        let child_class = if self
            .all
            .iter()
            .any(|field| is_element(field) && !is_inline(field))
        {
            imports.add_core_local("xml_utilities", "XmlChild")
        } else {
            String::new()
        };
        let order = imports.add_core_local("xml_utilities", "order_xml_content");
        let body = |w: &mut Writer| {
            w.line(&format!("return {serialize}("));
            w.indent();
            w.line(&format!("name={},", py_repr(&self.xml.name)));
            if let Some(namespace) = &self.xml.namespace {
                w.line(&format!("namespace={},", py_repr(namespace)));
            }
            if let Some(prefix) = &self.xml.prefix {
                w.line(&format!("prefix={},", py_repr(prefix)));
            }
            w.line("attributes=[");
            w.indent();
            for field in self.all.iter().filter(|field| is_attribute(field)) {
                let mut entry = format!(
                    "{attribute_class}(name={}, value=self.{}",
                    py_repr(xml_name(field)),
                    self.attribute_name(field)
                );
                if let Some(separator) = separator(field) {
                    entry.push_str(&format!(", separator={}", py_repr(separator)));
                }
                entry.push_str("),");
                w.line(&entry);
            }
            w.line(&format!("*{extra}(self),"));
            w.outdent();
            w.line("],");
            if let Some(field) = self.all.iter().find(|field| is_text(field)) {
                w.line(&format!("text=self.{},", self.attribute_name(field)));
                if let Some(separator) = separator(field) {
                    w.line(&format!("text_separator={},", py_repr(separator)));
                }
            }
            w.line("children=[");
            w.indent();
            for field in &self.all {
                if !is_element(field) || is_inline(field) {
                    continue;
                }
                let wrapped = if is_wrapped(field) {
                    ", wrapped=True"
                } else {
                    ""
                };
                w.line(&format!(
                    "{child_class}(name={}, value=self.{}{wrapped}),",
                    py_repr(xml_name(field)),
                    self.attribute_name(field)
                ));
            }
            w.outdent();
            w.line("],");
            let mut content = format!("content={order}(self.{CONTENT}");
            for field in &inline {
                content.push_str(&format!(", self.{}", self.attribute_name(field)));
            }
            content.push_str("),");
            w.line(&content);
            w.line(&format!("comments_before=self.{COMMENTS_BEFORE},"));
            w.line(&format!("comments_after=self.{COMMENTS_AFTER},"));
            w.line("xml_declaration=xml_declaration,");
            w.outdent();
            w.line(")");
        };
        let name = self.xml.name.clone();
        write_method(
            w,
            None,
            "to_xml",
            &Signature {
                receiver: "self",
                positional: Vec::new(),
                named: vec![Param {
                    name: "xml_declaration".to_string(),
                    hint: "bool".to_string(),
                    initializer: Some("True".to_string()),
                    docs: None,
                }],
                kwargs: false,
                returns: "str".to_string(),
            },
            Some(&|w: &mut Writer| {
                w.write(&format!(
                    "Serializes this object as a `<{}>` XML element, prefixed with the XML declaration unless `xml_declaration` is False.",
                    escape_docstring(&name)
                ));
            }),
            &body,
        );
    }

    fn write_str(&self, w: &mut Writer) {
        write_method(
            w,
            None,
            "__str__",
            &Signature {
                receiver: "self",
                positional: Vec::new(),
                named: Vec::new(),
                kwargs: false,
                returns: "str".to_string(),
            },
            None,
            &|w: &mut Writer| w.write("return self.to_xml()"),
        );
    }

    /// A constructor taking the text positionally, accepting extra attributes and
    /// seeding the ordered content with the inline children it is given — only
    /// for a model with text or inline children.
    fn write_init(&self, w: &mut Writer, imports: &mut Imports) {
        let text = self.all.iter().find(|field| is_text(field));
        let inline = self.inline_fields();
        if text.is_none() && inline.is_empty() {
            return;
        }
        let keyword = Self::literal_defaulted_last(
            self.all
                .iter()
                .filter(|field| text.is_none_or(|text| !std::ptr::eq(*field, text)))
                .collect(),
        );
        let mut ordered: Vec<&Field> = Vec::new();
        ordered.extend(text);
        ordered.extend(keyword.iter().copied());
        let positional: Vec<Param> = text
            .map(|field| Self::param(field, imports))
            .into_iter()
            .collect();
        let named: Vec<Param> = keyword
            .iter()
            .map(|field| Self::param(field, imports))
            .collect();
        let order = if inline.is_empty() {
            String::new()
        } else {
            imports.add_core_local("xml_utilities", "order_xml_content")
        };
        let arguments = ordered
            .iter()
            .map(|field| format!("{}={}", self.attribute_name(field), field.py_name))
            .collect::<Vec<_>>()
            .join(", ");
        let body = |w: &mut Writer| {
            w.line(&format!(
                "super().__init__(**dict({arguments}), **{EXTRA_ATTRIBUTES})"
            ));
            if !inline.is_empty() {
                let mut extend = format!("self.{CONTENT}.extend({order}([]");
                for field in &inline {
                    extend.push_str(&format!(", self.{}", self.attribute_name(field)));
                }
                extend.push_str("))");
                w.line(&extend);
            }
        };
        let documented: Vec<&Param> = positional.iter().chain(named.iter()).collect();
        let docstring = |w: &mut Writer| write_parameter_docstring(w, None, &documented);
        write_method(
            w,
            None,
            "__init__",
            &Signature {
                receiver: "self",
                positional: positional.clone(),
                named: named.clone(),
                kwargs: true,
                returns: "None".to_string(),
            },
            Some(&docstring),
            &body,
        );
    }

    /// A pre-validator letting a list-valued attribute or text be passed as one
    /// delimited string.
    fn write_list_coercion(&self, w: &mut Writer, imports: &mut Imports) {
        let mut separators: Vec<(String, String)> = Vec::new();
        let mut set =
            |key: &str, value: &str| match separators.iter_mut().find(|(known, _)| known == key) {
                Some(entry) => entry.1 = value.to_string(),
                None => separators.push((key.to_string(), value.to_string())),
            };
        for field in &self.all {
            if !(is_attribute(field) || is_text(field)) || list_item(field).is_none() {
                continue;
            }
            let separator = separator(field).filter(|s| !s.is_empty()).unwrap_or(" ");
            set(&field.py_name, separator);
            set(&field.wire_name, separator);
        }
        if separators.is_empty() {
            return;
        }
        let coerce = imports.add_core_local("xml_utilities", "coerce_xml_list_fields");
        let validator = imports.add_core_local("pydantic_utilities", "universal_root_validator");
        imports.add_plain("typing");
        let entries = separators
            .iter()
            .map(|(name, separator)| format!("{}: {}", py_repr(name), py_repr(separator)))
            .collect::<Vec<_>>()
            .join(", ");
        let values = "typing.Dict[str, typing.Any]".to_string();
        write_method(
            w,
            Some(&format!("{validator}(pre=True)")),
            "_coerce_xml_lists",
            &Signature {
                receiver: "cls",
                positional: vec![Param {
                    name: "values".to_string(),
                    hint: values.clone(),
                    initializer: None,
                    docs: None,
                }],
                named: Vec::new(),
                kwargs: false,
                returns: values,
            },
            None,
            &|w: &mut Writer| w.write(&format!("return {coerce}(values, {{{entries}}})")),
        );
    }

    fn write_from_xml(&self, w: &mut Writer, imports: &mut Imports) {
        let attribute_names: Vec<String> = self
            .all
            .iter()
            .filter(|field| is_attribute(field))
            .map(|field| xml_name(field).to_string())
            .collect();
        let has_text = self.all.iter().any(is_text);
        let inline = self.inline_fields();
        let mut skipped: Vec<String> = Vec::new();
        let mut wrappers: Vec<(String, Vec<String>)> = Vec::new();
        let mut inline_types: Vec<(String, String)> = Vec::new();
        let mut type_maps: Vec<Vec<(String, String)>> = Vec::new();
        for field in &self.all {
            if !is_element(field) {
                type_maps.push(Vec::new());
                continue;
            }
            let map = self.child_type_map(child_type(field), imports);
            if is_wrapped(field) {
                let items = if map.is_empty() {
                    vec![xml_name(field).to_string()]
                } else {
                    map.iter().map(|(tag, _)| tag.clone()).collect()
                };
                match wrappers
                    .iter_mut()
                    .find(|(name, _)| name == xml_name(field))
                {
                    Some(entry) => entry.1 = items,
                    None => wrappers.push((xml_name(field).to_string(), items)),
                }
            } else if map.is_empty() {
                skipped.push(xml_name(field).to_string());
            } else {
                for (tag, class) in &map {
                    match inline_types.iter_mut().find(|(known, _)| known == tag) {
                        Some(entry) => entry.1.clone_from(class),
                        None => inline_types.push((tag.clone(), class.clone())),
                    }
                }
            }
            type_maps.push(map);
        }
        let parse = imports.add_core_local("xml_utilities", "parse_xml");
        let content_fn = imports.add_core_local("xml_utilities", "xml_content");
        let build = imports.add_core_local("xml_utilities", "build_xml_model");
        let mut properties: Vec<String> = Vec::new();
        for (field, map) in self.all.iter().zip(&type_maps) {
            let separator_arg = separator(field)
                .map(|separator| format!(", separator={}", py_repr(separator)))
                .unwrap_or_default();
            let name = &field.py_name;
            if is_attribute(field) {
                let reader = imports.add_core_local("xml_utilities", "xml_attribute");
                properties.push(format!(
                    "{name}={reader}(node, {}{separator_arg}),",
                    py_repr(xml_name(field))
                ));
                continue;
            }
            if is_text(field) {
                let reader = imports.add_core_local("xml_utilities", "xml_leading_text");
                properties.push(format!("{name}={reader}(node{separator_arg}),"));
                continue;
            }
            let item = list_item(field);
            if inline.iter().any(|known| std::ptr::eq(*known, field)) {
                let reader = imports.add_core_local(
                    "xml_utilities",
                    if item.is_none() {
                        "xml_content_item"
                    } else {
                        "xml_content_items"
                    },
                );
                let mut entry = format!("{name}={reader}(content, (");
                for (_, class) in map {
                    entry.push_str(&format!("{class}, "));
                }
                entry.push(')');
                if item.is_some() && is_optional(field) {
                    entry.push_str(", optional=True");
                }
                entry.push_str("),");
                properties.push(entry);
                continue;
            }
            let reader = imports.add_core_local(
                "xml_utilities",
                if item.is_none() {
                    "xml_child"
                } else {
                    "xml_children"
                },
            );
            let mut entry = format!("{name}={reader}(node, {{");
            if map.is_empty() {
                entry.push_str(&format!("{}: str", py_repr(xml_name(field))));
            } else {
                let pairs: Vec<String> = map
                    .iter()
                    .map(|(tag, class)| format!("{}: {class}", py_repr(tag)))
                    .collect();
                entry.push_str(&pairs.join(", "));
            }
            entry.push('}');
            if item.is_some() {
                if is_wrapped(field) {
                    entry.push_str(&format!(", wrapper={}", py_repr(xml_name(field))));
                }
                if is_optional(field) {
                    entry.push_str(", optional=True");
                }
            }
            entry.push_str("),");
            properties.push(entry);
        }
        let mut content = format!("content = {content_fn}(node, {{");
        let pairs: Vec<String> = inline_types
            .iter()
            .map(|(tag, class)| format!("{}: {class}", py_repr(tag)))
            .collect();
        content.push_str(&pairs.join(", "));
        content.push('}');
        if has_text {
            content.push_str(", skip_leading_text=True");
        }
        if !skipped.is_empty() {
            content.push_str(&format!(", skip={}", set_literal(&skipped)));
        }
        if !wrappers.is_empty() {
            let literal = wrappers
                .iter()
                .map(|(name, items)| format!("{}: {}", py_repr(name), set_literal(items)))
                .collect::<Vec<_>>()
                .join(", ");
            content.push_str(&format!(", wrappers={{{literal}}}"));
        }
        content.push(')');
        let root = py_repr(&self.xml.name);
        let attributes = set_literal(&attribute_names);
        let body = |w: &mut Writer| {
            w.line(&format!("node = {parse}(xml, {root})"));
            w.line(&content);
            w.line(&format!("model = {build}("));
            w.indent();
            w.line("cls,");
            w.line("dict(");
            w.indent();
            for property in &properties {
                w.line(property);
            }
            w.outdent();
            w.line("),");
            w.line(&format!("node, {attributes},"));
            w.outdent();
            w.line(")");
            w.line(&format!("model.{CONTENT}[:] = content"));
            w.line("return model");
        };
        let node = imports.add_core_local("xml_utilities", "XmlNode");
        imports.add_plain("typing");
        let name = self.xml.name.clone();
        write_method(
            w,
            Some("classmethod"),
            "from_xml",
            &Signature {
                receiver: "cls",
                positional: vec![Param {
                    name: "xml".to_string(),
                    hint: format!("typing.Union[str, {node}]"),
                    initializer: None,
                    docs: None,
                }],
                named: Vec::new(),
                kwargs: false,
                returns: self.returns_self(),
            },
            Some(&|w: &mut Writer| {
                w.write(&format!(
                    "Parses a `<{}>` XML element from a document string or a parsed node.\n\nRaises `ValueError` for malformed XML, an unexpected root element or invalid values. Unknown attributes are kept as extra attributes; text segments and child elements (declared or not) are preserved in document order.",
                    escape_docstring(&name)
                ));
            }),
            &body,
        );
    }

    /// `add_child`, `add_text` and the three comment methods.
    fn write_content_methods(&self, w: &mut Writer, imports: &mut Imports) {
        let element = imports.add_core_local("xml_utilities", "XmlElement");
        let comment = imports.add_core_local("xml_utilities", "XmlComment");
        let simple = |w: &mut Writer, name: &str, param: (&str, &str), body: String, doc: &str| {
            write_method(
                w,
                None,
                name,
                &Signature {
                    receiver: "self",
                    positional: vec![Param {
                        name: param.0.to_string(),
                        hint: param.1.to_string(),
                        initializer: None,
                        docs: None,
                    }],
                    named: Vec::new(),
                    kwargs: false,
                    returns: self.returns_self(),
                },
                Some(&|w: &mut Writer| w.write(doc)),
                &|w: &mut Writer| {
                    w.line(&body);
                    w.line("return self");
                },
            );
        };
        simple(
            w,
            "add_child",
            ("child", &element),
            format!("self.{CONTENT}.append(child)"),
            "Appends an arbitrary child element (one the schema does not define) after the content added so far and returns this element.",
        );
        simple(
            w,
            "add_text",
            ("text", "str"),
            format!("self.{CONTENT}.append(text)"),
            "Appends a text segment after the children added so far and returns this element, so text and child elements can be interleaved.",
        );
        for (name, target, doc) in [
            (
                "comment",
                CONTENT,
                "Appends an XML comment (`<!--text-->`) inside this element, after the content added so far, and returns this element.",
            ),
            (
                "comment_before",
                COMMENTS_BEFORE,
                "Adds an XML comment rendered immediately before this element (as a sibling in its parent, or before the root element) and returns this element.",
            ),
            (
                "comment_after",
                COMMENTS_AFTER,
                "Adds an XML comment rendered immediately after this element (as a sibling in its parent, or after the root element) and returns this element.",
            ),
        ] {
            simple(
                w,
                name,
                ("text", "str"),
                format!("self.{target}.append({comment}(text))"),
                doc,
            );
        }
    }

    /// `append(child)` for a model with exactly one list of child elements, and
    /// a builder per XML model each list's items can be.
    fn write_builders(&self, w: &mut Writer, imports: &mut Imports) {
        let lists: Vec<(&Field, &TypeRef)> = self
            .all
            .iter()
            .filter(|field| is_element(field))
            .filter_map(|field| list_item(field).map(|item| (field, item)))
            .collect();
        if lists.is_empty() {
            return;
        }
        let append_child = imports.add_core_local("xml_utilities", "append_xml_child");
        for (field, item) in &lists {
            let wrapped = is_wrapped(field);
            let inline = append_arguments(wrapped);
            if lists.len() == 1 {
                let hint = render_type(item, imports).flat();
                let field_name = field.py_name.clone();
                write_method(
                    w,
                    None,
                    "append",
                    &Signature {
                        receiver: "self",
                        positional: vec![Param {
                            name: "child".to_string(),
                            hint,
                            initializer: None,
                            docs: None,
                        }],
                        named: Vec::new(),
                        kwargs: false,
                        returns: self.returns_self(),
                    },
                    Some(&|w: &mut Writer| {
                        w.write("Appends a child element and returns this element for chaining.");
                    }),
                    &|w: &mut Writer| {
                        w.line(&format!(
                            "{append_child}(self, {}, child{inline})",
                            py_repr(&field_name)
                        ));
                        w.line("return self");
                    },
                );
            }
            let names = self
                .builder_names
                .iter()
                .find(|(name, _)| *name == field.py_name)
                .map(|(_, names)| names.clone())
                .unwrap_or_default();
            for (class, method) in names {
                let append = ChildAppend {
                    field,
                    wrapped,
                    append_child: &append_child,
                };
                self.write_child_builder(w, imports, &method, &class, &append);
            }
        }
    }

    fn write_child_builder(
        &self,
        w: &mut Writer,
        imports: &mut Imports,
        method: &str,
        class: &str,
        append: &ChildAppend<'_>,
    ) {
        let ChildAppend {
            field,
            wrapped,
            append_child,
        } = *append;
        let inline = append_arguments(wrapped);
        let Some(child) = self.types.object(class) else {
            return;
        };
        let constructor = self.class_reference(class, imports);
        let returns = if class == self.obj.name {
            class.to_string()
        } else {
            render_type(&TypeRef::Named(class.to_string()), imports).flat()
        };
        let child_fields = self.types.all_fields(child, 0);
        let text = child_fields.iter().find(|field| is_text(field));
        let keyword = Self::literal_defaulted_last(
            child_fields
                .iter()
                .filter(|candidate| {
                    text.is_none_or(|text| !std::ptr::eq(*candidate, text))
                        && !(is_element(candidate) && list_item(candidate).is_some())
                })
                .collect(),
        );
        let mut forwarded: Vec<&Field> = Vec::new();
        forwarded.extend(text);
        forwarded.extend(keyword.iter().copied());
        let mut arguments: Vec<String> = forwarded
            .iter()
            .map(|field| format!("{0}={0}", field.py_name))
            .collect();
        for candidate in &child_fields {
            if forwarded
                .iter()
                .any(|known| std::ptr::eq(*known, candidate))
            {
                continue;
            }
            let empty = if is_optional(candidate) { "None" } else { "[]" };
            arguments.push(format!("{}={empty}", candidate.py_name));
        }
        arguments.push(format!("**{EXTRA_ATTRIBUTES}"));
        let field_name = field.py_name.clone();
        let body = |w: &mut Writer| {
            w.line(&format!("child = {constructor}({})", arguments.join(", ")));
            w.line(&format!(
                "{append_child}(self, {}, child{inline})",
                py_repr(&field_name)
            ));
            w.line("return child");
        };
        let mut summary = child
            .xml
            .as_ref()
            .map(|xml| format!("Appends a `<{}>` child element and returns it.", xml.name));
        if let Some(docs) = &child.docstring {
            summary = Some(match summary {
                Some(summary) => format!("{summary}\n\n{docs}"),
                None => docs.clone(),
            });
        }
        let positional: Vec<Param> = text
            .map(|field| Self::param(field, imports))
            .into_iter()
            .collect();
        let named: Vec<Param> = keyword
            .iter()
            .map(|field| Self::param(field, imports))
            .collect();
        let documented: Vec<&Param> = positional.iter().chain(named.iter()).collect();
        let docstring =
            |w: &mut Writer| write_parameter_docstring(w, summary.as_deref(), &documented);
        let has_docstring = summary.is_some() || !documented.is_empty();
        write_method(
            w,
            None,
            method,
            &Signature {
                receiver: "self",
                positional: positional.clone(),
                named: named.clone(),
                kwargs: true,
                returns,
            },
            has_docstring.then_some(&docstring as &dyn Fn(&mut Writer)),
            &body,
        );
    }
}

/// A sample value for an attribute or text property: its XML spelling and its
/// Python literal.
struct Sample {
    xml: String,
    python: String,
}

/// One property of a model under test.
struct TestProperty<'f> {
    field: &'f Field,
    wire_name: String,
    is_list: bool,
    is_required: bool,
}

/// The `tests/xml/test_<module>.py` round-trip suite of every XML model.
/// `first_party` says whether Fern's import sort files the SDK's own import in a
/// section of its own (see `scaffolding_files`): always in the packaged tree, and
/// in the flat tree only for a package named `fern`; otherwise it joins
/// `import pytest` with no blank line.
pub(super) fn test_files(pkg: &str, types: XmlTypes<'_>, first_party: bool) -> Vec<GeneratedFile> {
    types
        .all()
        .filter_map(|(decl, tag)| match decl {
            TypeDecl::Object(obj) => obj.xml.as_ref().map(|xml| (obj, xml, tag)),
            _ => None,
        })
        .map(|(obj, xml, tag)| {
            let module = match tag {
                Some(tag) if !tag.is_empty() => {
                    format!("{pkg}.{}.types.{}", module_path(tag), obj.module)
                }
                _ => format!("{pkg}.types.{}", obj.module),
            };
            let suite = TestSuite::new(obj, xml, types);
            GeneratedFile {
                path: PathBuf::from(format!("tests/xml/test_{}.py", obj.module)),
                contents: suite.render(&module, first_party),
            }
        })
        .collect()
}

const UNKNOWN_ENUM_VALUE: &str = "bogus-value";
const SPECIAL_CHARACTERS: &str = "a & b < c > d \"q\" 'r'";

struct TestSuite<'a> {
    class: &'a str,
    xml: &'a XmlEncoding,
    types: XmlTypes<'a>,
    fields: Vec<Field>,
}

impl<'a> TestSuite<'a> {
    fn new(obj: &'a ObjectType, xml: &'a XmlEncoding, types: XmlTypes<'a>) -> Self {
        let mut fields = types.extended_fields(obj);
        fields.extend(obj.fields.iter().cloned());
        fields.retain(|field| field.xml.is_some());
        TestSuite {
            class: &obj.name,
            xml,
            types,
            fields,
        }
    }

    fn properties(&self) -> Vec<TestProperty<'_>> {
        self.fields.iter().map(describe).collect()
    }

    fn render(&self, module: &str, first_party: bool) -> String {
        let mut body: Vec<String> = vec![
            HEADER.to_string(),
            String::new(),
            "import pytest".to_string(),
        ];
        if first_party {
            body.push(String::new());
        }
        body.push(format!("from {module} import {}", self.class));
        body.push(String::new());
        body.extend(self.round_trip_test());
        body.extend(self.unknown_content_test());
        body.extend(self.escaping_test());
        body.extend(self.open_enum_test());
        body.extend(self.child_order_test());
        body.extend(self.rejection_tests());
        body.join("\n") + "\n"
    }

    fn round_trip_test(&self) -> Vec<String> {
        let properties = self.properties();
        let sampled: Vec<(&TestProperty, Sample)> = properties
            .iter()
            .filter_map(|property| self.sample_value(property).map(|sample| (property, sample)))
            .collect();
        let document = self.sample_document(&sampled, &properties);
        let class = self.class;
        let mut lines = vec![
            String::new(),
            "def test_from_xml_to_xml_round_trips() -> None:".to_string(),
            format!("    parsed = {class}.from_xml({})", py_repr(&document)),
        ];
        for (property, sample) in &sampled {
            lines.push(format!(
                "    assert parsed.{} == {}",
                property.field.py_name, sample.python
            ));
        }
        lines.push("    serialized = parsed.to_xml(xml_declaration=False)".to_string());
        for (property, sample) in &sampled {
            match kind(property.field) {
                XmlKind::Attribute => lines.push(format!(
                    "    assert {} in serialized",
                    py_repr(&format!("{}=\"{}\"", property.wire_name, sample.xml))
                )),
                XmlKind::Text => lines.push(format!(
                    "    assert {} in serialized",
                    py_repr(&format!(">{}<", sample.xml))
                )),
                XmlKind::Element { .. } => {}
            }
        }
        lines.push(format!(
            "    assert {class}.from_xml(serialized).to_xml(xml_declaration=False) == serialized"
        ));
        lines.push("    assert parsed.to_xml().startswith('<?xml version=\"1.0\"')".to_string());
        lines.push("    assert str(parsed) == parsed.to_xml()".to_string());
        lines.push(String::new());
        lines
    }

    fn unknown_content_test(&self) -> Vec<String> {
        let document = self.document(" dataUnknown=\"1\"", "<Unknown a=\"1\">v</Unknown>", None);
        let class = self.class;
        vec![
            String::new(),
            "def test_from_xml_preserves_unknown_attributes_and_children() -> None:".to_string(),
            format!("    parsed = {class}.from_xml({})", py_repr(&document)),
            "    serialized = parsed.to_xml(xml_declaration=False)".to_string(),
            "    assert 'dataUnknown=\"1\"' in serialized".to_string(),
            "    assert '<Unknown a=\"1\">v</Unknown>' in serialized".to_string(),
            format!(
                "    assert {class}.from_xml(serialized).to_xml(xml_declaration=False) == serialized"
            ),
            String::new(),
        ]
    }

    fn escaping_test(&self) -> Vec<String> {
        let properties = self.properties();
        let Some(property) = properties.iter().find(|property| {
            matches!(kind(property.field), XmlKind::Attribute | XmlKind::Text)
                && !property.is_list
                && self.primitive(property) == Some(SamplePrimitive::String)
        }) else {
            return Vec::new();
        };
        let class = self.class;
        let mut arguments = vec![format!(
            "{}={}",
            property.field.py_name,
            py_repr(SPECIAL_CHARACTERS)
        )];
        arguments.extend(
            self.required_samples(&properties, Some(property))
                .iter()
                .map(|(other, sample)| format!("{}={}", other.field.py_name, sample.python)),
        );
        vec![
            String::new(),
            "def test_to_xml_escapes_special_characters() -> None:".to_string(),
            format!("    model = {class}({})", arguments.join(", ")),
            "    serialized = model.to_xml(xml_declaration=False)".to_string(),
            "    assert 'a & b' not in serialized".to_string(),
            "    assert '< c' not in serialized".to_string(),
            format!(
                "    assert {class}.from_xml(serialized).{} == {}",
                property.field.py_name,
                py_repr(SPECIAL_CHARACTERS)
            ),
            String::new(),
        ]
    }

    fn open_enum_test(&self) -> Vec<String> {
        let properties = self.properties();
        let Some(property) = properties.iter().find(|property| {
            kind(property.field) == XmlKind::Attribute
                && !property.is_list
                && self
                    .sample_type(property)
                    .and_then(|t| self.types.enum_values(t))
                    .is_some()
        }) else {
            return Vec::new();
        };
        let document = self.document(
            &format!(" {}=\"{UNKNOWN_ENUM_VALUE}\"", property.wire_name),
            "",
            Some(property),
        );
        let class = self.class;
        vec![
            String::new(),
            "def test_from_xml_keeps_unknown_enum_values() -> None:".to_string(),
            format!("    parsed = {class}.from_xml({})", py_repr(&document)),
            format!(
                "    assert {} in parsed.to_xml(xml_declaration=False)",
                py_repr(&format!("{}=\"{UNKNOWN_ENUM_VALUE}\"", property.wire_name))
            ),
            String::new(),
        ]
    }

    fn child_order_test(&self) -> Vec<String> {
        let properties = self.properties();
        let names = self.content_child_names(&properties);
        let has_text = properties.iter().any(|property| {
            kind(property.field) == XmlKind::Text
                && self.primitive(property) == Some(SamplePrimitive::String)
        });
        let body = if names.len() >= 2 {
            format!("<{0} /><{1} /><{0} />", names[0], names[1])
        } else if names.len() == 1 && has_text {
            format!("a<{} />b", names[0])
        } else {
            return Vec::new();
        };
        let document = self.document("", &body, None);
        let class = self.class;
        vec![
            String::new(),
            "def test_from_xml_preserves_child_order() -> None:".to_string(),
            format!("    parsed = {class}.from_xml({})", py_repr(&document)),
            format!(
                "    assert {} in parsed.to_xml(xml_declaration=False)",
                py_repr(&body)
            ),
            String::new(),
        ]
    }

    fn rejection_tests(&self) -> Vec<String> {
        let root = self.root_name();
        let class = self.class;
        let doctype = format!(
            "<!DOCTYPE {root} [<!ENTITY xxe \"injected\">]>{}&xxe;</{root}>",
            self.start_tag("", false)
        );
        vec![
            String::new(),
            "def test_from_xml_rejects_wrong_root_element() -> None:".to_string(),
            "    with pytest.raises(ValueError):".to_string(),
            format!(
                "        {class}.from_xml({})",
                py_repr(&format!("<NotThe{root} />"))
            ),
            String::new(),
            String::new(),
            "def test_from_xml_rejects_malformed_xml() -> None:".to_string(),
            "    with pytest.raises(ValueError):".to_string(),
            format!(
                "        {class}.from_xml({})",
                py_repr(&format!("{}<unclosed>", self.start_tag("", false)))
            ),
            String::new(),
            String::new(),
            "def test_from_xml_rejects_doctype() -> None:".to_string(),
            "    with pytest.raises(ValueError):".to_string(),
            format!("        {class}.from_xml({})", py_repr(&doctype)),
        ]
    }

    /// The required attributes and text with sample values, so a document in
    /// the tests other than the round trip still parses.
    fn required_samples<'p>(
        &self,
        properties: &'p [TestProperty<'p>],
        except: Option<&TestProperty<'_>>,
    ) -> Vec<(&'p TestProperty<'p>, Sample)> {
        properties
            .iter()
            .filter(|property| {
                property.is_required
                    && except.is_none_or(|except| !std::ptr::eq(except.field, property.field))
            })
            .filter_map(|property| self.sample_value(property).map(|sample| (property, sample)))
            .collect()
    }

    fn document(&self, attributes: &str, body: &str, except: Option<&TestProperty<'_>>) -> String {
        let properties = self.properties();
        let required = self.required_samples(&properties, except);
        let required_attributes: String = required
            .iter()
            .filter(|(property, _)| kind(property.field) == XmlKind::Attribute)
            .map(|(property, sample)| format!(" {}=\"{}\"", property.wire_name, sample.xml))
            .collect();
        let required_text = required
            .iter()
            .find(|(property, _)| kind(property.field) == XmlKind::Text)
            .map(|(_, sample)| sample.xml.clone())
            .unwrap_or_default();
        let content = format!("{required_text}{body}");
        let attributes = format!("{required_attributes}{attributes}");
        if content.is_empty() {
            return self.start_tag(&attributes, true);
        }
        format!(
            "{}{content}</{}>",
            self.start_tag(&attributes, false),
            self.root_name()
        )
    }

    fn sample_document(
        &self,
        sampled: &[(&TestProperty, Sample)],
        properties: &[TestProperty<'_>],
    ) -> String {
        let attributes: String = sampled
            .iter()
            .filter(|(property, _)| kind(property.field) == XmlKind::Attribute)
            .map(|(property, sample)| format!(" {}=\"{}\"", property.wire_name, sample.xml))
            .collect();
        let text = sampled
            .iter()
            .find(|(property, _)| kind(property.field) == XmlKind::Text)
            .map(|(_, sample)| sample.xml.clone())
            .unwrap_or_default();
        let children: String = properties
            .iter()
            .filter(|property| is_element(property.field))
            .map(|property| self.sample_child(property))
            .collect();
        let body = format!("{text}{children}");
        if body.is_empty() {
            return self.start_tag(&attributes, true);
        }
        format!(
            "{}{body}</{}>",
            self.start_tag(&attributes, false),
            self.root_name()
        )
    }

    /// The XML models a child element of the property can be, each declaring
    /// its own XML element.
    fn xml_children(&self, property: &TestProperty<'_>) -> Vec<&'a ObjectType> {
        self.types
            .xml_object_names(child_type(property.field), 0)
            .iter()
            .filter_map(|name| self.types.object(name))
            .collect()
    }

    fn sample_child(&self, property: &TestProperty<'_>) -> String {
        let Some(child) = self.xml_children(property).into_iter().next() else {
            return String::new();
        };
        let element = self.sample_element(child);
        if is_wrapped(property.field) && property.is_list {
            return format!("<{0}>{element}</{0}>", property.wire_name);
        }
        element
    }

    fn sample_element(&self, child: &ObjectType) -> String {
        let Some(xml) = &child.xml else {
            return String::new();
        };
        let mut fields = self.types.extended_fields(child);
        fields.extend(child.fields.iter().cloned());
        let properties: Vec<TestProperty> = fields
            .iter()
            .filter(|field| field.xml.is_some())
            .map(describe)
            .collect();
        let required: Vec<(&TestProperty, Sample)> = properties
            .iter()
            .filter(|property| property.is_required)
            .filter_map(|property| self.sample_value(property).map(|sample| (property, sample)))
            .collect();
        let attributes: String = required
            .iter()
            .filter(|(property, _)| kind(property.field) == XmlKind::Attribute)
            .map(|(property, sample)| format!(" {}=\"{}\"", property.wire_name, sample.xml))
            .collect();
        let text = required
            .iter()
            .find(|(property, _)| kind(property.field) == XmlKind::Text)
            .map(|(_, sample)| sample.xml.clone());
        let name = qualified(xml);
        let namespace = namespace_declaration(xml);
        match text {
            None => format!("<{name}{namespace}{attributes} />"),
            Some(text) => format!("<{name}{namespace}{attributes}>{text}</{name}>"),
        }
    }

    /// The element names of the non-namespaced XML models living in the ordered
    /// content (not inside a wrapper).
    fn content_child_names(&self, properties: &[TestProperty<'_>]) -> Vec<String> {
        let mut names: Vec<String> = Vec::new();
        for property in properties {
            if !is_element(property.field) || (is_wrapped(property.field) && property.is_list) {
                continue;
            }
            for child in self.xml_children(property) {
                if let Some(xml) = &child.xml {
                    if xml.namespace.is_none() && !names.contains(&xml.name) {
                        names.push(xml.name.clone());
                    }
                }
            }
        }
        names
    }

    fn root_name(&self) -> String {
        qualified(self.xml)
    }

    fn start_tag(&self, attributes: &str, self_closing: bool) -> String {
        format!(
            "<{}{}{attributes}{}",
            self.root_name(),
            namespace_declaration(self.xml),
            if self_closing { " />" } else { ">" }
        )
    }

    /// The type a property's sample is drawn from: a list's item, or a required
    /// value (an optional one is a container Fern draws no sample from).
    fn sample_type<'t>(&self, property: &TestProperty<'t>) -> Option<&'t TypeRef> {
        if property.is_list {
            list_item(property.field)
        } else if is_optional(property.field) {
            None
        } else {
            Some(&property.field.type_ref)
        }
    }

    fn primitive(&self, property: &TestProperty<'_>) -> Option<SamplePrimitive> {
        match self.sample_type(property)? {
            TypeRef::Primitive(Prim::Str) => (!property
                .field
                .xml
                .as_ref()
                .is_some_and(|xml| xml.opaque_string))
            .then_some(SamplePrimitive::String),
            TypeRef::Primitive(Prim::Int | Prim::Long) => Some(SamplePrimitive::Integer),
            TypeRef::Primitive(Prim::Float) => Some(SamplePrimitive::Double),
            TypeRef::Primitive(Prim::Bool) => Some(SamplePrimitive::Boolean),
            _ => None,
        }
    }

    fn sample_value(&self, property: &TestProperty<'_>) -> Option<Sample> {
        if !matches!(kind(property.field), XmlKind::Attribute | XmlKind::Text) {
            return None;
        }
        let first = self.sample_item(property, 0)?;
        if !property.is_list {
            return Some(first);
        }
        let second = self.sample_item(property, 1)?;
        let separator = separator(property.field).unwrap_or(" ");
        Some(Sample {
            xml: format!("{}{separator}{}", first.xml, second.xml),
            python: format!("[{}, {}]", first.python, second.python),
        })
    }

    fn sample_item(&self, property: &TestProperty<'_>, index: usize) -> Option<Sample> {
        if let Some(values) = self
            .sample_type(property)
            .and_then(|t| self.types.enum_values(t))
        {
            let value = values.get(index).or_else(|| values.first())?.clone();
            return Some(Sample {
                python: py_repr(&value),
                xml: value,
            });
        }
        let is_text = kind(property.field) == XmlKind::Text;
        match self.primitive(property)? {
            SamplePrimitive::String => {
                let stem = if is_text {
                    "text"
                } else {
                    property.wire_name.as_str()
                };
                let value = if index == 0 {
                    stem.to_string()
                } else {
                    format!("{stem}-{}", index + 1)
                };
                Some(Sample {
                    python: py_repr(&value),
                    xml: value,
                })
            }
            SamplePrimitive::Integer => Some(Sample {
                xml: (index + 1).to_string(),
                python: (index + 1).to_string(),
            }),
            SamplePrimitive::Boolean => Some(if index == 0 {
                Sample {
                    xml: "true".to_string(),
                    python: "True".to_string(),
                }
            } else {
                Sample {
                    xml: "false".to_string(),
                    python: "False".to_string(),
                }
            }),
            SamplePrimitive::Double => Some(Sample {
                xml: format!("{}.5", index + 1),
                python: format!("{}.5", index + 1),
            }),
        }
    }
}

/// How a child builder appends the element it builds: the list field it lands
/// in, whether that list is wrapped in an element of its own, and the core
/// helper that appends it.
#[derive(Clone, Copy)]
struct ChildAppend<'a> {
    field: &'a Field,
    wrapped: bool,
    append_child: &'a str,
}

/// The trailing arguments of an `append_xml_child` call: a wrapped list's
/// children are appended inside its wrapper, so the call says `inline=False`.
fn append_arguments(wrapped: bool) -> &'static str {
    if wrapped {
        ", inline=False"
    } else {
        ""
    }
}

/// The primitive a generated XML test samples a value of.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
enum SamplePrimitive {
    String,
    Integer,
    Double,
    Boolean,
}

fn describe(field: &Field) -> TestProperty<'_> {
    TestProperty {
        field,
        wire_name: xml_name(field).to_string(),
        is_list: list_item(field).is_some(),
        is_required: !is_optional(field),
    }
}

fn qualified(xml: &XmlEncoding) -> String {
    match &xml.prefix {
        Some(prefix) => format!("{prefix}:{}", xml.name),
        None => xml.name.clone(),
    }
}

fn namespace_declaration(xml: &XmlEncoding) -> String {
    match (&xml.namespace, &xml.prefix) {
        (Some(namespace), Some(prefix)) => format!(" xmlns:{prefix}=\"{namespace}\""),
        (Some(namespace), None) => format!(" xmlns=\"{namespace}\""),
        (None, _) => String::new(),
    }
}

#[cfg(test)]
mod tests {
    use super::{py_double_quoted, py_repr, set_literal, Writer};

    /// Every file the generator writes for `document`, formatted, keyed by path.
    fn generate(document: serde_json::Value) -> std::collections::BTreeMap<String, String> {
        let doc: crate::openapi::OpenApi =
            serde_json::from_value(document).expect("document deserializes");
        let config = crate::config::GenerateConfig::new(
            std::path::PathBuf::from("openapi.yml"),
            std::path::PathBuf::from("out"),
            Some("zoo".to_string()),
            None,
            None,
            crate::settings::ExtraFields::default(),
            "Zoo",
        )
        .expect("the config is well formed");
        super::super::generate(&crate::ir::build(&doc, &config))
            .expect("the document generates")
            .into_iter()
            .map(|file| {
                (
                    file.path.to_string_lossy().replace('\\', "/"),
                    file.contents,
                )
            })
            .collect()
    }

    /// An API answering `GET /pets` with `schemas.Pet`, declaring `schemas`.
    fn document(schemas: serde_json::Value) -> serde_json::Value {
        serde_json::json!({
            "openapi": "3.0.3",
            "info": {"title": "Zoo", "version": "1"},
            "paths": {"/pets": {"get": {
                "operationId": "getPet",
                "responses": {"200": {"description": "ok", "content": {
                    "application/xml": {"schema": {"$ref": "#/components/schemas/Pet"}}
                }}}
            }}},
            "components": {"schemas": schemas}
        })
    }

    /// A namespaced pet with an attribute, a delimited list attribute, an enum
    /// child, an inline category model and a wrapped list of tag models.
    fn zoo() -> serde_json::Value {
        document(serde_json::json!({
            "Kind": {"type": "string", "enum": ["cat", "dog"]},
            "Category": {"type": "object", "xml": {"name": "category"},
                "properties": {"name": {"type": "string"}}},
            "Tag": {"type": "object", "xml": {"name": "tag"}, "description": "A label on a pet.",
                "properties": {
                    "label": {"type": "string", "x-fern-xml-text": true},
                    "lang": {"type": "string", "xml": {"attribute": true}}
                }},
            "Pet": {"type": "object", "xml": {"name": "pet", "namespace": "urn:zoo", "prefix": "z"},
                "required": ["id", "kind", "nickname"],
                "properties": {
                    "id": {"type": "integer", "xml": {"attribute": true}},
                    "kind": {"$ref": "#/components/schemas/Kind"},
                    "nickname": {"type": "string", "xml": {"attribute": true, "name": "nick"}},
                    "codes": {"type": "array", "items": {"type": "string"},
                        "xml": {"attribute": true}, "x-fern-xml-list-separator": ","},
                    "category": {"$ref": "#/components/schemas/Category"},
                    "tags": {"type": "array", "xml": {"wrapped": true},
                        "items": {"$ref": "#/components/schemas/Tag"}}
                }}
        }))
    }

    #[test]
    fn an_xml_model_serializes_its_attributes_children_and_inline_content() {
        let files = generate(zoo());
        let pet = &files["src/zoo/types/pet.py"];
        for expected in [
            "from __future__ import annotations",
            "class Pet(UniversalBaseModel):",
            "_content: typing.List[XmlContent] = pydantic.PrivateAttr(default_factory=list)",
            "_comments_before: typing.List[XmlComment] = pydantic.PrivateAttr(default_factory=list)",
            "def to_xml(self, *, xml_declaration: bool = True) -> str:",
            "Serializes this object as a `<pet>` XML element, prefixed with the XML declaration unless `xml_declaration` is False.",
            "            name=\"pet\",\n            namespace=\"urn:zoo\",\n            prefix=\"z\",",
            "XmlAttribute(name=\"id\", value=self.id),",
            "XmlAttribute(name=\"nick\", value=self.nickname),",
            "XmlAttribute(name=\"codes\", value=self.codes, separator=\",\"),",
            "*extra_xml_attributes(self),",
            "XmlChild(name=\"kind\", value=self.kind),",
            "XmlChild(name=\"tags\", value=self.tags, wrapped=True),",
            "content=order_xml_content(self._content, self.category),",
            "def __str__(self) -> str:\n        return self.to_xml()",
            "self._content.extend(order_xml_content([], self.category))",
            "@universal_root_validator(pre=True)\n    def _coerce_xml_lists(cls, values: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:\n        return coerce_xml_list_fields(values, {\"codes\": \",\"})",
            "@classmethod\n    def from_xml(cls, xml: typing.Union[str, XmlNode]) -> Pet:",
            "node = parse_xml(xml, \"pet\")",
            "content = xml_content(node, {\"category\": Category}, skip={\"kind\"}, wrappers={\"tags\": {\"tag\"}})",
            "id=xml_attribute(node, \"id\"),",
            "codes=xml_attribute(node, \"codes\", separator=\",\"),",
            "category=xml_content_item(content, (Category,)),",
            "tags=xml_children(node, {\"tag\": Tag}, wrapper=\"tags\", optional=True),",
            "{\"id\", \"nick\", \"codes\"},",
            "model._content[:] = content",
            "def add_child(self, child: XmlElement) -> Pet:",
            "def add_text(self, text: str) -> Pet:",
            "def comment_before(self, text: str) -> Pet:",
            "self._comments_after.append(XmlComment(text))",
            "def append(self, child: Tag) -> Pet:",
            "append_xml_child(self, \"tags\", child, inline=False)",
            "copy_on_model_validation = \"none\"",
        ] {
            assert!(pet.contains(expected), "missing {expected:?} in\n{pet}");
        }
        // The builder for `<tag>` takes the text positionally and the attribute
        // by keyword, documents both, and returns the child it appended.
        assert!(pet.contains(
            "    def tag(\n        self, label: typing.Optional[str] = None, *, lang: typing.Optional[str] = None, **extra_attributes: str\n    ) -> Tag:\n        \"\"\"\n        Appends a `<tag>` child element and returns it.\n\n        A label on a pet.\n\n        Parameters\n        ----------\n        label : typing.Optional[str]\n\n        lang : typing.Optional[str]\n\n        **extra_attributes : str\n            Additional XML attributes not declared in the API definition.\n        \"\"\"\n        child = Tag(label=label, lang=lang, **extra_attributes)\n"
        ), "{pet}");
        // The utilities ship with the SDK, unexported from `core`.
        assert_eq!(files["src/zoo/core/xml_utilities.py"], super::XML_UTILITIES);
        assert!(!files["src/zoo/core/__init__.py"].contains("xml_utilities"));
        // A model without an `xml` object is untouched.
        assert!(!files["src/zoo/types/kind.py"].contains("xml"));
    }

    #[test]
    fn a_text_model_takes_its_text_positionally_and_reads_it_back() {
        let files = generate(zoo());
        let tag = &files["src/zoo/types/tag.py"];
        for expected in [
            "def __init__(\n        self, label: typing.Optional[str] = None, *, lang: typing.Optional[str] = None, **extra_attributes: str\n    ) -> None:",
            "super().__init__(**dict(label=label, lang=lang), **extra_attributes)",
            "text=self.label,",
            "content = xml_content(node, {}, skip_leading_text=True)",
            "label=xml_leading_text(node),",
            "lang=xml_attribute(node, \"lang\"),",
            "{\"lang\"},",
        ] {
            assert!(tag.contains(expected), "missing {expected:?} in\n{tag}");
        }
        // No child element at all: neither `XmlChild` nor a builder.
        assert!(!tag.contains("XmlChild"), "{tag}");
        assert!(!tag.contains("def append"), "{tag}");
    }

    #[test]
    fn every_xml_model_gets_a_round_trip_test_module() {
        let files = generate(zoo());
        let mut modules: Vec<&str> = files
            .keys()
            .filter(|path| path.starts_with("tests/xml/"))
            .map(String::as_str)
            .collect();
        modules.sort_unstable();
        assert_eq!(
            modules,
            [
                "tests/xml/test_category.py",
                "tests/xml/test_pet.py",
                "tests/xml/test_tag.py"
            ]
        );
        let pet = &files["tests/xml/test_pet.py"];
        for expected in [
            "import pytest\n\nfrom zoo.types.pet import Pet\n",
            // Required attributes and a two-item delimited list are sampled; the
            // first inline and wrapped children are written empty.
            "parsed = Pet.from_xml(\n        '<z:pet xmlns:z=\"urn:zoo\" id=\"1\" nick=\"nick\" codes=\"codes,codes-2\"><category /><tags><tag /></tags></z:pet>'\n    )",
            "assert parsed.id == 1",
            "assert parsed.nickname == \"nick\"",
            "assert parsed.codes == [\"codes\", \"codes-2\"]",
            "assert 'nick=\"nick\"' in serialized",
            "def test_to_xml_escapes_special_characters() -> None:\n    model = Pet(nickname=\"a & b < c > d \\\"q\\\" 'r'\", id=1)",
            "assert Pet.from_xml(serialized).nickname == \"a & b < c > d \\\"q\\\" 'r'\"",
            "Pet.from_xml(\"<NotThez:pet />\")",
            "Pet.from_xml('<z:pet xmlns:z=\"urn:zoo\"><unclosed>')",
            "'<!DOCTYPE z:pet [<!ENTITY xxe \"injected\">]><z:pet xmlns:z=\"urn:zoo\">&xxe;</z:pet>'",
        ] {
            assert!(pet.contains(expected), "missing {expected:?} in\n{pet}");
        }
        // One inline child type and no enum attribute: neither of those tests.
        assert!(
            !pet.contains("test_from_xml_preserves_child_order"),
            "{pet}"
        );
        assert!(
            !pet.contains("test_from_xml_keeps_unknown_enum_values"),
            "{pet}"
        );
    }

    #[test]
    fn an_enum_attribute_and_two_inline_child_types_get_their_tests() {
        let files = generate(document(serde_json::json!({
            "Size": {"type": "string", "enum": ["small", "large"]},
            "Bark": {"type": "object", "xml": {"name": "bark"}, "properties": {}},
            "Purr": {"type": "object", "xml": {"name": "purr"}, "properties": {}},
            "Sound": {"oneOf": [
                {"$ref": "#/components/schemas/Bark"},
                {"$ref": "#/components/schemas/Purr"}
            ]},
            "Pet": {"type": "object", "xml": {"name": "pet"}, "required": ["size"],
                "properties": {
                    "size": {"$ref": "#/components/schemas/Size", "xml": {"attribute": true}},
                    "sounds": {"type": "array", "items": {"$ref": "#/components/schemas/Sound"}}
                }}
        })));
        let pet = &files["src/zoo/types/pet.py"];
        for expected in [
            "content = xml_content(node, {\"bark\": Bark, \"purr\": Purr})",
            // Fern writes each class with a trailing comma, so ruff explodes the
            // tuple once it holds two.
            "sounds=xml_content_items(\n                    content,\n                    (\n                        Bark,\n                        Purr,\n                    ),\n                    optional=True,\n                ),",
            "content=order_xml_content(self._content, self.sounds),",
            "def bark(self, **extra_attributes: str) -> Bark:",
            "child = Bark(**extra_attributes)\n        append_xml_child(self, \"sounds\", child)\n        return child",
            "def purr(self, **extra_attributes: str) -> Purr:",
        ] {
            assert!(pet.contains(expected), "missing {expected:?} in\n{pet}");
        }
        let tests = &files["tests/xml/test_pet.py"];
        for expected in [
            "def test_from_xml_keeps_unknown_enum_values() -> None:\n    parsed = Pet.from_xml('<pet size=\"bogus-value\" />')\n    assert 'size=\"bogus-value\"' in parsed.to_xml(xml_declaration=False)",
            "def test_from_xml_preserves_child_order() -> None:\n    parsed = Pet.from_xml('<pet size=\"small\"><bark /><purr /><bark /></pet>')\n    assert \"<bark /><purr /><bark />\" in parsed.to_xml(xml_declaration=False)",
        ] {
            assert!(tests.contains(expected), "missing {expected:?} in\n{tests}");
        }
    }

    #[test]
    fn a_builder_named_like_the_text_field_moves_the_text_to_an_underscore_attribute() {
        let files = generate(document(serde_json::json!({
            "Number": {"type": "object", "xml": {"name": "number"},
                "properties": {"value": {"type": "string", "x-crozier-xml-text": true}}},
            "Pet": {"type": "object", "xml": {"name": "pet"},
                "properties": {
                    "number": {"type": "string",
                        "x-crozier-xml-text": true, "x-fern-xml-text": false},
                    "numbers": {"type": "array", "items": {"$ref": "#/components/schemas/Number"}}
                }}
        })));
        let pet = &files["src/zoo/types/pet.py"];
        for expected in [
            "number_: typing_extensions.Annotated[",
            "FieldMetadata(alias=\"number\")",
            "text=self.number_,",
            "super().__init__(**dict(number_=number, numbers=numbers), **extra_attributes)",
            "number=xml_leading_text(node),",
            "def number(self, value: typing.Optional[str] = None, **extra_attributes: str) -> Number:",
        ] {
            assert!(pet.contains(expected), "missing {expected:?} in\n{pet}");
        }
    }

    #[test]
    fn an_sdk_without_xml_models_ships_no_xml_utilities_or_tests() {
        let files = generate(document(serde_json::json!({
            "Pet": {"type": "object", "properties": {"name": {"type": "string"}}}
        })));
        assert!(!files.contains_key("src/zoo/core/xml_utilities.py"));
        assert!(!files.keys().any(|path| path.starts_with("tests/xml/")));
        let pet = &files["src/zoo/types/pet.py"];
        assert!(!pet.contains("__future__"), "{pet}");
        assert!(!pet.contains("copy_on_model_validation"), "{pet}");
    }

    #[test]
    fn python_literals_match_repr() {
        assert_eq!(py_repr("Order"), "'Order'");
        assert_eq!(py_repr("it's"), "\"it's\"");
        assert_eq!(py_repr("both ' and \""), "'both \\' and \"'");
        assert_eq!(py_repr("a\\b\n\t\u{1}"), "'a\\\\b\\n\\t\\x01'");
        // Each as Python 3's `repr()` writes it: separators, format and
        // private-use characters escaped at their width; a printable letter kept.
        assert_eq!(py_repr("a\u{a0}b"), "'a\\xa0b'");
        assert_eq!(
            py_repr("\u{ad}\u{200b}\u{2028}\u{3000}"),
            "'\\xad\\u200b\\u2028\\u3000'"
        );
        assert_eq!(
            py_repr("\u{e000}\u{e0001}\u{10fffd}"),
            "'\\ue000\\U000e0001\\U0010fffd'"
        );
        assert_eq!(py_repr("café, π"), "'café, π'");
        assert_eq!(set_literal(&[]), "()");
        assert_eq!(
            set_literal(&["b".to_string(), "a".to_string(), "b".to_string()]),
            "{'b', 'a'}"
        );
    }

    #[test]
    fn a_literal_initializer_escapes_its_quotes_backslashes_and_controls() {
        assert_eq!(py_double_quoted("pet"), "\"pet\"");
        assert_eq!(
            py_double_quoted("say \"hi\"\\ok\n"),
            "\"say \\\"hi\\\"\\\\ok\\n\""
        );
    }

    /// An element name a document spells with Python's docstring quote still
    /// generates valid Python: the serializer's and parser's docstrings escape it.
    #[test]
    fn a_triple_quote_in_an_xml_name_stays_inside_the_docstrings() {
        let files = generate(document(serde_json::json!({
            "Pet": {"type": "object", "xml": {"name": "pet\"\"\"x"},
                "properties": {"id": {"type": "integer", "xml": {"attribute": true}}}}
        })));
        let pet = &files["src/zoo/types/pet.py"];
        assert_eq!(
            pet.matches("`<pet\\\"\"\"x>` XML element").count(),
            2,
            "{pet}"
        );
    }

    /// The reserved names are what the emitter writes: every public method a
    /// generated XML model defines, apart from its child builders, is one a
    /// builder must not take.
    #[test]
    fn every_method_an_xml_model_defines_is_reserved_from_its_builders() {
        let files = generate(zoo());
        let mut seen = std::collections::BTreeSet::new();
        for (path, source) in files.iter().filter(|(path, source)| {
            path.starts_with("src/zoo/types/") && source.contains("def to_xml(")
        }) {
            let lines: Vec<&str> = source.lines().collect();
            for (index, line) in lines.iter().enumerate() {
                let Some(name) = line
                    .strip_prefix("    def ")
                    .and_then(|rest| rest.split('(').next())
                else {
                    continue;
                };
                let docstring = lines[index..]
                    .iter()
                    .skip_while(|line| !line.trim_start().starts_with("\"\"\""))
                    .nth(1)
                    .map(|line| line.trim())
                    .unwrap_or_default();
                // A private helper's leading underscore keeps it clear of every
                // builder, which is named after a child element.
                if name.starts_with('_') || docstring.starts_with("Appends a `<") {
                    continue;
                }
                assert!(
                    super::RESERVED_METHOD_NAMES.contains(&name),
                    "{path} defines `{name}`, which a child builder could take"
                );
                seen.insert(name.to_string());
            }
        }
        assert!(
            seen.contains("to_xml") && seen.contains("add_child"),
            "{seen:?}"
        );
    }

    #[test]
    fn the_writer_indents_at_line_starts_and_breaks_lines_to_indent() {
        let mut w = Writer::new(1);
        w.write("def f():");
        w.indent();
        w.line("x = 1");
        w.write("y = (\n2)");
        w.outdent();
        w.newline_if_needed();
        w.line("");
        assert_eq!(
            w.out,
            "    def f():\n        x = 1\n        y = (\n        2)\n    \n"
        );
    }
}
