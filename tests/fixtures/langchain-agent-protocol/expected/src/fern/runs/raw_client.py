

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
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.conflict_error import ConflictError
from ..errors.not_found_error import NotFoundError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.error_response import ErrorResponse
from ..types.message import Message
from ..types.run_create_config import RunCreateConfig
from ..types.run_create_if_not_exists import RunCreateIfNotExists
from ..types.run_create_input import RunCreateInput
from ..types.run_create_on_completion import RunCreateOnCompletion
from ..types.run_create_on_disconnect import RunCreateOnDisconnect
from ..types.run_stream_stream_mode import RunStreamStreamMode
from ..types.run_wait_response import RunWaitResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawRunsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    @contextlib.contextmanager
    def create_and_stream_run(
        self,
        *,
        stream_mode: typing.Optional[RunStreamStreamMode] = OMIT,
        thread_id: typing.Optional[str] = OMIT,
        agent_id: typing.Optional[str] = OMIT,
        input: typing.Optional[RunCreateInput] = OMIT,
        messages: typing.Optional[typing.Sequence[Message]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        config: typing.Optional[RunCreateConfig] = OMIT,
        webhook: typing.Optional[str] = OMIT,
        on_completion: typing.Optional[RunCreateOnCompletion] = OMIT,
        on_disconnect: typing.Optional[RunCreateOnDisconnect] = OMIT,
        if_not_exists: typing.Optional[RunCreateIfNotExists] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[str]]]:
        """
        Create a run in a new thread, stream the output.

        Parameters
        ----------
        stream_mode : typing.Optional[RunStreamStreamMode]
            The stream mode(s) to use.

        thread_id : typing.Optional[str]
            The ID of the thread to run. If not provided, creates a stateless run. 'thread_id' is ignored unless Threads stage is implemented.

        agent_id : typing.Optional[str]
            The agent ID to run. If not provided will use the default agent for this service. 'agent_id' is ignored unless Agents stage is implemented.

        input : typing.Optional[RunCreateInput]
            The input to the agent.

        messages : typing.Optional[typing.Sequence[Message]]
            The messages to pass an input to the agent.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to assign to the run.

        config : typing.Optional[RunCreateConfig]
            The configuration for the agent.

        webhook : typing.Optional[str]
            Webhook to call after run finishes.

        on_completion : typing.Optional[RunCreateOnCompletion]
            Whether to delete or keep the thread when run completes. Must be one of 'delete' or 'keep'. Defaults to 'delete' when thread_id not provided, otherwise 'keep'.

        on_disconnect : typing.Optional[RunCreateOnDisconnect]
            The disconnect mode to use. Must be one of 'cancel' or 'continue'.

        if_not_exists : typing.Optional[RunCreateIfNotExists]
            How to handle missing thread. Must be either 'reject' (raise error if missing), or 'create' (create new thread).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[HttpResponse[typing.Iterator[str]]]
            Success
        """
        with self._client_wrapper.httpx_client.stream(
            "runs/stream",
            method="POST",
            json={
                "stream_mode": convert_and_respect_annotation_metadata(
                    object_=stream_mode, annotation=RunStreamStreamMode, direction="write"
                ),
                "thread_id": thread_id,
                "agent_id": agent_id,
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=typing.Optional[RunCreateInput], direction="write"
                ),
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages, annotation=typing.Sequence[Message], direction="write"
                ),
                "metadata": metadata,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=RunCreateConfig, direction="write"
                ),
                "webhook": webhook,
                "on_completion": on_completion,
                "on_disconnect": on_disconnect,
                "if_not_exists": if_not_exists,
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
                    if _response.status_code == 409:
                        raise ConflictError(
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

    def create_and_wait_run(
        self,
        *,
        thread_id: typing.Optional[str] = OMIT,
        agent_id: typing.Optional[str] = OMIT,
        input: typing.Optional[RunCreateInput] = OMIT,
        messages: typing.Optional[typing.Sequence[Message]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        config: typing.Optional[RunCreateConfig] = OMIT,
        webhook: typing.Optional[str] = OMIT,
        on_completion: typing.Optional[RunCreateOnCompletion] = OMIT,
        on_disconnect: typing.Optional[RunCreateOnDisconnect] = OMIT,
        if_not_exists: typing.Optional[RunCreateIfNotExists] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RunWaitResponse]:
        """
        Create a run in a new thread. Wait for the final output and then return it.

        Parameters
        ----------
        thread_id : typing.Optional[str]
            The ID of the thread to run. If not provided, creates a stateless run. 'thread_id' is ignored unless Threads stage is implemented.

        agent_id : typing.Optional[str]
            The agent ID to run. If not provided will use the default agent for this service. 'agent_id' is ignored unless Agents stage is implemented.

        input : typing.Optional[RunCreateInput]
            The input to the agent.

        messages : typing.Optional[typing.Sequence[Message]]
            The messages to pass an input to the agent.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to assign to the run.

        config : typing.Optional[RunCreateConfig]
            The configuration for the agent.

        webhook : typing.Optional[str]
            Webhook to call after run finishes.

        on_completion : typing.Optional[RunCreateOnCompletion]
            Whether to delete or keep the thread when run completes. Must be one of 'delete' or 'keep'. Defaults to 'delete' when thread_id not provided, otherwise 'keep'.

        on_disconnect : typing.Optional[RunCreateOnDisconnect]
            The disconnect mode to use. Must be one of 'cancel' or 'continue'.

        if_not_exists : typing.Optional[RunCreateIfNotExists]
            How to handle missing thread. Must be either 'reject' (raise error if missing), or 'create' (create new thread).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RunWaitResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "runs/wait",
            method="POST",
            json={
                "thread_id": thread_id,
                "agent_id": agent_id,
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=typing.Optional[RunCreateInput], direction="write"
                ),
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages, annotation=typing.Sequence[Message], direction="write"
                ),
                "metadata": metadata,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=RunCreateConfig, direction="write"
                ),
                "webhook": webhook,
                "on_completion": on_completion,
                "on_disconnect": on_disconnect,
                "if_not_exists": if_not_exists,
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
                    RunWaitResponse,
                    parse_obj_as(
                        type_=RunWaitResponse,
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
            if _response.status_code == 409:
                raise ConflictError(
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


class AsyncRawRunsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    @contextlib.asynccontextmanager
    async def create_and_stream_run(
        self,
        *,
        stream_mode: typing.Optional[RunStreamStreamMode] = OMIT,
        thread_id: typing.Optional[str] = OMIT,
        agent_id: typing.Optional[str] = OMIT,
        input: typing.Optional[RunCreateInput] = OMIT,
        messages: typing.Optional[typing.Sequence[Message]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        config: typing.Optional[RunCreateConfig] = OMIT,
        webhook: typing.Optional[str] = OMIT,
        on_completion: typing.Optional[RunCreateOnCompletion] = OMIT,
        on_disconnect: typing.Optional[RunCreateOnDisconnect] = OMIT,
        if_not_exists: typing.Optional[RunCreateIfNotExists] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[str]]]:
        """
        Create a run in a new thread, stream the output.

        Parameters
        ----------
        stream_mode : typing.Optional[RunStreamStreamMode]
            The stream mode(s) to use.

        thread_id : typing.Optional[str]
            The ID of the thread to run. If not provided, creates a stateless run. 'thread_id' is ignored unless Threads stage is implemented.

        agent_id : typing.Optional[str]
            The agent ID to run. If not provided will use the default agent for this service. 'agent_id' is ignored unless Agents stage is implemented.

        input : typing.Optional[RunCreateInput]
            The input to the agent.

        messages : typing.Optional[typing.Sequence[Message]]
            The messages to pass an input to the agent.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to assign to the run.

        config : typing.Optional[RunCreateConfig]
            The configuration for the agent.

        webhook : typing.Optional[str]
            Webhook to call after run finishes.

        on_completion : typing.Optional[RunCreateOnCompletion]
            Whether to delete or keep the thread when run completes. Must be one of 'delete' or 'keep'. Defaults to 'delete' when thread_id not provided, otherwise 'keep'.

        on_disconnect : typing.Optional[RunCreateOnDisconnect]
            The disconnect mode to use. Must be one of 'cancel' or 'continue'.

        if_not_exists : typing.Optional[RunCreateIfNotExists]
            How to handle missing thread. Must be either 'reject' (raise error if missing), or 'create' (create new thread).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[str]]]
            Success
        """
        async with self._client_wrapper.httpx_client.stream(
            "runs/stream",
            method="POST",
            json={
                "stream_mode": convert_and_respect_annotation_metadata(
                    object_=stream_mode, annotation=RunStreamStreamMode, direction="write"
                ),
                "thread_id": thread_id,
                "agent_id": agent_id,
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=typing.Optional[RunCreateInput], direction="write"
                ),
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages, annotation=typing.Sequence[Message], direction="write"
                ),
                "metadata": metadata,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=RunCreateConfig, direction="write"
                ),
                "webhook": webhook,
                "on_completion": on_completion,
                "on_disconnect": on_disconnect,
                "if_not_exists": if_not_exists,
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
                    if _response.status_code == 409:
                        raise ConflictError(
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

    async def create_and_wait_run(
        self,
        *,
        thread_id: typing.Optional[str] = OMIT,
        agent_id: typing.Optional[str] = OMIT,
        input: typing.Optional[RunCreateInput] = OMIT,
        messages: typing.Optional[typing.Sequence[Message]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        config: typing.Optional[RunCreateConfig] = OMIT,
        webhook: typing.Optional[str] = OMIT,
        on_completion: typing.Optional[RunCreateOnCompletion] = OMIT,
        on_disconnect: typing.Optional[RunCreateOnDisconnect] = OMIT,
        if_not_exists: typing.Optional[RunCreateIfNotExists] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RunWaitResponse]:
        """
        Create a run in a new thread. Wait for the final output and then return it.

        Parameters
        ----------
        thread_id : typing.Optional[str]
            The ID of the thread to run. If not provided, creates a stateless run. 'thread_id' is ignored unless Threads stage is implemented.

        agent_id : typing.Optional[str]
            The agent ID to run. If not provided will use the default agent for this service. 'agent_id' is ignored unless Agents stage is implemented.

        input : typing.Optional[RunCreateInput]
            The input to the agent.

        messages : typing.Optional[typing.Sequence[Message]]
            The messages to pass an input to the agent.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to assign to the run.

        config : typing.Optional[RunCreateConfig]
            The configuration for the agent.

        webhook : typing.Optional[str]
            Webhook to call after run finishes.

        on_completion : typing.Optional[RunCreateOnCompletion]
            Whether to delete or keep the thread when run completes. Must be one of 'delete' or 'keep'. Defaults to 'delete' when thread_id not provided, otherwise 'keep'.

        on_disconnect : typing.Optional[RunCreateOnDisconnect]
            The disconnect mode to use. Must be one of 'cancel' or 'continue'.

        if_not_exists : typing.Optional[RunCreateIfNotExists]
            How to handle missing thread. Must be either 'reject' (raise error if missing), or 'create' (create new thread).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RunWaitResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "runs/wait",
            method="POST",
            json={
                "thread_id": thread_id,
                "agent_id": agent_id,
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=typing.Optional[RunCreateInput], direction="write"
                ),
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages, annotation=typing.Sequence[Message], direction="write"
                ),
                "metadata": metadata,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=RunCreateConfig, direction="write"
                ),
                "webhook": webhook,
                "on_completion": on_completion,
                "on_disconnect": on_disconnect,
                "if_not_exists": if_not_exists,
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
                    RunWaitResponse,
                    parse_obj_as(
                        type_=RunWaitResponse,
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
            if _response.status_code == 409:
                raise ConflictError(
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
