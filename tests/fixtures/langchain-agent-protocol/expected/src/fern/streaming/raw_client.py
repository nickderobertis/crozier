

import contextlib
import typing
from json.decoder import JSONDecodeError
from logging import error, warning

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.http_sse._api import EventSource
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as, parse_sse_obj
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.not_found_error import NotFoundError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.error_response import ErrorResponse
from ..types.streaming_channel import StreamingChannel
from ..types.streaming_command_response import StreamingCommandResponse
from ..types.streaming_namespace import StreamingNamespace
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawStreamingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def open_thread_websocket_stream(
        self, thread_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Upgrade to a WebSocket connection for a thread. After the connection is upgraded, clients send streaming protocol commands in-band and receive command responses plus unsolicited events on the same connection. Use `subscription.subscribe`, `subscription.unsubscribe`, and `subscription.reconnect` to manage event filters on the WebSocket.

        Parameters
        ----------
        thread_id : str
            The ID of the thread to open over WebSocket.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/stream",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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
    def open_thread_sse_stream(
        self,
        thread_id: str,
        *,
        channels: typing.Sequence[StreamingChannel],
        namespaces: typing.Optional[typing.Sequence[StreamingNamespace]] = OMIT,
        depth: typing.Optional[int] = OMIT,
        since: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[str]]]:
        """
        Open a connection-scoped Server-Sent Events stream for a thread. The request body selects channels, namespace prefixes, optional namespace depth, and an optional sequence number to replay buffered events after. Closing the HTTP connection unsubscribes from this stream.

        Parameters
        ----------
        thread_id : str
            The ID of the thread whose events should be streamed.

        channels : typing.Sequence[StreamingChannel]
            Channels to include in this event stream.

        namespaces : typing.Optional[typing.Sequence[StreamingNamespace]]
            Namespace prefixes to include. Omit to receive matching events from all namespaces.

        depth : typing.Optional[int]
            Maximum depth below each namespace prefix.

        since : typing.Optional[int]
            Replay buffered matching events after this monotonic sequence number, then switch to live delivery.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[HttpResponse[typing.Iterator[str]]]
            A filtered stream of protocol events in SSE format.
        """
        with self._client_wrapper.httpx_client.stream(
            f"threads/{encode_path_param(thread_id)}/stream",
            method="POST",
            json={
                "channels": convert_and_respect_annotation_metadata(
                    object_=channels, annotation=typing.Sequence[StreamingChannel], direction="write"
                ),
                "namespaces": namespaces,
                "depth": depth,
                "since": since,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[str]]:
                try:
                    if 200 <= _response.status_code < 300:

                        def _iter():
                            _event_source = EventSource(_response)
                            for _sse in _event_source.iter_sse():
                                if _sse.data == None:
                                    return
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
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorResponse,
                                parse_obj_as(
                                    type_=ErrorResponse,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 422:
                        raise UnprocessableEntityError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorResponse,
                                parse_obj_as(
                                    type_=ErrorResponse,
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

    def send_thread_streaming_command(
        self,
        thread_id: str,
        *,
        id: int,
        method: str,
        params: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[StreamingCommandResponse]:
        """
        Send a streaming protocol command to a thread over HTTP. This endpoint is the request/response companion to the SSE event stream and supports commands such as `run.start`, `input.respond`, `input.inject`, `state.get`, `state.listCheckpoints`, and `state.fork`.

        Parameters
        ----------
        thread_id : str
            The ID of the thread that should receive the command.

        id : int
            Client-assigned command ID used to correlate the command response.

        method : str
            Streaming protocol command method, such as `run.start`, `subscription.subscribe`, `input.respond`, or `state.get`.

        params : typing.Optional[typing.Dict[str, typing.Any]]
            Command parameters. Shape depends on the command method.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StreamingCommandResponse]
            Command response.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/commands",
            method="POST",
            json={
                "id": id,
                "method": method,
                "params": params,
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
                    StreamingCommandResponse,
                    parse_obj_as(
                        type_=StreamingCommandResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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


class AsyncRawStreamingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def open_thread_websocket_stream(
        self, thread_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Upgrade to a WebSocket connection for a thread. After the connection is upgraded, clients send streaming protocol commands in-band and receive command responses plus unsolicited events on the same connection. Use `subscription.subscribe`, `subscription.unsubscribe`, and `subscription.reconnect` to manage event filters on the WebSocket.

        Parameters
        ----------
        thread_id : str
            The ID of the thread to open over WebSocket.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/stream",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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
    async def open_thread_sse_stream(
        self,
        thread_id: str,
        *,
        channels: typing.Sequence[StreamingChannel],
        namespaces: typing.Optional[typing.Sequence[StreamingNamespace]] = OMIT,
        depth: typing.Optional[int] = OMIT,
        since: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[str]]]:
        """
        Open a connection-scoped Server-Sent Events stream for a thread. The request body selects channels, namespace prefixes, optional namespace depth, and an optional sequence number to replay buffered events after. Closing the HTTP connection unsubscribes from this stream.

        Parameters
        ----------
        thread_id : str
            The ID of the thread whose events should be streamed.

        channels : typing.Sequence[StreamingChannel]
            Channels to include in this event stream.

        namespaces : typing.Optional[typing.Sequence[StreamingNamespace]]
            Namespace prefixes to include. Omit to receive matching events from all namespaces.

        depth : typing.Optional[int]
            Maximum depth below each namespace prefix.

        since : typing.Optional[int]
            Replay buffered matching events after this monotonic sequence number, then switch to live delivery.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[str]]]
            A filtered stream of protocol events in SSE format.
        """
        async with self._client_wrapper.httpx_client.stream(
            f"threads/{encode_path_param(thread_id)}/stream",
            method="POST",
            json={
                "channels": convert_and_respect_annotation_metadata(
                    object_=channels, annotation=typing.Sequence[StreamingChannel], direction="write"
                ),
                "namespaces": namespaces,
                "depth": depth,
                "since": since,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[str]]:
                try:
                    if 200 <= _response.status_code < 300:

                        async def _iter():
                            _event_source = EventSource(_response)
                            async for _sse in _event_source.aiter_sse():
                                if _sse.data == None:
                                    return
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
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorResponse,
                                parse_obj_as(
                                    type_=ErrorResponse,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 422:
                        raise UnprocessableEntityError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ErrorResponse,
                                parse_obj_as(
                                    type_=ErrorResponse,
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

    async def send_thread_streaming_command(
        self,
        thread_id: str,
        *,
        id: int,
        method: str,
        params: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[StreamingCommandResponse]:
        """
        Send a streaming protocol command to a thread over HTTP. This endpoint is the request/response companion to the SSE event stream and supports commands such as `run.start`, `input.respond`, `input.inject`, `state.get`, `state.listCheckpoints`, and `state.fork`.

        Parameters
        ----------
        thread_id : str
            The ID of the thread that should receive the command.

        id : int
            Client-assigned command ID used to correlate the command response.

        method : str
            Streaming protocol command method, such as `run.start`, `subscription.subscribe`, `input.respond`, or `state.get`.

        params : typing.Optional[typing.Dict[str, typing.Any]]
            Command parameters. Shape depends on the command method.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StreamingCommandResponse]
            Command response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/commands",
            method="POST",
            json={
                "id": id,
                "method": method,
                "params": params,
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
                    StreamingCommandResponse,
                    parse_obj_as(
                        type_=StreamingCommandResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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
