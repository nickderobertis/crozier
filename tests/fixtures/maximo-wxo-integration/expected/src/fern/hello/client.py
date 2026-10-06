

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawHelloClient, RawHelloClient


class HelloClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawHelloClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawHelloClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawHelloClient
        """
        return self._raw_client

    def hello(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.hello.hello()
        """
        _response = self._raw_client.hello(request_options=request_options)
        return _response.data


class AsyncHelloClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawHelloClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawHelloClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawHelloClient
        """
        return self._raw_client

    async def hello(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.hello.hello()


        asyncio.run(main())
        """
        _response = await self._raw_client.hello(request_options=request_options)
        return _response.data
