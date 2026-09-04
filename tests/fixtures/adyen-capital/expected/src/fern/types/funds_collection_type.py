

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FundsCollectionType(enum.StrEnum):
    UNSCHEDULED_REPAYMENT = "UnscheduledRepayment"
    REVOCATION = "Revocation"

    def visit(
        self, unscheduled_repayment: typing.Callable[[], T_Result], revocation: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is FundsCollectionType.UNSCHEDULED_REPAYMENT:
            return unscheduled_repayment()
        if self is FundsCollectionType.REVOCATION:
            return revocation()
