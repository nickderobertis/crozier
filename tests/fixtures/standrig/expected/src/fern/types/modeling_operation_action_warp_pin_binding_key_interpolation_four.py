

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionWarpPinBindingKeyInterpolationFour(enum.StrEnum):
    CURVE = "curve"

    def visit(self, curve: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionWarpPinBindingKeyInterpolationFour.CURVE:
            return curve()
