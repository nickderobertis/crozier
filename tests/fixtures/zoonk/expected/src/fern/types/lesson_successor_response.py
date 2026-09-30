

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .lesson_successor_response_lesson import LessonSuccessorResponseLesson


class LessonSuccessorResponse(UniversalBaseModel):
    lesson: typing.Optional[LessonSuccessorResponseLesson] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
