

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .lesson_resource_generation_status import LessonResourceGenerationStatus
from .lesson_resource_kind import LessonResourceKind


class LessonResource(UniversalBaseModel):
    chapter_id: typing_extensions.Annotated[str, FieldMetadata(alias="chapterId"), pydantic.Field(alias="chapterId")]
    course_id: typing_extensions.Annotated[str, FieldMetadata(alias="courseId"), pydantic.Field(alias="courseId")]
    description: typing.Optional[str] = None
    generation_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="generationId"), pydantic.Field(alias="generationId")
    ] = None
    generation_status: typing_extensions.Annotated[
        LessonResourceGenerationStatus,
        FieldMetadata(alias="generationStatus"),
        pydantic.Field(alias="generationStatus"),
    ]
    id: str
    image_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="imageUrl"), pydantic.Field(alias="imageUrl")
    ] = None
    kind: LessonResourceKind
    language: str
    position: int
    slug: str
    title: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
