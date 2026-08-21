//! Resolving `$ref`s that point at another document over HTTP(S).
//!
//! Most OpenAPI documents are self-contained: every `$ref` is a local JSON
//! pointer into the same file. Some are not — a spec may name a schema in a
//! second document by absolute URL, and Fern's importer *fetches* that document
//! and resolves the pointer into it before generating. Matching Fern byte for
//! byte therefore means opening the second document too, so this module runs as
//! a load-time pass over the parsed document: every remote `$ref` node is
//! replaced, in place, by the schema the referenced document declares.
//!
//! Three rules follow from what Fern was measured to do (see the
//! `helios-verifiable-api` corpus row, whose 27 component schemas are all remote
//! references into `ethereum/execution-apis`):
//!
//! - **Resolution is transitive.** A fetched schema may itself carry a remote
//!   `$ref`, which is fetched in turn.
//! - **A local pointer inside a fetched schema stays local to the *root*
//!   document.** The referenced documents are schema fragments assembled by the
//!   root, so their `#/components/schemas/…` pointers are left untouched and
//!   resolve against the root's `components` like any other local ref — and, as
//!   with any unresolvable local ref, a name the root does not declare degrades
//!   to the unknown type rather than failing generation.
//! - **A fetch that fails is a hard error.** A silently dropped schema would
//!   generate a plausible SDK with the wrong types in it.
//!
//! Fetching is a *generation-time* capability, exercised only by a document that
//! actually carries a remote `$ref`; a self-contained spec never opens a socket.
//! It runs through `curl`, the same shell-out shape [`crate::pyfmt`] uses for
//! `ruff` — crozier ships one static binary and a TLS stack in-process would be a
//! large supply-chain addition for a rarely-taken path, so a missing `curl`
//! surfaces as an actionable [`Error::RemoteRef`] instead. The fetcher is a
//! trait so the resolution rules above are unit-testable without a network.

use std::collections::HashMap;
use std::path::Path;
use std::process::Command;

use crate::error::{Error, Result};
use crate::openapi::{
    for_each_root_schema, for_each_schema_in, referenced_component_schema, AdditionalProperties,
    OpenApi, Schema,
};

/// How long `curl` may spend on one referenced document before crozier gives up
/// with an actionable error rather than hanging a generation run.
const FETCH_TIMEOUT_SECONDS: u32 = 60;

/// Fetches a referenced document's text by absolute URL.
///
/// Injected into [`resolve`] so the resolution rules can be tested against
/// in-memory documents; production uses [`CurlFetcher`].
pub trait RemoteFetcher {
    /// Return the document at `url`, or a human-readable reason it could not be
    /// retrieved. The reason is surfaced verbatim in [`Error::RemoteRef`].
    fn fetch(&self, url: &str) -> std::result::Result<String, String>;
}

/// The production fetcher: `curl --fail --location`, one process per document.
pub struct CurlFetcher;

impl RemoteFetcher for CurlFetcher {
    fn fetch(&self, url: &str) -> std::result::Result<String, String> {
        curl_fetch(CURL, url)
    }
}

/// The program [`CurlFetcher`] runs. Named so the tests can drive the same
/// invocation against a program that is not installed.
const CURL: &str = "curl";

fn curl_fetch(program: &str, url: &str) -> std::result::Result<String, String> {
    let output = Command::new(program)
        .arg("--silent")
        .arg("--show-error")
        // Fail loudly on a 4xx/5xx instead of writing the error page into the
        // spec, and follow redirects the way an importer is expected to.
        .arg("--fail")
        .arg("--location")
        .arg("--max-time")
        .arg(FETCH_TIMEOUT_SECONDS.to_string())
        // `--` so a URL beginning with `-` can never be read as an option.
        .arg("--")
        .arg(url)
        .output()
        .map_err(|error| match error.kind() {
            std::io::ErrorKind::NotFound => "`curl` was not found on PATH; install it — \
                     crozier fetches documents named by an absolute-URL `$ref` with curl"
                .to_string(),
            _ => format!("could not run `curl`: {error}"),
        })?;
    if !output.status.success() {
        return Err(format!(
            "curl failed ({}): {}",
            output.status,
            String::from_utf8_lossy(&output.stderr).trim()
        ));
    }
    String::from_utf8(output.stdout).map_err(|error| format!("not valid UTF-8: {error}"))
}

