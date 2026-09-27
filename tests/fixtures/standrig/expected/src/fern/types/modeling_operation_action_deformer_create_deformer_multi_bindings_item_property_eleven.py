

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionDeformerCreateDeformerMultiBindingsItemPropertyEleven(enum.StrEnum):
    WARP_TAPER_Y = "warp.taperY"

    def visit(self, warp_taper_y: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionDeformerCreateDeformerMultiBindingsItemPropertyEleven.WARP_TAPER_Y:
            return warp_taper_y()
