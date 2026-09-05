

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.health_response import HealthResponse
from .raw_client import AsyncRawHealthClient, RawHealthClient


class HealthClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawHealthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawHealthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawHealthClient
        """
        return self._raw_client

    def get_health(self, *, request_options: typing.Optional[RequestOptions] = None) -> HealthResponse:
        """
        Reports process liveness and the current database and index-runtime state. Liveness returns 200 even when ready is false.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HealthResponse
            The server process is alive.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.health.get_health()
        """
        _response = self._raw_client.get_health(request_options=request_options)
        return _response.data

    def get_readiness(self, *, request_options: typing.Optional[RequestOptions] = None) -> HealthResponse:
        """
        Returns 200 only when the configured database handle and index runtime are ready to serve queries.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HealthResponse
            The database is ready.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.health.get_readiness()
        """
        _response = self._raw_client.get_readiness(request_options=request_options)
        return _response.data


class AsyncHealthClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawHealthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawHealthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawHealthClient
        """
        return self._raw_client

    async def get_health(self, *, request_options: typing.Optional[RequestOptions] = None) -> HealthResponse:
        """
        Reports process liveness and the current database and index-runtime state. Liveness returns 200 even when ready is false.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HealthResponse
            The server process is alive.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.health.get_health()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_health(request_options=request_options)
        return _response.data

    async def get_readiness(self, *, request_options: typing.Optional[RequestOptions] = None) -> HealthResponse:
        """
        Returns 200 only when the configured database handle and index runtime are ready to serve queries.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HealthResponse
            The database is ready.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.health.get_readiness()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_readiness(request_options=request_options)
        return _response.data
