# example-missing-required-property: refuse

Baseline: `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`. No SDK repair was
made to qualify this class. Checks use CPython 3.12, mypy 1.13.0 and the
generated `pyproject.toml`'s own configuration with its dependencies installed.

The [probe output](evaluation-logs/probe.log) imports its package and client
and has **zero mypy errors**. Its [public-client journey](evaluation-logs/probe.wire.log)
sends `GET /requests/r-1` with the path parameter and no body, and parses the
declared `Request.log` (a `FileMini` extending the nullable `FileBase`) with
`id` and `name` intact. The probe alone would qualify the class.

A population representative disqualifies it.
[Braille's QuickBooks description, `981dd0a3…`](evaluation-logs/population-braille.log)
imports and has zero mypy errors, but its [journey](evaluation-logs/population-braille.wire.log)
shows the declared `TaxCode` (`Id`, `Name`, `Description`) merged into the
distinct `Tax_Code` (a required `value`): the baseline's `TaxCode` declares
only `value`, and parsing a declared `TaxCode` query response fails with a
`ParsingError`. What the document declares is not parsed.

The class is `refuse` in both modes. No generated SDK changes.

## What Fern rejects, and what it lets through

Each shape is a committed `*-probe.yml` (refused) or `*-control.yml`
(accepted) with its pinned Fern log, driven through the CLI by
`example_missing_required_property_refusal_covers_measured_shapes`; the
detector is the shared example-value walker (`src/document_refusals/examples.rs`).

- **A nullable `allOf` parent with required properties**: Fern's example of
  the child omits them (the probe;
  [nullable child](evaluation-logs/fern-nullable-child.log),
  [array](evaluation-logs/fern-nullable-parent-array.log),
  [referenced additions](evaluation-logs/fern-referenced-additions.log)).
  Accepted: a non-nullable parent, a parent without required properties, no
  additions, an optional request
  ([controls](evaluation-logs/fern-non-nullable-parent.log),
  [2](evaluation-logs/fern-parent-without-required.log),
  [3](evaluation-logs/fern-no-additions.log),
  [4](evaluation-logs/fern-request-optional.log)).
- **A discriminant required two `allOf` levels up**
  ([probe](evaluation-logs/fern-discriminant-grandparent.log)); accepted when
  the parent declares it or it is not restated
  ([controls](evaluation-logs/fern-discriminant-parent.log),
  [2](evaluation-logs/fern-discriminant-not-restated.log)).
- **Name collisions where the later declaration wins**: a component object
  ([component-collision](evaluation-logs/fern-component-collision.log)), and an
  `allOf` loser flattened over its members against a winner requiring a
  property it lacks ([allof-collision](evaluation-logs/fern-allof-collision.log)),
  Clio's `TaskTemplateList` against `TaskTemplate_List`. Accepted: the winner
  declared first ([control](evaluation-logs/fern-allof-declared-first.log)).
- **`x-fern-examples`** missing a required property
  ([fern-examples](evaluation-logs/fern-fern-examples.log)); a plain written
  example is not checked this way ([control](evaluation-logs/fern-written-example.log)).
- **A readOnly own request property shadowing a required parent property**:
  an inline JSON request body with its own `properties` and an `allOf` `$ref`
  parent, where an own `readOnly` property redeclares a property the parent
  requires. Fern's request example omits the readOnly property and then
  validates against the parent's `required`
  ([python-enums](evaluation-logs/fern-readonly-shadow-required.generate.log),
  [literals](evaluation-logs/fern-readonly-shadow-required-literals.generate.log),
  [optional request body](evaluation-logs/fern-readonly-shadow-optional-request.generate.log)).
  Accepted: the same shadow over an optional parent property
  ([python-enums](evaluation-logs/fern-readonly-shadow-optional-parent.generate.log),
  [literals](evaluation-logs/fern-readonly-shadow-optional-parent-literals.generate.log)),
  which is the certified handwritten fixture
  [`inline-body-readonly-own-overlap`](../../openapi-surface/handwritten/inline-body-readonly-own-overlap/openapi.yml).
  These are `fern generate` logs at the pin, and their diagnostic is the one
  `fern check` reports for this class.

Every accepted control generates identical bytes in both crozier modes. The
[CLI assertion fails with only the nullable-parent rule disabled](evaluation-logs/refusal-e2e-induced-red.log);
the rule is restored.

[The population refusal log](evaluation-logs/population-refusals.jsonl) runs
the integrated release build over every retrievable document of the class in
both modes: all 130 are refused, each with exit 1, no files and one stderr
line naming the class that fires first, with `fern-strict` as the strict cause.

AWS MediaLive (`4cecee33…`) reaches this class only through a `names`-family
collision. Delta-debugging it against pinned Fern, first over its path items,
then over its component schemas, leaves `POST /prod/multiplexes` with four
components. On that [reduced document](evaluation-logs/fern-medialive-reduced.log)
Fern reports both `CreateMultiplexRequest is already declared in this file`
and the missing `request.multiplexSettings.TransportStreamBitrate`: the
operation's inline request body takes Fern's name `CreateMultiplexRequest`,
which a component already holds, and Fern validates its own example against
that component. The [hand-written collision alone](request-name-collision.yml)
reports [only the name collision](evaluation-logs/fern-request-name-collision.log).
MediaLive is therefore attributed to `type-name-collision`, the `names`
family, and no detector for it is added here. The planner's amendment would
leave such a document out of this class's `population_strict`; it is not left
out, because the `names` detectors merged from crozier PR #342 now refuse it in
both modes, as `request-property-camelcase-collision` (its schedule
operation's `maxResults` and `MaxResults`, a class Fern also reports for it),
and the planner ruled that this integration supersedes the exclusion. The
inline-request-name collision itself remains a `names` follow-up.
