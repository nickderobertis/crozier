

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResponseOutputItemAddedStreamingEventType(enum.StrEnum):
    """
    The type of the event, always `response.output_item.added`.
    """

    RESPONSE_OUTPUT_ITEM_ADDED = "response.output_item.added"

    def visit(self, response_output_item_added: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResponseOutputItemAddedStreamingEventType.RESPONSE_OUTPUT_ITEM_ADDED:
            return response_output_item_added()
