

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EntrySide(enum.StrEnum):
    DEBIT = "debit"
    CREDIT = "credit"

    def visit(self, debit: typing.Callable[[], T_Result], credit: typing.Callable[[], T_Result]) -> T_Result:
        if self is EntrySide.DEBIT:
            return debit()
        if self is EntrySide.CREDIT:
            return credit()
