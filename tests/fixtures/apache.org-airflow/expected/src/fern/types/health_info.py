

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .metadatabase_status import MetadatabaseStatus
from .scheduler_status import SchedulerStatus


class HealthInfo(UniversalBaseModel):
    """
    Instance status information.
    """

    metadatabase: typing.Optional[MetadatabaseStatus] = None
    scheduler: typing.Optional[SchedulerStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
