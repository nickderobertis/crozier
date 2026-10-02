

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.paged_result_of_ticket import PagedResultOfTicket
from ..types.paged_result_of_ticket_comment import PagedResultOfTicketComment
from ..types.paged_result_of_ticket_event import PagedResultOfTicketEvent
from ..types.sort_direction import SortDirection
from ..types.ticket import Ticket
from ..types.ticket_comment import TicketComment
from ..types.ticket_impact import TicketImpact
from ..types.ticket_priority import TicketPriority
from ..types.ticket_urgency import TicketUrgency
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

    def gettickets(
        self,
        *,
        organization_id: typing.Optional[str] = None,
        project_id: typing.Optional[int] = None,
        status: typing.Optional[typing.Sequence[int]] = None,
        assignee_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_by: typing.Optional[str] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PagedResultOfTicket:
        """
        Parameters
        ----------
        organization_id : typing.Optional[str]

        project_id : typing.Optional[int]

        status : typing.Optional[typing.Sequence[int]]

        assignee_id : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[SortDirection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PagedResultOfTicket


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tickets.gettickets()
        """
        _response = self._raw_client.gettickets(
            organization_id=organization_id,
            project_id=project_id,
            status=status,
            assignee_id=assignee_id,
            page=page,
            page_size=page_size,
            sort_by=sort_by,
            sort_direction=sort_direction,
            request_options=request_options,
        )
        return _response.data

    def createticket(
        self,
        *,
        organization_id: typing.Optional[str] = None,
        project_id: typing.Optional[int] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        status: typing.Optional[int] = OMIT,
        assignee_id: typing.Optional[str] = OMIT,
        estimated_time: typing.Optional[str] = OMIT,
        completed_time: typing.Optional[str] = OMIT,
        remaining_time: typing.Optional[str] = OMIT,
        priority: typing.Optional[TicketPriority] = OMIT,
        impact: typing.Optional[TicketImpact] = OMIT,
        urgency: typing.Optional[TicketUrgency] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ticket:
        """
        Parameters
        ----------
        organization_id : typing.Optional[str]

        project_id : typing.Optional[int]

        title : typing.Optional[str]

        description : typing.Optional[str]

        status : typing.Optional[int]

        assignee_id : typing.Optional[str]

        estimated_time : typing.Optional[str]

        completed_time : typing.Optional[str]

        remaining_time : typing.Optional[str]

        priority : typing.Optional[TicketPriority]

        impact : typing.Optional[TicketImpact]

        urgency : typing.Optional[TicketUrgency]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ticket


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tickets.createticket()
        """
        _response = self._raw_client.createticket(
            organization_id=organization_id,
            project_id=project_id,
            title=title,
            description=description,
            status=status,
            assignee_id=assignee_id,
            estimated_time=estimated_time,
            completed_time=completed_time,
            remaining_time=remaining_time,
            priority=priority,
            impact=impact,
            urgency=urgency,
            request_options=request_options,
        )
        return _response.data

    def getticketevents(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_by: typing.Optional[str] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PagedResultOfTicketEvent:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[SortDirection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PagedResultOfTicketEvent


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tickets.getticketevents(
            id=1,
        )
        """
        _response = self._raw_client.getticketevents(
            id,
            organization_id=organization_id,
            page=page,
            page_size=page_size,
            sort_by=sort_by,
            sort_direction=sort_direction,
            request_options=request_options,
        )
        return _response.data

    def getticketbyid(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ticket:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ticket


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tickets.getticketbyid(
            id=1,
        )
        """
        _response = self._raw_client.getticketbyid(id, organization_id=organization_id, request_options=request_options)
        return _response.data

    def deleteticket(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

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
        client.tickets.deleteticket(
            id=1,
        )
        """
        _response = self._raw_client.deleteticket(id, organization_id=organization_id, request_options=request_options)
        return _response.data

    def updateproject(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        project_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        project_id : typing.Optional[int]

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
        client.tickets.updateproject(
            id=1,
        )
        """
        _response = self._raw_client.updateproject(
            id, organization_id=organization_id, project_id=project_id, request_options=request_options
        )
        return _response.data

    def updatepriority(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        priority: typing.Optional[TicketPriority] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        priority : typing.Optional[TicketPriority]

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
        client.tickets.updatepriority(
            id=1,
        )
        """
        _response = self._raw_client.updatepriority(
            id, organization_id=organization_id, priority=priority, request_options=request_options
        )
        return _response.data

    def updateurgency(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        urgency: typing.Optional[TicketUrgency] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        urgency : typing.Optional[TicketUrgency]

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
        client.tickets.updateurgency(
            id=1,
        )
        """
        _response = self._raw_client.updateurgency(
            id, organization_id=organization_id, urgency=urgency, request_options=request_options
        )
        return _response.data

    def updateimpact(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        impact: typing.Optional[TicketImpact] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        impact : typing.Optional[TicketImpact]

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
        client.tickets.updateimpact(
            id=1,
        )
        """
        _response = self._raw_client.updateimpact(
            id, organization_id=organization_id, impact=impact, request_options=request_options
        )
        return _response.data

    def updatetitle(
        self,
        id: int,
        *,
        request: str,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int

        request : str

        organization_id : typing.Optional[str]

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
        client.tickets.updatetitle(
            id=1,
            request="string",
        )
        """
        _response = self._raw_client.updatetitle(
            id, request=request, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    def updatetext(
        self,
        id: int,
        *,
        request: str,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int

        request : str

        organization_id : typing.Optional[str]

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
        client.tickets.updatetext(
            id=1,
            request="string",
        )
        """
        _response = self._raw_client.updatetext(
            id, request=request, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    def updatestatus(
        self,
        id: int,
        *,
        request: int,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int

        request : int

        organization_id : typing.Optional[str]

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
        client.tickets.updatestatus(
            id=1,
            request=1,
        )
        """
        _response = self._raw_client.updatestatus(
            id, request=request, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    def updateassignee(
        self,
        id: int,
        *,
        request: str,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int

        request : str

        organization_id : typing.Optional[str]

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
        client.tickets.updateassignee(
            id=1,
            request="string",
        )
        """
        _response = self._raw_client.updateassignee(
            id, request=request, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    def updateestimatedtime(
        self,
        id: int,
        *,
        request: str,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int

        request : str

        organization_id : typing.Optional[str]

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
        client.tickets.updateestimatedtime(
            id=1,
            request="string",
        )
        """
        _response = self._raw_client.updateestimatedtime(
            id, request=request, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    def updatecompletedtime(
        self,
        id: int,
        *,
        request: str,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int

        request : str

        organization_id : typing.Optional[str]

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
        client.tickets.updatecompletedtime(
            id=1,
            request="string",
        )
        """
        _response = self._raw_client.updatecompletedtime(
            id, request=request, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    def updateremainingtime(
        self,
        id: int,
        *,
        request: str,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int

        request : str

        organization_id : typing.Optional[str]

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
        client.tickets.updateremainingtime(
            id=1,
            request="string",
        )
        """
        _response = self._raw_client.updateremainingtime(
            id, request=request, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    def getticketcomments(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_by: typing.Optional[str] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PagedResultOfTicketComment:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[SortDirection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PagedResultOfTicketComment


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tickets.getticketcomments(
            id=1,
        )
        """
        _response = self._raw_client.getticketcomments(
            id,
            organization_id=organization_id,
            page=page,
            page_size=page_size,
            sort_by=sort_by,
            sort_direction=sort_direction,
            request_options=request_options,
        )
        return _response.data

    def postticketcomment(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        text: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TicketComment:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        text : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicketComment


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tickets.postticketcomment(
            id=1,
        )
        """
        _response = self._raw_client.postticketcomment(
            id, organization_id=organization_id, text=text, request_options=request_options
        )
        return _response.data

    def getticketcommentbyid(
        self,
        id: int,
        comment_id: int,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TicketComment:
        """
        Parameters
        ----------
        id : int

        comment_id : int

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicketComment


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tickets.getticketcommentbyid(
            id=1,
            comment_id=1,
        )
        """
        _response = self._raw_client.getticketcommentbyid(
            id, comment_id, organization_id=organization_id, request_options=request_options
        )
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

    async def gettickets(
        self,
        *,
        organization_id: typing.Optional[str] = None,
        project_id: typing.Optional[int] = None,
        status: typing.Optional[typing.Sequence[int]] = None,
        assignee_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_by: typing.Optional[str] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PagedResultOfTicket:
        """
        Parameters
        ----------
        organization_id : typing.Optional[str]

        project_id : typing.Optional[int]

        status : typing.Optional[typing.Sequence[int]]

        assignee_id : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[SortDirection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PagedResultOfTicket


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tickets.gettickets()


        asyncio.run(main())
        """
        _response = await self._raw_client.gettickets(
            organization_id=organization_id,
            project_id=project_id,
            status=status,
            assignee_id=assignee_id,
            page=page,
            page_size=page_size,
            sort_by=sort_by,
            sort_direction=sort_direction,
            request_options=request_options,
        )
        return _response.data

    async def createticket(
        self,
        *,
        organization_id: typing.Optional[str] = None,
        project_id: typing.Optional[int] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        status: typing.Optional[int] = OMIT,
        assignee_id: typing.Optional[str] = OMIT,
        estimated_time: typing.Optional[str] = OMIT,
        completed_time: typing.Optional[str] = OMIT,
        remaining_time: typing.Optional[str] = OMIT,
        priority: typing.Optional[TicketPriority] = OMIT,
        impact: typing.Optional[TicketImpact] = OMIT,
        urgency: typing.Optional[TicketUrgency] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ticket:
        """
        Parameters
        ----------
        organization_id : typing.Optional[str]

        project_id : typing.Optional[int]

        title : typing.Optional[str]

        description : typing.Optional[str]

        status : typing.Optional[int]

        assignee_id : typing.Optional[str]

        estimated_time : typing.Optional[str]

        completed_time : typing.Optional[str]

        remaining_time : typing.Optional[str]

        priority : typing.Optional[TicketPriority]

        impact : typing.Optional[TicketImpact]

        urgency : typing.Optional[TicketUrgency]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ticket


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tickets.createticket()


        asyncio.run(main())
        """
        _response = await self._raw_client.createticket(
            organization_id=organization_id,
            project_id=project_id,
            title=title,
            description=description,
            status=status,
            assignee_id=assignee_id,
            estimated_time=estimated_time,
            completed_time=completed_time,
            remaining_time=remaining_time,
            priority=priority,
            impact=impact,
            urgency=urgency,
            request_options=request_options,
        )
        return _response.data

    async def getticketevents(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_by: typing.Optional[str] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PagedResultOfTicketEvent:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[SortDirection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PagedResultOfTicketEvent


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tickets.getticketevents(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getticketevents(
            id,
            organization_id=organization_id,
            page=page,
            page_size=page_size,
            sort_by=sort_by,
            sort_direction=sort_direction,
            request_options=request_options,
        )
        return _response.data

    async def getticketbyid(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ticket:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ticket


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tickets.getticketbyid(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getticketbyid(
            id, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    async def deleteticket(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

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
            await client.tickets.deleteticket(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deleteticket(
            id, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    async def updateproject(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        project_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        project_id : typing.Optional[int]

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
            await client.tickets.updateproject(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updateproject(
            id, organization_id=organization_id, project_id=project_id, request_options=request_options
        )
        return _response.data

    async def updatepriority(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        priority: typing.Optional[TicketPriority] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        priority : typing.Optional[TicketPriority]

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
            await client.tickets.updatepriority(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updatepriority(
            id, organization_id=organization_id, priority=priority, request_options=request_options
        )
        return _response.data

    async def updateurgency(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        urgency: typing.Optional[TicketUrgency] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        urgency : typing.Optional[TicketUrgency]

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
            await client.tickets.updateurgency(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updateurgency(
            id, organization_id=organization_id, urgency=urgency, request_options=request_options
        )
        return _response.data

    async def updateimpact(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        impact: typing.Optional[TicketImpact] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        impact : typing.Optional[TicketImpact]

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
            await client.tickets.updateimpact(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updateimpact(
            id, organization_id=organization_id, impact=impact, request_options=request_options
        )
        return _response.data

    async def updatetitle(
        self,
        id: int,
        *,
        request: str,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int

        request : str

        organization_id : typing.Optional[str]

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
            await client.tickets.updatetitle(
                id=1,
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updatetitle(
            id, request=request, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    async def updatetext(
        self,
        id: int,
        *,
        request: str,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int

        request : str

        organization_id : typing.Optional[str]

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
            await client.tickets.updatetext(
                id=1,
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updatetext(
            id, request=request, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    async def updatestatus(
        self,
        id: int,
        *,
        request: int,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int

        request : int

        organization_id : typing.Optional[str]

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
            await client.tickets.updatestatus(
                id=1,
                request=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updatestatus(
            id, request=request, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    async def updateassignee(
        self,
        id: int,
        *,
        request: str,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int

        request : str

        organization_id : typing.Optional[str]

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
            await client.tickets.updateassignee(
                id=1,
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updateassignee(
            id, request=request, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    async def updateestimatedtime(
        self,
        id: int,
        *,
        request: str,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int

        request : str

        organization_id : typing.Optional[str]

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
            await client.tickets.updateestimatedtime(
                id=1,
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updateestimatedtime(
            id, request=request, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    async def updatecompletedtime(
        self,
        id: int,
        *,
        request: str,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int

        request : str

        organization_id : typing.Optional[str]

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
            await client.tickets.updatecompletedtime(
                id=1,
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updatecompletedtime(
            id, request=request, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    async def updateremainingtime(
        self,
        id: int,
        *,
        request: str,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : int

        request : str

        organization_id : typing.Optional[str]

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
            await client.tickets.updateremainingtime(
                id=1,
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updateremainingtime(
            id, request=request, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    async def getticketcomments(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        sort_by: typing.Optional[str] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PagedResultOfTicketComment:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[SortDirection]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PagedResultOfTicketComment


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tickets.getticketcomments(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getticketcomments(
            id,
            organization_id=organization_id,
            page=page,
            page_size=page_size,
            sort_by=sort_by,
            sort_direction=sort_direction,
            request_options=request_options,
        )
        return _response.data

    async def postticketcomment(
        self,
        id: int,
        *,
        organization_id: typing.Optional[str] = None,
        text: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TicketComment:
        """
        Parameters
        ----------
        id : int

        organization_id : typing.Optional[str]

        text : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicketComment


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tickets.postticketcomment(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.postticketcomment(
            id, organization_id=organization_id, text=text, request_options=request_options
        )
        return _response.data

    async def getticketcommentbyid(
        self,
        id: int,
        comment_id: int,
        *,
        organization_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TicketComment:
        """
        Parameters
        ----------
        id : int

        comment_id : int

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicketComment


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tickets.getticketcommentbyid(
                id=1,
                comment_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getticketcommentbyid(
            id, comment_id, organization_id=organization_id, request_options=request_options
        )
        return _response.data
