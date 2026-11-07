

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .response_content_part_done_streaming_event_part import ResponseContentPartDoneStreamingEventPart
from .response_content_part_done_streaming_event_type import ResponseContentPartDoneStreamingEventType


class ResponseContentPartDoneStreamingEvent(UniversalBaseModel):
    """
    A streaming event that indicated a content part was completed.
    """

    type: ResponseContentPartDoneStreamingEventType = pydantic.Field()
    """
    The type of the event, always `response.content_part.done`.
    """

    sequence_number: int = pydantic.Field()
    """
    The sequence number of the event that was emitted.
    """

    item_id: str = pydantic.Field()
    """
    The ID of the item that was updated.
    """

    output_index: int = pydantic.Field()
    """
    The index of the output item that was updated.
    """

    content_index: int = pydantic.Field()
    """
    The index of the content part that was completed.
    """

    part: ResponseContentPartDoneStreamingEventPart = pydantic.Field()
    """
    A content part that makes up an input or output item.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
