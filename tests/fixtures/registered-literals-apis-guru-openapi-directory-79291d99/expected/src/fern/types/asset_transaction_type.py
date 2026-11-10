

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AssetTransactionType(enum.StrEnum):
    """
    Asset Transaction Type.
    """

    CREDIT = "Credit"
    DEBIT = "Debit"

    def visit(self, credit: typing.Callable[[], T_Result], debit: typing.Callable[[], T_Result]) -> T_Result:
        if self is AssetTransactionType.CREDIT:
            return credit()
        if self is AssetTransactionType.DEBIT:
            return debit()
