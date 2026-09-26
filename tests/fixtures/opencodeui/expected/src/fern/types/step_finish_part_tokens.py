

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .step_finish_part_tokens_cache import StepFinishPartTokensCache


class StepFinishPartTokens(UniversalBaseModel):
    input: float
    output: float
    reasoning: float
    cache: StepFinishPartTokensCache

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
