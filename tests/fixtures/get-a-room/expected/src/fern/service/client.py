

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawServiceClient, RawServiceClient
from .types.health_response import HealthResponse


class ServiceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawServiceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawServiceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawServiceClient
        """
        return self._raw_client

    def health(self, *, request_options: typing.Optional[RequestOptions] = None) -> HealthResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HealthResponse
            Service is responding

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.service.health()
        """
        _response = self._raw_client.health(request_options=request_options)
        return _response.data


class AsyncServiceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawServiceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawServiceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawServiceClient
        """
        return self._raw_client

    async def health(self, *, request_options: typing.Optional[RequestOptions] = None) -> HealthResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HealthResponse
            Service is responding

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.service.health()


        asyncio.run(main())
        """
        _response = await self._raw_client.health(request_options=request_options)
        return _response.data
