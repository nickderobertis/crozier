

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error_streaming_event_error import ErrorStreamingEventError
from .error_streaming_event_type import ErrorStreamingEventType


class ErrorStreamingEvent(UniversalBaseModel):
    """
    A streaming event that indicated an error was emitted.
    """

    type: ErrorStreamingEventType = pydantic.Field()
    """
    The type of the event, always `error`.
    """

    sequence_number: int = pydantic.Field()
    """
    The sequence number of the event that was emitted.
    """

    error: ErrorStreamingEventError = pydantic.Field()
    """
    The error payload that was emitted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
