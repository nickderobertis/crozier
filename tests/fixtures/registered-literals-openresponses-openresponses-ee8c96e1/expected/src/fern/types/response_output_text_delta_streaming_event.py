

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .log_prob import LogProb
from .response_output_text_delta_streaming_event_type import ResponseOutputTextDeltaStreamingEventType


class ResponseOutputTextDeltaStreamingEvent(UniversalBaseModel):
    """
    A streaming event that indicated output text was incrementally added.
    """

    type: ResponseOutputTextDeltaStreamingEventType = pydantic.Field()
    """
    The type of the event, always `response.output_text.delta`.
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
    The index of the content part that was updated.
    """

    delta: str = pydantic.Field()
    """
    The text delta that was appended.
    """

    logprobs: typing.List[LogProb] = pydantic.Field()
    """
    The token log probabilities that were emitted with the delta, if any.
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
