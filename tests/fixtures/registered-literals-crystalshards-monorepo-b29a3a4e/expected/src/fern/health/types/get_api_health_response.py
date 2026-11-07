

import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_api_health_response_services import GetApiHealthResponseServices


class GetApiHealthResponse(UniversalBaseModel):
    status: typing.Optional[str] = None
    timestamp: typing.Optional[dt.datetime] = None
    services: typing.Optional[GetApiHealthResponseServices] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
