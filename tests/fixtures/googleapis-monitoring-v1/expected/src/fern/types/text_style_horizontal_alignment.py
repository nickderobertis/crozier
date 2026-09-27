

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TextStyleHorizontalAlignment(enum.StrEnum):
    """
    The horizontal alignment of both the title and content
    """

    HORIZONTAL_ALIGNMENT_UNSPECIFIED = "HORIZONTAL_ALIGNMENT_UNSPECIFIED"
    H_LEFT = "H_LEFT"
    H_CENTER = "H_CENTER"
    H_RIGHT = "H_RIGHT"

    def visit(
        self,
        horizontal_alignment_unspecified: typing.Callable[[], T_Result],
        h_left: typing.Callable[[], T_Result],
        h_center: typing.Callable[[], T_Result],
        h_right: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TextStyleHorizontalAlignment.HORIZONTAL_ALIGNMENT_UNSPECIFIED:
            return horizontal_alignment_unspecified()
        if self is TextStyleHorizontalAlignment.H_LEFT:
            return h_left()
        if self is TextStyleHorizontalAlignment.H_CENTER:
            return h_center()
        if self is TextStyleHorizontalAlignment.H_RIGHT:
            return h_right()
