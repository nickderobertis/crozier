

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResponseReasoningSummaryDoneStreamingEventType(enum.StrEnum):
    """
    The type of the event, always `response.reasoning_summary.done`.
    """

    RESPONSE_REASONING_SUMMARY_TEXT_DONE = "response.reasoning_summary_text.done"

    def visit(self, response_reasoning_summary_text_done: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResponseReasoningSummaryDoneStreamingEventType.RESPONSE_REASONING_SUMMARY_TEXT_DONE:
            return response_reasoning_summary_text_done()
