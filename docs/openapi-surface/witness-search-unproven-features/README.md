# Witness search for the unproven features and arms

This bounded search reads the populations below for the twelve unproven keys
and the additional arm covers removed by the certified-pair retarget. Its
Fern measurements use CLI 5.163.1 and `fernapi/fern-python-sdk` 5.41.3.
This is an **unfinished screen**, not a claim that no real witness exists.
A key with outstanding candidates cannot yet cite this record as
`none-registrable`; the two zero-declarer keys are identified below. The two zero-declarer features are covered by the from-scratch
`observatory-example-arrays` fixture; other features and arms remain open.

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
- **The registered corpus.** Every OpenAPI 3 document under `tests/fixtures/`
  (each committed corpus source and each vendored fixture `openapi.*`): 274.
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
| `operation-id-digit-leading-method` | `search-incomplete` | 97 | outstanding: screen and parity/reach review not complete |
| `schema-example-array-null-element` | `search-incomplete` | 41 | outstanding: screen and parity/reach review not complete |
| `schema-example-empty-object` | `search-incomplete` | 171 | outstanding: screen and parity/reach review not complete |
| `schema-example-fractional-on-integer` | `search-incomplete` | 20 | outstanding: screen and parity/reach review not complete |
| `schema-example-null` | `search-incomplete` | 28 | outstanding: screen and parity/reach review not complete |
| `schema-example-object-on-map` | `search-incomplete` | 636 | outstanding: screen and parity/reach review not complete |
| `schema-example-on-ref-to-enum` | `search-incomplete` | 100 | outstanding: screen and parity/reach review not complete |
| `schema-example-on-ref-to-object` | `search-incomplete` | 93 | outstanding: screen and parity/reach review not complete |
| `schema-example-on-ref-to-union` | `search-incomplete` | 12 | outstanding: screen and parity/reach review not complete |
| `schema-example-outside-enum` | `search-incomplete` | 137 | outstanding: screen and parity/reach review not complete |

| `schema-example-temporal-duplicate-element` | `search-incomplete` | 0 | no declarer in the bounded populations |
| `schema-example-union-ref-sentinel` | `search-incomplete` | 0 | no declarer in the bounded populations |

The two zero-declarer keys have `none-registrable` outcomes within these
bounded populations. The other keys have no such conclusion yet. In
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
