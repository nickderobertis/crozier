

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .lesson_successor_response_lesson_lesson_generation_status import (
    LessonSuccessorResponseLessonLessonGenerationStatus,
)
from .lesson_successor_response_lesson_lesson_kind import LessonSuccessorResponseLessonLessonKind


class LessonSuccessorResponseLesson(UniversalBaseModel):
    chapter_id: typing_extensions.Annotated[str, FieldMetadata(alias="chapterId"), pydantic.Field(alias="chapterId")]
    chapter_position: typing_extensions.Annotated[
        int, FieldMetadata(alias="chapterPosition"), pydantic.Field(alias="chapterPosition")
    ]
    chapter_slug: typing_extensions.Annotated[
        str, FieldMetadata(alias="chapterSlug"), pydantic.Field(alias="chapterSlug")
    ]
    chapter_title: typing_extensions.Annotated[
        str, FieldMetadata(alias="chapterTitle"), pydantic.Field(alias="chapterTitle")
    ]
    lesson_description: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="lessonDescription"), pydantic.Field(alias="lessonDescription")
    ] = None
    lesson_generation_status: typing_extensions.Annotated[
        LessonSuccessorResponseLessonLessonGenerationStatus,
        FieldMetadata(alias="lessonGenerationStatus"),
        pydantic.Field(alias="lessonGenerationStatus"),
    ]
    lesson_id: typing_extensions.Annotated[str, FieldMetadata(alias="lessonId"), pydantic.Field(alias="lessonId")]
    lesson_kind: typing_extensions.Annotated[
        LessonSuccessorResponseLessonLessonKind, FieldMetadata(alias="lessonKind"), pydantic.Field(alias="lessonKind")
    ]
    lesson_position: typing_extensions.Annotated[
        int, FieldMetadata(alias="lessonPosition"), pydantic.Field(alias="lessonPosition")
    ]
    lesson_slug: typing_extensions.Annotated[str, FieldMetadata(alias="lessonSlug"), pydantic.Field(alias="lessonSlug")]
    lesson_title: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="lessonTitle"), pydantic.Field(alias="lessonTitle")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
