

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TextStylePointerLocation(enum.StrEnum):
    """
    The pointer location for this widget (also sometimes called a "tail")
    """

    POINTER_LOCATION_UNSPECIFIED = "POINTER_LOCATION_UNSPECIFIED"
    PL_TOP = "PL_TOP"
    PL_RIGHT = "PL_RIGHT"
    PL_BOTTOM = "PL_BOTTOM"
    PL_LEFT = "PL_LEFT"
    PL_TOP_LEFT = "PL_TOP_LEFT"
    PL_TOP_RIGHT = "PL_TOP_RIGHT"
    PL_RIGHT_TOP = "PL_RIGHT_TOP"
    PL_RIGHT_BOTTOM = "PL_RIGHT_BOTTOM"
    PL_BOTTOM_RIGHT = "PL_BOTTOM_RIGHT"
    PL_BOTTOM_LEFT = "PL_BOTTOM_LEFT"
    PL_LEFT_BOTTOM = "PL_LEFT_BOTTOM"
    PL_LEFT_TOP = "PL_LEFT_TOP"

    def visit(
        self,
        pointer_location_unspecified: typing.Callable[[], T_Result],
        pl_top: typing.Callable[[], T_Result],
        pl_right: typing.Callable[[], T_Result],
        pl_bottom: typing.Callable[[], T_Result],
        pl_left: typing.Callable[[], T_Result],
        pl_top_left: typing.Callable[[], T_Result],
        pl_top_right: typing.Callable[[], T_Result],
        pl_right_top: typing.Callable[[], T_Result],
        pl_right_bottom: typing.Callable[[], T_Result],
        pl_bottom_right: typing.Callable[[], T_Result],
        pl_bottom_left: typing.Callable[[], T_Result],
        pl_left_bottom: typing.Callable[[], T_Result],
        pl_left_top: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TextStylePointerLocation.POINTER_LOCATION_UNSPECIFIED:
            return pointer_location_unspecified()
        if self is TextStylePointerLocation.PL_TOP:
            return pl_top()
        if self is TextStylePointerLocation.PL_RIGHT:
            return pl_right()
        if self is TextStylePointerLocation.PL_BOTTOM:
            return pl_bottom()
        if self is TextStylePointerLocation.PL_LEFT:
            return pl_left()
        if self is TextStylePointerLocation.PL_TOP_LEFT:
            return pl_top_left()
        if self is TextStylePointerLocation.PL_TOP_RIGHT:
            return pl_top_right()
        if self is TextStylePointerLocation.PL_RIGHT_TOP:
            return pl_right_top()
        if self is TextStylePointerLocation.PL_RIGHT_BOTTOM:
            return pl_right_bottom()
        if self is TextStylePointerLocation.PL_BOTTOM_RIGHT:
            return pl_bottom_right()
        if self is TextStylePointerLocation.PL_BOTTOM_LEFT:
            return pl_bottom_left()
        if self is TextStylePointerLocation.PL_LEFT_BOTTOM:
            return pl_left_bottom()
        if self is TextStylePointerLocation.PL_LEFT_TOP:
            return pl_left_top()
