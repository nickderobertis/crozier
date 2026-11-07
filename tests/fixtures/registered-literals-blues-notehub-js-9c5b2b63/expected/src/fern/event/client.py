

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.route_log import RouteLog
from .raw_client import AsyncRawEventClient, RawEventClient
from .types.get_events_by_cursor_request_sort_order import GetEventsByCursorRequestSortOrder
from .types.get_events_by_cursor_response import GetEventsByCursorResponse
from .types.get_events_request_date_type import GetEventsRequestDateType
from .types.get_events_request_format import GetEventsRequestFormat
from .types.get_events_request_sort_by import GetEventsRequestSortBy
from .types.get_events_request_sort_order import GetEventsRequestSortOrder
from .types.get_fleet_events_by_cursor_request_sort_order import GetFleetEventsByCursorRequestSortOrder
from .types.get_fleet_events_by_cursor_response import GetFleetEventsByCursorResponse
from .types.get_fleet_events_request_date_type import GetFleetEventsRequestDateType
from .types.get_fleet_events_request_format import GetFleetEventsRequestFormat
from .types.get_fleet_events_request_sort_by import GetFleetEventsRequestSortBy
from .types.get_fleet_events_request_sort_order import GetFleetEventsRequestSortOrder


class EventClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEventClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEventClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEventClient
        """
        return self._raw_client

    def get_events(
        self,
        project_or_product_uid: str,
        *,
        page_size: typing.Optional[int] = None,
        page_num: typing.Optional[int] = None,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sensor_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort_by: typing.Optional[GetEventsRequestSortBy] = None,
        sort_order: typing.Optional[GetEventsRequestSortOrder] = None,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        date_type: typing.Optional[GetEventsRequestDateType] = None,
        system_files_only: typing.Optional[bool] = None,
        files: typing.Optional[str] = None,
        format: typing.Optional[GetEventsRequestFormat] = None,
        serial_number: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fleet_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        session_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        event_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        select_fields: typing.Optional[str] = None,
        device_ui_ds: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Get Events of a Project

        Parameters
        ----------
        project_or_product_uid : str

        page_size : typing.Optional[int]

        page_num : typing.Optional[int]

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        sensor_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A sensor UID to filter events by, matched exactly against the event sensor field. The value may carry any prefix.

        sort_by : typing.Optional[GetEventsRequestSortBy]

        sort_order : typing.Optional[GetEventsRequestSortOrder]

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        date_type : typing.Optional[GetEventsRequestDateType]
            Which date to filter on, either 'captured' or 'uploaded'.  This will apply to the startDate and endDate parameters

        system_files_only : typing.Optional[bool]

        files : typing.Optional[str]

        format : typing.Optional[GetEventsRequestFormat]
            Response format (JSON or CSV)

        serial_number : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter by Serial Number

        fleet_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter by Fleet UID

        session_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter by Session UID

        event_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter by Event UID

        select_fields : typing.Optional[str]
            Comma-separated list of fields to select from JSON payload (e.g., "field1,field2.subfield,field3"), this will reflect the columns in the CSV output.

        device_ui_ds : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Deprecated.

        since : typing.Optional[str]
            Deprecated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            The response body from a GET events request.
        """
        with self._raw_client.get_events(
            project_or_product_uid,
            page_size=page_size,
            page_num=page_num,
            device_uid=device_uid,
            sensor_uid=sensor_uid,
            sort_by=sort_by,
            sort_order=sort_order,
            start_date=start_date,
            end_date=end_date,
            date_type=date_type,
            system_files_only=system_files_only,
            files=files,
            format=format,
            serial_number=serial_number,
            fleet_uid=fleet_uid,
            session_uid=session_uid,
            event_uid=event_uid,
            select_fields=select_fields,
            device_ui_ds=device_ui_ds,
            since=since,
            request_options=request_options,
        ) as r:
            yield from r.data

    def get_events_by_cursor(
        self,
        project_or_product_uid: str,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        sort_order: typing.Optional[GetEventsByCursorRequestSortOrder] = None,
        system_files_only: typing.Optional[bool] = None,
        files: typing.Optional[str] = None,
        fleet_uid: typing.Optional[str] = None,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sensor_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetEventsByCursorResponse:
        """
        Get Events of a Project by cursor

        Parameters
        ----------
        project_or_product_uid : str

        limit : typing.Optional[int]

        cursor : typing.Optional[str]
            A cursor, which can be obtained from the `next_cursor` value from a previous call to this endpoint. The results set returned will include this event as its first result if the given identifier is actually the UID of an event. If this event UID is not found, the parameter is ignored and the results set is the same as if the parameter was not included.

        sort_order : typing.Optional[GetEventsByCursorRequestSortOrder]

        system_files_only : typing.Optional[bool]

        files : typing.Optional[str]

        fleet_uid : typing.Optional[str]

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        sensor_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A sensor UID to filter events by, matched exactly against the event sensor field. The value may carry any prefix.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetEventsByCursorResponse
            The response body from a GET events by cursor request.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.event.get_events_by_cursor(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            files="_health.qo, data.qo",
        )
        """
        _response = self._raw_client.get_events_by_cursor(
            project_or_product_uid,
            limit=limit,
            cursor=cursor,
            sort_order=sort_order,
            system_files_only=system_files_only,
            files=files,
            fleet_uid=fleet_uid,
            device_uid=device_uid,
            sensor_uid=sensor_uid,
            request_options=request_options,
        )
        return _response.data

    def get_route_logs_by_event(
        self, project_or_product_uid: str, event_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RouteLog]:
        """
        Get Route Logs by Event UID

        Parameters
        ----------
        project_or_product_uid : str

        event_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RouteLog]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.event.get_route_logs_by_event(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            event_uid="4506f411-dea6-44a0-9743-1130f57d7747",
        )
        """
        _response = self._raw_client.get_route_logs_by_event(
            project_or_product_uid, event_uid, request_options=request_options
        )
        return _response.data

    def get_fleet_events(
        self,
        project_or_product_uid: str,
        fleet_uid: str,
        *,
        page_size: typing.Optional[int] = None,
        page_num: typing.Optional[int] = None,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sensor_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort_by: typing.Optional[GetFleetEventsRequestSortBy] = None,
        sort_order: typing.Optional[GetFleetEventsRequestSortOrder] = None,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        date_type: typing.Optional[GetFleetEventsRequestDateType] = None,
        system_files_only: typing.Optional[bool] = None,
        files: typing.Optional[str] = None,
        format: typing.Optional[GetFleetEventsRequestFormat] = None,
        serial_number: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        session_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        event_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        select_fields: typing.Optional[str] = None,
        device_ui_ds: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Get Events of a Fleet

        Parameters
        ----------
        project_or_product_uid : str

        fleet_uid : str

        page_size : typing.Optional[int]

        page_num : typing.Optional[int]

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        sensor_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A sensor UID to filter events by, matched exactly against the event sensor field. The value may carry any prefix.

        sort_by : typing.Optional[GetFleetEventsRequestSortBy]

        sort_order : typing.Optional[GetFleetEventsRequestSortOrder]

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        date_type : typing.Optional[GetFleetEventsRequestDateType]
            Which date to filter on, either 'captured' or 'uploaded'.  This will apply to the startDate and endDate parameters

        system_files_only : typing.Optional[bool]

        files : typing.Optional[str]

        format : typing.Optional[GetFleetEventsRequestFormat]
            Response format (JSON or CSV)

        serial_number : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter by Serial Number

        session_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter by Session UID

        event_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter by Event UID

        select_fields : typing.Optional[str]
            Comma-separated list of fields to select from JSON payload (e.g., "field1,field2.subfield,field3"), this will reflect the columns in the CSV output.

        device_ui_ds : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Deprecated.

        since : typing.Optional[str]
            Deprecated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            The response body from a GET events request.
        """
        with self._raw_client.get_fleet_events(
            project_or_product_uid,
            fleet_uid,
            page_size=page_size,
            page_num=page_num,
            device_uid=device_uid,
            sensor_uid=sensor_uid,
            sort_by=sort_by,
            sort_order=sort_order,
            start_date=start_date,
            end_date=end_date,
            date_type=date_type,
            system_files_only=system_files_only,
            files=files,
            format=format,
            serial_number=serial_number,
            session_uid=session_uid,
            event_uid=event_uid,
            select_fields=select_fields,
            device_ui_ds=device_ui_ds,
            since=since,
            request_options=request_options,
        ) as r:
            yield from r.data

    def get_fleet_events_by_cursor(
        self,
        project_or_product_uid: str,
        fleet_uid: str,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        sort_order: typing.Optional[GetFleetEventsByCursorRequestSortOrder] = None,
        system_files_only: typing.Optional[bool] = None,
        files: typing.Optional[str] = None,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sensor_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetFleetEventsByCursorResponse:
        """
        Get Events of a Fleet by cursor

        Parameters
        ----------
        project_or_product_uid : str

        fleet_uid : str

        limit : typing.Optional[int]

        cursor : typing.Optional[str]
            A cursor, which can be obtained from the `next_cursor` value from a previous call to this endpoint. The results set returned will include this event as its first result if the given identifier is actually the UID of an event. If this event UID is not found, the parameter is ignored and the results set is the same as if the parameter was not included.

        sort_order : typing.Optional[GetFleetEventsByCursorRequestSortOrder]

        system_files_only : typing.Optional[bool]

        files : typing.Optional[str]

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        sensor_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A sensor UID to filter events by, matched exactly against the event sensor field. The value may carry any prefix.

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFleetEventsByCursorResponse
            The response body from a GET events by cursor request.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.event.get_fleet_events_by_cursor(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            fleet_uid="fleetUID",
            files="_health.qo, data.qo",
        )
        """
        _response = self._raw_client.get_fleet_events_by_cursor(
            project_or_product_uid,
            fleet_uid,
            limit=limit,
            cursor=cursor,
            sort_order=sort_order,
            system_files_only=system_files_only,
            files=files,
            device_uid=device_uid,
            sensor_uid=sensor_uid,
            start_date=start_date,
            end_date=end_date,
            request_options=request_options,
        )
        return _response.data


class AsyncEventClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEventClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEventClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEventClient
        """
        return self._raw_client

    async def get_events(
        self,
        project_or_product_uid: str,
        *,
        page_size: typing.Optional[int] = None,
        page_num: typing.Optional[int] = None,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sensor_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort_by: typing.Optional[GetEventsRequestSortBy] = None,
        sort_order: typing.Optional[GetEventsRequestSortOrder] = None,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        date_type: typing.Optional[GetEventsRequestDateType] = None,
        system_files_only: typing.Optional[bool] = None,
        files: typing.Optional[str] = None,
        format: typing.Optional[GetEventsRequestFormat] = None,
        serial_number: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fleet_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        session_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        event_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        select_fields: typing.Optional[str] = None,
        device_ui_ds: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Get Events of a Project

        Parameters
        ----------
        project_or_product_uid : str

        page_size : typing.Optional[int]

        page_num : typing.Optional[int]

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        sensor_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A sensor UID to filter events by, matched exactly against the event sensor field. The value may carry any prefix.

        sort_by : typing.Optional[GetEventsRequestSortBy]

        sort_order : typing.Optional[GetEventsRequestSortOrder]

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        date_type : typing.Optional[GetEventsRequestDateType]
            Which date to filter on, either 'captured' or 'uploaded'.  This will apply to the startDate and endDate parameters

        system_files_only : typing.Optional[bool]

        files : typing.Optional[str]

        format : typing.Optional[GetEventsRequestFormat]
            Response format (JSON or CSV)

        serial_number : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter by Serial Number

        fleet_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter by Fleet UID

        session_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter by Session UID

        event_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter by Event UID

        select_fields : typing.Optional[str]
            Comma-separated list of fields to select from JSON payload (e.g., "field1,field2.subfield,field3"), this will reflect the columns in the CSV output.

        device_ui_ds : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Deprecated.

        since : typing.Optional[str]
            Deprecated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            The response body from a GET events request.
        """
        async with self._raw_client.get_events(
            project_or_product_uid,
            page_size=page_size,
            page_num=page_num,
            device_uid=device_uid,
            sensor_uid=sensor_uid,
            sort_by=sort_by,
            sort_order=sort_order,
            start_date=start_date,
            end_date=end_date,
            date_type=date_type,
            system_files_only=system_files_only,
            files=files,
            format=format,
            serial_number=serial_number,
            fleet_uid=fleet_uid,
            session_uid=session_uid,
            event_uid=event_uid,
            select_fields=select_fields,
            device_ui_ds=device_ui_ds,
            since=since,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_events_by_cursor(
        self,
        project_or_product_uid: str,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        sort_order: typing.Optional[GetEventsByCursorRequestSortOrder] = None,
        system_files_only: typing.Optional[bool] = None,
        files: typing.Optional[str] = None,
        fleet_uid: typing.Optional[str] = None,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sensor_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetEventsByCursorResponse:
        """
        Get Events of a Project by cursor

        Parameters
        ----------
        project_or_product_uid : str

        limit : typing.Optional[int]

        cursor : typing.Optional[str]
            A cursor, which can be obtained from the `next_cursor` value from a previous call to this endpoint. The results set returned will include this event as its first result if the given identifier is actually the UID of an event. If this event UID is not found, the parameter is ignored and the results set is the same as if the parameter was not included.

        sort_order : typing.Optional[GetEventsByCursorRequestSortOrder]

        system_files_only : typing.Optional[bool]

        files : typing.Optional[str]

        fleet_uid : typing.Optional[str]

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        sensor_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A sensor UID to filter events by, matched exactly against the event sensor field. The value may carry any prefix.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetEventsByCursorResponse
            The response body from a GET events by cursor request.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.event.get_events_by_cursor(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                files="_health.qo, data.qo",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_events_by_cursor(
            project_or_product_uid,
            limit=limit,
            cursor=cursor,
            sort_order=sort_order,
            system_files_only=system_files_only,
            files=files,
            fleet_uid=fleet_uid,
            device_uid=device_uid,
            sensor_uid=sensor_uid,
            request_options=request_options,
        )
        return _response.data

    async def get_route_logs_by_event(
        self, project_or_product_uid: str, event_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RouteLog]:
        """
        Get Route Logs by Event UID

        Parameters
        ----------
        project_or_product_uid : str

        event_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RouteLog]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.event.get_route_logs_by_event(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                event_uid="4506f411-dea6-44a0-9743-1130f57d7747",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_route_logs_by_event(
            project_or_product_uid, event_uid, request_options=request_options
        )
        return _response.data

    async def get_fleet_events(
        self,
        project_or_product_uid: str,
        fleet_uid: str,
        *,
        page_size: typing.Optional[int] = None,
        page_num: typing.Optional[int] = None,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sensor_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort_by: typing.Optional[GetFleetEventsRequestSortBy] = None,
        sort_order: typing.Optional[GetFleetEventsRequestSortOrder] = None,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        date_type: typing.Optional[GetFleetEventsRequestDateType] = None,
        system_files_only: typing.Optional[bool] = None,
        files: typing.Optional[str] = None,
        format: typing.Optional[GetFleetEventsRequestFormat] = None,
        serial_number: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        session_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        event_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        select_fields: typing.Optional[str] = None,
        device_ui_ds: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Get Events of a Fleet

        Parameters
        ----------
        project_or_product_uid : str

        fleet_uid : str

        page_size : typing.Optional[int]

        page_num : typing.Optional[int]

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        sensor_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A sensor UID to filter events by, matched exactly against the event sensor field. The value may carry any prefix.

        sort_by : typing.Optional[GetFleetEventsRequestSortBy]

        sort_order : typing.Optional[GetFleetEventsRequestSortOrder]

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        date_type : typing.Optional[GetFleetEventsRequestDateType]
            Which date to filter on, either 'captured' or 'uploaded'.  This will apply to the startDate and endDate parameters

        system_files_only : typing.Optional[bool]

        files : typing.Optional[str]

        format : typing.Optional[GetFleetEventsRequestFormat]
            Response format (JSON or CSV)

        serial_number : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter by Serial Number

        session_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter by Session UID

        event_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter by Event UID

        select_fields : typing.Optional[str]
            Comma-separated list of fields to select from JSON payload (e.g., "field1,field2.subfield,field3"), this will reflect the columns in the CSV output.

        device_ui_ds : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Deprecated.

        since : typing.Optional[str]
            Deprecated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            The response body from a GET events request.
        """
        async with self._raw_client.get_fleet_events(
            project_or_product_uid,
            fleet_uid,
            page_size=page_size,
            page_num=page_num,
            device_uid=device_uid,
            sensor_uid=sensor_uid,
            sort_by=sort_by,
            sort_order=sort_order,
            start_date=start_date,
            end_date=end_date,
            date_type=date_type,
            system_files_only=system_files_only,
            files=files,
            format=format,
            serial_number=serial_number,
            session_uid=session_uid,
            event_uid=event_uid,
            select_fields=select_fields,
            device_ui_ds=device_ui_ds,
            since=since,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_fleet_events_by_cursor(
        self,
        project_or_product_uid: str,
        fleet_uid: str,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        sort_order: typing.Optional[GetFleetEventsByCursorRequestSortOrder] = None,
        system_files_only: typing.Optional[bool] = None,
        files: typing.Optional[str] = None,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sensor_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetFleetEventsByCursorResponse:
        """
        Get Events of a Fleet by cursor

        Parameters
        ----------
        project_or_product_uid : str

        fleet_uid : str

        limit : typing.Optional[int]

        cursor : typing.Optional[str]
            A cursor, which can be obtained from the `next_cursor` value from a previous call to this endpoint. The results set returned will include this event as its first result if the given identifier is actually the UID of an event. If this event UID is not found, the parameter is ignored and the results set is the same as if the parameter was not included.

        sort_order : typing.Optional[GetFleetEventsByCursorRequestSortOrder]

        system_files_only : typing.Optional[bool]

        files : typing.Optional[str]

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        sensor_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A sensor UID to filter events by, matched exactly against the event sensor field. The value may carry any prefix.

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFleetEventsByCursorResponse
            The response body from a GET events by cursor request.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.event.get_fleet_events_by_cursor(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                fleet_uid="fleetUID",
                files="_health.qo, data.qo",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_fleet_events_by_cursor(
            project_or_product_uid,
            fleet_uid,
            limit=limit,
            cursor=cursor,
            sort_order=sort_order,
            system_files_only=system_files_only,
            files=files,
            device_uid=device_uid,
            sensor_uid=sensor_uid,
            start_date=start_date,
            end_date=end_date,
            request_options=request_options,
        )
        return _response.data
