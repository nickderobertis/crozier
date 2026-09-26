

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LogsOrder(enum.StrEnum):
    ASCENDING = "ascending"
    DESCENDING = "descending"

    def visit(self, ascending: typing.Callable[[], T_Result], descending: typing.Callable[[], T_Result]) -> T_Result:
        if self is LogsOrder.ASCENDING:
            return ascending()
        if self is LogsOrder.DESCENDING:
            return descending()
