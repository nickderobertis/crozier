

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .response_completed_streaming_event_response import ResponseCompletedStreamingEventResponse
from .response_completed_streaming_event_type import ResponseCompletedStreamingEventType


class ResponseCompletedStreamingEvent(UniversalBaseModel):
    """
    A streaming event that indicated the response was completed.
    """

    type: ResponseCompletedStreamingEventType = pydantic.Field()
    """
    The type of the event, always `response.completed`.
    """

    sequence_number: int = pydantic.Field()
    """
    The sequence number of the event that was emitted.
    """

    response: ResponseCompletedStreamingEventResponse = pydantic.Field()
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
