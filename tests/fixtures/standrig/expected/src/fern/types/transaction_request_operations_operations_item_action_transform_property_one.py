

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionTransformPropertyOne(enum.StrEnum):
    Y = "y"

    def visit(self, y: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionTransformPropertyOne.Y:
            return y()