/// Replace every remote `$ref` in `doc` with the schema it names, fetching each
/// referenced document at most once. `spec` names the document being loaded, for
/// error messages. A document with no remote `$ref` fetches nothing.
pub fn resolve(doc: &mut OpenApi, fetcher: &dyn RemoteFetcher, spec: &Path) -> Result<()> {
    let mut resolver = Resolver {
        fetcher,
        spec,
        documents: HashMap::new(),
        active: Vec::new(),
    };
    register_component_schemas(doc, &mut resolver)?;
    let mut failure = None;
    for_each_root_schema(doc, &mut |schema| {
        if failure.is_none() {
            if let Err(error) = resolver.resolve_schema(schema) {
                failure = Some(error);
            }
        }
    });
    match failure {
        Some(error) => Err(error),
        None => Ok(()),
    }
}

/// Register the component schemas a remote `$ref` names — under the *pointer's*
/// name, not the local key.
///
/// Fern names a fetched schema after the pointer it came from and leaves the
/// local key as an alias to it. The two coincide for most references
/// (`address: $ref …#/address` declares `address`), and where they differ
/// (`TransactionReceipt: $ref …#/ReceiptInfo`) the document gains a
/// `ReceiptInfo` schema and `TransactionReceipt` becomes `$ref
/// #/components/schemas/ReceiptInfo` — which, being a bare alias, is transparent
/// at every other reference site (see `normalize_schema_aliases`).
///
/// A pointer name the document already uses keeps the schema in place under the
/// local key rather than silently rebinding an existing name.
fn register_component_schemas(doc: &mut OpenApi, resolver: &mut Resolver) -> Result<()> {
    let names: Vec<String> = doc.components.schemas.keys().cloned().collect();
    let mut fetched: Vec<(String, Schema)> = Vec::new();
    let mut renamed: Vec<(String, String)> = Vec::new();
    for name in names {
        let Some(reference) = doc.components.schemas[&name].reference.clone() else {
            continue;
        };
        let Some((_, fragment)) = split_remote(&reference) else {
            continue;
        };
        let target = fragment.rsplit('/').next().unwrap_or_default().to_string();
        let resolved = resolver.resolve_reference(&reference)?;
        if target.is_empty()
            || target == name
            || doc.components.schemas.contains_key(&target)
            || fetched.iter().any(|(taken, _)| *taken == target)
        {
            doc.components.schemas[&name] = resolved;
        } else {
            doc.components.schemas[&name] = Schema {
                reference: Some(format!("#/components/schemas/{target}")),
                ..Schema::default()
            };
            renamed.push((name, target.clone()));
            fetched.push((target, resolved));
        }
    }
    doc.components.schemas.extend(fetched);
    rename_references(doc, &renamed);
    Ok(())
}

/// Point every reference at the name the fetched schema was registered under.
///
/// The local key keeps its own declaration — `TransactionReceipt = ReceiptInfo`
/// — but it is the fetched name that the rest of the SDK is generated against,
/// so the two agree on which class each reference means. The alias declarations
/// themselves already point at their target and so are left alone.
fn rename_references(doc: &mut OpenApi, renamed: &[(String, String)]) {
    if renamed.is_empty() {
        return;
    }
    for_each_root_schema(doc, &mut |schema| {
        for_each_schema_in(schema, &mut |node| {
            let Some(reference) = node.reference.as_deref() else {
                return;
            };
            let Some(name) = referenced_component_schema(reference) else {
                return;
            };
            let Some((_, target)) = renamed.iter().find(|(from, _)| from == name) else {
                return;
            };
            let suffix = &reference["#/components/schemas/".len() + name.len()..];
            node.reference = Some(format!("#/components/schemas/{target}{suffix}"));
        });
    });
}

