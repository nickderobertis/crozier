

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.replay_response import ReplayResponse
from ..types.run import Run
from .raw_client import AsyncRawRunsClient, RawRunsClient
from .types.create_run_request_plan_tier import CreateRunRequestPlanTier


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

    def create_run(
        self,
        *,
        capabilities: typing.Optional[typing.Sequence[str]] = OMIT,
        plan_tier: typing.Optional[CreateRunRequestPlanTier] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Run:
        """
        Start a new deterministic execution run

        Parameters
        ----------
        capabilities : typing.Optional[typing.Sequence[str]]
            List of capabilities required for this run

        plan_tier : typing.Optional[CreateRunRequestPlanTier]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Run
            Run created successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.runs.create_run(
            capabilities=["tool.read", "tool.write"],
            plan_tier="free",
        )
        """
        _response = self._raw_client.create_run(
            capabilities=capabilities, plan_tier=plan_tier, request_options=request_options
        )
        return _response.data

    def get_run(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Run:
        """
        Retrieve details of a specific run by ID

        Parameters
        ----------
        id : str
            The run ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Run
            Run details

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.runs.get_run(
            id="id",
        )
        """
        _response = self._raw_client.get_run(id, request_options=request_options)
        return _response.data

    def get_run_events(
        self, id: str, *, after: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Retrieve events for a specific run. Supports both standard JSON and
        Server-Sent Events (SSE) streaming via the Accept header.

        Parameters
        ----------
        id : str
            The run ID

        after : typing.Optional[int]
            Event ID to start from (for pagination)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            List of events or SSE stream
        """
        with self._raw_client.get_run_events(id, after=after, request_options=request_options) as r:
            yield from r.data

    def replay_run(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ReplayResponse:
        """
        Replay a run from its event log for verification

        Parameters
        ----------
        id : str
            The run ID to replay

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReplayResponse
            Replay result

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.runs.replay_run(
            id="id",
        )
        """
        _response = self._raw_client.replay_run(id, request_options=request_options)
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

    async def create_run(
        self,
        *,
        capabilities: typing.Optional[typing.Sequence[str]] = OMIT,
        plan_tier: typing.Optional[CreateRunRequestPlanTier] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Run:
        """
        Start a new deterministic execution run

        Parameters
        ----------
        capabilities : typing.Optional[typing.Sequence[str]]
            List of capabilities required for this run

        plan_tier : typing.Optional[CreateRunRequestPlanTier]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Run
            Run created successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.runs.create_run(
                capabilities=["tool.read", "tool.write"],
                plan_tier="free",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_run(
            capabilities=capabilities, plan_tier=plan_tier, request_options=request_options
        )
        return _response.data

    async def get_run(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Run:
        """
        Retrieve details of a specific run by ID

        Parameters
        ----------
        id : str
            The run ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Run
            Run details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.runs.get_run(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_run(id, request_options=request_options)
        return _response.data

    async def get_run_events(
        self, id: str, *, after: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Retrieve events for a specific run. Supports both standard JSON and
        Server-Sent Events (SSE) streaming via the Accept header.

        Parameters
        ----------
        id : str
            The run ID

        after : typing.Optional[int]
            Event ID to start from (for pagination)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            List of events or SSE stream
        """
        async with self._raw_client.get_run_events(id, after=after, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def replay_run(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ReplayResponse:
        """
        Replay a run from its event log for verification

        Parameters
        ----------
        id : str
            The run ID to replay

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReplayResponse
            Replay result

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.runs.replay_run(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.replay_run(id, request_options=request_options)
        return _response.data
