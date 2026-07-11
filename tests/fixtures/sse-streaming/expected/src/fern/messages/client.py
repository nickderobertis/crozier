

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawMessagesClient, RawMessagesClient


class MessagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMessagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMessagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMessagesClient
        """
        return self._raw_client

    def streammessages(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[typing.Optional[typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[typing.Optional[typing.Any]]
            SSE stream

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.messages.streammessages()
        for chunk in response:
            yield chunk
        """
        with self._raw_client.streammessages(request_options=request_options) as r:
            yield from r.data


class AsyncMessagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMessagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMessagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMessagesClient
        """
        return self._raw_client

    async def streammessages(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[typing.Optional[typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[typing.Optional[typing.Any]]
            SSE stream

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            response = await client.messages.streammessages()
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.streammessages(request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk
