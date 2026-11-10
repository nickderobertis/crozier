

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawMapsClient, RawMapsClient


class MapsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMapsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMapsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMapsClient
        """
        return self._raw_client

    def returns_map_api_key(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Returns map api key.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.maps.returns_map_api_key()
        """
        _response = self._raw_client.returns_map_api_key(request_options=request_options)
        return _response.data


class AsyncMapsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMapsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMapsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMapsClient
        """
        return self._raw_client

    async def returns_map_api_key(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Returns map api key.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.maps.returns_map_api_key()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_map_api_key(request_options=request_options)
        return _response.data
