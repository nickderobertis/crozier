

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .parse_list_jobs_response_jobs_item import ParseListJobsResponseJobsItem


class ParseListJobsResponse(UniversalBaseModel):
    jobs: typing.Optional[typing.List[ParseListJobsResponseJobsItem]] = pydantic.Field(default=None)
    """
    The caller's parse jobs for this page, newest first.
    """

    page: typing.Optional[int] = pydantic.Field(default=None)
    """
    The 0-indexed page number.
    """

    page_size: typing.Optional[int] = pydantic.Field(default=None)
    """
    Items per page.
    """

    has_more: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether more jobs exist beyond this page; request the next ``page`` to fetch them.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
