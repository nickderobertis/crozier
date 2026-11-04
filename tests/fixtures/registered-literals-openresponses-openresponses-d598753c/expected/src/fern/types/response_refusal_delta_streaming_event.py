

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .response_refusal_delta_streaming_event_type import ResponseRefusalDeltaStreamingEventType


class ResponseRefusalDeltaStreamingEvent(UniversalBaseModel):
    """
    A streaming event that indicated refusal text was incrementally added.
    """

    type: ResponseRefusalDeltaStreamingEventType = pydantic.Field()
    """
    The type of the event, always `response.refusal.delta`.
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
    The index of the refusal content that was updated.
    """

    delta: str = pydantic.Field()
    """
    The refusal text delta that was appended.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
