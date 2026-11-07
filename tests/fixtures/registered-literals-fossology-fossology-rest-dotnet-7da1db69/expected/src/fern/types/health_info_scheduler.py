

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .health_info_scheduler_status import HealthInfoSchedulerStatus


class HealthInfoScheduler(UniversalBaseModel):
    """
    Scheduler information
    """

    status: typing.Optional[HealthInfoSchedulerStatus] = pydantic.Field(default=None)
    """
    Health status of scheduler
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
