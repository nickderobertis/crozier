

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.get_pricing_tier_by_id_response import GetPricingTierByIdResponse
from ..types.get_pricing_tiers_response import GetPricingTiersResponse
from .types.get_pricing_tiers_request_sort_field import GetPricingTiersRequestSortField
from .types.get_pricing_tiers_request_sort_order import GetPricingTiersRequestSortOrder
from pydantic import ValidationError


class RawPricingTiersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_pricing_tiers(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetPricingTiersRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        sort_field: typing.Optional[GetPricingTiersRequestSortField] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetPricingTiersResponse]:
        """
        Schema for a Pricing Tier

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetPricingTiersRequestSortOrder]

        page_cursor : typing.Optional[str]

        sort_field : typing.Optional[GetPricingTiersRequestSortField]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetPricingTiersResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "pricingTiers",
            method="GET",
            params={
                "pageSize": page_size,
                "sortOrder": sort_order,
                "pageCursor": page_cursor,
                "sortField": sort_field,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPricingTiersResponse,
                    parse_obj_as(
                        type_=GetPricingTiersResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_pricing_tiers_id(
        self, id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetPricingTierByIdResponse]:
        """
        Schema for a Pricing Tier by ID

        Parameters
        ----------
        id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetPricingTierByIdResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pricingTiers/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPricingTierByIdResponse,
                    parse_obj_as(
                        type_=GetPricingTierByIdResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawPricingTiersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_pricing_tiers(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetPricingTiersRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        sort_field: typing.Optional[GetPricingTiersRequestSortField] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetPricingTiersResponse]:
        """
        Schema for a Pricing Tier

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetPricingTiersRequestSortOrder]

        page_cursor : typing.Optional[str]

        sort_field : typing.Optional[GetPricingTiersRequestSortField]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetPricingTiersResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pricingTiers",
            method="GET",
            params={
                "pageSize": page_size,
                "sortOrder": sort_order,
                "pageCursor": page_cursor,
                "sortField": sort_field,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPricingTiersResponse,
                    parse_obj_as(
                        type_=GetPricingTiersResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_pricing_tiers_id(
        self, id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetPricingTierByIdResponse]:
        """
        Schema for a Pricing Tier by ID

        Parameters
        ----------
        id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetPricingTierByIdResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pricingTiers/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPricingTierByIdResponse,
                    parse_obj_as(
                        type_=GetPricingTierByIdResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
