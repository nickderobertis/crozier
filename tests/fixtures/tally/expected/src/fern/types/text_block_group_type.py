

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TextBlockGroupType(enum.StrEnum):
    TEXT = "TEXT"
    PAGE_BREAK = "PAGE_BREAK"
    DIVIDER = "DIVIDER"

    def visit(
        self,
        text: typing.Callable[[], T_Result],
        page_break: typing.Callable[[], T_Result],
        divider: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TextBlockGroupType.TEXT:
            return text()
        if self is TextBlockGroupType.PAGE_BREAK:
            return page_break()
        if self is TextBlockGroupType.DIVIDER:
            return divider()
