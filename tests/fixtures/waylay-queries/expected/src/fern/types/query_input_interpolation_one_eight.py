

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class QueryInputInterpolationOneEight(enum.StrEnum):
    """
    Interpolate with a spline function of order 3, which is a piecewise polynomial.
    """

    CUBIC = "cubic"

    def visit(self, cubic: typing.Callable[[], T_Result]) -> T_Result:
        if self is QueryInputInterpolationOneEight.CUBIC:
            return cubic()
