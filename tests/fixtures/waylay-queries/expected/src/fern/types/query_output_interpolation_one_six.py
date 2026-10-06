

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class QueryOutputInterpolationOneSix(enum.StrEnum):
    """
    Interpolate with a spline function of order 1, which is a piecewise polynomial.
    """

    SLINEAR = "slinear"

    def visit(self, slinear: typing.Callable[[], T_Result]) -> T_Result:
        if self is QueryOutputInterpolationOneSix.SLINEAR:
            return slinear()
