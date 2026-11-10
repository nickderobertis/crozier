

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IncomeVerificationPayrollFlowType(enum.StrEnum):
    """
    Flow types to retrieve payroll income data
    """

    PAYROLL_DIGITAL_INCOME = "payroll_digital_income"
    PAYROLL_DOCUMENT_INCOME = "payroll_document_income"

    def visit(
        self,
        payroll_digital_income: typing.Callable[[], T_Result],
        payroll_document_income: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IncomeVerificationPayrollFlowType.PAYROLL_DIGITAL_INCOME:
            return payroll_digital_income()
        if self is IncomeVerificationPayrollFlowType.PAYROLL_DOCUMENT_INCOME:
            return payroll_document_income()
