

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionWarpPinBindingKeyInterpolationThree(enum.StrEnum):
    ARC = "arc"

    def visit(self, arc: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionWarpPinBindingKeyInterpolationThree.ARC:
            return arc()
