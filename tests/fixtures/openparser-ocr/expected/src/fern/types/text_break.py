

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TextBreak(enum.StrEnum):
    NONE = "none"
    SPACE = "space"
    WIDE_SPACE = "wide_space"
    HYPHEN = "hyphen"
    LINE_BREAK = "line_break"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        space: typing.Callable[[], T_Result],
        wide_space: typing.Callable[[], T_Result],
        hyphen: typing.Callable[[], T_Result],
        line_break: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TextBreak.NONE:
            return none()
        if self is TextBreak.SPACE:
            return space()
        if self is TextBreak.WIDE_SPACE:
            return wide_space()
        if self is TextBreak.HYPHEN:
            return hyphen()
        if self is TextBreak.LINE_BREAK:
            return line_break()
