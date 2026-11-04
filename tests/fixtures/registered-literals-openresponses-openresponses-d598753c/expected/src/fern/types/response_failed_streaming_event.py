

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .response_failed_streaming_event_response import ResponseFailedStreamingEventResponse
from .response_failed_streaming_event_type import ResponseFailedStreamingEventType


class ResponseFailedStreamingEvent(UniversalBaseModel):
    """
    A streaming event that indicated the response had failed.
    """

    type: ResponseFailedStreamingEventType = pydantic.Field()
    """
    The type of the event, always `response.failed`.
    """

    sequence_number: int = pydantic.Field()
    """
    The sequence number of the event that was emitted.
    """

    response: ResponseFailedStreamingEventResponse = pydantic.Field()
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
