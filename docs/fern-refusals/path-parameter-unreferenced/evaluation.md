# path-parameter-unreferenced: refuse

Baseline: `2b046a72f1fb687c5ef2399d492a5fd2b57cab3b`. No emitted SDK was
repaired to change the result. Probe checks use CPython 3.12.3, the generated
project's mypy 1.13.0 configuration, and its installed dependencies.

The [probe log](evaluation-logs/probe.log) records successful package/client
imports and **zero mypy errors**. Its [wire journey](evaluation-logs/probe.wire.log)
passes `SENTINEL_ID` to the method's required `id` argument. The request is
still `GET /things`, with no parameter value in the URL or body; the empty
204 parses as `None`. The declared required path parameter is silently dropped
on the wire. That fails the useful-output rule even though imports and typing
pass, so the class is `refuse` in both modes.

One representative from [APWG/ecx2-openapi-doc,
`112b5d9658df34218ea3c584e82ff8a1bfdfe13771826326cbfb7c60b237ba3e`](evaluation-logs/population.log)
has unreferenced `noteId` declarations on note operations. Default baseline
generation exits 1 when ruff cannot parse an emitted model. There is no SDK
to import or type-check: **mypy count unavailable, not run**, rather than zero
errors; no request or response journey can run. The committed log records the
immutable source, digest, command, exit and exact formatting failure. Its
failure independently meets the task's explicit rule that failing generation
cannot qualify a class. Further representatives cannot rescue this class.

The structural detector reads inline and component-referenced path parameters
on operations and shared Path Items, comparing their exact wire names with
`{name}` placeholders. Colon-prefixed and `{+name}` routes do not invent
placeholders Fern accepts. It skips operations pruned by the existing
canonical ignore accessor; it never renames a parameter or changes a route.
The CLI recovery journey adds the missing placeholder and verifies identical
SDK bytes in both modes; an ignored operation also generates. Its refusal
assertion was [observed failing before the detector](evaluation-logs/refusal-e2e-red.log).

[All 29 population documents](evaluation-logs/population-refusals.jsonl) were
retrieved at their recorded digests and refused in both modes: exit 1, no
output, one class/element line and the strict cause where applicable.

A separate CLI journey covers a shared Path Item parameter referring to
`components.parameters.ThingId`: both modes refuse its absent placeholder,
and adding `{id}` restores generation. The [assertion was observed failing
with the detector disabled](evaluation-logs/shared-path-e2e-induced-red.log);
the mutation was reverted before the green run.
