

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResponseOutputItemDoneStreamingEventType(enum.StrEnum):
    """
    The type of the event, always `response.output_item.done`.
    """

    RESPONSE_OUTPUT_ITEM_DONE = "response.output_item.done"

    def visit(self, response_output_item_done: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResponseOutputItemDoneStreamingEventType.RESPONSE_OUTPUT_ITEM_DONE:
            return response_output_item_done()
