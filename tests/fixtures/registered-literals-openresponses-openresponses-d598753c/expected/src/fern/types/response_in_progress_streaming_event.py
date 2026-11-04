

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .response_in_progress_streaming_event_response import ResponseInProgressStreamingEventResponse
from .response_in_progress_streaming_event_type import ResponseInProgressStreamingEventType


class ResponseInProgressStreamingEvent(UniversalBaseModel):
    """
    A streaming event that indicated the response was in progress.
    """

    type: ResponseInProgressStreamingEventType = pydantic.Field()
    """
    The type of the event, always `response.in_progress`.
    """

    sequence_number: int = pydantic.Field()
    """
    The sequence number of the event that was emitted.
    """

    response: ResponseInProgressStreamingEventResponse = pydantic.Field()
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
