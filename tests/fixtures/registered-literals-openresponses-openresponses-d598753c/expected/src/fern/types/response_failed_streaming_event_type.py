

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResponseFailedStreamingEventType(enum.StrEnum):
    """
    The type of the event, always `response.failed`.
    """

    RESPONSE_FAILED = "response.failed"

    def visit(self, response_failed: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResponseFailedStreamingEventType.RESPONSE_FAILED:
            return response_failed()
