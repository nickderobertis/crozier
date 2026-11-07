

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .response_reasoning_summary_delta_streaming_event_type import ResponseReasoningSummaryDeltaStreamingEventType


class ResponseReasoningSummaryDeltaStreamingEvent(UniversalBaseModel):
    """
    A streaming event that indicated a reasoning summary was incrementally added.
    """

    type: ResponseReasoningSummaryDeltaStreamingEventType = pydantic.Field()
    """
    The type of the event, always `response.reasoning_summary.delta`.
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
    The index of the summary content that was updated.
    """

    delta: str = pydantic.Field()
    """
    The summary text delta that was appended.
    """

    obfuscation: typing.Optional[str] = pydantic.Field(default=None)
    """
    An obfuscation string that was added to pad the event payload.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
