

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v2ground_list_jobs_response_jobs_item import V2GroundListJobsResponseJobsItem


class V2GroundListJobsResponse(UniversalBaseModel):
    jobs: typing.Optional[typing.List[V2GroundListJobsResponseJobsItem]] = None
    page: typing.Optional[int] = None
    page_size: typing.Optional[int] = None
    has_more: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
