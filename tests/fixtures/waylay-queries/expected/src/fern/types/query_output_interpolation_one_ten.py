

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class QueryOutputInterpolationOneTen(enum.StrEnum):
    """
    Interpolate with a spline function of a user-specified order.
    """

    SPLINE = "spline"

    def visit(self, spline: typing.Callable[[], T_Result]) -> T_Result:
        if self is QueryOutputInterpolationOneTen.SPLINE:
            return spline()
