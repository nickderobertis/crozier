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

/// Convert free-form prose to a legal snake-case Python identifier. Unlike
/// [`to_snake_case`], this treats every punctuation run as a word boundary, so an
/// operation summary such as `The /content endpoint` becomes
/// `the_content_endpoint` rather than retaining the slash.
#[must_use]
pub fn prose_identifier(input: &str) -> String {
    let folded: String = input
        .chars()
        .filter_map(|c| match c {
            // Possessives are contractions, not word boundaries: Fern derives
            // `seller's feedback` as `sellers_feedback`.
            '\'' | '\u{2019}' => None,
            c if c.is_ascii_alphanumeric() => Some(c),
            _ => Some(' '),
        })
        .collect();
    sanitize_identifier(&collapse_digit_boundaries(&to_snake_case(&folded)))
}

/// `PascalCase` of an identifier.
#[must_use]
pub fn to_pascal_case(input: &str) -> String {
    split_words(input)
        .into_iter()
        .map(|w| {
            let mut out = String::with_capacity(w.len());
            let mut after_digit = false;
            for (index, c) in w.chars().enumerate() {
                if index == 0 || after_digit && c.is_ascii_alphabetic() {
                    out.push(c.to_ascii_uppercase());
                } else {
                    out.push(c);
                }
                after_digit = c.is_ascii_digit();
            }
            out
        })
        .collect()
}

/// The class name for a named schema.
#[must_use]
pub fn class_name(schema_key: &str) -> String {
    let pascal = to_pascal_case(schema_key);
    let expanded = pascal
        .chars()
        .next()
        .and_then(|digit| digit.to_digit(10))
        .map_or(pascal.clone(), |digit| {
            let word = [
                "Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
            ][digit as usize];
            format!("{word}{}", &pascal[1..])
        });
    sanitize_identifier(&expanded)
}

/// The module (file stem) name for a generated type.
#[must_use]
pub fn module_name(class_name: &str) -> String {
    let name = to_snake_case(class_name);
    if name.starts_with(|c: char| c.is_ascii_digit()) {
        format!("_{name}")
    } else if is_reserved(&name) {
        format!("{name}_")
    } else {
        name
    }
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
    let snake = field_snake_case(wire_name);
    if snake.starts_with(|c: char| c.is_ascii_digit()) {
        format!("f_{snake}")
    } else if is_reserved(&snake) {
        format!("{snake}_")
    } else {
        snake
    }
}

/// Python argument name for an inlined request-body property. Fern prefixes a
/// digit-leading body argument with `_` (distinct from model fields' `f_`).
#[must_use]
pub fn request_field_name(wire_name: &str) -> String {
    let snake = field_snake_case(wire_name);
    if snake.starts_with(|c: char| c.is_ascii_digit()) {
        format!("_{snake}")
    } else {
        field_name(wire_name)
    }
}

/// The `snake_case` stem shared by [`field_name`] and [`request_field_name`].
///
/// A whitespace run is a *hard* word boundary in Fern's property casing: the
/// digit-boundary collapse below joins segments freely inside one whitespace-
/// delimited chunk (`user_fields[1]` → `user_fields1`, `PF 17,5%` → `pf_175`)
/// but never reaches across a space, so `EAN 1` stays `ean_1` and `PF 17% ALC`
/// stays `pf_17_alc`. Chunking first is what keeps the two apart; every name
/// without whitespace is a single chunk and folds exactly as before.
fn field_snake_case(wire_name: &str) -> String {
    wire_name
        .split_whitespace()
        .map(|chunk| collapse_field_digit_boundaries(&to_snake_case(&fold_non_identifier(chunk))))
        .filter(|chunk| !chunk.is_empty())
        .collect::<Vec<String>>()
        .join("_")
}

/// Fern joins numeric field-name segments to their neighbors (`day_0_end_time` →
/// `day0end_time`, `user_fields[1]` → `user_fields1`) but preserves a boundary
/// after an initial digit (`2Factor` → `2_factor`). Serialization still uses the
/// original wire name through field aliases.
fn collapse_field_digit_boundaries(name: &str) -> String {
    let chars: Vec<char> = name.chars().collect();
    chars
        .iter()
        .enumerate()
        .filter_map(|(index, &ch)| {
            if ch == '_'
                && (index.checked_sub(1).is_some_and(|i| {
                    chars[i].is_ascii_digit() && digit_suffix_absorbs_following(&chars, i)
                }) || chars.get(index + 1).is_some_and(char::is_ascii_digit))
            {
                None
            } else {
                Some(ch)
            }
        })
        .collect()
}

