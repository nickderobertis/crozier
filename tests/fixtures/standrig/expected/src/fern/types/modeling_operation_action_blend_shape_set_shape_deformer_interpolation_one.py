

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionBlendShapeSetShapeDeformerInterpolationOne(enum.StrEnum):
    HOLD = "hold"

    def visit(self, hold: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionBlendShapeSetShapeDeformerInterpolationOne.HOLD:
            return hold()
