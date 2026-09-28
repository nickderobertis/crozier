

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolationThree(
    enum.StrEnum
):
    ARC = "arc"

    def visit(self, arc: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolationThree.ARC
        ):
            return arc()
