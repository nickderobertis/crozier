

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LessonPreloadResponseGenerationsItemChapter(UniversalBaseModel):
    chapter_id: typing_extensions.Annotated[str, FieldMetadata(alias="chapterId"), pydantic.Field(alias="chapterId")]
    generation_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="generationId"), pydantic.Field(alias="generationId")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
