

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .response_queued_streaming_event_response import ResponseQueuedStreamingEventResponse
from .response_queued_streaming_event_type import ResponseQueuedStreamingEventType


class ResponseQueuedStreamingEvent(UniversalBaseModel):
    """
    A streaming event that indicated the response was queued.
    """

    type: ResponseQueuedStreamingEventType = pydantic.Field()
    """
    The type of the event, always `response.queued`.
    """

    sequence_number: int = pydantic.Field()
    """
    The sequence number of the event that was emitted.
    """

    response: ResponseQueuedStreamingEventResponse = pydantic.Field()
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
