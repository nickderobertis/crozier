

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from .types.proxycredentials_request_logging import ProxycredentialsRequestLogging
from .types.proxycredentials_response import ProxycredentialsResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawProxyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def proxychat_completions(
        self, *, request: typing.Optional[typing.Any] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[typing.Any]]:
        """
        Proxy a chat/completions request to the specified model, converting its format as needed. Will cache if temperature=0 or seed is set.

        Parameters
        ----------
        request : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.Any]]
            Proxy response (supports both streaming and non-streaming formats)
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/proxy/chat/completions",
            method="POST",
            json=request,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def proxycompletions(
        self, *, request: typing.Optional[typing.Any] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[typing.Any]]:
        """
        Proxy a completions request to the specified model, converting its format as needed. Will cache if temperature=0 or seed is set.

        Parameters
        ----------
        request : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.Any]]
            Proxy response (supports both streaming and non-streaming formats)
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/proxy/completions",
            method="POST",
            json=request,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def proxyauto(
        self, *, request: typing.Optional[typing.Any] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[typing.Any]]:
        """
        Proxy a request to either chat/completions or completions automatically based on the model. Will cache if temperature=0 or seed is set.

        Parameters
        ----------
        request : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.Any]]
            Proxy response (supports both streaming and non-streaming formats)
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/proxy/auto",
            method="POST",
            json=request,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def proxyembeddings(
        self, *, request: typing.Optional[typing.Any] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[typing.Any]]:
        """
        Proxy an embeddings request to the specified model, converting its format as needed. Will cache automatically.

        Parameters
        ----------
        request : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.Any]]
            Proxy response (supports both streaming and non-streaming formats)
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/proxy/embeddings",
            method="POST",
            json=request,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def proxycredentials(
        self,
        *,
        model: typing.Optional[str] = OMIT,
        ttl_seconds: typing.Optional[float] = OMIT,
        logging: typing.Optional[ProxycredentialsRequestLogging] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProxycredentialsResponse]:
        """
        Create a temporary credential which can access the proxy for a limited time. The temporary credential will be allowed to make requests on behalf of the Braintrust API key (or model provider API key) provided in the `Authorization` header. See [docs](/docs/deploy/ai-proxy#create-temporary-credentials) for code examples.

        Parameters
        ----------
        model : typing.Optional[str]
            Granted model name. Null/undefined to grant usage of all models.

        ttl_seconds : typing.Optional[float]
            TTL of the temporary credential. 10 minutes by default.

        logging : typing.Optional[ProxycredentialsRequestLogging]
            If present, proxy will log requests to the given Braintrust project name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProxycredentialsResponse]
            Successfully created temporary credential
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/proxy/credentials",
            method="POST",
            json={
                "model": model,
                "ttl_seconds": ttl_seconds,
                "logging": convert_and_respect_annotation_metadata(
                    object_=logging, annotation=typing.Optional[ProxycredentialsRequestLogging], direction="write"
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
                    ProxycredentialsResponse,
                    parse_obj_as(
                        type_=ProxycredentialsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def path(
        self,
        path: typing.Sequence[str],
        *,
        request: typing.Optional[typing.Any] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[typing.Any]]:
        """
        Any requests which do not match the above paths will be proxied directly to the OpenAI API.

        Parameters
        ----------
        path : typing.Sequence[str]
            The path to proxy

        request : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.Any]]
            Proxy response (supports both streaming and non-streaming formats)
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/proxy/{encode_path_param(path)}",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawProxyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def proxychat_completions(
        self, *, request: typing.Optional[typing.Any] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[typing.Any]]:
        """
        Proxy a chat/completions request to the specified model, converting its format as needed. Will cache if temperature=0 or seed is set.

        Parameters
        ----------
        request : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.Any]]
            Proxy response (supports both streaming and non-streaming formats)
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/proxy/chat/completions",
            method="POST",
            json=request,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def proxycompletions(
        self, *, request: typing.Optional[typing.Any] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[typing.Any]]:
        """
        Proxy a completions request to the specified model, converting its format as needed. Will cache if temperature=0 or seed is set.

        Parameters
        ----------
        request : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.Any]]
            Proxy response (supports both streaming and non-streaming formats)
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/proxy/completions",
            method="POST",
            json=request,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def proxyauto(
        self, *, request: typing.Optional[typing.Any] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[typing.Any]]:
        """
        Proxy a request to either chat/completions or completions automatically based on the model. Will cache if temperature=0 or seed is set.

        Parameters
        ----------
        request : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.Any]]
            Proxy response (supports both streaming and non-streaming formats)
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/proxy/auto",
            method="POST",
            json=request,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def proxyembeddings(
        self, *, request: typing.Optional[typing.Any] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[typing.Any]]:
        """
        Proxy an embeddings request to the specified model, converting its format as needed. Will cache automatically.

        Parameters
        ----------
        request : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.Any]]
            Proxy response (supports both streaming and non-streaming formats)
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/proxy/embeddings",
            method="POST",
            json=request,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def proxycredentials(
        self,
        *,
        model: typing.Optional[str] = OMIT,
        ttl_seconds: typing.Optional[float] = OMIT,
        logging: typing.Optional[ProxycredentialsRequestLogging] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProxycredentialsResponse]:
        """
        Create a temporary credential which can access the proxy for a limited time. The temporary credential will be allowed to make requests on behalf of the Braintrust API key (or model provider API key) provided in the `Authorization` header. See [docs](/docs/deploy/ai-proxy#create-temporary-credentials) for code examples.

        Parameters
        ----------
        model : typing.Optional[str]
            Granted model name. Null/undefined to grant usage of all models.

        ttl_seconds : typing.Optional[float]
            TTL of the temporary credential. 10 minutes by default.

        logging : typing.Optional[ProxycredentialsRequestLogging]
            If present, proxy will log requests to the given Braintrust project name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProxycredentialsResponse]
            Successfully created temporary credential
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/proxy/credentials",
            method="POST",
            json={
                "model": model,
                "ttl_seconds": ttl_seconds,
                "logging": convert_and_respect_annotation_metadata(
                    object_=logging, annotation=typing.Optional[ProxycredentialsRequestLogging], direction="write"
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
                    ProxycredentialsResponse,
                    parse_obj_as(
                        type_=ProxycredentialsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def path(
        self,
        path: typing.Sequence[str],
        *,
        request: typing.Optional[typing.Any] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[typing.Any]]:
        """
        Any requests which do not match the above paths will be proxied directly to the OpenAI API.

        Parameters
        ----------
        path : typing.Sequence[str]
            The path to proxy

        request : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.Any]]
            Proxy response (supports both streaming and non-streaming formats)
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/proxy/{encode_path_param(path)}",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
