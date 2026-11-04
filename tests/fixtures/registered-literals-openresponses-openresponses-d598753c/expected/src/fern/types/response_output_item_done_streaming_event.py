

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .response_output_item_done_streaming_event_item import ResponseOutputItemDoneStreamingEventItem
from .response_output_item_done_streaming_event_type import ResponseOutputItemDoneStreamingEventType


class ResponseOutputItemDoneStreamingEvent(UniversalBaseModel):
    """
    A streaming event that indicated an output item was completed.
    """

    type: ResponseOutputItemDoneStreamingEventType = pydantic.Field()
    """
    The type of the event, always `response.output_item.done`.
    """

    sequence_number: int = pydantic.Field()
    """
    The sequence number of the event that was emitted.
    """

    output_index: int = pydantic.Field()
    """
    The index of the output item that was completed.
    """

    item: typing.Optional[ResponseOutputItemDoneStreamingEventItem] = pydantic.Field(default=None)
    """
    An item representing a message, tool call, tool output, reasoning, or other response element.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
