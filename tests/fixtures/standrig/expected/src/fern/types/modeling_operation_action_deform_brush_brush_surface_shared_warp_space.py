

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionDeformBrushBrushSurfaceSharedWarpSpace(enum.StrEnum):
    STAGE = "stage"

    def visit(self, stage: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionDeformBrushBrushSurfaceSharedWarpSpace.STAGE:
            return stage()
