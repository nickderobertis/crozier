

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemInterpolationFour(
    enum.StrEnum
):
    CURVE = "curve"

    def visit(self, curve: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemInterpolationFour.CURVE
        ):
            return curve()
