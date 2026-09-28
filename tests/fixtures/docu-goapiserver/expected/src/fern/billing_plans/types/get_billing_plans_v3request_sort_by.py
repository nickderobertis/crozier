

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetBillingPlansV3RequestSortBy(enum.StrEnum):
    SUM_MONTHLY_INVOICE_ASC = "sum_monthly_invoice_asc"
    SUM_MONTHLY_INVOICE_DESC = "sum_monthly_invoice_desc"
    AVG_MONTHLY_INVOICE_ASC = "avg_monthly_invoice_asc"
    AVG_MONTHLY_INVOICE_DESC = "avg_monthly_invoice_desc"
    COUNT_STUDENTS_ASC = "count_students_asc"
    COUNT_STUDENTS_DESC = "count_students_desc"
    GROUP_ASC = "group_asc"
    GROUP_DESC = "group_desc"

    def visit(
        self,
        sum_monthly_invoice_asc: typing.Callable[[], T_Result],
        sum_monthly_invoice_desc: typing.Callable[[], T_Result],
        avg_monthly_invoice_asc: typing.Callable[[], T_Result],
        avg_monthly_invoice_desc: typing.Callable[[], T_Result],
        count_students_asc: typing.Callable[[], T_Result],
        count_students_desc: typing.Callable[[], T_Result],
        group_asc: typing.Callable[[], T_Result],
        group_desc: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetBillingPlansV3RequestSortBy.SUM_MONTHLY_INVOICE_ASC:
            return sum_monthly_invoice_asc()
        if self is GetBillingPlansV3RequestSortBy.SUM_MONTHLY_INVOICE_DESC:
            return sum_monthly_invoice_desc()
        if self is GetBillingPlansV3RequestSortBy.AVG_MONTHLY_INVOICE_ASC:
            return avg_monthly_invoice_asc()
        if self is GetBillingPlansV3RequestSortBy.AVG_MONTHLY_INVOICE_DESC:
            return avg_monthly_invoice_desc()
        if self is GetBillingPlansV3RequestSortBy.COUNT_STUDENTS_ASC:
            return count_students_asc()
        if self is GetBillingPlansV3RequestSortBy.COUNT_STUDENTS_DESC:
            return count_students_desc()
        if self is GetBillingPlansV3RequestSortBy.GROUP_ASC:
            return group_asc()
        if self is GetBillingPlansV3RequestSortBy.GROUP_DESC:
            return group_desc()
