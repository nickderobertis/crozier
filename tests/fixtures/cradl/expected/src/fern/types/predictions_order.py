

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PredictionsOrder(enum.StrEnum):
    ASCENDING = "ascending"
    DESCENDING = "descending"

    def visit(self, ascending: typing.Callable[[], T_Result], descending: typing.Callable[[], T_Result]) -> T_Result:
        if self is PredictionsOrder.ASCENDING:
            return ascending()
        if self is PredictionsOrder.DESCENDING:
            return descending()
