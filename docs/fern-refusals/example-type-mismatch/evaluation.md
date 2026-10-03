# example-type-mismatch: refuse

Baseline: `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`. No SDK repair was
made to qualify this class. Checks use CPython 3.12, mypy 1.13.0 and the
generated `pyproject.toml`'s own configuration with its dependencies installed.

The [probe output](evaluation-logs/probe.log) imports its package and client
and has **zero mypy errors**. Its [public-client journey](evaluation-logs/probe.wire.log)
sends `GET /probe` with no body and parses the declared `Thing.born`
(`string`, `format: date`) as `datetime.date(2006, 1, 2)`, reserializing it
unchanged. The probe alone would qualify the class.

Three population representatives from different publishers decide it:

- [Corrently (apis.guru, `2c08e583…`)](evaluation-logs/population-corrently.log)
  imports with **zero mypy errors**; its [journey](evaluation-logs/population-corrently.wire.log)
  sends `GET /tariff/slph0?zipcode=…` and parses the declared integer `ap`/`gp`
  fields whose examples (`22.12`, `7.5`) Fern rejects.
- [MAX-API's relay description (sourcegraph, `7374a3aa…`)](evaluation-logs/population-max-api.log)
  imports with zero mypy errors, but Fern's diagnostic there comes from a name
  collision: `Message.content` is `oneOf [string, array of MessageContent]`,
  and its inline union is named like the component `MessageContent`. The
  baseline types `Message.content` as the `MessageContent` object. The
  [journey](evaluation-logs/population-max-api.wire.log) fails to construct a
  message with the declared string content and fails to parse a response
  whose `message.content` is the declared string. A declared shape is lost.
- [Instabase's AI Hub description (github-raw, `1f841b8b…`)](evaluation-logs/population-instabase.log)
  imports but reports **16 mypy errors**.

Losing a declared union branch and failing type checking disqualify the class
under the conjunction rule, so it is `refuse` in both modes. No generated SDK
changes.

## What Fern rejects, and what it lets through

Fern checks the examples it attaches to every endpoint: the ones a document
writes and the ones its importer assembles from schema examples. Each rule the
detector applies (`src/document_refusals/examples.rs`) is the measured shape of
one pinned-Fern check, refused below, and stops wherever a near miss was not
measured. Refused shapes, each a committed `*-probe.yml` with its Fern log:

- a fractional number as an `integer`'s schema example
  ([integer-fraction](evaluation-logs/fern-integer-fraction.log)), and a
  non-`YYYY-MM-DD` string as a `date`'s (the probe), under the first success
  response, the required properties of a request body that writes no example
  ([request-required](evaluation-logs/fern-request-required.log)), or a
  parameter's schema or own example
  ([parameter-schema-example](evaluation-logs/fern-parameter-schema-example.log),
  [parameter-example](evaluation-logs/fern-parameter-example.log));
- the same scalars inside a written response or request media example,
  through `allOf` members too
  ([written-date](evaluation-logs/fern-written-date.log),
  [written-request](evaluation-logs/fern-written-request.log),
  [written-allof-date](evaluation-logs/fern-written-allof-date.log));
- two or more named request examples beside a `204` and another `2XX` whose
  body is an object with empty `properties`, the shape of GitHub's
  `convertMemberToOutsideCollaborator`, refused whatever the examples hold
  ([empty-body-named-examples](evaluation-logs/fern-empty-body-named-examples.log));
- a tagged operation's optional header `$ref`ing an integer or date component,
  which Fern fills with the header's name
  ([header-name-integer](evaluation-logs/fern-header-name-integer.log));
- name collisions, where the later declaration of a Fern type name wins and the
  example of the other is validated against it: an inline string-led union
  ([string-union-collision](evaluation-logs/fern-string-union-collision.log),
  Stripe's `subscription.schedule`), an inline enum
  ([inline-enum-collision](evaluation-logs/fern-inline-enum-collision.log)),
  and a scalar component taken by a later inline object
  ([scalar-inline-object-collision](evaluation-logs/fern-scalar-inline-object-collision.log),
  PeerTube's `UserRole`);
- a map written as a string error's media example
  ([error-string-map](evaluation-logs/fern-error-string-map.log)), and a
  non-object for an object in `x-fern-examples`
  ([fern-examples-object](evaluation-logs/fern-fern-examples-object.log)).

Accepted near misses, each a committed `*-control.yml` whose Fern log exits 0
and which the CLI journey generates identically in both modes:
[date-time is not format-checked](evaluation-logs/fern-datetime-format.log),
[a wrong-kind schema example is dropped](evaluation-logs/fern-wrong-kind-example.log),
[an optional request property is left out](evaluation-logs/fern-request-optional.log),
[a media example replaces schema examples](evaluation-logs/fern-media-overrides-schema.log),
[one named request example](evaluation-logs/fern-single-named-example.log),
[`type: object` without `properties`](evaluation-logs/fern-untyped-object-body.log),
[a colliding component declared first](evaluation-logs/fern-union-collision-declared-first.log),
[an unreferenced colliding scalar](evaluation-logs/fern-unreferenced-scalar-collision.log),
[a map under a success response](evaluation-logs/fern-success-string-map.log) and
[a schema-level map on an error](evaluation-logs/fern-error-schema-level-map.log).
`x-crozier-examples` is never read: pinned Fern does not see it.

The [probe assertion failed with only its predicate disabled](evaluation-logs/refusal-e2e-induced-red.log)
(the probe generated 38 files), and passed again once restored. The corpus
byte-match passes with `fern-strict` off and on (189 tests each).

[All 331 population documents](evaluation-logs/population-refusals.jsonl),
measured with the finished detector, were retrieved at their digests and
refused in both modes: exit 1, no files, one class/element stderr line and the
strict cause when applicable. 186 are refused by this class; the rest by
another registered class or example-value rule that fires first.

## An optional promoted array header

Issue #353 extends the detector to the shape Contract A's `header-array` probe
isolates ([its record](../../openapi-surface/probe-expected/header-array.fern-refusal.txt),
re-measured [here](evaluation-logs/fern-header-array.log)). Fern promotes a
header that rides every operation to a client field and fills that field's
example with the header's name; an array header's check then rejects the name
as no list. So the refused shape is an **optional array header crozier
promotes** (`GlobalHeader`, the same rule that emits client fields) **with no
string `default`**: the probe, whose one operation carries it, and each
`header-array-*-probe.yml` here —
[without the control's default](evaluation-logs/fern-header-array-no-default.log),
[optional on both of two operations](evaluation-logs/fern-header-array-promoted-optional.log),
[with a list default](evaluation-logs/fern-header-array-list-default.log),
[with integer items](evaluation-logs/fern-header-array-integer-items.log),
[with a schema example](evaluation-logs/fern-header-array-schema-example.log) and
[with a parameter example](evaluation-logs/fern-header-array-parameter-example.log).
crozier names the route and header: `example-type-mismatch: GET /probe header
probeParam`.

Fern generates from every other measured array header, and so does crozier,
byte-matching each committed tree under
[`../../openapi-surface/authored-probes/`](../../openapi-surface/authored-probes/):
optional and required on one of two operations (a method argument,
`353-method-optional-array`, `353-method-required-array`), required on every
operation (a `typing.List[str]` client field, `353-promoted-required-array`,
`353-solo-required-array`), and optional with a string `default`, which Fern
types `str` and sends the default for (`353-string-default-probe`,
`353-string-default-control`, the
[`list-default-not-array` header control](../list-default-not-array/header-array-control.yml)).
That control's tree is the tree of the same header declared `type: string`
(`353-string-default-scalar`), so its `default: all` is what separates it from
the probe. The [class journey failed with only this predicate
disabled](evaluation-logs/header-array-e2e-induced-red.log), generating 39 files
from `header-array-integer-items-probe.yml`.
