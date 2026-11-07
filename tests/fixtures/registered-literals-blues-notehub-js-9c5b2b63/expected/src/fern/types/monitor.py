

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .monitor_aggregate_function import MonitorAggregateFunction
from .monitor_alert_routes_item import MonitorAlertRoutesItem
from .monitor_condition_type import MonitorConditionType
from .monitor_source_type import MonitorSourceType


class Monitor(UniversalBaseModel):
    aggregate_function: typing.Optional[MonitorAggregateFunction] = pydantic.Field(default=None)
    """
    Aggregate function to apply to the selected values before applying the condition. [none, sum, average, max, min]
    """

    aggregate_window: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time window to aggregate the selected values. It follows the format of a number followed by a time unit
    """

    alert: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, the monitor is in alert state.
    """

    alert_routes: typing.Optional[typing.List[MonitorAlertRoutesItem]] = None
    condition_type: typing.Optional[MonitorConditionType] = pydantic.Field(default=None)
    """
    A comparison operation to apply to the value selected by the source_selector [greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to]
    """

    description: typing.Optional[str] = None
    disabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, the monitor will not be evaluated.
    """

    fleet_filter: typing.Optional[typing.List[str]] = None
    last_routed_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The last time the monitor was evaluated and routed.
    """

    name: typing.Optional[str] = None
    notefile_filter: typing.Optional[typing.List[str]] = None
    per_device: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Only relevant when using an aggregate_function. If true, the monitor will be evaluated per device, | rather than across the set of selected devices. If true then if a single device matches the specified criteria, | and alert will be created, otherwise the aggregate function will be applied across all devices.
    """

    routing_cooldown_period: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time period to wait before routing another event after the monitor | has been triggered. It follows the format of a number followed by a time unit.
    """

    silenced: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, alerts will be created, but no notifications will be sent.
    """

    source_selector: typing.Optional[str] = pydantic.Field(default=None)
    """
    A valid JSONata expression that selects the value to monitor from the source. | It should return a single, numeric value.
    """

    source_type: typing.Optional[MonitorSourceType] = pydantic.Field(default=None)
    """
    The type of source to monitor. Supported values are "event" and "heartbeat".
    """

    threshold: typing.Optional[int] = pydantic.Field(default=None)
    """
    The type of condition to apply to the value selected by the source_selector
    """

    uid: typing.Optional[str] = None
    usage_scope: typing.Optional[str] = pydantic.Field(default=None)
    """
    For usage monitors: the scope of aggregation. Supported values are "device" and "fleet".
    """

    usage_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    For usage monitors: the type of data usage to monitor. Supported values are "cellular" and "satellite".
    """

    usage_window: typing.Optional[int] = pydantic.Field(default=None)
    """
    For usage monitors: the rolling time window in days to sum usage over (e.g. 30 for 30 days).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
