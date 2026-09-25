

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.v1report_totals import V1ReportTotals
from .raw_client import AsyncRawReportsClient, RawReportsClient
from .types.filter_reports_request_billed import FilterReportsRequestBilled
from .types.filter_reports_request_scope import FilterReportsRequestScope


class ReportsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawReportsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawReportsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawReportsClient
        """
        return self._raw_client

    def get_reports(
        self,
        account_id: int,
        *,
        since: typing.Optional[dt.date] = None,
        until: typing.Optional[dt.date] = None,
        user_ids: typing.Optional[str] = None,
        project_ids: typing.Optional[str] = None,
        client_ids: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[V1ReportTotals]:
        """
        Retrieve report totals grouped by clients and projects. This endpoint provides aggregated time tracking data including durations, costs, and billing information. The response includes clients with their associated projects and calculated metrics.

        Parameters
        ----------
        account_id : int
            Account ID

        since : typing.Optional[dt.date]
            Start date for the report period (ISO 8601 format: YYYY-MM-DD)

        until : typing.Optional[dt.date]
            End date for the report period (ISO 8601 format: YYYY-MM-DD)

        user_ids : typing.Optional[str]
            Comma-separated list of user IDs to filter by

        project_ids : typing.Optional[str]
            Comma-separated list of project IDs to filter by

        client_ids : typing.Optional[str]
            Comma-separated list of client IDs to filter by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1ReportTotals]
            Report totals retrieved successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.reports.get_reports(
            account_id=1,
        )
        """
        _response = self._raw_client.get_reports(
            account_id,
            since=since,
            until=until,
            user_ids=user_ids,
            project_ids=project_ids,
            client_ids=client_ids,
            request_options=request_options,
        )
        return _response.data

    def filter_reports(
        self,
        account_id: int,
        *,
        since: typing.Optional[dt.date] = None,
        until: typing.Optional[dt.date] = None,
        user_ids: typing.Optional[str] = None,
        project_ids: typing.Optional[str] = None,
        client_ids: typing.Optional[str] = None,
        label_ids: typing.Optional[str] = None,
        team_ids: typing.Optional[str] = None,
        state_ids: typing.Optional[str] = None,
        group_by: typing.Optional[str] = None,
        scope: typing.Optional[FilterReportsRequestScope] = None,
        billed: typing.Optional[FilterReportsRequestBilled] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[typing.Any]:
        """
        Filter and retrieve report data with flexible grouping options. Returns aggregated totals grouped by clients, projects, users, labels, days, or teams. Use scope=events to retrieve individual time entries instead of aggregated totals.

        Parameters
        ----------
        account_id : int
            Account ID

        since : typing.Optional[dt.date]
            Start date for the report period (ISO 8601 format: YYYY-MM-DD)

        until : typing.Optional[dt.date]
            End date for the report period (ISO 8601 format: YYYY-MM-DD)

        user_ids : typing.Optional[str]
            Comma-separated list of user IDs to filter by

        project_ids : typing.Optional[str]
            Comma-separated list of project IDs to filter by

        client_ids : typing.Optional[str]
            Comma-separated list of client IDs to filter by

        label_ids : typing.Optional[str]
            Comma-separated list of label IDs to filter by

        team_ids : typing.Optional[str]
            Comma-separated list of team IDs to filter by (requires teams feature)

        state_ids : typing.Optional[str]
            Comma-separated list of state IDs to filter by

        group_by : typing.Optional[str]
            Comma-separated list of grouping keys: clients, users, labels, days, teams. Default: all groups

        scope : typing.Optional[FilterReportsRequestScope]
            Result scope: totals (aggregated data) or events (individual entries). Default: totals

        billed : typing.Optional[FilterReportsRequestBilled]
            Filter by billed status

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Any]
            Report events retrieved successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.reports.filter_reports(
            account_id=1,
        )
        """
        _response = self._raw_client.filter_reports(
            account_id,
            since=since,
            until=until,
            user_ids=user_ids,
            project_ids=project_ids,
            client_ids=client_ids,
            label_ids=label_ids,
            team_ids=team_ids,
            state_ids=state_ids,
            group_by=group_by,
            scope=scope,
            billed=billed,
            request_options=request_options,
        )
        return _response.data


class AsyncReportsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawReportsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawReportsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawReportsClient
        """
        return self._raw_client

    async def get_reports(
        self,
        account_id: int,
        *,
        since: typing.Optional[dt.date] = None,
        until: typing.Optional[dt.date] = None,
        user_ids: typing.Optional[str] = None,
        project_ids: typing.Optional[str] = None,
        client_ids: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[V1ReportTotals]:
        """
        Retrieve report totals grouped by clients and projects. This endpoint provides aggregated time tracking data including durations, costs, and billing information. The response includes clients with their associated projects and calculated metrics.

        Parameters
        ----------
        account_id : int
            Account ID

        since : typing.Optional[dt.date]
            Start date for the report period (ISO 8601 format: YYYY-MM-DD)

        until : typing.Optional[dt.date]
            End date for the report period (ISO 8601 format: YYYY-MM-DD)

        user_ids : typing.Optional[str]
            Comma-separated list of user IDs to filter by

        project_ids : typing.Optional[str]
            Comma-separated list of project IDs to filter by

        client_ids : typing.Optional[str]
            Comma-separated list of client IDs to filter by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1ReportTotals]
            Report totals retrieved successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.reports.get_reports(
                account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_reports(
            account_id,
            since=since,
            until=until,
            user_ids=user_ids,
            project_ids=project_ids,
            client_ids=client_ids,
            request_options=request_options,
        )
        return _response.data

    async def filter_reports(
        self,
        account_id: int,
        *,
        since: typing.Optional[dt.date] = None,
        until: typing.Optional[dt.date] = None,
        user_ids: typing.Optional[str] = None,
        project_ids: typing.Optional[str] = None,
        client_ids: typing.Optional[str] = None,
        label_ids: typing.Optional[str] = None,
        team_ids: typing.Optional[str] = None,
        state_ids: typing.Optional[str] = None,
        group_by: typing.Optional[str] = None,
        scope: typing.Optional[FilterReportsRequestScope] = None,
        billed: typing.Optional[FilterReportsRequestBilled] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[typing.Any]:
        """
        Filter and retrieve report data with flexible grouping options. Returns aggregated totals grouped by clients, projects, users, labels, days, or teams. Use scope=events to retrieve individual time entries instead of aggregated totals.

        Parameters
        ----------
        account_id : int
            Account ID

        since : typing.Optional[dt.date]
            Start date for the report period (ISO 8601 format: YYYY-MM-DD)

        until : typing.Optional[dt.date]
            End date for the report period (ISO 8601 format: YYYY-MM-DD)

        user_ids : typing.Optional[str]
            Comma-separated list of user IDs to filter by

        project_ids : typing.Optional[str]
            Comma-separated list of project IDs to filter by

        client_ids : typing.Optional[str]
            Comma-separated list of client IDs to filter by

        label_ids : typing.Optional[str]
            Comma-separated list of label IDs to filter by

        team_ids : typing.Optional[str]
            Comma-separated list of team IDs to filter by (requires teams feature)

        state_ids : typing.Optional[str]
            Comma-separated list of state IDs to filter by

        group_by : typing.Optional[str]
            Comma-separated list of grouping keys: clients, users, labels, days, teams. Default: all groups

        scope : typing.Optional[FilterReportsRequestScope]
            Result scope: totals (aggregated data) or events (individual entries). Default: totals

        billed : typing.Optional[FilterReportsRequestBilled]
            Filter by billed status

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Any]
            Report events retrieved successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.reports.filter_reports(
                account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.filter_reports(
            account_id,
            since=since,
            until=until,
            user_ids=user_ids,
            project_ids=project_ids,
            client_ids=client_ids,
            label_ids=label_ids,
            team_ids=team_ids,
            state_ids=state_ids,
            group_by=group_by,
            scope=scope,
            billed=billed,
            request_options=request_options,
        )
        return _response.data
