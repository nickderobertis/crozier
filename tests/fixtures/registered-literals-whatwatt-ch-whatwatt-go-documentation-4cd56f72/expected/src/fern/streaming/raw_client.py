

import contextlib
import typing
from json.decoder import JSONDecodeError
from logging import error, warning

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.http_sse._api import EventSource
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as, parse_sse_obj
from ..core.request_options import RequestOptions
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.service_unavailable_error_body import ServiceUnavailableErrorBody
from ..types.unauthorized_error_body import UnauthorizedErrorBody
from pydantic import ValidationError


class RawStreamingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    @contextlib.contextmanager
    def stream_live(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[HttpResponse[typing.Iterator[str]]]:
        """
        Server-Sent Events stream with events named `live` that carry JSON payloads.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[HttpResponse[typing.Iterator[str]]]
            Server-Sent Events stream
        """
        with self._client_wrapper.httpx_client.stream(
            "api/v1/live",
            method="GET",
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[str]]:
                try:
                    if 200 <= _response.status_code < 300:

                        def _iter():
                            _event_source = EventSource(_response)
                            for _sse in _event_source.iter_sse():
                                if _sse.data == None:
                                    return
                                if len(_sse.data) == 0:
                                    continue
                                try:
                                    yield typing.cast(
                                        str,
                                        parse_sse_obj(
                                            sse=_sse,
                                            type_=str,
                                        ),
                                    )
                                except JSONDecodeError as e:
                                    warning(f"Skipping SSE event with invalid JSON: {e}, sse: {_sse!r}")
                                except (TypeError, ValueError, KeyError, AttributeError) as e:
                                    warning(
                                        f"Skipping SSE event due to model construction error: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                                except Exception as e:
                                    error(
                                        f"Unexpected error processing SSE event: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                            return

                        return HttpResponse(response=_response, data=_iter())
                    _response.read()
                    if _response.status_code == 401:
                        raise UnauthorizedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                UnauthorizedErrorBody,
                                parse_obj_as(
                                    type_=UnauthorizedErrorBody,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 503:
                        raise ServiceUnavailableError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ServiceUnavailableErrorBody,
                                parse_obj_as(
                                    type_=ServiceUnavailableErrorBody,
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


class AsyncRawStreamingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    @contextlib.asynccontextmanager
    async def stream_live(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[str]]]:
        """
        Server-Sent Events stream with events named `live` that carry JSON payloads.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[str]]]
            Server-Sent Events stream
        """
        async with self._client_wrapper.httpx_client.stream(
            "api/v1/live",
            method="GET",
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[str]]:
                try:
                    if 200 <= _response.status_code < 300:

                        async def _iter():
                            _event_source = EventSource(_response)
                            async for _sse in _event_source.aiter_sse():
                                if _sse.data == None:
                                    return
                                if len(_sse.data) == 0:
                                    continue
                                try:
                                    yield typing.cast(
                                        str,
                                        parse_sse_obj(
                                            sse=_sse,
                                            type_=str,
                                        ),
                                    )
                                except JSONDecodeError as e:
                                    warning(f"Skipping SSE event with invalid JSON: {e}, sse: {_sse!r}")
                                except (TypeError, ValueError, KeyError, AttributeError) as e:
                                    warning(
                                        f"Skipping SSE event due to model construction error: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                                except Exception as e:
                                    error(
                                        f"Unexpected error processing SSE event: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                            return

                        return AsyncHttpResponse(response=_response, data=_iter())
                    await _response.aread()
                    if _response.status_code == 401:
                        raise UnauthorizedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                UnauthorizedErrorBody,
                                parse_obj_as(
                                    type_=UnauthorizedErrorBody,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 503:
                        raise ServiceUnavailableError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ServiceUnavailableErrorBody,
                                parse_obj_as(
                                    type_=ServiceUnavailableErrorBody,
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
