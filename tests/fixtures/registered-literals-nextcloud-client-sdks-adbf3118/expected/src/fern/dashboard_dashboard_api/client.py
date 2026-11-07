

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.dashboard_dashboard_api_get_widget_items200response import DashboardDashboardApiGetWidgetItems200Response
from ..types.dashboard_dashboard_api_get_widgets200response import DashboardDashboardApiGetWidgets200Response
from .raw_client import AsyncRawDashboardDashboardApiClient, RawDashboardDashboardApiClient


class DashboardDashboardApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDashboardDashboardApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDashboardDashboardApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDashboardDashboardApiClient
        """
        return self._raw_client

    def get_widgets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DashboardDashboardApiGetWidgets200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DashboardDashboardApiGetWidgets200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.dashboard_dashboard_api.get_widgets()
        """
        _response = self._raw_client.get_widgets(request_options=request_options)
        return _response.data

    def get_widget_items(
        self,
        *,
        since_ids: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        widgets: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DashboardDashboardApiGetWidgetItems200Response:
        """
        Parameters
        ----------
        since_ids : typing.Optional[str]
            Array indexed by widget Ids, contains date/id from which we want the new items

        limit : typing.Optional[int]
            Limit number of result items per widget

        widgets : typing.Optional[str]
            Limit results to specific widgets

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DashboardDashboardApiGetWidgetItems200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.dashboard_dashboard_api.get_widget_items()
        """
        _response = self._raw_client.get_widget_items(
            since_ids=since_ids, limit=limit, widgets=widgets, request_options=request_options
        )
        return _response.data


class AsyncDashboardDashboardApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDashboardDashboardApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDashboardDashboardApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDashboardDashboardApiClient
        """
        return self._raw_client

    async def get_widgets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DashboardDashboardApiGetWidgets200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DashboardDashboardApiGetWidgets200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.dashboard_dashboard_api.get_widgets()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_widgets(request_options=request_options)
        return _response.data

    async def get_widget_items(
        self,
        *,
        since_ids: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        widgets: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DashboardDashboardApiGetWidgetItems200Response:
        """
        Parameters
        ----------
        since_ids : typing.Optional[str]
            Array indexed by widget Ids, contains date/id from which we want the new items

        limit : typing.Optional[int]
            Limit number of result items per widget

        widgets : typing.Optional[str]
            Limit results to specific widgets

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DashboardDashboardApiGetWidgetItems200Response


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.dashboard_dashboard_api.get_widget_items()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_widget_items(
            since_ids=since_ids, limit=limit, widgets=widgets, request_options=request_options
        )
        return _response.data
