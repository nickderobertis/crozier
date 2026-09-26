

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.message import Message
from ..types.run_create_config import RunCreateConfig
from ..types.run_create_if_not_exists import RunCreateIfNotExists
from ..types.run_create_input import RunCreateInput
from ..types.run_create_on_completion import RunCreateOnCompletion
from ..types.run_create_on_disconnect import RunCreateOnDisconnect
from ..types.run_stream_stream_mode import RunStreamStreamMode
from ..types.run_wait_response import RunWaitResponse
from .raw_client import AsyncRawRunsClient, RawRunsClient


OMIT = typing.cast(typing.Any, ...)


class RunsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRunsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRunsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRunsClient
        """
        return self._raw_client

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
    ) -> typing.Iterator[str]:
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
        typing.Iterator[str]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.runs.create_and_stream_run()
        for chunk in response:
            yield chunk
        """
        with self._raw_client.create_and_stream_run(
            stream_mode=stream_mode,
            thread_id=thread_id,
            agent_id=agent_id,
            input=input,
            messages=messages,
            metadata=metadata,
            config=config,
            webhook=webhook,
            on_completion=on_completion,
            on_disconnect=on_disconnect,
            if_not_exists=if_not_exists,
            request_options=request_options,
        ) as r:
            yield from r.data

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
    ) -> RunWaitResponse:
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
        RunWaitResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.runs.create_and_wait_run()
        """
        _response = self._raw_client.create_and_wait_run(
            thread_id=thread_id,
            agent_id=agent_id,
            input=input,
            messages=messages,
            metadata=metadata,
            config=config,
            webhook=webhook,
            on_completion=on_completion,
            on_disconnect=on_disconnect,
            if_not_exists=if_not_exists,
            request_options=request_options,
        )
        return _response.data


class AsyncRunsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRunsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRunsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRunsClient
        """
        return self._raw_client

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
    ) -> typing.AsyncIterator[str]:
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
            response = await client.runs.create_and_stream_run()
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.create_and_stream_run(
            stream_mode=stream_mode,
            thread_id=thread_id,
            agent_id=agent_id,
            input=input,
            messages=messages,
            metadata=metadata,
            config=config,
            webhook=webhook,
            on_completion=on_completion,
            on_disconnect=on_disconnect,
            if_not_exists=if_not_exists,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk

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
    ) -> RunWaitResponse:
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
        RunWaitResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.runs.create_and_wait_run()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_and_wait_run(
            thread_id=thread_id,
            agent_id=agent_id,
            input=input,
            messages=messages,
            metadata=metadata,
            config=config,
            webhook=webhook,
            on_completion=on_completion,
            on_disconnect=on_disconnect,
            if_not_exists=if_not_exists,
            request_options=request_options,
        )
        return _response.data
