

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .lesson_question_context_input_answer_answer import LessonQuestionContextInputAnswerAnswer


class LessonQuestionContextInput_Lesson(UniversalBaseModel):
    kind: typing.Literal["lesson"] = "lesson"
    step_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="stepIds"), pydantic.Field(alias="stepIds")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LessonQuestionContextInput_Step(UniversalBaseModel):
    kind: typing.Literal["step"] = "step"
    step_id: typing_extensions.Annotated[str, FieldMetadata(alias="stepId"), pydantic.Field(alias="stepId")]
    step_number: typing_extensions.Annotated[int, FieldMetadata(alias="stepNumber"), pydantic.Field(alias="stepNumber")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LessonQuestionContextInput_Answer(UniversalBaseModel):
    kind: typing.Literal["answer"] = "answer"
    answer: LessonQuestionContextInputAnswerAnswer
    step_id: typing_extensions.Annotated[str, FieldMetadata(alias="stepId"), pydantic.Field(alias="stepId")]
    step_number: typing_extensions.Annotated[int, FieldMetadata(alias="stepNumber"), pydantic.Field(alias="stepNumber")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


LessonQuestionContextInput = typing_extensions.Annotated[
    typing.Union[LessonQuestionContextInput_Lesson, LessonQuestionContextInput_Step, LessonQuestionContextInput_Answer],
    pydantic.Field(discriminator="kind"),
]
