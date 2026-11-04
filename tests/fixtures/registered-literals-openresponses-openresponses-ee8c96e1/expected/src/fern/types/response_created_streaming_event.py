

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .response_created_streaming_event_response import ResponseCreatedStreamingEventResponse
from .response_created_streaming_event_type import ResponseCreatedStreamingEventType


class ResponseCreatedStreamingEvent(UniversalBaseModel):
    """
    A streaming event that indicated the response was created.
    """

    type: ResponseCreatedStreamingEventType = pydantic.Field()
    """
    The type of the event, always `response.created`.
    """

    sequence_number: int = pydantic.Field()
    """
    The sequence number of the event that was emitted.
    """

    response: ResponseCreatedStreamingEventResponse = pydantic.Field()
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
