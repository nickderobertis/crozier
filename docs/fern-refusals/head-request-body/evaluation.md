# head-request-body: refuse

The minimal probe declares a required JSON string body on `HEAD /patina`.
Before this detector, crozier's default SDK imported and its public client
completed the request through `httpx.MockTransport`, but sent an empty body.
The [wire assertion](evaluation-logs/default-wire.log) fails because the
required JSON body is omitted. This invalid wire behavior establishes `refuse`;
no generated SDK was repaired to qualify it.

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
