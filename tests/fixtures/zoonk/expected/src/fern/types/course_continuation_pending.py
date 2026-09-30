

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .course_continuation_pending_chapter import CourseContinuationPendingChapter
from .course_continuation_pending_course import CourseContinuationPendingCourse
from .course_continuation_pending_lesson import CourseContinuationPendingLesson


class CourseContinuationPending(UniversalBaseModel):
    chapter: CourseContinuationPendingChapter
    course: CourseContinuationPendingCourse
    lesson: typing.Optional[CourseContinuationPendingLesson] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
