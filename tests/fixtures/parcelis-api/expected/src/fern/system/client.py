

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSystemClient, RawSystemClient
from .types.health_response import HealthResponse


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

    def health(self, *, request_options: typing.Optional[RequestOptions] = None) -> HealthResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HealthResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.system.health()
        """
        _response = self._raw_client.health(request_options=request_options)
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

    async def health(self, *, request_options: typing.Optional[RequestOptions] = None) -> HealthResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HealthResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.system.health()


        asyncio.run(main())
        """
        _response = await self._raw_client.health(request_options=request_options)
        return _response.data
