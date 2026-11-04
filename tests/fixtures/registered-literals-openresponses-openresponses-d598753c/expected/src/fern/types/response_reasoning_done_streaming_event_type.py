

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResponseReasoningDoneStreamingEventType(enum.StrEnum):
    """
    The type of the event, always `response.reasoning.done`.
    """

    RESPONSE_REASONING_DONE = "response.reasoning.done"

    def visit(self, response_reasoning_done: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResponseReasoningDoneStreamingEventType.RESPONSE_REASONING_DONE:
            return response_reasoning_done()
