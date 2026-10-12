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
//!   `merge=ordinary|error`, `legacy_octal`, `nonfinite=string`.

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
            return serde_saphyr::from_str_with_options(text, mode.options())
                .map_err(|e| YamlError(e.to_string()));
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
