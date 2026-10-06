

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SeriesSpecInterpolationOneFive(enum.StrEnum):
    """
    Interpolate with a spline function of order 0, which is a piecewise polynomial.
    """

    ZERO = "zero"

    def visit(self, zero: typing.Callable[[], T_Result]) -> T_Result:
        if self is SeriesSpecInterpolationOneFive.ZERO:
            return zero()
