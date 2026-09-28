

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemPropertyZero(enum.StrEnum):
    OFFSET_X = "offsetX"

    def visit(self, offset_x: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemPropertyZero.OFFSET_X
        ):
            return offset_x()
