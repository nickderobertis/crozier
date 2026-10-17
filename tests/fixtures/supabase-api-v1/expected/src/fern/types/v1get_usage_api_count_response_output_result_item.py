

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1GetUsageApiCountResponseOutputResultItem(UniversalBaseModel):
    timestamp: dt.datetime
    total_auth_requests: float
    total_realtime_requests: float
    total_rest_requests: float
    total_storage_requests: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
