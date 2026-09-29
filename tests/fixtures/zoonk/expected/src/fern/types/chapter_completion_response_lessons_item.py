

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ChapterCompletionResponseLessonsItem(UniversalBaseModel):
    is_completed: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isCompleted"),
        pydantic.Field(alias="isCompleted", description="Whether the lesson is completed"),
    ]
    """
    Whether the lesson is completed
    """

    lesson_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="lessonId"), pydantic.Field(alias="lessonId", description="Lesson ID")
    ]
    """
    Lesson ID
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
