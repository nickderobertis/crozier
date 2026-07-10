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
/// trailing `_` appended when it would collide with a reserved word.
#[must_use]
pub fn field_name(wire_name: &str) -> String {
    let snake = to_snake_case(wire_name);
    if is_reserved(&snake) {
        format!("{snake}_")
    } else {
        snake
    }
}

/// Python keywords plus the builtins/soft-keywords Fern reserves for Python SDKs.
/// Names here are suffixed with `_` (their wire name is kept as an alias).
#[must_use]
pub fn is_reserved(name: &str) -> bool {
    const RESERVED: &[&str] = &[
        // Python hard keywords.
        "False", "None", "True", "and", "as", "assert", "async", "await", "break", "class",
        "continue", "def", "del", "elif", "else", "except", "finally", "for", "from", "global",
        "if", "import", "in", "is", "lambda", "nonlocal", "not", "or", "pass", "raise", "return",
        "try", "while", "with", "yield",
        // Soft keywords.
        "match", "case",
        // Reserved builtins / conflicts Fern munges.
        "bool", "bytes", "dict", "float", "int", "list", "long", "map", "object", "set", "str",
        "type", "uuid", "id", "filter", "format", "property", "self",
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
}
