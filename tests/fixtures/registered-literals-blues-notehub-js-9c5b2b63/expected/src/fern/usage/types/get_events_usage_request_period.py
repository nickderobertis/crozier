

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsUsageRequestPeriod(enum.StrEnum):
    DAY = "day"
    WEEK = "week"
    MONTH = "month"

    def visit(
        self,
        day: typing.Callable[[], T_Result],
        week: typing.Callable[[], T_Result],
        month: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetEventsUsageRequestPeriod.DAY:
            return day()
        if self is GetEventsUsageRequestPeriod.WEEK:
            return week()
        if self is GetEventsUsageRequestPeriod.MONTH:
            return month()
