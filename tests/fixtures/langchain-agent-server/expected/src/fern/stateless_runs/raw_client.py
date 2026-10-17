

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
from ..types.command import Command
from ..types.error_response import ErrorResponse
from ..types.run_batch_create import RunBatchCreate
from ..types.run_create_stateless_config import RunCreateStatelessConfig
from ..types.run_create_stateless_durability import RunCreateStatelessDurability
from ..types.run_create_stateless_input import RunCreateStatelessInput
from ..types.run_create_stateless_on_completion import RunCreateStatelessOnCompletion
from ..types.run_create_stateless_stream_mode import RunCreateStatelessStreamMode
from ..types.run_create_streaming_stateless_on_disconnect import RunCreateStreamingStatelessOnDisconnect
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawStatelessRunsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    @contextlib.contextmanager
    def stream_run_stateless(
        self,
        *,
        assistant_id: str,
        on_disconnect: typing.Optional[RunCreateStreamingStatelessOnDisconnect] = OMIT,
        input: typing.Optional[RunCreateStatelessInput] = OMIT,
        command: typing.Optional[Command] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        config: typing.Optional[RunCreateStatelessConfig] = OMIT,
        context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        webhook: typing.Optional[str] = OMIT,
        stream_mode: typing.Optional[RunCreateStatelessStreamMode] = OMIT,
        feedback_keys: typing.Optional[typing.Sequence[str]] = OMIT,
        stream_subgraphs: typing.Optional[bool] = OMIT,
        stream_resumable: typing.Optional[bool] = OMIT,
        on_completion: typing.Optional[RunCreateStatelessOnCompletion] = OMIT,
        after_seconds: typing.Optional[float] = OMIT,
        checkpoint_during: typing.Optional[bool] = OMIT,
        durability: typing.Optional[RunCreateStatelessDurability] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[str]]]:
        """
        Create a run and stream the output.

        Parameters
        ----------
        assistant_id : str

        on_disconnect : typing.Optional[RunCreateStreamingStatelessOnDisconnect]
            The disconnect mode to use. Must be one of 'cancel' or 'continue'.

        input : typing.Optional[RunCreateStatelessInput]
            The input to the graph.

        command : typing.Optional[Command]
            The input to the graph.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to assign to the run.

        config : typing.Optional[RunCreateStatelessConfig]
            The configuration for the assistant.

        context : typing.Optional[typing.Dict[str, typing.Any]]
            Static context added to the assistant.

        webhook : typing.Optional[str]
            Webhook to call after LangGraph API call is done.

        stream_mode : typing.Optional[RunCreateStatelessStreamMode]
            The stream mode(s) to use.

        feedback_keys : typing.Optional[typing.Sequence[str]]
            Generate pre-signed URLs for assigning feedback keys to the run.

            For each key specified, a unique URL will be generated that can be called to assign the feedback key to the run. See [LangSmith Feedback](https://docs.langchain.com/langsmith/observability-concepts#feedback) for more details.

        stream_subgraphs : typing.Optional[bool]
            Whether to stream output from subgraphs.

        stream_resumable : typing.Optional[bool]
            Whether to persist the stream chunks in order to resume the stream later.

        on_completion : typing.Optional[RunCreateStatelessOnCompletion]
            Whether to delete or keep the thread created for a stateless run. Must be one of 'delete' or 'keep'.

        after_seconds : typing.Optional[float]
            The number of seconds to wait before starting the run. Use to schedule future runs.

        checkpoint_during : typing.Optional[bool]
            Whether to checkpoint during the run.

            Deprecated. Use `durability` instead to control checkpoint persistence behavior during the run.

        durability : typing.Optional[RunCreateStatelessDurability]
            Durability level for the run. Must be one of `sync`, `async`, or `exit`. See [durability modes](https://docs.langchain.com/oss/python/langgraph/durable-execution#durability-modes) for more details.

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
                "on_disconnect": on_disconnect,
                "assistant_id": assistant_id,
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=typing.Optional[RunCreateStatelessInput], direction="write"
                ),
                "command": convert_and_respect_annotation_metadata(
                    object_=command, annotation=typing.Optional[Command], direction="write"
                ),
                "metadata": metadata,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=RunCreateStatelessConfig, direction="write"
                ),
                "context": context,
                "webhook": webhook,
                "stream_mode": convert_and_respect_annotation_metadata(
                    object_=stream_mode, annotation=RunCreateStatelessStreamMode, direction="write"
                ),
                "feedback_keys": feedback_keys,
                "stream_subgraphs": stream_subgraphs,
                "stream_resumable": stream_resumable,
                "on_completion": on_completion,
                "after_seconds": after_seconds,
                "checkpoint_during": checkpoint_during,
                "durability": durability,
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
                                typing.Any,
                                parse_obj_as(
                                    type_=typing.Any,
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

    def wait_run_stateless(
        self,
        *,
        assistant_id: str,
        on_disconnect: typing.Optional[RunCreateStreamingStatelessOnDisconnect] = OMIT,
        input: typing.Optional[RunCreateStatelessInput] = OMIT,
        command: typing.Optional[Command] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        config: typing.Optional[RunCreateStatelessConfig] = OMIT,
        context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        webhook: typing.Optional[str] = OMIT,
        stream_mode: typing.Optional[RunCreateStatelessStreamMode] = OMIT,
        feedback_keys: typing.Optional[typing.Sequence[str]] = OMIT,
        stream_subgraphs: typing.Optional[bool] = OMIT,
        stream_resumable: typing.Optional[bool] = OMIT,
        on_completion: typing.Optional[RunCreateStatelessOnCompletion] = OMIT,
        after_seconds: typing.Optional[float] = OMIT,
        checkpoint_during: typing.Optional[bool] = OMIT,
        durability: typing.Optional[RunCreateStatelessDurability] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Create a run, wait for the final output and then return it.

        Parameters
        ----------
        assistant_id : str

        on_disconnect : typing.Optional[RunCreateStreamingStatelessOnDisconnect]
            The disconnect mode to use. Must be one of 'cancel' or 'continue'.

        input : typing.Optional[RunCreateStatelessInput]
            The input to the graph.

        command : typing.Optional[Command]
            The input to the graph.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to assign to the run.

        config : typing.Optional[RunCreateStatelessConfig]
            The configuration for the assistant.

        context : typing.Optional[typing.Dict[str, typing.Any]]
            Static context added to the assistant.

        webhook : typing.Optional[str]
            Webhook to call after LangGraph API call is done.

        stream_mode : typing.Optional[RunCreateStatelessStreamMode]
            The stream mode(s) to use.

        feedback_keys : typing.Optional[typing.Sequence[str]]
            Generate pre-signed URLs for assigning feedback keys to the run.

            For each key specified, a unique URL will be generated that can be called to assign the feedback key to the run. See [LangSmith Feedback](https://docs.langchain.com/langsmith/observability-concepts#feedback) for more details.

        stream_subgraphs : typing.Optional[bool]
            Whether to stream output from subgraphs.

        stream_resumable : typing.Optional[bool]
            Whether to persist the stream chunks in order to resume the stream later.

        on_completion : typing.Optional[RunCreateStatelessOnCompletion]
            Whether to delete or keep the thread created for a stateless run. Must be one of 'delete' or 'keep'.

        after_seconds : typing.Optional[float]
            The number of seconds to wait before starting the run. Use to schedule future runs.

        checkpoint_during : typing.Optional[bool]
            Whether to checkpoint during the run.

            Deprecated. Use `durability` instead to control checkpoint persistence behavior during the run.

        durability : typing.Optional[RunCreateStatelessDurability]
            Durability level for the run. Must be one of `sync`, `async`, or `exit`. See [durability modes](https://docs.langchain.com/oss/python/langgraph/durable-execution#durability-modes) for more details.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "runs/wait",
            method="POST",
            json={
                "on_disconnect": on_disconnect,
                "assistant_id": assistant_id,
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=typing.Optional[RunCreateStatelessInput], direction="write"
                ),
                "command": convert_and_respect_annotation_metadata(
                    object_=command, annotation=typing.Optional[Command], direction="write"
                ),
                "metadata": metadata,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=RunCreateStatelessConfig, direction="write"
                ),
                "context": context,
                "webhook": webhook,
                "stream_mode": convert_and_respect_annotation_metadata(
                    object_=stream_mode, annotation=RunCreateStatelessStreamMode, direction="write"
                ),
                "feedback_keys": feedback_keys,
                "stream_subgraphs": stream_subgraphs,
                "stream_resumable": stream_resumable,
                "on_completion": on_completion,
                "after_seconds": after_seconds,
                "checkpoint_during": checkpoint_during,
                "durability": durability,
            },
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
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def run_stateless(
        self,
        *,
        assistant_id: str,
        input: typing.Optional[RunCreateStatelessInput] = OMIT,
        command: typing.Optional[Command] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        config: typing.Optional[RunCreateStatelessConfig] = OMIT,
        context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        webhook: typing.Optional[str] = OMIT,
        stream_mode: typing.Optional[RunCreateStatelessStreamMode] = OMIT,
        feedback_keys: typing.Optional[typing.Sequence[str]] = OMIT,
        stream_subgraphs: typing.Optional[bool] = OMIT,
        stream_resumable: typing.Optional[bool] = OMIT,
        on_completion: typing.Optional[RunCreateStatelessOnCompletion] = OMIT,
        after_seconds: typing.Optional[float] = OMIT,
        checkpoint_during: typing.Optional[bool] = OMIT,
        durability: typing.Optional[RunCreateStatelessDurability] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Create a run and return the run ID immediately. Don't wait for the final run output.

        Parameters
        ----------
        assistant_id : str

        input : typing.Optional[RunCreateStatelessInput]
            The input to the graph.

        command : typing.Optional[Command]
            The input to the graph.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to assign to the run.

        config : typing.Optional[RunCreateStatelessConfig]
            The configuration for the assistant.

        context : typing.Optional[typing.Dict[str, typing.Any]]
            Static context added to the assistant.

        webhook : typing.Optional[str]
            Webhook to call after LangGraph API call is done.

        stream_mode : typing.Optional[RunCreateStatelessStreamMode]
            The stream mode(s) to use.

        feedback_keys : typing.Optional[typing.Sequence[str]]
            Generate pre-signed URLs for assigning feedback keys to the run.

            For each key specified, a unique URL will be generated that can be called to assign the feedback key to the run. See [LangSmith Feedback](https://docs.langchain.com/langsmith/observability-concepts#feedback) for more details.

        stream_subgraphs : typing.Optional[bool]
            Whether to stream output from subgraphs.

        stream_resumable : typing.Optional[bool]
            Whether to persist the stream chunks in order to resume the stream later.

        on_completion : typing.Optional[RunCreateStatelessOnCompletion]
            Whether to delete or keep the thread created for a stateless run. Must be one of 'delete' or 'keep'.

        after_seconds : typing.Optional[float]
            The number of seconds to wait before starting the run. Use to schedule future runs.

        checkpoint_during : typing.Optional[bool]
            Whether to checkpoint during the run.

            Deprecated. Use `durability` instead to control checkpoint persistence behavior during the run.

        durability : typing.Optional[RunCreateStatelessDurability]
            Durability level for the run. Must be one of `sync`, `async`, or `exit`. See [durability modes](https://docs.langchain.com/oss/python/langgraph/durable-execution#durability-modes) for more details.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "runs",
            method="POST",
            json={
                "assistant_id": assistant_id,
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=typing.Optional[RunCreateStatelessInput], direction="write"
                ),
                "command": convert_and_respect_annotation_metadata(
                    object_=command, annotation=typing.Optional[Command], direction="write"
                ),
                "metadata": metadata,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=RunCreateStatelessConfig, direction="write"
                ),
                "context": context,
                "webhook": webhook,
                "stream_mode": convert_and_respect_annotation_metadata(
                    object_=stream_mode, annotation=RunCreateStatelessStreamMode, direction="write"
                ),
                "feedback_keys": feedback_keys,
                "stream_subgraphs": stream_subgraphs,
                "stream_resumable": stream_resumable,
                "on_completion": on_completion,
                "after_seconds": after_seconds,
                "checkpoint_during": checkpoint_during,
                "durability": durability,
            },
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
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def run_batch_stateless_runs_post(
        self, *, request: RunBatchCreate, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Create a batch of runs and return immediately.

        Parameters
        ----------
        request : RunBatchCreate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "runs/batch",
            method="POST",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=RunBatchCreate, direction="write"),
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
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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


class AsyncRawStatelessRunsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    @contextlib.asynccontextmanager
    async def stream_run_stateless(
        self,
        *,
        assistant_id: str,
        on_disconnect: typing.Optional[RunCreateStreamingStatelessOnDisconnect] = OMIT,
        input: typing.Optional[RunCreateStatelessInput] = OMIT,
        command: typing.Optional[Command] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        config: typing.Optional[RunCreateStatelessConfig] = OMIT,
        context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        webhook: typing.Optional[str] = OMIT,
        stream_mode: typing.Optional[RunCreateStatelessStreamMode] = OMIT,
        feedback_keys: typing.Optional[typing.Sequence[str]] = OMIT,
        stream_subgraphs: typing.Optional[bool] = OMIT,
        stream_resumable: typing.Optional[bool] = OMIT,
        on_completion: typing.Optional[RunCreateStatelessOnCompletion] = OMIT,
        after_seconds: typing.Optional[float] = OMIT,
        checkpoint_during: typing.Optional[bool] = OMIT,
        durability: typing.Optional[RunCreateStatelessDurability] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[str]]]:
        """
        Create a run and stream the output.

        Parameters
        ----------
        assistant_id : str

        on_disconnect : typing.Optional[RunCreateStreamingStatelessOnDisconnect]
            The disconnect mode to use. Must be one of 'cancel' or 'continue'.

        input : typing.Optional[RunCreateStatelessInput]
            The input to the graph.

        command : typing.Optional[Command]
            The input to the graph.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to assign to the run.

        config : typing.Optional[RunCreateStatelessConfig]
            The configuration for the assistant.

        context : typing.Optional[typing.Dict[str, typing.Any]]
            Static context added to the assistant.

        webhook : typing.Optional[str]
            Webhook to call after LangGraph API call is done.

        stream_mode : typing.Optional[RunCreateStatelessStreamMode]
            The stream mode(s) to use.

        feedback_keys : typing.Optional[typing.Sequence[str]]
            Generate pre-signed URLs for assigning feedback keys to the run.

            For each key specified, a unique URL will be generated that can be called to assign the feedback key to the run. See [LangSmith Feedback](https://docs.langchain.com/langsmith/observability-concepts#feedback) for more details.

        stream_subgraphs : typing.Optional[bool]
            Whether to stream output from subgraphs.

        stream_resumable : typing.Optional[bool]
            Whether to persist the stream chunks in order to resume the stream later.

        on_completion : typing.Optional[RunCreateStatelessOnCompletion]
            Whether to delete or keep the thread created for a stateless run. Must be one of 'delete' or 'keep'.

        after_seconds : typing.Optional[float]
            The number of seconds to wait before starting the run. Use to schedule future runs.

        checkpoint_during : typing.Optional[bool]
            Whether to checkpoint during the run.

            Deprecated. Use `durability` instead to control checkpoint persistence behavior during the run.

        durability : typing.Optional[RunCreateStatelessDurability]
            Durability level for the run. Must be one of `sync`, `async`, or `exit`. See [durability modes](https://docs.langchain.com/oss/python/langgraph/durable-execution#durability-modes) for more details.

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
                "on_disconnect": on_disconnect,
                "assistant_id": assistant_id,
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=typing.Optional[RunCreateStatelessInput], direction="write"
                ),
                "command": convert_and_respect_annotation_metadata(
                    object_=command, annotation=typing.Optional[Command], direction="write"
                ),
                "metadata": metadata,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=RunCreateStatelessConfig, direction="write"
                ),
                "context": context,
                "webhook": webhook,
                "stream_mode": convert_and_respect_annotation_metadata(
                    object_=stream_mode, annotation=RunCreateStatelessStreamMode, direction="write"
                ),
                "feedback_keys": feedback_keys,
                "stream_subgraphs": stream_subgraphs,
                "stream_resumable": stream_resumable,
                "on_completion": on_completion,
                "after_seconds": after_seconds,
                "checkpoint_during": checkpoint_during,
                "durability": durability,
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
                                typing.Any,
                                parse_obj_as(
                                    type_=typing.Any,
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

    async def wait_run_stateless(
        self,
        *,
        assistant_id: str,
        on_disconnect: typing.Optional[RunCreateStreamingStatelessOnDisconnect] = OMIT,
        input: typing.Optional[RunCreateStatelessInput] = OMIT,
        command: typing.Optional[Command] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        config: typing.Optional[RunCreateStatelessConfig] = OMIT,
        context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        webhook: typing.Optional[str] = OMIT,
        stream_mode: typing.Optional[RunCreateStatelessStreamMode] = OMIT,
        feedback_keys: typing.Optional[typing.Sequence[str]] = OMIT,
        stream_subgraphs: typing.Optional[bool] = OMIT,
        stream_resumable: typing.Optional[bool] = OMIT,
        on_completion: typing.Optional[RunCreateStatelessOnCompletion] = OMIT,
        after_seconds: typing.Optional[float] = OMIT,
        checkpoint_during: typing.Optional[bool] = OMIT,
        durability: typing.Optional[RunCreateStatelessDurability] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Create a run, wait for the final output and then return it.

        Parameters
        ----------
        assistant_id : str

        on_disconnect : typing.Optional[RunCreateStreamingStatelessOnDisconnect]
            The disconnect mode to use. Must be one of 'cancel' or 'continue'.

        input : typing.Optional[RunCreateStatelessInput]
            The input to the graph.

        command : typing.Optional[Command]
            The input to the graph.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to assign to the run.

        config : typing.Optional[RunCreateStatelessConfig]
            The configuration for the assistant.

        context : typing.Optional[typing.Dict[str, typing.Any]]
            Static context added to the assistant.

        webhook : typing.Optional[str]
            Webhook to call after LangGraph API call is done.

        stream_mode : typing.Optional[RunCreateStatelessStreamMode]
            The stream mode(s) to use.

        feedback_keys : typing.Optional[typing.Sequence[str]]
            Generate pre-signed URLs for assigning feedback keys to the run.

            For each key specified, a unique URL will be generated that can be called to assign the feedback key to the run. See [LangSmith Feedback](https://docs.langchain.com/langsmith/observability-concepts#feedback) for more details.

        stream_subgraphs : typing.Optional[bool]
            Whether to stream output from subgraphs.

        stream_resumable : typing.Optional[bool]
            Whether to persist the stream chunks in order to resume the stream later.

        on_completion : typing.Optional[RunCreateStatelessOnCompletion]
            Whether to delete or keep the thread created for a stateless run. Must be one of 'delete' or 'keep'.

        after_seconds : typing.Optional[float]
            The number of seconds to wait before starting the run. Use to schedule future runs.

        checkpoint_during : typing.Optional[bool]
            Whether to checkpoint during the run.

            Deprecated. Use `durability` instead to control checkpoint persistence behavior during the run.

        durability : typing.Optional[RunCreateStatelessDurability]
            Durability level for the run. Must be one of `sync`, `async`, or `exit`. See [durability modes](https://docs.langchain.com/oss/python/langgraph/durable-execution#durability-modes) for more details.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "runs/wait",
            method="POST",
            json={
                "on_disconnect": on_disconnect,
                "assistant_id": assistant_id,
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=typing.Optional[RunCreateStatelessInput], direction="write"
                ),
                "command": convert_and_respect_annotation_metadata(
                    object_=command, annotation=typing.Optional[Command], direction="write"
                ),
                "metadata": metadata,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=RunCreateStatelessConfig, direction="write"
                ),
                "context": context,
                "webhook": webhook,
                "stream_mode": convert_and_respect_annotation_metadata(
                    object_=stream_mode, annotation=RunCreateStatelessStreamMode, direction="write"
                ),
                "feedback_keys": feedback_keys,
                "stream_subgraphs": stream_subgraphs,
                "stream_resumable": stream_resumable,
                "on_completion": on_completion,
                "after_seconds": after_seconds,
                "checkpoint_during": checkpoint_during,
                "durability": durability,
            },
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
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def run_stateless(
        self,
        *,
        assistant_id: str,
        input: typing.Optional[RunCreateStatelessInput] = OMIT,
        command: typing.Optional[Command] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        config: typing.Optional[RunCreateStatelessConfig] = OMIT,
        context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        webhook: typing.Optional[str] = OMIT,
        stream_mode: typing.Optional[RunCreateStatelessStreamMode] = OMIT,
        feedback_keys: typing.Optional[typing.Sequence[str]] = OMIT,
        stream_subgraphs: typing.Optional[bool] = OMIT,
        stream_resumable: typing.Optional[bool] = OMIT,
        on_completion: typing.Optional[RunCreateStatelessOnCompletion] = OMIT,
        after_seconds: typing.Optional[float] = OMIT,
        checkpoint_during: typing.Optional[bool] = OMIT,
        durability: typing.Optional[RunCreateStatelessDurability] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Create a run and return the run ID immediately. Don't wait for the final run output.

        Parameters
        ----------
        assistant_id : str

        input : typing.Optional[RunCreateStatelessInput]
            The input to the graph.

        command : typing.Optional[Command]
            The input to the graph.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to assign to the run.

        config : typing.Optional[RunCreateStatelessConfig]
            The configuration for the assistant.

        context : typing.Optional[typing.Dict[str, typing.Any]]
            Static context added to the assistant.

        webhook : typing.Optional[str]
            Webhook to call after LangGraph API call is done.

        stream_mode : typing.Optional[RunCreateStatelessStreamMode]
            The stream mode(s) to use.

        feedback_keys : typing.Optional[typing.Sequence[str]]
            Generate pre-signed URLs for assigning feedback keys to the run.

            For each key specified, a unique URL will be generated that can be called to assign the feedback key to the run. See [LangSmith Feedback](https://docs.langchain.com/langsmith/observability-concepts#feedback) for more details.

        stream_subgraphs : typing.Optional[bool]
            Whether to stream output from subgraphs.

        stream_resumable : typing.Optional[bool]
            Whether to persist the stream chunks in order to resume the stream later.

        on_completion : typing.Optional[RunCreateStatelessOnCompletion]
            Whether to delete or keep the thread created for a stateless run. Must be one of 'delete' or 'keep'.

        after_seconds : typing.Optional[float]
            The number of seconds to wait before starting the run. Use to schedule future runs.

        checkpoint_during : typing.Optional[bool]
            Whether to checkpoint during the run.

            Deprecated. Use `durability` instead to control checkpoint persistence behavior during the run.

        durability : typing.Optional[RunCreateStatelessDurability]
            Durability level for the run. Must be one of `sync`, `async`, or `exit`. See [durability modes](https://docs.langchain.com/oss/python/langgraph/durable-execution#durability-modes) for more details.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "runs",
            method="POST",
            json={
                "assistant_id": assistant_id,
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=typing.Optional[RunCreateStatelessInput], direction="write"
                ),
                "command": convert_and_respect_annotation_metadata(
                    object_=command, annotation=typing.Optional[Command], direction="write"
                ),
                "metadata": metadata,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=RunCreateStatelessConfig, direction="write"
                ),
                "context": context,
                "webhook": webhook,
                "stream_mode": convert_and_respect_annotation_metadata(
                    object_=stream_mode, annotation=RunCreateStatelessStreamMode, direction="write"
                ),
                "feedback_keys": feedback_keys,
                "stream_subgraphs": stream_subgraphs,
                "stream_resumable": stream_resumable,
                "on_completion": on_completion,
                "after_seconds": after_seconds,
                "checkpoint_during": checkpoint_during,
                "durability": durability,
            },
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
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def run_batch_stateless_runs_post(
        self, *, request: RunBatchCreate, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Create a batch of runs and return immediately.

        Parameters
        ----------
        request : RunBatchCreate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "runs/batch",
            method="POST",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=RunBatchCreate, direction="write"),
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
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
