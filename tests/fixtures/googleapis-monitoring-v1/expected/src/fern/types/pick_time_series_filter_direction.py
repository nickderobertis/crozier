

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PickTimeSeriesFilterDirection(enum.StrEnum):
    """
    How to use the ranking to select time series that pass through the filter.
    """

    DIRECTION_UNSPECIFIED = "DIRECTION_UNSPECIFIED"
    TOP = "TOP"
    BOTTOM = "BOTTOM"

    def visit(
        self,
        direction_unspecified: typing.Callable[[], T_Result],
        top: typing.Callable[[], T_Result],
        bottom: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PickTimeSeriesFilterDirection.DIRECTION_UNSPECIFIED:
            return direction_unspecified()
        if self is PickTimeSeriesFilterDirection.TOP:
            return top()
        if self is PickTimeSeriesFilterDirection.BOTTOM:
            return bottom()
