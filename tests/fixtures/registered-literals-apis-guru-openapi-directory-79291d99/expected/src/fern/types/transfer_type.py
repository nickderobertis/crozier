

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransferType(enum.StrEnum):
    """
    The type of transfer. This will be either `debit` or `credit`.  A `debit` indicates a transfer of money into the origination account; a `credit` indicates a transfer of money out of the origination account.
    """

    DEBIT = "debit"
    CREDIT = "credit"

    def visit(self, debit: typing.Callable[[], T_Result], credit: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransferType.DEBIT:
            return debit()
        if self is TransferType.CREDIT:
            return credit()
