# object-property-name-collision

Baseline: `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`. Decision: **refuse**.
No generator repair is made.

The probe imports and reports zero mypy errors under the generated pyproject configuration. It sends and parses sha1 exactly, but flattens two declared sha1 properties into one field. Merging declarations fails the required bar.
[generate](evidence/object-property-name-collision.generate.log), [import](evidence/object-property-name-collision.import.log), [mypy](evidence/object-property-name-collision.mypy.log), [wire](evidence/object-property-name-collision.wire.log)

Retrievable population representative `1bf315cf37b400e6a7e05f1470b8225fc09708724ae28c142eb28d2a7b2744fc` (source locator in generation log):
The PayPal representative imports but reports 36 mypy errors under its own generated pyproject configuration. It cannot satisfy the zero-error bar. A baseline HTTP journey sends one invoice_id JSON key for the inherited and local declarations and parses the returned capture id exactly.
[generate](evidence/1bf315cf37b400e6a7e05f1470b8225fc09708724ae28c142eb28d2a7b2744fc.generate.log), [import](evidence/1bf315cf37b400e6a7e05f1470b8225fc09708724ae28c142eb28d2a7b2744fc.import.log), [mypy](evidence/1bf315cf37b400e6a7e05f1470b8225fc09708724ae28c142eb28d2a7b2744fc.mypy.log)

All 41 retrievable population documents refuse with exit 1 and no output under strict mode: [measurements](evidence/population-strict.log).

Pinned Fern controls: [object-body-inline.pinned-fern](evidence/object-body-inline.pinned-fern.log), [object-body-reference.pinned-fern](evidence/object-body-reference.pinned-fern.log), [object-change-constraint.pinned-fern](evidence/object-change-constraint.pinned-fern.log), [object-change-description.pinned-fern](evidence/object-change-description.pinned-fern.log), [object-change-enum.pinned-fern](evidence/object-change-enum.pinned-fern.log), [object-change-required.pinned-fern](evidence/object-change-required.pinned-fern.log), [object-change-type.pinned-fern](evidence/object-change-type.pinned-fern.log), [object-nonnullable.pinned-fern](evidence/object-nonnullable.pinned-fern.log), [object-nullable.pinned-fern](evidence/object-nullable.pinned-fern.log), [object-typed.pinned-fern](evidence/object-typed.pinned-fern.log).
