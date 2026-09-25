

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1UserCapacity(UniversalBaseModel):
    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Capacity ID. Null for default capacity
    """

    weekly_capacity: float = pydantic.Field()
    """
    Specifies the user's weekly hour capacity. The default is account's weekly capacity. Can only have a decimal place of .5 (e.g. 3.5 hours)
    """

    daily_capacity: float = pydantic.Field()
    """
    Specifies the user's daily hour capacity
    """

    weekdays: typing.Optional[str] = pydantic.Field(default=None)
    """
    Legacy weekday format. Example: *'MO,TU,WE,TH,FR'*
    """

    work_days: str = pydantic.Field()
    """
    Comma-separated working days. Example: *'MON,TUE,WED,THU,FRI'*
    """

    total_working_days: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total working days in the capacity period. Null for open-ended capacities
    """

    weekly_working_days: int = pydantic.Field()
    """
    Specifies the number of user's weekly working days
    """

    current: bool = pydantic.Field()
    """
    True if this is the active capacity (no end date)
    """

    start_date: dt.date = pydantic.Field()
    """
    ISO8601 start date
    """

    end_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    ISO8601 end date. Null for open-ended capacities
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
