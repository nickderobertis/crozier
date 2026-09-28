

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HitlShapeMismatchErrorError(enum.StrEnum):
    SHAPE_MISMATCH = "shape mismatch"

    def visit(self, shape_mismatch: typing.Callable[[], T_Result]) -> T_Result:
        if self is HitlShapeMismatchErrorError.SHAPE_MISMATCH:
            return shape_mismatch()
