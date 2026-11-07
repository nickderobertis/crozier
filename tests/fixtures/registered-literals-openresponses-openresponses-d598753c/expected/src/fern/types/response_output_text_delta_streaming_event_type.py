

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResponseOutputTextDeltaStreamingEventType(enum.StrEnum):
    """
    The type of the event, always `response.output_text.delta`.
    """

    RESPONSE_OUTPUT_TEXT_DELTA = "response.output_text.delta"

    def visit(self, response_output_text_delta: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResponseOutputTextDeltaStreamingEventType.RESPONSE_OUTPUT_TEXT_DELTA:
            return response_output_text_delta()
