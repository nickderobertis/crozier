

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSseClient, RawSseClient
from .types.sse_subscribe_request_types import SseSubscribeRequestTypes


class SseClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSseClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSseClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSseClient
        """
        return self._raw_client

    def sse_subscribe(
        self,
        *,
        types: typing.Optional[SseSubscribeRequestTypes] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[str]:
        """
        Get a stream of Server-Sent Events.

        Parameters
        ----------
        types : typing.Optional[SseSubscribeRequestTypes]
            Types of events to subscribe to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[str]
            Request fulfilled, stream of Server-Sent Events follows

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.sse.sse_subscribe()
        for chunk in response:
            yield chunk
        """
        with self._raw_client.sse_subscribe(types=types, request_options=request_options) as r:
            yield from r.data


class AsyncSseClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSseClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSseClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSseClient
        """
        return self._raw_client

    async def sse_subscribe(
        self,
        *,
        types: typing.Optional[SseSubscribeRequestTypes] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[str]:
        """
        Get a stream of Server-Sent Events.

        Parameters
        ----------
        types : typing.Optional[SseSubscribeRequestTypes]
            Types of events to subscribe to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[str]
            Request fulfilled, stream of Server-Sent Events follows

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            response = client.sse.sse_subscribe()
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.sse_subscribe(types=types, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk
