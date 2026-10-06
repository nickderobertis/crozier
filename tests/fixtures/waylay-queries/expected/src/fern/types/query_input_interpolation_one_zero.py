

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class QueryInputInterpolationOneZero(enum.StrEnum):
    """
    Interpolate with the value of the first observed point. This method also extrapolates.
    """

    PAD = "pad"

    def visit(self, pad: typing.Callable[[], T_Result]) -> T_Result:
        if self is QueryInputInterpolationOneZero.PAD:
            return pad()
