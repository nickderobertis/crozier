# Witness search for schema combinations in examples

This bounded search covers the eleven `examples` rows owned by
`prove-schema-combinations` in [combinations.md](../combinations.md). The
certified pair is Fern CLI 5.163.1 and `fernapi/fern-python-sdk` 5.41.3.
A declaration alone does not prove the example-handling branch: its registered
golden must byte-match the generated files that branch writes.

## The search

Measured on 2026-10-22, without a new specification fetch:

- **APIs.guru:** `APIs-guru/openapi-directory` at
  `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49`, read from the shared cached archive
  with SHA-256 `816adb9fb4e19dc9ab28d7ad95363de146251fb41164abdb86f953f9f400c644`.
- **Committed sources:** every JSON/YAML document below `tests/fixtures/` at
  `a183c7c4ff597862991ad7a632aa95fc7be23cec`, including every registered corpus source. The
  golden-source census separately reads 257 sources (31 original fixtures and
  226 corpus sources); the broader search also reads acquired documents without
  a registered golden. Per-source immutable revisions and digests remain in
  `tests/fixtures/corpus-sources.tsv`.
- **Earlier acquisitions:** the GitHub code-search and Sourcegraph documents
  retained in the earlier searches' `candidate-documents.json` manifests.
  Every declarer's repository, document path, full revision and byte digest
  appear in `census.tsv`; multiple acquired names for identical bytes share one
  row per source pool. These are acquired snapshots, not a new live search.

Generator-vendor repositories and the index's excluded repositories are excluded
before reading documents, using normalized repository names (with an optional
`github.com/` host prefix removed). The filtering rule is the existing
`excluded_repository` / `normalize_repo` contract in
`tools/witness-search/witness-search-github-index.py`; no excluded document is
part of this record. No GitHub code search, portal or registry was queried.

| population | JSON/YAML files read | OpenAPI 3 | other version or no root OpenAPI 3 marker | unreadable |
|---|---:|---:|---:|---:|
| `apis.guru` | 4138 | 1970 | 2168 | 0 |
| `github-code-search` | 5124 | 4786 | 285 | 53 |
| `registered` | 895 | 275 | 620 | 0 |
| `sourcegraph` | 4078 | 2852 | 1209 | 17 |

The shared census reader and its optional PyYAML C-loader fallback read each
object model. The acquired-pool enumeration returns exit 1 for unreadable
inputs; [unreadable.tsv](unreadable.tsv) preserves every such classification,
rather than treating them as zero declarations.

### The detectors

Each detector is exactly its census conjunction: `&` joins conditions at the
same anchor, `>` follows an object edge, and `~>` resolves a local reference.
The conjunction grammar is [the census grammar](../../openapi-surface-coverage.md).

| key | detector | meaning |
|---|---|---|
| `combo-allof-schema-example` | `schema.allOf&schema.example` | a Schema Object declaring both a composition and an example |
| `combo-annotated-ref-property-example` | `schema.properties>schema.allOf:annotated-ref&schema.example` | a Schema Object with its own example and a property whose allOf is an annotated reference |
| `combo-anyof-schema-example` | `schema.anyOf&schema.example` | a Schema Object declaring both anyOf alternatives and an example |
| `combo-media-example-beside-component-example` | `mediaType.example&mediaType.schema>schema.$ref~>schema.example` | a Media Type Object with its own example and a schema reference to a component with its own example |
| `combo-media-example-on-inline-allof-body` | `mediaType.example&mediaType.schema>schema.allOf` | a Media Type Object with its own example and an inline allOf schema |
| `combo-media-example-on-ref-allof-body` | `mediaType.example&mediaType.schema>schema.$ref~>schema.allOf` | a Media Type Object with its own example and a schema reference to an allOf component |
| `combo-media-example-on-ref-union-body` | `mediaType.example&mediaType.schema>schema.$ref~>schema.oneOf` | a Media Type Object with its own example and a schema reference to a oneOf component |
| `combo-oneof-schema-example` | `schema.example&schema.oneOf` | a Schema Object declaring both oneOf alternatives and an example |
| `combo-param-example-beside-ref-schema` | `parameter.example&parameter.schema>schema.$ref` | a Parameter Object with its own example and a schema reference |
| `combo-root-oas30-binary-schema` | `operation.context:oas-three-zero&operation.context:root-client&operation.context:success-binary-schema` | an ungrouped root operation in OpenAPI 3.0 whose selected success schema is a binary string |
| `combo-root-oas30-download` | `operation.context:oas-three-zero&operation.context:root-client&operation.context:success-download` | an ungrouped root operation in OpenAPI 3.0 whose selected success media type is a download |

### Reproducing the bounded enumeration

