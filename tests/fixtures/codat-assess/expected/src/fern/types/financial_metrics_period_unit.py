

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FinancialMetricsPeriodUnit(enum.StrEnum):
    MONTH = "Month"
    WEEK = "Week"
    DAY = "Day"

    def visit(
        self,
        month: typing.Callable[[], T_Result],
        week: typing.Callable[[], T_Result],
        day: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FinancialMetricsPeriodUnit.MONTH:
            return month()
        if self is FinancialMetricsPeriodUnit.WEEK:
            return week()
        if self is FinancialMetricsPeriodUnit.DAY:
            return day()
