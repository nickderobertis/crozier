

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResponseContentPartAddedStreamingEventType(enum.StrEnum):
    """
    The type of the event, always `response.content_part.added`.
    """

    RESPONSE_CONTENT_PART_ADDED = "response.content_part.added"

    def visit(self, response_content_part_added: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResponseContentPartAddedStreamingEventType.RESPONSE_CONTENT_PART_ADDED:
            return response_content_part_added()
