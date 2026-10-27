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
declare. On conquery, `client.query.get_query_status` raised the same
`ParsingError` (`query.SECONDARY_ID_QUERY.value Field required`) on a status
whose query was `{"type": "SECONDARY_ID_QUERY", "secondaryId": "dataset.sid",
"dateAggregationMode": "MERGE"}`, and the wrapper sent
`{"type": "SECONDARY_ID_QUERY", "value": {"secondaryId": "dataset.sid"}}`.

crozier's `Reading_Meteor` carries `trail` and `brightness` beside the tag, as
every other wrapper carries its member's fields. The same script over crozier's
SDK, in either enum mode, exits 0:

```text
METEOR: parsed into Reading_Meteor and posted back as {"brightness": -3.5, "kind": "METEOR", "trail": {"colour": "green", "degrees": 12.0}}
```

`sdk_env_a_dangling_mapping_variant_round_trips_through_the_client` in
`crates/crozier-e2e/tests/e2e/emission_parity.rs` runs both, under
`just test-sdk-env`.

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
