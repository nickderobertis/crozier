# path-without-leading-slash: refuse

Baseline: `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`. No generated SDK was
repaired to qualify it. Logs use CPython 3.12.3 and the generated project's
mypy 1.13.0 configuration and dependencies.

The [probe](evaluation-logs/probe.log) imports its package and client and has
**zero mypy errors**. The [wire trace](evaluation-logs/probe.wire.log) sends
`GET /base/things` with `https://example.com/base` configured, and parses the
empty 204 as `None`. Its declared path `things` violates OpenAPI's leading
slash rule, but crozier still joins it onto the base URL. The probe by itself
has functioning generated output.

One population representative, [aki-lua87/PSO2API,
`6cfc658fe510e051684d34217dfa4fc0745e19097440a3337cd08fea5b10a90e`](evaluation-logs/population.log),
imports the package and root client but has **three mypy errors**. Its
malformed `api/coat_of_arms` path declares a response with `UpdateTime` and
`TargetList`. The [wire attempt](evaluation-logs/population.wire.log) cannot
reach the request: accessing the endpoint's subclient imports an enum with
duplicate `_` members and raises `TypeError`. No wire field or response can
be exercised through that public client. The immutable source and digest,
generation, root imports and full mypy report are recorded in the log.

The class therefore fails both the full import and zero-error typing
requirements on its population and is `refuse` in both modes. Further
representatives cannot qualify the class under the dispatch's conjunction
rule. The SDK's enum is not repaired, and its path is not rewritten.

The detector checks non-ignored operations under path keys without a leading
slash, leaving extension entries, ignored operations and non-operation Path Items alone. The
[real CLI recovery journey was observed failing before the detector](evaluation-logs/refusal-e2e-red.log).
Adding the missing slash restores generation with identical bytes in both
modes. [All four population documents](evaluation-logs/population-refusals.jsonl)
were retrieved at their digests and refused in both modes with exit 1, no
files, one class/element diagnostic, and the strict cause when applicable.

The [pinned Fern check and generation](evaluation-logs/fern-ignored-path.log)
accept the malformed path when its only operation has `x-fern-ignore: true`,
writing 28 Python files. An added CLI recovery assertion was [observed
failing](evaluation-logs/ignored-path-e2e-red.log) before the raw detector
respected the canonical ignore accessor; it now preserves this accepted case.
