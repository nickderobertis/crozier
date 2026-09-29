

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .course_edition_response_unsupported_reason import CourseEditionResponseUnsupportedReason


class CourseEditionResponseUnsupported(UniversalBaseModel):
    reason: CourseEditionResponseUnsupportedReason

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
