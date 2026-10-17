

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CallStatus(enum.StrEnum):
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    ERROR = "error"
    ENDED = "ended"

    def visit(
        self,
        not_started: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
        ended: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CallStatus.NOT_STARTED:
            return not_started()
        if self is CallStatus.IN_PROGRESS:
            return in_progress()
        if self is CallStatus.ERROR:
            return error()
        if self is CallStatus.ENDED:
            return ended()
