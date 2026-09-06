

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.api_paged_response_dealer_db_models_dealers_per_country import (
    ApiPagedResponseDealerDbModelsDealersPerCountry,
)
from pydantic import ValidationError


class RawDealerbycountryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getcountries(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiPagedResponseDealerDbModelsDealersPerCountry]:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiPagedResponseDealerDbModelsDealersPerCountry]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/DealerByCountry",
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
                    ApiPagedResponseDealerDbModelsDealersPerCountry,
                    parse_obj_as(
                        type_=ApiPagedResponseDealerDbModelsDealersPerCountry,
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


class AsyncRawDealerbycountryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getcountries(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiPagedResponseDealerDbModelsDealersPerCountry]:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiPagedResponseDealerDbModelsDealersPerCountry]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/DealerByCountry",
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
                    ApiPagedResponseDealerDbModelsDealersPerCountry,
                    parse_obj_as(
                        type_=ApiPagedResponseDealerDbModelsDealersPerCountry,
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
