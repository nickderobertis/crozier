

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.health import Health
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

    def get_health(self, *, request_options: typing.Optional[RequestOptions] = None) -> Health:
        """
        Returns the health status of the service

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Health
            Service is healthy

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.health.get_health()
        """
        _response = self._raw_client.get_health(request_options=request_options)
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

    async def get_health(self, *, request_options: typing.Optional[RequestOptions] = None) -> Health:
        """
        Returns the health status of the service

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Health
            Service is healthy

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.health.get_health()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_health(request_options=request_options)
        return _response.data
