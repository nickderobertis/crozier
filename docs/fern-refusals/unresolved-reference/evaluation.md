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
