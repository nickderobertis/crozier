

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .open_ai_reasoning_reasoning_effort import OpenAiReasoningReasoningEffort


class OpenAiReasoning(UniversalBaseModel):
    reasoning_effort: typing.Optional[OpenAiReasoningReasoningEffort] = pydantic.Field(default=None)
    """
    The reasoning effort to use when generating text reasoning models
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
