

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.usage_events_response import UsageEventsResponse
from .raw_client import AsyncRawUsageClient, RawUsageClient
from .types.get_data_usage_request_aggregate import GetDataUsageRequestAggregate
from .types.get_data_usage_request_period import GetDataUsageRequestPeriod
from .types.get_data_usage_response import GetDataUsageResponse
from .types.get_events_usage_request_aggregate import GetEventsUsageRequestAggregate
from .types.get_events_usage_request_period import GetEventsUsageRequestPeriod
from .types.get_route_logs_usage_request_aggregate import GetRouteLogsUsageRequestAggregate
from .types.get_route_logs_usage_request_period import GetRouteLogsUsageRequestPeriod
from .types.get_route_logs_usage_response import GetRouteLogsUsageResponse
from .types.get_sessions_usage_request_aggregate import GetSessionsUsageRequestAggregate
from .types.get_sessions_usage_request_period import GetSessionsUsageRequestPeriod
from .types.get_sessions_usage_response import GetSessionsUsageResponse


class UsageClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUsageClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUsageClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUsageClient
        """
        return self._raw_client

    def get_data_usage(
        self,
        project_or_product_uid: str,
        *,
        period: GetDataUsageRequestPeriod,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fleet_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        limit: typing.Optional[int] = None,
        aggregate: typing.Optional[GetDataUsageRequestAggregate] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetDataUsageResponse:
        """
        Get data usage in bytes for a project with time range and period aggregation

        Parameters
        ----------
        project_or_product_uid : str

        period : GetDataUsageRequestPeriod
            Period type for aggregation

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        fleet_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter by Fleet UID

        limit : typing.Optional[int]
            Limit the number of data points returned

        aggregate : typing.Optional[GetDataUsageRequestAggregate]
            Aggregation level for results

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDataUsageResponse
            Response body for Data Usage

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.usage.get_data_usage(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            period="day",
        )
        """
        _response = self._raw_client.get_data_usage(
            project_or_product_uid,
            period=period,
            start_date=start_date,
            end_date=end_date,
            device_uid=device_uid,
            fleet_uid=fleet_uid,
            limit=limit,
            aggregate=aggregate,
            request_options=request_options,
        )
        return _response.data

    def get_events_usage(
        self,
        project_or_product_uid: str,
        *,
        period: GetEventsUsageRequestPeriod,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fleet_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        limit: typing.Optional[int] = None,
        aggregate: typing.Optional[GetEventsUsageRequestAggregate] = None,
        notefile: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        skip_recent_data: typing.Optional[bool] = None,
        include_notefiles: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UsageEventsResponse:
        """
        Get events usage for a project with time range and period aggregation, when endDate is 0 or unspecified the current time is implied

        Parameters
        ----------
        project_or_product_uid : str

        period : GetEventsUsageRequestPeriod
            Period type for aggregation

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        fleet_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter by Fleet UID

        limit : typing.Optional[int]
            Limit the number of data points returned

        aggregate : typing.Optional[GetEventsUsageRequestAggregate]
            Aggregation level for results

        notefile : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter to specific notefiles

        skip_recent_data : typing.Optional[bool]
            When true, skips fetching recent data from raw event tables and only returns data from summary tables. Use this for better performance on large projects.

        include_notefiles : typing.Optional[bool]
            Include per-notefile event counts in the response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsageEventsResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.usage.get_events_usage(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            period="day",
        )
        """
        _response = self._raw_client.get_events_usage(
            project_or_product_uid,
            period=period,
            start_date=start_date,
            end_date=end_date,
            device_uid=device_uid,
            fleet_uid=fleet_uid,
            limit=limit,
            aggregate=aggregate,
            notefile=notefile,
            skip_recent_data=skip_recent_data,
            include_notefiles=include_notefiles,
            request_options=request_options,
        )
        return _response.data

    def get_route_logs_usage(
        self,
        project_or_product_uid: str,
        *,
        period: GetRouteLogsUsageRequestPeriod,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        route_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        limit: typing.Optional[int] = None,
        aggregate: typing.Optional[GetRouteLogsUsageRequestAggregate] = None,
        skip_recent_data: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetRouteLogsUsageResponse:
        """
        Get route logs usage for a project with time range and period aggregation, when endDate is 0 or unspecified the current time is implied

        Parameters
        ----------
        project_or_product_uid : str

        period : GetRouteLogsUsageRequestPeriod
            Period type for aggregation

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        route_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Route UID.

        limit : typing.Optional[int]
            Limit the number of data points returned

        aggregate : typing.Optional[GetRouteLogsUsageRequestAggregate]
            Aggregation level for results

        skip_recent_data : typing.Optional[bool]
            When true, skips fetching recent data from raw event tables and only returns data from summary tables. Use this for better performance on large projects.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetRouteLogsUsageResponse
            Response body for Route Log Usage

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.usage.get_route_logs_usage(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            period="day",
        )
        """
        _response = self._raw_client.get_route_logs_usage(
            project_or_product_uid,
            period=period,
            start_date=start_date,
            end_date=end_date,
            route_uid=route_uid,
            limit=limit,
            aggregate=aggregate,
            skip_recent_data=skip_recent_data,
            request_options=request_options,
        )
        return _response.data

    def get_sessions_usage(
        self,
        project_or_product_uid: str,
        *,
        period: GetSessionsUsageRequestPeriod,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fleet_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        limit: typing.Optional[int] = None,
        aggregate: typing.Optional[GetSessionsUsageRequestAggregate] = None,
        skip_recent_data: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetSessionsUsageResponse:
        """
        Get sessions usage for a project with time range and period aggregation, when endDate is 0 or unspecified the current time is implied

        Parameters
        ----------
        project_or_product_uid : str

        period : GetSessionsUsageRequestPeriod
            Period type for aggregation

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        fleet_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter by Fleet UID

        limit : typing.Optional[int]
            Limit the number of data points returned

        aggregate : typing.Optional[GetSessionsUsageRequestAggregate]
            Aggregation level for results

        skip_recent_data : typing.Optional[bool]
            When true, skips fetching recent data from raw event tables and only returns data from summary tables. Use this for better performance on large projects.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSessionsUsageResponse
            Response body for Session Usage

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.usage.get_sessions_usage(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            period="day",
        )
        """
        _response = self._raw_client.get_sessions_usage(
            project_or_product_uid,
            period=period,
            start_date=start_date,
            end_date=end_date,
            device_uid=device_uid,
            fleet_uid=fleet_uid,
            limit=limit,
            aggregate=aggregate,
            skip_recent_data=skip_recent_data,
            request_options=request_options,
        )
        return _response.data


class AsyncUsageClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUsageClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUsageClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUsageClient
        """
        return self._raw_client

    async def get_data_usage(
        self,
        project_or_product_uid: str,
        *,
        period: GetDataUsageRequestPeriod,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fleet_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        limit: typing.Optional[int] = None,
        aggregate: typing.Optional[GetDataUsageRequestAggregate] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetDataUsageResponse:
        """
        Get data usage in bytes for a project with time range and period aggregation

        Parameters
        ----------
        project_or_product_uid : str

        period : GetDataUsageRequestPeriod
            Period type for aggregation

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        fleet_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter by Fleet UID

        limit : typing.Optional[int]
            Limit the number of data points returned

        aggregate : typing.Optional[GetDataUsageRequestAggregate]
            Aggregation level for results

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDataUsageResponse
            Response body for Data Usage

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.usage.get_data_usage(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                period="day",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_data_usage(
            project_or_product_uid,
            period=period,
            start_date=start_date,
            end_date=end_date,
            device_uid=device_uid,
            fleet_uid=fleet_uid,
            limit=limit,
            aggregate=aggregate,
            request_options=request_options,
        )
        return _response.data

    async def get_events_usage(
        self,
        project_or_product_uid: str,
        *,
        period: GetEventsUsageRequestPeriod,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fleet_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        limit: typing.Optional[int] = None,
        aggregate: typing.Optional[GetEventsUsageRequestAggregate] = None,
        notefile: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        skip_recent_data: typing.Optional[bool] = None,
        include_notefiles: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UsageEventsResponse:
        """
        Get events usage for a project with time range and period aggregation, when endDate is 0 or unspecified the current time is implied

        Parameters
        ----------
        project_or_product_uid : str

        period : GetEventsUsageRequestPeriod
            Period type for aggregation

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        fleet_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter by Fleet UID

        limit : typing.Optional[int]
            Limit the number of data points returned

        aggregate : typing.Optional[GetEventsUsageRequestAggregate]
            Aggregation level for results

        notefile : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter to specific notefiles

        skip_recent_data : typing.Optional[bool]
            When true, skips fetching recent data from raw event tables and only returns data from summary tables. Use this for better performance on large projects.

        include_notefiles : typing.Optional[bool]
            Include per-notefile event counts in the response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsageEventsResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.usage.get_events_usage(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                period="day",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_events_usage(
            project_or_product_uid,
            period=period,
            start_date=start_date,
            end_date=end_date,
            device_uid=device_uid,
            fleet_uid=fleet_uid,
            limit=limit,
            aggregate=aggregate,
            notefile=notefile,
            skip_recent_data=skip_recent_data,
            include_notefiles=include_notefiles,
            request_options=request_options,
        )
        return _response.data

    async def get_route_logs_usage(
        self,
        project_or_product_uid: str,
        *,
        period: GetRouteLogsUsageRequestPeriod,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        route_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        limit: typing.Optional[int] = None,
        aggregate: typing.Optional[GetRouteLogsUsageRequestAggregate] = None,
        skip_recent_data: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetRouteLogsUsageResponse:
        """
        Get route logs usage for a project with time range and period aggregation, when endDate is 0 or unspecified the current time is implied

        Parameters
        ----------
        project_or_product_uid : str

        period : GetRouteLogsUsageRequestPeriod
            Period type for aggregation

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        route_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Route UID.

        limit : typing.Optional[int]
            Limit the number of data points returned

        aggregate : typing.Optional[GetRouteLogsUsageRequestAggregate]
            Aggregation level for results

        skip_recent_data : typing.Optional[bool]
            When true, skips fetching recent data from raw event tables and only returns data from summary tables. Use this for better performance on large projects.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetRouteLogsUsageResponse
            Response body for Route Log Usage

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.usage.get_route_logs_usage(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                period="day",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_route_logs_usage(
            project_or_product_uid,
            period=period,
            start_date=start_date,
            end_date=end_date,
            route_uid=route_uid,
            limit=limit,
            aggregate=aggregate,
            skip_recent_data=skip_recent_data,
            request_options=request_options,
        )
        return _response.data

    async def get_sessions_usage(
        self,
        project_or_product_uid: str,
        *,
        period: GetSessionsUsageRequestPeriod,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fleet_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        limit: typing.Optional[int] = None,
        aggregate: typing.Optional[GetSessionsUsageRequestAggregate] = None,
        skip_recent_data: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetSessionsUsageResponse:
        """
        Get sessions usage for a project with time range and period aggregation, when endDate is 0 or unspecified the current time is implied

        Parameters
        ----------
        project_or_product_uid : str

        period : GetSessionsUsageRequestPeriod
            Period type for aggregation

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        fleet_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter by Fleet UID

        limit : typing.Optional[int]
            Limit the number of data points returned

        aggregate : typing.Optional[GetSessionsUsageRequestAggregate]
            Aggregation level for results

        skip_recent_data : typing.Optional[bool]
            When true, skips fetching recent data from raw event tables and only returns data from summary tables. Use this for better performance on large projects.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSessionsUsageResponse
            Response body for Session Usage

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.usage.get_sessions_usage(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                period="day",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_sessions_usage(
            project_or_product_uid,
            period=period,
            start_date=start_date,
            end_date=end_date,
            device_uid=device_uid,
            fleet_uid=fleet_uid,
            limit=limit,
            aggregate=aggregate,
            skip_recent_data=skip_recent_data,
            request_options=request_options,
        )
        return _response.data
