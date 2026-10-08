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
| `locker-bank-claims-literals` | [`locker-bank-claims`](../../openapi-surface/handwritten/locker-bank-claims/openapi.yml) | Fern: `enum_type` unset; crozier: `--enum-type literals` | one- and two-member method-name sequences (`vacancies`, `lockers.claim_now`) beside the string `release`, with the `Locker.size` enum an open `Literal` union |
| `meter-reader-gateway-literals` | [`meter-reader-gateway`](../../openapi-surface/handwritten/meter-reader-gateway/openapi.yml) | Fern: `enum_type` unset; crozier: `--enum-type literals` | the `meter_token` credential sent behind `Meter`, with the `Reading.phase` enum an open `Literal` union |
| `ski-lift-gates-literals` | [`ski-lift-gates`](../../openapi-surface/handwritten/ski-lift-gates/openapi.yml) | Fern: `enum_type` unset; crozier: `--enum-type literals` | the `lift_pass` credential read from `LIFT_PASS`, with the `Turnstile.reason` enum an open `Literal` union |
| `lock-keeper-vault-literals` | [`lock-keeper-vault`](../../openapi-surface/handwritten/lock-keeper-vault/openapi.yml) | Fern: `enum_type` unset; crozier: `--enum-type literals` | the `username`/`pass_phrase` pair read from `VAULT_KEEPER`/`VAULT_PASS_PHRASE`, with the `Box.size` enum an open `Literal` union |
| `grid-valve-console-literals` | [`grid-valve-console`](../../openapi-surface/handwritten/grid-valve-console/openapi.yml) | Fern: `enum_type` unset; crozier: `--enum-type literals` | the bearer renamed `api_key` sharing the `X-Api-Key` header key's parameter, examples passing it once, with the `Valve.state` enum an open `Literal` union |
| `twin-key-relay-literals` | [`twin-key-relay`](../../openapi-surface/handwritten/twin-key-relay/openapi.yml) | Fern: `enum_type` unset; crozier: `--enum-type literals` | one `api_key` parameter for the two `X-Api-Key` schemes, examples passing it once, with the inline `priority` enum an open `Literal` union |
| `tide-gauge-sessions-literals` | [`tide-gauge-sessions`](../../openapi-surface/handwritten/tide-gauge-sessions/openapi.yml) | Fern: `enum_type` unset; crozier: `--enum-type literals` | the operation-required `Bearer` scheme read as `bearer`, with the `Level.trend` enum an open `Literal` union |
| `harbour-pilot-regions-literals` | [`harbour-pilot-regions`](../../openapi-surface/handwritten/harbour-pilot-regions/openapi.yml) | Fern: `enum_type` unset; crozier: `--enum-type literals` | `DEFAULT` as the declared default URL beside the `region` variable, with the inline `tug` enum an open `Literal` union |
| `orbit-ground-stations-literals` | [`orbit-ground-stations`](../../openapi-surface/handwritten/orbit-ground-stations/openapi.yml) | Fern: `enum_type` unset; crozier: `--enum-type literals` | the `PRIMARY` and `FAILOVER` members, with the `Pass.band` enum an open `Literal` union |
| `parcel-courier-desk-literals` | [`parcel-courier-desk`](../../openapi-surface/handwritten/parcel-courier-desk/openapi.yml) | Fern: `enum_type` unset; crozier: `--enum-type literals` | the idempotent `ship_parcel` taking `dedupe_token` and the retries-disabled `cancel_parcel`, with the inline `service` enum an open `Literal` union |
| `film-shot-planner-literals` | [`film-shot-planner`](../../openapi-surface/handwritten/film-shot-planner/openapi.yml) | Fern: `enum_type` unset; crozier: `--enum-type literals` | the inline `ShotSize`, `LensSpec` and `IsoBand` types beside the undeclared `GetSettingsResponseLight`, with their enums open `Literal` unions |
| `auction-house-bids-literals` | [`auction-house-bids`](../../openapi-surface/handwritten/auction-house-bids/openapi.yml) | Fern: `enum_type` unset; crozier: `--enum-type literals` | no `bid_placed` method and an ordinary `Bid` type beside `list_lots`, with the `Lot.state` enum an open `Literal` union |
