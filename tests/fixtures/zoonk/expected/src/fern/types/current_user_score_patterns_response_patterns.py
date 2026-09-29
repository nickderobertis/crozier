

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .current_user_score_patterns_response_patterns_strongest_time import (
    CurrentUserScorePatternsResponsePatternsStrongestTime,
)
from .current_user_score_patterns_response_patterns_strongest_weekday import (
    CurrentUserScorePatternsResponsePatternsStrongestWeekday,
)
from .current_user_score_patterns_response_patterns_times_item import CurrentUserScorePatternsResponsePatternsTimesItem
from .current_user_score_patterns_response_patterns_weekdays_item import (
    CurrentUserScorePatternsResponsePatternsWeekdaysItem,
)


class CurrentUserScorePatternsResponsePatterns(UniversalBaseModel):
    strongest_time: typing_extensions.Annotated[
        typing.Optional[CurrentUserScorePatternsResponsePatternsStrongestTime],
        FieldMetadata(alias="strongestTime"),
        pydantic.Field(alias="strongestTime"),
    ] = None
    strongest_weekday: typing_extensions.Annotated[
        typing.Optional[CurrentUserScorePatternsResponsePatternsStrongestWeekday],
        FieldMetadata(alias="strongestWeekday"),
        pydantic.Field(alias="strongestWeekday"),
    ] = None
    times: typing.List[CurrentUserScorePatternsResponsePatternsTimesItem]
    weekdays: typing.List[CurrentUserScorePatternsResponsePatternsWeekdaysItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
