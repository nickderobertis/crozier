# head-request-body: refuse

## At Fern CLI 5.163.1 / fern-python-sdk 5.41.3

Decision: **refuse**, unchanged. The [probe record](fern-refusal.txt) is measured at this pair. The population carries the class on 1 document at this pair, as at Fern CLI 5.67.1. crozier's release build refuses it under `--fern-strict` ([`documents.tsv`](../documents.tsv)).

The evaluation below was written at Fern CLI 5.67.1 / fern-python-sdk 5.20.0. Where it cites a committed shape, that shape's log is now the 5.163.1 measurement and its verdict is its role's; a population count or a Fern log named there is that pair's.

The minimal probe declares a required JSON string body on `HEAD /patina`.
Before this detector, crozier's default SDK imported and its public client
completed the request through `httpx.MockTransport`, but sent an empty body.
The [wire assertion](evaluation-logs/default-wire.log) fails because the
required JSON body is omitted. Under its emitted `pyproject.toml` configuration,
[mypy 1.13.0](evaluation-logs/default-mypy.log) reports zero errors across 29
source files with the project's declared runtime and development dependencies
and HTTP adapter extra installed. Omitting that optional adapter initially
produced a missing-import error; installing the declared extra resolved it.
This invalid wire behavior establishes `refuse`; no generated SDK was repaired
to qualify it.

The detector refuses non-ignored HEAD operations with a request body in both
modes. Its diagnostic names `head-request-body` and the operation's method and
route, adds `fern-strict` in strict mode, and writes no SDK. Removing the body
restores generation, exercised through the compiled CLI by
`head_request_body_refuses_then_recovers`.

The [registered-source scan](evaluation-logs/registered-sources.json) loaded all
241 registered documents with the census reader and found no HEAD operation
with a request body. The existing corpus therefore contains no newly refused
operation. The publisher representative is already refused for a request-name
collision; its committed measurement records exit 1 and no files in both modes.
