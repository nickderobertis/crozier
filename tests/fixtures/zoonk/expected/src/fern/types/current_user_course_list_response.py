

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .current_user_course import CurrentUserCourse
from .pagination import Pagination


class CurrentUserCourseListResponse(UniversalBaseModel):
    data: typing.List[CurrentUserCourse]
    pagination: Pagination

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
