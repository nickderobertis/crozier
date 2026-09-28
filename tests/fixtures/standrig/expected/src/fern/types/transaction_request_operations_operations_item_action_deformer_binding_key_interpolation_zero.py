

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionDeformerBindingKeyInterpolationZero(enum.StrEnum):
    LINEAR = "linear"

    def visit(self, linear: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionDeformerBindingKeyInterpolationZero.LINEAR:
            return linear()
