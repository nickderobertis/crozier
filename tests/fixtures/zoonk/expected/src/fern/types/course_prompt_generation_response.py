

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .course_prompt_generation_response_pending_completion_kind import (
    CoursePromptGenerationResponsePendingCompletionKind,
)
from .course_prompt_generation_response_pending_course_format import CoursePromptGenerationResponsePendingCourseFormat
from .course_prompt_generation_response_pending_generation_status import (
    CoursePromptGenerationResponsePendingGenerationStatus,
)
from .course_prompt_generation_response_ready_target import CoursePromptGenerationResponseReadyTarget


class CoursePromptGenerationResponse_Pending(UniversalBaseModel):
    status: typing.Literal["pending"] = "pending"
    completion_kind: typing_extensions.Annotated[
        CoursePromptGenerationResponsePendingCompletionKind,
        FieldMetadata(alias="completionKind"),
        pydantic.Field(alias="completionKind"),
    ]
    course_format: typing_extensions.Annotated[
        CoursePromptGenerationResponsePendingCourseFormat,
        FieldMetadata(alias="courseFormat"),
        pydantic.Field(alias="courseFormat"),
    ]
    course_prompt_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="coursePromptId"), pydantic.Field(alias="coursePromptId")
    ]
    generation_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="generationId"), pydantic.Field(alias="generationId")
    ] = None
    generation_status: typing_extensions.Annotated[
        CoursePromptGenerationResponsePendingGenerationStatus,
        FieldMetadata(alias="generationStatus"),
        pydantic.Field(alias="generationStatus"),
    ]
    title: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CoursePromptGenerationResponse_Ready(UniversalBaseModel):
    status: typing.Literal["ready"] = "ready"
    target: CoursePromptGenerationResponseReadyTarget

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


CoursePromptGenerationResponse = typing_extensions.Annotated[
    typing.Union[CoursePromptGenerationResponse_Pending, CoursePromptGenerationResponse_Ready],
    pydantic.Field(discriminator="status"),
]
