

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResponseReasoningSummaryPartDoneStreamingEventType(enum.StrEnum):
    """
    The type of the event, always `response.reasoning_summary_part.done`.
    """

    RESPONSE_REASONING_SUMMARY_PART_DONE = "response.reasoning_summary_part.done"

    def visit(self, response_reasoning_summary_part_done: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResponseReasoningSummaryPartDoneStreamingEventType.RESPONSE_REASONING_SUMMARY_PART_DONE:
            return response_reasoning_summary_part_done()
