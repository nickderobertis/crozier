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
| `combo-annotated-ref-property-example` | `schema.properties>schema.allOf:annotated-ref&schema.example` | a Schema Object with a property that writes an example beside an annotated reference (an allOf with one reference and annotation-only members) |
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

## Proof-strength amendment

The manager's renewed bar requires a removal control to change **both**
generators' output. The initial handling-site measurements below establish
reach, not output sensitivity. Zero-motion declarers are not witnesses.
The source search was extended within the same cached populations for
those keys; paired certified-output controls establish seven real witnesses, including two
declared-value departures.
Nine keys are proven by an output-sensitive witness; the two root-version keys
are decided output-insensitive, not proven (below).

## Verdicts

Every key is `search-incomplete`: these bounded cached populations cannot
exhaust the public specification population. The table's declarer count is its
number of `(source, document)` rows in `census.tsv`, including duplicate bytes
acquired in different source pools. Additional declarers retain their actual
screening state; one admitted generating registered witness per key suffices.

| key | outcome | declarers | selected proof |
|---|---|---:|---|
| `combo-allof-schema-example` | `search-incomplete` | 322 | registered `ahasend-api`; paired output-sensitive control passes |
| `combo-annotated-ref-property-example` | `search-incomplete` | 9 | hand-written `harbor-parcel-requests`; declared-value departure |
| `combo-anyof-schema-example` | `search-incomplete` | 169 | registered `supabase-api-v1`; output-sensitive declared-value departure |
| `combo-media-example-beside-component-example` | `search-incomplete` | 169 | registered `ahasend-api` (3202); complete golden and example attribution |
| `combo-media-example-on-inline-allof-body` | `search-incomplete` | 57 | registered `farmvibes-ai` (3201); complete golden and example attribution |
| `combo-media-example-on-ref-allof-body` | `search-incomplete` | 87 | registered `dashy-route-api` (3200); complete golden and example attribution |
| `combo-media-example-on-ref-union-body` | `search-incomplete` | 27 | registered `mockserver`; scoped golden reach |
| `combo-oneof-schema-example` | `search-incomplete` | 269 | registered `rgb-lightning-node` (3203); typed-example repairs and declared-value departure |
| `combo-param-example-beside-ref-schema` | `search-incomplete` | 138 | hand-written `harbor-parcel-requests`; declared-value departure |
| `combo-root-oas30-binary-schema` | `search-incomplete` | 61 | output-insensitive in both generators; paired real and authored controls, not proven |
| `combo-root-oas30-download` | `search-incomplete` | 69 | output-insensitive in both generators; paired real and authored controls, not proven |

## Root controls: output-insensitive

The two root OpenAPI-version conjunctions are decided as output-insensitive,
not proven. The renewed cached screen rendered seventeen distinct root documents;
none changed Crozier output after the final repair. Nimisampo reaches both
conjunctions but its version-removal control changes neither generator; the
complete comparisons are [nimisampo-fern-comparison.json](nimisampo-fern-comparison.json)
and [nimisampo-crozier-comparison.json](nimisampo-crozier-comparison.json).

Two from-scratch documents also isolate the version condition. The archive
control has a declared JSON error; the trace-archive control has no declared error
and offers both NDJSON and octet-stream success media. Changing only the root
version from 3.0.3 to 3.1.0 changes no generated file in either engine. Fern shows
the archive's worked example in both versions and omits the trace-archive's in
both. Crozier matches both complete certified trees after the root guard repair.
The complete path/digest maps are [root-fern-comparison.json](root-fern-comparison.json),
[root-crozier-comparison.json](root-crozier-comparison.json),
[root-no-error-fern-comparison.json](root-no-error-fern-comparison.json) and
[root-no-error-crozier-comparison.json](root-no-error-crozier-comparison.json).
The paired documents live in [removal-controls/](removal-controls/).
These controls are evidence of an output-insensitive decision, not hand-written
fixtures claimed as witnesses.

Both keys are rows of [the shared table](../output-insensitive.tsv) at context
`-` (`combo-root-oas30-binary-schema` and `combo-root-oas30-download`), citing
this record and the Nimisampo version-removal comparisons below, so each is
decided, neither proven nor unproven. Their region rows read `gap` and they
carry no golden-reach ledger row. Their reach, measured by the scoped golden-only
tier at commit 63c79bc0a430 before the decision, is recorded here:

