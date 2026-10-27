//! The parser options shared by typed documents and schema-less reads.

pub(crate) fn from_str<T: serde::de::DeserializeOwned>(text: &str) -> Result<T, String> {
    let mut options = serde_saphyr::Options::default();
    // Corpus property names such as y/n and on are strings, not YAML 1.1 booleans.
    options.strict_booleans = true;
    // Hasura metadata includes a JSON number beyond f64::MAX.
    options.reject_non_finite_typeless_float = false;
    let mut budget = serde_saphyr::Budget::default();
    // GitHub's full document exceeds the default node/event caps. Keep depth
    // and the remaining parser protections at their defaults.
    budget.max_nodes = usize::MAX;
    budget.max_events = usize::MAX;
    // A dereferenced description shares a schema by more than ten aliases per
    // anchor (GitHub's: 4,574 aliases of 412 anchors), which the parser's
    // alias/anchor ratio pre-scan refuses; the replay bound below caps what
    // aliases may expand to, so the ratio adds no protection of its own.
    budget.enforce_alias_anchor_ratio = false;
    options.budget = Some(budget);
    // A dereferenced description (GitHub's Enterprise Server releases) shares
    // each repeated schema by alias, and replays more events than the default
    // million. Bound the replay by the document's own size instead: a real
    // document replays fewer events than it has bytes, while an alias bomb's
    // expansion grows exponentially in its size and is still refused.
    options.alias_limits.max_total_replayed_events = replay_bound(text);
    match serde_saphyr::from_str_with_options(text, options.clone()) {
        Ok(value) => Ok(value),
        // Only a document the strict read refuses is ever re-indented, so a
        // document that already parses reads exactly as it did.
        Err(error) => match reindented(text) {
            Some(repaired) => serde_saphyr::from_str_with_options(&repaired, options)
                .map_err(|error| error.to_string()),
            None => Err(error.to_string()),
        },
    }
}

/// `text` with every under-indented continuation line of a multi-line quoted
/// scalar indented to the scalar's opening quote, or `None` when the parser
/// raises no such refusal (or one this repair cannot locate).
///
/// YAML requires a quoted scalar's continuation lines in block context to sit
/// deeper than the collection holding it; ingef/conquery's document continues
/// `description: "…` at the key's own column. The reader Fern's users generate
/// with folds such a line exactly as a deeper one, and a continuation line's
/// leading white space is never part of the scalar's value, so indenting it
/// reads the value that reader reads. Nothing else is touched: a line opening
/// with a document marker at column 0 (which that reader refuses too) is left
/// for the parser to refuse, as is every other refusal.
pub(crate) fn reindented(text: &str) -> Option<String> {
    let mut repaired: Option<String> = None;
    loop {
        let current = repaired.as_deref().unwrap_or(text);
        let Some(quote) = underindented_scalar(current) else {
            return repaired;
        };
        // A scalar this cannot repair is left for the parser to refuse, with
        // the scalars before it repaired so the refusal names it.
        let Some(padded) = pad_continuations(current, quote) else {
            return repaired;
        };
        repaired = Some(padded);
    }
}

/// The byte offset of the opening quote of the first quoted scalar the parser
/// refuses for a continuation line's indentation, if it refuses one. The
/// parser's own events are read, not the bare scanner's tokens: the parser
/// drives the scanner, and only its refusals are the strict read's.
fn underindented_scalar(text: &str) -> Option<usize> {
    use serde_saphyr::granit_parser::{ErrorKind, Parser};
    let mut parser = Parser::new_from_str(text);
    let mut after_last_event = 0;
    while let Some(next) = parser.next_event() {
        match next {
            Ok((_, span)) => after_last_event = span.end.index(),
            Err(error) if matches!(error.kind(), ErrorKind::InvalidQuotedScalarIndent) => {
                let start = text
                    .char_indices()
                    .nth(after_last_event)
                    .map_or(text.len(), |(byte, _)| byte);
                return opening_quote(text, start);
            }
            Err(_) => return None,
        }
    }
    None
}

/// The first quote at or after `start`, past white space, comments, the
/// indicator a zero-width token marks (`:`, `-`, `?`) and node properties (an
/// anchor or tag the scanner may still hold queued); `None` if anything else
/// comes first.
fn opening_quote(text: &str, start: usize) -> Option<usize> {
    let mut rest = text[start..].char_indices().peekable();
    while let Some((offset, character)) = rest.next() {
        match character {
            '"' | '\'' => return Some(start + offset),
            ' ' | '\t' | '\r' | '\n' | ':' | '-' | '?' => {}
            '#' | '&' | '!' => {
                let ends_at = if character == '#' {
                    |c: char| c == '\n' || c == '\r'
                } else {
                    |c: char| c.is_whitespace()
                };
                while rest.next_if(|(_, c)| !ends_at(*c)).is_some() {}
            }
            _ => return None,
        }
    }
    None
}

