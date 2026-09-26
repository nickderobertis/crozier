

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PreconditioningBaseAirConditioningFailureCause(enum.StrEnum):
    """
    failure cause
    """

    DEFECT = "Defect"
    DOOR_OPENED = "DoorOpened"
    LOW_BATTERY = "LowBattery"
    LOW_FUEL_LEVEL = "LowFuelLevel"
    TOO_MANY_UNUSED_PROG = "TooManyUnusedProg"
    WINDOWS_ROOF_OPENED = "WindowsRoofOpened"
    HOOD_OPENED = "HoodOpened"
    NOT_PARKED = "NotParked"
    OTHER_FAILURES = "OtherFailures"

    def visit(
        self,
        defect: typing.Callable[[], T_Result],
        door_opened: typing.Callable[[], T_Result],
        low_battery: typing.Callable[[], T_Result],
        low_fuel_level: typing.Callable[[], T_Result],
        too_many_unused_prog: typing.Callable[[], T_Result],
        windows_roof_opened: typing.Callable[[], T_Result],
        hood_opened: typing.Callable[[], T_Result],
        not_parked: typing.Callable[[], T_Result],
        other_failures: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PreconditioningBaseAirConditioningFailureCause.DEFECT:
            return defect()
        if self is PreconditioningBaseAirConditioningFailureCause.DOOR_OPENED:
            return door_opened()
        if self is PreconditioningBaseAirConditioningFailureCause.LOW_BATTERY:
            return low_battery()
        if self is PreconditioningBaseAirConditioningFailureCause.LOW_FUEL_LEVEL:
            return low_fuel_level()
        if self is PreconditioningBaseAirConditioningFailureCause.TOO_MANY_UNUSED_PROG:
            return too_many_unused_prog()
        if self is PreconditioningBaseAirConditioningFailureCause.WINDOWS_ROOF_OPENED:
            return windows_roof_opened()
        if self is PreconditioningBaseAirConditioningFailureCause.HOOD_OPENED:
            return hood_opened()
        if self is PreconditioningBaseAirConditioningFailureCause.NOT_PARKED:
            return not_parked()
        if self is PreconditioningBaseAirConditioningFailureCause.OTHER_FAILURES:
            return other_failures()
