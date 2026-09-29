

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .course_continuation_pending_lesson_kind import CourseContinuationPendingLessonKind


class CourseContinuationPendingLesson(UniversalBaseModel):
    description: typing.Optional[str] = None
    id: str
    kind: CourseContinuationPendingLessonKind
    slug: str
    title: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
