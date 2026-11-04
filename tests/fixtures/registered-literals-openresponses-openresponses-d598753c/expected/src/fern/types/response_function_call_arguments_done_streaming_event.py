

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .response_function_call_arguments_done_streaming_event_type import (
    ResponseFunctionCallArgumentsDoneStreamingEventType,
)


class ResponseFunctionCallArgumentsDoneStreamingEvent(UniversalBaseModel):
    """
    A streaming event that indicated function call arguments were completed.
    """

    type: ResponseFunctionCallArgumentsDoneStreamingEventType = pydantic.Field()
    """
    The type of the event, always `response.function_call_arguments.done`.
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

    arguments: str = pydantic.Field()
    """
    The final arguments string that was emitted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
