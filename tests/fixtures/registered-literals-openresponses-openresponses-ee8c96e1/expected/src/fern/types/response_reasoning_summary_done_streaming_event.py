

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .response_reasoning_summary_done_streaming_event_type import ResponseReasoningSummaryDoneStreamingEventType


class ResponseReasoningSummaryDoneStreamingEvent(UniversalBaseModel):
    """
    A streaming event that indicated a reasoning summary was completed.
    """

    type: ResponseReasoningSummaryDoneStreamingEventType = pydantic.Field()
    """
    The type of the event, always `response.reasoning_summary.done`.
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
    The index of the summary content that was completed.
    """

    text: str = pydantic.Field()
    """
    The final summary text that was emitted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
