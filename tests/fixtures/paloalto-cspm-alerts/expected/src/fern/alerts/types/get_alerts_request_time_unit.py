

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetAlertsRequestTimeUnit(enum.StrEnum):
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
        if self is GetAlertsRequestTimeUnit.MINUTE:
            return minute()
        if self is GetAlertsRequestTimeUnit.HOUR:
            return hour()
        if self is GetAlertsRequestTimeUnit.DAY:
            return day()
        if self is GetAlertsRequestTimeUnit.WEEK:
            return week()
        if self is GetAlertsRequestTimeUnit.MONTH:
            return month()
        if self is GetAlertsRequestTimeUnit.YEAR:
            return year()
