

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.dashboard import Dashboard
from ..types.dashboard_filter_parameters import DashboardFilterParameters
from ..types.dashboard_response import DashboardResponse
from ..types.labels import Labels
from .raw_client import AsyncRawDashboardsClient, RawDashboardsClient
from .types.dashboards_list_response import DashboardsListResponse


OMIT = typing.cast(typing.Any, ...)


class DashboardsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDashboardsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDashboardsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDashboardsClient
        """
        return self._raw_client

    def list(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
        filter: typing.Optional[DashboardFilterParameters] = None,
        sort: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DashboardsListResponse:
        """
        Get a paginated list of dashboards that your account has access to.

        Parameters
        ----------
        page_size : typing.Optional[int]
            The maximum number of items to include per page. The last page of a collection may include fewer items.

        page_number : typing.Optional[int]
            Determines which page of the entities to retrieve.

        filter : typing.Optional[DashboardFilterParameters]
            Filters dashboards in the response.

        sort : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DashboardsListResponse
            List of dashboards

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.dashboards.list(
            page_size=10,
            page_number=1,
            sort="created_at desc",
        )
        """
        _response = self._raw_client.list(
            page_size=page_size, page_number=page_number, filter=filter, sort=sort, request_options=request_options
        )
        return _response.data

    def create(
        self,
        *,
        name: str,
        definition: Dashboard,
        labels: typing.Optional[Labels] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DashboardResponse:
        """
        Creates a new dashboard from the provided definition.

        Parameters
        ----------
        name : str
            The dashboard name, which is displayed at the top of the dashboard and in lists.
            It does not need to be unique.

        definition : Dashboard

        labels : typing.Optional[Labels]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DashboardResponse
            The created dashboard, including generated fields.

        Examples
        --------
        from fern import (
            AdvancedFiltersItem_ControlPlane,
            Chart_Donut,
            ChartTileDefinition,
            ChartTileDefinitionQuery_ApiUsage,
            ChartTileLayout,
            ChartTileLayoutPosition,
            ChartTileLayoutSize,
            Dashboard,
            FernApi,
            Tile_Chart,
            TimeRange_Relative,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.dashboards.create(
            name="Single Tile, Timeseries Line",
            definition=Dashboard(
                tiles=[
                    Tile_Chart(
                        layout=ChartTileLayout(
                            position=ChartTileLayoutPosition(
                                col=3,
                                row=0,
                            ),
                            size=ChartTileLayoutSize(
                                cols=3,
                                rows=1,
                            ),
                        ),
                        definition=ChartTileDefinition(
                            query=ChartTileDefinitionQuery_ApiUsage(
                                metrics=["request_count", "response_latency_p99"],
                                dimensions=["time", "gateway_service"],
                                filters=[
                                    AdvancedFiltersItem_ControlPlane(
                                        operator="in",
                                        value=["d5ac5d88-efed-4e10-9dfe-0b0a6646c219"],
                                    )
                                ],
                                granularity="hourly",
                                time_range=TimeRange_Relative(
                                    time_range="15m",
                                ),
                            ),
                            chart=Chart_Donut(),
                        ),
                    )
                ],
            ),
        )
        """
        _response = self._raw_client.create(
            name=name, definition=definition, labels=labels, request_options=request_options
        )
        return _response.data

    def get(self, dashboard_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> DashboardResponse:
        """
        Get a dashboard that your account has access to.

        Parameters
        ----------
        dashboard_id : str
            The dashboard's ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DashboardResponse
            The dashboard with the given ID.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.dashboards.get(
            dashboard_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        )
        """
        _response = self._raw_client.get(dashboard_id, request_options=request_options)
        return _response.data

    def update(
        self,
        dashboard_id: str,
        *,
        name: str,
        definition: Dashboard,
        labels: typing.Optional[Labels] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DashboardResponse:
        """
        Update an existing dashboard, replacing its definition with the provided one.

        Parameters
        ----------
        dashboard_id : str
            The dashboard's ID.

        name : str
            The dashboard name, which is displayed at the top of the dashboard and in lists.
            It does not need to be unique.

        definition : Dashboard

        labels : typing.Optional[Labels]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DashboardResponse
            The created dashboard, including generated fields.

        Examples
        --------
        from fern import (
            AdvancedFiltersItem_ControlPlane,
            Chart_Donut,
            ChartTileDefinition,
            ChartTileDefinitionQuery_ApiUsage,
            ChartTileLayout,
            ChartTileLayoutPosition,
            ChartTileLayoutSize,
            Dashboard,
            FernApi,
            Tile_Chart,
            TimeRange_Relative,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.dashboards.update(
            dashboard_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
            name="Single Tile, Timeseries Line",
            definition=Dashboard(
                tiles=[
                    Tile_Chart(
                        layout=ChartTileLayout(
                            position=ChartTileLayoutPosition(
                                col=3,
                                row=0,
                            ),
                            size=ChartTileLayoutSize(
                                cols=3,
                                rows=1,
                            ),
                        ),
                        definition=ChartTileDefinition(
                            query=ChartTileDefinitionQuery_ApiUsage(
                                metrics=["request_count", "response_latency_p99"],
                                dimensions=["time", "gateway_service"],
                                filters=[
                                    AdvancedFiltersItem_ControlPlane(
                                        operator="in",
                                        value=["d5ac5d88-efed-4e10-9dfe-0b0a6646c219"],
                                    )
                                ],
                                granularity="hourly",
                                time_range=TimeRange_Relative(
                                    time_range="15m",
                                ),
                            ),
                            chart=Chart_Donut(),
                        ),
                    )
                ],
            ),
        )
        """
        _response = self._raw_client.update(
            dashboard_id, name=name, definition=definition, labels=labels, request_options=request_options
        )
        return _response.data

    def delete(self, dashboard_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete an existing dashboard.

        Parameters
        ----------
        dashboard_id : str
            The dashboard's ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.dashboards.delete(
            dashboard_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
        )
        """
        _response = self._raw_client.delete(dashboard_id, request_options=request_options)
        return _response.data


class AsyncDashboardsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDashboardsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDashboardsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDashboardsClient
        """
        return self._raw_client

    async def list(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
        filter: typing.Optional[DashboardFilterParameters] = None,
        sort: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DashboardsListResponse:
        """
        Get a paginated list of dashboards that your account has access to.

        Parameters
        ----------
        page_size : typing.Optional[int]
            The maximum number of items to include per page. The last page of a collection may include fewer items.

        page_number : typing.Optional[int]
            Determines which page of the entities to retrieve.

        filter : typing.Optional[DashboardFilterParameters]
            Filters dashboards in the response.

        sort : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DashboardsListResponse
            List of dashboards

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.dashboards.list(
                page_size=10,
                page_number=1,
                sort="created_at desc",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            page_size=page_size, page_number=page_number, filter=filter, sort=sort, request_options=request_options
        )
        return _response.data

    async def create(
        self,
        *,
        name: str,
        definition: Dashboard,
        labels: typing.Optional[Labels] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DashboardResponse:
        """
        Creates a new dashboard from the provided definition.

        Parameters
        ----------
        name : str
            The dashboard name, which is displayed at the top of the dashboard and in lists.
            It does not need to be unique.

        definition : Dashboard

        labels : typing.Optional[Labels]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DashboardResponse
            The created dashboard, including generated fields.

        Examples
        --------
        import asyncio

        from fern import (
            AdvancedFiltersItem_ControlPlane,
            AsyncFernApi,
            Chart_Donut,
            ChartTileDefinition,
            ChartTileDefinitionQuery_ApiUsage,
            ChartTileLayout,
            ChartTileLayoutPosition,
            ChartTileLayoutSize,
            Dashboard,
            Tile_Chart,
            TimeRange_Relative,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.dashboards.create(
                name="Single Tile, Timeseries Line",
                definition=Dashboard(
                    tiles=[
                        Tile_Chart(
                            layout=ChartTileLayout(
                                position=ChartTileLayoutPosition(
                                    col=3,
                                    row=0,
                                ),
                                size=ChartTileLayoutSize(
                                    cols=3,
                                    rows=1,
                                ),
                            ),
                            definition=ChartTileDefinition(
                                query=ChartTileDefinitionQuery_ApiUsage(
                                    metrics=["request_count", "response_latency_p99"],
                                    dimensions=["time", "gateway_service"],
                                    filters=[
                                        AdvancedFiltersItem_ControlPlane(
                                            operator="in",
                                            value=[
                                                "d5ac5d88-efed-4e10-9dfe-0b0a6646c219"
                                            ],
                                        )
                                    ],
                                    granularity="hourly",
                                    time_range=TimeRange_Relative(
                                        time_range="15m",
                                    ),
                                ),
                                chart=Chart_Donut(),
                            ),
                        )
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            name=name, definition=definition, labels=labels, request_options=request_options
        )
        return _response.data

    async def get(
        self, dashboard_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DashboardResponse:
        """
        Get a dashboard that your account has access to.

        Parameters
        ----------
        dashboard_id : str
            The dashboard's ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DashboardResponse
            The dashboard with the given ID.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.dashboards.get(
                dashboard_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(dashboard_id, request_options=request_options)
        return _response.data

    async def update(
        self,
        dashboard_id: str,
        *,
        name: str,
        definition: Dashboard,
        labels: typing.Optional[Labels] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DashboardResponse:
        """
        Update an existing dashboard, replacing its definition with the provided one.

        Parameters
        ----------
        dashboard_id : str
            The dashboard's ID.

        name : str
            The dashboard name, which is displayed at the top of the dashboard and in lists.
            It does not need to be unique.

        definition : Dashboard

        labels : typing.Optional[Labels]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DashboardResponse
            The created dashboard, including generated fields.

        Examples
        --------
        import asyncio

        from fern import (
            AdvancedFiltersItem_ControlPlane,
            AsyncFernApi,
            Chart_Donut,
            ChartTileDefinition,
            ChartTileDefinitionQuery_ApiUsage,
            ChartTileLayout,
            ChartTileLayoutPosition,
            ChartTileLayoutSize,
            Dashboard,
            Tile_Chart,
            TimeRange_Relative,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.dashboards.update(
                dashboard_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
                name="Single Tile, Timeseries Line",
                definition=Dashboard(
                    tiles=[
                        Tile_Chart(
                            layout=ChartTileLayout(
                                position=ChartTileLayoutPosition(
                                    col=3,
                                    row=0,
                                ),
                                size=ChartTileLayoutSize(
                                    cols=3,
                                    rows=1,
                                ),
                            ),
                            definition=ChartTileDefinition(
                                query=ChartTileDefinitionQuery_ApiUsage(
                                    metrics=["request_count", "response_latency_p99"],
                                    dimensions=["time", "gateway_service"],
                                    filters=[
                                        AdvancedFiltersItem_ControlPlane(
                                            operator="in",
                                            value=[
                                                "d5ac5d88-efed-4e10-9dfe-0b0a6646c219"
                                            ],
                                        )
                                    ],
                                    granularity="hourly",
                                    time_range=TimeRange_Relative(
                                        time_range="15m",
                                    ),
                                ),
                                chart=Chart_Donut(),
                            ),
                        )
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            dashboard_id, name=name, definition=definition, labels=labels, request_options=request_options
        )
        return _response.data

    async def delete(self, dashboard_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete an existing dashboard.

        Parameters
        ----------
        dashboard_id : str
            The dashboard's ID.

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.dashboards.delete(
                dashboard_id="d32d905a-ed33-46a3-a093-d8f536af9a8a",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(dashboard_id, request_options=request_options)
        return _response.data
