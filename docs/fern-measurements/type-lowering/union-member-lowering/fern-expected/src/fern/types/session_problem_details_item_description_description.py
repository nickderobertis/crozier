

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SessionProblemDetailsItemDescriptionDescription(enum.StrEnum):
    THE_SESSION_IS_CLOSED = "The session is closed."

    def visit(self, the_session_is_closed: typing.Callable[[], T_Result]) -> T_Result:
        if self is SessionProblemDetailsItemDescriptionDescription.THE_SESSION_IS_CLOSED:
            return the_session_is_closed()
