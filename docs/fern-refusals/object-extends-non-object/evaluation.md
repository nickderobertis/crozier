# object-extends-non-object: refuse

Baseline: `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`. No SDK repair.
Measurements use CPython 3.12.3, mypy 1.13.0 and the generated
`pyproject.toml` configuration with its declared dependencies.

The [probe](evaluation-logs/probe.log) imports its package and client and
reports zero mypy errors. `Tagged` declares an object branch with `id` while
extending the named string `Label`. The [public client journey](evaluation-logs/probe.wire.log)
sends `GET /probe` with an empty request body. When the 200 response contains
the object branch's `id`, parsing raises `PydanticSchemaGenerationError` for
`Tagged`; no declared model response is returned. This is a generation defect,
not a missing wire-name prefix to repair.

One representative, [APWG's eCX description,
`112b5d9658df34218ea3c584e82ff8a1bfdfe13771826326cbfb7c60b237ba3e`](evaluation-logs/population.log),
cannot generate: ruff rejects `report_phishing_resp_body.py` with a syntax
error. The [output log](evaluation-logs/population.wire.log) records zero SDK
files. Package imports and mypy cannot run without a package; their error
counts are unavailable, not zero. Its offending `/malicious-ip/search` filters
extend named array/string types, and no client exists to send or parse them.
The class is therefore `refuse`, based on the probe and representative's
failures rather than any proposed SDK repair.

The detector checks named bases of object extensions; it preserves scalar
aliases and inline constraints. Pinned measurements refuse named
[array](evaluation-logs/fern-array-base.log),
[map](evaluation-logs/fern-map-base.log),
[bare object](evaluation-logs/fern-empty-object-base.log), and
[two scalar](evaluation-logs/fern-two-scalar-refs.log) bases. They accept
[object bases](evaluation-logs/fern-object-base.log),
[empty explicit properties](evaluation-logs/fern-empty-properties-base.log),
[object aliases](evaluation-logs/fern-object-alias.log),
[scalar aliases](evaluation-logs/fern-scalar-alias.log),
[scalar constraints](evaluation-logs/fern-scalar-constrained.log),
[explicit scalar declarations](evaluation-logs/fern-typed-two-scalar-refs.log),
[nullable scalar declarations](evaluation-logs/fern-nullable-typed-two-scalar-refs.log)
and [inline scalar/object branches](evaluation-logs/fern-inline-scalar-object.log).
The CLI journey generates every accepted control with identical bytes in both
modes and refuses each offending control with one class/element line.

Declaration order is significant. An inline union imported after an existing
object can replace the named base used by an extension. The pinned
[ordered probe](evaluation-logs/fern-ordered-shadowed-object.log) refuses;
[reversing its declarations](evaluation-logs/fern-shadowed-object.log) and
[renaming its union property](evaluation-logs/fern-ordered-renamed-union.log)
are accepted. The same distinction isolates GitHub's population refusal:
[original declaration order](evaluation-logs/fern-github-mini-ordered.log)
fails while [reordering the extracted schemas](evaluation-logs/fern-github-mini-reordered.log)
passes. The detector tracks imported declaration shapes in document order,
using the existing naming functions and type accessor. Properties on a
discriminator base remain object definitions, preventing refusals of the
accepted Komga and Palo Alto corpus shapes.

The [CLI assertion fails with only the extension predicate disabled](evaluation-logs/refusal-e2e-induced-red.log),
writing 39 files instead of refusing. This evidence intentionally concerns an
induced earlier state; the predicate is restored in the finished source.

The [declaration-order assertion also fails with only inline declaration
registration disabled](evaluation-logs/declaration-order-e2e-induced-red.log),
writing 40 files for the ordered probe. [All 114 population documents](evaluation-logs/population-refusals.jsonl)
were retrieved at their recorded digests and refused in both modes: exit 1,
no files and one class/element line, with `fern-strict` as the strict cause.
Where another registered class is diagnosed first, the log records that actual
class. The population run uses a preserved build of the restored detector so
assertion-witness rebuilds cannot change its executable during measurement.
