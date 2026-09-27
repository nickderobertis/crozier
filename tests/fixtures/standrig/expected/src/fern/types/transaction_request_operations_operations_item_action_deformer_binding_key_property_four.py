

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionDeformerBindingKeyPropertyFour(enum.StrEnum):
    SCALE_Y = "scaleY"

    def visit(self, scale_y: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionDeformerBindingKeyPropertyFour.SCALE_Y:
            return scale_y()
