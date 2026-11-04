

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionFullProcessAs(enum.StrEnum):
    """
    Whether the transaction was processed as credit or debit.
    """

    CREDIT = "CREDIT"
    DEBIT = "DEBIT"

    def visit(self, credit: typing.Callable[[], T_Result], debit: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionFullProcessAs.CREDIT:
            return credit()
        if self is TransactionFullProcessAs.DEBIT:
            return debit()
