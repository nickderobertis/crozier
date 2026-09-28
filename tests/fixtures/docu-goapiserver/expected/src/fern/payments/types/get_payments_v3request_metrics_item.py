

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetPaymentsV3RequestMetricsItem(enum.StrEnum):
    COUNT = "count"
    SUM_AMOUNT = "sum_amount"
    SUM_TOTAL_AMOUNT = "sum_total_amount"
    SUM_FEE_AMOUNT = "sum_fee_amount"
    AVG_AMOUNT = "avg_amount"
    AVG_TOTAL_AMOUNT = "avg_total_amount"
    AVG_FEE_AMOUNT = "avg_fee_amount"

    def visit(
        self,
        count: typing.Callable[[], T_Result],
        sum_amount: typing.Callable[[], T_Result],
        sum_total_amount: typing.Callable[[], T_Result],
        sum_fee_amount: typing.Callable[[], T_Result],
        avg_amount: typing.Callable[[], T_Result],
        avg_total_amount: typing.Callable[[], T_Result],
        avg_fee_amount: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetPaymentsV3RequestMetricsItem.COUNT:
            return count()
        if self is GetPaymentsV3RequestMetricsItem.SUM_AMOUNT:
            return sum_amount()
        if self is GetPaymentsV3RequestMetricsItem.SUM_TOTAL_AMOUNT:
            return sum_total_amount()
        if self is GetPaymentsV3RequestMetricsItem.SUM_FEE_AMOUNT:
            return sum_fee_amount()
        if self is GetPaymentsV3RequestMetricsItem.AVG_AMOUNT:
            return avg_amount()
        if self is GetPaymentsV3RequestMetricsItem.AVG_TOTAL_AMOUNT:
            return avg_total_amount()
        if self is GetPaymentsV3RequestMetricsItem.AVG_FEE_AMOUNT:
            return avg_fee_amount()
