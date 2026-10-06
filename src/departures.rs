//! The catalog of crozier's **intended departures** from Fern's output, and the
//! rule each one applies.
//!
//! The catalog is one machine-readable file, `assets/departures.yml`, compiled
//! into the binary. Each entry names one place crozier writes something other
//! than Fern on purpose: a Fern defect crozier corrects, or a deliberate
//! non-defect choice (branding, packaging, provenance, ordering). Each entry's
//! rule — the function of the same id in [`rule`] — recognises exactly Fern's
//! construct and crozier's replacement in a pair of files; the comparison
//! engine in [`crate::parity`] applies the rules and reports every departure it
//! applied by id, file and line. `docs/departures/README.md` holds the rendered
//! reference ([`render_reference`]), the defect rule, and how a fix adds an
//! entry.

use std::collections::BTreeSet;
use std::io::Write;
use std::process::{Command, Stdio};
use std::sync::OnceLock;

use serde::Deserialize;

/// The catalog's source, as compiled into the binary.
pub const CATALOG_SOURCE: &str = include_str!("../assets/departures.yml");

/// Where every entry's evidence note lives, relative to the repository root.
pub const EVIDENCE_DIR: &str = "docs/departures/evidence/";

/// What sort of departure an entry is.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Deserialize)]
#[serde(rename_all = "kebab-case")]
pub enum Kind {
    /// Fern's output is wrong under the defect rule, and crozier writes the
    /// correct output instead.
    FernDefect,
    /// crozier names itself where Fern names itself.
    Branding,
    /// crozier writes the packaged SDK's publishing details from its own
    /// settings.
    Packaging,
    /// crozier writes a fixed record of how it was generated.
    Provenance,
    /// crozier orders statements whose order has no effect deterministically.
    Ordering,
}

impl Kind {
    /// Every kind, in the order the reference lists them.
    pub const ALL: [Kind; 5] = [
        Kind::FernDefect,
        Kind::Branding,
        Kind::Packaging,
        Kind::Provenance,
        Kind::Ordering,
    ];

    /// The kind as the catalog spells it.
    #[must_use]
    pub fn as_str(self) -> &'static str {
        match self {
            Kind::FernDefect => "fern-defect",
            Kind::Branding => "branding",
            Kind::Packaging => "packaging",
            Kind::Provenance => "provenance",
            Kind::Ordering => "ordering",
        }
    }

    /// What the kind covers, as the reference describes it.
    #[must_use]
    pub fn meaning(self) -> &'static str {
        match self {
            Kind::FernDefect => {
                "Fern's output is wrong under the defect rule; crozier writes the correct output."
            }
            Kind::Branding => "crozier names itself where Fern names itself.",
            Kind::Packaging => {
                "crozier writes the packaged SDK's publishing details from its own settings."
            }
            Kind::Provenance => "crozier writes a fixed record of how the SDK was generated.",
            Kind::Ordering => {
                "crozier writes statements whose order has no effect in its own deterministic order."
            }
        }
    }
}

/// One catalog entry: exactly these keys.
#[derive(Debug, Clone, PartialEq, Eq, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct Departure {
    /// A unique lower-kebab slug naming the shape in crozier's own terms.
    pub id: String,
    /// What sort of departure it is.
    pub kind: Kind,
    /// The input and file that produce it.
    pub trigger: String,
    /// What Fern writes there.
    pub fern: String,
    /// What crozier writes instead.
    pub crozier: String,
    /// Why it is intended; for a `fern-defect`, why Fern's output is wrong.
    pub reason: String,
    /// The repository-relative path of the committed evidence note.
    pub evidence: String,
}

/// The keys an entry holds, in the order the catalog writes them.
pub const KEYS: [&str; 7] = [
    "id", "kind", "trigger", "fern", "crozier", "reason", "evidence",
];

/// Parse a catalog's text, then validate it: every failure, each naming its
/// entry, rather than the first.
///
/// # Errors
///
/// When the text is not a list of entries with exactly [`KEYS`], or when
/// [`validation_failures`] finds anything.
pub fn parse(text: &str) -> Result<Vec<Departure>, Vec<String>> {
    let entries: Vec<Departure> = serde_yaml_ng::from_str(text).map_err(|error| {
        vec![format!(
            "the departure catalog is a list of entries holding exactly the keys {}: {error}",
            KEYS.join(", ")
        )]
    })?;
    let failures = validation_failures(&entries);
    if failures.is_empty() {
        Ok(entries)
    } else {
        Err(failures)
    }
}

/// The compiled catalog. Its validity is pinned by this module's tests, so a
/// build that ships an invalid one cannot pass the gate.
///
/// # Panics
///
/// When the compiled catalog is invalid.
#[must_use]
pub fn catalog() -> &'static [Departure] {
    static CATALOG: OnceLock<Vec<Departure>> = OnceLock::new();
    CATALOG.get_or_init(|| {
        parse(CATALOG_SOURCE).unwrap_or_else(|failures| {
            panic!(
                "the compiled departure catalog is invalid:\n{}",
                failures.join("\n")
            )
        })
    })
}

/// The compiled entry `id`, if the catalog holds one.
#[must_use]
pub fn find(id: &str) -> Option<&'static Departure> {
    catalog().iter().find(|departure| departure.id == id)
}

/// Whether `id` is a lower-kebab slug.
fn is_slug(id: &str) -> bool {
    !id.is_empty()
        && !id.starts_with('-')
        && !id.ends_with('-')
        && !id.contains("--")
        && id
            .bytes()
            .all(|byte| byte.is_ascii_lowercase() || byte.is_ascii_digit() || byte == b'-')
}

/// Every way `entries` break the catalog's contract, each naming its entry:
/// ids that are not unique lower-kebab slugs in sorted order, an empty field,
/// evidence outside [`EVIDENCE_DIR`], and an entry with no rule (or a rule with
/// no entry). Whether each evidence note is committed is the repository's to
/// check; the binary has no repository.
#[must_use]
pub fn validation_failures(entries: &[Departure]) -> Vec<String> {
    let mut failures = Vec::new();
    for pair in entries.windows(2) {
        let (previous, entry) = (&pair[0], &pair[1]);
        if previous.id == entry.id {
            failures.push(format!(
                "departure `{}`: the id appears twice; ids are unique",
                entry.id
            ));
        } else if previous.id > entry.id {
            failures.push(format!(
                "departure `{}`: follows `{}`; entries are sorted by id",
                entry.id, previous.id
            ));
        }
    }
    for entry in entries {
        let id = &entry.id;
        if !is_slug(id) {
            failures.push(format!(
                "departure `{id}`: the id is not a lower-kebab slug"
            ));
        }
        for (key, value) in [
            ("trigger", &entry.trigger),
            ("fern", &entry.fern),
            ("crozier", &entry.crozier),
            ("reason", &entry.reason),
        ] {
            if value.trim().is_empty() {
                failures.push(format!("departure `{id}`: `{key}` is empty"));
            }
        }
        let evidence = &entry.evidence;
        let plain = !evidence.contains('\\')
            && evidence
                .split('/')
                .all(|part| !part.is_empty() && part != "." && part != "..");
        if !plain || !evidence.starts_with(EVIDENCE_DIR) || !evidence.ends_with(".md") {
            failures.push(format!(
                "departure `{id}`: `evidence` `{evidence}` is not a note under {EVIDENCE_DIR}"
            ));
        }
        if rule(id).is_none() {
            failures.push(format!(
                "departure `{id}`: no rule of that id in src/departures.rs; every entry is \
                 applied through its rule"
            ));
        }
    }
    let ids: BTreeSet<&str> = entries.iter().map(|entry| entry.id.as_str()).collect();
    for id in RULE_IDS {
        if !ids.contains(id) {
            failures.push(format!(
                "departure rule `{id}` has no catalog entry; a rule is applied only as an entry's"
            ));
        }
    }
    failures
}

/// The opening and closing markers of the generated catalog in the reference.
pub const REFERENCE_MARKERS: (&str, &str) = (
    "<!-- BEGIN GENERATED CATALOG: edit assets/departures.yml, then regenerate -->",
    "<!-- END GENERATED CATALOG -->",
);

/// The catalog as the reference renders it, between [`REFERENCE_MARKERS`]: the
/// kinds, then one section per entry.
#[must_use]
pub fn render_reference(entries: &[Departure]) -> String {
    let one_line = |text: &str| text.split_whitespace().collect::<Vec<_>>().join(" ");
    let mut out = format!("{}\n\n", REFERENCE_MARKERS.0);
    out.push_str("| Kind | Entries | Meaning |\n| --- | --- | --- |\n");
    for kind in Kind::ALL {
        let count = entries.iter().filter(|entry| entry.kind == kind).count();
        out.push_str(&format!(
            "| `{}` | {count} | {} |\n",
            kind.as_str(),
            kind.meaning()
        ));
    }
    for entry in entries {
        out.push_str(&format!(
            "\n### `{}`\n\n- **Kind:** `{}`\n- **Trigger:** {}\n- **Fern writes:** {}\n\
             - **crozier writes:** {}\n- **Why:** {}\n- **Evidence:** [`{}`](../../{})\n",
            entry.id,
            entry.kind.as_str(),
            one_line(&entry.trigger),
            one_line(&entry.fern),
            one_line(&entry.crozier),
            one_line(&entry.reason),
            entry.evidence,
            entry.evidence,
        ));
    }
    out.push_str(&format!("\n{}\n", REFERENCE_MARKERS.1));
    out
}

/// What a rule may consult about the two trees a file pair belongs to: the
/// top-level class names each tree's Python modules define, the base-path
/// parameters crozier's routes read from the client, and the distribution name
/// crozier's `pyproject.toml` declares, read on first use. A file compared on
/// its own has an empty context, so no rule that needs one applies to it.
#[derive(Debug, Default)]
pub struct Context {
    roots: Option<(std::path::PathBuf, std::path::PathBuf)>,
    reference_classes: OnceLock<BTreeSet<String>>,
    crozier_classes: OnceLock<BTreeSet<String>>,
    crozier_lifted: OnceLock<BTreeSet<String>>,
    crozier_constant_headers: OnceLock<BTreeSet<(String, String)>>,
    reference_nullable_items: OnceLock<BTreeSet<String>>,
    crozier_project: OnceLock<Option<String>>,
}

