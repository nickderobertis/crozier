

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResponseReasoningDeltaStreamingEventType(enum.StrEnum):
    """
    The type of the event, always `response.reasoning.delta`.
    """

    RESPONSE_REASONING_DELTA = "response.reasoning.delta"

    def visit(self, response_reasoning_delta: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResponseReasoningDeltaStreamingEventType.RESPONSE_REASONING_DELTA:
            return response_reasoning_delta()
