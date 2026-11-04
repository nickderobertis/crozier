

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResponseRefusalDoneStreamingEventType(enum.StrEnum):
    """
    The type of the event, always `response.refusal.done`.
    """

    RESPONSE_REFUSAL_DONE = "response.refusal.done"

    def visit(self, response_refusal_done: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResponseRefusalDoneStreamingEventType.RESPONSE_REFUSAL_DONE:
            return response_refusal_done()
