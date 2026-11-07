

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionEventType(enum.StrEnum):
    """
    Type of the transaction event.
    """

    PAYOUT = "PAYOUT"
    CHARGE_BACK = "CHARGE_BACK"
    REFUND = "REFUND"
    PAYOUT_DEDUCTION = "PAYOUT_DEDUCTION"

    def visit(
        self,
        payout: typing.Callable[[], T_Result],
        charge_back: typing.Callable[[], T_Result],
        refund: typing.Callable[[], T_Result],
        payout_deduction: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TransactionEventType.PAYOUT:
            return payout()
        if self is TransactionEventType.CHARGE_BACK:
            return charge_back()
        if self is TransactionEventType.REFUND:
            return refund()
        if self is TransactionEventType.PAYOUT_DEDUCTION:
            return payout_deduction()
