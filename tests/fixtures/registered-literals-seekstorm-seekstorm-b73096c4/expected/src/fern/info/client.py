

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawInfoClient, RawInfoClient


class InfoClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInfoClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInfoClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInfoClient
        """
        return self._raw_client

    def live(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Returns a live message with the SeekStorm server version.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            SeekStorm server is live

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apikey="YOUR_APIKEY",
        )
        client.info.live()
        """
        _response = self._raw_client.live(request_options=request_options)
        return _response.data


class AsyncInfoClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInfoClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInfoClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInfoClient
        """
        return self._raw_client

    async def live(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Returns a live message with the SeekStorm server version.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            SeekStorm server is live

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apikey="YOUR_APIKEY",
        )


        async def main() -> None:
            await client.info.live()


        asyncio.run(main())
        """
        _response = await self._raw_client.live(request_options=request_options)
        return _response.data
