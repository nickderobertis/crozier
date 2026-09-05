

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawOtherClient, RawOtherClient


class OtherClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOtherClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOtherClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOtherClient
        """
        return self._raw_client

    def get_index(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Default endpoint. Simply replies with 'Hello, World!'. Authorization is not required

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Hello world string

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.other.get_index()
        """
        _response = self._raw_client.get_index(request_options=request_options)
        return _response.data


class AsyncOtherClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOtherClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOtherClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOtherClient
        """
        return self._raw_client

    async def get_index(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Default endpoint. Simply replies with 'Hello, World!'. Authorization is not required

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Hello world string

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.other.get_index()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_index(request_options=request_options)
        return _response.data
