

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionDeformerBindingRemovePropertyNine(enum.StrEnum):
    WARP_TAPER_Y = "warp.taperY"

    def visit(self, warp_taper_y: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionDeformerBindingRemovePropertyNine.WARP_TAPER_Y:
            return warp_taper_y()
