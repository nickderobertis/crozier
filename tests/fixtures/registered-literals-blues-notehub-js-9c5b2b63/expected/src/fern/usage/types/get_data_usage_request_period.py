

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetDataUsageRequestPeriod(enum.StrEnum):
    DAY = "day"
    WEEK = "week"
    MONTH = "month"

    def visit(
        self,
        day: typing.Callable[[], T_Result],
        week: typing.Callable[[], T_Result],
        month: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetDataUsageRequestPeriod.DAY:
            return day()
        if self is GetDataUsageRequestPeriod.WEEK:
            return week()
        if self is GetDataUsageRequestPeriod.MONTH:
            return month()
