

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResponseContentPartDoneStreamingEventType(enum.StrEnum):
    """
    The type of the event, always `response.content_part.done`.
    """

    RESPONSE_CONTENT_PART_DONE = "response.content_part.done"

    def visit(self, response_content_part_done: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResponseContentPartDoneStreamingEventType.RESPONSE_CONTENT_PART_DONE:
            return response_content_part_done()
