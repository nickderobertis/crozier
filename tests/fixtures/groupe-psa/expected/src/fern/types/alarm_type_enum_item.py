

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AlarmTypeEnumItem(enum.StrEnum):
    VEHICLE_ALARM_STATUS = "vehicle.alarm.status"
    VEHICLE_ALARM_TRIGGER = "vehicle.alarm.trigger"

    def visit(
        self, vehicle_alarm_status: typing.Callable[[], T_Result], vehicle_alarm_trigger: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is AlarmTypeEnumItem.VEHICLE_ALARM_STATUS:
            return vehicle_alarm_status()
        if self is AlarmTypeEnumItem.VEHICLE_ALARM_TRIGGER:
            return vehicle_alarm_trigger()
