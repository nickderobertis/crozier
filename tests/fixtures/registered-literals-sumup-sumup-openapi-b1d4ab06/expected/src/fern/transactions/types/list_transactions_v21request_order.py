

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListTransactionsV21RequestOrder(enum.StrEnum):
    ASCENDING = "ascending"
    DESCENDING = "descending"

    def visit(self, ascending: typing.Callable[[], T_Result], descending: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListTransactionsV21RequestOrder.ASCENDING:
            return ascending()
        if self is ListTransactionsV21RequestOrder.DESCENDING:
            return descending()
