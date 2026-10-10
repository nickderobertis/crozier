

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.gust import Gust
from .raw_client import AsyncRawGustsClient, RawGustsClient


class GustsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGustsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGustsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGustsClient
        """
        return self._raw_client

    def latest_gust(self, *, request_options: typing.Optional[RequestOptions] = None) -> Gust:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Gust
            The latest gust reading.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.gusts.latest_gust()
        """
        _response = self._raw_client.latest_gust(request_options=request_options)
        return _response.data


class AsyncGustsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGustsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGustsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGustsClient
        """
        return self._raw_client

    async def latest_gust(self, *, request_options: typing.Optional[RequestOptions] = None) -> Gust:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Gust
            The latest gust reading.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.gusts.latest_gust()


        asyncio.run(main())
        """
        _response = await self._raw_client.latest_gust(request_options=request_options)
        return _response.data
