

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_response import BaseResponse
from .report_response_jobs_item import ReportResponseJobsItem


class ReportResponse(BaseResponse):
    jobs: typing.Optional[typing.List[ReportResponseJobsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
