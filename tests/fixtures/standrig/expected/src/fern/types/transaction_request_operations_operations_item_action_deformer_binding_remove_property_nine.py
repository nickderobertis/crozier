

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionDeformerBindingRemovePropertyNine(enum.StrEnum):
    WARP_TAPER_Y = "warp.taperY"

    def visit(self, warp_taper_y: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionDeformerBindingRemovePropertyNine.WARP_TAPER_Y:
            return warp_taper_y()
