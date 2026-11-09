

import contextlib
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.route_log import RouteLog
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
from pydantic import ValidationError


class RawEventClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    @contextlib.contextmanager
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
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
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
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            The response body from a GET events request.
        """
        with self._client_wrapper.httpx_client.stream(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/events",
            method="GET",
            params={
                "pageSize": page_size,
                "pageNum": page_num,
                "deviceUID": device_uid,
                "sensorUID": sensor_uid,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "startDate": start_date,
                "endDate": end_date,
                "dateType": date_type,
                "systemFilesOnly": system_files_only,
                "files": files,
                "format": format,
                "serialNumber": serial_number,
                "fleetUID": fleet_uid,
                "sessionUID": session_uid,
                "eventUID": event_uid,
                "selectFields": select_fields,
                "deviceUIDs": device_ui_ds,
                "since": since,
            },
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

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
    ) -> HttpResponse[GetEventsByCursorResponse]:
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
        HttpResponse[GetEventsByCursorResponse]
            The response body from a GET events by cursor request.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/events-cursor",
            method="GET",
            params={
                "limit": limit,
                "cursor": cursor,
                "sortOrder": sort_order,
                "systemFilesOnly": system_files_only,
                "files": files,
                "fleetUID": fleet_uid,
                "deviceUID": device_uid,
                "sensorUID": sensor_uid,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetEventsByCursorResponse,
                    parse_obj_as(
                        type_=GetEventsByCursorResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_route_logs_by_event(
        self, project_or_product_uid: str, event_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[RouteLog]]:
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
        HttpResponse[typing.List[RouteLog]]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/events/{encode_path_param(event_uid)}/route-logs",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RouteLog],
                    parse_obj_as(
                        type_=typing.List[RouteLog],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    @contextlib.contextmanager
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
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
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
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            The response body from a GET events request.
        """
        with self._client_wrapper.httpx_client.stream(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/fleets/{encode_path_param(fleet_uid)}/events",
            method="GET",
            params={
                "pageSize": page_size,
                "pageNum": page_num,
                "deviceUID": device_uid,
                "sensorUID": sensor_uid,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "startDate": start_date,
                "endDate": end_date,
                "dateType": date_type,
                "systemFilesOnly": system_files_only,
                "files": files,
                "format": format,
                "serialNumber": serial_number,
                "sessionUID": session_uid,
                "eventUID": event_uid,
                "selectFields": select_fields,
                "deviceUIDs": device_ui_ds,
                "since": since,
            },
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

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
    ) -> HttpResponse[GetFleetEventsByCursorResponse]:
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
        HttpResponse[GetFleetEventsByCursorResponse]
            The response body from a GET events by cursor request.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/fleets/{encode_path_param(fleet_uid)}/events-cursor",
            method="GET",
            params={
                "limit": limit,
                "cursor": cursor,
                "sortOrder": sort_order,
                "systemFilesOnly": system_files_only,
                "files": files,
                "deviceUID": device_uid,
                "sensorUID": sensor_uid,
                "startDate": start_date,
                "endDate": end_date,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetFleetEventsByCursorResponse,
                    parse_obj_as(
                        type_=GetFleetEventsByCursorResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawEventClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    @contextlib.asynccontextmanager
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
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
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
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            The response body from a GET events request.
        """
        async with self._client_wrapper.httpx_client.stream(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/events",
            method="GET",
            params={
                "pageSize": page_size,
                "pageNum": page_num,
                "deviceUID": device_uid,
                "sensorUID": sensor_uid,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "startDate": start_date,
                "endDate": end_date,
                "dateType": date_type,
                "systemFilesOnly": system_files_only,
                "files": files,
                "format": format,
                "serialNumber": serial_number,
                "fleetUID": fleet_uid,
                "sessionUID": session_uid,
                "eventUID": event_uid,
                "selectFields": select_fields,
                "deviceUIDs": device_ui_ds,
                "since": since,
            },
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

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
    ) -> AsyncHttpResponse[GetEventsByCursorResponse]:
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
        AsyncHttpResponse[GetEventsByCursorResponse]
            The response body from a GET events by cursor request.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/events-cursor",
            method="GET",
            params={
                "limit": limit,
                "cursor": cursor,
                "sortOrder": sort_order,
                "systemFilesOnly": system_files_only,
                "files": files,
                "fleetUID": fleet_uid,
                "deviceUID": device_uid,
                "sensorUID": sensor_uid,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetEventsByCursorResponse,
                    parse_obj_as(
                        type_=GetEventsByCursorResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_route_logs_by_event(
        self, project_or_product_uid: str, event_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[RouteLog]]:
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
        AsyncHttpResponse[typing.List[RouteLog]]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/events/{encode_path_param(event_uid)}/route-logs",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RouteLog],
                    parse_obj_as(
                        type_=typing.List[RouteLog],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    @contextlib.asynccontextmanager
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
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
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
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            The response body from a GET events request.
        """
        async with self._client_wrapper.httpx_client.stream(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/fleets/{encode_path_param(fleet_uid)}/events",
            method="GET",
            params={
                "pageSize": page_size,
                "pageNum": page_num,
                "deviceUID": device_uid,
                "sensorUID": sensor_uid,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "startDate": start_date,
                "endDate": end_date,
                "dateType": date_type,
                "systemFilesOnly": system_files_only,
                "files": files,
                "format": format,
                "serialNumber": serial_number,
                "sessionUID": session_uid,
                "eventUID": event_uid,
                "selectFields": select_fields,
                "deviceUIDs": device_ui_ds,
                "since": since,
            },
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

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
    ) -> AsyncHttpResponse[GetFleetEventsByCursorResponse]:
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
        AsyncHttpResponse[GetFleetEventsByCursorResponse]
            The response body from a GET events by cursor request.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/fleets/{encode_path_param(fleet_uid)}/events-cursor",
            method="GET",
            params={
                "limit": limit,
                "cursor": cursor,
                "sortOrder": sort_order,
                "systemFilesOnly": system_files_only,
                "files": files,
                "deviceUID": device_uid,
                "sensorUID": sensor_uid,
                "startDate": start_date,
                "endDate": end_date,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetFleetEventsByCursorResponse,
                    parse_obj_as(
                        type_=GetFleetEventsByCursorResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
