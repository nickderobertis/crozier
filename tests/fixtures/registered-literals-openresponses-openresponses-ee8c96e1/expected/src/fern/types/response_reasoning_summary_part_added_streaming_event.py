

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .response_reasoning_summary_part_added_streaming_event_part import (
    ResponseReasoningSummaryPartAddedStreamingEventPart,
)
from .response_reasoning_summary_part_added_streaming_event_type import (
    ResponseReasoningSummaryPartAddedStreamingEventType,
)


class ResponseReasoningSummaryPartAddedStreamingEvent(UniversalBaseModel):
    """
    A streaming event that indicated a reasoning summary part was added.
    """

    type: ResponseReasoningSummaryPartAddedStreamingEventType = pydantic.Field()
    """
    The type of the event, always `response.reasoning_summary_part.added`.
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

    summary_index: int = pydantic.Field()
    """
    The index of the summary part that was added.
    """

    part: ResponseReasoningSummaryPartAddedStreamingEventPart = pydantic.Field()
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
