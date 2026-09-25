

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetAlertsV2RequestTimeUnit(enum.StrEnum):
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
        if self is GetAlertsV2RequestTimeUnit.MINUTE:
            return minute()
        if self is GetAlertsV2RequestTimeUnit.HOUR:
            return hour()
        if self is GetAlertsV2RequestTimeUnit.DAY:
            return day()
        if self is GetAlertsV2RequestTimeUnit.WEEK:
            return week()
        if self is GetAlertsV2RequestTimeUnit.MONTH:
            return month()
        if self is GetAlertsV2RequestTimeUnit.YEAR:
            return year()
