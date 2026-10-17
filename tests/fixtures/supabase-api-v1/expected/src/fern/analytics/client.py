

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.analytics_response_output import AnalyticsResponseOutput
from ..types.v1get_usage_api_count_response_output import V1GetUsageApiCountResponseOutput
from ..types.v1get_usage_api_requests_count_response_output import V1GetUsageApiRequestsCountResponseOutput
from .raw_client import AsyncRawAnalyticsClient, RawAnalyticsClient
from .types.v1get_project_function_combined_stats_request_interval import (
    V1GetProjectFunctionCombinedStatsRequestInterval,
)
from .types.v1get_project_usage_api_count_request_interval import V1GetProjectUsageApiCountRequestInterval


class AnalyticsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAnalyticsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAnalyticsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAnalyticsClient
        """
        return self._raw_client

    def v1get_project_logs_all(
        self,
        ref: str,
        *,
        sql: typing.Optional[str] = None,
        iso_timestamp_start: typing.Optional[dt.datetime] = None,
        iso_timestamp_end: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AnalyticsResponseOutput:
        """
        Executes a SQL query on the project's logs.

        Either the `iso_timestamp_start` and `iso_timestamp_end` parameters must be provided.
        If both are not provided, only the last 1 minute of logs will be queried.
        The timestamp range must be no more than 24 hours and is rounded to the nearest minute. If the range is more than 24 hours, a validation error will be thrown.

        Note: Unless the `sql` parameter is provided, only edge_logs will be queried. See the [log query docs](https://supabase.com/docs/guides/monitoring-and-debugging/logs#logs-explorer) for all available sources.

        Parameters
        ----------
        ref : str
            Project ref

        sql : typing.Optional[str]
            Custom SQL query to execute on the logs. See [querying logs](https://supabase.com/docs/guides/monitoring-and-debugging/logs#querying-with-the-logs-explorer) for more details.

        iso_timestamp_start : typing.Optional[dt.datetime]

        iso_timestamp_end : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AnalyticsResponseOutput


        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.analytics.v1get_project_logs_all(
            ref="abcdefghijklmnopqrst",
            sql="select event_message from edge_logs limit 10",
            iso_timestamp_start=datetime.datetime.fromisoformat(
                "2025-03-01 00:00:00+00:00",
            ),
            iso_timestamp_end=datetime.datetime.fromisoformat(
                "2025-03-01 23:59:59+00:00",
            ),
        )
        """
        _response = self._raw_client.v1get_project_logs_all(
            ref,
            sql=sql,
            iso_timestamp_start=iso_timestamp_start,
            iso_timestamp_end=iso_timestamp_end,
            request_options=request_options,
        )
        return _response.data

    def v1get_project_logs(
        self,
        ref: str,
        *,
        sql: typing.Optional[str] = None,
        iso_timestamp_start: typing.Optional[dt.datetime] = None,
        iso_timestamp_end: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AnalyticsResponseOutput:
        """
        Executes an SQL or LQL query on the project's unified logs stream.

        Either the `iso_timestamp_start` and `iso_timestamp_end` parameters must be provided.
        If both are not provided, only the last 1 minute of logs will be queried.
        The timestamp range must be no more than 24 hours and is rounded to the nearest minute. If the range is more than 24 hours, a validation error will be thrown.

        Filter by the `source` column to specify specific log sources, such as edge_logs, postgres_logs, etc.

        Note: SQL must be written in **ClickHouse SQL dialect**.

        Parameters
        ----------
        ref : str
            Project ref

        sql : typing.Optional[str]
            Custom SQL query to execute on the logs. See [querying logs](https://supabase.com/docs/guides/monitoring-and-debugging/logs#querying-with-the-logs-explorer) for more details.

        iso_timestamp_start : typing.Optional[dt.datetime]

        iso_timestamp_end : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AnalyticsResponseOutput


        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.analytics.v1get_project_logs(
            ref="abcdefghijklmnopqrst",
            sql="select event_message from edge_logs limit 10",
            iso_timestamp_start=datetime.datetime.fromisoformat(
                "2025-03-01 00:00:00+00:00",
            ),
            iso_timestamp_end=datetime.datetime.fromisoformat(
                "2025-03-01 23:59:59+00:00",
            ),
        )
        """
        _response = self._raw_client.v1get_project_logs(
            ref,
            sql=sql,
            iso_timestamp_start=iso_timestamp_start,
            iso_timestamp_end=iso_timestamp_end,
            request_options=request_options,
        )
        return _response.data

    def v1get_project_usage_api_count(
        self,
        ref: str,
        *,
        interval: typing.Optional[V1GetProjectUsageApiCountRequestInterval] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1GetUsageApiCountResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        interval : typing.Optional[V1GetProjectUsageApiCountRequestInterval]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1GetUsageApiCountResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.analytics.v1get_project_usage_api_count(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1get_project_usage_api_count(
            ref, interval=interval, request_options=request_options
        )
        return _response.data

    def v1get_project_usage_request_count(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1GetUsageApiRequestsCountResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1GetUsageApiRequestsCountResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.analytics.v1get_project_usage_request_count(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1get_project_usage_request_count(ref, request_options=request_options)
        return _response.data

    def v1get_project_function_combined_stats(
        self,
        ref: str,
        *,
        interval: V1GetProjectFunctionCombinedStatsRequestInterval,
        function_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AnalyticsResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        interval : V1GetProjectFunctionCombinedStatsRequestInterval

        function_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AnalyticsResponseOutput


        Examples
        --------
        from fern.analytics import V1GetProjectFunctionCombinedStatsRequestInterval

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.analytics.v1get_project_function_combined_stats(
            ref="abcdefghijklmnopqrst",
            interval=V1GetProjectFunctionCombinedStatsRequestInterval.FIFTEEN_MIN,
            function_id="3c078cce-ad70-4148-9f37-4da362789053",
        )
        """
        _response = self._raw_client.v1get_project_function_combined_stats(
            ref, interval=interval, function_id=function_id, request_options=request_options
        )
        return _response.data

    def v1scrape_project_metrics(self, ref: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Prometheus scrape endpoint. Returns metrics of a customer project in the Prometheus open exposition format.

        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Prometheus / OpenMetrics text exposition

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.analytics.v1scrape_project_metrics(
            ref="ref",
        )
        """
        _response = self._raw_client.v1scrape_project_metrics(ref, request_options=request_options)
        return _response.data


class AsyncAnalyticsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAnalyticsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAnalyticsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAnalyticsClient
        """
        return self._raw_client

    async def v1get_project_logs_all(
        self,
        ref: str,
        *,
        sql: typing.Optional[str] = None,
        iso_timestamp_start: typing.Optional[dt.datetime] = None,
        iso_timestamp_end: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AnalyticsResponseOutput:
        """
        Executes a SQL query on the project's logs.

        Either the `iso_timestamp_start` and `iso_timestamp_end` parameters must be provided.
        If both are not provided, only the last 1 minute of logs will be queried.
        The timestamp range must be no more than 24 hours and is rounded to the nearest minute. If the range is more than 24 hours, a validation error will be thrown.

        Note: Unless the `sql` parameter is provided, only edge_logs will be queried. See the [log query docs](https://supabase.com/docs/guides/monitoring-and-debugging/logs#logs-explorer) for all available sources.

        Parameters
        ----------
        ref : str
            Project ref

        sql : typing.Optional[str]
            Custom SQL query to execute on the logs. See [querying logs](https://supabase.com/docs/guides/monitoring-and-debugging/logs#querying-with-the-logs-explorer) for more details.

        iso_timestamp_start : typing.Optional[dt.datetime]

        iso_timestamp_end : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AnalyticsResponseOutput


        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.analytics.v1get_project_logs_all(
                ref="abcdefghijklmnopqrst",
                sql="select event_message from edge_logs limit 10",
                iso_timestamp_start=datetime.datetime.fromisoformat(
                    "2025-03-01 00:00:00+00:00",
                ),
                iso_timestamp_end=datetime.datetime.fromisoformat(
                    "2025-03-01 23:59:59+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_project_logs_all(
            ref,
            sql=sql,
            iso_timestamp_start=iso_timestamp_start,
            iso_timestamp_end=iso_timestamp_end,
            request_options=request_options,
        )
        return _response.data

    async def v1get_project_logs(
        self,
        ref: str,
        *,
        sql: typing.Optional[str] = None,
        iso_timestamp_start: typing.Optional[dt.datetime] = None,
        iso_timestamp_end: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AnalyticsResponseOutput:
        """
        Executes an SQL or LQL query on the project's unified logs stream.

        Either the `iso_timestamp_start` and `iso_timestamp_end` parameters must be provided.
        If both are not provided, only the last 1 minute of logs will be queried.
        The timestamp range must be no more than 24 hours and is rounded to the nearest minute. If the range is more than 24 hours, a validation error will be thrown.

        Filter by the `source` column to specify specific log sources, such as edge_logs, postgres_logs, etc.

        Note: SQL must be written in **ClickHouse SQL dialect**.

        Parameters
        ----------
        ref : str
            Project ref

        sql : typing.Optional[str]
            Custom SQL query to execute on the logs. See [querying logs](https://supabase.com/docs/guides/monitoring-and-debugging/logs#querying-with-the-logs-explorer) for more details.

        iso_timestamp_start : typing.Optional[dt.datetime]

        iso_timestamp_end : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AnalyticsResponseOutput


        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.analytics.v1get_project_logs(
                ref="abcdefghijklmnopqrst",
                sql="select event_message from edge_logs limit 10",
                iso_timestamp_start=datetime.datetime.fromisoformat(
                    "2025-03-01 00:00:00+00:00",
                ),
                iso_timestamp_end=datetime.datetime.fromisoformat(
                    "2025-03-01 23:59:59+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_project_logs(
            ref,
            sql=sql,
            iso_timestamp_start=iso_timestamp_start,
            iso_timestamp_end=iso_timestamp_end,
            request_options=request_options,
        )
        return _response.data

    async def v1get_project_usage_api_count(
        self,
        ref: str,
        *,
        interval: typing.Optional[V1GetProjectUsageApiCountRequestInterval] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1GetUsageApiCountResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        interval : typing.Optional[V1GetProjectUsageApiCountRequestInterval]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1GetUsageApiCountResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.analytics.v1get_project_usage_api_count(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_project_usage_api_count(
            ref, interval=interval, request_options=request_options
        )
        return _response.data

    async def v1get_project_usage_request_count(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1GetUsageApiRequestsCountResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1GetUsageApiRequestsCountResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.analytics.v1get_project_usage_request_count(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_project_usage_request_count(ref, request_options=request_options)
        return _response.data

    async def v1get_project_function_combined_stats(
        self,
        ref: str,
        *,
        interval: V1GetProjectFunctionCombinedStatsRequestInterval,
        function_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AnalyticsResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        interval : V1GetProjectFunctionCombinedStatsRequestInterval

        function_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AnalyticsResponseOutput


        Examples
        --------
        import asyncio

        from fern.analytics import V1GetProjectFunctionCombinedStatsRequestInterval

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.analytics.v1get_project_function_combined_stats(
                ref="abcdefghijklmnopqrst",
                interval=V1GetProjectFunctionCombinedStatsRequestInterval.FIFTEEN_MIN,
                function_id="3c078cce-ad70-4148-9f37-4da362789053",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_project_function_combined_stats(
            ref, interval=interval, function_id=function_id, request_options=request_options
        )
        return _response.data

    async def v1scrape_project_metrics(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Prometheus scrape endpoint. Returns metrics of a customer project in the Prometheus open exposition format.

        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Prometheus / OpenMetrics text exposition

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.analytics.v1scrape_project_metrics(
                ref="ref",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1scrape_project_metrics(ref, request_options=request_options)
        return _response.data
