

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BankTransferType(enum.StrEnum):
    """
    The type of bank transfer. This will be either `debit` or `credit`.  A `debit` indicates a transfer of money into the origination account; a `credit` indicates a transfer of money out of the origination account.
    """

    DEBIT = "debit"
    CREDIT = "credit"

    def visit(self, debit: typing.Callable[[], T_Result], credit: typing.Callable[[], T_Result]) -> T_Result:
        if self is BankTransferType.DEBIT:
            return debit()
        if self is BankTransferType.CREDIT:
            return credit()
