

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RemoteFailedEventStatus(enum.StrEnum):
    """
    The failure cause for event with failed status. This field is filled only is failure state.

    """

    GENERAL_ERROR = "GeneralError"
    VEHICLE_ERROR = "VehicleError"
    WRONG_COMMAND = "WrongCommand"
    VEHICLE_CONNECTION_TIMEOUT = "VehicleConnectionTimeout"
    MISSING_RIGHTS = "MissingRights"
    NOT_POSSIBLE_DUE_TO_VEHICLE_BATTERY_LEVEL = "NotPossibleDueToVehicleBatteryLevel"
    NOT_POSSIBLE_DUE_TO_VEHICLE_PRIVACY_LEVEL = "NotPossibleDueToVehiclePrivacyLevel"
    TOO_MANY_WAKE_UPS_OVER_MONTH = "TooManyWakeUpsOverMonth"
    TOO_MANY_REQUEST_IN_SHORT_TIME = "TooManyRequestInShortTime"
    SAME_ACTION_IN_PROGRESS = "SameActionInProgress"
    NOT_POSSIBLE_DUE_TO_VEHICLE_STOLEN_STATE = "NotPossibleDueToVehicleStolenState"
    VEHICLE_IN_USE = "VehicleInUse"
    TOO_MANY_REQUEST_SENT = "TooManyRequestSent"
    DOORS_OPEN = "DoorsOpen"
    VEHICLE_ERROR_OR_CID_INSIDE = "VehicleErrorOrCidInside"
    CID_INSIDE = "CidInside"
    EXTERNAL_CHARGING_SYSTEM_ERROR = "ExternalChargingSystemError"
    VEHICLE_CHARGING_SYSTEM_ERROR = "VehicleChargingSystemError"
    VEHICLE_IS_NOT_LOCKED = "VehicleIsNotLocked"
    CANCELED_BY_DRIVER = "CanceledByDriver"

    def visit(
        self,
        general_error: typing.Callable[[], T_Result],
        vehicle_error: typing.Callable[[], T_Result],
        wrong_command: typing.Callable[[], T_Result],
        vehicle_connection_timeout: typing.Callable[[], T_Result],
        missing_rights: typing.Callable[[], T_Result],
        not_possible_due_to_vehicle_battery_level: typing.Callable[[], T_Result],
        not_possible_due_to_vehicle_privacy_level: typing.Callable[[], T_Result],
        too_many_wake_ups_over_month: typing.Callable[[], T_Result],
        too_many_request_in_short_time: typing.Callable[[], T_Result],
        same_action_in_progress: typing.Callable[[], T_Result],
        not_possible_due_to_vehicle_stolen_state: typing.Callable[[], T_Result],
        vehicle_in_use: typing.Callable[[], T_Result],
        too_many_request_sent: typing.Callable[[], T_Result],
        doors_open: typing.Callable[[], T_Result],
        vehicle_error_or_cid_inside: typing.Callable[[], T_Result],
        cid_inside: typing.Callable[[], T_Result],
        external_charging_system_error: typing.Callable[[], T_Result],
        vehicle_charging_system_error: typing.Callable[[], T_Result],
        vehicle_is_not_locked: typing.Callable[[], T_Result],
        canceled_by_driver: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RemoteFailedEventStatus.GENERAL_ERROR:
            return general_error()
        if self is RemoteFailedEventStatus.VEHICLE_ERROR:
            return vehicle_error()
        if self is RemoteFailedEventStatus.WRONG_COMMAND:
            return wrong_command()
        if self is RemoteFailedEventStatus.VEHICLE_CONNECTION_TIMEOUT:
            return vehicle_connection_timeout()
        if self is RemoteFailedEventStatus.MISSING_RIGHTS:
            return missing_rights()
        if self is RemoteFailedEventStatus.NOT_POSSIBLE_DUE_TO_VEHICLE_BATTERY_LEVEL:
            return not_possible_due_to_vehicle_battery_level()
        if self is RemoteFailedEventStatus.NOT_POSSIBLE_DUE_TO_VEHICLE_PRIVACY_LEVEL:
            return not_possible_due_to_vehicle_privacy_level()
        if self is RemoteFailedEventStatus.TOO_MANY_WAKE_UPS_OVER_MONTH:
            return too_many_wake_ups_over_month()
        if self is RemoteFailedEventStatus.TOO_MANY_REQUEST_IN_SHORT_TIME:
            return too_many_request_in_short_time()
        if self is RemoteFailedEventStatus.SAME_ACTION_IN_PROGRESS:
            return same_action_in_progress()
        if self is RemoteFailedEventStatus.NOT_POSSIBLE_DUE_TO_VEHICLE_STOLEN_STATE:
            return not_possible_due_to_vehicle_stolen_state()
        if self is RemoteFailedEventStatus.VEHICLE_IN_USE:
            return vehicle_in_use()
        if self is RemoteFailedEventStatus.TOO_MANY_REQUEST_SENT:
            return too_many_request_sent()
        if self is RemoteFailedEventStatus.DOORS_OPEN:
            return doors_open()
        if self is RemoteFailedEventStatus.VEHICLE_ERROR_OR_CID_INSIDE:
            return vehicle_error_or_cid_inside()
        if self is RemoteFailedEventStatus.CID_INSIDE:
            return cid_inside()
        if self is RemoteFailedEventStatus.EXTERNAL_CHARGING_SYSTEM_ERROR:
            return external_charging_system_error()
        if self is RemoteFailedEventStatus.VEHICLE_CHARGING_SYSTEM_ERROR:
            return vehicle_charging_system_error()
        if self is RemoteFailedEventStatus.VEHICLE_IS_NOT_LOCKED:
            return vehicle_is_not_locked()
        if self is RemoteFailedEventStatus.CANCELED_BY_DRIVER:
            return canceled_by_driver()
