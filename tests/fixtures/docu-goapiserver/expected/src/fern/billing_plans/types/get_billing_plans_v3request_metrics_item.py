

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetBillingPlansV3RequestMetricsItem(enum.StrEnum):
    SUM_MONTHLY_INVOICE = "sum_monthly_invoice"
    AVG_MONTHLY_INVOICE = "avg_monthly_invoice"
    COUNT_STUDENTS = "count_students"

    def visit(
        self,
        sum_monthly_invoice: typing.Callable[[], T_Result],
        avg_monthly_invoice: typing.Callable[[], T_Result],
        count_students: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetBillingPlansV3RequestMetricsItem.SUM_MONTHLY_INVOICE:
            return sum_monthly_invoice()
        if self is GetBillingPlansV3RequestMetricsItem.AVG_MONTHLY_INVOICE:
            return avg_monthly_invoice()
        if self is GetBillingPlansV3RequestMetricsItem.COUNT_STUDENTS:
            return count_students()
