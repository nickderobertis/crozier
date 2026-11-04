

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResponseCompletedStreamingEventType(enum.StrEnum):
    """
    The type of the event, always `response.completed`.
    """

    RESPONSE_COMPLETED = "response.completed"

    def visit(self, response_completed: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResponseCompletedStreamingEventType.RESPONSE_COMPLETED:
            return response_completed()
