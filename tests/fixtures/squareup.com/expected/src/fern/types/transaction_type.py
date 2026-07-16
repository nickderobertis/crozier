

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionType(enum.StrEnum):
    """
    The transaction type used in the disputed payment.
    """

    DEBIT = "DEBIT"
    CREDIT = "CREDIT"

    def visit(self, debit: typing.Callable[[], T_Result], credit: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionType.DEBIT:
            return debit()
        if self is TransactionType.CREDIT:
            return credit()
