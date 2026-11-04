

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResponseQueuedStreamingEventType(enum.StrEnum):
    """
    The type of the event, always `response.queued`.
    """

    RESPONSE_QUEUED = "response.queued"

    def visit(self, response_queued: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResponseQueuedStreamingEventType.RESPONSE_QUEUED:
            return response_queued()
