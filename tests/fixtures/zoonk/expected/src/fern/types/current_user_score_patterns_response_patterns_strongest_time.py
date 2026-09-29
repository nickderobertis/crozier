

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .current_user_score_patterns_response_patterns_strongest_time_period import (
    CurrentUserScorePatternsResponsePatternsStrongestTimePeriod,
)


class CurrentUserScorePatternsResponsePatternsStrongestTime(UniversalBaseModel):
    correct_answers: typing_extensions.Annotated[
        int, FieldMetadata(alias="correctAnswers"), pydantic.Field(alias="correctAnswers")
    ]
    incorrect_answers: typing_extensions.Annotated[
        int, FieldMetadata(alias="incorrectAnswers"), pydantic.Field(alias="incorrectAnswers")
    ]
    score: float
    total_answers: typing_extensions.Annotated[
        int, FieldMetadata(alias="totalAnswers"), pydantic.Field(alias="totalAnswers")
    ]
    period: CurrentUserScorePatternsResponsePatternsStrongestTimePeriod

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