/// The URL and JSON-pointer fragment of a `$ref` that names another document
/// over HTTP(S), or `None` for a local pointer. Only `http`/`https` qualify, so
/// no other URL scheme can reach the fetcher.
fn split_remote(reference: &str) -> Option<(&str, &str)> {
    if !(reference.starts_with("http://") || reference.starts_with("https://")) {
        return None;
    }
    Some(match reference.split_once('#') {
        Some((url, fragment)) => (url, fragment),
        None => (reference, ""),
    })
}

/// One load's resolution state: the fetcher, the documents already retrieved,
/// and the references currently being resolved (for cycle detection).
struct Resolver<'a> {
    fetcher: &'a dyn RemoteFetcher,
    spec: &'a Path,
    documents: HashMap<String, serde_yaml_ng::Value>,
    active: Vec<String>,
}

impl Resolver<'_> {
    /// Resolve `schema` in place, then every schema nested inside it.
    fn resolve_schema(&mut self, schema: &mut Schema) -> Result<()> {
        if let Some(reference) = schema.reference.clone() {
            if split_remote(&reference).is_some() {
                *schema = self.resolve_reference(&reference)?;
                return Ok(());
            }
        }
        for property in schema.properties.values_mut() {
            self.resolve_schema(property)?;
        }
        if let Some(items) = &mut schema.items {
            self.resolve_schema(items)?;
        }
        if let Some(AdditionalProperties::Schema(value)) = &mut schema.additional_properties {
            self.resolve_schema(value)?;
        }
        for members in [&mut schema.one_of, &mut schema.any_of, &mut schema.all_of] {
            for member in members.iter_mut().flatten() {
                self.resolve_schema(member)?;
            }
        }
        Ok(())
    }

    /// Fetch, locate and fully resolve the schema `reference` names.
    fn resolve_reference(&mut self, reference: &str) -> Result<Schema> {
        // A reference cycle across documents has no name to emit, so it degrades
        // to the unknown type — the same shape an unresolvable local pointer
        // takes — rather than recursing forever.
        if self.active.iter().any(|active| active == reference) {
            return Ok(Schema::default());
        }
        let (url, fragment) =
            split_remote(reference).expect("caller checked the reference is remote");
        let node = pointer(self.document(url, reference)?, fragment).cloned();
        let node = node.ok_or_else(|| {
            self.error(
                reference,
                "the referenced document has no node at that pointer",
            )
        })?;
        let mut resolved: Schema = serde_yaml_ng::from_value(node)
            .map_err(|error| self.error(reference, &format!("not a schema: {error}")))?;
        self.active.push(reference.to_string());
        let nested = self.resolve_schema(&mut resolved);
        self.active.pop();
        nested?;
        Ok(resolved)
    }

    /// The parsed document at `url`, fetched once per load. YAML is a superset of
    /// JSON, so one parser reads both `.yaml` and `.json` references.
    fn document(&mut self, url: &str, reference: &str) -> Result<&serde_yaml_ng::Value> {
        if !self.documents.contains_key(url) {
            let text = self
                .fetcher
                .fetch(url)
                .map_err(|message| self.error(reference, &message))?;
            let value = serde_yaml_ng::from_str(&text)
                .map_err(|error| self.error(reference, &format!("could not parse it: {error}")))?;
            self.documents.insert(url.to_string(), value);
        }
        Ok(&self.documents[url])
    }

    fn error(&self, reference: &str, message: &str) -> Error {
        Error::RemoteRef {
            path: self.spec.to_path_buf(),
            reference: reference.to_string(),
            message: message.to_string(),
        }
    }
}

/// Walk a JSON pointer (RFC 6901) into a parsed document. An empty pointer is
/// the document itself.
fn pointer<'a>(
    document: &'a serde_yaml_ng::Value,
    fragment: &str,
) -> Option<&'a serde_yaml_ng::Value> {
    let mut node = document;
    for segment in fragment.split('/').skip_while(|segment| segment.is_empty()) {
        let key = segment.replace("~1", "/").replace("~0", "~");
        node = match node {
            serde_yaml_ng::Value::Mapping(map) => map.get(serde_yaml_ng::Value::from(key))?,
            serde_yaml_ng::Value::Sequence(items) => items.get(key.parse::<usize>().ok()?)?,
            _ => return None,
        };
    }
    Some(node)
}

