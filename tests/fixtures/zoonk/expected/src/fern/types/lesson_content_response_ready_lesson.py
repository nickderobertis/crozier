

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .lesson_content_response_ready_lesson_kind import LessonContentResponseReadyLessonKind
from .lesson_content_response_ready_lesson_lesson_sentences_item import (
    LessonContentResponseReadyLessonLessonSentencesItem,
)
from .lesson_content_response_ready_lesson_lesson_words_item import LessonContentResponseReadyLessonLessonWordsItem
from .lesson_content_response_ready_lesson_steps_item import LessonContentResponseReadyLessonStepsItem


class LessonContentResponseReadyLesson(UniversalBaseModel):
    description: typing.Optional[str] = None
    id: str
    kind: LessonContentResponseReadyLessonKind
    language: str
    lesson_sentences: typing_extensions.Annotated[
        typing.List[LessonContentResponseReadyLessonLessonSentencesItem],
        FieldMetadata(alias="lessonSentences"),
        pydantic.Field(alias="lessonSentences"),
    ]
    lesson_words: typing_extensions.Annotated[
        typing.List[LessonContentResponseReadyLessonLessonWordsItem],
        FieldMetadata(alias="lessonWords"),
        pydantic.Field(alias="lessonWords"),
    ]
    organization_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="organizationId"), pydantic.Field(alias="organizationId")
    ] = None
    steps: typing.List[LessonContentResponseReadyLessonStepsItem]
    title: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
