

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertyNine(enum.StrEnum):
    WARP_BEND_Y = "warp.bendY"

    def visit(self, warp_bend_y: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertyNine.WARP_BEND_Y
        ):
            return warp_bend_y()
