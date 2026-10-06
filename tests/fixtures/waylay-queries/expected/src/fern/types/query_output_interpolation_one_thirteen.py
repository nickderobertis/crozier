

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class QueryOutputInterpolationOneThirteen(enum.StrEnum):
    """
    Interpolate with a non-smoothing spline of order 2, called Akima interpolation.
    """

    AKIMA = "akima"

    def visit(self, akima: typing.Callable[[], T_Result]) -> T_Result:
        if self is QueryOutputInterpolationOneThirteen.AKIMA:
            return akima()
