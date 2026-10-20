# object-property-name-collision

## Re-measured at Fern CLI 5.163.1 / fern-python-sdk 5.41.3: refuse

Decision: **refuse**, in both modes. The shape the class names changed; its
refusal rule did not.

The probe's response is `allOf: [CollectionResponse, CommonFailure]`: both
parents declare `errors` and `result`, and `CollectionResponse` also inherits
them from `Common` through its own `$ref` parent. Fern flattens the two parents
into one object that extends `Common`, and both `fern check` and
`fern generate` exit 1 with `Object has multiple properties named "result"`
([check](../../openapi-surface/fern-refusals/probe-logs/object-property-name-collision.check.log),
[generate](../../openapi-surface/fern-refusals/probe-logs/object-property-name-collision.generate.log)).
The population's nine documents at the pair carry this phrase (Cloudflare,
whose `ClientRequestErrorBody` is this shape, Telnyx, Realcube and Gcore), and
every one of them carries another class too; all nine refuse under strict mode
([`documents.tsv`](../documents.tsv)).

crozier refuses the probe and the
[`error-response-two-parents`](error-response-two-parents-probe.yml) shape in
both modes, naming the response and the property. A generated SDK would have to
pick one of the two declarations for the flattened field, which no Fern output
shows, so there is no reference to match and the refusal stands. Fern generates,
and crozier generates byte for byte in both modes, the near misses
([`shapes.tsv`](../../openapi-surface/fern-refusals/shapes.tsv)): two parents
declaring the property with no inheritance (`two-direct-parents`), a second
parent not declaring it (`second-parent-unrelated`), a single parent
(`single-parent`), an object redeclaring its one parent's property
(`redeclared-non-nullable-base`; the nullable base of the class's former probe
is the finding `object-property-name-collision-generates`, authored probe
[`549-object-property-name-collision`](../../openapi-surface/authored-probes/549-object-property-name-collision/)),
and a `required` naming an inherited property (`inherited-required`).

## Evaluation at Fern CLI 5.67.1 / fern-python-sdk 5.20.0 (dated history)

Baseline: `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`. Decision: **refuse**.
No generator repair is made.

The probe imports and reports zero mypy errors under the generated pyproject configuration. It sends and parses sha1 exactly, but flattens two declared sha1 properties into one field. Merging declarations fails the required bar.
[generate](evidence/object-property-name-collision.generate.log), [import](evidence/object-property-name-collision.import.log), [mypy](evidence/object-property-name-collision.mypy.log), [wire](evidence/object-property-name-collision.wire.log)

Retrievable population representative `1bf315cf37b400e6a7e05f1470b8225fc09708724ae28c142eb28d2a7b2744fc` (source locator in generation log):
The PayPal representative imports but reports 36 mypy errors under its own generated pyproject configuration. It cannot satisfy the zero-error bar. A baseline HTTP journey sends one invoice_id JSON key for the inherited and local declarations and parses the returned capture id exactly.
[generate](evidence/1bf315cf37b400e6a7e05f1470b8225fc09708724ae28c142eb28d2a7b2744fc.generate.log), [import](evidence/1bf315cf37b400e6a7e05f1470b8225fc09708724ae28c142eb28d2a7b2744fc.import.log), [mypy](evidence/1bf315cf37b400e6a7e05f1470b8225fc09708724ae28c142eb28d2a7b2744fc.mypy.log)

All 41 retrievable population documents refuse with exit 1 and no output under strict mode: [measurements](evidence/population-strict.log).

Pinned Fern controls: [object-body-inline.pinned-fern](evidence/object-body-inline.pinned-fern.log), [object-body-reference.pinned-fern](evidence/object-body-reference.pinned-fern.log), [object-change-constraint.pinned-fern](evidence/object-change-constraint.pinned-fern.log), [object-change-description.pinned-fern](evidence/object-change-description.pinned-fern.log), [object-change-enum.pinned-fern](evidence/object-change-enum.pinned-fern.log), [object-change-required.pinned-fern](evidence/object-change-required.pinned-fern.log), [object-change-type.pinned-fern](evidence/object-change-type.pinned-fern.log), [object-nonnullable.pinned-fern](evidence/object-nonnullable.pinned-fern.log), [object-nullable.pinned-fern](evidence/object-nullable.pinned-fern.log), [object-typed.pinned-fern](evidence/object-typed.pinned-fern.log).

## Dated history

No claim about Fern CLI 5.163.1 rests on these. Taken at Fern CLI 5.67.1 / fern-python-sdk 5.20.0, over a document never committed or one since re-measured in `shapes.tsv`:

- [`evidence/object-body-inline.pinned-fern.log`](evidence/object-body-inline.pinned-fern.log)
- [`evidence/object-body-reference.pinned-fern.log`](evidence/object-body-reference.pinned-fern.log)
- [`evidence/object-change-constraint.pinned-fern.log`](evidence/object-change-constraint.pinned-fern.log)
- [`evidence/object-change-description.pinned-fern.log`](evidence/object-change-description.pinned-fern.log)
- [`evidence/object-change-enum.pinned-fern.log`](evidence/object-change-enum.pinned-fern.log)
- [`evidence/object-change-required.pinned-fern.log`](evidence/object-change-required.pinned-fern.log)
- [`evidence/object-change-type.pinned-fern.log`](evidence/object-change-type.pinned-fern.log)
- [`evidence/object-nonnullable.pinned-fern.log`](evidence/object-nonnullable.pinned-fern.log)
- [`evidence/object-nullable.pinned-fern.log`](evidence/object-nullable.pinned-fern.log)
- [`evidence/object-typed.pinned-fern.log`](evidence/object-typed.pinned-fern.log)
