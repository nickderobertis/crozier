

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.health_status import HealthStatus
from .raw_client import AsyncRawSystemClient, RawSystemClient


class SystemClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSystemClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSystemClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSystemClient
        """
        return self._raw_client

    def health_live(self, *, request_options: typing.Optional[RequestOptions] = None) -> HealthStatus:
        """
        Process liveness check.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HealthStatus
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.system.health_live()
        """
        _response = self._raw_client.health_live(request_options=request_options)
        return _response.data

    def health_ready(self, *, request_options: typing.Optional[RequestOptions] = None) -> HealthStatus:
        """
        Readiness check for PostgreSQL, migrations, and required runtime state.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HealthStatus
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.system.health_ready()
        """
        _response = self._raw_client.health_ready(request_options=request_options)
        return _response.data


class AsyncSystemClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSystemClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSystemClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSystemClient
        """
        return self._raw_client

    async def health_live(self, *, request_options: typing.Optional[RequestOptions] = None) -> HealthStatus:
        """
        Process liveness check.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HealthStatus
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.system.health_live()


        asyncio.run(main())
        """
        _response = await self._raw_client.health_live(request_options=request_options)
        return _response.data

    async def health_ready(self, *, request_options: typing.Optional[RequestOptions] = None) -> HealthStatus:
        """
        Readiness check for PostgreSQL, migrations, and required runtime state.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HealthStatus
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.system.health_ready()


        asyncio.run(main())
        """
        _response = await self._raw_client.health_ready(request_options=request_options)
        return _response.data
