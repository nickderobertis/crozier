

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionTransformOperatorTwo(enum.StrEnum):
    MULTIPLY = "multiply"

    def visit(self, multiply: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionTransformOperatorTwo.MULTIPLY:
            return multiply()
