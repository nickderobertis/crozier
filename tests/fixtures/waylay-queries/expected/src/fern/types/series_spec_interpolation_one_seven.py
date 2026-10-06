

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SeriesSpecInterpolationOneSeven(enum.StrEnum):
    """
    Interpolate with a spline function of order 2, which is a piecewise polynomial.
    """

    QUADRATIC = "quadratic"

    def visit(self, quadratic: typing.Callable[[], T_Result]) -> T_Result:
        if self is SeriesSpecInterpolationOneSeven.QUADRATIC:
            return quadratic()
