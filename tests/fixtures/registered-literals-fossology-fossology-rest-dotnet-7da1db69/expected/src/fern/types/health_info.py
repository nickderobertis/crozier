

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .health_info_db import HealthInfoDb
from .health_info_scheduler import HealthInfoScheduler
from .health_info_status import HealthInfoStatus


class HealthInfo(UniversalBaseModel):
    """
    Health status of server
    """

    status: typing.Optional[HealthInfoStatus] = pydantic.Field(default=None)
    """
    Status of service
    """

    scheduler: typing.Optional[HealthInfoScheduler] = pydantic.Field(default=None)
    """
    Scheduler information
    """

    db: typing.Optional[HealthInfoDb] = pydantic.Field(default=None)
    """
    DB connection status
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
