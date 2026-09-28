

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TextFormat(enum.StrEnum):
    """
    How the text content is formatted.
    """

    FORMAT_UNSPECIFIED = "FORMAT_UNSPECIFIED"
    MARKDOWN = "MARKDOWN"
    RAW = "RAW"

    def visit(
        self,
        format_unspecified: typing.Callable[[], T_Result],
        markdown: typing.Callable[[], T_Result],
        raw: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TextFormat.FORMAT_UNSPECIFIED:
            return format_unspecified()
        if self is TextFormat.MARKDOWN:
            return markdown()
        if self is TextFormat.RAW:
            return raw()
