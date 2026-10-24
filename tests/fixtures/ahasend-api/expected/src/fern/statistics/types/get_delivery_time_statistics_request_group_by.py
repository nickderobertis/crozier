

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetDeliveryTimeStatisticsRequestGroupBy(enum.StrEnum):
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
        if self is GetDeliveryTimeStatisticsRequestGroupBy.HOUR:
            return hour()
        if self is GetDeliveryTimeStatisticsRequestGroupBy.DAY:
            return day()
        if self is GetDeliveryTimeStatisticsRequestGroupBy.WEEK:
            return week()
        if self is GetDeliveryTimeStatisticsRequestGroupBy.MONTH:
            return month()
