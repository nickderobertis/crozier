

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.common_event_association import CommonEventAssociation
from ..types.crm_create_or_update_event_response import CrmCreateOrUpdateEventResponse
from ..types.crm_delete_event_response import CrmDeleteEventResponse
from ..types.crm_get_event_response import CrmGetEventResponse
from ..types.crm_get_events_response import CrmGetEventsResponse
from ..types.crm_search_events_response import CrmSearchEventsResponse
from .raw_client import AsyncRawCrmEventClient, RawCrmEventClient


OMIT = typing.cast(typing.Any, ...)


class CrmEventClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCrmEventClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCrmEventClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCrmEventClient
        """
        return self._raw_client

    def crm_event_get_event(
        self,
        id: str,
        *,
        fields: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmGetEventResponse:
        """
        Get details of a event

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmGetEventResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_event.crm_event_get_event(
            id="id",
        )
        """
        _response = self._raw_client.crm_event_get_event(
            id, fields=fields, associations=associations, request_options=request_options
        )
        return _response.data

    def crm_event_delete_event(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CrmDeleteEventResponse:
        """
        Delete details of an event in a CRM

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmDeleteEventResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_event.crm_event_delete_event(
            id="id",
        )
        """
        _response = self._raw_client.crm_event_delete_event(id, request_options=request_options)
        return _response.data

    def crm_event_update_event(
        self,
        id: str,
        *,
        additional: typing.Any,
        type: str,
        subject: str,
        start_date_time: str,
        end_date_time: str,
        is_all_day_event: bool,
        description: str,
        location: str,
        associations: typing.Optional[CommonEventAssociation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmCreateOrUpdateEventResponse:
        """
        Update a event

        Parameters
        ----------
        id : str

        additional : typing.Any

        type : str
            The type of the event in the CRM.

        subject : str
            The Subject of the event/meeting in the CRM.

        start_date_time : str
            Event start date time.

        end_date_time : str
            Event end date time.

        is_all_day_event : bool
            Is `true` if the event is an all day event.

        description : str
            Description of the event/meeting.

        location : str
            The location of the event/meeting.

        associations : typing.Optional[CommonEventAssociation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmCreateOrUpdateEventResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_event.crm_event_update_event(
            id="id",
            additional={"key": "value"},
            type="type",
            subject="subject",
            start_date_time="startDateTime",
            end_date_time="endDateTime",
            is_all_day_event=True,
            description="description",
            location="location",
        )
        """
        _response = self._raw_client.crm_event_update_event(
            id,
            additional=additional,
            type=type,
            subject=subject,
            start_date_time=start_date_time,
            end_date_time=end_date_time,
            is_all_day_event=is_all_day_event,
            description=description,
            location=location,
            associations=associations,
            request_options=request_options,
        )
        return _response.data

    def crm_event_get_events(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmGetEventsResponse:
        """
        Get all the events

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmGetEventsResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_event.crm_event_get_events()
        """
        _response = self._raw_client.crm_event_get_events(
            fields=fields,
            page_size=page_size,
            cursor=cursor,
            associations=associations,
            request_options=request_options,
        )
        return _response.data

    def crm_event_create_event(
        self,
        *,
        additional: typing.Any,
        type: str,
        subject: str,
        start_date_time: str,
        end_date_time: str,
        is_all_day_event: bool,
        description: str,
        location: str,
        associations: typing.Optional[CommonEventAssociation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmCreateOrUpdateEventResponse:
        """
        Create a new event

        Parameters
        ----------
        additional : typing.Any

        type : str
            The type of the event in the CRM.

        subject : str
            The Subject of the event/meeting in the CRM.

        start_date_time : str
            Event start date time.

        end_date_time : str
            Event end date time.

        is_all_day_event : bool
            Is `true` if the event is an all day event.

        description : str
            Description of the event/meeting.

        location : str
            The location of the event/meeting.

        associations : typing.Optional[CommonEventAssociation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmCreateOrUpdateEventResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_event.crm_event_create_event(
            additional={"key": "value"},
            type="type",
            subject="subject",
            start_date_time="startDateTime",
            end_date_time="endDateTime",
            is_all_day_event=True,
            description="description",
            location="location",
        )
        """
        _response = self._raw_client.crm_event_create_event(
            additional=additional,
            type=type,
            subject=subject,
            start_date_time=start_date_time,
            end_date_time=end_date_time,
            is_all_day_event=is_all_day_event,
            description=description,
            location=location,
            associations=associations,
            request_options=request_options,
        )
        return _response.data

    def crm_event_search_events(
        self,
        *,
        search_criteria: typing.Any,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmSearchEventsResponse:
        """
        Search for events

        Parameters
        ----------
        search_criteria : typing.Any

        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmSearchEventsResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crm_event.crm_event_search_events(
            search_criteria={"key": "value"},
        )
        """
        _response = self._raw_client.crm_event_search_events(
            search_criteria=search_criteria,
            fields=fields,
            page_size=page_size,
            cursor=cursor,
            request_options=request_options,
        )
        return _response.data


class AsyncCrmEventClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCrmEventClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCrmEventClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCrmEventClient
        """
        return self._raw_client

    async def crm_event_get_event(
        self,
        id: str,
        *,
        fields: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmGetEventResponse:
        """
        Get details of a event

        Parameters
        ----------
        id : str

        fields : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmGetEventResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_event.crm_event_get_event(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_event_get_event(
            id, fields=fields, associations=associations, request_options=request_options
        )
        return _response.data

    async def crm_event_delete_event(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CrmDeleteEventResponse:
        """
        Delete details of an event in a CRM

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmDeleteEventResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_event.crm_event_delete_event(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_event_delete_event(id, request_options=request_options)
        return _response.data

    async def crm_event_update_event(
        self,
        id: str,
        *,
        additional: typing.Any,
        type: str,
        subject: str,
        start_date_time: str,
        end_date_time: str,
        is_all_day_event: bool,
        description: str,
        location: str,
        associations: typing.Optional[CommonEventAssociation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmCreateOrUpdateEventResponse:
        """
        Update a event

        Parameters
        ----------
        id : str

        additional : typing.Any

        type : str
            The type of the event in the CRM.

        subject : str
            The Subject of the event/meeting in the CRM.

        start_date_time : str
            Event start date time.

        end_date_time : str
            Event end date time.

        is_all_day_event : bool
            Is `true` if the event is an all day event.

        description : str
            Description of the event/meeting.

        location : str
            The location of the event/meeting.

        associations : typing.Optional[CommonEventAssociation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmCreateOrUpdateEventResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_event.crm_event_update_event(
                id="id",
                additional={"key": "value"},
                type="type",
                subject="subject",
                start_date_time="startDateTime",
                end_date_time="endDateTime",
                is_all_day_event=True,
                description="description",
                location="location",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_event_update_event(
            id,
            additional=additional,
            type=type,
            subject=subject,
            start_date_time=start_date_time,
            end_date_time=end_date_time,
            is_all_day_event=is_all_day_event,
            description=description,
            location=location,
            associations=associations,
            request_options=request_options,
        )
        return _response.data

    async def crm_event_get_events(
        self,
        *,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        associations: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmGetEventsResponse:
        """
        Get all the events

        Parameters
        ----------
        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        associations : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmGetEventsResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_event.crm_event_get_events()


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_event_get_events(
            fields=fields,
            page_size=page_size,
            cursor=cursor,
            associations=associations,
            request_options=request_options,
        )
        return _response.data

    async def crm_event_create_event(
        self,
        *,
        additional: typing.Any,
        type: str,
        subject: str,
        start_date_time: str,
        end_date_time: str,
        is_all_day_event: bool,
        description: str,
        location: str,
        associations: typing.Optional[CommonEventAssociation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmCreateOrUpdateEventResponse:
        """
        Create a new event

        Parameters
        ----------
        additional : typing.Any

        type : str
            The type of the event in the CRM.

        subject : str
            The Subject of the event/meeting in the CRM.

        start_date_time : str
            Event start date time.

        end_date_time : str
            Event end date time.

        is_all_day_event : bool
            Is `true` if the event is an all day event.

        description : str
            Description of the event/meeting.

        location : str
            The location of the event/meeting.

        associations : typing.Optional[CommonEventAssociation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmCreateOrUpdateEventResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_event.crm_event_create_event(
                additional={"key": "value"},
                type="type",
                subject="subject",
                start_date_time="startDateTime",
                end_date_time="endDateTime",
                is_all_day_event=True,
                description="description",
                location="location",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_event_create_event(
            additional=additional,
            type=type,
            subject=subject,
            start_date_time=start_date_time,
            end_date_time=end_date_time,
            is_all_day_event=is_all_day_event,
            description=description,
            location=location,
            associations=associations,
            request_options=request_options,
        )
        return _response.data

    async def crm_event_search_events(
        self,
        *,
        search_criteria: typing.Any,
        fields: typing.Optional[str] = None,
        page_size: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmSearchEventsResponse:
        """
        Search for events

        Parameters
        ----------
        search_criteria : typing.Any

        fields : typing.Optional[str]

        page_size : typing.Optional[str]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmSearchEventsResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crm_event.crm_event_search_events(
                search_criteria={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.crm_event_search_events(
            search_criteria=search_criteria,
            fields=fields,
            page_size=page_size,
            cursor=cursor,
            request_options=request_options,
        )
        return _response.data