fn digit_suffix_absorbs_following(chars: &[char], digit_index: usize) -> bool {
    let mut digit_start = digit_index;
    while digit_start > 0 && chars[digit_start - 1].is_ascii_digit() {
        digit_start -= 1;
    }
    (digit_start > 0 && chars[digit_start - 1] == '_')
        || chars[..digit_start]
            .iter()
            .rev()
            .take_while(|&&candidate| candidate != '_')
            .any(|candidate| candidate.is_ascii_alphabetic())
}

fn collapse_digit_boundaries(name: &str) -> String {
    let chars: Vec<char> = name.chars().collect();
    chars
        .iter()
        .enumerate()
        .filter_map(|(index, &ch)| {
            if ch == '_'
                && (index
                    .checked_sub(1)
                    .is_some_and(|i| chars[i].is_ascii_digit())
                    || chars.get(index + 1).is_some_and(char::is_ascii_digit))
            {
                None
            } else {
                Some(ch)
            }
        })
        .collect()
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

/// Smart-case an enum wire value into Fern's identifier: every non-alphanumeric
/// run separates, `camelCase`/`PascalCase` boundaries split, a leading canonical
/// number is spelled out (`1200 bps` → `one_thousand_two_hundred_bps`), and word
/// boundaries touching a numeric token collapse (`DB-25` → `db25`). UUID-shaped
/// values use Fern's separate quirk in [`uuid_enum_identifier`].
fn enum_words(value: &str) -> String {
    if value.is_empty() {
        return "empty".to_string();
    }
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
    let mut words = split_words(&spaced);
    let has_leading_zero_identifier_segment = value.contains('_')
        && words.iter().any(|word| {
            word.len() > 1
                && word.starts_with('0')
                && word.bytes().all(|byte| byte.is_ascii_digit())
        });
    if let Some(first) = words.first_mut() {
        let digits = first.bytes().take_while(u8::is_ascii_digit).count();
        if digits > 0 {
            let suffix = first[digits..].to_string();
            if let Some(number) = numeric_enum_identifier(&first[..digits]) {
                *first = if suffix.is_empty() {
                    number
                } else {
                    format!("{number}_{suffix}")
                };
            }
        }
    }
    // Fern joins letter-only connector runs in hardware-style values, but keeps
    // ordinary lowercase words separated (`a-b` remains `A_B`). Digits are the
    // signal for the former; all-uppercase wire values take the same path for
    // connector spellings such as `P+N+E` and `E/F`.
    let join_single_letters = value.bytes().any(|byte| byte.is_ascii_digit())
        || value
            .bytes()
            .filter(|byte| byte.is_ascii_alphabetic())
            .all(|byte| byte.is_ascii_uppercase());
    let mut merged_words: Vec<String> = Vec::with_capacity(words.len());
    let mut single_letter_run = false;
    for word in words {
        let is_single_letter =
            word.len() == 1 && word.bytes().all(|byte| byte.is_ascii_alphabetic());
        if join_single_letters && is_single_letter && single_letter_run {
            merged_words
                .last_mut()
                .expect("a single-letter run has a previous word")
                .push_str(&word);
        } else {
            merged_words.push(word);
        }
        single_letter_run = is_single_letter;
    }
    let mut words = merged_words;
    let mut index = 1usize;
    while index < words.len() {
        let previous = &words[index - 1];
        let current = &words[index];
        let current_is_short_letter_run =
            current.len() <= 2 && current.bytes().all(|byte| byte.is_ascii_alphabetic());
        let previous_is_numeric_letter =
            previous
                .as_bytes()
                .split_last()
                .is_some_and(|(last, prefix)| {
                    last.is_ascii_alphabetic()
                        && !prefix.is_empty()
                        && prefix.iter().all(u8::is_ascii_digit)
                });
        let previous_is_single_letter =
            previous.len() == 1 && previous.bytes().all(|byte| byte.is_ascii_alphabetic());
        let current_is_letter_digits =
            current
                .as_bytes()
                .split_first()
                .is_some_and(|(first, rest)| {
                    first.is_ascii_alphabetic()
                        && !rest.is_empty()
                        && rest.iter().all(u8::is_ascii_digit)
                });
        if current_is_short_letter_run && previous_is_numeric_letter
            || previous_is_single_letter && current_is_letter_digits
        {
            let current = words.remove(index);
            words[index - 1].push_str(&current);
        } else {
            index += 1;
        }
    }
    let identifier = words.join("_");
    if has_leading_zero_identifier_segment {
        // Fern rejects this shape; keep Crozier's existing legal fallback stable.
        identifier
    } else {
        collapse_digit_boundaries(&identifier)
    }
}

fn enum_identifier(value: &str) -> String {
    let value = &deburr(value);
    if is_uuid(value) {
        uuid_enum_identifier(value)
    } else {
        enum_words(value)
    }
}

/// Fold Latin accents to their base ASCII letters, the way Fern's enum-name
/// casing does. This is the half of Fern's naming asymmetry that *keeps* the
/// letter: the same accented word yields the member `SUBSTANCIA` from
/// `SUBSTÂNCIA` while the property path drops the accent as a separator
/// (`subst_ncia`), which is why only this path deburrs. Golden-confirmed for
/// `Â`, `Ã`, `Ç`, `Ê`, `É` and `Ó` (`med-anvisa-price`); the rest of the table
/// is the rest of Latin-1 Supplement and Latin Extended-A, folded consistently
/// so a neighbouring accent cannot behave differently from a measured one.
fn deburr(value: &str) -> String {
    let mut folded = String::with_capacity(value.len());
    for character in value.chars() {
        match deburr_letter(character) {
            Some(ascii) => folded.push_str(ascii),
            None => folded.push(character),
        }
    }
    folded
}

/// The ASCII spelling of one accented Latin letter, or `None` when the character
/// is outside the folded range.
fn deburr_letter(character: char) -> Option<&'static str> {
    DEBURRED_LATIN
        .binary_search_by(|(candidate, _)| candidate.cmp(&character))
        .ok()
        .map(|index| DEBURRED_LATIN[index].1)
}

/// Latin-1 Supplement and Latin Extended-A letters paired with the ASCII they
/// fold to, sorted by code point so [`deburr_letter`] can binary-search it.
/// `the_latin_folding_table_is_sorted_and_spans_both_blocks` pins both invariants.
const DEBURRED_LATIN: &[(char, &str)] = &[
    ('À', "A"),
    ('Á', "A"),
    ('Â', "A"),
    ('Ã', "A"),
    ('Ä', "A"),
    ('Å', "A"),
    ('Æ', "Ae"),
    ('Ç', "C"),
    ('È', "E"),
    ('É', "E"),
    ('Ê', "E"),
    ('Ë', "E"),
    ('Ì', "I"),
    ('Í', "I"),
    ('Î', "I"),
    ('Ï', "I"),
    ('Ð', "D"),
    ('Ñ', "N"),
    ('Ò', "O"),
    ('Ó', "O"),
    ('Ô', "O"),
    ('Õ', "O"),
    ('Ö', "O"),
    ('Ø', "O"),
    ('Ù', "U"),
    ('Ú', "U"),
    ('Û', "U"),
    ('Ü', "U"),
    ('Ý', "Y"),
    ('Þ', "Th"),
    ('ß', "ss"),
    ('à', "a"),
    ('á', "a"),
    ('â', "a"),
    ('ã', "a"),
    ('ä', "a"),
    ('å', "a"),
    ('æ', "ae"),
    ('ç', "c"),
    ('è', "e"),
    ('é', "e"),
    ('ê', "e"),
    ('ë', "e"),
    ('ì', "i"),
    ('í', "i"),
    ('î', "i"),
    ('ï', "i"),
    ('ð', "d"),
    ('ñ', "n"),
    ('ò', "o"),
    ('ó', "o"),
    ('ô', "o"),
    ('õ', "o"),
    ('ö', "o"),
    ('ø', "o"),
    ('ù', "u"),
    ('ú', "u"),
    ('û', "u"),
    ('ü', "u"),
    ('ý', "y"),
    ('þ', "th"),
    ('ÿ', "y"),
    ('Ā', "A"),
    ('ā', "a"),
    ('Ă', "A"),
    ('ă', "a"),
    ('Ą', "A"),
    ('ą', "a"),
    ('Ć', "C"),
    ('ć', "c"),
    ('Ĉ', "C"),
    ('ĉ', "c"),
    ('Ċ', "C"),
    ('ċ', "c"),
    ('Č', "C"),
    ('č', "c"),
    ('Ď', "D"),
    ('ď', "d"),
    ('Đ', "D"),
    ('đ', "d"),
    ('Ē', "E"),
    ('ē', "e"),
    ('Ĕ', "E"),
    ('ĕ', "e"),
    ('Ė', "E"),
    ('ė', "e"),
    ('Ę', "E"),
    ('ę', "e"),
    ('Ě', "E"),
    ('ě', "e"),
    ('Ĝ', "G"),
    ('ĝ', "g"),
    ('Ğ', "G"),
    ('ğ', "g"),
    ('Ġ', "G"),
    ('ġ', "g"),
    ('Ģ', "G"),
    ('ģ', "g"),
    ('Ĥ', "H"),
    ('ĥ', "h"),
    ('Ħ', "H"),
    ('ħ', "h"),
    ('Ĩ', "I"),
    ('ĩ', "i"),
    ('Ī', "I"),
    ('ī', "i"),
    ('Ĭ', "I"),
    ('ĭ', "i"),
    ('Į', "I"),
    ('į', "i"),
    ('İ', "I"),
    ('ı', "i"),
    ('Ĳ', "IJ"),
    ('ĳ', "ij"),
    ('Ĵ', "J"),
    ('ĵ', "j"),
    ('Ķ', "K"),
    ('ķ', "k"),
    ('ĸ', "k"),
    ('Ĺ', "L"),
    ('ĺ', "l"),
    ('Ļ', "L"),
    ('ļ', "l"),
    ('Ľ', "L"),
    ('ľ', "l"),
    ('Ŀ', "L"),
    ('ŀ', "l"),
    ('Ł', "L"),
    ('ł', "l"),
    ('Ń', "N"),
    ('ń', "n"),
    ('Ņ', "N"),
    ('ņ', "n"),
    ('Ň', "N"),
    ('ň', "n"),
    ('ŉ', "'n"),
    ('Ŋ', "N"),
    ('ŋ', "n"),
    ('Ō', "O"),
    ('ō', "o"),
    ('Ŏ', "O"),
    ('ŏ', "o"),
    ('Ő', "O"),
    ('ő', "o"),
    ('Œ', "Oe"),
    ('œ', "oe"),
    ('Ŕ', "R"),
    ('ŕ', "r"),
    ('Ŗ', "R"),
    ('ŗ', "r"),
    ('Ř', "R"),
    ('ř', "r"),
    ('Ś', "S"),
    ('ś', "s"),
    ('Ŝ', "S"),
    ('ŝ', "s"),
    ('Ş', "S"),
    ('ş', "s"),
    ('Š', "S"),
    ('š', "s"),
    ('Ţ', "T"),
    ('ţ', "t"),
    ('Ť', "T"),
    ('ť', "t"),
    ('Ŧ', "T"),
    ('ŧ', "t"),
    ('Ũ', "U"),
    ('ũ', "u"),
    ('Ū', "U"),
    ('ū', "u"),
    ('Ŭ', "U"),
    ('ŭ', "u"),
    ('Ů', "U"),
    ('ů', "u"),
    ('Ű', "U"),
    ('ű', "u"),
    ('Ų', "U"),
    ('ų', "u"),
    ('Ŵ', "W"),
    ('ŵ', "w"),
    ('Ŷ', "Y"),
    ('ŷ', "y"),
    ('Ÿ', "Y"),
    ('Ź', "Z"),
    ('ź', "z"),
    ('Ż', "Z"),
    ('ż', "z"),
    ('Ž', "Z"),
    ('ž', "z"),
    ('ſ', "s"),
];

/// Fern spells a canonical, entirely numeric enum value as English words. This
/// The same spelling is applied to a leading numeric run in an alphanumeric value
/// (`100base` → `one_hundred_base`).
fn numeric_enum_identifier(value: &str) -> Option<String> {
    if value.is_empty()
        || (value.len() > 1 && value.starts_with('0'))
        || !value.bytes().all(|byte| byte.is_ascii_digit())
    {
        return None;
    }
    let value: u16 = value.parse().ok()?;
    if value > 9_999 {
        return None;
    }

    const SMALL: [&str; 20] = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ];
    const TENS: [&str; 10] = [
        "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety",
    ];

    fn below_hundred(value: u16) -> String {
        if value < 20 {
            return SMALL[usize::from(value)].to_string();
        }
        let mut words = TENS[usize::from(value / 10)].to_string();
        if !value.is_multiple_of(10) {
            words.push('_');
            words.push_str(SMALL[usize::from(value % 10)]);
        }
        words
    }

    fn below_thousand(value: u16) -> String {
        if value < 100 {
            return below_hundred(value);
        }
        let mut words = format!("{}_hundred", SMALL[usize::from(value / 100)]);
        if !value.is_multiple_of(100) {
            words.push('_');
            words.push_str(&below_hundred(value % 100));
        }
        words
    }

    if value < 1_000 {
        return Some(below_thousand(value));
    }
    let mut words = format!("{}_thousand", SMALL[usize::from(value / 1_000)]);
    if !value.is_multiple_of(1_000) {
        words.push('_');
        words.push_str(&below_thousand(value % 1_000));
    }
    Some(words)
}

fn is_uuid(value: &str) -> bool {
    let parts: Vec<&str> = value.split('-').collect();
    parts.len() == 5
        && parts.iter().zip([8, 4, 4, 4, 12]).all(|(part, len)| {
            part.len() == len && part.bytes().all(|byte| byte.is_ascii_hexdigit())
        })
}

/// Fern's smart-casing path handles UUID-shaped enum values differently from
/// ordinary digit-leading values: a leading digit is wordified, longer numeric
/// prefixes use its literal `undefined` fallback, and digit-adjacent separators
/// collapse. Keep this scoped to canonical UUIDs so Crozier's established legal
/// fallback for enums Fern rejects (`_01_00_AM`) remains intact.
fn uuid_enum_identifier(value: &str) -> String {
    let mut words = split_words(value);
    if let Some(first) = words.first_mut() {
        let digit_len = first.bytes().take_while(u8::is_ascii_digit).count();
        if digit_len > 0 {
            let suffix = first[digit_len..].to_string();
            let numeric = &first[..digit_len];
            *first = digit_word(numeric).unwrap_or("undefined").to_string();
            if !suffix.is_empty() {
                words.insert(1, suffix);
            }
        }
    }
    let collapsed = collapse_digit_boundaries(&words.join("_"));
    let chars: Vec<char> = collapsed.chars().collect();
    chars
        .iter()
        .enumerate()
        .filter_map(|(index, &ch)| {
            // Fern's smart casing also joins single-letter fragments bracketed by
            // numeric runs (`466d-b0` -> `466db0`) after digit-boundary folding.
            let numeric_single_letter_bridge = ch == '_'
                && index >= 2
                && index + 2 < chars.len()
                && chars[index - 2].is_ascii_digit()
                && chars[index - 1].is_ascii_alphabetic()
                && chars[index + 1].is_ascii_alphabetic()
                && chars[index + 2].is_ascii_digit();
            (!numeric_single_letter_bridge).then_some(ch)
        })
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
    finalize_enum_ident(enum_identifier(value).to_ascii_uppercase())
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
    let mut name = finalize_enum_ident(enum_identifier(value));
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
    const RESERVED_BUILTINS: &[&str] =
        &["all", "bool", "int", "list", "long", "map", "set", "uuid"];
    PYTHON_KEYWORDS.contains(&name) || RESERVED_BUILTINS.contains(&name)
}

