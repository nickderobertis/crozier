

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.watch_event import WatchEvent
from ..types.watch_event_filters import WatchEventFilters
from .raw_client import AsyncRawEventsClient, RawEventsClient


OMIT = typing.cast(typing.Any, ...)


class EventsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEventsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEventsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEventsClient
        """
        return self._raw_client

    def watch_events(
        self,
        *,
        filters: typing.Optional[WatchEventFilters] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[WatchEvent]:
        """
        Parameters
        ----------
        filters : typing.Optional[WatchEventFilters]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[WatchEvent]
            Server-Sent Events stream. Each data field contains one serialized
            CloudEvents 1.0 event. Comment fields are connection heartbeats.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.events.watch_events()
        for chunk in response:
            yield chunk
        """
        with self._raw_client.watch_events(filters=filters, request_options=request_options) as r:
            yield from r.data


class AsyncEventsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEventsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEventsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEventsClient
        """
        return self._raw_client

    async def watch_events(
        self,
        *,
        filters: typing.Optional[WatchEventFilters] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[WatchEvent]:
        """
        Parameters
        ----------
        filters : typing.Optional[WatchEventFilters]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[WatchEvent]
            Server-Sent Events stream. Each data field contains one serialized
            CloudEvents 1.0 event. Comment fields are connection heartbeats.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            response = await client.events.watch_events()
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.watch_events(filters=filters, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk
