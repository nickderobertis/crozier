

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .lesson_content_response_ready_lesson import LessonContentResponseReadyLesson
from .lesson_generation_target import LessonGenerationTarget


class LessonContentResponse_Ready(UniversalBaseModel):
    status: typing.Literal["ready"] = "ready"
    lesson: LessonContentResponseReadyLesson

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LessonContentResponse_NotGenerated(UniversalBaseModel):
    status: typing.Literal["notGenerated"] = "notGenerated"
    generation_target: typing_extensions.Annotated[
        typing.Optional[LessonGenerationTarget],
        FieldMetadata(alias="generationTarget"),
        pydantic.Field(alias="generationTarget"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LessonContentResponse_ReviewEmpty(UniversalBaseModel):
    status: typing.Literal["reviewEmpty"] = "reviewEmpty"
    generation_lesson_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="generationLessonId"), pydantic.Field(alias="generationLessonId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


LessonContentResponse = typing_extensions.Annotated[
    typing.Union[LessonContentResponse_Ready, LessonContentResponse_NotGenerated, LessonContentResponse_ReviewEmpty],
    pydantic.Field(discriminator="status"),
]
