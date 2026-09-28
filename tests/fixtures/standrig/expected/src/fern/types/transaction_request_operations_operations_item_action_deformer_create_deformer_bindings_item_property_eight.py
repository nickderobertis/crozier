

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemPropertyEight(enum.StrEnum):
    WARP_TAPER_X = "warp.taperX"

    def visit(self, warp_taper_x: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemPropertyEight.WARP_TAPER_X
        ):
            return warp_taper_x()
