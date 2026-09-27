

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AxisScale(enum.StrEnum):
    """
    The axis scale. By default, a linear scale is used.
    """

    SCALE_UNSPECIFIED = "SCALE_UNSPECIFIED"
    LINEAR = "LINEAR"
    LOG10 = "LOG10"

    def visit(
        self,
        scale_unspecified: typing.Callable[[], T_Result],
        linear: typing.Callable[[], T_Result],
        log10: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AxisScale.SCALE_UNSPECIFIED:
            return scale_unspecified()
        if self is AxisScale.LINEAR:
            return linear()
        if self is AxisScale.LOG10:
            return log10()
