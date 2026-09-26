

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ThresholdDirection(enum.StrEnum):
    """
    The direction for the current threshold. Direction is not allowed in a XyChart.
    """

    DIRECTION_UNSPECIFIED = "DIRECTION_UNSPECIFIED"
    ABOVE = "ABOVE"
    BELOW = "BELOW"

    def visit(
        self,
        direction_unspecified: typing.Callable[[], T_Result],
        above: typing.Callable[[], T_Result],
        below: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ThresholdDirection.DIRECTION_UNSPECIFIED:
            return direction_unspecified()
        if self is ThresholdDirection.ABOVE:
            return above()
        if self is ThresholdDirection.BELOW:
            return below()
