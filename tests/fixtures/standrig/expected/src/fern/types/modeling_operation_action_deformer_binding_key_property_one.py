

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionDeformerBindingKeyPropertyOne(enum.StrEnum):
    Y = "y"

    def visit(self, y: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionDeformerBindingKeyPropertyOne.Y:
            return y()
