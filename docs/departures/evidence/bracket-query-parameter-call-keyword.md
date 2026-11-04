# A `[]` query parameter's worked call names no argument

**Kind:** `fern-defect`. The independently authored
[Harbor Ledger document](../../fern-measurements/handed-off/snippet-rendering/snippet-rendering/openapi.yml)
declares two query parameters whose wire names end in `[]`: the required
`codes[]` of `GET /berths` and the required `ids[]` of `DELETE /berths`. Its
unedited complete certified tree sits beside it as `fern-expected/`, generated
by Fern CLI 5.163.1 with `fernapi/fern-python-sdk` 5.41.3 (packaged preview
layout, organization/package `fern`, project `default_package_name`, no
audience filter, `pydantic_config.enum_type: python_enums`).

The certified SDK's methods take `codes` and `ids`
(`src/fern/berths/client.py` declares
`codes: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None` on the
sync and async `list_berths`, lines 30 and 121, and `ids` of the same type on
`release_berths`, lines 69 and 168, and its docstring examples pass `codes=["codes[]"]`). Its `reference.md` worked calls
instead pass `codes_array=[` (line 90) and `ids_array=[` (line 159). The same
spelling reaches a real document: arawa/workspace's `uids[]` is
`uids_array=[` in both of its `reference.md` calls, beside methods taking `uids`
(the handed-off comparison in
[`../../fern-measurements/handed-off/snippet-rendering/README.md`](../../fern-measurements/handed-off/snippet-rendering/README.md)).

## Executed certified-output evidence

With the SDK's HTTPX and Pydantic dependencies installed, execute the committed
[proof script](bracket-query-parameter-call-keyword.py) against the certified
tree:

```sh
python docs/departures/evidence/bracket-query-parameter-call-keyword.py \
  docs/fern-measurements/handed-off/snippet-rendering/snippet-rendering/fern-expected/src \
  --reference docs/fern-measurements/handed-off/snippet-rendering/snippet-rendering/fern-expected/reference.md \
  --expected invalid
```

Run on 2026-11-03 (Python 3.14, HTTPX 0.28.1, Pydantic 2.14.0), it exited 0 and
printed:

```text
{"bindings": {"AsyncFernApi.list_berths": "got an unexpected keyword argument 'codes_array'", "AsyncFernApi.release_berths": "got an unexpected keyword argument 'ids_array'", "FernApi.list_berths": "got an unexpected keyword argument 'codes_array'", "FernApi.release_berths": "got an unexpected keyword argument 'ids_array'"}, "requests": 3}
```

The script imports the actual certified package, parses each worked call out of
`reference.md` with Python's AST, and binds its keyword arguments to
`inspect.signature` of the actual sync and async methods: every binding raises
`TypeError`. It then calls each method with the argument it does declare, through the
public client over a socket to a local HTTP server, and asserts the request the
server receives carries the values under the `codes[]` and `ids[]` wire names, so the defect is the documentation's alone.
Run the same way over crozier's generated tree with `--expected valid`, every
binding succeeds (`codes binds`, `ids binds`) and the same requests are sent.

## The rule

`bracket_query_parameter_call_keyword` admits only a README or `reference.md`
line whose sole change replaces `<name>_array=` with `<name>=`, for a query
parameter `<name>[]` the source document declares. A header with a `[]` name,
an undeclared name, a changed indentation or value, and every code file still
fail. `reference.md`'s parameter list keeps the certified `**<name>_array:**`
spelling, matched byte for byte. The unit test
`bracket_query_call_keywords_admit_only_the_declared_parameter_spelled_out`
holds those cases; the measurement's crozier-e2e journey compares the whole tree
with this departure applied and fails an unexplained byte beside it.
