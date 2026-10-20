# request-property-name-collision

## Re-measured at Fern CLI 5.163.1 / fern-python-sdk 5.41.3: refuse

Decision: **refuse**, in both modes. The shapes the class names changed; its
refusal rule did not.

Fern's importer renames a path parameter whose name a body property claims to
`{name}PathParam`, but it reserves only the body's own properties and each
`allOf` parent's own. The probe's path `id` sits beside an inline body that
extends `Request`, which extends `CommonRequest` declaring `id`: the name is
not reserved, the parameter keeps it, and both `fern check` and
`fern generate` exit 1 with `Multiple request properties have the name id`
([check](../../openapi-surface/fern-refusals/probe-logs/request-property-name-collision.check.log),
[generate](../../openapi-surface/fern-refusals/probe-logs/request-property-name-collision.generate.log)).
The same holds with the path parameter declared through `components/parameters`
(`path-reference-inline-body`). A header collides with a query parameter of its
name only where it rides too few operations to be lifted to the client:
`X-Namespace` beside `namespace` on two of three operations is refused
(`header-query-subset`), on every operation it generates
(`header-query-every-operation`) — crozier's `ir::global_headers` decides the
lift as Fern does. The population's eight documents at the pair (Rebilly's KYC
requests and the Irrigator API, which are these two shapes, and Telnyx) all
refuse under strict mode.

crozier refuses each refused shape in both modes, naming the operation and the
name. Generating would need a rename Fern does not make, so no Fern output is a
reference for it. Fern generates, and crozier generates in both modes, a
referenced body (`path-referenced-body`: the body is sent whole), a property an
`allOf` member redeclares (`body-allof-member-redeclared`; Mistral's
`stream`), and two parents sharing one (`body-two-parents-shared`)
([`shapes.tsv`](../../openapi-surface/fern-refusals/shapes.tsv)). The class's
former probe, a path `name` against a body's own `name`, is the finding
`request-property-name-collision-generates`, authored probe
[`549-request-property-name-collision`](../../openapi-surface/authored-probes/549-request-property-name-collision/).
The GitHub REST descriptions, which 5.67.1 refused under this class, no longer
carry it.

## Evaluation at Fern CLI 5.67.1 / fern-python-sdk 5.20.0 (dated history)

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
