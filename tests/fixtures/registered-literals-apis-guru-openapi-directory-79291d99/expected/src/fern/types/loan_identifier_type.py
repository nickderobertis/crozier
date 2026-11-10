

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LoanIdentifierType(enum.StrEnum):
    """
    A value from a MISMO prescribed list that specifies the type of loan identifier.
    """

    LENDER_LOAN = "LenderLoan"
    UNIVERSAL_LOAN = "UniversalLoan"

    def visit(
        self, lender_loan: typing.Callable[[], T_Result], universal_loan: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is LoanIdentifierType.LENDER_LOAN:
            return lender_loan()
        if self is LoanIdentifierType.UNIVERSAL_LOAN:
            return universal_loan()
