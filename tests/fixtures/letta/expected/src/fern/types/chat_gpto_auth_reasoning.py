

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_gpto_auth_reasoning_reasoning_effort import ChatGptoAuthReasoningReasoningEffort


class ChatGptoAuthReasoning(UniversalBaseModel):
    """
    Reasoning configuration for ChatGPT OAuth models (GPT-5.x, o-series).
    """

    reasoning_effort: typing.Optional[ChatGptoAuthReasoningReasoningEffort] = pydantic.Field(default=None)
    """
    The reasoning effort level for GPT-5.x and o-series models.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
