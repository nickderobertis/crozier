//! String-safe removal of Python `#` comments.
//!
//! Fern and crozier necessarily disagree on one thing: the comment naming which
//! tool generated the file. To compare the *code*, both sides pass through
//! [`strip_python_comments`] before the byte comparison — so header wording and
//! inline `# type: ignore` notes never affect the match.
//!
//! The same function produces the committed fixtures (via the `internal-strip`
//! subcommand) and normalizes crozier's fresh output in the e2e, so "comments
//! removed" has one definition and the two cannot drift.
//!
//! Removal is string-aware: a `#` inside a string or docstring (including
//! multi-line triple-quoted strings) is left alone. After removing comment text,
//! trailing whitespace is trimmed from each *code* line so a stripped inline
//! comment leaves nothing dangling; lines that end inside a string are preserved
//! verbatim. A file's final-newline state is preserved.

/// The kind of string literal currently open during the scan.
#[derive(Clone, Copy, PartialEq, Eq)]
enum Quote {
    Single,
    Double,
    TripleSingle,
    TripleDouble,
}

/// Remove every Python `#` comment from `source`, leaving strings and docstrings
/// intact and trimming the trailing whitespace a removed comment would leave.
#[must_use]
pub fn strip_python_comments(source: &str) -> String {
    let chars: Vec<char> = source.chars().collect();
    let n = chars.len();

    let mut lines: Vec<String> = Vec::new();
    let mut current = String::new();
    let mut in_string: Option<Quote> = None;
    let mut escaped = false;

    let mut i = 0;
    while i < n {
        let c = chars[i];

        // A newline ends the current line regardless of string state, so the
        // file's line structure is preserved. Trim only outside strings: a
        // comment can only have been stripped from a code line, and trimming a
        // line that ends mid-string could alter string content.
        if c == '\n' {
            lines.push(finish_line(&current, in_string.is_some()));
            current.clear();
            escaped = false;
            i += 1;
            continue;
        }

        match in_string {
            None => {
                if c == '#' {
                    // Comment: drop everything up to (not including) the newline.
                    while i < n && chars[i] != '\n' {
                        i += 1;
                    }
                    continue;
                }
                if c == '"' || c == '\'' {
                    if starts_triple(&chars, i, c) {
                        in_string = Some(if c == '"' {
                            Quote::TripleDouble
                        } else {
                            Quote::TripleSingle
                        });
                        current.push(c);
                        current.push(c);
                        current.push(c);
                        i += 3;
                        continue;
                    }
                    in_string = Some(if c == '"' {
                        Quote::Double
                    } else {
                        Quote::Single
                    });
                }
                current.push(c);
                i += 1;
            }
            Some(quote) => {
                if escaped {
                    current.push(c);
                    escaped = false;
                    i += 1;
                    continue;
                }
                if c == '\\' {
                    current.push(c);
                    escaped = true;
                    i += 1;
                    continue;
                }
                match quote {
                    Quote::Single | Quote::Double => {
                        let closer = if quote == Quote::Single { '\'' } else { '"' };
                        current.push(c);
                        if c == closer {
                            in_string = None;
                        }
                        i += 1;
                    }
                    Quote::TripleSingle | Quote::TripleDouble => {
                        let closer = if quote == Quote::TripleSingle {
                            '\''
                        } else {
                            '"'
                        };
                        if c == closer && starts_triple(&chars, i, closer) {
                            current.push(closer);
                            current.push(closer);
                            current.push(closer);
                            in_string = None;
                            i += 3;
                        } else {
                            current.push(c);
                            i += 1;
                        }
                    }
                }
            }
        }
    }
    // Content after the final newline (empty if the file ended with one). Pushing
    // it unconditionally makes `join` reproduce the input's trailing-newline
    // state: a trailing "" element re-adds the final `\n`, its absence omits it.
    lines.push(finish_line(&current, in_string.is_some()));
    lines.join("\n")
}

/// Trim a completed line's trailing spaces/tabs unless it ended inside a string.
fn finish_line(line: &str, inside_string: bool) -> String {
    if inside_string {
        line.to_string()
    } else {
        line.trim_end_matches([' ', '\t']).to_string()
    }
}

/// Does a run of three identical quote characters begin at `i`?
fn starts_triple(chars: &[char], i: usize, q: char) -> bool {
    i + 2 < chars.len() && chars[i] == q && chars[i + 1] == q && chars[i + 2] == q
}

#[cfg(test)]
mod tests {
    use super::strip_python_comments;

    #[test]
    fn removes_full_line_comment_keeping_blank_line() {
        assert_eq!(strip_python_comments("# header\n\nx = 1\n"), "\n\nx = 1\n");
    }

    #[test]
    fn removes_inline_comment_and_trailing_space() {
        assert_eq!(strip_python_comments("x = 1  # type: ignore\n"), "x = 1\n");
    }

    #[test]
    fn keeps_hash_inside_single_quoted_string() {
        assert_eq!(strip_python_comments("a = \"#nope\"\n"), "a = \"#nope\"\n");
    }

    #[test]
    fn keeps_hash_inside_docstring() {
        let src = "def f():\n    \"\"\"\n    a # b\n    \"\"\"\n    return 1\n";
        assert_eq!(strip_python_comments(src), src);
    }

    #[test]
    fn strips_comment_after_string_on_same_line() {
        assert_eq!(strip_python_comments("a = \"x\"  # c\n"), "a = \"x\"\n");
    }

    #[test]
    fn preserves_missing_trailing_newline() {
        assert_eq!(strip_python_comments("x = 1"), "x = 1");
        assert_eq!(strip_python_comments("x = 1  # c"), "x = 1");
    }

    #[test]
    fn preserves_utf8_in_strings() {
        assert_eq!(
            strip_python_comments("s = \"café # ☕\"  # c\n"),
            "s = \"café # ☕\"\n"
        );
    }

    #[test]
    fn empty_input_stays_empty() {
        assert_eq!(strip_python_comments(""), "");
        assert_eq!(strip_python_comments("\n"), "\n");
    }

    #[test]
    fn handles_escaped_quote_in_string() {
        assert_eq!(
            strip_python_comments("a = \"he said \\\"hi\\\"\"  # c\n"),
            "a = \"he said \\\"hi\\\"\"\n"
        );
    }
}
