# Client and package construction, measured under other settings

Each directory here is a tree Fern generated at Fern CLI 5.67.1 with
`fernapi/fern-python-sdk` 5.20.0 under a setting other than the one its
document's own gate uses, comment-stripped by `crozier internal-strip`. The
trees are Fern's output as measured; nothing in them was edited. The workspace
is the one `scripts/generate-fern-fixture.sh` scaffolds (Route A of
[`../../fern-goldens.md`](../../fern-goldens.md)), built outside any checkout.
`clients_extensions_measurements_match_fern` in
[`../../../tests/e2e.rs`](../../../tests/e2e.rs) generates each case's document
with crozier under the same setting and holds the whole tree to
`fern-expected/` under the corpus gate's normalization.

This is no corpus fixture and no coverage probe: it is never a `CORPUS.md` row
and settles no coverage row.

## The cases

| case | document | setting | what it pins |
|---|---|---|---|
| `impedance-complex-reading-literals` | [`impedance-complex-reading`](../../openapi-surface/handwritten/impedance-complex-reading/openapi.yml) | Fern: `enum_type` unset; crozier: `--enum-type literals` | the reserved `complex` (`types/complex_.py`, `complex_` field, method and query argument) when the `Form` enum is an open `Literal` union with no `visit` method, beside the fixture's `python_enums` tree |
