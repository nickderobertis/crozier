

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AmfEventType(enum.StrEnum):
    LOCATION_REPORT = "LOCATION_REPORT"
    PRESENCE_IN_AOI_REPORT = "PRESENCE_IN_AOI_REPORT"
    TIMEZONE_REPORT = "TIMEZONE_REPORT"
    ACCESS_TYPE_REPORT = "ACCESS_TYPE_REPORT"
    REGISTRATION_STATE_REPORT = "REGISTRATION_STATE_REPORT"
    CONNECTIVITY_STATE_REPORT = "CONNECTIVITY_STATE_REPORT"
    REACHABILITY_REPORT = "REACHABILITY_REPORT"
    SUBSCRIBED_DATA_REPORT = "SUBSCRIBED_DATA_REPORT"
    COMMUNICATION_FAILURE_REPORT = "COMMUNICATION_FAILURE_REPORT"
    UES_IN_AREA_REPORT = "UES_IN_AREA_REPORT"
    SUBSCRIPTION_ID_CHANGE = "SUBSCRIPTION_ID_CHANGE"
    SUBSCRIPTION_ID_ADDITION = "SUBSCRIPTION_ID_ADDITION"

    def visit(
        self,
        location_report: typing.Callable[[], T_Result],
        presence_in_aoi_report: typing.Callable[[], T_Result],
        timezone_report: typing.Callable[[], T_Result],
        access_type_report: typing.Callable[[], T_Result],
        registration_state_report: typing.Callable[[], T_Result],
        connectivity_state_report: typing.Callable[[], T_Result],
        reachability_report: typing.Callable[[], T_Result],
        subscribed_data_report: typing.Callable[[], T_Result],
        communication_failure_report: typing.Callable[[], T_Result],
        ues_in_area_report: typing.Callable[[], T_Result],
        subscription_id_change: typing.Callable[[], T_Result],
        subscription_id_addition: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AmfEventType.LOCATION_REPORT:
            return location_report()
        if self is AmfEventType.PRESENCE_IN_AOI_REPORT:
            return presence_in_aoi_report()
        if self is AmfEventType.TIMEZONE_REPORT:
            return timezone_report()
        if self is AmfEventType.ACCESS_TYPE_REPORT:
            return access_type_report()
        if self is AmfEventType.REGISTRATION_STATE_REPORT:
            return registration_state_report()
        if self is AmfEventType.CONNECTIVITY_STATE_REPORT:
            return connectivity_state_report()
        if self is AmfEventType.REACHABILITY_REPORT:
            return reachability_report()
        if self is AmfEventType.SUBSCRIBED_DATA_REPORT:
            return subscribed_data_report()
        if self is AmfEventType.COMMUNICATION_FAILURE_REPORT:
            return communication_failure_report()
        if self is AmfEventType.UES_IN_AREA_REPORT:
            return ues_in_area_report()
        if self is AmfEventType.SUBSCRIPTION_ID_CHANGE:
            return subscription_id_change()
        if self is AmfEventType.SUBSCRIPTION_ID_ADDITION:
            return subscription_id_addition()
