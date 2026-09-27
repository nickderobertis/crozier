

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolationOne(
    enum.StrEnum
):
    HOLD = "hold"

    def visit(self, hold: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolationOne.HOLD
        ):
            return hold()
