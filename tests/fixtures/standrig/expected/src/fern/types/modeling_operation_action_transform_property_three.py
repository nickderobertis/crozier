

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionTransformPropertyThree(enum.StrEnum):
    SCALE_X = "scaleX"

    def visit(self, scale_x: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionTransformPropertyThree.SCALE_X:
            return scale_x()
