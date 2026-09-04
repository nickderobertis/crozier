

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_health_all_response_checks import GetHealthAllResponseChecks


class GetHealthAllResponse(UniversalBaseModel):
    status: typing.Optional[str] = None
    uptime: typing.Optional[float] = None
    timestamp: typing.Optional[dt.datetime] = None
    checks: typing.Optional[GetHealthAllResponseChecks] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
