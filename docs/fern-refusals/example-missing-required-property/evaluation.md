# example-missing-required-property: refuse

## Component collisions retired at Fern CLI 5.216.0 / fern-python-sdk 5.42.0 (#991)

Decision: **refuse**, narrowed. Two components Fern names alike (`Thing_Item` and `ThingItem`) are one type to
the pair, the later declaration, and its check validates its example of the
earlier one, reached from a response, against that later one. crozier gives
each component its own class (the
[`colliding-component-own-class`](../../departures/evidence/colliding-component-own-class.md)
departure), so such a document is valid OpenAPI and the refusal only Fern's
limitation: crozier no longer refuses it, in either mode, with or without
`--fern-strict` (#991). An inline schema taking a component's name still
refuses: crozier types it with that component, as Fern does.

Its probe is no collision and stands. crozier generates the `component-collision` and `allof-collision` shapes in both modes, which Fern still refuses; braille-dev's integrations document `981dd0a3…`, refused only by `TaxCode` beside `Tax_Code`, is now a `fern-limitation` disposition with its [SDK evaluation](../../openapi-surface/fern-refusals/limitations/981dd0a3479197032c4ebd98b040f6a53d4b6878d008a3a83518fb1f7fc5e269.json). Every other population document crozier refused through the collision still refuses under `--fern-strict` with another class its Fern log carries.

## At Fern CLI 5.216.0 / fern-python-sdk 5.42.0

Decision: **refuse**, unchanged. The Fern goldens run 44880783817
re-took the [probe record](fern-refusal.txt) at this pair, and Fern still refuses
the probe as recorded. Every shape, confirmation and reduction the registry
carries for the class was retaken at this pair (`fern-refusals.py shapes`,
`confirm` and `reduce`, one Fern run at a time), each keeping its role's
verdict (`shapes.tsv` is unchanged), and `fern-refusals.py check` holds them
there. crozier's behaviour is unchanged: the e2e gate still runs its probe in
both modes. The sections below are history at the pairs they name.

## At Fern CLI 5.200.0 / fern-python-sdk 5.41.25

Decision: **refuse**, unchanged. The Fern goldens run 43423270787
re-took the [probe record](fern-refusal.txt) at this pair, and Fern still refuses
the probe as recorded. Every shape, confirmation and reduction the registry
carries for the class was retaken at this pair (`fern-refusals.py shapes`,
`confirm` and `reduce`, serially), each with its role's verdict, and
`fern-refusals.py check` holds them there. crozier's behaviour is unchanged: the
e2e gate still runs its probe in both modes. The sections below are history at
the pairs they name.

## Narrowed for the document-acceptance area (2026-11-01, Fern CLI 5.163.1 / fern-python-sdk 5.41.3)

A nullable parent's extension reached only through an object declaring `additionalProperties: true` is no refusal: measured variants show the certified pair generating it there and refusing it reached directly or through closed objects ([`crozier-refuses-nullable-error-extension`](../../fern-measurements/handed-off/document-acceptance/crozier-refuses-nullable-error-extension/README.md); plaid's `Warning.cause`). Decision otherwise unchanged: **refuse**, in both modes.

## At Fern CLI 5.163.1 / fern-python-sdk 5.41.3

Decision: **refuse**, unchanged. The [probe record](fern-refusal.txt) is measured at this pair. Its 9 probe and 9 control shapes are measured at this pair too ([`shapes.tsv`](../../openapi-surface/fern-refusals/shapes.tsv)): a `-probe` is a shape Fern refuses, a `-control` one it generates from, and each `evaluation-logs/fern-<shape>.log` holds that measurement. The population carries the class on 130 documents at this pair, as at Fern CLI 5.67.1. crozier's release build refuses 130 of the 130 retrievable ones under `--fern-strict` ([`documents.tsv`](../documents.tsv)).

The evaluation below was written at Fern CLI 5.67.1 / fern-python-sdk 5.20.0. Where it cites a committed shape, that shape's log is now the 5.163.1 measurement and its verdict is its role's; a population count or a Fern log named there is that pair's. The Fern logs listed under *Dated history* were taken at 5.67.1 and are kept as that record; no claim about 5.163.1 rests on them.

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

## Dated history

Taken at Fern CLI 5.67.1 / fern-python-sdk 5.20.0, over a document never committed or one since re-measured in `shapes.tsv`:

- [`evaluation-logs/fern-medialive-reduced.log`](evaluation-logs/fern-medialive-reduced.log)
- [`evaluation-logs/fern-readonly-shadow-optional-parent-literals.generate.log`](evaluation-logs/fern-readonly-shadow-optional-parent-literals.generate.log)
- [`evaluation-logs/fern-readonly-shadow-optional-parent.generate.log`](evaluation-logs/fern-readonly-shadow-optional-parent.generate.log)
- [`evaluation-logs/fern-request-name-collision.log`](evaluation-logs/fern-request-name-collision.log)
