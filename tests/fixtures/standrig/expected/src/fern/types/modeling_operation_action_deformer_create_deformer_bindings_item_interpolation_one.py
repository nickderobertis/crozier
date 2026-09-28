

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionDeformerCreateDeformerBindingsItemInterpolationOne(enum.StrEnum):
    HOLD = "hold"

    def visit(self, hold: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionDeformerCreateDeformerBindingsItemInterpolationOne.HOLD:
            return hold()
