

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawChainsClient, RawChainsClient
from .types.get_app_catalog_request_status import GetAppCatalogRequestStatus
from .types.get_app_catalog_response import GetAppCatalogResponse
from .types.get_chains_chain_id_dex_pools_request_kind import GetChainsChainIdDexPoolsRequestKind
from .types.get_chains_chain_id_dex_pools_request_sort import GetChainsChainIdDexPoolsRequestSort
from .types.get_chains_chain_id_dex_pools_request_tier import GetChainsChainIdDexPoolsRequestTier
from .types.get_chains_chain_id_dex_pools_request_venue import GetChainsChainIdDexPoolsRequestVenue
from .types.get_chains_chain_id_dex_pools_response import GetChainsChainIdDexPoolsResponse
from .types.get_chains_chain_id_markets_filters_response import GetChainsChainIdMarketsFiltersResponse
from .types.get_chains_chain_id_markets_request_activity import GetChainsChainIdMarketsRequestActivity
from .types.get_chains_chain_id_markets_request_data import GetChainsChainIdMarketsRequestData
from .types.get_chains_chain_id_markets_request_depth import GetChainsChainIdMarketsRequestDepth
from .types.get_chains_chain_id_markets_request_identity import GetChainsChainIdMarketsRequestIdentity
from .types.get_chains_chain_id_markets_request_kind import GetChainsChainIdMarketsRequestKind
from .types.get_chains_chain_id_markets_request_sort import GetChainsChainIdMarketsRequestSort
from .types.get_chains_chain_id_markets_request_trust import GetChainsChainIdMarketsRequestTrust
from .types.get_chains_chain_id_markets_response import GetChainsChainIdMarketsResponse
from .types.get_chains_response import GetChainsResponse
from .types.get_tokens_address_response import GetTokensAddressResponse


class ChainsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawChainsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawChainsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawChainsClient
        """
        return self._raw_client

    def list_robinhood_chain_networks(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetChainsResponse:
        """
        Public. The public RPC URL, the explorer and whether Fletch has a provider key for the chain; a configured provider URL is never returned.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetChainsResponse
            The two Robinhood chains

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.chains.list_robinhood_chain_networks()
        """
        _response = self._raw_client.list_robinhood_chain_networks(request_options=request_options)
        return _response.data

    def token_identity_and_current_market_observations_at_one_contract_address(
        self, address: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetTokensAddressResponse:
        """
        Public. The canonical trust verdict is shared by pages and pool responses. A lookalike records a normalized name or ticker collision; it does not establish intent. `reading` is the exact token-page observation: full address, economic selection reason, same-name alternatives, selected-pool volume, market cap and holders with source, timestamp and missing-value reason. Community dominance is an economic comparison. `market` retains the compact selected-pool view. V3 quote holdings and V4 bounded 1% quote input are separate measures. Volume sources distinguish nominal USDG quote units from WETH converted with a historical oracle estimate.

        Parameters
        ----------
        address : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTokensAddressResponse
            What this token is

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.chains.token_identity_and_current_market_observations_at_one_contract_address(
            address="0x0000000000000000000000000000000000000000",
        )
        """
        _response = self._raw_client.token_identity_and_current_market_observations_at_one_contract_address(
            address, request_options=request_options
        )
        return _response.data

    def get_app_catalog(
        self,
        chain_id: int,
        *,
        q: typing.Optional[str] = None,
        status: typing.Optional[GetAppCatalogRequestStatus] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetAppCatalogResponse:
        """
        Public. Includes symbols without a known on-chain contract. Display-only means a price feed without app trading. Inspect per-account tradability, stale and error. Symbols are ticker matches, not contract verification. Follow nextOffset until null. Pages read the current snapshot, which can change between requests. The observer targets 15 seconds; this endpoint reads its stored result.

        Parameters
        ----------
        chain_id : int

        q : typing.Optional[str]

        status : typing.Optional[GetAppCatalogRequestStatus]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAppCatalogResponse
            Recorded app catalog, with freshness and source errors

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.chains.get_app_catalog(
            chain_id=1,
        )
        """
        _response = self._raw_client.get_app_catalog(
            chain_id, q=q, status=status, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    def priority_tokens_one_contract_per_row_ordered_by_observed_selected_pool_volume(
        self,
        chain_id: int,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        kind: typing.Optional[GetChainsChainIdMarketsRequestKind] = None,
        trust: typing.Optional[GetChainsChainIdMarketsRequestTrust] = None,
        sort: typing.Optional[GetChainsChainIdMarketsRequestSort] = None,
        activity: typing.Optional[GetChainsChainIdMarketsRequestActivity] = None,
        data: typing.Optional[GetChainsChainIdMarketsRequestData] = None,
        depth: typing.Optional[GetChainsChainIdMarketsRequestDepth] = None,
        identity: typing.Optional[GetChainsChainIdMarketsRequestIdentity] = None,
        min_volume_usd: typing.Optional[float] = None,
        q: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetChainsChainIdMarketsResponse:
        """
        Public. Listed assets and selected major community contracts use the same token read model as token pages and /tokens/{address}. Each metric carries structured observation provenance, computation inputs, coverage, source/fetch times and expiry, alongside compatibility source/asOf/reason fields. Pool state expires after three minutes, changing supply and burn balances after five minutes, and selected-pool swap windows after two minutes. Capitalization expires with its earliest-expiring required input. Missing legacy provenance remains null. Selection time and its fifteen-minute policy expiry are explicit; stale selection withholds dominance. Volume covers the selected pool only. Missing volume sorts last with a stable name/address tie-break. Economic dominance never changes a trust verdict. The selected universe and same-name comparisons are bounded; registry history remains available through the pool and asset endpoints.

        Parameters
        ----------
        chain_id : int

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        kind : typing.Optional[GetChainsChainIdMarketsRequestKind]
            all: Issuer listings and priority community contracts. listed: Contracts in the issuer list, including pending checks. community: Priority contracts outside the issuer list. Check their trust badge.

        trust : typing.Optional[GetChainsChainIdMarketsRequestTrust]
            all: Keep every recorded identity verdict. verified: Issuer listing and matching contract checks. listed: Issuer listing with checks still incomplete. community: Resolved metadata with no recorded issuer-name collision. lookalike: Name or symbol collides with a verified asset. unknown: Identity calls have not resolved this contract.

        sort : typing.Optional[GetChainsChainIdMarketsRequestSort]
            volume: Selected-pool USD volume, highest first. swaps: Selected-pool swap events, highest first. market_cap: Outstanding supply estimate times current price, highest first. v3_depth: Observed quote-side holdings in dollars, highest first. v4_depth: Bounded quote input for a 1% move, highest first. name: Alphabetical name, then contract address.

        activity : typing.Optional[GetChainsChainIdMarketsRequestActivity]
            all: Include incomplete and unavailable swap windows. traded: At least one swap in a complete current 24-hour window. busy: At least 100 swaps in a complete current window. quiet: A complete current window with exactly zero swaps.

        data : typing.Optional[GetChainsChainIdMarketsRequestData]
            all: Keep unavailable measures with their reason. priced: Usable selected-pool price with pool state and quote conversion inside their three-minute freshness policy. volume: Valued 24-hour window counted through the last two minutes. complete: All three measures have usable current inputs.

        depth : typing.Optional[GetChainsChainIdMarketsRequestDepth]
            all: Keep both pool types and unavailable observations. v3_10k: At least $10,000 of current quote-side holdings. v3_100k: At least $100,000 of current quote-side holdings. v4_1k: At least $1,000 of bounded quote input for a 1% move. v4_10k: At least $10,000 of bounded quote input for a 1% move.

        identity : typing.Optional[GetChainsChainIdMarketsRequestIdentity]
            all: One row per recorded priority contract. dominant: Community contracts selected by the recorded economic comparison. same_name: Contracts with alternatives in the recorded comparison set. close_call: The dominance comparison recorded a close call.

        min_volume_usd : typing.Optional[float]
            Inclusive selected-pool USD volume threshold. Requires a complete current valued window.

        q : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetChainsChainIdMarketsResponse
            A page of token observations

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.chains.priority_tokens_one_contract_per_row_ordered_by_observed_selected_pool_volume(
            chain_id=1,
        )
        """
        _response = self._raw_client.priority_tokens_one_contract_per_row_ordered_by_observed_selected_pool_volume(
            chain_id,
            page=page,
            page_size=page_size,
            kind=kind,
            trust=trust,
            sort=sort,
            activity=activity,
            data=data,
            depth=depth,
            identity=identity,
            min_volume_usd=min_volume_usd,
            q=q,
            request_options=request_options,
        )
        return _response.data

    def discover_token_market_filters_labels_thresholds_and_useful_query_presets(
        self, chain_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetChainsChainIdMarketsFiltersResponse:
        """
        The catalog used by the token Markets page and query parser. Combine filters with AND. Activity requires a complete current selected-pool window. Numeric thresholds exclude unavailable data, including for a threshold of zero. V3 quote holdings and V4 bounded depth are separate filters and sorts.

        Parameters
        ----------
        chain_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetChainsChainIdMarketsFiltersResponse
            Machine-readable market filter catalog

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.chains.discover_token_market_filters_labels_thresholds_and_useful_query_presets(
            chain_id=1,
        )
        """
        _response = self._raw_client.discover_token_market_filters_labels_thresholds_and_useful_query_presets(
            chain_id, request_options=request_options
        )
        return _response.data

    def indexed_pools_with_token_identity_separate_depth_measures_and_current_swap_observations(
        self,
        chain_id: int,
        *,
        kind: typing.Optional[GetChainsChainIdDexPoolsRequestKind] = None,
        tier: typing.Optional[GetChainsChainIdDexPoolsRequestTier] = None,
        sort: typing.Optional[GetChainsChainIdDexPoolsRequestSort] = None,
        venue: typing.Optional[GetChainsChainIdDexPoolsRequestVenue] = None,
        q: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetChainsChainIdDexPoolsResponse:
        """
        Public. `kind=listed` filters membership in Robinhood's list; `kind=community` keeps unlisted priced tokens; `kind=lookalike` selects recorded collisions. The response `kind` is an alias of the canonical `trust` verdict; `listing` retains membership separately. `sort=volume` ranks actual current 24-hour volume, missing values last, with pool identity as the tie-break. `traction` explicitly adds depth and swap-count tie-breaks. Search accepts token names, tickers, full contracts, v3 pool addresses and v4 pool IDs. Swap and transaction counts require a complete current window. Volume sources distinguish nominal USDG denomination and historical WETH oracle estimates. V3 quote holdings and V4 bounded 1% quote input retain distinct labels and never form a combined TVL.

        Parameters
        ----------
        chain_id : int

        kind : typing.Optional[GetChainsChainIdDexPoolsRequestKind]
            Also accepted as `trust`.

        tier : typing.Optional[GetChainsChainIdDexPoolsRequestTier]
            Which tiers to list; the default is the pools worth watching.

        sort : typing.Optional[GetChainsChainIdDexPoolsRequestSort]

        venue : typing.Optional[GetChainsChainIdDexPoolsRequestVenue]

        q : typing.Optional[str]
            Token or pool name, symbol, or a complete 0x address. Addresses are matched in full.

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetChainsChainIdDexPoolsResponse
            A page of pools

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.chains.indexed_pools_with_token_identity_separate_depth_measures_and_current_swap_observations(
            chain_id=1,
            q="PIPE",
        )
        """
        _response = (
            self._raw_client.indexed_pools_with_token_identity_separate_depth_measures_and_current_swap_observations(
                chain_id,
                kind=kind,
                tier=tier,
                sort=sort,
                venue=venue,
                q=q,
                limit=limit,
                offset=offset,
                request_options=request_options,
            )
        )
        return _response.data


class AsyncChainsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawChainsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawChainsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawChainsClient
        """
        return self._raw_client

    async def list_robinhood_chain_networks(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetChainsResponse:
        """
        Public. The public RPC URL, the explorer and whether Fletch has a provider key for the chain; a configured provider URL is never returned.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetChainsResponse
            The two Robinhood chains

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.chains.list_robinhood_chain_networks()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_robinhood_chain_networks(request_options=request_options)
        return _response.data

    async def token_identity_and_current_market_observations_at_one_contract_address(
        self, address: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetTokensAddressResponse:
        """
        Public. The canonical trust verdict is shared by pages and pool responses. A lookalike records a normalized name or ticker collision; it does not establish intent. `reading` is the exact token-page observation: full address, economic selection reason, same-name alternatives, selected-pool volume, market cap and holders with source, timestamp and missing-value reason. Community dominance is an economic comparison. `market` retains the compact selected-pool view. V3 quote holdings and V4 bounded 1% quote input are separate measures. Volume sources distinguish nominal USDG quote units from WETH converted with a historical oracle estimate.

        Parameters
        ----------
        address : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTokensAddressResponse
            What this token is

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.chains.token_identity_and_current_market_observations_at_one_contract_address(
                address="0x0000000000000000000000000000000000000000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.token_identity_and_current_market_observations_at_one_contract_address(
            address, request_options=request_options
        )
        return _response.data

    async def get_app_catalog(
        self,
        chain_id: int,
        *,
        q: typing.Optional[str] = None,
        status: typing.Optional[GetAppCatalogRequestStatus] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetAppCatalogResponse:
        """
        Public. Includes symbols without a known on-chain contract. Display-only means a price feed without app trading. Inspect per-account tradability, stale and error. Symbols are ticker matches, not contract verification. Follow nextOffset until null. Pages read the current snapshot, which can change between requests. The observer targets 15 seconds; this endpoint reads its stored result.

        Parameters
        ----------
        chain_id : int

        q : typing.Optional[str]

        status : typing.Optional[GetAppCatalogRequestStatus]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAppCatalogResponse
            Recorded app catalog, with freshness and source errors

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.chains.get_app_catalog(
                chain_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_app_catalog(
            chain_id, q=q, status=status, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def priority_tokens_one_contract_per_row_ordered_by_observed_selected_pool_volume(
        self,
        chain_id: int,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        kind: typing.Optional[GetChainsChainIdMarketsRequestKind] = None,
        trust: typing.Optional[GetChainsChainIdMarketsRequestTrust] = None,
        sort: typing.Optional[GetChainsChainIdMarketsRequestSort] = None,
        activity: typing.Optional[GetChainsChainIdMarketsRequestActivity] = None,
        data: typing.Optional[GetChainsChainIdMarketsRequestData] = None,
        depth: typing.Optional[GetChainsChainIdMarketsRequestDepth] = None,
        identity: typing.Optional[GetChainsChainIdMarketsRequestIdentity] = None,
        min_volume_usd: typing.Optional[float] = None,
        q: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetChainsChainIdMarketsResponse:
        """
        Public. Listed assets and selected major community contracts use the same token read model as token pages and /tokens/{address}. Each metric carries structured observation provenance, computation inputs, coverage, source/fetch times and expiry, alongside compatibility source/asOf/reason fields. Pool state expires after three minutes, changing supply and burn balances after five minutes, and selected-pool swap windows after two minutes. Capitalization expires with its earliest-expiring required input. Missing legacy provenance remains null. Selection time and its fifteen-minute policy expiry are explicit; stale selection withholds dominance. Volume covers the selected pool only. Missing volume sorts last with a stable name/address tie-break. Economic dominance never changes a trust verdict. The selected universe and same-name comparisons are bounded; registry history remains available through the pool and asset endpoints.

        Parameters
        ----------
        chain_id : int

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        kind : typing.Optional[GetChainsChainIdMarketsRequestKind]
            all: Issuer listings and priority community contracts. listed: Contracts in the issuer list, including pending checks. community: Priority contracts outside the issuer list. Check their trust badge.

        trust : typing.Optional[GetChainsChainIdMarketsRequestTrust]
            all: Keep every recorded identity verdict. verified: Issuer listing and matching contract checks. listed: Issuer listing with checks still incomplete. community: Resolved metadata with no recorded issuer-name collision. lookalike: Name or symbol collides with a verified asset. unknown: Identity calls have not resolved this contract.

        sort : typing.Optional[GetChainsChainIdMarketsRequestSort]
            volume: Selected-pool USD volume, highest first. swaps: Selected-pool swap events, highest first. market_cap: Outstanding supply estimate times current price, highest first. v3_depth: Observed quote-side holdings in dollars, highest first. v4_depth: Bounded quote input for a 1% move, highest first. name: Alphabetical name, then contract address.

        activity : typing.Optional[GetChainsChainIdMarketsRequestActivity]
            all: Include incomplete and unavailable swap windows. traded: At least one swap in a complete current 24-hour window. busy: At least 100 swaps in a complete current window. quiet: A complete current window with exactly zero swaps.

        data : typing.Optional[GetChainsChainIdMarketsRequestData]
            all: Keep unavailable measures with their reason. priced: Usable selected-pool price with pool state and quote conversion inside their three-minute freshness policy. volume: Valued 24-hour window counted through the last two minutes. complete: All three measures have usable current inputs.

        depth : typing.Optional[GetChainsChainIdMarketsRequestDepth]
            all: Keep both pool types and unavailable observations. v3_10k: At least $10,000 of current quote-side holdings. v3_100k: At least $100,000 of current quote-side holdings. v4_1k: At least $1,000 of bounded quote input for a 1% move. v4_10k: At least $10,000 of bounded quote input for a 1% move.

        identity : typing.Optional[GetChainsChainIdMarketsRequestIdentity]
            all: One row per recorded priority contract. dominant: Community contracts selected by the recorded economic comparison. same_name: Contracts with alternatives in the recorded comparison set. close_call: The dominance comparison recorded a close call.

        min_volume_usd : typing.Optional[float]
            Inclusive selected-pool USD volume threshold. Requires a complete current valued window.

        q : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetChainsChainIdMarketsResponse
            A page of token observations

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.chains.priority_tokens_one_contract_per_row_ordered_by_observed_selected_pool_volume(
                chain_id=1,
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.priority_tokens_one_contract_per_row_ordered_by_observed_selected_pool_volume(
                chain_id,
                page=page,
                page_size=page_size,
                kind=kind,
                trust=trust,
                sort=sort,
                activity=activity,
                data=data,
                depth=depth,
                identity=identity,
                min_volume_usd=min_volume_usd,
                q=q,
                request_options=request_options,
            )
        )
        return _response.data

    async def discover_token_market_filters_labels_thresholds_and_useful_query_presets(
        self, chain_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetChainsChainIdMarketsFiltersResponse:
        """
        The catalog used by the token Markets page and query parser. Combine filters with AND. Activity requires a complete current selected-pool window. Numeric thresholds exclude unavailable data, including for a threshold of zero. V3 quote holdings and V4 bounded depth are separate filters and sorts.

        Parameters
        ----------
        chain_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetChainsChainIdMarketsFiltersResponse
            Machine-readable market filter catalog

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.chains.discover_token_market_filters_labels_thresholds_and_useful_query_presets(
                chain_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.discover_token_market_filters_labels_thresholds_and_useful_query_presets(
            chain_id, request_options=request_options
        )
        return _response.data

    async def indexed_pools_with_token_identity_separate_depth_measures_and_current_swap_observations(
        self,
        chain_id: int,
        *,
        kind: typing.Optional[GetChainsChainIdDexPoolsRequestKind] = None,
        tier: typing.Optional[GetChainsChainIdDexPoolsRequestTier] = None,
        sort: typing.Optional[GetChainsChainIdDexPoolsRequestSort] = None,
        venue: typing.Optional[GetChainsChainIdDexPoolsRequestVenue] = None,
        q: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetChainsChainIdDexPoolsResponse:
        """
        Public. `kind=listed` filters membership in Robinhood's list; `kind=community` keeps unlisted priced tokens; `kind=lookalike` selects recorded collisions. The response `kind` is an alias of the canonical `trust` verdict; `listing` retains membership separately. `sort=volume` ranks actual current 24-hour volume, missing values last, with pool identity as the tie-break. `traction` explicitly adds depth and swap-count tie-breaks. Search accepts token names, tickers, full contracts, v3 pool addresses and v4 pool IDs. Swap and transaction counts require a complete current window. Volume sources distinguish nominal USDG denomination and historical WETH oracle estimates. V3 quote holdings and V4 bounded 1% quote input retain distinct labels and never form a combined TVL.

        Parameters
        ----------
        chain_id : int

        kind : typing.Optional[GetChainsChainIdDexPoolsRequestKind]
            Also accepted as `trust`.

        tier : typing.Optional[GetChainsChainIdDexPoolsRequestTier]
            Which tiers to list; the default is the pools worth watching.

        sort : typing.Optional[GetChainsChainIdDexPoolsRequestSort]

        venue : typing.Optional[GetChainsChainIdDexPoolsRequestVenue]

        q : typing.Optional[str]
            Token or pool name, symbol, or a complete 0x address. Addresses are matched in full.

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetChainsChainIdDexPoolsResponse
            A page of pools

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.chains.indexed_pools_with_token_identity_separate_depth_measures_and_current_swap_observations(
                chain_id=1,
                q="PIPE",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.indexed_pools_with_token_identity_separate_depth_measures_and_current_swap_observations(
            chain_id,
            kind=kind,
            tier=tier,
            sort=sort,
            venue=venue,
            q=q,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data
