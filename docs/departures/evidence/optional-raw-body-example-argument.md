# An optional raw body's worked call does not match its signature

**Kind:** `fern-defect`, the standing kind *examples that do not match the
signature*.

`tryAGI/AssemblyAI` at `1028f8b6` (corpus row 5623) posts
`application/octet-stream` to `/v2/upload` with no `required` and with
`x-codeSamples`. The certified pair (Fern CLI 5.163.1, `fernapi/fern-python-sdk`
5.41.3) generates `upload(self, *, request: ..., request_options=None)`, so
`request` is a required keyword, and writes `client.files.upload()` in both
client docstrings, `README.md` and `reference.md`. crozier writes the same call
passing `request=b"string"`, the placeholder the `binary-json-body-example`
departure already uses for a bytes parameter.

The worked call is only written where the operation declares `x-codeSamples`:
`atacan/AssemblyAI` at `ed31d2fb` (corpus row 5620) has the same operation
without them, and neither side works it.

[The proof](optional-raw-body-example-argument.py) imports the committed certified
SDK and binds both calls against the real method signature. Run from the
repository root with HTTPX and Pydantic installed; it exits 0 and prints:

```text
certified call client.files.upload(): missing a required keyword-only argument: 'request'
corrected call client.files.upload(request=b"string"): binds
```
