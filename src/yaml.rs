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
    options.budget = Some(budget);
    serde_saphyr::from_str_with_options(text, options).map_err(|error| error.to_string())
}
