

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TraceScopeType(enum.StrEnum):
    TRACE = "trace"

    def visit(self, trace: typing.Callable[[], T_Result]) -> T_Result:
        if self is TraceScopeType.TRACE:
            return trace()
