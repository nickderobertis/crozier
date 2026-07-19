

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.letta_message_union import LettaMessageUnion
from ..types.run import Run
from ..types.run_metrics import RunMetrics
from ..types.step import Step
from ..types.stop_reason_type import StopReasonType
from ..types.usage_statistics import UsageStatistics
from .raw_client import AsyncRawRunsClient, RawRunsClient
from .types.list_messages_for_run_request_order import ListMessagesForRunRequestOrder
from .types.list_messages_for_run_request_order_by import ListMessagesForRunRequestOrderBy
from .types.list_runs_request_order import ListRunsRequestOrder
from .types.list_runs_request_order_by import ListRunsRequestOrderBy
from .types.list_steps_for_run_request_order import ListStepsForRunRequestOrder
from .types.list_steps_for_run_request_order_by import ListStepsForRunRequestOrderBy


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

    def list_runs(
        self,
        *,
        agent_id: typing.Optional[str] = None,
        agent_ids: typing.Optional[typing.Sequence[str]] = None,
        statuses: typing.Optional[typing.Sequence[str]] = None,
        background: typing.Optional[bool] = None,
        stop_reason: typing.Optional[StopReasonType] = None,
        conversation_id: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListRunsRequestOrder] = None,
        order_by: typing.Optional[ListRunsRequestOrderBy] = None,
        active: typing.Optional[bool] = None,
        ascending: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Run]:
        """
        List all runs.

        Parameters
        ----------
        agent_id : typing.Optional[str]
            The unique identifier of the agent associated with the run.

        agent_ids : typing.Optional[typing.Sequence[str]]
            The unique identifiers of the agents associated with the run. Deprecated in favor of agent_id field.

        statuses : typing.Optional[typing.Sequence[str]]
            Filter runs by status. Can specify multiple statuses.

        background : typing.Optional[bool]
            If True, filters for runs that were created in background mode.

        stop_reason : typing.Optional[StopReasonType]
            Filter runs by stop reason.

        conversation_id : typing.Optional[str]
            Filter runs by conversation ID.

        before : typing.Optional[str]
            Run ID cursor for pagination. Returns runs that come before this run ID in the specified sort order

        after : typing.Optional[str]
            Run ID cursor for pagination. Returns runs that come after this run ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of runs to return

        order : typing.Optional[ListRunsRequestOrder]
            Sort order for runs by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListRunsRequestOrderBy]
            Field to sort by

        active : typing.Optional[bool]
            Filter for active runs.

        ascending : typing.Optional[bool]
            Whether to sort agents oldest to newest (True) or newest to oldest (False, default). Deprecated in favor of order field.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Run]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.runs.list_runs()
        """
        _response = self._raw_client.list_runs(
            agent_id=agent_id,
            agent_ids=agent_ids,
            statuses=statuses,
            background=background,
            stop_reason=stop_reason,
            conversation_id=conversation_id,
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            active=active,
            ascending=ascending,
            request_options=request_options,
        )
        return _response.data

    def list_active_runs(
        self,
        *,
        agent_id: typing.Optional[str] = None,
        background: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Run]:
        """
        List all active runs.

        Parameters
        ----------
        agent_id : typing.Optional[str]
            The unique identifier of the agent associated with the run.

        background : typing.Optional[bool]
            If True, filters for runs that were created in background mode.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Run]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.runs.list_active_runs()
        """
        _response = self._raw_client.list_active_runs(
            agent_id=agent_id, background=background, request_options=request_options
        )
        return _response.data

    def retrieve_run(self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Run:
        """
        Get the status of a run.

        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Run
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.runs.retrieve_run(
            run_id="run_id",
        )
        """
        _response = self._raw_client.retrieve_run(run_id, request_options=request_options)
        return _response.data

    def delete_run(self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Delete a run by its run_id.

        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.runs.delete_run(
            run_id="run_id",
        )
        """
        _response = self._raw_client.delete_run(run_id, request_options=request_options)
        return _response.data

    def list_messages_for_run(
        self,
        run_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListMessagesForRunRequestOrder] = None,
        order_by: typing.Optional[ListMessagesForRunRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[LettaMessageUnion]:
        """
        Get response messages associated with a run.

        Parameters
        ----------
        run_id : str

        before : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come before this message ID in the specified sort order

        after : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come after this message ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of messages to return

        order : typing.Optional[ListMessagesForRunRequestOrder]
            Sort order for messages by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListMessagesForRunRequestOrderBy]
            Field to sort by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[LettaMessageUnion]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.runs.list_messages_for_run(
            run_id="run_id",
        )
        """
        _response = self._raw_client.list_messages_for_run(
            run_id,
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data

    def retrieve_usage_for_run(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UsageStatistics:
        """
        Get usage statistics for a run.

        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsageStatistics
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.runs.retrieve_usage_for_run(
            run_id="run_id",
        )
        """
        _response = self._raw_client.retrieve_usage_for_run(run_id, request_options=request_options)
        return _response.data

    def retrieve_metrics_for_run(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RunMetrics:
        """
        Get run metrics by run ID.

        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RunMetrics
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.runs.retrieve_metrics_for_run(
            run_id="run_id",
        )
        """
        _response = self._raw_client.retrieve_metrics_for_run(run_id, request_options=request_options)
        return _response.data

    def list_steps_for_run(
        self,
        run_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListStepsForRunRequestOrder] = None,
        order_by: typing.Optional[ListStepsForRunRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Step]:
        """
        Get steps associated with a run with filtering options.

        Parameters
        ----------
        run_id : str

        before : typing.Optional[str]
            Cursor for pagination

        after : typing.Optional[str]
            Cursor for pagination

        limit : typing.Optional[int]
            Maximum number of messages to return

        order : typing.Optional[ListStepsForRunRequestOrder]
            Sort order for steps by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListStepsForRunRequestOrderBy]
            Field to sort by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Step]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.runs.list_steps_for_run(
            run_id="run_id",
        )
        """
        _response = self._raw_client.list_steps_for_run(
            run_id,
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data

    def retrieve_trace_for_run(
        self,
        run_id: str,
        *,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[typing.Dict[str, typing.Any]]:
        """
        Retrieve OTEL trace spans for a run.

        Returns a filtered set of spans relevant for observability:
        - agent_step: Individual agent reasoning steps
        - tool executions: Tool call spans
        - Root span: The top-level request span
        - time_to_first_token: TTFT measurement span

        Requires ClickHouse to be configured for trace storage.

        Parameters
        ----------
        run_id : str

        limit : typing.Optional[int]
            Maximum number of spans to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Dict[str, typing.Any]]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.runs.retrieve_trace_for_run(
            run_id="run_id",
        )
        """
        _response = self._raw_client.retrieve_trace_for_run(run_id, limit=limit, request_options=request_options)
        return _response.data

    def retrieve_stream_for_run(
        self,
        run_id: str,
        *,
        starting_after: typing.Optional[int] = OMIT,
        include_pings: typing.Optional[bool] = OMIT,
        poll_interval: typing.Optional[float] = OMIT,
        batch_size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        run_id : str

        starting_after : typing.Optional[int]
            Sequence id to use as a cursor for pagination. Response will start streaming after this chunk sequence id

        include_pings : typing.Optional[bool]
            Whether to include periodic keepalive ping messages in the stream to prevent connection timeouts.

        poll_interval : typing.Optional[float]
            Seconds to wait between polls when no new data.

        batch_size : typing.Optional[int]
            Number of entries to read per batch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.runs.retrieve_stream_for_run(
            run_id="run_id",
        )
        """
        _response = self._raw_client.retrieve_stream_for_run(
            run_id,
            starting_after=starting_after,
            include_pings=include_pings,
            poll_interval=poll_interval,
            batch_size=batch_size,
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

    async def list_runs(
        self,
        *,
        agent_id: typing.Optional[str] = None,
        agent_ids: typing.Optional[typing.Sequence[str]] = None,
        statuses: typing.Optional[typing.Sequence[str]] = None,
        background: typing.Optional[bool] = None,
        stop_reason: typing.Optional[StopReasonType] = None,
        conversation_id: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListRunsRequestOrder] = None,
        order_by: typing.Optional[ListRunsRequestOrderBy] = None,
        active: typing.Optional[bool] = None,
        ascending: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Run]:
        """
        List all runs.

        Parameters
        ----------
        agent_id : typing.Optional[str]
            The unique identifier of the agent associated with the run.

        agent_ids : typing.Optional[typing.Sequence[str]]
            The unique identifiers of the agents associated with the run. Deprecated in favor of agent_id field.

        statuses : typing.Optional[typing.Sequence[str]]
            Filter runs by status. Can specify multiple statuses.

        background : typing.Optional[bool]
            If True, filters for runs that were created in background mode.

        stop_reason : typing.Optional[StopReasonType]
            Filter runs by stop reason.

        conversation_id : typing.Optional[str]
            Filter runs by conversation ID.

        before : typing.Optional[str]
            Run ID cursor for pagination. Returns runs that come before this run ID in the specified sort order

        after : typing.Optional[str]
            Run ID cursor for pagination. Returns runs that come after this run ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of runs to return

        order : typing.Optional[ListRunsRequestOrder]
            Sort order for runs by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListRunsRequestOrderBy]
            Field to sort by

        active : typing.Optional[bool]
            Filter for active runs.

        ascending : typing.Optional[bool]
            Whether to sort agents oldest to newest (True) or newest to oldest (False, default). Deprecated in favor of order field.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Run]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.runs.list_runs()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_runs(
            agent_id=agent_id,
            agent_ids=agent_ids,
            statuses=statuses,
            background=background,
            stop_reason=stop_reason,
            conversation_id=conversation_id,
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            active=active,
            ascending=ascending,
            request_options=request_options,
        )
        return _response.data

    async def list_active_runs(
        self,
        *,
        agent_id: typing.Optional[str] = None,
        background: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Run]:
        """
        List all active runs.

        Parameters
        ----------
        agent_id : typing.Optional[str]
            The unique identifier of the agent associated with the run.

        background : typing.Optional[bool]
            If True, filters for runs that were created in background mode.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Run]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.runs.list_active_runs()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_active_runs(
            agent_id=agent_id, background=background, request_options=request_options
        )
        return _response.data

    async def retrieve_run(self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Run:
        """
        Get the status of a run.

        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Run
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.runs.retrieve_run(
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_run(run_id, request_options=request_options)
        return _response.data

    async def delete_run(self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Delete a run by its run_id.

        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.runs.delete_run(
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_run(run_id, request_options=request_options)
        return _response.data

    async def list_messages_for_run(
        self,
        run_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListMessagesForRunRequestOrder] = None,
        order_by: typing.Optional[ListMessagesForRunRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[LettaMessageUnion]:
        """
        Get response messages associated with a run.

        Parameters
        ----------
        run_id : str

        before : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come before this message ID in the specified sort order

        after : typing.Optional[str]
            Message ID cursor for pagination. Returns messages that come after this message ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of messages to return

        order : typing.Optional[ListMessagesForRunRequestOrder]
            Sort order for messages by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListMessagesForRunRequestOrderBy]
            Field to sort by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[LettaMessageUnion]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.runs.list_messages_for_run(
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_messages_for_run(
            run_id,
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data

    async def retrieve_usage_for_run(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UsageStatistics:
        """
        Get usage statistics for a run.

        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsageStatistics
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.runs.retrieve_usage_for_run(
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_usage_for_run(run_id, request_options=request_options)
        return _response.data

    async def retrieve_metrics_for_run(
        self, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RunMetrics:
        """
        Get run metrics by run ID.

        Parameters
        ----------
        run_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RunMetrics
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.runs.retrieve_metrics_for_run(
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_metrics_for_run(run_id, request_options=request_options)
        return _response.data

    async def list_steps_for_run(
        self,
        run_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListStepsForRunRequestOrder] = None,
        order_by: typing.Optional[ListStepsForRunRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Step]:
        """
        Get steps associated with a run with filtering options.

        Parameters
        ----------
        run_id : str

        before : typing.Optional[str]
            Cursor for pagination

        after : typing.Optional[str]
            Cursor for pagination

        limit : typing.Optional[int]
            Maximum number of messages to return

        order : typing.Optional[ListStepsForRunRequestOrder]
            Sort order for steps by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListStepsForRunRequestOrderBy]
            Field to sort by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Step]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.runs.list_steps_for_run(
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_steps_for_run(
            run_id,
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data

    async def retrieve_trace_for_run(
        self,
        run_id: str,
        *,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[typing.Dict[str, typing.Any]]:
        """
        Retrieve OTEL trace spans for a run.

        Returns a filtered set of spans relevant for observability:
        - agent_step: Individual agent reasoning steps
        - tool executions: Tool call spans
        - Root span: The top-level request span
        - time_to_first_token: TTFT measurement span

        Requires ClickHouse to be configured for trace storage.

        Parameters
        ----------
        run_id : str

        limit : typing.Optional[int]
            Maximum number of spans to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Dict[str, typing.Any]]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.runs.retrieve_trace_for_run(
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_trace_for_run(run_id, limit=limit, request_options=request_options)
        return _response.data

    async def retrieve_stream_for_run(
        self,
        run_id: str,
        *,
        starting_after: typing.Optional[int] = OMIT,
        include_pings: typing.Optional[bool] = OMIT,
        poll_interval: typing.Optional[float] = OMIT,
        batch_size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        run_id : str

        starting_after : typing.Optional[int]
            Sequence id to use as a cursor for pagination. Response will start streaming after this chunk sequence id

        include_pings : typing.Optional[bool]
            Whether to include periodic keepalive ping messages in the stream to prevent connection timeouts.

        poll_interval : typing.Optional[float]
            Seconds to wait between polls when no new data.

        batch_size : typing.Optional[int]
            Number of entries to read per batch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.runs.retrieve_stream_for_run(
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_stream_for_run(
            run_id,
            starting_after=starting_after,
            include_pings=include_pings,
            poll_interval=poll_interval,
            batch_size=batch_size,
            request_options=request_options,
        )
        return _response.data
