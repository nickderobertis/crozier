

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

    def list_tickets(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Parameters
        ----------
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
            desk_agent="YOUR_DESK_AGENT",
            api_key="YOUR_API_KEY",
        )
        client.tickets.list_tickets()
        """
        _response = self._raw_client.list_tickets(request_options=request_options)
        return _response.data

    def list_escalated_tickets(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Escalated tickets.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            desk_agent="YOUR_DESK_AGENT",
            api_key="YOUR_API_KEY",
        )
        client.tickets.list_escalated_tickets()
        """
        _response = self._raw_client.list_escalated_tickets(request_options=request_options)
        return _response.data

    def list_archived_tickets(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Archived tickets.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            desk_agent="YOUR_DESK_AGENT",
            api_key="YOUR_API_KEY",
        )
        client.tickets.list_archived_tickets()
        """
        _response = self._raw_client.list_archived_tickets(request_options=request_options)
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

    async def list_tickets(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Parameters
        ----------
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
            desk_agent="YOUR_DESK_AGENT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tickets.list_tickets()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tickets(request_options=request_options)
        return _response.data

    async def list_escalated_tickets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Escalated tickets.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            desk_agent="YOUR_DESK_AGENT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tickets.list_escalated_tickets()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_escalated_tickets(request_options=request_options)
        return _response.data

    async def list_archived_tickets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Archived tickets.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            desk_agent="YOUR_DESK_AGENT",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tickets.list_archived_tickets()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_archived_tickets(request_options=request_options)
        return _response.data
