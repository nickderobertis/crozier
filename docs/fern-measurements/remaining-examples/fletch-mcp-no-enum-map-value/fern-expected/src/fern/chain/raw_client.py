

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.not_found_error import NotFoundError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..types.not_found_error_body import NotFoundErrorBody
from ..types.too_many_requests_error_body import TooManyRequestsErrorBody
from .types.get_chains_chain_id_bridge_response import GetChainsChainIdBridgeResponse
from .types.get_chains_chain_id_control_plane_response import GetChainsChainIdControlPlaneResponse
from .types.get_chains_chain_id_corporate_actions_response import GetChainsChainIdCorporateActionsResponse
from .types.get_chains_chain_id_dex_response import GetChainsChainIdDexResponse
from .types.get_chains_chain_id_health_response import GetChainsChainIdHealthResponse
from .types.get_chains_chain_id_issuer_request_kind import GetChainsChainIdIssuerRequestKind
from .types.get_chains_chain_id_issuer_response import GetChainsChainIdIssuerResponse
from .types.get_chains_chain_id_lookalikes_response import GetChainsChainIdLookalikesResponse
from pydantic import ValidationError


class RawChainClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def the_issuers_access_controls_registry_paused_implementation_blocked_address_count_and_its_latest_events(
        self,
        chain_id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetChainsChainIdControlPlaneResponse]:
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
        HttpResponse[GetChainsChainIdControlPlaneResponse]
            Registry state and events
        """
        _response = self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/control-plane",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsChainIdControlPlaneResponse,
                    parse_obj_as(
                        type_=GetChainsChainIdControlPlaneResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def the_chains_latest_vital_signs_head_block_time_base_fee_l1block_batch_count_delayed_messages_batch_poster_balance_status_page(
        self, chain_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetChainsChainIdHealthResponse]:
        """
        Parameters
        ----------
        chain_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetChainsChainIdHealthResponse]
            Latest reading
        """
        _response = self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/health",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsChainIdHealthResponse,
                    parse_obj_as(
                        type_=GetChainsChainIdHealthResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def corporate_actions_in_progress_as_robinhood_publishes_them_tied_to_the_token_each_affects(
        self, chain_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetChainsChainIdCorporateActionsResponse]:
        """
        Parameters
        ----------
        chain_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetChainsChainIdCorporateActionsResponse]
            Actions in progress
        """
        _response = self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/corporate-actions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsChainIdCorporateActionsResponse,
                    parse_obj_as(
                        type_=GetChainsChainIdCorporateActionsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def the_dex_venues_the_registry_reads_and_what_each_contributes_pools_trading_a_listed_asset_how_many_carry_a_dollar_price_the_last_days_swaps_and_volume_and_how_many_assets_take_their_premium_from_a_pool_there(
        self, chain_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetChainsChainIdDexResponse]:
        """
        Public. One row per venue read (`uniswap_v4`, `uniswap_v3`), whether or not it has a pool on record yet, so `venues` and `discovery` name the same set. `assetsPricedHere` counts the assets whose deepest pool in dollars sits on that venue, so the venues' figures add up to the assets with a DEX price. `depthUsd` sums depth over the venue's priced pools: observed quote-side holdings for v3, and a bounded quote estimate for a 1% price move for v4 where per-pool token reserves are unavailable; Uniswap's raw liquidity L compares two pools only when they hold the same pair. `swaps24h` counts swap logs and `transactions24h` counts distinct transactions in (metricsAsOf - 24 hours, metricsAsOf], using each event block timestamp. Values are null until the entire window is indexed and when its end is more than 120 seconds old. `volumeUsd24h` uses the indexed quote leg. USDG is nominally denominated at 1 USDG = $1; WETH uses a recorded historical oracle estimate with at most one-hour archive sample age and an oracle answer within its published heartbeat. `volumeValuation` retains the method and coverage reason. Zero means a completely scanned window with no matching activity. `checkedAt` is when the state read last priced a pool on that venue; `headAt` inside `discovery` is when the chain head there was read. `discovery` carries each venue's pool scan position against that head; while `readingHistory` is true the counts are a floor, not a total, and while `scanned` is false the venue has not been read at all. The Pons launchpad creates its pools on the Uniswap v3 factory, so they are counted as `uniswap_v3` rather than as a venue of their own.

        Parameters
        ----------
        chain_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetChainsChainIdDexResponse]
            DEX venues
        """
        _response = self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/dex",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsChainIdDexResponse,
                    parse_obj_as(
                        type_=GetChainsChainIdDexResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def the_token_bridge_each_bridged_assets_l1escrow_against_its_l2supply_recent_deposits_and_withdrawals_seen_on_l2and_withdrawals_past_their_seven_day_window(
        self,
        chain_id: int,
        *,
        symbol: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetChainsChainIdBridgeResponse]:
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
        HttpResponse[GetChainsChainIdBridgeResponse]
            Bridge
        """
        _response = self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/bridge",
            method="GET",
            params={
                "symbol": symbol,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsChainIdBridgeResponse,
                    parse_obj_as(
                        type_=GetChainsChainIdBridgeResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def the_issuers_paperwork_every_pdf_the_legal_hub_lists_with_e_tag_last_modified_and_the_token_it_maps_to_plus_watched_pages_and_when_their_text_changed(
        self,
        chain_id: int,
        *,
        kind: typing.Optional[GetChainsChainIdIssuerRequestKind] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetChainsChainIdIssuerResponse]:
        """
        Parameters
        ----------
        chain_id : int

        kind : typing.Optional[GetChainsChainIdIssuerRequestKind]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetChainsChainIdIssuerResponse]
            Documents and pages
        """
        _response = self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/issuer",
            method="GET",
            params={
                "kind": kind,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsChainIdIssuerResponse,
                    parse_obj_as(
                        type_=GetChainsChainIdIssuerResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def recorded_name_and_ticker_collisions_at_different_contract_addresses_with_available_holder_counts_and_beacon_checks(
        self,
        chain_id: int,
        *,
        symbol: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetChainsChainIdLookalikesResponse]:
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
        HttpResponse[GetChainsChainIdLookalikesResponse]
            Lookalikes, most held first
        """
        _response = self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/lookalikes",
            method="GET",
            params={
                "symbol": symbol,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsChainIdLookalikesResponse,
                    parse_obj_as(
                        type_=GetChainsChainIdLookalikesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawChainClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def the_issuers_access_controls_registry_paused_implementation_blocked_address_count_and_its_latest_events(
        self,
        chain_id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetChainsChainIdControlPlaneResponse]:
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
        AsyncHttpResponse[GetChainsChainIdControlPlaneResponse]
            Registry state and events
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/control-plane",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsChainIdControlPlaneResponse,
                    parse_obj_as(
                        type_=GetChainsChainIdControlPlaneResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def the_chains_latest_vital_signs_head_block_time_base_fee_l1block_batch_count_delayed_messages_batch_poster_balance_status_page(
        self, chain_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetChainsChainIdHealthResponse]:
        """
        Parameters
        ----------
        chain_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetChainsChainIdHealthResponse]
            Latest reading
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/health",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsChainIdHealthResponse,
                    parse_obj_as(
                        type_=GetChainsChainIdHealthResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def corporate_actions_in_progress_as_robinhood_publishes_them_tied_to_the_token_each_affects(
        self, chain_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetChainsChainIdCorporateActionsResponse]:
        """
        Parameters
        ----------
        chain_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetChainsChainIdCorporateActionsResponse]
            Actions in progress
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/corporate-actions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsChainIdCorporateActionsResponse,
                    parse_obj_as(
                        type_=GetChainsChainIdCorporateActionsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def the_dex_venues_the_registry_reads_and_what_each_contributes_pools_trading_a_listed_asset_how_many_carry_a_dollar_price_the_last_days_swaps_and_volume_and_how_many_assets_take_their_premium_from_a_pool_there(
        self, chain_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetChainsChainIdDexResponse]:
        """
        Public. One row per venue read (`uniswap_v4`, `uniswap_v3`), whether or not it has a pool on record yet, so `venues` and `discovery` name the same set. `assetsPricedHere` counts the assets whose deepest pool in dollars sits on that venue, so the venues' figures add up to the assets with a DEX price. `depthUsd` sums depth over the venue's priced pools: observed quote-side holdings for v3, and a bounded quote estimate for a 1% price move for v4 where per-pool token reserves are unavailable; Uniswap's raw liquidity L compares two pools only when they hold the same pair. `swaps24h` counts swap logs and `transactions24h` counts distinct transactions in (metricsAsOf - 24 hours, metricsAsOf], using each event block timestamp. Values are null until the entire window is indexed and when its end is more than 120 seconds old. `volumeUsd24h` uses the indexed quote leg. USDG is nominally denominated at 1 USDG = $1; WETH uses a recorded historical oracle estimate with at most one-hour archive sample age and an oracle answer within its published heartbeat. `volumeValuation` retains the method and coverage reason. Zero means a completely scanned window with no matching activity. `checkedAt` is when the state read last priced a pool on that venue; `headAt` inside `discovery` is when the chain head there was read. `discovery` carries each venue's pool scan position against that head; while `readingHistory` is true the counts are a floor, not a total, and while `scanned` is false the venue has not been read at all. The Pons launchpad creates its pools on the Uniswap v3 factory, so they are counted as `uniswap_v3` rather than as a venue of their own.

        Parameters
        ----------
        chain_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetChainsChainIdDexResponse]
            DEX venues
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/dex",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsChainIdDexResponse,
                    parse_obj_as(
                        type_=GetChainsChainIdDexResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def the_token_bridge_each_bridged_assets_l1escrow_against_its_l2supply_recent_deposits_and_withdrawals_seen_on_l2and_withdrawals_past_their_seven_day_window(
        self,
        chain_id: int,
        *,
        symbol: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetChainsChainIdBridgeResponse]:
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
        AsyncHttpResponse[GetChainsChainIdBridgeResponse]
            Bridge
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/bridge",
            method="GET",
            params={
                "symbol": symbol,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsChainIdBridgeResponse,
                    parse_obj_as(
                        type_=GetChainsChainIdBridgeResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def the_issuers_paperwork_every_pdf_the_legal_hub_lists_with_e_tag_last_modified_and_the_token_it_maps_to_plus_watched_pages_and_when_their_text_changed(
        self,
        chain_id: int,
        *,
        kind: typing.Optional[GetChainsChainIdIssuerRequestKind] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetChainsChainIdIssuerResponse]:
        """
        Parameters
        ----------
        chain_id : int

        kind : typing.Optional[GetChainsChainIdIssuerRequestKind]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetChainsChainIdIssuerResponse]
            Documents and pages
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/issuer",
            method="GET",
            params={
                "kind": kind,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsChainIdIssuerResponse,
                    parse_obj_as(
                        type_=GetChainsChainIdIssuerResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def recorded_name_and_ticker_collisions_at_different_contract_addresses_with_available_holder_counts_and_beacon_checks(
        self,
        chain_id: int,
        *,
        symbol: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetChainsChainIdLookalikesResponse]:
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
        AsyncHttpResponse[GetChainsChainIdLookalikesResponse]
            Lookalikes, most held first
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/lookalikes",
            method="GET",
            params={
                "symbol": symbol,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsChainIdLookalikesResponse,
                    parse_obj_as(
                        type_=GetChainsChainIdLookalikesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        TooManyRequestsErrorBody,
                        parse_obj_as(
                            type_=TooManyRequestsErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
