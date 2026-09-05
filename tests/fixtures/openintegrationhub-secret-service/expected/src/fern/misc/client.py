

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawMiscClient, RawMiscClient


class MiscClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMiscClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMiscClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMiscClient
        """
        return self._raw_client

    def perform_healthcheck(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Retrieve health status of the API.

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
        )
        client.misc.perform_healthcheck()
        """
        _response = self._raw_client.perform_healthcheck(request_options=request_options)
        return _response.data


class AsyncMiscClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMiscClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMiscClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMiscClient
        """
        return self._raw_client

    async def perform_healthcheck(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Retrieve health status of the API.

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
        )


        async def main() -> None:
            await client.misc.perform_healthcheck()


        asyncio.run(main())
        """
        _response = await self._raw_client.perform_healthcheck(request_options=request_options)
        return _response.data
