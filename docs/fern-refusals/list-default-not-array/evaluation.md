# list-default-not-array: refuse

## At Fern CLI 5.163.1 / fern-python-sdk 5.41.3

Decision: **refuse**, unchanged. The [probe record](fern-refusal.txt) is measured at this pair. Its 1 probe and 5 control shapes are measured at this pair too ([`shapes.tsv`](../../openapi-surface/fern-refusals/shapes.tsv)): a `-probe` is a shape Fern refuses, a `-control` one it generates from, and each `evaluation-logs/fern-<shape>.log` holds that measurement. The population carries the class on 7 documents at this pair, as at Fern CLI 5.67.1. crozier's release build refuses 7 of the 7 retrievable ones under `--fern-strict` ([`documents.tsv`](../documents.tsv)).

What moved: `boolean-default` is a probe (Fern refuses it, as before).

The evaluation below was written at Fern CLI 5.67.1 / fern-python-sdk 5.20.0. Where it cites a committed shape, that shape's log is now the 5.163.1 measurement and its verdict is its role's; a population count or a Fern log named there is that pair's. The Fern logs listed under *Dated history* were taken at 5.67.1 and are kept as that record; no claim about 5.163.1 rests on them.

Baseline: `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`. No SDK repair.
Measurements use CPython 3.12.3, mypy 1.13.0, generated `pyproject.toml`
configuration and declared dependencies.

The [probe](evaluation-logs/probe.log) imports its package and client with
zero mypy errors. `Thing.tags` declares an array of strings with string default
`all`. Its [public response journey](evaluation-logs/probe.wire.log) sends
`GET /probe`; an empty object leaves `tags` unset, and an explicit string list
parses unchanged. The invalid scalar default never becomes an array.

The representative [4dem description,
`1c1156cfd31816c502a507ef632e8f1f0c5254707c5bc7386f31942c1d4898e9`](evaluation-logs/population.log)
imports its package and client but reports **988 mypy errors in 34 files**
under its own configuration. At `WorkflowMessageTrigger.segments`, the
[wire journey](evaluation-logs/population.wire.log) sends
`PUT /workflows/1/messages/2` with `trigger: {}` when the list is unspecified,
and with `trigger.segments: [{id: 3}]` when explicitly supplied. It parses
`segments: [{id: 4}]` into the declared model unchanged and returns `None`
for the declared empty successful response. No field is renamed, merged or
dropped in this local journey, but the package's type-check failure
disqualifies the class under the class-wide conjunction rule.

The detector refuses non-null scalar defaults on array object properties.
Pinned [boolean-default](evaluation-logs/fern-boolean-default.log) measurement
confirms the same refusal. A [list default](evaluation-logs/fern-valid-list.log),
[null default](evaluation-logs/fern-null-list.log),
[unused primitive array declaration](evaluation-logs/fern-unused-array.log) and
[non-enum query array scalar default](evaluation-logs/fern-query-array.log)
are accepted and generate identical crozier bytes in both modes. The
[CLI assertion fails with only this predicate disabled](evaluation-logs/refusal-e2e-induced-red.log),
writing 38 files instead of refusing; the list-default recovery generates.

Parameter arrays are excluded. The [header check](evaluation-logs/fern-header-array.log)
and [header generation](evaluation-logs/fern-header-array-generate.log) both
succeed in Fern, whereas [baseline crozier](evaluation-logs/baseline-header-array.log)
refused array headers as unsupported; this class never masked that with
`list-default-not-array`. Issue #353 removed that baseline refusal: crozier
now generates the control, byte-matching Fern's committed tree
(`../../openapi-surface/authored-probes/353-string-default-control/`), and the
CLI journey holds it to identical output in both modes. Its `default: all` is
what Fern generates it by: without it the same header is the
`example-type-mismatch` refusal
([measured](../example-type-mismatch/evaluation.md#an-optional-promoted-array-header)).

[All seven population documents](evaluation-logs/population-refusals.jsonl)
were retrieved and refused in both modes: exit 1, no files and one diagnostic
line, including `fern-strict` as the strict cause. Other recorded classes may
be diagnosed first; each log names the actual class.

## Dated history

Taken at Fern CLI 5.67.1 / fern-python-sdk 5.20.0, over a document never committed or one since re-measured in `shapes.tsv`:

- [`evaluation-logs/fern-header-array-generate.log`](evaluation-logs/fern-header-array-generate.log)
