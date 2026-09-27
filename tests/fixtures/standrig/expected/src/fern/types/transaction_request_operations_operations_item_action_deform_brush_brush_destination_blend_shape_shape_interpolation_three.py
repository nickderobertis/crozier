

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBlendShapeShapeInterpolationThree(
    enum.StrEnum
):
    ARC = "arc"

    def visit(self, arc: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBlendShapeShapeInterpolationThree.ARC
        ):
            return arc()
