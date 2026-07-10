//! Laying out Python type expressions the way `ruff format` does.
//!
//! Fern runs `ruff format` (line length 120) over its generated code, so crozier
//! must wrap long lines identically to be byte-for-byte equal. Rather than parse
//! and re-format strings, the emitter builds a small [`Doc`] tree for each type
//! expression and [`layout`] renders it, reproducing ruff's recursive
//! right-hand-split: keep a statement on one line if it fits, else explode the
//! outermost bracket; if the exploded contents still don't fit on one line,
//! place each element on its own line with a trailing comma, recursively.

/// ruff's configured line length for Fern's output.
pub const LIMIT: usize = 120;

/// A renderable type expression: either an atomic token that is never split, or
/// a bracketed group (`open` … comma-separated `items` … `close`) that may be
/// exploded across lines when too long.
#[derive(Debug, Clone)]
pub enum Doc {
    /// A token rendered verbatim and never split (e.g. `str`, a class name, a
    /// `FieldMetadata(...)` call, a quoted literal).
    Atom(String),
    /// A bracketed group such as `typing.Union[` … `]`.
    Group {
        /// Text up to and including the opening bracket, e.g. `typing.List[`.
        open: String,
        /// The comma-separated elements between the brackets.
        items: Vec<Doc>,
        /// The closing bracket, e.g. `]`.
        close: String,
    },
}

impl Doc {
    /// An atomic token.
    pub fn atom(text: impl Into<String>) -> Doc {
        Doc::Atom(text.into())
    }

    /// A bracketed group.
    pub fn group(open: impl Into<String>, items: Vec<Doc>, close: impl Into<String>) -> Doc {
        Doc::Group {
            open: open.into(),
            items,
            close: close.into(),
        }
    }

    /// The single-line rendering, ignoring the line limit.
    pub fn flat(&self) -> String {
        match self {
            Doc::Atom(text) => text.clone(),
            Doc::Group { open, items, close } => {
                let inner = items.iter().map(Doc::flat).collect::<Vec<_>>().join(", ");
                format!("{open}{inner}{close}")
            }
        }
    }
}

/// Lay out `prefix` + `doc` + `suffix` as one or more lines. `indent` is the
/// number of leading spaces already in `prefix` (the statement's base indent).
/// Fits on one line → returned as-is; otherwise the outermost bracket is
/// exploded and its contents laid out at `indent + 4`.
pub fn layout(prefix: &str, doc: &Doc, suffix: &str, indent: usize) -> String {
    let flat = format!("{prefix}{}{suffix}", doc.flat());
    if flat.len() <= LIMIT {
        return flat;
    }
    match doc {
        // An atom cannot be split; leave it long (ruff does the same).
        Doc::Atom(_) => flat,
        Doc::Group { open, items, close } => {
            let mut out = format!("{prefix}{open}\n");
            out.push_str(&render_items(items, indent + 4));
            out.push_str(&" ".repeat(indent));
            out.push_str(close);
            out.push_str(suffix);
            out
        }
    }
}

/// Render the contents of an exploded bracket at `indent`. If the elements fit
/// on one line together they stay on one line (no trailing comma); otherwise
/// each element goes on its own line with a trailing comma.
fn render_items(items: &[Doc], indent: usize) -> String {
    let pad = " ".repeat(indent);
    let inner = items.iter().map(Doc::flat).collect::<Vec<_>>().join(", ");
    if indent + inner.len() <= LIMIT {
        return format!("{pad}{inner}\n");
    }
    let mut out = String::new();
    for item in items {
        out.push_str(&layout_item(item, indent));
    }
    out
}

/// Render one exploded element at `indent`, followed by a trailing comma. A
/// group whose flat form is too long is itself exploded.
fn layout_item(item: &Doc, indent: usize) -> String {
    let pad = " ".repeat(indent);
    let flat = item.flat();
    if indent + flat.len() <= LIMIT {
        return format!("{pad}{flat},\n");
    }
    match item {
        Doc::Atom(_) => format!("{pad}{flat},\n"),
        Doc::Group { open, items, close } => {
            let mut out = format!("{pad}{open}\n");
            out.push_str(&render_items(items, indent + 4));
            out.push_str(&pad);
            out.push_str(close);
            out.push_str(",\n");
            out
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn union(parts: Vec<Doc>) -> Doc {
        Doc::group("typing.Union[", parts, "]")
    }

    #[test]
    fn short_expression_stays_on_one_line() {
        let doc = union(vec![Doc::atom("float"), Doc::atom("str")]);
        assert_eq!(layout("X = ", &doc, "", 0), "X = typing.Union[float, str]");
    }

    #[test]
    fn wide_union_explodes_with_contents_on_one_line() {
        // Exceeds 120, but the exploded contents fit on one line → no trailing
        // comma (ruff's single-line-inside-brackets form).
        let doc = union(vec![
            Doc::group(
                "typing.Literal[",
                vec![
                    Doc::atom("\"API_ERROR\""),
                    Doc::atom("\"AUTHENTICATION_ERROR\""),
                    Doc::atom("\"INVALID_REQUEST_ERROR\""),
                ],
                "]",
            ),
            Doc::atom("typing.Any"),
        ]);
        assert_eq!(
            layout("EndpointsErrorCategory = ", &doc, "", 0),
            "EndpointsErrorCategory = typing.Union[\n    \
             typing.Literal[\"API_ERROR\", \"AUTHENTICATION_ERROR\", \"INVALID_REQUEST_ERROR\"], typing.Any\n]"
        );
    }

    #[test]
    fn very_wide_union_delimiter_splits_recursively() {
        let literal = Doc::group(
            "typing.Literal[",
            (0..11)
                .map(|i| Doc::atom(format!("\"VALUE_NUMBER_{i:02}_PADDING\"")))
                .collect(),
            "]",
        );
        let doc = union(vec![literal, Doc::atom("typing.Any")]);
        let out = layout("EndpointsErrorCode = ", &doc, "", 0);
        // The Literal is exploded one-per-line with trailing commas, nested under
        // the exploded Union (also one-per-line with trailing commas).
        assert!(out.starts_with("EndpointsErrorCode = typing.Union[\n    typing.Literal[\n"));
        assert!(out.contains("        \"VALUE_NUMBER_00_PADDING\",\n"));
        assert!(out.contains("        \"VALUE_NUMBER_10_PADDING\",\n"));
        assert!(out.ends_with("    ],\n    typing.Any,\n]"));
    }

    #[test]
    fn field_annotation_explodes_and_keeps_suffix_on_close_line() {
        let doc = Doc::group(
            "typing_extensions.Annotated[",
            vec![
                Doc::group(
                    "typing.Optional[",
                    vec![Doc::atom("TypesObjectWithOptionalField")],
                    "]",
                ),
                Doc::atom("FieldMetadata(alias=\"NestedObject\")"),
            ],
            "]",
        );
        assert_eq!(
            layout("    nested_object: ", &doc, " = None", 4),
            "    nested_object: typing_extensions.Annotated[\n        \
             typing.Optional[TypesObjectWithOptionalField], FieldMetadata(alias=\"NestedObject\")\n    ] = None"
        );
    }

    #[test]
    fn unsplittable_atom_is_left_long() {
        let doc = Doc::atom("x".repeat(200));
        assert_eq!(layout("", &doc, "", 0), "x".repeat(200));
    }
}
