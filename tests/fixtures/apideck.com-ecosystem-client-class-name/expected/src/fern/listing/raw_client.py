

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.get_listing_response import GetListingResponse
from ..types.get_listings_response import GetListingsResponse
from pydantic import ValidationError


class RawListingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def listings_all(
        self,
        ecosystem_id: str,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        external_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetListingsResponse]:
        """
        List listings

        Parameters
        ----------
        ecosystem_id : str

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of records to return

        external_id : typing.Optional[str]
            Filter on external_id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetListingsResponse]
            Listings
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ecosystems/{encode_path_param(ecosystem_id)}/listings",
            method="GET",
            params={
                "cursor": cursor,
                "limit": limit,
                "external_id": external_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetListingsResponse,
                    parse_obj_as(
                        type_=GetListingsResponse,
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

    def listings_one(
        self, ecosystem_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetListingResponse]:
        """
        Get listing

        Parameters
        ----------
        ecosystem_id : str

        id : str
            ID of the record you are acting upon.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetListingResponse]
            Listing
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ecosystems/{encode_path_param(ecosystem_id)}/listings/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetListingResponse,
                    parse_obj_as(
                        type_=GetListingResponse,
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


class AsyncRawListingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def listings_all(
        self,
        ecosystem_id: str,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        external_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetListingsResponse]:
        """
        List listings

        Parameters
        ----------
        ecosystem_id : str

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of records to return

        external_id : typing.Optional[str]
            Filter on external_id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetListingsResponse]
            Listings
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ecosystems/{encode_path_param(ecosystem_id)}/listings",
            method="GET",
            params={
                "cursor": cursor,
                "limit": limit,
                "external_id": external_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetListingsResponse,
                    parse_obj_as(
                        type_=GetListingsResponse,
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

    async def listings_one(
        self, ecosystem_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetListingResponse]:
        """
        Get listing

        Parameters
        ----------
        ecosystem_id : str

        id : str
            ID of the record you are acting upon.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetListingResponse]
            Listing
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ecosystems/{encode_path_param(ecosystem_id)}/listings/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetListingResponse,
                    parse_obj_as(
                        type_=GetListingResponse,
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
