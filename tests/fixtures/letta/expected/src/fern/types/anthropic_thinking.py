

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .anthropic_thinking_type import AnthropicThinkingType


class AnthropicThinking(UniversalBaseModel):
    type: typing.Optional[AnthropicThinkingType] = pydantic.Field(default=None)
    """
    The type of thinking to use.
    """

    budget_tokens: typing.Optional[int] = pydantic.Field(default=None)
    """
    The maximum number of tokens the model can use for extended thinking.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
