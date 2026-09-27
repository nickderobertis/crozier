

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertyTen(enum.StrEnum):
    WARP_TAPER_X = "warp.taperX"

    def visit(self, warp_taper_x: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertyTen.WARP_TAPER_X
        ):
            return warp_taper_x()
