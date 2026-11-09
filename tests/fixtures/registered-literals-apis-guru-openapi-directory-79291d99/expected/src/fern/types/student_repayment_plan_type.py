

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StudentRepaymentPlanType(enum.StrEnum):
    """
    The type of the repayment plan.
    """

    EXTENDED_GRADUATED = "extended graduated"
    EXTENDED_STANDARD = "extended standard"
    GRADUATED = "graduated"
    INCOME_CONTINGENT_REPAYMENT = "income-contingent repayment"
    INCOME_BASED_REPAYMENT = "income-based repayment"
    INTEREST_ONLY = "interest-only"
    OTHER = "other"
    PAY_AS_YOU_EARN = "pay as you earn"
    REVISED_PAY_AS_YOU_EARN = "revised pay as you earn"
    STANDARD = "standard"

    def visit(
        self,
        extended_graduated: typing.Callable[[], T_Result],
        extended_standard: typing.Callable[[], T_Result],
        graduated: typing.Callable[[], T_Result],
        income_contingent_repayment: typing.Callable[[], T_Result],
        income_based_repayment: typing.Callable[[], T_Result],
        interest_only: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
        pay_as_you_earn: typing.Callable[[], T_Result],
        revised_pay_as_you_earn: typing.Callable[[], T_Result],
        standard: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StudentRepaymentPlanType.EXTENDED_GRADUATED:
            return extended_graduated()
        if self is StudentRepaymentPlanType.EXTENDED_STANDARD:
            return extended_standard()
        if self is StudentRepaymentPlanType.GRADUATED:
            return graduated()
        if self is StudentRepaymentPlanType.INCOME_CONTINGENT_REPAYMENT:
            return income_contingent_repayment()
        if self is StudentRepaymentPlanType.INCOME_BASED_REPAYMENT:
            return income_based_repayment()
        if self is StudentRepaymentPlanType.INTEREST_ONLY:
            return interest_only()
        if self is StudentRepaymentPlanType.OTHER:
            return other()
        if self is StudentRepaymentPlanType.PAY_AS_YOU_EARN:
            return pay_as_you_earn()
        if self is StudentRepaymentPlanType.REVISED_PAY_AS_YOU_EARN:
            return revised_pay_as_you_earn()
        if self is StudentRepaymentPlanType.STANDARD:
            return standard()
