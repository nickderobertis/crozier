

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawChainClient, RawChainClient
from .types.get_chains_chain_id_bridge_response import GetChainsChainIdBridgeResponse
from .types.get_chains_chain_id_control_plane_response import GetChainsChainIdControlPlaneResponse
from .types.get_chains_chain_id_corporate_actions_response import GetChainsChainIdCorporateActionsResponse
from .types.get_chains_chain_id_dex_response import GetChainsChainIdDexResponse
from .types.get_chains_chain_id_health_response import GetChainsChainIdHealthResponse
from .types.get_chains_chain_id_issuer_request_kind import GetChainsChainIdIssuerRequestKind
from .types.get_chains_chain_id_issuer_response import GetChainsChainIdIssuerResponse
from .types.get_chains_chain_id_lookalikes_response import GetChainsChainIdLookalikesResponse


class ChainClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawChainClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawChainClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawChainClient
        """
        return self._raw_client

    def the_issuers_access_controls_registry_paused_implementation_blocked_address_count_and_its_latest_events(
        self,
        chain_id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetChainsChainIdControlPlaneResponse:
        """
        Public. One contract governs every Stock Token: this is the surface no other index publishes. `limit` caps events (default 50, max 200), newest first. `offset` skips that many events, so `offset=200&limit=200` is the second page; an event that lands between two page reads repeats one row on the next page, so a consumer copying the log dedupes by `txHash` and `logIndex`. A page shorter than `limit` is the last one. `state` is the same on every page.

        Parameters
        ----------
        chain_id : int

        limit : typing.Optional[int]
            Events per page (default 50)

        offset : typing.Optional[int]
            Events to skip before the page (default 0)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetChainsChainIdControlPlaneResponse
            Registry state and events

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.chain.the_issuers_access_controls_registry_paused_implementation_blocked_address_count_and_its_latest_events(
            chain_id=1,
        )
        """
        _response = self._raw_client.the_issuers_access_controls_registry_paused_implementation_blocked_address_count_and_its_latest_events(
            chain_id, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    def the_chains_latest_vital_signs_head_block_time_base_fee_l1block_batch_count_delayed_messages_batch_poster_balance_status_page(
        self, chain_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetChainsChainIdHealthResponse:
        """
        Parameters
        ----------
        chain_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetChainsChainIdHealthResponse
            Latest reading

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.chain.the_chains_latest_vital_signs_head_block_time_base_fee_l1block_batch_count_delayed_messages_batch_poster_balance_status_page(
            chain_id=1,
        )
        """
        _response = self._raw_client.the_chains_latest_vital_signs_head_block_time_base_fee_l1block_batch_count_delayed_messages_batch_poster_balance_status_page(
            chain_id, request_options=request_options
        )
        return _response.data

    def corporate_actions_in_progress_as_robinhood_publishes_them_tied_to_the_token_each_affects(
        self, chain_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetChainsChainIdCorporateActionsResponse:
        """
        Parameters
        ----------
        chain_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetChainsChainIdCorporateActionsResponse
            Actions in progress

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.chain.corporate_actions_in_progress_as_robinhood_publishes_them_tied_to_the_token_each_affects(
            chain_id=1,
        )
        """
        _response = (
            self._raw_client.corporate_actions_in_progress_as_robinhood_publishes_them_tied_to_the_token_each_affects(
                chain_id, request_options=request_options
            )
        )
        return _response.data

    def the_dex_venues_the_registry_reads_and_what_each_contributes_pools_trading_a_listed_asset_how_many_carry_a_dollar_price_the_last_days_swaps_and_volume_and_how_many_assets_take_their_premium_from_a_pool_there(
        self, chain_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetChainsChainIdDexResponse:
        """
        Public. One row per venue read (`uniswap_v4`, `uniswap_v3`), whether or not it has a pool on record yet, so `venues` and `discovery` name the same set. `assetsPricedHere` counts the assets whose deepest pool in dollars sits on that venue, so the venues' figures add up to the assets with a DEX price. `depthUsd` sums depth over the venue's priced pools: observed quote-side holdings for v3, and a bounded quote estimate for a 1% price move for v4 where per-pool token reserves are unavailable; Uniswap's raw liquidity L compares two pools only when they hold the same pair. `swaps24h` counts swap logs and `transactions24h` counts distinct transactions in (metricsAsOf - 24 hours, metricsAsOf], using each event block timestamp. Values are null until the entire window is indexed and when its end is more than 120 seconds old. `volumeUsd24h` uses the indexed quote leg. USDG is nominally denominated at 1 USDG = $1; WETH uses a recorded historical oracle estimate with at most one-hour archive sample age and an oracle answer within its published heartbeat. `volumeValuation` retains the method and coverage reason. Zero means a completely scanned window with no matching activity. `checkedAt` is when the state read last priced a pool on that venue; `headAt` inside `discovery` is when the chain head there was read. `discovery` carries each venue's pool scan position against that head; while `readingHistory` is true the counts are a floor, not a total, and while `scanned` is false the venue has not been read at all. The Pons launchpad creates its pools on the Uniswap v3 factory, so they are counted as `uniswap_v3` rather than as a venue of their own.

        Parameters
        ----------
        chain_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetChainsChainIdDexResponse
            DEX venues

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.chain.the_dex_venues_the_registry_reads_and_what_each_contributes_pools_trading_a_listed_asset_how_many_carry_a_dollar_price_the_last_days_swaps_and_volume_and_how_many_assets_take_their_premium_from_a_pool_there(
            chain_id=1,
        )
        """
        _response = self._raw_client.the_dex_venues_the_registry_reads_and_what_each_contributes_pools_trading_a_listed_asset_how_many_carry_a_dollar_price_the_last_days_swaps_and_volume_and_how_many_assets_take_their_premium_from_a_pool_there(
            chain_id, request_options=request_options
        )
        return _response.data

    def the_token_bridge_each_bridged_assets_l1escrow_against_its_l2supply_recent_deposits_and_withdrawals_seen_on_l2and_withdrawals_past_their_seven_day_window(
        self,
        chain_id: int,
        *,
        symbol: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetChainsChainIdBridgeResponse:
        """
        Parameters
        ----------
        chain_id : int

        symbol : typing.Optional[str]

        limit : typing.Optional[int]
            Flows, newest first; a malformed value reads as the default, a larger one as the maximum

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetChainsChainIdBridgeResponse
            Bridge

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.chain.the_token_bridge_each_bridged_assets_l1escrow_against_its_l2supply_recent_deposits_and_withdrawals_seen_on_l2and_withdrawals_past_their_seven_day_window(
            chain_id=1,
            symbol="WBTC",
        )
        """
        _response = self._raw_client.the_token_bridge_each_bridged_assets_l1escrow_against_its_l2supply_recent_deposits_and_withdrawals_seen_on_l2and_withdrawals_past_their_seven_day_window(
            chain_id, symbol=symbol, limit=limit, request_options=request_options
        )
        return _response.data

    def the_issuers_paperwork_every_pdf_the_legal_hub_lists_with_e_tag_last_modified_and_the_token_it_maps_to_plus_watched_pages_and_when_their_text_changed(
        self,
        chain_id: int,
        *,
        kind: typing.Optional[GetChainsChainIdIssuerRequestKind] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetChainsChainIdIssuerResponse:
        """
        Parameters
        ----------
        chain_id : int

        kind : typing.Optional[GetChainsChainIdIssuerRequestKind]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetChainsChainIdIssuerResponse
            Documents and pages

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.chain.the_issuers_paperwork_every_pdf_the_legal_hub_lists_with_e_tag_last_modified_and_the_token_it_maps_to_plus_watched_pages_and_when_their_text_changed(
            chain_id=1,
        )
        """
        _response = self._raw_client.the_issuers_paperwork_every_pdf_the_legal_hub_lists_with_e_tag_last_modified_and_the_token_it_maps_to_plus_watched_pages_and_when_their_text_changed(
            chain_id, kind=kind, request_options=request_options
        )
        return _response.data

    def recorded_name_and_ticker_collisions_at_different_contract_addresses_with_available_holder_counts_and_beacon_checks(
        self,
        chain_id: int,
        *,
        symbol: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetChainsChainIdLookalikesResponse:
        """
        Public. Most held first. A collision describes reused labels; it does not establish intent or issuer identity. `limit` caps rows (default 300, max 1000); `offset` skips that many rows, so `offset=1000&limit=1000` is the second page, and a page shorter than `limit` is the last one. Holder counts are refreshed by the lookalike scan, so the order can shift between pages read across a scan: a consumer copying the whole table dedupes by `address`.

        Parameters
        ----------
        chain_id : int

        symbol : typing.Optional[str]

        limit : typing.Optional[int]
            Rows per page (default 300)

        offset : typing.Optional[int]
            Rows to skip before the page (default 0)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetChainsChainIdLookalikesResponse
            Lookalikes, most held first

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.chain.recorded_name_and_ticker_collisions_at_different_contract_addresses_with_available_holder_counts_and_beacon_checks(
            chain_id=1,
            symbol="TSLA",
        )
        """
        _response = self._raw_client.recorded_name_and_ticker_collisions_at_different_contract_addresses_with_available_holder_counts_and_beacon_checks(
            chain_id, symbol=symbol, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data


class AsyncChainClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawChainClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawChainClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawChainClient
        """
        return self._raw_client

    async def the_issuers_access_controls_registry_paused_implementation_blocked_address_count_and_its_latest_events(
        self,
        chain_id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetChainsChainIdControlPlaneResponse:
        """
        Public. One contract governs every Stock Token: this is the surface no other index publishes. `limit` caps events (default 50, max 200), newest first. `offset` skips that many events, so `offset=200&limit=200` is the second page; an event that lands between two page reads repeats one row on the next page, so a consumer copying the log dedupes by `txHash` and `logIndex`. A page shorter than `limit` is the last one. `state` is the same on every page.

        Parameters
        ----------
        chain_id : int

        limit : typing.Optional[int]
            Events per page (default 50)

        offset : typing.Optional[int]
            Events to skip before the page (default 0)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetChainsChainIdControlPlaneResponse
            Registry state and events

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.chain.the_issuers_access_controls_registry_paused_implementation_blocked_address_count_and_its_latest_events(
                chain_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.the_issuers_access_controls_registry_paused_implementation_blocked_address_count_and_its_latest_events(
            chain_id, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def the_chains_latest_vital_signs_head_block_time_base_fee_l1block_batch_count_delayed_messages_batch_poster_balance_status_page(
        self, chain_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetChainsChainIdHealthResponse:
        """
        Parameters
        ----------
        chain_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetChainsChainIdHealthResponse
            Latest reading

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.chain.the_chains_latest_vital_signs_head_block_time_base_fee_l1block_batch_count_delayed_messages_batch_poster_balance_status_page(
                chain_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.the_chains_latest_vital_signs_head_block_time_base_fee_l1block_batch_count_delayed_messages_batch_poster_balance_status_page(
            chain_id, request_options=request_options
        )
        return _response.data

    async def corporate_actions_in_progress_as_robinhood_publishes_them_tied_to_the_token_each_affects(
        self, chain_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetChainsChainIdCorporateActionsResponse:
        """
        Parameters
        ----------
        chain_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetChainsChainIdCorporateActionsResponse
            Actions in progress

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.chain.corporate_actions_in_progress_as_robinhood_publishes_them_tied_to_the_token_each_affects(
                chain_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.corporate_actions_in_progress_as_robinhood_publishes_them_tied_to_the_token_each_affects(
            chain_id, request_options=request_options
        )
        return _response.data

    async def the_dex_venues_the_registry_reads_and_what_each_contributes_pools_trading_a_listed_asset_how_many_carry_a_dollar_price_the_last_days_swaps_and_volume_and_how_many_assets_take_their_premium_from_a_pool_there(
        self, chain_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetChainsChainIdDexResponse:
        """
        Public. One row per venue read (`uniswap_v4`, `uniswap_v3`), whether or not it has a pool on record yet, so `venues` and `discovery` name the same set. `assetsPricedHere` counts the assets whose deepest pool in dollars sits on that venue, so the venues' figures add up to the assets with a DEX price. `depthUsd` sums depth over the venue's priced pools: observed quote-side holdings for v3, and a bounded quote estimate for a 1% price move for v4 where per-pool token reserves are unavailable; Uniswap's raw liquidity L compares two pools only when they hold the same pair. `swaps24h` counts swap logs and `transactions24h` counts distinct transactions in (metricsAsOf - 24 hours, metricsAsOf], using each event block timestamp. Values are null until the entire window is indexed and when its end is more than 120 seconds old. `volumeUsd24h` uses the indexed quote leg. USDG is nominally denominated at 1 USDG = $1; WETH uses a recorded historical oracle estimate with at most one-hour archive sample age and an oracle answer within its published heartbeat. `volumeValuation` retains the method and coverage reason. Zero means a completely scanned window with no matching activity. `checkedAt` is when the state read last priced a pool on that venue; `headAt` inside `discovery` is when the chain head there was read. `discovery` carries each venue's pool scan position against that head; while `readingHistory` is true the counts are a floor, not a total, and while `scanned` is false the venue has not been read at all. The Pons launchpad creates its pools on the Uniswap v3 factory, so they are counted as `uniswap_v3` rather than as a venue of their own.

        Parameters
        ----------
        chain_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetChainsChainIdDexResponse
            DEX venues

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.chain.the_dex_venues_the_registry_reads_and_what_each_contributes_pools_trading_a_listed_asset_how_many_carry_a_dollar_price_the_last_days_swaps_and_volume_and_how_many_assets_take_their_premium_from_a_pool_there(
                chain_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.the_dex_venues_the_registry_reads_and_what_each_contributes_pools_trading_a_listed_asset_how_many_carry_a_dollar_price_the_last_days_swaps_and_volume_and_how_many_assets_take_their_premium_from_a_pool_there(
            chain_id, request_options=request_options
        )
        return _response.data

    async def the_token_bridge_each_bridged_assets_l1escrow_against_its_l2supply_recent_deposits_and_withdrawals_seen_on_l2and_withdrawals_past_their_seven_day_window(
        self,
        chain_id: int,
        *,
        symbol: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetChainsChainIdBridgeResponse:
        """
        Parameters
        ----------
        chain_id : int

        symbol : typing.Optional[str]

        limit : typing.Optional[int]
            Flows, newest first; a malformed value reads as the default, a larger one as the maximum

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetChainsChainIdBridgeResponse
            Bridge

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.chain.the_token_bridge_each_bridged_assets_l1escrow_against_its_l2supply_recent_deposits_and_withdrawals_seen_on_l2and_withdrawals_past_their_seven_day_window(
                chain_id=1,
                symbol="WBTC",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.the_token_bridge_each_bridged_assets_l1escrow_against_its_l2supply_recent_deposits_and_withdrawals_seen_on_l2and_withdrawals_past_their_seven_day_window(
            chain_id, symbol=symbol, limit=limit, request_options=request_options
        )
        return _response.data

    async def the_issuers_paperwork_every_pdf_the_legal_hub_lists_with_e_tag_last_modified_and_the_token_it_maps_to_plus_watched_pages_and_when_their_text_changed(
        self,
        chain_id: int,
        *,
        kind: typing.Optional[GetChainsChainIdIssuerRequestKind] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetChainsChainIdIssuerResponse:
        """
        Parameters
        ----------
        chain_id : int

        kind : typing.Optional[GetChainsChainIdIssuerRequestKind]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetChainsChainIdIssuerResponse
            Documents and pages

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.chain.the_issuers_paperwork_every_pdf_the_legal_hub_lists_with_e_tag_last_modified_and_the_token_it_maps_to_plus_watched_pages_and_when_their_text_changed(
                chain_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.the_issuers_paperwork_every_pdf_the_legal_hub_lists_with_e_tag_last_modified_and_the_token_it_maps_to_plus_watched_pages_and_when_their_text_changed(
            chain_id, kind=kind, request_options=request_options
        )
        return _response.data

    async def recorded_name_and_ticker_collisions_at_different_contract_addresses_with_available_holder_counts_and_beacon_checks(
        self,
        chain_id: int,
        *,
        symbol: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetChainsChainIdLookalikesResponse:
        """
        Public. Most held first. A collision describes reused labels; it does not establish intent or issuer identity. `limit` caps rows (default 300, max 1000); `offset` skips that many rows, so `offset=1000&limit=1000` is the second page, and a page shorter than `limit` is the last one. Holder counts are refreshed by the lookalike scan, so the order can shift between pages read across a scan: a consumer copying the whole table dedupes by `address`.

        Parameters
        ----------
        chain_id : int

        symbol : typing.Optional[str]

        limit : typing.Optional[int]
            Rows per page (default 300)

        offset : typing.Optional[int]
            Rows to skip before the page (default 0)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetChainsChainIdLookalikesResponse
            Lookalikes, most held first

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.chain.recorded_name_and_ticker_collisions_at_different_contract_addresses_with_available_holder_counts_and_beacon_checks(
                chain_id=1,
                symbol="TSLA",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.recorded_name_and_ticker_collisions_at_different_contract_addresses_with_available_holder_counts_and_beacon_checks(
            chain_id, symbol=symbol, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data
