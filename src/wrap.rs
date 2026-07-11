//! Building Python type expressions as flat strings.
//!
//! Fern runs `ruff format` (line length 120) over its generated code. crozier
//! defers that wrapping to `ruff` itself (see [`crate::pyfmt`]), so the emitter
//! only needs to build each type expression on a single line — a small [`Doc`]
//! tree assembled here and rendered with [`Doc::flat`]. `ruff format` then splits
//! any overflowing line with the same right-hand-split Fern's output uses.
//!
//! [`LIMIT`] remains for the few files crozier lays out by hand rather than
//! handing to `ruff` — the lazy-loader `__init__.py` aggregators, whose leading
//! blank lines a formatter cannot reproduce (see [`crate::emit`]).

/// ruff's configured line length for Fern's output. Used by the hand-laid-out
/// aggregator files, which are not passed through `ruff format`.
pub const LIMIT: usize = 120;

/// A renderable type expression: either an atomic token, or a bracketed group
/// (`open` … comma-separated `items` … `close`). Rendered on one line by
/// [`Doc::flat`]; `ruff format` handles any wrapping downstream.
#[derive(Debug, Clone)]
pub enum Doc {
    /// A token rendered verbatim (e.g. `str`, a class name, a `FieldMetadata(...)`
    /// call, a quoted literal).
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

    /// The single-line rendering. `ruff format` re-wraps the result if it exceeds
    /// the line length.
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

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn flat_renders_nested_groups_on_one_line() {
        let doc = Doc::group(
            "typing.Union[",
            vec![
                Doc::group(
                    "typing.Literal[",
                    vec![Doc::atom("\"a\""), Doc::atom("\"b\"")],
                    "]",
                ),
                Doc::atom("typing.Any"),
            ],
            "]",
        );
        assert_eq!(
            doc.flat(),
            "typing.Union[typing.Literal[\"a\", \"b\"], typing.Any]"
        );
    }

    #[test]
    fn flat_atom_is_verbatim() {
        assert_eq!(Doc::atom("dt.datetime").flat(), "dt.datetime");
    }
}
