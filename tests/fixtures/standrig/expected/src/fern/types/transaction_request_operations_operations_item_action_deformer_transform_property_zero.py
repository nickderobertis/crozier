

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionDeformerTransformPropertyZero(enum.StrEnum):
    X = "x"

    def visit(self, x: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionDeformerTransformPropertyZero.X:
            return x()
