

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawMapClient, RawMapClient


class MapClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMapClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMapClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMapClient
        """
        return self._raw_client

    def map_api_get_sentinel_key(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
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
        client.map_.map_api_get_sentinel_key()
        """
        _response = self._raw_client.map_api_get_sentinel_key(request_options=request_options)
        return _response.data


class AsyncMapClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMapClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMapClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMapClient
        """
        return self._raw_client

    async def map_api_get_sentinel_key(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
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
            await client.map_.map_api_get_sentinel_key()


        asyncio.run(main())
        """
        _response = await self._raw_client.map_api_get_sentinel_key(request_options=request_options)
        return _response.data
