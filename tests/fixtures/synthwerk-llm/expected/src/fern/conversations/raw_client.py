

import contextlib
import json
import typing
from json.decoder import JSONDecodeError
from logging import warning

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.http_sse._api import EventSource
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.content_too_large_error import ContentTooLargeError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.conversation import Conversation
from ..types.delta_event import DeltaEvent
from ..types.done_event import DoneEvent
from ..types.error_event import ErrorEvent
from ..types.model_alias import ModelAlias
from ..types.problem import Problem
from ..types.stream_event import StreamEvent
from ..types.usage_event import UsageEvent
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawConversationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def llm_create_conversation(
        self, *, model: typing.Optional[ModelAlias] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Conversation]:
        """
        Creates an empty conversation for the caller in the org of the token.

        Parameters
        ----------
        model : typing.Optional[ModelAlias]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Conversation]
            Conversation created.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/conversations",
            method="POST",
            json={
                "model": model,
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
                    Conversation,
                    parse_obj_as(
                        type_=Conversation,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Problem,
                        parse_obj_as(
                            type_=Problem,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Problem,
                        parse_obj_as(
                            type_=Problem,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Problem,
                        parse_obj_as(
                            type_=Problem,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Problem,
                        parse_obj_as(
                            type_=Problem,
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

    def llm_get_conversation(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Conversation]:
        """
        The conversation with its messages, oldest first.
        An unknown id and another owner's id both answer 404 with the same body.

        Parameters
        ----------
        id : str
            Conversation id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Conversation]
            The conversation.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/conversations/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Conversation,
                    parse_obj_as(
                        type_=Conversation,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Problem,
                        parse_obj_as(
                            type_=Problem,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Problem,
                        parse_obj_as(
                            type_=Problem,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Problem,
                        parse_obj_as(
                            type_=Problem,
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
    def llm_send_message(
        self,
        id: str,
        *,
        content: str,
        model: typing.Optional[ModelAlias] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[StreamEvent]]]:
        """
        Stores the user message and streams the assistant answer as Server-Sent Events.
        - Refusals before the first byte answer with a status code and `application/problem+json`.
        - After the first byte the status stays 200. A failure is an `error` event, then the stream ends.
        - Order of events: zero or more `delta`, then `usage`, then `done`. Or an `error` event at any point.
        - Cancel: the client closes the connection. The server stops the model call and keeps the partial answer.
        - Headers: `Cache-Control: no-store`, `X-Accel-Buffering: no`. A comment line (`: ping`) every 15 s keeps the connection open.

        Parameters
        ----------
        id : str
            Conversation id.

        content : str
            The user message. Plain text. Above the server limit the answer is 413.

        model : typing.Optional[ModelAlias]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[HttpResponse[typing.Iterator[StreamEvent]]]
            The answer as a `text/event-stream`. Each frame is one `StreamEvent`:
            the SSE `event:` field holds `event`, the `data:` field holds `data` as one line of JSON,
            and the `id:` field holds `<message_id>:<sequence>`. On the wire:

            ```text
            id: 0199f3b0-1a2c-7c3d-8e4f-5a6b7c8d9e10:1
            event: delta
            data: {"text":"Pulse reads "}

            id: 0199f3b0-1a2c-7c3d-8e4f-5a6b7c8d9e10:2
            event: delta
            data: {"text":"/readyz of every service."}

            id: 0199f3b0-1a2c-7c3d-8e4f-5a6b7c8d9e10:3
            event: usage
            data: {"input_tokens":412,"output_tokens":9,"model":"default"}

            id: 0199f3b0-1a2c-7c3d-8e4f-5a6b7c8d9e10:4
            event: done
            data: {"message_id":"0199f3b0-1a2c-7c3d-8e4f-5a6b7c8d9e10","finish_reason":"stop"}
            ```
        """
        with self._client_wrapper.httpx_client.stream(
            f"v1/conversations/{encode_path_param(id)}/messages",
            method="POST",
            json={
                "content": content,
                "model": model,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[StreamEvent]]:
                try:
                    if 200 <= _response.status_code < 300:

                        def _iter():
                            _event_source = EventSource(_response)
                            for _sse in _event_source.iter_sse():
                                if _sse.data == None:
                                    return
                                if len(_sse.data) == 0:
                                    continue
                                if _sse.event == "delta":
                                    try:
                                        yield typing.cast(
                                            DeltaEvent,
                                            parse_obj_as(
                                                type_=DeltaEvent,
                                                object_={"data": json.loads(_sse.data)},
                                            ),
                                        )
                                    except Exception as e:
                                        warning(f"Failed to parse SSE event 'delta': {e}, sse: {_sse!r}")
                                elif _sse.event == "usage":
                                    try:
                                        yield typing.cast(
                                            UsageEvent,
                                            parse_obj_as(
                                                type_=UsageEvent,
                                                object_={"data": json.loads(_sse.data)},
                                            ),
                                        )
                                    except Exception as e:
                                        warning(f"Failed to parse SSE event 'usage': {e}, sse: {_sse!r}")
                                elif _sse.event == "done":
                                    try:
                                        yield typing.cast(
                                            DoneEvent,
                                            parse_obj_as(
                                                type_=DoneEvent,
                                                object_={"data": json.loads(_sse.data)},
                                            ),
                                        )
                                    except Exception as e:
                                        warning(f"Failed to parse SSE event 'done': {e}, sse: {_sse!r}")
                                elif _sse.event == "error":
                                    try:
                                        yield typing.cast(
                                            ErrorEvent,
                                            parse_obj_as(
                                                type_=ErrorEvent,
                                                object_={"data": json.loads(_sse.data)},
                                            ),
                                        )
                                    except Exception as e:
                                        warning(f"Failed to parse SSE event 'error': {e}, sse: {_sse!r}")
                            return

                        return HttpResponse(response=_response, data=_iter())
                    _response.read()
                    if _response.status_code == 400:
                        raise BadRequestError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Problem,
                                parse_obj_as(
                                    type_=Problem,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 401:
                        raise UnauthorizedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Problem,
                                parse_obj_as(
                                    type_=Problem,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 403:
                        raise ForbiddenError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Problem,
                                parse_obj_as(
                                    type_=Problem,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Problem,
                                parse_obj_as(
                                    type_=Problem,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 413:
                        raise ContentTooLargeError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Problem,
                                parse_obj_as(
                                    type_=Problem,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 429:
                        raise TooManyRequestsError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Problem,
                                parse_obj_as(
                                    type_=Problem,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 503:
                        raise ServiceUnavailableError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Problem,
                                parse_obj_as(
                                    type_=Problem,
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


class AsyncRawConversationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def llm_create_conversation(
        self, *, model: typing.Optional[ModelAlias] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Conversation]:
        """
        Creates an empty conversation for the caller in the org of the token.

        Parameters
        ----------
        model : typing.Optional[ModelAlias]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Conversation]
            Conversation created.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/conversations",
            method="POST",
            json={
                "model": model,
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
                    Conversation,
                    parse_obj_as(
                        type_=Conversation,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Problem,
                        parse_obj_as(
                            type_=Problem,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Problem,
                        parse_obj_as(
                            type_=Problem,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Problem,
                        parse_obj_as(
                            type_=Problem,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Problem,
                        parse_obj_as(
                            type_=Problem,
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

    async def llm_get_conversation(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Conversation]:
        """
        The conversation with its messages, oldest first.
        An unknown id and another owner's id both answer 404 with the same body.

        Parameters
        ----------
        id : str
            Conversation id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Conversation]
            The conversation.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/conversations/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Conversation,
                    parse_obj_as(
                        type_=Conversation,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Problem,
                        parse_obj_as(
                            type_=Problem,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Problem,
                        parse_obj_as(
                            type_=Problem,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Problem,
                        parse_obj_as(
                            type_=Problem,
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
    async def llm_send_message(
        self,
        id: str,
        *,
        content: str,
        model: typing.Optional[ModelAlias] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[StreamEvent]]]:
        """
        Stores the user message and streams the assistant answer as Server-Sent Events.
        - Refusals before the first byte answer with a status code and `application/problem+json`.
        - After the first byte the status stays 200. A failure is an `error` event, then the stream ends.
        - Order of events: zero or more `delta`, then `usage`, then `done`. Or an `error` event at any point.
        - Cancel: the client closes the connection. The server stops the model call and keeps the partial answer.
        - Headers: `Cache-Control: no-store`, `X-Accel-Buffering: no`. A comment line (`: ping`) every 15 s keeps the connection open.

        Parameters
        ----------
        id : str
            Conversation id.

        content : str
            The user message. Plain text. Above the server limit the answer is 413.

        model : typing.Optional[ModelAlias]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[StreamEvent]]]
            The answer as a `text/event-stream`. Each frame is one `StreamEvent`:
            the SSE `event:` field holds `event`, the `data:` field holds `data` as one line of JSON,
            and the `id:` field holds `<message_id>:<sequence>`. On the wire:

            ```text
            id: 0199f3b0-1a2c-7c3d-8e4f-5a6b7c8d9e10:1
            event: delta
            data: {"text":"Pulse reads "}

            id: 0199f3b0-1a2c-7c3d-8e4f-5a6b7c8d9e10:2
            event: delta
            data: {"text":"/readyz of every service."}

            id: 0199f3b0-1a2c-7c3d-8e4f-5a6b7c8d9e10:3
            event: usage
            data: {"input_tokens":412,"output_tokens":9,"model":"default"}

            id: 0199f3b0-1a2c-7c3d-8e4f-5a6b7c8d9e10:4
            event: done
            data: {"message_id":"0199f3b0-1a2c-7c3d-8e4f-5a6b7c8d9e10","finish_reason":"stop"}
            ```
        """
        async with self._client_wrapper.httpx_client.stream(
            f"v1/conversations/{encode_path_param(id)}/messages",
            method="POST",
            json={
                "content": content,
                "model": model,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[StreamEvent]]:
                try:
                    if 200 <= _response.status_code < 300:

                        async def _iter():
                            _event_source = EventSource(_response)
                            async for _sse in _event_source.aiter_sse():
                                if _sse.data == None:
                                    return
                                if len(_sse.data) == 0:
                                    continue
                                if _sse.event == "delta":
                                    try:
                                        yield typing.cast(
                                            DeltaEvent,
                                            parse_obj_as(
                                                type_=DeltaEvent,
                                                object_={"data": json.loads(_sse.data)},
                                            ),
                                        )
                                    except Exception as e:
                                        warning(f"Failed to parse SSE event 'delta': {e}, sse: {_sse!r}")
                                elif _sse.event == "usage":
                                    try:
                                        yield typing.cast(
                                            UsageEvent,
                                            parse_obj_as(
                                                type_=UsageEvent,
                                                object_={"data": json.loads(_sse.data)},
                                            ),
                                        )
                                    except Exception as e:
                                        warning(f"Failed to parse SSE event 'usage': {e}, sse: {_sse!r}")
                                elif _sse.event == "done":
                                    try:
                                        yield typing.cast(
                                            DoneEvent,
                                            parse_obj_as(
                                                type_=DoneEvent,
                                                object_={"data": json.loads(_sse.data)},
                                            ),
                                        )
                                    except Exception as e:
                                        warning(f"Failed to parse SSE event 'done': {e}, sse: {_sse!r}")
                                elif _sse.event == "error":
                                    try:
                                        yield typing.cast(
                                            ErrorEvent,
                                            parse_obj_as(
                                                type_=ErrorEvent,
                                                object_={"data": json.loads(_sse.data)},
                                            ),
                                        )
                                    except Exception as e:
                                        warning(f"Failed to parse SSE event 'error': {e}, sse: {_sse!r}")
                            return

                        return AsyncHttpResponse(response=_response, data=_iter())
                    await _response.aread()
                    if _response.status_code == 400:
                        raise BadRequestError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Problem,
                                parse_obj_as(
                                    type_=Problem,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 401:
                        raise UnauthorizedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Problem,
                                parse_obj_as(
                                    type_=Problem,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 403:
                        raise ForbiddenError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Problem,
                                parse_obj_as(
                                    type_=Problem,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Problem,
                                parse_obj_as(
                                    type_=Problem,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 413:
                        raise ContentTooLargeError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Problem,
                                parse_obj_as(
                                    type_=Problem,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 429:
                        raise TooManyRequestsError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Problem,
                                parse_obj_as(
                                    type_=Problem,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 503:
                        raise ServiceUnavailableError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Problem,
                                parse_obj_as(
                                    type_=Problem,
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