impl Context {
    /// The context of two trees given as `(path, text)` pairs.
    pub fn from_sources<'a>(
        reference: impl IntoIterator<Item = (&'a str, &'a str)>,
        crozier: impl IntoIterator<Item = (&'a str, &'a str)>,
    ) -> Self {
        let reference: Vec<(&str, &str)> = reference.into_iter().collect();
        let crozier: Vec<(&str, &str)> = crozier.into_iter().collect();
        let project = crozier
            .iter()
            .find(|(path, _)| *path == "pyproject.toml")
            .and_then(|(_, text)| project_name(text));
        Context {
            roots: None,
            reference_classes: OnceLock::from(classes(reference.iter().copied())),
            crozier_classes: OnceLock::from(classes(crozier.iter().copied())),
            crozier_lifted: OnceLock::from(lifted_parameters(crozier.iter().copied())),
            crozier_constant_headers: OnceLock::from(constant_headers(crozier.iter().copied())),
            reference_nullable_items: OnceLock::from(nullable_item_parameters(
                reference
                    .iter()
                    .filter(|(path, _)| *path == "reference.md")
                    .map(|(_, text)| *text),
            )),
            crozier_project: OnceLock::from(project),
        }
    }

    /// The context of the trees at `reference` and `crozier`, read only if a
    /// rule asks for it. A module that cannot be read defines nothing.
    #[must_use]
    pub fn from_trees(reference: &std::path::Path, crozier: &std::path::Path) -> Self {
        Context {
            roots: Some((reference.to_path_buf(), crozier.to_path_buf())),
            ..Context::default()
        }
    }

    /// Classes the reference's modules define.
    pub fn reference_classes(&self) -> &BTreeSet<String> {
        self.reference_classes
            .get_or_init(|| self.tree_classes(|(reference, _)| reference))
    }

    /// Classes crozier's modules define.
    pub fn crozier_classes(&self) -> &BTreeSet<String> {
        self.crozier_classes
            .get_or_init(|| self.tree_classes(|(_, crozier)| crozier))
    }

    /// The base-path parameters crozier's routes read from the client wrapper
    /// rather than take as method arguments: each `X` of a route's
    /// `encode_path_param(self._client_wrapper._X)`.
    pub fn crozier_lifted_parameters(&self) -> &BTreeSet<String> {
        self.crozier_lifted.get_or_init(|| {
            let Some((_, root)) = self.roots.as_ref() else {
                return BTreeSet::new();
            };
            let sources: Vec<(String, String)> = python_sources(root);
            lifted_parameters(
                sources
                    .iter()
                    .map(|(rel, text)| (rel.as_str(), text.as_str())),
            )
        })
    }

    /// The headers crozier's raw clients send as constants, each as the
    /// `(wire name, value)` of a `"<wire>": "<value>",` line of a `headers` dict.
    pub fn crozier_constant_headers(&self) -> &BTreeSet<(String, String)> {
        self.crozier_constant_headers.get_or_init(|| {
            let Some((_, root)) = self.roots.as_ref() else {
                return BTreeSet::new();
            };
            let sources = python_sources(root);
            constant_headers(
                sources
                    .iter()
                    .map(|(rel, text)| (rel.as_str(), text.as_str())),
            )
        })
    }

    /// The query parameters the reference's `reference.md` documents with
    /// nullable items, as
    /// ``**NAME:** `typing.Optional[typing.Union[typing.Optional[T], typing.Sequence[typing.Optional[T]]]]` ``.
    pub fn reference_nullable_items(&self) -> &BTreeSet<String> {
        self.reference_nullable_items.get_or_init(|| {
            let Some((root, _)) = self.roots.as_ref() else {
                return BTreeSet::new();
            };
            let text = std::fs::read_to_string(root.join("reference.md")).unwrap_or_default();
            nullable_item_parameters([text.as_str()])
        })
    }

    /// The distribution name crozier's `pyproject.toml` declares, if its tree
    /// has one.
    pub fn crozier_project(&self) -> Option<&str> {
        self.crozier_project
            .get_or_init(|| {
                let (_, crozier) = self.roots.as_ref()?;
                project_name(&std::fs::read_to_string(crozier.join("pyproject.toml")).ok()?)
            })
            .as_deref()
    }

    /// The classes of the tree `side` picks, or none without trees.
    fn tree_classes(
        &self,
        side: impl Fn(&(std::path::PathBuf, std::path::PathBuf)) -> &std::path::PathBuf,
    ) -> BTreeSet<String> {
        let Some(root) = self.roots.as_ref().map(side) else {
            return BTreeSet::new();
        };
        let sources = python_sources(root);
        classes(
            sources
                .iter()
                .map(|(rel, text)| (rel.as_str(), text.as_str())),
        )
    }
}

/// Every `.py` file under `root` as `(relative path, text)`; a module that
/// cannot be read is left out.
fn python_sources(root: &std::path::Path) -> Vec<(String, String)> {
    crate::parity::walk_files(root)
        .unwrap_or_default()
        .into_iter()
        .filter(|rel| rel.ends_with(".py"))
        .filter_map(|rel| {
            let text = std::fs::read_to_string(root.join(&rel)).ok()?;
            Some((rel, text))
        })
        .collect()
}

/// The names `X` the `.py` files among `sources` read as
/// `encode_path_param(self._client_wrapper._X)`: base-path parameters a route
/// takes from the client.
fn lifted_parameters<'a>(
    sources: impl IntoIterator<Item = (&'a str, &'a str)>,
) -> BTreeSet<String> {
    const READ: &str = "encode_path_param(self._client_wrapper._";
    sources
        .into_iter()
        .filter(|(path, _)| path.ends_with(".py"))
        .flat_map(|(_, text)| {
            text.match_indices(READ)
                .map(move |(at, _)| &text[at + READ.len()..])
        })
        .filter_map(|rest| {
            let name: String = rest
                .chars()
                .take_while(|c| c.is_alphanumeric() || *c == '_')
                .collect();
            (!name.is_empty() && rest[name.len()..].starts_with(')')).then_some(name)
        })
        .collect()
}

/// The `(wire name, value)` of every `"<wire>": "<value>",` line inside a
/// `headers={` dict of the raw clients among `sources`.
fn constant_headers<'a>(
    sources: impl IntoIterator<Item = (&'a str, &'a str)>,
) -> BTreeSet<(String, String)> {
    let mut found = BTreeSet::new();
    for (path, text) in sources {
        if !path.ends_with("raw_client.py") {
            continue;
        }
        let mut in_headers = false;
        for line in text.lines() {
            let trimmed = line.trim();
            if trimmed == "headers={" {
                in_headers = true;
                continue;
            }
            if in_headers && trimmed.starts_with('}') {
                in_headers = false;
                continue;
            }
            if !in_headers {
                continue;
            }
            let pair = trimmed
                .strip_suffix(',')
                .and_then(|entry| entry.split_once(": "))
                .and_then(|(key, value)| {
                    let key = key.strip_prefix('"')?.strip_suffix('"')?;
                    let value = value.strip_prefix('"')?.strip_suffix('"')?;
                    (!key.contains('"') && !value.contains('"'))
                        .then(|| (key.to_string(), value.to_string()))
                });
            found.extend(pair);
        }
    }
    found
}

/// `(the reference.md type Fern writes, crozier's)` for a one-or-many query
/// parameter over `item`: Fern keeps the items' nullability that the signature
/// drops.
fn nullable_items_types(item: &str) -> (String, String) {
    (
        format!(
            "typing.Optional[typing.Union[typing.Optional[{item}], typing.Sequence[typing.Optional[{item}]]]]"
        ),
        format!("typing.Optional[typing.Union[{item}, typing.Sequence[{item}]]]"),
    )
}

/// `(NAME, type)` of a `reference.md` parameter line `**NAME:** \`type\` …`.
fn documented_parameter(line: &str) -> Option<(&str, &str)> {
    let (name, rest) = line.strip_prefix("**")?.split_once(":** `")?;
    let (annotation, _) = rest.split_once('`')?;
    Some((name, annotation))
}

/// The names `reference.md` texts document with Fern's nullable-items type.
fn nullable_item_parameters<'a>(texts: impl IntoIterator<Item = &'a str>) -> BTreeSet<String> {
    texts
        .into_iter()
        .flat_map(str::lines)
        .filter_map(documented_parameter)
        .filter(|(_, annotation)| {
            annotation
                .strip_prefix("typing.Optional[typing.Union[typing.Optional[")
                .and_then(|rest| rest.split_once("], "))
                .is_some_and(|(item, _)| nullable_items_types(item).0 == *annotation)
        })
        .map(|(name, _)| name.to_string())
        .collect()
}

/// The first `name = "…"` a `pyproject.toml` declares: its `[project]` name.
fn project_name(pyproject: &str) -> Option<String> {
    pyproject
        .lines()
        .find_map(|line| line.strip_prefix("name = \"")?.strip_suffix('"'))
        .map(str::to_string)
}

/// The top-level class names the `.py` files among `sources` define.
fn classes<'a>(sources: impl IntoIterator<Item = (&'a str, &'a str)>) -> BTreeSet<String> {
    sources
        .into_iter()
        .filter(|(path, _)| path.ends_with(".py"))
        .flat_map(|(_, text)| text.lines())
        .filter_map(|line| line.strip_prefix("class "))
        .map(|rest| {
            rest.chars()
                .take_while(|c| c.is_alphanumeric() || *c == '_')
                .collect::<String>()
        })
        .filter(|name| !name.is_empty())
        .collect()
}

/// One file pair as the rules see it: its `/`-separated path relative to the
/// SDK root, both sides' lines once the comparison's mechanics have run (Python
/// comments stripped, line numbers unchanged), and the trees' [`Context`].
pub struct Pair<'a> {
    /// The file's path relative to the SDK root.
    pub rel: &'a str,
    /// The reference's lines.
    pub fern: &'a [&'a str],
    /// crozier's lines.
    pub crozier: &'a [&'a str],
    /// What the rules may know about the two trees.
    pub context: &'a Context,
}

/// A region one rule accounts for: Fern's lines `fern` correspond to crozier's
/// lines `crozier` (half-open, 0-based), and the two differ.
#[derive(Debug, Clone, PartialEq, Eq)]
pub struct Region {
    /// Fern's lines.
    pub fern: std::ops::Range<usize>,
    /// crozier's lines.
    pub crozier: std::ops::Range<usize>,
}

