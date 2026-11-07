

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResponseIncompleteStreamingEventType(enum.StrEnum):
    """
    The type of the event, always `response.incomplete`.
    """

    RESPONSE_INCOMPLETE = "response.incomplete"

    def visit(self, response_incomplete: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResponseIncompleteStreamingEventType.RESPONSE_INCOMPLETE:
            return response_incomplete()
