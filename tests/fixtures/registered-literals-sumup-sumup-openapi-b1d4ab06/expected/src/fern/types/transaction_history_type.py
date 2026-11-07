

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionHistoryType(enum.StrEnum):
    """
    Type of the transaction for the registered user specified in the `user` property.
    """

    PAYMENT = "PAYMENT"
    REFUND = "REFUND"
    CHARGE_BACK = "CHARGE_BACK"

    def visit(
        self,
        payment: typing.Callable[[], T_Result],
        refund: typing.Callable[[], T_Result],
        charge_back: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TransactionHistoryType.PAYMENT:
            return payment()
        if self is TransactionHistoryType.REFUND:
            return refund()
        if self is TransactionHistoryType.CHARGE_BACK:
            return charge_back()
