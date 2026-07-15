

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.assignee import Assignee
from ..types.collection_tag import CollectionTag
from ..types.create_ticket_response import CreateTicketResponse
from ..types.created_at import CreatedAt
from ..types.created_by import CreatedBy
from ..types.delete_ticket_response import DeleteTicketResponse
from ..types.get_ticket_response import GetTicketResponse
from ..types.get_tickets_response import GetTicketsResponse
from ..types.id import Id
from ..types.issues_filter import IssuesFilter
from ..types.ticket_priority import TicketPriority
from ..types.tickets_sort import TicketsSort
from ..types.update_ticket_response import UpdateTicketResponse
from ..types.updated_at import UpdatedAt
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

    def collection_tickets_all(
        self,
        collection_id: str,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        sort: typing.Optional[TicketsSort] = None,
        filter: typing.Optional[IssuesFilter] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetTicketsResponse:
        """
        List Tickets

        Parameters
        ----------
        collection_id : str
            The collection ID

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        sort : typing.Optional[TicketsSort]
            Apply sorting

        filter : typing.Optional[IssuesFilter]
            Apply filters

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTicketsResponse
            List Tickets

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.tickets.collection_tickets_all(
            collection_id="apideck-io",
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.collection_tickets_all(
            collection_id,
            raw=raw,
            cursor=cursor,
            limit=limit,
            sort=sort,
            filter=filter,
            fields=fields,
            request_options=request_options,
        )
        return _response.data

    def collection_tickets_add(
        self,
        collection_id_: str,
        *,
        raw: typing.Optional[bool] = None,
        assignees: typing.Optional[typing.Sequence[Assignee]] = OMIT,
        collection_id: typing.Optional[str] = OMIT,
        completed_at: typing.Optional[dt.datetime] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        description: typing.Optional[str] = OMIT,
        due_date: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[Id] = OMIT,
        parent_id: typing.Optional[str] = OMIT,
        priority: typing.Optional[TicketPriority] = OMIT,
        status: typing.Optional[str] = OMIT,
        subject: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[CollectionTag]] = OMIT,
        type: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateTicketResponse:
        """
        Create Ticket

        Parameters
        ----------
        collection_id_ : str
            The collection ID

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        assignees : typing.Optional[typing.Sequence[Assignee]]

        collection_id : typing.Optional[str]
            The ticket's collection ID

        completed_at : typing.Optional[dt.datetime]
            When the ticket was completed

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        description : typing.Optional[str]
            The ticket's description. HTML version of description is mapped if supported by the third-party platform

        due_date : typing.Optional[dt.datetime]
            Due date of the ticket

        id : typing.Optional[Id]

        parent_id : typing.Optional[str]
            The ticket's parent ID

        priority : typing.Optional[TicketPriority]
            Priority of the ticket

        status : typing.Optional[str]
            The current status of the ticket. Possible values include: open, in_progress, closed, or - in cases where there is no clear mapping - the original value passed through.

        subject : typing.Optional[str]
            Subject of the ticket

        tags : typing.Optional[typing.Sequence[CollectionTag]]

        type : typing.Optional[str]
            The ticket's type

        updated_at : typing.Optional[UpdatedAt]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateTicketResponse
            Create a Ticket

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.tickets.collection_tickets_add(
            collection_id_="apideck-io",
        )
        """
        _response = self._raw_client.collection_tickets_add(
            collection_id_,
            raw=raw,
            assignees=assignees,
            collection_id=collection_id,
            completed_at=completed_at,
            created_at=created_at,
            created_by=created_by,
            description=description,
            due_date=due_date,
            id=id,
            parent_id=parent_id,
            priority=priority,
            status=status,
            subject=subject,
            tags=tags,
            type=type,
            updated_at=updated_at,
            request_options=request_options,
        )
        return _response.data

    def collection_tickets_one(
        self,
        collection_id: str,
        ticket_id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetTicketResponse:
        """
        Get Ticket

        Parameters
        ----------
        collection_id : str
            The collection ID

        ticket_id : str
            ID of the ticket you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTicketResponse
            Get a Ticket

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.tickets.collection_tickets_one(
            collection_id="apideck-io",
            ticket_id="ticket_id",
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.collection_tickets_one(
            collection_id, ticket_id, raw=raw, fields=fields, request_options=request_options
        )
        return _response.data

    def collection_tickets_delete(
        self,
        collection_id: str,
        ticket_id: str,
        *,
        raw: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteTicketResponse:
        """
        Delete Ticket

        Parameters
        ----------
        collection_id : str
            The collection ID

        ticket_id : str
            ID of the ticket you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteTicketResponse
            Delete a Ticket

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.tickets.collection_tickets_delete(
            collection_id="apideck-io",
            ticket_id="ticket_id",
        )
        """
        _response = self._raw_client.collection_tickets_delete(
            collection_id, ticket_id, raw=raw, request_options=request_options
        )
        return _response.data

    def collection_tickets_update(
        self,
        collection_id_: str,
        ticket_id: str,
        *,
        raw: typing.Optional[bool] = None,
        assignees: typing.Optional[typing.Sequence[Assignee]] = OMIT,
        collection_id: typing.Optional[str] = OMIT,
        completed_at: typing.Optional[dt.datetime] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        description: typing.Optional[str] = OMIT,
        due_date: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[Id] = OMIT,
        parent_id: typing.Optional[str] = OMIT,
        priority: typing.Optional[TicketPriority] = OMIT,
        status: typing.Optional[str] = OMIT,
        subject: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[CollectionTag]] = OMIT,
        type: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateTicketResponse:
        """
        Update Ticket

        Parameters
        ----------
        collection_id_ : str
            The collection ID

        ticket_id : str
            ID of the ticket you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        assignees : typing.Optional[typing.Sequence[Assignee]]

        collection_id : typing.Optional[str]
            The ticket's collection ID

        completed_at : typing.Optional[dt.datetime]
            When the ticket was completed

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        description : typing.Optional[str]
            The ticket's description. HTML version of description is mapped if supported by the third-party platform

        due_date : typing.Optional[dt.datetime]
            Due date of the ticket

        id : typing.Optional[Id]

        parent_id : typing.Optional[str]
            The ticket's parent ID

        priority : typing.Optional[TicketPriority]
            Priority of the ticket

        status : typing.Optional[str]
            The current status of the ticket. Possible values include: open, in_progress, closed, or - in cases where there is no clear mapping - the original value passed through.

        subject : typing.Optional[str]
            Subject of the ticket

        tags : typing.Optional[typing.Sequence[CollectionTag]]

        type : typing.Optional[str]
            The ticket's type

        updated_at : typing.Optional[UpdatedAt]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateTicketResponse
            Update a Ticket

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.tickets.collection_tickets_update(
            collection_id_="apideck-io",
            ticket_id="ticket_id",
        )
        """
        _response = self._raw_client.collection_tickets_update(
            collection_id_,
            ticket_id,
            raw=raw,
            assignees=assignees,
            collection_id=collection_id,
            completed_at=completed_at,
            created_at=created_at,
            created_by=created_by,
            description=description,
            due_date=due_date,
            id=id,
            parent_id=parent_id,
            priority=priority,
            status=status,
            subject=subject,
            tags=tags,
            type=type,
            updated_at=updated_at,
            request_options=request_options,
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

    async def collection_tickets_all(
        self,
        collection_id: str,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        sort: typing.Optional[TicketsSort] = None,
        filter: typing.Optional[IssuesFilter] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetTicketsResponse:
        """
        List Tickets

        Parameters
        ----------
        collection_id : str
            The collection ID

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        sort : typing.Optional[TicketsSort]
            Apply sorting

        filter : typing.Optional[IssuesFilter]
            Apply filters

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTicketsResponse
            List Tickets

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tickets.collection_tickets_all(
                collection_id="apideck-io",
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.collection_tickets_all(
            collection_id,
            raw=raw,
            cursor=cursor,
            limit=limit,
            sort=sort,
            filter=filter,
            fields=fields,
            request_options=request_options,
        )
        return _response.data

    async def collection_tickets_add(
        self,
        collection_id_: str,
        *,
        raw: typing.Optional[bool] = None,
        assignees: typing.Optional[typing.Sequence[Assignee]] = OMIT,
        collection_id: typing.Optional[str] = OMIT,
        completed_at: typing.Optional[dt.datetime] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        description: typing.Optional[str] = OMIT,
        due_date: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[Id] = OMIT,
        parent_id: typing.Optional[str] = OMIT,
        priority: typing.Optional[TicketPriority] = OMIT,
        status: typing.Optional[str] = OMIT,
        subject: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[CollectionTag]] = OMIT,
        type: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateTicketResponse:
        """
        Create Ticket

        Parameters
        ----------
        collection_id_ : str
            The collection ID

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        assignees : typing.Optional[typing.Sequence[Assignee]]

        collection_id : typing.Optional[str]
            The ticket's collection ID

        completed_at : typing.Optional[dt.datetime]
            When the ticket was completed

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        description : typing.Optional[str]
            The ticket's description. HTML version of description is mapped if supported by the third-party platform

        due_date : typing.Optional[dt.datetime]
            Due date of the ticket

        id : typing.Optional[Id]

        parent_id : typing.Optional[str]
            The ticket's parent ID

        priority : typing.Optional[TicketPriority]
            Priority of the ticket

        status : typing.Optional[str]
            The current status of the ticket. Possible values include: open, in_progress, closed, or - in cases where there is no clear mapping - the original value passed through.

        subject : typing.Optional[str]
            Subject of the ticket

        tags : typing.Optional[typing.Sequence[CollectionTag]]

        type : typing.Optional[str]
            The ticket's type

        updated_at : typing.Optional[UpdatedAt]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateTicketResponse
            Create a Ticket

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tickets.collection_tickets_add(
                collection_id_="apideck-io",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.collection_tickets_add(
            collection_id_,
            raw=raw,
            assignees=assignees,
            collection_id=collection_id,
            completed_at=completed_at,
            created_at=created_at,
            created_by=created_by,
            description=description,
            due_date=due_date,
            id=id,
            parent_id=parent_id,
            priority=priority,
            status=status,
            subject=subject,
            tags=tags,
            type=type,
            updated_at=updated_at,
            request_options=request_options,
        )
        return _response.data

    async def collection_tickets_one(
        self,
        collection_id: str,
        ticket_id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetTicketResponse:
        """
        Get Ticket

        Parameters
        ----------
        collection_id : str
            The collection ID

        ticket_id : str
            ID of the ticket you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTicketResponse
            Get a Ticket

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tickets.collection_tickets_one(
                collection_id="apideck-io",
                ticket_id="ticket_id",
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.collection_tickets_one(
            collection_id, ticket_id, raw=raw, fields=fields, request_options=request_options
        )
        return _response.data

    async def collection_tickets_delete(
        self,
        collection_id: str,
        ticket_id: str,
        *,
        raw: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteTicketResponse:
        """
        Delete Ticket

        Parameters
        ----------
        collection_id : str
            The collection ID

        ticket_id : str
            ID of the ticket you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteTicketResponse
            Delete a Ticket

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tickets.collection_tickets_delete(
                collection_id="apideck-io",
                ticket_id="ticket_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.collection_tickets_delete(
            collection_id, ticket_id, raw=raw, request_options=request_options
        )
        return _response.data

    async def collection_tickets_update(
        self,
        collection_id_: str,
        ticket_id: str,
        *,
        raw: typing.Optional[bool] = None,
        assignees: typing.Optional[typing.Sequence[Assignee]] = OMIT,
        collection_id: typing.Optional[str] = OMIT,
        completed_at: typing.Optional[dt.datetime] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        description: typing.Optional[str] = OMIT,
        due_date: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[Id] = OMIT,
        parent_id: typing.Optional[str] = OMIT,
        priority: typing.Optional[TicketPriority] = OMIT,
        status: typing.Optional[str] = OMIT,
        subject: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[CollectionTag]] = OMIT,
        type: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateTicketResponse:
        """
        Update Ticket

        Parameters
        ----------
        collection_id_ : str
            The collection ID

        ticket_id : str
            ID of the ticket you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        assignees : typing.Optional[typing.Sequence[Assignee]]

        collection_id : typing.Optional[str]
            The ticket's collection ID

        completed_at : typing.Optional[dt.datetime]
            When the ticket was completed

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        description : typing.Optional[str]
            The ticket's description. HTML version of description is mapped if supported by the third-party platform

        due_date : typing.Optional[dt.datetime]
            Due date of the ticket

        id : typing.Optional[Id]

        parent_id : typing.Optional[str]
            The ticket's parent ID

        priority : typing.Optional[TicketPriority]
            Priority of the ticket

        status : typing.Optional[str]
            The current status of the ticket. Possible values include: open, in_progress, closed, or - in cases where there is no clear mapping - the original value passed through.

        subject : typing.Optional[str]
            Subject of the ticket

        tags : typing.Optional[typing.Sequence[CollectionTag]]

        type : typing.Optional[str]
            The ticket's type

        updated_at : typing.Optional[UpdatedAt]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateTicketResponse
            Update a Ticket

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tickets.collection_tickets_update(
                collection_id_="apideck-io",
                ticket_id="ticket_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.collection_tickets_update(
            collection_id_,
            ticket_id,
            raw=raw,
            assignees=assignees,
            collection_id=collection_id,
            completed_at=completed_at,
            created_at=created_at,
            created_by=created_by,
            description=description,
            due_date=due_date,
            id=id,
            parent_id=parent_id,
            priority=priority,
            status=status,
            subject=subject,
            tags=tags,
            type=type,
            updated_at=updated_at,
            request_options=request_options,
        )
        return _response.data
