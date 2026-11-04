# Open combination union measurements

These are `open` records under the manager's failed-union amendment of
2026-11-04. They prove neither independence nor a real-specification interaction
branch. The complete executed-region sets within the audit's named functions
were compared without subtracting fallback or absence regions.

## Verdicts

| key | outcome | both-only regions | single-feature-union-only regions | what would settle it |
|---|---|---:|---:|---|
| `combo-allof-schema-example` | open (search-incomplete) | 0 | 4 | Locate a conjunctive condition and isolate its counter region, then measure a registered witness of that arm; `ahasend-api` remains the audit's registered declarer to inspect. |
| `combo-annotated-ref-property-example` | open (search-incomplete) | 0 | 42 | Locate a conjunctive condition and isolate its counter region, or establish a registered witness of that arm; the registered `zulip`, `zulip-jentic` and `zulip-jentic-entry` declarers remain candidates for that investigation, not certified interaction witnesses. |

The exact differing regions and the three documents for each row are in
[`evidence.json`](evidence.json). A region is `[path::function, [start line, start column,
end line, end column]]`. Lines are one-based relative to the named function's
first source line; columns retain LLVM's one-based positions. This keeps the
record stable when unrelated functions move without dropping any region. `both_only` is the
combined run minus the union of the single-feature runs; `singles_only` is the
reverse difference. Neither row has a both-only region. Each nonempty reverse
difference prevents the union equality required for independence.

## Source audit

The handling functions remain the ones each audit row names. The conditions
below are quoted as they occur in the source; none reads the two features in
one condition. Applying an example to fields already collected from composition
is not a source-level conjunction over the two declarations.

| key | handler | condition or fallible operand read |
|---|---|---|
| `combo-allof-schema-example` | `src/ir.rs::Builder::add_object` | `for (index, member) in schema.all_of.iter().flatten().enumerate() {` |
| `combo-allof-schema-example` | `src/ir.rs::Builder::add_object` | `if let Some(example) = schema_example(schema).and_then(serde_json::Value::as_object) {` |
| `combo-allof-schema-example` | `src/ir.rs::InlineHoister::hoist_object_with_doc` | `for member in schema.all_of.iter().flatten() {` |
| `combo-allof-schema-example` | `src/emit.rs::ExampleCtx::named_value_inner` | `field.parent_example` |
| `combo-annotated-ref-property-example` | `src/ir.rs::described_all_of_ref` | `if members.len() < 2 {` |
| `combo-annotated-ref-property-example` | `src/ir.rs::described_all_of_ref` | `} else if is_unknown(member) {` |
| `combo-annotated-ref-property-example` | `src/ir.rs::Builder::annotated_ref_type` | `described_all_of_ref(schema)?` |
| `combo-annotated-ref-property-example` | `src/ir.rs::Builder::collect_fields` | `example: resolved_schema_example_literal(prop_schema, Some(self.schemas))` |
| `combo-annotated-ref-property-example` | `src/ir.rs::resolved_schema_example_literal` | `typed_schema_example(schema)` |
| `combo-annotated-ref-property-example` | `src/ir.rs::schema_example` | `schema.example.as_ref().or_else(|| schema.examples.first())` |

## Controls and measurement provenance

All six documents were authored from scratch. `first` declares composition or
annotation without an example, `second` declares an example without composition
or annotation, and `both` declares their conjunction. The stock object-model
census reports zero conjunction sites in each single-feature document and one
in each combined document.

The real instrumented `crozier generate python` command generated each document
under `python_enums`; `llvm-profdata merge` and `llvm-cov export` supplied the
regions, scoped through `golden-reach.py`'s `handler_specs`, `resolve_site` and
`Site.holds`. The initial captures used the generator source at `c94bb1c1a`;
the instrumented test recomputes the full differences on the working tree.
These runs are not comparisons with certified output, and the documents
are not corpus registrations or hand-written fallback proofs.

`CooccurrenceOpenUnionTest` in `tools/surface-reach/tests/handwritten_reach_test.py`
validates each quoted source operand, each control's declarations and the exact
recorded region differences. Run it under the host's instrumented-measurement
lock. `CROZIER_UPDATE_OPEN_UNIONS=1` refreshes only the derived region lists;
the unchanged union inequality must still hold. The
[`harbor-parcel-requests`](../handwritten/harbor-parcel-requests/) fixture and its
certified tree remain diagnostic output evidence, not proof of an independently
handled combination or a registered interaction arm.

The first annotated-reference diagnostic used an invalid control for this
purpose: a one-member `allOf` with an outer description. Its reported 47 missing
regions is superseded and is not evidence for this combination. The committed
annotation documents instead have a reference member and a separate annotation
member, satisfy the census conjunction, and produce the 42-region difference
recorded here.

## Populations and outstanding work

This record does not claim a newly exhausted real-specification search. The
existing bounded populations, candidate identities, digests and screening
readings remain in the [examples search](../witness-search-schema-combinations-examples/README.md)
and its [candidate ledger](../witness-search-schema-combinations-examples/census.tsv).
The allOf/example search had a registered output-sensitive declarer; output
sensitivity alone does not isolate the requested interaction counter. The
annotated-reference search found no registered example-rendering witness.
Those readings are historical, not fresh certified-pair comparisons in this node.

All seven newly admitted hand-off documents, also exactly the `registered` rows
of the hand-off document ledger, were retried for the remaining hand-written
annotation combination. Each is named with its verified digest and zero site
count in the [hand-off retry](../witness-search-fixture-only-schemas/README.md#handed-off-document-retry-2026-11-04).
No new candidate from that population can declare this combination. The open
questions are the conjunctive condition or registered arm witness named above;
no hand-written fixture is counted as a substitute for either answer.

## Bounded search state

The [fresh bounded search](../witness-search-schema-interactions/README.md) reads
the retained populations for both rows. This record's census.tsv.gz is its exact
subset, preserving every candidate and reason. The complete outstanding identity
list is [outstanding-candidates.tsv](../witness-search-schema-interactions/outstanding-candidates.tsv).

| Combination | State | Candidates | Outstanding |
|---|---|---:|---:|
| `combo-allof-schema-example` | `search-incomplete` | 3566 | 3460 |
| `combo-annotated-ref-property-example` | `search-incomplete` | 3463 | 3352 |
