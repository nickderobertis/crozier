

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BankTransferEventListBankTransferType(enum.StrEnum):
    """
    The type of bank transfer. This will be either `debit` or `credit`.  A `debit` indicates a transfer of money into your origination account; a `credit` indicates a transfer of money out of your origination account.
    """

    DEBIT = "debit"
    CREDIT = "credit"

    def visit(self, debit: typing.Callable[[], T_Result], credit: typing.Callable[[], T_Result]) -> T_Result:
        if self is BankTransferEventListBankTransferType.DEBIT:
            return debit()
        if self is BankTransferEventListBankTransferType.CREDIT:
            return credit()