#[cfg(test)]
mod tests {
    use super::*;

    /// A fetcher backed by an in-memory URL → document map, recording what was
    /// asked for so the tests can assert each document is fetched once.
    struct FakeFetcher {
        documents: HashMap<String, String>,
        fetched: std::cell::RefCell<Vec<String>>,
    }

    impl FakeFetcher {
        fn new(documents: &[(&str, &str)]) -> Self {
            Self {
                documents: documents
                    .iter()
                    .map(|(url, body)| ((*url).to_string(), (*body).to_string()))
                    .collect(),
                fetched: std::cell::RefCell::new(Vec::new()),
            }
        }
    }

    impl RemoteFetcher for FakeFetcher {
        fn fetch(&self, url: &str) -> std::result::Result<String, String> {
            self.fetched.borrow_mut().push(url.to_string());
            self.documents
                .get(url)
                .cloned()
                .ok_or_else(|| format!("no such document {url}"))
        }
    }

    fn parse(spec: &str) -> OpenApi {
        serde_yaml_ng::from_str(spec).expect("valid spec")
    }

    fn resolved(spec: &str, documents: &[(&str, &str)]) -> (OpenApi, Vec<String>) {
        let fetcher = FakeFetcher::new(documents);
        let mut doc = parse(spec);
        resolve(&mut doc, &fetcher, Path::new("spec.yml")).expect("resolvable spec");
        let fetched = fetcher.fetched.borrow().clone();
        (doc, fetched)
    }

    const REMOTE: &str = "https://example.test/schemas.yaml";

    #[test]
    fn a_component_schema_becomes_the_referenced_document_s_schema() {
        let (doc, fetched) = resolved(
            &format!(
                r#"
openapi: 3.0.0
components:
  schemas:
    address:
      $ref: {REMOTE}#/address
"#
            ),
            &[(REMOTE, "address:\n  type: string\n  pattern: '^0x'\n")],
        );
        let address = &doc.components.schemas["address"];
        assert_eq!(address.reference, None);
        assert_eq!(
            address.ty.as_ref().and_then(|t| t.primary()),
            Some("string")
        );
        assert_eq!(fetched, vec![REMOTE.to_string()]);
    }

    #[test]
    fn a_fetched_schema_takes_its_pointer_s_name_and_the_local_key_aliases_it() {
        let (doc, _) = resolved(
            &format!(
                r##"
openapi: 3.0.0
components:
  schemas:
    TransactionReceipt:
      $ref: {REMOTE}#/ReceiptInfo
    Receipts:
      type: array
      items:
        $ref: "#/components/schemas/TransactionReceipt"
"##
            ),
            &[(
                REMOTE,
                "ReceiptInfo:\n  type: object\n  properties:\n    status:\n      type: string\n",
            )],
        );
        // The fetched schema is declared under the name its pointer ends with...
        assert!(doc.components.schemas["ReceiptInfo"]
            .properties
            .contains_key("status"));
        // ...the local key stays as an alias to it...
        assert_eq!(
            doc.components.schemas["TransactionReceipt"]
                .reference
                .as_deref(),
            Some("#/components/schemas/ReceiptInfo")
        );
        // ...and every other reference to the local key names the fetched schema.
        assert_eq!(
            doc.components.schemas["Receipts"]
                .items
                .as_ref()
                .and_then(|items| items.reference.as_deref()),
            Some("#/components/schemas/ReceiptInfo")
        );
    }

    #[test]
    fn a_pointer_name_the_document_already_declares_keeps_the_schema_in_place() {
        let (doc, _) = resolved(
            &format!(
                r#"
openapi: 3.0.0
components:
  schemas:
    Alias:
      $ref: {REMOTE}#/Taken
    Taken:
      type: boolean
"#
            ),
            &[(REMOTE, "Taken:\n  type: string\n")],
        );
        assert_eq!(
            doc.components.schemas["Alias"]
                .ty
                .as_ref()
                .and_then(|t| t.primary()),
            Some("string")
        );
        assert_eq!(
            doc.components.schemas["Taken"]
                .ty
                .as_ref()
                .and_then(|t| t.primary()),
            Some("boolean")
        );
    }

