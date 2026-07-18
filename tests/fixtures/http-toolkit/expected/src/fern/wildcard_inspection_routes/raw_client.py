

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.request_info import RequestInfo
from pydantic import ValidationError


class RawWildcardInspectionRoutesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def wildcard_inspect_anything(
        self, extra_path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RequestInfo]:
        """
        Any route or path that doesn't match other operations is automatically inspected, e.g. /blah/cheese/shoe will still return the details of the request

        Parameters
        ----------
        extra_path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RequestInfo]
            The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"anything/{encode_path_param(extra_path)}",
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

    def wildcard_inspect_anything_post(
        self, extra_path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RequestInfo]:
        """
        Any route or path that doesn't match other operations is automatically inspected, e.g. /blah/cheese/shoe will still return the details of the request

        Parameters
        ----------
        extra_path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RequestInfo]
            The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"anything/{encode_path_param(extra_path)}",
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

    def wildcard_inspect_anything_put(
        self, extra_path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RequestInfo]:
        """
        Any route or path that doesn't match other operations is automatically inspected, e.g. /blah/cheese/shoe will still return the details of the request

        Parameters
        ----------
        extra_path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RequestInfo]
            The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"anything/{encode_path_param(extra_path)}",
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

    def wildcard_inspect_anything_delete(
        self, extra_path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RequestInfo]:
        """
        Any route or path that doesn't match other operations is automatically inspected, e.g. /blah/cheese/shoe will still return the details of the request

        Parameters
        ----------
        extra_path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RequestInfo]
            The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"anything/{encode_path_param(extra_path)}",
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

    def wildcard_inspect_anything_patch(
        self, extra_path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RequestInfo]:
        """
        Any route or path that doesn't match other operations is automatically inspected, e.g. /blah/cheese/shoe will still return the details of the request

        Parameters
        ----------
        extra_path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RequestInfo]
            The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"anything/{encode_path_param(extra_path)}",
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


class AsyncRawWildcardInspectionRoutesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def wildcard_inspect_anything(
        self, extra_path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RequestInfo]:
        """
        Any route or path that doesn't match other operations is automatically inspected, e.g. /blah/cheese/shoe will still return the details of the request

        Parameters
        ----------
        extra_path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RequestInfo]
            The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"anything/{encode_path_param(extra_path)}",
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

    async def wildcard_inspect_anything_post(
        self, extra_path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RequestInfo]:
        """
        Any route or path that doesn't match other operations is automatically inspected, e.g. /blah/cheese/shoe will still return the details of the request

        Parameters
        ----------
        extra_path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RequestInfo]
            The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"anything/{encode_path_param(extra_path)}",
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

    async def wildcard_inspect_anything_put(
        self, extra_path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RequestInfo]:
        """
        Any route or path that doesn't match other operations is automatically inspected, e.g. /blah/cheese/shoe will still return the details of the request

        Parameters
        ----------
        extra_path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RequestInfo]
            The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"anything/{encode_path_param(extra_path)}",
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

    async def wildcard_inspect_anything_delete(
        self, extra_path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RequestInfo]:
        """
        Any route or path that doesn't match other operations is automatically inspected, e.g. /blah/cheese/shoe will still return the details of the request

        Parameters
        ----------
        extra_path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RequestInfo]
            The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"anything/{encode_path_param(extra_path)}",
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

    async def wildcard_inspect_anything_patch(
        self, extra_path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RequestInfo]:
        """
        Any route or path that doesn't match other operations is automatically inspected, e.g. /blah/cheese/shoe will still return the details of the request

        Parameters
        ----------
        extra_path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RequestInfo]
            The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"anything/{encode_path_param(extra_path)}",
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
