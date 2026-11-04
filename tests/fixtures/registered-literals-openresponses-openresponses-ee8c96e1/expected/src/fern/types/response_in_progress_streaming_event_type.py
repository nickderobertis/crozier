

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResponseInProgressStreamingEventType(enum.StrEnum):
    """
    The type of the event, always `response.in_progress`.
    """

    RESPONSE_IN_PROGRESS = "response.in_progress"

    def visit(self, response_in_progress: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResponseInProgressStreamingEventType.RESPONSE_IN_PROGRESS:
            return response_in_progress()
