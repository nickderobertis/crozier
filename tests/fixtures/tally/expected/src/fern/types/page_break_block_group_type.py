

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PageBreakBlockGroupType(enum.StrEnum):
    PAGE_BREAK = "PAGE_BREAK"

    def visit(self, page_break: typing.Callable[[], T_Result]) -> T_Result:
        if self is PageBreakBlockGroupType.PAGE_BREAK:
            return page_break()
