

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .assistant_message_tokens_cache import AssistantMessageTokensCache


class AssistantMessageTokens(UniversalBaseModel):
    input: float
    output: float
    reasoning: float
    cache: AssistantMessageTokensCache

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
