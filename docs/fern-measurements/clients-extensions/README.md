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
| `depot-bin-ledger-literals` | [`depot-bin-ledger`](../../openapi-surface/handwritten/depot-bin-ledger/openapi.yml) | Fern: `enum_type` unset; crozier: `--enum-type literals` | untagged `list`/`set` kept and `map` suffixed, tagged `bool`, `float`, `int`, `long` and `uuid` suffixed and `list` kept, when the `Bin.material` enum is an open `Literal` union |
| `ferry-berth-desk-literals` | [`ferry-berth-desk`](../../openapi-surface/handwritten/ferry-berth-desk/openapi.yml) | Fern: `enum_type` unset; crozier: `--enum-type literals` | tag-prefixed hyphenated ids lowercased (`checkstatus`, `assignvessel`, `all_`), two hyphens and the untagged id snake-cased, with the `BerthStatus.state` enum an open `Literal` union |
| `rfid-door-panel-literals` | [`rfid-door-panel`](../../openapi-surface/handwritten/rfid-door-panel/openapi.yml) | Fern: `enum_type` unset; crozier: `--enum-type literals` | the all-capitals `RFID` tag named from the tag with its split-prefix id kept whole, beside grouped `rfid_list` and `doors_doorgroups_list` and the ungrouped `badgeReaders_get`, with the `Decision.outcome` enum an open `Literal` union |
| `signal-box-relays-literals` | [`signal-box-relays`](../../openapi-surface/handwritten/signal-box-relays/openapi.yml) | Fern: `enum_type` unset; crozier: `--enum-type literals` | underscore-led group segments kept (`client._relays.reset`, `client._audit._trail.export`) beside the plain `signals` group, with the `RelayState.state` enum an open `Literal` union |
| `cargo-hold-pallets-literals` | [`cargo-hold-pallets`](../../openapi-surface/handwritten/cargo-hold-pallets/openapi.yml) | Fern: `enum_type` unset; crozier: `--enum-type literals` | group names without a method name ignored (root `list_pallets`, tagged `scales.weigh_pallet`) beside the honoured `manifests.list`, with the `Pallet.deck` enum an open `Literal` union |