| key | handling site | regions reached | golden-only witnesses | declared without a golden |
|---|---|---:|---|---|
| `combo-root-oas30-binary-schema` | `src/emit.rs::root_binary_download_undocumented` | 7/7 | `nimisampo` | — |
| `combo-root-oas30-download` | `src/emit.rs::root_binary_download_undocumented` | 7/7 | `chat-rest-api`, `nimisampo` | `color.pizza`, `loris-dataquery` |


The strict-form records of the Nimisampo version-removal control,
[nimisampo-version-removal-fern.json](nimisampo-version-removal-fern.json) and
[nimisampo-version-removal-crozier.json](nimisampo-version-removal-crozier.json),
hold complete 44-file trees whose before and after maps are identical in each
engine. The Fern maps are the certified pair's generation of the committed
source and of [removal-controls/nimisampo-after.yml](removal-controls/nimisampo-after.yml);
the crozier maps were regenerated from the same two documents on the tree that
merged base commit `0fe1f0c99`.

## Paired removal controls

[paired-removal-comparisons.json](paired-removal-comparisons.json) records the
seven completed real controls: five move both generators, while Supabase and
RGB move Crozier under evidenced declared-value departures. Each control deletes every
`example` field matching that key through the census object-kind traversal,
leaving the other fields unchanged; the conjunction counts zero afterwards.
The committed original source and complete certified-pair golden are the
before state. A fresh serial certified-pair generation supplies the after state,
and `crozier compare` matches that entire control tree. The record retains each
changed generated file's before/after SHA-256 in both engines, excludes the
corpus metadata marker, and records the comparison's exit code and counts.

[reaching-removal-comparisons.json](reaching-removal-comparisons.json) preserves
the broader Crozier preflight of every declarer joined by the scoped reach
ledger. A zero-file result is reaching but not proving. The ledger's join means
declaration plus executed site, and does not turn these controls into witnesses.
Zulip, Webflow and Nimisampo are expressly reaching-only for their zero-motion
keys. AhaSend replaces Zulip for the allOf schema-example proof. Dashy's
referenced-union removal also moves Crozier output, but the selected certified
proof for that key is MockServer.

## Renewed screening results

[renewed-screening.json](renewed-screening.json) records 93 additional preflight
outcomes: 35 generating request-side oneOf documents, 12 generating download
controls, 12 binary-schema controls, three annotated-reference controls, and 31
baseline failures. Seventeen distinct root documents were rendered before and
after the final root repair; their version-removal controls move no Crozier
file. The recorded earlier motions on several root documents belong to the
superseded broad suppression, and are explicitly identified as earlier states.
No preflight-only candidate is claimed to have generated with Fern.

RGB Lightning Node is the selected oneOf witness. Its source is the publisher's
`openapi.yaml` at `d4762ac3d1b3ca83f2f7b4f894e8569109dc572a`, SHA-256
`3f98f35065a55920e2659e0720ada89f6738d4bb651a4104964b18c549f93026`.
The complete certified baseline and removal control both compare; its declared
`SyncKeychain` example is retained under the richer-documentation ruling.
Typed maps of model lists, empty model-array examples and referenced
discriminator constructors are repaired generally. The existing required-file
example defect applies independently in the same client, with signature-binding
evidence in its catalogue note. Guardian also generates but is not selected;
its additional mismatch classes remain in the census and a drafted follow-up.

## Renewed search and authored reference examples

The renewed cached screen follows request inputs through local references,
properties and compositions, deduplicates source bytes, and prioritizes registered
sources and documents with a recorded redistribution grant. No typed-reference
parameter declarer in those populations carries the sibling `type: string`
that makes its own parameter example render. The annotated-reference search
finds the registered Zulip variants (zero motion), response-only declarations,
and Graphhopper variants that Crozier refuses for an undefined security scheme;
none supplies an output-sensitive admitted witness. The bounded search remains
`search-incomplete`.

| key | renewed search outcome |
|---|---|
| `combo-param-example-beside-ref-schema` | `none-registrable` |
| `combo-annotated-ref-property-example` | `none-registrable` |

`harbor-parcel-requests` is authored from scratch. A required query parameter
carries a string example beside its referenced schema; a required body property
carries an example beside an annotated reference. Removing either changes
Crozier's worked calls. Fern substitutes field-name placeholders in both states.
The manager's declared-content ruling keeps the richer examples through the
existing `anyof-path-param-schema-example` departure, extended narrowly to those
required reference shapes. This is a hand-written proof with an evidenced
intentional departure; it is not an output-insensitive decision.

