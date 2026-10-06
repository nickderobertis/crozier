

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
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

    def healthz_controller_health_check(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Check the health status of the API

        Parameters
        ----------
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
            base_url="https://yourhost.com/path/to/api",
        )
        client.health.healthz_controller_health_check()
        """
        _response = self._raw_client.healthz_controller_health_check(request_options=request_options)
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

    async def healthz_controller_health_check(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Check the health status of the API

        Parameters
        ----------
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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.health.healthz_controller_health_check()


        asyncio.run(main())
        """
        _response = await self._raw_client.healthz_controller_health_check(request_options=request_options)
        return _response.data
