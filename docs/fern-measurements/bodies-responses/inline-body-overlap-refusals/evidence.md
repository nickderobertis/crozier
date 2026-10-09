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
arguments and the inherited wire value are emitted.

The read-only overlap is refused under the same class, by manager ruling, in
default and `--fern-strict` mode and in the source-level fallback a malformed
sibling schema reaches. The refusal applies only to an inline body with its own
non-readOnly `properties` beside an `allOf` `$ref` parent declaring the same
name. Every other read-only shape stays exempt, as the class evaluation's
accepted controls require.
`inline_request_read_only_parent_overlap_refuses_and_disjoint_fields_recover_through_the_cli`
drives the committed read-only source. It requires exit 1, the class line
naming `POST /runs` and `"station"`, no ruff diagnostic and no output tree. It
then renames the own field and requires a generated SDK that declares each
argument once and compiles. Independently, the request-body flattening never
appends a parent field whose wire name an own field already holds.

`origin/main` at `5f224026330dd25fdc54d3bdf90fe6be0ef32b3c` generated 44 files
for the read-only source (exit 0), because it did not flatten inherited fields.
Before this repair, the branch reached ruff with `Duplicate keyword argument
"station"` (exit 1). The branch now refuses with
`request-property-name-collision` before rendering, as pinned Fern does. This
is a refusal-class agreement, not an accepted golden or a claim that crozier
matches Fern's diagnostic text.
