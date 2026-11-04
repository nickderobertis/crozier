

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .response_output_item_added_streaming_event_item import ResponseOutputItemAddedStreamingEventItem
from .response_output_item_added_streaming_event_type import ResponseOutputItemAddedStreamingEventType


class ResponseOutputItemAddedStreamingEvent(UniversalBaseModel):
    """
    A streaming event that indicated an output item was added to the response.
    """

    type: ResponseOutputItemAddedStreamingEventType = pydantic.Field()
    """
    The type of the event, always `response.output_item.added`.
    """

    sequence_number: int = pydantic.Field()
    """
    The sequence number of the event that was emitted.
    """

    output_index: int = pydantic.Field()
    """
    The index of the output item that was added.
    """

    item: typing.Optional[ResponseOutputItemAddedStreamingEventItem] = pydantic.Field(default=None)
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