/// `text` with each continuation line of the quoted scalar opening at byte
/// `quote` indented to the quote's column where it sits shallower; `None` when
/// the scalar never closes or no line needed it.
fn pad_continuations(text: &str, quote: usize) -> Option<String> {
    let line_start = text[..quote].rfind(['\n', '\r']).map_or(0, |at| at + 1);
    let quote_column = text[line_start..quote].chars().count();
    let delimiter = text[quote..].chars().next()?;
    let bytes = text.as_bytes();
    // (byte offset of a continuation line, spaces it needs)
    let mut pads: Vec<(usize, usize)> = Vec::new();
    let mut at = quote + 1;
    loop {
        let character = text[at..].chars().next()?;
        match character {
            '\\' if delimiter == '"' => {
                let escaped = text[at + 1..].chars().next()?;
                // An escaped line break still opens a continuation line.
                at += 1 + if matches!(escaped, '\n' | '\r') {
                    0
                } else {
                    escaped.len_utf8()
                };
            }
            '\'' if delimiter == '\'' && bytes.get(at + 1) == Some(&b'\'') => at += 2,
            c if c == delimiter => break,
            '\n' | '\r' => {
                at += if text[at..].starts_with("\r\n") { 2 } else { 1 };
                let blanks = text[at..]
                    .find(|c: char| c != ' ' && c != '\t')
                    .unwrap_or(text.len() - at);
                let content = &text[at + blanks..];
                let marker = blanks == 0
                    && (content.starts_with("---") || content.starts_with("..."))
                    && content[3..].chars().next().is_none_or(char::is_whitespace);
                let blank = content.starts_with(['\n', '\r']);
                let closes = content.starts_with(delimiter);
                let column = text[at..at + blanks].chars().count();
                if column < quote_column && !(marker || blank || closes) {
                    pads.push((at, quote_column - column));
                }
                at += blanks;
            }
            other => at += other.len_utf8(),
        }
    }
    if pads.is_empty() {
        return None;
    }
    let mut padded = String::with_capacity(text.len() + pads.iter().map(|(_, n)| n).sum::<usize>());
    let mut copied = 0;
    for (offset, spaces) in pads {
        padded.push_str(&text[copied..offset]);
        padded.extend(std::iter::repeat_n(' ', spaces));
        copied = offset;
    }
    padded.push_str(&text[copied..]);
    Some(padded)
}

/// How many alias-replayed events a document of `text`'s size may produce:
/// one per byte, never below the parser's default million.
fn replay_bound(text: &str) -> usize {
    text.len()
        .max(serde_saphyr::options::AliasLimits::default().max_total_replayed_events)
}

#[cfg(test)]
mod tests {
    use super::*;

    /// A document of 1,100 anchored lists of 100 members, each list replayed
    /// by eleven aliases, beside `padding` unique descriptions of 600 bytes
    /// each.
    fn shared_lists(padding: usize) -> String {
        let members = (0..100)
            .map(|m| m.to_string())
            .collect::<Vec<_>>()
            .join(",");
        let mut text = String::from("shared:\n");
        for list in 0..1_100 {
            text.push_str(&format!("  s{list}: &s{list} [{members}]\n"));
        }
        text.push_str("uses:\n");
        for list in 0..1_100 {
            for _ in 0..11 {
                text.push_str(&format!("  - *s{list}\n"));
            }
        }
        text.push_str("descriptions:\n");
        for index in 0..padding {
            text.push_str(&format!("  d{index}: {}\n", "x".repeat(600)));
        }
        text
    }

    #[test]
    fn a_large_document_replaying_more_than_a_million_events_parses() {
        // About 1.2 million replayed events in a 1.6 MB document, more aliases
        // per anchor than ten, as a dereferenced description shows (GitHub's:
        // 1.8 million events in 9.3 MB; 4,574 aliases of 412 anchors).
        let text = shared_lists(2_000);
        assert!(text.len() > 1_300_000, "{}", text.len());
        let value: serde_json::Value = from_str(&text).unwrap();
        assert_eq!(value["uses"].as_array().unwrap().len(), 12_100);
        assert_eq!(value["uses"][12_099][99], 99);
    }

    #[test]
    fn replaying_more_events_than_the_document_has_bytes_is_refused() {
        // The same replay without the unique content to account for it.
        let text = shared_lists(0);
        assert!(text.len() < 1_000_000, "{}", text.len());
        let error = from_str::<serde_json::Value>(&text).unwrap_err();
        assert!(error.contains("alias replay limit exceeded"), "{error}");
    }

    /// ingef/conquery's shape: a quoted description continued at its key's own
    /// column, which YAML reserves for the next key.
    const AT_KEY_COLUMN: &str = "schemas:\n  Output:\n    description: \"Creates a column.\n    This avoids copies.\"\n    type: object\n";

    #[test]
    fn a_quoted_continuation_at_its_keys_column_reads_as_folded() {
        let value: serde_json::Value = from_str(AT_KEY_COLUMN).unwrap();
        assert_eq!(
            value["schemas"]["Output"],
            serde_json::json!({"description": "Creates a column. This avoids copies.", "type": "object"})
        );
    }

