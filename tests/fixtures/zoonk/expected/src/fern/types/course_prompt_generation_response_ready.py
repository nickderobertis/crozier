

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .course_prompt_generation_response_ready_target import CoursePromptGenerationResponseReadyTarget


class CoursePromptGenerationResponseReady(UniversalBaseModel):
    target: CoursePromptGenerationResponseReadyTarget

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