Select the eleven key/selector rows above from `witness-search-keys.tsv` into a
TSV contract with its existing header. Stage the archive's `APIs/` tree and the
normalized, filtered acquisition manifests' documents in separate directories.
Run `just witness-search-local-census --contract CONTRACT --all-documents-jsonl
--documents SOURCE=DIR` for each population; the JSON objects retain every
input's SHA-256, classification and count. Join positive counts to the acquired
manifest's full identities, as [census.tsv](census.tsv) does. The registered
source walk is `--documents registered=tests/fixtures`.

## Verdicts

Every key is `search-incomplete`: these bounded cached populations cannot
exhaust the public specification population. The table's declarer count is its
number of `(source, document)` rows in `census.tsv`, including duplicate bytes
acquired in different source pools. Additional declarers retain their actual
screening state; one admitted generating registered witness per key suffices.

| key | outcome | declarers | selected proof |
|---|---|---:|---|
| `combo-allof-schema-example` | `search-incomplete` | 322 | registered `zulip`; scoped golden reach |
| `combo-annotated-ref-property-example` | `search-incomplete` | 9 | registered `zulip`; scoped golden reach |
| `combo-anyof-schema-example` | `search-incomplete` | 169 | registered `supabase-api-v1`; scoped golden reach |
| `combo-media-example-beside-component-example` | `search-incomplete` | 169 | registered `ahasend-api` (3202); complete golden and example attribution |
| `combo-media-example-on-inline-allof-body` | `search-incomplete` | 57 | registered `farmvibes-ai` (3201); complete golden and example attribution |
| `combo-media-example-on-ref-allof-body` | `search-incomplete` | 87 | registered `dashy-route-api` (3200); complete golden and example attribution |
| `combo-media-example-on-ref-union-body` | `search-incomplete` | 27 | registered `mockserver`; scoped golden reach |
| `combo-oneof-schema-example` | `search-incomplete` | 269 | registered `zulip`; scoped golden reach |
| `combo-param-example-beside-ref-schema` | `search-incomplete` | 138 | registered `hse`; scoped golden reach |
| `combo-root-oas30-binary-schema` | `search-incomplete` | 61 | registered `nimisampo`; scoped golden reach |
| `combo-root-oas30-download` | `search-incomplete` | 69 | registered `nimisampo`; scoped golden reach |

## Attribution

The existing selected witnesses have `unmatched: &[]` in the corpus gate.
Their named golden tests passed, and a separate instrumented run of the eight
candidate golden tests measured their reach at the source revision above.
The [site table](../golden-reach-sites.tsv) records the example handoff sites;
the [reach ledger](../golden-reach.tsv) carries the scoped run's provenance.
These handoff measurements do not claim every path of the containing function
is exhausted; the single-feature rows retain those wider handling branches.

Deleting the conjunction's examples in MockServer changes `reference.md` and
the expectation and verify clients. Deleting Supabase's `anyOf` schema examples
changes its README, reference and environments client. Removing examples in
HSE and Zulip moves no bytes; their proof here is the measured handling-site
reach plus their complete byte-matched goldens, rather than a claim of
output sensitivity.

The three media-example combinations require stronger witnesses than their
initial region entries named. D&D's inline/allOf media example occurs on the
monster GET response; deleting it moves no file. The same experiment on every
registered declarer of the referenced/allOf and competing-example conjunctions
moves no file either. The request-example handoff sites are unreached by the
initial D&D and NextGen witnesses. Those declarations remain in the census,
but they are not selected as proofs of these branches.

Three request-side documents now supply complete certified-pair goldens:

| corpus row | witness | grant location | matching example removal changes |
|---|---|---|---|
| 3200 | `dashy-route-api` | document `info.license` | README, reference, items and sections clients (2 sites) |
| 3201 | `farmvibes-ai` | publisher's pinned `LICENSE`, retained at `licenses/farmvibes-MIT.txt` | README, reference and workflows client (1 site) |
| 3202 | `ahasend-api` | document `info.license` | reference and sub-accounts client (12 sites) |

The immutable publisher revisions, source digests and acquisition identities are
in `census.tsv` and the corpus source registry. FarmVibes' grant was fetched
through the rate-limit guard and shared cache after this bounded specification
walk; no specification was newly fetched. The sources, NOTICE entries, complete
goldens and gate registrations are committed. The matching tests compare every
file, with no residual allowance, in default and strict modes. Literal-mode
outputs are fresh certified-pair overlays for these and the existing selected
witnesses where enums change the output.

The removal experiment uses crozier on a temporary copy of each document,
removing only the conjunction's media examples. It establishes attribution,
not a modified reference: the unmodified source's complete Fern output is the
comparison target. [attribution.json](attribution.json) records the changed paths.

Two repairs were needed: Markdown examples preserve free-form map values
without expanding their JSON arrays, and request media examples supersede whole
component examples while retaining property-level fallbacks. Unit regressions
exercise the triggering shapes and adjacent fallback cases. Existing committed
reference trees were not edited. No new departure rule was needed.

MockServer's literal regeneration staged its already-vendored remote-reference
bytes with absolute local paths so the generation workspace could resolve them;
the committed source and its immutable remote pins are unchanged.
