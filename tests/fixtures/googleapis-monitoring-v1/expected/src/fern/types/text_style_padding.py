

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TextStylePadding(enum.StrEnum):
    """
    The amount of padding around the widget
    """

    PADDING_SIZE_UNSPECIFIED = "PADDING_SIZE_UNSPECIFIED"
    P_EXTRA_SMALL = "P_EXTRA_SMALL"
    P_SMALL = "P_SMALL"
    P_MEDIUM = "P_MEDIUM"
    P_LARGE = "P_LARGE"
    P_EXTRA_LARGE = "P_EXTRA_LARGE"

    def visit(
        self,
        padding_size_unspecified: typing.Callable[[], T_Result],
        p_extra_small: typing.Callable[[], T_Result],
        p_small: typing.Callable[[], T_Result],
        p_medium: typing.Callable[[], T_Result],
        p_large: typing.Callable[[], T_Result],
        p_extra_large: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TextStylePadding.PADDING_SIZE_UNSPECIFIED:
            return padding_size_unspecified()
        if self is TextStylePadding.P_EXTRA_SMALL:
            return p_extra_small()
        if self is TextStylePadding.P_SMALL:
            return p_small()
        if self is TextStylePadding.P_MEDIUM:
            return p_medium()
        if self is TextStylePadding.P_LARGE:
            return p_large()
        if self is TextStylePadding.P_EXTRA_LARGE:
            return p_extra_large()
