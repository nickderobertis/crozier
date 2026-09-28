

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionDeformBrushBrushSurfaceWarpPinsSpace(enum.StrEnum):
    WARP_LOCAL = "warp-local"

    def visit(self, warp_local: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionDeformBrushBrushSurfaceWarpPinsSpace.WARP_LOCAL:
            return warp_local()
