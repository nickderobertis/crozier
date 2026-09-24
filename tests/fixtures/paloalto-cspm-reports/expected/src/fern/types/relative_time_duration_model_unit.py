

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RelativeTimeDurationModelUnit(enum.StrEnum):
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
        if self is RelativeTimeDurationModelUnit.MINUTE:
            return minute()
        if self is RelativeTimeDurationModelUnit.HOUR:
            return hour()
        if self is RelativeTimeDurationModelUnit.DAY:
            return day()
        if self is RelativeTimeDurationModelUnit.WEEK:
            return week()
        if self is RelativeTimeDurationModelUnit.MONTH:
            return month()
        if self is RelativeTimeDurationModelUnit.YEAR:
            return year()
