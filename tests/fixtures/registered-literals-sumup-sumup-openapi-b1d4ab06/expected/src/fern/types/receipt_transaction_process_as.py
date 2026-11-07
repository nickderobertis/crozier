

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReceiptTransactionProcessAs(enum.StrEnum):
    """
    Whether the transaction was processed as credit or debit.
    """

    CREDIT = "CREDIT"
    DEBIT = "DEBIT"

    def visit(self, credit: typing.Callable[[], T_Result], debit: typing.Callable[[], T_Result]) -> T_Result:
        if self is ReceiptTransactionProcessAs.CREDIT:
            return credit()
        if self is ReceiptTransactionProcessAs.DEBIT:
            return debit()