    #[test]
    fn resolution_is_transitive_across_documents() {
        let other = "https://example.test/other.yaml";
        let (doc, fetched) = resolved(
            &format!(
                r#"
openapi: 3.0.0
components:
  schemas:
    wrapper:
      $ref: {REMOTE}#/wrapper
"#
            ),
            &[
                (REMOTE, &format!("wrapper:\n  $ref: {other}#/leaf\n")),
                (other, "leaf:\n  type: integer\n"),
            ],
        );
        assert_eq!(
            doc.components.schemas["wrapper"]
                .ty
                .as_ref()
                .and_then(|t| t.primary()),
            Some("integer")
        );
        assert_eq!(fetched, vec![REMOTE.to_string(), other.to_string()]);
    }

    #[test]
    fn each_referenced_document_is_fetched_once_however_many_refs_name_it() {
        let (doc, fetched) = resolved(
            &format!(
                r#"
openapi: 3.0.0
components:
  schemas:
    a:
      $ref: {REMOTE}#/a
    b:
      $ref: {REMOTE}#/b
    c:
      $ref: {REMOTE}#/a
"#
            ),
            &[(REMOTE, "a:\n  type: string\nb:\n  type: boolean\n")],
        );
        assert_eq!(doc.components.schemas.len(), 3);
        assert_eq!(fetched, vec![REMOTE.to_string()]);
    }

    #[test]
    fn a_local_pointer_inside_a_fetched_schema_is_left_for_the_root_document() {
        let (doc, _) = resolved(
            &format!(
                r#"
openapi: 3.0.0
components:
  schemas:
    addresses:
      $ref: {REMOTE}#/addresses
    Address:
      type: string
"#
            ),
            &[(
                REMOTE,
                "addresses:\n  type: array\n  items:\n    $ref: '#/components/schemas/Address'\n",
            )],
        );
        let items = doc.components.schemas["addresses"]
            .items
            .as_ref()
            .expect("array items");
        assert_eq!(
            items.reference.as_deref(),
            Some("#/components/schemas/Address")
        );
    }

    #[test]
    fn a_remote_ref_nested_in_a_composition_resolves() {
        let (doc, _) = resolved(
            &format!(
                r#"
openapi: 3.0.0
components:
  schemas:
    Either:
      oneOf:
        - $ref: {REMOTE}#/left
        - type: string
"#
            ),
            &[(REMOTE, "left:\n  type: number\n")],
        );
        let variants = doc.components.schemas["Either"]
            .one_of
            .as_ref()
            .expect("oneOf variants");
        assert_eq!(
            variants[0].ty.as_ref().and_then(|t| t.primary()),
            Some("number")
        );
    }

