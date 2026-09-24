

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..types.index_range import IndexRange
from ..types.monitor import Monitor
from ..types.monitor_callback_subscribe import MonitorCallbackSubscribe
from ..types.monitor_parameter_extended_event_param_item import MonitorParameterExtendedEventParamItem
from ..types.monitor_parameter_trigger_param import MonitorParameterTriggerParam
from ..types.monitor_ref import MonitorRef
from ..types.monitors import Monitors
from .types.monitor_status_setter_status import MonitorStatusSetterStatus
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawMonitorsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_fleet_monitors(
        self,
        fid: str,
        *,
        index_range: typing.Optional[IndexRange] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Monitors]:
        """
        Returns the list of subscribed Monitors of the fleet.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        index_range : typing.Optional[IndexRange]
            Results indexes will be included in this range (see **indexRange** model).

              default: 0-

              example: 0-, 0-5

        page_size : typing.Optional[int]
            The maximum number of results (for a collection results response) to return per page. When not set, at most 60 results will be returned.  The range for this parameter is [1...60]

        page_token : typing.Optional[str]
            Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Monitors]
            A list of Monitors
        """
        _response = self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/monitors",
            method="GET",
            params={
                "indexRange": index_range,
                "pageSize": page_size,
                "pageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Monitors,
                    parse_obj_as(
                        type_=Monitors,
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

    def create_fleet_vehicle_monitor(
        self,
        fid: str,
        *,
        label: str,
        subscribe_param: MonitorCallbackSubscribe,
        trigger_param: MonitorParameterTriggerParam,
        extended_event_param: typing.Optional[typing.Sequence[MonitorParameterExtendedEventParamItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MonitorRef]:
        """
        >Create a Monitor for all Vehicles of the fleet. This is a kind of vehicle monitor that generates an event following the transition state of one of the (monitored) data  of the vehicles. As for example the fuel level, the moving out of a defined geographical area.

        >When the trigger occurs, the built event expressed as a JSON object will be sent over the subscribed callback.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        label : str
            Monitor label (usually its name).

        subscribe_param : MonitorCallbackSubscribe

        trigger_param : MonitorParameterTriggerParam
            Monitor trigger-param that allows to compound triggers by applying a boolean expression to evaluate them.

        extended_event_param : typing.Optional[typing.Sequence[MonitorParameterExtendedEventParamItem]]
            Allow to set extra vehicle data (defined in data model) to add to the monitor event
            when publishing. The possible values are :


            |value|description|Related model |
            |----------|:-------------|------:|
            |vehicle.doorsState|Latest known door state (timestamped) before the eventDate|DoorState|
            |vehicle.status|Latest known vehicle status (timestamped) before the eventDate|Status|
            |vehicle.maintenance|Latest known maintenance(timestamped) before the eventDate|Maintenance|
            |vehicle.position|Last vehicle position (timestamped) before the eventDate|Position|
            |vehicle.telemetry${.TelemetryEnum} |Latest known telemetry (timestamped) before the eventDate filtered with type|Telemetry
            |vehicle.alerts|List of active alerts at the eventDate|Alert|
            |vehicle.collisions|Latest known collisions before the eventDate|Collision|
            |vehicle.trip|Trip related to the event that triggers the notification|Trip|
            |vehicle.stolen|Vehicle Stolen context at the eventDate (only returns when vehicle is reported stolen) |Stolen|


            * For telemetry extension:
              * The suffix ```${.TelemetryEnum}``` can be selected to refine with telemetry type (from the TelemetryEnum list). This value (with suffix) can be selected **_several times_** to included suitable telemetry messages with the extention.
              * Using ```vehicle.telemetry``` without suffix means to include all available telemetries.
            * The set of data will then correspond to the union of extensions used in the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MonitorRef]
            Monitor created or updated successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/monitors",
            method="POST",
            json={
                "label": label,
                "subscribeParam": convert_and_respect_annotation_metadata(
                    object_=subscribe_param, annotation=MonitorCallbackSubscribe, direction="write"
                ),
                "extendedEventParam": extended_event_param,
                "triggerParam": convert_and_respect_annotation_metadata(
                    object_=trigger_param, annotation=MonitorParameterTriggerParam, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MonitorRef,
                    parse_obj_as(
                        type_=MonitorRef,
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

    def get_fleet_monitors_status_by_id(
        self, fid: str, mid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Monitor]:
        """
        Returns information about a specific Monitor for a given fleet.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        mid : str
            id of the monitor.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Monitor]
            Monitor response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/monitors/{encode_path_param(mid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Monitor,
                    parse_obj_as(
                        type_=Monitor,
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

    def update_fleet_vehicle_monitor(
        self,
        fid: str,
        mid: str,
        *,
        label: str,
        subscribe_param: MonitorCallbackSubscribe,
        trigger_param: MonitorParameterTriggerParam,
        extended_event_param: typing.Optional[typing.Sequence[MonitorParameterExtendedEventParamItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MonitorRef]:
        """
        Update an existing ```Monitor``` that has been posted (and accepted previously) for this fleet. The monitor object (body) provided should be complete because the aggregation is not supported for the update of the ```monitor```. You can first retrieve this object using the ```GET /monitor/{mid}``` API, then modify it and finally publish it (via this ```PUT API```).

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        mid : str
            id of the monitor.

        label : str
            Monitor label (usually its name).

        subscribe_param : MonitorCallbackSubscribe

        trigger_param : MonitorParameterTriggerParam
            Monitor trigger-param that allows to compound triggers by applying a boolean expression to evaluate them.

        extended_event_param : typing.Optional[typing.Sequence[MonitorParameterExtendedEventParamItem]]
            Allow to set extra vehicle data (defined in data model) to add to the monitor event
            when publishing. The possible values are :


            |value|description|Related model |
            |----------|:-------------|------:|
            |vehicle.doorsState|Latest known door state (timestamped) before the eventDate|DoorState|
            |vehicle.status|Latest known vehicle status (timestamped) before the eventDate|Status|
            |vehicle.maintenance|Latest known maintenance(timestamped) before the eventDate|Maintenance|
            |vehicle.position|Last vehicle position (timestamped) before the eventDate|Position|
            |vehicle.telemetry${.TelemetryEnum} |Latest known telemetry (timestamped) before the eventDate filtered with type|Telemetry
            |vehicle.alerts|List of active alerts at the eventDate|Alert|
            |vehicle.collisions|Latest known collisions before the eventDate|Collision|
            |vehicle.trip|Trip related to the event that triggers the notification|Trip|
            |vehicle.stolen|Vehicle Stolen context at the eventDate (only returns when vehicle is reported stolen) |Stolen|


            * For telemetry extension:
              * The suffix ```${.TelemetryEnum}``` can be selected to refine with telemetry type (from the TelemetryEnum list). This value (with suffix) can be selected **_several times_** to included suitable telemetry messages with the extention.
              * Using ```vehicle.telemetry``` without suffix means to include all available telemetries.
            * The set of data will then correspond to the union of extensions used in the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MonitorRef]
            Monitor created or updated successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/monitors/{encode_path_param(mid)}",
            method="PUT",
            json={
                "label": label,
                "subscribeParam": convert_and_respect_annotation_metadata(
                    object_=subscribe_param, annotation=MonitorCallbackSubscribe, direction="write"
                ),
                "extendedEventParam": extended_event_param,
                "triggerParam": convert_and_respect_annotation_metadata(
                    object_=trigger_param, annotation=MonitorParameterTriggerParam, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MonitorRef,
                    parse_obj_as(
                        type_=MonitorRef,
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

    def delete_fleet_monitor(
        self, fid: str, mid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Stop (disable) an existing Monitor.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        mid : str
            id of the monitor.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/monitors/{encode_path_param(mid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def set_fleet_vehicle_monitor_status(
        self,
        fid: str,
        mid: str,
        *,
        status: MonitorStatusSetterStatus,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MonitorRef]:
        """
        Set monitor status.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        mid : str
            id of the monitor.

        status : MonitorStatusSetterStatus

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MonitorRef]
            Monitor created or updated successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/monitors/{encode_path_param(mid)}/status",
            method="PUT",
            json={
                "status": status,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MonitorRef,
                    parse_obj_as(
                        type_=MonitorRef,
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


class AsyncRawMonitorsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_fleet_monitors(
        self,
        fid: str,
        *,
        index_range: typing.Optional[IndexRange] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Monitors]:
        """
        Returns the list of subscribed Monitors of the fleet.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        index_range : typing.Optional[IndexRange]
            Results indexes will be included in this range (see **indexRange** model).

              default: 0-

              example: 0-, 0-5

        page_size : typing.Optional[int]
            The maximum number of results (for a collection results response) to return per page. When not set, at most 60 results will be returned.  The range for this parameter is [1...60]

        page_token : typing.Optional[str]
            Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Monitors]
            A list of Monitors
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/monitors",
            method="GET",
            params={
                "indexRange": index_range,
                "pageSize": page_size,
                "pageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Monitors,
                    parse_obj_as(
                        type_=Monitors,
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

    async def create_fleet_vehicle_monitor(
        self,
        fid: str,
        *,
        label: str,
        subscribe_param: MonitorCallbackSubscribe,
        trigger_param: MonitorParameterTriggerParam,
        extended_event_param: typing.Optional[typing.Sequence[MonitorParameterExtendedEventParamItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MonitorRef]:
        """
        >Create a Monitor for all Vehicles of the fleet. This is a kind of vehicle monitor that generates an event following the transition state of one of the (monitored) data  of the vehicles. As for example the fuel level, the moving out of a defined geographical area.

        >When the trigger occurs, the built event expressed as a JSON object will be sent over the subscribed callback.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        label : str
            Monitor label (usually its name).

        subscribe_param : MonitorCallbackSubscribe

        trigger_param : MonitorParameterTriggerParam
            Monitor trigger-param that allows to compound triggers by applying a boolean expression to evaluate them.

        extended_event_param : typing.Optional[typing.Sequence[MonitorParameterExtendedEventParamItem]]
            Allow to set extra vehicle data (defined in data model) to add to the monitor event
            when publishing. The possible values are :


            |value|description|Related model |
            |----------|:-------------|------:|
            |vehicle.doorsState|Latest known door state (timestamped) before the eventDate|DoorState|
            |vehicle.status|Latest known vehicle status (timestamped) before the eventDate|Status|
            |vehicle.maintenance|Latest known maintenance(timestamped) before the eventDate|Maintenance|
            |vehicle.position|Last vehicle position (timestamped) before the eventDate|Position|
            |vehicle.telemetry${.TelemetryEnum} |Latest known telemetry (timestamped) before the eventDate filtered with type|Telemetry
            |vehicle.alerts|List of active alerts at the eventDate|Alert|
            |vehicle.collisions|Latest known collisions before the eventDate|Collision|
            |vehicle.trip|Trip related to the event that triggers the notification|Trip|
            |vehicle.stolen|Vehicle Stolen context at the eventDate (only returns when vehicle is reported stolen) |Stolen|


            * For telemetry extension:
              * The suffix ```${.TelemetryEnum}``` can be selected to refine with telemetry type (from the TelemetryEnum list). This value (with suffix) can be selected **_several times_** to included suitable telemetry messages with the extention.
              * Using ```vehicle.telemetry``` without suffix means to include all available telemetries.
            * The set of data will then correspond to the union of extensions used in the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MonitorRef]
            Monitor created or updated successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/monitors",
            method="POST",
            json={
                "label": label,
                "subscribeParam": convert_and_respect_annotation_metadata(
                    object_=subscribe_param, annotation=MonitorCallbackSubscribe, direction="write"
                ),
                "extendedEventParam": extended_event_param,
                "triggerParam": convert_and_respect_annotation_metadata(
                    object_=trigger_param, annotation=MonitorParameterTriggerParam, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MonitorRef,
                    parse_obj_as(
                        type_=MonitorRef,
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

    async def get_fleet_monitors_status_by_id(
        self, fid: str, mid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Monitor]:
        """
        Returns information about a specific Monitor for a given fleet.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        mid : str
            id of the monitor.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Monitor]
            Monitor response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/monitors/{encode_path_param(mid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Monitor,
                    parse_obj_as(
                        type_=Monitor,
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

    async def update_fleet_vehicle_monitor(
        self,
        fid: str,
        mid: str,
        *,
        label: str,
        subscribe_param: MonitorCallbackSubscribe,
        trigger_param: MonitorParameterTriggerParam,
        extended_event_param: typing.Optional[typing.Sequence[MonitorParameterExtendedEventParamItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MonitorRef]:
        """
        Update an existing ```Monitor``` that has been posted (and accepted previously) for this fleet. The monitor object (body) provided should be complete because the aggregation is not supported for the update of the ```monitor```. You can first retrieve this object using the ```GET /monitor/{mid}``` API, then modify it and finally publish it (via this ```PUT API```).

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        mid : str
            id of the monitor.

        label : str
            Monitor label (usually its name).

        subscribe_param : MonitorCallbackSubscribe

        trigger_param : MonitorParameterTriggerParam
            Monitor trigger-param that allows to compound triggers by applying a boolean expression to evaluate them.

        extended_event_param : typing.Optional[typing.Sequence[MonitorParameterExtendedEventParamItem]]
            Allow to set extra vehicle data (defined in data model) to add to the monitor event
            when publishing. The possible values are :


            |value|description|Related model |
            |----------|:-------------|------:|
            |vehicle.doorsState|Latest known door state (timestamped) before the eventDate|DoorState|
            |vehicle.status|Latest known vehicle status (timestamped) before the eventDate|Status|
            |vehicle.maintenance|Latest known maintenance(timestamped) before the eventDate|Maintenance|
            |vehicle.position|Last vehicle position (timestamped) before the eventDate|Position|
            |vehicle.telemetry${.TelemetryEnum} |Latest known telemetry (timestamped) before the eventDate filtered with type|Telemetry
            |vehicle.alerts|List of active alerts at the eventDate|Alert|
            |vehicle.collisions|Latest known collisions before the eventDate|Collision|
            |vehicle.trip|Trip related to the event that triggers the notification|Trip|
            |vehicle.stolen|Vehicle Stolen context at the eventDate (only returns when vehicle is reported stolen) |Stolen|


            * For telemetry extension:
              * The suffix ```${.TelemetryEnum}``` can be selected to refine with telemetry type (from the TelemetryEnum list). This value (with suffix) can be selected **_several times_** to included suitable telemetry messages with the extention.
              * Using ```vehicle.telemetry``` without suffix means to include all available telemetries.
            * The set of data will then correspond to the union of extensions used in the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MonitorRef]
            Monitor created or updated successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/monitors/{encode_path_param(mid)}",
            method="PUT",
            json={
                "label": label,
                "subscribeParam": convert_and_respect_annotation_metadata(
                    object_=subscribe_param, annotation=MonitorCallbackSubscribe, direction="write"
                ),
                "extendedEventParam": extended_event_param,
                "triggerParam": convert_and_respect_annotation_metadata(
                    object_=trigger_param, annotation=MonitorParameterTriggerParam, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MonitorRef,
                    parse_obj_as(
                        type_=MonitorRef,
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

    async def delete_fleet_monitor(
        self, fid: str, mid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Stop (disable) an existing Monitor.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        mid : str
            id of the monitor.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/monitors/{encode_path_param(mid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def set_fleet_vehicle_monitor_status(
        self,
        fid: str,
        mid: str,
        *,
        status: MonitorStatusSetterStatus,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MonitorRef]:
        """
        Set monitor status.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        mid : str
            id of the monitor.

        status : MonitorStatusSetterStatus

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MonitorRef]
            Monitor created or updated successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"fleets/{encode_path_param(fid)}/monitors/{encode_path_param(mid)}/status",
            method="PUT",
            json={
                "status": status,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MonitorRef,
                    parse_obj_as(
                        type_=MonitorRef,
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
