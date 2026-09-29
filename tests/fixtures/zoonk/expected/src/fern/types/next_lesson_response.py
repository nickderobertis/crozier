

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class NextLessonResponse_Chapter(UniversalBaseModel):
    type: typing.Literal["chapter"] = "chapter"
    can_prefetch: typing_extensions.Annotated[
        bool, FieldMetadata(alias="canPrefetch"), pydantic.Field(alias="canPrefetch")
    ]
    chapter_id: typing_extensions.Annotated[str, FieldMetadata(alias="chapterId"), pydantic.Field(alias="chapterId")]
    chapter_slug: typing_extensions.Annotated[
        str, FieldMetadata(alias="chapterSlug"), pydantic.Field(alias="chapterSlug")
    ]
    completed: bool
    course_id: typing_extensions.Annotated[str, FieldMetadata(alias="courseId"), pydantic.Field(alias="courseId")]
    course_slug: typing_extensions.Annotated[str, FieldMetadata(alias="courseSlug"), pydantic.Field(alias="courseSlug")]
    has_started: typing_extensions.Annotated[
        bool, FieldMetadata(alias="hasStarted"), pydantic.Field(alias="hasStarted")
    ]
    organization_slug: typing_extensions.Annotated[
        str, FieldMetadata(alias="organizationSlug"), pydantic.Field(alias="organizationSlug")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class NextLessonResponse_Empty(UniversalBaseModel):
    type: typing.Literal["empty"] = "empty"
    completed: bool
    has_started: typing_extensions.Annotated[
        bool, FieldMetadata(alias="hasStarted"), pydantic.Field(alias="hasStarted")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class NextLessonResponse_Lesson(UniversalBaseModel):
    type: typing.Literal["lesson"] = "lesson"
    can_prefetch: typing_extensions.Annotated[
        bool, FieldMetadata(alias="canPrefetch"), pydantic.Field(alias="canPrefetch")
    ]
    chapter_id: typing_extensions.Annotated[str, FieldMetadata(alias="chapterId"), pydantic.Field(alias="chapterId")]
    chapter_slug: typing_extensions.Annotated[
        str, FieldMetadata(alias="chapterSlug"), pydantic.Field(alias="chapterSlug")
    ]
    completed: bool
    course_id: typing_extensions.Annotated[str, FieldMetadata(alias="courseId"), pydantic.Field(alias="courseId")]
    course_slug: typing_extensions.Annotated[str, FieldMetadata(alias="courseSlug"), pydantic.Field(alias="courseSlug")]
    has_started: typing_extensions.Annotated[
        bool, FieldMetadata(alias="hasStarted"), pydantic.Field(alias="hasStarted")
    ]
    lesson_id: typing_extensions.Annotated[str, FieldMetadata(alias="lessonId"), pydantic.Field(alias="lessonId")]
    lesson_position: typing_extensions.Annotated[
        int, FieldMetadata(alias="lessonPosition"), pydantic.Field(alias="lessonPosition")
    ]
    lesson_slug: typing_extensions.Annotated[str, FieldMetadata(alias="lessonSlug"), pydantic.Field(alias="lessonSlug")]
    organization_slug: typing_extensions.Annotated[
        str, FieldMetadata(alias="organizationSlug"), pydantic.Field(alias="organizationSlug")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


NextLessonResponse = typing_extensions.Annotated[
    typing.Union[NextLessonResponse_Chapter, NextLessonResponse_Empty, NextLessonResponse_Lesson],
    pydantic.Field(discriminator="type"),
]
