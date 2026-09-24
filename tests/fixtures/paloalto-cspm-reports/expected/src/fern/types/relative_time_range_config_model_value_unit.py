

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RelativeTimeRangeConfigModelValueUnit(enum.StrEnum):
    """
    Time unit
    """

    MINUTE = "minute"
    HOUR = "hour"
    DAY = "day"
    WEEK = "week"
    MONTH = "month"
    YEAR = "year"

    def visit(
        self,
        minute: typing.Callable[[], T_Result],
        hour: typing.Callable[[], T_Result],
        day: typing.Callable[[], T_Result],
        week: typing.Callable[[], T_Result],
        month: typing.Callable[[], T_Result],
        year: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RelativeTimeRangeConfigModelValueUnit.MINUTE:
            return minute()
        if self is RelativeTimeRangeConfigModelValueUnit.HOUR:
            return hour()
        if self is RelativeTimeRangeConfigModelValueUnit.DAY:
            return day()
        if self is RelativeTimeRangeConfigModelValueUnit.WEEK:
            return week()
        if self is RelativeTimeRangeConfigModelValueUnit.MONTH:
            return month()
        if self is RelativeTimeRangeConfigModelValueUnit.YEAR:
            return year()
