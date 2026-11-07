

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .response_function_call_arguments_delta_streaming_event_type import (
    ResponseFunctionCallArgumentsDeltaStreamingEventType,
)


class ResponseFunctionCallArgumentsDeltaStreamingEvent(UniversalBaseModel):
    """
    A streaming event that indicated function call arguments were incrementally added.
    """

    type: ResponseFunctionCallArgumentsDeltaStreamingEventType = pydantic.Field()
    """
    The type of the event, always `response.function_call_arguments.delta`.
    """

    sequence_number: int = pydantic.Field()
    """
    The sequence number of the event that was emitted.
    """

    item_id: str = pydantic.Field()
    """
    The ID of the tool call item that was updated.
    """

    output_index: int = pydantic.Field()
    """
    The index of the output item that was updated.
    """

    delta: str = pydantic.Field()
    """
    The arguments delta that was appended.
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
