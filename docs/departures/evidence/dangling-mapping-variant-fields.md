# Dangling mapping variant fields

The from-scratch [observatory document](../../fern-measurements/emission-parity/dangling-mapping-target/openapi.yml)
declares `Reading`, a `oneOf` of `StarReading`, `CometReading` and
`MeteorReading` discriminated by `kind`. Its mapping names `STAR` and `COMET` by
their components, but maps `METEOR` to `#/components/schemas/meteor-reading`,
which names no component. `MeteorReading`, the member no mapping target names,
tags itself `METEOR`. This is the shape of ingef/conquery's `Query`, whose
`SECONDARY_ID_QUERY` target is `secondary-Id-query` beside a `SecondaryIdQuery`
member.

The certified pair, Fern CLI 5.163.1 with fern-python-sdk 5.41.3, writes the
discriminated union of `Reading_*` wrappers
([`fern-expected/src/fern/types/reading.py`](../../fern-measurements/emission-parity/dangling-mapping-target/fern-expected/src/fern/types/reading.py)).
Its `METEOR` wrapper holds nothing of the member:

```python
class Reading_Meteor(UniversalBaseModel):
    value: typing.Any
    kind: typing.Literal["METEOR"] = "METEOR"
```

`value` is required, and no `METEOR` payload the document declares has one. Fern
warns at generation that the unmapped member "will be omitted from the generated
union, so payloads using it will fail to serialize or deserialize".

## The failure, through the real client

[`dangling_mapping_wire.py`](../../../crates/crozier-e2e/tests/e2e/dangling_mapping_wire.py)
starts a local HTTP server and drives an SDK's `AsyncFernApi` against it. It reads a
logbook entry whose `reading` is
`{"kind": "METEOR", "brightness": -3.5, "trail": {"degrees": 12.0, "colour": "green"}}`,
then posts that reading back. A `STAR` reading makes the same round trip as the
control.

Run over the certified tree (`fern-expected/src`, Pydantic 2.14.1), the `STAR`
round trip passes and the `METEOR` read fails, exit 1:

```text
failed: METEOR: reading the entry raised ParsingError: reading.METEOR.value |   Field required [type=missing, …]
```

The only `METEOR` value Fern's types can build, `Reading_Meteor(value={...})`,
nests the member's properties under `value`, a shape the member schema does not
declare. On conquery, the only `Query_SecondaryIdQuery` Fern's types can build,
`Query_SecondaryIdQuery(value={"secondaryId": "dataset.sid"})`, was sent as
`{"type": "SECONDARY_ID_QUERY", "value": {"secondaryId": "dataset.sid"}}` during
the investigation that led to the ruling.

crozier's `Reading_Meteor` carries `trail` and `brightness` beside the tag, as
every other wrapper carries its member's fields. The same script over crozier's
SDK, in either enum mode, exits 0:

```text
METEOR: parsed into Reading_Meteor and posted back as {"brightness": -3.5, "kind": "METEOR", "trail": {"colour": "green", "degrees": 12.0}}
```

`sdk_env_a_dangling_mapping_variant_round_trips_through_the_client` runs both,
under `just test-sdk-env`.

## The same failure on conquery's registered document

[`conquery_secondary_id_wire.py`](../../../crates/crozier-e2e/tests/e2e/conquery_secondary_id_wire.py)
drives the client generated from the exact registered document,
`tests/fixtures/corpus-sources/ingef-conquery/openapi.yaml` (corpus row 3477,
sha256 `c3a52b3c…`), against a local HTTP server. It answers
`GET /queries/{query}` with a status whose `query` is
`{"type": "SECONDARY_ID_QUERY", "secondaryId": "dataset.sid",
"dateAggregationMode": "MERGE"}`. It requires that query to parse into
`Query_SecondaryIdQuery`, with `secondary_id` and `date_aggregation_mode`
carrying those values. It then posts the query back through `post_query` and
requires the server to receive exactly that payload. A `CONCEPT_QUERY` makes
the same round trip as the control.

Over crozier's SDK, generated from that document, the journey exits 0 in both
enum modes:

```text
CONCEPT_QUERY: parsed into Query_ConceptQuery and posted back as {"dateAggregationMode": "MERGE", "type": "CONCEPT_QUERY"}
SECONDARY_ID_QUERY: parsed into Query_SecondaryIdQuery and posted back as {"dateAggregationMode": "MERGE", "secondaryId": "dataset.sid", "type": "SECONDARY_ID_QUERY"}
```

Over the certified golden (`tests/fixtures/ingef-conquery/expected/src`,
Pydantic 2.14.1), the control passes and the `SECONDARY_ID_QUERY` read fails,
exit 1:

```text
failed: SECONDARY_ID_QUERY: reading the status raised ParsingError: query.SECONDARY_ID_QUERY.value |   Field required [type=missing, …]
```

`sdk_env_conquery_secondary_id_query_round_trips_through_the_client` runs all
three under `just test-sdk-env`. With crozier made to write Fern's
`value: typing.Any` wrapper instead, it fails on crozier's own SDK at that same
`ParsingError`.

Both journeys live in `crates/crozier-e2e/tests/e2e/emission_parity.rs`, behind
`sdk_env_*` wrappers at the crate root of `crates/crozier-e2e/tests/e2e.rs`.
They sit at the root because the `sdk-env` tier selects tests by full name,
with `test(/^sdk_env_/)`.

**Checks run with this journey.** The final source is `491ba4aba`. On it:

- Both runtime journeys pass through the `sdk-env` tier's own selector.
- The five `emission_parity` golden journeys pass.
- `just departures-ledger` re-ran every golden comparison with all passing,
  and the ledger was already current.
- The library's 737 unit tests, clippy and rustfmt pass.

At `5305ca288`, which adds only the derived records:

- the `surface-census` suite: 614 passed;
- the offline corpus tests: all three suites passed;
- `just lint-llm-diff` over the whole diff: no rule failed.

## What the rule admits

The rule reads the wrappers off the source document
(`crate::ir::dangling_mapping_wrappers`), each with the fields the member
lends it. A wrapper whose fields are not exactly those, in order, is not the
construct. For each, it rewrites crozier's class Fern's way: `value: typing.Any` in place of the docstring and fields, and the
configuration without `extra`. It also drops the wrapper's own
`update_forward_refs` call, and every single-name import only those lines used.
It accounts for the file only when the result is Fern's file exactly. The
departure applies only where every `oneOf` member resolves, some mapping target
names a component, and exactly one member the mapping leaves out tags itself
with the value. Every other dangling mapping keeps the output crozier wrote
before.
