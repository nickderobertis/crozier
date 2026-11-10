

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StudentLoanStatusType(enum.StrEnum):
    """
    The status type of the student loan
    """

    CANCELLED = "cancelled"
    CHARGED_OFF = "charged off"
    CLAIM = "claim"
    CONSOLIDATED = "consolidated"
    DEFERMENT = "deferment"
    DELINQUENT = "delinquent"
    DISCHARGED = "discharged"
    EXTENSION = "extension"
    FORBEARANCE = "forbearance"
    IN_GRACE = "in grace"
    IN_MILITARY = "in military"
    IN_SCHOOL = "in school"
    NOT_FULLY_DISBURSED = "not fully disbursed"
    OTHER = "other"
    PAID_IN_FULL = "paid in full"
    REFUNDED = "refunded"
    REPAYMENT = "repayment"
    TRANSFERRED = "transferred"

    def visit(
        self,
        cancelled: typing.Callable[[], T_Result],
        charged_off: typing.Callable[[], T_Result],
        claim: typing.Callable[[], T_Result],
        consolidated: typing.Callable[[], T_Result],
        deferment: typing.Callable[[], T_Result],
        delinquent: typing.Callable[[], T_Result],
        discharged: typing.Callable[[], T_Result],
        extension: typing.Callable[[], T_Result],
        forbearance: typing.Callable[[], T_Result],
        in_grace: typing.Callable[[], T_Result],
        in_military: typing.Callable[[], T_Result],
        in_school: typing.Callable[[], T_Result],
        not_fully_disbursed: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
        paid_in_full: typing.Callable[[], T_Result],
        refunded: typing.Callable[[], T_Result],
        repayment: typing.Callable[[], T_Result],
        transferred: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StudentLoanStatusType.CANCELLED:
            return cancelled()
        if self is StudentLoanStatusType.CHARGED_OFF:
            return charged_off()
        if self is StudentLoanStatusType.CLAIM:
            return claim()
        if self is StudentLoanStatusType.CONSOLIDATED:
            return consolidated()
        if self is StudentLoanStatusType.DEFERMENT:
            return deferment()
        if self is StudentLoanStatusType.DELINQUENT:
            return delinquent()
        if self is StudentLoanStatusType.DISCHARGED:
            return discharged()
        if self is StudentLoanStatusType.EXTENSION:
            return extension()
        if self is StudentLoanStatusType.FORBEARANCE:
            return forbearance()
        if self is StudentLoanStatusType.IN_GRACE:
            return in_grace()
        if self is StudentLoanStatusType.IN_MILITARY:
            return in_military()
        if self is StudentLoanStatusType.IN_SCHOOL:
            return in_school()
        if self is StudentLoanStatusType.NOT_FULLY_DISBURSED:
            return not_fully_disbursed()
        if self is StudentLoanStatusType.OTHER:
            return other()
        if self is StudentLoanStatusType.PAID_IN_FULL:
            return paid_in_full()
        if self is StudentLoanStatusType.REFUNDED:
            return refunded()
        if self is StudentLoanStatusType.REPAYMENT:
            return repayment()
        if self is StudentLoanStatusType.TRANSFERRED:
            return transferred()
