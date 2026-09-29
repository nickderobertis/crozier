

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .resolve_course_prompt_response_unsupported_course_format import ResolveCoursePromptResponseUnsupportedCourseFormat
from .resolve_course_prompt_response_unsupported_intent import ResolveCoursePromptResponseUnsupportedIntent


class ResolveCoursePromptResponse_Course(UniversalBaseModel):
    kind: typing.Literal["course"] = "course"
    course_id: typing_extensions.Annotated[str, FieldMetadata(alias="courseId"), pydantic.Field(alias="courseId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ResolveCoursePromptResponse_Generation(UniversalBaseModel):
    kind: typing.Literal["generation"] = "generation"
    course_prompt_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="coursePromptId"), pydantic.Field(alias="coursePromptId")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ResolveCoursePromptResponse_Exam(UniversalBaseModel):
    kind: typing.Literal["exam"] = "exam"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ResolveCoursePromptResponse_Language(UniversalBaseModel):
    kind: typing.Literal["language"] = "language"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ResolveCoursePromptResponse_Unsafe(UniversalBaseModel):
    kind: typing.Literal["unsafe"] = "unsafe"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ResolveCoursePromptResponse_Unsupported(UniversalBaseModel):
    kind: typing.Literal["unsupported"] = "unsupported"
    course_format: typing_extensions.Annotated[
        typing.Optional[ResolveCoursePromptResponseUnsupportedCourseFormat],
        FieldMetadata(alias="courseFormat"),
        pydantic.Field(alias="courseFormat"),
    ] = None
    intent: ResolveCoursePromptResponseUnsupportedIntent
    title: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ResolveCoursePromptResponse = typing_extensions.Annotated[
    typing.Union[
        ResolveCoursePromptResponse_Course,
        ResolveCoursePromptResponse_Generation,
        ResolveCoursePromptResponse_Exam,
        ResolveCoursePromptResponse_Language,
        ResolveCoursePromptResponse_Unsafe,
        ResolveCoursePromptResponse_Unsupported,
    ],
    pydantic.Field(discriminator="kind"),
]
