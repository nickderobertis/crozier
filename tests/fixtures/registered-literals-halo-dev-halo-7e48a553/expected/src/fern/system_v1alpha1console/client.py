

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.dashboard_stats import DashboardStats
from .raw_client import AsyncRawSystemV1Alpha1ConsoleClient, RawSystemV1Alpha1ConsoleClient


class SystemV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSystemV1Alpha1ConsoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSystemV1Alpha1ConsoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSystemV1Alpha1ConsoleClient
        """
        return self._raw_client

    def get_stats(self, *, request_options: typing.Optional[RequestOptions] = None) -> DashboardStats:
        """
        Get stats.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DashboardStats
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.system_v1alpha1console.get_stats()
        """
        _response = self._raw_client.get_stats(request_options=request_options)
        return _response.data


class AsyncSystemV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSystemV1Alpha1ConsoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSystemV1Alpha1ConsoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSystemV1Alpha1ConsoleClient
        """
        return self._raw_client

    async def get_stats(self, *, request_options: typing.Optional[RequestOptions] = None) -> DashboardStats:
        """
        Get stats.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DashboardStats
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.system_v1alpha1console.get_stats()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_stats(request_options=request_options)
        return _response.data
