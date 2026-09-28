

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ThresholdColor(enum.StrEnum):
    """
    The state color for this threshold. Color is not allowed in a XyChart.
    """

    COLOR_UNSPECIFIED = "COLOR_UNSPECIFIED"
    YELLOW = "YELLOW"
    RED = "RED"

    def visit(
        self,
        color_unspecified: typing.Callable[[], T_Result],
        yellow: typing.Callable[[], T_Result],
        red: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ThresholdColor.COLOR_UNSPECIFIED:
            return color_unspecified()
        if self is ThresholdColor.YELLOW:
            return yellow()
        if self is ThresholdColor.RED:
            return red()
