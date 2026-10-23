# Reference
## Chains
<details><summary><code>client.chains.<a href="src/fern/chains/client.py">list_robinhood_chain_networks</a>() -> GetChainsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Public. The public RPC URL, the explorer and whether Fletch has a provider key for the chain; a configured provider URL is never returned.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.chains.list_robinhood_chain_networks()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chains.<a href="src/fern/chains/client.py">token_identity_and_current_market_observations_at_one_contract_address</a>(...) -> GetTokensAddressResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Public. The canonical trust verdict is shared by pages and pool responses. A lookalike records a normalized name or ticker collision; it does not establish intent. `reading` is the exact token-page observation: full address, economic selection reason, same-name alternatives, selected-pool volume, market cap and holders with source, timestamp and missing-value reason. Community dominance is an economic comparison. `market` retains the compact selected-pool view. V3 quote holdings and V4 bounded 1% quote input are separate measures. Volume sources distinguish nominal USDG quote units from WETH converted with a historical oracle estimate.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.chains.token_identity_and_current_market_observations_at_one_contract_address(
    address="0x0000000000000000000000000000000000000000",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**address:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chains.<a href="src/fern/chains/client.py">get_app_catalog</a>(...) -> GetAppCatalogResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Public. Includes symbols without a known on-chain contract. Display-only means a price feed without app trading. Inspect per-account tradability, stale and error. Symbols are ticker matches, not contract verification. Follow nextOffset until null. Pages read the current snapshot, which can change between requests. The observer targets 15 seconds; this endpoint reads its stored result.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.chains.get_app_catalog(
    chain_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chain_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[GetAppCatalogRequestStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chains.<a href="src/fern/chains/client.py">priority_tokens_one_contract_per_row_ordered_by_observed_selected_pool_volume</a>(...) -> GetChainsChainIdMarketsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Public. Listed assets and selected major community contracts use the same token read model as token pages and /tokens/{address}. Each metric carries structured observation provenance, computation inputs, coverage, source/fetch times and expiry, alongside compatibility source/asOf/reason fields. Pool state expires after three minutes, changing supply and burn balances after five minutes, and selected-pool swap windows after two minutes. Capitalization expires with its earliest-expiring required input. Missing legacy provenance remains null. Selection time and its fifteen-minute policy expiry are explicit; stale selection withholds dominance. Volume covers the selected pool only. Missing volume sorts last with a stable name/address tie-break. Economic dominance never changes a trust verdict. The selected universe and same-name comparisons are bounded; registry history remains available through the pool and asset endpoints.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.chains.priority_tokens_one_contract_per_row_ordered_by_observed_selected_pool_volume(
    chain_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chain_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**kind:** `typing.Optional[GetChainsChainIdMarketsRequestKind]` — all: Issuer listings and priority community contracts. listed: Contracts in the issuer list, including pending checks. community: Priority contracts outside the issuer list. Check their trust badge.
    
</dd>
</dl>

<dl>
<dd>

**trust:** `typing.Optional[GetChainsChainIdMarketsRequestTrust]` — all: Keep every recorded identity verdict. verified: Issuer listing and matching contract checks. listed: Issuer listing with checks still incomplete. community: Resolved metadata with no recorded issuer-name collision. lookalike: Name or symbol collides with a verified asset. unknown: Identity calls have not resolved this contract.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetChainsChainIdMarketsRequestSort]` — volume: Selected-pool USD volume, highest first. swaps: Selected-pool swap events, highest first. market_cap: Outstanding supply estimate times current price, highest first. v3_depth: Observed quote-side holdings in dollars, highest first. v4_depth: Bounded quote input for a 1% move, highest first. name: Alphabetical name, then contract address.
    
</dd>
</dl>

<dl>
<dd>

**activity:** `typing.Optional[GetChainsChainIdMarketsRequestActivity]` — all: Include incomplete and unavailable swap windows. traded: At least one swap in a complete current 24-hour window. busy: At least 100 swaps in a complete current window. quiet: A complete current window with exactly zero swaps.
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Optional[GetChainsChainIdMarketsRequestData]` — all: Keep unavailable measures with their reason. priced: Usable selected-pool price with pool state and quote conversion inside their three-minute freshness policy. volume: Valued 24-hour window counted through the last two minutes. complete: All three measures have usable current inputs.
    
</dd>
</dl>

<dl>
<dd>

**depth:** `typing.Optional[GetChainsChainIdMarketsRequestDepth]` — all: Keep both pool types and unavailable observations. v3_10k: At least $10,000 of current quote-side holdings. v3_100k: At least $100,000 of current quote-side holdings. v4_1k: At least $1,000 of bounded quote input for a 1% move. v4_10k: At least $10,000 of bounded quote input for a 1% move.
    
</dd>
</dl>

<dl>
<dd>

**identity:** `typing.Optional[GetChainsChainIdMarketsRequestIdentity]` — all: One row per recorded priority contract. dominant: Community contracts selected by the recorded economic comparison. same_name: Contracts with alternatives in the recorded comparison set. close_call: The dominance comparison recorded a close call.
    
</dd>
</dl>

<dl>
<dd>

**min_volume_usd:** `typing.Optional[float]` — Inclusive selected-pool USD volume threshold. Requires a complete current valued window.
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chains.<a href="src/fern/chains/client.py">discover_token_market_filters_labels_thresholds_and_useful_query_presets</a>(...) -> GetChainsChainIdMarketsFiltersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The catalog used by the token Markets page and query parser. Combine filters with AND. Activity requires a complete current selected-pool window. Numeric thresholds exclude unavailable data, including for a threshold of zero. V3 quote holdings and V4 bounded depth are separate filters and sorts.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.chains.discover_token_market_filters_labels_thresholds_and_useful_query_presets(
    chain_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chain_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chains.<a href="src/fern/chains/client.py">indexed_pools_with_token_identity_separate_depth_measures_and_current_swap_observations</a>(...) -> GetChainsChainIdDexPoolsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Public. `kind=listed` filters membership in Robinhood's list; `kind=community` keeps unlisted priced tokens; `kind=lookalike` selects recorded collisions. The response `kind` is an alias of the canonical `trust` verdict; `listing` retains membership separately. `sort=volume` ranks actual current 24-hour volume, missing values last, with pool identity as the tie-break. `traction` explicitly adds depth and swap-count tie-breaks. Search accepts token names, tickers, full contracts, v3 pool addresses and v4 pool IDs. Swap and transaction counts require a complete current window. Volume sources distinguish nominal USDG denomination and historical WETH oracle estimates. V3 quote holdings and V4 bounded 1% quote input retain distinct labels and never form a combined TVL.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.chains.indexed_pools_with_token_identity_separate_depth_measures_and_current_swap_observations(
    chain_id=1,
    q="PIPE",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chain_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**kind:** `typing.Optional[GetChainsChainIdDexPoolsRequestKind]` — Also accepted as `trust`.
    
</dd>
</dl>

<dl>
<dd>

**tier:** `typing.Optional[GetChainsChainIdDexPoolsRequestTier]` — Which tiers to list; the default is the pools worth watching.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[GetChainsChainIdDexPoolsRequestSort]` 
    
</dd>
</dl>

<dl>
<dd>

**venue:** `typing.Optional[GetChainsChainIdDexPoolsRequestVenue]` 
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Token or pool name, symbol, or a complete 0x address. Addresses are matched in full.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Registry
<details><summary><code>client.registry.<a href="src/fern/registry/client.py">search_issuer_listed_assets_and_their_recorded_chain_observations</a>(...) -> GetChainsChainIdAssetsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Public. Anonymous callers get 120 requests a minute per address; a key or a session uses its own budget. Each asset carries `state`: multiplier, pending multiplier, pause flags, supply, recorded beacon dependency, the Chainlink feed and Robinhood's quote.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.registry.search_issuer_listed_assets_and_their_recorded_chain_observations(
    chain_id=1,
    symbols="TSLA,AAPL",
    fields="lookalikes,feedRounds,concentration",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chain_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**trust:** `typing.Optional[GetChainsChainIdAssetsRequestTrust]` — Filter the Robinhood listing collection by its shared trust verdict. Community tokens are resolved by /tokens/{address} and listed under /dex/pools; they are not added to Robinhood's registry.
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Symbol or name substring
    
</dd>
</dl>

<dl>
<dd>

**symbols:** `typing.Optional[str]` — Comma-separated exact tickers, up to 200; any past that are ignored
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Extra per-asset blocks: lookalikes, corporateActions, multiplierHistory, feedRounds, concentration (up to 50 assets)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.registry.<a href="src/fern/registry/client.py">get_one_registry_asset_by_symbol_with_its_state_multiplier_history_mints_and_burns_supply_snapshots_corporate_actions_and_control_plane_events</a>(...) -> GetChainsChainIdAssetsSymbolResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Public, rate-limited per address when anonymous. Raw amounts are strings (exact on chain); prices and multipliers are numbers.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.registry.get_one_registry_asset_by_symbol_with_its_state_multiplier_history_mints_and_burns_supply_snapshots_corporate_actions_and_control_plane_events(
    chain_id=1,
    symbol="AAPL",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chain_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**symbol:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.registry.<a href="src/fern/registry/client.py">holders_largest_first_with_share_of_supply_and_what_each_address_is_holder_count_the_latest_concentration_reading_with_the_shares_that_say_where_the_supply_sits_and_whether_the_ledger_has_reached_the_chain_head</a>(...) -> GetChainsChainIdAssetsSymbolHoldersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Public. `sits` is always one of `float`, `pools`, `issuer`, `bridge`, `contracts`, `unknown`, and names the concentration share this address's balance counts towards; `unknown` means the code probe has not checked this address yet. `label` and `labelKind` (`pool_manager`, `dex_pool`, `issuer`, `bridge_gateway`, `locker`, `contract`, `exchange`, `eoa`) are null for an address the registry has nothing to say about. `rawBalance` is in the token's base units; divide by 10^`decimals`. `sharePct` is that balance over `totalSupplyRaw`, read live, while the concentration shares are over the sum of every positive balance the ledger held at `concentration.asOfBlock`, so the two can differ slightly while the ledger trails the chain. `concentration` carries `top1Pct`, `top10Pct` and `gini` over every positive balance, and the six shares `floatPct`, `poolsPct`, `issuerPct`, `bridgePct`, `contractsPct` and `unknownPct`, which add to 100: float is the supply in ordinary wallets. `unknownPct` is the share held by addresses the code probe has not checked — it checks every holder above a ten-thousandth of a token's supply, so a tail of small holdings stays here permanently and `floatPct` is always a floor rather than a final answer. `issuerPct` is the share of every wallet labelled `issuer`, which is written only for Stock Tokens, whose mints are the issuer creating inventory; `issuerAddress` is this asset's largest mint recipient whatever the asset type. `concentration.day` is the UTC day of the reading, `takenAt` the ISO instant the job wrote it, and `asOfBlock` the ledger block it was computed at; the job runs every 24 h, so a share can be up to a day old. `concentration.holders` is the address count at that moment, while the top-level `holderCount` is read live and can differ. The shares come from the daily concentration job, which does not run while the transfer ledger is still reading history, so `concentration` is null until the ledger reaches head.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.registry.holders_largest_first_with_share_of_supply_and_what_each_address_is_holder_count_the_latest_concentration_reading_with_the_shares_that_say_where_the_supply_sits_and_whether_the_ledger_has_reached_the_chain_head(
    chain_id=1,
    symbol="TSLA",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chain_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**symbol:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — How many holders, largest first
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.registry.<a href="src/fern/registry/client.py">transfers_as_economics_one_row_per_utc_day_transfers_volume_mints_burns_dv_p_against_usdg_off_hours_transfers</a>(...) -> GetChainsChainIdAssetsSymbolActivityResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.registry.transfers_as_economics_one_row_per_utc_day_transfers_volume_mints_burns_dv_p_against_usdg_off_hours_transfers(
    chain_id=1,
    symbol="TSLA",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chain_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**symbol:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**days:** `typing.Optional[int]` — How many UTC days back; a malformed value reads as the default
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.registry.<a href="src/fern/registry/client.py">pools_trading_the_asset_on_every_dex_the_registry_reads_deepest_first_with_venue_price_liquidity_fee_hooks_last_day_swaps_and_volume_and_the_pool_behind_the_assets_premium_to_the_feed</a>(...) -> GetChainsChainIdAssetsSymbolPoolsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Public. `venue` is `uniswap_v4` or `uniswap_v3`; a v4 pool is an id inside the one PoolManager and has a null `poolAddress`, a v3 pool is a contract and carries its address. A pool is recorded when one side is this asset and the other is a listed quote (USDG, WETH or another Stock Token). Pools are deepest first by `depthUsd`. V3 depth uses observed quote-side holdings. V4 depth uses a bounded quote estimate for a 1% price move, where per-pool token reserves are unavailable; `liquidity` is the pool's in-range Uniswap liquidity L in raw units, not a dollar figure, and is comparable only between pools of the same pair (its scale follows the two tokens' decimals). `best` is the deepest pool in dollars of any venue, which is the one the asset's premium to the Chainlink feed is measured from, and names its venue. `swaps24h` counts swap logs and `transactions24h` counts distinct transactions in (metricsAsOf - 24 hours, metricsAsOf], using each event block timestamp. Values are null until the entire window is indexed and when its end is more than 120 seconds old. `volumeUsd24h` uses the indexed quote leg. USDG is nominally denominated at 1 USDG = $1; WETH uses a recorded historical oracle estimate with at most one-hour archive sample age and an oracle answer within its published heartbeat. `volumeValuation` retains the method and coverage reason. Zero means a completely scanned window with no matching activity. `discovery` says how far each venue's pool scan has read: while `readingHistory` is true, a pool created in blocks the scan has not reached yet is not listed, and a venue whose `scanned` is false has not been read at all.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.registry.pools_trading_the_asset_on_every_dex_the_registry_reads_deepest_first_with_venue_price_liquidity_fee_hooks_last_day_swaps_and_volume_and_the_pool_behind_the_assets_premium_to_the_feed(
    chain_id=1,
    symbol="TSLA",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chain_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**symbol:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.registry.<a href="src/fern/registry/client.py">one_row_per_utc_day_of_everything_the_registry_publishes_about_an_asset_multiplier_pause_and_halt_flags_feed_price_and_staleness_bid_and_ask_divergence_dex_price_premium_and_liquidity_supply_holders_and_lookalike_count</a>(...) -> GetChainsChainIdAssetsSymbolHistoryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Public. Written by the state-daily job, which runs hourly and rewrites the current UTC day's row, so a past day can be read back; the live tables carry only the current answer. Each row is a single reading taken at `takenAt`, not a daily open, close, mean or end-of-day value: it is the last reading the job took on that day, and the row for the current day is rewritten on the job's next run, so today's row is a partial day. Compare `takenAt` across rows before treating the series as evenly spaced. `from`/`to` are UTC days and default to the last 90; `days` sets the window length instead of `from`; `at=YYYY-MM-DD` returns that one day (an empty `days` array when no snapshot was taken); `fields` narrows each row to the keys named, `day` always included. `coverage` says how many days are actually on record and the first of them: there is nothing before the day the job first ran. A null is a figure that was not read that day, never a zero: a figure is copied only when the job that writes it read it that day, and `stateCheckedAt`, `feedCheckedAt`, `apiCheckedAt`, `dexCheckedAt` and `blockscoutCheckedAt` say when each group of figures was last read. `ledgerHolders` is written only for assets whose transfer history the ledger had finished reading, and `lookalikes` only once the lookalike scan has completed a pass. Rows are flat versions of the live `state` block: `feedPrice`/`feedStale` are `state.feed.price`/`.stale`, `bid`/`ask`/`tradingHalt` are `state.quote.bid`/`.ask`/`.tradingHalt`, `dexPriceUsd`/`dexPremiumPct`/`dexLiquidity` are `state.dex.priceUsd`/`.premiumPct`/`.liquidity`, `blockscoutHolders` is `state.secondSource.holders`, `multiplier` is `state.multiplier`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
import datetime

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.registry.one_row_per_utc_day_of_everything_the_registry_publishes_about_an_asset_multiplier_pause_and_halt_flags_feed_price_and_staleness_bid_and_ask_divergence_dex_price_premium_and_liquidity_supply_holders_and_lookalike_count(
    chain_id=1,
    symbol="TSLA",
    at=datetime.date.fromisoformat("2026-08-12"),
    fields="feedPrice,dexPremiumPct",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chain_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**symbol:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[datetime.date]` — First UTC day, YYYY-MM-DD; must not be after `to`
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[datetime.date]` — Last UTC day, YYYY-MM-DD; defaults to today
    
</dd>
</dl>

<dl>
<dd>

**days:** `typing.Optional[int]` — Window length in days ending at `to`; ignored when `from` is given
    
</dd>
</dl>

<dl>
<dd>

**at:** `typing.Optional[datetime.date]` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[str]` — Comma-separated keys to keep from each row: multiplier, tokenPaused, oraclePaused, tradingHalt, feedPrice, feedStale, bid, ask, priceDivergencePct, dexPriceUsd, dexPremiumPct, dexLiquidity, totalSupplyRaw, blockscoutHolders, ledgerHolders, lookalikes, stateCheckedAt, feedCheckedAt, apiCheckedAt, dexCheckedAt, blockscoutCheckedAt, takenAt. `day` is always included; an unknown key is a 400.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.registry.<a href="src/fern/registry/client.py">the_chainlink_feeds_round_history_for_one_asset_newest_first_round_id_answer_price_multiplier_usd_started_at_updated_at</a>(...) -> GetChainsChainIdAssetsSymbolFeedRoundsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.registry.the_chainlink_feeds_round_history_for_one_asset_newest_first_round_id_answer_price_multiplier_usd_started_at_updated_at(
    chain_id=1,
    symbol="TSLA",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chain_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**symbol:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Rounds, newest first; a malformed value reads as the default, a larger one as the maximum
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Chain
<details><summary><code>client.chain.<a href="src/fern/chain/client.py">the_issuers_access_controls_registry_paused_implementation_blocked_address_count_and_its_latest_events</a>(...) -> GetChainsChainIdControlPlaneResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Public. One contract governs every Stock Token: this is the surface no other index publishes. `limit` caps events (default 50, max 200), newest first. `offset` skips that many events, so `offset=200&limit=200` is the second page; an event that lands between two page reads repeats one row on the next page, so a consumer copying the log dedupes by `txHash` and `logIndex`. A page shorter than `limit` is the last one. `state` is the same on every page.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.chain.the_issuers_access_controls_registry_paused_implementation_blocked_address_count_and_its_latest_events(
    chain_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chain_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Events per page (default 50)
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Events to skip before the page (default 0)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chain.<a href="src/fern/chain/client.py">the_chains_latest_vital_signs_head_block_time_base_fee_l1block_batch_count_delayed_messages_batch_poster_balance_status_page</a>(...) -> GetChainsChainIdHealthResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.chain.the_chains_latest_vital_signs_head_block_time_base_fee_l1block_batch_count_delayed_messages_batch_poster_balance_status_page(
    chain_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chain_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chain.<a href="src/fern/chain/client.py">corporate_actions_in_progress_as_robinhood_publishes_them_tied_to_the_token_each_affects</a>(...) -> GetChainsChainIdCorporateActionsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.chain.corporate_actions_in_progress_as_robinhood_publishes_them_tied_to_the_token_each_affects(
    chain_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chain_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chain.<a href="src/fern/chain/client.py">the_dex_venues_the_registry_reads_and_what_each_contributes_pools_trading_a_listed_asset_how_many_carry_a_dollar_price_the_last_days_swaps_and_volume_and_how_many_assets_take_their_premium_from_a_pool_there</a>(...) -> GetChainsChainIdDexResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Public. One row per venue read (`uniswap_v4`, `uniswap_v3`), whether or not it has a pool on record yet, so `venues` and `discovery` name the same set. `assetsPricedHere` counts the assets whose deepest pool in dollars sits on that venue, so the venues' figures add up to the assets with a DEX price. `depthUsd` sums depth over the venue's priced pools: observed quote-side holdings for v3, and a bounded quote estimate for a 1% price move for v4 where per-pool token reserves are unavailable; Uniswap's raw liquidity L compares two pools only when they hold the same pair. `swaps24h` counts swap logs and `transactions24h` counts distinct transactions in (metricsAsOf - 24 hours, metricsAsOf], using each event block timestamp. Values are null until the entire window is indexed and when its end is more than 120 seconds old. `volumeUsd24h` uses the indexed quote leg. USDG is nominally denominated at 1 USDG = $1; WETH uses a recorded historical oracle estimate with at most one-hour archive sample age and an oracle answer within its published heartbeat. `volumeValuation` retains the method and coverage reason. Zero means a completely scanned window with no matching activity. `checkedAt` is when the state read last priced a pool on that venue; `headAt` inside `discovery` is when the chain head there was read. `discovery` carries each venue's pool scan position against that head; while `readingHistory` is true the counts are a floor, not a total, and while `scanned` is false the venue has not been read at all. The Pons launchpad creates its pools on the Uniswap v3 factory, so they are counted as `uniswap_v3` rather than as a venue of their own.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.chain.the_dex_venues_the_registry_reads_and_what_each_contributes_pools_trading_a_listed_asset_how_many_carry_a_dollar_price_the_last_days_swaps_and_volume_and_how_many_assets_take_their_premium_from_a_pool_there(
    chain_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chain_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chain.<a href="src/fern/chain/client.py">the_token_bridge_each_bridged_assets_l1escrow_against_its_l2supply_recent_deposits_and_withdrawals_seen_on_l2and_withdrawals_past_their_seven_day_window</a>(...) -> GetChainsChainIdBridgeResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.chain.the_token_bridge_each_bridged_assets_l1escrow_against_its_l2supply_recent_deposits_and_withdrawals_seen_on_l2and_withdrawals_past_their_seven_day_window(
    chain_id=1,
    symbol="WBTC",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chain_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**symbol:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Flows, newest first; a malformed value reads as the default, a larger one as the maximum
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chain.<a href="src/fern/chain/client.py">the_issuers_paperwork_every_pdf_the_legal_hub_lists_with_e_tag_last_modified_and_the_token_it_maps_to_plus_watched_pages_and_when_their_text_changed</a>(...) -> GetChainsChainIdIssuerResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.chain.the_issuers_paperwork_every_pdf_the_legal_hub_lists_with_e_tag_last_modified_and_the_token_it_maps_to_plus_watched_pages_and_when_their_text_changed(
    chain_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chain_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**kind:** `typing.Optional[GetChainsChainIdIssuerRequestKind]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.chain.<a href="src/fern/chain/client.py">recorded_name_and_ticker_collisions_at_different_contract_addresses_with_available_holder_counts_and_beacon_checks</a>(...) -> GetChainsChainIdLookalikesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Public. Most held first. A collision describes reused labels; it does not establish intent or issuer identity. `limit` caps rows (default 300, max 1000); `offset` skips that many rows, so `offset=1000&limit=1000` is the second page, and a page shorter than `limit` is the last one. Holder counts are refreshed by the lookalike scan, so the order can shift between pages read across a scan: a consumer copying the whole table dedupes by `address`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.chain.recorded_name_and_ticker_collisions_at_different_contract_addresses_with_available_holder_counts_and_beacon_checks(
    chain_id=1,
    symbol="TSLA",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chain_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**symbol:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Rows per page (default 300)
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Rows to skip before the page (default 0)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Status
<details><summary><code>client.status.<a href="src/fern/status/client.py">whether_the_registry_is_live_the_daemons_heartbeat_every_job_against_its_cadence_the_scanners_still_reading_history_and_the_age_of_every_published_figure</a>(...) -> GetChainsChainIdStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Public. Always 200; the verdict is in the body ('live', 'degraded', 'stale', 'never'), so a stale registry is a fact to read rather than an error to retry. Each job carries its cadence, last successful run, age and verdict ('fresh', 'late', 'failing', 'filling', 'stalled', 'never'); metadataBacklog reports the measured due, visible, never-read and failed token counts after the last successful metadata batch; filling does not mean complete coverage; each figure names the job that writes it and the newest timestamp behind it. Also served at /api/v1/status.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.status.whether_the_registry_is_live_the_daemons_heartbeat_every_job_against_its_cadence_the_scanners_still_reading_history_and_the_age_of_every_published_figure(
    chain_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chain_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.status.<a href="src/fern/status/client.py">alias_of_chains4663status_whether_the_registry_is_live</a>() -> GetStatusResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.status.alias_of_chains4663status_whether_the_registry_is_live()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Changelog
<details><summary><code>client.changelog.<a href="src/fern/changelog/client.py">the_registry_changelog_every_pause_block_upgrade_multiplier_change_stale_feed_supply_residual_listing_corporate_action_and_chain_status_change_the_daemon_recorded</a>(...) -> GetChainsChainIdEventsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Public. Without `since`/`cursor`: newest first, with `kinds` (every kind the daemon can emit) and `nextCursor`. With `since` or `cursor` (an ISO instant, use the previous `nextCursor`): only newer rows, oldest first, so a consumer catches up without gaps; a `since` or `cursor` that does not parse is a 400, never a silent restart from now. `kind` matches exactly or by prefix (`registry.`, `multiplier.`) and `symbol` narrows to one token, on the newest-first read only: the cursor read returns every kind, and a consumer following a cursor filters on `kind` itself. `limit` up to 500. When the changelog is empty, `nextCursor` is the epoch, which passed back yields every event from the first.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.changelog.the_registry_changelog_every_pause_block_upgrade_multiplier_change_stale_feed_supply_residual_listing_corporate_action_and_chain_status_change_the_daemon_recorded(
    chain_id=1,
    kind="multiplier.",
    symbol="TSLA",
    cursor="2026-09-05T11:50:43.476Z|ev_9f3256ce83b6dd98fedbe4ec",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chain_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**kind:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**symbol:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — An opaque position, `${observedAt}|${id}`, as returned in `nextCursor`. Pass it back verbatim; a bare ISO instant is also accepted.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — A malformed value reads as the default, a larger one as the maximum
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.changelog.<a href="src/fern/changelog/client.py">the_same_changelog_as_server_sent_events_each_frames_id_is_the_events_cursor_observed_at_id_so_last_event_id_or_since_resumes_without_gaps</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.changelog.the_same_changelog_as_server_sent_events_each_frames_id_is_the_events_cursor_observed_at_id_so_last_event_id_or_since_resumes_without_gaps(
    chain_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**chain_id:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[str]` — An ISO instant or a cursor `${observedAt}|${id}`; the Last-Event-ID header takes precedence. Without either the stream starts at now.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Watch
<details><summary><code>client.watch.<a href="src/fern/watch/client.py">list_this_accounts_watchers</a>() -> GetWatchersResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.watch.list_this_accounts_watchers()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.watch.<a href="src/fern/watch/client.py">create_a_watcher</a>(...) -> PostWatchersResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.watch.create_a_watcher()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — Repeat a POST with the same key to get the same watcher back instead of creating another.
    
</dd>
</dl>

<dl>
<dd>

**asset_id:** `typing.Optional[str]` — Required for large_transfer, wallet_activity and token_event; omitted for registry_event.
    
</dd>
</dl>

<dl>
<dd>

**threshold:** `typing.Optional[str]` — Required for large_transfer (positive) and wallet_activity ("0" means every transfer); ignored by registry_event, token_event and new_pool.
    
</dd>
</dl>

<dl>
<dd>

**kind:** `typing.Optional[PostWatchersRequestKind]` 
    
</dd>
</dl>

<dl>
<dd>

**lookalikes_only:** `typing.Optional[bool]` — new_pool only: alert only on a pool whose token borrows a listed ticker or name. Off by default.
    
</dd>
</dl>

<dl>
<dd>

**wallet:** `typing.Optional[str]` — Required when kind is wallet_activity — a 0x-prefixed 40-character hex address.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**webhook_id:** `typing.Optional[str]` — Deliver this watcher to a registered webhook endpoint instead of Telegram.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.watch.<a href="src/fern/watch/client.py">get_one_watcher</a>(...) -> GetWatchersIdResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.watch.get_one_watcher(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.watch.<a href="src/fern/watch/client.py">delete_a_watcher</a>(...) -> DeleteWatchersIdResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.watch.delete_a_watcher(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.watch.<a href="src/fern/watch/client.py">pause_resume_or_re_point_a_watcher</a>(...) -> PatchWatchersIdResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.watch.pause_resume_or_re_point_a_watcher(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**webhook_id:** `typing.Optional[str]` — Re-point this watcher: an endpoint id delivers there, null goes back to Telegram. The endpoint must be yours and enabled.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.watch.<a href="src/fern/watch/client.py">a_watchers_delivery_history</a>(...) -> GetWatchersIdRunsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.watch.a_watchers_delivery_history(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.watch.<a href="src/fern/watch/client.py">list_this_accounts_webhook_endpoints</a>() -> GetWebhooksResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.watch.list_this_accounts_webhook_endpoints()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.watch.<a href="src/fern/watch/client.py">register_a_webhook_endpoint</a>(...) -> PostWebhooksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the signing secret once. Every delivery carries X-Fletch-Signature: t=<unix>,v1=<hex hmac-sha256 over "<t>.<body>"> and X-Fletch-Event.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.watch.register_a_webhook_endpoint(
    url="https://example.com/fletch",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**url:** `str` — An https:// URL on a public host.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Defaults to the URL's host.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.watch.<a href="src/fern/watch/client.py">delete_an_endpoint</a>(...) -> DeleteWebhooksIdResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Watchers delivering to it are paused; the response says how many.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.watch.delete_an_endpoint(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.watch.<a href="src/fern/watch/client.py">enable_disable_or_rotate_the_secret_of_an_endpoint</a>(...) -> PatchWebhooksIdResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.watch.enable_disable_or_rotate_the_secret_of_an_endpoint(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**rotate_secret:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.watch.<a href="src/fern/watch/client.py">send_a_signed_ping_to_an_endpoint_now</a>(...) -> PostWebhooksIdTestResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Always HTTP 200: the endpoint's own answer is in the body as ok, status and error. Sent directly rather than through the delivery outbox, so a failure is not retried.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.watch.send_a_signed_ping_to_an_endpoint_now(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Build
<details><summary><code>client.build.<a href="src/fern/build/client.py">list_this_accounts_projects</a>() -> GetProjectsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.build.list_this_accounts_projects()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.build.<a href="src/fern/build/client.py">get_one_builds_status_contracts_and_toolchain_report</a>(...) -> GetBuildsIdResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.DEFAULT,
)

client.build.get_one_builds_status_contracts_and_toolchain_report(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

