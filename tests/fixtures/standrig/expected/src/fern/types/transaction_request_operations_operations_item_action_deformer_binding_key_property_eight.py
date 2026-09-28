

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionDeformerBindingKeyPropertyEight(enum.StrEnum):
    WARP_TAPER_X = "warp.taperX"

    def visit(self, warp_taper_x: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionDeformerBindingKeyPropertyEight.WARP_TAPER_X:
            return warp_taper_x()
