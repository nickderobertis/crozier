

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class NextLessonChapterResponse(UniversalBaseModel):
    can_prefetch: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="canPrefetch"),
        pydantic.Field(alias="canPrefetch", description="Whether the next lesson can be prefetched"),
    ]
    """
    Whether the next lesson can be prefetched
    """

    chapter_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="chapterId"), pydantic.Field(alias="chapterId", description="Chapter ID")
    ]
    """
    Chapter ID
    """

    chapter_slug: typing_extensions.Annotated[
        str, FieldMetadata(alias="chapterSlug"), pydantic.Field(alias="chapterSlug", description="Chapter slug")
    ]
    """
    Chapter slug
    """

    completed: bool = pydantic.Field()
    """
    Whether all lessons are completed
    """

    course_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="courseId"), pydantic.Field(alias="courseId", description="Course ID")
    ]
    """
    Course ID
    """

    course_slug: typing_extensions.Annotated[
        str, FieldMetadata(alias="courseSlug"), pydantic.Field(alias="courseSlug", description="Course slug")
    ]
    """
    Course slug
    """

    has_started: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="hasStarted"),
        pydantic.Field(alias="hasStarted", description="Whether the user has started"),
    ]
    """
    Whether the user has started
    """

    organization_slug: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="organizationSlug"),
        pydantic.Field(alias="organizationSlug", description="Organization slug"),
    ]
    """
    Organization slug
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
