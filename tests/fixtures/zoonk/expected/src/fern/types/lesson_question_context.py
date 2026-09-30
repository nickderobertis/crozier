

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LessonQuestionContext_Lesson(UniversalBaseModel):
    kind: typing.Literal["lesson"] = "lesson"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LessonQuestionContext_Step(UniversalBaseModel):
    kind: typing.Literal["step"] = "step"
    step_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="stepId"), pydantic.Field(alias="stepId")
    ] = None
    step_number: typing_extensions.Annotated[int, FieldMetadata(alias="stepNumber"), pydantic.Field(alias="stepNumber")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LessonQuestionContext_Answer(UniversalBaseModel):
    kind: typing.Literal["answer"] = "answer"
    step_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="stepId"), pydantic.Field(alias="stepId")
    ] = None
    step_number: typing_extensions.Annotated[int, FieldMetadata(alias="stepNumber"), pydantic.Field(alias="stepNumber")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


LessonQuestionContext = typing_extensions.Annotated[
    typing.Union[LessonQuestionContext_Lesson, LessonQuestionContext_Step, LessonQuestionContext_Answer],
    pydantic.Field(discriminator="kind"),
]
