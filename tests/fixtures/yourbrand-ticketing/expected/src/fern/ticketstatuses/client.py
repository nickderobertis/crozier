

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.paged_result_of_ticket_status import PagedResultOfTicketStatus
from ..types.sort_direction import SortDirection
from ..types.ticket_status import TicketStatus
from .raw_client import AsyncRawTicketstatusesClient, RawTicketstatusesClient


OMIT = typing.cast(typing.Any, ...)


class TicketstatusesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTicketstatusesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTicketstatusesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTicketstatusesClient
        """
        return self._raw_client

    def getstatuses(
        self,
        *,
        organization_id: typing.Optional[str] = None,
        search_term: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_by: typing.Optional[str] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PagedResultOfTicketStatus:
        """
        Parameters
        ----------
        organization_id : typing.Optional[str]

        search_term : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[SortDirection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PagedResultOfTicketStatus


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ticketstatuses.getstatuses()
        """
        _response = self._raw_client.getstatuses(
            organization_id=organization_id,
            search_term=search_term,
            page=page,
            page_size=page_size,
            sort_by=sort_by,
            sort_direction=sort_direction,
            request_options=request_options,
        )
        return _response.data

    def createticketstatus(
        self,
        *,
        organization_id: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        handle: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TicketStatus:
        """
        Parameters
        ----------
        organization_id : typing.Optional[str]

        name : typing.Optional[str]

        handle : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicketStatus


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ticketstatuses.createticketstatus()
        """
        _response = self._raw_client.createticketstatus(
            organization_id=organization_id,
            name=name,
            handle=handle,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def getticketstatusbyid(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TicketStatus:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicketStatus


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ticketstatuses.getticketstatusbyid(
            id=1,
        )
        """
        _response = self._raw_client.getticketstatusbyid(
            id, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    def updateticketstatus(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        handle: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TicketStatus:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        name : typing.Optional[str]

        handle : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicketStatus


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ticketstatuses.updateticketstatus(
            id=1,
        )
        """
        _response = self._raw_client.updateticketstatus(
            id,
            organization_id=organization_id,
            name=name,
            handle=handle,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def deleteticketstatus(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TicketStatus:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicketStatus


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ticketstatuses.deleteticketstatus(
            id=1,
        )
        """
        _response = self._raw_client.deleteticketstatus(
            id, organization_id=organization_id, request_options=request_options
        )
        return _response.data


class AsyncTicketstatusesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTicketstatusesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTicketstatusesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTicketstatusesClient
        """
        return self._raw_client

    async def getstatuses(
        self,
        *,
        organization_id: typing.Optional[str] = None,
        search_term: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_by: typing.Optional[str] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PagedResultOfTicketStatus:
        """
        Parameters
        ----------
        organization_id : typing.Optional[str]

        search_term : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[SortDirection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PagedResultOfTicketStatus


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ticketstatuses.getstatuses()


        asyncio.run(main())
        """
        _response = await self._raw_client.getstatuses(
            organization_id=organization_id,
            search_term=search_term,
            page=page,
            page_size=page_size,
            sort_by=sort_by,
            sort_direction=sort_direction,
            request_options=request_options,
        )
        return _response.data

    async def createticketstatus(
        self,
        *,
        organization_id: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        handle: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TicketStatus:
        """
        Parameters
        ----------
        organization_id : typing.Optional[str]

        name : typing.Optional[str]

        handle : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicketStatus


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ticketstatuses.createticketstatus()


        asyncio.run(main())
        """
        _response = await self._raw_client.createticketstatus(
            organization_id=organization_id,
            name=name,
            handle=handle,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def getticketstatusbyid(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TicketStatus:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicketStatus


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ticketstatuses.getticketstatusbyid(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getticketstatusbyid(
            id, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    async def updateticketstatus(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        handle: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TicketStatus:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        name : typing.Optional[str]

        handle : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicketStatus


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ticketstatuses.updateticketstatus(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updateticketstatus(
            id,
            organization_id=organization_id,
            name=name,
            handle=handle,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def deleteticketstatus(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TicketStatus:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicketStatus


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ticketstatuses.deleteticketstatus(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deleteticketstatus(
            id, organization_id=organization_id, request_options=request_options
        )
        return _response.data
