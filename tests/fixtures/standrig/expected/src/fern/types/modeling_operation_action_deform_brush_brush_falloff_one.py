

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionDeformBrushBrushFalloffOne(enum.StrEnum):
    SMOOTH = "smooth"

    def visit(self, smooth: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionDeformBrushBrushFalloffOne.SMOOTH:
            return smooth()
