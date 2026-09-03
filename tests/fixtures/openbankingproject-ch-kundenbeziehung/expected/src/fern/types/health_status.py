

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .health_status_services import HealthStatusServices
from .health_status_status import HealthStatusStatus


class HealthStatus(UniversalBaseModel):
    status: typing.Optional[HealthStatusStatus] = None
    timestamp: typing.Optional[dt.datetime] = None
    version: typing.Optional[str] = None
    services: typing.Optional[HealthStatusServices] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
