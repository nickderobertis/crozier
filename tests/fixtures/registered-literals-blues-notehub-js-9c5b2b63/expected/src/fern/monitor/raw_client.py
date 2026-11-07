

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
from ..types.monitor import Monitor
from ..types.monitor_aggregate_function import MonitorAggregateFunction
from ..types.monitor_alert_routes_item import MonitorAlertRoutesItem
from ..types.monitor_condition_type import MonitorConditionType
from ..types.monitor_source_type import MonitorSourceType
from .types.create_monitor_aggregate_function import CreateMonitorAggregateFunction
from .types.create_monitor_alert_routes_item import CreateMonitorAlertRoutesItem
from .types.create_monitor_condition_type import CreateMonitorConditionType
from .types.create_monitor_source_type import CreateMonitorSourceType
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawMonitorClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_monitors(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[Monitor]]:
        """
        Get list of defined Monitors

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Monitor]]
            The response body from GET /monitors
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/monitors",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Monitor],
                    parse_obj_as(
                        type_=typing.List[Monitor],
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

    def create_monitor(
        self,
        project_or_product_uid: str,
        *,
        alert_routes: typing.Sequence[CreateMonitorAlertRoutesItem],
        description: str,
        name: str,
        source_type: CreateMonitorSourceType,
        threshold: int,
        aggregate_function: typing.Optional[CreateMonitorAggregateFunction] = OMIT,
        aggregate_window: typing.Optional[str] = OMIT,
        alert: typing.Optional[bool] = OMIT,
        condition_type: typing.Optional[CreateMonitorConditionType] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        fleet_filter: typing.Optional[typing.Sequence[str]] = OMIT,
        last_routed_at: typing.Optional[str] = OMIT,
        notefile_filter: typing.Optional[typing.Sequence[str]] = OMIT,
        per_device: typing.Optional[bool] = OMIT,
        routing_cooldown_period: typing.Optional[str] = OMIT,
        silenced: typing.Optional[bool] = OMIT,
        source_selector: typing.Optional[str] = OMIT,
        uid: typing.Optional[str] = OMIT,
        usage_scope: typing.Optional[str] = OMIT,
        usage_type: typing.Optional[str] = OMIT,
        usage_window: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Monitor]:
        """
        Create a new Monitor

        Parameters
        ----------
        project_or_product_uid : str

        alert_routes : typing.Sequence[CreateMonitorAlertRoutesItem]

        description : str

        name : str

        source_type : CreateMonitorSourceType
            The type of source to monitor. Supported values are "event" and "heartbeat".

        threshold : int
            The type of condition to apply to the value selected by the source_selector

        aggregate_function : typing.Optional[CreateMonitorAggregateFunction]
            Aggregate function to apply to the selected values before applying the condition. [none, sum, average, max, min]

        aggregate_window : typing.Optional[str]
            The time window to aggregate the selected values. It follows the format of a number followed by a time unit

        alert : typing.Optional[bool]
            If true, the monitor is in alert state.

        condition_type : typing.Optional[CreateMonitorConditionType]
            A comparison operation to apply to the value selected by the source_selector [greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to]

        disabled : typing.Optional[bool]
            If true, the monitor will not be evaluated.

        fleet_filter : typing.Optional[typing.Sequence[str]]

        last_routed_at : typing.Optional[str]
            The last time the monitor was evaluated and routed.

        notefile_filter : typing.Optional[typing.Sequence[str]]

        per_device : typing.Optional[bool]
            Only relevant when using an aggregate_function. If true, the monitor will be evaluated per device, | rather than across the set of selected devices. If true then if a single device matches the specified criteria, | and alert will be created, otherwise the aggregate function will be applied across all devices.

        routing_cooldown_period : typing.Optional[str]
            The time period to wait before routing another event after the monitor | has been triggered. It follows the format of a number followed by a time unit.

        silenced : typing.Optional[bool]
            If true, alerts will be created, but no notifications will be sent.

        source_selector : typing.Optional[str]
            A valid JSONata expression that selects the value to monitor from the source. | It should return a single, numeric value.

        uid : typing.Optional[str]

        usage_scope : typing.Optional[str]
            For usage monitors: the scope of aggregation. Supported values are "device" and "fleet".

        usage_type : typing.Optional[str]
            For usage monitors: the type of data usage to monitor. Supported values are "cellular" and "satellite".

        usage_window : typing.Optional[int]
            For usage monitors: the rolling time window in days to sum usage over (e.g. 30 for 30 days).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Monitor]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/monitors",
            method="POST",
            json={
                "aggregate_function": aggregate_function,
                "aggregate_window": aggregate_window,
                "alert": alert,
                "alert_routes": convert_and_respect_annotation_metadata(
                    object_=alert_routes, annotation=typing.Sequence[CreateMonitorAlertRoutesItem], direction="write"
                ),
                "condition_type": condition_type,
                "description": description,
                "disabled": disabled,
                "fleet_filter": fleet_filter,
                "last_routed_at": last_routed_at,
                "name": name,
                "notefile_filter": notefile_filter,
                "per_device": per_device,
                "routing_cooldown_period": routing_cooldown_period,
                "silenced": silenced,
                "source_selector": source_selector,
                "source_type": source_type,
                "threshold": threshold,
                "uid": uid,
                "usage_scope": usage_scope,
                "usage_type": usage_type,
                "usage_window": usage_window,
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

    def get_monitor(
        self, project_or_product_uid: str, monitor_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Monitor]:
        """
        Get Monitor

        Parameters
        ----------
        project_or_product_uid : str

        monitor_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Monitor]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/monitors/{encode_path_param(monitor_uid)}",
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

    def update_monitor(
        self,
        project_or_product_uid: str,
        monitor_uid: str,
        *,
        aggregate_function: typing.Optional[MonitorAggregateFunction] = OMIT,
        aggregate_window: typing.Optional[str] = OMIT,
        alert: typing.Optional[bool] = OMIT,
        alert_routes: typing.Optional[typing.Sequence[MonitorAlertRoutesItem]] = OMIT,
        condition_type: typing.Optional[MonitorConditionType] = OMIT,
        description: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        fleet_filter: typing.Optional[typing.Sequence[str]] = OMIT,
        last_routed_at: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        notefile_filter: typing.Optional[typing.Sequence[str]] = OMIT,
        per_device: typing.Optional[bool] = OMIT,
        routing_cooldown_period: typing.Optional[str] = OMIT,
        silenced: typing.Optional[bool] = OMIT,
        source_selector: typing.Optional[str] = OMIT,
        source_type: typing.Optional[MonitorSourceType] = OMIT,
        threshold: typing.Optional[int] = OMIT,
        uid: typing.Optional[str] = OMIT,
        usage_scope: typing.Optional[str] = OMIT,
        usage_type: typing.Optional[str] = OMIT,
        usage_window: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Monitor]:
        """
        Update Monitor

        Parameters
        ----------
        project_or_product_uid : str

        monitor_uid : str

        aggregate_function : typing.Optional[MonitorAggregateFunction]
            Aggregate function to apply to the selected values before applying the condition. [none, sum, average, max, min]

        aggregate_window : typing.Optional[str]
            The time window to aggregate the selected values. It follows the format of a number followed by a time unit

        alert : typing.Optional[bool]
            If true, the monitor is in alert state.

        alert_routes : typing.Optional[typing.Sequence[MonitorAlertRoutesItem]]

        condition_type : typing.Optional[MonitorConditionType]
            A comparison operation to apply to the value selected by the source_selector [greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to]

        description : typing.Optional[str]

        disabled : typing.Optional[bool]
            If true, the monitor will not be evaluated.

        fleet_filter : typing.Optional[typing.Sequence[str]]

        last_routed_at : typing.Optional[str]
            The last time the monitor was evaluated and routed.

        name : typing.Optional[str]

        notefile_filter : typing.Optional[typing.Sequence[str]]

        per_device : typing.Optional[bool]
            Only relevant when using an aggregate_function. If true, the monitor will be evaluated per device, | rather than across the set of selected devices. If true then if a single device matches the specified criteria, | and alert will be created, otherwise the aggregate function will be applied across all devices.

        routing_cooldown_period : typing.Optional[str]
            The time period to wait before routing another event after the monitor | has been triggered. It follows the format of a number followed by a time unit.

        silenced : typing.Optional[bool]
            If true, alerts will be created, but no notifications will be sent.

        source_selector : typing.Optional[str]
            A valid JSONata expression that selects the value to monitor from the source. | It should return a single, numeric value.

        source_type : typing.Optional[MonitorSourceType]
            The type of source to monitor. Supported values are "event" and "heartbeat".

        threshold : typing.Optional[int]
            The type of condition to apply to the value selected by the source_selector

        uid : typing.Optional[str]

        usage_scope : typing.Optional[str]
            For usage monitors: the scope of aggregation. Supported values are "device" and "fleet".

        usage_type : typing.Optional[str]
            For usage monitors: the type of data usage to monitor. Supported values are "cellular" and "satellite".

        usage_window : typing.Optional[int]
            For usage monitors: the rolling time window in days to sum usage over (e.g. 30 for 30 days).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Monitor]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/monitors/{encode_path_param(monitor_uid)}",
            method="PUT",
            json={
                "aggregate_function": aggregate_function,
                "aggregate_window": aggregate_window,
                "alert": alert,
                "alert_routes": convert_and_respect_annotation_metadata(
                    object_=alert_routes, annotation=typing.Sequence[MonitorAlertRoutesItem], direction="write"
                ),
                "condition_type": condition_type,
                "description": description,
                "disabled": disabled,
                "fleet_filter": fleet_filter,
                "last_routed_at": last_routed_at,
                "name": name,
                "notefile_filter": notefile_filter,
                "per_device": per_device,
                "routing_cooldown_period": routing_cooldown_period,
                "silenced": silenced,
                "source_selector": source_selector,
                "source_type": source_type,
                "threshold": threshold,
                "uid": uid,
                "usage_scope": usage_scope,
                "usage_type": usage_type,
                "usage_window": usage_window,
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

    def delete_monitor(
        self, project_or_product_uid: str, monitor_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Monitor]:
        """
        Delete Monitor

        Parameters
        ----------
        project_or_product_uid : str

        monitor_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Monitor]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/monitors/{encode_path_param(monitor_uid)}",
            method="DELETE",
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


class AsyncRawMonitorClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_monitors(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[Monitor]]:
        """
        Get list of defined Monitors

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Monitor]]
            The response body from GET /monitors
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/monitors",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Monitor],
                    parse_obj_as(
                        type_=typing.List[Monitor],
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

    async def create_monitor(
        self,
        project_or_product_uid: str,
        *,
        alert_routes: typing.Sequence[CreateMonitorAlertRoutesItem],
        description: str,
        name: str,
        source_type: CreateMonitorSourceType,
        threshold: int,
        aggregate_function: typing.Optional[CreateMonitorAggregateFunction] = OMIT,
        aggregate_window: typing.Optional[str] = OMIT,
        alert: typing.Optional[bool] = OMIT,
        condition_type: typing.Optional[CreateMonitorConditionType] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        fleet_filter: typing.Optional[typing.Sequence[str]] = OMIT,
        last_routed_at: typing.Optional[str] = OMIT,
        notefile_filter: typing.Optional[typing.Sequence[str]] = OMIT,
        per_device: typing.Optional[bool] = OMIT,
        routing_cooldown_period: typing.Optional[str] = OMIT,
        silenced: typing.Optional[bool] = OMIT,
        source_selector: typing.Optional[str] = OMIT,
        uid: typing.Optional[str] = OMIT,
        usage_scope: typing.Optional[str] = OMIT,
        usage_type: typing.Optional[str] = OMIT,
        usage_window: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Monitor]:
        """
        Create a new Monitor

        Parameters
        ----------
        project_or_product_uid : str

        alert_routes : typing.Sequence[CreateMonitorAlertRoutesItem]

        description : str

        name : str

        source_type : CreateMonitorSourceType
            The type of source to monitor. Supported values are "event" and "heartbeat".

        threshold : int
            The type of condition to apply to the value selected by the source_selector

        aggregate_function : typing.Optional[CreateMonitorAggregateFunction]
            Aggregate function to apply to the selected values before applying the condition. [none, sum, average, max, min]

        aggregate_window : typing.Optional[str]
            The time window to aggregate the selected values. It follows the format of a number followed by a time unit

        alert : typing.Optional[bool]
            If true, the monitor is in alert state.

        condition_type : typing.Optional[CreateMonitorConditionType]
            A comparison operation to apply to the value selected by the source_selector [greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to]

        disabled : typing.Optional[bool]
            If true, the monitor will not be evaluated.

        fleet_filter : typing.Optional[typing.Sequence[str]]

        last_routed_at : typing.Optional[str]
            The last time the monitor was evaluated and routed.

        notefile_filter : typing.Optional[typing.Sequence[str]]

        per_device : typing.Optional[bool]
            Only relevant when using an aggregate_function. If true, the monitor will be evaluated per device, | rather than across the set of selected devices. If true then if a single device matches the specified criteria, | and alert will be created, otherwise the aggregate function will be applied across all devices.

        routing_cooldown_period : typing.Optional[str]
            The time period to wait before routing another event after the monitor | has been triggered. It follows the format of a number followed by a time unit.

        silenced : typing.Optional[bool]
            If true, alerts will be created, but no notifications will be sent.

        source_selector : typing.Optional[str]
            A valid JSONata expression that selects the value to monitor from the source. | It should return a single, numeric value.

        uid : typing.Optional[str]

        usage_scope : typing.Optional[str]
            For usage monitors: the scope of aggregation. Supported values are "device" and "fleet".

        usage_type : typing.Optional[str]
            For usage monitors: the type of data usage to monitor. Supported values are "cellular" and "satellite".

        usage_window : typing.Optional[int]
            For usage monitors: the rolling time window in days to sum usage over (e.g. 30 for 30 days).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Monitor]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/monitors",
            method="POST",
            json={
                "aggregate_function": aggregate_function,
                "aggregate_window": aggregate_window,
                "alert": alert,
                "alert_routes": convert_and_respect_annotation_metadata(
                    object_=alert_routes, annotation=typing.Sequence[CreateMonitorAlertRoutesItem], direction="write"
                ),
                "condition_type": condition_type,
                "description": description,
                "disabled": disabled,
                "fleet_filter": fleet_filter,
                "last_routed_at": last_routed_at,
                "name": name,
                "notefile_filter": notefile_filter,
                "per_device": per_device,
                "routing_cooldown_period": routing_cooldown_period,
                "silenced": silenced,
                "source_selector": source_selector,
                "source_type": source_type,
                "threshold": threshold,
                "uid": uid,
                "usage_scope": usage_scope,
                "usage_type": usage_type,
                "usage_window": usage_window,
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

    async def get_monitor(
        self, project_or_product_uid: str, monitor_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Monitor]:
        """
        Get Monitor

        Parameters
        ----------
        project_or_product_uid : str

        monitor_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Monitor]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/monitors/{encode_path_param(monitor_uid)}",
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

    async def update_monitor(
        self,
        project_or_product_uid: str,
        monitor_uid: str,
        *,
        aggregate_function: typing.Optional[MonitorAggregateFunction] = OMIT,
        aggregate_window: typing.Optional[str] = OMIT,
        alert: typing.Optional[bool] = OMIT,
        alert_routes: typing.Optional[typing.Sequence[MonitorAlertRoutesItem]] = OMIT,
        condition_type: typing.Optional[MonitorConditionType] = OMIT,
        description: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        fleet_filter: typing.Optional[typing.Sequence[str]] = OMIT,
        last_routed_at: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        notefile_filter: typing.Optional[typing.Sequence[str]] = OMIT,
        per_device: typing.Optional[bool] = OMIT,
        routing_cooldown_period: typing.Optional[str] = OMIT,
        silenced: typing.Optional[bool] = OMIT,
        source_selector: typing.Optional[str] = OMIT,
        source_type: typing.Optional[MonitorSourceType] = OMIT,
        threshold: typing.Optional[int] = OMIT,
        uid: typing.Optional[str] = OMIT,
        usage_scope: typing.Optional[str] = OMIT,
        usage_type: typing.Optional[str] = OMIT,
        usage_window: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Monitor]:
        """
        Update Monitor

        Parameters
        ----------
        project_or_product_uid : str

        monitor_uid : str

        aggregate_function : typing.Optional[MonitorAggregateFunction]
            Aggregate function to apply to the selected values before applying the condition. [none, sum, average, max, min]

        aggregate_window : typing.Optional[str]
            The time window to aggregate the selected values. It follows the format of a number followed by a time unit

        alert : typing.Optional[bool]
            If true, the monitor is in alert state.

        alert_routes : typing.Optional[typing.Sequence[MonitorAlertRoutesItem]]

        condition_type : typing.Optional[MonitorConditionType]
            A comparison operation to apply to the value selected by the source_selector [greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to]

        description : typing.Optional[str]

        disabled : typing.Optional[bool]
            If true, the monitor will not be evaluated.

        fleet_filter : typing.Optional[typing.Sequence[str]]

        last_routed_at : typing.Optional[str]
            The last time the monitor was evaluated and routed.

        name : typing.Optional[str]

        notefile_filter : typing.Optional[typing.Sequence[str]]

        per_device : typing.Optional[bool]
            Only relevant when using an aggregate_function. If true, the monitor will be evaluated per device, | rather than across the set of selected devices. If true then if a single device matches the specified criteria, | and alert will be created, otherwise the aggregate function will be applied across all devices.

        routing_cooldown_period : typing.Optional[str]
            The time period to wait before routing another event after the monitor | has been triggered. It follows the format of a number followed by a time unit.

        silenced : typing.Optional[bool]
            If true, alerts will be created, but no notifications will be sent.

        source_selector : typing.Optional[str]
            A valid JSONata expression that selects the value to monitor from the source. | It should return a single, numeric value.

        source_type : typing.Optional[MonitorSourceType]
            The type of source to monitor. Supported values are "event" and "heartbeat".

        threshold : typing.Optional[int]
            The type of condition to apply to the value selected by the source_selector

        uid : typing.Optional[str]

        usage_scope : typing.Optional[str]
            For usage monitors: the scope of aggregation. Supported values are "device" and "fleet".

        usage_type : typing.Optional[str]
            For usage monitors: the type of data usage to monitor. Supported values are "cellular" and "satellite".

        usage_window : typing.Optional[int]
            For usage monitors: the rolling time window in days to sum usage over (e.g. 30 for 30 days).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Monitor]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/monitors/{encode_path_param(monitor_uid)}",
            method="PUT",
            json={
                "aggregate_function": aggregate_function,
                "aggregate_window": aggregate_window,
                "alert": alert,
                "alert_routes": convert_and_respect_annotation_metadata(
                    object_=alert_routes, annotation=typing.Sequence[MonitorAlertRoutesItem], direction="write"
                ),
                "condition_type": condition_type,
                "description": description,
                "disabled": disabled,
                "fleet_filter": fleet_filter,
                "last_routed_at": last_routed_at,
                "name": name,
                "notefile_filter": notefile_filter,
                "per_device": per_device,
                "routing_cooldown_period": routing_cooldown_period,
                "silenced": silenced,
                "source_selector": source_selector,
                "source_type": source_type,
                "threshold": threshold,
                "uid": uid,
                "usage_scope": usage_scope,
                "usage_type": usage_type,
                "usage_window": usage_window,
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

    async def delete_monitor(
        self, project_or_product_uid: str, monitor_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Monitor]:
        """
        Delete Monitor

        Parameters
        ----------
        project_or_product_uid : str

        monitor_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Monitor]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/monitors/{encode_path_param(monitor_uid)}",
            method="DELETE",
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
