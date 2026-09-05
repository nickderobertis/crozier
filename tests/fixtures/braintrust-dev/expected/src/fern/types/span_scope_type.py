

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SpanScopeType(enum.StrEnum):
    SPAN = "span"

    def visit(self, span: typing.Callable[[], T_Result]) -> T_Result:
        if self is SpanScopeType.SPAN:
            return span()
