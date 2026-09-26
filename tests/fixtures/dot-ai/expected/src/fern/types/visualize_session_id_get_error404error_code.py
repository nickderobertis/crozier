

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VisualizeSessionIdGetError404ErrorCode(enum.StrEnum):
    SESSION_NOT_FOUND = "SESSION_NOT_FOUND"

    def visit(self, session_not_found: typing.Callable[[], T_Result]) -> T_Result:
        if self is VisualizeSessionIdGetError404ErrorCode.SESSION_NOT_FOUND:
            return session_not_found()
