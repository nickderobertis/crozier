

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionBindingKeyPropertyFour(enum.StrEnum):
    SCALE_Y = "scaleY"

    def visit(self, scale_y: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionBindingKeyPropertyFour.SCALE_Y:
            return scale_y()
