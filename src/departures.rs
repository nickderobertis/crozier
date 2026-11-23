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

use std::collections::{BTreeMap, BTreeSet};
use std::io::Write;
use std::process::{Command, Stdio};
use std::sync::OnceLock;

use serde::Deserialize;

mod declared_examples;
mod declared_values;
mod rejected_examples;

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
    /// Both outputs are valid, and crozier's documents more of what the
    /// specification declares.
    RicherDocumentation,
    /// Both outputs are valid, and crozier's behaves more usefully for the
    /// specification as written.
    Usefulness,
}

impl Kind {
    /// Every kind, in the order the reference lists them.
    pub const ALL: [Kind; 7] = [
        Kind::FernDefect,
        Kind::Branding,
        Kind::Packaging,
        Kind::Provenance,
        Kind::Ordering,
        Kind::RicherDocumentation,
        Kind::Usefulness,
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
            Kind::RicherDocumentation => "richer-documentation",
            Kind::Usefulness => "usefulness",
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
            Kind::RicherDocumentation => {
                "Both outputs are valid; crozier's documents more of what the specification declares."
            }
            Kind::Usefulness => {
                "Both outputs are valid; crozier's behaves more usefully for the specification as written."
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
    let entries: Vec<Departure> = crate::yaml::from_str(text).map_err(|error| {
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
    source_document: Option<crate::openapi::OpenApi>,
    source_enum_examples: OnceLock<Vec<SourceEnumExample>>,
    source_int64_examples: OnceLock<BTreeSet<i64>>,
    source_string_consts: OnceLock<BTreeSet<String>>,
    source_rejected_examples: OnceLock<rejected_examples::Index>,
    rejected_example_repairs: std::sync::Mutex<BTreeMap<String, rejected_examples::Repairs>>,
    roots: Option<(std::path::PathBuf, std::path::PathBuf)>,
    reference_classes: OnceLock<BTreeSet<String>>,
    crozier_classes: OnceLock<BTreeSet<String>>,
    crozier_lifted: OnceLock<BTreeSet<String>>,
    crozier_constant_headers: OnceLock<BTreeSet<(String, String)>>,
    reference_nullable_items: OnceLock<BTreeSet<String>>,
    reference_null_union_fields: OnceLock<BTreeSet<(String, String)>>,
    crozier_project: OnceLock<Option<String>>,
    crozier_returns: OnceLock<BTreeMap<(String, String), String>>,
    request_examples: OnceLock<RequestExampleContext>,
    empty_namespace: OnceLock<EmptyNamespace>,
    crozier_paths: OnceLock<BTreeSet<String>>,
    client_modules: OnceLock<ClientModules>,
}

/// One of the two trees a file pair belongs to.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
enum Tree {
    Reference,
    Crozier,
}

/// Every `client.py` module of the two trees, by path, with its text: what
/// `reference.md` links and anchors.
#[derive(Debug, Default)]
struct ClientModules {
    reference: BTreeMap<String, String>,
    crozier: BTreeMap<String, String>,
}

impl ClientModules {
    fn of(&self, tree: Tree) -> &BTreeMap<String, String> {
        match tree {
            Tree::Reference => &self.reference,
            Tree::Crozier => &self.crozier,
        }
    }
}

fn client_modules<'a>(
    files: impl IntoIterator<Item = (&'a str, &'a str)>,
) -> BTreeMap<String, String> {
    files
        .into_iter()
        .filter(|(path, _)| path.ends_with("client.py"))
        .map(|(path, text)| (path.to_string(), text.to_string()))
        .collect()
}

/// The files of an empty-namespace package (`_`) Fern wrote one level too high,
/// as [`empty_namespace_moves`] finds them.
#[derive(Debug, Default)]
struct EmptyNamespace {
    /// Package-root files crozier writes whole for the root client.
    replaced: BTreeSet<String>,
    /// Fern's copies of files crozier writes inside `_/`.
    reference_only: BTreeSet<String>,
    /// The `_` package crozier writes.
    crozier_only: BTreeSet<String>,
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
            source_document: None,
            source_enum_examples: OnceLock::new(),
            source_int64_examples: OnceLock::new(),
            source_string_consts: OnceLock::new(),
            source_rejected_examples: OnceLock::new(),
            rejected_example_repairs: std::sync::Mutex::default(),
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
            reference_null_union_fields: OnceLock::from(required_null_union_fields(
                reference.iter().copied(),
            )),
            crozier_project: OnceLock::from(project),
            empty_namespace: OnceLock::from(EmptyNamespace::default()),
            crozier_returns: OnceLock::from(method_returns(crozier.iter().copied())),
            request_examples: OnceLock::from(request_example_context(crozier.iter().copied())),
            crozier_paths: OnceLock::from(
                crozier
                    .iter()
                    .map(|(path, _)| (*path).to_string())
                    .collect::<BTreeSet<_>>(),
            ),
            client_modules: OnceLock::from(ClientModules {
                reference: client_modules(reference.iter().copied()),
                crozier: client_modules(crozier.iter().copied()),
            }),
        }
    }

    /// The two trees' `client.py` modules, read from the roots on first use.
    fn client_modules(&self) -> &ClientModules {
        self.client_modules.get_or_init(|| {
            let Some((reference, crozier)) = self.roots.as_ref() else {
                return ClientModules::default();
            };
            let read = |root: &std::path::Path| {
                let files: Vec<(String, String)> = crate::parity::walk_files(root)
                    .unwrap_or_default()
                    .into_iter()
                    .filter(|rel| rel.ends_with("client.py"))
                    .filter_map(|rel| {
                        Some((rel.clone(), std::fs::read_to_string(root.join(&rel)).ok()?))
                    })
                    .collect();
                client_modules(
                    files
                        .iter()
                        .map(|(rel, text)| (rel.as_str(), text.as_str())),
                )
            };
            ClientModules {
                reference: read(reference),
                crozier: read(crozier),
            }
        })
    }

    fn holds_client_module(&self, tree: Tree, rel: &str) -> bool {
        self.client_modules().of(tree).contains_key(rel)
    }

    /// The first and last lines of `method` in the sync client of `tree`'s
    /// module `rel`, as crozier's `reference.md` anchors them.
    fn client_method_lines(&self, tree: Tree, rel: &str, method: &str) -> Option<LineRange> {
        let text = self.client_modules().of(tree).get(rel)?;
        crate::emit::sync_client_method_lines(text, method)
            .map(|(start, end)| LineRange { start, end })
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

    /// Add the parsed source document for rules whose validity depends on a
    /// constraint that the generated Python does not retain. Existing callers
    /// omit it, so source-dependent rules remain inactive for them.
    #[must_use]
    pub fn with_source_document(mut self, source: crate::openapi::OpenApi) -> Self {
        self.source_document = Some(source);
        self.source_enum_examples = OnceLock::new();
        self.source_int64_examples = OnceLock::new();
        self.source_string_consts = OnceLock::new();
        self.source_rejected_examples = OnceLock::new();
        self
    }

    /// Whether a schema the source document declares for `argument` — the
    /// keyword, property or key a worked example passes a value as, its last
    /// dotted segment with any `[index]` dropped — provably accepts no value
    /// of `value`'s kind ([`crate::example_values::ValueConstraints::admits_nothing`]):
    /// a value Python spells as an enum member (`Kind.DRAFT`) is a string.
    /// `false` without a source document.
    #[must_use]
    pub fn admits_nothing(&self, argument: &str, value: &str) -> bool {
        let index = self
            .source_rejected_examples
            .get_or_init(|| rejected_examples::index(self.source_document.as_ref()));
        index.admits_nothing(argument, value)
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

    /// Every `(class, field)` of the reference's models whose field is required
    /// (no default) and typed by a union alias opening with an optional
    /// alternative, as `required_null_union_fields` finds them.
    pub fn reference_null_union_fields(&self) -> &BTreeSet<(String, String)> {
        self.reference_null_union_fields.get_or_init(|| {
            let Some((root, _)) = self.roots.as_ref() else {
                return BTreeSet::new();
            };
            let sources = python_sources(root);
            required_null_union_fields(
                sources
                    .iter()
                    .map(|(rel, text)| (rel.as_str(), text.as_str())),
            )
        })
    }

    /// The return annotation of each method crozier's modules define, keyed by
    /// `(module path, method name)`: the first `def` of the name in the module,
    /// which in a `client.py` is the sync client's.
    pub fn crozier_method_returns(&self) -> &BTreeMap<(String, String), String> {
        self.crozier_returns.get_or_init(|| {
            let Some((_, root)) = self.roots.as_ref() else {
                return BTreeMap::new();
            };
            let sources = python_sources(root);
            method_returns(
                sources
                    .iter()
                    .map(|(rel, text)| (rel.as_str(), text.as_str())),
            )
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

    /// The relative path of every file crozier's tree holds.
    fn crozier_paths(&self) -> &BTreeSet<String> {
        self.crozier_paths.get_or_init(|| {
            self.roots
                .as_ref()
                .and_then(|(_, crozier)| crate::parity::walk_files(crozier).ok())
                .unwrap_or_default()
                .into_iter()
                .collect()
        })
    }

    /// The empty-namespace package files the two trees place apart.
    fn empty_namespace(&self) -> &EmptyNamespace {
        self.empty_namespace.get_or_init(|| {
            self.roots
                .as_ref()
                .map(|(reference, crozier)| empty_namespace_moves(reference, crozier))
                .unwrap_or_default()
        })
    }

    fn request_examples(&self) -> &RequestExampleContext {
        self.request_examples.get_or_init(|| {
            let Some((_, root)) = &self.roots else {
                return RequestExampleContext::default();
            };
            let sources = python_sources(root);
            request_example_context(
                sources
                    .iter()
                    .map(|(rel, text)| (rel.as_str(), text.as_str())),
            )
        })
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

#[derive(Debug)]
struct SourceEnumExample {
    keyword: String,
    enum_name: String,
    first_value: String,
    valid_value: String,
    first_member: String,
    valid_member: String,
}

/// Derive identities from the same IR as generation, including inline request
/// hoists and renamed body arguments. The fixed package/client labels do not
/// affect model identities; absent source or an unusable config grants no rule.
fn source_enum_examples(source: Option<&crate::openapi::OpenApi>) -> Vec<SourceEnumExample> {
    let Some(source) = source else {
        return Vec::new();
    };
    // The constructor only rejects unsafe package names. The fixed "parity"
    // segment is valid, and supplied names bypass title-derived defaults, so a
    // loaded document cannot make this config fail. Keep defensive abstention
    // if the constructor gains another validation condition in the future.
    let Ok(config) = crate::config::GenerateConfig::new(
        std::path::PathBuf::new(),
        std::path::PathBuf::new(),
        Some("parity".into()),
        Some("parity".into()),
        Some("ParityClient".into()),
        crate::settings::ExtraFields::Allow,
        &source.info.title,
    ) else {
        return Vec::new();
    };
    let ir = crate::ir::build(source, &config);
    let enums: std::collections::HashMap<_, _> = ir
        .types
        .iter()
        .filter_map(|decl| match decl {
            crate::ir::TypeDecl::Enum(declaration) if declaration.has_corrected_example() => {
                Some((declaration.name.as_str(), declaration))
            }
            _ => None,
        })
        .collect();
    fn enum_name(reference: &crate::ir::TypeRef) -> Option<&str> {
        match reference {
            crate::ir::TypeRef::Named(name) => Some(name),
            crate::ir::TypeRef::Optional(inner) => enum_name(inner),
            _ => None,
        }
    }
    let mut examples = Vec::new();
    let mut add = |keyword: &str, reference: &crate::ir::TypeRef| {
        let Some(declaration) = enum_name(reference).and_then(|name| enums.get(name)) else {
            return;
        };
        let (Some(first), Some(valid)) =
            (declaration.members.first(), declaration.example_member())
        else {
            return;
        };
        if first.value == valid.value {
            return;
        }
        examples.push(SourceEnumExample {
            keyword: keyword.into(),
            enum_name: declaration.name.clone(),
            first_value: first.value.clone(),
            valid_value: valid.value.clone(),
            first_member: first.name.clone(),
            valid_member: valid.name.clone(),
        });
    };
    for declaration in &ir.types {
        if let crate::ir::TypeDecl::Object(object) = declaration {
            for field in &object.fields {
                add(&field.py_name, &field.type_ref);
            }
        }
    }
    for endpoint in &ir.endpoints {
        if let Some(crate::ir::RequestBody::Inline(fields)) = &endpoint.request_body {
            for field in fields {
                add(&field.py_name, &field.type_ref);
            }
        }
    }
    examples
}

#[derive(Debug, Clone, PartialEq, Eq, PartialOrd, Ord)]
struct MethodKey {
    raw_client_path: String,
    method_name: String,
}

#[derive(Clone, Copy, PartialEq, Eq)]
enum ExampleSide {
    Reference,
    Corrected,
}

#[derive(Debug, Default)]
struct RequestExampleContext {
    binary_json_methods: BTreeSet<MethodKey>,
    alias_fields: std::collections::BTreeMap<String, BTreeSet<String>>,
    method_parameters: std::collections::BTreeMap<
        MethodKey,
        std::collections::BTreeMap<String, GeneratedParameter>,
    >,
    json_object_methods: BTreeSet<MethodKey>,
    /// Models with no field of their own or from a base; only the runtime base.
    fieldless_models: BTreeSet<String>,
    /// Methods whose raw request sends the literal `json={}`.
    empty_json_methods: BTreeSet<MethodKey>,
    wire_fields: std::collections::BTreeMap<MethodKey, std::collections::BTreeMap<String, String>>,
}

#[derive(Debug, Default)]
struct GeneratedParameter {
    annotation: String,
    description: Vec<String>,
}

/// Read actual raw signatures and their parameter documentation, never examples.
fn generated_method_parameters(
    text: &str,
) -> std::collections::BTreeMap<String, std::collections::BTreeMap<String, GeneratedParameter>> {
    let mut out = std::collections::BTreeMap::new();
    let mut method = None;
    let mut signature = String::new();
    let mut in_signature = false;
    let mut in_doc = false;
    let mut parameters = false;
    let mut parameter = None;
    for line in text.lines() {
        if let Some(name) = python_method_name(line) {
            method = Some(name.to_string());
            signature.clear();
            in_signature = true;
            in_doc = false;
            parameters = false;
            parameter = None;
        }
        let Some(method) = method.as_ref() else {
            continue;
        };
        if in_signature {
            signature.push_str(line.trim());
            if line.trim_end().ends_with(':') {
                in_signature = false;
                if let Some((open, close)) = signature.find('(').zip(signature.rfind(')')) {
                    if open <= close {
                        let call = format!("method{}", &signature[open..=close]);
                        if let Some((_, arguments)) = example_call_arguments(&call) {
                            let fields = out
                                .entry(method.clone())
                                .or_insert_with(std::collections::BTreeMap::new);
                            for argument in arguments {
                                if let Some((name, annotation)) = argument.trim().split_once(':') {
                                    if python_identifier(name) {
                                        fields.insert(
                                            name.to_string(),
                                            GeneratedParameter {
                                                annotation: annotation
                                                    .trim()
                                                    .split(" = ")
                                                    .next()
                                                    .unwrap_or_default()
                                                    .to_string(),
                                                description: Vec::new(),
                                            },
                                        );
                                    }
                                }
                            }
                        }
                    }
                }
            }
            continue;
        }
        if line.trim() == "\"\"\"" {
            in_doc = !in_doc;
            parameters = false;
            continue;
        }
        if !in_doc {
            continue;
        }
        if line == "        Parameters" {
            parameters = true;
            continue;
        }
        if line == "        Returns" || line == "        Yields" {
            parameters = false;
        }
        if !parameters {
            continue;
        }
        if let Some((name, _)) = line
            .strip_prefix("        ")
            .and_then(|line| line.split_once(" : "))
        {
            if python_identifier(name) {
                parameter = Some(name.to_string());
                continue;
            }
        }
        if let (Some(name), Some(description)) =
            (parameter.as_ref(), line.strip_prefix("            "))
        {
            if let Some(field) = out.get_mut(method).and_then(|fields| fields.get_mut(name)) {
                field.description.push(description.replace("\\\\", "\\"));
            }
        }
    }
    out
}

fn python_identifier(value: &str) -> bool {
    let mut chars = value.chars();
    chars.next().is_some_and(|c| c == '_' || c.is_alphabetic())
        && chars.all(|c| c == '_' || c.is_alphanumeric())
}

fn python_method_name(line: &str) -> Option<&str> {
    line.strip_prefix("    def ")
        .or_else(|| line.strip_prefix("    async def "))?
        .split_once('(')
        .map(|(name, _)| name)
        .filter(|name| python_identifier(name))
}

fn request_example_context<'a>(
    sources: impl IntoIterator<Item = (&'a str, &'a str)>,
) -> RequestExampleContext {
    let sources: Vec<_> = sources.into_iter().collect();
    let aliases: std::collections::BTreeMap<_, _> = sources
        .iter()
        .filter(|(rel, _)| rel.ends_with(".py"))
        .flat_map(|(_, text)| text.lines())
        .filter_map(|line| line.split_once(" = "))
        .filter(|(name, _)| python_identifier(name))
        .collect();
    let mut out = RequestExampleContext::default();
    let mut model_fields: std::collections::BTreeMap<String, BTreeSet<String>> =
        std::collections::BTreeMap::new();
    let mut model_bases: std::collections::BTreeMap<String, Vec<String>> =
        std::collections::BTreeMap::new();
    for (_, text) in &sources {
        let mut model = None;
        for line in text.lines() {
            if let Some((name, bases)) = line
                .strip_prefix("class ")
                .and_then(|line| line.strip_suffix("):"))
                .and_then(|line| line.split_once('('))
            {
                model = Some(name.to_string());
                model_bases.insert(
                    name.to_string(),
                    bases
                        .split(',')
                        .map(|base| base.trim().to_string())
                        .collect::<Vec<_>>(),
                );
            } else if let Some(name) = line
                .strip_prefix("class ")
                .and_then(|line| line.split_once('(').map(|(name, _)| name))
            {
                model = Some(name.to_string());
            }
            if let (Some(model), Some((name, annotation))) = (
                model.as_ref(),
                line.strip_prefix("    ")
                    .and_then(|line| line.split_once(": ")),
            ) {
                if python_identifier(name) && !annotation.starts_with("typing.ClassVar[") {
                    model_fields
                        .entry(model.clone())
                        .or_default()
                        .insert(name.to_string());
                }
            }
        }
    }
    // A model's fields include what it inherits: Revert's
    // `CrmSetObjectPropertiesRequest` aliases a model adding `additional` to a
    // base holding `name`, `type` and `description`, and the method spreads all
    // four.
    let declared_fields = model_fields.clone();
    for (model, fields) in &mut model_fields {
        let mut pending: Vec<&String> = model_bases.get(model).into_iter().flatten().collect();
        let mut visited = BTreeSet::new();
        while let Some(base) = pending.pop() {
            // The runtime's own base classes hold no request field.
            if !base.starts_with("Universal") && visited.insert(base) {
                fields.extend(declared_fields.get(base).into_iter().flatten().cloned());
                pending.extend(model_bases.get(base).into_iter().flatten());
            }
        }
    }
    for (name, target) in &aliases {
        let mut current = *target;
        let mut seen = BTreeSet::new();
        while seen.insert(current) {
            if let Some(fields) = model_fields
                .get(current)
                .filter(|fields| !fields.is_empty())
            {
                out.alias_fields.insert((*name).to_string(), fields.clone());
                break;
            }
            let Some(next) = aliases.get(current) else {
                break;
            };
            current = next;
        }
    }
    out.fieldless_models = model_bases
        .iter()
        .filter(|(model, bases)| {
            !model_fields.contains_key(*model)
                && !bases.is_empty()
                && bases.iter().all(|base| base.starts_with("Universal"))
        })
        .map(|(model, _)| model.clone())
        .collect();
    // A retained object and an alias of it have the same documentation defect
    // when the method spreads the object's fields instead of taking `request`.
    out.alias_fields.extend(model_fields);
    let mut bytes_methods = BTreeSet::new();
    let mut json_methods = BTreeSet::new();
    let mut json_headers = BTreeSet::new();
    for (rel, text) in sources
        .iter()
        .filter(|(rel, _)| *rel == "raw_client.py" || rel.ends_with("/raw_client.py"))
    {
        for (method, fields) in generated_method_parameters(text) {
            out.method_parameters.insert(
                MethodKey {
                    raw_client_path: (*rel).to_string(),
                    method_name: method,
                },
                fields,
            );
        }
        let mut method = None;
        let mut signature = false;
        let mut converter_wire = None;
        for line in text.lines() {
            if let Some(name) = python_method_name(line) {
                method = Some(name);
                signature = true;
            }
            let Some(method) = method else {
                continue;
            };
            let key = MethodKey {
                raw_client_path: (*rel).to_string(),
                method_name: method.to_string(),
            };
            if signature
                && compact_python(&[line])
                    .split(',')
                    .any(|field| field == "request:bytes")
            {
                bytes_methods.insert(key.clone());
            }
            if line.trim_end().ends_with(':') {
                signature = false;
            }
            if line.trim() == "json={" {
                out.json_object_methods.insert(key.clone());
            }
            if line.trim() == "json={}," {
                out.empty_json_methods.insert(key.clone());
            }
            if line.trim() == "json=request," {
                json_methods.insert(key.clone());
            }
            if line.trim() == "\"content-type\": \"application/json\"," {
                json_headers.insert(key.clone());
            }
            // A wire field written through the annotation converter opens the
            // call on its own line and names the variable on the next:
            // guardian's `"policyTopics": convert_and_respect_annotation_metadata(`.
            if let Some(variable) = line
                .trim()
                .strip_prefix("object_=")
                .and_then(|rest| rest.split(',').next())
            {
                if let Some(wire) = converter_wire.take() {
                    if python_identifier(variable) {
                        out.wire_fields
                            .entry(key)
                            .or_default()
                            .insert(variable.to_string(), wire);
                    }
                }
                continue;
            }
            let Some((wire, value)) = line
                .trim()
                .strip_prefix('"')
                .and_then(|s| s.split_once("\": "))
            else {
                continue;
            };
            if value.trim_end() == "convert_and_respect_annotation_metadata(" {
                converter_wire = Some(wire.to_string());
                continue;
            }
            let value = value.trim_end_matches(',');
            let variable = value
                .split_once("file=")
                .and_then(|(_, rest)| rest.split_once(',').map(|(name, _)| name))
                .unwrap_or(value);
            if python_identifier(variable) {
                out.wire_fields
                    .entry(key)
                    .or_default()
                    .insert(variable.to_string(), wire.to_string());
            }
        }
    }
    out.binary_json_methods = bytes_methods
        .into_iter()
        .filter(|key| json_methods.contains(key) && json_headers.contains(key))
        .collect();
    out
}

/// A complete generated call, split only at outer argument commas. Quoted
/// values and nested model/dictionary constructors remain byte-exact.
fn example_call_arguments(call: &str) -> Option<(&str, Vec<&str>)> {
    let (prefix, _) = call.split_once('(')?;
    let open = prefix.len();
    let mut depth = 0usize;
    let mut quote = None;
    let mut escaped = false;
    let mut start = open + 1;
    let mut arguments = Vec::new();
    for (index, character) in call.char_indices().skip_while(|(index, _)| *index < open) {
        if let Some(delimiter) = quote {
            if escaped {
                escaped = false;
            } else if character == '\\' {
                escaped = true;
            } else if character == delimiter {
                quote = None;
            }
            continue;
        }
        match character {
            '\'' | '"' => quote = Some(character),
            '(' | '[' | '{' => depth += 1,
            ')' | ']' | '}' => {
                depth = depth.checked_sub(1)?;
                if depth == 0 {
                    if character != ')' || index + 1 != call.len() {
                        return None;
                    }
                    if start < index {
                        arguments.push(&call[start..index]);
                    }
                    return Some((prefix, arguments));
                }
            }
            ',' if depth == 1 => {
                if start < index {
                    arguments.push(&call[start..index]);
                }
                start = index + 1;
            }
            _ => {}
        }
    }
    None
}

/// Canonicalize eligible example calls, removing only actual required-file
/// placeholders on the corrected side. Everything outside the calls is exact.
fn multipart_example_lines<'a>(
    lines: &'a [&'a str],
    raw_rel: &str,
    context: &RequestExampleContext,
    side: ExampleSide,
) -> Option<(Vec<String>, bool)> {
    let mut kept = Vec::new();
    let mut signature = Vec::new();
    let mut method = "";
    let mut in_doc = false;
    let mut in_example = false;
    let mut allowed = BTreeSet::new();
    let mut removed = false;
    let mut index = 0;
    while index < lines.len() {
        let line = lines[index];
        if let Some(name) = python_method_name(line) {
            method = name;
            signature.clear();
            in_doc = false;
            in_example = false;
            allowed.clear();
        }
        if line.trim() == "\"\"\"" {
            if !in_doc {
                let signature = compact_python(&signature);
                let fields: Vec<_> = signature
                    .split(',')
                    .filter_map(|part| {
                        let (name, annotation) = part.split_once(':')?;
                        python_identifier(name).then_some((name, annotation))
                    })
                    .collect();
                let key = MethodKey {
                    raw_client_path: raw_rel.to_string(),
                    method_name: method.to_string(),
                };
                if let Some(wires) = context.wire_fields.get(&key) {
                    for (name, annotation) in &fields {
                        if annotation.contains('=') || !annotation.contains("core.File") {
                            continue;
                        }
                        let Some(wire) = wires.get(*name) else {
                            continue;
                        };
                        // A list of files is either sequence annotation:
                        // Supabase's function deploy takes
                        // `file: typing.List[core.File]`.
                        let value =
                            if annotation.contains("Sequence[") || annotation.contains("List[") {
                                format!("[\"example_{wire}\"]")
                            } else {
                                format!("\"example_{wire}\"")
                            };
                        allowed.insert(format!("{name}={value}"));
                    }
                }
            }
            in_doc = !in_doc;
            in_example = false;
        } else if !in_doc && allowed.is_empty() {
            signature.push(line);
        }
        if in_doc && line.trim() == "Examples" {
            in_example = true;
        }
        let call_head = line
            .trim_start()
            .strip_prefix("await ")
            .unwrap_or(line.trim_start());
        let is_method_call = call_head
            .strip_prefix("client.")
            .and_then(|s| s.split_once('('))
            .is_some_and(|(name, _)| name.rsplit('.').next() == Some(method));
        if in_doc && in_example && !allowed.is_empty() && is_method_call {
            let mut end = index;
            loop {
                let compact = compact_python(&lines[index..=end]);
                if let Some((prefix, arguments)) = example_call_arguments(&compact) {
                    let args: Vec<_> = arguments
                        .into_iter()
                        .filter(|argument| {
                            if side == ExampleSide::Corrected && allowed.contains(*argument) {
                                removed = true;
                                false
                            } else {
                                true
                            }
                        })
                        .collect();
                    kept.push(format!("{prefix}({})", args.join(",")));
                    index = end + 1;
                    break;
                }
                end += 1;
                if end >= lines.len() || lines[end].trim() == "\"\"\"" {
                    return None;
                }
            }
        } else {
            kept.push(line.to_string());
            index += 1;
        }
    }
    Some((kept, removed))
}

/// Whether a compacted call `crozier` differs from Fern's `fern` only by kept
/// declared examples (`declared-example-over-placeholder`), argument by
/// argument and through nested constructor arguments (runZero's
/// `import_task=ImportCustomIntegrationAssetsRequestImportTask(name=…)`).
fn kept_call_argument(pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    let (Some((fern_call, fern_args)), Some((call, args))) = (
        example_call_arguments(fern),
        example_call_arguments(crozier),
    ) else {
        return false;
    };
    fern_call == call
        && fern_args.len() == args.len()
        && fern_args.iter().zip(&args).all(|(fern_arg, arg)| {
            fern_arg == arg
                || declared_values::declared_example_over_placeholder(
                    pair,
                    &format!("    {fern_arg},"),
                    &format!("    {arg},"),
                )
                || kept_call_argument(pair, fern_arg, arg)
        })
}

fn multipart_object_required_file_example(pair: &Pair<'_>) -> Result<Option<Region>, String> {
    let Some(prefix) = pair.rel.strip_suffix("client.py") else {
        return Ok(None);
    };
    if !prefix.is_empty() && !prefix.ends_with('/') {
        return Ok(None);
    }
    let raw_rel = format!("{prefix}raw_client.py");
    let context = pair.context.request_examples();
    let Some((reference, _)) =
        multipart_example_lines(pair.fern, &raw_rel, context, ExampleSide::Reference)
    else {
        return Ok(None);
    };
    let Some((corrected, removed)) =
        multipart_example_lines(pair.crozier, &raw_rel, context, ExampleSide::Corrected)
    else {
        return Ok(None);
    };
    // A kept declared example beside the file (a text part's own example, the
    // `declared-example-over-placeholder` departure) is the one other difference
    // the call may carry.
    let same_call = reference.len() == corrected.len()
        && reference.iter().zip(&corrected).all(|(fern, crozier)| {
            fern == crozier
                || declared_values::declared_example_over_placeholder(pair, fern, crozier)
                || kept_call_argument(pair, fern, crozier)
        });
    Ok((removed && same_call)
        .then(|| differing_window(pair.fern, pair.crozier))
        .flatten())
}

/// Permit only the default string-to-bytes example correction for a method
/// whose actual raw signature and JSON request establish the mismatch.
fn binary_json_example_lines(
    lines: &[&str],
    rel: &str,
    context: &RequestExampleContext,
    side: ExampleSide,
) -> Option<(Vec<String>, bool)> {
    let reference = rel == "reference.md";
    let readme = rel == "README.md";
    let raw = rel
        .strip_suffix("client.py")
        .filter(|prefix| prefix.is_empty() || prefix.ends_with('/'))
        .map(|prefix| format!("{prefix}raw_client.py"));
    if !reference && !readme && raw.is_none() {
        return None;
    }
    let mut method = None;
    let mut doc = false;
    let mut example = false;
    let mut kept = Vec::new();
    let mut changed = false;
    let mut index = 0;
    while index < lines.len() {
        let line = lines[index];
        if reference {
            if let Some((_, after)) = line.split_once("<details><summary><code>client.") {
                method = after
                    .split_once("<a href=\"")
                    .and_then(|(_, after)| after.split_once("\">"))
                    .and_then(|(path, after)| {
                        after.split_once("</a>").map(|(name, _)| (path, name))
                    })
                    .and_then(|(href, name)| {
                        // The `#L<start>-L<end>` anchor names lines of the module.
                        let path = href.split_once("#L").map_or(href, |(module, _)| module);
                        path.strip_suffix("client.py").map(|prefix| MethodKey {
                            raw_client_path: format!("{prefix}raw_client.py"),
                            method_name: name.to_string(),
                        })
                    })
                    .filter(|key| context.binary_json_methods.contains(key));
            }
        } else {
            if let Some(name) = python_method_name(line) {
                method = raw
                    .as_ref()
                    .map(|raw| MethodKey {
                        raw_client_path: raw.clone(),
                        method_name: name.to_string(),
                    })
                    .filter(|key| context.binary_json_methods.contains(key));
                doc = false;
                example = false;
            }
            if line.trim() == "\"\"\"" {
                doc = !doc;
                example = false;
            } else if doc && line.trim() == "Examples" {
                example = true;
            }
        }
        let head = line.trim().strip_prefix("await ").unwrap_or(line.trim());
        if readme {
            let qualified = head
                .strip_prefix("client.")
                .and_then(|head| head.split_once('('))
                .map(|(name, _)| name);
            method = qualified.and_then(|qualified| {
                context
                    .binary_json_methods
                    .iter()
                    .find(|key| {
                        let prefix = key
                            .raw_client_path
                            .strip_suffix("raw_client.py")
                            .unwrap_or("")
                            .trim_end_matches('/');
                        let module = prefix
                            .strip_prefix("src/")
                            .map_or(prefix, |prefix| {
                                prefix.split_once('/').map_or("", |(_, module)| module)
                            })
                            .replace('/', ".");
                        let expected = if module.is_empty() {
                            key.method_name.clone()
                        } else {
                            format!("{module}.{}", key.method_name)
                        };
                        qualified == expected
                    })
                    .cloned()
            });
        }
        let call_method = head
            .strip_prefix("client.")
            .and_then(|head| head.split_once('('))
            .and_then(|(name, _)| name.rsplit('.').next());
        if (reference || readme || doc && example)
            && method
                .as_ref()
                .is_some_and(|key| call_method == Some(key.method_name.as_str()))
        {
            let mut end = index;
            loop {
                let compact = compact_python(&lines[index..=end]);
                if let Some((prefix, arguments)) = example_call_arguments(&compact) {
                    let arguments: Vec<_> = arguments
                        .into_iter()
                        .map(|argument| {
                            if side == ExampleSide::Corrected && argument == "request=b\"string\"" {
                                changed = true;
                                "request=\"string\""
                            } else {
                                argument
                            }
                        })
                        .collect();
                    kept.push(format!("{prefix}({})", arguments.join(",")));
                    index = end + 1;
                    break;
                }
                end += 1;
                if end >= lines.len() || lines[end].trim() == "\"\"\"" {
                    return None;
                }
            }
        } else {
            // Both sides document the parameter as `bytes` (fern-python-sdk
            // 5.41.3; 5.20.0 wrote `str`), so only the example differs.
            kept.push(line.to_string());
            index += 1;
        }
    }
    Some((kept, changed))
}

fn binary_json_body_example(pair: &Pair<'_>) -> Result<Option<Region>, String> {
    if pair.rel != "reference.md"
        && pair.rel != "README.md"
        && !pair
            .rel
            .strip_suffix("client.py")
            .is_some_and(|prefix| prefix.is_empty() || prefix.ends_with('/'))
    {
        return Ok(None);
    }
    let context = pair.context.request_examples();
    let Some((reference, _)) =
        binary_json_example_lines(pair.fern, pair.rel, context, ExampleSide::Reference)
    else {
        return Ok(None);
    };
    let Some((corrected, changed)) =
        binary_json_example_lines(pair.crozier, pair.rel, context, ExampleSide::Corrected)
    else {
        return Ok(None);
    };
    Ok((changed && reference == corrected)
        .then(|| differing_window(pair.fern, pair.crozier))
        .flatten())
}

/// `binary-json-body-example` on one line, in a file other departures also touch
/// where the whole-file form cannot hold: Fern's `request="string",` beside
/// crozier's `request=b"string",`, in a document with a binary JSON body method.
fn binary_json_body_example_line(pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    let (Some(fern_value), Some(crozier_value)) = (
        fern.trim_start().strip_prefix("request="),
        crozier.trim_start().strip_prefix("request="),
    ) else {
        return false;
    };
    fern_value == "\"string\","
        && crozier_value == "b\"string\","
        && fern.len() + 1 == crozier.len()
        && !pair
            .context
            .request_examples()
            .binary_json_methods
            .is_empty()
}

fn reference_method_key(line: &str) -> Option<MethodKey> {
    let (_, after) = line.split_once("<details><summary><code>client.")?;
    let (_, after) = after.split_once("<a href=\"")?;
    let (href, after) = after.split_once("\">")?;
    let (name, _) = after.split_once("</a>")?;
    // The `#L<start>-L<end>` anchor names lines of the module.
    let path = href.split_once("#L").map_or(href, |(module, _)| module);
    let prefix = path.strip_suffix("client.py")?;
    Some(MethodKey {
        raw_client_path: format!("{prefix}raw_client.py"),
        method_name: name.to_string(),
    })
}

/// One parameter's complete HTML block, including its description and separator.
fn reference_parameter_block<'a>(
    lines: &'a [&'a str],
    index: usize,
) -> Option<(&'a str, &'a str, usize, usize)> {
    if lines.get(index..index + 3)? != ["<dl>", "<dd>", ""] {
        return None;
    }
    let header = lines.get(index + 3)?.strip_prefix("**")?;
    let (name, after) = header.split_once(":** `")?;
    if !python_identifier(name) {
        return None;
    }
    let (annotation, _) = after.split_once('`')?;
    let close = (index + 4..lines.len()).find(|&i| lines[i] == "</dd>")?;
    if lines.get(close + 1)? != &"</dl>" {
        return None;
    }
    let end = close + 2 + usize::from(lines.get(close + 2) == Some(&""));
    Some((name, annotation, close, end))
}

/// Parameter blocks grouped by their actual client method, with source ranges.
fn reference_parameters(
    lines: &[&str],
) -> std::collections::BTreeMap<MethodKey, Vec<(usize, usize)>> {
    let mut out = std::collections::BTreeMap::<_, Vec<_>>::new();
    let mut method = None;
    for index in 0..lines.len() {
        if let Some(key) = reference_method_key(lines[index]) {
            method = Some(key);
        }
        if let (Some(key), Some((_, _, _, end))) =
            (&method, reference_parameter_block(lines, index))
        {
            out.entry(key.clone()).or_default().push((index, end));
        }
    }
    out
}

/// Fern's `request` block for a field-less model the method sends as `json={}`
/// and does not take (guardian's `Object`): crozier writes no block, so the
/// region is the empty point before the block Fern writes next.
fn fieldless_model_request_block(
    pair: &Pair<'_>,
    key: &MethodKey,
    blocks: &[(usize, usize)],
    actual: &[(usize, usize)],
    context: &RequestExampleContext,
) -> Option<Region> {
    if !context.empty_json_methods.contains(key) {
        return None;
    }
    blocks.iter().find_map(|&(start, end)| {
        let ("request", model, close, _) = reference_parameter_block(pair.fern, start)? else {
            return None;
        };
        if !context.fieldless_models.contains(model)
            || pair.fern[start + 3] != format!("**request:** `{model}` ")
            || !pair.fern[start + 4..close]
                .iter()
                .all(|line| line.trim().is_empty())
        {
            return None;
        }
        let (_, next_end) = *blocks.iter().find(|&&(first, _)| first == end)?;
        let next = &pair.fern[end..next_end];
        let first = actual
            .iter()
            .map(|&(first, _)| first)
            .find(|&first| pair.crozier.get(first..first + next.len()) == Some(next))?;
        Some(Region {
            fern: start..end,
            crozier: first..first,
        })
    })
}

fn alias_reference_parameters(pair: &Pair<'_>) -> Result<Option<Region>, String> {
    if pair.rel != "reference.md" {
        return Ok(None);
    }
    let context = pair.context.request_examples();
    let corrected = reference_parameters(pair.crozier);
    for (key, blocks) in reference_parameters(pair.fern) {
        let Some(actual) = corrected.get(&key) else {
            continue;
        };
        // An unchanged whole-request block is not a corrected signature.
        if actual.iter().any(|&(start, _)| {
            reference_parameter_block(pair.crozier, start)
                .is_some_and(|(name, _, _, _)| name == "request")
        }) {
            continue;
        }
        let Some(parameters) = context.method_parameters.get(&key) else {
            continue;
        };
        if parameters.contains_key("request") {
            continue;
        }
        if let Some(region) = fieldless_model_request_block(pair, &key, &blocks, actual, context) {
            return Ok(Some(region));
        }
        if !context.json_object_methods.contains(&key) {
            continue;
        }
        for (start, end) in blocks {
            let Some(("request", alias, close, _)) = reference_parameter_block(pair.fern, start)
            else {
                continue;
            };
            let (Some(fields), Some(wires)) = (
                context.alias_fields.get(alias),
                context.wire_fields.get(&key),
            ) else {
                continue;
            };
            if fields.is_empty()
                || pair.fern[start + 3] != format!("**request:** `{alias}` ")
                || !pair.fern[start + 4..close]
                    .iter()
                    .all(|line| line.trim().is_empty())
                || !fields.iter().all(|field| {
                    // A reserved-word model field (`uuid_`) is the method's `uuid`.
                    let plain = field.strip_suffix('_').unwrap_or(field);
                    let suffixed = format!("{field}_");
                    let present =
                        |keys: &dyn Fn(&str) -> bool| keys(field) || keys(plain) || keys(&suffixed);
                    present(&|key| parameters.contains_key(key))
                        && present(&|key| wires.contains_key(key))
                })
            {
                continue;
            }
            let mut seen = BTreeSet::new();
            let mut path_shared = BTreeSet::new();
            let mut range: Option<std::ops::Range<usize>> = None;
            let mut valid = true;
            for &(first, last) in actual {
                let Some((name, annotation, close, _)) =
                    reference_parameter_block(pair.crozier, first)
                else {
                    continue;
                };
                // A field whose model name a reserved word suffixed (`uuid_`) is
                // documented under its plain spelling.
                let suffixed = format!("{name}_");
                let field = if fields.contains(name) {
                    name
                } else {
                    suffixed.as_str()
                };
                if !fields.contains(field) {
                    continue;
                }
                let parameter = parameters
                    .get(field)
                    .or_else(|| parameters.get(name))
                    .or_else(|| parameters.get(suffixed.as_str()));
                let Some(parameter) = parameter else {
                    continue;
                };
                let description = parameter.description.join("\n");
                let description = description.trim_end_matches('\n');
                let suffix = crate::emit::reference_param_suffix(
                    (!description.is_empty()).then_some(description),
                );
                let expected = format!("**{name}:** `{annotation}`{suffix}\n    ");
                // The reference documents a signature's `typing.Sequence` as
                // `typing.List`.
                let documented = parameter
                    .annotation
                    .replace("typing.Sequence[", "typing.List[");
                // A path parameter sharing a model field's name keeps its own
                // block on both sides: guardian's `topic_id` path argument beside
                // `Schema.topicId`.
                if annotation != crate::emit::reference_param_annotation(&documented)
                    && pair.fern.contains(&pair.crozier[first + 3])
                {
                    path_shared.insert(field.to_string());
                    continue;
                }
                if annotation != crate::emit::reference_param_annotation(&documented)
                    || pair.crozier[first + 3..close].join("\n") != expected
                    || !seen.insert(field.to_string())
                    || range.as_ref().is_some_and(|previous| {
                        pair.crozier[previous.end..first]
                            .iter()
                            .any(|line| !line.trim().is_empty())
                    })
                {
                    valid = false;
                    break;
                }
                match &mut range {
                    Some(range) => range.end = last,
                    None => range = Some(first..last),
                }
            }
            if valid && seen.union(&path_shared).cloned().collect::<BTreeSet<_>>() == *fields {
                if let Some(crozier) = range {
                    return Ok(Some(Region {
                        fern: start..end,
                        crozier,
                    }));
                }
            }
        }
    }
    Ok(None)
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

/// Where Fern wrote an empty-namespace package (`_`) over the package root and
/// crozier wrote it under `_/`. A package qualifies when the reference's root
/// `client.py` imports the runtime from above the package (`from ..core.`, the
/// `_` client's import) and crozier's `_/client.py` is that client but for its
/// docstring examples. Each other file crozier writes inside `_/` must then be
/// Fern's root-level copy unchanged (`__init__.py` but for leading blank lines),
/// except `types/__init__.py`, whose root path holds Fern's root aggregator;
/// otherwise nothing is found for the package.
fn empty_namespace_moves(reference: &std::path::Path, crozier: &std::path::Path) -> EmptyNamespace {
    let read = |root: &std::path::Path, rel: &str| {
        std::fs::read_to_string(root.join(rel))
            .ok()
            .map(|text| crate::strip_python_comments(&text))
    };
    let leading_blank_free = |text: &str| text.trim_start_matches('\n').to_string();
    let crozier_files = crate::parity::walk_files(crozier).unwrap_or_default();
    let packages: BTreeSet<&str> = crozier_files
        .iter()
        .filter_map(|rel| rel.strip_suffix("/_/client.py"))
        .filter(|pkg| {
            pkg.strip_prefix("src/")
                .is_some_and(|name| !name.contains('/'))
        })
        .collect();
    let mut found = EmptyNamespace::default();
    'packages: for pkg in packages {
        let (Some(root_client), Some(moved_client)) = (
            read(reference, &format!("{pkg}/client.py")),
            read(crozier, &format!("{pkg}/_/client.py")),
        ) else {
            continue;
        };
        if !root_client
            .lines()
            .any(|line| line.starts_with("from ..core."))
            || without_examples(&root_client) != without_examples(&moved_client)
        {
            continue;
        }
        let mut reference_only = BTreeSet::new();
        let mut crozier_only = BTreeSet::new();
        for rel in &crozier_files {
            let Some(inner) = rel.strip_prefix(&format!("{pkg}/_/")) else {
                continue;
            };
            let fern_rel = format!("{pkg}/{inner}");
            match inner {
                "client.py" | "types/__init__.py" => {}
                "__init__.py" => {
                    let (ours, theirs) = (read(crozier, rel), read(reference, &fern_rel));
                    if ours.as_deref().map(leading_blank_free)
                        != theirs.as_deref().map(leading_blank_free)
                    {
                        continue 'packages;
                    }
                }
                _ => {
                    let ours = read(crozier, rel);
                    if ours.is_none() || ours != read(reference, &fern_rel) {
                        continue 'packages;
                    }
                    if !crozier.join(&fern_rel).exists() {
                        reference_only.insert(fern_rel);
                    }
                }
            }
            crozier_only.insert(rel.clone());
        }
        found.reference_only.extend(reference_only);
        found.crozier_only.extend(crozier_only);
        found
            .replaced
            .extend([format!("{pkg}/client.py"), format!("{pkg}/__init__.py")]);
    }
    found
}

/// A client module's lines without its docstrings' `Examples` sections.
fn without_examples(text: &str) -> Vec<&str> {
    let lines: Vec<&str> = text.lines().collect();
    let mut kept = Vec::with_capacity(lines.len());
    let mut in_examples = false;
    for (index, line) in lines.iter().enumerate() {
        if in_examples {
            in_examples = line.trim() != "\"\"\"";
            if in_examples {
                continue;
            }
        } else if line.trim() == "Examples"
            && lines
                .get(index + 1)
                .is_some_and(|next| next.trim() == "--------")
        {
            in_examples = true;
            continue;
        }
        kept.push(*line);
    }
    kept
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

/// The return annotation of each method the `.py` files among `sources` define
/// at class level (four spaces in), keyed by `(path, name)`; the first `def` of a
/// name in a module wins. A signature ruff wraps over several lines is read to
/// the line closing it.
fn method_returns<'a>(
    sources: impl IntoIterator<Item = (&'a str, &'a str)>,
) -> BTreeMap<(String, String), String> {
    let mut out = BTreeMap::new();
    for (path, text) in sources {
        if !path.ends_with(".py") {
            continue;
        }
        let lines: Vec<&str> = text.lines().collect();
        for (index, line) in lines.iter().enumerate() {
            let Some(rest) = line
                .strip_prefix("    def ")
                .or_else(|| line.strip_prefix("    async def "))
            else {
                continue;
            };
            let name: String = rest
                .chars()
                .take_while(|c| c.is_alphanumeric() || *c == '_')
                .collect();
            let Some(end) = lines[index..]
                .iter()
                .position(|line| line.ends_with(':') && !line.starts_with("     "))
            else {
                continue;
            };
            let signature: String = lines[index..=index + end]
                .iter()
                .map(|line| line.trim())
                .collect();
            if let Some((_, annotation)) = signature.rsplit_once(") -> ") {
                out.entry((path.to_string(), name))
                    .or_insert_with(|| annotation.trim_end_matches(':').to_string());
            }
        }
    }
    out
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

/// A rule's recogniser for one line crozier writes with no Fern counterpart,
/// given its 0-based index in crozier's file, for a line whose meaning depends
/// on the lines around it (an item of a list argument, a docstring line).
pub type AddedAtRule = fn(&Pair<'_>, usize) -> bool;

/// The tree a file present on only one side belongs to.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum Side {
    /// Only the reference has the file.
    Reference,
    /// Only crozier wrote the file.
    Crozier,
}

/// A rule's recogniser for a whole file at a path only one side has.
pub type FileRule = fn(&Context, &str, Side) -> bool;

/// How one entry's rule recognises its departure: by any of the five shapes.
#[derive(Clone, Copy, Default)]
pub struct Rule {
    /// A region of the pair.
    pub region: Option<RegionRule>,
    /// An aligned pair of lines.
    pub line: Option<LineRule>,
    /// A line only crozier writes.
    pub added: Option<AddedRule>,
    /// A line only crozier writes, recognised by its position.
    pub added_at: Option<AddedAtRule>,
    /// A file only one side has.
    pub file: Option<FileRule>,
}

/// Every rule's id, in catalog order — the order the engine tries them in.
pub const RULE_IDS: [&str; 58] = [
    "anyof-path-param-schema-example",
    "binary-json-body-example",
    "body-query-parameter-value",
    "bracket-query-parameter-call-keyword",
    "closed-empty-object-example",
    "collapsed-anyof-property-description",
    "colliding-component-own-class",
    "constant-header-docs-arguments",
    "dangling-mapping-variant-fields",
    "date-header-constructor-example",
    "declared-example-over-placeholder",
    "declared-examples-array-parameter-value",
    "declared-timestamp-property-example",
    "digit-leading-method-reference-identifiers",
    "digit-leading-property-example-keyword",
    "docstring-literal-dollar-escape",
    "emoji-tag-reference-identifiers",
    "empty-namespace-package",
    "empty-root-security-optional-credential",
    "escaped-field-alias-literal",
    "fern-metadata-generator-config",
    "flat-reference-link-target",
    "init-type-checking-import-order",
    "int64-example-rounded-out-of-range",
    "lifted-base-path-docs-examples",
    "list-path-parameter-example",
    "minimal-worked-call-optional-parameter",
    "multipart-object-required-file-example",
    "nested-discriminator-flat-wire",
    "non-string-client-header-example",
    "nullable-items-docs",
    "optional-lowered-required-query-array-example",
    "optional-raw-body-example-argument",
    "pattern-narrowed-enum-example",
    "readme-abbreviated-call-arguments",
    "readme-client-class-casing",
    "readme-constructor-required-header",
    "readme-environment-constructor-arguments",
    "readme-escaped-method-call",
    "reference-anchor-follows-corrected-client",
    "reference-heading-escaped-method-name",
    "repeated-credential-example-keyword",
    "repeated-query-body-example-keyword",
    "request-alias-reference-parameters",
    "required-null-union-field-example",
    "schema-rejected-array-length-example",
    "schema-rejected-declared-example",
    "schema-rejected-name-example",
    "schema-rejected-number-example",
    "schema-rejected-placeholder-string-example",
    "schema-rejected-sized-string-example",
    "sdk-identity-header-prefix",
    "sdk-name-version-headers",
    "sdk-variable-docs-examples",
    "stream-reference-return-type",
    "text-response-optional-query-examples",
    "unquoted-timestamp-parameter-example",
    "wrapped-union-member-docs-example",
];

/// The rule of the catalog entry `id`, if crozier has one.
#[must_use]
pub fn rule(id: &str) -> Option<Rule> {
    let none = Rule::default();
    Some(match id {
        "anyof-path-param-schema-example" => Rule {
            region: Some(declared_examples::region),
            line: Some(declared_request_string_example),
            ..none
        },
        "dangling-mapping-variant-fields" => Rule {
            region: Some(dangling_mapping_variant_fields),
            ..none
        },
        "nested-discriminator-flat-wire" => Rule {
            region: Some(nested_discriminator_flat_wire),
            ..none
        },
        "body-query-parameter-value" => Rule {
            region: Some(body_query_parameter_value),
            ..none
        },
        "bracket-query-parameter-call-keyword" => Rule {
            line: Some(bracket_query_parameter_call_keyword),
            ..none
        },
        "non-string-client-header-example" => Rule {
            line: Some(non_string_client_header_example),
            ..none
        },
        "collapsed-anyof-property-description" => Rule {
            line: Some(collapsed_anyof_property_description),
            added_at: Some(collapsed_anyof_property_description_line),
            ..none
        },
        "flat-reference-link-target" => Rule {
            line: Some(flat_reference_link_target),
            ..none
        },
        "reference-anchor-follows-corrected-client" => Rule {
            region: Some(reference_anchor_follows_corrected_client),
            ..none
        },
        "reference-heading-escaped-method-name" => Rule {
            line: Some(reference_heading_escaped_method_name),
            ..none
        },
        "digit-leading-method-reference-identifiers" => Rule {
            line: Some(digit_leading_method_reference_identifiers),
            ..none
        },
        "digit-leading-property-example-keyword" => Rule {
            line: Some(digit_leading_property_example_keyword),
            ..none
        },
        "emoji-tag-reference-identifiers" => Rule {
            line: Some(emoji_tag_reference_identifiers),
            ..none
        },
        "optional-lowered-required-query-array-example" => Rule {
            added_at: Some(optional_lowered_required_query_array_example),
            ..none
        },
        // llmlint: ignore[changed_behavior_has_e2e] The list-item-nested-union journey proves acceptance, and rejection where Fern's model defaults the field, through `crozier compare`; another field, another class, a multi-line value or a union opening with a required member each need a Fern tree Fern never writes, so the unit test feeds the rule those crafted inputs.
        "required-null-union-field-example" => Rule {
            added_at: Some(required_null_union_field_example),
            ..none
        },
        "text-response-optional-query-examples" => Rule {
            added: Some(text_response_optional_query_examples),
            ..none
        },
        "declared-example-over-placeholder" => Rule {
            region: Some(declared_values::declared_example_regions),
            line: Some(declared_values::declared_example_over_placeholder),
            added: Some(declared_values::kept_falsy_optional_line),
            added_at: Some(declared_values::kept_wrapped_list_line),
            ..none
        },
        "declared-examples-array-parameter-value" => Rule {
            line: Some(declared_values::declared_examples_array_parameter_value),
            ..none
        },
        "declared-timestamp-property-example" => Rule {
            line: Some(declared_values::declared_timestamp_property_example),
            ..none
        },
        "unquoted-timestamp-parameter-example" => Rule {
            region: Some(declared_values::unquoted_timestamp_call),
            line: Some(declared_values::unquoted_timestamp_parameter_example),
            added_at: Some(declared_values::unquoted_timestamp_parameter_line),
            ..none
        },
        "wrapped-union-member-docs-example" => Rule {
            region: Some(wrapped_union_member_docs_example),
            ..none
        },
        "closed-empty-object-example" => Rule {
            region: Some(closed_empty_object_example_region),
            line: Some(closed_empty_object_example_line),
            ..none
        },
        "colliding-component-own-class" => Rule {
            line: Some(colliding_component_own_class),
            added: Some(colliding_component_own_class_line),
            file: Some(colliding_component_own_class_file),
            ..none
        },
        "constant-header-docs-arguments" => Rule {
            region: Some(constant_header_docs_arguments),
            ..none
        },
        "date-header-constructor-example" => Rule {
            region: Some(date_header_constructor_example),
            ..none
        },
        "docstring-literal-dollar-escape" => Rule {
            line: Some(docstring_literal_dollar_escape),
            ..none
        },
        "int64-example-rounded-out-of-range" => Rule {
            line: Some(int64_example_rounded_out_of_range),
            ..none
        },
        "empty-namespace-package" => Rule {
            region: Some(empty_namespace_package_root),
            line: Some(empty_namespace_reference_anchor),
            file: Some(empty_namespace_package_file),
            ..none
        },
        "empty-root-security-optional-credential" => Rule {
            region: Some(empty_root_security_header_guard),
            line: Some(empty_root_security_optional_credential),
            ..none
        },
        "escaped-field-alias-literal" => Rule {
            line: Some(escaped_field_alias_literal),
            ..none
        },
        "fern-metadata-generator-config" => Rule {
            region: Some(metadata_generator_config),
            ..none
        },
        "binary-json-body-example" => Rule {
            region: Some(binary_json_body_example),
            line: Some(binary_json_body_example_line),
            ..Rule::default()
        },
        "request-alias-reference-parameters" => Rule {
            region: Some(alias_reference_parameters),
            ..none
        },
        // llmlint: ignore[changed_behavior_has_e2e] Each rejection needs a reference tree Fern never writes, so declared_values.rs feeds the rule the crafted input directly; corpus row 5623 proves the acceptance path through real SDK trees.
        "optional-raw-body-example-argument" => Rule {
            region: Some(declared_values::optional_raw_body_example_argument),
            ..none
        },
        "minimal-worked-call-optional-parameter" => Rule {
            region: Some(declared_values::minimal_call_optional_parameter),
            ..none
        },
        "multipart-object-required-file-example" => Rule {
            region: Some(multipart_object_required_file_example),
            ..none
        },
        "init-type-checking-import-order" => Rule {
            region: Some(init_type_checking_import_order),
            ..none
        },
        "readme-environment-constructor-arguments" => Rule {
            region: Some(readme_environment_constructor_arguments),
            ..none
        },
        "list-path-parameter-example" => Rule {
            region: Some(list_path_parameter_call),
            line: Some(list_path_parameter_docstring_value),
            ..none
        },
        "readme-abbreviated-call-arguments" => Rule {
            line: Some(readme_abbreviated_call_arguments),
            ..none
        },
        "readme-constructor-required-header" => Rule {
            region: Some(readme_constructor_required_header),
            ..none
        },
        "readme-escaped-method-call" => Rule {
            line: Some(readme_escaped_method_call),
            ..none
        },
        "lifted-base-path-docs-examples" => Rule {
            region: Some(lifted_base_path_docs_examples),
            ..none
        },
        "nullable-items-docs" => Rule {
            region: Some(nullable_items_docs),
            line: Some(nullable_items_docs_line),
            ..none
        },
        "pattern-narrowed-enum-example" => Rule {
            line: Some(pattern_narrowed_enum_example),
            ..none
        },
        "readme-client-class-casing" => Rule {
            line: Some(readme_client_class_casing),
            ..none
        },
        "repeated-credential-example-keyword" => Rule {
            region: Some(repeated_credential_example_keyword),
            ..none
        },
        "repeated-query-body-example-keyword" => Rule {
            region: Some(repeated_query_body_example_keyword),
            ..none
        },
        "stream-reference-return-type" => Rule {
            line: Some(stream_reference_return_type),
            ..none
        },
        "schema-rejected-array-length-example" => Rule {
            region: Some(schema_rejected_array_length_example),
            ..none
        },
        "schema-rejected-name-example" => Rule {
            region: Some(schema_rejected_name_example_region),
            line: Some(schema_rejected_name_example),
            ..none
        },
        "schema-rejected-declared-example" => Rule {
            region: Some(schema_rejected_declared_example_region),
            line: Some(schema_rejected_declared_example),
            ..none
        },
        "schema-rejected-number-example" => Rule {
            region: Some(schema_rejected_number_example_region),
            line: Some(schema_rejected_number_example),
            ..none
        },
        "schema-rejected-placeholder-string-example" => Rule {
            region: Some(schema_rejected_placeholder_string_example_region),
            line: Some(schema_rejected_placeholder_string_example),
            ..none
        },
        "schema-rejected-sized-string-example" => Rule {
            region: Some(schema_rejected_sized_string_example_region),
            line: Some(schema_rejected_sized_string_example),
            ..none
        },
        "sdk-identity-header-prefix" => Rule {
            line: Some(sdk_identity_header_prefix),
            ..none
        },
        "sdk-name-version-headers" => Rule {
            line: Some(sdk_name_version_header),
            added: Some(sdk_name_version_header_added),
            ..none
        },
        "sdk-variable-docs-examples" => Rule {
            region: Some(sdk_variable_docs_examples),
            ..none
        },
        _ => return None,
    })
}

/// The entries of each inline JSON body, including the converter's continuation
/// lines. Delimiters use the raw client's fixed indentation, so nested Python
/// values cannot close the request argument itself.
fn inline_json_entries(lines: &[&str]) -> Vec<std::ops::Range<usize>> {
    let mut entries = Vec::new();
    let mut in_body = false;
    let mut start = None;
    for (index, line) in lines.iter().enumerate() {
        if *line == "            json={" {
            in_body = true;
        } else if in_body && *line == "            }," {
            if let Some(begin) = start.take() {
                entries.push(begin..index);
            }
            in_body = false;
        } else if in_body && line.starts_with("                \"") {
            if let Some(begin) = start.replace(index) {
                entries.push(begin..index);
            }
        }
    }
    entries
}

/// Whitespace outside Python string literals is formatting. Keep string contents
/// and escapes byte-exact while comparing the same converter on two layouts.
fn compact_python(lines: &[&str]) -> String {
    let mut out = String::new();
    let mut quote = None;
    let mut escaped = false;
    for character in lines.iter().flat_map(|line| line.chars()) {
        if let Some(delimiter) = quote {
            out.push(character);
            if escaped {
                escaped = false;
            } else if character == '\\' {
                escaped = true;
            } else if character == delimiter {
                quote = None;
            }
        } else if matches!(character, '\'' | '"') {
            quote = Some(character);
            out.push(character);
        } else if !character.is_whitespace() {
            out.push(character);
        }
    }
    out
}

fn body_entry_value(expression: &str) -> Option<(&str, &str, bool)> {
    let expression = expression.strip_prefix('"')?;
    let (wire, value) = expression.split_once("\":")?;
    let (value, converted) = value
        .strip_prefix("convert_and_respect_annotation_metadata(object_=")
        .map_or((value, false), |value| (value, true));
    let end =
        value.find(|character: char| !character.is_ascii_alphanumeric() && character != '_')?;
    let name = &value[..end];
    (!name.is_empty() && (converted || &value[end..] == ",")).then_some((wire, name, converted))
}

/// `dangling-mapping-variant-fields`: in a types module, Fern's file is
/// crozier's once each wrapper [`crate::ir::dangling_mapping_wrappers`] reads off
/// the source document is written Fern's way: `value: typing.Any` ahead of the
/// tag in place of the member's fields, a configuration without `extra`, no
/// `update_forward_refs` call of its own, and no import only those lines used.
/// The region is the whole file; every other line must already match.
fn dangling_mapping_variant_fields(pair: &Pair<'_>) -> Result<Option<Region>, String> {
    let Some(source) = pair.context.source_document.as_ref() else {
        return Ok(None);
    };
    if !pair.rel.ends_with(".py") {
        return Ok(None);
    }
    let mut lines: Vec<String> = pair.crozier.iter().map(|line| (*line).to_owned()).collect();
    let mut removed = Vec::new();
    for (wrapper, value, fields) in crate::ir::dangling_mapping_wrappers(source) {
        removed.extend(any_valued_wrapper(&mut lines, &wrapper, &value, &fields));
    }
    if removed.is_empty() {
        return Ok(None);
    }
    drop_unused_imports(&mut lines, &removed);
    Ok(lines
        .iter()
        .map(String::as_str)
        .eq(pair.fern.iter().copied())
        .then_some(Region {
            fern: 0..pair.fern.len(),
            crozier: 0..pair.crozier.len(),
        }))
}

/// Rewrite crozier's `wrapper` class as Fern writes a wrapper holding an unknown
/// `value`, and drop its own `update_forward_refs` call, returning the lines
/// taken out. Nothing changes, and nothing is returned, unless the class is an
/// optional docstring, the tag's `Literal` line, exactly the member's `fields`
/// in order and the pydantic configuration.
fn any_valued_wrapper(
    lines: &mut Vec<String>,
    wrapper: &str,
    value: &str,
    fields: &[String],
) -> Vec<String> {
    let header = format!("class {wrapper}(UniversalBaseModel):");
    let Some(class) = lines.iter().position(|line| *line == header) else {
        return Vec::new();
    };
    let end = lines[class + 1..]
        .iter()
        .position(|line| !line.is_empty() && !line.starts_with(' '))
        .map_or(lines.len(), |index| class + 1 + index);
    // The union's description, which Fern writes on its other wrappers, is not
    // on one holding `value`.
    let quotes = "    \"\"\"";
    let tag = if lines.get(class + 1).is_some_and(|line| line == quotes) {
        match (class + 2..end).find(|index| lines[*index] == quotes) {
            Some(close) if lines.get(close + 1).is_some_and(String::is_empty) => close + 2,
            _ => return Vec::new(),
        }
    } else {
        class + 1
    };
    let literal = serde_json::Value::String(value.to_owned()).to_string();
    let tag_suffix = format!(": typing.Literal[{literal}] = {literal}");
    let tag_line = lines.get(tag).is_some_and(|line| {
        line.strip_prefix("    ")
            .and_then(|rest| rest.strip_suffix(&tag_suffix))
            .is_some_and(|name| !name.is_empty() && !name.contains(' '))
    });
    let Some(config) = (tag..end).find(|index| lines[*index] == "    if IS_PYDANTIC_V2:") else {
        return Vec::new();
    };
    // The fields sit between the tag and the blank line before the configuration.
    if !tag_line || config < tag + 3 || !lines[config - 1].is_empty() {
        return Vec::new();
    }
    // Each field opens at the class's indent with `name:`; its continuation
    // lines sit deeper.
    let declared: Vec<&str> = lines[tag + 1..config - 1]
        .iter()
        .filter_map(|line| line.strip_prefix("    "))
        .filter(|line| !line.starts_with(' ') && !line.starts_with(']'))
        .map(|line| line.split_once(':').map_or(line, |(name, _)| name))
        .collect();
    if !declared
        .iter()
        .copied()
        .eq(fields.iter().map(String::as_str))
    {
        return Vec::new();
    }
    let mut config_lines: Vec<String> = lines[config..end]
        .iter()
        .filter(|line| *line != "            extra = pydantic.Extra.allow")
        .map(|line| {
            line.replace(
                "pydantic.ConfigDict(extra=\"allow\", frozen=True)",
                "pydantic.ConfigDict(frozen=True)",
            )
        })
        .collect();
    let mut rewritten = vec![
        header,
        "    value: typing.Any".to_owned(),
        lines[tag].clone(),
        String::new(),
    ];
    rewritten.append(&mut config_lines);
    let mut taken: Vec<String> = lines[class + 1..tag]
        .iter()
        .chain(&lines[tag + 1..config - 1])
        .cloned()
        .collect();
    lines.splice(class..end, rewritten);
    let single = format!("update_forward_refs({wrapper})");
    let opening = format!("    {wrapper},");
    if let Some(call) = lines.iter().position(|line| *line == single) {
        taken.push(lines.remove(call));
    } else if let Some((call, close)) = lines
        .iter()
        .enumerate()
        .position(|(index, line)| {
            line == "update_forward_refs(" && lines.get(index + 1) == Some(&opening)
        })
        .and_then(|call| {
            let close = lines[call..].iter().position(|line| line == ")")?;
            Some((call, call + close))
        })
    {
        taken.extend(lines.drain(call..=close));
    }
    // A call that closed the file leaves the blank lines before it at the end,
    // where the formatted file has none.
    while lines.len() > 1 && lines.iter().rev().take(2).all(String::is_empty) {
        lines.pop();
    }
    taken
}

/// Drop each single-name import whose name only `removed` lines used.
fn drop_unused_imports(lines: &mut Vec<String>, removed: &[String]) {
    let used_by = |text: &str, name: &str| {
        text.split(|character: char| !character.is_ascii_alphanumeric() && character != '_')
            .any(|word| word == name)
    };
    let imported = |line: &str| -> Option<String> {
        let name = match line.strip_prefix("from ") {
            Some(rest) => rest.split_once(" import ")?.1,
            None => line.strip_prefix("import ")?,
        };
        (!name.is_empty()
            && name
                .chars()
                .all(|c| c.is_ascii_alphanumeric() || c == '_' || c == '.'))
        .then(|| name.rsplit('.').next().unwrap_or(name).to_owned())
    };
    let candidates: Vec<(usize, String)> = lines
        .iter()
        .enumerate()
        .filter_map(|(index, line)| imported(line).map(|name| (index, name)))
        .filter(|(_, name)| removed.iter().any(|line| used_by(line, name)))
        .collect();
    let unused: Vec<usize> = candidates
        .into_iter()
        .filter(|(index, name)| {
            !lines.iter().enumerate().any(|(other, line)| {
                other != *index && imported(line).is_none() && used_by(line, name)
            })
        })
        .map(|(index, _)| index)
        .collect();
    for index in unused.into_iter().rev() {
        lines.remove(index);
    }
}

/// Recognize only the measured nested wrapper's adapters and broken examples.
/// All surrounding declarations and text must still match the reference.
fn nested_discriminator_flat_wire(pair: &Pair<'_>) -> Result<Option<Region>, String> {
    let Some(source) = pair.context.source_document.as_ref() else {
        return Ok(None);
    };
    let mut normalized: Vec<String> = pair.crozier.iter().map(|line| (*line).to_owned()).collect();
    let mut changed = false;
    for (name, schema) in &source.components.schemas {
        let Some(outer) = &schema.discriminator else {
            continue;
        };
        for (tag, target) in &outer.mapping {
            let Some(inner) = target
                .rsplit('/')
                .next()
                .and_then(|name| source.components.schemas.get(name))
            else {
                continue;
            };
            if inner.discriminator.is_none() {
                continue;
            }
            let wrapper = format!(
                "{}_{}",
                crate::naming::class_name(name),
                crate::naming::class_name(tag)
            );
            if pair.rel.ends_with(".py") {
                changed |= nested_wire_adapter(
                    &mut normalized,
                    &wrapper,
                    &outer.property_name,
                    inner.discriminator.as_ref().unwrap().property_name.as_str(),
                );
            } else if matches!(pair.rel, "README.md" | "reference.md") {
                changed |=
                    nested_wire_examples(&mut normalized, &wrapper, tag, target, inner, source);
            }
        }
    }
    Ok((changed
        && normalized
            .iter()
            .map(String::as_str)
            .eq(pair.fern.iter().copied()))
    .then_some(Region {
        fern: 0..pair.fern.len(),
        crozier: 0..pair.crozier.len(),
    }))
}

/// Match the exact adapter body, leaving the original fields and config intact.
fn nested_wire_adapter(lines: &mut Vec<String>, wrapper: &str, tag: &str, inner_tag: &str) -> bool {
    let Some(class) = lines
        .iter()
        .position(|line| line == &format!("class {wrapper}(UniversalBaseModel):"))
    else {
        return false;
    };
    let end = lines[class + 1..]
        .iter()
        .position(|line| line.starts_with("class "))
        .map_or(lines.len(), |index| class + 1 + index);
    let Some(start) = (class + 1..end)
        .find(|index| lines[*index].trim() == "@pydantic.model_validator(mode=\"before\")")
    else {
        return false;
    };
    let Some(begin) = start.checked_sub(3).filter(|begin| *begin > class) else {
        return false;
    };
    let Some(last) =
        (start..end).rfind(|index| lines[*index].trim_start().starts_with("yield from "))
    else {
        return false;
    };
    let actual: Vec<&str> = lines[begin..=last].iter().map(String::as_str).collect();
    let expected = crate::emit::nested_discriminator_methods(
        tag,
        &crate::naming::model_field_name(tag),
        inner_tag,
    );
    if compact_python(&actual) != compact_python(&expected.lines().collect::<Vec<_>>()) {
        return false;
    }
    lines.drain(begin..=last);
    true
}

/// The measured documentation defect uses primitive string placeholders. Admit
/// their exact constructors and values, not arbitrary edits inside an example.
fn nested_wire_examples(
    lines: &mut Vec<String>,
    wrapper: &str,
    tag: &str,
    target: &str,
    inner: &crate::openapi::Schema,
    source: &crate::openapi::OpenApi,
) -> bool {
    let Some(discriminator) = &inner.discriminator else {
        return false;
    };
    let mut changed = false;
    for (inner_tag, reference) in &discriminator.mapping {
        let Some(schema) = reference
            .rsplit('/')
            .next()
            .and_then(|name| source.components.schemas.get(name))
        else {
            continue;
        };
        let fields: Vec<_> = schema
            .properties
            .iter()
            .filter(|(name, _)| {
                schema.required.contains(name) && **name != discriminator.property_name
            })
            .collect();
        if fields.iter().any(|(_, field)| {
            field
                .ty
                .as_ref()
                .and_then(crate::openapi::TypeField::primary)
                != Some("string")
                || field.example.is_some()
        }) {
            continue;
        }
        let constructor = format!(
            "{}_{}",
            crate::naming::class_name(target.rsplit('/').next().unwrap_or(target)),
            crate::naming::class_name(inner_tag)
        );
        let mut index = 0;
        while index + 1 < lines.len() {
            if !lines[index].trim_end().ends_with(&format!("={wrapper}(")) {
                index += 1;
                continue;
            }
            let start = index + 1;
            let indent = lines[start].len() - lines[start].trim_start().len();
            let expected: Vec<String> =
                std::iter::once(format!("{}value={constructor}(", " ".repeat(indent)))
                    .chain(fields.iter().map(|(name, _)| {
                        format!(
                            "{}{}={:?},",
                            " ".repeat(indent + 4),
                            crate::naming::model_field_name(name),
                            name
                        )
                    }))
                    .chain(std::iter::once(format!("{})", " ".repeat(indent))))
                    .collect();
            let end = start + expected.len();
            if lines.get(start..end) != Some(expected.as_slice()) {
                index += 1;
                continue;
            }
            lines.splice(
                start..end,
                [format!(
                    "{}{}=,",
                    " ".repeat(indent),
                    crate::naming::model_field_name(tag)
                )],
            );
            for line in lines
                .iter_mut()
                .filter(|line| line.starts_with("from ") && line.contains(" import "))
            {
                *line = line.replace(&format!(", {constructor}"), "");
            }
            changed = true;
            index = start + 1;
        }
    }
    changed
}

/// `wrapped-union-member-docs-example`: in `README.md` or `reference.md`, Fern's
/// file is crozier's once each worked example of a wrapper whose mapping target
/// is a union of references without a discriminator of its own is written
/// Fern's way: `Wrapper(` and its closing line kept, the `value=` argument
/// between them replaced by the empty `<tag>=,` Fern writes. The wrappers are
/// read off the source document, and a union target that declares its own
/// discriminator is `nested-discriminator-flat-wire`'s instead. The region is
/// the two files' differing window.
fn wrapped_union_member_docs_example(pair: &Pair<'_>) -> Result<Option<Region>, String> {
    if !DOCS_FILES.contains(&pair.rel) {
        return Ok(None);
    }
    let Some(source) = pair.context.source_document.as_ref() else {
        return Ok(None);
    };
    let schemas = &source.components.schemas;
    let mut wrappers = Vec::new();
    for (name, schema) in schemas {
        let Some(discriminator) = &schema.discriminator else {
            continue;
        };
        for (tag, target) in &discriminator.mapping {
            let Some(inner) = target.rsplit('/').next().and_then(|key| schemas.get(key)) else {
                continue;
            };
            let union_of_references =
                inner
                    .one_of
                    .as_ref()
                    .or(inner.any_of.as_ref())
                    .is_some_and(|members| {
                        members.len() > 1 && members.iter().all(|member| member.reference.is_some())
                    });
            if inner.discriminator.is_none() && inner.properties.is_empty() && union_of_references {
                wrappers.push((
                    format!(
                        "{}_{}",
                        crate::naming::class_name(name),
                        crate::naming::class_name(tag)
                    ),
                    crate::naming::model_field_name(tag),
                ));
            }
        }
    }
    let mut normalized: Vec<String> = pair.crozier.iter().map(|line| (*line).to_owned()).collect();
    let mut changed = false;
    for (wrapper, keyword) in &wrappers {
        changed |= empty_wrapped_arguments(&mut normalized, wrapper, keyword);
    }
    if !changed
        || !normalized
            .iter()
            .map(String::as_str)
            .eq(pair.fern.iter().copied())
    {
        return Ok(None);
    }
    Ok(differing_window(pair.fern, pair.crozier))
}

/// Rewrite every one-line `wrapper(value=…)` construct of `lines` into Fern's
/// three-line `wrapper(` / `<keyword>=,` / `)` form. Whether any was rewritten.
/// Only the one-line form is the certified tree's (`tidepool-survey-log`); an
/// exploded wrapper is left alone, so its file still fails.
fn empty_wrapped_arguments(lines: &mut Vec<String>, wrapper: &str, keyword: &str) -> bool {
    let open = format!("{wrapper}(");
    let mut changed = false;
    let mut index = 0;
    while index < lines.len() {
        let line = lines[index].clone();
        let indent = &line[..line.len() - line.trim_start().len()];
        let empty = format!("{indent}    {keyword}=,");
        let Some(at) = line.find(&format!("{open}value=")) else {
            index += 1;
            continue;
        };
        let Some(end) = closing_paren(&line, at + open.len() - 1) else {
            index += 1;
            continue;
        };
        lines.splice(
            index..=index,
            [
                line[..at + open.len()].to_string(),
                empty,
                format!("{indent}{}", &line[end..]),
            ],
        );
        changed = true;
        index += 3;
    }
    changed
}

/// The byte index of the `)` closing the `(` at `open` in `line`, skipping
/// string literals; `None` when the line does not close it.
fn closing_paren(line: &str, open: usize) -> Option<usize> {
    let mut depth = 0usize;
    let mut quote: Option<char> = None;
    let mut escaped = false;
    for (at, character) in line.char_indices().skip_while(|(at, _)| *at < open) {
        if let Some(delimiter) = quote {
            if escaped {
                escaped = false;
            } else if character == '\\' {
                escaped = true;
            } else if character == delimiter {
                quote = None;
            }
            continue;
        }
        match character {
            '"' | '\'' => quote = Some(character),
            '(' | '[' | '{' => depth += 1,
            ')' | ']' | '}' => {
                depth = depth.checked_sub(1)?;
                if depth == 0 {
                    return (character == ')').then_some(at);
                }
            }
            _ => {}
        }
    }
    None
}

/// A renamed body argument shares a wire key with a query parameter. Fern uses
/// the query variable in `json`; crozier uses the signature's body argument.
/// Accept only that variable substitution (and its formatter's line wrapping),
/// after proving both arguments and the query mapping in the enclosing method.
fn body_query_parameter_value(pair: &Pair<'_>) -> Result<Option<Region>, String> {
    if pair.rel != "raw_client.py" && !pair.rel.ends_with("/raw_client.py") {
        return Ok(None);
    }
    let fern_entries = inline_json_entries(pair.fern);
    let crozier_entries = inline_json_entries(pair.crozier);
    if fern_entries.len() != crozier_entries.len() {
        return Ok(None);
    }
    let mut corrected = Vec::new();
    for (fern, crozier) in fern_entries.iter().zip(&crozier_entries) {
        let reference = &pair.fern[fern.clone()];
        let generated = &pair.crozier[crozier.clone()];
        if reference == generated {
            continue;
        }
        let a = compact_python(reference);
        let b = compact_python(generated);
        let Some((wire, query, converted)) = body_entry_value(&a) else {
            return Ok(None);
        };
        let Some((body_wire, body, body_converted)) = body_entry_value(&b) else {
            return Ok(None);
        };
        if wire != body_wire
            || converted != body_converted
            || body == query
            || !body.ends_with(&format!("_{query}"))
        {
            return Ok(None);
        }
        let method = pair.crozier[..crozier.start]
            .iter()
            .rposition(|line| line.starts_with("    def ") || line.starts_with("    async def "))
            .unwrap_or(0);
        let before = &pair.crozier[method..crozier.start];
        let signature: Vec<_> = before
            .iter()
            .take_while(|line| line.trim_start() != "\"\"\"")
            .collect();
        let declared = |name: &str| {
            signature.iter().any(|line| {
                line.starts_with(&format!("        {name}:"))
                    || ((line.starts_with("    def ") || line.starts_with("    async def "))
                        && line.contains(&format!(", {name}:")))
            })
        };
        let query_mapping = format!("                \"{wire}\": {query},");
        if !declared(query) || !declared(body) || !before.contains(&query_mapping.as_str()) {
            return Ok(None);
        }
        let replaced = if converted {
            b.replacen(&format!("object_={body},"), &format!("object_={query},"), 1)
        } else {
            format!("\"{wire}\":{query},")
        };
        // Ruff adds a trailing call comma when the longer body argument wraps.
        let normalize_call_comma = |value: &str| {
            value
                .strip_suffix(",),")
                .map_or_else(|| value.to_owned(), |prefix| format!("{prefix}),"))
        };
        if normalize_call_comma(&replaced) != normalize_call_comma(&a) {
            return Ok(None);
        }
        corrected.push((fern.clone(), crozier.clone()));
    }
    let Some((first_fern, first_crozier)) = corrected.first() else {
        return Ok(None);
    };
    let (last_fern, last_crozier) = corrected.last().expect("nonempty corrections");
    let fern_span = first_fern.start..last_fern.end;
    let crozier_span = first_crozier.start..last_crozier.end;
    let mut normalized = Vec::new();
    let mut position = crozier_span.start;
    for (fern, crozier) in &corrected {
        normalized.extend_from_slice(&pair.crozier[position..crozier.start]);
        normalized.extend_from_slice(&pair.fern[fern.clone()]);
        position = crozier.end;
    }
    normalized.extend_from_slice(&pair.crozier[position..crozier_span.end]);
    Ok(
        (normalized == pair.fern[fern_span.clone()]).then_some(Region {
            fern: fern_span,
            crozier: crozier_span,
        }),
    )
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
    if equal {
        return Ok(Some(Region {
            fern: begin..fern_end,
            crozier: begin..end,
        }));
    }
    Ok(sole_closed_empty_object_block(pair))
}

/// One `closed-empty-object-example` placeholder in a file other departures
/// also touch, where the two sides' lines no longer start the region together:
/// the first of Fern's three-line placeholders with crozier's `<keyword>={},`
/// between the same two neighbours.
fn sole_closed_empty_object_block(pair: &Pair<'_>) -> Option<Region> {
    let (fern, crozier) = (pair.fern, pair.crozier);
    (1..fern.len().saturating_sub(3)).find_map(|index| {
        let block = &fern[index..index + 3];
        let (indent, keyword) = keyword_argument(block[0], "{")?;
        let line = format!("{indent}{keyword}={{}},");
        if !closed_empty_object_example_block(block, &line) {
            return None;
        }
        let at = (1..crozier.len().saturating_sub(1)).find(|&at| {
            crozier[at] == line
                && crozier[at - 1] == fern[index - 1]
                && crozier[at + 1] == fern[index + 3]
        })?;
        Some(Region {
            fern: index..index + 3,
            crozier: at..at + 1,
        })
    })
}

/// `closed-empty-object-example` written on one line, as a method docstring's
/// example and a short snippet write it: Fern's `<indent><keyword>={"key":
/// "value"},` where crozier's line is `<indent><keyword>={},`.
fn closed_empty_object_example_line(_: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    keyword_argument(fern, &format!("{{{KEY_VALUE_PLACEHOLDER}}},"))
        .is_some_and(|(indent, keyword)| crozier == format!("{indent}{keyword}={{}},"))
}

/// Require every occurrence of the candidate line to be in an example. The
/// line-rule interface does not carry an occurrence index, so a duplicated
/// runtime line must conservatively prevent normalization too. The public-API
/// integration control is `tests/generation.rs::narrowed_enum_departure_requires_source_validity_and_rejects_other_changes`;
/// it checks missing source, non-Python fences and duplicated runtime lines.
pub(super) fn documented_example_line(rel: &str, lines: &[&str], candidate: &str) -> bool {
    let mut in_doc = false;
    let mut example = false;
    let mut found = false;
    for line in lines {
        if rel.ends_with(".py") {
            if line.matches("\"\"\"").count() % 2 == 1 {
                in_doc = !in_doc;
                example = false;
            }
            if in_doc && line.trim() == "Examples" {
                example = true;
            }
        } else if line.trim() == "```python" {
            example = true;
        } else if line.trim() == "```" {
            example = false;
        }
        if *line == candidate {
            if !example {
                return false;
            }
            found = true;
        }
    }
    found
}

/// `int64-example-rounded-out-of-range`: an example line of `README.md`,
/// `reference.md` or a client docstring equal on both sides but for one integer
/// keyword value, where Fern's is the spelling JavaScript gives the double
/// nearest crozier's, crozier's lies inside the signed 64-bit range and Fern's
/// does not.
fn int64_example_rounded_out_of_range(pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    if pair.rel != "README.md" && pair.rel != "reference.md" && !high_level_client(pair.rel) {
        return false;
    }
    let Some((prefix, fern_digits, crozier_digits)) = differing_integer(fern, crozier) else {
        return false;
    };
    // The value stands alone as a keyword's value or a list's element: after
    // `=`, `[` or `, `, or on a line of its own in a Markdown list, and before
    // `,`, `]`, `)` or the line's end.
    let (negative, unsigned) = prefix
        .strip_suffix('-')
        .map_or((false, prefix), |rest| (true, rest));
    let after = &fern[prefix.len() + fern_digits.len()..];
    let stands_alone =
        (unsigned.ends_with(['=', '[']) || unsigned.ends_with(", ") || unsigned.trim().is_empty())
            && (after.is_empty() || after.starts_with([',', ']', ')']));
    if !stands_alone {
        return false;
    }
    let signed = |digits: &str| {
        let magnitude = digits.parse::<i128>().ok()?;
        Some(if negative { -magnitude } else { magnitude })
    };
    let in_int64 = |value: i128| i128::from(i64::MIN) <= value && value <= i128::from(i64::MAX);
    let (Some(fern_value), Some(crozier_value)) = (signed(fern_digits), signed(crozier_digits))
    else {
        return false;
    };
    let Ok(exact) = i64::try_from(crozier_value) else {
        return false;
    };
    let declared = pair.context.source_int64_examples.get_or_init(|| {
        let mut examples = BTreeSet::new();
        visit_source_schemas(pair.context.source_document.as_ref(), &mut |schema| {
            if schema.format.as_deref() == Some("int64")
                && schema
                    .ty
                    .as_ref()
                    .and_then(crate::openapi::TypeField::primary)
                    == Some("integer")
            {
                examples.extend(
                    schema
                        .example
                        .iter()
                        .chain(&schema.examples)
                        .filter_map(serde_json::Value::as_i64),
                );
            }
        });
        examples
    });
    if !declared.contains(&exact) {
        return false;
    }
    let rounded = crate::ir::js_integer_literal(&serde_json::Number::from(exact));
    rounded.trim_start_matches('-') == fern_digits
        && !in_int64(fern_value)
        && documented_example_line(pair.rel, pair.fern, fern)
        && documented_example_line(pair.rel, pair.crozier, crozier)
}

/// Apply `visit` to every schema the loaded source document writes, wherever
/// it sits — component schemas, parameters (by `schema` or by `content`),
/// request bodies and responses, operation-level or component-level, and every
/// schema nested inside one; to none without a source document. Loading has
/// already moved webhooks into the paths they are read from.
fn visit_source_schemas(
    source: Option<&crate::openapi::OpenApi>,
    visit: &mut dyn FnMut(&crate::openapi::Schema),
) {
    fn walk(schema: &crate::openapi::Schema, visit: &mut dyn FnMut(&crate::openapi::Schema)) {
        visit(schema);
        for property in schema.properties.values() {
            walk(property, visit);
        }
        if let Some(items) = &schema.items {
            walk(items, visit);
        }
        if let Some(crate::openapi::AdditionalProperties::Schema(value)) =
            &schema.additional_properties
        {
            walk(value, visit);
        }
        for members in [&schema.one_of, &schema.any_of, &schema.all_of] {
            for member in members.iter().flatten() {
                walk(member, visit);
            }
        }
    }
    fn walk_content(
        content: &indexmap::IndexMap<String, crate::openapi::MediaType>,
        visit: &mut dyn FnMut(&crate::openapi::Schema),
    ) {
        for schema in content.values().filter_map(|media| media.schema.as_ref()) {
            walk(schema, visit);
        }
    }
    let Some(source) = source else {
        return;
    };
    for schema in source.components.schemas.values() {
        walk(schema, visit);
    }
    let parameters = source
        .components
        .parameters
        .values()
        .chain(source.paths.values().flat_map(|item| {
            item.parameters.iter().chain(
                item.operations()
                    .into_iter()
                    .flat_map(|(_, op)| &op.parameters),
            )
        }));
    for parameter in parameters {
        if let Some(schema) = &parameter.schema {
            walk(schema, visit);
        }
        walk_content(&parameter.content, visit);
    }
    for body in source.components.request_bodies.values() {
        walk_content(&body.content, visit);
    }
    for response in source.components.responses.values() {
        walk_content(&response.content, visit);
    }
    for item in source.paths.values() {
        for (_, operation) in item.operations() {
            if let Some(body) = &operation.request_body {
                walk_content(&body.content, visit);
            }
            for response in operation.responses.values() {
                walk_content(&response.content, visit);
            }
        }
    }
}

/// Whether `rel` is a generated high-level `client.py`, whose docstrings carry
/// the worked examples, rather than its `raw_client.py`.
fn high_level_client(rel: &str) -> bool {
    rel.rsplit('/').next() == Some("client.py")
}

/// `(prefix, Fern's digits, crozier's digits)` when two lines differ in exactly
/// one run of ASCII digits and nothing else. Lines differing anywhere else —
/// inside a multi-byte character included — have no such run.
fn differing_integer<'a>(fern: &'a str, crozier: &'a str) -> Option<(&'a str, &'a str, &'a str)> {
    let (left, right) = (fern.as_bytes(), crozier.as_bytes());
    let common_prefix = left
        .iter()
        .zip(right)
        .take_while(|(left, right)| left == right)
        .count();
    let common_suffix = left
        .iter()
        .rev()
        .zip(right.iter().rev())
        .take_while(|(left, right)| left == right)
        .count()
        .min(left.len().min(right.len()) - common_prefix);
    let leading_digits = left[..common_prefix]
        .iter()
        .rev()
        .take_while(|byte| byte.is_ascii_digit())
        .count();
    let start = common_prefix - leading_digits;
    let trailing_digits = left[left.len() - common_suffix..]
        .iter()
        .take_while(|byte| byte.is_ascii_digit())
        .count();
    let suffix = common_suffix - trailing_digits;
    let fern_digits = fern.get(start..fern.len() - suffix)?;
    let crozier_digits = crozier.get(start..crozier.len() - suffix)?;
    let digits = |text: &str| !text.is_empty() && text.bytes().all(|byte| byte.is_ascii_digit());
    (fern_digits != crozier_digits && digits(fern_digits) && digits(crozier_digits))
        .then(|| {
            fern.get(..start)
                .map(|prefix| (prefix, fern_digits, crozier_digits))
        })
        .flatten()
}

/// `docstring-literal-dollar-escape`: a client docstring example line passing a
/// keyword a string `const` the parsed source document declares, where Fern's
/// literal is crozier's with every `$` preceded by an escaped backslash
/// (`"\\$PS1"` for `"$PS1"`).
fn docstring_literal_dollar_escape(pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    if !high_level_client(pair.rel) || !crozier.contains('$') {
        return false;
    }
    let consts = pair.context.source_string_consts.get_or_init(|| {
        let mut consts = BTreeSet::new();
        visit_source_schemas(pair.context.source_document.as_ref(), &mut |schema| {
            if let Some(serde_json::Value::String(value)) = &schema.const_value {
                consts.insert(value.clone());
            }
        });
        consts
    });
    let keyword_const = crozier
        .trim_start()
        .split_once('=')
        .is_some_and(|(name, value)| {
            python_identifier(name)
                && value
                    .strip_suffix(',')
                    .and_then(|literal| serde_json::from_str::<String>(literal).ok())
                    .is_some_and(|literal| consts.contains(&literal))
        });
    keyword_const
        && fern == crozier.replace('$', "\\\\$")
        && documented_example_line(pair.rel, pair.fern, fern)
        && documented_example_line(pair.rel, pair.crozier, crozier)
}

/// `schema-rejected-array-length-example`: see
/// [`rejected_examples::array_region`].
fn schema_rejected_array_length_example(pair: &Pair<'_>) -> Result<Option<Region>, String> {
    rejected_examples::array_region(pair)
}

/// Fern's literal where two worked-example lines differ in exactly one
/// literal and nothing else (`"X-Request-Id"` beside crozier's uuid); `None`
/// where they differ in anything else, or in more than one.
#[must_use]
pub fn differing_literal(fern: &str, crozier: &str) -> Option<String> {
    rejected_examples::single_literal_change(fern, crozier)
}

/// `schema-rejected-declared-example`: see [`rejected_examples::holds`].
fn schema_rejected_declared_example(pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    rejected_examples::holds(
        crate::example_values::Mechanism::Declared,
        pair,
        fern,
        crozier,
    )
}

/// `schema-rejected-declared-example` beside another difference: see [`rejected_examples::region`].
fn schema_rejected_declared_example_region(pair: &Pair<'_>) -> Result<Option<Region>, String> {
    rejected_examples::region(crate::example_values::Mechanism::Declared, pair)
}

/// `schema-rejected-name-example`: see [`rejected_examples::holds`].
fn schema_rejected_name_example(pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    rejected_examples::holds(crate::example_values::Mechanism::Name, pair, fern, crozier)
}

/// `schema-rejected-name-example` beside another difference: see [`rejected_examples::region`].
fn schema_rejected_name_example_region(pair: &Pair<'_>) -> Result<Option<Region>, String> {
    rejected_examples::region(crate::example_values::Mechanism::Name, pair)
}

/// `schema-rejected-number-example`: see [`rejected_examples::holds`].
fn schema_rejected_number_example(pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    rejected_examples::holds(
        crate::example_values::Mechanism::Number,
        pair,
        fern,
        crozier,
    )
}

/// `schema-rejected-number-example` beside another difference: see [`rejected_examples::region`].
fn schema_rejected_number_example_region(pair: &Pair<'_>) -> Result<Option<Region>, String> {
    rejected_examples::region(crate::example_values::Mechanism::Number, pair)
}

/// `schema-rejected-placeholder-string-example`: see [`rejected_examples::holds`].
fn schema_rejected_placeholder_string_example(pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    rejected_examples::holds(
        crate::example_values::Mechanism::Placeholder,
        pair,
        fern,
        crozier,
    )
}

/// `schema-rejected-placeholder-string-example` beside another difference: see [`rejected_examples::region`].
fn schema_rejected_placeholder_string_example_region(
    pair: &Pair<'_>,
) -> Result<Option<Region>, String> {
    rejected_examples::region(crate::example_values::Mechanism::Placeholder, pair)
}

/// `schema-rejected-sized-string-example`: see [`rejected_examples::holds`].
fn schema_rejected_sized_string_example(pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    rejected_examples::holds(crate::example_values::Mechanism::Sized, pair, fern, crozier)
}

/// `schema-rejected-sized-string-example` beside another difference: see [`rejected_examples::region`].
fn schema_rejected_sized_string_example_region(pair: &Pair<'_>) -> Result<Option<Region>, String> {
    rejected_examples::region(crate::example_values::Mechanism::Sized, pair)
}

/// Correct only a generated default rejected by a scalar use-site pattern.
fn pattern_narrowed_enum_example(pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    if pair.rel != "README.md" && pair.rel != "reference.md" && !pair.rel.ends_with("client.py") {
        return false;
    }
    let examples = pair
        .context
        .source_enum_examples
        .get_or_init(|| source_enum_examples(pair.context.source_document.as_ref()));
    for example in examples {
        for (old, new) in [
            (
                format!(
                    "{}={}.{},",
                    example.keyword, example.enum_name, example.first_member
                ),
                format!(
                    "{}={}.{},",
                    example.keyword, example.enum_name, example.valid_member
                ),
            ),
            (
                format!(
                    "{}={},",
                    example.keyword,
                    serde_json::to_string(&example.first_value).unwrap_or_default()
                ),
                format!(
                    "{}={},",
                    example.keyword,
                    serde_json::to_string(&example.valid_value).unwrap_or_default()
                ),
            ),
        ] {
            let indent = fern.len() - fern.trim_start().len();
            if fern[indent..] == old && crozier == format!("{}{new}", &fern[..indent]) {
                // Scan complete example regions only for a matching correction,
                // not for every unrelated line in a large client module.
                return documented_example_line(pair.rel, pair.fern, fern)
                    && documented_example_line(pair.rel, pair.crozier, crozier);
            }
        }
    }
    false
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

/// Whether `rel` is the root package's `__init__.py`: `src/<package>/__init__.py`
/// in the packaged layout, `__init__.py` in the flat one.
fn root_package_init(rel: &str) -> bool {
    rel == "__init__.py"
        || rel
            .strip_prefix("src/")
            .and_then(|rest| rest.strip_suffix("/__init__.py"))
            .is_some_and(|package| !package.is_empty() && !package.contains('/'))
}

/// `init-type-checking-import-order`: in an `__init__.py`, both sides'
/// `if typing.TYPE_CHECKING:` blocks differ, yet sort to the same text under
/// ruff's isort. The region is the blocks' differing window. When they do not
/// sort alike, the region is instead the window of import statements the two
/// sides order differently, when that window is the same statements, each
/// importing the same names ([`reordered_statements`]); every other difference
/// in the block stays a difference.
///
/// The root package's own `__init__.py` is no part of it: crozier writes that
/// block in the certified pair's order, the default clients, root client,
/// environment, tag subpackages' re-exports and `__version__` sorted by module
/// (issue #920), so a reordering there is a difference.
fn init_type_checking_import_order(pair: &Pair<'_>) -> Result<Option<Region>, String> {
    if pair.rel != "__init__.py" && !pair.rel.ends_with("/__init__.py") {
        return Ok(None);
    }
    if root_package_init(pair.rel) {
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
    let window = if ruff_isort(&fern_body)? == ruff_isort(&crozier_body)? {
        window
    } else {
        match reordered_statements(fern, crozier) {
            Some(window) => window,
            None => return Ok(None),
        }
    };
    Ok(Some(Region {
        fern: fern_block.start + window.fern.start..fern_block.start + window.fern.end,
        crozier: crozier_block.start + window.crozier.start
            ..crozier_block.start + window.crozier.end,
    }))
}

/// The lines of the import statements two `TYPE_CHECKING` blocks order
/// differently: from the first statement whose source module differs between
/// the sides to the last. `None` unless both blocks import from the same modules,
/// the only statements that move are the root client's and environment's
/// (`from .client`, `from .environment`), and each statement in that window is
/// the same text on both sides, so the window is one permutation of identical
/// statements. A package whose tag subpackages re-export types is that case
/// beside another difference: Fern sorts `from .client` and `from .environment`
/// among `from .auth`, `from .crons`, …, crozier writes them ahead, and a name
/// only one side re-exports stays outside the window.
fn reordered_statements(fern: &[&str], crozier: &[&str]) -> Option<Region> {
    let (fern_statements, crozier_statements) = (statements(fern)?, statements(crozier)?);
    let module = |side: &[&str], range: &std::ops::Range<usize>| -> String {
        let head = side[range.start].trim_start();
        head.split_once(" import")
            .map_or(head, |(module, _)| module)
            .to_string()
    };
    let fern_modules: Vec<String> = fern_statements
        .iter()
        .map(|range| module(fern, range))
        .collect();
    let crozier_modules: Vec<String> = crozier_statements
        .iter()
        .map(|range| module(crozier, range))
        .collect();
    let mut sorted = (fern_modules.clone(), crozier_modules.clone());
    sorted.0.sort();
    sorted.1.sort();
    if sorted.0 != sorted.1 || sorted.0.windows(2).any(|pair| pair[0] == pair[1]) {
        return None;
    }
    let first = fern_modules
        .iter()
        .zip(&crozier_modules)
        .position(|(f, c)| f != c)?;
    let last = fern_modules.len()
        - 1
        - fern_modules
            .iter()
            .rev()
            .zip(crozier_modules.iter().rev())
            .position(|(f, c)| f != c)?;
    let settled = |modules: &[String]| -> Vec<String> {
        modules[first..=last]
            .iter()
            .filter(|module| !matches!(module.as_str(), "from .client" | "from .environment"))
            .cloned()
            .collect()
    };
    if settled(&fern_modules) != settled(&crozier_modules) {
        return None;
    }
    let text = |side: &[&str], range: &std::ops::Range<usize>| side[range.clone()].join("\n");
    for (index, name) in fern_modules.iter().enumerate().take(last + 1).skip(first) {
        let other = crozier_modules
            .iter()
            .position(|candidate| candidate == name)?;
        if !(first..=last).contains(&other)
            || text(fern, &fern_statements[index]) != text(crozier, &crozier_statements[other])
        {
            return None;
        }
    }
    Some(Region {
        fern: fern_statements[first].start..fern_statements[last].end,
        crozier: crozier_statements[first].start..crozier_statements[last].end,
    })
}

/// A `TYPE_CHECKING` block's import statements, each the lines from its
/// `from …`/`import …` line to the next; `None` when a non-blank line precedes
/// the first statement.
fn statements(block: &[&str]) -> Option<Vec<std::ops::Range<usize>>> {
    let starts: Vec<usize> = block
        .iter()
        .enumerate()
        .filter(|(_, line)| line.starts_with("    from ") || line.starts_with("    import "))
        .map(|(index, _)| index)
        .collect();
    if block[..starts.first().copied().unwrap_or(block.len())]
        .iter()
        .any(|line| !line.is_empty())
    {
        return None;
    }
    Some(
        starts
            .iter()
            .enumerate()
            .map(|(index, start)| *start..starts.get(index + 1).copied().unwrap_or(block.len()))
            .collect(),
    )
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
    // Fern's async snippet imports the names its sync snippet does, less the
    // root client under Fern's own lowered spelling; the sync snippet names it
    // correctly cased, so that import survives beside the async client
    // (`from PetStore import AsyncPetstoreApi, PetStoreApi`). crozier's imports
    // only what the snippet uses: the line is judged without it.
    let leaked = async_import_without_sync_client(pair, fern, crozier);
    let fern = leaked.as_deref().unwrap_or(fern);
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

/// Fern's async-snippet import line (`from <pkg> import Async<Client>, <Sync>, …`)
/// without the sync root client crozier's line does not import: `<Sync>` must be
/// a class crozier's modules define, follow the first imported name directly,
/// be absent from crozier's line, and be that first name (crozier's
/// `Async<Sync>`) without `Async`. `None` for any other line.
fn async_import_without_sync_client(pair: &Pair<'_>, fern: &str, crozier: &str) -> Option<String> {
    let (package, names) = fern.strip_prefix("from ")?.split_once(" import ")?;
    let crozier_names: Vec<&str> = crozier
        .strip_prefix(&format!("from {package} import "))?
        .split(", ")
        .collect();
    let sync = crozier_names.first()?.strip_prefix("Async")?;
    let mut fern_names: Vec<&str> = names.split(", ").collect();
    if fern_names.get(1) != Some(&sync)
        || !fern_names[0].eq_ignore_ascii_case(crozier_names[0])
        || !pair.context.crozier_classes().contains(sync)
        || crozier_names.contains(&sync)
    {
        return None;
    }
    fern_names.remove(1);
    Some(format!("from {package} import {}", fern_names.join(", ")))
}

/// `stream-reference-return-type`: a `reference.md` heading line,
/// `<details><summary><code>client.….<a href="PATH">NAME</a>(…) -> T</code></summary>`,
/// equal on both sides but for its return annotation: Fern's
/// `typing.Iterator[bytes]`, crozier's another `typing.Iterator[…]` — which is
/// exactly what crozier's module `PATH` declares its method `NAME` returns.
fn stream_reference_return_type(pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    const OPEN: &str = "<details><summary><code>client.";
    const CLOSE: &str = "</code></summary>";
    const FERN: &str = " -> typing.Iterator[bytes]";
    if pair.rel != "reference.md" || !fern.starts_with(OPEN) {
        return false;
    }
    // A range shifted by the client's other departures, or a flat tree's link
    // to the module it holds, is judged apart.
    let flat = flat_link_in_fern_form(pair, fern, crozier);
    let crozier = flat.as_deref().unwrap_or(crozier);
    let (fern, crozier) = without_verified_ranges(pair, fern, crozier);
    let (fern, crozier) = (fern.as_ref(), crozier.as_ref());
    let Some(head) = fern
        .strip_suffix(CLOSE)
        .and_then(|line| line.strip_suffix(FERN))
    else {
        return false;
    };
    let Some(annotation) = crozier
        .strip_suffix(CLOSE)
        .and_then(|line| line.strip_prefix(head))
        .and_then(|rest| rest.strip_prefix(" -> "))
    else {
        return false;
    };
    if !annotation.starts_with("typing.Iterator[") || annotation == "typing.Iterator[bytes]" {
        return false;
    }
    let Some((path, rest)) = head
        .split_once("<a href=\"")
        .and_then(|(_, rest)| rest.split_once("\">"))
    else {
        return false;
    };
    let Some((method, _)) = rest.split_once("</a>") else {
        return false;
    };
    // The link's `#L<start>-L<end>` anchor, which both sides carry, names lines
    // of the module rather than another module.
    let path = path.split_once("#L").map_or(path, |(module, _)| module);
    // `reference.md` links the packaged module (`src/<package>/…`) in either
    // layout; a packaged tree holds it at that path, a flat tree at the root.
    let returns = pair.context.crozier_method_returns();
    let declared = |path: &str| returns.get(&(path.to_string(), method.to_string()));
    declared(path)
        .or_else(|| {
            path.strip_prefix("src/")
                .and_then(|packaged| packaged.split_once('/'))
                .and_then(|(_, flat)| declared(flat))
        })
        .is_some_and(|declared| declared.replace("dt.", "datetime.") == annotation)
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

/// The lines of the first `client = <Class>(` constructor after the `README.md`
/// heading `heading` up to its `environment=` argument, or its closing `)`
/// where it passes none: `(opener index, argument lines)`.
fn readme_constructor<'a>(lines: &[&'a str], heading: &str) -> Option<(usize, Vec<&'a str>)> {
    let start = lines.iter().position(|line| *line == heading)?;
    let opener = lines[start..]
        .iter()
        .position(|line| line.starts_with("client = ") && line.ends_with('('))
        .map(|offset| start + offset)?;
    let arguments = lines[opener + 1..]
        .iter()
        .take_while(|line| line.starts_with("    ") && !line.starts_with("    environment="))
        .copied()
        .collect();
    Some((opener, arguments))
}

/// `readme-environment-constructor-arguments`: `README.md`'s Environments
/// snippet constructs the client with the environment alone, where crozier
/// passes it the arguments the README's usage snippet passes its constructor
/// (credentials and required headers) first. The region is crozier's run of
/// such argument lines (a lifted base-path parameter's line is
/// `lifted-base-path-docs-examples`'), each the very line the usage snippet's
/// constructor holds, or passing a required typed header of crozier's
/// constructor, and absent from Fern's snippet; Fern's side is the point
/// before its `environment=` argument.
fn readme_environment_constructor_arguments(pair: &Pair<'_>) -> Result<Option<Region>, String> {
    if pair.rel != "README.md" {
        return Ok(None);
    }
    const HEADING: &str = "## Environments";
    let (Some((opener, arguments)), Some((fern_opener, fern_arguments)), Some((_, usage))) = (
        readme_constructor(pair.crozier, HEADING),
        readme_constructor(pair.fern, HEADING),
        readme_constructor(pair.crozier, "## Usage"),
    ) else {
        return Ok(None);
    };
    let lifted = pair.context.crozier_lifted_parameters();
    let Some(first) = arguments
        .iter()
        .position(|line| lifted_argument(line, lifted).is_none())
    else {
        return Ok(None);
    };
    // The usage constructor's arguments, each with its lines joined: it lays a
    // list over several lines where the Environments snippet writes one.
    let squeeze = |text: &str| {
        text.chars()
            .filter(|c| !c.is_whitespace())
            .collect::<String>()
    };
    let mut usage_arguments: Vec<String> = Vec::new();
    for line in &usage {
        if line.starts_with("    ") && !line.starts_with("     ") {
            usage_arguments.push(squeeze(line));
        } else if let Some(last) = usage_arguments.last_mut() {
            last.push_str(&squeeze(line));
        }
    }
    // `readme-constructor-required-header`, earlier by id, may already have
    // taken a required typed header out of the usage constructor.
    let required = required_typed_constructor_parameters(pair.context);
    let run: Vec<&str> = arguments[first..]
        .iter()
        .take_while(|line| {
            let header = line
                .trim_start()
                .split_once('=')
                .is_some_and(|(name, _)| required.contains(name));
            (usage_arguments.contains(&squeeze(line)) || header) && !fern_arguments.contains(line)
        })
        .copied()
        .collect();
    if run.is_empty() || first + run.len() != arguments.len() {
        return Ok(None);
    }
    let at = opener + 1 + first;
    let fern_at = fern_opener + 1 + fern_arguments.len();
    if pair
        .fern
        .get(fern_at)
        .is_none_or(|line| !line.starts_with("    environment="))
    {
        return Ok(None);
    }
    Ok(Some(Region {
        fern: fern_at..fern_at,
        crozier: at..at + run.len(),
    }))
}

/// The positional parameters of every method crozier's client modules define
/// that are typed as lists (`id: typing.Sequence[int]`): its list-typed path
/// parameters, each with its annotation.
fn list_path_parameters(context: &Context) -> BTreeMap<String, String> {
    let mut found = BTreeMap::new();
    for text in context.client_modules().crozier.values() {
        let mut rest = text.as_str();
        while let Some(start) = rest.find("def ") {
            rest = &rest[start + 4..];
            let (Some(open), Some(close)) = (rest.find('('), signature_close(rest)) else {
                break;
            };
            if close < open {
                continue;
            }
            let mut depth = 0usize;
            let mut parameter = String::new();
            for character in rest[open + 1..close].chars().chain([',']) {
                match character {
                    '[' | '(' => depth += 1,
                    ']' | ')' => depth = depth.saturating_sub(1),
                    _ => {}
                }
                if character == ',' && depth == 0 {
                    let trimmed = parameter.trim();
                    if trimmed == "*" {
                        break;
                    }
                    if let Some((name, annotation)) = trimmed.split_once(": ") {
                        if ["typing.Sequence[", "typing.List[", "typing.Set["]
                            .iter()
                            .any(|list| annotation.starts_with(list))
                            && !annotation.contains('=')
                        {
                            found.insert(name.to_string(), annotation.to_string());
                        }
                    }
                    parameter.clear();
                } else {
                    parameter.push(character);
                }
            }
        }
    }
    found
}

/// `list-path-parameter-example` in a client docstring: the line passing a
/// list-typed path parameter whose items are not strings, where Fern passes
/// its string placeholder (`id="ID",`) and crozier a list (`id=[1],`).
fn list_path_parameter_docstring_value(pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    if !pair.rel.ends_with("client.py") || fern == crozier {
        return false;
    }
    let argument = crozier.trim_start();
    let indent = &crozier[..crozier.len() - argument.len()];
    let Some((name, value)) = argument
        .strip_suffix(',')
        .and_then(|argument| argument.split_once('='))
    else {
        return false;
    };
    let Some(fern_value) = fern
        .strip_prefix(&format!("{indent}{name}="))
        .and_then(|value| value.strip_suffix(','))
    else {
        return false;
    };
    value.starts_with('[')
        && value.ends_with(']')
        && fern_value.starts_with('"')
        && fern_value.ends_with('"')
        && list_path_parameters(pair.context)
            .get(name)
            .is_some_and(|annotation| !annotation.ends_with("[str]"))
}

/// `list-path-parameter-example` in `README.md` and `reference.md`: a call that
/// passes a list-typed path parameter where Fern's passes nothing. Crozier's
/// call, without that argument's lines (and closed on its opening line when
/// nothing else is left, `client.probe()`), is Fern's call at the nearest place.
fn list_path_parameter_call(pair: &Pair<'_>) -> Result<Option<Region>, String> {
    if !DOCS_FILES.contains(&pair.rel) {
        return Ok(None);
    }
    let names = list_path_parameters(pair.context);
    if names.is_empty() {
        return Ok(None);
    }
    let lines = pair.crozier;
    for (at, line) in lines.iter().enumerate() {
        let argument = line.trim_start();
        let indent = line.len() - argument.len();
        let Some((name, value)) = argument.split_once('=') else {
            continue;
        };
        if indent == 0 || !names.contains_key(name) {
            continue;
        }
        let Some(opener) = (0..at).rev().find(|index| lines[*index].ends_with('(')) else {
            continue;
        };
        if !opens_method_call(lines[opener].trim_start()) {
            continue;
        }
        let opener_indent = lines[opener].len() - lines[opener].trim_start().len();
        if indent != opener_indent + 4 {
            continue;
        }
        // The argument's own lines: one, or a list laid out over several.
        let argument_end = if value.ends_with(',') {
            at
        } else {
            let Some(offset) = lines[at + 1..]
                .iter()
                .position(|line| line.len() - line.trim_start().len() == indent)
            else {
                continue;
            };
            at + 1 + offset
        };
        let Some(close) = lines[argument_end + 1..]
            .iter()
            .position(|line| line.len() - line.trim_start().len() == opener_indent)
            .map(|offset| argument_end + 1 + offset)
        else {
            continue;
        };
        let mut reduced: Vec<String> = lines[opener..at]
            .iter()
            .chain(&lines[argument_end + 1..=close])
            .map(|line| (*line).to_string())
            .collect();
        if reduced.len() == 2 && reduced[1].trim_start() == ")" {
            reduced = vec![format!("{}){}", reduced[0], &reduced[1].trim_start()[1..])];
        }
        let fern_start = pair
            .fern
            .iter()
            .enumerate()
            .filter(|(index, _)| {
                pair.fern
                    .get(*index..*index + reduced.len())
                    .is_some_and(|window| {
                        window
                            .iter()
                            .zip(&reduced)
                            .all(|(left, right)| left == right)
                    })
            })
            .map(|(index, _)| index)
            .min_by_key(|index| index.abs_diff(opener));
        let Some(fern_start) = fern_start else {
            continue;
        };
        return Ok(Some(Region {
            fern: fern_start..fern_start + reduced.len(),
            crozier: opener..close + 1,
        }));
    }
    Ok(None)
}

/// Where the `def` signature `rest` starts with closes: its first `) ->` or
/// `):`, whichever comes first, so a signature without a return annotation does
/// not run on into the next one.
fn signature_close(rest: &str) -> Option<usize> {
    [rest.find(") ->"), rest.find("):")]
        .into_iter()
        .flatten()
        .min()
}

/// Whether `method`, as the first `def` of the name in the client module
/// `text`, declares a parameter besides `self` without a default.
fn method_requires_argument(text: &str, method: &str) -> bool {
    let Some(start) = text
        .find(&format!("    def {method}("))
        .or_else(|| text.find(&format!("    async def {method}(")))
    else {
        return false;
    };
    let rest = &text[start..];
    let Some(open) = rest.find('(') else {
        return false;
    };
    let Some(close) = signature_close(rest) else {
        return false;
    };
    let mut depth = 0usize;
    let mut parameters = vec![String::new()];
    for character in rest[open + 1..close].chars() {
        match character {
            '[' | '(' => depth += 1,
            ']' | ')' => depth = depth.saturating_sub(1),
            ',' if depth == 0 => {
                parameters.push(String::new());
                continue;
            }
            _ => {}
        }
        if let Some(last) = parameters.last_mut() {
            last.push(character);
        }
    }
    parameters
        .iter()
        .map(|parameter| parameter.trim())
        .any(|parameter| {
            !parameter.is_empty()
                && parameter != "self"
                && parameter != "*"
                && !parameter.starts_with("**")
                && !parameter.contains('=')
        })
}

/// `readme-abbreviated-call-arguments`: a `README.md` abbreviated call
/// (exception handling, raw response, retries, timeouts) of a method that
/// requires an argument Fern does not count, a required header: Fern writes
/// `client.probe()` (or `client.probe(request_options={`), crozier
/// `client.probe(...)` (`client.probe(..., request_options={`), its own
/// elision for a call that takes arguments. crozier's client must define the
/// method with a parameter that has no default.
fn readme_abbreviated_call_arguments(pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    if pair.rel != "README.md" || fern == crozier {
        return false;
    }
    let Some((head, tail)) = crozier
        .split_once("(...)")
        .map(|(head, tail)| (head, format!("(){tail}")))
        .or_else(|| {
            crozier
                .split_once("(..., request_options={")
                .map(|(head, tail)| (head, format!("(request_options={{{tail}")))
        })
    else {
        return false;
    };
    if fern != format!("{head}{tail}") {
        return false;
    }
    let Some(start) = head.find("client.") else {
        return false;
    };
    let chain: Vec<&str> = head[start..].split('.').collect();
    let Some((method, receiver)) = chain.split_last() else {
        return false;
    };
    if !chain.iter().all(|part| python_identifier(part)) {
        return false;
    }
    let groups: Vec<&str> = receiver[1..]
        .iter()
        .copied()
        .filter(|part| *part != "with_raw_response")
        .collect();
    let module = if groups.is_empty() {
        String::new()
    } else {
        format!("/{}", groups.join("/"))
    };
    pair.context
        .client_modules()
        .crozier
        .iter()
        .any(|(path, text)| {
            // The root client is `src/<package>/client.py` (`client.py` flat); a
            // group's ends in its own directories.
            let called = if groups.is_empty() {
                path == "client.py" || path.split('/').count() == 3
            } else {
                path.ends_with(&format!("{module}/client.py"))
            };
            called && method_requires_argument(text, method)
        })
}

/// The keyword-only parameters of crozier's client constructors that take a
/// boolean, a number or a list and have no default.
fn required_typed_constructor_parameters(context: &Context) -> BTreeSet<String> {
    let mut found = BTreeSet::new();
    for text in context.client_modules().crozier.values() {
        let mut rest = text.as_str();
        while let Some(start) = rest.find("    def __init__(") {
            rest = &rest[start + 17..];
            // The signature closes on its own indent, `    ):` or `    ) -> None:`.
            let Some(close) = rest.find("\n    )") else {
                break;
            };
            for line in rest[..close].lines() {
                let Some((name, annotation)) = line
                    .trim()
                    .strip_suffix(',')
                    .and_then(|line| line.split_once(": "))
                else {
                    continue;
                };
                if !annotation.contains('=')
                    && (["bool", "int", "float"].contains(&annotation)
                        || annotation.starts_with("typing.List["))
                {
                    found.insert(name.to_string());
                }
            }
        }
    }
    found
}

/// `readme-constructor-required-header`: a client construction in `README.md`
/// or `reference.md` passing a required boolean, numeric or array header Fern's
/// leaves out. crozier's construction, without those arguments' lines (and
/// closed on its opening line when nothing else is left, `client = FernApi()`),
/// is Fern's at the nearest place.
fn readme_constructor_required_header(pair: &Pair<'_>) -> Result<Option<Region>, String> {
    if !DOCS_FILES.contains(&pair.rel) {
        return Ok(None);
    }
    let names = required_typed_constructor_parameters(pair.context);
    if names.is_empty() {
        return Ok(None);
    }
    let lines = pair.crozier;
    for (opener, line) in lines.iter().enumerate() {
        if !opens_constructor_call(line.trim_start()) {
            continue;
        }
        let indent = line.len() - line.trim_start().len();
        let Some(close) = lines[opener + 1..]
            .iter()
            .position(|line| line.len() - line.trim_start().len() == indent)
            .map(|offset| opener + 1 + offset)
        else {
            continue;
        };
        let mut reduced: Vec<String> = vec![(*line).to_string()];
        let mut removed = false;
        let mut skipping = false;
        for argument in &lines[opener + 1..close] {
            let depth = argument.len() - argument.trim_start().len();
            // A list laid over several lines closes at its own indent.
            let closes = argument.trim_start().starts_with([']', ')', '}']);
            if depth == indent + 4 && !closes {
                skipping = argument
                    .trim_start()
                    .split_once('=')
                    .is_some_and(|(name, _)| names.contains(name));
                removed |= skipping;
            }
            if !skipping {
                reduced.push((*argument).to_string());
            }
        }
        if !removed {
            continue;
        }
        reduced.push(lines[close].to_string());
        if reduced.len() == 2 && reduced[1].trim_start() == ")" {
            reduced = vec![format!("{})", reduced[0])];
        }
        let fern_start = pair
            .fern
            .iter()
            .enumerate()
            .filter(|(index, _)| {
                pair.fern
                    .get(*index..*index + reduced.len())
                    .is_some_and(|window| {
                        window
                            .iter()
                            .zip(&reduced)
                            .all(|(left, right)| left == right)
                    })
            })
            .map(|(index, _)| index)
            .min_by_key(|index| index.abs_diff(opener));
        let Some(fern_start) = fern_start else {
            continue;
        };
        if pair.fern[fern_start..fern_start + reduced.len()] == lines[opener..=close] {
            continue;
        }
        return Ok(Some(Region {
            fern: fern_start..fern_start + reduced.len(),
            crozier: opener..close + 1,
        }));
    }
    Ok(None)
}

/// `readme-escaped-method-call`: a `README.md` line calling a method the SDK
/// escapes with a trailing `_` (`client.apis.all_(`, or through
/// `with_raw_response`), where Fern's line is the same with the escape dropped
/// (`client.apis.all(`), a name the client does not define. crozier's tree must
/// define the escaped method in the called group's client or raw client.
fn readme_escaped_method_call(pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    if pair.rel != "README.md" || fern == crozier {
        return false;
    }
    let Some(start) = crozier.find("client.") else {
        return false;
    };
    let call = &crozier[start..];
    let Some(open) = call.find('(') else {
        return false;
    };
    let chain: Vec<&str> = call[..open].split('.').collect();
    let Some((method, receiver)) = chain.split_last() else {
        return false;
    };
    let unescaped = method.trim_end_matches('_');
    if method.len() == unescaped.len()
        || !python_identifier(unescaped)
        || !chain.iter().all(|part| python_identifier(part))
    {
        return false;
    }
    let groups: Vec<&str> = receiver[1..]
        .iter()
        .copied()
        .filter(|part| *part != "with_raw_response")
        .collect();
    let module = if groups.is_empty() {
        String::new()
    } else {
        format!("/{}", groups.join("/"))
    };
    let defined = pair
        .context
        .crozier_method_returns()
        .keys()
        .any(|(path, name)| {
            name == method
                && (path.ends_with(&format!("{module}/client.py"))
                    || path.ends_with(&format!("{module}/raw_client.py")))
        });
    let renamed = format!(
        "{}{}.{unescaped}{}",
        &crozier[..start],
        receiver.join("."),
        &call[open..]
    );
    defined && fern == renamed
}

/// `repeated-credential-example-keyword`: in `README.md`, `reference.md` or a
/// `client.py`, Fern's file is crozier's once every keyword argument line of a
/// client constructor call (`client = <Class>(`) that repeats a keyword an
/// earlier line of the same call passed is removed — Fern's two credentials
/// sharing one parameter, written `api_key=…` twice. The region is the two
/// files' differing window.
fn repeated_credential_example_keyword(pair: &Pair<'_>) -> Result<Option<Region>, String> {
    if !DOCS_FILES.contains(&pair.rel)
        && pair.rel != "client.py"
        && !pair.rel.ends_with("/client.py")
    {
        return Ok(None);
    }
    let mut kept: Vec<&str> = Vec::with_capacity(pair.fern.len());
    let mut keywords: Option<(usize, BTreeSet<&str>)> = None;
    let mut removed = false;
    for line in pair.fern {
        let trimmed = line.trim_start();
        let indent = line.len() - trimmed.len();
        if opens_constructor_call(trimmed) {
            keywords = Some((indent, BTreeSet::new()));
        } else if let Some((opened, seen)) = keywords.as_mut() {
            if trimmed == ")" && indent == *opened {
                keywords = None;
            } else if let Some((name, _)) = trimmed.split_once('=').filter(|_| line.ends_with(','))
            {
                if !seen.insert(name) {
                    removed = true;
                    continue;
                }
            }
        }
        kept.push(line);
    }
    if !removed || kept != pair.crozier {
        return Ok(None);
    }
    Ok(differing_window(pair.fern, pair.crozier))
}

/// `repeated-query-body-example-keyword`: in `README.md` or `reference.md`, a
/// method call's worked example (`client.<…>(` or `await client.<…>(`) whose
/// argument line repeats a keyword an earlier argument line of the same call
/// passed, where crozier's aligned line passes `<model>_<keyword>` with the same
/// value. The source document must declare the collision Fern renames that way:
/// an operation with a query parameter and a JSON body that `$ref`s component
/// `<Model>`, which declares a property of the same argument name and is
/// referenced somewhere besides that body, so Fern keeps it a named model. Fern's
/// file, with each such line replaced by crozier's, must be crozier's. The
/// region is the two files' differing window. The same mechanism as
/// `repeated-credential-example-keyword`, in a method call rather than the
/// client constructor.
fn repeated_query_body_example_keyword(pair: &Pair<'_>) -> Result<Option<Region>, String> {
    if !DOCS_FILES.contains(&pair.rel) || pair.fern.len() != pair.crozier.len() {
        return Ok(None);
    }
    let Some(source) = pair.context.source_document.as_ref() else {
        return Ok(None);
    };
    let mut kept: Vec<&str> = Vec::with_capacity(pair.fern.len());
    let mut call: Option<(usize, BTreeSet<&str>)> = None;
    let mut replaced = false;
    for (fern, crozier) in pair.fern.iter().zip(pair.crozier) {
        let trimmed = fern.trim_start();
        let indent = fern.len() - trimmed.len();
        if trimmed.ends_with('(') && opens_method_call(trimmed) {
            call = Some((indent, BTreeSet::new()));
        } else if let Some((opened, seen)) = call.as_mut() {
            if trimmed == ")" && indent == *opened {
                call = None;
            } else if let Some((fern_indent, name, value)) = keyword_argument_line(fern) {
                if fern_indent.len() == *opened + 4 && !seen.insert(name) {
                    let renamed = keyword_argument_line(crozier).filter(|(at, renamed, kept)| {
                        *at == fern_indent
                            && kept == &value
                            && reused_query_body_model(source, name, renamed)
                    });
                    if renamed.is_none() {
                        return Ok(None);
                    }
                    replaced = true;
                    kept.push(crozier);
                    continue;
                }
            }
        }
        kept.push(fern);
    }
    if !replaced || kept != pair.crozier {
        return Ok(None);
    }
    Ok(differing_window(pair.fern, pair.crozier))
}

/// Whether `source` declares an operation whose query parameter passes
/// `keyword` beside a JSON body `$ref` to a component that declares a property
/// passed as `keyword`, is referenced somewhere besides that body, and whose
/// snake-cased name prefixes `renamed` as `<model>_<keyword>`.
fn reused_query_body_model(source: &crate::openapi::OpenApi, keyword: &str, renamed: &str) -> bool {
    source_operations(source).any(|(operation, parameters)| {
        let queried = parameters
            .iter()
            .any(|parameter| is_query(parameter) && argument_names(&parameter.name, keyword));
        let Some(pointer) = operation
            .request_body
            .as_ref()
            .and_then(|body| {
                body.content
                    .iter()
                    .find(|(media, _)| media.contains("json"))
            })
            .and_then(|(_, media)| media.schema.as_ref())
            .and_then(|schema| schema.reference.as_deref())
        else {
            return false;
        };
        let Some(model) = pointer.strip_prefix("#/components/schemas/") else {
            return false;
        };
        let Some(component) = source.components.schemas.get(model) else {
            return false;
        };
        let declares = component
            .properties
            .keys()
            .any(|property| argument_names(property, keyword));
        let mut references = 0;
        visit_source_schemas(Some(source), &mut |schema| {
            if schema.reference.as_deref() == Some(pointer) {
                references += 1;
            }
        });
        queried
            && declares
            && references > 1
            && renamed == format!("{}_{keyword}", crate::naming::to_snake_case(model))
    })
}

/// `empty-namespace-package`: the package root's `client.py` and `__init__.py`,
/// where Fern wrote the empty namespace's client and package marker, are
/// crozier's root client and package whole.
fn empty_namespace_package_root(pair: &Pair<'_>) -> Result<Option<Region>, String> {
    Ok(pair
        .context
        .empty_namespace()
        .replaced
        .contains(pair.rel)
        .then_some(Region {
            fern: 0..pair.fern.len(),
            crozier: 0..pair.crozier.len(),
        }))
}

/// `empty-namespace-package`: a file of the `_` package crozier writes, or
/// Fern's copy of one at the package root.
fn empty_namespace_package_file(context: &Context, rel: &str, side: Side) -> bool {
    let moves = context.empty_namespace();
    match side {
        Side::Reference => moves.reference_only.contains(rel),
        Side::Crozier => moves.crozier_only.contains(rel),
    }
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
    if !pair.fern.iter().enumerate().any(|(index, line)| {
        lifted_argument(line, names).is_some()
            && call_opener(pair.fern, index).is_some_and(opens_method_call)
    }) {
        return Ok(None);
    }
    let (Some(fern), Some(crozier)) = (
        fern_docs_without_lifted(pair.fern, names),
        crozier_docs_without_lifted(pair.crozier, names),
    ) else {
        return Ok(None);
    };
    if !fern
        .iter()
        .zip(&crozier)
        .all(|(left, right)| *left == right)
        || fern.len() != crozier.len()
    {
        let methods: BTreeSet<String> = lifted_methods(pair.context, names)
            .into_iter()
            .filter(|method| {
                crozier
                    .iter()
                    .any(|line| line.contains(&format!(".{method}()")))
            })
            .collect();
        if without_lifted_method_placeholders(&fern, &methods) != crozier {
            return Ok(None);
        }
    }
    Ok(differing_window(pair.fern, pair.crozier))
}

/// Constructor examples must supply a date or date-time, rather than a placeholder
/// string. Only constructor parameters typed as optional dates or date-times qualify. After replacing
/// those exact placeholders and accounting for the example import, every line
/// must match; string-header placeholders remain untouched.
fn date_header_constructor_example(pair: &Pair<'_>) -> Result<Option<Region>, String> {
    if !pair.rel.ends_with("client.py") || pair.rel.ends_with("raw_client.py") {
        return Ok(None);
    }
    // Each annotation's parameters, with the value crozier's example passes.
    // A sub-client's docstring constructs the root client, whose wrapper is
    // where a parameter's annotation stands.
    let wrappers: Vec<String> = pair
        .context
        .roots
        .iter()
        .flat_map(|(_, root)| python_sources(root))
        .filter(|(rel, _)| is_client_wrapper(rel))
        .map(|(_, text)| text)
        .collect();
    let names_typed = |annotation: &str| -> BTreeSet<String> {
        pair.fern
            .iter()
            .copied()
            .chain(wrappers.iter().flat_map(|text| text.lines()))
            .filter_map(|line| {
                line.trim()
                    .split_once(&format!(": typing.Optional[{annotation}] = None"))
                    .map(|(name, _)| name.to_string())
            })
            .collect()
    };
    let corrections: Vec<(String, &str)> = names_typed("dt.date")
        .into_iter()
        .map(|name| (name, "datetime.date.fromisoformat(\"2023-01-15\")"))
        .chain(names_typed("dt.datetime").into_iter().map(|name| {
            (
                name,
                "datetime.datetime.fromisoformat(\"2024-01-15T09:30:00+00:00\")",
            )
        }))
        .collect();
    if corrections.is_empty() {
        return Ok(None);
    }
    let mut changed = false;
    let fern: Vec<String> = pair
        .fern
        .iter()
        .map(|line| {
            let mut line = (*line).to_string();
            for (name, value) in &corrections {
                let placeholder = format!("{name}=\"YOUR_{}\"", name.to_uppercase());
                if line.contains(&placeholder) {
                    changed = true;
                    line = line.replace(&placeholder, &format!("{name}={value}"));
                }
            }
            line
        })
        .collect();
    let without_example_import = |lines: &[String]| {
        let mut result = Vec::new();
        let mut index = 0;
        while index < lines.len() {
            if lines[index].trim() == "import datetime"
                && index + 2 < lines.len()
                && lines[index + 1].is_empty()
                && lines[index + 2].trim_start().starts_with("from ")
            {
                index += if index > 0 && lines[index - 1].trim() == "import asyncio" {
                    1
                } else {
                    2
                };
            } else {
                result.push(lines[index].clone());
                index += 1;
            }
        }
        result
    };
    let crozier: Vec<String> = pair
        .crozier
        .iter()
        .map(|line| (*line).to_string())
        .collect();
    if !changed || without_example_import(&fern) != without_example_import(&crozier) {
        return Ok(None);
    }
    Ok(differing_window(pair.fern, pair.crozier))
}

/// Methods whose generated URL reads a client field.
fn lifted_methods(context: &Context, names: &BTreeSet<String>) -> BTreeSet<String> {
    let Some((_, root)) = &context.roots else {
        return BTreeSet::new();
    };
    let mut methods = BTreeSet::new();
    for (_, source) in python_sources(root) {
        let mut method = None;
        for line in source.lines() {
            let trimmed = line.trim_start();
            if let Some(rest) = trimmed
                .strip_prefix("def ")
                .or_else(|| trimmed.strip_prefix("async def "))
            {
                method = rest.split_once('(').map(|(name, _)| name.to_string());
            }
            if names
                .iter()
                .any(|name| line.contains(&format!("self._client_wrapper._{name}")))
            {
                if let Some(method) = &method {
                    methods.insert(method.clone());
                }
            }
        }
    }
    methods
}

/// Remove only positional placeholders and empty calls for lifted methods.
fn without_lifted_method_placeholders(lines: &[&str], methods: &BTreeSet<String>) -> Vec<String> {
    let mut kept: Vec<String> = Vec::new();
    for line in lines {
        let mut line = (*line).to_string();
        for method in methods {
            line = line.replace(&format!(".{method}(..., "), &format!(".{method}("));
            line = line.replace(&format!(".{method}(...)"), &format!(".{method}()"));
            line = line.replace(&format!(">{method}</a>(...)"), &format!(">{method}</a>()"));
        }
        if line.trim() == ")"
            && kept.last().is_some_and(|previous| {
                methods
                    .iter()
                    .any(|method| previous.trim_end().ends_with(&format!(".{method}(")))
            })
        {
            if let Some(previous) = kept.last_mut() {
                previous.push(')');
            }
        } else {
            kept.push(line);
        }
    }
    kept
}

/// SDK-variable documentation forgets the lifted constructor argument and
/// retains a method parameter block and positional placeholder for it. Only
/// methods whose generated route reads a lifted client field are eligible;
/// every remaining line must equal the reference.
fn sdk_variable_docs_examples(pair: &Pair<'_>) -> Result<Option<Region>, String> {
    if !DOCS_FILES.contains(&pair.rel) {
        return Ok(None);
    }
    let names = pair.context.crozier_lifted_parameters();
    let methods = lifted_methods(pair.context, names);
    let Some(crozier) = crozier_docs_without_lifted(pair.crozier, names) else {
        return Ok(None);
    };
    let mut fern = Vec::new();
    let mut index = 0;
    while index < pair.fern.len() {
        if let Some(length) = lifted_parameter_block(pair.fern, index, names) {
            index += length;
            continue;
        }
        let mut line = pair.fern[index].to_string();
        for method in &methods {
            line = line.replace(&format!(".{method}(..., "), &format!(".{method}("));
            line = line.replace(&format!(".{method}(...)"), &format!(".{method}()"));
            line = line.replace(&format!(">{method}</a>(...)"), &format!(">{method}</a>()"));
        }
        fern.push(line);
        index += 1;
    }
    if methods.is_empty() || fern != crozier {
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

/// `constant-header-docs-arguments`: in `reference.md`, Fern's file is
/// crozier's but for the headers crozier's raw clients send as constants:
/// every block documenting one under a method as `**NAME:** \`typing.Literal\``.
/// Those blocks are set aside, and the rest must equal crozier's file; the
/// region is the two files' differing window. Fern's worked calls leave the
/// constants out at fern-python-sdk 5.41.3, as crozier's do, so a call still
/// passing one is no part of this departure.
fn constant_header_docs_arguments(pair: &Pair<'_>) -> Result<Option<Region>, String> {
    if pair.rel != "reference.md" {
        return Ok(None);
    }
    let constants = pair.context.crozier_constant_headers();
    if constants.is_empty() {
        return Ok(None);
    }
    let documented: BTreeSet<String> = constants
        .iter()
        .flat_map(|(wire, _)| header_doc_names(wire))
        .collect();
    let lines = pair.fern;
    let mut kept: Vec<&str> = Vec::with_capacity(lines.len());
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
        kept.push(lines[index]);
        index += 1;
    }
    if !removed {
        return Ok(None);
    }
    if kept == pair.crozier {
        return Ok(differing_window(pair.fern, pair.crozier));
    }
    Ok(sole_constant_block_region(pair, &documented))
}

/// One `constant-header-docs-arguments` block in a `reference.md` other
/// departures also touch, where the whole-file comparison above cannot hold:
/// Fern's block whose `**NAME:**` line crozier does not have, set where
/// crozier's text resumes. The block's neighbours must be crozier's, and every
/// other difference stays for its own rule.
fn sole_constant_block_region(pair: &Pair<'_>, documented: &BTreeSet<String>) -> Option<Region> {
    let is_constant = |line: &str| {
        line.strip_prefix("**")
            .and_then(|rest| rest.split_once(":** `typing.Literal`"))
            .is_some_and(|(name, after)| {
                documented.contains(name) && (after == " " || after.starts_with(" — "))
            })
    };
    let (fern, crozier) = (pair.fern, pair.crozier);
    let ops = crate::parity::align_lines(fern, crozier);
    let mut equal = Vec::new();
    for op in ops {
        match op {
            crate::parity::Op::Equal(left, right) => equal.push((left, right)),
            crate::parity::Op::Delete(line) if is_constant(fern[line]) && line >= 3 => {
                let start = line - 3;
                parameter_block(fern, start, is_constant)?;
                // The block's frame may have paired with crozier's next block,
                // so crozier resumes after the last pair ahead of the frame.
                let &(left, right) = equal.iter().rev().find(|(left, _)| *left < start)?;
                let at = right + (start - left);
                return (start > 0
                    && crozier.get(at.checked_sub(1)?) == fern.get(start - 1)
                    && crozier.get(at) == fern.get(start + 8))
                .then_some(Region {
                    fern: start..start + 8,
                    crozier: at..at,
                });
            }
            _ => {}
        }
    }
    None
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

/// `nullable-items-docs` on one `reference.md` type line, where the whole-file
/// form above cannot hold: another parameter sharing the name keeps its plain
/// type, or another departure touches the file. Fern's line is crozier's with
/// the type's items' `Optional` restored, and nothing else.
fn nullable_items_docs_line(pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    pair.rel == "reference.md"
        && documented_parameter(crozier).is_some_and(|(_, annotation)| {
            annotation
                .strip_prefix("typing.Optional[typing.Union[")
                .and_then(|rest| rest.split_once(", typing.Sequence["))
                .is_some_and(|(item, _)| {
                    let (restored, plain) = nullable_items_types(item);
                    plain == annotation && crozier.replacen(&plain, &restored, 1) == fern
                })
        })
}

/// Whether `rel` is an SDK's client wrapper, where the identity headers are set.
fn is_client_wrapper(rel: &str) -> bool {
    rel == "core/client_wrapper.py" || rel.ends_with("/core/client_wrapper.py")
}

/// The credentials `empty-root-security-optional-credential` may make
/// optional: those of a source document whose credential crozier makes optional
/// only through its empty root `security` list
/// ([`crate::ir::empty_root_security_credentials`]). None without a source.
fn empty_root_security_params(pair: &Pair<'_>) -> Vec<String> {
    pair.context
        .source_document
        .as_ref()
        .map(crate::ir::empty_root_security_credentials)
        .unwrap_or_default()
}

/// Whether `rel` is the root client or its wrapper, the two files the root
/// client's credential reaches.
fn is_root_client_file(rel: &str) -> bool {
    let root_client =
        rel == "client.py" || (rel.ends_with("/client.py") && rel.matches('/').count() <= 2);
    is_client_wrapper(rel) || root_client
}

/// `escaped-field-alias-literal`: a model field's wire alias, in a generated
/// `.py` file. Fern writes the declared property name between double quotes
/// unescaped (`alias="<name>"`, which its `ruff format` may requote), so a
/// quote or backslash in the name reads as Python; crozier writes a string
/// literal whose value is the name. Each `alias=` literal crozier's line holds
/// for such a declared name is put back as Fern's spelling of it, and the result
/// must be Fern's line.
fn escaped_field_alias_literal(pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    if !pair.rel.ends_with(".py") || fern == crozier || !crozier.contains("alias=") {
        return false;
    }
    let mut names = BTreeSet::new();
    visit_source_schemas(pair.context.source_document.as_ref(), &mut |schema| {
        names.extend(
            schema
                .properties
                .keys()
                .filter(|name| name.contains(['"', '\\']))
                .cloned(),
        );
    });
    names.iter().any(|wire| {
        python_string_literals(wire).iter().any(|literal| {
            let ours = format!("alias={literal}");
            crozier.contains(&ours)
                && unescaped_alias_spellings(wire)
                    .iter()
                    .any(|theirs| crozier.replace(&ours, &format!("alias={theirs}")) == fern)
        })
    })
}

/// The two literals `ruff format` may write for `value`: double-quoted, and the
/// single-quoted form it prefers where that needs fewer escapes.
fn python_string_literals(value: &str) -> [String; 2] {
    let single = value
        .replace('\\', "\\\\")
        .replace('\'', "\\'")
        .replace('\n', "\\n")
        .replace('\r', "\\r");
    [
        format!("\"{}\"", crate::emit::escape_py_str(value)),
        format!("'{single}'"),
    ]
}

/// What Fern's `alias="<wire>"` reads as once formatted: the text verbatim, or,
/// where it is one string literal, either literal of the value Python reads.
fn unescaped_alias_spellings(wire: &str) -> Vec<String> {
    let mut spellings = vec![format!("\"{wire}\"")];
    let mut value = String::new();
    let mut characters = wire.chars();
    while let Some(character) = characters.next() {
        match character {
            '"' => return spellings,
            '\\' => match characters.next() {
                Some('n') => value.push('\n'),
                Some('r') => value.push('\r'),
                Some('t') => value.push('\t'),
                Some(escaped @ ('\\' | '"' | '\'')) => value.push(escaped),
                Some(other) => {
                    value.push('\\');
                    value.push(other);
                }
                None => return spellings,
            },
            other => value.push(other),
        }
    }
    spellings.extend(python_string_literals(&value));
    spellings
}

/// `empty-root-security-optional-credential`, aligned half: in the root client
/// or its wrapper, Fern's required credential parameter `<name>: T,`, or its
/// docstring entry `<name> : T`, against crozier's `<name>:
/// typing.Optional[T] = None,` or `<name> : typing.Optional[T]`, at the same
/// indentation, for a credential of a document the departure covers.
fn empty_root_security_optional_credential(pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    if !is_root_client_file(pair.rel) {
        return false;
    }
    let indent = &fern[..fern.len() - fern.trim_start().len()];
    let Some(ours) = crozier.strip_prefix(indent) else {
        return false;
    };
    let theirs = fern.trim_start();
    let optional = |name: &str| {
        if let Some(ty) = theirs
            .strip_prefix(&format!("{name}: "))
            .and_then(|rest| rest.strip_suffix(','))
        {
            return ours == format!("{name}: typing.Optional[{ty}] = None,");
        }
        theirs
            .strip_prefix(&format!("{name} : "))
            .is_some_and(|ty| ours == format!("{name} : typing.Optional[{ty}]"))
    };
    !ours.starts_with(' ')
        && empty_root_security_params(pair)
            .iter()
            .any(|name| optional(name))
}

/// `empty-root-security-optional-credential`, header half: in the wrapper,
/// Fern's `headers[...] = self.<name>` against crozier's same assignment
/// indented beneath `if self.<name> is not None:`, the guard at Fern's
/// indentation. Fern's lines are matched to crozier's guards in order.
fn empty_root_security_header_guard(pair: &Pair<'_>) -> Result<Option<Region>, String> {
    if !is_client_wrapper(pair.rel) {
        return Ok(None);
    }
    let params = empty_root_security_params(pair);
    for (j, line) in pair.crozier.iter().enumerate() {
        let indent = &line[..line.len() - line.trim_start().len()];
        let Some(name) = params
            .iter()
            .find(|name| line.trim_start() == format!("if self.{name} is not None:"))
        else {
            continue;
        };
        let Some(assignment) = pair
            .crozier
            .get(j + 1)
            .and_then(|next| next.strip_prefix(indent))
            .and_then(|next| next.strip_prefix("    "))
            .filter(|next| {
                !next.starts_with(' ')
                    && next.starts_with("headers[")
                    && next.ends_with(&format!("= self.{name}"))
            })
        else {
            continue;
        };
        // Guards already replaced left Fern's line in crozier's place, so this
        // guard answers the next of Fern's lines.
        let wanted = format!("{indent}{assignment}");
        let earlier = pair.crozier[..j]
            .iter()
            .filter(|seen| **seen == wanted)
            .count();
        let Some(i) = pair
            .fern
            .iter()
            .enumerate()
            .filter(|(_, fern)| **fern == wanted)
            .nth(earlier)
            .map(|(i, _)| i)
        else {
            continue;
        };
        return Ok(Some(Region {
            fern: i..i + 1,
            crozier: j..j + 2,
        }));
    }
    Ok(None)
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

/// The files whose worked examples document a method call: the Markdown
/// writers' and each high-level `client.py`'s docstrings.
fn example_file(rel: &str) -> bool {
    DOCS_FILES.contains(&rel) || high_level_client(rel)
}

/// A keyword argument line of a worked example call, `<indent><name>=<value>,`,
/// as its indentation, keyword and value text.
fn keyword_argument_line(line: &str) -> Option<(&str, &str, &str)> {
    let trimmed = line.trim_start();
    let indent = &line[..line.len() - trimmed.len()];
    let (name, value) = trimmed.strip_suffix(',')?.split_once('=')?;
    python_identifier(name).then_some((indent, name, value))
}

/// Every operation of the source document, each with the parameters it takes:
/// its own and its path item's.
fn source_operations(
    source: &crate::openapi::OpenApi,
) -> impl Iterator<Item = (&crate::openapi::Operation, Vec<&crate::openapi::Parameter>)> {
    source.paths.values().flat_map(|item| {
        item.operations().into_iter().map(move |(_, operation)| {
            let parameters = operation
                .parameters
                .iter()
                .chain(item.parameters.iter().filter(|shared| {
                    !operation
                        .parameters
                        .iter()
                        .any(|own| own.name == shared.name && own.location == shared.location)
                }))
                .collect();
            (operation, parameters)
        })
    })
}

/// Whether `keyword` is the argument a parameter or property named `wire` is
/// passed as.
fn argument_names(wire: &str, keyword: &str) -> bool {
    [
        crate::naming::field_name(wire),
        crate::naming::request_field_name(wire),
        crate::naming::model_field_name(wire),
    ]
    .iter()
    .any(|name| name.trim_end_matches('_') == keyword.trim_end_matches('_'))
}

/// A schema's own declared example, the singular `example` before the first of
/// `examples`.
fn declared_schema_example(schema: &crate::openapi::Schema) -> Option<&serde_json::Value> {
    schema.example.as_ref().or_else(|| schema.examples.first())
}

/// The example values a parameter declares: its own `example` and `examples`,
/// then its schema's.
fn declared_parameter_examples(
    parameter: &crate::openapi::Parameter,
) -> impl Iterator<Item = &serde_json::Value> {
    parameter
        .example
        .iter()
        .chain(
            parameter
                .examples
                .values()
                .filter_map(|example| example.value.as_ref()),
        )
        .chain(parameter.schema.as_ref().and_then(declared_schema_example))
}

fn is_query(parameter: &crate::openapi::Parameter) -> bool {
    parameter.location == Some(crate::openapi::ParameterLocation::Query)
}

fn is_path(parameter: &crate::openapi::Parameter) -> bool {
    parameter.location == Some(crate::openapi::ParameterLocation::Path)
}

/// `anyof-path-param-schema-example`: in a worked example, Fern's
/// `<name>="<name>"` placeholder for a path parameter whose schema is an
/// `anyOf`/`oneOf` composition, against crozier's `<name>=<example>` — the
/// string the composition's own schema-level `example` declares. It also keeps
/// a required referenced query parameter's own valid string example and a required
/// annotated-reference property's string example. Every other character of the
/// line is the same.
fn declared_request_string_example(pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    if !example_file(pair.rel) {
        return false;
    }
    let (Some((fern_indent, fern_name, fern_value)), Some((indent, name, value))) =
        (keyword_argument_line(fern), keyword_argument_line(crozier))
    else {
        return false;
    };
    if fern_indent != indent || fern_name != name || fern_value == value {
        return false;
    }
    let Some(source) = pair.context.source_document.as_ref() else {
        return false;
    };
    let parameter_example = source_operations(source).any(|(_, parameters)| {
        parameters.iter().any(|parameter| {
            let Some(schema) = parameter.schema.as_ref() else {
                return false;
            };
            let composed_path = is_path(parameter)
                && schema.reference.is_none()
                && (schema.any_of.is_some() || schema.one_of.is_some());
            let referenced_query = is_query(parameter)
                && parameter.required == Some(true)
                && schema.reference.is_some()
                && schema
                    .ty
                    .as_ref()
                    .and_then(crate::openapi::TypeField::primary)
                    == Some("string");
            argument_names(&parameter.name, name)
                && fern_value == format!("{:?}", parameter.name)
                && (composed_path || referenced_query)
                && (if referenced_query {
                    parameter.example.as_ref()
                } else {
                    declared_schema_example(schema)
                })
                .filter(|example| example.is_string())
                .filter(|example| {
                    !referenced_query
                        || crate::openapi::example_validation::matches(
                            &source.components.schemas,
                            schema,
                            example,
                            0,
                        ) == Some(true)
                })
                .and_then(crate::ir::example_literal)
                .is_some_and(|literal| literal == value)
        })
    });
    if parameter_example {
        return true;
    }
    annotated_reference_property_example(source, name, fern_value, value)
}

/// A locally referenced unconstrained string, the measured reference-example shape.
fn plain_string_reference(source: &crate::openapi::OpenApi, reference: &str) -> bool {
    reference
        .strip_prefix("#/components/schemas/")
        .and_then(|name| source.components.schemas.get(name))
        .is_some_and(|target| {
            target
                .ty
                .as_ref()
                .and_then(crate::openapi::TypeField::primary)
                == Some("string")
                && target.format.is_none()
                && target.pattern.is_none()
                && target.min_length.is_none()
                && target.max_length.is_none()
                && target.enum_values.is_none()
                && target.const_value.is_none()
                && target.reference.is_none()
                && target.all_of.is_none()
                && target.one_of.is_none()
                && target.any_of.is_none()
                && target.not_schema.is_none()
                && !target.drops_applicator()
                && target.unmodeled_keywords.is_empty()
                && target.type_crozier.is_none()
                && target.type_fern.is_none()
        })
}

fn annotated_reference_property_example(
    source: &crate::openapi::OpenApi,
    name: &str,
    fern_value: &str,
    value: &str,
) -> bool {
    let mut property_example = false;
    visit_source_schemas(Some(source), &mut |schema| {
        for (wire, property) in &schema.properties {
            let Some(members) = property.all_of.as_ref() else {
                continue;
            };
            let reference_count = members
                .iter()
                .filter(|member| member.reference.is_some())
                .count();
            let description_members = members
                .iter()
                .filter(|member| member.reference.is_none())
                .all(|member| {
                    member.description.is_some()
                        && member.ty.is_none()
                        && member.properties.is_empty()
                        && member.items.is_none()
                        && member.all_of.is_none()
                        && member.any_of.is_none()
                        && member.one_of.is_none()
                });
            property_example |= schema.required.contains(wire)
                && argument_names(wire, name)
                && fern_value == format!("{wire:?}")
                && members.len() >= 2
                && reference_count == 1
                && members
                    .iter()
                    .filter_map(|member| member.reference.as_deref())
                    .all(|reference| plain_string_reference(source, reference))
                && description_members
                && declared_schema_example(property)
                    .filter(|example| example.is_string())
                    .filter(|example| {
                        crate::openapi::example_validation::matches(
                            &source.components.schemas,
                            property,
                            example,
                            0,
                        ) == Some(true)
                    })
                    .and_then(crate::ir::example_literal)
                    .is_some_and(|literal| literal == value);
        }
    });
    property_example
}

/// Whether an operation's successful responses answer only `text/*` content.
fn text_only_success(operation: &crate::openapi::Operation) -> bool {
    let mut media = operation
        .responses
        .iter()
        .filter(|(status, _)| status.starts_with('2'))
        .flat_map(|(_, response)| response.content.keys())
        .peekable();
    media.peek().is_some() && media.all(|media_type| media_type.starts_with("text/"))
}

/// `text-response-optional-query-examples`: a worked-example argument line only
/// crozier writes, `<name>=<example>,`, passing an optional query parameter of
/// an operation whose successful responses are all `text/*`, where the value
/// is one the parameter or its schema declares.
fn text_response_optional_query_examples(pair: &Pair<'_>, crozier: &str) -> bool {
    if !example_file(pair.rel) {
        return false;
    }
    let Some((_, name, value)) = keyword_argument_line(crozier) else {
        return false;
    };
    let Some(source) = pair.context.source_document.as_ref() else {
        return false;
    };
    source_operations(source)
        .filter(|(operation, _)| text_only_success(operation))
        .any(|(_, parameters)| {
            parameters.iter().any(|parameter| {
                is_query(parameter)
                    && parameter.required != Some(true)
                    && argument_names(&parameter.name, name)
                    && declared_parameter_examples(parameter)
                        .filter_map(crate::ir::example_literal)
                        .any(|literal| literal == value)
            })
        })
}

/// The list argument a worked example's line `at` belongs to, when it is one:
/// its keyword and its items' text. A list on one line, `<name>=[a, b],`, is its
/// own block; a wrapped one runs from `<indent><name>=[` to `<indent>],` with
/// one item on each line between.
fn list_argument_at<'l>(lines: &[&'l str], at: usize) -> Option<(&'l str, Vec<&'l str>)> {
    let line = *lines.get(at)?;
    if let Some((_, name, value)) = keyword_argument_line(line) {
        let items = value.strip_prefix('[')?.strip_suffix(']')?;
        let items = if items.is_empty() {
            Vec::new()
        } else {
            items.split(", ").collect()
        };
        return Some((name, items));
    }
    // The nearest opener at or above the line, indented no deeper than it:
    // the line itself, the list an item or the closer belongs to.
    let depth = |line: &str| line.len() - line.trim_start().len();
    let opener = (0..=at)
        .rev()
        .find(|&index| lines[index].ends_with("=[") && depth(lines[index]) <= depth(line))?;
    let indent = &lines[opener][..depth(lines[opener])];
    let name = lines[opener].trim_start().strip_suffix("=[")?;
    let closer = (opener + 1..lines.len()).find(|&index| lines[index] == format!("{indent}],"))?;
    if at > closer || !python_identifier(name) {
        return None;
    }
    // Every item is flat, on its own line one level in.
    let items = lines[opener + 1..closer]
        .iter()
        .map(|item| {
            let item = item.strip_prefix(indent)?.strip_prefix("    ")?;
            (!item.starts_with(' ') && !item.is_empty()).then(|| item.trim_end_matches(','))
        })
        .collect::<Option<Vec<_>>>()?;
    Some((name, items))
}

/// Whether a list item's Python text is the JSON value `expected`: a number of
/// equal value (`1.0` for `1`), a string, or a boolean.
fn item_is_value(item: &str, expected: &serde_json::Value) -> bool {
    match expected {
        serde_json::Value::Number(number) => item
            .parse::<f64>()
            .ok()
            .zip(number.as_f64())
            .is_some_and(|(left, right)| left == right),
        serde_json::Value::String(_) => {
            crate::ir::example_literal(expected).as_deref() == Some(item)
        }
        serde_json::Value::Bool(value) => item == if *value { "True" } else { "False" },
        _ => false,
    }
}

/// `optional-lowered-required-query-array-example`: a line only crozier writes
/// that belongs to a worked example's list argument for a required query array
/// parameter, whose items are exactly the array example the parameter or its
/// schema declares. A synthesized list is not admitted.
fn optional_lowered_required_query_array_example(pair: &Pair<'_>, at: usize) -> bool {
    if !example_file(pair.rel) {
        return false;
    }
    let Some((name, items)) = list_argument_at(pair.crozier, at) else {
        return false;
    };
    let Some(source) = pair.context.source_document.as_ref() else {
        return false;
    };
    source_operations(source).any(|(_, parameters)| {
        parameters.iter().any(|parameter| {
            is_query(parameter)
                && parameter.required == Some(true)
                && parameter
                    .schema
                    .as_ref()
                    .and_then(|schema| schema.ty.as_ref()?.primary())
                    == Some("array")
                && argument_names(&parameter.name, name)
                && declared_parameter_examples(parameter).any(|example| {
                    example.as_array().is_some_and(|values| {
                        !values.is_empty()
                            && values.len() == items.len()
                            && values
                                .iter()
                                .zip(&items)
                                .all(|(value, item)| item_is_value(item, value))
                    })
                })
        })
    })
}

/// Whether crozier's line `at` is the one-line keyword argument `<field>=<value>,`
/// of a worked example's `<Class>(` constructor, where the reference's model
/// `Class` requires `field` and types it by a union opening with an optional
/// alternative: the argument Fern's example omits (`required-null-union-field-example`).
fn required_null_union_field_example(pair: &Pair<'_>, at: usize) -> bool {
    if !example_file(pair.rel) {
        return false;
    }
    let Some((indent, name, value)) = pair
        .crozier
        .get(at)
        .and_then(|line| keyword_argument_line(line))
    else {
        return false;
    };
    // One line only: a value opening a bracket continues onto lines of its own.
    if value.is_empty() || value.ends_with(['(', '[', '{']) {
        return false;
    }
    let Some(opener) = pair.crozier[..at].iter().rev().find(|line| {
        let trimmed = line.trim_start();
        !trimmed.is_empty() && line.len() - trimmed.len() < indent.len()
    }) else {
        return false;
    };
    let Some(class) = opener.trim_start().strip_suffix('(') else {
        return false;
    };
    python_identifier(class)
        && pair
            .context
            .reference_null_union_fields()
            .contains(&(class.to_string(), name.to_string()))
}

/// Every `(class, field)` of the models `sources` define whose field line is
/// `    field: Alias` with no default, where `Alias` is a module-level
/// `typing.Union[…]` whose first alternative is `typing.Optional[…]`: a required
/// field Fern examples as null, since its union opens with a nullable member.
fn required_null_union_fields<'a>(
    sources: impl IntoIterator<Item = (&'a str, &'a str)>,
) -> BTreeSet<(String, String)> {
    let sources: Vec<(&str, &str)> = sources
        .into_iter()
        .filter(|(rel, _)| rel.ends_with(".py"))
        .collect();
    let mut nullable_unions = BTreeSet::new();
    for (_, text) in &sources {
        let lines: Vec<&str> = text.lines().collect();
        for (index, line) in lines.iter().enumerate() {
            let Some((alias, rest)) = line.split_once(" = typing.Union[") else {
                continue;
            };
            if !python_identifier(alias) {
                continue;
            }
            let first = if rest.is_empty() {
                lines.get(index + 1).map_or("", |next| next.trim_start())
            } else {
                rest
            };
            if first.starts_with("typing.Optional[") {
                nullable_unions.insert(alias.to_string());
            }
        }
    }
    let mut fields = BTreeSet::new();
    for (_, text) in &sources {
        let mut class = None;
        for line in text.lines() {
            if let Some(rest) = line.strip_prefix("class ") {
                class = rest
                    .split_once('(')
                    .map(|(name, _)| name.to_string())
                    .filter(|name| python_identifier(name));
                continue;
            }
            if !line.starts_with(' ') && !line.trim().is_empty() {
                class = None;
                continue;
            }
            let (Some(class), Some(field)) = (class.as_ref(), line.strip_prefix("    ")) else {
                continue;
            };
            let Some((name, annotation)) = field.split_once(": ") else {
                continue;
            };
            if python_identifier(name) && nullable_unions.contains(annotation) {
                fields.insert((class.clone(), name.to_string()));
            }
        }
    }
    fields
}

/// The descriptions of every source property that is an `anyOf`/`oneOf` of two
/// or more non-null inline alternatives, the first of them undescribed, with a
/// description of its own: keyed by the property's wire name.
fn collapsed_property_descriptions(source: &crate::openapi::OpenApi) -> Vec<(String, String)> {
    let mut found = Vec::new();
    let mut visit = |schema: &crate::openapi::Schema| {
        for (name, property) in &schema.properties {
            let Some(members) = property.any_of.as_ref().or(property.one_of.as_ref()) else {
                continue;
            };
            let alternatives: Vec<_> = members
                .iter()
                .filter(|member| member.ty.as_ref().and_then(|ty| ty.primary()) != Some("null"))
                .collect();
            let Some(description) = property.description.as_deref() else {
                continue;
            };
            if property.reference.is_none()
                && alternatives.len() >= 2
                && alternatives.iter().all(|member| {
                    member.reference.is_none()
                        && member.properties.is_empty()
                        && member.items.is_none()
                })
                && alternatives[0].description.is_none()
            {
                found.push((
                    name.clone(),
                    description.trim_end_matches(['\r', '\n']).to_string(),
                ));
            }
        }
    };
    visit_source_schemas(Some(source), &mut visit);
    found
}

/// `collapsed-anyof-property-description`, on an aligned pair of lines: the
/// `reference.md` parameter row Fern writes bare, `**<name>:** `<type>` `, that
/// crozier ends with the property's description, and the model field Fern
/// declares bare, `<name>: <type>`, that crozier declares
/// `<name>: <type> = pydantic.Field()` to carry it.
fn collapsed_anyof_property_description(pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    let Some(source) = pair.context.source_document.as_ref() else {
        return false;
    };
    let properties = collapsed_property_descriptions(source);
    if pair.rel == "reference.md" {
        let Some(head) = fern.strip_suffix(' ') else {
            return false;
        };
        let Some(name) = head
            .strip_prefix("**")
            .and_then(|rest| rest.split_once(":** `"))
            .map(|(name, _)| name)
        else {
            return false;
        };
        return properties.iter().any(|(wire, description)| {
            argument_names(wire, name)
                && crozier
                    == format!(
                        "{head}{}",
                        crate::emit::reference_param_suffix(Some(description))
                    )
        });
    }
    pair.rel.ends_with(".py")
        && crozier.strip_suffix(" = pydantic.Field()") == Some(fern)
        && fern.trim_start().split_once(": ").is_some_and(|(name, _)| {
            fern.starts_with("    ")
                && properties
                    .iter()
                    .any(|(wire, _)| argument_names(wire, name))
        })
}

/// `collapsed-anyof-property-description`, on a line only crozier writes: a
/// line of the description a `client.py`/`raw_client.py` docstring documents
/// under `<name> : <type>`, or of the docstring block (with the blank line
/// after it) that follows a model's `<name>: <type> = pydantic.Field()`. The
/// block's text must be the property's description.
fn collapsed_anyof_property_description_line(pair: &Pair<'_>, at: usize) -> bool {
    if !pair.rel.ends_with(".py") {
        return false;
    }
    let Some(source) = pair.context.source_document.as_ref() else {
        return false;
    };
    let lines = pair.crozier;
    let described = |name: &str, text: &str| {
        collapsed_property_descriptions(source)
            .iter()
            .any(|(wire, description)| argument_names(wire, name) && description.trim() == text)
    };
    // A model field's docstring block: `"""`, the description, `"""`, blank.
    if let Some(field) = (at.saturating_sub(64)..=at).rev().find(|&index| {
        lines[index].starts_with("    ")
            && !lines[index].starts_with("     ")
            && lines[index].ends_with(" = pydantic.Field()")
    }) {
        let open = field + 1;
        if lines.get(open) == Some(&"    \"\"\"") {
            if let Some(close) = (open + 1..lines.len()).find(|&index| lines[index] == "    \"\"\"")
            {
                let blank = close + 1;
                let text = lines[open + 1..close]
                    .iter()
                    .map(|line| line.strip_prefix("    ").unwrap_or(line))
                    .collect::<Vec<_>>()
                    .join("\n");
                let name = lines[field]
                    .trim_start()
                    .split_once(": ")
                    .map_or("", |(name, _)| name);
                if (open..=blank).contains(&at)
                    && lines.get(blank).is_some_and(|line| line.is_empty())
                    && described(name, text.trim())
                {
                    return true;
                }
            }
        }
    }
    // A method docstring's parameter description, indented one level under
    // `<name> : <type>`.
    let indent = lines[at].len() - lines[at].trim_start().len();
    if lines[at].trim().is_empty() || indent < 4 {
        return false;
    }
    let Some(header) = (0..at).rev().find(|&index| {
        let line = lines[index];
        line.trim().is_empty() || line.len() - line.trim_start().len() < indent
    }) else {
        return false;
    };
    let header_line = lines[header];
    if header_line.len() - header_line.trim_start().len() + 4 != indent {
        return false;
    }
    let Some((name, _)) = header_line.trim_start().split_once(" : ") else {
        return false;
    };
    let end = (header + 1..lines.len())
        .find(|&index| {
            lines[index].trim().is_empty()
                || lines[index].len() - lines[index].trim_start().len() < indent
        })
        .unwrap_or(lines.len());
    let text = lines[header + 1..end]
        .iter()
        .map(|line| &line[indent..])
        .collect::<Vec<_>>()
        .join("\n");
    described(name, text.trim())
}

/// The module directories crozier's package holds, each the directory of a
/// `client.py` under `src/<package>/`.
fn crozier_modules(context: &Context) -> BTreeSet<String> {
    context
        .crozier_paths()
        .iter()
        .filter_map(|path| {
            let rest = path.strip_prefix("src/")?;
            let (_, module) = rest.split_once('/')?;
            module.strip_suffix("/client.py").map(str::to_string)
        })
        .collect()
}

/// `emoji-tag-reference-identifiers`: a `README.md` or `reference.md` line Fern
/// writes with a tag's raw spelling, its words joined by `_` with a character
/// no Python identifier admits kept (`⚠️_not_supported_yet`), where crozier's
/// line is the same with the identifier crozier's package uses for that tag's
/// module (`not_supported_yet`) at every occurrence.
fn emoji_tag_reference_identifiers(pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    if !DOCS_FILES.contains(&pair.rel) || fern == crozier {
        return false;
    }
    let Some(source) = pair.context.source_document.as_ref() else {
        return false;
    };
    let modules = crozier_modules(pair.context);
    source
        .paths
        .values()
        .flat_map(|item| item.operations())
        .flat_map(|(_, operation)| &operation.tags)
        .any(|tag| {
            let raw = tag
                .to_lowercase()
                .split_whitespace()
                .collect::<Vec<_>>()
                .join("_");
            let identifier: String = raw
                .chars()
                .filter(|character| character.is_ascii_alphanumeric() || *character == '_')
                .collect::<String>()
                .trim_matches('_')
                .to_string();
            // A heading's link into the raw-spelt module Fern's tree does not
            // hold anchors nothing; crozier's anchor is part of the correction.
            let unanchored = reference_heading_without_anchor(pair, crozier);
            let line = unanchored.as_deref().unwrap_or(crozier);
            raw != identifier
                && python_identifier(&identifier)
                && modules.contains(&identifier)
                && line.contains(identifier.as_str())
                && line.replace(identifier.as_str(), &raw) == fern
        })
}

/// `bracket-query-parameter-call-keyword`: an argument whose wire name ends in
/// `[]`, named in Markdown. In a README or `reference.md` worked call, the
/// keyword of such a query parameter: Fern writes `<name>_array=`, which the
/// generated method does not take, and crozier the method's own `<name>=`. In a
/// `reference.md` parameter list, the `**<name>_array:**` entry of such a query
/// parameter or form property, where crozier lists the argument the method
/// declares, `**<name>:**`. The source document must declare the parameter or
/// property, and every other byte of the line is the same.
fn bracket_query_parameter_call_keyword(pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    if !DOCS_FILES.contains(&pair.rel) || fern == crozier {
        return false;
    }
    let Some(source) = pair.context.source_document.as_ref() else {
        return false;
    };
    if let Some((keyword, rest)) = crozier
        .strip_prefix("**")
        .and_then(|entry| entry.split_once(":**"))
    {
        return pair.rel == "reference.md"
            && python_identifier(keyword)
            && bracket_stems(source).iter().any(|stem| {
                crate::naming::field_name(stem) == keyword
                    && fern
                        == format!(
                            "**{}:**{rest}",
                            crate::naming::field_name(&format!("{stem}_array"))
                        )
            });
    }
    let argument = crozier.trim_start();
    let indent = &crozier[..crozier.len() - argument.len()];
    let Some((keyword, value)) = argument.split_once('=') else {
        return false;
    };
    if !python_identifier(keyword) || value.is_empty() {
        return false;
    }
    source_operations(source).any(|(_, parameters)| {
        parameters.iter().any(|parameter| {
            parameter.name.strip_suffix("[]").is_some_and(|stem| {
                is_query(parameter)
                    && crate::naming::field_name(stem) == keyword
                    && fern
                        == format!(
                            "{indent}{}={value}",
                            crate::naming::field_name(&format!("{stem}_array"))
                        )
            })
        })
    })
}

/// The stem before `[]` of every query parameter, and every form-encoded or
/// multipart request-body property, whose wire name ends in `[]`. A body schema
/// named by `$ref` is read from `components.schemas`.
fn bracket_stems(source: &crate::openapi::OpenApi) -> BTreeSet<&str> {
    let mut stems = BTreeSet::new();
    for (operation, parameters) in source_operations(source) {
        stems.extend(
            parameters
                .iter()
                .filter(|parameter| is_query(parameter))
                .filter_map(|parameter| parameter.name.strip_suffix("[]")),
        );
        let forms = operation.request_body.iter().flat_map(|body| {
            body.content
                .iter()
                .filter(|(media, _)| {
                    media.starts_with("application/x-www-form-urlencoded")
                        || media.starts_with("multipart/form-data")
                })
                .filter_map(|(_, media)| media.schema.as_ref())
        });
        for schema in forms {
            let schema = schema
                .reference
                .as_deref()
                .and_then(|reference| reference.strip_prefix("#/components/schemas/"))
                .and_then(|name| source.components.schemas.get(name))
                .unwrap_or(schema);
            stems.extend(
                schema
                    .properties
                    .keys()
                    .filter_map(|name| name.strip_suffix("[]")),
            );
        }
    }
    stems
}

/// `non-string-client-header-example`: in a `client.py` docstring's client
/// construction, a promoted header the source document declares `boolean`,
/// `integer` or `number`. Fern passes the `YOUR_<NAME>` string placeholder its
/// string headers take; crozier passes the generator's own placeholder for the
/// declared type (`True`, `1`, `1.1`). Every other byte of the line is the same.
fn non_string_client_header_example(pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    if !pair.rel.ends_with("client.py") || pair.rel.ends_with("raw_client.py") || fern == crozier {
        return false;
    }
    let argument = crozier.trim_start();
    let indent = &crozier[..crozier.len() - argument.len()];
    let Some((name, value)) = argument
        .strip_suffix(',')
        .and_then(|argument| argument.split_once('='))
    else {
        return false;
    };
    if fern != format!("{indent}{name}=\"YOUR_{}\",", name.to_uppercase()) {
        return false;
    }
    // A header crozier's constructor types as a one-value `typing.Literal` takes
    // that value, which the placeholder is not.
    if let Some(literal) = value
        .strip_prefix('"')
        .and_then(|value| value.strip_suffix('"'))
        .filter(|literal| !literal.contains(['"', '\\']))
    {
        let annotation = format!("typing.Literal[\"{literal}\"]");
        return pair
            .context
            .client_modules()
            .crozier
            .values()
            .any(|module| {
                module.contains(&format!("        {name}: {annotation},"))
                    || module.contains(&format!(
                        "        {name}: typing.Optional[{annotation}] = None,"
                    ))
            });
    }
    // An array header crozier's constructor types `typing.List[...]` takes a
    // list, which the placeholder is not.
    if value.starts_with('[') && value.ends_with(']') {
        return pair
            .context
            .client_modules()
            .crozier
            .values()
            .any(|module| {
                module.contains(&format!("        {name}: typing.List["))
                    || module.contains(&format!("        {name}: typing.Optional[typing.List["))
            });
    }
    let declared = match value {
        "True" => "boolean",
        "1" => "integer",
        "1.1" => "number",
        _ => return false,
    };
    let Some(source) = pair.context.source_document.as_ref() else {
        return false;
    };
    source_operations(source).any(|(_, parameters)| {
        parameters.iter().any(|parameter| {
            parameter.location == Some(crate::openapi::ParameterLocation::Header)
                && crate::naming::field_name(crate::ir::header_param_stem(&parameter.name)) == name
                && parameter
                    .schema
                    .as_ref()
                    .and_then(|schema| schema.ty.as_ref()?.primary())
                    == Some(declared)
        })
    })
}

/// A `reference.md` heading link's range, `L<start>-L<end>`: the documented
/// method's `def` line through its last line, both 1-based.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
struct LineRange {
    start: usize,
    end: usize,
}

impl LineRange {
    /// `L<start>-L<end>` with `0 < start <= end`; `None` for anything else.
    fn parse(text: &str) -> Option<Self> {
        let (start, end) = text.strip_prefix('L')?.split_once("-L")?;
        let number = |text: &str| {
            (!text.is_empty() && text.bytes().all(|b| b.is_ascii_digit()))
                .then(|| text.parse::<usize>().ok())
                .flatten()
        };
        let (start, end) = (number(start)?, number(end)?);
        (0 < start && start <= end).then_some(Self { start, end })
    }
}

impl std::fmt::Display for LineRange {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "L{}-L{}", self.start, self.end)
    }
}

/// A `reference.md` heading split around its link:
/// `<head><a href="<module>[#<range>]"><method></a><tail>`.
#[derive(Debug, Clone, PartialEq, Eq)]
struct ReferenceHeading {
    head: String,
    module: String,
    range: Option<LineRange>,
    method: String,
    tail: String,
}

impl ReferenceHeading {
    /// The heading `line`, or `None` for a line that is no heading or whose
    /// link's fragment is not a line range.
    fn parse(line: &str) -> Option<Self> {
        if !line.starts_with("<details><summary><code>client.") {
            return None;
        }
        let (head, rest) = line.split_once("<a href=\"")?;
        let (href, rest) = rest.split_once("\">")?;
        let (method, tail) = rest.split_once("</a>")?;
        let (module, range) = match href.split_once('#') {
            Some((module, range)) => (module, Some(LineRange::parse(range)?)),
            None => (href, None),
        };
        Some(Self {
            head: head.to_string(),
            module: module.to_string(),
            range,
            method: method.to_string(),
            tail: tail.to_string(),
        })
    }

    /// The heading with `module` and `range` as its link.
    fn render(&self) -> String {
        let range = self
            .range
            .map(|range| format!("#{range}"))
            .unwrap_or_default();
        format!(
            "{}<a href=\"{}{range}\">{}</a>{}",
            self.head, self.module, self.method, self.tail
        )
    }

    /// Whether its range is exactly its method's lines in `tree`'s module.
    fn range_is_its_method(&self, context: &Context, tree: Tree) -> bool {
        self.range.is_some()
            && context.client_method_lines(tree, &self.module, &self.method) == self.range
    }

    /// The same heading without a range.
    fn without_range(&self) -> Self {
        Self {
            range: None,
            ..self.clone()
        }
    }
}

/// crozier's `reference.md` heading `line` without its link's range, when the
/// range is exactly the documented method's lines in crozier's linked client:
/// crozier anchors every heading at the method it documents, where Fern's
/// lookup of a name its SDK does not define finds no lines and leaves the bare
/// path. `None` for any other line.
fn reference_heading_without_anchor(pair: &Pair<'_>, line: &str) -> Option<String> {
    let heading = ReferenceHeading::parse(line)?;
    heading
        .range_is_its_method(pair.context, Tree::Crozier)
        .then(|| heading.without_range().render())
}

/// `empty-namespace-package`'s `reference.md` heading: both sides link the `_`
/// package's `src/<package>/_/client.py`, which only crozier's tree holds, so
/// only crozier's link carries the `#L<start>-L<end>` range of the documented
/// method, exactly its lines there. Every other byte of the line is Fern's.
fn empty_namespace_reference_anchor(pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    if pair.rel != "reference.md" || fern == crozier {
        return false;
    }
    let Some(heading) = ReferenceHeading::parse(crozier) else {
        return false;
    };
    heading.module.ends_with("/_/client.py")
        && heading.module.starts_with("src/")
        && heading.without_range().render() == fern
        && !pair
            .context
            .holds_client_module(Tree::Reference, &heading.module)
        && heading.range_is_its_method(pair.context, Tree::Crozier)
}

/// Two `reference.md` heading lines with their ranges taken out, when both link
/// the same module and method and each range is exactly that method's lines in
/// its own tree's client: the ranges then differ only because the clients do
/// (`reference-anchor-follows-corrected-client`), and a heading rule judges the
/// rest of the line. Otherwise the lines as they are.
fn without_verified_ranges<'a>(
    pair: &Pair<'_>,
    fern: &'a str,
    crozier: &'a str,
) -> (std::borrow::Cow<'a, str>, std::borrow::Cow<'a, str>) {
    use std::borrow::Cow;
    let (Some(fern_heading), Some(crozier_heading)) = (
        ReferenceHeading::parse(fern),
        ReferenceHeading::parse(crozier),
    ) else {
        return (Cow::Borrowed(fern), Cow::Borrowed(crozier));
    };
    if fern_heading.module != crozier_heading.module
        || fern_heading.method != crozier_heading.method
        || !fern_heading.range_is_its_method(pair.context, Tree::Reference)
        || !crozier_heading.range_is_its_method(pair.context, Tree::Crozier)
    {
        return (Cow::Borrowed(fern), Cow::Borrowed(crozier));
    }
    (
        Cow::Owned(fern_heading.without_range().render()),
        Cow::Owned(crozier_heading.without_range().render()),
    )
}

/// A flat tree's `reference.md` heading as Fern writes its link: crozier links
/// the module the flat tree holds (`pet/client.py#L34-L93`), where Fern links
/// `src/<package>/pet/client.py`, which its own flat tree does not hold, and so
/// carries no range. `Some` with crozier's line in Fern's link form when Fern's
/// link is exactly `src/<package>/` before crozier's module, Fern's tree lacks
/// that module, and crozier's range is exactly the named method's lines in its
/// own; `None` otherwise.
fn flat_link_in_fern_form(pair: &Pair<'_>, fern: &str, crozier: &str) -> Option<String> {
    let (fern_heading, crozier_heading) = (
        ReferenceHeading::parse(fern)?,
        ReferenceHeading::parse(crozier)?,
    );
    let (package, packaged) = fern_heading.module.strip_prefix("src/")?.split_once('/')?;
    (packaged == crozier_heading.module
        && !package.is_empty()
        && fern_heading.range.is_none()
        && !pair
            .context
            .holds_client_module(Tree::Reference, &fern_heading.module)
        && crozier_heading.range_is_its_method(pair.context, Tree::Crozier))
    .then(|| {
        ReferenceHeading {
            module: fern_heading.module.clone(),
            range: None,
            ..crozier_heading.clone()
        }
        .render()
    })
}

/// `flat-reference-link-target`: a flat tree's `reference.md` heading linking
/// the module the tree holds, with its range, where Fern links a `src/` path
/// its flat tree does not hold (see [`flat_link_in_fern_form`]). Every other
/// byte of the line is Fern's.
fn flat_reference_link_target(pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    pair.rel == "reference.md"
        && fern != crozier
        && flat_link_in_fern_form(pair, fern, crozier).is_some_and(|line| line == fern)
}

/// The classes crozier gave components whose class Fern's merges with another
/// (`colliding-component-own-class`), each with the class Fern writes in its
/// place: `KilnGlazeCoat2` for `KilnGlazeCoat`. Read from the source document's
/// load, which records each renamed component's shared class.
fn colliding_classes(context: &Context) -> Vec<(String, String)> {
    let Some(document) = context.source_document.as_ref() else {
        return Vec::new();
    };
    document
        .components
        .schemas
        .iter()
        .filter_map(|(key, schema)| {
            let shared = schema.colliding_class.as_ref()?;
            Some((crate::naming::class_name(key), shared.clone()))
        })
        .collect()
}

/// The starts of `identifier`'s whole-identifier occurrences in `text`.
fn identifier_starts(text: &str, identifier: &str) -> Vec<usize> {
    let word = |c: char| c.is_alphanumeric() || c == '_';
    text.match_indices(identifier)
        .map(|(start, _)| start)
        .filter(|start| {
            !text[..*start].chars().next_back().is_some_and(word)
                && !text[start + identifier.len()..].chars().next().is_some_and(word)
        })
        .collect()
}

/// Whether `text` names `identifier` as a whole identifier.
fn names_identifier(text: &str, identifier: &str) -> bool {
    !identifier_starts(text, identifier).is_empty()
}

/// `text` with every whole-identifier `from` written `to`.
fn replace_identifier(text: &str, from: &str, to: &str) -> String {
    let mut out = String::with_capacity(text.len());
    let mut done = 0;
    for start in identifier_starts(text, from) {
        out.push_str(&text[done..start]);
        out.push_str(to);
        done = start + from.len();
    }
    out.push_str(&text[done..]);
    out
}

/// crozier's line as Fern writes it: each renamed class (and its module) read
/// as the class Fern merges it into, a name an import list then repeats kept
/// once.
fn colliding_line_in_fern_form(line: &str, renames: &[(String, String)]) -> String {
    let mut text = line.to_string();
    for (own, shared) in renames {
        text = replace_identifier(&text, own, shared);
        text = replace_identifier(
            &text,
            &crate::naming::module_name(own),
            &crate::naming::module_name(shared),
        );
    }
    // An item repeating the end of the one before it (`import A, A`,
    // `{"A": ".a", "A": ".a"}`, `["A", "A"]`) is dropped, its closing brackets
    // kept.
    let word = |c: char| c.is_alphanumeric() || c == '_';
    let mut out = String::new();
    for (index, item) in text.split(", ").enumerate() {
        let core = item.trim_end_matches([']', '}', ')']);
        let repeats = index > 0
            && !core.is_empty()
            && out.ends_with(core)
            && !out[..out.len() - core.len()].chars().next_back().is_some_and(word);
        if repeats {
            out.push_str(&item[core.len()..]);
        } else {
            if index > 0 {
                out.push_str(", ");
            }
            out.push_str(item);
        }
    }
    out
}

/// `colliding-component-own-class`: a line naming a component's own class
/// where Fern names the class it merged that component into, and which is
/// otherwise Fern's line (`left: typing.Optional[KilnGlazeCoat2] = OMIT,` for
/// `left: typing.Optional[KilnGlazeCoat] = OMIT,`; `KilnGlazeCoat,
/// KilnGlazeCoat2` imported for `KilnGlazeCoat`).
fn colliding_component_own_class(pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    if fern == crozier {
        return false;
    }
    let renames = colliding_classes(pair.context);
    !renames.is_empty() && colliding_line_in_fern_form(crozier, &renames) == fern
}

/// `colliding-component-own-class`: a line only crozier writes that names a
/// renamed component's class or module — its import, its lazy-import entry and
/// its `__all__` entry.
fn colliding_component_own_class_line(pair: &Pair<'_>, crozier: &str) -> bool {
    colliding_classes(pair.context).iter().any(|(own, _)| {
        names_identifier(crozier, own)
            || names_identifier(crozier, &crate::naming::module_name(own))
    })
}

/// `colliding-component-own-class`: the module only crozier writes for a
/// renamed component, under a `types/` package.
fn colliding_component_own_class_file(context: &Context, rel: &str, side: Side) -> bool {
    side == Side::Crozier
        && colliding_classes(context).iter().any(|(own, _)| {
            rel.ends_with(&format!("/types/{}.py", crate::naming::module_name(own)))
        })
}

/// `reference-anchor-follows-corrected-client`: a `reference.md` heading whose
/// only difference is its link's `#L<start>-L<end>` range, where each side's
/// range is exactly the documented method's lines in its own tree's linked
/// client. The ranges differ only because the two clients do: a departure
/// crozier makes in that file adds or removes lines above or inside the method,
/// so Fern's range would name the wrong lines of crozier's client. A region of
/// the one heading line, so the file's other departures, which each compare
/// the rest of the file whole, see Fern's heading there.
fn reference_anchor_follows_corrected_client(pair: &Pair<'_>) -> Result<Option<Region>, String> {
    if pair.rel != "reference.md" {
        return Ok(None);
    }
    for (at, crozier) in pair.crozier.iter().enumerate() {
        if pair.fern.contains(crozier) {
            continue;
        }
        let Some(crozier_heading) =
            ReferenceHeading::parse(crozier).filter(|heading| heading.range.is_some())
        else {
            continue;
        };
        let frame = crozier_heading.without_range();
        let mut matches = pair
            .fern
            .iter()
            .enumerate()
            .filter_map(|(index, fern)| Some((index, ReferenceHeading::parse(fern)?)))
            .filter(|(_, fern_heading)| {
                fern_heading.range.is_some() && fern_heading.without_range() == frame
            });
        let (Some((index, fern_heading)), None) = (matches.next(), matches.next()) else {
            continue;
        };
        if fern_heading.range_is_its_method(pair.context, Tree::Reference)
            && crozier_heading.range_is_its_method(pair.context, Tree::Crozier)
        {
            return Ok(Some(Region {
                fern: index..index + 1,
                crozier: at..at + 1,
            }));
        }
    }
    Ok(None)
}

/// `reference-heading-escaped-method-name`: a `reference.md` heading whose
/// method the SDK escapes with a trailing `_` (`all_`, `import_`). Fern's
/// heading names the method without it (`all`), which the client does not
/// define, so its link has no anchor; crozier's names the method the linked
/// file defines and anchors the link at its lines. Every other byte of the
/// line is the same.
fn reference_heading_escaped_method_name(pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    if pair.rel != "reference.md" || fern == crozier {
        return false;
    }
    let Some(bare) = reference_heading_without_anchor(pair, crozier) else {
        return false;
    };
    let Some((head, rest)) = bare.split_once("<a href=\"") else {
        return false;
    };
    let Some((path, rest)) = rest.split_once("\">") else {
        return false;
    };
    let Some((method, tail)) = rest.split_once("</a>") else {
        return false;
    };
    let unescaped = method.trim_end_matches('_');
    method.len() > unescaped.len()
        && python_identifier(unescaped)
        && pair
            .context
            .crozier_method_returns()
            .contains_key(&(path.to_string(), method.to_string()))
        && (fern == format!("{head}<a href=\"{path}\">{unescaped}</a>{tail}")
            // A flat tree's link Fern writes into the `src/` tree it lacks.
            || fern
                .split_once("<a href=\"src/")
                .and_then(|(_, rest)| rest.split_once('/'))
                .is_some_and(|(package, _)| {
                    let packaged = format!("src/{package}/{path}");
                    !pair.context.holds_client_module(Tree::Reference, &packaged)
                        && fern == format!("{head}<a href=\"{packaged}\">{unescaped}</a>{tail}")
                }))
}

/// `digit-leading-property-example-keyword`: a worked call's argument line for
/// a body property whose name starts with a digit (`5gMmCauseValue`), which the
/// method takes as `_5g_mm_cause_value`. Fern's line passes
/// `f_5g_mm_cause_value` (a client docstring) or `f_value` (`reference.md`,
/// the name's last word), neither of which the method takes; crozier's passes
/// the parameter, which crozier's client declares, with the same value.
fn digit_leading_property_example_keyword(pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    if !(DOCS_FILES.contains(&pair.rel) || pair.rel.ends_with("client.py")) || fern == crozier {
        return false;
    }
    let argument = crozier.trim_start();
    let indent = &crozier[..crozier.len() - argument.len()];
    let Some((name, value)) = argument.split_once('=') else {
        return false;
    };
    let Some(stem) = name
        .strip_prefix('_')
        .filter(|stem| stem.starts_with(|c: char| c.is_ascii_digit()))
    else {
        return false;
    };
    if !python_identifier(name) || !value.ends_with(',') {
        return false;
    }
    let last = stem.rsplit('_').next().unwrap_or(stem);
    let fern_names = [format!("f_{stem}"), format!("f_{last}")];
    fern_names
        .iter()
        .any(|fern_name| fern == format!("{indent}{fern_name}={value}"))
        && pair
            .context
            .client_modules()
            .crozier
            .values()
            .any(|module| module.contains(&format!("        {name}: ")))
}

/// Only the underscore missing from a declared, generated method's documentation.
fn digit_leading_method_reference_identifiers(pair: &Pair<'_>, fern: &str, crozier: &str) -> bool {
    if !DOCS_FILES.contains(&pair.rel) || fern == crozier {
        return false;
    }
    let Some(source) = pair.context.source_document.as_ref() else {
        return false;
    };
    source
        .paths
        .values()
        .flat_map(|item| item.operations())
        .any(|(_, operation)| {
            let Some(id) = operation.operation_id.as_deref() else {
                return false;
            };
            if operation.sdk_method_name().is_some()
                || !id.starts_with(|character: char| character.is_ascii_digit())
            {
                return false;
            }
            let raw = crate::naming::to_snake_case(id);
            let identifier = crate::naming::sanitize_identifier(&raw);
            let generated = pair
                .context
                .crozier_method_returns()
                .keys()
                .any(|(_, method)| method == &identifier);
            let call =
                crozier
                    .split_once(&format!(".{identifier}("))
                    .is_some_and(|(head, tail)| {
                        let receiver = head.trim_start();
                        let receiver = receiver.strip_prefix("response = ").unwrap_or(receiver);
                        (receiver == "client" || receiver.starts_with("client."))
                            && receiver
                                .chars()
                                .all(|c| c.is_ascii_alphanumeric() || c == '_' || c == '.')
                            && format!("{head}.{raw}({tail}") == fern
                    });
            // Fern's misspelt name anchors nothing; crozier's anchor is part
            // of the same correction.
            let unanchored = reference_heading_without_anchor(pair, crozier);
            let heading_line = unanchored.as_deref().unwrap_or(crozier);
            let heading = heading_line.starts_with("<details><summary><code>client.")
                && heading_line
                    .split_once(&format!(">{identifier}</a>"))
                    .is_some_and(|(head, tail)| {
                        head.contains("<a href=\"")
                            && !head.contains("</a>")
                            && format!("{head}>{raw}</a>{tail}") == fern
                    });
            generated && (call || heading)
        })
}

#[cfg(test)]
mod tests {
    use super::*;

    // End-to-end rejection proof declined: `crozier compare` refuses only against a
    // Fern tree carrying the crafted defect, which Fern never writes, so each case
    // would cost a reference regeneration while handing the rule the same Pair these
    // cases build. Acceptance runs end to end in every golden comparison, pinned line
    // by line in tests/fixtures/departures-ledger.tsv.
    #[test]
    fn escaped_field_aliases_admit_only_a_declared_name_spelled_as_its_value() {
        let document = serde_json::json!({"components": {"schemas": {"Beacon": {
            "type": "object",
            "properties": {
                "relay\\\"code": {"type": "string"},
                "a\" + bearing + \"": {"type": "integer"},
                "call-sign": {"type": "string"}
            }
        }}}});
        let context = source_context(document, &[]);
        let rule: LineRule = escaped_field_alias_literal;
        let rel = "src/fern/types/beacon.py";
        for (fern, crozier) in [
            (
                r#"        typing.Optional[str], FieldMetadata(alias='relay"code'), pydantic.Field(alias='relay"code')"#,
                r#"        typing.Optional[str], FieldMetadata(alias='relay\\"code'), pydantic.Field(alias='relay\\"code')"#,
            ),
            (
                r#"        typing.Optional[int], FieldMetadata(alias="a" + bearing + ""), pydantic.Field(alias="a" + bearing + "")"#,
                r#"        typing.Optional[int], FieldMetadata(alias='a" + bearing + "'), pydantic.Field(alias='a" + bearing + "')"#,
            ),
        ] {
            assert!(line_holds(rule, rel, &context, fern, crozier), "{crozier}");
            // Any other change on the line still fails.
            assert!(!line_holds(
                rule,
                rel,
                &context,
                fern,
                &crozier.replace("typing.Optional[", "typing.List[")
            ));
            // Only generated Python, and only with the source declaring the name.
            assert!(!line_holds(rule, "reference.md", &context, fern, crozier));
            assert!(!line_holds(rule, rel, &Context::default(), fern, crozier));
        }
        // A name the source does not declare, or a plain alias, is no departure.
        assert!(!line_holds(
            rule,
            rel,
            &context,
            r#"        FieldMetadata(alias="b" + c + "")"#,
            r#"        FieldMetadata(alias='b" + c + "')"#
        ));
        assert!(!line_holds(
            rule,
            rel,
            &context,
            r#"        FieldMetadata(alias="call-sign")"#,
            r#"        FieldMetadata(alias="call_sign")"#
        ));
    }

    #[test]
    fn non_string_client_header_examples_admit_only_the_declared_type() {
        let document = serde_json::json!({"paths": {"/berths": {"get": {
            "parameters": [
                {"name": "X-Strict-Mode", "in": "header", "required": true, "schema": {"type": "boolean"}},
                {"name": "X-Shift-Number", "in": "header", "required": true, "schema": {"type": "integer"}},
                {"name": "X-Draft-Depth", "in": "header", "required": true, "schema": {"type": "number"}},
                {"name": "X-Tenant-Code", "in": "header", "required": true, "schema": {"type": "string"}},
                {"name": "strict_count", "in": "query", "schema": {"type": "integer"}}
            ],
            "responses": {}
        }}}});
        let context = source_context(document, &[]);
        let rule: LineRule = non_string_client_header_example;
        for rel in ["src/fern/client.py", "src/fern/berths/client.py"] {
            for (fern, crozier) in [
                (
                    "        strict_mode=\"YOUR_STRICT_MODE\",",
                    "        strict_mode=True,",
                ),
                (
                    "        shift_number=\"YOUR_SHIFT_NUMBER\",",
                    "        shift_number=1,",
                ),
                (
                    "        draft_depth=\"YOUR_DRAFT_DEPTH\",",
                    "        draft_depth=1.1,",
                ),
            ] {
                assert!(
                    line_holds(rule, rel, &context, fern, crozier),
                    "{rel}: {crozier}"
                );
            }
        }
        // A header crozier's constructor types as a one-value Literal takes that
        // value; another value, or a header typed `str`, is no departure.
        let literal = Context::from_sources(
            [],
            [(
                "src/fern/client.py",
                "class FernApi:\n    def __init__(\n        self,\n        *,\n        book: typing.Optional[typing.Literal[\"general\"]] = None,\n    ) -> None:\n        pass\n",
            )],
        );
        assert!(line_holds(
            rule,
            "src/fern/client.py",
            &literal,
            "        book=\"YOUR_BOOK\",",
            "        book=\"general\","
        ));
        for crozier in ["        book=\"draft\",", "        tenant=\"general\","] {
            assert!(
                !line_holds(
                    rule,
                    "src/fern/client.py",
                    &literal,
                    "        book=\"YOUR_BOOK\",",
                    crozier
                ),
                "{crozier}"
            );
        }
        // The value must be the declared type's placeholder, the line otherwise
        // unchanged, and the header a declared boolean or numeric one.
        let fern = "        strict_mode=\"YOUR_STRICT_MODE\",";
        for crozier in [
            "        strict_mode=1,",
            "        strict_mode=False,",
            "            strict_mode=True,",
            "        strict_mode=True",
        ] {
            assert!(
                !line_holds(rule, "src/fern/client.py", &context, fern, crozier),
                "{crozier}"
            );
        }
        assert!(!line_holds(
            rule,
            "src/fern/client.py",
            &context,
            "        tenant_code=\"YOUR_TENANT_CODE\",",
            "        tenant_code=1,"
        ));
        assert!(!line_holds(
            rule,
            "src/fern/client.py",
            &context,
            "        strict_count=\"YOUR_STRICT_COUNT\",",
            "        strict_count=1,"
        ));
        // Only the client docstrings: never a raw client or the Markdown files.
        for rel in ["src/fern/raw_client.py", "README.md", "reference.md"] {
            assert!(!line_holds(
                rule,
                rel,
                &context,
                fern,
                "        strict_mode=True,"
            ));
        }
        assert!(!line_holds(
            rule,
            "src/fern/client.py",
            &Context::default(),
            fern,
            "        strict_mode=True,"
        ));
    }

    #[test]
    fn bracket_query_call_keywords_admit_only_the_declared_parameter_spelled_out() {
        let document = serde_json::json!({"paths": {"/berths": {"get": {
            "parameters": [
                {"name": "codes[]", "in": "query", "schema": {"type": "array", "items": {"type": "string"}}},
                {"name": "zone[]", "in": "header", "schema": {"type": "string"}}
            ],
            "responses": {}
        }}}});
        let context = source_context(document, &[]);
        let rule: LineRule = bracket_query_parameter_call_keyword;
        for rel in ["README.md", "reference.md"] {
            assert!(line_holds(
                rule,
                rel,
                &context,
                "    codes_array=[",
                "    codes=["
            ));
            // Any other change on the line still fails.
            assert!(!line_holds(
                rule,
                rel,
                &context,
                "    codes_array=[",
                "    codes=[1,"
            ));
            assert!(!line_holds(
                rule,
                rel,
                &context,
                "    codes_array=[",
                "        codes=["
            ));
        }
        // Only a declared `[]` query parameter, never a header or another name.
        assert!(!line_holds(
            rule,
            "reference.md",
            &context,
            "    zone_array=[",
            "    zone=["
        ));
        assert!(!line_holds(
            rule,
            "reference.md",
            &context,
            "    ids_array=[",
            "    ids=["
        ));
        // Only the Markdown files; a docstring already passes the argument.
        assert!(!line_holds(
            rule,
            "src/fern/berths/client.py",
            &context,
            "    codes_array=[",
            "    codes=["
        ));
        assert!(!line_holds(
            rule,
            "reference.md",
            &Context::default(),
            "    codes_array=[",
            "    codes=["
        ));
    }

    #[test]
    fn bracket_parameter_list_entries_admit_only_a_declared_query_parameter_or_form_property() {
        let document = serde_json::json!({
            "paths": {
                "/berths": {"get": {
                    "parameters": [
                        {"name": "codes[]", "in": "query", "schema": {"type": "array", "items": {"type": "string"}}},
                        {"name": "zone[]", "in": "header", "schema": {"type": "string"}}
                    ],
                    "responses": {}
                }},
                "/invites": {"post": {
                    "requestBody": {"content": {"application/x-www-form-urlencoded": {
                        "schema": {"$ref": "#/components/schemas/Invite"}
                    }}},
                    "responses": {}
                }},
                "/notes": {"post": {
                    "requestBody": {"content": {"application/json": {
                        "schema": {"type": "object", "properties": {"tags[]": {"type": "string"}}}
                    }}},
                    "responses": {}
                }}
            },
            "components": {"schemas": {"Invite": {
                "type": "object",
                "properties": {"emails[]": {"type": "array", "items": {"type": "string"}}}
            }}}
        });
        let context = source_context(document, &[]);
        let rule: LineRule = bracket_query_parameter_call_keyword;
        for (fern, crozier) in [
            (
                "**codes_array:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` ",
                "**codes:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` ",
            ),
            (
                "**emails_array:** `typing.Optional[typing.List[str]]` ",
                "**emails:** `typing.Optional[typing.List[str]]` ",
            ),
        ] {
            assert!(
                line_holds(rule, "reference.md", &context, fern, crozier),
                "{crozier}"
            );
            // Only reference.md lists parameters.
            assert!(!line_holds(rule, "README.md", &context, fern, crozier));
            // Any other change on the line still fails.
            assert!(!line_holds(
                rule,
                "reference.md",
                &context,
                fern,
                &crozier.replace("typing.Optional[", "typing.List[")
            ));
        }
        // A header, a JSON body property or an undeclared name is no departure.
        for stem in ["zone", "tags", "ids"] {
            assert!(!line_holds(
                rule,
                "reference.md",
                &context,
                &format!("**{stem}_array:** `typing.Optional[str]` "),
                &format!("**{stem}:** `typing.Optional[str]` ")
            ));
        }
    }

    // End-to-end rejection proof declined: `crozier compare` refuses only against a
    // Fern tree carrying the crafted defect, which Fern never writes, so each case
    // would cost a reference regeneration while handing the rule the same Pair these
    // cases build. Acceptance runs end to end in every golden comparison, pinned line
    // by line in tests/fixtures/departures-ledger.tsv.
    #[test]
    fn digit_leading_documented_methods_require_the_declared_generated_identifier() {
        let document = serde_json::json!({"paths": {"/readings": {"get": {
            "operationId": "7readings", "responses": {}
        }}}});
        let context = source_context(
            document.clone(),
            &[(
                "src/fern/client.py",
                "    def _7readings(self) -> None:\n        pass\n",
            )],
        );
        let fern = "client.7readings()";
        let crozier = "client._7readings()";
        let rule: LineRule = digit_leading_method_reference_identifiers;
        for rel in ["README.md", "reference.md"] {
            assert!(line_holds(rule, rel, &context, fern, crozier));
            assert!(!line_holds(
                rule,
                rel,
                &context,
                fern,
                "client._7readings(changed=True)"
            ));
        }
        assert!(!line_holds(
            rule,
            "README.md",
            &context,
            "client.other(name=\"client.7readings()\")",
            "client.other(name=\"client._7readings()\")"
        ));
        assert!(!line_holds(
            rule,
            "src/fern/client.py",
            &context,
            fern,
            crozier
        ));
        let absent = source_context(document, &[]);
        assert!(!line_holds(rule, "README.md", &absent, fern, crozier));
        assert!(!line_holds(
            rule,
            "README.md",
            &Context::default(),
            fern,
            crozier
        ));
        assert!(!line_holds(
            rule,
            "README.md",
            &context,
            "print(\"7readings\")",
            "print(\"_7readings\")"
        ));
        assert!(line_holds(
            rule,
            "reference.md",
            &context,
            "<details><summary><code>client.<a href=\"client.py\">7readings</a>()</code></summary>",
            "<details><summary><code>client.<a href=\"client.py\">_7readings</a>()</code></summary>"
        ));
    }

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

    /// A tree's files as `(path, text)`.
    type Tree = Vec<(&'static str, String)>;

    /// Fern's empty-namespace tree and crozier's: Fern's `_` package at the
    /// package root, crozier's under `_/`.
    fn empty_namespace_trees() -> (Tree, Tree) {
        let client = |example: &str| {
            format!(
                "from ..core.client_wrapper import SyncClientWrapper\nfrom .raw_client import RawClient\n\n\nclass Client:\n    def ping(self) -> None:\n        \"\"\"\n        Examples\n        --------\n        {example}\n        \"\"\"\n        return None\n"
            )
        };
        let raw =
            "from ..core.client_wrapper import SyncClientWrapper\n\n\nclass RawClient:\n    pass\n";
        let hoisted = "from ...core.pydantic_utilities import UniversalBaseModel\n\n\nclass Ping(UniversalBaseModel):\n    pass\n";
        let reference = vec![
            ("src/fern/client.py", client("client..ping()")),
            ("src/fern/raw_client.py", raw.to_string()),
            (
                "src/fern/__init__.py",
                "\n\nfrom .types import Ping\n".to_string(),
            ),
            ("src/fern/types/ping.py", hoisted.to_string()),
            (
                "src/fern/types/__init__.py",
                "from .ping import Ping\n".to_string(),
            ),
        ];
        let crozier = vec![
            (
                "src/fern/client.py",
                "class FernApi:\n    @property\n    def _(self):\n        pass\n".to_string(),
            ),
            (
                "src/fern/__init__.py",
                "from .client import FernApi\n".to_string(),
            ),
            (
                "src/fern/types/__init__.py",
                "from .ping import Ping\n".to_string(),
            ),
            ("src/fern/_/client.py", client("client._.ping()")),
            ("src/fern/_/raw_client.py", raw.to_string()),
            (
                "src/fern/_/__init__.py",
                "from .types import Ping\n".to_string(),
            ),
            ("src/fern/_/types/ping.py", hoisted.to_string()),
            (
                "src/fern/_/types/__init__.py",
                "from .ping import Ping\n".to_string(),
            ),
        ];
        (reference, crozier)
    }

    fn write_tree(files: &[(&str, String)]) -> tempfile::TempDir {
        let root = tempfile::tempdir().unwrap();
        for (rel, text) in files {
            let path = root.path().join(rel);
            std::fs::create_dir_all(path.parent().unwrap()).unwrap();
            std::fs::write(path, text).unwrap();
        }
        root
    }

    #[test]
    fn the_empty_namespace_rule_holds_only_where_crozier_moves_fern_s_files_unchanged() {
        let (reference, crozier) = empty_namespace_trees();
        let (fern_tree, crozier_tree) = (write_tree(&reference), write_tree(&crozier));
        let context = Context::from_trees(fern_tree.path(), crozier_tree.path());
        let found = context.empty_namespace();
        assert_eq!(
            found.crozier_only,
            BTreeSet::from(
                [
                    "src/fern/_/__init__.py",
                    "src/fern/_/client.py",
                    "src/fern/_/raw_client.py",
                    "src/fern/_/types/__init__.py",
                    "src/fern/_/types/ping.py"
                ]
                .map(String::from)
            )
        );
        assert_eq!(
            found.reference_only,
            BTreeSet::from(["src/fern/raw_client.py", "src/fern/types/ping.py"].map(String::from))
        );
        assert!(empty_namespace_package_file(
            &context,
            "src/fern/raw_client.py",
            Side::Reference
        ));
        assert!(!empty_namespace_package_file(
            &context,
            "src/fern/raw_client.py",
            Side::Crozier
        ));
        let (fern, ours) = (["class Client:", ""], ["class FernApi:", "", ""]);
        let root = Pair {
            rel: "src/fern/client.py",
            fern: &fern,
            crozier: &ours,
            context: &context,
        };
        assert_eq!(
            empty_namespace_package_root(&root).unwrap(),
            Some(Region {
                fern: 0..2,
                crozier: 0..3
            })
        );
        let elsewhere = Pair {
            rel: "src/fern/types/__init__.py",
            ..root
        };
        assert_eq!(empty_namespace_package_root(&elsewhere).unwrap(), None);

        // Each guard: a root client that is not the `_` client, a moved file that
        // is not Fern's copy, a `_/client.py` differing outside its examples, and
        // no trees at all find nothing.
        let unfound = |edit: &dyn Fn(&mut Tree, &mut Tree)| {
            let (mut reference, mut crozier) = empty_namespace_trees();
            edit(&mut reference, &mut crozier);
            let (fern_tree, crozier_tree) = (write_tree(&reference), write_tree(&crozier));
            let context = Context::from_trees(fern_tree.path(), crozier_tree.path());
            let found = context.empty_namespace();
            found.crozier_only.is_empty()
                && found.reference_only.is_empty()
                && found.replaced.is_empty()
        };
        assert!(unfound(&|reference, _| {
            reference[0].1 = reference[0].1.replace("from ..core.", "from .core.");
        }));
        assert!(unfound(&|_, crozier| crozier[4]
            .1
            .push_str("# kept\nx = 1\n")));
        assert!(unfound(
            &|_, crozier| crozier[3].1 = crozier[3].1.replace("return None", "return 1")
        ));
        assert!(Context::default().empty_namespace().replaced.is_empty());
    }

    #[test]
    fn examples_are_the_only_lines_without_examples_drops() {
        let text = "def f():\n    \"\"\"\n    Doc.\n\n    Examples\n    --------\n    client..f()\n    \"\"\"\n    return 1\n";
        assert_eq!(
            without_examples(text),
            [
                "def f():",
                "    \"\"\"",
                "    Doc.",
                "",
                "    \"\"\"",
                "    return 1"
            ]
        );
        // A line reading `Examples` without its underline is kept.
        assert_eq!(without_examples("Examples\nx"), ["Examples", "x"]);
    }

    // End-to-end rejection proof declined: `crozier compare` refuses only against a
    // Fern tree carrying the crafted defect, which Fern never writes, so each case
    // would cost a reference regeneration while handing the rule the same Pair these
    // cases build. Acceptance runs end to end in every golden comparison, pinned line
    // by line in tests/fixtures/departures-ledger.tsv.
    #[test]
    fn the_stream_heading_rule_holds_only_on_the_declared_iterator() {
        let client = "class FernApi:\n    def watch(\n        self, *, request_options: typing.Optional[RequestOptions] = None\n    ) -> typing.Iterator[Tick]:\n        pass\n    def at(self) -> typing.Iterator[dt.datetime]:\n        pass\n    def raw(self) -> typing.Iterator[bytes]:\n        pass\nclass AsyncFernApi:\n    async def watch(self) -> typing.AsyncIterator[Tick]:\n        pass\n";
        let context = Context::from_sources(
            [("src/fern/client.py", client)],
            [("src/fern/client.py", client)],
        );
        let lines: [&str; 0] = [];
        let pair = Pair {
            rel: "reference.md",
            fern: &lines,
            crozier: &lines,
            context: &context,
        };
        let heading = |method: &str, annotation: &str| {
            format!("<details><summary><code>client.<a href=\"src/fern/client.py\">{method}</a>(...) -> {annotation}</code></summary>")
        };
        let holds = |fern: &str, crozier: &str| stream_reference_return_type(&pair, fern, crozier);
        let fern = heading("watch", "typing.Iterator[bytes]");
        assert!(holds(&fern, &heading("watch", "typing.Iterator[Tick]")));
        // The datetime prose spelling of a `dt.` annotation is the same type.
        assert!(holds(
            &heading("at", "typing.Iterator[bytes]"),
            &heading("at", "typing.Iterator[datetime.datetime]")
        ));
        // Not the type the method declares, not an iterator, the method's own
        // `bytes`, an undefined method, another heading or another file: no.
        assert!(!holds(&fern, &heading("watch", "typing.Iterator[Other]")));
        assert!(!holds(&fern, &heading("watch", "Tick")));
        assert!(!holds(
            &heading("raw", "typing.Iterator[bytes]"),
            &heading("raw", "typing.Iterator[bytes]")
        ));
        assert!(!holds(
            &heading("missing", "typing.Iterator[bytes]"),
            &heading("missing", "typing.Iterator[Tick]")
        ));
        assert!(!holds(&fern, &heading("other", "typing.Iterator[Tick]")));
        assert!(!holds(
            &heading("watch", "Tick"),
            &heading("watch", "typing.Iterator[Tick]")
        ));
        // Both sides anchor the link at the method's lines (fern-python-sdk
        // 5.41.25): the anchor names lines of the module, not another module.
        let anchored = |method: &str, annotation: &str| {
            heading(method, annotation).replace("client.py\"", "client.py#L2-L5\"")
        };
        assert!(holds(
            &anchored("watch", "typing.Iterator[bytes]"),
            &anchored("watch", "typing.Iterator[Tick]")
        ));
        assert!(!holds(
            &anchored("watch", "typing.Iterator[bytes]"),
            &anchored("watch", "typing.Iterator[Other]")
        ));
        assert!(!holds(
            &anchored("watch", "typing.Iterator[bytes]"),
            &heading("watch", "typing.Iterator[Tick]")
        ));
        // Each side's range its own client's lines for the method, shifted by
        // the client's other departures: the return type is judged apart.
        let fern_client = format!(
            "class FernApi:\n    \"\"\"\n    extra\n    \"\"\"\n{}",
            &client["class FernApi:\n".len()..]
        );
        let shifted = Context::from_sources(
            [("src/fern/client.py", fern_client.as_str())],
            [("src/fern/client.py", client)],
        );
        let shifted = Pair {
            context: &shifted,
            ..pair
        };
        let ranged = |method: &str, annotation: &str, range: &str| {
            heading(method, annotation).replace("client.py\"", &format!("client.py#{range}\""))
        };
        assert!(stream_reference_return_type(
            &shifted,
            &ranged("watch", "typing.Iterator[bytes]", "L5-L8"),
            &ranged("watch", "typing.Iterator[Tick]", "L2-L5")
        ));
        // A range that is not the method's lines on either side is no departure.
        assert!(!stream_reference_return_type(
            &shifted,
            &ranged("watch", "typing.Iterator[bytes]", "L5-L8"),
            &ranged("watch", "typing.Iterator[Tick]", "L2-L6")
        ));
        assert!(!stream_reference_return_type(
            &shifted,
            &ranged("watch", "typing.Iterator[bytes]", "L4-L8"),
            &ranged("watch", "typing.Iterator[Tick]", "L2-L5")
        ));
        let readme = Pair {
            rel: "README.md",
            ..pair
        };
        assert!(!stream_reference_return_type(
            &readme,
            &fern,
            &heading("watch", "typing.Iterator[Tick]")
        ));
        // A flat tree holds the linked `src/<package>/` module at its root.
        let flat = Context::from_sources([("client.py", client)], [("client.py", client)]);
        let flat = Pair {
            context: &flat,
            ..pair
        };
        assert!(stream_reference_return_type(
            &flat,
            &fern,
            &heading("watch", "typing.Iterator[Tick]")
        ));
        assert!(!stream_reference_return_type(
            &flat,
            &fern,
            &heading("watch", "typing.Iterator[Other]")
        ));
        // A file compared on its own has no tree to read the method from.
        let alone = Context::default();
        let alone = Pair {
            context: &alone,
            ..pair
        };
        assert!(!stream_reference_return_type(
            &alone,
            &fern,
            &heading("watch", "typing.Iterator[Tick]")
        ));
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
    fn the_int64_rule_takes_only_a_rounding_that_leaves_the_range() {
        let fern_line = "            metres=9223372036854776000,";
        let crozier_line = "            metres=9223372036854775807,";
        let fern = [
            "        \"\"\"",
            "        Examples",
            "        --------",
            "        client.record_reading(",
            fern_line,
            "        )",
            "        \"\"\"",
        ];
        let crozier = fern.map(|line| {
            if line == fern_line {
                crozier_line
            } else {
                line
            }
        });
        let source: crate::openapi::OpenApi = serde_json::from_value(serde_json::json!({
            "openapi": "3.0.3",
            "paths": {"/readings": {"post": {
                "parameters": [{"name": "low", "in": "query", "schema": {
                    "type": "integer", "format": "int64", "example": i64::MIN
                }}],
                "requestBody": {"content": {"application/json": {"schema": {
                    "type": "object",
                    "properties": {
                        "metres": {"type": "integer", "format": "int64", "example": i64::MAX},
                        "trip": {"type": "integer", "format": "int64", "example": 9_007_199_254_740_993_i64},
                        "plain": {"type": "integer", "example": 9_223_372_036_854_000_000_i64},
                        "label": {"type": "string", "format": "int64", "example": 9_223_372_036_854_775_805_i64}
                    }
                }}}},
                "responses": {}
            }}}
        }))
        .expect("a source document");
        let context = Context::default().with_source_document(source);
        let holds =
            |rel: &str, fern_text: &[&str], crozier_text: &[&str], left: &str, right: &str| {
                let pair = Pair {
                    rel,
                    fern: fern_text,
                    crozier: crozier_text,
                    context: &context,
                };
                int64_example_rounded_out_of_range(&pair, left, right)
            };
        assert!(holds(
            "src/fern/client.py",
            &fern,
            &crozier,
            fern_line,
            crozier_line
        ));
        // Without the source document's declared example the rule abstains.
        assert!(!int64_example_rounded_out_of_range(
            &pair("src/fern/client.py", &fern, &crozier),
            fern_line,
            crozier_line
        ));
        // A value the document does not declare is no correction, even one that
        // rounds to Fern's spelling.
        let undeclared = "            metres=9223372036854775806,";
        let undeclared_text = fern.map(|line| if line == fern_line { undeclared } else { line });
        assert!(!holds(
            "src/fern/client.py",
            &fern,
            &undeclared_text,
            fern_line,
            undeclared
        ));
        // `format: int64` alone, on a schema that is no integer, declares no
        // int64 example.
        let untyped = "            label=9223372036854775805,";
        let untyped_fern = "            label=9223372036854776000,";
        let untyped_fern_text = fern.map(|line| {
            if line == fern_line {
                untyped_fern
            } else {
                line
            }
        });
        let untyped_text = fern.map(|line| if line == fern_line { untyped } else { line });
        assert!(!holds(
            "src/fern/client.py",
            &untyped_fern_text,
            &untyped_text,
            untyped_fern,
            untyped
        ));
        // An in-range rounding is Fern's valid value, kept as Fern writes it.
        let near = (
            "            trip=9007199254740992,",
            "            trip=9007199254740993,",
        );
        let near_fern = fern.map(|line| if line == fern_line { near.0 } else { line });
        let near_crozier = fern.map(|line| if line == fern_line { near.1 } else { line });
        assert!(!holds(
            "src/fern/client.py",
            &near_fern,
            &near_crozier,
            near.0,
            near.1
        ));
        // The minimum rounds to -2^63, whose spelling also leaves the range.
        let low = (
            "            metres=-9223372036854776000,",
            "            metres=-9223372036854775808,",
        );
        let low_fern = fern.map(|line| if line == fern_line { low.0 } else { line });
        let low_crozier = fern.map(|line| if line == fern_line { low.1 } else { line });
        assert!(holds(
            "src/fern/client.py",
            &low_fern,
            &low_crozier,
            low.0,
            low.1
        ));
        for (left, right) in [
            ("            metres=9223372036854776001,", crozier_line),
            (fern_line, "            metres=9223372036854000000,"),
            (fern_line, "            other=9223372036854775807,"),
            (
                "            metres=\"9223372036854776000\",",
                "            metres=\"9223372036854775807\",",
            ),
            (fern_line, fern_line),
        ] {
            let left_text = fern.map(|line| if line == fern_line { left } else { line });
            let right_text = fern.map(|line| if line == fern_line { right } else { line });
            assert!(
                !holds("src/fern/client.py", &left_text, &right_text, left, right),
                "{left} {right}"
            );
        }
        assert!(!holds(
            "src/fern/raw_client.py",
            &fern,
            &crozier,
            fern_line,
            crozier_line
        ));
        // Outside an example the same value is no documented call.
        let bare_fern = [fern_line];
        let bare_crozier = [crozier_line];
        assert!(!holds(
            "src/fern/client.py",
            &bare_fern,
            &bare_crozier,
            fern_line,
            crozier_line
        ));
        let readme_fern = ["```python", "    metres=9223372036854776000,", "```"];
        let readme_crozier = ["```python", "    metres=9223372036854775807,", "```"];
        assert!(holds(
            "README.md",
            &readme_fern,
            &readme_crozier,
            readme_fern[1],
            readme_crozier[1]
        ));
    }

    #[test]
    fn the_int64_rule_reads_list_elements_and_declines_other_differences() {
        let source: crate::openapi::OpenApi = serde_json::from_value(serde_json::json!({
            "openapi": "3.0.3",
            "paths": {},
            "components": {"schemas": {"Reading": {
                "type": "object",
                "properties": {"checkpoints": {"type": "array", "items": {
                    "type": "integer", "format": "int64", "example": i64::MAX
                }}}
            }}}
        }))
        .expect("a source document");
        let context = Context::default().with_source_document(source);
        let holds = |left: &str, right: &str| {
            let fern = ["```python", left, "```"];
            let crozier = ["```python", right, "```"];
            let pair = Pair {
                rel: "README.md",
                fern: &fern,
                crozier: &crozier,
                context: &context,
            };
            int64_example_rounded_out_of_range(&pair, left, right)
        };
        // A list element, inline or on a line of its own, is the same value.
        for (left, right) in [
            (
                "    checkpoints=[9223372036854776000],",
                "    checkpoints=[9223372036854775807],",
            ),
            ("        9223372036854776000", "        9223372036854775807"),
            (
                "    ids=[1, 9223372036854776000],",
                "    ids=[1, 9223372036854775807],",
            ),
        ] {
            assert!(holds(left, right), "{left}");
        }
        // Digits inside a word or before other text are no value.
        for (left, right) in [
            (
                "    name=v9223372036854776000,",
                "    name=v9223372036854775807,",
            ),
            (
                "    metres=9223372036854776000x,",
                "    metres=9223372036854775807x,",
            ),
        ] {
            assert!(!holds(left, right), "{left}");
        }
        // Lines differing inside a multi-byte character decline, never panic.
        assert_eq!(
            differing_integer("            name=\"é\",", "            name=\"ê\","),
            None
        );
        assert_eq!(
            differing_integer("x=12é", "x=13é"),
            Some(("x=", "12", "13"))
        );
    }

    #[test]
    fn the_dollar_rule_takes_only_an_escaped_docstring_literal() {
        let fern_line = "            variable=\"\\\\$PS1\",";
        let crozier_line = "            variable=\"$PS1\",";
        let fern = [
            "        \"\"\"",
            "        Examples",
            "        --------",
            "        client.define_prompt(",
            fern_line,
            "        )",
            "        \"\"\"",
        ];
        let crozier = fern.map(|line| {
            if line == fern_line {
                crozier_line
            } else {
                line
            }
        });
        let source: crate::openapi::OpenApi = serde_json::from_value(serde_json::json!({
            "openapi": "3.0.3",
            "paths": {},
            "components": {"schemas": {"PromptSpec": {
                "type": "object",
                "properties": {
                    "variable": {"type": "string", "const": "$PS1"},
                    "label": {"type": "string", "example": "$5"}
                }
            }}}
        }))
        .expect("a source document");
        let context = Context::default().with_source_document(source);
        let holds =
            |rel: &str, fern_text: &[&str], crozier_text: &[&str], left: &str, right: &str| {
                let pair = Pair {
                    rel,
                    fern: fern_text,
                    crozier: crozier_text,
                    context: &context,
                };
                docstring_literal_dollar_escape(&pair, left, right)
            };
        assert!(holds(
            "src/fern/client.py",
            &fern,
            &crozier,
            fern_line,
            crozier_line
        ));
        // Without the source document's const the rule abstains, and a string
        // the document declares no const for takes no correction.
        assert!(!docstring_literal_dollar_escape(
            &pair("src/fern/client.py", &fern, &crozier),
            fern_line,
            crozier_line
        ));
        let label = ("            label=\"\\\\$5\",", "            label=\"$5\",");
        let label_fern = fern.map(|line| if line == fern_line { label.0 } else { line });
        let label_crozier = fern.map(|line| if line == fern_line { label.1 } else { line });
        assert!(!holds(
            "src/fern/client.py",
            &label_fern,
            &label_crozier,
            label.0,
            label.1
        ));
        for (left, right) in [
            ("            variable=\"\\\\$PS2\",", crozier_line),
            ("            variable=\"\\$PS1\",", crozier_line),
            ("            other=\"\\\\$PS1\",", crozier_line),
            (
                "            variable=\"PS1\",",
                "            variable=\"PS1\",",
            ),
            (
                "            variable=\\\\$PS1,",
                "            variable=$PS1,",
            ),
        ] {
            let left_text = fern.map(|line| if line == fern_line { left } else { line });
            let right_text = fern.map(|line| if line == fern_line { right } else { line });
            assert!(
                !holds("src/fern/client.py", &left_text, &right_text, left, right),
                "{left} {right}"
            );
        }
        let readme_fern = ["```python", "    variable=\"\\\\$PS1\",", "```"];
        let readme_crozier = ["```python", "    variable=\"$PS1\",", "```"];
        assert!(!holds(
            "README.md",
            &readme_fern,
            &readme_crozier,
            readme_fern[1],
            readme_crozier[1]
        ));
        let bare_fern = [fern_line];
        let bare_crozier = [crozier_line];
        assert!(!holds(
            "src/fern/client.py",
            &bare_fern,
            &bare_crozier,
            fern_line,
            crozier_line
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

    /// `source` is a method's raw client body beside a model; each case drops one
    /// thing the correction needs and must leave the block unexplained.
    // llmlint: ignore[changed_behavior_has_e2e] A rejection needs a reference tree Fern never writes, so these cases feed the rule the crafted mismatch directly; the acceptance path is proved end to end by the corpus row 5625 comparison.
    #[test]
    fn alias_reference_correction_reads_converted_reserved_and_path_shared_fields() {
        let model = "class Rule(UniversalBaseModel):\n    uuid_: str\n    tags: str\n    topic_id: typing.Optional[str] = None\n";
        let raw = |wire: &str| {
            format!(
                "    def put(self, topic_id: typing.Optional[str], *, uuid_: str, tags: str):\n        json={{\n                \"uuid\": uuid_,\n                \"{wire}\": convert_and_respect_annotation_metadata(\n                    object_=tags, annotation=str, direction=\"write\"\n                ),\n                \"topicId\": topic_id,\n        }},\n"
            )
        };
        let block = |name: &str, ty: &str, doc: &str| {
            format!("<dl>\n<dd>\n\n**{name}:** `{ty}`{doc}\n    \n</dd>\n</dl>\n\n")
        };
        let head = "<details><summary><code>client.<a href=\"src/fern/rules/client.py\">put</a>(...)</code></summary>\n";
        let path = block("topic_id", "str", " — Topic.");
        let fern = format!("{head}{path}{}", block("request", "Rule", " "));
        let crozier = format!(
            "{head}{path}{}{}",
            block("uuid", "str", " "),
            block("tags", "str", " ")
        );
        let holds = |raw_client: &str| {
            let sources = [
                ("src/fern/rules/raw_client.py", raw_client),
                ("src/fern/types/rule.py", model),
            ];
            let context = Context::from_sources([], sources);
            let (fern, crozier): (Vec<&str>, Vec<&str>) =
                (fern.lines().collect(), crozier.lines().collect());
            alias_reference_parameters(&Pair {
                rel: "reference.md",
                fern: &fern,
                crozier: &crozier,
                context: &context,
            })
            .unwrap()
            .is_some()
        };
        assert!(holds(&raw("tags")));
        // Without the wire entry the converter names, nothing is spread.
        assert!(!holds(
            &raw("tags").replace("object_=tags", "object_=other")
        ));
    }

    // llmlint: ignore[changed_behavior_has_e2e] A rejection needs a reference tree Fern never writes, so these cases feed the rule the crafted mismatch directly; the acceptance path is proved end to end by the corpus row 5625 comparison.
    #[test]
    fn alias_reference_correction_drops_a_fieldless_models_request_block() {
        let raw =
            "    def stop(self, policy_id: str, *, request_options=None):\n        json={},\n";
        let block = |name: &str, ty: &str, doc: &str| {
            format!("<dl>\n<dd>\n\n**{name}:** `{ty}`{doc}\n    \n</dd>\n</dl>\n\n")
        };
        let head = "<details><summary><code>client.<a href=\"src/fern/record/client.py\">stop</a>(...)</code></summary>\n";
        let path = block("policy_id", "str", " — Policy.");
        let options = block(
            "request_options",
            "typing.Optional[RequestOptions]",
            " — Options.",
        );
        let fern = format!("{head}{path}{}{options}", block("request", "Empty", " "));
        let crozier = format!("{head}{path}{options}");
        let model = "class Empty(UniversalBaseModel):\n    pass\n";
        let holds = |raw_client: &str, model: &str, crozier: &str| {
            let sources = [
                ("src/fern/record/raw_client.py", raw_client),
                ("src/fern/types/empty.py", model),
            ];
            let context = Context::from_sources([], sources);
            let (fern, crozier): (Vec<&str>, Vec<&str>) =
                (fern.lines().collect(), crozier.lines().collect());
            alias_reference_parameters(&Pair {
                rel: "reference.md",
                fern: &fern,
                crozier: &crozier,
                context: &context,
            })
            .unwrap()
        };
        let region = holds(raw, model, &crozier).expect("the block is recognised");
        assert_eq!(region.crozier.start, region.crozier.end);
        assert_eq!(region.fern.len(), 8);
        // The method must really send nothing.
        assert!(holds(&raw.replace("json={},", "json=body,"), model, &crozier).is_none());
        // A model holding a field, or only a base's, is a different shape.
        let with_field = "class Empty(UniversalBaseModel):\n    id: str\n";
        assert!(holds(raw, with_field, &crozier).is_none());
        assert!(holds(raw, "class Empty(Base):\n    pass\n", &crozier).is_none());
        // The next block must follow unchanged.
        let changed = crozier.replace("— Options.", "— Altered.");
        assert!(holds(raw, model, &changed).is_none());
    }

    #[test]
    fn alias_reference_correction_requires_the_actual_alias_signature_json_and_descriptions() {
        let root = std::path::Path::new(env!("CARGO_MANIFEST_DIR"))
            .join("docs/fern-measurements/superseded-fixtures/request-alias/fern-expected");
        let fern = std::fs::read_to_string(root.join("reference.md")).unwrap();
        let before = "<dl>\n<dd>\n\n**request:** `TitleAlias` \n    \n</dd>\n</dl>";
        let after = "<dl>\n<dd>\n\n**ticket:** `int` \n    \n</dd>\n</dl>\n\n<dl>\n<dd>\n\n**caption:** `typing.Optional[str]` — Shown on cabinet labels.\n    \n</dd>\n</dl>";
        assert!(fern.contains(before));
        let corrected = fern.replace(before, after);
        let sources = python_sources(&root);
        let context = Context::from_sources(
            [],
            sources
                .iter()
                .map(|(path, text)| (path.as_str(), text.as_str())),
        );
        let rule: RegionRule = alias_reference_parameters;
        assert!(region_of(rule, "reference.md", &fern, &corrected, &context).is_some());
        for wrong in [
            corrected.replace("**ticket:** `int`", "**ticket:** `str`"),
            corrected.replace("Shown on cabinet labels.", "Wrong description."),
            corrected.replace("**caption:**", "**unknown:**"),
            corrected.replace("**ticket:** `int`", "**request:** `int`"),
        ] {
            assert!(
                region_of(rule, "reference.md", &fern, &wrong, &context).is_none(),
                "{wrong}"
            );
        }
        for wrong in [
            corrected.replace("#### 🔌 Usage", "Unexplained heading"),
            corrected.replace("**request_options:**", "**extra:**"),
        ] {
            let comparison =
                crate::parity::compare_file(&context, "reference.md", &wrong, &fern).unwrap();
            assert!(
                !comparison.matches(),
                "an adjacent unexplained edit must remain: {wrong}"
            );
        }
        for (from, to) in [
            ("json={", "data={"),
            ("ticket: int", "ticket: str"),
            ("TitleAlias = Title", "TitleAlias = str"),
            ("\"caption\": caption,", "\"caption\": missing,"),
        ] {
            let changed: Vec<_> = sources
                .iter()
                .map(|(path, text)| (path.clone(), text.replace(from, to)))
                .collect();
            let context = Context::from_sources(
                [],
                changed
                    .iter()
                    .map(|(path, text)| (path.as_str(), text.as_str())),
            );
            assert!(
                region_of(rule, "reference.md", &fern, &corrected, &context).is_none(),
                "{from}"
            );
        }
        assert!(region_of(rule, "client.py", &fern, &corrected, &context).is_none());
        assert!(region_of(rule, "reference.md", &fern, &corrected, &Context::default()).is_none());
        assert!(
            reference_parameter_block(&["<dl>", "<dd>", "", "**request:** `TitleAlias` "], 0)
                .is_none()
        );
        assert!(generated_method_parameters("unrelated text").is_empty());
    }

    #[test]
    fn binary_json_examples_require_the_actual_bytes_json_signature_and_exact_doc_changes() {
        let raw = "    def ship(self, *, request: bytes, request_options=None):\n        json=request,\n        \"content-type\": \"application/json\",\n";
        let context = Context::from_sources([], [("src/acme/vault/raw_client.py", raw)]);
        let fern = "    def ship(self, *, request: bytes, request_options=None):\n        \"\"\"\n        Examples\n        --------\n        client.vault.ship(request=\"string\")\n        \"\"\"\n";
        let corrected = fern.replace("request=\"string\"", "request=b\"string\"");
        let rule: RegionRule = binary_json_body_example;
        assert!(region_of(rule, "src/acme/vault/client.py", fern, &corrected, &context).is_some());
        let reference = "<details><summary><code>client.vault.<a href=\"src/acme/vault/client.py\">ship</a>(...)</code></summary>\nclient.vault.ship(\n    request=\"string\",\n)\n**request:** `bytes` \n</details>\n";
        let correct_reference = reference.replace("request=\"string\"", "request=b\"string\"");
        assert!(region_of(
            rule,
            "reference.md",
            reference,
            &correct_reference,
            &context
        )
        .is_some());
        let readme = "client.vault.ship(\n    request=\"string\",\n)\n";
        let correct_readme = readme.replace("request=\"string\"", "request=b\"string\"");
        assert!(region_of(rule, "README.md", readme, &correct_readme, &context).is_some());
        for wrong in [
            corrected.replace("b\"string\"", "b\"other\""),
            corrected.replace("client.vault.ship", "client.other.ship"),
            corrected.replace("Examples", "Parameters"),
            corrected.replace("request=b\"string\"", "extra=b\"string\""),
            corrected.replace("request=b\"string\"", "request=Model(request=b\"string\")"),
        ] {
            // Client receiver group is left exact even when the leaf method matches.
            assert!(
                region_of(rule, "src/acme/vault/client.py", fern, &wrong, &context).is_none(),
                "{wrong}"
            );
        }
        for source in [
            raw.replace("request: bytes", "request: str"),
            raw.replace("request: bytes", "otherrequest: bytes"),
            raw.replace("json=request", "data=request"),
            raw.replace("application/json", "text/plain"),
            raw.replace("request: bytes", "request: str")
                .replace("json=request", "request : bytes\n        json=request"),
        ] {
            let context =
                Context::from_sources([], [("src/acme/vault/raw_client.py", source.as_str())]);
            assert!(
                region_of(rule, "src/acme/vault/client.py", fern, &corrected, &context).is_none()
            );
        }
        assert!(region_of(
            rule,
            "reference.md",
            reference,
            &correct_reference.replace("`bytes`", "`int`"),
            &context
        )
        .is_none());
        assert!(region_of(
            rule,
            "README.md",
            readme,
            &correct_readme.replace("vault.ship", "other.ship"),
            &context
        )
        .is_none());
        assert!(region_of(
            rule,
            "src/acme/vault/raw_client.py",
            fern,
            &corrected,
            &context
        )
        .is_none());
        assert!(region_of(
            rule,
            "README.md",
            readme,
            &correct_readme,
            &Context::default()
        )
        .is_none());
    }

    #[test]
    fn multipart_required_file_examples_allow_only_the_proven_missing_argument() {
        for (field, annotation, declaration) in [
            (
                "plan",
                "PlanAlias",
                "class Plan(Model):\n    pass\nPlanAlias = Plan\n",
            ),
            ("json", "Plan", "class Plan(Model):\n    pass\n"),
        ] {
            let raw = format!("    def upload(\n        self,\n    ):\n        data={{\n            \"{field}\": json.dumps(jsonable_encoder({field})),\n        }}\n        files={{\n            \"attachment\": attachment,\n        }}\n");
            let context = Context::from_sources(
                [],
                [
                    ("src/acme/raw_client.py", raw.as_str()),
                    ("src/acme/types/plan.py", declaration),
                ],
            );
            let fern = format!("    def upload(\n        self,\n        *,\n        {field}: {annotation},\n        attachment: core.File,\n    ) -> None:\n        \"\"\"\n        Examples\n        --------\n        client.upload(\n            {field}=Plan(bearing=1),\n        )\n        \"\"\"\n");
            let corrected = fern.replace(
                "        )\n",
                "            attachment=\"example_attachment\",\n        )\n",
            );
            let rule: RegionRule = multipart_object_required_file_example;
            assert!(region_of(rule, "src/acme/client.py", &fern, &corrected, &context).is_some());
            for changed in [
                corrected.replace("example_attachment", "other_file"),
                corrected.replace("bearing=1", "bearing=2"),
                corrected.replace("bearing=1", "bearing=1, attachment=\"example_attachment\""),
                corrected.replace("client.upload", "client.other"),
                corrected.replace("attachment: core.File", "attachment: core.File = None"),
                corrected.replace("        Examples", "        Parameters"),
                corrected.replace("        )\n", "            unknown=1,\n        )\n"),
            ] {
                assert!(
                    region_of(rule, "src/acme/client.py", &fern, &changed, &context).is_none(),
                    "{changed}"
                );
            }
            assert!(
                region_of(rule, "src/acme/raw_client.py", &fern, &corrected, &context).is_none()
            );
            assert!(region_of(
                rule,
                "src/acme/client.py",
                &fern,
                &corrected,
                &Context::default()
            )
            .is_none());
            // A plain multipart body, with no JSON-encoded part, takes the same
            // correction; a file the raw client never sends takes none.
            let not_encoded = raw.replace("json.dumps(jsonable_encoder", "convert");
            let unsent = raw.replace("            \"attachment\": attachment,\n", "");
            for (raw, accepted) in [(not_encoded, true), (unsent, false)] {
                let context = Context::from_sources(
                    [],
                    [
                        ("src/acme/raw_client.py", raw.as_str()),
                        ("src/acme/types/plan.py", declaration),
                    ],
                );
                assert_eq!(
                    region_of(rule, "src/acme/client.py", &fern, &corrected, &context).is_some(),
                    accepted,
                    "{raw}"
                );
            }
        }
        assert!(example_call_arguments(
            "client.upload(value=[\"a,b\", {\"x\": (1, 2)}], attachment=\"example_attachment\")"
        )
        .is_some());
        for invalid in ["no_call", "call(", "call(\"unterminated)", "call(x))"] {
            assert!(example_call_arguments(invalid).is_none(), "{invalid}");
        }
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

    const CONSTANT_FERN: &str = "client.beds.list_beds(\n    section=\"section\",\n)\n\n<dl>\n<dd>\n\n**mist_mode:** `typing.Literal` — How fine.\n    \n</dd>\n</dl>\n\n<dl>\n<dd>\n\n**section:** `str` \n";
    const CONSTANT_CROZIER: &str = "client.beds.list_beds(\n    section=\"section\",\n)\n\n<dl>\n<dd>\n\n**section:** `str` \n";

    #[test]
    fn the_constant_header_docs_rule_takes_only_the_constants_reference_blocks() {
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
        // One more difference leaves the block alone explained: the region is the
        // block, and the other difference and a worked call still passing the
        // constant (Fern 5.41.3 leaves it out, as crozier does) stay unexplained.
        for (fern, crozier) in [
            (format!("{CONSTANT_FERN}x"), format!("{CONSTANT_CROZIER}y")),
            (
                CONSTANT_FERN.replace(
                    "    section=\"section\",\n",
                    "    section=\"section\",\n    mist_mode=\"fine\",\n",
                ),
                CONSTANT_CROZIER.to_string(),
            ),
        ] {
            let region = region_of(rule, "reference.md", &fern, &crozier, &context).unwrap();
            assert_eq!(region.fern.len(), 8, "{fern}");
            assert!(region.crozier.is_empty(), "{fern}");
            let compared =
                crate::parity::compare_file(&context, "reference.md", &crozier, &fern).unwrap();
            assert!(compared.residual.is_some(), "{fern}");
        }
        for (fern, crozier) in [
            // A block typed otherwise, and a header crozier does not send as a
            // constant.
            (
                CONSTANT_FERN.replace("`typing.Literal`", "`str`"),
                CONSTANT_CROZIER.to_string(),
            ),
            (
                CONSTANT_FERN.replace("**mist_mode:**", "**fan_speed:**"),
                CONSTANT_CROZIER.to_string(),
            ),
        ] {
            assert_eq!(
                region_of(rule, "reference.md", &fern, &crozier, &context),
                None,
                "{fern}"
            );
        }
        // Only reference.md, only with a constant header, only where they differ.
        for rel in ["README.md", "src/acme/beds/client.py"] {
            assert_eq!(
                region_of(rule, rel, CONSTANT_FERN, CONSTANT_CROZIER, &context),
                None,
                "{rel}"
            );
        }
        assert_eq!(
            region_of(
                rule,
                "reference.md",
                CONSTANT_FERN,
                CONSTANT_CROZIER,
                &Context::default()
            ),
            None
        );
        assert_eq!(
            region_of(rule, "reference.md", CONSTANT_FERN, CONSTANT_FERN, &context),
            None
        );
    }

    #[test]
    fn a_constant_header_block_composes_with_a_line_departure_in_the_same_file() {
        let context = Context::from_sources(
            [],
            [(
                "raw_client.py",
                "headers={\n    \"X-Mist-Mode\": \"fine\",\n},\n",
            )],
        );
        // A `closed-empty-object-example` docstring line sits above the block.
        let fern = format!("    plot={{\"key\": \"value\"}},\n{CONSTANT_FERN}");
        let crozier = format!("    plot={{}},\n{CONSTANT_CROZIER}");
        let compared =
            crate::parity::compare_file(&context, "reference.md", &crozier, &fern).unwrap();
        assert!(compared.residual.is_none());
        let ids: Vec<_> = compared.departures.iter().map(|found| found.id).collect();
        assert!(ids.contains(&"constant-header-docs-arguments"), "{ids:?}");
        assert!(ids.contains(&"closed-empty-object-example"), "{ids:?}");
    }

    #[test]
    fn the_nullable_items_line_rule_takes_only_the_restored_type() {
        let context = Context::default();
        let rel = "reference.md";
        let holds = |fern: &str, crozier: &str| {
            let (left, right) = ([fern], [crozier]);
            nullable_items_docs_line(
                &Pair {
                    rel,
                    fern: &left,
                    crozier: &right,
                    context: &context,
                },
                fern,
                crozier,
            )
        };
        let plain = "**rows:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` — Rows.";
        let restored = "**rows:** `typing.Optional[typing.Union[typing.Optional[int], typing.Sequence[typing.Optional[int]]]]` — Rows.";
        assert!(holds(restored, plain));
        // Another description, another item type, and the same line on both sides.
        assert!(!holds(&restored.replace("Rows", "Pots"), plain));
        assert!(!holds(&restored.replace("int", "str"), plain));
        assert!(!holds(plain, plain));
        // Only `reference.md` documents the type.
        let (left, right) = ([restored], [plain]);
        assert!(!nullable_items_docs_line(
            &Pair {
                rel: "src/acme/client.py",
                fern: &left,
                crozier: &right,
                context: &context,
            },
            restored,
            plain,
        ));
    }

    #[test]
    fn a_closed_empty_placeholder_composes_with_a_line_count_shift_above_it() {
        // A departure above shifted crozier's lines, so the regions no longer
        // start together: the one placeholder is still taken, and a neighbour
        // of another call is not.
        let fern = "a\nb\nc\nfirst(\n    plot={\n        \"key\": \"value\"\n    },\n)";
        let crozier = "z\nc\nfirst(\n    plot={},\n)";
        let (fern, crozier): (Vec<&str>, Vec<&str>) =
            (fern.split('\n').collect(), crozier.split('\n').collect());
        let context = Context::default();
        let pair = Pair {
            rel: "reference.md",
            fern: &fern,
            crozier: &crozier,
            context: &context,
        };
        assert_eq!(
            closed_empty_object_example_region(&pair).unwrap(),
            Some(Region {
                fern: 4..7,
                crozier: 3..4,
            })
        );
        let other = ["z", "c", "second(", "    plot={},", ")"];
        let pair = Pair {
            crozier: &other,
            ..pair
        };
        assert_eq!(closed_empty_object_example_region(&pair).unwrap(), None);
    }

    #[test]
    fn the_binary_json_line_rule_needs_a_binary_body_method_and_the_exact_values() {
        let holds = |context: &Context, fern: &str, crozier: &str| {
            let (left, right) = ([fern], [crozier]);
            binary_json_body_example_line(
                &Pair {
                    rel: "reference.md",
                    fern: &left,
                    crozier: &right,
                    context,
                },
                fern,
                crozier,
            )
        };
        let fern = "    request=\"string\",";
        let crozier = "    request=b\"string\",";
        // Without a generated binary JSON body method, nothing is excused.
        assert!(!holds(&Context::default(), fern, crozier));
        let raw = "class RawThingsClient:\n    def upload(\n        self,\n        *,\n        request: bytes,\n    ) -> None:\n        self._client_wrapper.httpx_client.request(\n            json=request,\n            headers={\n                \"content-type\": \"application/json\",\n            },\n        )\n";
        let context = Context::from_sources([], [("things/raw_client.py", raw)]);
        assert!(!context.request_examples().binary_json_methods.is_empty());
        assert!(holds(&context, fern, crozier));
        assert!(!holds(&context, "    request=\"other\",", crozier));
        assert!(!holds(&context, fern, "    request=b\"other\","));
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
        // Anything else differing inside the region leaves only the placeholder
        // with both neighbours intact, and a placeholder crozier keeps is not
        // this departure.
        let mut other = crozier;
        other[3] = ");";
        assert_eq!(
            closed_empty_object_example_region(&pair("README.md", &fern, &other)),
            Ok(Some(Region {
                fern: 7..10,
                crozier: 5..6
            }))
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
    fn the_repeated_keyword_rule_takes_only_a_constructor_call_repeat() {
        let fern = [
            "client = FernApi(",
            "    api_key=\"<value>\",",
            "    api_key=\"<X-Api-Key>\",",
            ")",
            "client.relay(",
            "    to=\"to\",",
            ")",
        ];
        let crozier = [
            "client = FernApi(",
            "    api_key=\"<value>\",",
            ")",
            "client.relay(",
            "    to=\"to\",",
            ")",
        ];
        let found =
            repeated_credential_example_keyword(&pair("README.md", &fern, &crozier)).unwrap();
        assert_eq!(
            found,
            Some(Region {
                fern: 2..3,
                crozier: 2..2
            })
        );
        // Any `client.py` reads the same; another file does not.
        assert!(
            repeated_credential_example_keyword(&pair("src/fern/client.py", &fern, &crozier))
                .unwrap()
                .is_some()
        );
        assert!(repeated_credential_example_keyword(&pair(
            "src/fern/raw_client.py",
            &fern,
            &crozier
        ))
        .unwrap()
        .is_none());
        // crozier keeping the repeat, or dropping the first keyword instead, is
        // not the departure.
        assert!(
            repeated_credential_example_keyword(&pair("README.md", &fern, &fern))
                .unwrap()
                .is_none()
        );
        let wrong = [
            "client = FernApi(",
            "    api_key=\"<X-Api-Key>\",",
            ")",
            "client.relay(",
            "    to=\"to\",",
            ")",
        ];
        assert!(
            repeated_credential_example_keyword(&pair("README.md", &fern, &wrong))
                .unwrap()
                .is_none()
        );
        // A repeated keyword in a method call is no constructor call.
        let method = ["client.relay(", "    to=\"a\",", "    to=\"b\",", ")"];
        let once = ["client.relay(", "    to=\"a\",", ")"];
        assert!(
            repeated_credential_example_keyword(&pair("README.md", &method, &once))
                .unwrap()
                .is_none()
        );
    }

    /// A document whose `POST /questions` takes a query parameter `location`
    /// beside a `$ref` body `Question` declaring `bench`; `reused` adds a
    /// response listing `Question` again.
    fn reused_body_source(location: &str, reused: bool) -> serde_json::Value {
        let mut paths = serde_json::json!({
            "/questions": {"post": {
                "parameters": [{"name": "bench", "in": location, "required": true,
                                "schema": {"type": "string"}}],
                "requestBody": {"content": {"application/json": {
                    "schema": {"$ref": "#/components/schemas/Question"}}}},
                "responses": {"200": {"description": "ok"}}
            }}
        });
        if reused {
            paths["/questions"]["get"] = serde_json::json!({"responses": {"200": {
                "description": "ok",
                "content": {"application/json": {"schema": {
                    "type": "array", "items": {"$ref": "#/components/schemas/Question"}}}}
            }}});
        }
        serde_json::json!({
            "openapi": "3.0.3",
            "info": {"title": "t", "version": "1"},
            "paths": paths,
            "components": {"schemas": {"Question": {"type": "object", "properties": {
                "bench": {"type": "string"}, "asked_by": {"type": "string"}}}}}
        })
    }

    #[test]
    fn the_query_body_keyword_rule_takes_only_a_reused_body_s_renamed_keyword() {
        let fern = [
            "client.questions.file_question(",
            "    bench=\"bench\",",
            "    bench=\"bench\",",
            "    asked_by=\"asked_by\",",
            ")",
        ];
        let crozier = [
            "client.questions.file_question(",
            "    bench=\"bench\",",
            "    question_bench=\"bench\",",
            "    asked_by=\"asked_by\",",
            ")",
        ];
        let holds = |rel: &str, source: &Context, fern: &[&str], crozier: &[&str]| {
            repeated_query_body_example_keyword(&Pair {
                rel,
                fern,
                crozier,
                context: source,
            })
            .unwrap()
        };
        let reused = source_context(reused_body_source("query", true), &[]);
        assert_eq!(
            holds("reference.md", &reused, &fern, &crozier),
            Some(Region {
                fern: 2..3,
                crozier: 2..3
            })
        );
        assert!(holds("README.md", &reused, &fern, &crozier).is_some());
        // The async twin's indented `await` call reads the same.
        let indent = |lines: &[&str]| -> Vec<String> {
            lines
                .iter()
                .map(|line| format!("    {}", line.replacen("client.", "await client.", 1)))
                .collect()
        };
        let (fern_async, crozier_async) = (indent(&fern), indent(&crozier));
        let fern_async: Vec<&str> = fern_async.iter().map(String::as_str).collect();
        let crozier_async: Vec<&str> = crozier_async.iter().map(String::as_str).collect();
        assert!(holds("README.md", &reused, &fern_async, &crozier_async).is_some());
        // Not in a client's docstring, where Fern already writes the rename.
        assert!(holds("src/fern/questions/client.py", &reused, &fern, &crozier).is_none());
        // Not without the source document, nor when the body is referenced
        // only once (Fern inlines it and writes the rename itself), nor for a
        // path parameter's clash (Fern renames the path argument instead).
        assert!(holds("reference.md", &Context::default(), &fern, &crozier).is_none());
        let once = source_context(reused_body_source("query", false), &[]);
        assert!(holds("reference.md", &once, &fern, &crozier).is_none());
        let path = source_context(reused_body_source("path", true), &[]);
        assert!(holds("reference.md", &path, &fern, &crozier).is_none());
        // A rename the signature does not declare, a changed value, or crozier
        // keeping the repeat, is not the departure.
        for wrong in [
            "    body_bench=\"bench\",",
            "    question_bench=\"other\",",
            "    bench=\"bench\",",
        ] {
            let mut lines = crozier;
            lines[2] = wrong;
            assert!(
                holds("reference.md", &reused, &fern, &lines).is_none(),
                "{wrong}"
            );
        }
        // Another line differing beside the rename is not explained either.
        let mut extra = crozier;
        extra[3] = "    asked_by=\"someone\",";
        assert!(holds("reference.md", &reused, &fern, &extra).is_none());
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
        let sdk = crate::emit::certified_fern_pair().python_sdk;
        let shared = literals.replace(
            &format!("\"generatorVersion\": \"{sdk}\",\n  \"generatorConfig\""),
            &format!("\"generatorVersion\": \"{sdk}\", \"generatorConfig\""),
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
            region(reordered, "src/acme/types/__init__.py"),
            Some(Region {
                fern: 3..5,
                crozier: 3..5
            })
        );
        assert!(region(reordered, "types/__init__.py").is_some());
        // The root package's block is written in Fern's order (#920).
        assert_eq!(region(reordered, "src/acme/__init__.py"), None);
        assert_eq!(region(reordered, "__init__.py"), None);
        // Another import, another module, no block, or the same order.
        let other = reordered.replace("from .b import B", "from .c import C");
        assert_eq!(region(&other, "types/__init__.py"), None);
        assert_eq!(region(reordered, "client.py"), None);
        assert_eq!(region("import typing\n", "types/__init__.py"), None);
        assert_eq!(region(&crozier.join("\n"), "types/__init__.py"), None);
        // A block line that is not indented one level cannot be sorted alone.
        let shallow = "if typing.TYPE_CHECKING:\n  from .b import B\n    from .a import A\nx\n";
        assert_eq!(region(shallow, "types/__init__.py"), None);
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
            let parsed: Kind = crate::yaml::from_str(kind.as_str()).unwrap();
            assert_eq!(parsed, kind);
        }
    }
    #[test]
    fn body_query_departure_accepts_only_the_body_variable_substitution() {
        let fern = [
            "    def record(self, *, level: int, reading_level: int):",
            "            params={",
            "                \"level\": level,",
            "            },",
            "            json={",
            "                \"level\": level,",
            "            },",
        ];
        let mut crozier = fern;
        crozier[5] = "                \"level\": reading_level,";
        assert_eq!(
            super::body_query_parameter_value(&pair("src/api/raw_client.py", &fern, &crozier)),
            Ok(Some(super::Region {
                fern: 5..6,
                crozier: 5..6
            }))
        );
        assert_eq!(
            super::body_query_parameter_value(&pair("src/api/client.py", &fern, &crozier)),
            Ok(None)
        );
        assert_eq!(
            super::body_query_parameter_value(&pair("src/api/raw_client.py", &fern, &fern)),
            Ok(None)
        );
        for changed in [
            "                \"level\": other_level,",
            "                \"threshold\": reading_level,",
            "                \"level\": 3,",
            "                \"level\": \"a b\",",
        ] {
            crozier[5] = changed;
            assert_eq!(
                super::body_query_parameter_value(&pair("src/api/raw_client.py", &fern, &crozier)),
                Ok(None)
            );
        }
        crozier[5] = "                \"level\": reading_level,";
        crozier[0] = "    def record(self, *, level: int):";
        assert_eq!(
            super::body_query_parameter_value(&pair("src/api/raw_client.py", &fern, &crozier)),
            Ok(None)
        );
        crozier[0] = fern[0];
        crozier[2] = "                \"threshold\": level,";
        assert_eq!(
            super::body_query_parameter_value(&pair("src/api/raw_client.py", &fern, &crozier)),
            Ok(None)
        );
    }

    #[test]
    fn body_query_departure_keeps_converter_annotation_and_string_contents() {
        let fern = [
            "    def record(self, *, level: int, reading_level: int):",
            "            params={",
            "                \"level\": level,",
            "            },",
            "            json={",
            "                \"level\": convert_and_respect_annotation_metadata(object_=level, annotation=int, direction=\"write\"),",
            "            },",
        ];
        let crozier = [
            fern[0],
            fern[1],
            fern[2],
            fern[3],
            fern[4],
            "                \"level\": convert_and_respect_annotation_metadata(",
            "                    object_=reading_level, annotation=int, direction=\"write\",",
            "                ),",
            fern[6],
        ];
        assert_eq!(
            super::body_query_parameter_value(&pair("src/api/raw_client.py", &fern, &crozier)),
            Ok(Some(super::Region {
                fern: 5..6,
                crozier: 5..8
            }))
        );
        assert!(matches!(
            super::body_query_parameter_value(&pair("raw_client.py", &fern, &crozier)),
            Ok(Some(_))
        ));
        let mut changed = crozier;
        changed[6] =
            "                    object_=reading_level, annotation=str, direction=\"write\"";
        assert_eq!(
            super::body_query_parameter_value(&pair("src/api/raw_client.py", &fern, &changed)),
            Ok(None)
        );
        assert_eq!(
            super::compact_python(&[" \"a b\" : '\\'c d' "]),
            "\"a b\":'\\'c d'"
        );
    }

    /// The tide-pool survey's `SurveyEntry`: `level` names a union of two
    /// references with no discriminator, `sighting` an object.
    fn wrapped_union_document(inner_discriminator: bool) -> serde_json::Value {
        let mut level = serde_json::json!({"oneOf": [
            {"$ref": "#/components/schemas/DepthCentimetres"},
            {"$ref": "#/components/schemas/GaugeReading"}
        ]});
        if inner_discriminator {
            level["discriminator"] = serde_json::json!({"propertyName": "unit"});
        }
        serde_json::json!({"components": {"schemas": {
            "SurveyEntry": {
                "oneOf": [
                    {"$ref": "#/components/schemas/WaterLevel"},
                    {"$ref": "#/components/schemas/CreatureSighting"}
                ],
                "discriminator": {"propertyName": "entryType", "mapping": {
                    "level": "#/components/schemas/WaterLevel",
                    "sighting": "#/components/schemas/CreatureSighting"
                }}
            },
            "WaterLevel": level,
            "DepthCentimetres": {"type": "number"},
            "GaugeReading": {"type": "object", "properties": {"gauge": {"type": "string"}}},
            "CreatureSighting": {"type": "object", "properties": {"species": {"type": "string"}}}
        }}})
    }

    const WRAPPED_FERN: &str = "client.log_entry(\n    pool_id=\"poolId\",\n    request=SurveyEntry_Level(\n        level=,\n    ),\n)\n";
    const WRAPPED_CROZIER: &str =
        "client.log_entry(\n    pool_id=\"poolId\",\n    request=SurveyEntry_Level(value=1.1),\n)\n";

    #[test]
    fn the_wrapped_union_member_rule_takes_only_the_empty_keyword_examples() {
        let rule: RegionRule = wrapped_union_member_docs_example;
        let context = source_context(wrapped_union_document(false), &[]);
        for rel in ["README.md", "reference.md"] {
            assert_eq!(
                region_of(rule, rel, WRAPPED_FERN, WRAPPED_CROZIER, &context),
                Some(Region {
                    fern: 2..5,
                    crozier: 2..3
                })
            );
        }
        // An exploded wrapper is no measured form, so it is left to fail.
        let exploded = "client.log_entry(\n    pool_id=\"poolId\",\n    request=SurveyEntry_Level(\n        value=GaugeReading(\n            gauge=\"gauge\",\n        )\n    ),\n)\n";
        assert_eq!(
            region_of(rule, "README.md", WRAPPED_FERN, exploded, &context),
            None
        );
        // A string payload holding a parenthesis still closes at the call.
        let quoted = WRAPPED_CROZIER.replace("value=1.1", "value=\"a (b\"");
        assert!(region_of(rule, "README.md", WRAPPED_FERN, &quoted, &context).is_some());
        for (rel, fern, crozier, context) in [
            // An adjacent unexplained difference still fails the file.
            (
                "README.md",
                WRAPPED_FERN.to_string(),
                WRAPPED_CROZIER.replace("poolId", "pool"),
                &context,
            ),
            // Fern's keyword must be the mapping value.
            (
                "README.md",
                WRAPPED_FERN.replace("level=,", "depth=,"),
                WRAPPED_CROZIER.to_string(),
                &context,
            ),
            // A wrapper the document does not declare.
            (
                "README.md",
                WRAPPED_FERN.replace("SurveyEntry_Level", "SurveyEntry_Tide"),
                WRAPPED_CROZIER.replace("SurveyEntry_Level", "SurveyEntry_Tide"),
                &context,
            ),
            // Python files are compared as Fern writes them.
            (
                "src/fern/client.py",
                WRAPPED_FERN.to_string(),
                WRAPPED_CROZIER.to_string(),
                &context,
            ),
            // Nothing to correct.
            (
                "README.md",
                WRAPPED_CROZIER.to_string(),
                WRAPPED_CROZIER.to_string(),
                &context,
            ),
        ] {
            assert_eq!(
                region_of(rule, rel, &fern, &crozier, context),
                None,
                "{fern}"
            );
        }
        // A union target with its own discriminator is another departure's.
        let nested = source_context(wrapped_union_document(true), &[]);
        assert_eq!(
            region_of(rule, "README.md", WRAPPED_FERN, WRAPPED_CROZIER, &nested),
            None
        );
        assert_eq!(
            region_of(
                rule,
                "README.md",
                WRAPPED_FERN,
                WRAPPED_CROZIER,
                &Context::default()
            ),
            None
        );
    }

    /// A context whose source document is `document` and whose crozier tree
    /// holds `crozier` (each `(path, text)`).
    fn source_context(document: serde_json::Value, crozier: &[(&str, &str)]) -> Context {
        Context::from_sources([], crozier.iter().copied())
            .with_source_document(serde_json::from_value(document).expect("a source document"))
    }

    fn line_holds(rule: LineRule, rel: &str, context: &Context, fern: &str, crozier: &str) -> bool {
        let (fern_lines, crozier_lines) = ([fern], [crozier]);
        rule(
            &Pair {
                rel,
                fern: &fern_lines,
                crozier: &crozier_lines,
                context,
            },
            fern,
            crozier,
        )
    }

    fn added_at_holds(rule: AddedAtRule, rel: &str, context: &Context, crozier: &str) -> Vec<bool> {
        let lines: Vec<&str> = crozier.split('\n').collect();
        (0..lines.len())
            .map(|at| {
                rule(
                    &Pair {
                        rel,
                        fern: &[],
                        crozier: &lines,
                        context,
                    },
                    at,
                )
            })
            .collect()
    }

    #[test]
    fn declared_request_string_example_admits_only_the_declared_composition_example() {
        let document = |schema: serde_json::Value, location: &str| {
            serde_json::json!({"openapi": "3.0.3", "paths": {"/docks/{dock}": {"get": {
                "parameters": [{"name": "dock", "in": location, "required": true, "schema": schema}],
                "responses": {}
            }}}})
        };
        let composed = serde_json::json!({
            "example": "northbasin",
            "anyOf": [{"type": "string", "pattern": "^[a-z]+$"}, {"type": "string", "format": "uuid"}]
        });
        let context = source_context(document(composed.clone(), "path"), &[]);
        let (fern, crozier) = ("    dock=\"dock\",", "    dock=\"northbasin\",");
        let rule: LineRule = declared_request_string_example;
        for rel in ["README.md", "reference.md", "src/fern/docks/client.py"] {
            assert!(line_holds(rule, rel, &context, fern, crozier), "{rel}");
        }
        // Outside an example file, another value, another keyword, another
        // indentation, or Fern's line naming something else: no departure.
        assert!(!line_holds(
            rule,
            "src/fern/docks/raw_client.py",
            &context,
            fern,
            crozier
        ));
        for (left, right) in [
            (fern, "    dock=\"southbasin\","),
            (fern, "    berth=\"northbasin\","),
            (fern, "        dock=\"northbasin\","),
            ("    dock=\"other\",", crozier),
            (fern, fern),
        ] {
            assert!(
                !line_holds(rule, "README.md", &context, left, right),
                "{right}"
            );
        }
        // A query parameter, a plain string schema, or no source document.
        let query = source_context(document(composed, "query"), &[]);
        assert!(!line_holds(rule, "README.md", &query, fern, crozier));
        let plain = source_context(
            document(
                serde_json::json!({"type": "string", "example": "northbasin"}),
                "path",
            ),
            &[],
        );
        assert!(!line_holds(rule, "README.md", &plain, fern, crozier));
        assert!(!line_holds(
            rule,
            "README.md",
            &Context::default(),
            fern,
            crozier
        ));
    }

    #[test]
    fn declared_reference_examples_admit_only_source_values_and_leave_adjacent_mismatches() {
        let context = source_context(
            serde_json::json!({
                "openapi": "3.1.0", "paths": {"/parcels": {"post": {
                    "parameters": [{"name": "tracking", "in": "query", "required": true,
                        "schema": {"$ref": "#/components/schemas/Code", "type": "string"},
                        "example": "harbor-842"}], "responses": {}
                }}}, "components": {"schemas": {
                    "Code": {"type": "string"},
                    "Parcel": {"type": "object", "required": ["category"], "properties": {
                        "category": {"allOf": [{"$ref": "#/components/schemas/Code"},
                            {"description": "The delivery category."}], "example": "overnight"}
                    }}
                }}
            }),
            &[],
        );
        let rule: LineRule = declared_request_string_example;
        for rel in ["README.md", "reference.md", "src/fern/client.py"] {
            for (name, example) in [("tracking", "harbor-842"), ("category", "overnight")] {
                let fern = format!("    {name}=\"{name}\",");
                let crozier = format!("    {name}=\"{example}\",");
                assert!(
                    line_holds(rule, rel, &context, &fern, &crozier),
                    "{rel}: {name}"
                );
                assert!(!line_holds(
                    rule,
                    rel,
                    &context,
                    &fern,
                    "    category=\"unexplained\","
                ));
                assert!(!line_holds(
                    rule,
                    rel,
                    &context,
                    "    adjacent=\"adjacent\",",
                    "    adjacent=\"changed\","
                ));
            }
        }
    }

    #[test]
    fn referenced_query_examples_require_established_schema_validity() {
        for (keywords, eligible) in [
            (serde_json::json!({}), true),
            (serde_json::json!({"minLength":1}), true),
            (serde_json::json!({"minLength":100}), false),
            (serde_json::json!({"maxLength":5}), false),
            (serde_json::json!({"pattern":"^harbor-"}), false),
        ] {
            let mut component = serde_json::json!({"type":"string"});
            component
                .as_object_mut()
                .unwrap()
                .extend(keywords.as_object().unwrap().clone());
            let context = source_context(
                serde_json::json!({
                    "openapi":"3.1.0", "paths":{"/parcels":{"post":{
                        "parameters":[{"name":"tracking","in":"query","required":true,
                            "schema":{"$ref":"#/components/schemas/Code","type":"string"},
                            "example":"harbor-842"}], "responses":{}
                    }}}, "components":{"schemas":{"Code":component}}
                }),
                &[],
            );
            for rel in ["README.md", "reference.md", "src/fern/client.py"] {
                assert_eq!(
                    line_holds(
                        declared_request_string_example,
                        rel,
                        &context,
                        "    tracking=\"tracking\",",
                        "    tracking=\"harbor-842\","
                    ),
                    eligible,
                    "{rel}: {keywords}"
                );
            }
        }
    }

    #[test]
    fn referenced_string_departures_abstain_on_unchecked_assertions() {
        for assertion in [
            serde_json::json!({"not":{"type":"string"}}),
            serde_json::json!({"unevaluatedProperties":false}),
        ] {
            let mut target = serde_json::json!({"type":"string"});
            target
                .as_object_mut()
                .unwrap()
                .extend(assertion.as_object().unwrap().clone());
            let context = source_context(
                serde_json::json!({"openapi":"3.1.0", "paths":{},
                "components":{"schemas":{"Code":target}}}),
                &[],
            );
            assert!(!plain_string_reference(
                context.source_document.as_ref().unwrap(),
                "#/components/schemas/Code"
            ));
        }
    }

    #[test]
    fn text_response_optional_query_examples_admit_only_a_declared_optional_query_value() {
        let document = |media: &str, required: bool| {
            serde_json::json!({"openapi": "3.0.3", "paths": {"/log": {"get": {
                "parameters": [{"name": "columns", "in": "query", "required": required,
                    "schema": {"type": "string", "example": "vessel,arrival"}}],
                "responses": {"200": {"description": "ok", "content": {media: {"schema": {"type": "string"}}}}}
            }}}})
        };
        let context = source_context(document("text/plain", false), &[]);
        let line = "    columns=\"vessel,arrival\",";
        for rel in ["README.md", "reference.md", "src/fern/docks/client.py"] {
            assert!(
                text_response_optional_query_examples(&pair_with(rel, &context), line),
                "{rel}"
            );
        }
        assert!(!text_response_optional_query_examples(
            &pair_with("README.md", &context),
            "    columns=\"vessel\","
        ));
        assert!(!text_response_optional_query_examples(
            &pair_with("README.md", &context),
            "    rows=\"vessel,arrival\","
        ));
        assert!(!text_response_optional_query_examples(
            &pair_with("src/fern/docks/raw_client.py", &context),
            line
        ));
        for (media, required) in [("application/json", false), ("text/plain", true)] {
            let other = source_context(document(media, required), &[]);
            assert!(
                !text_response_optional_query_examples(&pair_with("README.md", &other), line),
                "{media} {required}"
            );
        }
        assert!(!text_response_optional_query_examples(
            &pair_with("README.md", &Context::default()),
            line
        ));
    }

    fn pair_with<'a>(rel: &'a str, context: &'a Context) -> Pair<'a> {
        Pair {
            rel,
            fern: &[],
            crozier: &[],
            context,
        }
    }

    #[test]
    fn required_null_union_field_example_admits_only_the_reference_model_s_required_field() {
        let alias = "import typing\n\nShelfItemPayload = typing.Union[\n    typing.Optional[ShelfItemPayloadZero],\n    typing.List[typing.Optional[ShelfItemPayloadOneItem]],\n]\n";
        let model = |payload: &str| {
            format!("class ShelfItem(UniversalBaseModel):\n    label: str\n    payload: {payload}\n\n    if IS_PYDANTIC_V2:\n        model_config = 1\n")
        };
        let required = model("ShelfItemPayload");
        let context = |model: &str, alias: &str| {
            Context::from_sources(
                [
                    ("src/fern/types/shelf_item.py", model.to_string()),
                    ("src/fern/types/shelf_item_payload.py", alias.to_string()),
                ]
                .iter()
                .map(|(rel, text)| (*rel, text.as_str()))
                .collect::<Vec<_>>(),
                [],
            )
        };
        let rule: AddedAtRule = required_null_union_field_example;
        let docstring = "            items=[\n                ShelfItem(\n                    label=\"label\",\n                    payload=\"payload\",\n                )\n            ],";
        let held = context(&required, alias);
        assert_eq!(
            added_at_holds(rule, "src/fern/shelves/client.py", &held, docstring),
            [false, false, false, true, false, false]
        );
        assert_eq!(
            added_at_holds(rule, "reference.md", &held, docstring),
            [false, false, false, true, false, false]
        );
        // A raw client, another field, a multi-line value, another class, a
        // field Fern gives a default, or a union opening with a required
        // member: no departure.
        let defaulted = model("typing.Optional[ShelfItemPayload] = None");
        let opens_required = alias.replace(
            "typing.Optional[ShelfItemPayloadZero]",
            "ShelfItemPayloadZero",
        );
        for (rel, context, text) in [
            (
                "src/fern/shelves/raw_client.py",
                &held,
                docstring.to_string(),
            ),
            (
                "src/fern/shelves/client.py",
                &held,
                docstring.replace("payload=", "label="),
            ),
            (
                "src/fern/shelves/client.py",
                &held,
                docstring.replace("payload=\"payload\",", "payload=["),
            ),
            (
                "src/fern/shelves/client.py",
                &held,
                docstring.replace("ShelfItem(", "ShelfNote("),
            ),
            (
                "src/fern/shelves/client.py",
                &context(&defaulted, alias),
                docstring.to_string(),
            ),
            (
                "src/fern/shelves/client.py",
                &context(&required, &opens_required),
                docstring.to_string(),
            ),
        ] {
            assert!(
                !added_at_holds(rule, rel, context, &text).contains(&true),
                "{rel}: {text}"
            );
        }
    }

    #[test]
    fn optional_lowered_required_query_array_example_admits_only_the_declared_list() {
        let document = |required: bool, example: serde_json::Value| {
            serde_json::json!({"openapi": "3.0.3", "paths": {"/tides": {"get": {
                "parameters": [{"name": "gauges", "in": "query", "required": required,
                    "schema": {"type": "array", "items": {"type": "number"}, "example": example}}],
                "responses": {}
            }}}})
        };
        let context = source_context(document(true, serde_json::json!([3, 7])), &[]);
        let rule: AddedAtRule = optional_lowered_required_query_array_example;
        let wrapped = "client.tides.get_surge(\n    station_id=\"s\",\n    gauges=[\n        3,\n        7\n    ],\n)";
        assert_eq!(
            added_at_holds(rule, "reference.md", &context, wrapped),
            [false, false, true, true, true, true, false]
        );
        let flat = "        client.tides.get_surge(\n            gauges=[3.0, 7.0],\n        )";
        assert_eq!(
            added_at_holds(rule, "src/fern/tides/client.py", &context, flat),
            [false, true, false]
        );
        // Another list, a nested one, a raw client, an optional or undeclared
        // parameter, or no source document: no departure.
        for (rel, text) in [
            (
                "reference.md",
                wrapped.replace("        7\n", "        8\n"),
            ),
            (
                "reference.md",
                wrapped.replace("        7\n", "            7\n"),
            ),
            ("src/fern/tides/client.py", flat.replace("7.0", "7.5")),
            (
                "src/fern/tides/client.py",
                flat.replace("[3.0, 7.0]", "[1.1]"),
            ),
            ("src/fern/tides/raw_client.py", flat.to_string()),
        ] {
            assert!(
                !added_at_holds(rule, rel, &context, &text)
                    .iter()
                    .any(|holds| *holds),
                "{text}"
            );
        }
        for other in [
            source_context(document(false, serde_json::json!([3, 7])), &[]),
            source_context(document(true, serde_json::Value::Null), &[]),
            Context::default(),
        ] {
            assert!(!added_at_holds(rule, "reference.md", &other, wrapped)
                .iter()
                .any(|holds| *holds));
        }
        assert!(item_is_value("\"a\"", &serde_json::json!("a")));
        assert!(item_is_value("True", &serde_json::json!(true)));
        assert!(!item_is_value("{}", &serde_json::json!({})));
    }

    #[test]
    fn collapsed_anyof_property_description_admits_only_the_property_description() {
        let property = |first: serde_json::Value| {
            serde_json::json!({"openapi": "3.0.3", "paths": {}, "components": {"schemas": {
                "Charter": {"type": "object", "required": ["skipper"], "properties": {
                    "skipper": {"description": "The skipper's ID.", "anyOf": [first, {"type": "string"}]}
                }}
            }}})
        };
        let context = source_context(
            property(serde_json::json!({"type": "string", "format": "uuid"})),
            &[],
        );
        let rule: LineRule = collapsed_anyof_property_description;
        let row = "**skipper:** `str` ";
        assert!(line_holds(
            rule,
            "reference.md",
            &context,
            row,
            "**skipper:** `str` — The skipper's ID."
        ));
        assert!(!line_holds(
            rule,
            "reference.md",
            &context,
            row,
            "**skipper:** `str` — Another."
        ));
        assert!(!line_holds(
            rule,
            "reference.md",
            &context,
            "**guests:** `int` ",
            "**guests:** `int` — The skipper's ID."
        ));
        let field = "    skipper: str";
        assert!(line_holds(
            rule,
            "src/fern/types/charter.py",
            &context,
            field,
            "    skipper: str = pydantic.Field()"
        ));
        assert!(!line_holds(
            rule,
            "src/fern/types/charter.py",
            &context,
            field,
            "    skipper: str = pydantic.Field(alias=\"s\")"
        ));
        assert!(!line_holds(
            rule,
            "src/fern/types/charter.py",
            &context,
            "    guests: int",
            "    guests: int = pydantic.Field()"
        ));
        let added: AddedAtRule = collapsed_anyof_property_description_line;
        let model = "class Charter(UniversalBaseModel):\n    skipper: str = pydantic.Field()\n    \"\"\"\n    The skipper's ID.\n    \"\"\"\n\n    vessel: str";
        assert_eq!(
            added_at_holds(added, "src/fern/types/charter.py", &context, model),
            [false, false, true, true, true, true, false]
        );
        let docstring = "        Parameters\n        ----------\n        skipper : str\n            The skipper's ID.\n\n        guests : int";
        assert_eq!(
            added_at_holds(added, "src/fern/charters/client.py", &context, docstring),
            [false, false, false, true, false, false]
        );
        for text in [
            model.replace("The skipper's ID.", "Another."),
            docstring.replace("The skipper's ID.", "Another."),
        ] {
            assert!(
                !added_at_holds(added, "src/fern/charters/client.py", &context, &text)
                    .iter()
                    .any(|holds| *holds)
            );
        }
        assert!(!added_at_holds(added, "reference.md", &context, docstring)
            .iter()
            .any(|holds| *holds));
        // A first alternative carrying its own description is the one Fern
        // keeps, and the rule does not apply; nor without the document.
        let described = source_context(
            property(serde_json::json!({"type": "string", "description": "Own."})),
            &[],
        );
        assert!(!line_holds(
            rule,
            "reference.md",
            &described,
            row,
            "**skipper:** `str` — The skipper's ID."
        ));
        assert!(
            !added_at_holds(added, "src/fern/charters/client.py", &described, docstring)
                .iter()
                .any(|holds| *holds)
        );
        assert!(!line_holds(
            rule,
            "reference.md",
            &Context::default(),
            row,
            "**skipper:** `str` — The skipper's ID."
        ));
    }

    // End-to-end rejection proof declined: `crozier compare` refuses only against a
    // Fern tree carrying the crafted defect, which Fern never writes, so each case
    // would cost a reference regeneration while handing the rule the same Pair these
    // cases build. Acceptance runs end to end in every golden comparison, pinned line
    // by line in tests/fixtures/departures-ledger.tsv.
    #[test]
    fn emoji_tag_reference_identifiers_admit_only_the_raw_tag_spelling_of_a_module() {
        let document = serde_json::json!({"openapi": "3.0.3", "paths": {"/legacy": {"get": {
            "tags": ["🚧 Legacy endpoints"], "responses": {}
        }}}});
        let modules = [("src/fern/legacy_endpoints/client.py", "")];
        let context = source_context(document.clone(), &modules);
        let rule: LineRule = emoji_tag_reference_identifiers;
        let crozier = "<code>client.legacy_endpoints.<a href=\"src/fern/legacy_endpoints/client.py\">list</a>(...)</code>";
        let fern = crozier.replace("legacy_endpoints", "🚧_legacy_endpoints");
        for rel in ["README.md", "reference.md"] {
            assert!(line_holds(rule, rel, &context, &fern, crozier), "{rel}");
        }
        assert!(!line_holds(
            rule,
            "src/fern/client.py",
            &context,
            &fern,
            crozier
        ));
        // One occurrence left raw, another module, a module crozier lacks, or no
        // document: no departure.
        let half = crozier.replacen("legacy_endpoints", "🚧_legacy_endpoints", 1);
        assert!(!line_holds(rule, "reference.md", &context, &fern, &half));
        let other = fern.replace("🚧_legacy_endpoints.<a", "🚧_legacy.<a");
        assert!(!line_holds(rule, "reference.md", &context, &other, crozier));
        let without_module = source_context(document, &[("src/fern/other/client.py", "")]);
        assert!(!line_holds(
            rule,
            "reference.md",
            &without_module,
            &fern,
            crozier
        ));
        assert!(!line_holds(
            rule,
            "reference.md",
            &Context::default(),
            &fern,
            crozier
        ));
        assert!(!line_holds(
            rule,
            "reference.md",
            &context,
            crozier,
            crozier
        ));
    }

    // Rejection runs end to end too: crates/crozier-e2e/tests/e2e/compare.rs's
    // `compare_holds_each_reference_link_departure_to_its_own_shape` drives `crozier compare` over
    // the real golden with Fern's heading edited into a different defect, and this rule refuses
    // it. These cases add the controls a golden cannot carry (a client without the escaped method,
    // a name needing no escape, another file).
    #[test]
    fn reference_heading_escaped_method_names_admit_only_the_method_the_client_defines() {
        let client = "class ApplicantsClient:\n    def all_(self) -> None:\n        pass\n";
        let context = Context::from_sources([], [("src/fern/applicants/client.py", client)]);
        let rule: LineRule = reference_heading_escaped_method_name;
        let fern = "<details><summary><code>client.applicants.<a href=\"src/fern/applicants/client.py\">all</a>(...) -> GetApplicantsResponse</code></summary>";
        let crozier = "<details><summary><code>client.applicants.<a href=\"src/fern/applicants/client.py#L2-L3\">all_</a>(...) -> GetApplicantsResponse</code></summary>";
        assert!(line_holds(rule, "reference.md", &context, fern, crozier));
        // Only reference.md, and only when the client defines the escaped method.
        for rel in ["README.md", "src/fern/applicants/client.py"] {
            assert!(!line_holds(rule, rel, &context, fern, crozier), "{rel}");
        }
        let elsewhere = Context::from_sources([], [("src/fern/jobs/client.py", client)]);
        assert!(!line_holds(rule, "reference.md", &elsewhere, fern, crozier));
        assert!(!line_holds(
            rule,
            "reference.md",
            &Context::default(),
            fern,
            crozier
        ));
        // An unrelated change on the same line, a name that is not the escape
        // of Fern's, an anchor that is not a line range, or no anchor at all.
        for mutated in [
            crozier.replace("GetApplicantsResponse", "GetJobsResponse"),
            crozier.replace(">all_<", ">al_<"),
            crozier.replace("#L2-L3", "#Lx-L3"),
            crozier.replace("#L2-L3", "#L999-L1000"),
            crozier.replace("#L2-L3", ""),
            crozier.replace("client.applicants.", "client.jobs."),
        ] {
            assert!(
                !line_holds(rule, "reference.md", &context, fern, &mutated),
                "{mutated}"
            );
        }
        // A name that needs no escape is no departure: crozier writes Fern's.
        let plain = Context::from_sources(
            [],
            [(
                "src/fern/applicants/client.py",
                "class ApplicantsClient:\n    def list(self) -> None:\n        pass\n",
            )],
        );
        assert!(!line_holds(
            rule,
            "reference.md",
            &plain,
            &fern.replace(">all<", ">list<"),
            &crozier.replace(">all_<", ">list<")
        ));
    }

    // End-to-end rejection proof declined: `crozier compare` refuses only against a
    // Fern tree carrying the crafted defect, which Fern never writes, so each case
    // would cost a reference regeneration while handing the rule the same Pair these
    // cases build. Acceptance runs end to end in every golden comparison, pinned line
    // by line in tests/fixtures/departures-ledger.tsv.
    #[test]
    fn a_reference_anchor_departs_only_where_each_side_names_its_own_method() {
        let fern_client = "class FernApi:\n    def __init__(self):\n        \"\"\"\n        api_key=\"k\",\n        api_key=\"k\",\n        \"\"\"\n\n    def relay(self) -> None:\n        pass\n";
        let crozier_client = "class FernApi:\n    def __init__(self):\n        \"\"\"\n        api_key=\"k\",\n        \"\"\"\n\n    def relay(self) -> None:\n        pass\n";
        let context = Context::from_sources(
            [("src/fern/client.py", fern_client)],
            [("src/fern/client.py", crozier_client)],
        );
        let rule: RegionRule = reference_anchor_follows_corrected_client;
        let heading = |range: &str| {
            format!("# Reference\n<details><summary><code>client.<a href=\"src/fern/client.py#{range}\">relay</a>(...)</code></summary>\n<dl>\n")
        };
        let region = region_of(
            rule,
            "reference.md",
            &heading("L8-L9"),
            &heading("L7-L8"),
            &context,
        )
        .expect("each side's range is its own method's lines");
        assert_eq!((region.fern, region.crozier), (1..2, 1..2));
        // A range that is not the method's lines on either side, an unrelated
        // change beside the range, another file, or one side without a range.
        for (fern, crozier) in [
            (heading("L8-L9"), heading("L7-L9")),
            (heading("L7-L8"), heading("L7-L9")),
            (heading("L8-L9"), heading("L7-L8").replace("(...)", "()")),
            (heading("L8-L9").replace("#L8-L9", ""), heading("L7-L8")),
        ] {
            assert!(
                region_of(rule, "reference.md", &fern, &crozier, &context).is_none(),
                "{crozier}"
            );
        }
        assert!(region_of(
            rule,
            "README.md",
            &heading("L8-L9"),
            &heading("L7-L8"),
            &context
        )
        .is_none());
        assert!(region_of(
            rule,
            "reference.md",
            &heading("L8-L9"),
            &heading("L7-L8"),
            &Context::default()
        )
        .is_none());
    }

    // Rejection runs end to end too: crates/crozier-e2e/tests/e2e/compare.rs's
    // `compare_holds_each_reference_link_departure_to_its_own_shape` drives `crozier compare` over
    // the real golden with Fern's heading edited into a different defect, and this rule refuses
    // it. These cases add the controls a golden cannot carry (a `_` module Fern's tree holds too,
    // another module, another file).
    #[test]
    fn an_empty_namespace_heading_takes_only_the_anchor_of_crozier_s_own_module() {
        let client = "class UnderscoreClient:\n    def list_lamps(self) -> None:\n        pass\n";
        let context = Context::from_sources(
            [("src/fern/client.py", client)],
            [("src/fern/_/client.py", client)],
        );
        let rule: LineRule = empty_namespace_reference_anchor;
        let fern = "<details><summary><code>client._.<a href=\"src/fern/_/client.py\">list_lamps</a>(...) -> typing.List[Lamp]</code></summary>";
        let crozier = fern.replace("_/client.py\"", "_/client.py#L2-L3\"");
        assert!(line_holds(rule, "reference.md", &context, fern, &crozier));
        for mutated in [
            crozier.replace("#L2-L3", "#L2-L4"),
            crozier.replace("typing.List[Lamp]", "Lamp"),
            crozier.replace(">list_lamps<", ">get_lamp<"),
        ] {
            assert!(
                !line_holds(rule, "reference.md", &context, fern, &mutated),
                "{mutated}"
            );
        }
        assert!(!line_holds(rule, "README.md", &context, fern, &crozier));
        // Another module, or a `_` module Fern's tree holds too, anchors on both sides.
        let elsewhere = crozier.replace("/_/", "/lamps/");
        let fern_elsewhere = fern.replace("/_/", "/lamps/");
        let lamps = Context::from_sources([], [("src/fern/lamps/client.py", client)]);
        assert!(!line_holds(
            rule,
            "reference.md",
            &lamps,
            &fern_elsewhere,
            &elsewhere
        ));
        let both = Context::from_sources(
            [("src/fern/_/client.py", client)],
            [("src/fern/_/client.py", client)],
        );
        assert!(!line_holds(rule, "reference.md", &both, fern, &crozier));
    }

    // End-to-end rejection proof declined: `crozier compare` refuses only against a
    // Fern tree carrying the crafted defect, which Fern never writes, so each case
    // would cost a reference regeneration while handing the rule the same Pair these
    // cases build. Acceptance runs end to end in every golden comparison, pinned line
    // by line in tests/fixtures/departures-ledger.tsv.
    #[test]
    fn misspelt_reference_headings_admit_crozier_s_anchor_only_with_their_correction() {
        let document = serde_json::json!({"paths": {"/readings": {"get": {
            "operationId": "7readings", "responses": {}
        }}}});
        let context = source_context(
            document,
            &[(
                "src/fern/client.py",
                "class FernApi:\n    def _7readings(self) -> None:\n        pass\n",
            )],
        );
        let rule: LineRule = digit_leading_method_reference_identifiers;
        let fern = "<details><summary><code>client.<a href=\"src/fern/client.py\">7readings</a>()</code></summary>";
        let crozier = "<details><summary><code>client.<a href=\"src/fern/client.py#L2-L3\">_7readings</a>()</code></summary>";
        assert!(line_holds(rule, "reference.md", &context, fern, crozier));
        // The anchor alone, without the corrected name, is no departure.
        let anchored_only = crozier.replace(">_7readings<", ">7readings<");
        assert!(!line_holds(
            rule,
            "reference.md",
            &context,
            fern,
            &anchored_only
        ));
        assert!(!line_holds(
            rule,
            "reference.md",
            &context,
            fern,
            &crozier.replace("()</code>", "(...)</code>")
        ));

        let document = serde_json::json!({"openapi": "3.0.3", "paths": {"/legacy": {"get": {
            "tags": ["🚧 Legacy endpoints"], "responses": {}
        }}}});
        let context = source_context(
            document,
            &[(
                "src/fern/legacy_endpoints/client.py",
                "class LegacyEndpointsClient:\n    def list(self) -> None:\n        pass\n",
            )],
        );
        let rule: LineRule = emoji_tag_reference_identifiers;
        let crozier = "<details><summary><code>client.legacy_endpoints.<a href=\"src/fern/legacy_endpoints/client.py#L2-L3\">list</a>(...)</code></summary>";
        let fern = "<details><summary><code>client.🚧_legacy_endpoints.<a href=\"src/fern/🚧_legacy_endpoints/client.py\">list</a>(...)</code></summary>";
        assert!(line_holds(rule, "reference.md", &context, fern, crozier));
        // A range that is not the method's lines is no departure.
        assert!(!line_holds(
            rule,
            "reference.md",
            &context,
            fern,
            &crozier.replace("#L2-L3", "#L26-L40")
        ));
        assert!(!line_holds(
            rule,
            "reference.md",
            &context,
            fern,
            &crozier.replace(">list<", ">get<")
        ));
    }

    // End-to-end rejection proof declined: `crozier compare` refuses only against a
    // Fern tree carrying the crafted defect, which Fern never writes, so each case
    // would cost a reference regeneration while handing the rule the same Pair these
    // cases build. Acceptance runs end to end in every golden comparison, pinned line
    // by line in tests/fixtures/departures-ledger.tsv.
    #[test]
    fn the_async_import_drops_only_the_sync_client_fern_s_casing_leaks() {
        let client = "class PetStoreApi:\n    pass\n\n\nclass AsyncPetStoreApi:\n    pass\n\n\nclass Pet:\n    pass\n";
        let context = Context::from_sources([], [("client.py", client)]);
        let rule: LineRule = readme_client_class_casing;
        let crozier = "from PetStore import AsyncPetStoreApi";
        for (fern, crozier) in [
            (
                "from PetStore import AsyncPetstoreApi, PetStoreApi",
                crozier,
            ),
            (
                "from PetStore import AsyncPetstoreApi, PetStoreApi, Pet",
                "from PetStore import AsyncPetStoreApi, Pet",
            ),
        ] {
            assert!(
                line_holds(rule, "README.md", &context, fern, crozier),
                "{fern}"
            );
        }
        // Another leaked name, the sync client elsewhere in the list, or another
        // async client.
        for (fern, crozier) in [
            ("from PetStore import AsyncPetstoreApi, Pet", crozier),
            (
                "from PetStore import AsyncPetstoreApi, Pet, PetStoreApi",
                "from PetStore import AsyncPetStoreApi, Pet",
            ),
            (
                "from PetStore import AsyncPetstoreApi, PetStoreApi",
                "from PetStore import AsyncOtherApi",
            ),
        ] {
            assert!(
                !line_holds(rule, "README.md", &context, fern, crozier),
                "{fern} / {crozier}"
            );
        }
        let undefined =
            Context::from_sources([], [("client.py", "class AsyncPetStoreApi:\n    pass\n")]);
        assert!(!line_holds(
            rule,
            "README.md",
            &undefined,
            "from PetStore import AsyncPetstoreApi, PetStoreApi",
            crozier
        ));
    }

    // Rejection runs end to end too: crates/crozier-e2e/tests/e2e/compare.rs's
    // `compare_holds_each_reference_link_departure_to_its_own_shape` drives `crozier compare` over
    // the real golden with Fern's heading edited into a different defect, and this rule refuses
    // it. These cases add the controls a golden cannot carry (a Fern tree holding the file its
    // link names, another file).
    #[test]
    fn a_flat_link_departs_only_to_the_module_the_flat_tree_holds() {
        let client = "class PetClient:\n    def add_pet(self) -> None:\n        pass\n";
        let context =
            Context::from_sources([("pet/client.py", client)], [("pet/client.py", client)]);
        let rule: LineRule = flat_reference_link_target;
        let fern = "<details><summary><code>client.pet.<a href=\"src/fern/pet/client.py\">add_pet</a>(...) -> Pet</code></summary>";
        let crozier = "<details><summary><code>client.pet.<a href=\"pet/client.py#L2-L3\">add_pet</a>(...) -> Pet</code></summary>";
        assert!(line_holds(rule, "reference.md", &context, fern, crozier));
        // A wrong range, no range, another module, another method, an unrelated
        // change, or another file.
        for mutated in [
            crozier.replace("#L2-L3", "#L2-L4"),
            crozier.replace("#L2-L3", ""),
            crozier.replace("pet/client.py", "store/client.py"),
            crozier.replace(">add_pet<", ">get_pet<"),
            crozier.replace("-> Pet", "-> Store"),
        ] {
            assert!(
                !line_holds(rule, "reference.md", &context, fern, &mutated),
                "{mutated}"
            );
        }
        assert!(!line_holds(rule, "README.md", &context, fern, crozier));
        // Fern's link is no defect where its own tree holds the file it names.
        let packaged = Context::from_sources(
            [("src/fern/pet/client.py", client)],
            [("pet/client.py", client)],
        );
        assert!(!line_holds(rule, "reference.md", &packaged, fern, crozier));
        // Escaped names and stream return types still depart in a flat tree.
        let escaped = Context::from_sources(
            [("applicants/client.py", "")],
            [(
                "applicants/client.py",
                "class ApplicantsClient:\n    def all_(self) -> None:\n        pass\n",
            )],
        );
        assert!(line_holds(
            reference_heading_escaped_method_name,
            "reference.md",
            &escaped,
            "<details><summary><code>client.applicants.<a href=\"src/fern/applicants/client.py\">all</a>(...)</code></summary>",
            "<details><summary><code>client.applicants.<a href=\"applicants/client.py#L2-L3\">all_</a>(...)</code></summary>"
        ));
    }

    // End-to-end rejection proof declined: `crozier compare` refuses only against a
    // Fern tree carrying the crafted defect, which Fern never writes, so each case
    // would cost a reference regeneration while handing the rule the same Pair these
    // cases build. Acceptance runs end to end in every golden comparison, pinned line
    // by line in tests/fixtures/departures-ledger.tsv.
    #[test]
    fn the_environment_snippet_takes_only_the_usage_constructor_s_arguments() {
        let readme = |environment_arguments: &str| {
            format!(
                "## Usage\n\n```python\nclient = FernApi(\n    api_key=\"<value>\",\n)\n```\n\n\
                 ## Environments\n\n```python\nclient = FernApi(\n{environment_arguments}    environment=FernApiEnvironment.DEFAULT,\n)\n```\n"
            )
        };
        let rule: RegionRule = readme_environment_constructor_arguments;
        let fern = readme("");
        let crozier = readme("    api_key=\"<value>\",\n");
        let context = Context::default();
        let region =
            region_of(rule, "README.md", &fern, &crozier, &context).expect("the usage argument");
        assert_eq!(region.crozier.len(), 1);
        assert!(region.fern.is_empty());
        for mutated in [
            readme("    api_key=\"other\",\n"),
            readme("    api_key=\"<value>\",\n    timeout=1,\n"),
            crozier.replace("## Usage", "## Use"),
        ] {
            assert!(
                region_of(rule, "README.md", &fern, &mutated, &context).is_none(),
                "{mutated}"
            );
        }
        assert!(region_of(rule, "reference.md", &fern, &crozier, &context).is_none());
        // A required typed header `readme-constructor-required-header` already
        // took out of the usage constructor; an optional one is not.
        let client = "class FernApi:\n    def __init__(\n        self,\n        *,\n        strict_mode: bool,\n        retries: typing.Optional[int] = None,\n    ):\n        pass\n";
        let headers = Context::from_sources([], [("src/fern/client.py", client)]);
        let crozier = readme("    api_key=\"<value>\",\n    strict_mode=True,\n");
        let region = region_of(rule, "README.md", &fern, &crozier, &headers)
            .expect("the usage argument and the required header");
        assert_eq!(region.crozier.len(), 2);
        let optional = readme("    api_key=\"<value>\",\n    retries=1,\n");
        assert!(region_of(rule, "README.md", &fern, &optional, &headers).is_none());
        assert!(region_of(rule, "README.md", &fern, &crozier, &context).is_none());
    }

    // End-to-end rejection proof declined: `crozier compare` refuses only against a
    // Fern tree carrying the crafted defect, which Fern never writes, so each case
    // would cost a reference regeneration while handing the rule the same Pair these
    // cases build. Acceptance runs end to end in every golden comparison, pinned line
    // by line in tests/fixtures/departures-ledger.tsv.
    #[test]
    fn a_readme_call_departs_only_to_the_escaped_method_the_group_defines() {
        let client = "class ApisClient:\n    def all_(self) -> None:\n        pass\n";
        let context = Context::from_sources(
            [],
            [
                ("src/fern/apis/client.py", client),
                ("src/fern/apis/raw_client.py", client),
            ],
        );
        let rule: LineRule = readme_escaped_method_call;
        for (fern, crozier) in [
            ("    client.apis.all(...)", "    client.apis.all_(...)"),
            (
                "response = client.apis.with_raw_response.all(...)",
                "response = client.apis.with_raw_response.all_(...)",
            ),
            (
                "client.apis.all(..., request_options={",
                "client.apis.all_(..., request_options={",
            ),
        ] {
            assert!(
                line_holds(rule, "README.md", &context, fern, crozier),
                "{crozier}"
            );
        }
        let fern = "    client.apis.all(...)";
        for mutated in [
            "    client.apis.all_(x)",
            "    client.apis.al_(...)",
            "    client.other.all_(...)",
            "    client.apis.list(...)",
        ] {
            assert!(
                !line_holds(rule, "README.md", &context, fern, mutated),
                "{mutated}"
            );
        }
        assert!(!line_holds(
            rule,
            "reference.md",
            &context,
            fern,
            "    client.apis.all_(...)"
        ));
        assert!(!line_holds(
            rule,
            "README.md",
            &Context::default(),
            fern,
            "    client.apis.all_(...)"
        ));
    }

    // End-to-end rejection proof declined: `crozier compare` refuses only against a
    // Fern tree carrying the crafted defect, which Fern never writes, so each case
    // would cost a reference regeneration while handing the rule the same Pair these
    // cases build. Acceptance runs end to end in every golden comparison, pinned line
    // by line in tests/fixtures/departures-ledger.tsv.
    #[test]
    fn an_abbreviated_call_departs_only_for_a_method_requiring_an_argument() {
        let required = "class FernApi:\n    def probe(\n        self, *, probe_param: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None\n    ) -> None:\n        pass\n";
        let optional = required.replace(
            "probe_param: typing.Sequence[str],",
            "probe_param: typing.Optional[str] = None,",
        );
        let context = Context::from_sources([], [("src/fern/client.py", required)]);
        let rule: LineRule = readme_abbreviated_call_arguments;
        for (fern, crozier) in [
            ("    client.probe()", "    client.probe(...)"),
            (
                "response = client.with_raw_response.probe()",
                "response = client.with_raw_response.probe(...)",
            ),
            (
                "client.probe(request_options={",
                "client.probe(..., request_options={",
            ),
        ] {
            assert!(
                line_holds(rule, "README.md", &context, fern, crozier),
                "{crozier}"
            );
        }
        let fern = "    client.probe()";
        for mutated in [
            "    client.probe(x)",
            "    client.other(...)",
            "    client.probe(...) ",
        ] {
            assert!(
                !line_holds(rule, "README.md", &context, fern, mutated),
                "{mutated}"
            );
        }
        let optional = Context::from_sources([], [("src/fern/client.py", optional.as_str())]);
        assert!(!line_holds(
            rule,
            "README.md",
            &optional,
            fern,
            "    client.probe(...)"
        ));
        assert!(!line_holds(
            rule,
            "reference.md",
            &context,
            fern,
            "    client.probe(...)"
        ));
        // A signature with no return annotation ends at its own `):`, not at the
        // next method's.
        let unannotated = "class FernApi:\n    def ping(self):\n        pass\n\n    def probe(self, value: int) -> None:\n        pass\n";
        let unannotated = Context::from_sources([], [("src/fern/client.py", unannotated)]);
        assert!(!line_holds(
            rule,
            "README.md",
            &unannotated,
            "    client.ping()",
            "    client.ping(...)"
        ));
    }

    // End-to-end rejection proof declined: `crozier compare` refuses only against a
    // Fern tree carrying the crafted defect, which Fern never writes, so each case
    // would cost a reference regeneration while handing the rule the same Pair these
    // cases build. Acceptance runs end to end in every golden comparison, pinned line
    // by line in tests/fixtures/departures-ledger.tsv.
    #[test]
    fn a_list_path_parameter_departs_only_where_crozier_passes_that_parameter() {
        let client = "class UsersClient:\n    def get_users_id(\n        self, id: typing.Sequence[int], *, request_options: typing.Optional[RequestOptions] = None\n    ) -> None:\n        pass\n    def probe(\n        self, probe_param: typing.Sequence[str], *, request_options: typing.Optional[RequestOptions] = None\n    ) -> None:\n        pass\n";
        let context = Context::from_sources([], [("src/fern/users/client.py", client)]);
        let call: RegionRule = list_path_parameter_call;
        let fern = "# Reference\nclient.users.get_users_id()\nafter";
        let crozier =
            "# Reference\nclient.users.get_users_id(\n    id=[\n        1\n    ],\n)\nafter";
        let region =
            region_of(call, "reference.md", fern, crozier, &context).expect("the list argument");
        assert_eq!((region.fern, region.crozier), (1..2, 1..6));
        let fern = "client.users.probe(\n    other=1,\n)";
        let crozier = "client.users.probe(\n    probe_param=\"probeParam\",\n    other=1,\n)";
        assert!(region_of(call, "README.md", fern, crozier, &context).is_some());
        for (fern, crozier) in [
            // Not a list-typed path parameter, another change, not a method call.
            (
                "client.users.get_users_id()",
                "client.users.get_users_id(\n    page=1,\n)",
            ),
            (
                "client.users.get_users_id()",
                "client.users.get_users_id(\n    id=[\n        1\n    ],\n    page=1,\n)",
            ),
            ("print()", "print(\n    id=[\n        1\n    ],\n)"),
        ] {
            assert!(
                region_of(call, "README.md", fern, crozier, &context).is_none(),
                "{crozier}"
            );
        }
        assert!(region_of(
            call,
            "src/fern/users/client.py",
            "client.users.get_users_id()",
            "client.users.get_users_id(\n    id=[\n        1\n    ],\n)",
            &context
        )
        .is_none());

        let line: LineRule = list_path_parameter_docstring_value;
        let rel = "src/fern/users/client.py";
        assert!(line_holds(
            line,
            rel,
            &context,
            "            id=\"ID\",",
            "            id=[1],"
        ));
        for (fern, crozier) in [
            // A list of strings keeps Fern's placeholder; another value or name.
            (
                "            probe_param=\"probeParam\",",
                "            probe_param=[\"probeParam\"],",
            ),
            ("            id=\"ID\",", "            id=1,"),
            ("            page=\"ID\",", "            page=[1],"),
        ] {
            assert!(!line_holds(line, rel, &context, fern, crozier), "{crozier}");
        }
        assert!(!line_holds(
            line,
            "README.md",
            &context,
            "            id=\"ID\",",
            "            id=[1],"
        ));
    }

    // End-to-end rejection proof declined: `crozier compare` refuses only against a
    // Fern tree carrying the crafted defect, which Fern never writes, so each case
    // would cost a reference regeneration while handing the rule the same Pair these
    // cases build. Acceptance runs end to end in every golden comparison, pinned line
    // by line in tests/fixtures/departures-ledger.tsv.
    #[test]
    fn a_digit_leading_property_keyword_departs_only_to_the_declared_parameter() {
        let client = "class ContextClient:\n    def update_sm_context(\n        self,\n        *,\n        _5g_mm_cause_value: typing.Optional[int] = OMIT,\n    ) -> None:\n        pass\n";
        let context = Context::from_sources([], [("src/fern/context/client.py", client)]);
        let rule: LineRule = digit_leading_property_example_keyword;
        for (rel, fern) in [
            (
                "src/fern/context/client.py",
                "            f_5g_mm_cause_value=0,",
            ),
            ("reference.md", "            f_value=0,"),
        ] {
            assert!(
                line_holds(
                    rule,
                    rel,
                    &context,
                    fern,
                    "            _5g_mm_cause_value=0,"
                ),
                "{rel}"
            );
        }
        let fern = "            f_5g_mm_cause_value=0,";
        for crozier in [
            "            _5g_mm_cause_value=1,",
            "            _5g_mm_cause=0,",
            "        _5g_mm_cause_value=0,",
            "            mm_cause_value=0,",
        ] {
            assert!(
                !line_holds(rule, "reference.md", &context, fern, crozier),
                "{crozier}"
            );
        }
        assert!(!line_holds(
            rule,
            "reference.md",
            &Context::default(),
            fern,
            "            _5g_mm_cause_value=0,"
        ));
        assert!(!line_holds(
            rule,
            "src/fern/types/model.py",
            &context,
            fern,
            "            _5g_mm_cause_value=0,"
        ));
    }

    // End-to-end rejection proof declined: `crozier compare` refuses only against a
    // Fern tree carrying the crafted defect, which Fern never writes, so each case
    // would cost a reference regeneration while handing the rule the same Pair these
    // cases build. Acceptance runs end to end in every golden comparison, pinned line
    // by line in tests/fixtures/departures-ledger.tsv.
    #[test]
    fn a_constructor_departs_only_for_its_required_typed_headers() {
        let client = "class FernApi:\n    def __init__(\n        self,\n        *,\n        probe_param: typing.List[str],\n        tenant: str,\n        retries: typing.Optional[int] = None,\n    ):\n        pass\n\n    def probe(\n        self,\n        *,\n        count: int,\n    ) -> None:\n        pass\n";
        let context = Context::from_sources([], [("src/fern/client.py", client)]);
        let rule: RegionRule = readme_constructor_required_header;
        let fern = "x\nclient = FernApi()\ny";
        let crozier = "x\nclient = FernApi(\n    probe_param=[\n        \"probeParam\",\n        \"probeParam\"\n    ],\n)\ny";
        let region = region_of(rule, "README.md", fern, crozier, &context)
            .expect("the required list header");
        assert_eq!((region.fern, region.crozier), (1..2, 1..7));
        let fern = "client = FernApi(\n    tenant=\"<X-Tenant>\",\n)";
        let crozier = "client = FernApi(\n    tenant=\"<X-Tenant>\",\n    probe_param=[\"probeParam\", \"probeParam\"],\n)";
        assert!(region_of(rule, "reference.md", fern, crozier, &context).is_some());
        for (fern, crozier) in [
            // A string or optional parameter, another change, a method call.
            (
                "client = FernApi()",
                "client = FernApi(\n    tenant=\"<X-Tenant>\",\n)",
            ),
            ("client = FernApi()", "client = FernApi(\n    retries=1,\n)"),
            // A required parameter of a method, not of the constructor.
            ("client = FernApi()", "client = FernApi(\n    count=1,\n)"),
            (
                "client = FernApi()",
                "client = FernApi(\n    probe_param=[],\n    retries=1,\n)",
            ),
            ("client.probe()", "client.probe(\n    probe_param=[],\n)"),
        ] {
            assert!(
                region_of(rule, "README.md", fern, crozier, &context).is_none(),
                "{crozier}"
            );
        }
        assert!(region_of(
            rule,
            "src/fern/client.py",
            "client = FernApi()",
            "client = FernApi(\n    probe_param=[],\n)",
            &context
        )
        .is_none());
    }

    #[test]
    fn a_list_of_files_takes_the_list_placeholder() {
        let raw = "    def deploy(\n        self,\n    ):\n        files={\n            \"bundle\": bundle,\n        }\n";
        let context = Context::from_sources([], [("src/acme/raw_client.py", raw)]);
        let fern = "    def deploy(\n        self,\n        *,\n        bundle: typing.List[core.File],\n    ) -> None:\n        \"\"\"\n        Examples\n        --------\n        client.deploy(\n            slug=\"s\",\n        )\n        \"\"\"\n";
        let rule: RegionRule = multipart_object_required_file_example;
        let listed = fern.replace(
            "            slug=\"s\",\n",
            "            slug=\"s\",\n            bundle=[\"example_bundle\"],\n",
        );
        assert!(region_of(rule, "src/acme/client.py", fern, &listed, &context).is_some());
        let single = fern.replace(
            "            slug=\"s\",\n",
            "            slug=\"s\",\n            bundle=\"example_bundle\",\n",
        );
        assert!(region_of(rule, "src/acme/client.py", fern, &single, &context).is_none());
    }

    /// The rejected-example rules through the comparison engine: a client
    /// module whose docstring example passes `keyword=fern` against crozier's
    /// `keyword=crozier`, with `runtime` a line outside the example.
    fn rejected_example_comparison(
        source: &serde_json::Value,
        (fern, crozier): (&str, &str),
        runtime: (&str, &str),
    ) -> crate::parity::FileComparison {
        let module = |value: &str, code: &str| {
            format!(
                "class Client:\n    def read(self) -> None:\n        \"\"\"\n        Examples\n        \
                 --------\n        from api import Api\n\n        client = Api()\n        \
                 client.read(\n            {value}\n        )\n        \"\"\"\n        {code}\n"
            )
        };
        let context = Context::default()
            .with_source_document(serde_json::from_value(source.clone()).expect("a source"));
        crate::parity::compare_file(
            &context,
            "src/api/client.py",
            &module(crozier, runtime.1),
            &module(fern, runtime.0),
        )
        .expect("the comparison runs")
    }

    /// One document declaring `schema` as the property `field` of a body model.
    fn rejected_example_source(field: &str, schema: serde_json::Value) -> serde_json::Value {
        serde_json::json!({
            "openapi": "3.1.0",
            "info": {"title": "Api", "version": "1"},
            "paths": {},
            "components": {"schemas": {"Body": {
                "type": "object",
                "properties": {field: schema}
            }}}
        })
    }

    #[test]
    fn a_wrapped_one_item_repair_holds_only_in_an_example_and_only_for_the_repair() {
        let schema = serde_json::json!({"type": "array",
            "items": {"type": "string", "pattern": "^[a-f]{64}$"}});
        let repaired = "a".repeat(64);
        let docstring = |argument: &str| {
            format!("        \"\"\"\n        Examples\n        --------\n        client.post_check(\n{argument}        )\n        \"\"\"\n")
        };
        let runtime = |argument: &str| format!("        client.post_check(\n{argument}        )\n");
        let fern_arg = "            addresses=[\"addresses\"],\n";
        let wrapped =
            format!("            addresses=[\n                \"{repaired}\"\n            ],\n");
        let compare = |source: serde_json::Value, crozier: String, fern: String| {
            let context = Context::default()
                .with_source_document(serde_json::from_value(source).expect("a document"));
            crate::parity::compare_file(&context, "src/fern/batch/client.py", &crozier, &fern)
                .unwrap()
        };
        let source_again = || rejected_example_source("addresses", schema.clone());
        let source = source_again();
        let held = compare(source.clone(), docstring(&wrapped), docstring(fern_arg));
        assert!(held.residual.is_none(), "{held:?}");
        assert!(held
            .departures
            .iter()
            .any(|found| found.id == "schema-rejected-name-example"));
        // The same lines as runtime code are no example.
        assert!(compare(source, runtime(&wrapped), runtime(fern_arg))
            .residual
            .is_some());
        // A wrapped value the schema's repair does not choose is no repair.
        let other = format!(
            "            addresses=[\n                \"{}\"\n            ],\n",
            "b".repeat(64)
        );
        assert!(
            compare(source_again(), docstring(&other), docstring(fern_arg))
                .residual
                .is_some()
        );
    }

    #[test]
    fn each_rejected_example_rule_accounts_for_its_repair_and_nothing_else() {
        let cases = [
            (
                "schema-rejected-name-example",
                rejected_example_source(
                    "guild_id",
                    serde_json::json!({"type": "string", "pattern": "^(0|[1-9][0-9]*)$"}),
                ),
                ("guild_id=\"guild_id\",", "guild_id=\"0\","),
                "guild_id=\"guild\",",
                ("guild_id=\"7\",", "guild_id=\"abc\","),
            ),
            (
                "schema-rejected-number-example",
                rejected_example_source(
                    "count",
                    serde_json::json!({"type": "integer", "minimum": 5}),
                ),
                ("count=1,", "count=5,"),
                "count=-1,",
                ("count=6,", "count=2,"),
            ),
            (
                "schema-rejected-placeholder-string-example",
                rejected_example_source(
                    "labels",
                    serde_json::json!({"type": "object",
                        "additionalProperties": {"type": "string", "format": "uuid"}}),
                ),
                (
                    "labels={\"key\": \"value\"},",
                    "labels={\"key\": \"d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32\"},",
                ),
                "labels={\"key\": \"not-a-uuid\"},",
                (
                    "labels={\"key\": \"00000000-0000-4000-8000-000000000000\"},",
                    "labels={\"key\": \"nope\"},",
                ),
            ),
            (
                "schema-rejected-array-length-example",
                rejected_example_source(
                    "tags",
                    serde_json::json!({"type": "array", "minItems": 4,
                        "items": {"type": "string"}}),
                ),
                (
                    "tags=[\"tags\"],",
                    "tags=[\"tags\", \"tags\", \"tags\", \"tags\"],",
                ),
                "tags=[\"tags\", \"tags\"],",
                (
                    "tags=[\"tags\", \"tags\", \"tags\", \"tags\", \"tags\"],",
                    "tags=[\"tags\", \"tags\", \"tags\"],",
                ),
            ),
            (
                "schema-rejected-declared-example",
                rejected_example_source(
                    "share",
                    serde_json::json!({"type": "number", "maximum": 1, "example": 42}),
                ),
                ("share=42,", "share=1,"),
                "share=5,",
                ("share=0.5,", "share=7,"),
            ),
            (
                "schema-rejected-array-length-example",
                rejected_example_source(
                    "bounds",
                    serde_json::json!({"type": "array", "minItems": 2, "maxItems": 2,
                        "items": false,
                        "prefixItems": [{"type": "number"}, {"type": "string", "enum": ["x", "y"]}]}),
                ),
                ("bounds=[],", "bounds=[1.1, \"x\"],"),
                "bounds=[1.1],",
                ("bounds=[2.5, \"y\"],", "bounds=[1.1, 1.1, 1.1],"),
            ),
            (
                "schema-rejected-sized-string-example",
                rejected_example_source(
                    "code",
                    serde_json::json!({"type": "string", "minLength": 7, "pattern": "^[0-9]+$"}),
                ),
                ("code=\"apricot\",", "code=\"0000000\","),
                "code=\"abcdefg\",",
                ("code=\"1234567\",", "code=\"abcdefg\","),
            ),
        ];
        for (id, source, (fern, crozier), rejected, (other_valid, unconstructed)) in cases {
            // The repair is the rule's departure, and the only one.
            let compared = rejected_example_comparison(&source, (fern, crozier), ("pass", "pass"));
            assert!(compared.matches(), "{id}: {:?}", compared.diff());
            assert_eq!(
                compared.departures.iter().map(|d| d.id).collect::<Vec<_>>(),
                [id],
                "{id}"
            );
            // A replacement the schema itself rejects is no repair.
            let compared = rejected_example_comparison(&source, (fern, rejected), ("pass", "pass"));
            assert!(!compared.matches(), "{id}: {rejected} was accepted");
            // Nor one the schema accepts that its repair does not choose.
            let compared =
                rejected_example_comparison(&source, (fern, other_valid), ("pass", "pass"));
            assert!(!compared.matches(), "{id}: {other_valid} was not chosen");
            // Nor a rejected Fern value its construction does not give.
            let compared =
                rejected_example_comparison(&source, (unconstructed, crozier), ("pass", "pass"));
            assert!(
                !compared.matches(),
                "{id}: Fern never writes {unconstructed}"
            );
            // Nor is any change to a value the schema accepts.
            let permissive = rejected_example_source(
                source["components"]["schemas"]["Body"]["properties"]
                    .as_object()
                    .and_then(|properties| properties.keys().next())
                    .expect("one property"),
                serde_json::json!({"type": "object", "additionalProperties": true}),
            );
            let compared =
                rejected_example_comparison(&permissive, (fern, crozier), ("pass", "pass"));
            assert!(!compared.matches(), "{id}: an accepted value was replaced");
            // Nor the same change outside the documented example.
            let compared = rejected_example_comparison(
                &source,
                (fern, fern),
                (fern.trim_end_matches(','), crozier.trim_end_matches(',')),
            );
            assert!(!compared.matches(), "{id}: a runtime line was excused");
            // Nor without the source document to validate against.
            let compared = rejected_example_comparison(
                &serde_json::json!({"openapi": "3.1.0", "info": {"title": "Api", "version": "1"},
                    "paths": {}}),
                (fern, crozier),
                ("pass", "pass"),
            );
            assert!(!compared.matches(), "{id}: excused without its schema");
        }
    }

    /// An empty list crozier seeds with a model it constructs brings that
    /// model into the example's import, wrapped or not; an import adding a
    /// name no seeded list writes is no repair.
    #[test]
    fn a_seeded_list_s_model_import_is_the_array_departure_s_and_nothing_else() {
        let source = serde_json::json!({
            "openapi": "3.1.0",
            "info": {"title": "Api", "version": "1"},
            "paths": {},
            "components": {"schemas": {"Filter": {"type": "object", "properties": {
                "all": {"type": "array", "minItems": 1, "items": {"anyOf": [
                    {"$ref": "#/components/schemas/Filter"},
                    {"type": "object", "required": ["field"],
                        "properties": {"field": {"type": "string"}}}
                ]}}
            }}}}
        });
        let module = |import: &str, call: &str| {
            format!(
                "class Client:\n    def read(self) -> None:\n        \"\"\"\n        Examples\n        \
                 --------\n{import}\n\n        client = Api()\n        client.read(\n{call}        )\n        \
                 \"\"\"\n        pass\n"
            )
        };
        let fern_call = "            filter=Filter(\n                all_=[],\n            ),\n";
        let crozier_call = "            filter=Filter(\n                all_=[\n                    \
                            FilterAllItem(\n                        field=\"string\",\n                    \
                            )\n                ],\n            ),\n";
        let fern_import = "        from api import Api, Filter";
        let compare = |import: &str, call: &str| {
            let context = Context::default()
                .with_source_document(serde_json::from_value(source.clone()).expect("a source"));
            crate::parity::compare_file(
                &context,
                "src/api/client.py",
                &module(import, call),
                &module(fern_import, fern_call),
            )
            .expect("the comparison runs")
        };
        for import in [
            "        from api import Api, Filter, FilterAllItem",
            "        from api import (\n            Api,\n            Filter,\n            FilterAllItem,\n        )",
        ] {
            let compared = compare(import, crozier_call);
            assert!(compared.matches(), "{import}: {:?}", compared.diff());
            assert!(compared
                .departures
                .iter()
                .all(|found| found.id == "schema-rejected-array-length-example"));
        }
        // A name the seeded list does not construct, or one Fern's import loses.
        for import in [
            "        from api import Api, Filter, FilterAllItem, Other",
            "        from api import Api, FilterAllItem",
        ] {
            assert!(!compare(import, crozier_call).matches(), "{import}");
        }
        // Nor without a seeded list to construct the name.
        assert!(!compare(
            "        from api import Api, Filter, FilterAllItem",
            fern_call
        )
        .matches());
    }

    /// A list `reference.md` spreads over lines: only its added items are the
    /// array departure's region, so its first item's repair stays a line of
    /// its own; distinct padding under `uniqueItems` is the item schema's own.
    #[test]
    fn a_list_over_several_lines_is_padded_by_its_added_items_alone() {
        let source = serde_json::json!({
            "openapi": "3.1.0",
            "info": {"title": "Api", "version": "1"},
            "paths": {},
            "components": {"schemas": {"Body": {"type": "object", "properties": {
                "ids": {"type": "array", "minItems": 2, "uniqueItems": true,
                    "items": {"type": "string", "pattern": "^(0|[1-9][0-9]*)$"}}
            }}}}
        });
        let page = |items: &[&str]| {
            let mut lines = vec![
                "```python".to_string(),
                "client.read(".to_string(),
                "    ids=[".to_string(),
            ];
            let last = items.len() - 1;
            for (index, item) in items.iter().enumerate() {
                lines.push(format!(
                    "        {item}{}",
                    if index < last { "," } else { "" }
                ));
            }
            lines.extend([
                "    ],".to_string(),
                ")".to_string(),
                "```".to_string(),
                String::new(),
            ]);
            lines.join("\n")
        };
        let context = Context::default()
            .with_source_document(serde_json::from_value(source).expect("a source"));
        let compare = |crozier: &[&str]| {
            crate::parity::compare_file(
                &context,
                "reference.md",
                &page(crozier),
                &page(&["\"ids\""]),
            )
            .expect("the comparison runs")
        };
        let compared = compare(&["\"0\"", "\"1\""]);
        assert!(compared.matches(), "{:?}", compared.diff());
        assert_eq!(
            compared
                .departures
                .iter()
                .map(|d| (d.line.get(), d.id))
                .collect::<Vec<_>>(),
            [(4, "schema-rejected-array-length-example")]
        );
        // A repeated item, or a distinct one the item schema rejects, is not
        // the padding a `uniqueItems` list takes.
        let dup = compare(&["\"0\"", "\"0\""]);
        assert!(!dup.matches(), "{:?}", dup.departures);
        assert!(!compare(&["\"0\"", "\"x\""]).matches());
    }

    /// A repair the source indexes for one argument excuses the same change at
    /// no other: an unrelated number, map value or list keeps failing.
    #[test]
    fn a_repair_indexed_for_one_argument_excuses_no_other() {
        let source = serde_json::json!({
            "openapi": "3.1.0",
            "info": {"title": "Api", "version": "1"},
            "paths": {},
            "components": {"schemas": {"Body": {"type": "object", "properties": {
                "count": {"type": "integer", "minimum": 5},
                "other": {"type": "integer"},
                "labels": {"type": "object",
                    "additionalProperties": {"type": "string", "format": "uuid"}},
                "notes": {"type": "object", "additionalProperties": {"type": "string"}},
                "tags": {"type": "array", "minItems": 3, "items": {"type": "string"}},
                "names": {"type": "array", "items": {"type": "string"}}
            }}}}
        });
        let uuid = "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32";
        let labels = format!("labels={{\"key\": \"{uuid}\"}},");
        let notes = format!("notes={{\"key\": \"{uuid}\"}},");
        for ((own_fern, own_crozier), (other_fern, other_crozier)) in [
            (("count=1,", "count=5,"), ("other=1,", "other=5,")),
            (
                ("labels={\"key\": \"value\"},", labels.as_str()),
                ("notes={\"key\": \"value\"},", notes.as_str()),
            ),
            (
                ("tags=[\"tags\"],", "tags=[\"tags\", \"tags\", \"tags\"],"),
                (
                    "names=[\"names\"],",
                    "names=[\"names\", \"names\", \"names\"],",
                ),
            ),
        ] {
            let own =
                rejected_example_comparison(&source, (own_fern, own_crozier), ("pass", "pass"));
            assert!(own.matches(), "{own_crozier}: {:?}", own.diff());
            let other =
                rejected_example_comparison(&source, (other_fern, other_crozier), ("pass", "pass"));
            assert!(
                !other.matches(),
                "{other_crozier} was excused by another argument's repair"
            );
        }
    }

    /// `Sighting` maps `METEOR` to a target naming no component, and
    /// `MeteorReading`, the member no target names, tags itself `METEOR`.
    fn dangling_mapping_source(meteor_target: &str) -> crate::openapi::OpenApi {
        serde_json::from_value(serde_json::json!({
            "openapi": "3.0.3",
            "info": {"title": "t", "version": "1"},
            "paths": {},
            "components": {"schemas": {
                "Sighting": {
                    "discriminator": {"propertyName": "kind", "mapping": {
                        "STAR": "#/components/schemas/StarReading",
                        "METEOR": meteor_target
                    }},
                    "oneOf": [
                        {"$ref": "#/components/schemas/StarReading"},
                        {"$ref": "#/components/schemas/MeteorReading"}
                    ]
                },
                "StarReading": {"type": "object", "properties": {
                    "kind": {"type": "string", "enum": ["STAR"]}
                }},
                "MeteorReading": {"type": "object", "properties": {
                    "trail": {"$ref": "#/components/schemas/Trail"},
                    "kind": {"type": "string", "enum": ["METEOR"]}
                }},
                "Trail": {"type": "object", "properties": {"degrees": {"type": "number"}}}
            }}
        }))
        .expect("a source document")
    }

    const DANGLING_FERN: &str = r#"import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class Sighting_Meteor(UniversalBaseModel):
    value: typing.Any
    kind: typing.Literal["METEOR"] = "METEOR"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
"#;

    const DANGLING_CROZIER: &str = r#"import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .trail import Trail


class Sighting_Meteor(UniversalBaseModel):
    """
    One sighting.
    """

    kind: typing.Literal["METEOR"] = "METEOR"
    trail: typing.Optional["Trail"] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(
    Sighting_Meteor,
    Trail=Trail,
)
"#;

    #[test]
    fn dangling_mapping_variant_fields_holds_on_the_wrapper_and_nowhere_else() {
        let rel = "src/fern/types/sighting.py";
        let with =
            |target: &str| Context::default().with_source_document(dangling_mapping_source(target));
        let dangling = with("#/components/schemas/meteor-reading");
        let crozier_lines = DANGLING_CROZIER.split('\n').count();
        assert_eq!(
            region_of(
                dangling_mapping_variant_fields,
                rel,
                DANGLING_FERN,
                DANGLING_CROZIER,
                &dangling
            ),
            Some(Region {
                fern: 0..DANGLING_FERN.split('\n').count(),
                crozier: 0..crozier_lines,
            })
        );
        // Without the source document, or where the mapping names the member
        // by reference, the rule abstains.
        assert_eq!(
            region_of(
                dangling_mapping_variant_fields,
                rel,
                DANGLING_FERN,
                DANGLING_CROZIER,
                &Context::default()
            ),
            None
        );
        let resolved = with("#/components/schemas/MeteorReading");
        assert_eq!(
            region_of(
                dangling_mapping_variant_fields,
                rel,
                DANGLING_FERN,
                DANGLING_CROZIER,
                &resolved
            ),
            None
        );
        // Any other difference in the file is still a difference.
        let drifted = DANGLING_CROZIER.replace("import pydantic\n", "import pydantic  \n");
        assert_eq!(
            region_of(
                dangling_mapping_variant_fields,
                rel,
                DANGLING_FERN,
                &drifted,
                &dangling
            ),
            None
        );
        // An import the rewritten file still uses stays: Fern's file must have it.
        let still_used = DANGLING_CROZIER.replace(
            "update_forward_refs(\n    Sighting_Meteor,",
            "Default = Trail\nupdate_forward_refs(\n    Sighting_Meteor,",
        );
        assert_eq!(
            region_of(
                dangling_mapping_variant_fields,
                rel,
                DANGLING_FERN,
                &still_used,
                &dangling
            ),
            None
        );
        // Nor are fields other than the member's: the departure is its fields.
        let renamed = DANGLING_CROZIER.replace("    trail:", "    path:");
        assert_eq!(
            region_of(
                dangling_mapping_variant_fields,
                rel,
                DANGLING_FERN,
                &renamed,
                &dangling
            ),
            None
        );
        // A wrapper whose tag is not the mapping's value is not the construct.
        let other_tag = DANGLING_CROZIER.replace("\"METEOR\"", "\"COMET\"");
        assert_eq!(
            region_of(
                dangling_mapping_variant_fields,
                rel,
                DANGLING_FERN,
                &other_tag,
                &dangling
            ),
            None
        );
        // Nor is a file that ends at the wrapper's header.
        let truncated = DANGLING_CROZIER
            .split_once("class Sighting_Meteor(UniversalBaseModel):")
            .map(|(head, _)| format!("{head}class Sighting_Meteor(UniversalBaseModel):"))
            .unwrap();
        assert_eq!(
            region_of(
                dangling_mapping_variant_fields,
                rel,
                DANGLING_FERN,
                &truncated,
                &dangling
            ),
            None
        );
        // Nor is a file other than Python.
        assert_eq!(
            region_of(
                dangling_mapping_variant_fields,
                "reference.md",
                DANGLING_FERN,
                DANGLING_CROZIER,
                &dangling
            ),
            None
        );
    }

    /// A document whose root `security` is `[]` beside one secured and one
    /// unsecured operation, with `own` as the unsecured operation's own
    /// `security` (absent when `None`) and `root` as the root's.
    fn empty_root_security_source(
        root: Option<serde_json::Value>,
        own: Option<serde_json::Value>,
    ) -> serde_json::Value {
        let mut open = serde_json::json!({"responses": {"200": {"description": "ok"}}});
        if let Some(own) = own {
            open["security"] = own;
        }
        let mut document = serde_json::json!({
            "openapi": "3.1.0",
            "info": {"title": "Api", "version": "1"},
            "paths": {
                "/ping": {"get": open},
                "/vault": {"get": {
                    "security": [{"key": []}],
                    "responses": {"200": {"description": "ok"}}
                }}
            },
            "components": {"securitySchemes": {
                "key": {"type": "apiKey", "in": "header", "name": "x-api-key"}
            }}
        });
        if let Some(root) = root {
            document["security"] = root;
        }
        document
    }

    const CREDENTIAL_WRAPPER_FERN: &str = "class BaseClientWrapper:\n    def __init__(\n        self,\n        *,\n        api_key: str,\n        base_url: str,\n    ):\n        self.api_key = api_key\n\n    def get_headers(self) -> typing.Dict[str, str]:\n        headers: typing.Dict[str, str] = {}\n        headers[\"x-api-key\"] = self.api_key\n        return headers\n";
    const CREDENTIAL_WRAPPER_CROZIER: &str = "class BaseClientWrapper:\n    def __init__(\n        self,\n        *,\n        api_key: typing.Optional[str] = None,\n        base_url: str,\n    ):\n        self.api_key = api_key\n\n    def get_headers(self) -> typing.Dict[str, str]:\n        headers: typing.Dict[str, str] = {}\n        if self.api_key is not None:\n            headers[\"x-api-key\"] = self.api_key\n        return headers\n";

    fn credential_wrapper_comparison(
        source: serde_json::Value,
        crozier: &str,
    ) -> crate::parity::FileComparison {
        let context = Context::default()
            .with_source_document(serde_json::from_value(source).expect("a source"));
        crate::parity::compare_file(
            &context,
            "src/fern/core/client_wrapper.py",
            crozier,
            CREDENTIAL_WRAPPER_FERN,
        )
        .expect("the comparison runs")
    }

    #[test]
    fn an_empty_root_security_list_excuses_only_its_optional_credential() {
        let covered = empty_root_security_source(Some(serde_json::json!([])), None);
        let comparison = credential_wrapper_comparison(covered.clone(), CREDENTIAL_WRAPPER_CROZIER);
        assert!(comparison.matches(), "{:?}", comparison.residual);
        let ids: Vec<&str> = comparison
            .departures
            .iter()
            .map(|departure| departure.id)
            .collect();
        assert_eq!(ids, ["empty-root-security-optional-credential"; 2]);

        // An absent root `security`, or an operation's own empty list, makes
        // the certified pair's credential optional too: nothing to excuse.
        for uncovered in [
            empty_root_security_source(None, None),
            empty_root_security_source(Some(serde_json::json!([])), Some(serde_json::json!([]))),
            empty_root_security_source(
                Some(serde_json::json!([])),
                Some(serde_json::json!([{"key": []}])),
            ),
        ] {
            assert!(
                !credential_wrapper_comparison(uncovered, CREDENTIAL_WRAPPER_CROZIER).matches()
            );
        }

        // An adjacent credential mismatch the departure does not describe
        // still fails: another type, another default, another header value,
        // or a guard on another attribute.
        for (from, to) in [
            (
                "api_key: typing.Optional[str] = None,",
                "api_key: typing.Optional[int] = None,",
            ),
            (
                "api_key: typing.Optional[str] = None,",
                "api_key: typing.Optional[str] = \"\",",
            ),
            (
                "            headers[\"x-api-key\"] = self.api_key",
                "            headers[\"x-api-key\"] = self.api_key.strip()",
            ),
            ("if self.api_key is not None:", "if self.token is not None:"),
        ] {
            let crozier = CREDENTIAL_WRAPPER_CROZIER.replacen(from, to, 1);
            assert_ne!(crozier, CREDENTIAL_WRAPPER_CROZIER, "{to}");
            assert!(
                !credential_wrapper_comparison(covered.clone(), &crozier).matches(),
                "{to} was excused"
            );
        }

        // The root client's constructor and docstring lines, never a
        // sub-client's.
        let context = source_context(covered, &[]);
        let rule: LineRule = empty_root_security_optional_credential;
        for (fern, crozier) in [
            (
                "        api_key: str,",
                "        api_key: typing.Optional[str] = None,",
            ),
            ("    api_key : str", "    api_key : typing.Optional[str]"),
        ] {
            assert!(line_holds(
                rule,
                "src/fern/client.py",
                &context,
                fern,
                crozier
            ));
            assert!(!line_holds(
                rule,
                "src/fern/catalog/client.py",
                &context,
                fern,
                crozier
            ));
            assert!(!line_holds(
                rule,
                "src/fern/client.py",
                &context,
                fern,
                &crozier.replacen("api_key", "token", 1)
            ));
        }
    }
}
