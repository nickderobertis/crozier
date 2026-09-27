

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurfaceWarpPinsSpace(enum.StrEnum):
    WARP_LOCAL = "warp-local"

    def visit(self, warp_local: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurfaceWarpPinsSpace.WARP_LOCAL:
            return warp_local()
