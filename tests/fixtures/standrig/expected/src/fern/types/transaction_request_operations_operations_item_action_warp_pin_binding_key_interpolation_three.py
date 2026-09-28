

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyInterpolationThree(enum.StrEnum):
    ARC = "arc"

    def visit(self, arc: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyInterpolationThree.ARC:
            return arc()
