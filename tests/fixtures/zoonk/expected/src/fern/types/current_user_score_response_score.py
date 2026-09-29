

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .current_user_score_response_score_data_points_item import CurrentUserScoreResponseScoreDataPointsItem


class CurrentUserScoreResponseScore(UniversalBaseModel):
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
    data_points: typing_extensions.Annotated[
        typing.List[CurrentUserScoreResponseScoreDataPointsItem],
        FieldMetadata(alias="dataPoints"),
        pydantic.Field(alias="dataPoints"),
    ]
    period_end: typing_extensions.Annotated[
        dt.date,
        FieldMetadata(alias="periodEnd"),
        pydantic.Field(alias="periodEnd", description="Learner-local calendar date without a time or UTC offset"),
    ]
    """
    Learner-local calendar date without a time or UTC offset
    """

    period_start: typing_extensions.Annotated[
        dt.date,
        FieldMetadata(alias="periodStart"),
        pydantic.Field(alias="periodStart", description="Learner-local calendar date without a time or UTC offset"),
    ]
    """
    Learner-local calendar date without a time or UTC offset
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
