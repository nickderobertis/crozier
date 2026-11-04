

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.me_get_response import MeGetResponse
from .types.me_vals2response import MeVals2Response
from pydantic import ValidationError


class RawMeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[MeGetResponse]:
        """
        Get profile information for the current user

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MeGetResponse]
            Your user information, with tier and email included
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/me",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MeGetResponse,
                    parse_obj_as(
                        type_=MeGetResponse,
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

    def me_vals2(
        self, *, offset: int, limit: int, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MeVals2Response]:
        """
        [BETA] List all of a user's vals for authenticated users

        Parameters
        ----------
        offset : int
            Number of items to skip in order to deliver paginated results

        limit : int
            Maximum items to return in each paginated response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MeVals2Response]
            A paginated result set
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/me/vals",
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MeVals2Response,
                    parse_obj_as(
                        type_=MeVals2Response,
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


class AsyncRawMeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(self, *, request_options: typing.Optional[RequestOptions] = None) -> AsyncHttpResponse[MeGetResponse]:
        """
        Get profile information for the current user

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MeGetResponse]
            Your user information, with tier and email included
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/me",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MeGetResponse,
                    parse_obj_as(
                        type_=MeGetResponse,
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

    async def me_vals2(
        self, *, offset: int, limit: int, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MeVals2Response]:
        """
        [BETA] List all of a user's vals for authenticated users

        Parameters
        ----------
        offset : int
            Number of items to skip in order to deliver paginated results

        limit : int
            Maximum items to return in each paginated response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MeVals2Response]
            A paginated result set
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/me/vals",
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MeVals2Response,
                    parse_obj_as(
                        type_=MeVals2Response,
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
