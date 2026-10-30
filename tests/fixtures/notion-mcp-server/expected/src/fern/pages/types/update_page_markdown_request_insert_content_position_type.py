

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdatePageMarkdownRequestInsertContentPositionType(enum.StrEnum):
    START = "start"
    END = "end"

    def visit(self, start: typing.Callable[[], T_Result], end: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdatePageMarkdownRequestInsertContentPositionType.START:
            return start()
        if self is UpdatePageMarkdownRequestInsertContentPositionType.END:
            return end()
