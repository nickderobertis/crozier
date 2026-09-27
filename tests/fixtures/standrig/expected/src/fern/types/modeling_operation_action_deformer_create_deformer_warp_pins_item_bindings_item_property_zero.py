

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemPropertyZero(enum.StrEnum):
    OFFSET_X = "offsetX"

    def visit(self, offset_x: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemPropertyZero.OFFSET_X:
            return offset_x()
