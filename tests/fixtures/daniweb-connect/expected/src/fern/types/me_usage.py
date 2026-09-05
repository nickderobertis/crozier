

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MeUsage(UniversalBaseModel):
    available_status: typing.Optional[bool] = None
    joined_timestamp: typing.Optional[dt.datetime] = None
    last_activity_timestamp: typing.Optional[dt.datetime] = None
    online_status: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
