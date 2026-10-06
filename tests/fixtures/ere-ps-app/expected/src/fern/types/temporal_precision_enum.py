

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TemporalPrecisionEnum(enum.StrEnum):
    YEAR = "YEAR"
    MONTH = "MONTH"
    DAY = "DAY"
    MINUTE = "MINUTE"
    SECOND = "SECOND"
    MILLI = "MILLI"

    def visit(
        self,
        year: typing.Callable[[], T_Result],
        month: typing.Callable[[], T_Result],
        day: typing.Callable[[], T_Result],
        minute: typing.Callable[[], T_Result],
        second: typing.Callable[[], T_Result],
        milli: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TemporalPrecisionEnum.YEAR:
            return year()
        if self is TemporalPrecisionEnum.MONTH:
            return month()
        if self is TemporalPrecisionEnum.DAY:
            return day()
        if self is TemporalPrecisionEnum.MINUTE:
            return minute()
        if self is TemporalPrecisionEnum.SECOND:
            return second()
        if self is TemporalPrecisionEnum.MILLI:
            return milli()
