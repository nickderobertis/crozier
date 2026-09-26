

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1ProjectUsersItem(UniversalBaseModel):
    user_id: int
    hour_rate: float
    hour_rate_in_cents: float
    updated_at: dt.datetime
    created_at: dt.datetime
    deleted: bool
    internal_hour_rate: float
    internal_hour_rate_in_cents: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
