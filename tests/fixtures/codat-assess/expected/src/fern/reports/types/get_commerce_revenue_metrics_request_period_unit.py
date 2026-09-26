

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetCommerceRevenueMetricsRequestPeriodUnit(enum.StrEnum):
    DAY = "Day"
    WEEK = "Week"
    MONTH = "Month"
    YEAR = "Year"

    def visit(
        self,
        day: typing.Callable[[], T_Result],
        week: typing.Callable[[], T_Result],
        month: typing.Callable[[], T_Result],
        year: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetCommerceRevenueMetricsRequestPeriodUnit.DAY:
            return day()
        if self is GetCommerceRevenueMetricsRequestPeriodUnit.WEEK:
            return week()
        if self is GetCommerceRevenueMetricsRequestPeriodUnit.MONTH:
            return month()
        if self is GetCommerceRevenueMetricsRequestPeriodUnit.YEAR:
            return year()
