

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.get_headers_request_response import GetHeadersRequestResponse
from .types.get_headers_undeclared_response import GetHeadersUndeclaredResponse
from pydantic import ValidationError


class RawRequestHeadersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_headers_undeclared(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetHeadersUndeclaredResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetHeadersUndeclaredResponse]
            success
        """
        _response = self._client_wrapper.httpx_client.request(
            "headers/undeclared",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetHeadersUndeclaredResponse,
                    parse_obj_as(
                        type_=GetHeadersUndeclaredResponse,
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

    def get_headers_request(
        self,
        *,
        route_level_header: typing.Optional[str] = None,
        number_header: typing.Optional[float] = None,
        boolean_header: typing.Optional[bool] = None,
        second_boolean_header: typing.Optional[bool] = None,
        authorization: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetHeadersRequestResponse]:
        """
        Parameters
        ----------
        route_level_header : typing.Optional[str]

        number_header : typing.Optional[float]

        boolean_header : typing.Optional[bool]

        second_boolean_header : typing.Optional[bool]

        authorization : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetHeadersRequestResponse]
            success
        """
        _response = self._client_wrapper.httpx_client.request(
            "headers/request",
            method="GET",
            headers={
                "Route-Level-Header": str(route_level_header) if route_level_header is not None else None,
                "Number-Header": str(number_header) if number_header is not None else None,
                "Boolean-Header": str(boolean_header) if boolean_header is not None else None,
                "Second-Boolean-Header": str(second_boolean_header) if second_boolean_header is not None else None,
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetHeadersRequestResponse,
                    parse_obj_as(
                        type_=GetHeadersRequestResponse,
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


class AsyncRawRequestHeadersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_headers_undeclared(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetHeadersUndeclaredResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetHeadersUndeclaredResponse]
            success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "headers/undeclared",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetHeadersUndeclaredResponse,
                    parse_obj_as(
                        type_=GetHeadersUndeclaredResponse,
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

    async def get_headers_request(
        self,
        *,
        route_level_header: typing.Optional[str] = None,
        number_header: typing.Optional[float] = None,
        boolean_header: typing.Optional[bool] = None,
        second_boolean_header: typing.Optional[bool] = None,
        authorization: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetHeadersRequestResponse]:
        """
        Parameters
        ----------
        route_level_header : typing.Optional[str]

        number_header : typing.Optional[float]

        boolean_header : typing.Optional[bool]

        second_boolean_header : typing.Optional[bool]

        authorization : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetHeadersRequestResponse]
            success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "headers/request",
            method="GET",
            headers={
                "Route-Level-Header": str(route_level_header) if route_level_header is not None else None,
                "Number-Header": str(number_header) if number_header is not None else None,
                "Boolean-Header": str(boolean_header) if boolean_header is not None else None,
                "Second-Boolean-Header": str(second_boolean_header) if second_boolean_header is not None else None,
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetHeadersRequestResponse,
                    parse_obj_as(
                        type_=GetHeadersRequestResponse,
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
