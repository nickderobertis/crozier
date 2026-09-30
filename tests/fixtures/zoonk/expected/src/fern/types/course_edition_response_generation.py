

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .course_edition_response_generation_generation_status import CourseEditionResponseGenerationGenerationStatus


class CourseEditionResponseGeneration(UniversalBaseModel):
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
