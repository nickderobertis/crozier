# Schema interaction controls

`controls.json` names the two registered-interaction schema conjunction arms tested by
`CooccurrenceOutcomeTest.test_schema_interaction_controls_reach_their_region_only_with_both_features`.
Each document is authored from scratch. The test checks its two feature
selectors as well as its combination selector, then invokes the instrumented
CLI: each single-feature document misses the arm and the combined document
executes it. A control passing does not establish a registered witness; the
co-occurrence audit records that separate requirement.

The three `combo-anyof-schema-example` documents are retained as diagnostic
inputs, outside the interaction manifest. The example consumer handles both
`oneOf` and `anyOf` as `TypeRef::Union`; an earlier shortcut checking `anyOf`
returned the same literal as the generic path and has been removed. These
inputs do not certify an anyOf-specific interaction. The audit leaves that
combination open until a consumer arm distinguishing its origin is located
and executed by a byte-matching registered specification.

The other six previously listed controls are retained as diagnostic inputs,
outside the interaction manifest. Their added conjunction guards repeated the
generic path's result and were removed: allOf/required, annotated-reference/
nullable-target, parameter-example/reference and the three composition/media
example combinations. Earlier counter execution for those guards is withdrawn
as interaction proof; their rows are open.

The genuine map/oneOf arm remains covered separately by
`test_maps_beside_unions_reach_a_keyword_specific_region_only_with_both_features`.
Its controls are retained here outside the registered-interaction manifest,
and its exact branch specification and zero-hit real-specification diagnostic
are in the bounded search. Its formal ledger site stays `co-occurrence` while
the audit is open: no golden declaration is counted as an interaction match.
