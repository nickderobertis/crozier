

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .course_continuation_ready_lesson_kind import CourseContinuationReadyLessonKind


class CourseContinuationReadyLesson(UniversalBaseModel):
    description: typing.Optional[str] = None
    id: str
    kind: CourseContinuationReadyLessonKind
    slug: str
    title: typing.Optional[str] = None
    position: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
