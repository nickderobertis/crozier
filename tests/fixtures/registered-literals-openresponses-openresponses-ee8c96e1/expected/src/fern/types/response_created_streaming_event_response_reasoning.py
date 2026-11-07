

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .reasoning_effort_enum import ReasoningEffortEnum
from .response_created_streaming_event_response_reasoning_summary import (
    ResponseCreatedStreamingEventResponseReasoningSummary,
)


class ResponseCreatedStreamingEventResponseReasoning(UniversalBaseModel):
    """
    Reasoning configuration and outputs that were produced for this response.
    """

    effort: typing.Optional[ReasoningEffortEnum] = None
    summary: typing.Optional[ResponseCreatedStreamingEventResponseReasoningSummary] = pydantic.Field(default=None)
    """
    A model-generated summary of its reasoning that was produced, if available.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