    #[test]
    fn single_quoted_escaped_and_blank_continuations_read_as_folded() {
        let text = "a:\n  b: 'it''s\n  here'\n  c: \"one\\\n  \\ two\n\n  three\"\n  d: [x]\n";
        let value: serde_json::Value = from_str(text).unwrap();
        assert_eq!(
            value["a"],
            serde_json::json!({"b": "it's here", "c": "one two\nthree", "d": ["x"]})
        );
    }

    #[test]
    fn a_continuation_shallower_than_its_key_reads_as_folded() {
        let text = "a:\n  - \"oil\n  wick\"\n  - \"gas\nmantle\"\n";
        let value: serde_json::Value = from_str(text).unwrap();
        assert_eq!(value["a"], serde_json::json!(["oil wick", "gas mantle"]));
        // The parser refuses a top-level key's continuation at column 1 too.
        let top: serde_json::Value = from_str("a: \"one\n two\"\n").unwrap();
        assert_eq!(top, serde_json::json!({"a": "one two"}));
    }

    #[test]
    fn reindented_pads_only_the_refused_lines_to_the_opening_quote() {
        assert_eq!(
            reindented(AT_KEY_COLUMN).as_deref(),
            Some("schemas:\n  Output:\n    description: \"Creates a column.\n                 This avoids copies.\"\n    type: object\n")
        );
        // A closing quote alone at the key's column is valid and left alone.
        let closing = "a:\n  b: \"one\n  two\n  \"\n";
        assert_eq!(
            reindented(closing).as_deref(),
            Some("a:\n  b: \"one\n     two\n  \"\n")
        );
    }

    #[test]
    fn a_valid_document_is_never_reindented() {
        for text in [
            "a:\n  b: \"one\n    two\"\n",
            "a:\n  b: plain\n    continued\n",
            "a:\n  b: \"one\"\n  c: d\n",
        ] {
            assert_eq!(reindented(text), None, "{text:?}");
        }
    }

    #[test]
    fn yaml_the_lenient_reader_refuses_stays_refused() {
        for text in [
            // Never closed.
            "a:\n  b: \"one\n  two\n",
            // A document marker at column 0 inside the scalar.
            "a:\n  b: \"one\n---\n  two\"\n",
            // Content after the closing quote.
            "a:\n  b: \"one\n  two\" three\n  c: d\n",
        ] {
            assert!(from_str::<serde_json::Value>(text).is_err(), "{text:?}");
        }
    }

    #[test]
    fn a_later_unrepairable_scalar_is_the_one_refused() {
        // The first scalar is repaired, so the refusal names the marker's line.
        let text = "a:\n  b: \"one\n  two\"\n  c: \"three\n---\n\"\n";
        let repaired = reindented(text).unwrap();
        assert!(
            repaired.starts_with("a:\n  b: \"one\n     two\"\n"),
            "{repaired:?}"
        );
        let error = from_str::<serde_json::Value>(text).unwrap_err();
        assert!(error.contains("line 5 column 1"), "{error}");
    }

    #[test]
    fn underindented_scalar_finds_the_opening_quote_past_properties() {
        let text = "a:\n  b: &anchor !!str \"one\n  two\"\n";
        assert_eq!(underindented_scalar(text), text.find('"'));
        assert_eq!(underindented_scalar("a:\n  b: \"one\n    two\"\n"), None);
        // Some other refusal is not this repair's.
        assert_eq!(underindented_scalar("a: [\n"), None);
    }

    #[test]
    fn opening_quote_skips_only_separators_comments_and_properties() {
        assert_eq!(opening_quote(": # note\n  'x'", 0), Some(11));
        assert_eq!(opening_quote("- &a !t \"x\"", 0), Some(8));
        assert_eq!(opening_quote(": plain", 0), None);
        assert_eq!(opening_quote(":  ", 0), None);
    }

    #[test]
    fn pad_continuations_needs_a_closed_scalar_with_a_shallow_line() {
        assert_eq!(pad_continuations("b: \"one\ntwo", 3), None);
        assert_eq!(pad_continuations("b: \"one\n    two\"", 3), None);
        assert_eq!(
            pad_continuations("b: \"x\\\"y\nz\"", 3).as_deref(),
            Some("b: \"x\\\"y\n   z\"")
        );
        // A non-ASCII line before the quote counts columns in characters.
        assert_eq!(
            pad_continuations("é: 'a\nb'", 4).as_deref(),
            Some("é: 'a\n   b'")
        );
    }

    #[test]
    fn an_alias_expansion_bomb_is_refused() {
        // Nine levels of ten aliases each: a billion scalars from under a kilobyte.
        let mut text = String::from("l0: &l0 [lol, lol, lol, lol, lol, lol, lol, lol, lol, lol]\n");
        for level in 1..=9 {
            let previous = format!("*l{}", level - 1);
            let members = [previous.as_str(); 10].join(", ");
            text.push_str(&format!("l{level}: &l{level} [{members}]\n"));
        }
        assert!(text.len() < 1_000);
        let error = from_str::<serde_json::Value>(&text).unwrap_err();
        assert!(error.contains("budget breached"), "{error}");
    }
}
