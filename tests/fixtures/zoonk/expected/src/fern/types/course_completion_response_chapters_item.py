

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CourseCompletionResponseChaptersItem(UniversalBaseModel):
    chapter_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="chapterId"), pydantic.Field(alias="chapterId", description="Chapter ID")
    ]
    """
    Chapter ID
    """

    completed_lessons: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="completedLessons"),
        pydantic.Field(alias="completedLessons", description="Number of completed lessons"),
    ]
    """
    Number of completed lessons
    """

    total_lessons: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="totalLessons"),
        pydantic.Field(alias="totalLessons", description="Total number of lessons"),
    ]
    """
    Total number of lessons
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
