

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DecimalSeparator(enum.StrEnum):
    COMMA = "COMMA"
    DOT = "DOT"

    def visit(self, comma: typing.Callable[[], T_Result], dot: typing.Callable[[], T_Result]) -> T_Result:
        if self is DecimalSeparator.COMMA:
            return comma()
        if self is DecimalSeparator.DOT:
            return dot()
