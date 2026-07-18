

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.request_info import RequestInfo
from pydantic import ValidationError


class RawInspectRoutesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def inspect_inspect(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[RequestInfo]:
        """
        Inspect the incoming HTTP request and return the details

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RequestInfo]
            The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            "inspect",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RequestInfo,
                    parse_obj_as(
                        type_=RequestInfo,
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

    def inspect_inspect_post(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RequestInfo]:
        """
        Inspect the incoming HTTP request and return the details

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RequestInfo]
            The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            "inspect",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RequestInfo,
                    parse_obj_as(
                        type_=RequestInfo,
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

    def inspect_inspect_put(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RequestInfo]:
        """
        Inspect the incoming HTTP request and return the details

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RequestInfo]
            The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            "inspect",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RequestInfo,
                    parse_obj_as(
                        type_=RequestInfo,
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

    def inspect_inspect_delete(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RequestInfo]:
        """
        Inspect the incoming HTTP request and return the details

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RequestInfo]
            The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            "inspect",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RequestInfo,
                    parse_obj_as(
                        type_=RequestInfo,
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

    def inspect_inspect_patch(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RequestInfo]:
        """
        Inspect the incoming HTTP request and return the details

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RequestInfo]
            The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            "inspect",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RequestInfo,
                    parse_obj_as(
                        type_=RequestInfo,
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


class AsyncRawInspectRoutesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def inspect_inspect(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RequestInfo]:
        """
        Inspect the incoming HTTP request and return the details

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RequestInfo]
            The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inspect",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RequestInfo,
                    parse_obj_as(
                        type_=RequestInfo,
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

    async def inspect_inspect_post(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RequestInfo]:
        """
        Inspect the incoming HTTP request and return the details

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RequestInfo]
            The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inspect",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RequestInfo,
                    parse_obj_as(
                        type_=RequestInfo,
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

    async def inspect_inspect_put(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RequestInfo]:
        """
        Inspect the incoming HTTP request and return the details

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RequestInfo]
            The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inspect",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RequestInfo,
                    parse_obj_as(
                        type_=RequestInfo,
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

    async def inspect_inspect_delete(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RequestInfo]:
        """
        Inspect the incoming HTTP request and return the details

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RequestInfo]
            The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inspect",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RequestInfo,
                    parse_obj_as(
                        type_=RequestInfo,
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

    async def inspect_inspect_patch(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RequestInfo]:
        """
        Inspect the incoming HTTP request and return the details

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RequestInfo]
            The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inspect",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RequestInfo,
                    parse_obj_as(
                        type_=RequestInfo,
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