/// A rule's recogniser for one region of a pair, found from the files'
/// structure.
pub type RegionRule = fn(&Pair<'_>) -> Result<Option<Region>, String>;

/// A rule's recogniser for one Fern line and the crozier line aligned with it.
pub type LineRule = fn(&Pair<'_>, &str, &str) -> bool;

/// A rule's recogniser for one line crozier writes with no Fern counterpart.
pub type AddedRule = fn(&Pair<'_>, &str) -> bool;

/// How one entry's rule recognises its departure: by any of the three shapes.
#[derive(Clone, Copy, Default)]
pub struct Rule {
    /// A region of the pair.
    pub region: Option<RegionRule>,
    /// An aligned pair of lines.
    pub line: Option<LineRule>,
    /// A line only crozier writes.
    pub added: Option<AddedRule>,
}

/// Every rule's id, in catalog order — the order the engine tries them in.
pub const RULE_IDS: [&str; 10] = [
    "closed-empty-object-example",
    "constant-header-docs-arguments",
    "fern-metadata-generator-config",
    "init-type-checking-import-order",
    "lifted-base-path-docs-examples",
    "lifted-base-path-positional-example",
    "nullable-items-docs",
    "readme-client-class-casing",
    "sdk-identity-header-prefix",
    "sdk-name-version-headers",
];

/// The rule of the catalog entry `id`, if crozier has one.
#[must_use]
pub fn rule(id: &str) -> Option<Rule> {
    let none = Rule::default();
    Some(match id {
        "closed-empty-object-example" => Rule {
            region: Some(closed_empty_object_example_region),
            line: Some(closed_empty_object_example_line),
            added: None,
        },
        "constant-header-docs-arguments" => Rule {
            region: Some(constant_header_docs_arguments),
            ..none
        },
        "fern-metadata-generator-config" => Rule {
            region: Some(metadata_generator_config),
            ..none
        },
        "init-type-checking-import-order" => Rule {
            region: Some(init_type_checking_import_order),
            ..none
        },
        "lifted-base-path-docs-examples" => Rule {
            region: Some(lifted_base_path_docs_examples),
            ..none
        },
        "lifted-base-path-positional-example" => Rule {
            line: Some(lifted_base_path_positional_example),
            ..none
        },
        "nullable-items-docs" => Rule {
            region: Some(nullable_items_docs),
            ..none
        },
        "readme-client-class-casing" => Rule {
            line: Some(readme_client_class_casing),
            ..none
        },
        "sdk-identity-header-prefix" => Rule {
            line: Some(sdk_identity_header_prefix),
            ..none
        },
        "sdk-name-version-headers" => Rule {
            line: Some(sdk_name_version_header),
            added: Some(sdk_name_version_header_added),
            region: None,
        },
        _ => return None,
    })
}

/// Fern's free-form example placeholder, the value of `name={…}` in a snippet.
const KEY_VALUE_PLACEHOLDER: &str = "\"key\": \"value\"";

/// `(indentation, keyword)` of a snippet line `<indent><keyword>=<value>,` whose
/// value is exactly `value`.
fn keyword_argument<'l>(line: &'l str, value: &str) -> Option<(&'l str, &'l str)> {
    let indent = &line[..line.len() - line.trim_start().len()];
    let (keyword, rest) = line.trim_start().split_once('=')?;
    let identifier = keyword
        .chars()
        .next()
        .is_some_and(|first| first.is_ascii_alphabetic() || first == '_')
        && keyword
            .chars()
            .all(|ch| ch.is_ascii_alphanumeric() || ch == '_');
    (identifier && rest == value).then_some((indent, keyword))
}

/// `closed-empty-object-example`, in a snippet laid out one argument per line:
/// Fern's three lines `<indent><keyword>={`, `<indent>    "key": "value"`,
/// `<indent>},` where crozier writes the one line `<indent><keyword>={},`.
fn closed_empty_object_example_block(fern: &[&str], crozier: &str) -> bool {
    let [open, member, close] = fern else {
        return false;
    };
    let Some((indent, keyword)) = keyword_argument(open, "{") else {
        return false;
    };
    *member == format!("{indent}    {KEY_VALUE_PLACEHOLDER}")
        && *close == format!("{indent}}},")
        && crozier == format!("{indent}{keyword}={{}},")
}

/// `closed-empty-object-example` in `README.md` or `reference.md`: the region
/// from Fern's first three-line `{"key": "value"}` placeholder to its last.
/// Every line before it is equal on both sides' line count, so the region
/// starts at the same line on each; inside it, Fern's lines with each
/// placeholder collapsed to crozier's `<keyword>={},` equal crozier's exactly.
fn closed_empty_object_example_region(pair: &Pair<'_>) -> Result<Option<Region>, String> {
    if !DOCS_FILES.contains(&pair.rel) {
        return Ok(None);
    }
    let fern = pair.fern;
    // Fern's lines with each placeholder collapsed, and the Fern and collapsed
    // line ranges from the first placeholder to the end of the last.
    let mut collapsed: Vec<String> = Vec::new();
    let mut span: Option<(usize, usize, usize)> = None;
    let mut index = 0;
    while index < fern.len() {
        let line = fern
            .get(index..index + 3)
            .and_then(|block| Some((block, keyword_argument(block[0], "{")?)))
            .map(|(block, (indent, keyword))| (block, format!("{indent}{keyword}={{}},")))
            .filter(|(block, line)| closed_empty_object_example_block(block, line));
        if let Some((_, line)) = line {
            let begin = span.map_or(index, |(begin, _, _)| begin);
            collapsed.push(line);
            index += 3;
            span = Some((begin, index, collapsed.len()));
        } else {
            collapsed.push(fern[index].to_string());
            index += 1;
        }
    }
    let Some((begin, fern_end, end)) = span else {
        return Ok(None);
    };
    let equal = pair.crozier.get(begin..end).is_some_and(|region| {
        region
            .iter()
            .zip(&collapsed[begin..end])
            .all(|(crozier, collapsed)| crozier == collapsed)
    });
    Ok(equal.then_some(Region {
        fern: begin..fern_end,
        crozier: begin..end,
    }))
}

/// `closed-empty-object-example` written on one line, as a method docstring's
/// example and a short snippet write it: Fern's `<indent><keyword>={"key":
/// "value"},` where crozier's line is `<indent><keyword>={},`.
fn closed_empty_object_example_line(_: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    keyword_argument(fern, &format!("{{{KEY_VALUE_PLACEHOLDER}}},"))
        .is_some_and(|(indent, keyword)| crozier == format!("{indent}{keyword}={{}},"))
}

/// The SDK-relative path of Fern's own metadata record.
pub const FERN_METADATA: &str = ".fern/metadata.json";

/// `fern-metadata-generator-config`: crozier's `.fern/metadata.json` is exactly
/// its fixed record; read as JSON, the two objects are equal but for their
/// `generatorConfig` member, which differs; and every line that differs lies
/// within that member on each side. The member's lines are found string-aware, so a brace or quote inside a
/// string can neither hide a difference nor stretch the member.
fn metadata_generator_config(pair: &Pair<'_>) -> Result<Option<Region>, String> {
    if pair.rel != FERN_METADATA {
        return Ok(None);
    }
    let (fern_text, crozier_text) = (pair.fern.join("\n"), pair.crozier.join("\n"));
    if crozier_text != crate::emit::FERN_METADATA_RECORD {
        return Ok(None);
    }
    let (Ok(serde_json::Value::Object(mut fern)), Ok(serde_json::Value::Object(mut crozier))) = (
        serde_json::from_str::<serde_json::Value>(&fern_text),
        serde_json::from_str::<serde_json::Value>(&crozier_text),
    ) else {
        return Ok(None);
    };
    let (fern_config, crozier_config) = (
        fern.remove("generatorConfig"),
        crozier.remove("generatorConfig"),
    );
    if fern != crozier || fern_config == crozier_config {
        return Ok(None);
    }
    let (Some(window), Member::Lines(crozier_block)) = (
        differing_window(pair.fern, pair.crozier),
        generator_config_member(&crozier_text),
    ) else {
        return Ok(None);
    };
    let within = |range: &std::ops::Range<usize>, block: &std::ops::Range<usize>| {
        range.is_empty() || (range.start >= block.start && range.end <= block.end)
    };
    let holds = match generator_config_member(&fern_text) {
        Member::Lines(fern_block) => {
            within(&window.fern, &fern_block) && within(&window.crozier, &crozier_block)
        }
        // crozier's member is not its record's last, so where Fern has none,
        // crozier's member lines are all that differ.
        Member::Absent => window.fern.is_empty() && within(&window.crozier, &crozier_block),
        Member::Shared => false,
    };
    Ok(holds.then_some(window))
}

/// Where a JSON document's top-level `generatorConfig` member sits.
#[derive(Debug, PartialEq, Eq)]
enum Member {
    /// The document has no such member.
    Absent,
    /// The member owns these whole lines: nothing but indentation before its
    /// key, nothing but a comma after its value.
    Lines(std::ops::Range<usize>),
    /// The member shares a line with other text.
    Shared,
}

/// The byte after the closing quote of the JSON string opening at `start` in
/// `bytes`, if it closes.
fn string_end(bytes: &[u8], start: usize) -> Option<usize> {
    let mut index = start + 1;
    while index < bytes.len() {
        match bytes[index] {
            b'\\' => index += 2,
            b'"' => return Some(index + 1),
            _ => index += 1,
        }
    }
    None
}

/// The top-level `generatorConfig` member of the JSON object `text`, located
/// string-aware: braces, brackets and quotes inside strings are text.
fn generator_config_member(text: &str) -> Member {
    let bytes = text.as_bytes();
    let (mut depth, mut index, mut found) = (0usize, 0usize, None);
    while index < bytes.len() {
        match bytes[index] {
            b'"' => {
                let Some(end) = string_end(bytes, index) else {
                    return Member::Absent;
                };
                let after = text[end..].trim_start();
                if depth == 1
                    && &text[index..end] == "\"generatorConfig\""
                    && after.starts_with(':')
                {
                    found = Some((index, text.len() - after.len() + 1));
                    break;
                }
                index = end;
                continue;
            }
            b'{' | b'[' => depth += 1,
            b'}' | b']' => depth = depth.saturating_sub(1),
            _ => {}
        }
        index += 1;
    }
    let Some((key, value_start)) = found else {
        return Member::Absent;
    };
    // The value runs to the close of what it opens, or to the next `,` or
    // closer at its own level.
    let (mut depth, mut index, mut value_end) = (0usize, value_start, None);
    while index < bytes.len() {
        match bytes[index] {
            b'"' => {
                let Some(end) = string_end(bytes, index) else {
                    return Member::Absent;
                };
                if depth == 0 {
                    value_end = Some(end);
                }
                index = end;
                continue;
            }
            b'{' | b'[' => depth += 1,
            b'}' | b']' if depth == 0 => break,
            b'}' | b']' => {
                depth -= 1;
                if depth == 0 {
                    value_end = Some(index + 1);
                    break;
                }
            }
            b',' if depth == 0 => break,
            byte if depth == 0 && !byte.is_ascii_whitespace() => value_end = Some(index + 1),
            _ => {}
        }
        index += 1;
    }
    let Some(value_end) = value_end else {
        return Member::Absent;
    };
    let line_of = |offset: usize| text[..offset].matches('\n').count();
    let line_start = text[..key].rfind('\n').map_or(0, |newline| newline + 1);
    let line_end = text[value_end..]
        .find('\n')
        .map_or(text.len(), |newline| value_end + newline);
    let owns = text[line_start..key].trim().is_empty()
        && matches!(text[value_end..line_end].trim(), "" | ",");
    if owns {
        Member::Lines(line_of(key)..line_of(value_end) + 1)
    } else {
        Member::Shared
    }
}

/// The smallest window of lines outside which `fern` and `crozier` are equal:
/// their common leading and trailing lines removed. `None` when they are equal.
#[must_use]
pub fn differing_window(fern: &[&str], crozier: &[&str]) -> Option<Region> {
    if fern == crozier {
        return None;
    }
    let prefix = fern
        .iter()
        .zip(crozier)
        .take_while(|(left, right)| left == right)
        .count();
    let suffix = fern[prefix..]
        .iter()
        .rev()
        .zip(crozier[prefix..].iter().rev())
        .take_while(|(left, right)| left == right)
        .count();
    Some(Region {
        fern: prefix..fern.len() - suffix,
        crozier: prefix..crozier.len() - suffix,
    })
}

/// `init-type-checking-import-order`: in an `__init__.py`, both sides'
/// `if typing.TYPE_CHECKING:` blocks differ, yet sort to the same text under
/// ruff's isort. The region is the blocks' differing window.
fn init_type_checking_import_order(pair: &Pair<'_>) -> Result<Option<Region>, String> {
    if pair.rel != "__init__.py" && !pair.rel.ends_with("/__init__.py") {
        return Ok(None);
    }
    let (Some(fern_block), Some(crozier_block)) = (
        type_checking_block(pair.fern),
        type_checking_block(pair.crozier),
    ) else {
        return Ok(None);
    };
    let fern = &pair.fern[fern_block.clone()];
    let crozier = &pair.crozier[crozier_block.clone()];
    let Some(window) = differing_window(fern, crozier) else {
        return Ok(None);
    };
    let (Some(fern_body), Some(crozier_body)) = (dedent(fern), dedent(crozier)) else {
        return Ok(None);
    };
    if ruff_isort(&fern_body)? != ruff_isort(&crozier_body)? {
        return Ok(None);
    }
    Ok(Some(Region {
        fern: fern_block.start + window.fern.start..fern_block.start + window.fern.end,
        crozier: crozier_block.start + window.crozier.start
            ..crozier_block.start + window.crozier.end,
    }))
}

/// The lines inside `lines`' `if typing.TYPE_CHECKING:` block: from the line
/// after it to the next line that is neither blank nor indented.
fn type_checking_block(lines: &[&str]) -> Option<std::ops::Range<usize>> {
    let start = lines
        .iter()
        .position(|line| *line == "if typing.TYPE_CHECKING:")?
        + 1;
    let end = lines[start..]
        .iter()
        .position(|line| !line.is_empty() && !line.starts_with(' '))
        .map_or(lines.len(), |offset| start + offset);
    Some(start..end)
}

/// `lines` with one level (four spaces) of indentation removed, as one text;
/// `None` when a non-blank line is not indented that far.
fn dedent(lines: &[&str]) -> Option<String> {
    let mut out = String::new();
    for line in lines {
        if !line.is_empty() {
            out.push_str(line.strip_prefix("    ")?);
        }
        out.push('\n');
    }
    Some(out)
}

/// Run `ruff check --select I --fix` over a source string, returning the
/// import-sorted result. Uses the same `ruff` the generator depends on.
///
/// # Errors
///
/// When `ruff` cannot be run, or rejects the input.
pub fn ruff_isort(source: &str) -> Result<String, String> {
    let mut child = Command::new("ruff")
        .args([
            "check",
            "--select",
            "I",
            "--fix",
            "--stdin-filename",
            "x.py",
            "-",
        ])
        .stdin(Stdio::piped())
        .stdout(Stdio::piped())
        .stderr(Stdio::piped())
        .spawn()
        .map_err(|error| format!("could not run ruff (see docs/matching.md): {error}"))?;
    child
        .stdin
        .take()
        .ok_or_else(|| "ruff stdin was not piped".to_string())?
        .write_all(source.as_bytes())
        .map_err(|error| format!("could not write to ruff: {error}"))?;
    let out = child
        .wait_with_output()
        .map_err(|error| format!("could not wait for ruff: {error}"))?;
    // Trust ruff's stdout only when it exited cleanly — a non-zero exit (e.g. a
    // syntax error in the input) must surface, not silently yield wrong text.
    if !out.status.success() {
        return Err(format!(
            "ruff isort failed ({}): {}",
            out.status,
            String::from_utf8_lossy(&out.stderr).trim()
        ));
    }
    String::from_utf8(out.stdout).map_err(|error| format!("ruff output is not UTF-8: {error}"))
}

/// The files `readme-client-class-casing` reads: the SDK's README and its
/// endpoint reference.
const DOCS_FILES: [&str; 2] = ["README.md", "reference.md"];

/// `line` split into identifier runs and the single characters between them,
/// so two lines compare token by token.
fn tokens(line: &str) -> Vec<&str> {
    let mut out = Vec::new();
    let mut start = None;
    for (index, ch) in line.char_indices() {
        let word = ch.is_alphanumeric() || ch == '_';
        match (word, start) {
            (true, None) => start = Some(index),
            (false, Some(begun)) => {
                out.push(&line[begun..index]);
                out.push(&line[index..index + ch.len_utf8()]);
                start = None;
            }
            (false, None) => out.push(&line[index..index + ch.len_utf8()]),
            (true, Some(_)) => {}
        }
    }
    if let Some(begun) = start {
        out.push(&line[begun..]);
    }
    out
}

/// `readme-client-class-casing`: in `README.md` or `reference.md`, the two lines
/// are equal but for identifiers that differ only in letter case, and at each
/// one crozier names a class its modules define where Fern names one that
/// neither tree defines.
fn readme_client_class_casing(pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    if !DOCS_FILES.contains(&pair.rel) {
        return false;
    }
    let (fern, crozier) = (tokens(fern), tokens(crozier));
    if fern.len() != crozier.len() {
        return false;
    }
    let mut renamed = 0;
    for (fern, crozier) in fern.iter().zip(&crozier) {
        if fern == crozier {
            continue;
        }
        if !fern.eq_ignore_ascii_case(crozier)
            || !pair.context.crozier_classes().contains(*crozier)
            || pair.context.reference_classes().contains(*fern)
            || pair.context.crozier_classes().contains(*fern)
        {
            return false;
        }
        renamed += 1;
    }
    renamed > 0
}

/// `NAME` of an argument line `<indent>NAME=<value>,` whose `NAME` is one of
/// `names`.
fn lifted_argument<'l>(line: &'l str, names: &BTreeSet<String>) -> Option<&'l str> {
    let trimmed = line.trim_start();
    if trimmed.len() == line.len() || !line.ends_with(',') {
        return None;
    }
    let (name, _) = trimmed.split_once('=')?;
    names.contains(name).then_some(name)
}

