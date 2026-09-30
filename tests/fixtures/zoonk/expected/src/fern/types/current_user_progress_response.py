

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .current_user_progress_response_activity import CurrentUserProgressResponseActivity
from .current_user_progress_response_energy import CurrentUserProgressResponseEnergy
from .current_user_progress_response_level import CurrentUserProgressResponseLevel
from .current_user_progress_response_score import CurrentUserProgressResponseScore
from .current_user_progress_response_score_patterns import CurrentUserProgressResponseScorePatterns


class CurrentUserProgressResponse(UniversalBaseModel):
    activity: CurrentUserProgressResponseActivity
    energy: typing.Optional[CurrentUserProgressResponseEnergy] = None
    level: typing.Optional[CurrentUserProgressResponseLevel] = None
    score: typing.Optional[CurrentUserProgressResponseScore] = None
    score_patterns: typing_extensions.Annotated[
        typing.Optional[CurrentUserProgressResponseScorePatterns],
        FieldMetadata(alias="scorePatterns"),
        pydantic.Field(alias="scorePatterns"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
