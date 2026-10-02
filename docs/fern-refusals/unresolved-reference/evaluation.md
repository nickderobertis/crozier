# unresolved-reference: refuse

Baseline: `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`. No SDK repairs were
made to qualify a document for generation. Logs use CPython 3.12.3, mypy 1.13.0
and the generated `pyproject.toml` configuration with its dependencies installed.

The [probe log](evaluation-logs/probe.log) shows a successful package/client
import and zero mypy errors. Its declared required `BearerAuth` points to a
missing document. The [wire journey](evaluation-logs/probe.wire.log) shows that
the client exposes no credential argument and silently sends `GET /probe`
without Authorization, parsing its declared empty 200 as `None`. It cannot
honor the unresolved security declaration; treating it as no authentication
produces misleading output, so the probe fails the useful-wire requirement.

One population representative, [ccfos/huatuo,
`2e49fdc63bcf90614020270c9648b47cb634aad678ac045ba75cef775da8f6d1`](evaluation-logs/population.log),
also imports but has **62 mypy errors** in four files. Its required BearerAuth
points to `../components.yaml`. The [wire trace](evaluation-logs/population.wire.log)
sends `GET /openapi.json`, parses the declared JSON object, and exposes neither a
credential argument nor Authorization. The generation/type-check log records
the immutable source URL and digest. Both the typing errors and the silently
unauthenticated request independently disqualify it; further representatives
cannot rescue this class under the dispatch's conjunction rule.

The detector examines Non-Schema Reference Objects before normalization, not
Fern's source: missing relative documents, missing local targets and targets
outside the reference object's corresponding component collection are refused.
Schema and Path Item references have distinct measured behavior and are left to
their existing handling. Example/default/extension payloads are not Reference
Objects. Canonical ignore precedence uses the existing schema accessor.

Replacing the probe reference with an inline bearer scheme restores generation
with identical bytes in both modes. The [real binary recovery test was observed
failing before the detector](evaluation-logs/refusal-e2e-red.log), with the
unrelated service-auth diagnostic instead of the required reference diagnostic.
The final registry gate also checks the refusal's exit, empty output and strict
cause. [Population refusal evidence](evaluation-logs/population-refusals.jsonl)
records the retrievable documents in both modes; the registry's strict counts
and exits are derived from those runs.

YAML response status keys may be numeric. A refused population document also
contains a numeric bound beyond `u64`; the detector's structural reader can
inspect its references without changing the SDK loader's numeric contract.
Its non-reference numeric bound is ignored by this structural reader only.

[Unit mutation evidence](evaluation-logs/reference-unit-induced-red.log)
shows both the reference exemption/diagnostic test and escaped-pointer test
failing when their guarded behavior is disabled. [Additional mutation
evidence](evaluation-logs/reference-drift-induced-red.log) shows the auth
importer drift gate and the ignore-precedence CLI journey failing when their
behavior is disabled. All mutations were reverted before the final tests.
The auth predicate remains reconciled to the actual IR importer without
changing emitted SDKs. Service classification deliberately follows Fern
importer groups, rather than IR module flattening; the site-scoped lint
rationale at that grouping loop states this distinction.

A response Reference Object naming a parameter component is also a reference
into the wrong component collection, even when that parameter exists. Its
CLI recovery journey refuses it and generates when the response is inlined;
the [refusal assertion failed against the preserved starting binary](evaluation-logs/response-parameter-reference-e2e-red.log).

The accepted Groupe PSA corpus supplies a component-only response alias into
`#/x-fragment/general_error_fragment`. The [isolated Fern measurements](evaluation-logs/fern-response-fragment.log)
and [description-free control](evaluation-logs/fern-response-fragment-pure.log)
both pass check and generation. Unused response definitions are therefore not
eagerly traversed; operation response Reference Objects retain their checks.
The [CLI assertion failed before this restriction](evaluation-logs/response-component-fragment-e2e-red.log).
The accepted control generates identical bytes in both modes, while moving the
fragment reference onto the operation refuses. After this restriction, all 42
retrievable unresolved-reference documents still refuse in both modes.

The refusal boundary requires an unresolved document: providing the relative
security-scheme file is a [Fern-accepted control](evaluation-logs/fern-present-security-reference-check.log),
with [successful generation](evaluation-logs/fern-present-security-reference-generate.log)
writing 36 files. The first detector still rejected that control as undefined
auth; its [real CLI recovery assertion failed](evaluation-logs/present-security-reference-e2e-red.log).
The auth detector now inspects relative scheme declarations without changing
the SDK document or its emitted authentication. A [chained bearer declaration](evaluation-logs/fern-present-security-chain.log)
is also accepted, while a [referenced cookie declaration](evaluation-logs/fern-present-security-unimported.log)
retains Fern's service-auth refusal. The CLI journey covers all three and proves
identical emitted bytes between modes and between the two accepted declarations.
[Disabling chain traversal made the assertion fail](evaluation-logs/chained-security-reference-e2e-induced-red.log).
The reader canonicalizes file paths and guards cycles; [a mutation falsely
accepting a cycle failed its real-files unit test](evaluation-logs/security-reference-cycle-unit-induced-red.log).
