

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.event_stream_ticket import EventStreamTicket
from .raw_client import AsyncRawEventsClient, RawEventsClient


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

    def create_event_stream_ticket(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EventStreamTicket:
        """
        Create a short-lived browser-compatible event stream credential.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EventStreamTicket
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.events.create_event_stream_ticket()
        """
        _response = self._raw_client.create_event_stream_ticket(request_options=request_options)
        return _response.data

    def stream_events(
        self,
        *,
        after: typing.Optional[int] = None,
        types: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        last_event_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Subscribe to ordered, replayable events for the authenticated user.

        Parameters
        ----------
        after : typing.Optional[int]
            Header-equivalent cursor for clients that cannot set Last-Event-ID.

        types : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional comma-separated event types to include.

        last_event_id : typing.Optional[str]
            Resume after the last successfully processed event.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.events.stream_events()
        """
        with self._raw_client.stream_events(
            after=after, types=types, last_event_id=last_event_id, request_options=request_options
        ) as r:
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

    async def create_event_stream_ticket(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EventStreamTicket:
        """
        Create a short-lived browser-compatible event stream credential.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EventStreamTicket
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.events.create_event_stream_ticket()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_event_stream_ticket(request_options=request_options)
        return _response.data

    async def stream_events(
        self,
        *,
        after: typing.Optional[int] = None,
        types: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        last_event_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Subscribe to ordered, replayable events for the authenticated user.

        Parameters
        ----------
        after : typing.Optional[int]
            Header-equivalent cursor for clients that cannot set Last-Event-ID.

        types : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional comma-separated event types to include.

        last_event_id : typing.Optional[str]
            Resume after the last successfully processed event.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.events.stream_events()


        asyncio.run(main())
        """
        async with self._raw_client.stream_events(
            after=after, types=types, last_event_id=last_event_id, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk
