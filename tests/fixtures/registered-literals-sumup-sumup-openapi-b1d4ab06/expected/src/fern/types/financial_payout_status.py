

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FinancialPayoutStatus(enum.StrEnum):
    """
    Merchant-facing outcome of the payout record.
    """

    SUCCESSFUL = "SUCCESSFUL"
    FAILED = "FAILED"

    def visit(self, successful: typing.Callable[[], T_Result], failed: typing.Callable[[], T_Result]) -> T_Result:
        if self is FinancialPayoutStatus.SUCCESSFUL:
            return successful()
        if self is FinancialPayoutStatus.FAILED:
            return failed()
