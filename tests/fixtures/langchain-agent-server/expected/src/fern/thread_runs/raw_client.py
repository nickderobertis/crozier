

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
from ..errors.conflict_error import ConflictError
from ..errors.not_found_error import NotFoundError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.checkpoint_config import CheckpointConfig
from ..types.command import Command
from ..types.error_response import ErrorResponse
from ..types.run import Run
from ..types.run_create_stateful_config import RunCreateStatefulConfig
from ..types.run_create_stateful_durability import RunCreateStatefulDurability
from ..types.run_create_stateful_if_not_exists import RunCreateStatefulIfNotExists
from ..types.run_create_stateful_input import RunCreateStatefulInput
from ..types.run_create_stateful_interrupt_after import RunCreateStatefulInterruptAfter
from ..types.run_create_stateful_interrupt_before import RunCreateStatefulInterruptBefore
from ..types.run_create_stateful_multitask_strategy import RunCreateStatefulMultitaskStrategy
from ..types.run_create_stateful_stream_mode import RunCreateStatefulStreamMode
from ..types.run_create_streaming_stateful_on_disconnect import RunCreateStreamingStatefulOnDisconnect
from .types.cancel_run_http_threads_thread_id_runs_run_id_cancel_post_request_action import (
    CancelRunHttpThreadsThreadIdRunsRunIdCancelPostRequestAction,
)
from .types.cancel_runs_post_request_action import CancelRunsPostRequestAction
from .types.list_runs_http_threads_thread_id_runs_get_request_select_item import (
    ListRunsHttpThreadsThreadIdRunsGetRequestSelectItem,
)
from .types.list_runs_http_threads_thread_id_runs_get_request_status import (
    ListRunsHttpThreadsThreadIdRunsGetRequestStatus,
)
from .types.runs_cancel_status import RunsCancelStatus
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawThreadRunsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_runs_http(
        self,
        thread_id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        status: typing.Optional[ListRunsHttpThreadsThreadIdRunsGetRequestStatus] = None,
        select: typing.Optional[
            typing.Union[
                ListRunsHttpThreadsThreadIdRunsGetRequestSelectItem,
                typing.Sequence[ListRunsHttpThreadsThreadIdRunsGetRequestSelectItem],
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Run]]:
        """
        List runs for a thread.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        status : typing.Optional[ListRunsHttpThreadsThreadIdRunsGetRequestStatus]

        select : typing.Optional[typing.Union[ListRunsHttpThreadsThreadIdRunsGetRequestSelectItem, typing.Sequence[ListRunsHttpThreadsThreadIdRunsGetRequestSelectItem]]]
            Specify which fields to return. If not provided, all fields are returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Run]]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/runs",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "status": status,
                "select": select,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Run],
                    parse_obj_as(
                        type_=typing.List[Run],
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

    def create_run(
        self,
        thread_id: str,
        *,
        assistant_id: str,
        checkpoint: typing.Optional[CheckpointConfig] = OMIT,
        input: typing.Optional[RunCreateStatefulInput] = OMIT,
        command: typing.Optional[Command] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        config: typing.Optional[RunCreateStatefulConfig] = OMIT,
        context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        webhook: typing.Optional[str] = OMIT,
        interrupt_before: typing.Optional[RunCreateStatefulInterruptBefore] = OMIT,
        interrupt_after: typing.Optional[RunCreateStatefulInterruptAfter] = OMIT,
        stream_mode: typing.Optional[RunCreateStatefulStreamMode] = OMIT,
        stream_subgraphs: typing.Optional[bool] = OMIT,
        stream_resumable: typing.Optional[bool] = OMIT,
        feedback_keys: typing.Optional[typing.Sequence[str]] = OMIT,
        multitask_strategy: typing.Optional[RunCreateStatefulMultitaskStrategy] = OMIT,
        if_not_exists: typing.Optional[RunCreateStatefulIfNotExists] = OMIT,
        after_seconds: typing.Optional[float] = OMIT,
        checkpoint_during: typing.Optional[bool] = OMIT,
        durability: typing.Optional[RunCreateStatefulDurability] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Run]:
        """
        Create a run in existing thread, return the run ID immediately. Don't wait for the final run output.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        assistant_id : str

        checkpoint : typing.Optional[CheckpointConfig]
            The checkpoint to resume from.

        input : typing.Optional[RunCreateStatefulInput]
            The input to the graph.

        command : typing.Optional[Command]
            The input to the graph.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to assign to the run.

        config : typing.Optional[RunCreateStatefulConfig]
            The configuration for the assistant.

        context : typing.Optional[typing.Dict[str, typing.Any]]
            Static context added to the assistant.

        webhook : typing.Optional[str]
            Webhook to call after LangGraph API call is done.

        interrupt_before : typing.Optional[RunCreateStatefulInterruptBefore]
            Nodes to interrupt immediately before they get executed.

        interrupt_after : typing.Optional[RunCreateStatefulInterruptAfter]
            Nodes to interrupt immediately after they get executed.

        stream_mode : typing.Optional[RunCreateStatefulStreamMode]
            The stream mode(s) to use.

        stream_subgraphs : typing.Optional[bool]
            Whether to stream output from subgraphs.

        stream_resumable : typing.Optional[bool]
            Whether to persist the stream chunks in order to resume the stream later.

        feedback_keys : typing.Optional[typing.Sequence[str]]
            Generate pre-signed URLs for assigning feedback keys to the run.

            For each key specified, a unique URL will be generated that can be called to assign the feedback key to the run. See [LangSmith Feedback](https://docs.langchain.com/langsmith/observability-concepts#feedback) for more details.

        multitask_strategy : typing.Optional[RunCreateStatefulMultitaskStrategy]
            Multitask strategy to use. Must be one of 'reject', 'interrupt', 'rollback', or 'enqueue'.

        if_not_exists : typing.Optional[RunCreateStatefulIfNotExists]
            How to handle missing thread. Must be either 'reject' (raise error if missing), or 'create' (create new thread).

        after_seconds : typing.Optional[float]
            The number of seconds to wait before starting the run. Use to schedule future runs.

        checkpoint_during : typing.Optional[bool]
            Whether to checkpoint during the run.

            Deprecated. Use `durability` instead to control checkpoint persistence behavior during the run.

        durability : typing.Optional[RunCreateStatefulDurability]
            Durability level for the run. Must be one of `sync`, `async`, or `exit`. See [durability modes](https://docs.langchain.com/oss/python/langgraph/durable-execution#durability-modes) for more details.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Run]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/runs",
            method="POST",
            json={
                "assistant_id": assistant_id,
                "checkpoint": convert_and_respect_annotation_metadata(
                    object_=checkpoint, annotation=CheckpointConfig, direction="write"
                ),
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=typing.Optional[RunCreateStatefulInput], direction="write"
                ),
                "command": convert_and_respect_annotation_metadata(
                    object_=command, annotation=typing.Optional[Command], direction="write"
                ),
                "metadata": metadata,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=RunCreateStatefulConfig, direction="write"
                ),
                "context": context,
                "webhook": webhook,
                "interrupt_before": convert_and_respect_annotation_metadata(
                    object_=interrupt_before, annotation=RunCreateStatefulInterruptBefore, direction="write"
                ),
                "interrupt_after": convert_and_respect_annotation_metadata(
                    object_=interrupt_after, annotation=RunCreateStatefulInterruptAfter, direction="write"
                ),
                "stream_mode": convert_and_respect_annotation_metadata(
                    object_=stream_mode, annotation=RunCreateStatefulStreamMode, direction="write"
                ),
                "stream_subgraphs": stream_subgraphs,
                "stream_resumable": stream_resumable,
                "feedback_keys": feedback_keys,
                "multitask_strategy": multitask_strategy,
                "if_not_exists": if_not_exists,
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
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Run,
                    parse_obj_as(
                        type_=Run,
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

    @contextlib.contextmanager
    def stream_run(
        self,
        thread_id: str,
        *,
        assistant_id: str,
        on_disconnect: typing.Optional[RunCreateStreamingStatefulOnDisconnect] = OMIT,
        checkpoint: typing.Optional[CheckpointConfig] = OMIT,
        input: typing.Optional[RunCreateStatefulInput] = OMIT,
        command: typing.Optional[Command] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        config: typing.Optional[RunCreateStatefulConfig] = OMIT,
        context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        webhook: typing.Optional[str] = OMIT,
        interrupt_before: typing.Optional[RunCreateStatefulInterruptBefore] = OMIT,
        interrupt_after: typing.Optional[RunCreateStatefulInterruptAfter] = OMIT,
        stream_mode: typing.Optional[RunCreateStatefulStreamMode] = OMIT,
        stream_subgraphs: typing.Optional[bool] = OMIT,
        stream_resumable: typing.Optional[bool] = OMIT,
        feedback_keys: typing.Optional[typing.Sequence[str]] = OMIT,
        multitask_strategy: typing.Optional[RunCreateStatefulMultitaskStrategy] = OMIT,
        if_not_exists: typing.Optional[RunCreateStatefulIfNotExists] = OMIT,
        after_seconds: typing.Optional[float] = OMIT,
        checkpoint_during: typing.Optional[bool] = OMIT,
        durability: typing.Optional[RunCreateStatefulDurability] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[str]]]:
        """
        Create a run in existing thread. Stream the output.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        assistant_id : str

        on_disconnect : typing.Optional[RunCreateStreamingStatefulOnDisconnect]
            The disconnect mode to use. Must be one of 'cancel' or 'continue'.

        checkpoint : typing.Optional[CheckpointConfig]
            The checkpoint to resume from.

        input : typing.Optional[RunCreateStatefulInput]
            The input to the graph.

        command : typing.Optional[Command]
            The input to the graph.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to assign to the run.

        config : typing.Optional[RunCreateStatefulConfig]
            The configuration for the assistant.

        context : typing.Optional[typing.Dict[str, typing.Any]]
            Static context added to the assistant.

        webhook : typing.Optional[str]
            Webhook to call after LangGraph API call is done.

        interrupt_before : typing.Optional[RunCreateStatefulInterruptBefore]
            Nodes to interrupt immediately before they get executed.

        interrupt_after : typing.Optional[RunCreateStatefulInterruptAfter]
            Nodes to interrupt immediately after they get executed.

        stream_mode : typing.Optional[RunCreateStatefulStreamMode]
            The stream mode(s) to use.

        stream_subgraphs : typing.Optional[bool]
            Whether to stream output from subgraphs.

        stream_resumable : typing.Optional[bool]
            Whether to persist the stream chunks in order to resume the stream later.

        feedback_keys : typing.Optional[typing.Sequence[str]]
            Generate pre-signed URLs for assigning feedback keys to the run.

            For each key specified, a unique URL will be generated that can be called to assign the feedback key to the run. See [LangSmith Feedback](https://docs.langchain.com/langsmith/observability-concepts#feedback) for more details.

        multitask_strategy : typing.Optional[RunCreateStatefulMultitaskStrategy]
            Multitask strategy to use. Must be one of 'reject', 'interrupt', 'rollback', or 'enqueue'.

        if_not_exists : typing.Optional[RunCreateStatefulIfNotExists]
            How to handle missing thread. Must be either 'reject' (raise error if missing), or 'create' (create new thread).

        after_seconds : typing.Optional[float]
            The number of seconds to wait before starting the run. Use to schedule future runs.

        checkpoint_during : typing.Optional[bool]
            Whether to checkpoint during the run.

            Deprecated. Use `durability` instead to control checkpoint persistence behavior during the run.

        durability : typing.Optional[RunCreateStatefulDurability]
            Durability level for the run. Must be one of `sync`, `async`, or `exit`. See [durability modes](https://docs.langchain.com/oss/python/langgraph/durable-execution#durability-modes) for more details.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[HttpResponse[typing.Iterator[str]]]
            Success
        """
        with self._client_wrapper.httpx_client.stream(
            f"threads/{encode_path_param(thread_id)}/runs/stream",
            method="POST",
            json={
                "on_disconnect": on_disconnect,
                "assistant_id": assistant_id,
                "checkpoint": convert_and_respect_annotation_metadata(
                    object_=checkpoint, annotation=CheckpointConfig, direction="write"
                ),
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=typing.Optional[RunCreateStatefulInput], direction="write"
                ),
                "command": convert_and_respect_annotation_metadata(
                    object_=command, annotation=typing.Optional[Command], direction="write"
                ),
                "metadata": metadata,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=RunCreateStatefulConfig, direction="write"
                ),
                "context": context,
                "webhook": webhook,
                "interrupt_before": convert_and_respect_annotation_metadata(
                    object_=interrupt_before, annotation=RunCreateStatefulInterruptBefore, direction="write"
                ),
                "interrupt_after": convert_and_respect_annotation_metadata(
                    object_=interrupt_after, annotation=RunCreateStatefulInterruptAfter, direction="write"
                ),
                "stream_mode": convert_and_respect_annotation_metadata(
                    object_=stream_mode, annotation=RunCreateStatefulStreamMode, direction="write"
                ),
                "stream_subgraphs": stream_subgraphs,
                "stream_resumable": stream_resumable,
                "feedback_keys": feedback_keys,
                "multitask_strategy": multitask_strategy,
                "if_not_exists": if_not_exists,
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

    def wait_run(
        self,
        thread_id: str,
        *,
        assistant_id: str,
        on_disconnect: typing.Optional[RunCreateStreamingStatefulOnDisconnect] = OMIT,
        checkpoint: typing.Optional[CheckpointConfig] = OMIT,
        input: typing.Optional[RunCreateStatefulInput] = OMIT,
        command: typing.Optional[Command] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        config: typing.Optional[RunCreateStatefulConfig] = OMIT,
        context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        webhook: typing.Optional[str] = OMIT,
        interrupt_before: typing.Optional[RunCreateStatefulInterruptBefore] = OMIT,
        interrupt_after: typing.Optional[RunCreateStatefulInterruptAfter] = OMIT,
        stream_mode: typing.Optional[RunCreateStatefulStreamMode] = OMIT,
        stream_subgraphs: typing.Optional[bool] = OMIT,
        stream_resumable: typing.Optional[bool] = OMIT,
        feedback_keys: typing.Optional[typing.Sequence[str]] = OMIT,
        multitask_strategy: typing.Optional[RunCreateStatefulMultitaskStrategy] = OMIT,
        if_not_exists: typing.Optional[RunCreateStatefulIfNotExists] = OMIT,
        after_seconds: typing.Optional[float] = OMIT,
        checkpoint_during: typing.Optional[bool] = OMIT,
        durability: typing.Optional[RunCreateStatefulDurability] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Create a run in existing thread. Wait for the final output and then return it.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        assistant_id : str

        on_disconnect : typing.Optional[RunCreateStreamingStatefulOnDisconnect]
            The disconnect mode to use. Must be one of 'cancel' or 'continue'.

        checkpoint : typing.Optional[CheckpointConfig]
            The checkpoint to resume from.

        input : typing.Optional[RunCreateStatefulInput]
            The input to the graph.

        command : typing.Optional[Command]
            The input to the graph.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to assign to the run.

        config : typing.Optional[RunCreateStatefulConfig]
            The configuration for the assistant.

        context : typing.Optional[typing.Dict[str, typing.Any]]
            Static context added to the assistant.

        webhook : typing.Optional[str]
            Webhook to call after LangGraph API call is done.

        interrupt_before : typing.Optional[RunCreateStatefulInterruptBefore]
            Nodes to interrupt immediately before they get executed.

        interrupt_after : typing.Optional[RunCreateStatefulInterruptAfter]
            Nodes to interrupt immediately after they get executed.

        stream_mode : typing.Optional[RunCreateStatefulStreamMode]
            The stream mode(s) to use.

        stream_subgraphs : typing.Optional[bool]
            Whether to stream output from subgraphs.

        stream_resumable : typing.Optional[bool]
            Whether to persist the stream chunks in order to resume the stream later.

        feedback_keys : typing.Optional[typing.Sequence[str]]
            Generate pre-signed URLs for assigning feedback keys to the run.

            For each key specified, a unique URL will be generated that can be called to assign the feedback key to the run. See [LangSmith Feedback](https://docs.langchain.com/langsmith/observability-concepts#feedback) for more details.

        multitask_strategy : typing.Optional[RunCreateStatefulMultitaskStrategy]
            Multitask strategy to use. Must be one of 'reject', 'interrupt', 'rollback', or 'enqueue'.

        if_not_exists : typing.Optional[RunCreateStatefulIfNotExists]
            How to handle missing thread. Must be either 'reject' (raise error if missing), or 'create' (create new thread).

        after_seconds : typing.Optional[float]
            The number of seconds to wait before starting the run. Use to schedule future runs.

        checkpoint_during : typing.Optional[bool]
            Whether to checkpoint during the run.

            Deprecated. Use `durability` instead to control checkpoint persistence behavior during the run.

        durability : typing.Optional[RunCreateStatefulDurability]
            Durability level for the run. Must be one of `sync`, `async`, or `exit`. See [durability modes](https://docs.langchain.com/oss/python/langgraph/durable-execution#durability-modes) for more details.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/runs/wait",
            method="POST",
            json={
                "on_disconnect": on_disconnect,
                "assistant_id": assistant_id,
                "checkpoint": convert_and_respect_annotation_metadata(
                    object_=checkpoint, annotation=CheckpointConfig, direction="write"
                ),
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=typing.Optional[RunCreateStatefulInput], direction="write"
                ),
                "command": convert_and_respect_annotation_metadata(
                    object_=command, annotation=typing.Optional[Command], direction="write"
                ),
                "metadata": metadata,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=RunCreateStatefulConfig, direction="write"
                ),
                "context": context,
                "webhook": webhook,
                "interrupt_before": convert_and_respect_annotation_metadata(
                    object_=interrupt_before, annotation=RunCreateStatefulInterruptBefore, direction="write"
                ),
                "interrupt_after": convert_and_respect_annotation_metadata(
                    object_=interrupt_after, annotation=RunCreateStatefulInterruptAfter, direction="write"
                ),
                "stream_mode": convert_and_respect_annotation_metadata(
                    object_=stream_mode, annotation=RunCreateStatefulStreamMode, direction="write"
                ),
                "stream_subgraphs": stream_subgraphs,
                "stream_resumable": stream_resumable,
                "feedback_keys": feedback_keys,
                "multitask_strategy": multitask_strategy,
                "if_not_exists": if_not_exists,
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

    def get_run_http(
        self, thread_id: str, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Run]:
        """
        Get a run by ID.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        run_id : str
            The ID of the run.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Run]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/runs/{encode_path_param(run_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Run,
                    parse_obj_as(
                        type_=Run,
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

    def delete_run(
        self, thread_id: str, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Delete a run by ID.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        run_id : str
            The ID of the run.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/runs/{encode_path_param(run_id)}",
            method="DELETE",
            request_options=request_options,
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

    def join_run_http(
        self,
        thread_id: str,
        run_id: str,
        *,
        cancel_on_disconnect: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Wait for a run to finish.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        run_id : str
            The ID of the run.

        cancel_on_disconnect : typing.Optional[bool]
            If true, the run will be cancelled if the client disconnects.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/runs/{encode_path_param(run_id)}/join",
            method="GET",
            params={
                "cancel_on_disconnect": cancel_on_disconnect,
            },
            request_options=request_options,
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
    def stream_run_http_threads_thread_id_runs_run_id_join_get(
        self,
        thread_id: str,
        run_id: str,
        *,
        stream_mode: typing.Optional[str] = None,
        cancel_on_disconnect: typing.Optional[bool] = None,
        last_event_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[str]]]:
        """
        Join a run stream. This endpoint streams output in real-time from a run similar to the /threads/__THREAD_ID__/runs/stream endpoint. If the run has been created with `stream_resumable=true`, the stream can be resumed from the last seen event ID.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        run_id : str
            The ID of the run.

        stream_mode : typing.Optional[str]
            The mode to stream the run in. If not provided, the default mode will be used.

        cancel_on_disconnect : typing.Optional[bool]
            If true, the run will be cancelled if the client disconnects.

        last_event_id : typing.Optional[str]
            The ID of the last event received. Set to -1 if you want to stream all events. Requires `stream_resumable=true` to be set when creating the run.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[HttpResponse[typing.Iterator[str]]]
            Success
        """
        with self._client_wrapper.httpx_client.stream(
            f"threads/{encode_path_param(thread_id)}/runs/{encode_path_param(run_id)}/stream",
            method="GET",
            params={
                "stream_mode": stream_mode,
                "cancel_on_disconnect": cancel_on_disconnect,
            },
            headers={
                "Last-Event-ID": str(last_event_id) if last_event_id is not None else None,
            },
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

    def cancel_run_http(
        self,
        thread_id: str,
        run_id: str,
        *,
        wait: typing.Optional[bool] = None,
        action: typing.Optional[CancelRunHttpThreadsThreadIdRunsRunIdCancelPostRequestAction] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        run_id : str
            The ID of the run.

        wait : typing.Optional[bool]

        action : typing.Optional[CancelRunHttpThreadsThreadIdRunsRunIdCancelPostRequestAction]
            Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. `interrupt` will simply cancel the run. `rollback` will cancel the run and delete the run and associated checkpoints afterwards.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/runs/{encode_path_param(run_id)}/cancel",
            method="POST",
            params={
                "wait": wait,
                "action": action,
            },
            request_options=request_options,
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

    def cancel_runs_post(
        self,
        *,
        action: typing.Optional[CancelRunsPostRequestAction] = None,
        status: typing.Optional[RunsCancelStatus] = OMIT,
        thread_id: typing.Optional[str] = OMIT,
        run_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Cancel one or more runs. Can cancel runs by thread ID and run IDs, or by status filter.

        Parameters
        ----------
        action : typing.Optional[CancelRunsPostRequestAction]
            Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. `interrupt` will simply cancel the run. `rollback` will cancel the run and delete the run and associated checkpoints afterwards.

        status : typing.Optional[RunsCancelStatus]
            Filter runs by status to cancel. Must be one of 'pending', 'running', or 'all'.

        thread_id : typing.Optional[str]
            The ID of the thread containing runs to cancel.

        run_ids : typing.Optional[typing.Sequence[str]]
            List of run IDs to cancel.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "runs/cancel",
            method="POST",
            params={
                "action": action,
            },
            json={
                "status": status,
                "thread_id": thread_id,
                "run_ids": run_ids,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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


class AsyncRawThreadRunsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_runs_http(
        self,
        thread_id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        status: typing.Optional[ListRunsHttpThreadsThreadIdRunsGetRequestStatus] = None,
        select: typing.Optional[
            typing.Union[
                ListRunsHttpThreadsThreadIdRunsGetRequestSelectItem,
                typing.Sequence[ListRunsHttpThreadsThreadIdRunsGetRequestSelectItem],
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Run]]:
        """
        List runs for a thread.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        status : typing.Optional[ListRunsHttpThreadsThreadIdRunsGetRequestStatus]

        select : typing.Optional[typing.Union[ListRunsHttpThreadsThreadIdRunsGetRequestSelectItem, typing.Sequence[ListRunsHttpThreadsThreadIdRunsGetRequestSelectItem]]]
            Specify which fields to return. If not provided, all fields are returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Run]]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/runs",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "status": status,
                "select": select,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Run],
                    parse_obj_as(
                        type_=typing.List[Run],
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

    async def create_run(
        self,
        thread_id: str,
        *,
        assistant_id: str,
        checkpoint: typing.Optional[CheckpointConfig] = OMIT,
        input: typing.Optional[RunCreateStatefulInput] = OMIT,
        command: typing.Optional[Command] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        config: typing.Optional[RunCreateStatefulConfig] = OMIT,
        context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        webhook: typing.Optional[str] = OMIT,
        interrupt_before: typing.Optional[RunCreateStatefulInterruptBefore] = OMIT,
        interrupt_after: typing.Optional[RunCreateStatefulInterruptAfter] = OMIT,
        stream_mode: typing.Optional[RunCreateStatefulStreamMode] = OMIT,
        stream_subgraphs: typing.Optional[bool] = OMIT,
        stream_resumable: typing.Optional[bool] = OMIT,
        feedback_keys: typing.Optional[typing.Sequence[str]] = OMIT,
        multitask_strategy: typing.Optional[RunCreateStatefulMultitaskStrategy] = OMIT,
        if_not_exists: typing.Optional[RunCreateStatefulIfNotExists] = OMIT,
        after_seconds: typing.Optional[float] = OMIT,
        checkpoint_during: typing.Optional[bool] = OMIT,
        durability: typing.Optional[RunCreateStatefulDurability] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Run]:
        """
        Create a run in existing thread, return the run ID immediately. Don't wait for the final run output.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        assistant_id : str

        checkpoint : typing.Optional[CheckpointConfig]
            The checkpoint to resume from.

        input : typing.Optional[RunCreateStatefulInput]
            The input to the graph.

        command : typing.Optional[Command]
            The input to the graph.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to assign to the run.

        config : typing.Optional[RunCreateStatefulConfig]
            The configuration for the assistant.

        context : typing.Optional[typing.Dict[str, typing.Any]]
            Static context added to the assistant.

        webhook : typing.Optional[str]
            Webhook to call after LangGraph API call is done.

        interrupt_before : typing.Optional[RunCreateStatefulInterruptBefore]
            Nodes to interrupt immediately before they get executed.

        interrupt_after : typing.Optional[RunCreateStatefulInterruptAfter]
            Nodes to interrupt immediately after they get executed.

        stream_mode : typing.Optional[RunCreateStatefulStreamMode]
            The stream mode(s) to use.

        stream_subgraphs : typing.Optional[bool]
            Whether to stream output from subgraphs.

        stream_resumable : typing.Optional[bool]
            Whether to persist the stream chunks in order to resume the stream later.

        feedback_keys : typing.Optional[typing.Sequence[str]]
            Generate pre-signed URLs for assigning feedback keys to the run.

            For each key specified, a unique URL will be generated that can be called to assign the feedback key to the run. See [LangSmith Feedback](https://docs.langchain.com/langsmith/observability-concepts#feedback) for more details.

        multitask_strategy : typing.Optional[RunCreateStatefulMultitaskStrategy]
            Multitask strategy to use. Must be one of 'reject', 'interrupt', 'rollback', or 'enqueue'.

        if_not_exists : typing.Optional[RunCreateStatefulIfNotExists]
            How to handle missing thread. Must be either 'reject' (raise error if missing), or 'create' (create new thread).

        after_seconds : typing.Optional[float]
            The number of seconds to wait before starting the run. Use to schedule future runs.

        checkpoint_during : typing.Optional[bool]
            Whether to checkpoint during the run.

            Deprecated. Use `durability` instead to control checkpoint persistence behavior during the run.

        durability : typing.Optional[RunCreateStatefulDurability]
            Durability level for the run. Must be one of `sync`, `async`, or `exit`. See [durability modes](https://docs.langchain.com/oss/python/langgraph/durable-execution#durability-modes) for more details.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Run]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/runs",
            method="POST",
            json={
                "assistant_id": assistant_id,
                "checkpoint": convert_and_respect_annotation_metadata(
                    object_=checkpoint, annotation=CheckpointConfig, direction="write"
                ),
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=typing.Optional[RunCreateStatefulInput], direction="write"
                ),
                "command": convert_and_respect_annotation_metadata(
                    object_=command, annotation=typing.Optional[Command], direction="write"
                ),
                "metadata": metadata,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=RunCreateStatefulConfig, direction="write"
                ),
                "context": context,
                "webhook": webhook,
                "interrupt_before": convert_and_respect_annotation_metadata(
                    object_=interrupt_before, annotation=RunCreateStatefulInterruptBefore, direction="write"
                ),
                "interrupt_after": convert_and_respect_annotation_metadata(
                    object_=interrupt_after, annotation=RunCreateStatefulInterruptAfter, direction="write"
                ),
                "stream_mode": convert_and_respect_annotation_metadata(
                    object_=stream_mode, annotation=RunCreateStatefulStreamMode, direction="write"
                ),
                "stream_subgraphs": stream_subgraphs,
                "stream_resumable": stream_resumable,
                "feedback_keys": feedback_keys,
                "multitask_strategy": multitask_strategy,
                "if_not_exists": if_not_exists,
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
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Run,
                    parse_obj_as(
                        type_=Run,
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

    @contextlib.asynccontextmanager
    async def stream_run(
        self,
        thread_id: str,
        *,
        assistant_id: str,
        on_disconnect: typing.Optional[RunCreateStreamingStatefulOnDisconnect] = OMIT,
        checkpoint: typing.Optional[CheckpointConfig] = OMIT,
        input: typing.Optional[RunCreateStatefulInput] = OMIT,
        command: typing.Optional[Command] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        config: typing.Optional[RunCreateStatefulConfig] = OMIT,
        context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        webhook: typing.Optional[str] = OMIT,
        interrupt_before: typing.Optional[RunCreateStatefulInterruptBefore] = OMIT,
        interrupt_after: typing.Optional[RunCreateStatefulInterruptAfter] = OMIT,
        stream_mode: typing.Optional[RunCreateStatefulStreamMode] = OMIT,
        stream_subgraphs: typing.Optional[bool] = OMIT,
        stream_resumable: typing.Optional[bool] = OMIT,
        feedback_keys: typing.Optional[typing.Sequence[str]] = OMIT,
        multitask_strategy: typing.Optional[RunCreateStatefulMultitaskStrategy] = OMIT,
        if_not_exists: typing.Optional[RunCreateStatefulIfNotExists] = OMIT,
        after_seconds: typing.Optional[float] = OMIT,
        checkpoint_during: typing.Optional[bool] = OMIT,
        durability: typing.Optional[RunCreateStatefulDurability] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[str]]]:
        """
        Create a run in existing thread. Stream the output.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        assistant_id : str

        on_disconnect : typing.Optional[RunCreateStreamingStatefulOnDisconnect]
            The disconnect mode to use. Must be one of 'cancel' or 'continue'.

        checkpoint : typing.Optional[CheckpointConfig]
            The checkpoint to resume from.

        input : typing.Optional[RunCreateStatefulInput]
            The input to the graph.

        command : typing.Optional[Command]
            The input to the graph.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to assign to the run.

        config : typing.Optional[RunCreateStatefulConfig]
            The configuration for the assistant.

        context : typing.Optional[typing.Dict[str, typing.Any]]
            Static context added to the assistant.

        webhook : typing.Optional[str]
            Webhook to call after LangGraph API call is done.

        interrupt_before : typing.Optional[RunCreateStatefulInterruptBefore]
            Nodes to interrupt immediately before they get executed.

        interrupt_after : typing.Optional[RunCreateStatefulInterruptAfter]
            Nodes to interrupt immediately after they get executed.

        stream_mode : typing.Optional[RunCreateStatefulStreamMode]
            The stream mode(s) to use.

        stream_subgraphs : typing.Optional[bool]
            Whether to stream output from subgraphs.

        stream_resumable : typing.Optional[bool]
            Whether to persist the stream chunks in order to resume the stream later.

        feedback_keys : typing.Optional[typing.Sequence[str]]
            Generate pre-signed URLs for assigning feedback keys to the run.

            For each key specified, a unique URL will be generated that can be called to assign the feedback key to the run. See [LangSmith Feedback](https://docs.langchain.com/langsmith/observability-concepts#feedback) for more details.

        multitask_strategy : typing.Optional[RunCreateStatefulMultitaskStrategy]
            Multitask strategy to use. Must be one of 'reject', 'interrupt', 'rollback', or 'enqueue'.

        if_not_exists : typing.Optional[RunCreateStatefulIfNotExists]
            How to handle missing thread. Must be either 'reject' (raise error if missing), or 'create' (create new thread).

        after_seconds : typing.Optional[float]
            The number of seconds to wait before starting the run. Use to schedule future runs.

        checkpoint_during : typing.Optional[bool]
            Whether to checkpoint during the run.

            Deprecated. Use `durability` instead to control checkpoint persistence behavior during the run.

        durability : typing.Optional[RunCreateStatefulDurability]
            Durability level for the run. Must be one of `sync`, `async`, or `exit`. See [durability modes](https://docs.langchain.com/oss/python/langgraph/durable-execution#durability-modes) for more details.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[str]]]
            Success
        """
        async with self._client_wrapper.httpx_client.stream(
            f"threads/{encode_path_param(thread_id)}/runs/stream",
            method="POST",
            json={
                "on_disconnect": on_disconnect,
                "assistant_id": assistant_id,
                "checkpoint": convert_and_respect_annotation_metadata(
                    object_=checkpoint, annotation=CheckpointConfig, direction="write"
                ),
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=typing.Optional[RunCreateStatefulInput], direction="write"
                ),
                "command": convert_and_respect_annotation_metadata(
                    object_=command, annotation=typing.Optional[Command], direction="write"
                ),
                "metadata": metadata,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=RunCreateStatefulConfig, direction="write"
                ),
                "context": context,
                "webhook": webhook,
                "interrupt_before": convert_and_respect_annotation_metadata(
                    object_=interrupt_before, annotation=RunCreateStatefulInterruptBefore, direction="write"
                ),
                "interrupt_after": convert_and_respect_annotation_metadata(
                    object_=interrupt_after, annotation=RunCreateStatefulInterruptAfter, direction="write"
                ),
                "stream_mode": convert_and_respect_annotation_metadata(
                    object_=stream_mode, annotation=RunCreateStatefulStreamMode, direction="write"
                ),
                "stream_subgraphs": stream_subgraphs,
                "stream_resumable": stream_resumable,
                "feedback_keys": feedback_keys,
                "multitask_strategy": multitask_strategy,
                "if_not_exists": if_not_exists,
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

    async def wait_run(
        self,
        thread_id: str,
        *,
        assistant_id: str,
        on_disconnect: typing.Optional[RunCreateStreamingStatefulOnDisconnect] = OMIT,
        checkpoint: typing.Optional[CheckpointConfig] = OMIT,
        input: typing.Optional[RunCreateStatefulInput] = OMIT,
        command: typing.Optional[Command] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        config: typing.Optional[RunCreateStatefulConfig] = OMIT,
        context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        webhook: typing.Optional[str] = OMIT,
        interrupt_before: typing.Optional[RunCreateStatefulInterruptBefore] = OMIT,
        interrupt_after: typing.Optional[RunCreateStatefulInterruptAfter] = OMIT,
        stream_mode: typing.Optional[RunCreateStatefulStreamMode] = OMIT,
        stream_subgraphs: typing.Optional[bool] = OMIT,
        stream_resumable: typing.Optional[bool] = OMIT,
        feedback_keys: typing.Optional[typing.Sequence[str]] = OMIT,
        multitask_strategy: typing.Optional[RunCreateStatefulMultitaskStrategy] = OMIT,
        if_not_exists: typing.Optional[RunCreateStatefulIfNotExists] = OMIT,
        after_seconds: typing.Optional[float] = OMIT,
        checkpoint_during: typing.Optional[bool] = OMIT,
        durability: typing.Optional[RunCreateStatefulDurability] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Create a run in existing thread. Wait for the final output and then return it.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        assistant_id : str

        on_disconnect : typing.Optional[RunCreateStreamingStatefulOnDisconnect]
            The disconnect mode to use. Must be one of 'cancel' or 'continue'.

        checkpoint : typing.Optional[CheckpointConfig]
            The checkpoint to resume from.

        input : typing.Optional[RunCreateStatefulInput]
            The input to the graph.

        command : typing.Optional[Command]
            The input to the graph.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to assign to the run.

        config : typing.Optional[RunCreateStatefulConfig]
            The configuration for the assistant.

        context : typing.Optional[typing.Dict[str, typing.Any]]
            Static context added to the assistant.

        webhook : typing.Optional[str]
            Webhook to call after LangGraph API call is done.

        interrupt_before : typing.Optional[RunCreateStatefulInterruptBefore]
            Nodes to interrupt immediately before they get executed.

        interrupt_after : typing.Optional[RunCreateStatefulInterruptAfter]
            Nodes to interrupt immediately after they get executed.

        stream_mode : typing.Optional[RunCreateStatefulStreamMode]
            The stream mode(s) to use.

        stream_subgraphs : typing.Optional[bool]
            Whether to stream output from subgraphs.

        stream_resumable : typing.Optional[bool]
            Whether to persist the stream chunks in order to resume the stream later.

        feedback_keys : typing.Optional[typing.Sequence[str]]
            Generate pre-signed URLs for assigning feedback keys to the run.

            For each key specified, a unique URL will be generated that can be called to assign the feedback key to the run. See [LangSmith Feedback](https://docs.langchain.com/langsmith/observability-concepts#feedback) for more details.

        multitask_strategy : typing.Optional[RunCreateStatefulMultitaskStrategy]
            Multitask strategy to use. Must be one of 'reject', 'interrupt', 'rollback', or 'enqueue'.

        if_not_exists : typing.Optional[RunCreateStatefulIfNotExists]
            How to handle missing thread. Must be either 'reject' (raise error if missing), or 'create' (create new thread).

        after_seconds : typing.Optional[float]
            The number of seconds to wait before starting the run. Use to schedule future runs.

        checkpoint_during : typing.Optional[bool]
            Whether to checkpoint during the run.

            Deprecated. Use `durability` instead to control checkpoint persistence behavior during the run.

        durability : typing.Optional[RunCreateStatefulDurability]
            Durability level for the run. Must be one of `sync`, `async`, or `exit`. See [durability modes](https://docs.langchain.com/oss/python/langgraph/durable-execution#durability-modes) for more details.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/runs/wait",
            method="POST",
            json={
                "on_disconnect": on_disconnect,
                "assistant_id": assistant_id,
                "checkpoint": convert_and_respect_annotation_metadata(
                    object_=checkpoint, annotation=CheckpointConfig, direction="write"
                ),
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=typing.Optional[RunCreateStatefulInput], direction="write"
                ),
                "command": convert_and_respect_annotation_metadata(
                    object_=command, annotation=typing.Optional[Command], direction="write"
                ),
                "metadata": metadata,
                "config": convert_and_respect_annotation_metadata(
                    object_=config, annotation=RunCreateStatefulConfig, direction="write"
                ),
                "context": context,
                "webhook": webhook,
                "interrupt_before": convert_and_respect_annotation_metadata(
                    object_=interrupt_before, annotation=RunCreateStatefulInterruptBefore, direction="write"
                ),
                "interrupt_after": convert_and_respect_annotation_metadata(
                    object_=interrupt_after, annotation=RunCreateStatefulInterruptAfter, direction="write"
                ),
                "stream_mode": convert_and_respect_annotation_metadata(
                    object_=stream_mode, annotation=RunCreateStatefulStreamMode, direction="write"
                ),
                "stream_subgraphs": stream_subgraphs,
                "stream_resumable": stream_resumable,
                "feedback_keys": feedback_keys,
                "multitask_strategy": multitask_strategy,
                "if_not_exists": if_not_exists,
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

    async def get_run_http(
        self, thread_id: str, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Run]:
        """
        Get a run by ID.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        run_id : str
            The ID of the run.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Run]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/runs/{encode_path_param(run_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Run,
                    parse_obj_as(
                        type_=Run,
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

    async def delete_run(
        self, thread_id: str, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Delete a run by ID.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        run_id : str
            The ID of the run.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/runs/{encode_path_param(run_id)}",
            method="DELETE",
            request_options=request_options,
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

    async def join_run_http(
        self,
        thread_id: str,
        run_id: str,
        *,
        cancel_on_disconnect: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Wait for a run to finish.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        run_id : str
            The ID of the run.

        cancel_on_disconnect : typing.Optional[bool]
            If true, the run will be cancelled if the client disconnects.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/runs/{encode_path_param(run_id)}/join",
            method="GET",
            params={
                "cancel_on_disconnect": cancel_on_disconnect,
            },
            request_options=request_options,
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
    async def stream_run_http_threads_thread_id_runs_run_id_join_get(
        self,
        thread_id: str,
        run_id: str,
        *,
        stream_mode: typing.Optional[str] = None,
        cancel_on_disconnect: typing.Optional[bool] = None,
        last_event_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[str]]]:
        """
        Join a run stream. This endpoint streams output in real-time from a run similar to the /threads/__THREAD_ID__/runs/stream endpoint. If the run has been created with `stream_resumable=true`, the stream can be resumed from the last seen event ID.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        run_id : str
            The ID of the run.

        stream_mode : typing.Optional[str]
            The mode to stream the run in. If not provided, the default mode will be used.

        cancel_on_disconnect : typing.Optional[bool]
            If true, the run will be cancelled if the client disconnects.

        last_event_id : typing.Optional[str]
            The ID of the last event received. Set to -1 if you want to stream all events. Requires `stream_resumable=true` to be set when creating the run.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[str]]]
            Success
        """
        async with self._client_wrapper.httpx_client.stream(
            f"threads/{encode_path_param(thread_id)}/runs/{encode_path_param(run_id)}/stream",
            method="GET",
            params={
                "stream_mode": stream_mode,
                "cancel_on_disconnect": cancel_on_disconnect,
            },
            headers={
                "Last-Event-ID": str(last_event_id) if last_event_id is not None else None,
            },
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

    async def cancel_run_http(
        self,
        thread_id: str,
        run_id: str,
        *,
        wait: typing.Optional[bool] = None,
        action: typing.Optional[CancelRunHttpThreadsThreadIdRunsRunIdCancelPostRequestAction] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        run_id : str
            The ID of the run.

        wait : typing.Optional[bool]

        action : typing.Optional[CancelRunHttpThreadsThreadIdRunsRunIdCancelPostRequestAction]
            Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. `interrupt` will simply cancel the run. `rollback` will cancel the run and delete the run and associated checkpoints afterwards.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/runs/{encode_path_param(run_id)}/cancel",
            method="POST",
            params={
                "wait": wait,
                "action": action,
            },
            request_options=request_options,
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

    async def cancel_runs_post(
        self,
        *,
        action: typing.Optional[CancelRunsPostRequestAction] = None,
        status: typing.Optional[RunsCancelStatus] = OMIT,
        thread_id: typing.Optional[str] = OMIT,
        run_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Cancel one or more runs. Can cancel runs by thread ID and run IDs, or by status filter.

        Parameters
        ----------
        action : typing.Optional[CancelRunsPostRequestAction]
            Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. `interrupt` will simply cancel the run. `rollback` will cancel the run and delete the run and associated checkpoints afterwards.

        status : typing.Optional[RunsCancelStatus]
            Filter runs by status to cancel. Must be one of 'pending', 'running', or 'all'.

        thread_id : typing.Optional[str]
            The ID of the thread containing runs to cancel.

        run_ids : typing.Optional[typing.Sequence[str]]
            List of run IDs to cancel.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "runs/cancel",
            method="POST",
            params={
                "action": action,
            },
            json={
                "status": status,
                "thread_id": thread_id,
                "run_ids": run_ids,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
