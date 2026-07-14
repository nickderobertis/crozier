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

/// `snake_case` of an identifier. A word that follows one ending in a digit *and*
/// containing a letter (`Cvc2`) is joined without an underscore, matching Fern's
/// module/method names (`CardGeneratedCvc2Create` → `card_generated_cvc2create`,
/// `GeneratedCvc2_for` → `generated_cvc2for`). This join is snake-only — the class
/// name (`to_pascal_case`) keeps `Cvc2Create`. A standalone digit word (`2`, from
/// `2Factor`) does not absorb the next word.
#[must_use]
pub fn to_snake_case(input: &str) -> String {
    let mut out = String::new();
    for word in split_words(input) {
        let after_digit_word = out.ends_with(|p: char| p.is_ascii_digit())
            && out.rsplit('_').next().is_some_and(|w| {
                w.ends_with(|p: char| p.is_ascii_digit())
                    && w.chars().any(|c| c.is_ascii_alphabetic())
            });
        if !out.is_empty() && !after_digit_word {
            out.push('_');
        }
        out.push_str(&word);
    }
    out
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
///
/// Property names that aren't valid identifiers — the bracketed JSON:API / Rails
/// / Stripe convention (`filter[name]`, `page[size]`) most of all — are folded
/// into the `snake_case` the same way Fern does: every non-alphanumeric run is a
/// word boundary, so `filter[name]` → `filter_name` (issue #74). The raw wire
/// name still rides along as the serialization key, since `needs_alias` fires.
#[must_use]
pub fn field_name(wire_name: &str) -> String {
    let snake = to_snake_case(&fold_non_identifier(wire_name));
    if snake.starts_with(|c: char| c.is_ascii_digit()) {
        format!("f_{snake}")
    } else if is_reserved(&snake) {
        format!("{snake}_")
    } else {
        snake
    }
}

/// Replace every character that can't appear in a Python identifier with a space
/// so [`split_words`] treats it as a word boundary. `_`, `-`, `.`, and space are
/// already boundaries there, so a name that was already identifier-legal folds to
/// the exact same words — this only changes names that would otherwise emit
/// illegal Python (`filter[name]` → `filter name`).
fn fold_non_identifier(name: &str) -> String {
    name.chars()
        .map(|c| if c.is_ascii_alphanumeric() { c } else { ' ' })
        .collect()
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

/// The English word for a bare single decimal digit. Fern's enum-name generator
/// spells out a one-character digit word so a leading digit becomes a legal
/// identifier (`0: Active` → `zero_active`); a multi-digit run (`01`) is left
/// alone (Fern rejects the result, crozier keeps it legal via the prefix in
/// [`finalize_enum_ident`]).
fn digit_word(word: &str) -> Option<&'static str> {
    let mut chars = word.chars();
    let (first, rest) = (chars.next()?, chars.next());
    if rest.is_some() {
        return None;
    }
    Some(match first {
        '0' => "zero",
        '1' => "one",
        '2' => "two",
        '3' => "three",
        '4' => "four",
        '5' => "five",
        '6' => "six",
        '7' => "seven",
        '8' => "eight",
        '9' => "nine",
        _ => return None,
    })
}

/// Split an enum wire value into Fern's identifier words: every non-alphanumeric
/// run separates, `camelCase`/`PascalCase` boundaries split, and a bare
/// single-digit word is spelled out (`0` → `zero`). This reproduces Fern's
/// enum-value name generation, whose cased forms drive both the member name and
/// the `visit` parameter (`0: Active` → words `[zero, active]`; `1: InActive` →
/// `[one, in, active]`).
fn enum_words(value: &str) -> Vec<String> {
    let mut spaced = String::new();
    for c in value.chars() {
        if c == '*' {
            // Fern spells a bare `*` wildcard enum value the word "all"
            // (`"*"` → `ALL`); every other non-alphanumeric is a word boundary.
            spaced.push_str(" all ");
        } else if c.is_ascii_alphanumeric() {
            spaced.push(c);
        } else {
            spaced.push(' ');
        }
    }
    split_words(&spaced)
        .into_iter()
        .map(|w| digit_word(&w).map_or(w, str::to_string))
        .collect()
}

/// Coerce a cased enum identifier into a legal, non-empty Python name: a value
/// with no usable characters falls back to `_`, a leading digit (a multi-digit
/// token Fern would reject) is prefixed with `_`, and a reserved word gets the
/// trailing-`_` `safe_name` treatment Fern applies. Shared by the member and
/// `visit`-parameter derivations so both stay valid and mutually consistent.
fn finalize_enum_ident(mut name: String) -> String {
    if name.is_empty() {
        name.push('_');
    }
    if name.starts_with(|c: char| c.is_ascii_digit()) {
        name.insert(0, '_');
    }
    if is_reserved(&name) {
        name.push('_');
    }
    name
}

/// The `SCREAMING_SNAKE` member identifier for an enum wire value, sanitized to
/// a legal Python name (Fern's `screaming_snake_case.safe_name`): `global` →
/// `GLOBAL`, `0: Active` → `ZERO_ACTIVE`.
#[must_use]
pub fn enum_member_name(value: &str) -> String {
    finalize_enum_ident(enum_words(value).join("_").to_ascii_uppercase())
}

/// The `snake_case` `visit` callback parameter for an enum wire value, sanitized
/// to a legal Python name (Fern's `snake_case.safe_name`): `global` → `global_`
/// (keyword), `0: Active` → `zero_active`. The method receiver `self` is escaped
/// the same way (issue #57): the `visit(self, …)` signature would otherwise emit a
/// duplicate `self` argument — grammatically valid Python that passes `ruff format`
/// but fails at import — so a value sanitizing to `self` gets the trailing `_`
/// (`self` → `self_`). `cls` is deliberately *not* escaped: `visit` is an ordinary
/// instance method, so a `cls` parameter is legal and does not shadow the receiver
/// — Fern leaves it alone, and matching Fern is the contract.
#[must_use]
pub fn enum_visit_param(value: &str) -> String {
    let mut name = finalize_enum_ident(enum_words(value).join("_"));
    if name == "self" {
        name.push('_');
    }
    name
}

/// Names Fern suffixes with `_` (keeping the wire name as an alias): Python hard
/// keywords (syntactically un-usable as identifiers) plus the specific builtins
/// observed in Fern's output. The builtin set is deliberately evidence-based —
/// only names confirmed against a Fern fixture belong here, since over-munging a
/// name Fern leaves alone would break the byte-for-byte match. Expand it as new
/// fixtures confirm more.
#[must_use]
pub fn is_reserved(name: &str) -> bool {
    // Builtins/module names Fern munges in *field/type* contexts (confirmed in the
    // exhaustive fixture). Method names are narrower — see `is_reserved_method`.
    const RESERVED_BUILTINS: &[&str] = &["all", "bool", "list", "long", "map", "set", "uuid"];
    PYTHON_KEYWORDS.contains(&name) || RESERVED_BUILTINS.contains(&name)
}

/// Reserved-word check for *derived method* names. Fern safe-names Python keywords
/// and the builtin `all` (a REST "list all" method → `all_`), but — unlike field and
/// type names — leaves other builtins alone: appwrite's derived `list` stays `list`,
/// not `list_`, and `bool`/`set`/… likewise. Evidence-based against the golden corpus
/// (the only `_`-suffixed method names Fern emits are keywords, `all`, and dunders);
/// widen only when a fixture shows Fern suffixing another method name.
#[must_use]
pub fn is_reserved_method(name: &str) -> bool {
    PYTHON_KEYWORDS.contains(&name) || name == "all"
}

/// Python hard keywords — reserved in every naming context.
const PYTHON_KEYWORDS: &[&str] = &[
    "False", "None", "True", "and", "as", "assert", "async", "await", "break", "class", "continue",
    "def", "del", "elif", "else", "except", "finally", "for", "from", "global", "if", "import",
    "in", "is", "lambda", "nonlocal", "not", "or", "pass", "raise", "return", "try", "while",
    "with", "yield",
];

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn method_reserved_set_is_narrower_than_general() {
        // Fern safe-names `all` and keywords as method names (apideck's `all_`,
        // `import_`) but leaves other builtins alone (appwrite's `list`, not `list_`).
        assert!(is_reserved_method("all"));
        assert!(is_reserved_method("import"));
        assert!(!is_reserved_method("list"));
        assert!(!is_reserved_method("bool"));
        // The general set still guards field/type names (confirmed in the exhaustive
        // fixture), so `list`/`bool` stay reserved there.
        assert!(is_reserved("list"));
        assert!(is_reserved("bool"));
        assert!(is_reserved("all"));
    }

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
    fn bracketed_property_names_fold_to_snake_identifiers() {
        // Issue #74: JSON:API / Rails / Stripe bracketed params aren't valid
        // Python identifiers; Fern folds them to snake_case and keeps the raw
        // name as the wire key (which `needs_alias` handles).
        assert_eq!(field_name("filter[name]"), "filter_name");
        assert_eq!(field_name("filter[color]"), "filter_color");
        assert_eq!(field_name("page[size]"), "page_size");
        assert_eq!(field_name("hours[day]"), "hours_day");
        // Deeper nesting collapses each bracket run to a single boundary; no
        // trailing underscore from the closing bracket.
        assert_eq!(field_name("filter[user][name]"), "filter_user_name");
        // A leading-digit result still gets the `f_` guard after folding.
        assert_eq!(field_name("[2fa]enabled"), "f_2fa_enabled");
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
    fn enum_names_match_ferns_sanitized_identifiers() {
        // Keyword value: member is safe (upper-cased), the visit param is escaped.
        assert_eq!(enum_member_name("global"), "GLOBAL");
        assert_eq!(enum_visit_param("global"), "global_");
        assert_eq!(enum_member_name("practice"), "PRACTICE");
        assert_eq!(enum_visit_param("practice"), "practice");
        // Punctuation + a leading single digit: the digit is spelled out and the
        // `:`/space become word boundaries (Fern: `0: Active` → `ZERO_ACTIVE`).
        assert_eq!(enum_member_name("0: Active"), "ZERO_ACTIVE");
        assert_eq!(enum_visit_param("0: Active"), "zero_active");
        assert_eq!(enum_member_name("1: InActive"), "ONE_IN_ACTIVE");
        assert_eq!(enum_visit_param("1: InActive"), "one_in_active");
    }

    #[test]
    fn enum_receiver_value_escapes_the_visit_param() {
        // Issue #57: a value that sanitizes to the `visit(self, …)` receiver name
        // `self` would emit a duplicate `self` argument (invalid at import though
        // `ruff` accepts it); the visit param is escaped like a keyword, while the
        // member upper-cases to `SELF` (never a receiver collision) and is untouched.
        assert_eq!(enum_member_name("self"), "SELF");
        assert_eq!(enum_visit_param("self"), "self_");
        // Casing that sanitizes to `self` is escaped too.
        assert_eq!(enum_visit_param("Self"), "self_");
        // `cls` is NOT escaped: `visit` is an instance method, so a `cls` parameter
        // is legal and does not shadow the receiver — Fern leaves it alone.
        assert_eq!(enum_member_name("cls"), "CLS");
        assert_eq!(enum_visit_param("cls"), "cls");
    }

    #[test]
    fn enum_names_stay_legal_where_fern_would_error() {
        // A multi-digit leading token is not spelled out (Fern rejects it); crozier
        // prefixes `_` so the identifier is still legal Python.
        assert_eq!(enum_member_name("_01_00_AM"), "_01_00_AM");
        assert_eq!(enum_visit_param("_01_00_AM"), "_01_00_am");
        assert_eq!(enum_member_name("2fa"), "_2FA");
        assert_eq!(enum_visit_param("2fa"), "_2fa");
        // A value with no identifier characters still yields a legal name.
        assert_eq!(enum_member_name("!!!"), "_");
        assert_eq!(enum_visit_param("!!!"), "_");
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
