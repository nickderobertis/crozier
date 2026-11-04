

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.log_list_request_direction import LogListRequestDirection
from .types.log_list_response import LogListResponse
from .types.trace_list_request_direction import TraceListRequestDirection
from .types.trace_list_request_order_by import TraceListRequestOrderBy
from .types.trace_list_response import TraceListResponse
from pydantic import ValidationError


class RawTelemetryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def trace_list(
        self,
        *,
        direction: TraceListRequestDirection,
        limit: int,
        file_id: typing.Optional[str] = None,
        branch_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        start: typing.Optional[dt.datetime] = None,
        end: typing.Optional[dt.datetime] = None,
        order_by: typing.Optional[TraceListRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TraceListResponse]:
        """
        Get OpenTelemetry traces within a specified time window with flexible pagination options: Pass in only the end time to paginate backwards from there. Pass in a start time to paginate backwards from now until the start time. Pass in both to get resources within the time window. Choose to return in end_time order instead to view traces that completed in a window or since a time. Filter additionally by branch_ids or file_id.

        Parameters
        ----------
        direction : TraceListRequestDirection
            Sort direction for the traces. Defaults to descending order of timestamp.

        limit : int
            Maximum items to return in each paginated response

        file_id : typing.Optional[str]
            Include only resources from a given file identified by its ID

        branch_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Branch IDs to filter by

        start : typing.Optional[dt.datetime]
            Start date of the time window (earliest time)

        end : typing.Optional[dt.datetime]
            End date of the time window (latest time)

        order_by : typing.Optional[TraceListRequestOrderBy]
            When set to end_time, traces are sorted by their end time, and pending traces are omitted. When set to start_time, all traces are included, with pending traces given "0" for their end time.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TraceListResponse]
            A paginated result set
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/telemetry/traces",
            method="GET",
            params={
                "file_id": file_id,
                "branch_ids": branch_ids,
                "direction": direction,
                "start": serialize_datetime(start) if start is not None else None,
                "end": serialize_datetime(end) if end is not None else None,
                "limit": limit,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TraceListResponse,
                    parse_obj_as(
                        type_=TraceListResponse,
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

    def log_list(
        self,
        *,
        direction: LogListRequestDirection,
        limit: int,
        trace_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        file_id: typing.Optional[str] = None,
        branch_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        start: typing.Optional[dt.datetime] = None,
        end: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[LogListResponse]:
        """
        Get OpenTelemetry logs within a specified time window with flexible pagination options: Pass in only the end time to paginate backwards from there. Pass in a start time to paginate backwards from now until the start time. Pass in both to get resources within the time window. Filter additionally by branch_ids or file_id.

        Parameters
        ----------
        direction : LogListRequestDirection
            Sort direction for the traces. Defaults to descending order of timestamp.

        limit : int
            Maximum items to return in each paginated response

        trace_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        file_id : typing.Optional[str]
            Include only resources from a given file identified by its ID

        branch_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Branch IDs to filter by

        start : typing.Optional[dt.datetime]
            Start date of the time window (earliest time)

        end : typing.Optional[dt.datetime]
            End date of the time window (latest time)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LogListResponse]
            A paginated result set
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/telemetry/logs",
            method="GET",
            params={
                "trace_ids": trace_ids,
                "file_id": file_id,
                "branch_ids": branch_ids,
                "direction": direction,
                "start": serialize_datetime(start) if start is not None else None,
                "end": serialize_datetime(end) if end is not None else None,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LogListResponse,
                    parse_obj_as(
                        type_=LogListResponse,
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


class AsyncRawTelemetryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def trace_list(
        self,
        *,
        direction: TraceListRequestDirection,
        limit: int,
        file_id: typing.Optional[str] = None,
        branch_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        start: typing.Optional[dt.datetime] = None,
        end: typing.Optional[dt.datetime] = None,
        order_by: typing.Optional[TraceListRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TraceListResponse]:
        """
        Get OpenTelemetry traces within a specified time window with flexible pagination options: Pass in only the end time to paginate backwards from there. Pass in a start time to paginate backwards from now until the start time. Pass in both to get resources within the time window. Choose to return in end_time order instead to view traces that completed in a window or since a time. Filter additionally by branch_ids or file_id.

        Parameters
        ----------
        direction : TraceListRequestDirection
            Sort direction for the traces. Defaults to descending order of timestamp.

        limit : int
            Maximum items to return in each paginated response

        file_id : typing.Optional[str]
            Include only resources from a given file identified by its ID

        branch_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Branch IDs to filter by

        start : typing.Optional[dt.datetime]
            Start date of the time window (earliest time)

        end : typing.Optional[dt.datetime]
            End date of the time window (latest time)

        order_by : typing.Optional[TraceListRequestOrderBy]
            When set to end_time, traces are sorted by their end time, and pending traces are omitted. When set to start_time, all traces are included, with pending traces given "0" for their end time.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TraceListResponse]
            A paginated result set
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/telemetry/traces",
            method="GET",
            params={
                "file_id": file_id,
                "branch_ids": branch_ids,
                "direction": direction,
                "start": serialize_datetime(start) if start is not None else None,
                "end": serialize_datetime(end) if end is not None else None,
                "limit": limit,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TraceListResponse,
                    parse_obj_as(
                        type_=TraceListResponse,
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

    async def log_list(
        self,
        *,
        direction: LogListRequestDirection,
        limit: int,
        trace_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        file_id: typing.Optional[str] = None,
        branch_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        start: typing.Optional[dt.datetime] = None,
        end: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[LogListResponse]:
        """
        Get OpenTelemetry logs within a specified time window with flexible pagination options: Pass in only the end time to paginate backwards from there. Pass in a start time to paginate backwards from now until the start time. Pass in both to get resources within the time window. Filter additionally by branch_ids or file_id.

        Parameters
        ----------
        direction : LogListRequestDirection
            Sort direction for the traces. Defaults to descending order of timestamp.

        limit : int
            Maximum items to return in each paginated response

        trace_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        file_id : typing.Optional[str]
            Include only resources from a given file identified by its ID

        branch_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Branch IDs to filter by

        start : typing.Optional[dt.datetime]
            Start date of the time window (earliest time)

        end : typing.Optional[dt.datetime]
            End date of the time window (latest time)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LogListResponse]
            A paginated result set
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/telemetry/logs",
            method="GET",
            params={
                "trace_ids": trace_ids,
                "file_id": file_id,
                "branch_ids": branch_ids,
                "direction": direction,
                "start": serialize_datetime(start) if start is not None else None,
                "end": serialize_datetime(end) if end is not None else None,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LogListResponse,
                    parse_obj_as(
                        type_=LogListResponse,
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
