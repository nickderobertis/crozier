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
    serde_saphyr::from_str_with_options(text, options).map_err(|error| error.to_string())
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
