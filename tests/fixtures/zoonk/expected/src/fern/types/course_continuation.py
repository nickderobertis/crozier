

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .course_continuation_pending_chapter import CourseContinuationPendingChapter
from .course_continuation_pending_course import CourseContinuationPendingCourse
from .course_continuation_pending_lesson import CourseContinuationPendingLesson
from .course_continuation_ready_chapter import CourseContinuationReadyChapter
from .course_continuation_ready_course import CourseContinuationReadyCourse
from .course_continuation_ready_lesson import CourseContinuationReadyLesson


class CourseContinuation_Ready(UniversalBaseModel):
    status: typing.Literal["ready"] = "ready"
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


class CourseContinuation_Pending(UniversalBaseModel):
    status: typing.Literal["pending"] = "pending"
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


CourseContinuation = typing_extensions.Annotated[
    typing.Union[CourseContinuation_Ready, CourseContinuation_Pending], pydantic.Field(discriminator="status")
]
