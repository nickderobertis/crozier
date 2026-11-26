# Required typeless body arguments in worked calls

**Kind:** `fern-defect`. Measured at Fern CLI 5.216.0 / fern-python-sdk 5.42.0.

A JSON body that requires a typeless (`{}`) value gets no importer example
from Fern. On the screened witness candidate Aether
(`Science-Discovery/Aether/packages/sdk/openapi.json`, sha256 `74a8b9b2…`)
three operations take one: `tui.control.response` (a whole `{}` body),
`knowledge.state.post` (inline, `required: [data]`, `data: {}`) and
`reading-mode.annotations.update` (inline, `required: [sessionID, data]`).
The generated methods require those arguments — `request: typing.Any`,
`data: typing.Any`, `session_id: str, data: typing.Any`, none with a default —
and the certified pair's tree, in both enum modes, documents each as the bare
call (`client.knowledge_state_post()`) in `reference.md` and both docstrings.

pyright 1.1.408 (basic mode), every worked example of the certified
python-enums tree each its own module, against the tree's own `src/`:

```text
s0164_reference.py:7:1 - error: Argument missing for parameter "request" (reportCallIssue)
s0168_reference.py:7:1 - error: Argument missing for parameter "data" (reportCallIssue)
s0218_reference.py:7:1 - error: Arguments missing for parameters "session_id", "data" (reportCallIssue)
... the same three for each docstring (sync and async): 9 in all
```

crozier passes exactly the required arguments (`request={"key": "value"}`,
`data={"key": "value"}`, `session_id="sessionID", data={"key": "value"}`),
and the same check over crozier's tree reports none of the nine; the errors
both trees share are the matched module-level `yield` of streaming examples.
A required field the schema makes nullable (`extra: anyOf [{}, null]`) is no
such argument: crozier matches the pair, leaving it out of the docstring and
writing `extra=None` in the Markdown.

The region rule admits a crozier call only where Fern's is the bare call at
that place and every argument crozier passes is one its method declares
without a default. Its unit test rejects an optional argument and a Fern call
that passes anything; the departures ledger pins every occurrence.
