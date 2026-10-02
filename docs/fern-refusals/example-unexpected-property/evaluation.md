# example-unexpected-property: refuse

Baseline: `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`. No SDK repair was
made to qualify this class. Checks use CPython 3.12, mypy 1.13.0 and the
generated `pyproject.toml`'s own configuration with its dependencies installed.

The [probe output](evaluation-logs/probe.log) imports its package and client
and has **zero mypy errors**, but its [public-client journey](evaluation-logs/probe.wire.log)
shows the offending element lost: the document declares two distinct
components, `Thing_Item` (`id`) and `ThingItem` (`name`), and the baseline
types both response fields `a` and `b` as one `ThingItem` declaring only
`name`. `Thing_Item.id` is no declared field of `a`'s model; the declared
field is dropped. `GET /probe` is sent with no body.

Two population representatives from different publishers also fail their own
type checks:

- [CommunityToolkit Datasync's NSwag test document, `1a978bc6…`](evaluation-logs/population-datasync.log)
  imports but reports **72 mypy errors in three files**.
- [Moffin's API, `0d1c316a…`](evaluation-logs/population-moffin.log)
  imports but reports **68 mypy errors in six files**.

The class is `refuse` in both modes. No generated SDK changes.

## What Fern rejects, and what it lets through

Each shape is a committed `*-probe.yml` (refused) or `*-control.yml`
(accepted) with its pinned Fern log, all driven through the CLI by
`example_unexpected_property_refusal_covers_measured_shapes`; the detector is
the shared example-value walker (`src/document_refusals/examples.rs`).

- **Name collisions where the later declaration wins** (Fern's example of the
  earlier object, reached from a response, is validated against the later
  one): two component objects (the probe), an inline object property against
  a component ([inline-object-collision](evaluation-logs/fern-inline-object-collision.log),
  [empty winner](evaluation-logs/fern-inline-object-empty-winner.log)), and an
  `allOf` loser, flattened over its members as Fern's example of it is
  ([allof-collision](evaluation-logs/fern-allof-collision.log),
  [base only](evaluation-logs/fern-allof-base-collision.log),
  [inline only](evaluation-logs/fern-allof-inline-collision.log)) — Clio's
  `TaskTemplateList` against `TaskTemplate_List`. Accepted: a winner declaring
  every property ([superset](evaluation-logs/fern-winner-superset.log),
  [allOf superset](evaluation-logs/fern-allof-superset-winner.log)), an open
  winner, the winner declared first
  ([component](evaluation-logs/fern-component-declared-first.log),
  [allOf](evaluation-logs/fern-allof-declared-first.log)), a loser reached only
  from a request, and the winner alone.
- **A request body declaring `properties` beside a discriminated union**
  (two or more object members sharing a single-value enum property): Fern
  takes an object property both declare from the members, so a written request
  example nesting a key no member declares there is unexpected, whatever the
  top level says ([anyOf](evaluation-logs/fern-discriminated-union-nested.log),
  [oneOf](evaluation-logs/fern-discriminated-oneof-nested.log)) — Moffin's
  `serviceQueries.renapoCURP` against its members' `renapoCurp`. Accepted: no
  top-level `properties` ([control](evaluation-logs/fern-union-without-top-properties.log)),
  a key some member declares ([control](evaluation-logs/fern-union-member-declares-key.log)),
  members without the shared enum ([control](evaluation-logs/fern-union-without-enum.log)),
  a single member ([control](evaluation-logs/fern-union-single-member.log)),
  and members not declaring the property ([control](evaluation-logs/fern-union-members-lack-property.log)).
- **A required top-level property beside an `allOf` member referenced into a
  component's own `definitions`** (NSwag; Datasync's `KitchenSink`): Fern does
  not follow that member, and its response example carries the required
  property no member it reads declares
  ([array item](evaluation-logs/fern-definitions-member.log),
  [direct](evaluation-logs/fern-definitions-member-direct.log),
  [open member](evaluation-logs/fern-definitions-open-member.log)). Accepted:
  the member referencing a component ([control](evaluation-logs/fern-component-member.log)),
  an absent reference ([control](evaluation-logs/fern-absent-member.log)), an
  optional ([control](evaluation-logs/fern-optional-top-property.log)) or no
  ([control](evaluation-logs/fern-no-top-properties.log)) top-level property.
- **`x-fern-examples`** carrying a property the type does not declare
  ([fern-examples](evaluation-logs/fern-fern-examples.log)); a plain written
  example is not checked this way ([control](evaluation-logs/fern-written-example.log)).

Every accepted control generates identical bytes in both crozier modes. The
[CLI assertion fails with only the component-collision rule disabled](evaluation-logs/refusal-e2e-induced-red.log);
the rule is restored.

[All 196 population documents](evaluation-logs/population-refusals.jsonl) were
run with the integrated release build in both modes; each is refused with
exit 1, no files and one stderr line naming the class that fires first and
its element, with `fern-strict` as the strict cause.
