

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SessionProblemDetailsItemDescriptionIssue(enum.StrEnum):
    SESSION_CLOSED = "SESSION_CLOSED"

    def visit(self, session_closed: typing.Callable[[], T_Result]) -> T_Result:
        if self is SessionProblemDetailsItemDescriptionIssue.SESSION_CLOSED:
            return session_closed()
