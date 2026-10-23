

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..types.bad_request_error_body import BadRequestErrorBody
from ..types.not_found_error_body import NotFoundErrorBody
from ..types.service_unavailable_error_body import ServiceUnavailableErrorBody
from ..types.too_many_requests_error_body import TooManyRequestsErrorBody
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
from pydantic import ValidationError


class RawChainsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_robinhood_chain_networks(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetChainsResponse]:
        """
        Public. The public RPC URL, the explorer and whether Fletch has a provider key for the chain; a configured provider URL is never returned.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetChainsResponse]
            The two Robinhood chains
        """
        _response = self._client_wrapper.httpx_client.request(
            "chains",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsResponse,
                    parse_obj_as(
                        type_=GetChainsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def token_identity_and_current_market_observations_at_one_contract_address(
        self, address: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetTokensAddressResponse]:
        """
        Public. The canonical trust verdict is shared by pages and pool responses. A lookalike records a normalized name or ticker collision; it does not establish intent. `reading` is the exact token-page observation: full address, economic selection reason, same-name alternatives, selected-pool volume, market cap and holders with source, timestamp and missing-value reason. Community dominance is an economic comparison. `market` retains the compact selected-pool view. V3 quote holdings and V4 bounded 1% quote input are separate measures. Volume sources distinguish nominal USDG quote units from WETH converted with a historical oracle estimate.

        Parameters
        ----------
        address : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetTokensAddressResponse]
            What this token is
        """
        _response = self._client_wrapper.httpx_client.request(
            f"tokens/{encode_path_param(address)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetTokensAddressResponse,
                    parse_obj_as(
                        type_=GetTokensAddressResponse,
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

    def get_app_catalog(
        self,
        chain_id: int,
        *,
        q: typing.Optional[str] = None,
        status: typing.Optional[GetAppCatalogRequestStatus] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetAppCatalogResponse]:
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
        HttpResponse[GetAppCatalogResponse]
            Recorded app catalog, with freshness and source errors
        """
        _response = self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/app-catalog",
            method="GET",
            params={
                "q": q,
                "status": status,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAppCatalogResponse,
                    parse_obj_as(
                        type_=GetAppCatalogResponse,
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
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ServiceUnavailableErrorBody,
                        parse_obj_as(
                            type_=ServiceUnavailableErrorBody,
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
    ) -> HttpResponse[GetChainsChainIdMarketsResponse]:
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
        HttpResponse[GetChainsChainIdMarketsResponse]
            A page of token observations
        """
        _response = self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/markets",
            method="GET",
            params={
                "page": page,
                "pageSize": page_size,
                "kind": kind,
                "trust": trust,
                "sort": sort,
                "activity": activity,
                "data": data,
                "depth": depth,
                "identity": identity,
                "minVolumeUsd": min_volume_usd,
                "q": q,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsChainIdMarketsResponse,
                    parse_obj_as(
                        type_=GetChainsChainIdMarketsResponse,
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

    def discover_token_market_filters_labels_thresholds_and_useful_query_presets(
        self, chain_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetChainsChainIdMarketsFiltersResponse]:
        """
        The catalog used by the token Markets page and query parser. Combine filters with AND. Activity requires a complete current selected-pool window. Numeric thresholds exclude unavailable data, including for a threshold of zero. V3 quote holdings and V4 bounded depth are separate filters and sorts.

        Parameters
        ----------
        chain_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetChainsChainIdMarketsFiltersResponse]
            Machine-readable market filter catalog
        """
        _response = self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/markets/filters",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsChainIdMarketsFiltersResponse,
                    parse_obj_as(
                        type_=GetChainsChainIdMarketsFiltersResponse,
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
    ) -> HttpResponse[GetChainsChainIdDexPoolsResponse]:
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
        HttpResponse[GetChainsChainIdDexPoolsResponse]
            A page of pools
        """
        _response = self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/dex/pools",
            method="GET",
            params={
                "kind": kind,
                "tier": tier,
                "sort": sort,
                "venue": venue,
                "q": q,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsChainIdDexPoolsResponse,
                    parse_obj_as(
                        type_=GetChainsChainIdDexPoolsResponse,
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


class AsyncRawChainsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_robinhood_chain_networks(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetChainsResponse]:
        """
        Public. The public RPC URL, the explorer and whether Fletch has a provider key for the chain; a configured provider URL is never returned.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetChainsResponse]
            The two Robinhood chains
        """
        _response = await self._client_wrapper.httpx_client.request(
            "chains",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsResponse,
                    parse_obj_as(
                        type_=GetChainsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def token_identity_and_current_market_observations_at_one_contract_address(
        self, address: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetTokensAddressResponse]:
        """
        Public. The canonical trust verdict is shared by pages and pool responses. A lookalike records a normalized name or ticker collision; it does not establish intent. `reading` is the exact token-page observation: full address, economic selection reason, same-name alternatives, selected-pool volume, market cap and holders with source, timestamp and missing-value reason. Community dominance is an economic comparison. `market` retains the compact selected-pool view. V3 quote holdings and V4 bounded 1% quote input are separate measures. Volume sources distinguish nominal USDG quote units from WETH converted with a historical oracle estimate.

        Parameters
        ----------
        address : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetTokensAddressResponse]
            What this token is
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tokens/{encode_path_param(address)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetTokensAddressResponse,
                    parse_obj_as(
                        type_=GetTokensAddressResponse,
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

    async def get_app_catalog(
        self,
        chain_id: int,
        *,
        q: typing.Optional[str] = None,
        status: typing.Optional[GetAppCatalogRequestStatus] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetAppCatalogResponse]:
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
        AsyncHttpResponse[GetAppCatalogResponse]
            Recorded app catalog, with freshness and source errors
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/app-catalog",
            method="GET",
            params={
                "q": q,
                "status": status,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAppCatalogResponse,
                    parse_obj_as(
                        type_=GetAppCatalogResponse,
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
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ServiceUnavailableErrorBody,
                        parse_obj_as(
                            type_=ServiceUnavailableErrorBody,
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
    ) -> AsyncHttpResponse[GetChainsChainIdMarketsResponse]:
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
        AsyncHttpResponse[GetChainsChainIdMarketsResponse]
            A page of token observations
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/markets",
            method="GET",
            params={
                "page": page,
                "pageSize": page_size,
                "kind": kind,
                "trust": trust,
                "sort": sort,
                "activity": activity,
                "data": data,
                "depth": depth,
                "identity": identity,
                "minVolumeUsd": min_volume_usd,
                "q": q,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsChainIdMarketsResponse,
                    parse_obj_as(
                        type_=GetChainsChainIdMarketsResponse,
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

    async def discover_token_market_filters_labels_thresholds_and_useful_query_presets(
        self, chain_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetChainsChainIdMarketsFiltersResponse]:
        """
        The catalog used by the token Markets page and query parser. Combine filters with AND. Activity requires a complete current selected-pool window. Numeric thresholds exclude unavailable data, including for a threshold of zero. V3 quote holdings and V4 bounded depth are separate filters and sorts.

        Parameters
        ----------
        chain_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetChainsChainIdMarketsFiltersResponse]
            Machine-readable market filter catalog
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/markets/filters",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsChainIdMarketsFiltersResponse,
                    parse_obj_as(
                        type_=GetChainsChainIdMarketsFiltersResponse,
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
    ) -> AsyncHttpResponse[GetChainsChainIdDexPoolsResponse]:
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
        AsyncHttpResponse[GetChainsChainIdDexPoolsResponse]
            A page of pools
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"chains/{encode_path_param(chain_id)}/dex/pools",
            method="GET",
            params={
                "kind": kind,
                "tier": tier,
                "sort": sort,
                "venue": venue,
                "q": q,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChainsChainIdDexPoolsResponse,
                    parse_obj_as(
                        type_=GetChainsChainIdDexPoolsResponse,
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
