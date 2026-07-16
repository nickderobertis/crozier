

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.post_assets_prices_adjusted_forward_request_assets_item import (
    PostAssetsPricesAdjustedForwardRequestAssetsItem,
)
from .types.post_assets_prices_adjusted_forward_response import PostAssetsPricesAdjustedForwardResponse
from .types.post_assets_prices_adjusted_request_assets_item import PostAssetsPricesAdjustedRequestAssetsItem
from .types.post_assets_prices_adjusted_response import PostAssetsPricesAdjustedResponse


OMIT = typing.cast(typing.Any, ...)


class RawAssetsPricesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def adjusted_prices(
        self,
        *,
        assets: typing.Sequence[PostAssetsPricesAdjustedRequestAssetsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostAssetsPricesAdjustedResponse]:
        """
        Compute the backward-adjusted prices of one or several asset(s) for one or several date(s) from:
        * Unadjusted prices
        * Capital distributions, like stock dividends
        * Splits, like stock splits

        The adjustment base date is chosen to be the last date for which unadjusted prices are available, which implies that:
        * The price on the last date for which unadjusted prices are available is left unadjusted
        * The price on any other date is adjusted based on the capital distributions and the splits which occurred between this date and the last date for which unadjusted prices are available

        References
        * [Center for Research in Security Prices](https://www.crsp.org/products/documentation/crsp-calculations)

        Parameters
        ----------
        assets : typing.Sequence[PostAssetsPricesAdjustedRequestAssetsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostAssetsPricesAdjustedResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "assets/prices/adjusted",
            method="POST",
            json={
                "assets": convert_and_respect_annotation_metadata(
                    object_=assets,
                    annotation=typing.Sequence[PostAssetsPricesAdjustedRequestAssetsItem],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostAssetsPricesAdjustedResponse,
                    parse_obj_as(
                        type_=PostAssetsPricesAdjustedResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def forward_adjusted_prices(
        self,
        *,
        assets: typing.Sequence[PostAssetsPricesAdjustedForwardRequestAssetsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostAssetsPricesAdjustedForwardResponse]:
        """
        Compute the forward-adjusted prices of one or several asset(s) for one or several date(s) from:
        * Unadjusted prices
        * Capital distributions, like stock dividends
        * Splits, like stock splits

        The adjustment base date is chosen to be the first date for which unadjusted prices are available, which implies that:
        * The price on the first date for which unadjusted prices are available is left unadjusted
        * The price on any other date is adjusted based on the capital distributions and the splits which occurred between this date and the first date for which unadjusted prices are available

        References
        * [Center for Research in Security Prices](https://www.crsp.org/products/documentation/crsp-calculations)

        Parameters
        ----------
        assets : typing.Sequence[PostAssetsPricesAdjustedForwardRequestAssetsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostAssetsPricesAdjustedForwardResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "assets/prices/adjusted/forward",
            method="POST",
            json={
                "assets": convert_and_respect_annotation_metadata(
                    object_=assets,
                    annotation=typing.Sequence[PostAssetsPricesAdjustedForwardRequestAssetsItem],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostAssetsPricesAdjustedForwardResponse,
                    parse_obj_as(
                        type_=PostAssetsPricesAdjustedForwardResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawAssetsPricesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def adjusted_prices(
        self,
        *,
        assets: typing.Sequence[PostAssetsPricesAdjustedRequestAssetsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostAssetsPricesAdjustedResponse]:
        """
        Compute the backward-adjusted prices of one or several asset(s) for one or several date(s) from:
        * Unadjusted prices
        * Capital distributions, like stock dividends
        * Splits, like stock splits

        The adjustment base date is chosen to be the last date for which unadjusted prices are available, which implies that:
        * The price on the last date for which unadjusted prices are available is left unadjusted
        * The price on any other date is adjusted based on the capital distributions and the splits which occurred between this date and the last date for which unadjusted prices are available

        References
        * [Center for Research in Security Prices](https://www.crsp.org/products/documentation/crsp-calculations)

        Parameters
        ----------
        assets : typing.Sequence[PostAssetsPricesAdjustedRequestAssetsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostAssetsPricesAdjustedResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "assets/prices/adjusted",
            method="POST",
            json={
                "assets": convert_and_respect_annotation_metadata(
                    object_=assets,
                    annotation=typing.Sequence[PostAssetsPricesAdjustedRequestAssetsItem],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostAssetsPricesAdjustedResponse,
                    parse_obj_as(
                        type_=PostAssetsPricesAdjustedResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def forward_adjusted_prices(
        self,
        *,
        assets: typing.Sequence[PostAssetsPricesAdjustedForwardRequestAssetsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostAssetsPricesAdjustedForwardResponse]:
        """
        Compute the forward-adjusted prices of one or several asset(s) for one or several date(s) from:
        * Unadjusted prices
        * Capital distributions, like stock dividends
        * Splits, like stock splits

        The adjustment base date is chosen to be the first date for which unadjusted prices are available, which implies that:
        * The price on the first date for which unadjusted prices are available is left unadjusted
        * The price on any other date is adjusted based on the capital distributions and the splits which occurred between this date and the first date for which unadjusted prices are available

        References
        * [Center for Research in Security Prices](https://www.crsp.org/products/documentation/crsp-calculations)

        Parameters
        ----------
        assets : typing.Sequence[PostAssetsPricesAdjustedForwardRequestAssetsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostAssetsPricesAdjustedForwardResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "assets/prices/adjusted/forward",
            method="POST",
            json={
                "assets": convert_and_respect_annotation_metadata(
                    object_=assets,
                    annotation=typing.Sequence[PostAssetsPricesAdjustedForwardRequestAssetsItem],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostAssetsPricesAdjustedForwardResponse,
                    parse_obj_as(
                        type_=PostAssetsPricesAdjustedForwardResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
