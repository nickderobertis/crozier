

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class QueryOutputInterpolationOneOne(enum.StrEnum):
    """
    Interpolate with a fixed, user-specified value. This method also extrapolates.
    """

    FIXED = "fixed"

    def visit(self, fixed: typing.Callable[[], T_Result]) -> T_Result:
        if self is QueryOutputInterpolationOneOne.FIXED:
            return fixed()
