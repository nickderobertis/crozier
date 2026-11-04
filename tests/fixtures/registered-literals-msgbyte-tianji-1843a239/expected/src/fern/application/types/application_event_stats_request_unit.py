

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ApplicationEventStatsRequestUnit(enum.StrEnum):
    MINUTE = "minute"
    HOUR = "hour"
    DAY = "day"
    MONTH = "month"
    YEAR = "year"

    def visit(
        self,
        minute: typing.Callable[[], T_Result],
        hour: typing.Callable[[], T_Result],
        day: typing.Callable[[], T_Result],
        month: typing.Callable[[], T_Result],
        year: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ApplicationEventStatsRequestUnit.MINUTE:
            return minute()
        if self is ApplicationEventStatsRequestUnit.HOUR:
            return hour()
        if self is ApplicationEventStatsRequestUnit.DAY:
            return day()
        if self is ApplicationEventStatsRequestUnit.MONTH:
            return month()
        if self is ApplicationEventStatsRequestUnit.YEAR:
            return year()
