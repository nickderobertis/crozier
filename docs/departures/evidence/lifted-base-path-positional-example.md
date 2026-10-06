# `lifted-base-path-positional-example`

**Kind:** `fern-defect`. Fern's docstring examples pass a lifted base-path
parameter's default to the client constructor positionally, and the
constructor is keyword-only.

## The input

The crozier-authored documents
[`base-path-lifted-default/openapi.yml`](../../fern-measurements/parameter-lowering/base-path-lifted-default/openapi.yml)
and
[`base-path-lifted-unincluded/openapi.yml`](../../fern-measurements/parameter-lowering/base-path-lifted-unincluded/openapi.yml):
a document-level `x-fern-base-path` object whose `path` is `/{edition}`, with
`parameters: {edition: {type: string, default: v2}}`, the second without
`paths-include-base-path` and with routes that do not repeat the prefix.

## Fern's output

Fern CLI 5.67.1 with `fernapi/fern-python-sdk` 5.20.0, generated as
[`lifted-base-path-docs-examples`](lifted-base-path-docs-examples.md#fern-s-output)
describes, exits 0 on both; the comment-stripped trees are each document's
`fern-expected/`. The constructor is

```python
def __init__(self, *, base_url=None, environment=…, edition: typing.Optional[str] = "v2", …)
```

and every constructor example in a docstring — `src/fern/client.py` lines 64
and 177, `src/fern/layers/client.py` lines 56, 84, 138 and 174 — reads

```python
client = FernApi(
    "v2",
)
```

## Why it is a defect

With the tree's `src/` on `PYTHONPATH` beside `httpx` and `pydantic` (a copy):

```text
$ python -c 'from fern import FernApi; FernApi("v2")'
TypeError: FernApi.__init__() takes 1 positional argument but 2 were given
$ python -c 'from fern import FernApi; FernApi(edition="v2")'
$
```

The example call does not match the generated signature, so it cannot run: a
defect under the defect rule. (Without a default, Fern writes
`edition="YOUR_EDITION"` by keyword, which is correct and matched.)

## crozier's output

crozier writes `edition="v2",` on each of those lines. `crozier compare` over
the pair matches and reports this departure at each line;
those are the trees' `lifted-base-path-positional-example` rows in
`tests/fixtures/departures-ledger.tsv`, and
`compare_reports_the_lifted_base_path_departures_and_fails_on_any_other_difference`
in `tests/e2e/compare.rs` drives it.
