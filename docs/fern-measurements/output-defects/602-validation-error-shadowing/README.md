# A schema named `ValidationError` beside the runtime exception

Issue [#602](https://github.com/nickderobertis/crozier/issues/602).
[`openapi.yml`](openapi.yml) was authored from scratch: a component schema
`ValidationError` that a JSON operation returns, that an event-stream
operation yields, and that all three operations, including a binary
download, return as their `422` body. So each raw-response path imports the
schema into `raw_client.py` beside pydantic's exception of the same name.

`fern-expected/` is the complete, comment-stripped tree Fern CLI 5.163.1 with
`fernapi/fern-python-sdk` 5.41.3 generated from it, through
`just fern-references measurements
output-defects/602-validation-error-shadowing` (the case is a
[`../../cases.tsv`](../../cases.tsv) row). Nothing in it was edited.

## Comparison

Both generators alias the two imports in `raw_client.py`:

```python
from .types.validation_error import ValidationError as types_validation_error_ValidationError
from pydantic import ValidationError as pydantic_ValidationError
```

Fern catches `pydantic_ValidationError` in all six raw methods (sync and
async, for the JSON, event-stream and binary-download paths). crozier caught
the bare `ValidationError`, a name that file never binds. Every other file
matched.

## Verdict: parity gap, repaired

Fern's output is not defective. [`runtime.txt`](runtime.txt) runs both SDKs
against a local HTTP server whose responses fail validation. Fern's SDK raises
`ParsingError` caused by pydantic's `ValidationError` on all six methods.
crozier's SDK, before this repair, raised `NameError: name 'ValidationError' is
not defined`. crozier now catches the alias that `Imports` assigned
(`emit::raw_body`, `raw_stream_method`, `raw_binary_stream_method`) and
byte-matches this tree apart from the catalogued `sdk-identity-header-prefix`
and `stream-reference-return-type` departures that the ledger records.

These hold it:

- `output_defect_measurements_match_fern` in
  [`crates/crozier-e2e/tests/e2e.rs`](../../../../crates/crozier-e2e/tests/e2e.rs),
  which compares the whole tree;
- `sdk_env_output_defect_sdks_parse_and_send_what_fern_does`, which runs the
  journey on crozier's SDK;
- the unit test
  `a_validation_error_schema_aliases_the_exception_every_raw_parser_catches`
  in `src/emit.rs`.

No registered golden imports the aliased exception, so the repair moves none.
