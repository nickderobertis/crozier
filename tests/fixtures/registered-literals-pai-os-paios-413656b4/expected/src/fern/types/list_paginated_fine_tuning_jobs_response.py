

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .fine_tuning_job import FineTuningJob
from .list_paginated_fine_tuning_jobs_response_object import ListPaginatedFineTuningJobsResponseObject


class ListPaginatedFineTuningJobsResponse(UniversalBaseModel):
    data: typing.List[FineTuningJob]
    has_more: bool
    object: ListPaginatedFineTuningJobsResponseObject

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
