

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionDeformerCreateDeformerBlendShapesItemInterpolationFour(enum.StrEnum):
    CURVE = "curve"

    def visit(self, curve: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionDeformerCreateDeformerBlendShapesItemInterpolationFour.CURVE:
            return curve()
