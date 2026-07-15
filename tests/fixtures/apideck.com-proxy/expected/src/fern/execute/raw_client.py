

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.unauthorized_error import UnauthorizedError
from .types.patch_proxy_request_body import PatchProxyRequestBody
from .types.post_proxy_request_body import PostProxyRequestBody
from .types.put_proxy_request_body import PutProxyRequestBody


OMIT = typing.cast(typing.Any, ...)


class RawExecuteClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_proxy(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[typing.Any]]:
        """
        Proxies a downstream GET request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization.
        **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.Any]]
            Ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "proxy",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.Any],
                    parse_obj_as(
                        type_=typing.Optional[typing.Any],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_proxy(
        self, *, request: PostProxyRequestBody, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[typing.Any]]:
        """
        Proxies a downstream POST request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization.
        **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers.

        Parameters
        ----------
        request : PostProxyRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.Any]]
            Ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "proxy",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PostProxyRequestBody, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.Any],
                    parse_obj_as(
                        type_=typing.Optional[typing.Any],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def put_proxy(
        self, *, request: PutProxyRequestBody, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[typing.Any]]:
        """
        Proxies a downstream PUT request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization.
        **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers.

        Parameters
        ----------
        request : PutProxyRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.Any]]
            Ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "proxy",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PutProxyRequestBody, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.Any],
                    parse_obj_as(
                        type_=typing.Optional[typing.Any],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_proxy(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[typing.Any]]:
        """
        Proxies a downstream DELETE request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization.
        **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.Any]]
            Ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "proxy",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.Any],
                    parse_obj_as(
                        type_=typing.Optional[typing.Any],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def patch_proxy(
        self, *, request: PatchProxyRequestBody, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[typing.Any]]:
        """
        Proxies a downstream PATCH request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization.
        **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers.

        Parameters
        ----------
        request : PatchProxyRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.Any]]
            Ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "proxy",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PatchProxyRequestBody, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.Any],
                    parse_obj_as(
                        type_=typing.Optional[typing.Any],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawExecuteClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_proxy(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[typing.Any]]:
        """
        Proxies a downstream GET request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization.
        **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.Any]]
            Ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "proxy",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.Any],
                    parse_obj_as(
                        type_=typing.Optional[typing.Any],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_proxy(
        self, *, request: PostProxyRequestBody, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[typing.Any]]:
        """
        Proxies a downstream POST request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization.
        **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers.

        Parameters
        ----------
        request : PostProxyRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.Any]]
            Ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "proxy",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PostProxyRequestBody, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.Any],
                    parse_obj_as(
                        type_=typing.Optional[typing.Any],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def put_proxy(
        self, *, request: PutProxyRequestBody, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[typing.Any]]:
        """
        Proxies a downstream PUT request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization.
        **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers.

        Parameters
        ----------
        request : PutProxyRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.Any]]
            Ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "proxy",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PutProxyRequestBody, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.Any],
                    parse_obj_as(
                        type_=typing.Optional[typing.Any],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_proxy(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[typing.Any]]:
        """
        Proxies a downstream DELETE request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization.
        **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.Any]]
            Ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "proxy",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.Any],
                    parse_obj_as(
                        type_=typing.Optional[typing.Any],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def patch_proxy(
        self, *, request: PatchProxyRequestBody, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[typing.Any]]:
        """
        Proxies a downstream PATCH request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization.
        **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers.

        Parameters
        ----------
        request : PatchProxyRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.Any]]
            Ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "proxy",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PatchProxyRequestBody, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.Any],
                    parse_obj_as(
                        type_=typing.Optional[typing.Any],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
