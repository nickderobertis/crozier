

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.checkpoint_config import CheckpointConfig
from ..types.command import Command
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
from ..types.runs_cancel import RunsCancel
from .raw_client import AsyncRawThreadRunsClient, RawThreadRunsClient
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


OMIT = typing.cast(typing.Any, ...)


class ThreadRunsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawThreadRunsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawThreadRunsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawThreadRunsClient
        """
        return self._raw_client

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
    ) -> typing.List[Run]:
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

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Run]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.thread_runs.list_runs_http(
            thread_id="thread_id",
        )
        """
        _response = self._raw_client.list_runs_http(
            thread_id, limit=limit, offset=offset, status=status, select=select, request_options=request_options
        )
        return _response.data

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
    ) -> Run:
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
        Run
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.thread_runs.create_run(
            thread_id="thread_id",
            assistant_id="assistant_id",
        )
        """
        _response = self._raw_client.create_run(
            thread_id,
            assistant_id=assistant_id,
            checkpoint=checkpoint,
            input=input,
            command=command,
            metadata=metadata,
            config=config,
            context=context,
            webhook=webhook,
            interrupt_before=interrupt_before,
            interrupt_after=interrupt_after,
            stream_mode=stream_mode,
            stream_subgraphs=stream_subgraphs,
            stream_resumable=stream_resumable,
            feedback_keys=feedback_keys,
            multitask_strategy=multitask_strategy,
            if_not_exists=if_not_exists,
            after_seconds=after_seconds,
            checkpoint_during=checkpoint_during,
            durability=durability,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Iterator[str]:
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
        typing.Iterator[str]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.thread_runs.stream_run(
            thread_id="thread_id",
            assistant_id="assistant_id",
        )
        for chunk in response:
            yield chunk
        """
        with self._raw_client.stream_run(
            thread_id,
            assistant_id=assistant_id,
            on_disconnect=on_disconnect,
            checkpoint=checkpoint,
            input=input,
            command=command,
            metadata=metadata,
            config=config,
            context=context,
            webhook=webhook,
            interrupt_before=interrupt_before,
            interrupt_after=interrupt_after,
            stream_mode=stream_mode,
            stream_subgraphs=stream_subgraphs,
            stream_resumable=stream_resumable,
            feedback_keys=feedback_keys,
            multitask_strategy=multitask_strategy,
            if_not_exists=if_not_exists,
            after_seconds=after_seconds,
            checkpoint_during=checkpoint_during,
            durability=durability,
            request_options=request_options,
        ) as r:
            yield from r.data

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
    ) -> typing.Any:
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
        typing.Any
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.thread_runs.wait_run(
            thread_id="thread_id",
            assistant_id="assistant_id",
        )
        """
        _response = self._raw_client.wait_run(
            thread_id,
            assistant_id=assistant_id,
            on_disconnect=on_disconnect,
            checkpoint=checkpoint,
            input=input,
            command=command,
            metadata=metadata,
            config=config,
            context=context,
            webhook=webhook,
            interrupt_before=interrupt_before,
            interrupt_after=interrupt_after,
            stream_mode=stream_mode,
            stream_subgraphs=stream_subgraphs,
            stream_resumable=stream_resumable,
            feedback_keys=feedback_keys,
            multitask_strategy=multitask_strategy,
            if_not_exists=if_not_exists,
            after_seconds=after_seconds,
            checkpoint_during=checkpoint_during,
            durability=durability,
            request_options=request_options,
        )
        return _response.data

    def get_run_http(
        self, thread_id: str, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Run:
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
        Run
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.thread_runs.get_run_http(
            thread_id="thread_id",
            run_id="run_id",
        )
        """
        _response = self._raw_client.get_run_http(thread_id, run_id, request_options=request_options)
        return _response.data

    def delete_run(
        self, thread_id: str, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
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
        typing.Any
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.thread_runs.delete_run(
            thread_id="thread_id",
            run_id="run_id",
        )
        """
        _response = self._raw_client.delete_run(thread_id, run_id, request_options=request_options)
        return _response.data

    def join_run_http(
        self,
        thread_id: str,
        run_id: str,
        *,
        cancel_on_disconnect: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Wait for a run to finish.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        run_id : str
            The ID of the run.

        cancel_on_disconnect : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.thread_runs.join_run_http(
            thread_id="thread_id",
            run_id="run_id",
        )
        """
        _response = self._raw_client.join_run_http(
            thread_id, run_id, cancel_on_disconnect=cancel_on_disconnect, request_options=request_options
        )
        return _response.data

    def stream_run_http_threads_thread_id_runs_run_id_join_get(
        self,
        thread_id: str,
        run_id: str,
        *,
        stream_mode: typing.Optional[str] = None,
        cancel_on_disconnect: typing.Optional[bool] = None,
        last_event_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[str]:
        """
        Join a run stream. This endpoint streams output in real-time from a run similar to the /threads/__THREAD_ID__/runs/stream endpoint. If the run has been created with `stream_resumable=true`, the stream can be resumed from the last seen event ID.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        run_id : str
            The ID of the run.

        stream_mode : typing.Optional[str]

        cancel_on_disconnect : typing.Optional[bool]

        last_event_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[str]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        response = (
            client.thread_runs.stream_run_http_threads_thread_id_runs_run_id_join_get(
                thread_id="thread_id",
                run_id="run_id",
            )
        )
        for chunk in response:
            yield chunk
        """
        with self._raw_client.stream_run_http_threads_thread_id_runs_run_id_join_get(
            thread_id,
            run_id,
            stream_mode=stream_mode,
            cancel_on_disconnect=cancel_on_disconnect,
            last_event_id=last_event_id,
            request_options=request_options,
        ) as r:
            yield from r.data

    def cancel_run_http(
        self,
        thread_id: str,
        run_id: str,
        *,
        wait: typing.Optional[bool] = None,
        action: typing.Optional[CancelRunHttpThreadsThreadIdRunsRunIdCancelPostRequestAction] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
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
        typing.Any
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.thread_runs.cancel_run_http(
            thread_id="thread_id",
            run_id="run_id",
        )
        """
        _response = self._raw_client.cancel_run_http(
            thread_id, run_id, wait=wait, action=action, request_options=request_options
        )
        return _response.data

    def cancel_runs_post(
        self,
        *,
        request: RunsCancel,
        action: typing.Optional[CancelRunsPostRequestAction] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Cancel one or more runs. Can cancel runs by thread ID and run IDs, or by status filter.

        Parameters
        ----------
        request : RunsCancel

        action : typing.Optional[CancelRunsPostRequestAction]
            Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. `interrupt` will simply cancel the run. `rollback` will cancel the run and delete the run and associated checkpoints afterwards.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.thread_runs.cancel_runs_post(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.cancel_runs_post(request=request, action=action, request_options=request_options)
        return _response.data


class AsyncThreadRunsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawThreadRunsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawThreadRunsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawThreadRunsClient
        """
        return self._raw_client

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
    ) -> typing.List[Run]:
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

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Run]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.thread_runs.list_runs_http(
                thread_id="thread_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_runs_http(
            thread_id, limit=limit, offset=offset, status=status, select=select, request_options=request_options
        )
        return _response.data

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
    ) -> Run:
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
        Run
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.thread_runs.create_run(
                thread_id="thread_id",
                assistant_id="assistant_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_run(
            thread_id,
            assistant_id=assistant_id,
            checkpoint=checkpoint,
            input=input,
            command=command,
            metadata=metadata,
            config=config,
            context=context,
            webhook=webhook,
            interrupt_before=interrupt_before,
            interrupt_after=interrupt_after,
            stream_mode=stream_mode,
            stream_subgraphs=stream_subgraphs,
            stream_resumable=stream_resumable,
            feedback_keys=feedback_keys,
            multitask_strategy=multitask_strategy,
            if_not_exists=if_not_exists,
            after_seconds=after_seconds,
            checkpoint_during=checkpoint_during,
            durability=durability,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.AsyncIterator[str]:
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
        typing.AsyncIterator[str]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            response = await client.thread_runs.stream_run(
                thread_id="thread_id",
                assistant_id="assistant_id",
            )
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.stream_run(
            thread_id,
            assistant_id=assistant_id,
            on_disconnect=on_disconnect,
            checkpoint=checkpoint,
            input=input,
            command=command,
            metadata=metadata,
            config=config,
            context=context,
            webhook=webhook,
            interrupt_before=interrupt_before,
            interrupt_after=interrupt_after,
            stream_mode=stream_mode,
            stream_subgraphs=stream_subgraphs,
            stream_resumable=stream_resumable,
            feedback_keys=feedback_keys,
            multitask_strategy=multitask_strategy,
            if_not_exists=if_not_exists,
            after_seconds=after_seconds,
            checkpoint_during=checkpoint_during,
            durability=durability,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk

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
    ) -> typing.Any:
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
        typing.Any
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.thread_runs.wait_run(
                thread_id="thread_id",
                assistant_id="assistant_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.wait_run(
            thread_id,
            assistant_id=assistant_id,
            on_disconnect=on_disconnect,
            checkpoint=checkpoint,
            input=input,
            command=command,
            metadata=metadata,
            config=config,
            context=context,
            webhook=webhook,
            interrupt_before=interrupt_before,
            interrupt_after=interrupt_after,
            stream_mode=stream_mode,
            stream_subgraphs=stream_subgraphs,
            stream_resumable=stream_resumable,
            feedback_keys=feedback_keys,
            multitask_strategy=multitask_strategy,
            if_not_exists=if_not_exists,
            after_seconds=after_seconds,
            checkpoint_during=checkpoint_during,
            durability=durability,
            request_options=request_options,
        )
        return _response.data

    async def get_run_http(
        self, thread_id: str, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Run:
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
        Run
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.thread_runs.get_run_http(
                thread_id="thread_id",
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_run_http(thread_id, run_id, request_options=request_options)
        return _response.data

    async def delete_run(
        self, thread_id: str, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
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
        typing.Any
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.thread_runs.delete_run(
                thread_id="thread_id",
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_run(thread_id, run_id, request_options=request_options)
        return _response.data

    async def join_run_http(
        self,
        thread_id: str,
        run_id: str,
        *,
        cancel_on_disconnect: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Wait for a run to finish.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        run_id : str
            The ID of the run.

        cancel_on_disconnect : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.thread_runs.join_run_http(
                thread_id="thread_id",
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.join_run_http(
            thread_id, run_id, cancel_on_disconnect=cancel_on_disconnect, request_options=request_options
        )
        return _response.data

    async def stream_run_http_threads_thread_id_runs_run_id_join_get(
        self,
        thread_id: str,
        run_id: str,
        *,
        stream_mode: typing.Optional[str] = None,
        cancel_on_disconnect: typing.Optional[bool] = None,
        last_event_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[str]:
        """
        Join a run stream. This endpoint streams output in real-time from a run similar to the /threads/__THREAD_ID__/runs/stream endpoint. If the run has been created with `stream_resumable=true`, the stream can be resumed from the last seen event ID.

        Parameters
        ----------
        thread_id : str
            The ID of the thread.

        run_id : str
            The ID of the run.

        stream_mode : typing.Optional[str]

        cancel_on_disconnect : typing.Optional[bool]

        last_event_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[str]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            response = await client.thread_runs.stream_run_http_threads_thread_id_runs_run_id_join_get(
                thread_id="thread_id",
                run_id="run_id",
            )
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.stream_run_http_threads_thread_id_runs_run_id_join_get(
            thread_id,
            run_id,
            stream_mode=stream_mode,
            cancel_on_disconnect=cancel_on_disconnect,
            last_event_id=last_event_id,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def cancel_run_http(
        self,
        thread_id: str,
        run_id: str,
        *,
        wait: typing.Optional[bool] = None,
        action: typing.Optional[CancelRunHttpThreadsThreadIdRunsRunIdCancelPostRequestAction] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
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
        typing.Any
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.thread_runs.cancel_run_http(
                thread_id="thread_id",
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_run_http(
            thread_id, run_id, wait=wait, action=action, request_options=request_options
        )
        return _response.data

    async def cancel_runs_post(
        self,
        *,
        request: RunsCancel,
        action: typing.Optional[CancelRunsPostRequestAction] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Cancel one or more runs. Can cancel runs by thread ID and run IDs, or by status filter.

        Parameters
        ----------
        request : RunsCancel

        action : typing.Optional[CancelRunsPostRequestAction]
            Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. `interrupt` will simply cancel the run. `rollback` will cancel the run and delete the run and associated checkpoints afterwards.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.thread_runs.cancel_runs_post(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_runs_post(
            request=request, action=action, request_options=request_options
        )
        return _response.data
