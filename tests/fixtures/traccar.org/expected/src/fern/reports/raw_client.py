

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.event import Event
from ..types.position import Position
from ..types.report_stops import ReportStops
from ..types.report_summary import ReportSummary
from ..types.report_trips import ReportTrips


class RawReportsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def fetch_a_list_of_events_within_the_time_period_for_the_devices_or_groups(
        self,
        *,
        from_: dt.datetime,
        to: dt.datetime,
        device_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        group_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        type: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Event]]:
        """
        At least one _deviceId_ or one _groupId_ must be passed

        Parameters
        ----------
        from_ : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        to : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        device_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        group_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        type : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            % can be used to return events of all types

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Event]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "reports/events",
            method="GET",
            params={
                "deviceId": device_id,
                "groupId": group_id,
                "type": type,
                "from": serialize_datetime(from_),
                "to": serialize_datetime(to),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Event],
                    parse_obj_as(
                        type_=typing.List[Event],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def fetch_a_list_of_positions_within_the_time_period_for_the_devices_or_groups(
        self,
        *,
        from_: dt.datetime,
        to: dt.datetime,
        device_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        group_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Position]]:
        """
        At least one _deviceId_ or one _groupId_ must be passed

        Parameters
        ----------
        from_ : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        to : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        device_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        group_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Position]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "reports/route",
            method="GET",
            params={
                "deviceId": device_id,
                "groupId": group_id,
                "from": serialize_datetime(from_),
                "to": serialize_datetime(to),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Position],
                    parse_obj_as(
                        type_=typing.List[Position],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def fetch_a_list_of_report_stops_within_the_time_period_for_the_devices_or_groups(
        self,
        *,
        from_: dt.datetime,
        to: dt.datetime,
        device_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        group_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[ReportStops]]:
        """
        At least one _deviceId_ or one _groupId_ must be passed

        Parameters
        ----------
        from_ : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        to : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        device_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        group_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ReportStops]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "reports/stops",
            method="GET",
            params={
                "deviceId": device_id,
                "groupId": group_id,
                "from": serialize_datetime(from_),
                "to": serialize_datetime(to),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ReportStops],
                    parse_obj_as(
                        type_=typing.List[ReportStops],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def fetch_a_list_of_report_summary_within_the_time_period_for_the_devices_or_groups(
        self,
        *,
        from_: dt.datetime,
        to: dt.datetime,
        device_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        group_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[ReportSummary]]:
        """
        At least one _deviceId_ or one _groupId_ must be passed

        Parameters
        ----------
        from_ : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        to : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        device_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        group_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ReportSummary]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "reports/summary",
            method="GET",
            params={
                "deviceId": device_id,
                "groupId": group_id,
                "from": serialize_datetime(from_),
                "to": serialize_datetime(to),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ReportSummary],
                    parse_obj_as(
                        type_=typing.List[ReportSummary],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def fetch_a_list_of_report_trips_within_the_time_period_for_the_devices_or_groups(
        self,
        *,
        from_: dt.datetime,
        to: dt.datetime,
        device_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        group_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[ReportTrips]]:
        """
        At least one _deviceId_ or one _groupId_ must be passed

        Parameters
        ----------
        from_ : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        to : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        device_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        group_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ReportTrips]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "reports/trips",
            method="GET",
            params={
                "deviceId": device_id,
                "groupId": group_id,
                "from": serialize_datetime(from_),
                "to": serialize_datetime(to),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ReportTrips],
                    parse_obj_as(
                        type_=typing.List[ReportTrips],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawReportsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def fetch_a_list_of_events_within_the_time_period_for_the_devices_or_groups(
        self,
        *,
        from_: dt.datetime,
        to: dt.datetime,
        device_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        group_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        type: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Event]]:
        """
        At least one _deviceId_ or one _groupId_ must be passed

        Parameters
        ----------
        from_ : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        to : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        device_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        group_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        type : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            % can be used to return events of all types

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Event]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "reports/events",
            method="GET",
            params={
                "deviceId": device_id,
                "groupId": group_id,
                "type": type,
                "from": serialize_datetime(from_),
                "to": serialize_datetime(to),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Event],
                    parse_obj_as(
                        type_=typing.List[Event],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def fetch_a_list_of_positions_within_the_time_period_for_the_devices_or_groups(
        self,
        *,
        from_: dt.datetime,
        to: dt.datetime,
        device_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        group_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Position]]:
        """
        At least one _deviceId_ or one _groupId_ must be passed

        Parameters
        ----------
        from_ : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        to : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        device_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        group_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Position]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "reports/route",
            method="GET",
            params={
                "deviceId": device_id,
                "groupId": group_id,
                "from": serialize_datetime(from_),
                "to": serialize_datetime(to),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Position],
                    parse_obj_as(
                        type_=typing.List[Position],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def fetch_a_list_of_report_stops_within_the_time_period_for_the_devices_or_groups(
        self,
        *,
        from_: dt.datetime,
        to: dt.datetime,
        device_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        group_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[ReportStops]]:
        """
        At least one _deviceId_ or one _groupId_ must be passed

        Parameters
        ----------
        from_ : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        to : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        device_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        group_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ReportStops]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "reports/stops",
            method="GET",
            params={
                "deviceId": device_id,
                "groupId": group_id,
                "from": serialize_datetime(from_),
                "to": serialize_datetime(to),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ReportStops],
                    parse_obj_as(
                        type_=typing.List[ReportStops],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def fetch_a_list_of_report_summary_within_the_time_period_for_the_devices_or_groups(
        self,
        *,
        from_: dt.datetime,
        to: dt.datetime,
        device_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        group_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[ReportSummary]]:
        """
        At least one _deviceId_ or one _groupId_ must be passed

        Parameters
        ----------
        from_ : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        to : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        device_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        group_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ReportSummary]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "reports/summary",
            method="GET",
            params={
                "deviceId": device_id,
                "groupId": group_id,
                "from": serialize_datetime(from_),
                "to": serialize_datetime(to),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ReportSummary],
                    parse_obj_as(
                        type_=typing.List[ReportSummary],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def fetch_a_list_of_report_trips_within_the_time_period_for_the_devices_or_groups(
        self,
        *,
        from_: dt.datetime,
        to: dt.datetime,
        device_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        group_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[ReportTrips]]:
        """
        At least one _deviceId_ or one _groupId_ must be passed

        Parameters
        ----------
        from_ : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        to : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        device_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        group_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ReportTrips]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "reports/trips",
            method="GET",
            params={
                "deviceId": device_id,
                "groupId": group_id,
                "from": serialize_datetime(from_),
                "to": serialize_datetime(to),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ReportTrips],
                    parse_obj_as(
                        type_=typing.List[ReportTrips],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
