

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemCompositionZero(enum.StrEnum):
    MULTIPLY = "multiply"

    def visit(self, multiply: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemCompositionZero.MULTIPLY
        ):
            return multiply()
