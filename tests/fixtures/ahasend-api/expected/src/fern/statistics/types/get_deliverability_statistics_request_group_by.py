

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetDeliverabilityStatisticsRequestGroupBy(enum.StrEnum):
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
        if self is GetDeliverabilityStatisticsRequestGroupBy.HOUR:
            return hour()
        if self is GetDeliverabilityStatisticsRequestGroupBy.DAY:
            return day()
        if self is GetDeliverabilityStatisticsRequestGroupBy.WEEK:
            return week()
        if self is GetDeliverabilityStatisticsRequestGroupBy.MONTH:
            return month()
