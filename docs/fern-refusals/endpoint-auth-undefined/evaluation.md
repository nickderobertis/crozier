# endpoint-auth-undefined: refuse

Evaluated on starting commit `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`,
without repairing any generated output.

The [probe](evaluation-logs/endpoint-auth-undefined.log) generates 36 files,
imports the package and client, and reports **zero mypy errors**. Its declared
mypy 1.13.0 runs under CPython 3.12.3 with the SDK's own `pyproject.toml`
configuration and installed runtime, optional and dev dependencies.

The [wire trace](evaluation-logs/endpoint-auth-undefined-wire.log) calls the
generated client's `probe` through an injected `httpx.MockTransport`. This
operation requires the `session` api key in the `SESSION` cookie. Its generated
constructor exposes no session credential and the request carries no Cookie
header. The 204 response parses as the declared absence of a body (`None`).
The missing credential makes this output insufficient; arbitrary caller-supplied
headers do not provide a generated representation of the declared credential.

Three population documents from distinct publishers were measured:

| Publisher and digest | Import | mypy errors | Offending security declaration |
| --- | --- | --- | --- |
| [dx-zone/certbot-rpm-mtls-repo, `120566bc0a…`](evaluation-logs/endpoint-auth-undefined-120566bc0a941b6e75429cb792e58a41fdf27726df9c745e7b02e0f5db808b18.log) | succeeds | 2 | Operation-level mutual TLS |
| [peter209393/open-check, `1270468883…`](evaluation-logs/endpoint-auth-undefined-12704688834f5729410fa352c1d0a0d60627732a822eb7bc9c2534ee627a8532.log) | succeeds | 0 | Operation-level cookie session and mutual TLS |
| [jentic/jentic-public-apis, `2240627eb1…`](evaluation-logs/endpoint-auth-undefined-2240627eb1a4c3dd6c70fffd5ed527ec02766ddc17f0f05b643a2fccdcd96592.log) | succeeds | 0 | Operation-level query api key `apikey` |

Each log names the immutable source URL and digest. The population wire traces
exercise [GET /certs](evaluation-logs/120566bc0a941b6e75429cb792e58a41fdf27726df9c745e7b02e0f5db808b18.wire.log)
and parse its declared certificate array, [GET /api/v1/session](evaluation-logs/12704688834f5729410fa352c1d0a0d60627732a822eb7bc9c2534ee627a8532.wire.log)
with its declared bodyless response, and [POST /debitauthorizations](evaluation-logs/2240627eb1a4c3dd6c70fffd5ed527ec02766ddc17f0f05b643a2fccdcd96592.wire.log)
with its request body and typed 201 response. The second omits the required
`opencheck_session` cookie; the third preserves `apiVersion`, `instructedAmount`
and `authorizeToPay` but omits the required `apikey` query credential. The first
trace bypasses TLS and cannot establish whether a client certificate is sent;
its two mypy errors independently require `refuse`. None of these results
establishes full wire/security correctness.

The structural detector rejects nonempty operation security when no supported
scheme is imported, including inherited security in a service that also has a
public operation. A wholly authenticated service instead uses its service-level
refusal. A supported scheme prevents this refusal; unused cookie
schemes and explicit `security: []` do not require authentication. The real
binary journey checks refusal in both modes (one stderr line, no output), then
removes the operation's security requirement and checks byte-identical
generation in both modes.

[The induced baseline failure](evaluation-logs/endpoint-auth-red.log) proves the
recovery e2e rejects the original generator's 36-file false success.

The mixed-service classification also has an observed [unit failure before the
grouping correction](evaluation-logs/mixed-auth-unit-red.log) and a [real binary
failure against the starting generator](evaluation-logs/mixed-auth-e2e-red.log).
Its real journey names the private endpoint and recovers after removing the
inherited requirement.

[All 22 population documents](evaluation-logs/population-refusals.jsonl) were
retrieved at their recorded digests and refused in both modes: exit 1, zero
output files, one stderr line, and `fern-strict` named in strict mode.
`population_strict` is `22/22` and all 22 strict exits are recorded.
