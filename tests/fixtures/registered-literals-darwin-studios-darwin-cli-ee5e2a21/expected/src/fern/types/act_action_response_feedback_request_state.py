

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActActionResponseFeedbackRequestState(enum.StrEnum):
    OPEN = "OPEN"
    SUBMITTED = "SUBMITTED"
    EXPIRED = "EXPIRED"
    UNAVAILABLE = "UNAVAILABLE"

    def visit(
        self,
        open: typing.Callable[[], T_Result],
        submitted: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
        unavailable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ActActionResponseFeedbackRequestState.OPEN:
            return open()
        if self is ActActionResponseFeedbackRequestState.SUBMITTED:
            return submitted()
        if self is ActActionResponseFeedbackRequestState.EXPIRED:
            return expired()
        if self is ActActionResponseFeedbackRequestState.UNAVAILABLE:
            return unavailable()
