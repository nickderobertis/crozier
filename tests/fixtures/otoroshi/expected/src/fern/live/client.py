

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.host_metrics import HostMetrics
from ..types.live_stats import LiveStats
from .raw_client import AsyncRawLiveClient, RawLiveClient


class LiveClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLiveClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLiveClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLiveClient
        """
        return self._raw_client

    def otoroshi_controllers_adminapi_stats_controller_host_metrics(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HostMetrics:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HostMetrics
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.live.otoroshi_controllers_adminapi_stats_controller_host_metrics()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_stats_controller_host_metrics(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_stats_controller_service_live_stats_live(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LiveStats:
        """
        Parameters
        ----------
        id : str
            the id parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LiveStats
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.live.otoroshi_controllers_adminapi_stats_controller_service_live_stats_live(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_stats_controller_service_live_stats_live(
            id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_stats_controller_global_live_stats(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LiveStats:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LiveStats
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.live.otoroshi_controllers_adminapi_stats_controller_global_live_stats()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_stats_controller_global_live_stats(
            request_options=request_options
        )
        return _response.data


class AsyncLiveClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLiveClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLiveClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLiveClient
        """
        return self._raw_client

    async def otoroshi_controllers_adminapi_stats_controller_host_metrics(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HostMetrics:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HostMetrics
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.live.otoroshi_controllers_adminapi_stats_controller_host_metrics()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_stats_controller_host_metrics(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_stats_controller_service_live_stats_live(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LiveStats:
        """
        Parameters
        ----------
        id : str
            the id parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LiveStats
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.live.otoroshi_controllers_adminapi_stats_controller_service_live_stats_live(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_stats_controller_service_live_stats_live(
            id, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_stats_controller_global_live_stats(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LiveStats:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LiveStats
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.live.otoroshi_controllers_adminapi_stats_controller_global_live_stats()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_stats_controller_global_live_stats(
            request_options=request_options
        )
        return _response.data
