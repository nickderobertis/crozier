

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JournalEntryLineItemType(enum.StrEnum):
    """
    Debit entries are considered positive, and credit entries are considered negative.
    """

    DEBIT = "debit"
    CREDIT = "credit"

    def visit(self, debit: typing.Callable[[], T_Result], credit: typing.Callable[[], T_Result]) -> T_Result:
        if self is JournalEntryLineItemType.DEBIT:
            return debit()
        if self is JournalEntryLineItemType.CREDIT:
            return credit()
