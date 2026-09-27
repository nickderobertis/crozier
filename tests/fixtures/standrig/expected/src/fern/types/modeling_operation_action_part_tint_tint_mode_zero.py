

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionPartTintTintModeZero(enum.StrEnum):
    MULTIPLY = "multiply"

    def visit(self, multiply: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionPartTintTintModeZero.MULTIPLY:
            return multiply()
