

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionDeformerBindingKeyPropertySix(enum.StrEnum):
    WARP_BEND_X = "warp.bendX"

    def visit(self, warp_bend_x: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionDeformerBindingKeyPropertySix.WARP_BEND_X:
            return warp_bend_x()
