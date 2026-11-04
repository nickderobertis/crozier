

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .response_in_progress_streaming_event_response_text_format import (
    ResponseInProgressStreamingEventResponseTextFormat,
)
from .verbosity_enum import VerbosityEnum


class ResponseInProgressStreamingEventResponseText(UniversalBaseModel):
    """
    Configuration options for text output that were used.
    """

    format: ResponseInProgressStreamingEventResponseTextFormat
    verbosity: typing.Optional[VerbosityEnum] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
