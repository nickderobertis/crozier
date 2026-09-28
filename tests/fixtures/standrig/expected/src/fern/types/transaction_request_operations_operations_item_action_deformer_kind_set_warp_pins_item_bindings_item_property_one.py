

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemPropertyOne(enum.StrEnum):
    OFFSET_Y = "offsetY"

    def visit(self, offset_y: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemPropertyOne.OFFSET_Y
        ):
            return offset_y()
