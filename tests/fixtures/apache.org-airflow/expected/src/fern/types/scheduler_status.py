

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .health_status import HealthStatus


class SchedulerStatus(UniversalBaseModel):
    """
    The status and the latest scheduler heartbeat.
    """

    latest_scheduler_heartbeat: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time the scheduler last do a heartbeat.
    """

    status: typing.Optional[HealthStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
