

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TextStyleVerticalAlignment(enum.StrEnum):
    """
    The vertical alignment of both the title and content
    """

    VERTICAL_ALIGNMENT_UNSPECIFIED = "VERTICAL_ALIGNMENT_UNSPECIFIED"
    V_TOP = "V_TOP"
    V_CENTER = "V_CENTER"
    V_BOTTOM = "V_BOTTOM"

    def visit(
        self,
        vertical_alignment_unspecified: typing.Callable[[], T_Result],
        v_top: typing.Callable[[], T_Result],
        v_center: typing.Callable[[], T_Result],
        v_bottom: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TextStyleVerticalAlignment.VERTICAL_ALIGNMENT_UNSPECIFIED:
            return vertical_alignment_unspecified()
        if self is TextStyleVerticalAlignment.V_TOP:
            return v_top()
        if self is TextStyleVerticalAlignment.V_CENTER:
            return v_center()
        if self is TextStyleVerticalAlignment.V_BOTTOM:
            return v_bottom()
