

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .response_incomplete_streaming_event_response_text_format import ResponseIncompleteStreamingEventResponseTextFormat
from .verbosity_enum import VerbosityEnum


class ResponseIncompleteStreamingEventResponseText(UniversalBaseModel):
    """
    Configuration options for text output that were used.
    """

    format: ResponseIncompleteStreamingEventResponseTextFormat
    verbosity: typing.Optional[VerbosityEnum] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
