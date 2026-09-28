

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemInterpolationTwo(enum.StrEnum):
    SMOOTHSTEP = "smoothstep"

    def visit(self, smoothstep: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemInterpolationTwo.SMOOTHSTEP
        ):
            return smoothstep()
