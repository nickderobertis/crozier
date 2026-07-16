

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConnectionScheduleTimeUnit(enum.StrEnum):
    MINUTES = "minutes"
    HOURS = "hours"
    DAYS = "days"
    WEEKS = "weeks"
    MONTHS = "months"

    def visit(
        self,
        minutes: typing.Callable[[], T_Result],
        hours: typing.Callable[[], T_Result],
        days: typing.Callable[[], T_Result],
        weeks: typing.Callable[[], T_Result],
        months: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConnectionScheduleTimeUnit.MINUTES:
            return minutes()
        if self is ConnectionScheduleTimeUnit.HOURS:
            return hours()
        if self is ConnectionScheduleTimeUnit.DAYS:
            return days()
        if self is ConnectionScheduleTimeUnit.WEEKS:
            return weeks()
        if self is ConnectionScheduleTimeUnit.MONTHS:
            return months()
