

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.health_info import HealthInfo
from ..types.version_info import VersionInfo
from .raw_client import AsyncRawMonitoringClient, RawMonitoringClient


class MonitoringClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMonitoringClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMonitoringClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMonitoringClient
        """
        return self._raw_client

    def get_health(self, *, request_options: typing.Optional[RequestOptions] = None) -> HealthInfo:
        """
        Get the status of Airflow's metadatabase and scheduler. It includes info about
        metadatabase and last heartbeat of scheduler.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HealthInfo
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.monitoring.get_health()
        """
        _response = self._raw_client.get_health(request_options=request_options)
        return _response.data

    def get_version(self, *, request_options: typing.Optional[RequestOptions] = None) -> VersionInfo:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VersionInfo
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.monitoring.get_version()
        """
        _response = self._raw_client.get_version(request_options=request_options)
        return _response.data


class AsyncMonitoringClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMonitoringClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMonitoringClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMonitoringClient
        """
        return self._raw_client

    async def get_health(self, *, request_options: typing.Optional[RequestOptions] = None) -> HealthInfo:
        """
        Get the status of Airflow's metadatabase and scheduler. It includes info about
        metadatabase and last heartbeat of scheduler.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HealthInfo
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.monitoring.get_health()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_health(request_options=request_options)
        return _response.data

    async def get_version(self, *, request_options: typing.Optional[RequestOptions] = None) -> VersionInfo:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VersionInfo
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.monitoring.get_version()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_version(request_options=request_options)
        return _response.data
