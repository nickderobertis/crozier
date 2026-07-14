

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.event_response import EventResponse
from ..types.event_types_list import EventTypesList
from ..types.events_list import EventsList
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

    def list_event_types(self, *, request_options: typing.Optional[RequestOptions] = None) -> EventTypesList:
        """
        Returns list of event types in the category hierarchy

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EventTypesList
            List of event types

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.events.list_event_types()
        """
        _response = self._raw_client.list_event_types(request_options=request_options)
        return _response.data

    def list_events(
        self,
        *,
        source_servicename: typing.Optional[str] = None,
        source_hostid: typing.Optional[str] = None,
        event_type: typing.Optional[str] = None,
        resource_type: typing.Optional[str] = None,
        resource_id: typing.Optional[str] = None,
        level: typing.Optional[str] = None,
        since: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EventsList:
        """
        Returns a paginated list of events in the descending order of their occurrence. Optional query parameters may be used for filtering results

        Parameters
        ----------
        source_servicename : typing.Optional[str]
            Filter events by the originating service

        source_hostid : typing.Optional[str]
            Filter events by the originating host ID

        event_type : typing.Optional[str]
            Filter events by a prefix match on the event type (e.g. "user.image.")

        resource_type : typing.Optional[str]
            Filter events by the type of resource - tag, imageDigest, repository etc

        resource_id : typing.Optional[str]
            Filter events by the id of the resource

        level : typing.Optional[str]
            Filter events by the level - INFO or ERROR

        since : typing.Optional[str]
            Return events that occurred after the timestamp

        before : typing.Optional[str]
            Return events that occurred before the timestamp

        page : typing.Optional[int]
            Pagination controls - return the nth page of results. Defaults to first page if left empty

        limit : typing.Optional[int]
            Number of events in the result set. Defaults to 100 if left empty

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EventsList
            Paginated list of event records and the next token

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.events.list_events()
        """
        _response = self._raw_client.list_events(
            source_servicename=source_servicename,
            source_hostid=source_hostid,
            event_type=event_type,
            resource_type=resource_type,
            resource_id=resource_id,
            level=level,
            since=since,
            before=before,
            page=page,
            limit=limit,
            anchore_account=anchore_account,
            request_options=request_options,
        )
        return _response.data

    def delete_events(
        self,
        *,
        before: typing.Optional[str] = None,
        since: typing.Optional[str] = None,
        level: typing.Optional[str] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Delete all or a subset of events filtered using the optional query parameters

        Parameters
        ----------
        before : typing.Optional[str]
            Delete events that occurred before the timestamp

        since : typing.Optional[str]
            Delete events that occurred after the timestamp

        level : typing.Optional[str]
            Delete events that match the level - INFO or ERROR

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            List of deleted event IDs

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.events.delete_events()
        """
        _response = self._raw_client.delete_events(
            before=before, since=since, level=level, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    def get_event(
        self,
        event_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EventResponse:
        """
        Lookup an event by its event ID

        Parameters
        ----------
        event_id : str
            Event ID of the event for lookup

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EventResponse
            Single event record

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.events.get_event(
            event_id="eventId",
        )
        """
        _response = self._raw_client.get_event(
            event_id, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    def delete_event(
        self,
        event_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete an event by its event ID

        Parameters
        ----------
        event_id : str
            Event ID of the event to be deleted

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.events.delete_event(
            event_id="eventId",
        )
        """
        _response = self._raw_client.delete_event(
            event_id, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data


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

    async def list_event_types(self, *, request_options: typing.Optional[RequestOptions] = None) -> EventTypesList:
        """
        Returns list of event types in the category hierarchy

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EventTypesList
            List of event types

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.events.list_event_types()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_event_types(request_options=request_options)
        return _response.data

    async def list_events(
        self,
        *,
        source_servicename: typing.Optional[str] = None,
        source_hostid: typing.Optional[str] = None,
        event_type: typing.Optional[str] = None,
        resource_type: typing.Optional[str] = None,
        resource_id: typing.Optional[str] = None,
        level: typing.Optional[str] = None,
        since: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EventsList:
        """
        Returns a paginated list of events in the descending order of their occurrence. Optional query parameters may be used for filtering results

        Parameters
        ----------
        source_servicename : typing.Optional[str]
            Filter events by the originating service

        source_hostid : typing.Optional[str]
            Filter events by the originating host ID

        event_type : typing.Optional[str]
            Filter events by a prefix match on the event type (e.g. "user.image.")

        resource_type : typing.Optional[str]
            Filter events by the type of resource - tag, imageDigest, repository etc

        resource_id : typing.Optional[str]
            Filter events by the id of the resource

        level : typing.Optional[str]
            Filter events by the level - INFO or ERROR

        since : typing.Optional[str]
            Return events that occurred after the timestamp

        before : typing.Optional[str]
            Return events that occurred before the timestamp

        page : typing.Optional[int]
            Pagination controls - return the nth page of results. Defaults to first page if left empty

        limit : typing.Optional[int]
            Number of events in the result set. Defaults to 100 if left empty

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EventsList
            Paginated list of event records and the next token

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.events.list_events()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_events(
            source_servicename=source_servicename,
            source_hostid=source_hostid,
            event_type=event_type,
            resource_type=resource_type,
            resource_id=resource_id,
            level=level,
            since=since,
            before=before,
            page=page,
            limit=limit,
            anchore_account=anchore_account,
            request_options=request_options,
        )
        return _response.data

    async def delete_events(
        self,
        *,
        before: typing.Optional[str] = None,
        since: typing.Optional[str] = None,
        level: typing.Optional[str] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Delete all or a subset of events filtered using the optional query parameters

        Parameters
        ----------
        before : typing.Optional[str]
            Delete events that occurred before the timestamp

        since : typing.Optional[str]
            Delete events that occurred after the timestamp

        level : typing.Optional[str]
            Delete events that match the level - INFO or ERROR

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            List of deleted event IDs

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.events.delete_events()


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_events(
            before=before, since=since, level=level, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    async def get_event(
        self,
        event_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EventResponse:
        """
        Lookup an event by its event ID

        Parameters
        ----------
        event_id : str
            Event ID of the event for lookup

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EventResponse
            Single event record

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.events.get_event(
                event_id="eventId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_event(
            event_id, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    async def delete_event(
        self,
        event_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete an event by its event ID

        Parameters
        ----------
        event_id : str
            Event ID of the event to be deleted

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.events.delete_event(
                event_id="eventId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_event(
            event_id, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data