    #[test]
    fn remote_refs_resolve_in_parameters_bodies_and_responses() {
        let (doc, _) = resolved(
            &format!(
                r#"
openapi: 3.0.0
paths:
  /items:
    parameters:
      - name: shared
        in: query
        schema:
          $ref: {REMOTE}#/leaf
    post:
      parameters:
        - name: filter
          in: query
          schema:
            $ref: {REMOTE}#/leaf
      requestBody:
        content:
          application/json:
            schema:
              $ref: {REMOTE}#/leaf
      responses:
        "200":
          description: ok
          content:
            application/json:
              schema:
                $ref: {REMOTE}#/leaf
components:
  parameters:
    Reusable:
      name: reusable
      in: query
      schema:
        $ref: {REMOTE}#/leaf
  requestBodies:
    Body:
      content:
        application/json:
          schema:
            $ref: {REMOTE}#/leaf
  responses:
    Ok:
      description: ok
      content:
        application/json:
          schema:
            $ref: {REMOTE}#/leaf
"#
            ),
            &[(REMOTE, "leaf:\n  type: string\n")],
        );
        let item = &doc.paths["/items"];
        let is_leaf =
            |schema: &Schema| schema.ty.as_ref().and_then(|t| t.primary()) == Some("string");
        assert!(is_leaf(
            item.parameters[0]
                .schema
                .as_ref()
                .expect("path parameter schema")
        ));
        let post = item.post.as_ref().expect("post operation");
        assert!(is_leaf(
            post.parameters[0]
                .schema
                .as_ref()
                .expect("operation parameter schema")
        ));
        assert!(is_leaf(
            post.request_body.as_ref().expect("request body").content["application/json"]
                .schema
                .as_ref()
                .expect("body schema")
        ));
        assert!(is_leaf(
            post.responses["200"].content["application/json"]
                .schema
                .as_ref()
                .expect("response schema")
        ));
        assert!(is_leaf(
            doc.components.parameters["Reusable"]
                .schema
                .as_ref()
                .expect("component parameter schema")
        ));
        assert!(is_leaf(
            doc.components.request_bodies["Body"].content["application/json"]
                .schema
                .as_ref()
                .expect("component body schema")
        ));
        assert!(is_leaf(
            doc.components.responses["Ok"].content["application/json"]
                .schema
                .as_ref()
                .expect("component response schema")
        ));
    }

    #[test]
    fn a_remote_ref_inside_a_content_parameter_resolves() {
        let (doc, _) = resolved(
            &format!(
                r#"
openapi: 3.0.0
components:
  parameters:
    Query:
      name: query
      in: query
      content:
        application/json:
          schema:
            $ref: {REMOTE}#/leaf
"#
            ),
            &[(REMOTE, "leaf:\n  type: string\n")],
        );
        assert_eq!(
            doc.components.parameters["Query"].content["application/json"]
                .schema
                .as_ref()
                .and_then(|s| s.ty.as_ref())
                .and_then(|t| t.primary()),
            Some("string")
        );
    }

    #[test]
    fn a_reference_cycle_across_documents_degrades_to_the_unknown_type() {
        let (doc, _) = resolved(
            &format!(
                r#"
openapi: 3.0.0
components:
  schemas:
    node:
      $ref: {REMOTE}#/node
"#
            ),
            &[(
                REMOTE,
                &format!(
                    "node:\n  type: object\n  properties:\n    next:\n      $ref: {REMOTE}#/node\n"
                ),
            )],
        );
        let next = &doc.components.schemas["node"].properties["next"];
        assert_eq!(next.reference, None);
        assert_eq!(next.ty.as_ref().and_then(|t| t.primary()), None);
    }

    #[test]
    fn a_self_contained_document_fetches_nothing() {
        let (_, fetched) = resolved(
            r##"
openapi: 3.0.0
components:
  schemas:
    Local:
      $ref: "#/components/schemas/Other"
    Other:
      type: string
"##,
            &[],
        );
        assert!(fetched.is_empty(), "fetched {fetched:?}");
    }

    fn resolve_error(spec: &str, documents: &[(&str, &str)]) -> String {
        let fetcher = FakeFetcher::new(documents);
        let mut doc = parse(spec);
        resolve(&mut doc, &fetcher, Path::new("spec.yml"))
            .expect_err("unresolvable spec")
            .to_string()
    }

    #[test]
    fn a_document_that_cannot_be_fetched_is_an_actionable_error() {
        let message = resolve_error(
            &format!("openapi: 3.0.0\ncomponents:\n  schemas:\n    A:\n      $ref: {REMOTE}#/a\n"),
            &[],
        );
        assert!(message.contains(REMOTE), "{message}");
        assert!(message.contains("no such document"), "{message}");
        assert!(message.contains("spec.yml"), "{message}");
    }

    #[test]
    fn a_missing_pointer_in_a_fetched_document_is_an_actionable_error() {
        let message = resolve_error(
            &format!(
                "openapi: 3.0.0\ncomponents:\n  schemas:\n    A:\n      $ref: {REMOTE}#/missing\n"
            ),
            &[(REMOTE, "present:\n  type: string\n")],
        );
        assert!(message.contains("no node at that pointer"), "{message}");
    }

