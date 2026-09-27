

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetFamilyBalancesV3RequestMetricsItem(enum.StrEnum):
    COUNT = "count"
    SUM_BALANCE = "sum_balance"
    AVG_BALANCE = "avg_balance"
    MIN_BALANCE = "min_balance"
    MAX_BALANCE = "max_balance"
    SUM_POSITIVE_BALANCE = "sum_positive_balance"
    SUM_NEGATIVE_BALANCE = "sum_negative_balance"
    COUNT_ZERO_BALANCE = "count_zero_balance"

    def visit(
        self,
        count: typing.Callable[[], T_Result],
        sum_balance: typing.Callable[[], T_Result],
        avg_balance: typing.Callable[[], T_Result],
        min_balance: typing.Callable[[], T_Result],
        max_balance: typing.Callable[[], T_Result],
        sum_positive_balance: typing.Callable[[], T_Result],
        sum_negative_balance: typing.Callable[[], T_Result],
        count_zero_balance: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetFamilyBalancesV3RequestMetricsItem.COUNT:
            return count()
        if self is GetFamilyBalancesV3RequestMetricsItem.SUM_BALANCE:
            return sum_balance()
        if self is GetFamilyBalancesV3RequestMetricsItem.AVG_BALANCE:
            return avg_balance()
        if self is GetFamilyBalancesV3RequestMetricsItem.MIN_BALANCE:
            return min_balance()
        if self is GetFamilyBalancesV3RequestMetricsItem.MAX_BALANCE:
            return max_balance()
        if self is GetFamilyBalancesV3RequestMetricsItem.SUM_POSITIVE_BALANCE:
            return sum_positive_balance()
        if self is GetFamilyBalancesV3RequestMetricsItem.SUM_NEGATIVE_BALANCE:
            return sum_negative_balance()
        if self is GetFamilyBalancesV3RequestMetricsItem.COUNT_ZERO_BALANCE:
            return count_zero_balance()
