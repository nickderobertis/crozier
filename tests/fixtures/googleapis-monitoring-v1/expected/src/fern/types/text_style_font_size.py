

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TextStyleFontSize(enum.StrEnum):
    """
    Font sizes for both the title and content. The title will still be larger relative to the content.
    """

    FONT_SIZE_UNSPECIFIED = "FONT_SIZE_UNSPECIFIED"
    FS_EXTRA_SMALL = "FS_EXTRA_SMALL"
    FS_SMALL = "FS_SMALL"
    FS_MEDIUM = "FS_MEDIUM"
    FS_LARGE = "FS_LARGE"
    FS_EXTRA_LARGE = "FS_EXTRA_LARGE"

    def visit(
        self,
        font_size_unspecified: typing.Callable[[], T_Result],
        fs_extra_small: typing.Callable[[], T_Result],
        fs_small: typing.Callable[[], T_Result],
        fs_medium: typing.Callable[[], T_Result],
        fs_large: typing.Callable[[], T_Result],
        fs_extra_large: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TextStyleFontSize.FONT_SIZE_UNSPECIFIED:
            return font_size_unspecified()
        if self is TextStyleFontSize.FS_EXTRA_SMALL:
            return fs_extra_small()
        if self is TextStyleFontSize.FS_SMALL:
            return fs_small()
        if self is TextStyleFontSize.FS_MEDIUM:
            return fs_medium()
        if self is TextStyleFontSize.FS_LARGE:
            return fs_large()
        if self is TextStyleFontSize.FS_EXTRA_LARGE:
            return fs_extra_large()
