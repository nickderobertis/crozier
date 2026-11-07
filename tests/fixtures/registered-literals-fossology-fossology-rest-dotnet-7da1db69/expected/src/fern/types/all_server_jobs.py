

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .all_server_jobs_data_item import AllServerJobsDataItem
from .all_server_jobs_scheduler import AllServerJobsScheduler


class AllServerJobs(UniversalBaseModel):
    data: typing.Optional[typing.List[AllServerJobsDataItem]] = pydantic.Field(default=None)
    """
    List of agents
    """

    scheduler: typing.Optional[AllServerJobsScheduler] = pydantic.Field(default=None)
    """
    Current scheduler status
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
