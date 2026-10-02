# default-not-enum-value: refuse

Baseline: `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`. No SDK repair was
made to qualify this class. Checks use CPython 3.12.3, mypy 1.13.0 and the
generated `pyproject.toml`'s own configuration with its dependencies installed.

The [probe output](evaluation-logs/probe.log) imports its package and client
and has **zero mypy errors**. `ListRequest.sort` declares the distinct wire
values `createdAt` and `-createdAt`, with default `-createdAt`. The baseline
keeps only `CREATED_AT = createdAt`. Its [public enum/client journey](evaluation-logs/probe.wire.log)
raises `ValueError` constructing the declared negative value and sends no
request for it. Omitting the value sends `POST /contacts` with `{}` and parses
the declared empty 204 as `None`; that omission does not restore the missing
enum branch. Losing a declared value disqualifies the class, despite successful
package imports and typing.

One representative, [Jentic's Ducky description,
`fe8b00c68174c422b7c5410477991bd62e0beec017a9752caea02c52806fe12a`](evaluation-logs/population.log),
also imports and has **zero mypy errors**. Its `POST /calculator` query
`categories` is an array of five enum values, with `explode: false`, but its
written default is a string containing a JSON array. The [wire log](evaluation-logs/population.wire.log)
shows the omitted argument sends no `categories` value; explicit public and
consumption values send `categories=public%2Cconsumption`, preserving the wire
name and declared CSV representation. It parses the declared footprint fields
and numeric values correctly. The log records the default's actual string
shape rather than claiming it became a valid array. This representative does
not rescue the probe's missing branch under the class-wide conjunction rule.

The class is `refuse` in both modes. A scalar string default naming a
removed enum value is refused wherever Fern imports that enum, including
unused component schemas and whole request/response schemas. Scalar defaults
that never named a declared value are ignored by Fern, rather than treated as
this class. Query arrays instead import an enum-or-list union and validate
their scalar default against the item enum; ordinary array properties belong
to `list-default-not-array`. No generated SDK changes.

The [probe assertion failed with its predicate disabled](evaluation-logs/refusal-e2e-induced-red.log),
writing 38 files. The [query-array assertion likewise failed with only its
non-member branch disabled](evaluation-logs/query-array-induced-red.log).
Real CLI journeys cover collision defaults in operation and shared parameters,
unused schemas and properties, and root request/response types. Replacing the
default with its retained first value recovers generation in both modes.
Pinned Fern checks substantiate each additional shape:
[operation parameter](evaluation-logs/fern-operation-scalar-collision.log),
[query array](evaluation-logs/fern-operation-array.log),
[shared parameter](evaluation-logs/fern-shared-parameter-collision.log),
[unused schema](evaluation-logs/fern-unused-schema-collision.log),
[unused property](evaluation-logs/fern-unused-object-property-collision.log),
[response root](evaluation-logs/fern-response-root-collision.log), and
[request root](evaluation-logs/fern-request-root-collision.log).

Accepted controls distinguish those refusals from ignored non-member scalar
defaults in [unused properties](unused-object-control.yml),
[shared parameters](shared-parameter-control.yml),
[response roots](response-root-control.yml) and [request roots](request-root-control.yml).
The corresponding [unused](evaluation-logs/fern-unused-object-active-api.log),
[shared](evaluation-logs/fern-shared-parameter.log),
[response](evaluation-logs/fern-response-root.log) and
[request](evaluation-logs/fern-request-root.log) check logs accept them;
[unused generation](evaluation-logs/fern-unused-object-active-api-generate.log),
[response generation](evaluation-logs/fern-response-root-generate.log) and
[request generation](evaluation-logs/fern-request-root-generate.log) produce SDKs.
[Explicit names](declared-members-control.yml),
[measured by Fern](evaluation-logs/fern-declared-members.log), preserve both
values. Pinned Fern ignores `x-crozier-*`, so it also [accepts those names
beside an empty `x-crozier-enum`](evaluation-logs/fern-canonical-empty-members.log)
([control](canonical-empty-members-control.yml)). Per the manager's ruling,
the detector reads enum members as Fern does, dropping `x-crozier-*` before
asking the IR's enum builder which members survive; emission keeps canonical
precedence. All accepted controls generate identical bytes in both crozier modes.

[All five population documents](evaluation-logs/population-refusals.jsonl),
measured with the finished detector, were retrieved at their digests and refused in both modes: exit 1, no files,
one class/element stderr line and the strict cause when applicable.
