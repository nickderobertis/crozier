

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawTicketsClient, RawTicketsClient


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

    def list_tickets(
        self,
        *,
        referer: typing.Optional[str] = None,
        host: typing.Optional[str] = None,
        accept_encoding: typing.Optional[str] = None,
        note: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        referer : typing.Optional[str]

        host : typing.Optional[str]

        accept_encoding : typing.Optional[str]

        note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Tickets.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tickets.list_tickets()
        """
        _response = self._raw_client.list_tickets(
            referer=referer, host=host, accept_encoding=accept_encoding, note=note, request_options=request_options
        )
        return _response.data

    def open_ticket(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tickets.open_ticket()
        """
        _response = self._raw_client.open_ticket(request_options=request_options)
        return _response.data

    def get_ticket(self, ticket_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        ticket_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            One ticket.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tickets.get_ticket(
            ticket_id="ticket_id",
        )
        """
        _response = self._raw_client.get_ticket(ticket_id, request_options=request_options)
        return _response.data


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

    async def list_tickets(
        self,
        *,
        referer: typing.Optional[str] = None,
        host: typing.Optional[str] = None,
        accept_encoding: typing.Optional[str] = None,
        note: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        referer : typing.Optional[str]

        host : typing.Optional[str]

        accept_encoding : typing.Optional[str]

        note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Tickets.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tickets.list_tickets()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tickets(
            referer=referer, host=host, accept_encoding=accept_encoding, note=note, request_options=request_options
        )
        return _response.data

    async def open_ticket(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tickets.open_ticket()


        asyncio.run(main())
        """
        _response = await self._raw_client.open_ticket(request_options=request_options)
        return _response.data

    async def get_ticket(self, ticket_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        ticket_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            One ticket.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tickets.get_ticket(
                ticket_id="ticket_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_ticket(ticket_id, request_options=request_options)
        return _response.data
