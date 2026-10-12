//! SPIKE (serde-yaml-replacement): throwaway YAML read shim, never landed.
//!
//! Every production YAML read in crozier goes through [`from_str`] (a read into
//! one of crozier's own types) or [`value_from_str`] (a schema-less read into a
//! dynamic tree). Without the `spike-saphyr` feature both are `serde_yaml_ng`,
//! so the default build behaves exactly as `main`. With it, the reader is chosen
//! at run time by `CROZIER_SPIKE_YAML`, a comma list:
//!
//! - `off` — `serde_yaml_ng` for everything (the baseline, in the same binary);
//! - `tree=direct` (default) — schema-less reads go serde-saphyr straight into
//!   the dynamic tree the walks use today; `tree=json` — through
//!   `serde_json::Value` (`preserve_order`) first; `tree=saphyr` — through
//!   `saphyr` 0.2's node tree first;
//! - serde-saphyr `Options`: `budget=none`, `strict_booleans`, `dup=first|last`,
//!   `merge=ordinary|error`, `legacy_octal`, `nonfinite=string`;
//! - `wording=today` — typed reads render errors through [`today_wording`];
//! - `depth=N` — a serde-saphyr `Budget` with `max_depth` N and the node and
//!   event caps lifted (every other cap at its default);
//! - `code=bool` — crozier's `Option<bool>` fields read through [`opt_bool`]'s
//!   strict visitor; `code=string` — its `String` fields through [`string`].

use serde::de::DeserializeOwned;

/// A YAML read failure; crozier only ever displays it.
#[derive(Debug)]
pub struct YamlError(pub String);

impl std::fmt::Display for YamlError {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        f.write_str(&self.0)
    }
}

impl std::error::Error for YamlError {}

/// Read `text` into one of crozier's own types.
pub fn from_str<T: DeserializeOwned>(text: &str) -> Result<T, YamlError> {
    #[cfg(feature = "spike-saphyr")]
    {
        let mode = Mode::from_env();
        if !mode.off {
            if mode.flags.iter().any(|f| f == "code=string") {
                SOURCE.with(|cell| *cell.borrow_mut() = Some(text.to_owned()));
            }
            // `string`'s `Spanned` exists only under serde-saphyr's deserializer.
            IN_SAPHYR.with(|cell| cell.set(true));
            let result = if mode.flags.iter().any(|f| f == "wording=today") {
                today_wording::read_with(text, mode.options()).map_err(YamlError)
            } else {
                serde_saphyr::from_str_with_options(text, mode.options()).map_err(|e| YamlError(e.to_string()))
            };
            IN_SAPHYR.with(|cell| cell.set(false));
            return result;
        }
    }
    serde_yaml_ng::from_str(text).map_err(|e| YamlError(e.to_string()))
}

/// Read `text` into a schema-less tree (`serde_yaml_ng::Value` or a visitor
/// shaped like it) for the refusal walks and `$ref` resolution.
pub fn value_from_str<T: DeserializeOwned>(text: &str) -> Result<T, YamlError> {
    #[cfg(feature = "spike-saphyr")]
    {
        let mode = Mode::from_env();
        if !mode.off {
            return match mode.tree {
                Tree::Direct => from_str(text),
                Tree::Json => {
                    let value: serde_json::Value =
                        serde_saphyr::from_str_with_options(text, mode.options())
                            .map_err(|e| YamlError(e.to_string()))?;
                    T::deserialize(value).map_err(|e| YamlError(e.to_string()))
                }
                Tree::Saphyr => {
                    let value = saphyr_tree::load(text)?;
                    serde_yaml_ng::from_value(value).map_err(|e| YamlError(e.to_string()))
                }
            };
        }
    }
    serde_yaml_ng::from_str(text).map_err(|e| YamlError(e.to_string()))
}

#[cfg(feature = "spike-saphyr")]
thread_local! {
    static OVERRIDE: std::cell::RefCell<Option<String>> = const { std::cell::RefCell::new(None) };
    /// The text the current typed read is reading, for [`string`]'s spans.
    static SOURCE: std::cell::RefCell<Option<String>> = const { std::cell::RefCell::new(None) };
    /// Set while [`from_str`] runs serde-saphyr.
    static IN_SAPHYR: std::cell::Cell<bool> = const { std::cell::Cell::new(false) };
}

/// Whether the current serde-saphyr read has code flag `name` on.
#[cfg(feature = "spike-saphyr")]
fn code_flag(name: &str) -> bool {
    let mode = Mode::from_env();
    !mode.off && mode.flags.iter().any(|f| f == name)
}

/// `Option<bool>` field reader. Plain `Option<bool>` unless `code=bool`, which
/// accepts only a scalar the reader itself resolved to a boolean, so a quoted
/// `"true"` is refused as today.
pub fn opt_bool<'de, D: serde::Deserializer<'de>>(deserializer: D) -> Result<Option<bool>, D::Error> {
    #[cfg(feature = "spike-saphyr")]
    if code_flag("code=bool") {
        return <Option<StrictBool> as serde::Deserialize>::deserialize(deserializer).map(|b| b.map(|b| b.0));
    }
    <Option<bool> as serde::Deserialize>::deserialize(deserializer)
}

#[cfg(feature = "spike-saphyr")]
struct StrictBool(bool);

#[cfg(feature = "spike-saphyr")]
impl<'de> serde::Deserialize<'de> for StrictBool {
    fn deserialize<D: serde::Deserializer<'de>>(deserializer: D) -> Result<Self, D::Error> {
        struct Visitor;
        impl serde::de::Visitor<'_> for Visitor {
            type Value = StrictBool;
            fn expecting(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
                f.write_str("a boolean")
            }
            fn visit_bool<E: serde::de::Error>(self, value: bool) -> Result<StrictBool, E> {
                Ok(StrictBool(value))
            }
        }
        deserializer.deserialize_any(Visitor)
    }
}

/// `String` field reader. Plain `String` unless `code=string` inside a
/// serde-saphyr read (JSON documents and `$ref` nodes use other deserializers), which reads a
/// null scalar (`~`, `null`, an empty value) as its source spelling, as
/// serde_yaml_ng does, from serde-saphyr's `Spanned` location.
pub fn string<'de, D: serde::Deserializer<'de>>(deserializer: D) -> Result<String, D::Error> {
    #[cfg(feature = "spike-saphyr")]
    if code_flag("code=string") && IN_SAPHYR.with(std::cell::Cell::get) {
        let spanned = <serde_saphyr::Spanned<Option<String>> as serde::Deserialize>::deserialize(deserializer)?;
        return Ok(spanned.value.unwrap_or_else(|| {
            let span = spanned.referenced.span();
            let (Some(offset), Some(len)) = (span.byte_offset(), span.byte_len()) else {
                return String::new();
            };
            SOURCE.with(|cell| {
                cell.borrow()
                    .as_deref()
                    .and_then(|text| text.get(offset as usize..(offset + len) as usize))
                    .unwrap_or_default()
                    .to_owned()
            })
        }));
    }
    <String as serde::Deserialize>::deserialize(deserializer)
}

/// Override `CROZIER_SPIKE_YAML` for reads on this thread (the harness's switch).
#[cfg(feature = "spike-saphyr")]
pub fn set_thread_mode(mode: Option<&str>) {
    OVERRIDE.with(|cell| *cell.borrow_mut() = mode.map(str::to_owned));
}

#[cfg(feature = "spike-saphyr")]
#[derive(Clone, Copy)]
enum Tree {
    Direct,
    Json,
    Saphyr,
}

#[cfg(feature = "spike-saphyr")]
struct Mode {
    off: bool,
    tree: Tree,
    flags: Vec<String>,
}

#[cfg(feature = "spike-saphyr")]
impl Mode {
    fn from_env() -> Self {
        let raw = OVERRIDE
            .with(|cell| cell.borrow().clone())
            .unwrap_or_else(|| std::env::var("CROZIER_SPIKE_YAML").unwrap_or_default());
        let flags: Vec<String> = raw
            .split(',')
            .map(str::trim)
            .filter(|f| !f.is_empty())
            .map(str::to_owned)
            .collect();
        let tree = if flags.iter().any(|f| f == "tree=json") {
            Tree::Json
        } else if flags.iter().any(|f| f == "tree=saphyr") {
            Tree::Saphyr
        } else {
            Tree::Direct
        };
        Mode {
            off: flags.iter().any(|f| f == "off"),
            tree,
            flags,
        }
    }

    fn options(&self) -> serde_saphyr::Options {
        options_from_flags(&self.flags.iter().map(String::as_str).collect::<Vec<_>>())
    }
}

/// Build serde-saphyr `Options` from spike flags (shared with the harness).
#[cfg(feature = "spike-saphyr")]
pub fn options_from_flags(flags: &[&str]) -> serde_saphyr::Options {
    use serde_saphyr::options::{DuplicateKeyPolicy, MergeKeyPolicy};
    let mut options = serde_saphyr::Options::default();
    for flag in flags {
        match *flag {
            "budget=none" => options.budget = None,
            "strict_booleans" => options.strict_booleans = true,
            "dup=first" => options.duplicate_keys = DuplicateKeyPolicy::FirstWins,
            "dup=last" => options.duplicate_keys = DuplicateKeyPolicy::LastWins,
            "merge=ordinary" => options.merge_keys = MergeKeyPolicy::AsOrdinary,
            "merge=error" => options.merge_keys = MergeKeyPolicy::Error,
            "legacy_octal" => options.legacy_octal_numbers = true,
            "nonfinite=string" => options.reject_non_finite_typeless_float = false,
            "no_snippet" => options.with_snippet = false,
            flag if flag.starts_with("depth=") => {
                let depth = flag["depth=".len()..].parse().expect("depth=N takes a number");
                let mut budget = serde_saphyr::Budget::default();
                budget.max_depth = depth;
                budget.max_nodes = usize::MAX;
                budget.max_events = usize::MAX;
                options.budget = Some(budget);
            }
            _ => {}
        }
    }
    options
}

/// `saphyr` 0.2's node tree, converted to the dynamic tree the walks read.
#[cfg(feature = "spike-saphyr")]
pub mod saphyr_tree {
    use super::YamlError;
    use saphyr::{LoadableYamlNode, Scalar, Yaml};
    use serde_yaml_ng::value::{Tag, TaggedValue};
    use serde_yaml_ng::{Mapping, Number, Value};

    /// Parse the first document of `text` with saphyr and convert it.
    pub fn load(text: &str) -> Result<Value, YamlError> {
        let docs = Yaml::load_from_str(text).map_err(|e| YamlError(e.to_string()))?;
        Ok(docs.into_iter().next().map_or(Value::Null, |doc| convert(&doc)))
    }

    /// Convert one saphyr node.
    pub fn convert(node: &Yaml<'_>) -> Value {
        match node {
            Yaml::Value(scalar) => scalar_value(scalar),
            Yaml::Representation(text, _, _) => Value::String(text.to_string()),
            Yaml::Sequence(items) => Value::Sequence(items.iter().map(convert).collect()),
            Yaml::Mapping(map) => {
                let mut out = Mapping::new();
                for (k, v) in map {
                    out.insert(convert(k), convert(v));
                }
                Value::Mapping(out)
            }
            Yaml::Tagged(tag, inner) => {
                if tag.handle == "tag:yaml.org,2002:" || tag.handle == "!!" {
                    convert(inner)
                } else {
                    Value::Tagged(Box::new(TaggedValue {
                        tag: Tag::new(format!("{}{}", tag.handle, tag.suffix)),
                        value: convert(inner),
                    }))
                }
            }
            Yaml::Alias(_) | Yaml::BadValue => Value::Null,
        }
    }

    fn scalar_value(scalar: &Scalar<'_>) -> Value {
        match scalar {
            Scalar::Null => Value::Null,
            Scalar::Boolean(b) => Value::Bool(*b),
            Scalar::Integer(i) => Value::Number(Number::from(*i)),
            Scalar::FloatingPoint(f) => Value::Number(Number::from(f.into_inner())),
            Scalar::String(s) => Value::String(s.to_string()),
        }
    }
}

/// A code change measured for the error differences: serde-saphyr's public
/// `MessageFormatter` and `Localizer` restating serde's own wording and
/// serde_yaml_ng's ` at line L column C` suffix, `serde_path_to_error` for the
/// `a.b[0].c: ` prefix serde_yaml_ng gives, and snippets off.
#[cfg(feature = "spike-saphyr")]
pub mod today_wording {
    use std::borrow::Cow;
    use std::cell::RefCell;

    use serde::de::DeserializeOwned;
    use serde_saphyr::{DefaultMessageFormatter, Error, Localizer, Location, MessageFormatter, RenderOptions, SnippetMode};

    struct Suffix;
    impl Localizer for Suffix {
        fn attach_location<'a>(&self, base: Cow<'a, str>, loc: Location) -> Cow<'a, str> {
            if loc == Location::UNKNOWN {
                base
            } else {
                Cow::Owned(format!("{base} at line {} column {}", loc.line(), loc.column()))
            }
        }
    }

    fn one_of(names: &[&str], what: &str) -> String {
        match names {
            [] => format!("there are no {what}"),
            [a] => format!("expected `{a}`"),
            [a, b] => format!("expected `{a}` or `{b}`"),
            _ => format!("expected one of {}", names.iter().map(|n| format!("`{n}`")).collect::<Vec<_>>().join(", ")),
        }
    }

    struct Serde;
    impl MessageFormatter for Serde {
        fn localizer(&self) -> &dyn Localizer {
            &Suffix
        }
        fn format_message<'a>(&self, err: &'a Error) -> Cow<'a, str> {
            match err {
                Error::SerdeUnknownVariant { variant, expected, .. } => {
                    Cow::Owned(format!("unknown variant `{variant}`, {}", one_of(expected, "variants")))
                }
                Error::SerdeUnknownField { field, expected, .. } => {
                    Cow::Owned(format!("unknown field `{field}`, {}", one_of(expected, "fields")))
                }
                _ => DefaultMessageFormatter.format_message(err),
            }
        }
    }

    /// Read `text` with serde-saphyr under `flags`, rendering a failure in today's wording.
    pub fn read<T: DeserializeOwned>(text: &str, flags: &[&str]) -> Result<T, String> {
        read_with(text, super::options_from_flags(flags))
    }

    /// [`read`] with prepared `Options`.
    pub fn read_with<T: DeserializeOwned>(text: &str, mut options: serde_saphyr::Options) -> Result<T, String> {
        let path = RefCell::new(String::new());
        options.with_snippet = false;
        serde_saphyr::with_deserializer_from_str_with_options(text, options, |de| {
            serde_path_to_error::deserialize(de).map_err(|e| {
                *path.borrow_mut() = e.path().to_string();
                e.into_inner()
            })
        })
        .map_err(|e| {
            let mut render = RenderOptions::new(&Serde);
            render.snippets = SnippetMode::Off;
            let message = e.render_with_options(render);
            let path = path.borrow();
            match path.as_str() {
                "" | "." | "?" => message,
                p if p.starts_with('[') => format!(".{p}: {message}"),
                p => format!("{p}: {message}"),
            }
        })
    }
}
