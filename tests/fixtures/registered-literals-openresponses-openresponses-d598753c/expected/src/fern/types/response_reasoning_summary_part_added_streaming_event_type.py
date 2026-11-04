

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResponseReasoningSummaryPartAddedStreamingEventType(enum.StrEnum):
    """
    The type of the event, always `response.reasoning_summary_part.added`.
    """

    RESPONSE_REASONING_SUMMARY_PART_ADDED = "response.reasoning_summary_part.added"

    def visit(self, response_reasoning_summary_part_added: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResponseReasoningSummaryPartAddedStreamingEventType.RESPONSE_REASONING_SUMMARY_PART_ADDED:
            return response_reasoning_summary_part_added()
