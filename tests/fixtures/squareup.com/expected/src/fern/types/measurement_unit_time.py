

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class MeasurementUnitTime(str, enum.Enum):
    """
    Unit of time used to measure a quantity (a duration).
    """

    GENERIC_MILLISECOND = "GENERIC_MILLISECOND"
    GENERIC_SECOND = "GENERIC_SECOND"
    GENERIC_MINUTE = "GENERIC_MINUTE"
    GENERIC_HOUR = "GENERIC_HOUR"
    GENERIC_DAY = "GENERIC_DAY"

    def visit(
        self,
        generic_millisecond: typing.Callable[[], T_Result],
        generic_second: typing.Callable[[], T_Result],
        generic_minute: typing.Callable[[], T_Result],
        generic_hour: typing.Callable[[], T_Result],
        generic_day: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MeasurementUnitTime.GENERIC_MILLISECOND:
            return generic_millisecond()
        if self is MeasurementUnitTime.GENERIC_SECOND:
            return generic_second()
        if self is MeasurementUnitTime.GENERIC_MINUTE:
            return generic_minute()
        if self is MeasurementUnitTime.GENERIC_HOUR:
            return generic_hour()
        if self is MeasurementUnitTime.GENERIC_DAY:
            return generic_day()
