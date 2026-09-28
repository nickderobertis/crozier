

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemInterpolationOne(
    enum.StrEnum
):
    HOLD = "hold"

    def visit(self, hold: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemInterpolationOne.HOLD
        ):
            return hold()
