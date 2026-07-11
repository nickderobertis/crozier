//! Name transforms shared by the IR builder and the emitter.
//!
//! Byte-exact output depends on these matching Fern's choices: `snake_case` field
//! and module names, `PascalCase` class names, and appending `_` to a name that
//! collides with a Python keyword or a reserved builtin (Fern then preserves the
//! original wire name as an alias). The reserved set is deliberately explicit so
//! a future mismatch is a one-line change here.

/// Split an identifier into lowercase words, handling `camelCase`, `PascalCase`,
/// `snake_case`, `kebab-case`, and `ACRONYMCase` boundaries.
#[must_use]
pub fn split_words(input: &str) -> Vec<String> {
    let mut words: Vec<String> = Vec::new();
    let mut current = String::new();
    let chars: Vec<char> = input.chars().collect();

    for idx in 0..chars.len() {
        let c = chars[idx];
        if c == '_' || c == '-' || c == ' ' || c == '.' {
            if !current.is_empty() {
                words.push(std::mem::take(&mut current));
            }
            continue;
        }

        let prev = if idx > 0 { Some(chars[idx - 1]) } else { None };
        let next = chars.get(idx + 1).copied();

        // Boundary before an uppercase letter that begins a new word:
        //  - lower/digit -> Upper  (fooBar -> foo|Bar)
        //  - Upper -> Upper followed by lower  (HTTPServer -> HTTP|Server)
        let boundary = c.is_ascii_uppercase()
            && !current.is_empty()
            && (prev.is_some_and(|p| p.is_ascii_lowercase() || p.is_ascii_digit())
                || (prev.is_some_and(|p| p.is_ascii_uppercase())
                    && next.is_some_and(|n| n.is_ascii_lowercase())));

        if boundary {
            words.push(std::mem::take(&mut current));
        }
        current.push(c.to_ascii_lowercase());
    }
    if !current.is_empty() {
        words.push(current);
    }
    words
}

/// `snake_case` of an identifier.
#[must_use]
pub fn to_snake_case(input: &str) -> String {
    split_words(input).join("_")
}

/// `PascalCase` of an identifier.
#[must_use]
pub fn to_pascal_case(input: &str) -> String {
    split_words(input)
        .into_iter()
        .map(|w| {
            let mut chars = w.chars();
            match chars.next() {
                Some(first) => first.to_ascii_uppercase().to_string() + chars.as_str(),
                None => String::new(),
            }
        })
        .collect()
}

/// The class name for a named schema.
#[must_use]
pub fn class_name(schema_key: &str) -> String {
    to_pascal_case(schema_key)
}

/// The module (file stem) name for a generated type.
#[must_use]
pub fn module_name(class_name: &str) -> String {
    to_snake_case(class_name)
}

/// The Python field identifier for a wire property name: `snake_case`, with a
/// trailing `_` appended when it would collide with a reserved word, or an `f_`
/// prefix when it would otherwise start with a digit (an illegal identifier).
/// Both transforms make [`crate::ir::Field::needs_alias`] fire, so the wire name
/// is preserved as a `FieldMetadata` alias — matching Fern (`2fa_enabled` →
/// `f_2fa_enabled`).
#[must_use]
pub fn field_name(wire_name: &str) -> String {
    let snake = to_snake_case(wire_name);
    if snake.starts_with(|c: char| c.is_ascii_digit()) {
        format!("f_{snake}")
    } else if is_reserved(&snake) {
        format!("{snake}_")
    } else {
        snake
    }
}

