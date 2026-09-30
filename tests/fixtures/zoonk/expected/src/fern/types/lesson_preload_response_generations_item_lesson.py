

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LessonPreloadResponseGenerationsItemLesson(UniversalBaseModel):
    generation_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="generationId"), pydantic.Field(alias="generationId")
    ]
    lesson_id: typing_extensions.Annotated[str, FieldMetadata(alias="lessonId"), pydantic.Field(alias="lessonId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
