

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_response_body_reasoning_summary import CreateResponseBodyReasoningSummary
from .reasoning_effort_enum import ReasoningEffortEnum


class CreateResponseBodyReasoning(UniversalBaseModel):
    """
    Configuration options for reasoning behavior.
    """

    effort: typing.Optional[ReasoningEffortEnum] = None
    summary: typing.Optional[CreateResponseBodyReasoningSummary] = pydantic.Field(default=None)
    """
    Controls whether the response includes a reasoning summary.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
