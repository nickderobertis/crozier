

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionDeformerTransformPropertyOne(enum.StrEnum):
    Y = "y"

    def visit(self, y: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionDeformerTransformPropertyOne.Y:
            return y()
