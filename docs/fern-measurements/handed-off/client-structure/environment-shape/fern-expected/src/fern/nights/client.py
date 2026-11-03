

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawNightsClient, RawNightsClient


class NightsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNightsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNightsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNightsClient
        """
        return self._raw_client

    def list_nights(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Observing nights.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.nights.list_nights()
        """
        _response = self._raw_client.list_nights(request_options=request_options)
        return _response.data


class AsyncNightsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNightsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNightsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNightsClient
        """
        return self._raw_client

    async def list_nights(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Observing nights.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.nights.list_nights()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_nights(request_options=request_options)
        return _response.data
