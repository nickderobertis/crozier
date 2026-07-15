

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ConnectionScheduleDataBasicScheduleTimeUnit(str, enum.Enum):
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
        if self is ConnectionScheduleDataBasicScheduleTimeUnit.MINUTES:
            return minutes()
        if self is ConnectionScheduleDataBasicScheduleTimeUnit.HOURS:
            return hours()
        if self is ConnectionScheduleDataBasicScheduleTimeUnit.DAYS:
            return days()
        if self is ConnectionScheduleDataBasicScheduleTimeUnit.WEEKS:
            return weeks()
        if self is ConnectionScheduleDataBasicScheduleTimeUnit.MONTHS:
            return months()
