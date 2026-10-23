

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..types.bad_request_error_body import BadRequestErrorBody
from ..types.not_found_error_body import NotFoundErrorBody
from ..types.too_many_requests_error_body import TooManyRequestsErrorBody
from .types.get_chains_chain_id_assets_request_trust import GetChainsChainIdAssetsRequestTrust
from .types.get_chains_chain_id_assets_response import GetChainsChainIdAssetsResponse
from .types.get_chains_chain_id_assets_symbol_activity_response import GetChainsChainIdAssetsSymbolActivityResponse
from .types.get_chains_chain_id_assets_symbol_feed_rounds_response import GetChainsChainIdAssetsSymbolFeedRoundsResponse
from .types.get_chains_chain_id_assets_symbol_history_response import GetChainsChainIdAssetsSymbolHistoryResponse
from .types.get_chains_chain_id_assets_symbol_holders_response import GetChainsChainIdAssetsSymbolHoldersResponse
from .types.get_chains_chain_id_assets_symbol_pools_response import GetChainsChainIdAssetsSymbolPoolsResponse
from .types.get_chains_chain_id_assets_symbol_response import GetChainsChainIdAssetsSymbolResponse
from pydantic import ValidationError


class RawRegistryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def search_issuer_listed_assets_and_their_recorded_chain_observations(
        self,
        chain_id: int,
        *,
        trust: typing.Optional[GetChainsChainIdAssetsRequestTrust] = None,
        q: typing.Optional[str] = None,
        symbols: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetChainsChainIdAssetsResponse]:
        """
        Public. Anonymous callers get 120 requests a minute per address; a key or a session uses its own budget. Each asset carries `state`: multiplier, pending multiplier, pause flags, supply, recorded beacon dependency, the Chainlink feed and Robinhood's quote.

        Parameters
        ----------
        chain_id : int

        trust : typing.Optional[GetChainsChainIdAssetsRequestTrust]
            Filter the Robinhood listing collection by its shared trust verdict. Community tokens are resolved by /tokens/{address} and listed under /dex/pools; they are not added to Robinhood's registry.

        q : typing.Optional[str]
            Symbol or name substring

        symbols : typing.Optional[str]
            Comma-separated exact tickers, up to 200; any past that are ignored

        fields : typing.Optional[str]
            Extra per-asset blocks: lookalikes, corporateActions, multiplierHistory, feedRounds, concentration (up to 50 assets)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetChainsChainIdAssetsResponse]
            Assets, each with trust and state, plus any extra blocks fields= asked for
        """
        _response = self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/assets",
            method="GET",
            params={
                "trust": trust,
                "q": q,
                "symbols": symbols,
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsChainIdAssetsResponse,
                    parse_obj_as(
                        type_=GetChainsChainIdAssetsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    def get_one_registry_asset_by_symbol_with_its_state_multiplier_history_mints_and_burns_supply_snapshots_corporate_actions_and_control_plane_events(
        self, chain_id: int, symbol: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetChainsChainIdAssetsSymbolResponse]:
        """
        Public, rate-limited per address when anonymous. Raw amounts are strings (exact on chain); prices and multipliers are numbers.

        Parameters
        ----------
        chain_id : int

        symbol : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetChainsChainIdAssetsSymbolResponse]
            The asset with everything the registry knows about it
        """
        _response = self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/assets/{encode_path_param(symbol)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsChainIdAssetsSymbolResponse,
                    parse_obj_as(
                        type_=GetChainsChainIdAssetsSymbolResponse,
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

    def holders_largest_first_with_share_of_supply_and_what_each_address_is_holder_count_the_latest_concentration_reading_with_the_shares_that_say_where_the_supply_sits_and_whether_the_ledger_has_reached_the_chain_head(
        self,
        chain_id: int,
        symbol: str,
        *,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetChainsChainIdAssetsSymbolHoldersResponse]:
        """
        Public. `sits` is always one of `float`, `pools`, `issuer`, `bridge`, `contracts`, `unknown`, and names the concentration share this address's balance counts towards; `unknown` means the code probe has not checked this address yet. `label` and `labelKind` (`pool_manager`, `dex_pool`, `issuer`, `bridge_gateway`, `locker`, `contract`, `exchange`, `eoa`) are null for an address the registry has nothing to say about. `rawBalance` is in the token's base units; divide by 10^`decimals`. `sharePct` is that balance over `totalSupplyRaw`, read live, while the concentration shares are over the sum of every positive balance the ledger held at `concentration.asOfBlock`, so the two can differ slightly while the ledger trails the chain. `concentration` carries `top1Pct`, `top10Pct` and `gini` over every positive balance, and the six shares `floatPct`, `poolsPct`, `issuerPct`, `bridgePct`, `contractsPct` and `unknownPct`, which add to 100: float is the supply in ordinary wallets. `unknownPct` is the share held by addresses the code probe has not checked — it checks every holder above a ten-thousandth of a token's supply, so a tail of small holdings stays here permanently and `floatPct` is always a floor rather than a final answer. `issuerPct` is the share of every wallet labelled `issuer`, which is written only for Stock Tokens, whose mints are the issuer creating inventory; `issuerAddress` is this asset's largest mint recipient whatever the asset type. `concentration.day` is the UTC day of the reading, `takenAt` the ISO instant the job wrote it, and `asOfBlock` the ledger block it was computed at; the job runs every 24 h, so a share can be up to a day old. `concentration.holders` is the address count at that moment, while the top-level `holderCount` is read live and can differ. The shares come from the daily concentration job, which does not run while the transfer ledger is still reading history, so `concentration` is null until the ledger reaches head.

        Parameters
        ----------
        chain_id : int

        symbol : str

        limit : typing.Optional[int]
            How many holders, largest first

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetChainsChainIdAssetsSymbolHoldersResponse]
            Holders
        """
        _response = self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/assets/{encode_path_param(symbol)}/holders",
            method="GET",
            params={
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsChainIdAssetsSymbolHoldersResponse,
                    parse_obj_as(
                        type_=GetChainsChainIdAssetsSymbolHoldersResponse,
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

    def transfers_as_economics_one_row_per_utc_day_transfers_volume_mints_burns_dv_p_against_usdg_off_hours_transfers(
        self,
        chain_id: int,
        symbol: str,
        *,
        days: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetChainsChainIdAssetsSymbolActivityResponse]:
        """
        Parameters
        ----------
        chain_id : int

        symbol : str

        days : typing.Optional[int]
            How many UTC days back; a malformed value reads as the default

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetChainsChainIdAssetsSymbolActivityResponse]
            Days
        """
        _response = self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/assets/{encode_path_param(symbol)}/activity",
            method="GET",
            params={
                "days": days,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsChainIdAssetsSymbolActivityResponse,
                    parse_obj_as(
                        type_=GetChainsChainIdAssetsSymbolActivityResponse,
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

    def pools_trading_the_asset_on_every_dex_the_registry_reads_deepest_first_with_venue_price_liquidity_fee_hooks_last_day_swaps_and_volume_and_the_pool_behind_the_assets_premium_to_the_feed(
        self, chain_id: int, symbol: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetChainsChainIdAssetsSymbolPoolsResponse]:
        """
        Public. `venue` is `uniswap_v4` or `uniswap_v3`; a v4 pool is an id inside the one PoolManager and has a null `poolAddress`, a v3 pool is a contract and carries its address. A pool is recorded when one side is this asset and the other is a listed quote (USDG, WETH or another Stock Token). Pools are deepest first by `depthUsd`. V3 depth uses observed quote-side holdings. V4 depth uses a bounded quote estimate for a 1% price move, where per-pool token reserves are unavailable; `liquidity` is the pool's in-range Uniswap liquidity L in raw units, not a dollar figure, and is comparable only between pools of the same pair (its scale follows the two tokens' decimals). `best` is the deepest pool in dollars of any venue, which is the one the asset's premium to the Chainlink feed is measured from, and names its venue. `swaps24h` counts swap logs and `transactions24h` counts distinct transactions in (metricsAsOf - 24 hours, metricsAsOf], using each event block timestamp. Values are null until the entire window is indexed and when its end is more than 120 seconds old. `volumeUsd24h` uses the indexed quote leg. USDG is nominally denominated at 1 USDG = $1; WETH uses a recorded historical oracle estimate with at most one-hour archive sample age and an oracle answer within its published heartbeat. `volumeValuation` retains the method and coverage reason. Zero means a completely scanned window with no matching activity. `discovery` says how far each venue's pool scan has read: while `readingHistory` is true, a pool created in blocks the scan has not reached yet is not listed, and a venue whose `scanned` is false has not been read at all.

        Parameters
        ----------
        chain_id : int

        symbol : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetChainsChainIdAssetsSymbolPoolsResponse]
            Pools
        """
        _response = self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/assets/{encode_path_param(symbol)}/pools",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsChainIdAssetsSymbolPoolsResponse,
                    parse_obj_as(
                        type_=GetChainsChainIdAssetsSymbolPoolsResponse,
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

    def one_row_per_utc_day_of_everything_the_registry_publishes_about_an_asset_multiplier_pause_and_halt_flags_feed_price_and_staleness_bid_and_ask_divergence_dex_price_premium_and_liquidity_supply_holders_and_lookalike_count(
        self,
        chain_id: int,
        symbol: str,
        *,
        from_: typing.Optional[dt.date] = None,
        to: typing.Optional[dt.date] = None,
        days: typing.Optional[int] = None,
        at: typing.Optional[dt.date] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetChainsChainIdAssetsSymbolHistoryResponse]:
        """
        Public. Written by the state-daily job, which runs hourly and rewrites the current UTC day's row, so a past day can be read back; the live tables carry only the current answer. Each row is a single reading taken at `takenAt`, not a daily open, close, mean or end-of-day value: it is the last reading the job took on that day, and the row for the current day is rewritten on the job's next run, so today's row is a partial day. Compare `takenAt` across rows before treating the series as evenly spaced. `from`/`to` are UTC days and default to the last 90; `days` sets the window length instead of `from`; `at=YYYY-MM-DD` returns that one day (an empty `days` array when no snapshot was taken); `fields` narrows each row to the keys named, `day` always included. `coverage` says how many days are actually on record and the first of them: there is nothing before the day the job first ran. A null is a figure that was not read that day, never a zero: a figure is copied only when the job that writes it read it that day, and `stateCheckedAt`, `feedCheckedAt`, `apiCheckedAt`, `dexCheckedAt` and `blockscoutCheckedAt` say when each group of figures was last read. `ledgerHolders` is written only for assets whose transfer history the ledger had finished reading, and `lookalikes` only once the lookalike scan has completed a pass. Rows are flat versions of the live `state` block: `feedPrice`/`feedStale` are `state.feed.price`/`.stale`, `bid`/`ask`/`tradingHalt` are `state.quote.bid`/`.ask`/`.tradingHalt`, `dexPriceUsd`/`dexPremiumPct`/`dexLiquidity` are `state.dex.priceUsd`/`.premiumPct`/`.liquidity`, `blockscoutHolders` is `state.secondSource.holders`, `multiplier` is `state.multiplier`.

        Parameters
        ----------
        chain_id : int

        symbol : str

        from_ : typing.Optional[dt.date]
            First UTC day, YYYY-MM-DD; must not be after `to`

        to : typing.Optional[dt.date]
            Last UTC day, YYYY-MM-DD; defaults to today

        days : typing.Optional[int]
            Window length in days ending at `to`; ignored when `from` is given

        at : typing.Optional[dt.date]

        fields : typing.Optional[str]
            Comma-separated keys to keep from each row: multiplier, tokenPaused, oraclePaused, tradingHalt, feedPrice, feedStale, bid, ask, priceDivergencePct, dexPriceUsd, dexPremiumPct, dexLiquidity, totalSupplyRaw, blockscoutHolders, ledgerHolders, lookalikes, stateCheckedAt, feedCheckedAt, apiCheckedAt, dexCheckedAt, blockscoutCheckedAt, takenAt. `day` is always included; an unknown key is a 400.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetChainsChainIdAssetsSymbolHistoryResponse]
            History
        """
        _response = self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/assets/{encode_path_param(symbol)}/history",
            method="GET",
            params={
                "from": str(from_) if from_ is not None else None,
                "to": str(to) if to is not None else None,
                "days": days,
                "at": str(at) if at is not None else None,
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsChainIdAssetsSymbolHistoryResponse,
                    parse_obj_as(
                        type_=GetChainsChainIdAssetsSymbolHistoryResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    def the_chainlink_feeds_round_history_for_one_asset_newest_first_round_id_answer_price_multiplier_usd_started_at_updated_at(
        self,
        chain_id: int,
        symbol: str,
        *,
        since: typing.Optional[dt.datetime] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetChainsChainIdAssetsSymbolFeedRoundsResponse]:
        """
        Parameters
        ----------
        chain_id : int

        symbol : str

        since : typing.Optional[dt.datetime]

        limit : typing.Optional[int]
            Rounds, newest first; a malformed value reads as the default, a larger one as the maximum

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetChainsChainIdAssetsSymbolFeedRoundsResponse]
            Rounds
        """
        _response = self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/assets/{encode_path_param(symbol)}/feed/rounds",
            method="GET",
            params={
                "since": serialize_datetime(since) if since is not None else None,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsChainIdAssetsSymbolFeedRoundsResponse,
                    parse_obj_as(
                        type_=GetChainsChainIdAssetsSymbolFeedRoundsResponse,
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


class AsyncRawRegistryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def search_issuer_listed_assets_and_their_recorded_chain_observations(
        self,
        chain_id: int,
        *,
        trust: typing.Optional[GetChainsChainIdAssetsRequestTrust] = None,
        q: typing.Optional[str] = None,
        symbols: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetChainsChainIdAssetsResponse]:
        """
        Public. Anonymous callers get 120 requests a minute per address; a key or a session uses its own budget. Each asset carries `state`: multiplier, pending multiplier, pause flags, supply, recorded beacon dependency, the Chainlink feed and Robinhood's quote.

        Parameters
        ----------
        chain_id : int

        trust : typing.Optional[GetChainsChainIdAssetsRequestTrust]
            Filter the Robinhood listing collection by its shared trust verdict. Community tokens are resolved by /tokens/{address} and listed under /dex/pools; they are not added to Robinhood's registry.

        q : typing.Optional[str]
            Symbol or name substring

        symbols : typing.Optional[str]
            Comma-separated exact tickers, up to 200; any past that are ignored

        fields : typing.Optional[str]
            Extra per-asset blocks: lookalikes, corporateActions, multiplierHistory, feedRounds, concentration (up to 50 assets)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetChainsChainIdAssetsResponse]
            Assets, each with trust and state, plus any extra blocks fields= asked for
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/assets",
            method="GET",
            params={
                "trust": trust,
                "q": q,
                "symbols": symbols,
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsChainIdAssetsResponse,
                    parse_obj_as(
                        type_=GetChainsChainIdAssetsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    async def get_one_registry_asset_by_symbol_with_its_state_multiplier_history_mints_and_burns_supply_snapshots_corporate_actions_and_control_plane_events(
        self, chain_id: int, symbol: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetChainsChainIdAssetsSymbolResponse]:
        """
        Public, rate-limited per address when anonymous. Raw amounts are strings (exact on chain); prices and multipliers are numbers.

        Parameters
        ----------
        chain_id : int

        symbol : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetChainsChainIdAssetsSymbolResponse]
            The asset with everything the registry knows about it
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/assets/{encode_path_param(symbol)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsChainIdAssetsSymbolResponse,
                    parse_obj_as(
                        type_=GetChainsChainIdAssetsSymbolResponse,
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

    async def holders_largest_first_with_share_of_supply_and_what_each_address_is_holder_count_the_latest_concentration_reading_with_the_shares_that_say_where_the_supply_sits_and_whether_the_ledger_has_reached_the_chain_head(
        self,
        chain_id: int,
        symbol: str,
        *,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetChainsChainIdAssetsSymbolHoldersResponse]:
        """
        Public. `sits` is always one of `float`, `pools`, `issuer`, `bridge`, `contracts`, `unknown`, and names the concentration share this address's balance counts towards; `unknown` means the code probe has not checked this address yet. `label` and `labelKind` (`pool_manager`, `dex_pool`, `issuer`, `bridge_gateway`, `locker`, `contract`, `exchange`, `eoa`) are null for an address the registry has nothing to say about. `rawBalance` is in the token's base units; divide by 10^`decimals`. `sharePct` is that balance over `totalSupplyRaw`, read live, while the concentration shares are over the sum of every positive balance the ledger held at `concentration.asOfBlock`, so the two can differ slightly while the ledger trails the chain. `concentration` carries `top1Pct`, `top10Pct` and `gini` over every positive balance, and the six shares `floatPct`, `poolsPct`, `issuerPct`, `bridgePct`, `contractsPct` and `unknownPct`, which add to 100: float is the supply in ordinary wallets. `unknownPct` is the share held by addresses the code probe has not checked — it checks every holder above a ten-thousandth of a token's supply, so a tail of small holdings stays here permanently and `floatPct` is always a floor rather than a final answer. `issuerPct` is the share of every wallet labelled `issuer`, which is written only for Stock Tokens, whose mints are the issuer creating inventory; `issuerAddress` is this asset's largest mint recipient whatever the asset type. `concentration.day` is the UTC day of the reading, `takenAt` the ISO instant the job wrote it, and `asOfBlock` the ledger block it was computed at; the job runs every 24 h, so a share can be up to a day old. `concentration.holders` is the address count at that moment, while the top-level `holderCount` is read live and can differ. The shares come from the daily concentration job, which does not run while the transfer ledger is still reading history, so `concentration` is null until the ledger reaches head.

        Parameters
        ----------
        chain_id : int

        symbol : str

        limit : typing.Optional[int]
            How many holders, largest first

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetChainsChainIdAssetsSymbolHoldersResponse]
            Holders
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/assets/{encode_path_param(symbol)}/holders",
            method="GET",
            params={
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsChainIdAssetsSymbolHoldersResponse,
                    parse_obj_as(
                        type_=GetChainsChainIdAssetsSymbolHoldersResponse,
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

    async def transfers_as_economics_one_row_per_utc_day_transfers_volume_mints_burns_dv_p_against_usdg_off_hours_transfers(
        self,
        chain_id: int,
        symbol: str,
        *,
        days: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetChainsChainIdAssetsSymbolActivityResponse]:
        """
        Parameters
        ----------
        chain_id : int

        symbol : str

        days : typing.Optional[int]
            How many UTC days back; a malformed value reads as the default

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetChainsChainIdAssetsSymbolActivityResponse]
            Days
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/assets/{encode_path_param(symbol)}/activity",
            method="GET",
            params={
                "days": days,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsChainIdAssetsSymbolActivityResponse,
                    parse_obj_as(
                        type_=GetChainsChainIdAssetsSymbolActivityResponse,
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

    async def pools_trading_the_asset_on_every_dex_the_registry_reads_deepest_first_with_venue_price_liquidity_fee_hooks_last_day_swaps_and_volume_and_the_pool_behind_the_assets_premium_to_the_feed(
        self, chain_id: int, symbol: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetChainsChainIdAssetsSymbolPoolsResponse]:
        """
        Public. `venue` is `uniswap_v4` or `uniswap_v3`; a v4 pool is an id inside the one PoolManager and has a null `poolAddress`, a v3 pool is a contract and carries its address. A pool is recorded when one side is this asset and the other is a listed quote (USDG, WETH or another Stock Token). Pools are deepest first by `depthUsd`. V3 depth uses observed quote-side holdings. V4 depth uses a bounded quote estimate for a 1% price move, where per-pool token reserves are unavailable; `liquidity` is the pool's in-range Uniswap liquidity L in raw units, not a dollar figure, and is comparable only between pools of the same pair (its scale follows the two tokens' decimals). `best` is the deepest pool in dollars of any venue, which is the one the asset's premium to the Chainlink feed is measured from, and names its venue. `swaps24h` counts swap logs and `transactions24h` counts distinct transactions in (metricsAsOf - 24 hours, metricsAsOf], using each event block timestamp. Values are null until the entire window is indexed and when its end is more than 120 seconds old. `volumeUsd24h` uses the indexed quote leg. USDG is nominally denominated at 1 USDG = $1; WETH uses a recorded historical oracle estimate with at most one-hour archive sample age and an oracle answer within its published heartbeat. `volumeValuation` retains the method and coverage reason. Zero means a completely scanned window with no matching activity. `discovery` says how far each venue's pool scan has read: while `readingHistory` is true, a pool created in blocks the scan has not reached yet is not listed, and a venue whose `scanned` is false has not been read at all.

        Parameters
        ----------
        chain_id : int

        symbol : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetChainsChainIdAssetsSymbolPoolsResponse]
            Pools
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/assets/{encode_path_param(symbol)}/pools",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsChainIdAssetsSymbolPoolsResponse,
                    parse_obj_as(
                        type_=GetChainsChainIdAssetsSymbolPoolsResponse,
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

    async def one_row_per_utc_day_of_everything_the_registry_publishes_about_an_asset_multiplier_pause_and_halt_flags_feed_price_and_staleness_bid_and_ask_divergence_dex_price_premium_and_liquidity_supply_holders_and_lookalike_count(
        self,
        chain_id: int,
        symbol: str,
        *,
        from_: typing.Optional[dt.date] = None,
        to: typing.Optional[dt.date] = None,
        days: typing.Optional[int] = None,
        at: typing.Optional[dt.date] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetChainsChainIdAssetsSymbolHistoryResponse]:
        """
        Public. Written by the state-daily job, which runs hourly and rewrites the current UTC day's row, so a past day can be read back; the live tables carry only the current answer. Each row is a single reading taken at `takenAt`, not a daily open, close, mean or end-of-day value: it is the last reading the job took on that day, and the row for the current day is rewritten on the job's next run, so today's row is a partial day. Compare `takenAt` across rows before treating the series as evenly spaced. `from`/`to` are UTC days and default to the last 90; `days` sets the window length instead of `from`; `at=YYYY-MM-DD` returns that one day (an empty `days` array when no snapshot was taken); `fields` narrows each row to the keys named, `day` always included. `coverage` says how many days are actually on record and the first of them: there is nothing before the day the job first ran. A null is a figure that was not read that day, never a zero: a figure is copied only when the job that writes it read it that day, and `stateCheckedAt`, `feedCheckedAt`, `apiCheckedAt`, `dexCheckedAt` and `blockscoutCheckedAt` say when each group of figures was last read. `ledgerHolders` is written only for assets whose transfer history the ledger had finished reading, and `lookalikes` only once the lookalike scan has completed a pass. Rows are flat versions of the live `state` block: `feedPrice`/`feedStale` are `state.feed.price`/`.stale`, `bid`/`ask`/`tradingHalt` are `state.quote.bid`/`.ask`/`.tradingHalt`, `dexPriceUsd`/`dexPremiumPct`/`dexLiquidity` are `state.dex.priceUsd`/`.premiumPct`/`.liquidity`, `blockscoutHolders` is `state.secondSource.holders`, `multiplier` is `state.multiplier`.

        Parameters
        ----------
        chain_id : int

        symbol : str

        from_ : typing.Optional[dt.date]
            First UTC day, YYYY-MM-DD; must not be after `to`

        to : typing.Optional[dt.date]
            Last UTC day, YYYY-MM-DD; defaults to today

        days : typing.Optional[int]
            Window length in days ending at `to`; ignored when `from` is given

        at : typing.Optional[dt.date]

        fields : typing.Optional[str]
            Comma-separated keys to keep from each row: multiplier, tokenPaused, oraclePaused, tradingHalt, feedPrice, feedStale, bid, ask, priceDivergencePct, dexPriceUsd, dexPremiumPct, dexLiquidity, totalSupplyRaw, blockscoutHolders, ledgerHolders, lookalikes, stateCheckedAt, feedCheckedAt, apiCheckedAt, dexCheckedAt, blockscoutCheckedAt, takenAt. `day` is always included; an unknown key is a 400.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetChainsChainIdAssetsSymbolHistoryResponse]
            History
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/assets/{encode_path_param(symbol)}/history",
            method="GET",
            params={
                "from": str(from_) if from_ is not None else None,
                "to": str(to) if to is not None else None,
                "days": days,
                "at": str(at) if at is not None else None,
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsChainIdAssetsSymbolHistoryResponse,
                    parse_obj_as(
                        type_=GetChainsChainIdAssetsSymbolHistoryResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    async def the_chainlink_feeds_round_history_for_one_asset_newest_first_round_id_answer_price_multiplier_usd_started_at_updated_at(
        self,
        chain_id: int,
        symbol: str,
        *,
        since: typing.Optional[dt.datetime] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetChainsChainIdAssetsSymbolFeedRoundsResponse]:
        """
        Parameters
        ----------
        chain_id : int

        symbol : str

        since : typing.Optional[dt.datetime]

        limit : typing.Optional[int]
            Rounds, newest first; a malformed value reads as the default, a larger one as the maximum

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetChainsChainIdAssetsSymbolFeedRoundsResponse]
            Rounds
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/assets/{encode_path_param(symbol)}/feed/rounds",
            method="GET",
            params={
                "since": serialize_datetime(since) if since is not None else None,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsChainIdAssetsSymbolFeedRoundsResponse,
                    parse_obj_as(
                        type_=GetChainsChainIdAssetsSymbolFeedRoundsResponse,
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
