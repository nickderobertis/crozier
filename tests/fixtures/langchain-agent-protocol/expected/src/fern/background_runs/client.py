

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.message import Message
from ..types.run import Run
from ..types.run_create_config import RunCreateConfig
from ..types.run_create_if_not_exists import RunCreateIfNotExists
from ..types.run_create_input import RunCreateInput
from ..types.run_create_on_completion import RunCreateOnCompletion
from ..types.run_create_on_disconnect import RunCreateOnDisconnect
from ..types.run_status import RunStatus
from ..types.run_stream_stream_mode import RunStreamStreamMode
from ..types.run_wait_response import RunWaitResponse
from .raw_client import AsyncRawBackgroundRunsClient, RawBackgroundRunsClient
from .types.cancel_run_request_action import CancelRunRequestAction


OMIT = typing.cast(typing.Any, ...)


class BackgroundRunsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBackgroundRunsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBackgroundRunsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBackgroundRunsClient
        """
        return self._raw_client

    def search_runs(
        self,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        status: typing.Optional[RunStatus] = OMIT,
        thread_id: typing.Optional[str] = OMIT,
        agent_id: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Run]:
        """
        List runs for a thread, agent or status

        Parameters
        ----------
        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Run metadata to filter on.

        status : typing.Optional[RunStatus]
            Run status to filter on.

        thread_id : typing.Optional[str]
            The ID of the thread to filter on.

        agent_id : typing.Optional[str]
            The ID of the agent to filter on.

        limit : typing.Optional[int]
            Maximum number to return.

        offset : typing.Optional[int]
            Offset to start from.

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
        client.background_runs.search_runs()
        """
        _response = self._raw_client.search_runs(
            metadata=metadata,
            status=status,
            thread_id=thread_id,
            agent_id=agent_id,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def get_run(self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Run:
        """
        Get a run by ID.

        Parameters
        ----------
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
        client.background_runs.get_run(
            run_id="run_id",
        )
        """
        _response = self._raw_client.get_run(run_id, request_options=request_options)
        return _response.data

    def delete_run(self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a run by ID.

        Parameters
        ----------
        run_id : str
            The ID of the run.

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
        client.background_runs.delete_run(
            run_id="run_id",
        )
        """
        _response = self._raw_client.delete_run(run_id, request_options=request_options)
        return _response.data

    def wait_run(self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> RunWaitResponse:
        """
        Wait for a run to finish, return the final output. If the run already finished, returns its final output immediately.

        Parameters
        ----------
        run_id : str
            The ID of the run.

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
        client.background_runs.wait_run(
            run_id="run_id",
        )
        """
        _response = self._raw_client.wait_run(run_id, request_options=request_options)
        return _response.data

    def stream_run(self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Join the output stream of an existing run. This endpoint streams output in real-time from a run similar to the /threads/__THREAD_ID__/runs/stream endpoint. Only output produced after this endpoint is called will be streamed.

        Parameters
        ----------
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
        client.background_runs.stream_run(
            run_id="run_id",
        )
        """
        _response = self._raw_client.stream_run(run_id, request_options=request_options)
        return _response.data

    def cancel_run(
        self,
        run_id: str,
        *,
        wait: typing.Optional[bool] = None,
        action: typing.Optional[CancelRunRequestAction] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        run_id : str
            The ID of the run.

        wait : typing.Optional[bool]

        action : typing.Optional[CancelRunRequestAction]
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
        client.background_runs.cancel_run(
            run_id="run_id",
        )
        """
        _response = self._raw_client.cancel_run(run_id, wait=wait, action=action, request_options=request_options)
        return _response.data

    def create_run(
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
    ) -> Run:
        """
        Create a run in a new thread, return the run ID immediately. Don't wait for the final run output.

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
        client.background_runs.create_run()
        """
        _response = self._raw_client.create_run(
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
        )
        return _response.data


class AsyncBackgroundRunsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBackgroundRunsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBackgroundRunsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBackgroundRunsClient
        """
        return self._raw_client

    async def search_runs(
        self,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        status: typing.Optional[RunStatus] = OMIT,
        thread_id: typing.Optional[str] = OMIT,
        agent_id: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Run]:
        """
        List runs for a thread, agent or status

        Parameters
        ----------
        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Run metadata to filter on.

        status : typing.Optional[RunStatus]
            Run status to filter on.

        thread_id : typing.Optional[str]
            The ID of the thread to filter on.

        agent_id : typing.Optional[str]
            The ID of the agent to filter on.

        limit : typing.Optional[int]
            Maximum number to return.

        offset : typing.Optional[int]
            Offset to start from.

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
            await client.background_runs.search_runs()


        asyncio.run(main())
        """
        _response = await self._raw_client.search_runs(
            metadata=metadata,
            status=status,
            thread_id=thread_id,
            agent_id=agent_id,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def get_run(self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Run:
        """
        Get a run by ID.

        Parameters
        ----------
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
            await client.background_runs.get_run(
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_run(run_id, request_options=request_options)
        return _response.data

    async def delete_run(self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a run by ID.

        Parameters
        ----------
        run_id : str
            The ID of the run.

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
            await client.background_runs.delete_run(
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_run(run_id, request_options=request_options)
        return _response.data

    async def wait_run(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RunWaitResponse:
        """
        Wait for a run to finish, return the final output. If the run already finished, returns its final output immediately.

        Parameters
        ----------
        run_id : str
            The ID of the run.

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
            await client.background_runs.wait_run(
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.wait_run(run_id, request_options=request_options)
        return _response.data

    async def stream_run(self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Join the output stream of an existing run. This endpoint streams output in real-time from a run similar to the /threads/__THREAD_ID__/runs/stream endpoint. Only output produced after this endpoint is called will be streamed.

        Parameters
        ----------
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
            await client.background_runs.stream_run(
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.stream_run(run_id, request_options=request_options)
        return _response.data

    async def cancel_run(
        self,
        run_id: str,
        *,
        wait: typing.Optional[bool] = None,
        action: typing.Optional[CancelRunRequestAction] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        run_id : str
            The ID of the run.

        wait : typing.Optional[bool]

        action : typing.Optional[CancelRunRequestAction]
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
            await client.background_runs.cancel_run(
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_run(run_id, wait=wait, action=action, request_options=request_options)
        return _response.data

    async def create_run(
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
    ) -> Run:
        """
        Create a run in a new thread, return the run ID immediately. Don't wait for the final run output.

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
            await client.background_runs.create_run()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_run(
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
        )
        return _response.data