/// A Python field identifier for a pydantic model. In addition to ordinary
/// Python collisions, Fern protects names exposed by pydantic's model API.
#[must_use]
pub fn model_field_name(wire_name: &str) -> String {
    let name = field_name(wire_name);
    if matches!(name.as_str(), "kwargs" | "schema" | "self") {
        format!("{name}_")
    } else {
        name
    }
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

/// Apply Python's mandatory keyword escaping without treating ordinary builtins
/// as reserved. Method derivation uses this as a final validity boundary after
/// its context-specific Fern naming rules have run.
#[must_use]
pub fn escape_python_keyword(mut name: String) -> String {
    if PYTHON_KEYWORDS.contains(&name.as_str()) {
        name.push('_');
    }
    name
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
    fn method_keyword_escape_leaves_builtins_unchanged() {
        assert_eq!(escape_python_keyword("del".to_string()), "del_");
        assert_eq!(escape_python_keyword("list".to_string()), "list");
        assert_eq!(escape_python_keyword("all".to_string()), "all");
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
        assert_eq!(module_name("Class"), "class_");
        assert_eq!(module_name("_5GmmCause"), "_5_gmm_cause");
    }

    #[test]
    fn digit_leading_schema_names_get_legal_class_names() {
        assert_eq!(class_name("5GmmCause"), "FiveGmmCause");
        assert_eq!(class_name("Widget"), "Widget");
    }

    #[test]
    fn reserved_fields_get_suffixed() {
        assert_eq!(field_name("list"), "list_");
        assert_eq!(field_name("bool"), "bool_");
        assert_eq!(field_name("uuid"), "uuid_");
        assert_eq!(field_name("name"), "name");
        assert_eq!(field_name("tags"), "tags");
        assert_eq!(model_field_name("self"), "self_");
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
        // Fern's default smart casing rejoins digit-adjacent fragments before
        // applying the leading-digit prefix.
        assert_eq!(field_name("2-factor"), "f_2_factor");
        // Non-digit-leading names are untouched.
        assert_eq!(field_name("v2"), "v2");
    }

    #[test]
    fn numeric_field_boundaries_match_fern_without_changing_adjacent_word_rules() {
        assert_eq!(field_name("address_line_1"), "address_line1");
        assert_eq!(field_name("Cvc2Create"), "cvc2create");
        assert_eq!(field_name("prop65_warning"), "prop65warning");
        assert_eq!(field_name("prop_65_warning"), "prop65warning");
        assert_eq!(field_name("2Factor"), "f_2_factor");
    }

    #[test]
    fn whitespace_is_a_hard_boundary_for_field_digit_collapse() {
        // Measured on `med-anvisa-price`: inside one whitespace-delimited chunk
        // the digit boundaries collapse exactly as they always have, but a space
        // between a word and a digit survives into the identifier.
        assert_eq!(field_name("EAN 1"), "ean_1");
        assert_eq!(field_name("PF 0%"), "pf_0");
        assert_eq!(field_name("CONFAZ 87"), "confaz_87");
        assert_eq!(field_name("PF 17% ALC"), "pf_17_alc");
        assert_eq!(field_name("PF 17,5%"), "pf_175");
        assert_eq!(field_name("PF 17,5% ALC"), "pf_175_alc");
        // A chunk of pure punctuation contributes no segment at all.
        assert_eq!(field_name("PF 17 % ALC"), "pf_17_alc");
        assert_eq!(field_name("   "), "");
        // Non-ASCII letters remain separators on this path — Fern does not fold
        // them here, unlike the enum path.
        assert_eq!(field_name("SUBSTÂNCIA"), "subst_ncia");
        assert_eq!(field_name("COMERCIALIZAÇÃO 2019"), "comercializa_o_2019");
        assert_eq!(
            field_name("LISTA DE CONCESSÃO DE CRÉDITO TRIBUTÁRIO (PIS/COFINS)"),
            "lista_de_concess_o_de_cr_dito_tribut_rio_pis_cofins"
        );
        // Chunking leaves every whitespace-free name exactly where it was.
        assert_eq!(field_name("day_0_end_time"), "day0end_time");
        assert_eq!(field_name("user_fields[1]"), "user_fields1");
        assert_eq!(request_field_name("user_fields[1]"), "user_fields1");
        assert_eq!(request_field_name("EAN 1"), "ean_1");
    }

    #[test]
    fn enum_member_names_fold_latin_accents_the_property_path_drops() {
        // The two halves of Fern's asymmetry over one `med-anvisa-price` word.
        assert_eq!(enum_member_name("SUBSTÂNCIA"), "SUBSTANCIA");
        assert_eq!(field_name("SUBSTÂNCIA"), "subst_ncia");
        assert_eq!(enum_member_name("LABORATÓRIO"), "LABORATORIO");
        assert_eq!(enum_member_name("CÓDIGO GGREM"), "CODIGO_GGREM");
        assert_eq!(enum_member_name("APRESENTAÇÃO"), "APRESENTACAO");
        assert_eq!(enum_member_name("CLASSE TERAPÊUTICA"), "CLASSE_TERAPEUTICA");
        assert_eq!(enum_member_name("REGIME DE PREÇO"), "REGIME_DE_PRECO");
        assert_eq!(
            enum_member_name("COMERCIALIZAÇÃO 2019"),
            "COMERCIALIZACAO2019"
        );
        assert_eq!(enum_visit_param("ANÁLISE RECURSAL"), "analise_recursal");
    }

    #[test]
    fn the_latin_folding_table_is_sorted_and_spans_both_blocks() {
        assert!(
            DEBURRED_LATIN.windows(2).all(|pair| pair[0].0 < pair[1].0),
            "DEBURRED_LATIN must stay sorted for the binary search in deburr_letter"
        );
        assert!(
            DEBURRED_LATIN
                .iter()
                .all(|(accented, ascii)| !accented.is_ascii() && ascii.is_ascii()),
            "every entry folds one non-ASCII letter to an ASCII spelling"
        );
        // Latin-1 Supplement and Latin Extended-A, including the multi-letter and
        // unmapped-neighbour cases.
        assert_eq!(deburr_letter('Ä'), Some("A"));
        assert_eq!(deburr_letter('ß'), Some("ss"));
        assert_eq!(deburr_letter('Æ'), Some("Ae"));
        assert_eq!(deburr_letter('ŉ'), Some("'n"));
        assert_eq!(deburr_letter('ž'), Some("z"));
        assert_eq!(deburr_letter('×'), None);
        assert_eq!(deburr_letter('a'), None);
        assert_eq!(deburr_letter('気'), None);
        // Unmapped characters ride through untouched, so a CJK enum value keeps
        // reaching the existing separator fold rather than silently changing.
        assert_eq!(deburr("Ærøskøbing 気温"), "Aeroskobing 気温");
        assert_eq!(enum_member_name("気温"), "_");
    }

    #[test]
    fn digit_leading_request_fields_get_underscore_prefix() {
        assert_eq!(request_field_name("5gMmCauseValue"), "_5g_mm_cause_value");
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
        assert_eq!(enum_member_name("oauth2.0"), "OAUTH20");
        assert_eq!(enum_member_name("ID_CUSIP_8_CHR"), "ID_CUSIP8CHR");
        assert_eq!(enum_visit_param("ID_CUSIP_8_CHR"), "id_cusip8chr");
        assert_eq!(enum_member_name("SCHEDULE5MANUAL"), "SCHEDULE5MANUAL");
        assert_eq!(enum_visit_param("SCHEDULE5MANUAL"), "schedule5manual");
        assert_eq!(enum_member_name("200"), "TWO_HUNDRED");
        assert_eq!(enum_visit_param("201"), "two_hundred_one");
        assert_eq!(enum_member_name("1200 bps"), "ONE_THOUSAND_TWO_HUNDRED_BPS");
        assert_eq!(enum_member_name("19.2 kbps"), "NINETEEN2KBPS");
        assert_eq!(enum_member_name("DB-25"), "DB25");
        assert_eq!(enum_member_name("SFP+ (10GE)"), "SFP10GE");
        assert_eq!(enum_member_name("IEEE 802.11a"), "IEEE80211A");
        assert_eq!(enum_member_name("IEEE 802.11b/g"), "IEEE80211BG");
        assert_eq!(enum_member_name("10gbase-x-x2"), "TEN_GBASE_XX2");
        assert_eq!(enum_member_name("P+N+E 4H"), "PNE4H");
        assert_eq!(enum_member_name("2P+E 4H"), "TWO_PE4H");
        assert_eq!(
            enum_member_name("ITA Type E/F (CEE 7/7)"),
            "ITA_TYPE_EF_CEE77"
        );
        assert_eq!(enum_member_name("iec-60309-3p-n-e-4h"), "IEC603093PNE4H");
        assert_eq!(
            enum_member_name("100BASE-FX (10/100ME FIBER)"),
            "ONE_HUNDRED_BASE_FX10100ME_FIBER"
        );
        assert_eq!(
            enum_member_name("fbf35668-96a0-4baa-bcde-ab18d6b1b329"),
            "FBF3566896A04BAA_BCDE_AB18D6B1B329"
        );
        assert_eq!(
            enum_member_name("6a9dfcad-600b-46c8-9e08-ce6e5057921e"),
            "SIX_A9DFCAD600B46C89E08CE6E5057921E"
        );
        assert_eq!(
            enum_member_name("98777886-76d0-44c8-865e-bb40e669e934"),
            "UNDEFINED76D044C8865E_BB40E669E934"
        );
        assert_eq!(
            enum_member_name("ac5b9c1e-dc78-466d-b0b3-7cf712967a48"),
            "AC5B9C1E_DC78466DB0B37CF712967A48"
        );
        assert_eq!(
            enum_visit_param("ac5b9c1e-dc78-466d-b0b3-7cf712967a48"),
            "ac5b9c1e_dc78466db0b37cf712967a48"
        );
        assert_eq!(enum_member_name(""), "EMPTY");
        assert_eq!(enum_visit_param(""), "empty");
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
    fn spelled_number_tables_cover_every_digit_and_stop_at_five_figures() {
        // `digit_word` and `numeric_enum_identifier` are lookup tables: a wrong
        // entry changes an enum member silently, so pin every branch of both.
        for (digit, word) in [
            ("0", "zero"),
            ("1", "one"),
            ("2", "two"),
            ("3", "three"),
            ("4", "four"),
            ("5", "five"),
            ("6", "six"),
            ("7", "seven"),
            ("8", "eight"),
            ("9", "nine"),
        ] {
            assert_eq!(digit_word(digit), Some(word));
        }
        assert_eq!(digit_word("12"), None);
        assert_eq!(digit_word("x"), None);
        assert_eq!(digit_word(""), None);
        // Tens with and without a trailing unit, and the hundreds/thousands join.
        assert_eq!(enum_member_name("40"), "FORTY");
        assert_eq!(enum_member_name("45"), "FORTY_FIVE");
        assert_eq!(enum_member_name("19"), "NINETEEN");
        assert_eq!(enum_member_name("999"), "NINE_HUNDRED_NINETY_NINE");
        assert_eq!(
            enum_member_name("9999"),
            "NINE_THOUSAND_NINE_HUNDRED_NINETY_NINE"
        );
        // Past four figures Fern stops spelling; Crozier keeps the name legal.
        assert_eq!(enum_member_name("10000"), "_10000");
        // A bare wildcard is the one non-alphanumeric value Fern names rather
        // than treating as a separator.
        assert_eq!(enum_member_name("*"), "ALL");
        assert_eq!(enum_visit_param("*"), "all_");
    }

    #[test]
    fn enum_names_stay_legal_where_fern_would_error() {
        // A leading-zero token retains Crozier's legal-identifier guard where
        // Fern would reject the enum name.
        assert_eq!(enum_member_name("_01_00_AM"), "_01_00_AM");
        assert_eq!(enum_visit_param("_01_00_AM"), "_01_00_am");
        assert_eq!(enum_member_name("2fa"), "TWO_FA");
        assert_eq!(enum_visit_param("2fa"), "two_fa");
        // A value with no identifier characters still yields a legal name.
        assert_eq!(enum_member_name("!!!"), "_");
        assert_eq!(enum_visit_param("!!!"), "_");
    }

    #[test]
    fn sanitize_identifier_coerces_illegal_chars() {
        assert_eq!(sanitize_identifier("get-all-widgets"), "get_all_widgets");
        assert_eq!(sanitize_identifier("verify code"), "verify_code");
        assert_eq!(sanitize_identifier("2fa"), "_2fa");
        assert_eq!(to_pascal_case("ipam_l2vpns_list"), "IpamL2VpnsList");
        // Already-legal identifiers pass through unchanged.
        assert_eq!(sanitize_identifier("postwithnoauth"), "postwithnoauth");
        assert_eq!(
            prose_identifier("The /content endpoint"),
            "the_content_endpoint"
        );
        assert_eq!(
            prose_identifier("Get seller's feedback"),
            "get_sellers_feedback"
        );
        assert_eq!(
            prose_identifier("Returns 200 on success or 422 on failure"),
            "returns200on_success_or422on_failure"
        );
        assert_eq!(
            sanitize_identifier("endpoints_container"),
            "endpoints_container"
        );
    }
}
