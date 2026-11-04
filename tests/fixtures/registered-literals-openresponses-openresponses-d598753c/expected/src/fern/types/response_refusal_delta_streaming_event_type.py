

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResponseRefusalDeltaStreamingEventType(enum.StrEnum):
    """
    The type of the event, always `response.refusal.delta`.
    """

    RESPONSE_REFUSAL_DELTA = "response.refusal.delta"

    def visit(self, response_refusal_delta: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResponseRefusalDeltaStreamingEventType.RESPONSE_REFUSAL_DELTA:
            return response_refusal_delta()
