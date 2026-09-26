

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EventsRemediationsGetResponseEvent(enum.StrEnum):
    """
    SSE event type
    """

    SESSION_CREATED = "session-created"
    SESSION_UPDATED = "session-updated"

    def visit(
        self, session_created: typing.Callable[[], T_Result], session_updated: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is EventsRemediationsGetResponseEvent.SESSION_CREATED:
            return session_created()
        if self is EventsRemediationsGetResponseEvent.SESSION_UPDATED:
            return session_updated()