/// Coerce a derived name into a legal Python identifier: any character that is
/// not `[A-Za-z0-9_]` becomes `_`, and a leading digit is prefixed with `_`.
/// Applied to operationId-derived module/method names so a hyphen or space in an
/// `operationId` (`get-all-widgets`, `verify code`) yields valid Python rather
/// than source that fails to parse. Names already valid pass through unchanged,
/// so this never perturbs the byte-matched fixtures.
#[must_use]
pub fn sanitize_identifier(name: &str) -> String {
    let mut out: String = name
        .chars()
        .map(|c| {
            if c.is_ascii_alphanumeric() || c == '_' {
                c
            } else {
                '_'
            }
        })
        .collect();
    if out.starts_with(|c: char| c.is_ascii_digit()) {
        out.insert(0, '_');
    }
    out
}

/// Names Fern suffixes with `_` (keeping the wire name as an alias): Python hard
/// keywords (syntactically un-usable as identifiers) plus the specific builtins
/// observed in Fern's output. The builtin set is deliberately evidence-based —
/// only names confirmed against a Fern fixture belong here, since over-munging a
/// name Fern leaves alone would break the byte-for-byte match. Expand it as new
/// fixtures confirm more.
#[must_use]
pub fn is_reserved(name: &str) -> bool {
    const RESERVED: &[&str] = &[
        // Python hard keywords.
        "False", "None", "True", "and", "as", "assert", "async", "await", "break", "class",
        "continue", "def", "del", "elif", "else", "except", "finally", "for", "from", "global",
        "if", "import", "in", "is", "lambda", "nonlocal", "not", "or", "pass", "raise", "return",
        "try", "while", "with", "yield",
        // Builtins/module names Fern munges (confirmed in the exhaustive fixture).
        "bool", "list", "long", "map", "set", "uuid",
    ];
    RESERVED.contains(&name)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn snake_case_variants() {
        assert_eq!(to_snake_case("NestedUser"), "nested_user");
        assert_eq!(to_snake_case("SearchResponse"), "search_response");
        assert_eq!(to_snake_case("name"), "name");
        assert_eq!(to_snake_case("customFields"), "custom_fields");
        assert_eq!(to_snake_case("custom_fields"), "custom_fields");
        assert_eq!(to_snake_case("HTTPServer"), "http_server");
        assert_eq!(to_snake_case("kebab-case-name"), "kebab_case_name");
    }

    #[test]
    fn pascal_case_is_idempotent_on_pascal() {
        assert_eq!(to_pascal_case("NestedUser"), "NestedUser");
        assert_eq!(to_pascal_case("nested_user"), "NestedUser");
        assert_eq!(to_pascal_case("search_response"), "SearchResponse");
    }

    #[test]
    fn module_name_snakes_class() {
        assert_eq!(module_name("NestedUser"), "nested_user");
    }

    #[test]
    fn reserved_fields_get_suffixed() {
        assert_eq!(field_name("list"), "list_");
        assert_eq!(field_name("bool"), "bool_");
        assert_eq!(field_name("uuid"), "uuid_");
        assert_eq!(field_name("name"), "name");
        assert_eq!(field_name("tags"), "tags");
    }

    #[test]
    fn digit_leading_fields_get_f_prefix() {
        // Fern renames a leading-digit property to `f_<name>` and aliases it.
        assert_eq!(field_name("2fa_enabled"), "f_2fa_enabled");
        assert_eq!(field_name("3d"), "f_3d");
        // A hyphenated, digit-leading name still snakes then prefixes.
        assert_eq!(field_name("2-factor"), "f_2_factor");
        // Non-digit-leading names are untouched.
        assert_eq!(field_name("v2"), "v2");
    }

    #[test]
    fn sanitize_identifier_coerces_illegal_chars() {
        assert_eq!(sanitize_identifier("get-all-widgets"), "get_all_widgets");
        assert_eq!(sanitize_identifier("verify code"), "verify_code");
        assert_eq!(sanitize_identifier("2fa"), "_2fa");
        // Already-legal identifiers pass through unchanged.
        assert_eq!(sanitize_identifier("postwithnoauth"), "postwithnoauth");
        assert_eq!(
            sanitize_identifier("endpoints_container"),
            "endpoints_container"
        );
    }
}
