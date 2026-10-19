# object-property-name-collision

## Retiring: measured at Fern CLI 5.163.1 / fern-python-sdk 5.41.3

Fern generates from the probe: `fern check` and `fern generate` both exit 0
([check](../../openapi-surface/fern-refusals/probe-logs/object-property-name-collision.check.log),
[generate](../../openapi-surface/fern-refusals/probe-logs/object-property-name-collision.generate.log)).
Its tree is the authored-probe case
[`549-object-property-name-collision`](../../openapi-surface/authored-probes/549-object-property-name-collision/):
`FileConflict` keeps one `sha1: typing.Optional[str]` field beside its nullable
`FileMini` base.

crozier generates too, in default mode and under `--fern-strict`, and
byte-matches Fern's tree in both (`authored_probe_measurements_match_fern`,
`nullable_inherited_property_redeclarations_generate_in_both_modes`). The
`findings.tsv` row `object-property-name-collision-generates` names this
class's probe, which makes the class **retiring**: `fern_refusal_failures`
holds crozier to generating the probe in both modes, and `fern-refusal.txt`
stays as the class's last refusal record (Fern CLI 5.67.1). The `classes.tsv`
row (whose `status` still reads `refuse`) and its `documents.tsv` references
stay until the population is measured again at the new pair.

## Evaluation at Fern CLI 5.67.1 / fern-python-sdk 5.20.0

Baseline: `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`. Decision: **refuse**.
No generator repair is made.

The probe imports and reports zero mypy errors under the generated pyproject configuration. It sends and parses sha1 exactly, but flattens two declared sha1 properties into one field. Merging declarations fails the required bar.
[generate](evidence/object-property-name-collision.generate.log), [import](evidence/object-property-name-collision.import.log), [mypy](evidence/object-property-name-collision.mypy.log), [wire](evidence/object-property-name-collision.wire.log)

Retrievable population representative `1bf315cf37b400e6a7e05f1470b8225fc09708724ae28c142eb28d2a7b2744fc` (source locator in generation log):
The PayPal representative imports but reports 36 mypy errors under its own generated pyproject configuration. It cannot satisfy the zero-error bar. A baseline HTTP journey sends one invoice_id JSON key for the inherited and local declarations and parses the returned capture id exactly.
[generate](evidence/1bf315cf37b400e6a7e05f1470b8225fc09708724ae28c142eb28d2a7b2744fc.generate.log), [import](evidence/1bf315cf37b400e6a7e05f1470b8225fc09708724ae28c142eb28d2a7b2744fc.import.log), [mypy](evidence/1bf315cf37b400e6a7e05f1470b8225fc09708724ae28c142eb28d2a7b2744fc.mypy.log)

All 41 retrievable population documents refuse with exit 1 and no output under strict mode: [measurements](evidence/population-strict.log).

Pinned Fern controls: [object-body-inline.pinned-fern](evidence/object-body-inline.pinned-fern.log), [object-body-reference.pinned-fern](evidence/object-body-reference.pinned-fern.log), [object-change-constraint.pinned-fern](evidence/object-change-constraint.pinned-fern.log), [object-change-description.pinned-fern](evidence/object-change-description.pinned-fern.log), [object-change-enum.pinned-fern](evidence/object-change-enum.pinned-fern.log), [object-change-required.pinned-fern](evidence/object-change-required.pinned-fern.log), [object-change-type.pinned-fern](evidence/object-change-type.pinned-fern.log), [object-nonnullable.pinned-fern](evidence/object-nonnullable.pinned-fern.log), [object-nullable.pinned-fern](evidence/object-nullable.pinned-fern.log), [object-typed.pinned-fern](evidence/object-typed.pinned-fern.log).
