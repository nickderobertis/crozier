

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.comparison_operator import ComparisonOperator
from ..types.run import Run
from ..types.stop_reason_type import StopReasonType
from .raw_client import AsyncRawInternalRunsClient, RawInternalRunsClient
from .types.list_internal_runs_request_duration_operator import ListInternalRunsRequestDurationOperator
from .types.list_internal_runs_request_order import ListInternalRunsRequestOrder
from .types.list_internal_runs_request_order_by import ListInternalRunsRequestOrderBy


class InternalRunsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInternalRunsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInternalRunsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInternalRunsClient
        """
        return self._raw_client

    def list_internal_runs(
        self,
        *,
        run_id: typing.Optional[str] = None,
        agent_id: typing.Optional[str] = None,
        agent_ids: typing.Optional[typing.Sequence[str]] = None,
        statuses: typing.Optional[typing.Sequence[str]] = None,
        background: typing.Optional[bool] = None,
        stop_reason: typing.Optional[StopReasonType] = None,
        template_family: typing.Optional[str] = None,
        step_count: typing.Optional[int] = None,
        step_count_operator: typing.Optional[ComparisonOperator] = None,
        tools_used: typing.Optional[typing.Sequence[str]] = None,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListInternalRunsRequestOrder] = None,
        order_by: typing.Optional[ListInternalRunsRequestOrderBy] = None,
        active: typing.Optional[bool] = None,
        ascending: typing.Optional[bool] = None,
        project_id: typing.Optional[str] = None,
        conversation_id: typing.Optional[str] = None,
        duration_percentile: typing.Optional[int] = None,
        duration_value: typing.Optional[int] = None,
        duration_operator: typing.Optional[ListInternalRunsRequestDurationOperator] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Run]:
        """
        List all runs.

        Parameters
        ----------
        run_id : typing.Optional[str]
            Filter by a specific run ID.

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

        template_family : typing.Optional[str]
            Filter runs by template family (base_template_id).

        step_count : typing.Optional[int]
            Filter runs by step count. Must be provided with step_count_operator.

        step_count_operator : typing.Optional[ComparisonOperator]
            Operator for step_count filter: 'eq' for equals, 'gte' for greater than or equal, 'lte' for less than or equal.

        tools_used : typing.Optional[typing.Sequence[str]]
            Filter runs that used any of the specified tools.

        before : typing.Optional[str]
            Run ID cursor for pagination. Returns runs that come before this run ID in the specified sort order

        after : typing.Optional[str]
            Run ID cursor for pagination. Returns runs that come after this run ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of runs to return

        order : typing.Optional[ListInternalRunsRequestOrder]
            Sort order for runs by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListInternalRunsRequestOrderBy]
            Field to sort by

        active : typing.Optional[bool]
            Filter for active runs.

        ascending : typing.Optional[bool]
            Whether to sort agents oldest to newest (True) or newest to oldest (False, default). Deprecated in favor of order field.

        project_id : typing.Optional[str]
            Filter runs by project ID.

        conversation_id : typing.Optional[str]
            Filter runs by conversation ID.

        duration_percentile : typing.Optional[int]
            Filter runs by duration percentile (1-100). Returns runs slower than this percentile.

        duration_value : typing.Optional[int]
            Duration value in nanoseconds for filtering. Must be used with duration_operator.

        duration_operator : typing.Optional[ListInternalRunsRequestDurationOperator]
            Comparison operator for duration filter: 'gt' (greater than), 'lt' (less than), 'eq' (equals).

        start_date : typing.Optional[dt.datetime]
            Filter runs created on or after this date (ISO 8601 format).

        end_date : typing.Optional[dt.datetime]
            Filter runs created on or before this date (ISO 8601 format).

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
        client.internal_runs.list_internal_runs()
        """
        _response = self._raw_client.list_internal_runs(
            run_id=run_id,
            agent_id=agent_id,
            agent_ids=agent_ids,
            statuses=statuses,
            background=background,
            stop_reason=stop_reason,
            template_family=template_family,
            step_count=step_count,
            step_count_operator=step_count_operator,
            tools_used=tools_used,
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            active=active,
            ascending=ascending,
            project_id=project_id,
            conversation_id=conversation_id,
            duration_percentile=duration_percentile,
            duration_value=duration_value,
            duration_operator=duration_operator,
            start_date=start_date,
            end_date=end_date,
            request_options=request_options,
        )
        return _response.data


class AsyncInternalRunsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInternalRunsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInternalRunsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInternalRunsClient
        """
        return self._raw_client

    async def list_internal_runs(
        self,
        *,
        run_id: typing.Optional[str] = None,
        agent_id: typing.Optional[str] = None,
        agent_ids: typing.Optional[typing.Sequence[str]] = None,
        statuses: typing.Optional[typing.Sequence[str]] = None,
        background: typing.Optional[bool] = None,
        stop_reason: typing.Optional[StopReasonType] = None,
        template_family: typing.Optional[str] = None,
        step_count: typing.Optional[int] = None,
        step_count_operator: typing.Optional[ComparisonOperator] = None,
        tools_used: typing.Optional[typing.Sequence[str]] = None,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListInternalRunsRequestOrder] = None,
        order_by: typing.Optional[ListInternalRunsRequestOrderBy] = None,
        active: typing.Optional[bool] = None,
        ascending: typing.Optional[bool] = None,
        project_id: typing.Optional[str] = None,
        conversation_id: typing.Optional[str] = None,
        duration_percentile: typing.Optional[int] = None,
        duration_value: typing.Optional[int] = None,
        duration_operator: typing.Optional[ListInternalRunsRequestDurationOperator] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Run]:
        """
        List all runs.

        Parameters
        ----------
        run_id : typing.Optional[str]
            Filter by a specific run ID.

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

        template_family : typing.Optional[str]
            Filter runs by template family (base_template_id).

        step_count : typing.Optional[int]
            Filter runs by step count. Must be provided with step_count_operator.

        step_count_operator : typing.Optional[ComparisonOperator]
            Operator for step_count filter: 'eq' for equals, 'gte' for greater than or equal, 'lte' for less than or equal.

        tools_used : typing.Optional[typing.Sequence[str]]
            Filter runs that used any of the specified tools.

        before : typing.Optional[str]
            Run ID cursor for pagination. Returns runs that come before this run ID in the specified sort order

        after : typing.Optional[str]
            Run ID cursor for pagination. Returns runs that come after this run ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of runs to return

        order : typing.Optional[ListInternalRunsRequestOrder]
            Sort order for runs by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListInternalRunsRequestOrderBy]
            Field to sort by

        active : typing.Optional[bool]
            Filter for active runs.

        ascending : typing.Optional[bool]
            Whether to sort agents oldest to newest (True) or newest to oldest (False, default). Deprecated in favor of order field.

        project_id : typing.Optional[str]
            Filter runs by project ID.

        conversation_id : typing.Optional[str]
            Filter runs by conversation ID.

        duration_percentile : typing.Optional[int]
            Filter runs by duration percentile (1-100). Returns runs slower than this percentile.

        duration_value : typing.Optional[int]
            Duration value in nanoseconds for filtering. Must be used with duration_operator.

        duration_operator : typing.Optional[ListInternalRunsRequestDurationOperator]
            Comparison operator for duration filter: 'gt' (greater than), 'lt' (less than), 'eq' (equals).

        start_date : typing.Optional[dt.datetime]
            Filter runs created on or after this date (ISO 8601 format).

        end_date : typing.Optional[dt.datetime]
            Filter runs created on or before this date (ISO 8601 format).

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
            await client.internal_runs.list_internal_runs()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_internal_runs(
            run_id=run_id,
            agent_id=agent_id,
            agent_ids=agent_ids,
            statuses=statuses,
            background=background,
            stop_reason=stop_reason,
            template_family=template_family,
            step_count=step_count,
            step_count_operator=step_count_operator,
            tools_used=tools_used,
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            active=active,
            ascending=ascending,
            project_id=project_id,
            conversation_id=conversation_id,
            duration_percentile=duration_percentile,
            duration_value=duration_value,
            duration_operator=duration_operator,
            start_date=start_date,
            end_date=end_date,
            request_options=request_options,
        )
        return _response.data
