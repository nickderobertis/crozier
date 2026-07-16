

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.stats import Stats
from .raw_client import AsyncRawStatsClient, RawStatsClient


class StatsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStatsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStatsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStatsClient
        """
        return self._raw_client

    def global_live_stats(self, *, request_options: typing.Optional[RequestOptions] = None) -> Stats:
        """
        Get global otoroshi stats

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Stats
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.stats.global_live_stats()
        """
        _response = self._raw_client.global_live_stats(request_options=request_options)
        return _response.data

    def service_live_stats(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Stats:
        """
        Get live feed of global otoroshi stats (global) or for a service {id}

        Parameters
        ----------
        id : str
            The service id or global for otoroshi stats

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Stats
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.stats.service_live_stats(
            id="id",
        )
        """
        _response = self._raw_client.service_live_stats(id, request_options=request_options)
        return _response.data


class AsyncStatsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStatsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStatsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStatsClient
        """
        return self._raw_client

    async def global_live_stats(self, *, request_options: typing.Optional[RequestOptions] = None) -> Stats:
        """
        Get global otoroshi stats

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Stats
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
            await client.stats.global_live_stats()


        asyncio.run(main())
        """
        _response = await self._raw_client.global_live_stats(request_options=request_options)
        return _response.data

    async def service_live_stats(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Stats:
        """
        Get live feed of global otoroshi stats (global) or for a service {id}

        Parameters
        ----------
        id : str
            The service id or global for otoroshi stats

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Stats
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
            await client.stats.service_live_stats(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.service_live_stats(id, request_options=request_options)
        return _response.data
