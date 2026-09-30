

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .current_user_progress_response_score_patterns_strongest_time import (
    CurrentUserProgressResponseScorePatternsStrongestTime,
)
from .current_user_progress_response_score_patterns_strongest_weekday import (
    CurrentUserProgressResponseScorePatternsStrongestWeekday,
)


class CurrentUserProgressResponseScorePatterns(UniversalBaseModel):
    strongest_time: typing_extensions.Annotated[
        typing.Optional[CurrentUserProgressResponseScorePatternsStrongestTime],
        FieldMetadata(alias="strongestTime"),
        pydantic.Field(alias="strongestTime"),
    ] = None
    strongest_weekday: typing_extensions.Annotated[
        typing.Optional[CurrentUserProgressResponseScorePatternsStrongestWeekday],
        FieldMetadata(alias="strongestWeekday"),
        pydantic.Field(alias="strongestWeekday"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
