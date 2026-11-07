

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .response_incomplete_streaming_event_response import ResponseIncompleteStreamingEventResponse
from .response_incomplete_streaming_event_type import ResponseIncompleteStreamingEventType


class ResponseIncompleteStreamingEvent(UniversalBaseModel):
    """
    A streaming event that indicated the response was incomplete.
    """

    type: ResponseIncompleteStreamingEventType = pydantic.Field()
    """
    The type of the event, always `response.incomplete`.
    """

    sequence_number: int = pydantic.Field()
    """
    The sequence number of the event that was emitted.
    """

    response: ResponseIncompleteStreamingEventResponse = pydantic.Field()
    """
    The response snapshot that was emitted with the event.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
