# unresolved-schema-reference: refuse

Baseline: `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`. No SDK repair.
Measurements use CPython 3.12.3, mypy 1.13.0 and the generated
`pyproject.toml` configuration with its declared dependencies.

The [probe package and client import](evaluation-logs/probe.log), and mypy
reports zero errors. Its required `attributes` field names an absent schema,
`custom_attributes`; crozier annotates the argument as `Any`. The
[public client journey](evaluation-logs/probe.wire.log) preserves the outer
wire field on `POST /contacts` and parses the empty 204 as `None`. The intended
inner type cannot be compared with an absent declaration; this is not evidence
that the unresolved reference has a useful typed representation.

One representative, [NVIDIA table-structure description published by
JithendraNara,
`01c4f9b4d87421faa2cb1fbb053bf6d1ac53cb8f02aeace1c8180320a415120e`](evaluation-logs/population.log),
imports its package and client but reports **six mypy errors in one file**.
Its required response `usage` refers to `$defs/UsageInfo`, an object with a
required numeric `images_size_mb`. Crozier annotates `usage` as `Any`. The
[public client journey](evaluation-logs/population.wire.log) sends the declared
image request and preserves the valid response values, including the raw usage
dictionary. Its own type-checking failure nevertheless disqualifies the package,
so this class is `refuse` in both modes.

The pinned [probe run](evaluation-logs/fern-probe.log) confirms a false success:
Fern reports failure resolving `custom_attributes`, then check and generation
exit 0 and emit a package from an unparsed document. The same failure occurs
for required fields through [definitions](evaluation-logs/fern-deep-definitions-field.log),
[$defs](evaluation-logs/fern-deep-defs-field.log),
[response fields](evaluation-logs/fern-required-response-field.log),
[nullable references](evaluation-logs/fern-nullable-required-field.log),
[nullable roots](evaluation-logs/fern-nullable-root.log), and
[an optional known child with a required unresolved field](evaluation-logs/fern-optional-known-child.log).

Fern accepts [a supplied definition](evaluation-logs/fern-defined-field.log),
[a standard properties fragment](evaluation-logs/fern-deep-field.log),
[a property named definitions](evaluation-logs/fern-definitions-property-name.log),
[missing response roots](evaluation-logs/fern-missing-response-root.log),
[missing request roots](evaluation-logs/fern-missing-request-root.log),
[deep response roots](evaluation-logs/fern-deep-response-root.log),
[optional request fields](evaluation-logs/fern-optional-field.log),
[optional response fields](evaluation-logs/fern-optional-response-field.log),
[optional definition fragments](evaluation-logs/fern-optional-deep-field.log),
[explicit optional request examples](evaluation-logs/fern-explicit-optional-request.log),
[required arrays of unresolved items](evaluation-logs/fern-required-array.log),
and unused schemas containing [optional](evaluation-logs/fern-unused-missing-field.log),
[required](evaluation-logs/fern-unused-required-field.log), or
[deep](evaluation-logs/fern-unused-deep-field.log) references.
The detector follows schemas bound to operations and diagnoses the measured
required-field resolution failure; it does not blanket-refuse deep or missing
references. The CLI journey preserves every accepted control with identical
bytes in both modes, and covers an ignored operation and both supported
ignore-extension spellings on the offending schema.

[All 49 population documents](evaluation-logs/population-refusals.jsonl) were
retrieved at their recorded digests and refused in both modes: exit 1, no files,
one class/element line, with `fern-strict` as the strict-mode cause. Where another
registered structural refusal is diagnosed first, the log records that actual
class. The measurement uses a preserved build of the finished detector.

The [CLI assertion fails with only the required-field resolution predicate disabled](evaluation-logs/refusal-e2e-induced-red.log),
writing 36 files for the probe instead of refusing. This deliberately records
an induced earlier state; the finished source restores the predicate.
