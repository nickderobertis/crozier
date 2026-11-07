

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .response_refusal_done_streaming_event_type import ResponseRefusalDoneStreamingEventType


class ResponseRefusalDoneStreamingEvent(UniversalBaseModel):
    """
    A streaming event that indicated refusal text was completed.
    """

    type: ResponseRefusalDoneStreamingEventType = pydantic.Field()
    """
    The type of the event, always `response.refusal.done`.
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
    The index of the refusal content that was completed.
    """

    refusal: str = pydantic.Field()
    """
    The final refusal text that was emitted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
