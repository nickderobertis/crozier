

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .course_continuation import CourseContinuation


class CourseContinuationListResponse(UniversalBaseModel):
    data: typing.List[CourseContinuation] = pydantic.Field()
    """
    Current continuation targets, ordered by recent learning activity
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
