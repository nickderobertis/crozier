# Inline request fields overlapping an inherited field

These controls were derived from the independently authored
[JSON request proof](../../../openapi-surface/handwritten/json-request-shapes/openapi.yml).
Both add a required inline `station` field beside the inherited
`RunSettings.station`. The read-only variant marks the inherited field
`readOnly: true`. They are refusal measurements, not accepted handwritten
fixtures or real specification witnesses.

Both runs used Fern CLI 5.67.1 and `fernapi/fern-python-sdk` 5.20.0,
packaged preview, organization/package `fern`, project `default_package_name`,
no audience filter, and `pydantic_config.enum_type: python_enums`.
The complete generator diagnostics are committed as
[writable-parent.fern.log](writable-parent.fern.log) and
[readonly-parent.fern.log](readonly-parent.fern.log); both generation commands
exited 1. Each reports `Object has multiple properties named "station"` and
`Multiple request properties have the name station`. Neither produced an
accepted SDK tree.

The real-binary test
`inline_request_parent_overlap_refuses_and_disjoint_fields_recover_through_the_cli`
requires the writable overlap to fail with `request-property-name-collision`,
then restores the disjoint source and checks that both own and inherited
arguments and the inherited wire value are emitted. The read-only difference
is outside the owned shape and is recorded for a separate refusal decision.

A fresh `origin/main` build at
`5f224026330dd25fdc54d3bdf90fe6be0ef32b3c` generated 44 files for the
read-only source (exit 0); its raw client compiles and emits the own station
argument and description once per sync/async method. After removing this
branch's added duplicate-field filter, a fresh branch build refuses that same
source (exit 1): ruff reports `Duplicate keyword argument "station"` while
formatting `src/fern/client.py`. This is a refusal diagnostic difference,
not an accepted golden or a claim that crozier matches Fern's diagnostic.
The adjacent boundary-validation gap is recorded for follow-up; the owned
certified inputs retain disjoint own and inherited fields.
