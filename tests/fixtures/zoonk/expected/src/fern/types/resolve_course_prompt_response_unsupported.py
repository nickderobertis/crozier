

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .resolve_course_prompt_response_unsupported_course_format import ResolveCoursePromptResponseUnsupportedCourseFormat
from .resolve_course_prompt_response_unsupported_intent import ResolveCoursePromptResponseUnsupportedIntent


class ResolveCoursePromptResponseUnsupported(UniversalBaseModel):
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
