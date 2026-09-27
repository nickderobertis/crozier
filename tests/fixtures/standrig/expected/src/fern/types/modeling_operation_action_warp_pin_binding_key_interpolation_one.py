

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionWarpPinBindingKeyInterpolationOne(enum.StrEnum):
    HOLD = "hold"

    def visit(self, hold: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionWarpPinBindingKeyInterpolationOne.HOLD:
            return hold()
