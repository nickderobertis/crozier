

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResponseReasoningSummaryDeltaStreamingEventType(enum.StrEnum):
    """
    The type of the event, always `response.reasoning_summary.delta`.
    """

    RESPONSE_REASONING_SUMMARY_TEXT_DELTA = "response.reasoning_summary_text.delta"

    def visit(self, response_reasoning_summary_text_delta: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResponseReasoningSummaryDeltaStreamingEventType.RESPONSE_REASONING_SUMMARY_TEXT_DELTA:
            return response_reasoning_summary_text_delta()
