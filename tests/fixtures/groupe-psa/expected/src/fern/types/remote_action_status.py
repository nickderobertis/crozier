

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RemoteActionStatus(enum.StrEnum):
    ACCEPTED = "Accepted"
    FAILED = "Failed"
    SUCCESS = "Success"
    ALREADY_DONE = "AlreadyDone"
    WAKING_UP_VEHICLE = "WakingUpVehicle"
    CHECKING_VEHICLE = "CheckingVehicle"
    SENT_TO_VEHICLE = "SentToVehicle"
    VEHICLE_BATTERY_CHARGE_TOO_LOW = "VehicleBatteryChargeTooLow"
    TOO_MANY_WAKE_UPS_OVER_MONTH = "TooManyWakeUpsOverMonth"

    def visit(
        self,
        accepted: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        success: typing.Callable[[], T_Result],
        already_done: typing.Callable[[], T_Result],
        waking_up_vehicle: typing.Callable[[], T_Result],
        checking_vehicle: typing.Callable[[], T_Result],
        sent_to_vehicle: typing.Callable[[], T_Result],
        vehicle_battery_charge_too_low: typing.Callable[[], T_Result],
        too_many_wake_ups_over_month: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RemoteActionStatus.ACCEPTED:
            return accepted()
        if self is RemoteActionStatus.FAILED:
            return failed()
        if self is RemoteActionStatus.SUCCESS:
            return success()
        if self is RemoteActionStatus.ALREADY_DONE:
            return already_done()
        if self is RemoteActionStatus.WAKING_UP_VEHICLE:
            return waking_up_vehicle()
        if self is RemoteActionStatus.CHECKING_VEHICLE:
            return checking_vehicle()
        if self is RemoteActionStatus.SENT_TO_VEHICLE:
            return sent_to_vehicle()
        if self is RemoteActionStatus.VEHICLE_BATTERY_CHARGE_TOO_LOW:
            return vehicle_battery_charge_too_low()
        if self is RemoteActionStatus.TOO_MANY_WAKE_UPS_OVER_MONTH:
            return too_many_wake_ups_over_month()
