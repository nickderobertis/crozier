# generator-missing-type: refuse

Baseline: `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`. No SDK repair.
Measurements use CPython 3.12.3, mypy 1.13.0 and the generated
`pyproject.toml` configuration with its declared dependencies.

The [probe package and client import](evaluation-logs/probe.log), and mypy
reports zero errors. Its [public client journey](evaluation-logs/probe.wire.log)
sends `GET /agents` with the exact declared `Api-Version: 2026-03-11`
header and parses the declared empty 204 response as `None`.

The sole population document, [ben-ic's Notion description,
`1542bad104f5ca9f559e34400a9206fdb672a98f5a7a9e6ae01f1a3c81655888`](evaluation-logs/population.log),
imports its package and client but reports **402 mypy errors in 12 files**.
Its offending header is `Notion-Version`, imported from a Parameter Object
reference with an inline singleton string enum, without an explicit type.
The [public client journey](evaluation-logs/population.wire.log) sends its
exact declared header on `POST /v1/agents/batch` and parses the declared
async-task response without losing fields. Correct wire behavior on this
journey does not rescue a package that fails its own type-checking configuration.
The population failure makes the class `refuse` in both modes.

Pinned generation measurements fail after a passing check for
[optional headers](evaluation-logs/fern-optional-singleton.log),
[multiple string enum values](evaluation-logs/fern-two-values.log),
[another ordinary header](evaluation-logs/fern-other-header.log),
[`Accept`](evaluation-logs/fern-accept-header.log),
[inferred string enums](evaluation-logs/fern-inferred-type.log),
[repeated headers across operations](evaluation-logs/fern-two-operations.log)
and [string constants](evaluation-logs/fern-const-header.log).
They generate successfully for [named enum schemas](evaluation-logs/fern-named-enum.log),
[`Authorization`](evaluation-logs/fern-authorization-header.log),
[`User-Agent`](evaluation-logs/fern-user-agent-header.log),
[`Content-Type`](evaluation-logs/fern-content-type-header.log)
and [numeric enums](evaluation-logs/fern-numeric-enum.log).
The detector preserves these accepted cases and follows local Parameter
Object references; the real CLI journey compares accepted output bytes
between both modes.

The [CLI assertion fails with only this class's predicate disabled](evaluation-logs/refusal-e2e-induced-red.log),
writing 38 files instead of refusing. This log deliberately records an induced
earlier state; the finished source restores the predicate.

The [population refusal log](evaluation-logs/population-refusals.jsonl) covers
its one retrievable document in both modes: exit 1, no files, one line naming
the class and `Notion-Version`, and `fern-strict` as the strict-mode cause.

Both supported ignore-extension spellings are exercised on the inline header
schema. The [ignore exemption assertion fails when only that guard is removed](evaluation-logs/ignore-e2e-induced-red.log):
the CLI refuses the ignored schema instead of generating. The guard is restored.