[annotated-context-screening.json](annotated-context-screening.json) records the
four unregistered annotated-reference document hashes separately. DigitalOcean
and OGC have no request path to the annotated property, including through local
references, and no external input references. GraphHopper's two variants do
have an input path. The bounded [repository-grant lookup](graphhopper-grant-lookup/lookup.json)
finds an admissible aggregation grant for the index copy; the other repository's
pinned licence endpoint returns 404, so no grant was found there. A fresh serial
[certified-pair measurement](graphhopper-annotation-measurement/measurement.json)
of the admitted index copy refuses both annotation states for missing service
auth and writes no SDK. The logs and both canonical inputs are committed beside
the measurement. This source refusal screens a candidate; it does not classify
the combination itself as non-generating, since its hand-written proof generates.

## Attribution

The registered witnesses have `unmatched: &[]` in the corpus gate. The latest
completed scoped measurement runs 63 golden tests at
`ca5ec9b4a7fbad31237cedbb41ec54b070d75607`, after the rendering-mode,
component-policy and identifier-validation refactors. All 63 pass, including the seven real-witness keys' declarers and
every joined witness of the two single-feature rows whose request-field site
moved. This supersedes the earlier 62-test measurement at
`63c79bc0a430d622930dca3486d55d4d728b3ca2`, which preceded the later rendering
and departure repairs. The region join retains every measured declarer; the
paired removal controls, rather than reach alone, establish sensitivity.
The [site table](../golden-reach-sites.tsv) records the example handoff sites;
the [reach ledger](../golden-reach.tsv) carries the scoped run's provenance.
All nine generating removal controls were replayed at the same production
revision: their complete change/digest maps stayed identical and each certified
control tree still compared. The archive, trace-archive and Nimisampo version
pairs were also replayed: each retained its complete unchanged digest maps and
both versions compared to their certified trees.

These handoff measurements do not claim every path of the containing function
is exhausted; the single-feature rows retain those wider handling branches.

Deleting the conjunction's examples in MockServer changes `reference.md` and
the expectation and verify clients. Supabase's removal changes Crozier's README,
reference and environments client, while the certified Fern control changes no
generated file. The existing declared-value departure preserves the valid
source content; both the complete baseline and removal control compare.
Removing examples in HSE and Zulip moves no bytes. Their earlier reach evidence
is handling-site reach only; neither is an output-sensitive witness.

The three media-example combinations require stronger witnesses than their
initial region entries named. D&D's inline/allOf media example occurs on the
monster GET response; deleting it moves no file. The same experiment on the registered declarer population at
`a183c7c4ff597862991ad7a632aa95fc7be23cec`, before these admissions, moved no
file for the referenced/allOf and competing-example conjunctions either. The request-example handoff sites are unreached by the
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

### Correcting the inline-composition attribution

The first site selected for `combo-media-example-on-inline-allof-body` was the
IR branch merging compositions whose members are all inline objects. It
measured **0/6** regions: FarmVibes instead writes one reference inside its
inline composition. A second attempted attribution used
`inline_schema_pointers` (**7/35**) and the plain inline-property request branch
(**0/63**); neither describes that request's actual lowering. The pointer
normalizer does not expand a simple component reference here.

The actual path is `normalize_request_bodies` calling
`collapse_sole_composition_member`: FarmVibes' nonnullable wrapper, carrying
only a title and description beside its single-reference `allOf`, becomes that
reference. `resolve_request_body` then flattens its component fields and applies
the media example through the same referenced-object path already proven by
other bodies. The corrected site table measures that composition-collapse arm
and the referenced-object handoff. These sites attribute this witness; they do
not claim every possible multi-member composition is exhausted.

The from-scratch unit test
`inline_single_reference_composition_examples_use_the_referenced_object_path`
drives the public loader and IR builder with the same document shape. It
asserts the normalized reference, preserved title, flattened field and winning
media value over a competing component example. An induced run bypassing the
loader failed at the reference assertion (`None` versus the expected component
reference); restoring the loader passed. Together with FarmVibes' complete
byte-match and example-removal attribution, it ties the sites to this shape
rather than to unrelated code the witness happens to execute.
