

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyPropertyOne(enum.StrEnum):
    OFFSET_Y = "offsetY"

    def visit(self, offset_y: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyPropertyOne.OFFSET_Y:
            return offset_y()
