

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class QueryInputInterpolationOneTwelve(enum.StrEnum):
    """
    Interpolate with a piecewise cubic spline function.
    """

    PCHIP = "pchip"

    def visit(self, pchip: typing.Callable[[], T_Result]) -> T_Result:
        if self is QueryInputInterpolationOneTwelve.PCHIP:
            return pchip()
