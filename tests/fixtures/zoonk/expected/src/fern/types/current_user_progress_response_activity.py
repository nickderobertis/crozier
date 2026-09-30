

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CurrentUserProgressResponseActivity(UniversalBaseModel):
    learning_days: typing_extensions.Annotated[
        int, FieldMetadata(alias="learningDays"), pydantic.Field(alias="learningDays")
    ]
    total_learning_seconds: typing_extensions.Annotated[
        int, FieldMetadata(alias="totalLearningSeconds"), pydantic.Field(alias="totalLearningSeconds")
    ]
    total_lesson_completions: typing_extensions.Annotated[
        int, FieldMetadata(alias="totalLessonCompletions"), pydantic.Field(alias="totalLessonCompletions")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
