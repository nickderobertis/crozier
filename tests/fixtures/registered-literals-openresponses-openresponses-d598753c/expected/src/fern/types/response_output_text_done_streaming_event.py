

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .log_prob import LogProb
from .response_output_text_done_streaming_event_type import ResponseOutputTextDoneStreamingEventType


class ResponseOutputTextDoneStreamingEvent(UniversalBaseModel):
    """
    A streaming event that indicated output text was completed.
    """

    type: ResponseOutputTextDoneStreamingEventType = pydantic.Field()
    """
    The type of the event, always `response.output_text.done`.
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

    text: str = pydantic.Field()
    """
    The final text that was emitted.
    """

    logprobs: typing.Optional[typing.List[LogProb]] = pydantic.Field(default=None)
    """
    The token log probabilities that were emitted with the final text, if any.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
