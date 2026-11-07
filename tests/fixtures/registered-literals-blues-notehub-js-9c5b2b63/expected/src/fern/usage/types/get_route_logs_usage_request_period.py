

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetRouteLogsUsageRequestPeriod(enum.StrEnum):
    DAY = "day"
    WEEK = "week"
    MONTH = "month"

    def visit(
        self,
        day: typing.Callable[[], T_Result],
        week: typing.Callable[[], T_Result],
        month: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetRouteLogsUsageRequestPeriod.DAY:
            return day()
        if self is GetRouteLogsUsageRequestPeriod.WEEK:
            return week()
        if self is GetRouteLogsUsageRequestPeriod.MONTH:
            return month()
