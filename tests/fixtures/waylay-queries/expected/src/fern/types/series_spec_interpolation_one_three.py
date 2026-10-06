

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SeriesSpecInterpolationOneThree(enum.StrEnum):
    """
    Linearly go from the first observed value of the gap to the last observed oneThis method also extrapolates
    """

    LINEAR = "linear"

    def visit(self, linear: typing.Callable[[], T_Result]) -> T_Result:
        if self is SeriesSpecInterpolationOneThree.LINEAR:
            return linear()
