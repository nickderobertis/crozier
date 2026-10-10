

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.tide import Tide
from .raw_client import AsyncRawTidesClient, RawTidesClient


class TidesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTidesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTidesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTidesClient
        """
        return self._raw_client

    def next_tide(self, *, request_options: typing.Optional[RequestOptions] = None) -> Tide:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tide
            The next tide.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.tides.next_tide()
        """
        _response = self._raw_client.next_tide(request_options=request_options)
        return _response.data


class AsyncTidesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTidesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTidesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTidesClient
        """
        return self._raw_client

    async def next_tide(self, *, request_options: typing.Optional[RequestOptions] = None) -> Tide:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tide
            The next tide.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tides.next_tide()


        asyncio.run(main())
        """
        _response = await self._raw_client.next_tide(request_options=request_options)
        return _response.data
