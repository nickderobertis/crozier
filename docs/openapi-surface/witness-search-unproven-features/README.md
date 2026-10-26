# Witness search for the unproven features and arms

This bounded search reads the populations below for the twelve unproven keys
and the additional arm covers removed by the certified-pair retarget. Its
Fern measurements use CLI 5.163.1 and `fernapi/fern-python-sdk` 5.41.3.
This is an **unfinished screen**, not a claim that no real witness exists.
A key with outstanding candidates cannot yet cite this record as
`none-registrable`; the qualifying renewed searches are identified below. The
zero-declarer features are covered by `observatory-example-arrays`.
`onmyshelf-api` proves digit-leading methods, and `harbor-signal-null` supplies
the weaker residual-only null proof. `formbricks` proves the object-on-map arm.
The fractional optional request property, the three examples beside a `$ref`
and the empty-object arm are decided output-insensitive, not proven. After the
[renewed bounds](#remaining-bounds-after-the-source-repairs), the array-null
key and the outside-enum and string-const arms rest on hand-written fixtures.
`discriminator-mapping`'s two arms were screened over every declarer
([arm probe](#discriminator-mapping-arm-probe)); none is a witness, so they
rest on the hand-written `tidepool-survey-log` fixture.

## The search

The population census was taken on 2026-10-21. These are the acquired pools at
that time; their pinned identities are retained in the acquisition manifests.

- **APIs.guru.** `APIs-guru/openapi-directory` at
  `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49`, the revision the corpus's
  APIs.guru rows already pin, fetched once as its archive through
  `tools/witness-search/witness-acquire-github.py` under
  `tools/witness-search/rate_limit_guard.py` (one `core` call; SHA-256
  `816adb9fb4e19dc9ab28d7ad95363de146251fb41164abdb86f953f9f400c644`, the
  digest [`../witness-search-prove-matches/`](../witness-search-prove-matches/README.md#the-search)
  records, and now held in the shared GitHub response cache). Its `APIs/` tree
  holds 4,138 JSON and YAML files: 1,927 OpenAPI 3 documents, 2,163 Swagger 2
  ones and 48 that PyYAML 6.0.3's C loader cannot parse.
- **The registered corpus.** The recovered source tree at
  `91311a3a8626b118586c7daf1d35d49f58905e1a` (unchanged from its retargeted parent): every
  OpenAPI 3 document under `tests/fixtures/` (each committed corpus source and
  each vendored fixture `openapi.*`), 274.
- **The GitHub code-search pool.** The documents the earlier searches' GitHub
  REST code-search acquisitions left in their search cache
  (`.local/golden-reach-search/github-code-search/`), each named by its
  repository, path and pinned commit: 5,162 files under 5,657 names, of which
  4,810 parse as OpenAPI 3 documents. One of them,
  `jhannes/logevents:logevents/src/main/resources/org/logevents/openapi.json@9c6c11ae395000f50da022b57e9e3d3fdce3c319`,
  stops the census evaluator (its `required` lists hold objects) and is
  counted unreadable.
- **The Sourcegraph pool.** The same cache's Sourcegraph acquisitions
  (`.local/golden-reach-search/sourcegraph/`): 4,095 files under 5,210 names,
  2,854 of them OpenAPI 3 documents.

The two pools also hold 52 documents taken from the generator vendor's own
repositories; they were left out of every count and table below. No other
document was fetched for the census: the populations were read from the
archive and the pools as they stood.

### The detectors

| key | selector | site |
|---|---|---|
| `operation-id-digit-leading-method` | `operation.operationId:digit-leading-method` | an Operation Object under the Paths Object whose `operationId`-derived method name, after crozier's tag, group, FastAPI-suffix and template transforms, starts with a digit; an operation naming its method by extension, or carrying no id, is not one |
| `schema-example-fractional-on-integer` | `schema.example:fractional-on-integer` | a Schema Object whose primary type is `integer` and whose selected example is a JSON fraction |
| `schema-example-array-null-element` | `schema.example:array-null-element` | a Schema Object whose selected example is an array holding a `null` |
| `schema-example-temporal-duplicate-element` | `schema.example:temporal-duplicate-element` | a Schema Object whose `items` write `format: date` or `date-time` and whose selected example is an array repeating an element |
| `schema-example-union-ref-sentinel` | `schema.example:union-ref-sentinel` | a Schema Object declaring `oneOf` or `anyOf` whose selected example is an object holding only `$ref` |
| `schema-example-on-ref-to-object` | `schema.example:on-ref-to-object` | a Schema Object with a selected example beside a `$ref` that resolves, in the document's `components.schemas`, to a schema with a non-empty `properties` map and no `oneOf`, `anyOf` or string-valued `enum` |
| `schema-example-on-ref-to-enum` | `schema.example:on-ref-to-enum` | a Schema Object with a selected example beside a `$ref` resolving in `components.schemas` to a string-valued `enum` with no `oneOf` or `anyOf` |
| `schema-example-on-ref-to-union` | `schema.example:on-ref-to-union` | a Schema Object with a selected example beside a `$ref` resolving in `components.schemas` to a `oneOf` or `anyOf` |
| `schema-example-null` | `schema.example=null` | a Schema Object whose selected example (its `example`, else its first `examples` member) is `null`; a declarer is a witness only where removing those nulls moves a generated file, which [`residual-attribution.py`](../../../tools/surface-census/residual-attribution.py) asks of a registered golden |
| `schema-example-empty-object` | `schema.example:empty-object` | a declarer of the selector (a Schema Object whose selected example is `{}`) on which the instrumented crozier `just handwritten-reach` builds, run over that document alone, executes `src/emit.rs::ExampleCtx::value_from_example[if fields.is_empty\(\) \{]` |
| `schema-example-object-on-map` | `schema.example:object-on-map` | a declarer of the selector (a Schema Object writing `additionalProperties`, with no non-empty `properties`, whose selected example is an object) on which that instrumented run executes `src/emit.rs::ExampleCtx::example_matches_type_through[=TypeRef::Dict\(_, _\) => value.is_object\(\),]` |
| `schema-example-outside-enum` | `schema.example:outside-enum` | a declarer of the selector (a Schema Object with a string-valued `enum` whose selected example is a string none of its members is) on which that instrumented run executes `src/emit.rs::ExampleCtx::example_matches_type_through[=Some\(TypeDecl::Enum\(decl\)\) => value]` |
| `discriminator-mapping` | `schema.discriminator.mapping` | a declarer of the selector on which that instrumented run executes `src/ir.rs::Builder::discriminated_union[if union_target \{]` or `src/emit.rs::ExampleCtx::named_value_inner[Some\(m\) if m\.layout\.is_wrapped\(\) => \{]` |
| `oneof-string-const-variant` | `schema.oneOf>schema.const:string-valued` | a declarer of the selector on which that instrumented run executes `src/ir.rs::InlineHoister::hoist_union_variant[if let Some\(values\) = string_enum_values\(variant\) \{]` |

### Declarers and screening

[`census.tsv`](census.tsv) records every counted declarer, its site count and,
for arm candidates, the instrumented execution result. A declaration alone
cannot prove an arm: the named handling site must execute. Registered documents
retain their individual revisions in `tests/fixtures/corpus-sources.tsv`.
The two acquisition pools retain repository/path/commit identities in their
`candidate-documents.json` manifests. Duplicate byte-identical acquisitions are
counted once with their additional-name count.

[`screening.tsv`](screening.tsv) records the selected candidate queue, including
full immutable revisions. Its licence and reference outcomes come from
[`screens.jsonl`](screens.jsonl); the latter retains the complete measurements,
content hashes and hash-addressed logs in [`screens/`](screens/). A successful
licence screen means the grant passed the corpus policy, not that publisher
provenance has been established. Each candidate still needs that publisher
review, crozier whole-tree comparison, and, where applicable, instrumented arm
reach before registration. Aggregator origin alone does not establish publisher
provenance. A registered declarer already has its provenance and gate wiring;
its existing proof must still execute the requested arm or move a byte-matched
file for the null-example key.

The recovered queue contains 116 selected documents. Of these, 77 have a
committed screen; six further measured arm candidates are also in the screen
ledger. The other 39 selected documents remain outstanding. Existing results
are reused, not re-fetched or re-generated. Timeout outcomes are outstanding,
not non-generation proofs: the resumed bound for remaining Fern candidates is
10 minutes under the shared generation lock.

## Verdicts

`search-incomplete` describes the bounded populations, not eligibility for a
hand-written cover. `discriminator-mapping` alone reads `exhausted`: every one
of its declarers has a decision. Pending candidates must be resolved before a
`none-registrable` renewed-search line can be written. The census count below
is document/key rows, not a count of distinct APIs or successful witnesses.

| key | verdict | declaring documents | registration status |
|---|---|---|---|
| `discriminator-mapping` | `exhausted` | 899 | every declarer decided ([arm probe](#discriminator-mapping-arm-probe)): no admissible real document executes either arm and generates at the certified pair; admitted lower-proof `tidepool-survey-log` fixture covering `src/ir.rs::Builder::discriminated_union[if union_target \{]` and `src/emit.rs::ExampleCtx::named_value_inner[Some\(m\) if m\.layout\.is_wrapped\(\) => \{]` |
| `oneof-string-const-variant` | `search-incomplete` | 70 | no admissible real document reaches the arm and generates at the certified pair ([bound](#remaining-bounds-after-the-source-repairs)); admitted lower-proof `compass-choice` fixture |
| `property-map-value-enum` | `search-incomplete` | 106 | registered: corpus row 3003, `fletch-mcp`; complete certified-pair SDK byte-match, arm reach measured ([map-value search](#map-value-branch-search)) |
| `property-map-value-oneof` | `search-incomplete` | 83 | no admissible real document reaches the arm and byte-matches at the certified pair ([map-value search](#map-value-branch-search)); admitted lower-proof `shelf-labels-map-variants` fixture covering `src/ir.rs::InlineHoister::prop_type_ref[if value.reference.is_none\(\) && value.declared_type_name\(\).is_none\(\) && structured \{]` |
| `property-map-value-struct` | `search-incomplete` | 304 | registered: corpus row 3002, `panoptes`; complete certified-pair SDK byte-match, arm reach measured ([map-value search](#map-value-branch-search)) |
| `operation-id-digit-leading-method` | `search-incomplete` | 97 | registered: corpus row 3000, `onmyshelf-api`; complete certified-pair SDK byte-match |
| `schema-example-array-null-element` | `search-incomplete` | 41 | no admissible real document both generates at the certified pair and moves output ([bound](#remaining-bounds-after-the-source-repairs)); admitted lower-proof `lunar-null-labels` fixture |
| `schema-example-empty-object` | `search-incomplete` | 171 | arm decided output-insensitive ([attribution](#empty-object-arm-attribution)); no real declarer moves output |
| `schema-example-fractional-on-integer` | `search-incomplete` | 20 | generating context decided output-insensitive ([attribution](#optional-fractional-request-property-attribution)); other contexts refused |
| `schema-example-null` | `search-incomplete` | 28 | cached attribution preflight complete: no qualifying byte-moving witness; admitted lower-proof `harbor-signal-null` fixture |
| `schema-example-object-on-map` | `search-incomplete` | 636 | registered: corpus row 3001, `formbricks`; complete certified-pair SDK byte-match, arm reach measured ([attribution](#formbricks-map-example-attribution)) |
| `schema-example-on-ref-to-enum` | `search-incomplete` | 100 | decided output-insensitive in every measured context ([attribution](#examples-beside-a-ref-attribution)) |
| `schema-example-on-ref-to-object` | `search-incomplete` | 93 | decided output-insensitive in every measured context ([attribution](#examples-beside-a-ref-attribution)) |
| `schema-example-on-ref-to-union` | `search-incomplete` | 12 | decided output-insensitive in every measured context ([attribution](#examples-beside-a-ref-attribution)) |
| `schema-example-outside-enum` | `search-incomplete` | 137 | no admissible real document reaches the arm and generates at the certified pair ([bound](#remaining-bounds-after-the-source-repairs)); admitted lower-proof `enum-media-selection` fixture |
| `schema-example-temporal-duplicate-element` | `search-incomplete` | 0 | no declarer in the bounded populations |
| `schema-example-union-ref-sentinel` | `search-incomplete` | 0 | no declarer in the bounded populations |

The two zero-declarer keys have `none-registrable` outcomes within these
bounded populations. The null-example key also has that outcome after the
bounded attribution preflight below, and the array-null, outside-enum and
string-const keys have it after the
[renewed bounds](#remaining-bounds-after-the-source-repairs). The
residual-only hand-written rule for `schema-example-null` remains a fallback
only if no real witness can be registered.

## Renewed search

| key | verdict | outcome |
|---|---|---|
| `schema-example-temporal-duplicate-element` | `search-incomplete` | none-registrable |
| `schema-example-union-ref-sentinel` | `search-incomplete` | none-registrable |
| `schema-example-null` | `search-incomplete` | none-registrable |
| `schema-example-array-null-element` | `search-incomplete` | none-registrable |
| `schema-example-outside-enum` | `search-incomplete` | none-registrable |
| `oneof-string-const-variant` | `search-incomplete` | none-registrable |
| `property-map-value-oneof` | `search-incomplete` | none-registrable |

## Null-example attribution preflight

The renewed null search is bounded to all 28 declarers already acquired above;
it makes no new document fetch and no Fern run. [`null-preflight.tsv`](null-preflight.tsv)
records every identity and source digest, including Webflow and SandboxFusion.
Byte-identical acquisitions reuse their measurement and retain every declaring
identity in the table.

For each cached document, load its object model with the census's own reader,
clone it, and apply `residual-attribution.py::_stringify_null_examples`. Generate
both JSON object models with the compiled crozier, `--no-config`, package `fern`
and project `default_package_name`, under the existing corpus offline harness's
inherited socket-denial filter. Compare every generated file byte for byte.
This is the attribution tool's JSON-model protocol. The perturbation count is
not a new schema census: the transform also visits nested example content;
`census.tsv` retains the object-model detector's declaring-site counts.

No successful model pair moves a file. Other rows explicitly record refusal of
the unperturbed or perturbed model, not a claim that a refused run generated an
unchanged SDK. None therefore supplies the byte-moving, byte-matched-file proof
this residual-only key requires. A generating declarer without such motion is
not a qualifying real witness, even with an admissible grant and publisher.

That eligibility check precedes renewed licence and publisher review. The table
retains prior grant screens where available, identifies registered provenance
and obvious third-party copies, and explicitly marks reviews not renewed after
the preflight disqualified the document. No qualifying witness was discarded
on an unverified licensing or publisher assumption.

An earlier exploratory comparison serialized only the perturbed side as YAML.
That changed unrelated timestamp examples in Vercel and Runpod and was discarded;
those apparent file movements are not evidence. The accepted table comes only
from the two-sided JSON-model run. An audit of all 28 cached sources found no
absolute remote references; the accepted run additionally denied sockets.

## Retargeted arm inventory

The removed arm covers were identified with
`git show e99fe8d6 -- 'docs/openapi-surface/handwritten/*/evidence.toml'`.
Excluding renamed sites, four covers were removed: `discriminator-mapping`'s
`src/openapi.rs::collect_schema_refs[if let Some\(disc\) = &schema\.discriminator \{]`,
`src/ir.rs::Builder::discriminated_union[if union_target \{]`,
`src/emit.rs::ExampleCtx::named_value_inner[Some\(m\) if m\.layout\.is_wrapped\(\) => \{]`,
and `oneof-string-const-variant`'s
`src/ir.rs::InlineHoister::hoist_union_variant[if let Some\(values\) = string_enum_values\(variant\) \{]`.
The first already has registered golden reach; the other three were searched
here, and each now rests on a hand-written fixture. This inventory does not count renamed handling sites as lost proof.

## Pending nested-mapping defect

The from-scratch [nested discriminator measurement](../../fern-measurements/examples/nested-discriminator-wire/README.md)
executes the certified SDK against its source schema: the SDK emits a nested
`value` envelope where the schema requires a flat object and rejects a valid
flat response; its README example also fails compilation. That defect is now
the catalogued departure
[`nested-discriminator-flat-wire`](../../departures/evidence/nested-discriminator-flat-wire.md).
It bears on a mapping target that is a union with a discriminator of its own,
which the `union_target` arm lays out as a nested discriminator. The arm
probe below covers both arms with a target that has no discriminator, so
the wrapper holds it whole in `value`.

## Discriminator-mapping arm probe

Every one of the 899 `discriminator-mapping` declarers in
[`census.tsv`](census.tsv) has a decision in its `arm` cell. Those cells answer
three questions: whether the instrumented run executes
`src/ir.rs::Builder::discriminated_union[if union_target \{]` or
`src/emit.rs::ExampleCtx::named_value_inner[Some\(m\) if m\.layout\.is_wrapped\(\) => \{]`,
whether the document was screened for admission, and whether the certified pair
generates from it. No document outside the four populations above was read;
they came from the existing caches and the pinned APIs.guru archive.

Each declarer was generated on its own by crozier at this branch's base,
`80331e4b`, built with the `llvm-cov` instrumentation `just handwritten-reach`
uses, and both arm sites were read off the run's profile. A profile is written
whether crozier generates, refuses or fails, so a refused document's row still
records that neither site ran. Since then the branch has changed only a wrapper's
docstring, the line breaking of its example and the self-mapped refusal below,
and none of these moves either site. The outcomes below are counted in census
rows:

- **532 generate and execute neither arm, and 31 registered rows execute
  neither.** A document that runs no arm is no witness, so its licence and
  certified-pair run were not reviewed.
- **4 build every type but fail `ruff format`, executing neither arm.**
- **329 are refused by crozier at the boundary, before any type is built.**
  For the 68 of them whose document holds a shape from which crozier builds a
  wrapped member, the certified pair was run under the shared generation lock
  (one at a time, 1800-second bound). Such a shape is a mapping target that is a
  union of references, a mapping naming its own schema, a composed union member,
  or a mapping naming an absent schema. Those runs, with one `ruff` failure's,
  are in [`discriminator-mapping-fern.tsv`](discriminator-mapping-fern.tsv)
  with each refusal's first diagnostic. Fern refuses 59 and generates from 9,
  as it does from that `ruff` failure. None of those 10 reaches either arm. None
  has a mapping target that is a union, a mapping naming its own schema or a
  composed member. Where a mapping names an absent schema, that ends the union
  before any member is built (`self.schemas.get(target_key)?` or
  `resolve_ref_from_schemas(...)?`). The other 261
  refused documents hold none of those shapes, so neither arm can execute
  whatever Fern does. They were not run.
- **The two Microsoft Graph descriptions (APIs.guru `graph` and `graph-beta`,
  25 MB and more) are decided from the document.** Their instrumented runs
  passed 3600 seconds without finishing. Read in full, their 476 discriminator mappings hold
  no self mapping and no absent target, and no target or member is a composed
  union. So no wrapped member is built and neither arm can execute.
- **Apple's SiriKit Cloud Media (`APIs/apple.com/sirikit-cloud-media/1.0.2`)
  executes the wrapped-example arm alone.** Its
  `AddMediaIntentHandlingInvocation` and `UpdateMediaAffinityIntentHandlingInvocation`
  map every `method` value to themselves. The certified pair refuses the
  document: `Missing discriminant property ("method")` on both endpoints'
  examples. crozier now refuses it in both modes, through the
  `missing-discriminant-property` refusal's self-mapped shape
  (`self-mapped-probe.yml` and its two controls under
  [`../fern-refusals/`](../fern-refusals/shapes.tsv)).

So no admissible real document both executes either arm and generates at the
certified pair, and the key's verdict is `exhausted`. The hand-written
[`tidepool-survey-log`](../handwritten/tidepool-survey-log/openapi.yml) fixture
covers both arms. It maps `level` to `WaterLevel`, a `oneOf` of a bare number and an
object with no discriminator. Crozier byte-matches its certified-pair tree apart
from the worked examples of `README.md` and `reference.md`. There, Fern writes
`SurveyEntry_Level(level=,)`, which does not compile; that is the catalogued
`fern-defect` departure
[`wrapped-union-member-docs-example`](../../departures/evidence/wrapped-union-member-docs-example.md).

## Publisher reviews after the recovered queue

These reviews apply the [corpus grant rule](../../corpus-licensing.md) to the
pinned source paths, rather than assuming a successful generator run establishes
redistribution rights. They supplement the 83 formal screening records; they do
not claim the 39 outstanding queue entries were screened.

| candidate | publisher provenance and grant scope | grant bytes SHA-256 | outcome |
|---|---|---|---|
| `microsoft/adme-samples:rest-apis/M18/seismic_ddms_openapi.yaml@df39d22ed32acfe80fcdbc5b554871b2c752a39a` | Microsoft's own organization distributes this service API document. Its document grant and [repository grant](https://raw.githubusercontent.com/microsoft/adme-samples/df39d22ed32acfe80fcdbc5b554871b2c752a39a/LICENSE) both permit redistribution; the latter covers the source directory. | `c2cfccb812fe482101a8f04597dfc5a9991a6b2748266c47ac91b6a5aae15383` | admissible; complete certified-pair generation succeeds, but crozier does not byte-match; registration pending repair |
| `formbricks/formbricks:docs/api-v2-reference/openapi.yml@bfe7933cb2882c99f2196aa6a46edd104cd7fbb8` | The publisher's own repository describes its cloud API at `app.formbricks.com/api/v2`. The [repository grant](https://raw.githubusercontent.com/formbricks/formbricks/bfe7933cb2882c99f2196aa6a46edd104cd7fbb8/LICENSE) places this `docs/` source outside its separately licensed directories and grants redistribution. | `4df0924663a08fbc0d591f6ae39069dcabd913af382b87011055569dea177770` | admissible; registered as corpus row 3001 ([attribution](#formbricks-map-example-attribution)) |
| `APIs/vercel.com/0.0.1/openapi.yaml@f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | The pinned aggregation declares `https://openapi.vercel.sh` as publisher origin and `api.vercel.com` as server. Its [aggregation grant](https://raw.githubusercontent.com/APIs-guru/openapi-directory/f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49/LICENSE) permits redistribution; no document-specific grant overrides it. | `a2010f343487d3f7618affe54f789f5487602331c0a8d03f49e9a7c547cf0499` | admissible pinned redistribution; not a string-const witness: its `oneOf` string constants are all untyped, so they merge into one enum and never enter the arm ([bound](#remaining-bounds-after-the-source-repairs)) |

The seismic generation used the already acquired source digest
`cdf6d45a8d6ec230dd2f2e73e14394f83cb562a1b19ab222ac63dd9f9c460ddf`
and freshly produced a complete 219-file SDK at the certified pair. Its first
comparison differs in discriminator class names, discriminator example fields,
typed object examples and an extension-property example. This is
**matched-pending repair**, not a registered byte-match or a
`none-registrable` result. The empty-object arm remains named unproven.

The three grants and publisher metadata were read from the shared acquisition
cache or through the guarded cache-filling client. No new witness generation
was used for the Formbricks or Vercel reviews. The null-example proof is now the
admitted lower-proof [harbor-signal-null fixture](../handwritten/harbor-signal-null/evidence.toml),
with its residual-only registry; it does not turn any pending candidate into a
real-specification proof.

## Optional fractional request-property attribution

The optional request-property context is generating but output-insensitive in
this measurement. The locally authored
[`before.json`](fractional-optional-attribution/before.json) declares optional
`Thing.v` as `integer` with `example: 0.7`; the
[`after.json`](fractional-optional-attribution/after.json) control removes only
that `example`. Both pass `fern check` and complete packaged generation at
CLI 5.163.1 / fern-python-sdk 5.41.3. The four `*.fern-*.log` files beside the
documents retain those runs.

All 36 raw Fern files are identical between the two documents. All 36 crozier
files are also identical between them. [`trees.tsv`](fractional-optional-attribution/trees.tsv)
records each complete tree's Contract A digest, before any normalization;
compare each generator's two rows, not the two generators' raw digests.
`crozier compare` additionally matches all 36 files against each document's
Fern output in both normal mode and with `CROZIER_FERN_STRICT=true`, using the
existing parity normalization and departure catalog. The crozier subprocesses
ran under `tests/corpus_match/corpus_offline_test.py`'s `deny_network` filter.

These documents use the existing
[optional request-property control](../../fern-refusals/example-type-mismatch/request-optional-control.yml)
shape, with its property changed to the integer example above.
This context is decided as output-insensitive in both generators, never proven.
Its Contract A differential pair is registered under
`schema-example-fractional-on-integer` in `../probe-expected/MANIFEST.tsv`; the
coverage row records `ignores` for this context and the existing refusal class
for the non-optional contexts. The measurement does not settle outstanding real
candidates in other contexts.

## Examples beside a `$ref` attribution

`schema-example-on-ref-to-object`, `schema-example-on-ref-to-enum` and
`schema-example-on-ref-to-union` are decided output-insensitive in both
generators, never proven. For each key, six locally authored before/after pairs
place the example beside a `$ref` to `Thing` (an object), `Choice` (a string
enum) or `Either` (a `oneOf`) in a different context, and each control removes
only that `example`:

| context | where the example sits |
|---|---|
| `request-body-root` | the request body schema itself (OpenAPI 3.1.0) |
| `required-request-property` | a required request-body property (OpenAPI 3.0.3; also the Contract A differential probe) |
| `required-request-property-openapi-3.1` | the same property in an OpenAPI 3.1.0 document |
| `array-item-reference-sibling` | an array's `items` |
| `required-query-parameter` | a required query parameter's schema |
| `optional-query-parameter` | an optional query parameter's schema |

Every document passed `fern check` and completed packaged generation at
CLI 5.163.1 / fern-python-sdk 5.41.3; the logs sit beside each pair under
`<target>-<context>-attribution/` (the 3.0.3 property pairs under
`<target>-required-ref-property-attribution/`, the array pairs under
`<target>-array-items-attribution/`). In all 18 pairs the complete raw Fern tree
is identical between the two documents, and so is crozier's, generated under
`tests/corpus_match/corpus_offline_test.py`'s `deny_network` filter with the
current build. Each pair's two comparison records are a row of
[the shared table](../output-insensitive.tsv).

The real declarer populations (93, 100 and 12 census rows) were re-preflighted
with crozier alone on the current build: every document it generated from moves
no generated file when its examples beside a `$ref` are deleted. No real
document is a witness, because no context of these keys changes output.

## Empty-object arm attribution

`schema-example-empty-object` is a `golden` feature; its
`src/emit.rs::ExampleCtx::value_from_example[if fields.is_empty\(\) \{]` arm was
decided output-insensitive, never proven, until the reconciled reach
measurement found all 5 of its regions executed by its byte-matched golden-only
witnesses, which since the previous measurement gained `microsoft-adme-seismic`
(corpus row 3004) and `rgb-lightning-node` (row 3203): it is now a reached arm in [the ledger](../golden-reach.tsv), and its row of
[the shared table](../output-insensitive.tsv) was withdrawn, since an arm is never
both reached and decided. The record below stays as the evidence that decision
rested on. The four real declarers the census
records executing the arm (two Meraki versions, Open Banking PCM and ADME
seismic) move no crozier-generated file when their empty-object examples are
deleted, so none is an output-sensitive witness. The locally
authored [`before.json`](empty-model-media-example-attribution/before.json)
puts `{value: {}}` in the request media type's `example`, where `value` refers
to an `Empty` component with no properties of its own; the
[`after.json`](empty-model-media-example-attribution/after.json) control drops
only that media-type example. An instrumented crozier built from this branch
executes all 5 of the arm's regions on the original and none on the control.
Both complete trees are identical between the two documents at the certified
pair (38 Fern files) and in crozier. The two documents are also committed as
`measured` probe trees (`empty-model-media-example` and
`empty-model-media-example-no-media-control` in `../probe-expected/MANIFEST.tsv`),
which crozier byte-matches. The comparison records were the arm's row of
the shared table and remain committed beside this record.

## Remaining bounds after the source repairs

This search renews three keys with the build carrying this branch's example and
union repairs, so no candidate is dismissed on behaviour those repairs changed.
[`remaining-bounds.tsv`](remaining-bounds.tsv) lists every candidate it read,
one row per distinct source digest: what crozier does with the original bytes
(and, for an arm key, how many of the arm's regions an instrumented build of
this branch executes on that document alone), its licence and provenance
outcome, and its certified-pair Fern baseline where one was run. Every crozier
run was offline under `tests/corpus_match/corpus_offline_test.py`'s
`deny_network` filter. Every Fern run held the shared generation lock, with a
600-second bound, retried once at 1800 seconds after a timeout. No new source
document was fetched; licence and grant reads went through the guarded shared
cache. [`ogc-licence-review.md`](ogc-licence-review.md) records why the OGC
document licence is not admissible.

- **`schema-example-array-null-element`** — 41 census rows, 35 distinct
  documents. Crozier generates 12 from their original bytes, and deleting
  their null-holding array examples moves no file (three controls are exact
  byte-range deletions; the other nine are round-trip controls whose base tree
  equals the original's). Crozier refuses the other 23. Of those, 14 are not
  admissible: 12 under the OGC licence and 2 that are third-party copies of
  another publisher's definition. Of the 9 admissible, Fern refuses 6; Fern
  generates `georust/ogcapi`, and deleting its examples moves none of Fern's
  files. The last two are unresolved: `52North/connected-systems-pygeoapi`'s
  `fern check` passed neither 600 nor 1800 seconds, and
  `brazil-data-cube/bdc-stac`'s baseline passed neither the 600-second
  three-run screen nor an 1800-second baseline-only run. Those two remain
  named unresolved candidates; nothing settles them.
- **`schema-example-outside-enum`** — 137 census rows. 111 hold no type shape
  the arm tests and 4 are registered goldens whose reach is already in the
  ledger. Of the 22 other distinct documents, none executes the arm: crozier
  generates 5 without reaching it and refuses 17. Of those 17, 2 are not
  admissible (a third-party copy and a document with no grant), and Fern
  refuses all 15 admissible ones.
- **`oneof-string-const-variant`** — 70 census rows. 41 hold no typed
  alternative beside the string `const`: their untyped constants merge into one
  enum, which never enters the arm. 2 have no located source and 4 are
  registered goldens. Of the 23 typed declarers, the only document executing
  the arm is a synthetic test router in tRPC's own test suite, which is not
  admissible. Of the six crozier refuses, Fern refuses AstrLink and
  coolercontrol, three are not admissible (two synthetic emulator contracts and
  Peridio's field-of-use grant), and 52North is unresolved as above.

Within these bounded populations no admissible real document both generates
at the certified pair and changes output for the key or arm. So each key's
renewed outcome is `none-registrable` in the table above, and the hand-written
fixtures `lunar-null-labels`, `enum-media-selection` and `compass-choice` are
admitted as lower proof. Each is output-sensitive: deleting the scoped example
or `const` from its document changes the same files in Fern's complete tree and
in crozier's, which `remaining_witnesses_have_output_sensitive_examples_and_enum_alternatives`
in `crates/crozier-e2e/tests/e2e.rs` re-checks against committed controls under
`docs/fern-measurements/remaining-examples/`.

## Formbricks map-example attribution

`schema-example-object-on-map`'s
`src/emit.rs::ExampleCtx::example_matches_type_through[=TypeRef::Dict\(_, _\) => value.is_object\(\),]`
arm is proven by a real specification: corpus row 3001, `formbricks`, the
publisher's own `docs/api-v2-reference/openapi.yml` at
`bfe7933cb2882c99f2196aa6a46edd104cd7fbb8` (source SHA-256
`6b83214a2f72ea3fc49df82eb135ddf6d7963723295edea2c4feef526e502d61`; its grant is
reviewed under [Publisher reviews](#publisher-reviews-after-the-recovered-queue)).
Its scoped golden test executes both of the arm's regions
([ledger](../golden-reach.tsv)), and crozier byte-matches its complete 418-file
certified-pair tree in normal and strict mode.

The paired control [`after.yml`](formbricks-map-attribution/after.yml) is the
original [`before.yml`](formbricks-map-attribution/before.yml) with exactly one
line deleted, the `example` of the management-responses request body's `data`
map (line 787); it is committed as the measurement
`remaining-examples/formbricks-no-map-example`. Deleting it changes the same two
files, `reference.md` and `src/fern/management_api_responses/client.py`, in
Fern's complete tree and in crozier's; the two comparison records sit beside the
documents, and `remaining_witnesses_have_output_sensitive_examples_and_enum_alternatives`
re-checks that motion through the binary.

## Map-value branch search

`src/ir.rs::InlineHoister::prop_type_ref`'s operation-scoped map branch lowers a
structured, unreferenced `additionalProperties` value through the component
builder. The census reads it as four features, cases 19a to 19d:
`property-map-value-enum`, `-struct`, `-oneof` and `-anyof`. `formbricks`
(corpus row 3001) already reaches the branch for `-anyof`. This search covers the
other three.

**Population.** The same cached pools as [the search](#the-search): APIs.guru at
`f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49`, and the GitHub code-search and
Sourcegraph acquisitions. That is 12,713 distinct documents, read from the
shared cache with no new document fetched. Of them, 449 declare at least one of
the three keys' census selectors. An instrumented crozier build ran over each
declarer alone. On 51 of them it executes the branch (17 of its 18 regions),
and those 51 are the candidates. The 106, 304 and 83 declarers in the verdict
table count documents per key; one document can declare several.
Licence and grant reads went through `tools/witness-search/rate_limit_guard.py`
and the shared response cache under `~/.cache/crozier/`. Every crozier run was
offline under `tests/corpus_match/corpus_offline_test.py`'s `deny_network`. Every
Fern run held the shared generation lock at CLI 5.163.1 and
`fernapi/fern-python-sdk` 5.41.3. Whole-tree comparisons used the public
`crozier compare` in normal and `fern-strict` mode.

[`map-value-bounds.tsv`](map-value-bounds.tsv) lists every candidate, one row per
distinct source digest: which keys it declares, what crozier does with its
original bytes, the branch regions executed, its licence and provenance outcome,
its Fern baseline where one was run, and the whole-tree comparison.

- **`property-map-value-struct`** is witnessed by corpus row 3002, `panoptes`,
  the KNAW Humanities Cluster's own `docs/openapi.yaml` (GPL-3.0). Its request
  bodies map facet names to inline structs. Crozier byte-matches its complete
  certified-pair tree. The control
  `remaining-examples/panoptes-no-struct-map-value` deletes only the `properties`
  of the `search` body's `facets` map value. That changes the same files in
  Fern's complete tree and in crozier's.
- **`property-map-value-enum`** is witnessed by corpus row 3003, `fletch-mcp`,
  Fletch's own `docs/openapi-2026-09-13.json` (MIT). Its responses map account
  types to an inline string enum (`tradability_by_account_type`). Crozier
  byte-matches its complete tree once a map value whose `type` list names
  `null` is typed `Optional`, as Fern types it. The control
  `remaining-examples/fletch-mcp-no-enum-map-value` deletes only one value's
  `enum`, a single byte range of the original. That moves the same five files in
  both generators. `OpenRecruiterTools/linkedin-toolkit` also byte-matches; one
  witness is enough.
- **`property-map-value-oneof`** has no registrable real witness in this
  population. Eleven candidates declare it.
  - Four are not admissible: `lobehub` at two revisions and `recallnet/js-recall`
    fail the licence screen, and `Lap-Platform/LAP`'s copy of Vercel's
    definition is not the publisher's.
  - The `ballerina-platform/openapi-tools` document is a copy of Vercel's
    definition among a generator's test resources, not a publisher service
    source.
  - Crozier refuses `christophhart/HISE`, and its pinned commit grants nothing.
  - Fern refuses `getchat-dev/node-sdk`.
  - The four that generate in both are admissible: `mishrasanjeev/grantex`,
    `crate-works/ro-crate-api`, APIs.guru's `journy.io` and APIs.guru's
    `vercel.com`. Each still differs from Fern's tree, for reasons
    outside this branch, which the bounds table names.

  The renewed outcome is `none-registrable`, so the hand-written fixture
  `shelf-labels-map-variants` is admitted as lower proof. It is a request
  body's `labels` map whose value is an inline `oneOf` of a string and an
  integer. Crozier byte-matches Fern's complete tree in normal and strict mode.
  The control `remaining-examples/shelf-labels-map-variants-control` deletes only
  that value's `oneOf`, and both generators then change the same five entries.

`remaining_witnesses_have_output_sensitive_examples_and_enum_alternatives` in
`crates/crozier-e2e/tests/e2e.rs` re-checks all three controls through the binary.
Each other mismatching candidate is recorded as a follow-up for its own root
cause. Only Vercel's residual touches a map value, its `items` map of a `oneOf`
whose first member is itself a `oneOf` with a `null` alternative. Fern types that
member `Optional` and drops the `null`; crozier keeps a plain union holding
`typing.Any`. Crozier lowers the same shape identically when it sits in a
component schema, so the cause is the shared nested-union lowering, not the
operation-scoped branch this search proves.

