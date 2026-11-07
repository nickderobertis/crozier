

import contextlib
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError as core_api_error_ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.gone_error import GoneError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.api_error import ApiError as types_api_error_ApiError
from ..types.app_id import AppId
from ..types.deployment_id import DeploymentId
from ..types.logs_follow import LogsFollow
from ..types.process_id import ProcessId
from ..types.region import Region
from ..types.tail_lines import TailLines
from pydantic import ValidationError


class RawLogV1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    @contextlib.contextmanager
    def get_logs_for_app(
        self,
        app_id: AppId,
        *,
        follow: typing.Optional[LogsFollow] = None,
        tail_lines: typing.Optional[TailLines] = None,
        region: typing.Optional[Region] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Returns a stream of logs for an [application](https://hathora.dev/docs/concepts/hathora-entities#application) using `appId`.

        Parameters
        ----------
        app_id : AppId

        follow : typing.Optional[LogsFollow]

        tail_lines : typing.Optional[TailLines]

        region : typing.Optional[Region]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            Ok
        """
        with self._client_wrapper.httpx_client.stream(
            f"logs/v1/{encode_path_param(app_id)}/all",
            method="GET",
            params={
                "follow": follow,
                "tailLines": tail_lines,
                "region": region,
            },
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
                    if _response.status_code == 401:
                        raise UnauthorizedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                types_api_error_ApiError,
                                parse_obj_as(
                                    type_=types_api_error_ApiError,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                types_api_error_ApiError,
                                parse_obj_as(
                                    type_=types_api_error_ApiError,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise core_api_error_ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise core_api_error_ApiError(
                    status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
                )

            yield _stream()

    @contextlib.contextmanager
    def get_logs_for_process(
        self,
        app_id: AppId,
        process_id: ProcessId,
        *,
        follow: typing.Optional[LogsFollow] = None,
        tail_lines: typing.Optional[TailLines] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Returns a stream of logs for a [process](https://hathora.dev/docs/concepts/hathora-entities#process) using `appId` and `processId`.

        Parameters
        ----------
        app_id : AppId

        process_id : ProcessId

        follow : typing.Optional[LogsFollow]

        tail_lines : typing.Optional[TailLines]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            Ok
        """
        with self._client_wrapper.httpx_client.stream(
            f"logs/v1/{encode_path_param(app_id)}/process/{encode_path_param(process_id)}",
            method="GET",
            params={
                "follow": follow,
                "tailLines": tail_lines,
            },
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
                    if _response.status_code == 400:
                        raise BadRequestError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                types_api_error_ApiError,
                                parse_obj_as(
                                    type_=types_api_error_ApiError,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 401:
                        raise UnauthorizedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                types_api_error_ApiError,
                                parse_obj_as(
                                    type_=types_api_error_ApiError,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                types_api_error_ApiError,
                                parse_obj_as(
                                    type_=types_api_error_ApiError,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 410:
                        raise GoneError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                types_api_error_ApiError,
                                parse_obj_as(
                                    type_=types_api_error_ApiError,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 500:
                        raise InternalServerError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                types_api_error_ApiError,
                                parse_obj_as(
                                    type_=types_api_error_ApiError,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise core_api_error_ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise core_api_error_ApiError(
                    status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
                )

            yield _stream()

    @contextlib.contextmanager
    def download_log_for_process(
        self, app_id: AppId, process_id: ProcessId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Download entire log file for a stopped process.

        Parameters
        ----------
        app_id : AppId

        process_id : ProcessId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            Ok
        """
        with self._client_wrapper.httpx_client.stream(
            f"logs/v1/{encode_path_param(app_id)}/process/{encode_path_param(process_id)}/download",
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
                    if _response.status_code == 400:
                        raise BadRequestError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                types_api_error_ApiError,
                                parse_obj_as(
                                    type_=types_api_error_ApiError,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 401:
                        raise UnauthorizedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                types_api_error_ApiError,
                                parse_obj_as(
                                    type_=types_api_error_ApiError,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                types_api_error_ApiError,
                                parse_obj_as(
                                    type_=types_api_error_ApiError,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 410:
                        raise GoneError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                types_api_error_ApiError,
                                parse_obj_as(
                                    type_=types_api_error_ApiError,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise core_api_error_ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise core_api_error_ApiError(
                    status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
                )

            yield _stream()

    @contextlib.contextmanager
    def get_logs_for_deployment(
        self,
        app_id: AppId,
        deployment_id: DeploymentId,
        *,
        follow: typing.Optional[LogsFollow] = None,
        tail_lines: typing.Optional[TailLines] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Returns a stream of logs for a [deployment](https://hathora.dev/docs/concepts/hathora-entities#deployment) using `appId` and `deploymentId`.

        Parameters
        ----------
        app_id : AppId

        deployment_id : DeploymentId

        follow : typing.Optional[LogsFollow]

        tail_lines : typing.Optional[TailLines]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            Ok
        """
        with self._client_wrapper.httpx_client.stream(
            f"logs/v1/{encode_path_param(app_id)}/deployment/{encode_path_param(deployment_id)}",
            method="GET",
            params={
                "follow": follow,
                "tailLines": tail_lines,
            },
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
                    if _response.status_code == 401:
                        raise UnauthorizedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                types_api_error_ApiError,
                                parse_obj_as(
                                    type_=types_api_error_ApiError,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                types_api_error_ApiError,
                                parse_obj_as(
                                    type_=types_api_error_ApiError,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise core_api_error_ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise core_api_error_ApiError(
                    status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
                )

            yield _stream()


class AsyncRawLogV1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    @contextlib.asynccontextmanager
    async def get_logs_for_app(
        self,
        app_id: AppId,
        *,
        follow: typing.Optional[LogsFollow] = None,
        tail_lines: typing.Optional[TailLines] = None,
        region: typing.Optional[Region] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Returns a stream of logs for an [application](https://hathora.dev/docs/concepts/hathora-entities#application) using `appId`.

        Parameters
        ----------
        app_id : AppId

        follow : typing.Optional[LogsFollow]

        tail_lines : typing.Optional[TailLines]

        region : typing.Optional[Region]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            Ok
        """
        async with self._client_wrapper.httpx_client.stream(
            f"logs/v1/{encode_path_param(app_id)}/all",
            method="GET",
            params={
                "follow": follow,
                "tailLines": tail_lines,
                "region": region,
            },
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
                    if _response.status_code == 401:
                        raise UnauthorizedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                types_api_error_ApiError,
                                parse_obj_as(
                                    type_=types_api_error_ApiError,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                types_api_error_ApiError,
                                parse_obj_as(
                                    type_=types_api_error_ApiError,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise core_api_error_ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise core_api_error_ApiError(
                    status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
                )

            yield await _stream()

    @contextlib.asynccontextmanager
    async def get_logs_for_process(
        self,
        app_id: AppId,
        process_id: ProcessId,
        *,
        follow: typing.Optional[LogsFollow] = None,
        tail_lines: typing.Optional[TailLines] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Returns a stream of logs for a [process](https://hathora.dev/docs/concepts/hathora-entities#process) using `appId` and `processId`.

        Parameters
        ----------
        app_id : AppId

        process_id : ProcessId

        follow : typing.Optional[LogsFollow]

        tail_lines : typing.Optional[TailLines]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            Ok
        """
        async with self._client_wrapper.httpx_client.stream(
            f"logs/v1/{encode_path_param(app_id)}/process/{encode_path_param(process_id)}",
            method="GET",
            params={
                "follow": follow,
                "tailLines": tail_lines,
            },
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
                    if _response.status_code == 400:
                        raise BadRequestError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                types_api_error_ApiError,
                                parse_obj_as(
                                    type_=types_api_error_ApiError,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 401:
                        raise UnauthorizedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                types_api_error_ApiError,
                                parse_obj_as(
                                    type_=types_api_error_ApiError,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                types_api_error_ApiError,
                                parse_obj_as(
                                    type_=types_api_error_ApiError,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 410:
                        raise GoneError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                types_api_error_ApiError,
                                parse_obj_as(
                                    type_=types_api_error_ApiError,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 500:
                        raise InternalServerError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                types_api_error_ApiError,
                                parse_obj_as(
                                    type_=types_api_error_ApiError,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise core_api_error_ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise core_api_error_ApiError(
                    status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
                )

            yield await _stream()

    @contextlib.asynccontextmanager
    async def download_log_for_process(
        self, app_id: AppId, process_id: ProcessId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Download entire log file for a stopped process.

        Parameters
        ----------
        app_id : AppId

        process_id : ProcessId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            Ok
        """
        async with self._client_wrapper.httpx_client.stream(
            f"logs/v1/{encode_path_param(app_id)}/process/{encode_path_param(process_id)}/download",
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
                    if _response.status_code == 400:
                        raise BadRequestError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                types_api_error_ApiError,
                                parse_obj_as(
                                    type_=types_api_error_ApiError,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 401:
                        raise UnauthorizedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                types_api_error_ApiError,
                                parse_obj_as(
                                    type_=types_api_error_ApiError,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                types_api_error_ApiError,
                                parse_obj_as(
                                    type_=types_api_error_ApiError,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 410:
                        raise GoneError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                types_api_error_ApiError,
                                parse_obj_as(
                                    type_=types_api_error_ApiError,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise core_api_error_ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise core_api_error_ApiError(
                    status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
                )

            yield await _stream()

    @contextlib.asynccontextmanager
    async def get_logs_for_deployment(
        self,
        app_id: AppId,
        deployment_id: DeploymentId,
        *,
        follow: typing.Optional[LogsFollow] = None,
        tail_lines: typing.Optional[TailLines] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Returns a stream of logs for a [deployment](https://hathora.dev/docs/concepts/hathora-entities#deployment) using `appId` and `deploymentId`.

        Parameters
        ----------
        app_id : AppId

        deployment_id : DeploymentId

        follow : typing.Optional[LogsFollow]

        tail_lines : typing.Optional[TailLines]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            Ok
        """
        async with self._client_wrapper.httpx_client.stream(
            f"logs/v1/{encode_path_param(app_id)}/deployment/{encode_path_param(deployment_id)}",
            method="GET",
            params={
                "follow": follow,
                "tailLines": tail_lines,
            },
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
                    if _response.status_code == 401:
                        raise UnauthorizedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                types_api_error_ApiError,
                                parse_obj_as(
                                    type_=types_api_error_ApiError,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                types_api_error_ApiError,
                                parse_obj_as(
                                    type_=types_api_error_ApiError,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise core_api_error_ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise core_api_error_ApiError(
                    status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
                )

            yield await _stream()
