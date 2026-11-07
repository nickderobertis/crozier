

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawStreamingClient, RawStreamingClient


class StreamingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStreamingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStreamingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStreamingClient
        """
        return self._raw_client

    def stream_live(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Iterator[str]:
        """
        Server-Sent Events stream with events named `live` that carry JSON payloads.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[str]
            Server-Sent Events stream

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        response = client.streaming.stream_live()
        for chunk in response:
            yield chunk
        """
        with self._raw_client.stream_live(request_options=request_options) as r:
            yield from r.data


class AsyncStreamingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStreamingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStreamingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStreamingClient
        """
        return self._raw_client

    async def stream_live(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[str]:
        """
        Server-Sent Events stream with events named `live` that carry JSON payloads.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[str]
            Server-Sent Events stream

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            response = client.streaming.stream_live()
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.stream_live(request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk
