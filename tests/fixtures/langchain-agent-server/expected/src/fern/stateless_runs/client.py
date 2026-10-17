

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.command import Command
from ..types.run_batch_create import RunBatchCreate
from ..types.run_create_stateless_config import RunCreateStatelessConfig
from ..types.run_create_stateless_durability import RunCreateStatelessDurability
from ..types.run_create_stateless_input import RunCreateStatelessInput
from ..types.run_create_stateless_on_completion import RunCreateStatelessOnCompletion
from ..types.run_create_stateless_stream_mode import RunCreateStatelessStreamMode
from ..types.run_create_streaming_stateless_on_disconnect import RunCreateStreamingStatelessOnDisconnect
from .raw_client import AsyncRawStatelessRunsClient, RawStatelessRunsClient


OMIT = typing.cast(typing.Any, ...)


class StatelessRunsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStatelessRunsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStatelessRunsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStatelessRunsClient
        """
        return self._raw_client

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
    ) -> typing.Iterator[str]:
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
        typing.Iterator[str]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.stateless_runs.stream_run_stateless(
            assistant_id="assistant_id",
        )
        for chunk in response:
            yield chunk
        """
        with self._raw_client.stream_run_stateless(
            assistant_id=assistant_id,
            on_disconnect=on_disconnect,
            input=input,
            command=command,
            metadata=metadata,
            config=config,
            context=context,
            webhook=webhook,
            stream_mode=stream_mode,
            feedback_keys=feedback_keys,
            stream_subgraphs=stream_subgraphs,
            stream_resumable=stream_resumable,
            on_completion=on_completion,
            after_seconds=after_seconds,
            checkpoint_during=checkpoint_during,
            durability=durability,
            request_options=request_options,
        ) as r:
            yield from r.data

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
    ) -> typing.Any:
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
        typing.Any
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.stateless_runs.wait_run_stateless(
            assistant_id="assistant_id",
        )
        """
        _response = self._raw_client.wait_run_stateless(
            assistant_id=assistant_id,
            on_disconnect=on_disconnect,
            input=input,
            command=command,
            metadata=metadata,
            config=config,
            context=context,
            webhook=webhook,
            stream_mode=stream_mode,
            feedback_keys=feedback_keys,
            stream_subgraphs=stream_subgraphs,
            stream_resumable=stream_resumable,
            on_completion=on_completion,
            after_seconds=after_seconds,
            checkpoint_during=checkpoint_during,
            durability=durability,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Any:
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
        typing.Any
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.stateless_runs.run_stateless(
            assistant_id="assistant_id",
        )
        """
        _response = self._raw_client.run_stateless(
            assistant_id=assistant_id,
            input=input,
            command=command,
            metadata=metadata,
            config=config,
            context=context,
            webhook=webhook,
            stream_mode=stream_mode,
            feedback_keys=feedback_keys,
            stream_subgraphs=stream_subgraphs,
            stream_resumable=stream_resumable,
            on_completion=on_completion,
            after_seconds=after_seconds,
            checkpoint_during=checkpoint_during,
            durability=durability,
            request_options=request_options,
        )
        return _response.data

    def run_batch_stateless_runs_post(
        self, *, request: RunBatchCreate, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Create a batch of runs and return immediately.

        Parameters
        ----------
        request : RunBatchCreate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Success

        Examples
        --------
        from fern import FernApi, RunCreateStateless

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.stateless_runs.run_batch_stateless_runs_post(
            request=[
                RunCreateStateless(
                    assistant_id="assistant_id",
                )
            ],
        )
        """
        _response = self._raw_client.run_batch_stateless_runs_post(request=request, request_options=request_options)
        return _response.data


class AsyncStatelessRunsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStatelessRunsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStatelessRunsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStatelessRunsClient
        """
        return self._raw_client

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
    ) -> typing.AsyncIterator[str]:
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
            response = await client.stateless_runs.stream_run_stateless(
                assistant_id="assistant_id",
            )
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.stream_run_stateless(
            assistant_id=assistant_id,
            on_disconnect=on_disconnect,
            input=input,
            command=command,
            metadata=metadata,
            config=config,
            context=context,
            webhook=webhook,
            stream_mode=stream_mode,
            feedback_keys=feedback_keys,
            stream_subgraphs=stream_subgraphs,
            stream_resumable=stream_resumable,
            on_completion=on_completion,
            after_seconds=after_seconds,
            checkpoint_during=checkpoint_during,
            durability=durability,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk

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
    ) -> typing.Any:
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
            await client.stateless_runs.wait_run_stateless(
                assistant_id="assistant_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.wait_run_stateless(
            assistant_id=assistant_id,
            on_disconnect=on_disconnect,
            input=input,
            command=command,
            metadata=metadata,
            config=config,
            context=context,
            webhook=webhook,
            stream_mode=stream_mode,
            feedback_keys=feedback_keys,
            stream_subgraphs=stream_subgraphs,
            stream_resumable=stream_resumable,
            on_completion=on_completion,
            after_seconds=after_seconds,
            checkpoint_during=checkpoint_during,
            durability=durability,
            request_options=request_options,
        )
        return _response.data

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
    ) -> typing.Any:
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
            await client.stateless_runs.run_stateless(
                assistant_id="assistant_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.run_stateless(
            assistant_id=assistant_id,
            input=input,
            command=command,
            metadata=metadata,
            config=config,
            context=context,
            webhook=webhook,
            stream_mode=stream_mode,
            feedback_keys=feedback_keys,
            stream_subgraphs=stream_subgraphs,
            stream_resumable=stream_resumable,
            on_completion=on_completion,
            after_seconds=after_seconds,
            checkpoint_during=checkpoint_during,
            durability=durability,
            request_options=request_options,
        )
        return _response.data

    async def run_batch_stateless_runs_post(
        self, *, request: RunBatchCreate, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Create a batch of runs and return immediately.

        Parameters
        ----------
        request : RunBatchCreate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, RunCreateStateless

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.stateless_runs.run_batch_stateless_runs_post(
                request=[
                    RunCreateStateless(
                        assistant_id="assistant_id",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.run_batch_stateless_runs_post(
            request=request, request_options=request_options
        )
        return _response.data
