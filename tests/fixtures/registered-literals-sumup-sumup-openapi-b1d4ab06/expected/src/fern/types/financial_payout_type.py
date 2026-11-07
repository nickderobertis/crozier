

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FinancialPayoutType(enum.StrEnum):
    """
    High-level payout record category.
    """

    PAYOUT = "PAYOUT"
    CHARGE_BACK_DEDUCTION = "CHARGE_BACK_DEDUCTION"
    REFUND_DEDUCTION = "REFUND_DEDUCTION"
    DD_RETURN_DEDUCTION = "DD_RETURN_DEDUCTION"
    BALANCE_DEDUCTION = "BALANCE_DEDUCTION"

    def visit(
        self,
        payout: typing.Callable[[], T_Result],
        charge_back_deduction: typing.Callable[[], T_Result],
        refund_deduction: typing.Callable[[], T_Result],
        dd_return_deduction: typing.Callable[[], T_Result],
        balance_deduction: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FinancialPayoutType.PAYOUT:
            return payout()
        if self is FinancialPayoutType.CHARGE_BACK_DEDUCTION:
            return charge_back_deduction()
        if self is FinancialPayoutType.REFUND_DEDUCTION:
            return refund_deduction()
        if self is FinancialPayoutType.DD_RETURN_DEDUCTION:
            return dd_return_deduction()
        if self is FinancialPayoutType.BALANCE_DEDUCTION:
            return balance_deduction()
