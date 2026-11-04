# Withdrawal remainder search

## Bound and inputs

This search reads the four source shapes left by the
[Nexmo withdrawal](../withdrawn-witnesses/nexmo-conversation.md#the-reach-row-223-alone-carried).
The census selectors describe declarations, not a claim that an emitted line
has executed. The controls in `WithdrawnWitnessSelectorTests` read the actual
`ref-pointer-walk/openapi.yml`, distinguish copied references from ordinary
ones, and distinguish plain timestamps from quoted, temporal, required and
header examples.

[withdrawal-census.tsv](withdrawal-census.tsv) records the offline walk of all 336 acquired source
identities in the current registry, including the original authored fixtures;
none failed to parse. Authored fixtures are controls, not real candidates.
Seven additional handed-off documents were recovered from the preflight cache
by matching their exact SHA-256 against `handed-off/documents.tsv`. The eighth
is Cyoda, fetched through `witness-acquire-github.py` and its rate-limit guard:
`Cyoda/cyoda-go:docs/cyoda/openapi.yml` at
`0021e97806811b369a13d87701fe4a6454ac99fa`, SHA-256
`5ce9d61397d9e296c2de0644bfe07bb90bf500e81f5472a8773f5fddcb9432b9`.
Its bytes match the handoff. The other 139 handoff hashes were not recovered
from that cache; some overlap registered sources, but this walk does not claim
complete coverage of the handoff population.

The shared read-only APIs.guru archive at
`f04b8d0bcd39c52e1cf3ad7a5fe744709832ae49` was subsequently located.
[archive-census.tsv.gz](archive-census.tsv.gz) records the new selectors over
all 1970 OpenAPI 3 documents, with no unreadable document. All 4138 archive
document hashes were verified against the acquisition manifest; archive SHA-256
is `7a0bdff93afc94d373c7e596d24739cc8aff7d93c4e8b75a82e9c0cf7e0606a1`.
The acquired GitHub and Sourcegraph pools remain unavailable, and the handoff
walk remains partial. No live code search was run. No new witness is registered.

## Verdicts

| key | selector | verdict | reason |
|---|---|---|---|
| `withdrawn-properties-reference-copy` | `schema.$ref:properties-copy` | `search-incomplete` | Three registered sources declare the broader copying predicate; their pointers end on properties or items, not the withdrawn plain component or composition-member forms. The acquired pools are unavailable, and the handoff walk is partial. |
| `withdrawn-properties-copy-variant-name` | `schema.oneOf:properties-copy-type-variant` | `search-incomplete` | No certified witness established; archive declarers remain unscreened. The acquired pools are unavailable, and the handoff walk is partial. |
| `withdrawn-properties-copy-inferred-type` | `schema.oneOf:properties-copy-inferred-type` | `search-incomplete` | No certified witness established; archive declarers remain unscreened. The acquired pools are unavailable, and the handoff walk is partial. |
| `withdrawn-optional-nontemporal-timestamp` | `parameter.example:optional-nontemporal-yaml-timestamp` | `search-incomplete` | No real witness found. Thirty archive documents declare the timestamp selector and remain unscreened; Cyoda does not. The acquired pools are unavailable, and the handoff walk is partial. |

The broader reference-copy selector counts `dnd5eapi.co` (2),
`openbanking-brasil-directory` (1), and `embedpdf-cloudpdf` (1160).
The handed-off `ogcincubator/developer-website-v3` document contributes one
more declaration. A broader pointer-copy declaration does not establish the
withdrawn union naming and inferred-tag behaviours.

**No certified real witness of the optional non-temporal YAML-timestamp drop
has been established here.** The archive supplies 30 declaration candidates;
a declaration alone does not establish the generated drop. Cyoda's unquoted parameter timestamps have
`format: date-time`, as the
[certified example-value measurement](../../fern-measurements/handed-off/example-values/yaml-timestamp-parameter-example/README.md)
already records. They are temporal and do not satisfy the selector. This
search does not override the timestamp ruling or that measurement.

## Authored verdicts

All 31 authored cases have a decided tier in
[`evidence-tiers.tsv`](../authored-probes/evidence-tiers.tsv) (format version 1).
Six single naming behaviours become hand-written fixtures. Twenty-five
combination cases remain **open**, under `exhausted-combination-fallback` and
the planner's explicit declaration-census screening bound. Open means no real
witness or admitted combination fixture has established the complete scenario;
it does not mean non-generation. The case's existing certified measurement is
still byte-gated separately from its evidence tier.

[`authored-census.tsv`](authored-census.tsv) records declarations on the acquired
registered sources, the eight recoverable handed-off documents and the 31 authored controls. A selector is a candidate
screen, not proof that all contextual conditions of its authored case hold.
[`unscreened.tsv`](unscreened.tsv) lists **every non-local declaring candidate** with
its hash, reading and outstanding screen, including the archive declarations. The original authored source fixtures
are local controls, not real candidates. The planner bounded this pass at that
declaration census because exact-trigger and certified-pair screening of the
broader declarers would require more generations than this step can run under
the shared lock. Each listed candidate needs its complete trigger validated
(placement, requiredness, tag/default and pointer shape), followed by a
certified-pair generation and complete comparison on the exact bytes. No listed
candidate is silently treated as rejected or byte-matching.

The outstanding populations for **every** row are the unavailable acquired
GitHub and Sourcegraph pools and the unrecovered handed-off documents described
above. Archive declarations are included in `unscreened.tsv`; their exact-trigger
and certified screens remain outstanding at the approved declaration bound. The older
committed census tables have no readings for these new selectors. The eight
recoverable handoff documents also have the new readings in `authored-census.tsv`.

| key | verdict | declaring candidates | outstanding work |
|---|---|---|---|
| `combo-allof-unresolved-nested-pointer` | `search-incomplete` | 3 | Restore the missing populations; screen each `combo-allof-unresolved-nested-pointer` declarer in `unscreened.tsv` for the complete trigger and against the certified pair. |
| `combo-array-defs-pointer` | `search-incomplete` | 1 | Restore the missing populations; screen each `combo-array-defs-pointer` declarer in `unscreened.tsv` for the complete trigger and against the certified pair. |
| `combo-array-unresolved-nested-pointer` | `search-incomplete` | 6 | Restore the missing populations; screen each `combo-array-unresolved-nested-pointer` declarer in `unscreened.tsv` for the complete trigger and against the certified pair. |
| `combo-body-property-named-as-path-param` | `search-incomplete` | 432 | Restore the missing populations; screen each `combo-body-property-named-as-path-param` declarer in `unscreened.tsv` for the complete trigger and against the certified pair. |
| `combo-header-array-accepted-placements` | `search-incomplete` | 3 | Restore the missing populations; screen each `combo-header-array-accepted-placements` declarer in `unscreened.tsv` for the complete trigger and against the certified pair. |
| `combo-header-string-default` | `search-incomplete` | 66 | Restore the missing populations; screen each `combo-header-string-default` declarer in `unscreened.tsv` for the complete trigger and against the certified pair. |
| `combo-map-unresolved-nested-pointer` | `search-incomplete` | 2 | Restore the missing populations; screen each `combo-map-unresolved-nested-pointer` declarer in `unscreened.tsv` for the complete trigger and against the certified pair. |
| `combo-nullable-allof-parent-own-property` | `search-incomplete` | 3 | Restore the missing populations; screen each `combo-nullable-allof-parent-own-property` declarer in `unscreened.tsv` for the complete trigger and against the certified pair. |
| `combo-property-anyof-composed-sibling` | `search-incomplete` | 5 | Restore the missing populations; screen each `combo-property-anyof-composed-sibling` declarer in `unscreened.tsv` for the complete trigger and against the certified pair. |
| `combo-property-defs-pointer` | `search-incomplete` | 1 | Restore the missing populations; screen each `combo-property-defs-pointer` declarer in `unscreened.tsv` for the complete trigger and against the certified pair. |
| `combo-property-unresolved-nested-pointer` | `search-incomplete` | 7 | Restore the missing populations; screen each `combo-property-unresolved-nested-pointer` declarer in `unscreened.tsv` for the complete trigger and against the certified pair. |
| `combo-request-unresolved-nested-pointer` | `search-incomplete` | 0 | Restore the missing populations; screen each `combo-request-unresolved-nested-pointer` declarer in `unscreened.tsv` for the complete trigger and against the certified pair. |
| `combo-required-query-array-enum-items` | `search-incomplete` | 29 | Restore the missing populations; screen each `combo-required-query-array-enum-items` declarer in `unscreened.tsv` for the complete trigger and against the certified pair. |
| `combo-response-unresolved-nested-pointer` | `search-incomplete` | 0 | Restore the missing populations; screen each `combo-response-unresolved-nested-pointer` declarer in `unscreened.tsv` for the complete trigger and against the certified pair. |
| `combo-tag-only-operation-id` | `search-incomplete` | 2 | Restore the missing populations; screen each `combo-tag-only-operation-id` declarer in `unscreened.tsv` for the complete trigger and against the certified pair. |
| `combo-unrequired-tag-anyof-reference` | `search-incomplete` | 75 | Restore the missing populations; screen each `combo-unrequired-tag-anyof-reference` declarer in `unscreened.tsv` for the complete trigger and against the certified pair. |
| `combo-unrequired-tag-oneof-reference` | `search-incomplete` | 114 | Restore the missing populations; screen each `combo-unrequired-tag-oneof-reference` declarer in `unscreened.tsv` for the complete trigger and against the certified pair. |
| `model-property-construct` | `search-incomplete` | 0 | Restore the missing populations; screen each `model-property-construct` declarer in `unscreened.tsv` for the complete trigger and against the certified pair. |
| `schema-type-name-component` | `search-incomplete` | 0 | Restore the missing populations; screen each `schema-type-name-component` declarer in `unscreened.tsv` for the complete trigger and against the certified pair. |

The header-array candidate `komga` declares referenced object items, rather than
the probes' inline string items. `auto-agent-protocol` declares `$defs`
pointers, but not the probes' pointer through a `properties` segment.
`bbci.co.uk` declares `Search_` tagged `Search`; its source is acquired, but its
golden was dropped after generation failed, so it is an outstanding certified
screen rather than an established witness. The remaining broader candidates
are retained individually in `unscreened.tsv`, including candidates whose
complete trigger has not yet been checked. No new witness is registered.

## Renewed authored search

| key | result | scope |
|---|---|---|
| `schema-type-name-component` | `none-registrable` | No registered declarer of the component override selector; missing external populations remain outstanding. |
| `model-property-construct` | `none-registrable` | No registered declarer of the model API property selector; missing external populations remain outstanding. |

These two single-feature rows may rest on hand-written evidence with a renewed
`search-incomplete` search. The combination cases may not: their search is
incomplete, so ruling 8 leaves them open. No search here reads `exhausted`, and
no generated case is presented as a limitation.

## Missing populations

| key | population | why not screened |
|---|---|---|
| `combo-allof-unresolved-nested-pointer` | acquired GitHub and Sourcegraph pools | Inputs not retained on this host; the planner directed that the unavailable population not be reacquired. |
| `combo-allof-unresolved-nested-pointer` | unrecovered handed-off documents | Inputs not retained on this host; the planner directed that the unavailable population not be reacquired. |
| `combo-array-defs-pointer` | acquired GitHub and Sourcegraph pools | Inputs not retained on this host; the planner directed that the unavailable population not be reacquired. |
| `combo-array-defs-pointer` | unrecovered handed-off documents | Inputs not retained on this host; the planner directed that the unavailable population not be reacquired. |
| `combo-array-unresolved-nested-pointer` | acquired GitHub and Sourcegraph pools | Inputs not retained on this host; the planner directed that the unavailable population not be reacquired. |
| `combo-array-unresolved-nested-pointer` | unrecovered handed-off documents | Inputs not retained on this host; the planner directed that the unavailable population not be reacquired. |
| `combo-body-property-named-as-path-param` | acquired GitHub and Sourcegraph pools | Inputs not retained on this host; the planner directed that the unavailable population not be reacquired. |
| `combo-body-property-named-as-path-param` | unrecovered handed-off documents | Inputs not retained on this host; the planner directed that the unavailable population not be reacquired. |
| `combo-header-array-accepted-placements` | acquired GitHub and Sourcegraph pools | Inputs not retained on this host; the planner directed that the unavailable population not be reacquired. |
| `combo-header-array-accepted-placements` | unrecovered handed-off documents | Inputs not retained on this host; the planner directed that the unavailable population not be reacquired. |
| `combo-header-string-default` | acquired GitHub and Sourcegraph pools | Inputs not retained on this host; the planner directed that the unavailable population not be reacquired. |
| `combo-header-string-default` | unrecovered handed-off documents | Inputs not retained on this host; the planner directed that the unavailable population not be reacquired. |
| `combo-map-unresolved-nested-pointer` | acquired GitHub and Sourcegraph pools | Inputs not retained on this host; the planner directed that the unavailable population not be reacquired. |
| `combo-map-unresolved-nested-pointer` | unrecovered handed-off documents | Inputs not retained on this host; the planner directed that the unavailable population not be reacquired. |
| `combo-nullable-allof-parent-own-property` | acquired GitHub and Sourcegraph pools | Inputs not retained on this host; the planner directed that the unavailable population not be reacquired. |
| `combo-nullable-allof-parent-own-property` | unrecovered handed-off documents | Inputs not retained on this host; the planner directed that the unavailable population not be reacquired. |
| `combo-property-anyof-composed-sibling` | acquired GitHub and Sourcegraph pools | Inputs not retained on this host; the planner directed that the unavailable population not be reacquired. |
| `combo-property-anyof-composed-sibling` | unrecovered handed-off documents | Inputs not retained on this host; the planner directed that the unavailable population not be reacquired. |
| `combo-property-defs-pointer` | acquired GitHub and Sourcegraph pools | Inputs not retained on this host; the planner directed that the unavailable population not be reacquired. |
| `combo-property-defs-pointer` | unrecovered handed-off documents | Inputs not retained on this host; the planner directed that the unavailable population not be reacquired. |
| `combo-property-unresolved-nested-pointer` | acquired GitHub and Sourcegraph pools | Inputs not retained on this host; the planner directed that the unavailable population not be reacquired. |
| `combo-property-unresolved-nested-pointer` | unrecovered handed-off documents | Inputs not retained on this host; the planner directed that the unavailable population not be reacquired. |
| `combo-request-unresolved-nested-pointer` | acquired GitHub and Sourcegraph pools | Inputs not retained on this host; the planner directed that the unavailable population not be reacquired. |
| `combo-request-unresolved-nested-pointer` | unrecovered handed-off documents | Inputs not retained on this host; the planner directed that the unavailable population not be reacquired. |
| `combo-required-query-array-enum-items` | acquired GitHub and Sourcegraph pools | Inputs not retained on this host; the planner directed that the unavailable population not be reacquired. |
| `combo-required-query-array-enum-items` | unrecovered handed-off documents | Inputs not retained on this host; the planner directed that the unavailable population not be reacquired. |
| `combo-response-unresolved-nested-pointer` | acquired GitHub and Sourcegraph pools | Inputs not retained on this host; the planner directed that the unavailable population not be reacquired. |
| `combo-response-unresolved-nested-pointer` | unrecovered handed-off documents | Inputs not retained on this host; the planner directed that the unavailable population not be reacquired. |
| `combo-tag-only-operation-id` | acquired GitHub and Sourcegraph pools | Inputs not retained on this host; the planner directed that the unavailable population not be reacquired. |
| `combo-tag-only-operation-id` | unrecovered handed-off documents | Inputs not retained on this host; the planner directed that the unavailable population not be reacquired. |
| `combo-unrequired-tag-anyof-reference` | acquired GitHub and Sourcegraph pools | Inputs not retained on this host; the planner directed that the unavailable population not be reacquired. |
| `combo-unrequired-tag-anyof-reference` | unrecovered handed-off documents | Inputs not retained on this host; the planner directed that the unavailable population not be reacquired. |
| `combo-unrequired-tag-oneof-reference` | acquired GitHub and Sourcegraph pools | Inputs not retained on this host; the planner directed that the unavailable population not be reacquired. |
| `combo-unrequired-tag-oneof-reference` | unrecovered handed-off documents | Inputs not retained on this host; the planner directed that the unavailable population not be reacquired. |
| `model-property-construct` | acquired GitHub and Sourcegraph pools | Inputs not retained on this host; the planner directed that the unavailable population not be reacquired. |
| `model-property-construct` | unrecovered handed-off documents | Inputs not retained on this host; the planner directed that the unavailable population not be reacquired. |
| `schema-type-name-component` | acquired GitHub and Sourcegraph pools | Inputs not retained on this host; the planner directed that the unavailable population not be reacquired. |
| `schema-type-name-component` | unrecovered handed-off documents | Inputs not retained on this host; the planner directed that the unavailable population not be reacquired. |

The counted [named census](census.tsv) contains every non-local declaring candidate, with its source population and required screen. A count of zero is an empty candidate set, not an invented document.

## Unscreened withdrawal declarations

The archive has 19 reference-copy declaring documents and one declaring document
for each union selector, plus 30 timestamp declaring documents. Each positive
reading in `archive-census.tsv.gz` is an outstanding candidate: verify its exact
trigger, publisher provenance and grant, then generate and compare its exact
bytes with the certified pair. These searches remain `search-incomplete`; the
missing pools and partial handoff also prevent exhaustion.
