

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LiveActivityJobResponseStatus(enum.StrEnum):
    STARTED = "started"
    UPDATED = "updated"
    ENDED = "ended"
    ALREADY_STARTED = "already_started"
    CLOSED = "closed"

    def visit(
        self,
        started: typing.Callable[[], T_Result],
        updated: typing.Callable[[], T_Result],
        ended: typing.Callable[[], T_Result],
        already_started: typing.Callable[[], T_Result],
        closed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LiveActivityJobResponseStatus.STARTED:
            return started()
        if self is LiveActivityJobResponseStatus.UPDATED:
            return updated()
        if self is LiveActivityJobResponseStatus.ENDED:
            return ended()
        if self is LiveActivityJobResponseStatus.ALREADY_STARTED:
            return already_started()
        if self is LiveActivityJobResponseStatus.CLOSED:
            return closed()
