

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ThousandsSeparator(enum.StrEnum):
    COMMA = "COMMA"
    DOT = "DOT"
    SPACE = "SPACE"
    NONE = "NONE"

    def visit(
        self,
        comma: typing.Callable[[], T_Result],
        dot: typing.Callable[[], T_Result],
        space: typing.Callable[[], T_Result],
        none: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ThousandsSeparator.COMMA:
            return comma()
        if self is ThousandsSeparator.DOT:
            return dot()
        if self is ThousandsSeparator.SPACE:
            return space()
        if self is ThousandsSeparator.NONE:
            return none()
