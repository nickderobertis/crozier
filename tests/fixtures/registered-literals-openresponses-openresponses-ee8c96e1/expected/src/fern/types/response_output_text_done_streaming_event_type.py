

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResponseOutputTextDoneStreamingEventType(enum.StrEnum):
    """
    The type of the event, always `response.output_text.done`.
    """

    RESPONSE_OUTPUT_TEXT_DONE = "response.output_text.done"

    def visit(self, response_output_text_done: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResponseOutputTextDoneStreamingEventType.RESPONSE_OUTPUT_TEXT_DONE:
            return response_output_text_done()
