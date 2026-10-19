# request-property-name-collision

## Retiring: measured at Fern CLI 5.163.1 / fern-python-sdk 5.41.3

Fern generates from the probe: `fern check` and `fern generate` both exit 0
([check](../../openapi-surface/fern-refusals/probe-logs/request-property-name-collision.check.log),
[generate](../../openapi-surface/fern-refusals/probe-logs/request-property-name-collision.generate.log)).
Its tree is the authored-probe case
[`549-request-property-name-collision`](../../openapi-surface/authored-probes/549-request-property-name-collision/):
Fern's OpenAPI importer renames the path parameter `name` to `namePathParam`
(`name_path_param` in Python, still sent at `/repos/{…}`) because the body
property claims `name`, so no two request properties share a name.

crozier generates too, in default mode and under `--fern-strict`, and
byte-matches Fern's tree in both (`authored_probe_measurements_match_fern`,
`body_names_colliding_with_path_names_rename_the_path_parameter_in_both_modes`).
The `findings.tsv` row `request-property-name-collision-generates` names this
class's probe, which makes the class **retiring**: `fern_refusal_failures`
holds crozier to generating the probe in both modes, and `fern-refusal.txt`
stays as the class's last refusal record (Fern CLI 5.67.1). The `classes.tsv`
row (whose `status` still reads `refuse`) and its `documents.tsv` references
stay until the population is measured again at the new pair.

Only the probe's shape is measured at the new pair. The 5.163.1 bundle still
carries the `no-conflicting-request-wrapper-properties` rule that prints this
class's phrase, and its importer renames only a path parameter that declares no
name of its own (no `x-fern-parameter-name`), reserving the query parameters'
names, the headers' declared-or-wire names and the body's property names. So
crozier still refuses, under this class id, the shapes the rename does not
reach: a path parameter whose declared name a body property shares, differently
spelled parameters in different locations with one declared name, a body
property repeated through an inherited `allOf`, and an inline body's own
property a `$ref` parent redeclares. Re-measuring the population decides
whether those shapes keep a class of their own.

## Evaluation at Fern CLI 5.67.1 / fern-python-sdk 5.20.0

Baseline: `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`. Decision: **refuse**.
No generator repair is made.

The probe generates, imports, and reports zero mypy errors under its generated pyproject configuration. It sends PATCH /repos/original with body {"name":"new"} and parses the 204 response as None. However, the path parameter is emitted as name_, adding a suffix absent from the document. The required identifier bar fails.
[generate](evidence/request-property-name-collision.generate.log), [import](evidence/request-property-name-collision.import.log), [mypy](evidence/request-property-name-collision.mypy.log), [wire](evidence/request-property-name-collision.wire.log)

Retrievable population representative `b647ad473786da2dc733e115a1066da8c0485e2f6be78e85f54bf615a6140f90` (source locator in generation log):
The Irrigator representative exits 1 before producing a package. Import, mypy and a send/parse journey are unavailable; that independently fails the required bar.
[generate](evidence/b647ad473786da2dc733e115a1066da8c0485e2f6be78e85f54bf615a6140f90.generate.log)

Pinned Fern refuses a name shared by a [path parameter and body property](evidence/request-path.pinned-fern.log),
including a [referenced body](evidence/request-reference.pinned-fern.log),
but accepts the tested [query/body](evidence/request-query.pinned-fern.log) and
[header/body](evidence/request-header.pinned-fern.log) pairs.
It accepts [duplicate query declarations](evidence/same-parameter-query-query.pinned-fern.log)
and refuses parameters in [different locations](evidence/same-parameter-query-header.pinned-fern.log).
Cross-location pairs with the same wire spelling belong to the normalization
class; differently spelled names such as X-Namespace and namespace belong to
this exact-name class. Repeated
properties within an expanded request body also belong to this exact-name class.

All 296 retrievable population documents refuse under strict mode with no output: [population measurements](evidence/population-strict.log). The name collision hidden by a malformed nullable flag is classified from source metadata without repairing that flag.

An accepted neighboring shape is retained: [pinned Fern control](evidence/request-readonly.pinned-fern.log).

Fern also accepts [referenced read-only fields](evidence/request-readonly-reference.pinned-fern.log) and [repeated properties across inline allOf members](evidence/request-inline-allof-duplicates.pinned-fern.log). The detector preserves those cases.

An inline body with its own `properties` and an `allOf` `$ref` parent is the
exception: crozier flattens the parent's fields beside the own ones, and pinned
Fern refuses an own property the parent redeclares even when the parent's is
`readOnly`
([writable](../../fern-measurements/bodies-responses/inline-body-overlap-refusals/writable-parent.fern.log),
[read-only](../../fern-measurements/bodies-responses/inline-body-overlap-refusals/readonly-parent.fern.log)).
The detector counts the read-only parent field for that shape alone, in both
modes and in the source-level fallback.
