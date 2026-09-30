

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .course_continuation_ready_chapter import CourseContinuationReadyChapter
from .course_continuation_ready_course import CourseContinuationReadyCourse
from .course_continuation_ready_lesson import CourseContinuationReadyLesson


class CourseContinuationReady(UniversalBaseModel):
    chapter: CourseContinuationReadyChapter
    course: CourseContinuationReadyCourse
    lesson: CourseContinuationReadyLesson

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
