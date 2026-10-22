# Witness search for the unproven features and arms

This bounded search reads the populations below for the twelve unproven keys
and the additional arm covers removed by the certified-pair retarget. Its
Fern measurements use CLI 5.163.1 and `fernapi/fern-python-sdk` 5.41.3.
This is an **unfinished screen**, not a claim that no real witness exists.
A key with outstanding candidates cannot yet cite this record as
`none-registrable`; the qualifying renewed searches are identified below. The
zero-declarer features are covered by `observatory-example-arrays`.
`onmyshelf-api` proves digit-leading methods, and `harbor-signal-null` supplies
the weaker residual-only null proof. The remaining named features and arms
keep their incomplete search outcomes below.

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
| `discriminator-mapping` | `schema.discriminator.mapping` | a declarer of the selector on which that instrumented run executes `src/ir.rs::Builder::discriminated_union[if union_target \{]` or `src/emit.rs::ExampleCtx::named_value_inner[Some\(m\) if m\.wrapped => \{]` |
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
hand-written cover. Pending candidates must be resolved before a
`none-registrable` renewed-search line can be written. The census count below
is document/key rows, not a count of distinct APIs or successful witnesses.

| key | verdict | declaring documents | registration status |
|---|---|---|---|
| `discriminator-mapping` | `search-incomplete` | 899 | outstanding: screen and parity/reach review not complete |
| `oneof-string-const-variant` | `search-incomplete` | 70 | outstanding: screen and parity/reach review not complete |
| `operation-id-digit-leading-method` | `search-incomplete` | 97 | registered: corpus row 3000, `onmyshelf-api`; complete certified-pair SDK byte-match |
| `schema-example-array-null-element` | `search-incomplete` | 41 | outstanding: screen and parity/reach review not complete |
| `schema-example-empty-object` | `search-incomplete` | 171 | outstanding: screen and parity/reach review not complete |
| `schema-example-fractional-on-integer` | `search-incomplete` | 20 | outstanding: screen and parity/reach review not complete |
| `schema-example-null` | `search-incomplete` | 28 | cached attribution preflight complete: no qualifying byte-moving witness; admitted lower-proof `harbor-signal-null` fixture |
| `schema-example-object-on-map` | `search-incomplete` | 636 | outstanding: screen and parity/reach review not complete |
| `schema-example-on-ref-to-enum` | `search-incomplete` | 100 | outstanding: screen and parity/reach review not complete |
| `schema-example-on-ref-to-object` | `search-incomplete` | 93 | outstanding: screen and parity/reach review not complete |
| `schema-example-on-ref-to-union` | `search-incomplete` | 12 | outstanding: screen and parity/reach review not complete |
| `schema-example-outside-enum` | `search-incomplete` | 137 | outstanding: screen and parity/reach review not complete |

| `schema-example-temporal-duplicate-element` | `search-incomplete` | 0 | no declarer in the bounded populations |
| `schema-example-union-ref-sentinel` | `search-incomplete` | 0 | no declarer in the bounded populations |

The two zero-declarer keys have `none-registrable` outcomes within these
bounded populations. The null-example key also has that outcome after the
bounded attribution preflight below. The other unresolved keys have no such
conclusion yet. In
particular, the ledger contains successful Fern and licence screens for the
digit-leading method, array-null element, examples beside object/enum/union
references, null example, empty-object arm, object-on-map arm and string-const
variant arm. Those candidates take precedence over authoring a substitute.
The residual-only hand-written rule for `schema-example-null` remains a
fallback only if no real witness can be registered.

## Renewed search

| key | verdict | outcome |
|---|---|---|
| `schema-example-temporal-duplicate-element` | `search-incomplete` | none-registrable |
| `schema-example-union-ref-sentinel` | `search-incomplete` | none-registrable |
| `schema-example-null` | `search-incomplete` | none-registrable |

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
`src/emit.rs::ExampleCtx::named_value_inner[Some\(m\) if m\.wrapped => \{]`,
and `oneof-string-const-variant`'s
`src/ir.rs::InlineHoister::hoist_union_variant[if let Some\(values\) = string_enum_values\(variant\) \{]`.
The first already has registered golden reach; the other three remain in this
search. This inventory does not count renamed handling sites as lost proof.

## Pending nested-mapping defect

The from-scratch [nested discriminator measurement](../../fern-measurements/examples/nested-discriminator-wire/README.md)
executes the certified SDK against its source schema: the SDK emits a nested
`value` envelope where the schema requires a flat object and rejects a valid
flat response; its README example also fails compilation. This is a documented
Fern runtime defect pending a separate crozier repair, not a byte-matched arm
proof. Neither nested mapping arm leaves the named unproven list on this evidence.

## Publisher reviews after the recovered queue

These reviews apply the [corpus grant rule](../../corpus-licensing.md) to the
pinned source paths, rather than assuming a successful generator run establishes
redistribution rights. They supplement the 83 formal screening records; they do
not claim the 39 outstanding queue entries were screened.

| candidate | publisher provenance and grant scope | grant bytes SHA-256 | outcome |
|---|---|---|---|
| `microsoft/adme-samples:rest-apis/M18/seismic_ddms_openapi.yaml@df39d22ed32acfe80fcdbc5b554871b2c752a39a` | Microsoft's own organization distributes this service API document. Its document grant and [repository grant](https://raw.githubusercontent.com/microsoft/adme-samples/df39d22ed32acfe80fcdbc5b554871b2c752a39a/LICENSE) both permit redistribution; the latter covers the source directory. | `c2cfccb812fe482101a8f04597dfc5a9991a6b2748266c47ac91b6a5aae15383` | admissible; complete certified-pair generation succeeds, but crozier does not byte-match; registration pending repair |
| `formbricks/formbricks:docs/api-v2-reference/openapi.yml@bfe7933cb2882c99f2196aa6a46edd104cd7fbb8` | The publisher's own repository describes its cloud API at `app.formbricks.com/api/v2`. The [repository grant](https://raw.githubusercontent.com/formbricks/formbricks/bfe7933cb2882c99f2196aa6a46edd104cd7fbb8/LICENSE) places this `docs/` source outside its separately licensed directories and grants redistribution. | `4df0924663a08fbc0d591f6ae39069dcabd913af382b87011055569dea177770` | admissible; recovered generation screen succeeds; complete parity and arm proof remain outstanding |
| `APIs/vercel.com/0.0.1/openapi.yaml@f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` | The pinned aggregation declares `https://openapi.vercel.sh` as publisher origin and `api.vercel.com` as server. Its [aggregation grant](https://raw.githubusercontent.com/APIs-guru/openapi-directory/f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49/LICENSE) permits redistribution; no document-specific grant overrides it. | `a2010f343487d3f7618affe54f789f5487602331c0a8d03f49e9a7c547cf0499` | admissible pinned redistribution; complete parity and string-const arm proof remain outstanding |

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
