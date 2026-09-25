

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1UsersCreateUserCapacity(UniversalBaseModel):
    id: typing.Optional[int] = None
    weekly_capacity: float
    daily_capacity: float
    weekdays: typing.Optional[str] = None
    work_days: str
    total_working_days: typing.Optional[int] = None
    weekly_working_days: int
    current: bool
    start_date: dt.date
    end_date: typing.Optional[dt.date] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
