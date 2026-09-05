

import contextlib
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.forbidden_error import ForbiddenError
from ..errors.method_not_allowed_error import MethodNotAllowedError
from ..errors.not_found_error import NotFoundError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.api_error_model import ApiErrorModel
from ..types.http_validation_error import HttpValidationError
from ..types.v1alpha1plugin import V1Alpha1Plugin
from ..types.v1alpha1plugin_files import V1Alpha1PluginFiles
from pydantic import ValidationError


class RawPluginsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_plugin(
        self, plugin_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[V1Alpha1Plugin]:
        """
        Parameters
        ----------
        plugin_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1Alpha1Plugin]
            Plugin info
        """
        _response = self._client_wrapper.httpx_client.request(
            f"plugin/{encode_path_param(plugin_name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Alpha1Plugin,
                    parse_obj_as(
                        type_=V1Alpha1Plugin,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def list_plugins(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[V1Alpha1Plugin]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[V1Alpha1Plugin]]
            List of Plugins
        """
        _response = self._client_wrapper.httpx_client.request(
            "plugin/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1Alpha1Plugin],
                    parse_obj_as(
                        type_=typing.List[V1Alpha1Plugin],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def list_plugin_files(
        self, plugin_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[V1Alpha1PluginFiles]:
        """
        Parameters
        ----------
        plugin_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1Alpha1PluginFiles]
            List of files
        """
        _response = self._client_wrapper.httpx_client.request(
            f"plugin/{encode_path_param(plugin_name)}/files",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Alpha1PluginFiles,
                    parse_obj_as(
                        type_=V1Alpha1PluginFiles,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    @contextlib.contextmanager
    def get_plugin_file(
        self, plugin_name: str, file_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Parameters
        ----------
        plugin_name : str

        file_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            The file requested
        """
        with self._client_wrapper.httpx_client.stream(
            f"plugin/{encode_path_param(plugin_name)}/files/{encode_path_param(file_name)}",
            method="GET",
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    if _response.status_code == 403:
                        raise ForbiddenError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ApiErrorModel,
                                parse_obj_as(
                                    type_=ApiErrorModel,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ApiErrorModel,
                                parse_obj_as(
                                    type_=ApiErrorModel,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 405:
                        raise MethodNotAllowedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ApiErrorModel,
                                parse_obj_as(
                                    type_=ApiErrorModel,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 422:
                        raise UnprocessableEntityError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                HttpValidationError,
                                parse_obj_as(
                                    type_=HttpValidationError,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()


class AsyncRawPluginsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_plugin(
        self, plugin_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[V1Alpha1Plugin]:
        """
        Parameters
        ----------
        plugin_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1Alpha1Plugin]
            Plugin info
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"plugin/{encode_path_param(plugin_name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Alpha1Plugin,
                    parse_obj_as(
                        type_=V1Alpha1Plugin,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def list_plugins(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[V1Alpha1Plugin]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[V1Alpha1Plugin]]
            List of Plugins
        """
        _response = await self._client_wrapper.httpx_client.request(
            "plugin/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1Alpha1Plugin],
                    parse_obj_as(
                        type_=typing.List[V1Alpha1Plugin],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def list_plugin_files(
        self, plugin_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[V1Alpha1PluginFiles]:
        """
        Parameters
        ----------
        plugin_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1Alpha1PluginFiles]
            List of files
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"plugin/{encode_path_param(plugin_name)}/files",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Alpha1PluginFiles,
                    parse_obj_as(
                        type_=V1Alpha1PluginFiles,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    @contextlib.asynccontextmanager
    async def get_plugin_file(
        self, plugin_name: str, file_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Parameters
        ----------
        plugin_name : str

        file_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            The file requested
        """
        async with self._client_wrapper.httpx_client.stream(
            f"plugin/{encode_path_param(plugin_name)}/files/{encode_path_param(file_name)}",
            method="GET",
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    if _response.status_code == 403:
                        raise ForbiddenError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ApiErrorModel,
                                parse_obj_as(
                                    type_=ApiErrorModel,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ApiErrorModel,
                                parse_obj_as(
                                    type_=ApiErrorModel,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 405:
                        raise MethodNotAllowedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ApiErrorModel,
                                parse_obj_as(
                                    type_=ApiErrorModel,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 422:
                        raise UnprocessableEntityError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                HttpValidationError,
                                parse_obj_as(
                                    type_=HttpValidationError,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()
