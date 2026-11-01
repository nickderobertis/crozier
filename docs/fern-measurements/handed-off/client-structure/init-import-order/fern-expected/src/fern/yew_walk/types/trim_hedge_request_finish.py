

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class TrimHedgeRequestFinish(enum.StrEnum):
    SQUARE = "square"
    ROUNDED = "rounded"

    def visit(self, square: typing.Callable[[], T_Result], rounded: typing.Callable[[], T_Result]) -> T_Result:
        if self is TrimHedgeRequestFinish.SQUARE:
            return square()
        if self is TrimHedgeRequestFinish.ROUNDED:
            return rounded()