/// The line opening the call whose argument list holds line `index`: the
/// nearest line above it ending in `(`.
fn call_opener<'l>(lines: &[&'l str], index: usize) -> Option<&'l str> {
    lines[..index]
        .iter()
        .rev()
        .find(|line| line.ends_with('('))
        .map(|line| line.trim_start())
}

/// Whether `opener` opens a call of an endpoint method, `client.<…>(` or
/// `await client.<…>(`, rather than the client's constructor.
fn opens_method_call(opener: &str) -> bool {
    let call = opener.strip_prefix("await ").unwrap_or(opener);
    call.starts_with("client.")
}

/// Whether `opener` opens a client constructor call, `client = <Class>(`.
fn opens_constructor_call(opener: &str) -> bool {
    opener.strip_prefix("client = ").is_some_and(|class| {
        class.strip_suffix('(').is_some_and(|name| {
            !name.is_empty() && name.chars().all(|c| c.is_alphanumeric() || c == '_')
        })
    })
}

/// The length of the `reference.md` parameter block starting at `lines[at]`
/// that documents one of `names` — `<dl>`, `<dd>`, a blank line, `**NAME:** …`,
/// a whitespace-only line, `</dd>`, `</dl>` and a blank line — if one starts
/// there.
fn lifted_parameter_block(lines: &[&str], at: usize, names: &BTreeSet<String>) -> Option<usize> {
    parameter_block(lines, at, |line| {
        line.strip_prefix("**")
            .and_then(|rest| rest.split_once(":** "))
            .is_some_and(|(name, _)| names.contains(name))
    })
}

/// The length of the `reference.md` parameter block starting at `lines[at]`
/// whose `**NAME:** …` line `documents` accepts, if one starts there.
fn parameter_block(lines: &[&str], at: usize, documents: impl Fn(&str) -> bool) -> Option<usize> {
    let block = lines.get(at..at + 8)?;
    let documented = documents(block[3]);
    (block[0] == "<dl>"
        && block[1] == "<dd>"
        && block[2].is_empty()
        && documented
        && block[4].trim().is_empty()
        && block[5] == "</dd>"
        && block[6] == "</dl>"
        && block[7].is_empty())
    .then_some(8)
}

/// Fern's documentation lines with its lifted-argument defects taken out: each
/// method call's argument line naming a lifted parameter, and each
/// `reference.md` block documenting one. `None` when there is none to take out.
fn fern_docs_without_lifted<'l>(
    lines: &[&'l str],
    names: &BTreeSet<String>,
) -> Option<Vec<&'l str>> {
    let mut kept = Vec::with_capacity(lines.len());
    let mut index = 0;
    while index < lines.len() {
        if let Some(length) = lifted_parameter_block(lines, index, names) {
            index += length;
            continue;
        }
        let in_method_call = lifted_argument(lines[index], names).is_some()
            && call_opener(lines, index).is_some_and(opens_method_call);
        if !in_method_call {
            kept.push(lines[index]);
        }
        index += 1;
    }
    (kept.len() < lines.len()).then_some(kept)
}

/// crozier's documentation lines with its lifted constructor arguments taken
/// out, a constructor call left empty closing on its opening line
/// (`client = FernApi()`), as Fern writes it. `None` when there is none.
fn crozier_docs_without_lifted(lines: &[&str], names: &BTreeSet<String>) -> Option<Vec<String>> {
    let mut kept: Vec<String> = Vec::with_capacity(lines.len());
    let mut removed = false;
    for (index, line) in lines.iter().enumerate() {
        if lifted_argument(line, names).is_some()
            && call_opener(lines, index).is_some_and(opens_constructor_call)
        {
            removed = true;
            continue;
        }
        let closes_empty = *line == ")"
            && kept
                .last()
                .is_some_and(|opener| opens_constructor_call(opener));
        match kept.last_mut() {
            Some(opener) if closes_empty => opener.push(')'),
            _ => kept.push((*line).to_string()),
        }
    }
    removed.then_some(kept)
}

/// `lifted-base-path-docs-examples`: in `README.md` or `reference.md`, Fern's
/// file is crozier's once three things move back to where Fern puts them —
/// every lifted base-path parameter crozier passes to the client constructor
/// leaves it (a constructor left empty closes on its own line,
/// `client = FernApi()`), and Fern's method calls passing a lifted parameter and
/// `reference.md` blocks documenting one under a method are set aside. Both
/// sides must carry the construct. The region is the two files' differing
/// window, so any other difference in the file is left unexplained.
fn lifted_base_path_docs_examples(pair: &Pair<'_>) -> Result<Option<Region>, String> {
    if !DOCS_FILES.contains(&pair.rel) {
        return Ok(None);
    }
    let names = pair.context.crozier_lifted_parameters();
    if names.is_empty() {
        return Ok(None);
    }
    let (Some(fern), Some(crozier)) = (
        fern_docs_without_lifted(pair.fern, names),
        crozier_docs_without_lifted(pair.crozier, names),
    ) else {
        return Ok(None);
    };
    if fern.len() != crozier.len()
        || fern
            .iter()
            .zip(&crozier)
            .any(|(left, right)| *left != right)
    {
        return Ok(None);
    }
    Ok(differing_window(pair.fern, pair.crozier))
}

/// The names Fern's Markdown gives the header `wire`: its parameter stem (`X-`
/// dropped) and its whole name, each snake-cased.
fn header_doc_names(wire: &str) -> [String; 2] {
    [
        crate::naming::field_name(crate::ir::header_param_stem(wire)),
        crate::naming::field_name(wire)
            .trim_end_matches('_')
            .to_string(),
    ]
}

