# Schema combination interaction witnesses

This bounded search covers the four `prove-schema-combinations` keys named as
unproven at base `bc66bfb087fbd34abfe89f1075912b103e848896`: one in `examples`
and three in `models-unions-refs`. The certified pair is Fern CLI 5.163.1 with
`fernapi/fern-python-sdk` 5.41.3. All four now have a from-scratch
[`orchard-dispatch-schemas`](../handwritten/orchard-dispatch-schemas/) proof.

## Populations read

Measured on 2026-10-28, without a specification fetch or a live search request:

- **APIs.guru:** `APIs-guru/openapi-directory` at
  `f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49`. The cached archive's verified
  SHA-256 is
  `816adb9fb4e19dc9ab28d7ad95363de146251fb41164abdb86f953f9f400c644`.
  Every JSON/YAML document in the extracted archive was read.
- **Registered:** every JSON/YAML file below `tests/fixtures/` at the base above,
  including every registered source. Individual corpus revisions and grants
  remain in `tests/fixtures/corpus-sources.tsv` and `NOTICE`.
- **Earlier acquisitions:** the union of both retained `candidate-documents.json`
  manifests for each of `github-code-search` and `sourcegraph`. Each acquired
  document was read and its bytes verified against its content-addressed
  filename. The full publisher revision is part of each identity in
  [census.tsv](census.tsv). Repository exclusions use `excluded_repository` and
  `normalize_repo` from `tools/witness-search/witness-search-github-index.py`.

Several acquired identities name identical bytes. The census groups those
identities by population and digest; their site counts agree. The population
counts below keep identities and distinct byte digests separate. OpenAPI and
unreadable counts are identity counts.

| population | identities read | distinct digests | OpenAPI 3 | unreadable |
|---|---:|---:|---:|---:|
| APIs.guru | 4138 | 4138 | 1970 | 0 |
| registered | 977 | 626 | 293 | 0 |
| github-code-search | 5619 | 5125 | 5256 | 65 |
| sourcegraph | 5188 | 4078 | 3694 | 20 |

[unreadable.tsv](unreadable.tsv) preserves the unreadable identities and their
diagnostics. They contribute no zero counts and remain outside the declaration
measurement. No code search, portal or registry was queried.

### Detectors and calibration

A detector requires its census conjunction **and** an instrumented crozier run
executing every interaction site that the key's unchanged row in
[`golden-reach-sites.tsv`](../golden-reach-sites.tsv) declares.

| key | census conjunction | interaction |
|---|---|---|
| `combo-allof-nullable` | `schema.allOf&schema.nullable` | nullable single-reference alias lowering in `Builder::add_named_shape` |
| `combo-anyof-beside-properties` | `schema.anyOf&schema.properties:non-empty` | sibling-field lowering in `Builder::add_named_shape` and shared-base field collection in `Builder::discriminated_union` |
| `combo-oneof-beside-properties` | `schema.oneOf&schema.properties:non-empty` | the same two declared sites, over `oneOf` |
| `combo-oneof-schema-example` | `schema.example&schema.oneOf` | `referenced_example_literal` rejects a referenced component's example that does not validate against its `oneOf` |

Enumeration used the census's `OBJECTS` walk, reference-node stopping rules and
`conjunction_holds` evaluator. Its declaration pass was restricted to the four
conjunctions' schema fields and `schema.properties:non-empty`; it did not evaluate
unrelated surface predicates. JSON used the standard-library reader. YAML used
PyYAML 6.0.3's C safe loader, falling back to the repository reader. A second read
kept timestamps and the YAML `=` scalar as strings. The four counts agreed on
all 15,837 readable identities between these reads, and on all 883 completed
identities of the stock census run. No complete stock run is claimed. Three
superseded thread-based runs were stopped; the completed process-based reads
supply the counts here.

## Screening bound

The registered witnesses were considered first, through the base's committed
[`golden-reach.tsv`](../golden-reach.tsv). It reports the missing interaction
unreached for every registered golden-only declarer of these keys. Ten registered
golden tests were additionally rerun in isolation with `golden-reach.py measure`:
`ecommerce-ai-skills-runtime`, `free5gc-namf-communication`,
`free5gc-pdu-session`, `onevoice`, `qredence-fleet-rlm`, `rgb-lightning-node`,
`webflow-v2`, `zulip`, `zulip-jentic` and `zulip-jentic-entry`. Their complete
goldens byte-matched; their isolated profiles supplied no complete interaction
witness.

The next bound was thirteen unique APIs.guru declarers, run through the
instrumented binary at the base above with a 60-second generation timeout.
Five generated, seven were refused by crozier, and one timed out. None of the
twelve completed profiles executed an interaction site. A crozier refusal here
is not a certified-pair refusal measurement. The timeout supplies no branch
verdict.

Every declarer has its site count, digest and screening state in `census.tsv`.
Its `outside instrumented screen bound` rows still owe interaction reach,
licence and certified-generation screens. The timed-out document owes a longer
instrumented run. A crozier-refused document still owes a certified-pair run
before its refusal can be classified. The search admits no real witness;
remaining declarers are outstanding, rather than screened negatives. No corpus
row or refusal class changes as a result of this bound.

## Verdicts

The counts are distinct `(population, digest)` declarers in `census.tsv`.
Each fixture cover cites this section.

| key | outcome | declarers | proof |
|---|---|---:|---|
| `combo-allof-nullable` | `search-incomplete` | 377 | `orchard-dispatch-schemas`: nullable alias beside a single object reference |
| `combo-anyof-beside-properties` | `search-incomplete` | 337 | `orchard-dispatch-schemas`: both required-only alternatives and inline tagged alternatives beside properties |
| `combo-oneof-beside-properties` | `search-incomplete` | 390 | `orchard-dispatch-schemas`: the corresponding `oneOf` shapes |
| `combo-oneof-schema-example` | `search-incomplete` | 270 | `orchard-dispatch-schemas`: a referenced union's example matches both alternatives and is rejected as a `oneOf` example |

## Renewed search

These outcomes concern admission within the screening bound above. The census
retains the remaining candidates and their outstanding screens for continuation.

| key | outcome | admission |
|---|---|---|
| `combo-allof-nullable` | `none-registrable` | no generating, admissible branch-reaching witness established within the bound |
| `combo-anyof-beside-properties` | `none-registrable` | no generating, admissible branch-reaching witness established within the bound |
| `combo-oneof-beside-properties` | `none-registrable` | no generating, admissible branch-reaching witness established within the bound |
| `combo-oneof-schema-example` | `none-registrable` | no generating, admissible branch-reaching witness established within the bound |

## Hand-written proof

The orchard document was authored from scratch. Its feature-level covers cite
this record. `handwritten-reach.tsv` measures its execution of all six declared
interaction-site entries, including both entries for each sibling-properties
key. The alias, both union forms and the ambiguous example are part of one
complete SDK comparison.

The certified pair freshly generated its complete `fern-expected/` tree under
`python_enums`. A second fresh run under `literals` supplies the reduced overlay
under `docs/fern-measurements/union-literals/orchard-dispatch-schemas/`.
`handwritten_fixtures_match_fern_goldens` and
`union_shapes_match_complete_goldens_in_both_enum_modes` gate those references.
No generated reference was edited to fit crozier. Only the existing SDK-identity,
type-import-order and generator-configuration metadata departures apply.
