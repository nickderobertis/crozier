

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .llm_choice import LlmChoice
from .llm_token_usage import LlmTokenUsage


class LlmResponse(UniversalBaseModel):
    id: str
    model: str
    created: int
    usage: LlmTokenUsage
    choices: typing.List[LlmChoice]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
