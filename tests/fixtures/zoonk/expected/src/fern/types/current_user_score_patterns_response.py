

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .current_user_score_patterns_response_patterns import CurrentUserScorePatternsResponsePatterns


class CurrentUserScorePatternsResponse(UniversalBaseModel):
    patterns: typing.Optional[CurrentUserScorePatternsResponsePatterns] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
