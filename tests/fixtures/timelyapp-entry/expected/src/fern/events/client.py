

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.v1hour import V1Hour
from .raw_client import AsyncRawEventsClient, RawEventsClient
from .types.list_time_entries_request_order import ListTimeEntriesRequestOrder
from .types.list_time_entries_request_sort import ListTimeEntriesRequestSort
from .types.v1hours_create_event import V1HoursCreateEvent
from .types.v1hours_update_event import V1HoursUpdateEvent


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

    def list_time_entries(
        self,
        account_id: int,
        *,
        since: typing.Optional[dt.date] = None,
        upto: typing.Optional[dt.date] = None,
        day: typing.Optional[dt.date] = None,
        hour_ids: typing.Optional[str] = None,
        sort: typing.Optional[ListTimeEntriesRequestSort] = None,
        order: typing.Optional[ListTimeEntriesRequestOrder] = None,
        per_page: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        project_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[V1Hour]:
        """
        List all time entries in the Timely account. Time entries will be returned in a paginated format with optional filtering.

        Parameters
        ----------
        account_id : int
            Account ID for the time entries you want to retrieve

        since : typing.Optional[dt.date]
            Filter time entries from this date (inclusive). Both since and upto needs to be present

        upto : typing.Optional[dt.date]
            Filter time entries up to this date (inclusive). Both since and upto needs to be present

        day : typing.Optional[dt.date]
            Filter time entries for a specific date. Defaults to current date if omitted. Disregarded if since and upto is present

        hour_ids : typing.Optional[str]
            Comma-separated list of time entry IDs to filter by

        sort : typing.Optional[ListTimeEntriesRequestSort]
            Field to sort by

        order : typing.Optional[ListTimeEntriesRequestOrder]
            Sort order

        per_page : typing.Optional[int]
            Number of results per page (max 5000)

        page : typing.Optional[int]
            Page number for pagination

        project_id : typing.Optional[int]
            Filter by project ID

        user_id : typing.Optional[int]
            Filter by user ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1Hour]
            Time entries list

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.events.list_time_entries(
            account_id=1,
        )
        """
        _response = self._raw_client.list_time_entries(
            account_id,
            since=since,
            upto=upto,
            day=day,
            hour_ids=hour_ids,
            sort=sort,
            order=order,
            per_page=per_page,
            page=page,
            project_id=project_id,
            user_id=user_id,
            request_options=request_options,
        )
        return _response.data

    def create_hour(
        self, account_id: int, *, event: V1HoursCreateEvent, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Hour:
        """
        Create a new time entry in the Timely account. The time entry will be created with the provided details.

        Parameters
        ----------
        account_id : int
            Account ID where the time entry will be created

        event : V1HoursCreateEvent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Hour
            Time entry created

        Examples
        --------
        from fern.events import V1HoursCreateEvent

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.events.create_hour(
            account_id=1,
            event=V1HoursCreateEvent(
                project_id=1,
                hours=2,
                minutes=30,
                day="2024-01-01",
                note="Working on API documentation",
                billable=True,
            ),
        )
        """
        _response = self._raw_client.create_hour(account_id, event=event, request_options=request_options)
        return _response.data

    def show_hour(self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> V1Hour:
        """
        Retrieve details for a specific time entry.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Time entry ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Hour
            Time entry details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.events.show_hour(
            account_id=1,
            id=1,
        )
        """
        _response = self._raw_client.show_hour(account_id, id, request_options=request_options)
        return _response.data

    def update_hour(
        self,
        account_id: int,
        id: int,
        *,
        event: V1HoursUpdateEvent,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Hour:
        """
        Update an existing time entry. Only the provided fields will be updated.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Time entry ID

        event : V1HoursUpdateEvent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Hour
            Time entry updated

        Examples
        --------
        from fern.events import V1HoursUpdateEvent

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.events.update_hour(
            account_id=1,
            id=1,
            event=V1HoursUpdateEvent(
                hours=3,
                note="Updated note",
            ),
        )
        """
        _response = self._raw_client.update_hour(account_id, id, event=event, request_options=request_options)
        return _response.data

    def delete_hour(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete a time entry. Locked or invoiced time entries cannot be deleted.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Time entry ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Time entry deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.events.delete_hour(
            account_id=1,
            id=1,
        )
        """
        _response = self._raw_client.delete_hour(account_id, id, request_options=request_options)
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

    async def list_time_entries(
        self,
        account_id: int,
        *,
        since: typing.Optional[dt.date] = None,
        upto: typing.Optional[dt.date] = None,
        day: typing.Optional[dt.date] = None,
        hour_ids: typing.Optional[str] = None,
        sort: typing.Optional[ListTimeEntriesRequestSort] = None,
        order: typing.Optional[ListTimeEntriesRequestOrder] = None,
        per_page: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        project_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[V1Hour]:
        """
        List all time entries in the Timely account. Time entries will be returned in a paginated format with optional filtering.

        Parameters
        ----------
        account_id : int
            Account ID for the time entries you want to retrieve

        since : typing.Optional[dt.date]
            Filter time entries from this date (inclusive). Both since and upto needs to be present

        upto : typing.Optional[dt.date]
            Filter time entries up to this date (inclusive). Both since and upto needs to be present

        day : typing.Optional[dt.date]
            Filter time entries for a specific date. Defaults to current date if omitted. Disregarded if since and upto is present

        hour_ids : typing.Optional[str]
            Comma-separated list of time entry IDs to filter by

        sort : typing.Optional[ListTimeEntriesRequestSort]
            Field to sort by

        order : typing.Optional[ListTimeEntriesRequestOrder]
            Sort order

        per_page : typing.Optional[int]
            Number of results per page (max 5000)

        page : typing.Optional[int]
            Page number for pagination

        project_id : typing.Optional[int]
            Filter by project ID

        user_id : typing.Optional[int]
            Filter by user ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1Hour]
            Time entries list

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.events.list_time_entries(
                account_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_time_entries(
            account_id,
            since=since,
            upto=upto,
            day=day,
            hour_ids=hour_ids,
            sort=sort,
            order=order,
            per_page=per_page,
            page=page,
            project_id=project_id,
            user_id=user_id,
            request_options=request_options,
        )
        return _response.data

    async def create_hour(
        self, account_id: int, *, event: V1HoursCreateEvent, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Hour:
        """
        Create a new time entry in the Timely account. The time entry will be created with the provided details.

        Parameters
        ----------
        account_id : int
            Account ID where the time entry will be created

        event : V1HoursCreateEvent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Hour
            Time entry created

        Examples
        --------
        import asyncio

        from fern.events import V1HoursCreateEvent

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.events.create_hour(
                account_id=1,
                event=V1HoursCreateEvent(
                    project_id=1,
                    hours=2,
                    minutes=30,
                    day="2024-01-01",
                    note="Working on API documentation",
                    billable=True,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_hour(account_id, event=event, request_options=request_options)
        return _response.data

    async def show_hour(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1Hour:
        """
        Retrieve details for a specific time entry.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Time entry ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Hour
            Time entry details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.events.show_hour(
                account_id=1,
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.show_hour(account_id, id, request_options=request_options)
        return _response.data

    async def update_hour(
        self,
        account_id: int,
        id: int,
        *,
        event: V1HoursUpdateEvent,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Hour:
        """
        Update an existing time entry. Only the provided fields will be updated.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Time entry ID

        event : V1HoursUpdateEvent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Hour
            Time entry updated

        Examples
        --------
        import asyncio

        from fern.events import V1HoursUpdateEvent

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.events.update_hour(
                account_id=1,
                id=1,
                event=V1HoursUpdateEvent(
                    hours=3,
                    note="Updated note",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_hour(account_id, id, event=event, request_options=request_options)
        return _response.data

    async def delete_hour(
        self, account_id: int, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete a time entry. Locked or invoiced time entries cannot be deleted.

        Parameters
        ----------
        account_id : int
            Account ID

        id : int
            Time entry ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Time entry deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.events.delete_hour(
                account_id=1,
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_hour(account_id, id, request_options=request_options)
        return _response.data
