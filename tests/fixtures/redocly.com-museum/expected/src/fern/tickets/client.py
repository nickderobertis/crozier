

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.date import Date
from ..types.email import Email
from ..types.event_id import EventId
from ..types.museum_tickets_confirmation import MuseumTicketsConfirmation
from ..types.ticket_id import TicketId
from ..types.ticket_type import TicketType
from .raw_client import AsyncRawTicketsClient, RawTicketsClient


OMIT = typing.cast(typing.Any, ...)


class TicketsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTicketsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTicketsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTicketsClient
        """
        return self._raw_client

    def buy_museum_tickets(
        self,
        *,
        ticket_date: Date,
        ticket_type: TicketType,
        email: typing.Optional[Email] = OMIT,
        ticket_id: typing.Optional[TicketId] = OMIT,
        event_id: typing.Optional[EventId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MuseumTicketsConfirmation:
        """
        Purchase museum tickets for general entry or special events.

        Parameters
        ----------
        ticket_date : Date
            Date when this ticket can be used for museum entry.

        ticket_type : TicketType

        email : typing.Optional[Email]

        ticket_id : typing.Optional[TicketId]

        event_id : typing.Optional[EventId]
            Unique identifier for a special event. Required if purchasing tickets for the museum's special events.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MuseumTicketsConfirmation
            Created.

        Examples
        --------
        import datetime

        from fern import FernApi, TicketType

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.tickets.buy_museum_tickets(
            ticket_date=datetime.date.fromisoformat(
                "2023-09-07",
            ),
            ticket_type=TicketType.GENERAL,
            email="todd@example.com",
        )
        """
        _response = self._raw_client.buy_museum_tickets(
            ticket_date=ticket_date,
            ticket_type=ticket_type,
            email=email,
            ticket_id=ticket_id,
            event_id=event_id,
            request_options=request_options,
        )
        return _response.data

    def get_ticket_code(
        self, ticket_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Return an image of your ticket with scannable QR code. Used for event entry.

        Parameters
        ----------
        ticket_id : str
            Identifier for a ticket to a museum event. Used to generate ticket image.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Scannable event ticket in image format.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.tickets.get_ticket_code(
            ticket_id="ticketId",
        )
        """
        with self._raw_client.get_ticket_code(ticket_id, request_options=request_options) as r:
            yield from r.data


class AsyncTicketsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTicketsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTicketsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTicketsClient
        """
        return self._raw_client

    async def buy_museum_tickets(
        self,
        *,
        ticket_date: Date,
        ticket_type: TicketType,
        email: typing.Optional[Email] = OMIT,
        ticket_id: typing.Optional[TicketId] = OMIT,
        event_id: typing.Optional[EventId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MuseumTicketsConfirmation:
        """
        Purchase museum tickets for general entry or special events.

        Parameters
        ----------
        ticket_date : Date
            Date when this ticket can be used for museum entry.

        ticket_type : TicketType

        email : typing.Optional[Email]

        ticket_id : typing.Optional[TicketId]

        event_id : typing.Optional[EventId]
            Unique identifier for a special event. Required if purchasing tickets for the museum's special events.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MuseumTicketsConfirmation
            Created.

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi, TicketType

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.tickets.buy_museum_tickets(
                ticket_date=datetime.date.fromisoformat(
                    "2023-09-07",
                ),
                ticket_type=TicketType.GENERAL,
                email="todd@example.com",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.buy_museum_tickets(
            ticket_date=ticket_date,
            ticket_type=ticket_type,
            email=email,
            ticket_id=ticket_id,
            event_id=event_id,
            request_options=request_options,
        )
        return _response.data

    async def get_ticket_code(
        self, ticket_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Return an image of your ticket with scannable QR code. Used for event entry.

        Parameters
        ----------
        ticket_id : str
            Identifier for a ticket to a museum event. Used to generate ticket image.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Scannable event ticket in image format.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.tickets.get_ticket_code(
                ticket_id="ticketId",
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_ticket_code(ticket_id, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk
