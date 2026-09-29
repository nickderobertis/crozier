

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .course_edition_response_generation_generation_status import CourseEditionResponseGenerationGenerationStatus
from .course_edition_response_unsupported_reason import CourseEditionResponseUnsupportedReason


class CourseEditionResponse_Course(UniversalBaseModel):
    kind: typing.Literal["course"] = "course"
    course_id: typing_extensions.Annotated[str, FieldMetadata(alias="courseId"), pydantic.Field(alias="courseId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CourseEditionResponse_Generation(UniversalBaseModel):
    kind: typing.Literal["generation"] = "generation"
    course_prompt_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="coursePromptId"), pydantic.Field(alias="coursePromptId")
    ]
    generation_status: typing_extensions.Annotated[
        CourseEditionResponseGenerationGenerationStatus,
        FieldMetadata(alias="generationStatus"),
        pydantic.Field(alias="generationStatus"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CourseEditionResponse_Missing(UniversalBaseModel):
    kind: typing.Literal["missing"] = "missing"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CourseEditionResponse_Unsupported(UniversalBaseModel):
    kind: typing.Literal["unsupported"] = "unsupported"
    reason: CourseEditionResponseUnsupportedReason

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


CourseEditionResponse = typing_extensions.Annotated[
    typing.Union[
        CourseEditionResponse_Course,
        CourseEditionResponse_Generation,
        CourseEditionResponse_Missing,
        CourseEditionResponse_Unsupported,
    ],
    pydantic.Field(discriminator="kind"),
]
