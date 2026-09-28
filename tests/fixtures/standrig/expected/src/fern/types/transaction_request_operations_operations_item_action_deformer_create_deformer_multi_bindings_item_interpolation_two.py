

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemInterpolationTwo(
    enum.StrEnum
):
    SMOOTHSTEP = "smoothstep"

    def visit(self, smoothstep: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemInterpolationTwo.SMOOTHSTEP
        ):
            return smoothstep()