    #[test]
    fn a_document_that_is_not_parseable_is_an_actionable_error() {
        let message = resolve_error(
            &format!("openapi: 3.0.0\ncomponents:\n  schemas:\n    A:\n      $ref: {REMOTE}#/a\n"),
            &[(REMOTE, "a:\n  - unbalanced: [\n")],
        );
        assert!(message.contains("could not parse it"), "{message}");
    }

    #[test]
    fn a_pointer_at_a_non_schema_node_is_an_actionable_error() {
        let message = resolve_error(
            &format!("openapi: 3.0.0\ncomponents:\n  schemas:\n    A:\n      $ref: {REMOTE}#/a\n"),
            &[(REMOTE, "a: 7\n")],
        );
        assert!(message.contains("not a schema"), "{message}");
    }

    #[test]
    fn a_pointer_walks_sequences_escapes_and_the_whole_document() {
        let document: serde_yaml_ng::Value =
            serde_yaml_ng::from_str("a/b:\n  - first\n  - second\n").expect("valid yaml");
        assert_eq!(
            pointer(&document, "/a~1b/1").and_then(serde_yaml_ng::Value::as_str),
            Some("second")
        );
        assert!(pointer(&document, "").is_some());
        assert_eq!(pointer(&document, "/a~1b/9"), None);
        assert_eq!(pointer(&document, "/a~1b/nope"), None);
        assert_eq!(pointer(&document, "/missing"), None);
        assert_eq!(pointer(&document, "/a~1b/0/deeper"), None);
    }

    /// A loopback server that answers one request with a fixed status and body,
    /// so the real `curl` invocation is exercised without leaving the machine.
    fn serve_once(status: &'static str, body: &'static str) -> String {
        use std::io::{BufRead, BufReader, Write};
        let listener = std::net::TcpListener::bind("127.0.0.1:0").expect("bind a loopback port");
        let url = format!(
            "http://{}/doc.yaml",
            listener.local_addr().expect("address")
        );
        std::thread::spawn(move || {
            let Ok((mut stream, _)) = listener.accept() else {
                return;
            };
            let mut reader = BufReader::new(stream.try_clone().expect("clone the socket"));
            let mut line = String::new();
            while reader.read_line(&mut line).is_ok() {
                if line.trim().is_empty() {
                    break;
                }
                line.clear();
            }
            let response = format!(
                "HTTP/1.1 {status}\r\nContent-Length: {}\r\nConnection: close\r\n\r\n{body}",
                body.len()
            );
            let _ = stream.write_all(response.as_bytes());
        });
        url
    }

    #[test]
    fn the_curl_fetcher_returns_the_served_document() {
        let url = serve_once("200 OK", "address:\n  type: string\n");
        assert_eq!(
            CurlFetcher.fetch(&url).expect("a served document"),
            "address:\n  type: string\n"
        );
    }

    #[test]
    fn the_curl_fetcher_reports_an_error_status_rather_than_its_body() {
        let url = serve_once("404 Not Found", "<html>nope</html>");
        let message = curl_fetch(CURL, &url).expect_err("a 404 is not a document");
        assert!(message.starts_with("curl failed"), "{message}");
        assert!(!message.contains("<html>"), "{message}");
    }

    #[test]
    fn a_missing_curl_is_an_actionable_error() {
        let message = curl_fetch(
            "crozier-no-such-fetcher-on-path",
            "https://example.test/doc.yaml",
        )
        .expect_err("the program does not exist");
        assert!(message.contains("was not found on PATH"), "{message}");
    }

    #[test]
    fn only_http_and_https_references_are_fetched() {
        assert_eq!(
            split_remote("https://example.test/s.yaml#/a"),
            Some(("https://example.test/s.yaml", "/a"))
        );
        assert_eq!(
            split_remote("http://example.test/s.yaml"),
            Some(("http://example.test/s.yaml", ""))
        );
        assert_eq!(split_remote("#/components/schemas/A"), None);
        assert_eq!(split_remote("file:///etc/passwd"), None);
        assert_eq!(split_remote("./other.yaml#/A"), None);
    }
}
