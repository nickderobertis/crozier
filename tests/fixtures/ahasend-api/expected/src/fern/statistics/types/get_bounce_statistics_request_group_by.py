

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetBounceStatisticsRequestGroupBy(enum.StrEnum):
    HOUR = "hour"
    DAY = "day"
    WEEK = "week"
    MONTH = "month"

    def visit(
        self,
        hour: typing.Callable[[], T_Result],
        day: typing.Callable[[], T_Result],
        week: typing.Callable[[], T_Result],
        month: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetBounceStatisticsRequestGroupBy.HOUR:
            return hour()
        if self is GetBounceStatisticsRequestGroupBy.DAY:
            return day()
        if self is GetBounceStatisticsRequestGroupBy.WEEK:
            return week()
        if self is GetBounceStatisticsRequestGroupBy.MONTH:
            return month()