/// `constant-header-docs-arguments`: in `README.md` or `reference.md`, Fern's
/// file is crozier's but for the headers crozier's raw clients send as
/// constants: every method call line passing one its constant,
/// `<indent>NAME="<value>",`, and every `reference.md` block documenting one as
/// `**NAME:** \`typing.Literal\``. Both are set aside, and the rest must equal
/// crozier's file; the region is the two files' differing window.
fn constant_header_docs_arguments(pair: &Pair<'_>) -> Result<Option<Region>, String> {
    if !DOCS_FILES.contains(&pair.rel) {
        return Ok(None);
    }
    let constants = pair.context.crozier_constant_headers();
    if constants.is_empty() {
        return Ok(None);
    }
    let passed: BTreeSet<String> = constants
        .iter()
        .flat_map(|(wire, value)| header_doc_names(wire).map(|name| format!("{name}=\"{value}\",")))
        .collect();
    let documented: BTreeSet<String> = constants
        .iter()
        .flat_map(|(wire, _)| header_doc_names(wire))
        .collect();
    let lines = pair.fern;
    let mut kept: Vec<String> = Vec::with_capacity(lines.len());
    let mut removed = false;
    let mut index = 0;
    while index < lines.len() {
        let block = parameter_block(lines, index, |line| {
            line.strip_prefix("**")
                .and_then(|rest| rest.split_once(":** `typing.Literal`"))
                .is_some_and(|(name, after)| {
                    documented.contains(name) && (after == " " || after.starts_with(" — "))
                })
        });
        if let Some(length) = block {
            index += length;
            removed = true;
            continue;
        }
        let passes_constant = passed.contains(lines[index].trim_start())
            && lines[index].len() > lines[index].trim_start().len()
            && call_opener(lines, index).is_some_and(opens_method_call);
        if passes_constant {
            removed = true;
        } else {
            // A method call the constants were the only arguments of closes on
            // its opening line, as crozier writes it.
            let line = lines[index];
            let indent = &line[..line.len() - line.trim_start().len()];
            let closes_empty = line.trim_start() == ")"
                && kept.last().is_some_and(|opener| {
                    opener.ends_with('(')
                        && opener.starts_with(indent)
                        && opens_method_call(opener.trim_start())
                });
            match kept.last_mut() {
                Some(opener) if closes_empty => opener.push(')'),
                _ => kept.push(line.to_string()),
            }
        }
        index += 1;
    }
    if !removed
        || kept.len() != pair.crozier.len()
        || kept
            .iter()
            .zip(pair.crozier)
            .any(|(left, right)| left != right)
    {
        return Ok(None);
    }
    Ok(differing_window(pair.fern, pair.crozier))
}

/// `nullable-items-docs`: in `README.md` or `reference.md`, Fern's file is
/// crozier's once each query parameter Fern's `reference.md` documents with
/// nullable items is written Fern's way — its type with the items' `Optional`
/// restored, and each element of its worked list `None` — and both sides carry
/// the construct. The region is the two files' differing window.
fn nullable_items_docs(pair: &Pair<'_>) -> Result<Option<Region>, String> {
    if !DOCS_FILES.contains(&pair.rel) {
        return Ok(None);
    }
    let names = pair.context.reference_nullable_items();
    if names.is_empty() {
        return Ok(None);
    }
    let mut fern_form: Vec<String> = Vec::with_capacity(pair.crozier.len());
    let mut list: Option<String> = None;
    for line in pair.crozier {
        if let Some(close) = &list {
            if *line == close {
                list = None;
                fern_form.push((*line).to_string());
            } else {
                let indent = &line[..line.len() - line.trim_start().len()];
                fern_form.push(format!("{indent}None"));
            }
            continue;
        }
        let trimmed = line.trim_start();
        let indent = &line[..line.len() - trimmed.len()];
        if let Some(name) = trimmed.strip_suffix("=[") {
            if names.contains(name) {
                list = Some(format!("{indent}],"));
            }
            fern_form.push((*line).to_string());
            continue;
        }
        let restored = documented_parameter(line).and_then(|(name, annotation)| {
            if !names.contains(name) {
                return None;
            }
            let item = annotation
                .strip_prefix("typing.Optional[typing.Union[")?
                .split_once(", typing.Sequence[")?
                .0;
            let (fern, crozier) = nullable_items_types(item);
            (crozier == annotation).then(|| line.replacen(&crozier, &fern, 1))
        });
        fern_form.push(restored.unwrap_or_else(|| (*line).to_string()));
    }
    if fern_form.len() != pair.fern.len()
        || fern_form
            .iter()
            .zip(pair.fern)
            .any(|(left, right)| left != right)
        || fern_form
            .iter()
            .zip(pair.crozier)
            .all(|(left, right)| left == right)
    {
        return Ok(None);
    }
    Ok(differing_window(pair.fern, pair.crozier))
}

/// `lifted-base-path-positional-example`: in a `.py` file, Fern's line passes a
/// string positionally, `<indent>"<value>",`, where crozier's line passes the
/// same string by the keyword of a lifted base-path parameter,
/// `<indent>NAME="<value>",`.
fn lifted_base_path_positional_example(pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    if !pair.rel.ends_with(".py") {
        return false;
    }
    let Some(name) = lifted_argument(crozier, pair.context.crozier_lifted_parameters()) else {
        return false;
    };
    let indent = &crozier[..crozier.len() - crozier.trim_start().len()];
    let value = &crozier.trim_start()[name.len() + 1..];
    value.starts_with('"') && fern.strip_prefix(indent) == Some(value)
}

/// Whether `rel` is an SDK's client wrapper, where the identity headers are set.
fn is_client_wrapper(rel: &str) -> bool {
    rel == "core/client_wrapper.py" || rel.ends_with("/core/client_wrapper.py")
}

/// `sdk-identity-header-prefix`: in the client wrapper, crozier's line is Fern's
/// `"X-Fern-…"` header line with the prefix `X-Crozier-` and nothing else
/// changed.
fn sdk_identity_header_prefix(pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    is_client_wrapper(pair.rel)
        && fern.trim_start().starts_with("\"X-Fern-")
        && fern.replacen("\"X-Fern-", "\"X-Crozier-", 1) == crozier
}

/// `(indentation, header, value)` of a client-wrapper header line
/// `<indent>"<prefix>SDK-<Name|Version>": <value>,` whose prefix is `prefix`.
fn identity_pair_line<'l>(line: &'l str, prefix: &str) -> Option<(&'l str, &'l str, &'l str)> {
    let indent = &line[..line.len() - line.trim_start().len()];
    let rest = line.trim_start().strip_prefix('"')?.strip_prefix(prefix)?;
    let (header, value) = ["SDK-Name\": ", "SDK-Version\": "]
        .iter()
        .find_map(|header| rest.strip_prefix(header).map(|value| (*header, value)))?;
    let value = value.strip_suffix(',')?;
    (value.len() >= 2 && value.starts_with('"') && value.ends_with('"'))
        .then_some((indent, header, value))
}

/// Whether `value` is exactly what crozier writes on its `header` identity
/// line: its project name, as its `pyproject.toml` declares it, or its fixed
/// packaged version.
fn is_crozier_identity_value(pair: &Pair<'_>, header: &str, value: &str) -> bool {
    let expected = if header.starts_with("SDK-Name") {
        match pair.context.crozier_project() {
            Some(project) => format!("\"{project}\""),
            None => return false,
        }
    } else {
        format!("\"{}\"", crate::emit::DEFAULT_SDK_VERSION)
    };
    value == expected
}

/// `sdk-name-version-headers`, aligned half: in the client wrapper, Fern's
/// `X-Fern-SDK-Name`/`-Version` line and crozier's `X-Crozier-` one name the
/// same header at the same indentation with different string values, crozier's
/// being exactly its project name or its fixed packaged version.
fn sdk_name_version_header(pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    if !is_client_wrapper(pair.rel) {
        return false;
    }
    match (
        identity_pair_line(fern, "X-Fern-"),
        identity_pair_line(crozier, "X-Crozier-"),
    ) {
        (Some(fern), Some(crozier)) => {
            fern.0 == crozier.0
                && fern.1 == crozier.1
                && fern.2 != crozier.2
                && is_crozier_identity_value(pair, crozier.1, crozier.2)
        }
        _ => false,
    }
}

/// `sdk-name-version-headers`, added half: in the client wrapper, crozier
/// writes an `X-Crozier-SDK-Name`/`-Version` line, carrying exactly its project
/// name or its fixed packaged version, where the reference has none.
fn sdk_name_version_header_added(pair: &Pair<'_>, crozier: &str) -> bool {
    is_client_wrapper(pair.rel)
        && identity_pair_line(crozier, "X-Crozier-")
            .is_some_and(|(_, header, value)| is_crozier_identity_value(pair, header, value))
        && !pair
            .fern
            .iter()
            .any(|line| identity_pair_line(line, "X-Fern-").is_some())
}

#[cfg(test)]
mod tests {
    use super::*;

    fn pair<'a>(rel: &'a str, fern: &'a [&'a str], crozier: &'a [&'a str]) -> Pair<'a> {
        static EMPTY: OnceLock<Context> = OnceLock::new();
        Pair {
            rel,
            fern,
            crozier,
            context: EMPTY.get_or_init(Context::default),
        }
    }

    #[test]
    fn the_compiled_catalog_is_valid_and_every_entry_has_a_rule() {
        let entries = parse(CATALOG_SOURCE).unwrap_or_else(|failures| panic!("{failures:#?}"));
        assert_eq!(
            entries
                .iter()
                .map(|entry| entry.id.as_str())
                .collect::<Vec<_>>(),
            RULE_IDS
        );
        assert_eq!(catalog(), entries.as_slice());
        assert!(find("readme-client-class-casing").is_some());
        assert!(find("no-such-departure").is_none());
        assert!(entries.iter().any(|entry| entry.kind == Kind::FernDefect));
    }

    /// The evidence notes are committed beside the catalog.
    #[test]
    fn every_evidence_note_is_committed() {
        let root = std::path::Path::new(env!("CARGO_MANIFEST_DIR"));
        for entry in catalog() {
            assert!(
                root.join(&entry.evidence).is_file(),
                "departure `{}`: evidence {} is not committed",
                entry.id,
                entry.evidence
            );
        }
    }

    fn entry_text(id: &str, kind: &str, evidence: &str) -> String {
        let keys = "  trigger: t\n  fern: f\n  crozier: c\n  reason: r\n";
        format!("- id: {id}\n  kind: {kind}\n{keys}  evidence: {evidence}\n")
    }

    fn failures_of(text: &str) -> Vec<String> {
        parse(text).expect_err("the catalog is refused")
    }

    fn assert_refused(text: &str, says: &str) {
        let failures = failures_of(text);
        assert!(
            failures.iter().any(|failure| failure.contains(says)),
            "expected a failure saying {says:?}: {failures:#?}"
        );
    }

    #[test]
    fn a_broken_catalog_is_refused_naming_the_entry() {
        let evidence = "docs/departures/evidence/x.md";
        let good = |id: &str| entry_text(id, "branding", evidence);
        // Out of order, duplicated.
        assert_refused(
            &format!(
                "{}{}",
                good("sdk-name-version-headers"),
                good("sdk-identity-header-prefix")
            ),
            "departure `sdk-identity-header-prefix`: follows `sdk-name-version-headers`",
        );
        assert_refused(
            &format!(
                "{}{}",
                good("sdk-identity-header-prefix"),
                good("sdk-identity-header-prefix")
            ),
            "the id appears twice",
        );
        // Not a slug, no rule, a rule with no entry.
        assert_refused(&good("Not_A_Slug"), "departure `Not_A_Slug`: the id is not");
        assert_refused(&good("unruled-departure"), "no rule of that id");
        assert_refused(
            &good("sdk-identity-header-prefix"),
            "departure rule `readme-client-class-casing` has no catalog entry",
        );
        // An empty field, evidence elsewhere.
        assert_refused(
            &good("sdk-identity-header-prefix").replace("reason: r", "reason: ''"),
            "`reason` is empty",
        );
        for evidence in ["docs/elsewhere/x.md", "docs/departures/evidence/../x.md"] {
            assert_refused(
                &entry_text("sdk-identity-header-prefix", "branding", evidence),
                "is not a note under docs/departures/evidence/",
            );
        }
        // An unknown kind or key, a missing key.
        assert_refused(
            &entry_text("sdk-identity-header-prefix", "cosmetic", evidence),
            "holding exactly the keys id, kind, trigger, fern, crozier, reason, evidence",
        );
        assert_refused(
            &format!("{}  extra: x\n", good("sdk-identity-header-prefix")),
            "unknown field `extra`",
        );
        assert_refused(
            &good("sdk-identity-header-prefix").replace("  fern: f\n", ""),
            "missing field `fern`",
        );
    }

    #[test]
    fn the_reference_renders_every_kind_and_entry() {
        let rendered = render_reference(catalog());
        assert!(rendered.starts_with(REFERENCE_MARKERS.0), "{rendered}");
        assert!(
            rendered.trim_end().ends_with(REFERENCE_MARKERS.1),
            "{rendered}"
        );
        for kind in Kind::ALL {
            assert!(rendered.contains(&format!("| `{}` |", kind.as_str())));
        }
        for entry in catalog() {
            assert!(rendered.contains(&format!("### `{}`", entry.id)));
            assert!(rendered.contains(&format!("(../../{})", entry.evidence)));
        }
    }

    /// `docs/departures/README.md` holds the rendered catalog. When the catalog
    /// changes, regenerate it with
    /// `CROZIER_UPDATE_DEPARTURES=1 cargo test --lib departures`.
    #[test]
    fn the_rendered_reference_is_current() {
        let path =
            std::path::Path::new(env!("CARGO_MANIFEST_DIR")).join("docs/departures/README.md");
        let page = std::fs::read_to_string(&path).expect("docs/departures/README.md");
        let (begin, end) = REFERENCE_MARKERS;
        let (Some(start), Some(stop)) = (page.find(begin), page.find(end)) else {
            panic!("docs/departures/README.md holds no generated catalog markers");
        };
        let committed = &page[start..stop + end.len() + 1];
        let rendered = render_reference(catalog());
        if std::env::var_os("CROZIER_UPDATE_DEPARTURES").is_some() {
            std::fs::write(&path, page.replacen(committed, &rendered, 1)).unwrap();
            return;
        }
        assert!(
            committed == rendered,
            concat!(
                "docs/departures/README.md's catalog differs from assets/departures.yml; ",
                "regenerate it with `CROZIER_UPDATE_DEPARTURES=1 cargo test --lib departures`"
            )
        );
    }

    #[test]
    fn classes_are_read_from_top_level_python_class_lines_only() {
        let context = Context::from_sources(
            [
                (
                    "client.py",
                    "class Acme:\n    class Inner:\nclass Async_2(x):\n",
                ),
                ("README.md", "class Ignored:\n"),
            ],
            [("a.py", "class  Spaced:\nclass :\n")],
        );
        assert_eq!(
            context.reference_classes(),
            &BTreeSet::from(["Acme".to_string(), "Async_2".to_string()])
        );
        assert!(context.crozier_classes().is_empty());
        // Two trees on disk are read on first use; without trees, nothing.
        let reference = tempfile::tempdir().unwrap();
        let crozier = tempfile::tempdir().unwrap();
        std::fs::create_dir_all(reference.path().join("pkg")).unwrap();
        std::fs::write(reference.path().join("pkg/client.py"), "class Acme:\n").unwrap();
        std::fs::write(reference.path().join("README.md"), "class Not:\n").unwrap();
        let trees = Context::from_trees(reference.path(), crozier.path());
        assert_eq!(
            trees.reference_classes(),
            &BTreeSet::from(["Acme".to_string()])
        );
        assert!(trees.crozier_classes().is_empty());
        assert!(Context::default().reference_classes().is_empty());
    }

    #[test]
    fn the_casing_rule_holds_only_where_crozier_names_the_defined_class() {
        let context = Context::from_sources(
            [("client.py", "class LanternHarborApi:\n")],
            [("client.py", "class LanternHarborApi:\n")],
        );
        let lines: [&str; 0] = [];
        let pair = Pair {
            rel: "README.md",
            fern: &lines,
            crozier: &lines,
            context: &context,
        };
        let holds = |fern: &str, crozier: &str| readme_client_class_casing(&pair, fern, crozier);
        assert!(holds(
            "from LanternHarbor import LanternharborApi",
            "from LanternHarbor import LanternHarborApi"
        ));
        // Anything else on the line differing, a different word, the same
        // line, or Fern's name being defined: not this departure.
        assert!(!holds(
            "from LanternHarbor import LanternharborApi",
            "from LanternHarbor import LanternHarborApi, X"
        ));
        assert!(!holds(
            "client = LanternharborApi()",
            "client = LanternHarborApi( )"
        ));
        assert!(!holds("x = Lanternharbor", "x = LanternHarbor"));
        assert!(!holds("x = LanternHarborApi", "x = LanternHarborApi"));
        assert!(!holds("x = LanternHarborApi", "x = lanternharborapi"));
        let defined = Context::from_sources(
            [(
                "client.py",
                "class LanternharborApi:\nclass LanternHarborApi:\n",
            )],
            [("client.py", "class LanternHarborApi:\n")],
        );
        let pair = Pair {
            context: &defined,
            ..pair
        };
        assert!(!readme_client_class_casing(
            &pair,
            "x = LanternharborApi",
            "x = LanternHarborApi"
        ));
        // Only the README and the endpoint reference.
        let other = Pair {
            rel: "docs/README.md",
            context: &context,
            ..pair
        };
        assert!(!readme_client_class_casing(
            &other,
            "x = LanternharborApi",
            "x = LanternHarborApi"
        ));
    }

    /// A context whose crozier tree's routes read `edition` from the client.
    fn lifted_context() -> Context {
        Context::from_sources(
            [],
            [(
                "src/acme/layers/raw_client.py",
                "f\"{encode_path_param(self._client_wrapper._edition)}/layers\",\n",
            )],
        )
    }

    #[test]
    fn lifted_parameters_are_read_from_routes_reading_the_client_wrapper() {
        assert_eq!(
            lifted_context().crozier_lifted_parameters(),
            &BTreeSet::from(["edition".to_string()])
        );
        // An attribute read anywhere else, or not closed at once: none.
        let other = Context::from_sources(
            [("a.py", "encode_path_param(self._client_wrapper._edition)\n")],
            [
                ("README.md", "encode_path_param(self._client_wrapper._a)\n"),
                (
                    "b.py",
                    "self._client_wrapper._b\nencode_path_param(self._client_wrapper._c.x)\n",
                ),
            ],
        );
        assert!(other.crozier_lifted_parameters().is_empty());
        let crozier = tempfile::tempdir().unwrap();
        std::fs::write(
            crozier.path().join("raw_client.py"),
            "encode_path_param(self._client_wrapper._tenant)\n",
        )
        .unwrap();
        let reference = tempfile::tempdir().unwrap();
        assert_eq!(
            Context::from_trees(reference.path(), crozier.path()).crozier_lifted_parameters(),
            &BTreeSet::from(["tenant".to_string()])
        );
        assert!(Context::default().crozier_lifted_parameters().is_empty());
    }

    const LIFTED_FERN: &str = "client = FernApi()\n\nclient.layers.create_layer(\n    edition=\"v2\",\n    title=\"title\",\n)\n\n<dl>\n<dd>\n\n**edition:** `str` \n    \n</dd>\n</dl>\n\n<dl>\n<dd>\n\n**request:** `Layer` \n";
    const LIFTED_CROZIER: &str = "client = FernApi(\n    edition=\"v2\",\n)\n\nclient.layers.create_layer(\n    title=\"title\",\n)\n\n<dl>\n<dd>\n\n**request:** `Layer` \n";

    fn docs_region(rel: &str, fern: &str, crozier: &str, context: &Context) -> Option<Region> {
        let fern: Vec<&str> = fern.split('\n').collect();
        let crozier: Vec<&str> = crozier.split('\n').collect();
        let pair = Pair {
            rel,
            fern: &fern,
            crozier: &crozier,
            context,
        };
        lifted_base_path_docs_examples(&pair).unwrap()
    }

    #[test]
    fn the_lifted_docs_rule_takes_exactly_the_three_constructs() {
        let context = lifted_context();
        assert_eq!(
            docs_region("reference.md", LIFTED_FERN, LIFTED_CROZIER, &context),
            Some(Region {
                fern: 0..14,
                crozier: 0..7,
            })
        );
        // The required form: crozier adds the argument to a constructor that
        // keeps another, and an awaited method call loses it.
        assert!(docs_region(
            "README.md",
            "client = AsyncFernApi(\n    environment=E,\n)\n    await client.layers.get(\n        edition=\"edition\",\n    )",
            "client = AsyncFernApi(\n    edition=\"YOUR_EDITION\",\n    environment=E,\n)\n    await client.layers.get(\n    )",
            &context,
        )
        .is_some());
        // One more line differing anywhere, another argument only Fern passes,
        // a lifted argument crozier passes to a method, or a name the routes do
        // not lift: not this.
        for (fern, crozier) in [
            (format!("{LIFTED_FERN}x"), format!("{LIFTED_CROZIER}y")),
            (
                LIFTED_FERN.replace("    title=", "    opacity=1,\n    title="),
                LIFTED_CROZIER.to_string(),
            ),
            (
                LIFTED_FERN.to_string(),
                LIFTED_CROZIER.replace("    title=", "    edition=\"v2\",\n    title="),
            ),
            (
                LIFTED_FERN.replace("**edition:**", "**tenant:**"),
                LIFTED_CROZIER.to_string(),
            ),
            (
                LIFTED_FERN.to_string(),
                LIFTED_CROZIER.replace("    edition=\"v2\",\n", "    tenant=\"v2\",\n"),
            ),
            (
                LIFTED_FERN.replace("client = FernApi()", "client = FernApi(1)"),
                LIFTED_CROZIER.to_string(),
            ),
        ] {
            assert_eq!(
                docs_region("reference.md", &fern, &crozier, &context),
                None,
                "{fern}\n---\n{crozier}"
            );
        }
        // Only the README and the endpoint reference, only with lifted
        // parameters, and only where both sides carry the construct.
        assert_eq!(
            docs_region("client.py", LIFTED_FERN, LIFTED_CROZIER, &context),
            None
        );
        assert_eq!(
            docs_region(
                "README.md",
                LIFTED_FERN,
                LIFTED_CROZIER,
                &Context::default()
            ),
            None
        );
        assert_eq!(
            docs_region("README.md", LIFTED_FERN, LIFTED_FERN, &context),
            None
        );
        assert_eq!(
            docs_region("README.md", LIFTED_CROZIER, LIFTED_CROZIER, &context),
            None
        );
    }

    #[test]
    fn the_positional_rule_takes_only_the_lifted_keyword_with_the_same_value() {
        let context = lifted_context();
        let lines: [&str; 0] = [];
        let pair = Pair {
            rel: "src/acme/client.py",
            fern: &lines,
            crozier: &lines,
            context: &context,
        };
        let holds =
            |fern: &str, crozier: &str| lifted_base_path_positional_example(&pair, fern, crozier);
        assert!(holds("        \"v2\",", "        edition=\"v2\","));
        assert!(!holds("        \"v3\",", "        edition=\"v2\","));
        assert!(!holds("    \"v2\",", "        edition=\"v2\","));
        assert!(!holds("        \"v2\",", "        tenant=\"v2\","));
        assert!(!holds("        edition=\"v2\",", "        edition=\"v2\","));
        assert!(!holds("        2,", "        edition=2,"));
        assert!(!holds("\"v2\",", "edition=\"v2\","));
        let readme = Pair {
            rel: "README.md",
            ..pair
        };
        assert!(!lifted_base_path_positional_example(
            &readme,
            "    \"v2\",",
            "    edition=\"v2\","
        ));
    }

    fn region_of(
        rule: RegionRule,
        rel: &str,
        fern: &str,
        crozier: &str,
        context: &Context,
    ) -> Option<Region> {
        let fern: Vec<&str> = fern.split('\n').collect();
        let crozier: Vec<&str> = crozier.split('\n').collect();
        rule(&Pair {
            rel,
            fern: &fern,
            crozier: &crozier,
            context,
        })
        .unwrap()
    }

    #[test]
    fn constant_headers_are_read_from_raw_client_header_dicts() {
        let context = Context::from_sources(
            [],
            [
                (
                    "src/acme/beds/raw_client.py",
                    "json={\n    \"kind\": \"x\",\n},\nheaders={\n    \"X-Mist-Mode\": \"fine\",\n    \"X-Vent\": str(vent) if vent is not None else None,\n},\n",
                ),
                ("src/acme/client.py", "headers={\n    \"X-Other\": \"y\",\n},\n"),
            ],
        );
        assert_eq!(
            context.crozier_constant_headers(),
            &BTreeSet::from([("X-Mist-Mode".to_string(), "fine".to_string())])
        );
        assert!(Context::default().crozier_constant_headers().is_empty());
        let crozier = tempfile::tempdir().unwrap();
        std::fs::write(
            crozier.path().join("raw_client.py"),
            "headers={\n    \"storage-unit\": \"GB\",\n},\n",
        )
        .unwrap();
        let reference = tempfile::tempdir().unwrap();
        assert_eq!(
            Context::from_trees(reference.path(), crozier.path()).crozier_constant_headers(),
            &BTreeSet::from([("storage-unit".to_string(), "GB".to_string())])
        );
    }

    const CONSTANT_FERN: &str = "client.beds.list_beds(\n    section=\"section\",\n    mist_mode=\"fine\",\n)\n\n<dl>\n<dd>\n\n**mist_mode:** `typing.Literal` — How fine.\n    \n</dd>\n</dl>\n\n<dl>\n<dd>\n\n**section:** `str` \n";
    const CONSTANT_CROZIER: &str = "client.beds.list_beds(\n    section=\"section\",\n)\n\n<dl>\n<dd>\n\n**section:** `str` \n";

    #[test]
    fn the_constant_header_docs_rule_takes_only_the_constants_arguments_and_blocks() {
        let context = Context::from_sources(
            [],
            [(
                "raw_client.py",
                "headers={\n    \"X-Mist-Mode\": \"fine\",\n},\n",
            )],
        );
        let rule: RegionRule = constant_header_docs_arguments;
        assert!(region_of(
            rule,
            "reference.md",
            CONSTANT_FERN,
            CONSTANT_CROZIER,
            &context
        )
        .is_some());
        for (fern, crozier) in [
            // Another value, another argument, one more difference, an
            // argument to the constructor, a block typed otherwise.
            (
                CONSTANT_FERN.replace("=\"fine\"", "=\"coarse\""),
                CONSTANT_CROZIER.to_string(),
            ),
            (
                CONSTANT_FERN.replace("    mist_mode", "    fan_speed=3,\n    mist_mode"),
                CONSTANT_CROZIER.to_string(),
            ),
            (format!("{CONSTANT_FERN}x"), format!("{CONSTANT_CROZIER}y")),
            (
                CONSTANT_FERN.replace("client.beds.list_beds(", "client = FernApi("),
                CONSTANT_CROZIER.replace("client.beds.list_beds(", "client = FernApi("),
            ),
            (
                CONSTANT_FERN.replace("`typing.Literal`", "`str`"),
                CONSTANT_CROZIER.to_string(),
            ),
        ] {
            assert_eq!(
                region_of(rule, "reference.md", &fern, &crozier, &context),
                None,
                "{fern}"
            );
        }
        // A call the constant was the only argument of closes on its own line;
        // a constructor never takes one.
        assert!(region_of(
            rule,
            "README.md",
            "client.beds.count_beds(\n    mist_mode=\"fine\",\n)",
            "client.beds.count_beds()",
            &context
        )
        .is_some());
        assert_eq!(
            region_of(
                rule,
                "README.md",
                "client = FernApi(\n    mist_mode=\"fine\",\n)",
                "client = FernApi()",
                &context
            ),
            None
        );
        assert_eq!(
            region_of(rule, "client.py", CONSTANT_FERN, CONSTANT_CROZIER, &context),
            None
        );
        assert_eq!(
            region_of(
                rule,
                "README.md",
                CONSTANT_FERN,
                CONSTANT_CROZIER,
                &Context::default()
            ),
            None
        );
        assert_eq!(
            region_of(rule, "README.md", CONSTANT_FERN, CONSTANT_FERN, &context),
            None
        );
    }

    const NULLABLE_FERN: &str = "client.beds.list_beds(\n    rows=[\n        None\n    ],\n)\n\n**rows:** `typing.Optional[typing.Union[typing.Optional[int], typing.Sequence[typing.Optional[int]]]]` \n";
    const NULLABLE_CROZIER: &str = "client.beds.list_beds(\n    rows=[\n        1\n    ],\n)\n\n**rows:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` \n";

    #[test]
    fn the_nullable_items_rule_takes_only_the_documented_parameters() {
        let context = Context::from_sources([("reference.md", NULLABLE_FERN)], []);
        assert_eq!(
            context.reference_nullable_items(),
            &BTreeSet::from(["rows".to_string()])
        );
        let rule: RegionRule = nullable_items_docs;
        assert!(region_of(
            rule,
            "reference.md",
            NULLABLE_FERN,
            NULLABLE_CROZIER,
            &context
        )
        .is_some());
        // The README carries only the worked call.
        let call = |text: &str| text.split("\n\n").next().unwrap().to_string();
        assert!(region_of(
            rule,
            "README.md",
            &call(NULLABLE_FERN),
            &call(NULLABLE_CROZIER),
            &context
        )
        .is_some());
        for (fern, crozier) in [
            // Another parameter, another type, one more difference, the same
            // file on both sides.
            (
                NULLABLE_FERN.replace("rows", "pots"),
                NULLABLE_CROZIER.replace("rows", "pots"),
            ),
            (
                NULLABLE_FERN.to_string(),
                NULLABLE_CROZIER.replace(
                    "typing.Union[int, typing.Sequence[int]]",
                    "typing.Sequence[int]",
                ),
            ),
            (format!("{NULLABLE_FERN}x"), format!("{NULLABLE_CROZIER}y")),
            (NULLABLE_FERN.to_string(), NULLABLE_FERN.to_string()),
        ] {
            assert_eq!(
                region_of(rule, "reference.md", &fern, &crozier, &context),
                None,
                "{fern}"
            );
        }
        assert_eq!(
            region_of(rule, "client.py", NULLABLE_FERN, NULLABLE_CROZIER, &context),
            None
        );
        assert!(Context::default().reference_nullable_items().is_empty());
        let reference = tempfile::tempdir().unwrap();
        std::fs::write(reference.path().join("reference.md"), NULLABLE_FERN).unwrap();
        let crozier = tempfile::tempdir().unwrap();
        assert_eq!(
            Context::from_trees(reference.path(), crozier.path()).reference_nullable_items(),
            &BTreeSet::from(["rows".to_string()])
        );
    }

    #[test]
    fn the_closed_empty_object_rule_recognises_only_the_placeholder_and_its_correction() {
        let holds = |fern: &str, crozier: &str| {
            closed_empty_object_example_line(&pair("src/fern/client.py", &[], &[]), fern, crozier)
        };
        assert!(holds(
            "            profile={\"key\": \"value\"},",
            "            profile={},"
        ));
        // Another value on either side, another keyword, or another indent.
        assert!(!holds(
            "            profile={\"key\": 1},",
            "            profile={},"
        ));
        assert!(!holds(
            "            profile={\"key\": \"value\"},",
            "            profile={\"key\": \"value\"},"
        ));
        assert!(!holds(
            "            profile={\"key\": \"value\"},",
            "            notes={},"
        ));
        assert!(!holds(
            "            profile={\"key\": \"value\"},",
            "    profile={},"
        ));
        assert!(!holds(
            "            1x={\"key\": \"value\"},",
            "            1x={},"
        ));

        // The docs' region: from the first three-line placeholder to the last,
        // everything between equal once each placeholder is collapsed.
        let fern = [
            "client.firings.schedule_firing(",
            "    kiln=\"kiln\",",
            "    profile={",
            "        \"key\": \"value\"",
            "    },",
            ")",
            "await client.firings.schedule_firing(",
            "    profile={",
            "        \"key\": \"value\"",
            "    },",
            ")",
        ];
        let crozier = [
            "client.firings.schedule_firing(",
            "    kiln=\"kiln\",",
            "    profile={},",
            ")",
            "await client.firings.schedule_firing(",
            "    profile={},",
            ")",
        ];
        assert_eq!(
            closed_empty_object_example_region(&pair("README.md", &fern, &crozier)),
            Ok(Some(Region {
                fern: 2..10,
                crozier: 2..6
            }))
        );
        // Only the README and the endpoint reference.
        assert_eq!(
            closed_empty_object_example_region(&pair("src/fern/client.py", &fern, &crozier)),
            Ok(None)
        );
        // Anything else differing inside the region, or a placeholder crozier
        // keeps, is not this departure.
        let mut other = crozier;
        other[3] = ");";
        assert_eq!(
            closed_empty_object_example_region(&pair("README.md", &fern, &other)),
            Ok(None)
        );
        let open = ["    profile={", "        \"key\": \"value\"", "    },"];
        assert_eq!(
            closed_empty_object_example_region(&pair("reference.md", &open, &open)),
            Ok(None)
        );
        let nested = ["    profile={", "        \"key\": 1", "    },"];
        assert_eq!(
            closed_empty_object_example_region(&pair(
                "reference.md",
                &nested,
                &["    profile={},"]
            )),
            Ok(None)
        );
    }

    #[test]
    fn the_header_rules_recognise_only_identity_header_lines() {
        let lines: [&str; 0] = [];
        let wrapper = pair("src/acme/core/client_wrapper.py", &lines, &lines);
        assert!(sdk_identity_header_prefix(
            &wrapper,
            "    \"X-Fern-Language\": \"Python\",",
            "    \"X-Crozier-Language\": \"Python\","
        ));
        assert!(!sdk_identity_header_prefix(
            &wrapper,
            "    \"X-Fern-Language\": \"Python\",",
            "    \"X-Crozier-Language\": \"Pythn\","
        ));
        assert!(!sdk_identity_header_prefix(
            &pair("client.py", &lines, &lines),
            "\"X-Fern-Language\": \"Python\",",
            "\"X-Crozier-Language\": \"Python\","
        ));
        assert!(!sdk_identity_header_prefix(&wrapper, "x = 1", "x = 1"));
    }

    /// A client-wrapper pair whose crozier tree declares the project `acme`.
    fn wrapper_pair<'a>(rel: &'a str, fern: &'a [&'a str]) -> Pair<'a> {
        static PROJECT: OnceLock<Context> = OnceLock::new();
        Pair {
            rel,
            fern,
            crozier: &[],
            context: PROJECT.get_or_init(|| {
                Context::from_sources([], [("pyproject.toml", "[project]\nname = \"acme\"\n")])
            }),
        }
    }

    #[test]
    fn the_sdk_pair_rule_takes_only_crozier_s_own_name_and_fixed_version() {
        let wrapper = wrapper_pair("src/acme/core/client_wrapper.py", &[]);
        assert!(sdk_name_version_header(
            &wrapper,
            "    \"X-Fern-SDK-Version\": \"1.4.2\",",
            "    \"X-Crozier-SDK-Version\": \"0.0.0\","
        ));
        assert!(sdk_name_version_header(
            &wrapper,
            "    \"X-Fern-SDK-Name\": \"acme-sdk\",",
            "    \"X-Crozier-SDK-Name\": \"acme\","
        ));
        // crozier's value is exactly its fixed version and its project name;
        // the same value is the prefix rule's; another header, indentation or
        // shape is no departure.
        for (fern, crozier) in [
            (
                "\"X-Fern-SDK-Version\": \"1.4.2\",",
                "\"X-Crozier-SDK-Version\": \"9.9.9\",",
            ),
            (
                "\"X-Fern-SDK-Name\": \"a\",",
                "\"X-Crozier-SDK-Name\": \"other\",",
            ),
            (
                "\"X-Fern-SDK-Name\": \"acme\",",
                "\"X-Crozier-SDK-Name\": \"acme\",",
            ),
            (
                "\"X-Fern-SDK-Name\": \"a\",",
                "\"X-Crozier-SDK-Version\": \"0.0.0\",",
            ),
            (
                "  \"X-Fern-SDK-Name\": \"a\",",
                "\"X-Crozier-SDK-Name\": \"acme\",",
            ),
            (
                "\"X-Fern-SDK-Name\": a,",
                "\"X-Crozier-SDK-Name\": \"acme\",",
            ),
            (
                "\"X-Fern-SDK-Name\": \"a\"",
                "\"X-Crozier-SDK-Name\": \"acme\"",
            ),
            (
                "\"X-Fern-Language\": \"a\",",
                "\"X-Crozier-Language\": \"0.0.0\",",
            ),
        ] {
            assert!(
                !sdk_name_version_header(&wrapper, fern, crozier),
                "{crozier}"
            );
        }
        // Without a crozier tree, nothing says what its project is.
        let lines: [&str; 0] = [];
        assert!(!sdk_name_version_header(
            &pair("core/client_wrapper.py", &lines, &lines),
            "\"X-Fern-SDK-Name\": \"a\",",
            "\"X-Crozier-SDK-Name\": \"acme\","
        ));

        let without = ["headers = {", "}"];
        let added = wrapper_pair("core/client_wrapper.py", &without);
        assert!(sdk_name_version_header_added(
            &added,
            "    \"X-Crozier-SDK-Name\": \"acme\","
        ));
        assert!(sdk_name_version_header_added(
            &added,
            "    \"X-Crozier-SDK-Version\": \"0.0.0\","
        ));
        for crozier in [
            "    \"X-Crozier-SDK-Name\": \"other\",",
            "    \"X-Crozier-SDK-Version\": \"0.0.1\",",
            "    \"X-Crozier-Language\": \"Python\",",
        ] {
            assert!(!sdk_name_version_header_added(&added, crozier), "{crozier}");
        }
        // Where the reference has the pair, an added line is no departure.
        let with = ["    \"X-Fern-SDK-Name\": \"acme\","];
        assert!(!sdk_name_version_header_added(
            &wrapper_pair("core/client_wrapper.py", &with),
            "    \"X-Crozier-SDK-Version\": \"0.0.0\","
        ));
        assert!(!sdk_name_version_header_added(
            &wrapper_pair("client.py", &without),
            "    \"X-Crozier-SDK-Name\": \"acme\","
        ));
    }

    fn lines(text: &str) -> Vec<&str> {
        text.split('\n').collect()
    }

    /// The metadata rule's region for Fern's `fern` against `crozier`.
    fn metadata_region(fern: &str, crozier: &str, rel: &str) -> Option<Region> {
        let (fern, crozier) = (lines(fern), lines(crozier));
        metadata_generator_config(&pair(rel, &fern, &crozier)).unwrap()
    }

    #[test]
    fn the_metadata_rule_takes_only_generator_config_differences() {
        let record = crate::emit::FERN_METADATA_RECORD;
        let region = |fern: &str| metadata_region(fern, record, FERN_METADATA);
        // A different value inside the member.
        let literals = record.replace("python_enums", "literals");
        assert_eq!(
            region(&literals),
            Some(Region {
                fern: 6..7,
                crozier: 6..7
            })
        );
        // Braces and quotes inside a string are text, inside the member.
        let braced = record.replace("python_enums", "lit}{\\\"erals");
        assert!(region(&braced).is_some(), "{braced}");
        // No member on Fern's side at all: crozier's member lines.
        let start = record.find("  \"generatorConfig\"").unwrap();
        let end = record.find("  \"invokedBy\"").unwrap();
        let absent = format!("{}{}", &record[..start], &record[end..]);
        assert_eq!(
            region(&absent),
            Some(Region {
                fern: 4..4,
                crozier: 4..9
            })
        );
        // Anything else differing too — even with braces in the member's
        // strings — another path, or no difference at all.
        assert_eq!(region(&literals.replace("github", "gitlab")), None);
        assert_eq!(region(&braced.replace("github", "gitlab")), None);
        assert_eq!(
            region(&literals.replace("\"ci\",", "\"ci\" ,")),
            None,
            "a formatting change outside the member"
        );
        assert_eq!(
            metadata_region(&literals, record, "types/user_metadata.json"),
            None
        );
        assert_eq!(region(record), None);
        // Fern's member sharing a line with another member, or a document
        // that is not JSON.
        let shared = literals.replace(
            "\"generatorVersion\": \"5.20.0\",\n  \"generatorConfig\"",
            "\"generatorVersion\": \"5.20.0\", \"generatorConfig\"",
        );
        assert_ne!(shared, literals);
        assert_eq!(region(&shared), None);
        assert_eq!(region("{ not json"), None);
    }

    #[test]
    fn the_metadata_rule_takes_only_crozier_s_fixed_record() {
        let record = crate::emit::FERN_METADATA_RECORD;
        let fern = record.replace("python_enums", "literals");
        // crozier's member changed is no departure, whatever Fern holds.
        for crozier in [
            record.replace("python_enums", "literals_too"),
            record.replace("python_enums", "literals"),
            record.replace("\"ci\"", "\"manual\""),
        ] {
            assert_eq!(metadata_region(&fern, &crozier, FERN_METADATA), None);
        }
    }

    #[test]
    fn the_member_is_located_string_aware() {
        assert_eq!(
            generator_config_member("{\n  \"a\": \"}{\",\n  \"generatorConfig\": {\n    \"x\": \"}\"\n  },\n  \"b\": 1\n}"),
            Member::Lines(2..5)
        );
        assert_eq!(
            generator_config_member("{\n  \"generatorConfig\": \"x,}\"\n}"),
            Member::Lines(1..2)
        );
        assert_eq!(
            generator_config_member("{\n  \"generatorConfig\": [1, {\"a\": 2}],\n  \"b\": 1\n}"),
            Member::Lines(1..2)
        );
        assert_eq!(
            generator_config_member("{\n  \"generatorConfig\": 12\n}"),
            Member::Lines(1..2)
        );
        assert_eq!(
            generator_config_member("{\"a\": 1, \"generatorConfig\": {}}"),
            Member::Shared
        );
        // Only the top-level member, and only a key.
        assert_eq!(
            generator_config_member(
                "{\n  \"x\": {\"generatorConfig\": {}},\n  \"y\": \"generatorConfig\"\n}"
            ),
            Member::Absent
        );
        assert_eq!(generator_config_member("{\"a\": \"open"), Member::Absent);
        assert_eq!(
            generator_config_member("{\"generatorConfig\": \"open"),
            Member::Absent
        );
        assert_eq!(
            generator_config_member("{\"generatorConfig\": }"),
            Member::Absent
        );
    }

    #[test]
    fn the_import_order_rule_takes_only_a_reordered_type_checking_block() {
        let crozier = lines(
            concat!("import typing\n\nif typing.TYPE_CHECKING:\n    from .a import A\n    from .b import B\n", "_dynamic_imports = {}\n"),
        );
        let region = |fern: &str, rel: &str| {
            let fern = lines(fern);
            init_type_checking_import_order(&pair(rel, &fern, &crozier)).unwrap()
        };
        let reordered = concat!(
            "import typing\n\nif typing.TYPE_CHECKING:\n    from .b import B\n    ",
            "from .a import A\n_dynamic_imports = {}\n"
        );
        assert_eq!(
            region(reordered, "src/acme/__init__.py"),
            Some(Region {
                fern: 3..5,
                crozier: 3..5
            })
        );
        assert!(region(reordered, "__init__.py").is_some());
        // Another import, another module, no block, or the same order.
        let other = reordered.replace("from .b import B", "from .c import C");
        assert_eq!(region(&other, "__init__.py"), None);
        assert_eq!(region(reordered, "client.py"), None);
        assert_eq!(region("import typing\n", "__init__.py"), None);
        assert_eq!(region(&crozier.join("\n"), "__init__.py"), None);
        // A block line that is not indented one level cannot be sorted alone.
        let shallow = "if typing.TYPE_CHECKING:\n  from .b import B\n    from .a import A\nx\n";
        assert_eq!(region(shallow, "__init__.py"), None);
    }

    #[test]
    fn ruff_refusing_the_input_surfaces_as_an_error() {
        let error = ruff_isort("def (:\n").unwrap_err();
        assert!(error.contains("ruff isort failed"), "{error}");
        assert_eq!(
            ruff_isort("import typing\nimport enum\n").unwrap(),
            "import enum\nimport typing\n"
        );
    }

    #[test]
    fn tokens_split_identifiers_from_everything_between_them() {
        assert_eq!(
            tokens("from a.b import C, déjà_2"),
            ["from", " ", "a", ".", "b", " ", "import", " ", "C", ",", " ", "déjà_2"]
        );
        assert_eq!(tokens("(x)"), ["(", "x", ")"]);
        assert!(tokens("").is_empty());
    }

    #[test]
    fn the_differing_window_drops_common_leading_and_trailing_lines() {
        assert_eq!(differing_window(&["a", "b"], &["a", "b"]), None);
        assert_eq!(
            differing_window(&["a", "x", "c"], &["a", "y", "z", "c"]),
            Some(Region {
                fern: 1..2,
                crozier: 1..3
            })
        );
        assert_eq!(
            differing_window(&["a"], &["a", "a"]),
            Some(Region {
                fern: 1..1,
                crozier: 1..2
            })
        );
    }

    #[test]
    fn every_kind_has_a_spelling_and_a_meaning() {
        let spellings: BTreeSet<&str> = Kind::ALL.iter().map(|kind| kind.as_str()).collect();
        assert_eq!(spellings.len(), Kind::ALL.len());
        for kind in Kind::ALL {
            assert!(!kind.meaning().is_empty());
            let parsed: Kind = serde_yaml_ng::from_str(kind.as_str()).unwrap();
            assert_eq!(parsed, kind);
        }
    }
}
