

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionDeformerBindingKeyPropertyEight(enum.StrEnum):
    WARP_TAPER_X = "warp.taperX"

    def visit(self, warp_taper_x: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionDeformerBindingKeyPropertyEight.WARP_TAPER_X:
            return warp_taper_x()
