

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetSessionsUsageRequestPeriod(enum.StrEnum):
    DAY = "day"
    WEEK = "week"
    MONTH = "month"

    def visit(
        self,
        day: typing.Callable[[], T_Result],
        week: typing.Callable[[], T_Result],
        month: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetSessionsUsageRequestPeriod.DAY:
            return day()
        if self is GetSessionsUsageRequestPeriod.WEEK:
            return week()
        if self is GetSessionsUsageRequestPeriod.MONTH:
            return month()
